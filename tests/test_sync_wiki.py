import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("sync_wiki", Path(__file__).resolve().parents[1] / "scripts/sync_wiki.py")
wiki = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wiki)


class WikiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        (self.root / "assets").mkdir()
        (self.root / "README.md").write_text("# Proposal\n", encoding="utf-8")

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target.resolve()

    def builder(self):
        return wiki.WikiBuilder(self.root, "owner/repo", "abc123")

    def test_document_anchor_image_and_external_links(self):
        self.put("assets/map.svg", "<svg/>")
        self.put("docs/01-raids.md", "# Raids\n\n## Entry rules\n")
        self.put("README.md", '# Proposal\n[Raids](docs/01-raids.md#entry-rules)\n![Map](assets/map.svg)\n[Site](https://example.com/a)\n')
        page = self.builder().build()["Proposal.md"]
        self.assertIn("https://github.com/owner/repo/wiki/Raids#entry-rules", page)
        self.assertIn("https://raw.githubusercontent.com/owner/repo/abc123/assets/map.svg", page)
        self.assertIn("[Site](https://example.com/a)", page)

    def test_nested_new_pages_and_duplicate_heading_anchors(self):
        self.put("docs/10-world/02-events.md", "# Events\n\n## Entry\n\n## Entry\n")
        self.put("README.md", "# Proposal\n[Events](docs/10-world/02-events.md#entry-1)\n")
        pages = self.builder().build()
        self.assertIn("World-Events.md", pages)
        self.assertIn("#entry-1", pages["Topic-Index.md"])
        self.assertIn("World-Events", pages["_Sidebar.md"])

    def test_code_examples_are_not_rewritten_or_validated(self):
        self.put("README.md", "# Proposal\n\n```md\n[Example](missing.md)\n```\n\n`[Literal](also-missing.md)`\n")
        page = self.builder().build()["Proposal.md"]
        self.assertIn("[Example](missing.md)", page)
        self.assertIn("`[Literal](also-missing.md)`", page)

    def test_missing_source_or_anchor_blocks_publication(self):
        for text in ("[Bad](gone.md)", "[Bad](#missing-heading)"):
            self.put("README.md", "# Proposal\n" + text)
            with self.assertRaises(ValueError):
                self.builder().build()

    def test_colliding_names_are_rejected(self):
        self.put("docs/01-world.md", "# World\n")
        self.put("docs/02-world.md", "# Another world\n")
        with self.assertRaises(ValueError):
            self.builder()

    def test_only_previously_managed_pages_are_removed(self):
        output = self.root / "output"
        wiki.write_pages(output, {"Home.md": "one", "Old.md": "old"}, "one")
        (output / "Handwritten.md").write_text("keep", encoding="utf-8")
        wiki.write_pages(output, {"Home.md": "two"}, "two")
        self.assertFalse((output / "Old.md").exists())
        self.assertEqual((output / "Handwritten.md").read_text(), "keep")
        self.assertEqual((output / "Home.md").read_text(), "two")

    def test_unsafe_manifest_and_outside_links_are_rejected(self):
        output = self.root / "output"
        output.mkdir()
        (output / wiki.MANIFEST).write_text(json.dumps({"pages": ["../outside.md"]}))
        with self.assertRaises(ValueError):
            wiki.write_pages(output, {"Home.md": "safe"}, "abc123")
        self.put("README.md", "# Proposal\n[Outside](../outside.md)")
        with self.assertRaises(ValueError):
            self.builder().build()

    def test_same_revision_produces_identical_output(self):
        self.assertEqual(self.builder().build(), self.builder().build())

    def test_unclosed_code_fence_blocks_publication(self):
        self.put("README.md", "# Proposal\n\n```text\nunfinished example\n")
        with self.assertRaises(ValueError):
            self.builder().build()


if __name__ == "__main__":
    unittest.main()
