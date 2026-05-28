#!/usr/bin/env python3
"""Inline the embedded fonts into the deck template to produce a single,
self-contained index.html.

Run: python3 build_deck.py
(Run build_fonts.py first to generate fonts_embedded.css.)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "deck.template.html")
FONTS = os.path.join(HERE, "fonts_embedded.css")
OUT = os.path.join(HERE, "index.html")
MARKER = "/*FONTS_EMBEDDED*/"


def main() -> int:
    with open(TEMPLATE) as f:
        html = f.read()
    if not os.path.exists(FONTS):
        print("ERROR: fonts_embedded.css missing — run build_fonts.py first.",
              file=sys.stderr)
        return 1
    with open(FONTS) as f:
        fonts_css = f.read()
    if MARKER not in html:
        print(f"ERROR: marker {MARKER} not found in template.", file=sys.stderr)
        return 1
    html = html.replace(MARKER, fonts_css)
    with open(OUT, "w") as f:
        f.write(html)
    print(f"wrote index.html ({len(html)//1024} KB)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
