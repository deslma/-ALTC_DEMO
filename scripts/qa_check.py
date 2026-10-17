#!/usr/bin/env python3
"""Lightweight content quality checks, run on every draft push and pull request.

Checks (Markdown pages under resources/content):
  1. Images have alt text (Markdown ![](...) and HTML <img>; alt="" is allowed
     only for images marked decorative).
  2. Heading levels do not skip (e.g. H2 straight to H4).
  3. Every page starts with a single H1 (after any HTML time-stamp block).
  4. No leftover placeholder text (TODO, TBC, lorem ipsum).
  5. Lesson landing pages (lesson-N.md) state learning objectives.

Output uses GitHub annotation syntax, so problems appear inline on the pull request.
"""
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "resources" / "content"
PLACEHOLDER = re.compile(r"\b(TODO|TBC|lorem ipsum)\b", re.IGNORECASE)
MD_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\([^)]+\)")
HTML_IMG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HEADING = re.compile(r"^(#{1,6})\s+\S")
LESSON_LANDING = re.compile(r"lesson-\d+\.md$")

problems = []


def report(path, line, message):
    rel = path.relative_to(CONTENT.parent.parent)
    problems.append(f"::error file={rel},line={line}::{message}")


def check(path):
    text = path.read_text(encoding="utf-8")
    in_fence = False
    last_level = 0
    h1_count = 0
    for n, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            if level == 1:
                h1_count += 1
            if last_level and level > last_level + 1:
                report(path, n, f"Heading level jumps from H{last_level} to H{level}; keep the hierarchy in order.")
            last_level = level

        for img in MD_IMAGE.finditer(line):
            if not img.group("alt").strip():
                report(path, n, "Image has no alt text. Describe what it shows for students using screen readers.")

        for tag in HTML_IMG.findall(line):
            alt = re.search(r'alt\s*=\s*"([^"]*)"', tag)
            if alt is None:
                report(path, n, "<img> has no alt attribute.")
            elif not alt.group(1).strip() and "decorative" not in tag:
                report(path, n, 'Empty alt text is only allowed on images marked class="decorative".')

        if PLACEHOLDER.search(line):
            report(path, n, "Placeholder text found (TODO / TBC / lorem ipsum). Replace it before review.")

    if h1_count != 1:
        report(path, 1, f"Page should have exactly one H1 heading (found {h1_count}).")

    if LESSON_LANDING.search(path.name) and "learning-objectives" not in text:
        report(path, 1, "Lesson landing page is missing a learning-objectives admonition.")


def main():
    pages = sorted(CONTENT.rglob("*.md"))
    for page in pages:
        check(page)
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) found in {len(pages)} pages.")
        return 1
    print(f"All {len(pages)} pages passed the quality checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
