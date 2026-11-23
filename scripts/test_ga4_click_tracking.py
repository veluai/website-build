"""Offline checks for the prepared GA4 click-event snippet (70.50)."""

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SNIPPET = ROOT / "70-implementation" / "70.50-ga4-cta-click-tracking.html"


class Ga4ClickTrackingSnippetTest(unittest.TestCase):
    def setUp(self):
        self.source = SNIPPET.read_text(encoding="utf-8")
        scripts = re.findall(r"<script>(.*?)</script>", self.source, re.S)
        self.assertEqual(len(scripts), 1, "expected exactly one script block")
        self.script = scripts[0]

    def test_sends_to_both_collecting_properties(self):
        match = re.search(r"var SEND_TO = \[([^\]]*)\];", self.script)
        self.assertIsNotNone(match)
        ids = re.findall(r"'(G-[A-Z0-9]+)'", match.group(1))
        self.assertEqual(ids, ["G-9BB7KPXPCQ", "G-7LGS60FFST"])

    def test_event_names(self):
        names = set(re.findall(r"gtag\('event', '([a-z_]+)'", self.script))
        self.assertEqual(
            names, {"book_call_click", "service_link_click", "about_link_click"}
        )

    def test_does_not_load_or_configure_tags(self):
        self.assertIsNone(re.search(r"gtag\(\s*'config'\s*,", self.script))
        self.assertNotIn("googletagmanager.com", self.script)
        self.assertNotIn("fbq(", self.script)

    def test_reads_no_form_or_personal_data(self):
        for token in (".value", "FormData", "mailto:", "tel:", "cookie",
                      "localStorage", "url.search", "url.hash"):
            self.assertNotIn(token, self.script, token)


if __name__ == "__main__":
    unittest.main()
