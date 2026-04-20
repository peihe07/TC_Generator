# TC Generator — Design System

A Windows 95-themed design system for **TC Generator**, an AI-powered desktop tool that ingests ASPICE SWE.6 test-case workbooks, generates test cases with LLMs, and exports back to Excel.

The product is a deliberately retro **single-page Win95 desktop** — not a web app. Every surface (dropzone, form, table, diff viewer, agent chat) lives inside a draggable 98.css-styled window. The entire visual language is built on a seven-step gray scale, navy + teal accents, and a ruthlessly consistent set of sunken/raised 3D bezels.

> **Rule of thumb:** if a pixel looks blurry, rounded, gradient-y, or warm, it's wrong. Win95 is sharp, cool-gray, and high-contrast.

---

## Sources

This system was reverse-engineered from:

- **Codebase:** `TC_Generator/` (Next.js + Python, attached via File System Access API)
  - `frontend/src/styles/win95.css` — all tokens (1049 lines)
  - `frontend/src/components/ui/` — 8 typed React primitives (Button, IconButton, StatusBadge, Checkbox, Radio, Select, Input, TitleBarMini)
  - `frontend/src/components/modules/` — 9 feature modules (upload, configure, generate, review, export, chat, quickGenerate, diagrams, rules)
  - `frontend/src/components/system/` — desktop chrome (Desktop, Taskbar, AppWindow, CostMeter)
- **Docs:**
  - `docs/DESIGN_SYSTEM.md` — authoritative design system reference
  - `docs/DESIGN_SYSTEM_AUDIT.md` — historical audit that motivated the current token layer
  - `docs/RULES.md` / `docs/ASPICE_SWE6_Test_Case_Writing_Rules.md` — product domain

## Index

```
.
├── README.md                — this file
├── SKILL.md                 — Agent Skill entry point
├── colors_and_type.css      — CSS variables (tokens) + semantic classes
├── fonts/                   — Pixelated MS Sans Serif .woff files (copied from 98.css)
├── assets/
│   └── icons/               — product icons (SVG, pixel-art, 32×32 → 48px render)
├── preview/                 — design-system cards (typography, color, components, ...)
├── ui_kits/
│   └── desktop/             — Win95 desktop recreation (index.html + JSX components)
└── slides/                  — (none — product has no decks)
```

---

## Product at a glance

TC Generator is a five-step pipeline exposed as five draggable windows:

1. **Upload** — drop the TC Specification `.xlsx`, optional reference workbook, optional spec PDF/DOCX.
2. **Configure** — three tabs (Grouping → Spec Matching → Options) that set `batchSize`, model, and budget.
3. **Generate** — live progress bar + streaming log + session stats (processed / cost / elapsed).
4. **Review** — table of generated TCs with expand-to-edit, flag-for-human, bulk regenerate, side-by-side diff against LLM re-runs.
5. **Export** — choose scope (all / accepted-only), confirm filename, download.

Two auxiliary surfaces:

- **Quick TC** — one-off "paste a requirement, get a TC" flow that bypasses the full job pipeline.
- **Agent Co-pilot** — persistent taskbar chat that watches the current window and offers context-aware help. Can also drive the pipeline via tool calls.

There is **one product** (the desktop) and **one brand**. No marketing site, no mobile, no print collateral.

---

## Content fundamentals

**Tone.** Dry, technical, imperative. The UI talks to engineers, not marketers.

- **Casing:** Title Case for window titles and section legends (`Export Scope`, `Generation Log`), UPPERCASE for status badges (`ACCEPTED`, `FLAGGED`) and mini-title-bars (`ORIGINAL REQUIREMENT`).
- **Voice:** Instructional ("Drag & Drop TC Spec Excel here"), second-person rare, no first-person. The system narrates its own state: _"Parsing SomeProject_SWQT_… through the shared job adapter."_, _"Re-generation complete. Review highlighted rows before applying."_
- **Bilingual:** UI labels are English; comments, logs and help contexts occasionally switch to Traditional Chinese (`求助 AI`, `[context: 目前在 Upload Module]`). When writing new strings, mirror this — English for user-facing, bilingual OK in internal help contexts.
- **Jargon OK.** The audience is QA/test-automation engineers. Use terms like _TC_, _Req ID_, _Test Set_, _SWE.6_, _regen diff_ without glossing.
- **Numbers are precise.** Costs show four decimals (`$0.0123`), durations are `mm:ss` with zero-padding, rows are _N / total_ never _N out of total_.
- **No emoji in product copy.** Emoji appear only in the Start menu (`📁 ⚙ ▶ 📋 💾 ⚡ 📊 📖 🤖`) as compact icon glyphs. Everything else uses Remix Icon SVGs or hand-drawn pixel-art SVGs.
- **Error messages are blunt.** _"Export failed."_, _"No accepted rows available for export. Switch scope to All Generated Cases or accept rows first."_ No apology, no "Oops".

### Examples (real strings from the app)

| Surface | Copy |
|---|---|
| Upload dropzone | `Drag & Drop TC Spec Excel here` |
| Upload ready banner | `[READY] Workbook staged. Parse the job to populate the shared desktop state.` |
| Generate log success | `Loaded 42 row(s) for SomeProject_DeviceManager.` |
| Review bulk action | `Marked 7 row(s) as accepted.` |
| Export confirm | `Final file will be named: results_generated.xlsx` |
| Agent taskbar (streaming) | (pulsing navy blue; no text beyond the robot icon) |
| Empty-state | `No accepted rows available for export. Switch scope…` |

---

## Visual foundations

### The seven grays

Everything is built on the Win95 neutral stack. Never invent a new gray.

```
#000000  --win95-black          text, icon strokes
#404040  --win95-gray-darker    outlines on dark surfaces
#606060  --win95-gray-dark      sunken-bezel shadow
#808080  --win95-gray-mid       secondary text, raised-bezel shadow
#c0c0c0  --win95-gray           DEFAULT SURFACE — 80% of the UI is this color
#dfdfdf  --win95-gray-light     raised-bezel highlight
#e0e0e0  --win95-gray-lighter   field-header separator
#ffffff  --win95-white          paper-card / input background, raised-bezel highlight
```

Two accents:

```
#008080  --win95-teal           desktop wallpaper (ONLY place teal appears)
#000080  --win95-navy           active title bar, selection highlight, user chat bubble
#1084d0  --win95-navy-light     gradient partner for active title bars
```

### Typography

Single family: **Pixelated MS Sans Serif** (self-hosted from 98.css, woff). No fallbacks for aesthetic reasons — if it fails to load the browser picks `MS Sans Serif` → `Arial`, which looks wrong but stays functional.

The scale is tight (5 sizes, 10–14px) because Win95 UI density demanded it:

```
--font-xs  10px   meta, captions, log timestamps, inspector labels
--font-sm  11px   row details, status-badge text
--font-md  12px   body inside modules, paper-card content
--font-base 13px  default UI
--font-lg  14px   section headings
```

Weight: effectively two-tone — normal or **bold**. Bold is used for legends (`<legend>`), active tabs, title-bar text, emphasised meta, and the pressed-button label offset.

`letter-spacing: 0.5px` is added to `.title-bar-mini` and status badges to mimic old bitmap-font tracking.

Body font is set on `body` with `!important` and propagated to `button, input, textarea, select, table, td, th, label` — browsers don't inherit font-family onto form elements by default, and missing this rule is the fastest way to break the aesthetic.

### Spacing

Driven by an internal 2px grid:

```
--space-1 2px   tight icon gaps
--space-2 4px   inter-button gap in toolbars
--space-3 6px   title-bar internal padding
--space-4 8px   standard row padding
--space-6 12px  section separator
--space-8 16px  module-level padding
```

Tailwind utilities (`p-2`, `gap-3`) are used for layout; the tokens above only appear when writing component CSS.

### Borders — the 3D bezel system

This is the single most important visual convention. Every surface is either **raised** (elevated, clickable, "above" the gray canvas) or **sunken** (recessed, inputs, sunken panels). Both are achieved with 2px borders using the gray scale:

**Raised** (buttons, title bars, taskbar, window chrome):
```css
border: 2px solid;
border-color: #ffffff #808080 #808080 #ffffff;   /* top/left light, bottom/right dark */
```

**Sunken** (inputs, dropzones, paper cards, progress bars, status badges):
```css
border: 2px solid;
border-color: #808080 #ffffff #ffffff #808080;   /* inverse — top/left dark, bottom/right light */
box-shadow: inset 1px 1px 0 #000000;             /* optional extra depth */
```

**Pressed state** flips the bezel so the element appears to "push in". Defined once in `win95.css` for `button:active`.

**No rounded corners. Ever.** The first rule in win95.css is `* { border-radius: 0 !important; }`. Sharp corners are non-negotiable — the entire 98.css library and every third-party component loses its modern softening when this stylesheet loads.

### Shadows

Two shadow vocabularies coexist:

- **Internal 3D (inset):** the bezel system above — `inset 1px 1px 0 #ffffff` for raised highlights, `inset -1px -1px 0 #808080` for raised shadows.
- **Floating drop (2-to-4px, hard):** offset-only, no blur, `box-shadow: 2px 2px 0 rgba(0,0,0,0.15)` on paper cards, `4px 4px 0 rgba(0,0,0,0.35)` on the floating toolbox. Blur is never used — Win95 didn't have the GPU for it, so we don't either.

No `elevation-1/2/3` scale. There are exactly two depths (cards and floating toolboxes) and you pick by context.

### Color — semantic status palette

Status signals come in a **bold** fill + **dark** text + **soft** background triad so the same semantic can be used as a badge, a row highlight, or an inline banner:

| Semantic | Bold | Dark | BG |
|---|---|---|---|
| Accept  | `#00a000` | `#006400` | `#c4e9c4` |
| Reject  | `#c00000` | `#8b0000` | `#f5b7b7` |
| Warn    | `#e0a000` | `#7d4e00` | — |
| Edit    | `#fb923c` | `#c2410c` | `#fffbe0` |
| Error   | `#cc0000` (border) | — | `#ffcccc` / `#fff0f0` |

**Orange is the "you're actively editing" signal** — it appears on `.paper-card.edit-mode`, the edit-variant `.title-bar-mini`, and the staging banner for regen diffs. Never use orange for anything else.

**Diff palette** (RegenDiff):
```
--diff-remove-bg: #faf6f4    --diff-remove-fg: #991b1b
--diff-add-bg:    #f4faf4    --diff-add-fg:    #166534
```

Slightly off-white, not the saturated red/green you see elsewhere — the diff viewer is read-heavy so the backgrounds need to calm down.

### Backgrounds

- **Desktop wallpaper:** solid `--win95-teal` (`#008080`). No pattern, no gradient, no image. This is the only place teal appears.
- **Window chrome:** `--win95-gray` (`#c0c0c0`). 80% of the UI surface.
- **Paper cards:** `#ffffff` with a sunken bezel and a hard drop shadow — they read as actual paper on a gray desk.
- **Orange edit mode:** `#fffbe0` wash with `--status-edit` border.
- **Agent chat user bubble:** `--win95-navy` (`#000080`), white text. The only navy surface that isn't a title bar.
- **No gradients anywhere** except the two canonical title-bar gradients: `linear-gradient(to right, #000080, #1084d0)` for active windows and `linear-gradient(to right, #c2410c, #ea580c)` for the edit-variant mini title bar.

### Motion

Intentionally minimal — anything over 200ms feels laggy against the static pixel aesthetic.

```
--motion-fast     120ms ease     hover/press transitions (color, bg, border)
--motion-progress 200ms linear   progress bar fill
```

- **Pulse animation** (agent-pulse, 1s) is used only on the taskbar Agent button and `.status-badge.generating` to signal "we're working".
- **Spin animation** (`.spin`, 1s linear) is used on loading icons inside tool cards.
- **No fade-in, no slide-in, no stagger.** Windows appear instantly. Rows expand instantly (no height transition). The only "animation" a user sees on most days is the 200ms progress-bar fill.

### Hover & press

- **Buttons:** no hover color change on 98.css base; `:focus-visible` shows a 1px dotted black outline inset 4px into the button face (Win95-accurate).
- **Icon buttons:** hover shows a 1px navy outline inset 2px (`outline: 1px solid #000080`).
- **Accept/reject icon buttons:** hover shows the soft status-bg (`#a8e6b8` / `#f5b7b7`) — the only place semantic BG colors appear on hover.
- **Table rows:** hover = selection (navy bg, white text). There is no "soft hover" — you're either selected or you aren't.
- **Press:** the 3D bezel flips + label shifts 1px down/right. No color change, no ripple.
- **Disabled:** `opacity: 0.5` and `cursor: not-allowed`. 98.css handles the 3D "disabled" bezel on buttons natively.

### Transparency & blur

Used sparingly:

- `rgba(0,0,0,0.15)` — paper-card drop shadow.
- `rgba(0,0,0,0.35)` — floating toolbox drop shadow.
- `rgba(0,0,0,0.25)` — status-badge inset shadow.
- `rgba(255,255,255,0.4)` — start-menu side stripe text.

**No backdrop-filter, no backdrop-blur.** Win95 had no alpha compositing and neither do we.

### Layout rules (fixed elements)

- **Taskbar:** 28px tall, pinned to `bottom: 0`, `z-index: 9999`, portaled via `createPortal` to escape stacking contexts.
- **CostMeter:** fixed top-right.
- **Start menu:** pops up from the Start button with a navy side stripe (`start-menu-side`, vertical "TC Generator" text, rotated 180°).
- **Windows:** draggable + resizable via `react-draggable` + `react-resizable`. Min 300×200, max 1600×1200. Title-bar height = 26px. Clamped so at least 80px of title bar remains visible at all times.
- **Floating toolbox** (`ReviewToolbox`): only appears when selection > 0 rows. 3D raised border + grip handle (dotted highlight/shadow pattern).

### Corner radii

Zero. Globally enforced. (`* { border-radius: 0 !important }`)

### Cards & containers

Three distinct container vocabularies, used consistently:

1. **`.paper-card`** — white, sunken-bezeled, hard drop-shadow. Expanded-detail content, TC cards, diff panels, agent bubbles. _"A sheet of paper on the gray desk."_
2. **`.stat-sunken`** / **`.dropzone-sunken`** — inset content regions, white bg, no drop shadow. Stats, dropzones.
3. **`<fieldset>` + `<legend>`** — 98.css provides these natively. Used for every form group (`Export Scope`, `Output Settings`, `Session Stats`). Always include a `<legend>`; always make it `font-bold`.

### Color vibe of imagery

There is effectively no imagery — the system is made of bezels, pixel icons, and typography. The nine desktop icons are 48×48 (rendered from 32×32 viewBox) hand-drawn pixel-art SVGs using `shapeRendering="crispEdges"`, stroked in pure `#000000`, filled with the brand palette (`#c0c0c0`, `#000080`, `#008080`, `#ffff00`, `#00ff00`, `#ff0000`). No grain, no photo, no illustration.

---

## Iconography

Three icon vocabularies coexist:

1. **Hand-drawn pixel-art SVGs (32×32 viewBox, rendered 48×48)** — used only for the nine desktop shortcuts. The app loads them from `/icons/desktop/*.svg` in `frontend/public/icons/desktop/`, referenced by `frontend/src/components/system/Desktop.tsx`. `shapeRendering="crispEdges"`, 1px black strokes, flat fills from the brand palette. The design-system copies live in `assets/icons/desktop/` so new surfaces can reuse them.

2. **Remix Icon (`@remixicon/react`)** — the primary icon set for everything inside modules. Loaded via CDN in this design system (npm package in the real app). Stroke-based line icons, 16–20px default. Used for toolbar buttons, status glyphs, action buttons.
   - CDN: `https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css`
   - React export pattern: `<RiCheckFill className="size-4" />`
   - Overrides: `button svg { width: 20px !important; height: 20px !important }` inside `win95.css`, but `svg.remixicon` gets `image-rendering: auto` (line icons should not be pixelated).

3. **Unicode glyphs** — appear only in the Start menu (`📁 ⚙ ▶ 📋 💾 ⚡ 📊 📖 🤖`) as cheap icon stand-ins. This is canon, but don't extend it to other surfaces; prefer Remix Icon or a new pixel-art SVG.

**Never invent SVG icons unless you're sure the system doesn't already have one.** Remix Icon has ~2800 icons; the ones actually used in the app live in `frontend/src/components/modules/**/*.tsx` imports (grep for `@remixicon/react`).

Common Remix Icons in the product (for quick reference):
- `RiCheckFill` / `RiCloseFill` — accept / reject row actions
- `RiFlagLine` / `RiFlagFill` — flag-for-human
- `RiEditLine` / `RiEditBoxLine` / `RiSaveLine` — edit flow
- `RiDeleteBinLine` — delete
- `RiRefreshLine` — regenerate
- `RiArrowDownSLine` / `RiArrowUpSLine` — row expand/collapse
- `RiFileExcel2Line` / `RiFileExcel2Fill` — workbook upload / export
- `RiFileSearchLine` / `RiFileLine` — reference docs
- `RiPlayListAddLine` — start run
- `RiStopCircleLine` — stop/cancel
- `RiMoneyDollarCircleLine` — cost
- `RiTimeLine` — elapsed
- `RiDownload2Line` — download
- `RiArrowRightLine` / `RiArrowLeftLine` — wizard nav
- `RiSettings4Line` / `RiFlashlightLine` — settings / quick TC
- `RiFileTextLine` — spec reference

---

## Font substitution note

The product uses **Pixelated MS Sans Serif** (via 98.css CDN, `.woff`). We copy both weights into `fonts/` so this design system works offline. No substitute is needed — the font is CC0 / public-domain per 98.css.

If for any reason the font fails to load, the cascade falls to `MS Sans Serif → Arial → sans-serif`. Arial looks wrong; flag this to the user if you see it.

---

## UI kits

- **`ui_kits/desktop/`** — The Windows 95 desktop shell + all 5 workflow modules as clickable prototypes. Demonstrates the full pipeline (Upload → Configure → Generate → Review → Export) plus the Agent chat, Start menu, Taskbar, desktop icons, and window chrome. This is the only UI kit — TC Generator has exactly one surface.

No separate marketing / mobile / docs kits exist in the product; if you need one, it doesn't exist yet and you should flag it.

---

## Caveats & known gaps

- **`border-sunken` Tailwind class:** referenced in `Input` and several modules but has no matching CSS rule (documented in `docs/DESIGN_SYSTEM.md` as a known dead class). Any "sunken" look today comes from `border-2` + browser default border color. Keep using it for parity; the upstream plans to define or remove it.
- **No dark mode.** The teal desktop + gray chrome is the only theme. Don't invent one.
- **No responsive layout.** Windows are fixed-size and draggable; on small screens they just overflow. The product is desktop-only by design.
