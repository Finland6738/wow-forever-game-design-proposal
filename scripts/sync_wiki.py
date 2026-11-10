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


def discover(root: Path):
    sources = set(root.glob("*.md"))
    for directory in ("docs", "assets"):
        sources.update((root / directory).rglob("*.md"))
    mapping = {}
    used = set(RESERVED)
    for source in sorted(sources):
        relative = source.relative_to(root).as_posix()
        page = OVERRIDES.get(relative)
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
        self.mapping = discover(self.root)
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

    def build(self):
        output = {}
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
            output[page + ".md"] = header + toc + text.rstrip() + "\n"

        docs = sorted((p for p in self.mapping if p.is_relative_to(self.root / "docs")),
                      key=lambda p: p.relative_to(self.root).as_posix())
        entries = [f"- [{self.title(p)}]({self.page_url(self.mapping[p])})" for p in docs]
        proposal = self.page_url("Proposal")
        output["Home.md"] = (
            "# WoW: Forever — Complete Design Wiki\n\n"
            "A lasting level-60 world built around cooperation, clear rules and earned accomplishments. "
            "This independent community proposal separates permanent preparation, scoped raid progression "
            "and prestige without an endless permanent gear ladder.\n\n"
            f"**[Read the full proposal and author background]({proposal})** · "
            f"[Browse every topic]({self.page_url('Topic-Index')}) · "
            f"[Repository]({self.repo_url})\n\n"
            "## Reading paths\n\n"
            "- **Players:** start with the proposal, social principles and player journeys.\n"
            "- **System designers:** read progression, the technical framework, reward policies and the decision register.\n"
            "- **Contributors:** use the documentation index, open decisions and wiki-maintenance guide.\n\n"
            "## Complete documentation\n\n" + "\n".join(entries) + "\n\n"
            "## Updating the concept\n\n"
            "Edit the repository Markdown. Validated changes on `main` automatically publish here. "
            "Source links identify the exact revision; numerical prototypes and open decisions remain labeled.\n"
        )
        topics = ["# Detailed topic index\n", "Every section below links to its complete design page.\n"]
        for source in docs:
            url = self.page_url(self.mapping[source])
            topics.append(f"## [{self.title(source)}]({url})\n")
            topics.extend(f'{"  " * (level - 2)}- [{title}]({url}#{slug})'
                          for level, title, slug in self.sections[source] if level in (2, 3))
            topics.append("")
        output["Topic-Index.md"] = "\n".join(topics).rstrip() + "\n"
        output["_Sidebar.md"] = (
            f"**[Wiki home]({self.page_url('Home')})**\n\n"
            f"- [Complete proposal]({proposal})\n- [All topics]({self.page_url('Topic-Index')})\n"
            + "\n".join(entries) + "\n\n"
            + f"[Contributing]({self.page_url('Contributing')}) · [Change history]({self.page_url('Change-History')})\n"
        )
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
