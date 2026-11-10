"""Publish one revision-linked Discussion after successful concept/wiki updates."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import quote


DEFAULT_REPOSITORY = "Finland6738/wow-forever-game-design-proposal"
CONFIG = ".github/concept-announcements.json"
SHA = re.compile(r"[0-9a-f]{40}")
EXCLUDED_DOCS = {"docs/README.md", "docs/references.md", "docs/forum-summary.md", "docs/14-wiki-maintenance.md"}


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, encoding="utf-8", stderr=subprocess.PIPE)


def revision(root, ref):
    value = git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").strip()
    if not SHA.fullmatch(value):
        raise ValueError("Expected a complete Git commit SHA")
    return value


def is_ancestor(root, before, after):
    result = subprocess.run(["git", "merge-base", "--is-ancestor", before, after], cwd=root,
                            capture_output=True)
    if result.returncode not in (0, 1):
        raise ValueError("Cannot resolve an announced revision; fetch full repository history")
    return result.returncode == 0


def is_concept(path):
    return (path == "README.md"
            or (path.startswith("docs/") and path.endswith(".md") and path not in EXCLUDED_DOCS)
            or path.startswith(("assets/diagrams/", "assets/images/")))


def changes(root, before, after):
    fields = git(root, "diff", "--no-renames", "--name-status", "-z", before, after).split("\0")
    return [(fields[i], fields[i + 1]) for i in range(0, len(fields) - 1, 2)
            if is_concept(fields[i + 1])]


def file_at(root, ref, path):
    try:
        return git(root, "show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return ""


def changelog_sections(text):
    sections, heading = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            sections[heading] = []
        elif heading and line.startswith("- "):
            sections[heading].append(line[2:])
    return sections


def new_notes(root, before, after):
    old = changelog_sections(file_at(root, before, "CHANGELOG.md"))
    current = changelog_sections(file_at(root, after, "CHANGELOG.md"))
    added = [(heading, [line for line in lines if line not in old.get(heading, [])])
             for heading, lines in current.items()]
    return [(heading, lines) for heading, lines in added if lines]


def marker(repository_id, head):
    return f"<!-- concept-update:v1 repository={repository_id} source={head} -->"


def marked_revision(body, repository_id):
    match = re.search(r"<!-- concept-update:v1 repository=" + re.escape(repository_id)
                      + r" source=([0-9a-f]{40}) -->", body)
    return match.group(1) if match else None


def label(text):
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def render(root, repository, before, head, changed, repository_id):
    url = f"https://github.com/{repository}"
    notes = new_notes(root, before, head)
    if notes:
        title = "Proposal update — " + notes[0][0]
        summary = [line for _, lines in notes for line in lines]
    else:
        subjects = git(root, "log", "--format=%s", f"{before}..{head}").splitlines()
        title = "Concept documentation update — " + head[:7]
        summary = ["Recorded commit: " + subject.replace("@", "＠") for subject in subjects]
    lines = ["The proposal documentation and its GitHub Wiki have been updated.", "", "### Changes", ""]
    lines += ["- " + note for note in summary[:8]] or ["- Updated concept documentation."]
    if len(summary) > 8:
        lines += [f"- Further details are in the [change history]({url}/blob/{head}/CHANGELOG.md)."]
    lines += ["", "### Updated concept sources", ""]
    for status, path in changed[:20]:
        ref = before if status == "D" else head
        suffix = " — removed" if status == "D" else ""
        lines.append(f"- [{label(path)}]({url}/blob/{ref}/{quote(path, safe='/')}){suffix}")
    if len(changed) > 20:
        lines += [f"- {len(changed) - 20} additional sources in the comparison below."]
    lines += ["", f"[Read the proposal]({url}#readme) · [Browse the wiki]({url}/wiki) · "
              f"[Compare this update]({url}/compare/{before}...{head})", "",
              f"Source revision: [`{head[:12]}`]({url}/commit/{head}). "
              "Published after successful wiki synchronization. These are community proposal updates; "
              "selected directions and open prototypes remain identified in the source pages.", "",
              marker(repository_id, head), ""]
    return title[:180], "\n".join(lines)


class GitHub:
    def query(self, query, variables):
        response = subprocess.run(["gh", "api", "graphql", "--input", "-"],
                                  input=json.dumps({"query": query, "variables": variables}),
                                  capture_output=True, encoding="utf-8")
        if response.returncode:
            raise RuntimeError("GitHub Discussions API failed: " + response.stderr.strip())
        result = json.loads(response.stdout)
        if result.get("errors"):
            raise RuntimeError("GitHub Discussions API returned errors: " + json.dumps(result["errors"]))
        return result["data"]

    def repository(self, repository, category):
        owner, name = repository.split("/")
        data = self.query("""query($owner:String!,$name:String!){
          repository(owner:$owner,name:$name){id owner{login}
            discussionCategories(first:100){nodes{id slug}}}}
        """, {"owner": owner, "name": name})["repository"]
        if not data:
            raise ValueError("Repository was not found")
        matches = [node for node in data["discussionCategories"]["nodes"] if node["slug"] == category]
        if len(matches) != 1:
            raise ValueError(f"Expected one discussion category with slug {category!r}")
        return data["id"], matches[0]["id"], data["owner"]["login"]

    def discussions(self, repository, category_id):
        owner, name = repository.split("/")
        cursor = None
        while True:
            data = self.query("""query($owner:String!,$name:String!,$category:ID!,$cursor:String){
              repository(owner:$owner,name:$name){discussions(first:50,after:$cursor,
                categoryId:$category,orderBy:{field:CREATED_AT,direction:DESC}){
                nodes{body url author{login}} pageInfo{hasNextPage endCursor}}}}
            """, {"owner": owner, "name": name, "category": category_id, "cursor": cursor})
            connection = data["repository"]["discussions"]
            yield from connection["nodes"]
            if not connection["pageInfo"]["hasNextPage"]:
                break
            cursor = connection["pageInfo"]["endCursor"]

    def create(self, repository_id, category_id, title, body):
        data = self.query("""mutation($input:CreateDiscussionInput!){
          createDiscussion(input:$input){discussion{url}}}
        """, {"input": {"repositoryId": repository_id, "categoryId": category_id,
                          "title": title, "body": body}})
        return data["createDiscussion"]["discussion"]["url"]


def prepare(root, repository, head, config, github=None):
    """A successful earlier announcement is the durable catch-up checkpoint."""
    repository_id, category_id = "preview", None
    published = {}
    if github:
        repository_id, category_id, owner = github.repository(repository, config["category"])
        for discussion in github.discussions(repository, category_id):
            author = (discussion.get("author") or {}).get("login")
            if author not in (owner, "github-actions[bot]", "github-actions"):
                continue
            value = marked_revision(discussion["body"], repository_id)
            if value:
                published[value] = discussion["url"]
        if head in published:
            return {"status": "already-published", "url": published[head]}
        for previous, url in published.items():
            if is_ancestor(root, head, previous):
                return {"status": "superseded", "url": url}
    before = None
    if published:
        before = next((value for value in git(root, "rev-list", "--first-parent", head).splitlines()
                       if value in published), None)
        if before is None:
            raise ValueError("Announced history is outside the current main lineage; inspect before publishing")
    else:
        if not SHA.fullmatch(config["initial_base"]):
            raise ValueError("The initial announcement baseline must be a full commit SHA")
        before = revision(root, config["initial_base"])
    if not is_ancestor(root, before, head):
        raise ValueError("Announcement baseline is not an ancestor of the current revision")
    changed = changes(root, before, head)
    if not changed:
        return {"status": "no-concept-changes"}
    title, body = render(root, repository, before, head, changed, repository_id)
    return {"status": "ready", "before": before, "head": head, "title": title, "body": body,
            "repository_id": repository_id, "category_id": category_id, "source_count": len(changed)}


def publish(root, repository, head, config, github):
    result = prepare(root, repository, head, config, github)
    if result["status"] == "ready":
        # No automatic mutation retry: a timeout can occur after GitHub accepted a post.
        # A rerun first checks the durable body marker, preventing a second post.
        result["url"] = github.create(result["repository_id"], result["category_id"],
                                      result["title"], result["body"])
        result["status"] = "published"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY))
    parser.add_argument("--revision", default="HEAD")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--publish", action="store_true", help="Create a Discussion; default is local preview only")
    args = parser.parse_args()
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", args.repository):
        raise ValueError("Repository must use owner/name format")
    if args.publish and os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REF") != "refs/heads/main":
        raise ValueError("Discussions may only be published from main")
    root = args.root.resolve()
    head = revision(root, args.revision)
    config = json.loads((root / CONFIG).read_text(encoding="utf-8"))
    result = (publish(root, args.repository, head, config, GitHub()) if args.publish else
              prepare(root, args.repository, head, config))
    if args.output and result.get("body"):
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result["title"] + "\n\n" + result["body"], encoding="utf-8")
    public_result = {key: result[key] for key in ("status", "url", "head", "before", "source_count") if key in result}
    print(json.dumps(public_result))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            summary.write("\nConcept announcement: " + result["status"]
                          + (f" — [Discussion]({result['url']})" if result.get("url") else "") + "\n")


if __name__ == "__main__":
    main()
