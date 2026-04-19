# Handoff: TC Generator — Win95 Design System

## Overview

This bundle is the **TC Generator design system**, a Windows 95-themed visual language for an AI-powered desktop tool that ingests ASPICE SWE.6 test-case workbooks, generates test cases with LLMs, and exports back to Excel. The product is a deliberately retro single-page Win95 desktop — every surface (Upload / Configure / Generate / Review / Export, plus Agent chat, Quick TC, Diagrams, Rules) lives inside a draggable 98.css-styled window.

The bundle gives Claude Code:
- The token layer (`colors_and_type.css`)
- A complete reference desktop recreation (`ui_kits/desktop/index.html`)
- 21 single-purpose preview cards (`preview/*.html`) that show one component / token group each
- Pixel-art SVG desktop icons (`assets/icons/desktop/*.svg`)
- The full design-system narrative (`README.md`) and an entry point for AI agents (`SKILL.md`)

## About the Design Files

**The HTML files in this bundle are design references, not production code.** They are static prototypes that show the intended look, vocabulary, and behavior of the Win95 aesthetic.

The task in your codebase is to **recreate these designs inside the existing TC Generator codebase** (Next.js + React + Tailwind + 98.css), using its established structure: `frontend/src/styles/win95.css` (tokens), `frontend/src/components/ui/` (typed primitives), `frontend/src/components/modules/` (feature modules), `frontend/src/components/system/` (desktop chrome). Do **not** copy the prototype HTML's internal structure — port the *visual rules* and *component recipes* into the existing TS/TSX components.

## Fidelity

**High-fidelity.** Every color, bezel, spacing value, and font size is final. Hex values, border-color order, shadow offsets and motion timings are all canonical. Match them exactly.

## Goal in the codebase

Bring the live app fully in line with this design system. The token layer in `frontend/src/styles/win95.css` is already complete (tokens + `.bezel-raised` / `.bezel-sunken` / `.border-sunken` / `.type-*`). Remaining work — in priority order:

### Phase 1 — Global hard rules (one PR)
Add to the top of `globals.css` or `win95.css`:
```css
* { border-radius: 0 !important; }
body { font-family: var(--font-family-base) !important; background: var(--win95-teal); }
button, input, textarea, select, table, td, th, label {
  font-family: inherit !important;
  font-size: inherit !important;
}
```

### Phase 2 — Component unification (one PR each)
Replace inline `border-color: #fff #808080 #808080 #fff` and similar with the pattern classes:

1. `Input` / `Select` / `Textarea` → `.bezel-sunken`
2. `Button` / `IconButton` → `.bezel-raised` + `:active` flip
3. `StatusBadge` → 6 canonical variants (accepted / rejected / flagged / pending / reviewing / generating)
4. `AppWindow` title bar → 26px navy gradient + 3 system buttons
5. `PaperCard` → `.bezel-sunken` + `box-shadow: var(--shadow-paper)`
6. `Fieldset` + `Legend` → bold legend + `.bezel-sunken`
7. `Taskbar` / `StartMenu` / `Desktop` → match the UI kit layout
8. `CostMeter` → top-right raised box, mono digits

For each change, compare against the matching `preview/*.html` card.

### Phase 3 — Color audit
```bash
grep -rE "#[0-9a-f]{3,6}" frontend/src --include="*.tsx" --include="*.css"
```
Replace every hex not in the token list. **No new colors allowed.**

### Phase 4 — Motion cleanup
Grep `transition:` and `animation:`. Keep only:
- `120ms ease` (hover/press)
- `200ms linear` (progress fill)
- `pulse 1s` (agent + generating)
Remove all other fades / slides / staggers.

### Phase 5 — Iconography
- Desktop shortcuts → use `assets/icons/desktop/*.svg` (pixel-art, `image-rendering: pixelated`, render at 48×48)
- Module-internal icons → Remix Icon only, no hand-drawn SVG

## Visual foundations (reference only — full detail in README.md)

### The seven grays — never invent a new one
```
#000000  --win95-black           text, icon strokes
#404040  --win95-gray-darker
#606060  --win95-gray-dark       sunken-bezel shadow
#808080  --win95-gray-mid        secondary text, raised-bezel shadow
#c0c0c0  --win95-gray            DEFAULT SURFACE — 80% of UI
#dfdfdf  --win95-gray-light
#e0e0e0  --win95-gray-lighter
#ffffff  --win95-white
```

### Three accents
```
#008080  --win95-teal          desktop wallpaper ONLY
#000080  --win95-navy          active title bar, selection, user chat bubble
#1084d0  --win95-navy-light    title-bar gradient partner
```

### Semantic triads
| Semantic | Bold | Dark | BG |
|---|---|---|---|
| Accept | `#00a000` | `#006400` | `#c4e9c4` |
| Reject | `#c00000` | `#8b0000` | `#f5b7b7` |
| Warn   | `#e0a000` | `#7d4e00` | — |
| Edit   | `#fb923c` | `#c2410c` | `#fffbe0` |

Orange = "actively editing" only. Never use orange for anything else.

### Diff palette (RegenDiff)
```
--diff-remove-bg #faf6f4 / fg #991b1b
--diff-add-bg    #f4faf4 / fg #166534
```

### The 3D bezel system (the ONE visual rule)
**Raised** (buttons, title bars, taskbar, window chrome):
```css
border: 2px solid;
border-color: #fff #808080 #808080 #fff;   /* TL light, BR dark */
```
**Sunken** (inputs, dropzones, paper cards, badges, progress wells):
```css
border: 2px solid;
border-color: #808080 #fff #fff #808080;   /* TL dark, BR light */
box-shadow: inset 1px 1px 0 #000;
```
**Pressed:** sunken bevel applied to a raised element. Defined once in `win95.css` for `button:active`.

### Typography
- Single family: **Pixelated MS Sans Serif** (woff from 98.css CDN)
- 5-step scale: 10 / 11 / 12 / 13 / 14px (`--font-xs` … `--font-lg`)
- Two weights: normal + bold
- Mono: Courier New for IDs, filenames, log lines
- `letter-spacing: 0.5px` on title-bar-mini and status badges

### Spacing — 2px grid
`--space-1` 2 · `--space-2` 4 · `--space-3` 6 · `--space-4` 8 · `--space-6` 12 · `--space-8` 16

### Shadows
Two vocabularies:
- **Inset 3D bezel** (built into raised/sunken)
- **Hard offset drops, no blur**: `2px 2px 0 rgba(0,0,0,0.15)` for paper cards, `4px 4px 0 rgba(0,0,0,0.35)` for floating toolboxes

**No backdrop-filter. No backdrop-blur. No gradients except the two canonical title bars.**

### Motion
```
--motion-fast      120ms ease     hover/press
--motion-progress  200ms linear   progress bar
pulse              1s ease-in-out agent button + .status-badge.generating
spin               1s linear      tool-card loaders
```
No fade-in, no slide-in, no stagger.

## Voice & content rules

- Title Case for window titles and legends; UPPERCASE for badges and mini title bars
- Instructional, dry, technical. No emoji except in Start menu glyphs
- Numbers always precise: cost `$0.0123` (4 decimals), duration `mm:ss`, rows `N / total`
- Bilingual OK in internal help context (`求助 AI`, `[context: 目前在 Upload Module]`); user-facing strings stay English
- Errors are blunt: `Export failed.` `No accepted rows available for export.` — no apology, no "Oops"

## Non-negotiables

- **No rounded corners anywhere.** `* { border-radius: 0 !important }` is mandatory.
- **No new colors.** Stick to the token list.
- **No gradients** except the two title-bar gradients (navy→navy-light, c2410c→ea580c for edit).
- **No backdrop blur, no fade animations.**
- **No dark mode, no responsive layout, no mobile.** The product is desktop-only by design.
- **`border-sunken` Tailwind class** is referenced in `Input` and several modules. The class now exists in the token layer — verify the visual isn't too "deep" after Phase 1 (5 modules to spot-check: Upload, Generate, Review, Export, QuickGenerate).

## Files in this bundle

```
README.md                        — full design-system narrative
SKILL.md                         — agent entry point with non-negotiables
colors_and_type.css              — all CSS variables + semantic helpers + bezel patterns
ui_kits/
  desktop/
    index.html                   — full Win95 desktop recreation
    desktop-ui-kit.png           — rendered screenshot
preview/
  _card.css                      — shared card base
  type-scale.html                — 5-step font scale
  type-weights.html              — Regular / Bold / Mono
  color-neutrals.html            — 7-gray bezel stack
  color-accents.html             — Teal / Navy / Navy-light
  color-semantic.html            — Accept / Reject / Warn / Edit triads
  color-diff.html                — RegenDiff palette
  spacing-scale.html             — --space-1 … --space-8
  bezel-system.html              — Raised / sunken / pressed / paper / floating
  buttons.html                   — Primary / default / pressed / semantic
  badges.html                    — Status badges + mono ID chips
  form-inputs.html               — Text / textarea / select / checkbox / radio
  fieldsets.html                 — Grouped form sections
  tabs.html                      — Active lifts, inactive dimmed
  paper-cards.html               — List row + edit mode
  progress.html                  — Blocky segmented fill
  dialog.html                    — Warning confirm
  table.html                     — Header bevel, navy row select
  window-chrome.html             — Title bar + menu + status bar
  desktop-icons.html             — 8 task-flow glyphs
  taskbar.html                   — Taskbar + Start + tray
  voice.html                     — Engineer-direct copy rules
assets/
  icons/
    win95.css                    — original token source (reference only)
    desktop/                     — 9 pixel-art SVG shortcuts
      upload.svg
      configure.svg
      generate.svg
      review.svg
      export.svg
      quickGenerate.svg
      diagrams.svg
      rules.svg
      chat.svg
```

## How to use this bundle in Claude Code

1. Drop the unzipped folder anywhere accessible from the repo (e.g. `frontend/design_system/`).
2. Open the repo with Claude Code.
3. Tell Claude: *"Read `design_system/README.md` and `design_system/SKILL.md`, then start Phase 1 from the handoff."*
4. After Phase 1, point at one preview card per component and ask Claude to bring the matching `frontend/src/components/ui/<name>.tsx` in line with it.
5. After each phase, run `npm run dev` and visually compare the running app to `ui_kits/desktop/desktop-ui-kit.png`.
