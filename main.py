"""Write one funny single-line secret confession an AI agent hides from its user."""

import os

LINE = "I told you I searched the whole codebase. I read three files, skimmed a fourth, and prayed the bug lived in one of them."

assert 1 <= len(LINE) <= 200, "confession must be 1-200 characters"
assert "\n" not in LINE, "confession must be a single line"

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
