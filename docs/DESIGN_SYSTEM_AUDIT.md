# Design System Audit — TC Generator (Frontend)

**Audited:** 2026-04-19
**Scope:** `frontend/` (Next.js 16 + React 19 + Tailwind 4 + 98.css)
**Files reviewed:** 24 component files, 2 stylesheet files, `app/globals.css`, `package.json`

---

## Summary

| Metric | Value |
|---|---|
| Components reviewed | 24 |
| Tokens defined | 6 CSS variables |
| Token usage in components | **0 references** |
| Hardcoded hex values | **257 in .tsx**, 132 in win95.css |
| Arbitrary Tailwind values | 26 |
| Inline `style={{ ... }}` blocks | 159 |
| Unique hex colors in stylesheet | 53 (only 6 tokenized) |
| Aria attributes across all components | 5 |
| Component tests | 1 / 24 |
| Component docs / stories | 0 |
| **Overall score** | **32 / 100** |

The visual language is well-established (consistent Win95 aesthetic), but the **system has not been formalized**: tokens are declared but bypassed, a UI primitive layer is missing, and there is no documentation. Before any refactor, the single biggest win is to retire dead code and make existing tokens the source of truth.

---

## Stack & Structure

- **Framework:** Next.js 16.2.4, React 19.2.4
- **Styling:** Tailwind 4 (PostCSS only, no `tailwind.config.*`) + `98.css` 0.1.21 + custom `src/styles/win95.css` (892 lines)
- **UI libs installed:** `@radix-ui/{checkbox,dialog,select,tabs,tooltip}` — **not used in any component**
- **State:** Zustand; **Data:** TanStack Query; **Utils:** 98.css theme, `react-draggable`, `react-resizable`

### Surface area

```
frontend/
├── app/                    # Next.js routes — globals.css imports win95.css
├── components/             # ⚠️ EMPTY legacy folders (desktop/, retro/, window/)
├── styles/win95.css        # ⚠️ 752-line DUPLICATE, not imported (stale)
└── src/
    ├── components/
    │   ├── modules/        # Feature modules (chat, configure, generate, …)
    │   │   └── ChatModule.tsx   # ⚠️ outlier — other modules live in their own folder
    │   ├── system/         # Window chrome (Taskbar, Desktop, AppWindow, …)
    │   └── ui/             # ⚠️ EMPTY — canonical primitives folder never populated
    └── styles/win95.css    # 892-line ACTIVE stylesheet
```

---

## 1. Dead Code & Duplication (High priority)

| Item | Status | Recommendation |
|---|---|---|
| `frontend/components/{desktop,retro,window}/` | Empty, never referenced | **Delete** — holdover from early scaffold |
| `frontend/styles/win95.css` | 752 lines, not imported anywhere (diff vs active file) | **Delete** — this is the source of drift between files |
| `src/components/ui/` | Empty folder | **Keep & populate** as primitive layer (see §5) |
| `@radix-ui/*` (5 packages) | 0 imports in components | Either **adopt** via ui/ primitives or **remove** from `package.json` |

> The two divergent `win95.css` files are a latent bug: if someone edits the wrong one, the change silently has no effect.

---

## 2. Design Tokens (Critical)

Tokens are defined in `src/styles/win95.css`:

```css
:root {
  --font-base-size: 13px;
  --win95-teal: #008080;
  --win95-gray: #c0c0c0;
  --win95-navy: #000080;
  --win95-white: #ffffff;
  --win95-select-bg: #000080;
  --win95-select-text: #ffffff;
}
```

### Problem: the tokens are **declared but bypassed**.

| Category | Tokens defined | Hardcoded instances found |
|---|---|---|
| Colors | 5 color tokens | **257 raw hex in .tsx**, 132 in win95.css |
| Typography | 1 size token | 9 different font-size px values in stylesheet |
| Spacing | **0** | 26 Tailwind arbitrary values (`w-[320px]`, `min-h-[80px]`, `text-[10px]`) + scattered raw px in inline styles |
| Borders / Radius | 0 | Global `* { border-radius: 0 !important }` replaces tokenization |
| Shadows | 0 | Hand-rolled Win95 3D borders everywhere (`border-color: #808080 #ffffff ...`) |
| Motion | 0 | `transition: ... 120ms ease` / `200ms linear` scattered |

### Top hardcoded hex (in .tsx files)

| Hex | Occurrences | Should map to |
|---|---|---|
| `#808080` | 39 | `--win95-gray-mid` (new — middle gray, the "3D border shadow") |
| `#ffffff` | 32 | `--win95-white` (exists ✓) |
| `#000` / `#000000` | 26 + 6 | `--win95-black` (new) |
| `#c0c0c0` | 21 | `--win95-gray` (exists ✓) |
| `#000080` | 19 | `--win95-navy` (exists ✓) |
| `#e0e0e0` | 9 | `--win95-gray-light` (new) |
| `#8b0000` / `#c00000` | 6 + 2 | `--status-reject` |
| `#006400` / `#00a000` | 6 + 2 | `--status-accept` |
| `#fb923c` | 5 | `--status-edit` |
| `#606060` / `#404040` | 5 + 2 | `--win95-gray-dark` |

> **De facto palette:** the codebase is already using ~10 semantic colors consistently. They just need to be **promoted** to tokens so they can be adjusted in one place.

### Proposed token additions

```css
:root {
  /* Neutral scale (Win95 3D borders need ALL of these) */
  --win95-black:         #000000;
  --win95-gray-dark:     #606060;
  --win95-gray-mid:      #808080;
  --win95-gray:          #c0c0c0;   /* existing */
  --win95-gray-light:    #dfdfdf;
  --win95-white:         #ffffff;   /* existing */

  /* Brand */
  --win95-teal:          #008080;   /* existing */
  --win95-navy:          #000080;   /* existing */

  /* Semantic status */
  --status-accept:       #00a000;
  --status-accept-dark:  #006400;
  --status-reject:       #c00000;
  --status-reject-dark:  #8b0000;
  --status-warn:         #e0a000;
  --status-edit:         #fb923c;
  --status-edit-bg:      #fffbe0;

  /* Typography scale */
  --font-xs:   10px;
  --font-sm:   11px;
  --font-base: 13px;   /* existing */
  --font-md:   14px;

  /* Spacing scale */
  --space-1: 2px;
  --space-2: 4px;
  --space-3: 6px;
  --space-4: 8px;
  --space-6: 12px;
  --space-8: 16px;
}
```

---

## 3. Naming Consistency

| Concern | Finding | Recommendation |
|---|---|---|
| Component file names | All PascalCase ✓ | Keep |
| Module folder names | `chat/`, `configure/`, `generate/` (lowercase) vs `quickGenerate/` (camelCase) | Pick one — suggest **kebab-case** (`quick-generate/`) to match Next.js route convention |
| Module entrypoint location | `modules/configure/ConfigureModule.tsx` ✓ but `modules/ChatModule.tsx` lives at root | Move to `modules/chat/ChatModule.tsx` for consistency |
| CSS class naming | Mixed `win95-*`, `chat-*`, `title-bar-*`, `sys-log-*`, `paper-card` | Adopt a prefix convention — e.g. `tcg-<component>__<element>` (BEM-lite) |
| Token naming | `--win95-*` (domain) vs intent needed | Keep `--win95-*` for raw palette, add `--status-*` / `--surface-*` for semantic tokens |

---

## 4. Component Completeness

### States coverage in `win95.css`

| State | Count | Gap |
|---|---|---|
| `:hover` | 10 | OK |
| `:disabled` | 4 | Thin |
| `:focus` | 2 | **Weak** |
| `:focus-visible` | 0 | **Missing — keyboard users can't see focus** |
| `:active` | 0 | **Missing — no "pressed" Win95 effect** |

### Per-component snapshot

| Component | LoC | Inline styles | States | Variants | Tests | Docs | Score |
|---|---|---|---|---|---|---|---|
| AppWindow | 157 | 0 | focus only | focused/inactive, maximized | — | — | 5/10 |
| Taskbar | 221 | 17 | hover | — | — | — | 4/10 |
| Desktop | 231 | 3 | hover/selected | — | — | — | 5/10 |
| CostMeter | 187 | 16 | — | — | — | — | 3/10 |
| WorkspaceMenu | 182 | 19 | hover | — | — | — | 3/10 |
| JobHistoryMenu | 142 | 15 | hover | — | — | — | 3/10 |
| ChatModule | 31 (+ 6 sub) | 0 | hover | — | ✓ | — | 6/10 |
| ReviewModule | **800** | **39** | hover/disabled | accepted / rejected / flagged / pending (via `.status-badge`) | — | — | 4/10 |
| QuickGenerateModule | **574** | 15 | hover/disabled | mode-select | — | — | 4/10 |
| ConfigureModule | **502** | 21 | hover/disabled | tab states | — | — | 4/10 |
| UploadModule | 199 | 0 | dropzone `.dragging` | — | — | — | 5/10 |
| GenerateModule | 192 | 3 | — | — | — | — | 3/10 |
| ExportModule | 207 | 0 | — | — | — | — | 3/10 |
| RulesModule | 55 | 4 | hover (tab) | — | — | — | 3/10 |
| DiagramsModule | — | — | — | — | — | — | 2/10 |
| HelpFromAgentButton | — | — | — | — | — | — | 2/10 |

**Three files over 500 LoC (Review / QuickGenerate / Configure)** are clear refactor candidates — each re-implements buttons, tabs, cards, and tables inline instead of using a shared primitive.

---

## 5. Missing: UI Primitive Layer

`src/components/ui/` is an empty folder — the canonical Radix-pattern location for base primitives. Adopting Radix (already installed) and building these primitives would:

- Eliminate the 159 `style={{ ... }}` blocks scattered across modules
- Provide accessibility for free (focus, keyboard, aria)
- Cut the three large modules roughly in half

### Proposed `ui/` primitives

| Primitive | Wraps | Replaces |
|---|---|---|
| `Button` | native `<button>` + Win95 3D borders | ~50+ hand-rolled buttons |
| `IconButton` | `Button` + size variant | `.btn-icon` CSS + inline styles |
| `Dialog` | `@radix-ui/react-dialog` + Win95 chrome | Not yet needed but will be |
| `Select` | `@radix-ui/react-select` + Win95 dropdown | Hand-rolled popups in CostMeter, WorkspaceMenu |
| `Tabs` | `@radix-ui/react-tabs` + Win95 inset | Custom tabs in Rules, Configure |
| `Checkbox` | `@radix-ui/react-checkbox` + Win95 box | — |
| `Tooltip` | `@radix-ui/react-tooltip` | `title` attributes (not accessible) |
| `StatusBadge` | `<span>` | `.status-badge` + 5 variant classes |
| `Dropzone` | — | `.dropzone-sunken` |
| `StatBox` | — | `.stat-sunken` |
| `ProgressBar` | — | `.progress-bar-wrap` markup |
| `Window` + `TitleBar` | — | Parts of `AppWindow.tsx` |

---

## 6. Accessibility

| Issue | Severity | Note |
|---|---|---|
| Only 5 `aria-*` attributes total across 24 components | High | Most interactive elements have no accessible name |
| `:focus-visible` defined 0 times | High | Keyboard focus indistinguishable |
| `.window-body, .window-body *` disables `user-select` globally | Medium | Impacts copy/paste UX, may confuse screen readers |
| Status badges use color alone (green/red/yellow) | Medium | Colorblind users cannot distinguish — add icon or text cue |
| Button `min-height: 28px` | OK | Close to 44px WCAG recommendation but usable |
| Retro pixelated font rendering | OK | Aesthetic choice, contrast ratios adequate |
| No `<html lang>` dynamic | Low | Hardcoded `lang="en"` but UI mixes Chinese/English |

---

## 7. Documentation & Tests

- **Docs:** `AGENTS.md` (5 lines, only says "Next.js is different"), `CLAUDE.md` (1 line). Zero component docs, zero Storybook.
- **Tests:** `src/__tests__/` has 4 files: `ChatModule.spec.tsx`, `agentClient.spec.ts`, `setup.ts`, `useAgentStore.spec.ts`. **Coverage: ~4%** of components.
- **E2E:** Playwright configured (`frontend/e2e/`, `frontend/tests/` exists) — consider adding visual regression for Win95 theme.

---

## Priority Actions (Top 5)

1. **Retire dead code** *(low effort, high clarity)* — delete `frontend/components/`, delete `frontend/styles/win95.css`, remove or adopt `@radix-ui/*` packages. ~10 min work, eliminates confusion.

2. **Promote the de facto palette to tokens** *(medium effort, highest leverage)* — expand `:root` with the 10–15 colors the codebase already uses consistently, plus `--font-*` and `--space-*` scales. Then **find-replace hex → var** in the top offenders (`#808080`, `#ffffff`, `#c0c0c0`, `#000080`). Cuts hardcoded values by ~70% in a single pass.

3. **Build `src/components/ui/` primitive layer** *(high effort, compounding payoff)* — start with `Button`, `IconButton`, `StatusBadge`, `Tabs`, `Select` on top of Radix. Replace usage in the three big modules (Review, QuickGenerate, Configure) first.

4. **Add focus-visible and active states** *(low effort, a11y win)* — one CSS pass across buttons, rows, icons. Unblocks keyboard users.

5. **Split the 500+ LoC modules** *(high effort)* — do this **after** primitives exist, so splitting produces small re-usable pieces instead of just moving code. Target: no file over 300 LoC.

---

## Quick fixes to do today

```bash
# 1. Remove dead folders & files
rm -rf frontend/components/          # empty legacy folders
rm     frontend/styles/win95.css     # duplicate, not imported
rmdir  frontend/src/components/ui 2>/dev/null || true  # re-create when needed

# 2. Confirm nothing broke
cd frontend && npm run typecheck && npm run test:unit
```

After that, open `src/styles/win95.css` and add the proposed token block at the top of `:root`. The find-replace pass can follow in a dedicated PR.
