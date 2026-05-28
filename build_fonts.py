#!/usr/bin/env python3
"""Fetch EB Garamond + JetBrains Mono from Google Fonts as woff2,
base64-embed them, and write a self-contained @font-face CSS file
(fonts_embedded.css) for inlining into the deck.

Run: python3 build_fonts.py
"""
import base64
import re
import sys
import urllib.request

CHROME_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

# Keep only the latin glyph subsets to keep the file small.
KEEP_SUBSETS = {"latin"}

CSS_URLS = {
    "EB Garamond": (
        "https://fonts.googleapis.com/css2?family=EB+Garamond:"
        "ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap"
    ),
    "JetBrains Mono": (
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:"
        "wght@400;500&display=swap"
    ),
}

# matches:  /* latin */\n@font-face { ... }
BLOCK_RE = re.compile(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", re.S)
URL_RE = re.compile(r"url\((https://[^)]+\.woff2)\)")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": CHROME_UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main() -> int:
    out_blocks = []
    for family, css_url in CSS_URLS.items():
        print(f"fetching CSS for {family} ...", file=sys.stderr)
        css = fetch(css_url).decode("utf-8")
        kept = 0
        for subset, block in BLOCK_RE.findall(css):
            if subset not in KEEP_SUBSETS:
                continue
            m = URL_RE.search(block)
            if not m:
                continue
            woff2_url = m.group(1)
            data = fetch(woff2_url)
            b64 = base64.b64encode(data).decode("ascii")
            data_uri = f"url(data:font/woff2;base64,{b64}) format('woff2')"
            block = URL_RE.sub(lambda _m: data_uri, block, count=1)
            # strip the format('woff2') Google already appends after url()
            block = block.replace(") format('woff2') format('woff2')",
                                  ") format('woff2')")
            out_blocks.append(f"/* {family} — {subset} */\n{block}")
            kept += 1
            print(f"  embedded {family} {subset} "
                  f"({len(data)//1024} KB)", file=sys.stderr)
        if kept == 0:
            print(f"  WARNING: no subsets embedded for {family}",
                  file=sys.stderr)

    css_out = "\n".join(out_blocks) + "\n"
    with open("fonts_embedded.css", "w") as f:
        f.write(css_out)
    print(f"\nwrote fonts_embedded.css "
          f"({len(css_out)//1024} KB, {len(out_blocks)} faces)",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
