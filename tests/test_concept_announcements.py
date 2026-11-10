import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("announcements", Path(__file__).resolve().parents[1] / "scripts/announce_concept_changes.py")
announcement = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(announcement)


class FakeGitHub:
    def __init__(self):
        self.posts = []
        self.fail_after_create = False

    def repository(self, repository, category):
        if category != "announcements":
            raise ValueError("Missing category")
        return "R_test", "C_test", "owner"

    def discussions(self, repository, category):
        return iter(self.posts)

    def create(self, repository_id, category_id, title, body):
        url = f"https://github.com/owner/repo/discussions/{len(self.posts) + 1}"
        self.posts.append({"body": body, "url": url, "title": title,
                           "author": {"login": "github-actions[bot]"}})
        if self.fail_after_create:
            raise RuntimeError("Connection lost after GitHub accepted the post")
        return url


class AnnouncementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.command("init", "-q")
        self.command("config", "user.name", "Test")
        self.command("config", "user.email", "test@example.com")
        self.write("README.md", "# Proposal\n")
        self.write("CHANGELOG.md", "# History\n\n## 0.1\n\n- Original concept.\n")
        self.base = self.commit("Initial proposal")
        self.config = {"category": "announcements", "initial_base": self.base}
        self.github = FakeGitHub()

    def command(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, encoding="utf-8", stderr=subprocess.PIPE).strip()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def commit(self, subject):
        self.command("add", "--all")
        self.command("commit", "-qm", subject)
        return self.command("rev-parse", "HEAD")

    def publish(self, head):
        return announcement.publish(self.root, "owner/repo", head, self.config, self.github)

    def test_infrastructure_only_does_not_post(self):
        self.write("scripts/build.py", "print('test')\n")
        self.write("docs/14-wiki-maintenance.md", "# Publishing\n")
        self.write("CONTRIBUTING.md", "# Contributions\n")
        self.assertEqual(self.publish(self.commit("Improve publishing"))["status"], "no-concept-changes")
        self.assertEqual(self.github.posts, [])

    def test_new_notes_are_used_without_reposting_old_release_notes(self):
        self.write("docs/identity/classes/artificer.md", "# Artificer\nSeparate device health.\n")
        self.write("CHANGELOG.md", "# History\n\n## 0.2\n\n- Independent construct health.\n\n## 0.1\n\n- Original concept.\n")
        head = self.commit("Develop Artificer")
        result = self.publish(head)
        self.assertIn("Independent construct health", result["body"])
        self.assertNotIn("Original concept", result["body"])
        self.assertIn(f"/blob/{head}/docs/identity/classes/artificer.md", result["body"])
        self.assertEqual(result["title"], "Proposal update — 0.2")

    def test_retry_and_accepted_but_timed_out_post_do_not_duplicate(self):
        self.write("README.md", "# Changed proposal\n")
        head = self.commit("Explain group play")
        self.github.fail_after_create = True
        with self.assertRaises(RuntimeError):
            self.publish(head)
        self.github.fail_after_create = False
        self.assertEqual(self.publish(head)["status"], "already-published")
        self.assertEqual(len(self.github.posts), 1)

    def test_unannounced_change_is_caught_after_an_infrastructure_push(self):
        self.write("docs/raids.md", "# Raids\nFirst version\n")
        first = self.commit("Define raids")
        self.publish(first)
        self.write("docs/races.md", "# Races\nNew origin\n")
        self.commit("Define neutral origins")  # Simulate a failed publication.
        self.write("scripts/check.py", "# infrastructure\n")
        result = self.publish(self.commit("Improve checks"))
        self.assertEqual(result["before"], first)
        self.assertIn("docs/races.md", result["body"])
        self.assertNotIn("docs/raids.md", result["body"])

    def test_old_workflow_rerun_is_superseded(self):
        self.write("README.md", "# Changed\n")
        first = self.commit("First change")
        self.write("README.md", "# Changed again\n")
        second = self.commit("Second change")
        self.publish(second)
        self.assertEqual(self.publish(first)["status"], "superseded")
        self.assertEqual(len(self.github.posts), 1)

    def test_deleted_document_links_to_its_last_range_baseline(self):
        self.write("docs/old.md", "# Old\n")
        first = self.commit("Add old concept")
        self.publish(first)
        (self.root / "docs/old.md").unlink()
        result = self.publish(self.commit("Retire old concept"))
        self.assertIn(f"/blob/{first}/docs/old.md", result["body"])
        self.assertIn("— removed", result["body"])

    def test_missing_changelog_uses_literal_commit_subjects_without_mentions(self):
        self.write("README.md", "# Updated\n")
        result = self.publish(self.commit("Explain @example's build `choice`"))
        self.assertIn("Recorded commit: Explain ＠example's build `choice`", result["body"])

    def test_wrong_category_stops_before_creation(self):
        self.config["category"] = "missing"
        with self.assertRaises(ValueError):
            self.publish(self.base)
        self.assertEqual(self.github.posts, [])

    def test_untrusted_author_marker_does_not_skip_publication(self):
        self.write("README.md", "# Updated\n")
        head = self.commit("Explain group composition")
        self.github.posts.append({"body": announcement.marker("R_test", head), "url": "ignored",
                                  "author": {"login": "someone-else"}})
        self.assertEqual(self.publish(head)["status"], "published")

    def test_api_graphql_errors_are_not_treated_as_a_success(self):
        fake = subprocess.CompletedProcess([], 0, '{"errors":[{"message":"Denied"}]}', '')
        with patch.object(announcement.subprocess, "run", return_value=fake):
            with self.assertRaisesRegex(RuntimeError, "Denied"):
                announcement.GitHub().query("query{}", {})

    def test_github_client_paginates_category_discussions(self):
        client = announcement.GitHub()
        responses = [{"repository": {"discussions": {"nodes": [{"body": "first"}],
                     "pageInfo": {"hasNextPage": True, "endCursor": "next"}}}},
                     {"repository": {"discussions": {"nodes": [{"body": "second"}],
                     "pageInfo": {"hasNextPage": False, "endCursor": None}}}}]
        with patch.object(client, "query", side_effect=responses) as query:
            self.assertEqual(len(list(client.discussions("owner/repo", "C_test"))), 2)
            self.assertEqual(query.call_args.args[1]["cursor"], "next")


if __name__ == "__main__":
    unittest.main()
