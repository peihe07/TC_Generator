# TC Generator — Frontend Plan

## Tech Stack

| Category | Choice | Why |
| --- | --- | --- |
| Framework | Next.js 15 (App Router) + TypeScript | SSR, file-based routing |
| Retro UI | 98.css | Pure CSS, zero JS dependency, Win95/98 look |
| Layout | Tailwind CSS | Utility-first layout, grid, spacing |
| Icons | Remix Icon (`@remixicon/react`) | https://remixicon.com/ |
| State | React Context + JSON job file | No database needed |

---

## Design Concept

### Visual Style: Windows 95/98

- **Desktop background**: Classic teal (`#008080`) fullscreen
- **Pages as Windows**: Each page renders inside a draggable 98.css `window` frame
- **Taskbar**: Bottom bar with Start button, page tabs, clock
- **3D elements**: Raised buttons, sunken inputs, beveled borders
- **Font**: `"Pixelated MS Sans Serif"`, fallback to system monospace
- **Dialogs**: Classic modal dialogs for errors and confirmations
- **No emoji anywhere** — use Remix Icon for all iconography

### Color Palette

| Element | Color | Hex |
| --- | --- | --- |
| Desktop background | Teal | `#008080` |
| Title bar (active) | Navy blue gradient | `#000080` to `#1084D0` |
| Title bar (inactive) | Gray | `#808080` |
| Window background | Light gray | `#C0C0C0` |
| Button face | Light gray | `#C0C0C0` |
| Text | Black | `#000000` |
| Selected text bg | Navy | `#000080` |
| Selected text fg | White | `#FFFFFF` |

---

## Directory Structure

```
frontend/
├── public/
│   └── icons/                     # Desktop shortcut icons
├── src/
│   ├── app/
│   │   ├── layout.tsx             # Root layout: 98.css + Tailwind + desktop bg
│   │   ├── page.tsx               # Desktop with app shortcut icon
│   │   ├── upload/page.tsx        # Upload page
│   │   ├── configure/page.tsx     # Configure page
│   │   ├── generate/page.tsx      # Generate page
│   │   ├── review/page.tsx        # Review page
│   │   ├── export/page.tsx        # Export page
│   │   └── api/                   # API routes (call Python backend)
│   │       ├── parse/route.ts
│   │       ├── group/route.ts
│   │       ├── match/route.ts
│   │       ├── generate/route.ts
│   │       ├── validate/route.ts
│   │       └── export/route.ts
│   ├── components/
│   │   ├── desktop/
│   │   │   ├── Desktop.tsx        # Teal background + icon grid
│   │   │   ├── DesktopIcon.tsx    # Double-click to open app
│   │   │   ├── Taskbar.tsx        # Bottom bar: Start + tabs + clock
│   │   │   └── StartMenu.tsx      # Navigation menu
│   │   ├── window/
│   │   │   ├── AppWindow.tsx      # 98.css window frame + title bar
│   │   │   ├── TitleBar.tsx       # Title text + minimize/maximize/close
│   │   │   └── StatusBar.tsx      # Window bottom status info
│   │   ├── retro/
│   │   │   ├── RetroButton.tsx    # 98.css button
│   │   │   ├── RetroProgress.tsx  # Segmented progress bar
│   │   │   ├── RetroTable.tsx     # Sunken-border table
│   │   │   ├── RetroTabs.tsx      # 98.css tab control
│   │   │   ├── RetroTreeView.tsx  # Tree view for Test Set groups
│   │   │   ├── RetroDialog.tsx    # Modal dialog (error/confirm)
│   │   │   ├── RetroSelect.tsx    # Dropdown select
│   │   │   └── RetroCheckbox.tsx  # Checkbox with label
│   │   ├── upload/
│   │   │   ├── FileUploadSlot.tsx # Drag-and-drop file slot
│   │   │   └── MetadataCard.tsx   # Detected file metadata display
│   │   ├── review/
│   │   │   ├── TcRow.tsx          # Expandable TC row (original vs generated)
│   │   │   ├── DiffView.tsx       # Side-by-side diff highlight
│   │   │   ├── ValidationPanel.tsx# Sidebar: red/yellow/green per check
│   │   │   └── BulkActions.tsx    # Accept all / Reject / Export buttons
│   │   └── generate/
│   │       ├── GenerateLog.tsx    # Live log textarea
│   │       └── CostDisplay.tsx    # Running token + cost counter
│   ├── hooks/
│   │   ├── useJob.ts              # Job state context
│   │   └── usePython.ts           # Call Python backend via API routes
│   ├── lib/
│   │   ├── types.ts               # TypeScript types (Job, Row, Config, etc.)
│   │   └── constants.ts           # Shared constants
│   └── styles/
│       └── win95.css              # Custom overrides on top of 98.css
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.ts
```

---

## Pages Detail

### Page 1: Upload

**Window title**: TC Generator - Upload Files
**Title bar icon**: `ri-folder-upload-line`

**Content**:
- Three file upload slots styled as sunken fieldsets:
  - Slot A: TC Specification xlsx (required) — `ri-file-excel-2-line`
  - Slot B: SYS1 Spec xlsx (optional) — `ri-file-search-line`
  - Slot C: Spec document PDF/DOCX/XLSX (optional) — `ri-file-text-line`
- Each slot: drag-and-drop area with dashed border, click to browse
- After upload: metadata summary in a sunken group box:
  - Project name, Test Group, row count, column fill status
  - Slot C: detected format + preview snippet
- Bottom: [Next >>] button (disabled until Slot A uploaded)

### Page 2: Configure

**Window title**: TC Generator - Configure
**Title bar icon**: `ri-settings-3-line`

**Content** (tabbed interface):
- **Tab 1: Test Set Grouping**
  - Tree view showing AI-suggested groups
  - Drag-and-drop to reassign TCs between groups
  - Right-click context menu: rename / merge / split
- **Tab 2: Spec Matching**
  - Table: Req ID | Test Item | Matched Spec | Match Type
  - Layer 1 (exact) shown in green, Layer 2 (AI) in yellow
  - Click to manually override match
- **Tab 3: Options**
  - Generation scope: checkboxes per column (I rewrite, J, K, L, M, N, P, Q)
  - Model: radio buttons (Sonnet / Haiku)
  - Batch size: dropdown (1 / 5 / 10)
  - Budget limit: text input with USD label
- Bottom: [<< Back] [Start Generate >>]

### Page 3: Generate

**Window title**: TC Generator - Generate
**Title bar icon**: `ri-play-circle-line`

**Content**:
- Top: progress bar (segmented Win95 style) + "X / N TCs"
- Center: log textarea (monospace, sunken border, auto-scroll)
  - Each line: `[OK] newR1L-DMR-001` or `[FAIL] newR1L-DMR-005: parse error`
- Right panel: cost display group box
  - Input tokens / Output tokens
  - Running cost in USD
  - Budget remaining bar
- Bottom: [Pause] [Resume] [Cancel] buttons
- When done: auto-transition dialog "Generation complete. Review results?"

### Page 4: Review

**Window title**: TC Generator - Review
**Title bar icon**: `ri-file-list-3-line`

**Content**:
- Toolbar: filter dropdowns (validation status / Test Set / review status)
- Main table (sunken border, alternating row colors):
  - Columns: TC ID | Req ID | Status | Actions
  - Click row to expand: original vs generated side-by-side
  - Diff highlighting (green = added, red = removed)
- Per-row action buttons:
  - Accept: `ri-check-line` (green)
  - Edit: `ri-edit-line` (blue) — opens inline editor
  - Reject: `ri-close-line` (red) — mark for regeneration
  - Flag: `ri-flag-line` (orange) — needs human attention
- Right sidebar: Validation panel
  - Red items: critical violations
  - Yellow items: warnings
  - Green: all passed
  - Icon per severity: `ri-error-warning-line` / `ri-alert-line` / `ri-checkbox-circle-line`
- Bottom toolbar: [Accept All Passing] [Regenerate Rejected] [Export Accepted >>]

### Page 5: Export

**Window title**: TC Generator - Export
**Title bar icon**: `ri-download-2-line`

**Content** (group boxes):
- **Export Scope** (radio buttons):
  - All generated
  - Accepted only
  - By Test Set (checkboxes per set)
- **Output Format** (radio buttons):
  - Create new file (`{input}_generated.xlsx`)
  - Overwrite original
- **Include Columns** (checkboxes):
  - TC ID, Test Group, Test Set, Test Item rewrite, Pre-Conditions, etc.
- **Framework Sheet** (checkbox):
  - Populate Test Case Framework sheet
- Bottom: [<< Back to Review] [Export] button
- After export: download dialog with file link + summary stats

---

## Navigation Flow

```
Desktop (teal background)
  |
  +-- Double-click "TC Generator" icon
  |
  +-- Taskbar appears at bottom
  |     |
  |     +-- [Start] button --> Start menu (all pages listed)
  |     +-- [Upload] [Configure] [Generate] [Review] [Export] tabs
  |     +-- Clock display (right side)
  |
  +-- Window opens with current page content
        |
        Upload --> Configure --> Generate --> Review --> Export
        [Next>>]  [Start>>]    [auto]      [Export>>]  [Download]
```

---

## Shared Components Behavior

### AppWindow

- 98.css `window` class with custom title bar
- Title bar: icon (Remix) + title text + [ _ ] [ [] ] [ X ] buttons
- Minimize: collapse to taskbar
- Maximize: fill desktop area (exclude taskbar)
- Close: return to desktop / confirm dialog if unsaved
- Draggable by title bar (optional, for desktop feel)
- Content area scrollable with 98.css sunken border

### Taskbar

- Fixed bottom, 98.css raised border
- Left: Start button with `ri-windows-line` icon
- Center: one tab per open page (active = pressed state)
- Right: clock + `ri-time-line` icon

### RetroDialog

- Modal overlay (semi-transparent black)
- 98.css window style, centered
- Icon variants:
  - Error: `ri-error-warning-fill` (red)
  - Warning: `ri-alert-fill` (yellow)
  - Info: `ri-information-fill` (blue)
  - Success: `ri-checkbox-circle-fill` (green)
- Buttons: [OK] / [OK] [Cancel] / [Yes] [No] [Cancel]

---

## State Management

Single React Context (`JobContext`) holding the job JSON:

```typescript
interface Job {
  jobId: string;
  project: string;
  testGroup: string;
  files: { tcXlsx: File | null; sys1Xlsx: File | null; specDoc: File | null };
  config: { model: string; batchSize: number; budget: number; columns: string[] };
  framework: Record<string, string[]>;
  specIndex: Record<string, SpecEntry>;
  rows: TcRow[];
  stats: { total: number; generated: number; accepted: number; rejected: number; flagged: number };
  currentPage: "upload" | "configure" | "generate" | "review" | "export";
}
```

No database. Job state persisted to `localStorage` for session recovery.

---

## API Routes (Next.js -> Python Backend)

| Route | Method | Python Script | Purpose |
| --- | --- | --- | --- |
| `/api/parse` | POST | `parser.py` | Parse uploaded xlsx, return metadata + rows |
| `/api/group` | POST | `grouper.py` | AI cluster Test Items into Test Sets |
| `/api/match` | POST | `spec_matcher.py` | Match spec references (Layer 1 + 2) |
| `/api/generate` | POST | `generator.py` | Generate TCs, stream progress via SSE |
| `/api/validate` | POST | `validator.py` | Validate generated rows |
| `/api/export` | POST | `writer.py` | Write xlsx, return download URL |

All routes call Python via `child_process.exec` or HTTP to a local Flask/FastAPI server.

---

## Implementation Order

1. Project setup: `create-next-app` + 98.css + Tailwind + Remix Icon
2. Shared components: Desktop, AppWindow, Taskbar, RetroButton, RetroDialog
3. Upload page (most independent, validates file handling)
4. Configure page (tabs + tree view + table)
5. Generate page (progress bar + SSE log)
6. Review page (most complex: table + diff + validation sidebar)
7. Export page (simplest UI)
8. API routes integration (Phase 12)
