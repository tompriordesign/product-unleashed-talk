# Learn to ship native, with AI — talk deck

A self-contained, animated HTML presentation for a 13-minute talk at
Product Unleashed's design + AI launch event (London, June 5 2026).

**One file does it all:** `index.html` holds all 17 slides, the full design
system, embedded fonts (EB Garamond + JetBrains Mono), and the navigation +
animation logic. No internet, no build step needed to present — just open it.

## Present it

Open `index.html` in any modern browser and press **F** for fullscreen.
Each slide is designed at 1920×1080 and scales to fit any screen/projector.

Or serve it locally:

```
python3 -m http.server 8090 --directory .
# then open http://localhost:8090/
```

### Navigation

| Key | Action |
| --- | --- |
| `→` `Space` `PageDown` `↓` | Next slide |
| `←` `PageUp` `↑` | Previous slide |
| `Home` / `End` | First / last slide |
| `F` | Toggle fullscreen |
| Click | Next (click far-left 22% to go back) |

The URL hash tracks the current slide (`#7`), so you can deep-link or refresh
into any slide while rehearsing.

### Motion

Subtle-editorial: soft fades + gentle upward rises with staggered text reveals,
a slow cross-dissolve between slides, growing timeline bars (slide 7) and a
drawn-on quality/effort curve (slide 6). Respects `prefers-reduced-motion`.

## Rebuilding (only if you edit content)

Source of truth is `deck.template.html`. Fonts are injected at build time.

```
python3 build_fonts.py    # downloads EB Garamond + JetBrains Mono → fonts_embedded.css
python3 build_deck.py     # inlines fonts into deck.template.html → index.html
```

`build_fonts.py` needs internet (once). After that everything is offline.

## Running order (17 slides)

| # | Slide | Beat |
| --- | --- | --- |
| 01 | Hook | "How many of you have an app idea you haven't built yet?" |
| 02 | This is Migrapulse | What I built — voice-first migraine tracker, shipped, built with AI |
| 03 | Inflatable furniture | The problem: a vibe-coded app looks great until you sit on it |
| 04 | Gambling | My false start — two months in Lovable, no app |
| 05 | Vibing → Orchestrating | The hinge / spine idea: the level-up when you hit the ceiling |
| 06 | The curve | More effort, far higher ceiling (quality vs effort, crossover) |
| 07 | Timeline | More than a day, still almost nothing (months / a day / ~2 weeks) |
| 08 | Why apps | Apps are still a moat — +24%, 500M+, 2 wks |
| 09 | The map | Vibe·Design → Agentic·Build → AI-Assisted·Ship |
| 10 | Black box vs open | A black box — or every step in the open |
| 11 | The recipe | A chat is shouting; a doc is the recipe (markdown) |
| 12 | Phase 01 · Design | Rich context in, original out (contrast) |
| 13 | Phase 01 · the flow | Voice → brief → UX Pilot → real screens |
| 14 | Phase 02 · Build | Like sitting next to a developer (contrast) |
| 15 | Phase 02 · the flow | The doc → Cursor → a working app |
| 16 | Why it matters | With health data, trust is the product |
| 17 | Takeaway + QR | "It doesn't look vibe-coded — because it isn't." |

## Manual-swap placeholders

Four slides have dashed placeholders to drop real artwork into later:

- **Slide 02** — Migrapulse screenshot (phone frame)
- **Slide 04** — slot-machine / gambling image
- **Slide 16** — competitor App Store review screenshot ("my data is gone")
- **Slide 17** — real QR code (currently a decorative faux-QR; target URL TBC)

To swap one in, replace the matching `.ph` / `.qrbox` element in
`deck.template.html` with an `<img>` and rebuild — or, if you only need stills,
drop the image over the placeholder in your presentation tool.

## Note on the Keynote / PNG path

The original brief mentioned rendering each slide to a PNG for Keynote. That
path is **set aside for now** (per request) — this deliverable is the live HTML
deck. If you later want PNG stills, a small Playwright `render.py` can screenshot
each `.slide` at 2×; ask and it can be added.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The deck — open this to present (self-contained) |
| `deck.template.html` | Editable source (fonts injected at build) |
| `build_fonts.py` | Fetches + base64-embeds the two fonts |
| `build_deck.py` | Inlines fonts → `index.html` |
| `fonts_embedded.css` | Generated embedded-font CSS |
