# TC Generator — Frontend Plan (Optimized Architecture)

## Tech Stack

| Category | Choice | Why |
| --- | --- | --- |
| Framework | Next.js 15 (App Router) + TypeScript | Modern SSR/CSR hybrid, high performance |
| Retro UI | 98.css + Radix UI Primitives | 98.css for look, Radix for robust logic (A11y/State) |
| State Management | **Zustand** | High performance, selective re-rendering, multi-store support |
| Data Fetching | **TanStack Query (React Query)** | Efficient caching, loading states, and SSE handling |
| Layout | Tailwind CSS v4 | Utility-first for fine-grained Win98 positioning |
| Icons | Remix Icon (`@remixicon/react`) | Comprehensive and consistent icon set |

---

## Design Concept: The "Virtual Desktop" OS

Instead of a traditional multi-page website, the app functions as a **Single Page Application (SPA) Desktop Environment**.

### Visual Style: Windows 95/98
- **Desktop**: Fullscreen teal (`#008080`) at `/`.
- **Dynamic Windows**: Functional modules (Upload, Review, etc.) open as draggable/resizable `AppWindow` components.
- **Taskbar**: Bottom bar for managing active windows, Start menu, and system clock.
- **Component Logic**: Use Radix UI (Tabs, Dialogs, Selects) wrapped in 98.css styles to ensure keyboard accessibility and stable UI logic.

---

## Optimized Directory Structure

```text
frontend/
├── src/
│   ├── store/                     # Zustand Stores
│   │   ├── useJobStore.ts         # TC Data, Config, Stats
│   │   └── useWindowStore.ts      # Active windows, Z-index, focus management
│   ├── hooks/
│   │   ├── usePythonAPI.ts        # TanStack Query wrappers for FastAPI calls
│   │   └── useSSE.ts              # Server-Sent Events for real-time generation logs
│   ├── components/
│   │   ├── system/                # OS-level components
│   │   │   ├── WindowManager.tsx  # Renders active windows from store
│   │   │   ├── AppWindow.tsx      # Draggable 98.css frame + Radix Dialog logic
│   │   │   ├── Taskbar.tsx        # Start button + Window tabs + Clock
│   │   │   └── Desktop.tsx        # Teal BG + Icon Grid
│   │   ├── ui/                    # Primitive 98.css components (Radix-powered)
│   │   │   ├── Button.tsx
│   │   │   ├── Tabs.tsx           # Radix Tabs + 98.css
│   │   │   ├── Dialog.tsx         # Radix Dialog + 98.css
│   │   │   └── TreeView.tsx
│   │   └── modules/               # Feature-specific window content
│   │       ├── upload/            # File upload logic
│   │       ├── configure/         # Spec matching & settings
│   │       ├── generate/          # Progress & live logs
│   │       ├── review/            # Diff viewer & validation sidebar
│   │       └── export/            # Download & options
│   ├── services/                  # API client (Axios/Fetch)
│   ├── lib/                       # Utils (diff-logic, constants, types)
│   └── styles/
│       └── win95.css              # Custom 98.css overrides & Tailwind layers
└── package.json
```

---

## Detailed State Specifications (Zustand)

### 1. `useWindowStore` (The OS Kernel)
Handles the lifecycle of windows on the desktop.

**State:**
- `windows: Map<WindowID, WindowState>`
  - `id`: Unique identifier (e.g., 'upload', 'review-1')
  - `title`: Window title string
  - `isOpen`: boolean
  - `isMinimized`: boolean
  - `zIndex`: number
  - `position`: `{ x, y }`
- `focusedWindowId: WindowID | null`

**Actions:**
- `openWindow(id, config)`: Creates or restores a window.
- `closeWindow(id)`: Removes window from state.
- `focusWindow(id)`: Brings window to front (increments Z-index).
- `minimizeWindow(id)`: Hides window but keeps it in taskbar.
- `updatePosition(id, pos)`: For draggability.

### 2. `useJobStore` (The Data Layer)
Stores the actual business data being processed.

**State:**
- `jobId: string | null`
- `files: { raw: File | null, parsed: boolean }`
- `tcRows: TcRow[]` (The core data array)
- `config: { model: string, batchSize: number, budget: number }`
- `logs: { timestamp: string, level: 'info'|'error', message: string }[]`
- `stats: { total: number, processed: number, currentCost: number }`

**Actions:**
- `setRows(rows)`: Update entire dataset.
- `updateRow(id, updates)`: Surgical update for single TC (after review).
- `appendLog(log)`: For real-time generation feed.
- `resetJob()`: Clear everything.

---

## Technical Implementations

### A. WindowManager & AppWindow Logic
The `WindowManager` will map over the `windows` store and render `AppWindow` components.
- **Draggability**: Use `react-draggable` on the title bar element.
- **Focus**: `onClick` anywhere in the window triggers `focusWindow(id)`.
- **Radix Integration**: `AppWindow` acts as a `Radix.Dialog.Content` if it's modal, or just a portal-rendered div for non-modal windows.

### B. Radix UI + 98.css Wrapper (Example: Tabs)
```tsx
// Wrap Radix Tabs with 98.css classes
<Tabs.Root className="tabs">
  <Tabs.List aria-label="Settings">
    <Tabs.Trigger className="tabs-tab" value="tab1">Grouping</Tabs.Trigger>
    <Tabs.Trigger className="tabs-tab" value="tab2">Matching</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content className="window-body" value="tab1">
    {/* Content */}
  </Tabs.Content>
</Tabs.Root>
```

### C. SSE (Server-Sent Events) Handling
- **Endpoint**: `/api/generate/stream?jobId=xxx`
- **Frontend**: A custom hook `useSSE` that:
  1. Opens `EventSource`.
  2. On `message`: updates `useJobStore` stats and appends to `logs`.
  3. On `complete`: triggers a system notification/dialog.
  4. Handles reconnection and error states gracefully.

---

## Module-Specific Detailed Specs

### 1. Upload Module
- **Validation**: Client-side check for `.xlsx` / `.pdf` headers.
- **Preview**: Show the first 5 rows of the uploaded Excel in a 98.css table before committing to the full parse.

### 2. Review Module (The "Diff Viewer")
- **Side-by-Side**: Left (Original Requirement) vs Right (Generated TC).
- **Highlighting**: Use a simple character-level diffing library to wrap changes in `<ins>` (green) and `<del>` (red) tags within the 98.css text area.
- **Batch Actions**: "Select All Passing" -> updates `status` in `useJobStore` for all rows with 0 critical errors.

### 3. Export Module
- **Configurable Output**: Checkboxes for which columns to include in the final Excel.
- **Progressive Download**: Backend generates the file, frontend receives a signed URL to trigger the native browser download.

---

## UI/UX Rules
- **Double-Click**: Required for desktop icons to open apps.
- **Active State**: Only the `focusedWindow` has the high-contrast navy blue title bar; others are gray.
- **Cursor**: Use the classic `wait` (hourglass) cursor during API calls.
- **Sound (Optional)**: Play classic Win95 `.wav` sounds for errors or completion (if enabled).

---

## Implementation Priority (Phase 1)

1.  **Project Foundation**:
    - Install `zustand`, `@tanstack/react-query`, `@radix-ui/react-*`, `react-draggable`.
    - Setup `useWindowStore` and the root `WindowManager`.
2.  **The Shell**:
    - Build `Desktop`, `Taskbar` (with Clock), and `StartMenu`.
    - Create the base `AppWindow` with minimize/close logic.
3.  **Data Flow**:
    - Build `useJobStore`.
    - Implement the **Upload** window as the first test case for data persistence.
