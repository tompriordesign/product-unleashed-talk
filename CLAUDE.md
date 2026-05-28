# Talk deck — working notes for Claude

This repo is a **self-contained animated HTML slide deck** for a 13-minute talk
("Learn to ship native, with AI", Product Unleashed, June 5 2026). It is
deployed on Vercel and viewed on a phone.

## How to make changes (IMPORTANT)

- **Edit content/layout in `deck.template.html`** — never hand-edit `index.html`
  (it contains ~400 KB of base64-embedded fonts and is generated).
- After editing the template, **rebuild and commit the output**:
  ```
  python3 build_deck.py        # inlines fonts_embedded.css into index.html
  ```
  Then commit BOTH `deck.template.html` and the regenerated `index.html`.
- **Vercel serves `index.html` as a static file**, so the rebuilt `index.html`
  must be committed for changes to appear on the live URL.
- `build_deck.py` is pure stdlib and needs **no network**. Do NOT run
  `build_fonts.py` (it fetches Google Fonts and needs internet, which the cloud
  sandbox blocks). The fonts are already embedded in `fonts_embedded.css`.

## Workflow: explore on a preview URL, ship on approval (USER PREFERENCE)

Tom's chosen loop (confirmed 2026-05-28) for iterating on slides:

1. Edit `deck.template.html`, then `python3 build_deck.py`.
2. Commit BOTH `deck.template.html` and `index.html` and push the working
   branch. Vercel auto-builds a **preview** for that branch (~1 min). Give Tom
   the branch preview URL (deep-link the slide with `#<n>`):
   ```
   https://product-unleashed-talk-git-<branch-slug>-tomprioruk-2872s-projects.vercel.app/#<slide-number>
   ```
   The branch alias auto-updates to the latest build on every push, so Tom just
   refreshes in Chrome. Vercel **Deployment Protection → Require Log In is OFF**,
   so preview URLs are publicly viewable (he flipped it 2026-05-28).
3. **Only when Tom approves**, ship to production: merge the branch to `main`
   (Vercel auto-deploys production). Pre-authorized once he approves — he can
   also say "push it live" anytime. Then reply with a cache-busted production
   deep link:
   ```
   https://product-unleashed-talk.vercel.app/?v=<short-sha>#<slide-number>
   ```
   `?v=<short-sha>` busts mobile Safari's cache; `#<n>` deep-links the slide (1–17).

**Claude cannot verify any URL itself**: the sandbox egress allowlist blocks all
`*.vercel.app` hosts (`x-deny-reason: host_not_allowed`), so Tom is the one who
confirms a preview/production URL loads. Fallback if a preview ever won't build:
send the self-contained `index.html` via `SendUserFile` (renders offline in any
browser). Do NOT send PNG screenshots — Tom wants the real interactive HTML.

## Verifying

Serve locally and screenshot a few slides before committing:
```
python3 -m http.server 8090
# open http://localhost:8090/  — press F for fullscreen, arrows/space to navigate
```
The deck is designed at 1920×1080 and scales to fit. See `README.md` for the
full running order, navigation keys, and the four manual-swap placeholders
(slides 02, 04, 16, 17).

## Design system (keep consistent)

Cream `#fbf7f2`, ink `#1c1a24`, coral `#d4604f`, violet `#c074e8`, green
`#5fa572`. Serif headlines (EB Garamond) with accent words in coral italic;
mono labels (JetBrains Mono) for kicker/topbar/footer. One idea per slide, big
type, readable from the back of a room. Motion is subtle-editorial (soft fades,
staggered reveals, slow cross-dissolves). Spine phrases: "from vibing to
orchestrating" and "vibe-designed, not vibe-coded".
