# TC Generator — Design System (Skill)

A Windows 95-themed design system for **TC Generator**, an AI-powered desktop tool that generates ASPICE SWE.6 test cases from Excel workbooks. The product is a single-page retro desktop — every surface lives inside a draggable 98.css-styled window.

## When to use this skill

Use when the user asks for designs, mocks, explorations or copy for **TC Generator** — module UI, dialogs, icons, agent-chat states, export flows, diff viewers, or anything that would render inside the desktop shell.

Do **not** use this skill for a marketing site, mobile app, print collateral, or any other product — TC Generator has one surface (the Win95 desktop) and no extended brand.

## Start here

1. **`README.md`** — full product context, content fundamentals, visual foundations. Read first for anything non-trivial.
2. **`colors_and_type.css`** — all tokens as CSS variables (fonts, spacing, grays, accents, semantic status triads, diff palette, shadows, motion). Link this from every new HTML file.
3. **`preview/`** — design-system cards (type, color, bezels, components, brand). Good reference for exact bezel recipes, badge styles, etc.
4. **`ui_kits/desktop/index.html`** — the complete desktop recreation (all 5 modules, agent chat, taskbar, start menu, dialog, diff). Copy windows out of this file when building new mocks.
5. **`assets/icons/desktop/`** — nine pixel-art SVG icons for desktop shortcuts. Use `width="48" height="48"` and `image-rendering: pixelated`.
6. **`fonts/`** — Pixelated MS Sans Serif woff files (referenced by `colors_and_type.css`).

## Non-negotiables

- **No rounded corners anywhere.** The global `* { border-radius: 0 !important }` is mandatory — keep it loaded.
- **Only seven grays + three accents** (teal, navy, navy-light). Never invent colors outside the token list. Semantic (accept/reject/warn/edit) and diff palettes are the only other hues allowed.
- **Teal (`#008080`) is ONLY the desktop wallpaper.** Navy (`#000080`) = active chrome + selection. Orange (`#fb923c`) = active-edit state, nothing else.
- **3D bezel system is the whole vocabulary.** Every surface is raised (light TL / dark BR) or sunken (dark TL / light BR). Pressed = bezel flips. See `preview/bezel-system.html`.
- **No gradients** except the two canonical title bars (navy→navy-light, or the edit variant c2410c→ea580c).
- **No blur, no backdrop-filter.** Drop shadows are offset-only (`2px 2px 0 rgba(0,0,0,0.15)` for paper, `4px 4px 0 rgba(0,0,0,0.35)` for floating).
- **Typography:** Pixelated MS Sans Serif only. Scale is 10–14px. Two weights (normal / bold). Courier New for IDs, filenames, log lines.
- **Motion is minimal.** 120ms hover/press, 200ms progress fills. Pulse for agent/generating. No fades, slides, or staggered reveals.
- **Voice:** terse, technical, imperative. No emoji (except Start menu). No apologies. Quantify everything ("14 test cases generated", "00:42 elapsed", "$0.0128").

## Typical tasks

- **New module / window** → copy a window block from `ui_kits/desktop/index.html`, swap the body. Keep title-bar height 26px, min window 300×200.
- **Form in a module** → wrap every group in `<fieldset class="w95"><legend>…</legend>`, bold legend, labels above inputs.
- **New status** → reuse one of the six badges (accepted/rejected/flagged/pending/reviewing/generating). If you truly need a new one, pick a bold+dark+bg triad that doesn't collide with the existing five.
- **New icon** → first grep `frontend/src/components/modules/` for an existing Remix Icon; only hand-draw a pixel-art SVG if it's a desktop shortcut.
- **Dialog** → the warning-dialog block in the UI kit is canonical: heavy drop shadow, chunky yellow `!` glyph, right-aligned action row with the default button bolded + outlined.

## Known gaps

- No dark mode. No responsive layout. No mobile. Don't invent them.
- `border-sunken` Tailwind class is referenced in upstream code but has no CSS rule; fall back to the `.bezel-sunken` pattern (or inline `border-color: #808080 #fff #fff #808080`).
- The upstream app uses `react-draggable` + `react-resizable` for window chrome. In static mocks, skip the drag/resize and just position windows absolutely.
