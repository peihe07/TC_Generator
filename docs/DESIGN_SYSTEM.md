# Design System — TC Generator (Frontend)

**Last updated:** 2026-04-19
**Scope:** `frontend/src/components/ui/` primitives + `frontend/src/styles/win95.css` tokens

This document is the authoritative reference for the Win95-themed design system used in TC Generator.

---

## Overview

The system is intentionally small and non-magical:

- **Base stylesheet:** [`98.css`](https://jdan.github.io/98.css/) (v0.1.21) gives us the Win95 look for native elements — `<button>`, `<input>`, `<select>`, `<fieldset>`, window chrome.
- **Custom layer:** `src/styles/win95.css` (~1048 lines) defines CSS design tokens, utility classes, and app-specific components (title bars, status badges, paper cards).
- **Tailwind 4** (PostCSS-only, no config file) supplies layout utilities (`flex`, `grid`, `gap-*`, `p-*`).
- **UI primitives:** `frontend/src/components/ui/` exports 8 React components that wrap native elements with type-safe props, consistent class merging, and `forwardRef`.

The primitives are **stateless**. They don't own any interactive state themselves — everything is controlled via native props (`checked`, `onChange`, `disabled`). Complex interactions (dialogs, comboboxes) are deferred until we genuinely need them, at which point we'd add Radix-based primitives alongside these.

---

## Design tokens

All tokens live under `:root` in `src/styles/win95.css`. Tailwind utilities are for layout only; **never hardcode colors in components** — reach for a token instead.

### Typography

| Token | Value | Use |
|---|---|---|
| `--font-xs` | 10px | Meta / captions (field labels, TC metadata) |
| `--font-sm` | 11px | Secondary text (row details) |
| `--font-md` | 12px | Body text inside modules |
| `--font-base` | 13px | Default UI size (matches 98.css) |
| `--font-lg` | 14px | Section headings |

### Spacing

| Token | Value |
|---|---|
| `--space-1` | 2px |
| `--space-2` | 4px |
| `--space-3` | 6px |
| `--space-4` | 8px |
| `--space-6` | 12px |
| `--space-8` | 16px |

Prefer Tailwind's spacing utilities (`p-2`, `gap-3`) for layout; use these tokens when writing component CSS.

### Palette

The Win95 neutrals stack from `--win95-black` → `--win95-white`. These are the seven grays the entire UI is built on:

```
--win95-black         #000000
--win95-gray-darker   #404040    outline on dark surfaces
--win95-gray-dark     #606060
--win95-gray-mid      #808080    secondary text
--win95-gray          #c0c0c0    default surface (title bars, chrome)
--win95-gray-light    #dfdfdf
--win95-gray-lighter  #e0e0e0    field-header separators
--win95-white         #ffffff
```

Accents:

```
--win95-teal          #008080    desktop background
--win95-navy          #000080    title-bar background, select highlight
--win95-navy-light    #1084d0    active window chrome
--win95-select-bg     #000080    focused select highlight
--win95-select-text   #ffffff    on select-bg
--text-muted          #666666    secondary text on light surface
```

### Status colors

Two layers per semantic: a **bold** shade for icons/fills and a **bg** shade for backgrounds.

| Semantic | Bold | Dark text | Background |
|---|---|---|---|
| Accept | `--status-accept` #00a000 | `--status-accept-dark` #006400 | `--status-accept-bg` #c4e9c4 |
| Reject | `--status-reject` #c00000 | `--status-reject-dark` #8b0000 | `--status-reject-bg` #f5b7b7 |
| Warn | `--status-warn` #e0a000 | `--status-warn-dark` #7d4e00 | — |
| Edit | `--status-edit` #fb923c | `--status-edit-dark` #c2410c | `--status-edit-bg` #fffbe0 |
| Error | `--status-error-border` #cc0000 | — | `--status-error-bg` #ffcccc / `--status-error-bg-soft` #fff0f0 |

Edit-mode accent (orange staging banner, RegenDiff header): `--edit-accent-bg` / `--edit-accent-border` / `--edit-accent-fg`.

Diff rendering (RegenDiff side-by-side):

```
--diff-remove-bg  #faf6f4     --diff-remove-fg  #991b1b
--diff-add-bg     #f4faf4     --diff-add-fg     #166534
```

Field-header chrome (paper-card section headers):

```
--field-header-bg     #e8e8e8
--field-header-border #d0d0d0
```

### Motion

```
--motion-fast      120ms ease     hover / press transitions
--motion-progress  200ms linear   progress bar fill
```

Keep animations short — anything over 200ms starts to feel laggy against the static Win95 aesthetic.

---

## Primitives

All primitives live in `src/components/ui/` and are re-exported from `ui/index.ts`. Import them via the barrel:

```tsx
import { Button, IconButton, StatusBadge, Checkbox, Radio, Select, Input, TitleBarMini } from '../../ui';
```

Every primitive:
- Uses `React.forwardRef` so parent callers can access the underlying DOM node.
- Spreads remaining props onto the native element (`...rest`), so native attributes like `disabled`, `onClick`, `aria-*`, `data-*` all work without special-casing.
- Merges a caller-provided `className` with the primitive's own classes rather than overriding.

### Button

```tsx
<Button variant="accept" onClick={handleAccept}>
  Apply Changes
</Button>
```

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `'default' \| 'accept' \| 'reject'` | `'default'` | `accept` → green text, `reject` → red text |
| `type` | `'button' \| 'submit' \| 'reset'` | `'button'` | Defaults to `'button'` to avoid accidental form submits |
| ... | all `<button>` HTML attrs | | |

Uses 98.css button styling plus our `:focus-visible` and `:active` overrides from win95.css.

### IconButton

Square 22×22 icon-only button. `label` is **required** and applied to both `title` (tooltip) and `aria-label` (screen readers).

```tsx
<IconButton label="Delete row" variant="reject" onClick={() => remove(id)}>
  <RiDeleteBinLine className="size-4" />
</IconButton>
```

| Prop | Type | Required |
|---|---|---|
| `label` | `string` | **yes** — a11y name for the icon |
| `variant` | `ButtonVariant` | no (same values as Button) |

### StatusBadge

Sunken Win95-style pill, used in row status columns.

```tsx
<StatusBadge status="accepted" />                           // "ACCEPTED"
<StatusBadge status="flagged">awaiting review</StatusBadge> // custom label
```

| Prop | Type | Notes |
|---|---|---|
| `status` | `'accepted' \| 'rejected' \| 'flagged' \| 'pending' \| 'reviewing' \| 'generating'` | Drives the background color via `.status-badge.<status>` CSS class |
| `children` | `ReactNode` | Optional — defaults to `status.toUpperCase()` |

Color alone is not enough — the badge always renders text too, so color-blind users still get the semantic.

### Checkbox / Radio

Both primitives bundle the native input with its `<label>` inside a `.field-row` wrapper. Auto-generates an `id` via `React.useId()` when one isn't provided, so the `htmlFor` pairing always works.

```tsx
<Checkbox label="Include Steps" defaultChecked />

<Radio name="scope" label="All Cases" checked={scope === 'all'} onChange={...} />
<Radio name="scope" label="Accepted Only" checked={scope === 'accepted'} onChange={...} />
```

| Prop | Type | Notes |
|---|---|---|
| `label` | `ReactNode \| null` | Pass `null` + `aria-label` for bare inputs (e.g. table-row select) |
| `name` (Radio only) | `string` | Required — groups the radios |
| `wrapperClassName` | `string` | Defaults to `"field-row"` — override for non-standard layouts |

### Select

Native `<select>` with an `options` convenience prop. Either pass `options` or provide raw `<option>` children — `children` wins when both are present.

```tsx
<Select value={model} onChange={(e) => setModel(e.target.value)} options={MODEL_OPTIONS} />

<Select value={testSet} onChange={...}>
  <option value="all">All Sets</option>
  {dynamicSets.map((s) => <option key={s} value={s}>{s}</option>)}
</Select>
```

### Input

Win95 text input with a sunken 3D border by default. Set `inputStyle="flat"` inside table cells where a full border would be visually noisy.

```tsx
<Input placeholder="Filter…" value={query} onChange={(e) => setQuery(e.target.value)} />
<Input inputStyle="flat" type="number" />
```

### TitleBarMini

Miniature title-bar row used above "paper-card" content blocks (TC cards, Original/Generated split in Review, RegenDiff staging header).

```tsx
<TitleBarMini
  icon={<RiFlashlightLine className="size-3" />}
  title={`TC ${index + 1} — ${scenarioName}`}
>
  <span style={{ ...PRIORITY_BASE, ...priorityColor }}>{priority}</span>
</TitleBarMini>

<TitleBarMini variant="edit" icon={<RiRefreshLine />} title="New Version Ready">
  <Button onClick={discard}>Discard</Button>
  <Button className="default" onClick={apply}>Apply</Button>
</TitleBarMini>
```

| Prop | Type | Notes |
|---|---|---|
| `title` | `ReactNode` | flex-1 middle slot — pass string or JSX |
| `icon` | `ReactNode` | Optional leading icon (typically `size-3`) |
| `variant` | `'default' \| 'edit'` | `edit` applies the orange edit-accent class |
| `children` | `ReactNode` | Trailing content — badges, buttons, labels |

The primitive extends `HTMLAttributes<HTMLDivElement>` minus `title` (which we redefine as ReactNode), so `className`, `style`, `onClick`, `aria-*` all pass through.

---

## CSS utility classes

These are app-level classes defined in `win95.css` that components still use directly (they haven't been wrapped into primitives because they're one-offs or pure layout).

- **`.paper-card`** — off-white content panel with sunken border, used for TC content blocks and diff panels. Pairs with `.edit-mode` for the orange edit outline.
- **`.title-bar`** / **`.title-bar-text`** — full window-chrome title bar (used by `AppWindow`, not by primitives).
- **`.win95-row`** — table-row hover/selected styling, used in the Review table.
- **`.win95-th`** — sticky table header cell; add `.center` for center-aligned columns.
- **`.win95-toolbox`** / **`.win95-toolbox-handle`** / **`.win95-toolbox-group`** — floating draggable toolbox (Agent taskbar button).
- **`.dropzone-sunken`** / **`.stat-sunken`** — inset content regions (upload dropzone, dashboard stat cards).
- **`.progress-bar-wrap`** — wraps a `.progress-fill` + optional `.progress-label` for the Win95-style progress bar.
- **`.status-bar-field`** — footer-style field from 98.css, used for "final filename will be…" notices.
- **`.selectable`** — opts text back into user selection inside the global-noselect window body.
- **`.diff-add`** / **`.diff-del`** — inline token highlighting inside RegenDiff's `DiffText` renderer.

> Known dead class: `border-sunken` is referenced by `Input` and several modules (via `border-2 border-sunken`) but has no matching CSS rule. The "sunken" visual today comes from `border-2` alone + browser default border color. Candidate for cleanup in the upcoming CSS split (P3-3) — either define it as a real Tailwind 4 utility or remove the references.

Classes not listed here (chat module, desktop, start menu, taskbar) are feature-module-specific and shouldn't be used outside their module.

---

## When to add a new primitive

Add one when **three or more call sites** share the same DOM shape and would benefit from type safety / consistency. Examples that already met the bar: `Button`, `StatusBadge`, `TitleBarMini`. Examples that haven't (yet): `PaperCard`, `Fieldset`, `ProgressBar` — each has only one or two call sites today, so a primitive would be premature.

Checklist for new primitives:

1. **Stateless** — take controlled props, no internal state unless genuinely required (e.g. disclosure). If state is needed, document why.
2. **`forwardRef`** — always. Parents may need to focus, measure, or animate the node.
3. **Spread `...rest`** — don't swallow native props. If a prop conflicts (e.g. our `title: ReactNode` vs HTML `title: string`), `Omit` it from the extended type.
4. **Merge `className`** — never overwrite. Filter out falsy values before `join(' ')` to avoid double spaces.
5. **Label / a11y mandatory where it matters** — icon-only buttons require `label`; checkboxes accept `label={null}` only when paired with `aria-label`.
6. **Test** — at minimum: renders, applies variants, merges className, passes through style/aria. See `src/__tests__/ui.*.spec.tsx` for the pattern.

---

## Testing

- Unit: **Vitest** + **@testing-library/react** in `src/__tests__/ui.*.spec.tsx`. Each primitive has 5–7 tests covering variants, class merging, event wiring, and attribute passthrough.
- e2e: **Playwright** in `frontend/e2e/`. Currently one smoke test (`generate-export.spec.ts`) exercising the full flow.

Run everything:

```bash
cd frontend
npm run typecheck         # tsc --noEmit
npm run test:unit         # vitest run
npm run test:e2e          # playwright test
```

---

## File map

```
frontend/src/
├── components/ui/
│   ├── Button.tsx            ButtonProps, ButtonVariant
│   ├── IconButton.tsx        IconButtonProps
│   ├── StatusBadge.tsx       StatusBadgeProps, StatusVariant
│   ├── Checkbox.tsx          CheckboxProps
│   ├── Radio.tsx             RadioProps
│   ├── Select.tsx            SelectProps, SelectOption
│   ├── Input.tsx             InputProps
│   ├── TitleBarMini.tsx      TitleBarMiniProps, TitleBarMiniVariant
│   └── index.ts              barrel — import from here
├── styles/win95.css          tokens (:root) + utility classes + .status-badge rules
└── __tests__/ui.*.spec.tsx   one spec file per primitive
```
