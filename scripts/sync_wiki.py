"""Build the GitHub Wiki from repository Markdown using only Python's standard library."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit

MANIFEST = ".wiki-sync-manifest.json"
LINK = re.compile(r"(?P<image>!?)\[(?P<label>[^\]\n]*)\]\((?P<target>[^)\n]+)\)")
OVERRIDES = {
    "README.md": "Proposal",
    "CONTRIBUTING.md": "Contributing",
    "CHANGELOG.md": "Change-History",
    "docs/README.md": "Documentation-Index",
    "assets/README.md": "Asset-Notes",
}
RESERVED = {"home", "topic-index", "_sidebar", "_footer"}


def prose_chunks(text: str):
    """Yield fenced code unchanged so examples are never parsed as document links."""
    fence = None
    chunks = []
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match and fence is None:
            if chunks:
                yield True, "".join(chunks)
                chunks = []
            fence = match.group(1)
        chunks.append(line)
        if match and fence and len(chunks) > 1:
            token = match.group(1)
            if token[0] == fence[0] and len(token) >= len(fence):
                yield False, "".join(chunks)
                chunks = []
                fence = None
    if chunks:
        if fence is not None:
            raise ValueError("Unclosed Markdown code fence")
        yield True, "".join(chunks)


def slugify(text: str) -> str:
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def headings(text: str):
    counts = {}
    result = []
    for is_prose, chunk in prose_chunks(text):
        if not is_prose:
            continue
        for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*#*\s*$", chunk, re.M):
            level, title = len(match.group(1)), match.group(2)
            base = slugify(title)
            slug = base
            number = 0
            while slug in counts:
                number += 1
                slug = f"{base}-{number}"
            counts[slug] = True
            result.append((level, title, slug))
    return result


def read_navigation(root: Path):
    path = root / "wiki/navigation.json"
    if not path.exists():
        return []
    groups = json.loads(path.read_text(encoding="utf-8")).get("groups", [])
    if not isinstance(groups, list):
        raise ValueError("Wiki navigation groups must be a list")
    seen = set()
    group_names = set()
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("title"), str) or not group["title"].strip():
            raise ValueError("Every navigation group needs a title")
        if not isinstance(group.get("items"), list):
            raise ValueError("Every navigation group needs an items list")
        group_slug = slugify(group["title"])
        if not group_slug or group_slug in group_names:
            raise ValueError("Navigation groups need distinct anchor names")
        group_names.add(group_slug)
        for item in group["items"]:
            if not isinstance(item, dict) or not all(isinstance(item.get(key), str) and item[key].strip()
                                                     for key in ("source", "page", "label", "description")):
                raise ValueError("Every navigation topic needs source, page, label and description")
            source = (root / item["source"]).resolve()
            if not source.is_relative_to(root.resolve()) or source in seen:
                raise ValueError(f"Duplicate or outside navigation source: {item['source']}")
            if not source.is_file() or source.suffix != ".md":
                raise ValueError(f"Missing Markdown navigation source: {item['source']}")
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*", item["page"]):
                raise ValueError(f"Invalid navigation page name: {item['page']}")
            seen.add(source)
    return groups


def discover(root: Path, custom_overrides=None):
    sources = set(root.glob("*.md"))
    for directory in ("docs", "assets"):
        sources.update((root / directory).rglob("*.md"))
    mapping = {}
    used = set(RESERVED)
    for source in sorted(sources):
        relative = source.relative_to(root).as_posix()
        page = (custom_overrides or {}).get(relative, OVERRIDES.get(relative))
        if page is None:
            parts = list(source.relative_to(root).with_suffix("").parts)
            if parts[0] == "docs":
                parts = parts[1:]
            name = "-".join(re.sub(r"^\d+-", "", part) for part in parts)
            page = "-".join(word[:1].upper() + word[1:] for word in name.split("-"))
        if page.casefold() in used:
            raise ValueError(f"Duplicate or reserved wiki page name: {relative} -> {page}")
        used.add(page.casefold())
        mapping[source.resolve()] = page
    return mapping


class WikiBuilder:
    def __init__(self, root: Path, repository: str, revision: str, branch: str = "main"):
        self.root = root.resolve()
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository):
            raise ValueError("Repository must use owner/name format")
        if not re.fullmatch(r"[A-Za-z0-9._/-]+", revision):
            raise ValueError("Invalid source revision")
        self.repository = repository
        self.revision = revision
        self.branch = branch
        self.repo_url = f"https://github.com/{repository}"
        self.wiki_url = self.repo_url + "/wiki"
        self.navigation = read_navigation(self.root)
        overrides = {(self.root / item["source"]).resolve().relative_to(self.root).as_posix(): item["page"]
                     for group in self.navigation for item in group["items"]}
        self.mapping = discover(self.root, overrides)
        if any((self.root / path).resolve() not in self.mapping for path in overrides):
            raise ValueError("A configured navigation source is outside the generated document collection")
        self.texts = {path: path.read_text(encoding="utf-8") for path in self.mapping}
        self.sections = {path: headings(text) for path, text in self.texts.items()}
        self.link_count = 0

    def page_url(self, page: str) -> str:
        return f"{self.wiki_url}/{quote(page)}"

    def resolve_link(self, source: Path, target: str, image: bool = False) -> str:
        # Optional Markdown titles are preserved, including angle-delimited paths.
        match = re.fullmatch(r'(<[^>]+>|\S+?)(\s+"[^"]*")?', target)
        if not match:
            raise ValueError(f"Unsupported link target in {source.name}: {target}")
        raw, title = match.group(1).strip("<>"), match.group(2) or ""
        parsed = urlsplit(raw)
        if parsed.scheme or raw.startswith("//"):
            return target
        self.link_count += 1
        destination = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
        if not destination.is_relative_to(self.root):
            raise ValueError(f"Link escapes repository: {source.name}: {raw}")
        if not destination.exists():
            raise ValueError(f"Missing link: {source.relative_to(self.root)} -> {raw}")
        fragment = unquote(parsed.fragment)
        if fragment and destination in self.sections:
            if fragment not in {row[2] for row in self.sections[destination]}:
                raise ValueError(f"Missing heading: {source.relative_to(self.root)} -> {raw}")
        suffix = ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")
        if destination in self.mapping and not image:
            return self.page_url(self.mapping[destination]) + suffix + title
        relative = quote(destination.relative_to(self.root).as_posix(), safe="/")
        if image:
            if not destination.is_file():
                raise ValueError(f"Image is not a file: {raw}")
            url = f"https://raw.githubusercontent.com/{self.repository}/{self.revision}/{relative}"
        else:
            route = "tree" if destination.is_dir() else "blob"
            url = f"{self.repo_url}/{route}/{self.revision}/{relative}"
        return url + suffix + title

    def convert(self, source: Path) -> str:
        result = []
        for is_prose, chunk in prose_chunks(self.texts[source]):
            if not is_prose:
                result.append(chunk)
                continue
            # Inline code examples must remain literal, too.
            parts = re.split(r"(`+[^`\n]*`+)", chunk)
            for index in range(0, len(parts), 2):
                def replace(match):
                    target = self.resolve_link(source, match.group("target"), bool(match.group("image")))
                    return f'{match.group("image")}[{match.group("label")}]({target})'
                parts[index] = LINK.sub(replace, parts[index])
            result.append("".join(parts))
        return "".join(result)

    def title(self, source: Path):
        return next((title for level, title, _ in self.sections[source] if level == 1), self.mapping[source])

    def navigation_groups(self):
        groups = []
        listed = set()
        for group in self.navigation:
            entries = []
            for item in group["items"]:
                source = (self.root / item["source"]).resolve()
                listed.add(source)
                entries.append((source, item["label"], item["description"]))
            groups.append((group["title"], bool(group.get("collapsed")), entries))
        remaining = [p for p in self.mapping if p not in listed]
        if remaining:
            groups.append(("Additional Topics" if groups else "Complete Documentation", False,
                           [(p, self.title(p), "Read the complete topic.") for p in remaining]))
        return groups

    def build(self):
        output = {}
        groups = self.navigation_groups()
        topic_groups = {source: title for title, _, entries in groups for source, _, _ in entries}
        for source, page in self.mapping.items():
            text = self.convert(source)
            relative = source.relative_to(self.root).as_posix()
            header = (
                f"> Source: [{relative}]({self.repo_url}/blob/{self.revision}/{quote(relative, safe='/')})"
                f" · [Edit the concept]({self.repo_url}/edit/{self.branch}/{quote(relative, safe='/')})\n\n"
            )
            contents = [f'{"  " * (level - 2)}- [{title}](#{slug})'
                        for level, title, slug in self.sections[source] if level in (2, 3)]
            toc = ("<details>\n<summary>On this page</summary>\n\n" + "\n".join(contents) + "\n\n</details>\n\n") if contents else ""
            group = topic_groups[source]
            breadcrumb = f"[Wiki home]({self.page_url('Home')}) / [{group}]({self.page_url('Home')}#{slugify(group)})\n\n"
            source_note = "\n\n<details>\n<summary>Source and editing</summary>\n\n" + header.rstrip() + "\n\n</details>\n"
            output[page + ".md"] = breadcrumb + toc + text.rstrip() + source_note

        proposal = self.page_url("Proposal")
        output["Home.md"] = (
            "# WoW: Forever — Complete Design Wiki\n\n"
            "A lasting level-60 world built around cooperation, clear rules and earned accomplishments. "
            "This independent community proposal separates permanent preparation, scoped raid progression "
            "and prestige without an endless permanent gear ladder.\n\n"
            f"**[Read the full proposal and author background]({proposal})** · "
            f"[Browse every topic]({self.page_url('Topic-Index')}) · "
            f"[Repository]({self.repo_url})\n\n"
            "## Find your topic\n\n"
            "Choose an activity or character topic below. Each page contains its rules, rewards, risks "
            "and links to related systems. The same categories are available in the sidebar.\n\n"
        )
        topics = ["# Detailed Topic Index\n", "Browse by subject, then jump directly to a section.\n"]
        sidebar = (
            f"**[Wiki home]({self.page_url('Home')})**\n\n"
            f"- [Complete proposal]({proposal})\n- [All topics]({self.page_url('Topic-Index')})\n"
        )
        for title, collapsed, entries in groups:
            output["Home.md"] += f"## {title}\n\n"
            if collapsed:
                output["Home.md"] += "<details>\n<summary>Show guides and technical documentation</summary>\n\n"
                sidebar += f"\n<details>\n<summary>{title}</summary>\n\n"
            else:
                sidebar += f"\n**{title}**\n\n"
            output["Home.md"] += "| Topic | What you will find |\n| --- | --- |\n"
            topics.append(f"## {title}\n")
            for source, label, description in entries:
                url = self.page_url(self.mapping[source])
                output["Home.md"] += f"| [{label}]({url}) | {description} |\n"
                sidebar += f"- [{label}]({url})\n"
                topics.append(f"### [{label}]({url})\n")
                topics.extend(f'{"  " * (level - 2)}- [{section}]({url}#{slug})'
                              for level, section, slug in self.sections[source] if level in (2, 3))
                topics.append("")
            if collapsed:
                output["Home.md"] += "\n</details>\n"
                sidebar += "\n</details>\n"
            output["Home.md"] += "\n"
        output["Home.md"] += (
            "## Updating the Concept\n\nEdit the repository Markdown. Validated changes on `main` automatically "
            "publish here, including topic navigation. Proposals under review stay separate from selected rules.\n"
        )
        output["Topic-Index.md"] = "\n".join(topics).rstrip() + "\n"
        output["_Sidebar.md"] = sidebar
        output["_Footer.md"] = (
            f"Generated from [source revision `{self.revision[:12]}`]({self.repo_url}/commit/{self.revision}). "
            f"Edit the [repository]({self.repo_url}) to update the concept. Independent community design proposal.\n"
        )
        return output


def write_pages(output: Path, pages: dict[str, str], revision: str):
    output.mkdir(parents=True, exist_ok=True)
    manifest = output / MANIFEST
    old = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else {}
    for name in old.get("pages", []):
        if not isinstance(name, str) or Path(name).name != name or not name.endswith(".md"):
            raise ValueError("Unsafe page entry in wiki manifest")
    for name in old.get("pages", []):
        if name not in pages:
            (output / name).unlink(missing_ok=True)
    for name, text in pages.items():
        (output / name).write_text(text, encoding="utf-8", newline="\n")
    manifest.write_text(json.dumps({"version": 1, "source_commit": revision, "pages": sorted(pages)}, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "Finland6738/wow-forever-game-design"))
    parser.add_argument("--revision")
    args = parser.parse_args()
    revision = args.revision or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.root, text=True).strip()
    builder = WikiBuilder(args.root, args.repository, revision)
    pages = builder.build()
    if args.output:
        output = args.output.resolve()
        if any((output / name).resolve() in builder.mapping for name in pages):
            raise ValueError("Wiki output would overwrite a source document")
        write_pages(output, pages, revision)
    print(f"Validated {len(builder.mapping)} source documents and {builder.link_count} local references; built {len(pages)} wiki files.")


if __name__ == "__main__":
    main()
