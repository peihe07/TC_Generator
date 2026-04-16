# TC Generator — Frontend Plan (Optimized Architecture)

## Tech Stack

| Category | Choice | Why |
| --- | --- | --- |
| Framework | Next.js 15 (App Router) + TypeScript | Modern SSR/CSR hybrid, high performance |
| Retro UI | 98.css + Radix UI Primitives | 98.css for look, Radix for robust logic (A11y/State) |
| State Management | **Zustand** | High performance, selective re-rendering, multi-store support |
| Data Fetching | **TanStack Query (React Query)** | Efficient caching, loading states, and SSE handling |
| Layout | Tailwind CSS v4 | Utility-first for fine-grained Win98 positioning |
| Icons | Remix Icon (`@remixicon/react`) | **Required for high-visibility O/X and window controls** |

---

## Design Concept: The "Virtual Desktop" OS

Instead of a traditional multi-page website, the app functions as a **Single Page Application (SPA) Desktop Environment**.

### Visual Style: Windows 95/98
- **Desktop**: Fullscreen teal (`#008080`) at `/`.
- **Dynamic Windows**: Functional modules (Upload, Review, etc.) open as draggable/resizable `AppWindow` components.
- **Taskbar**: Bottom bar for managing active windows, Start menu, and system clock.

---

## Technical Implementations

### A. WindowManager & AppWindow Logic
- **Draggability & Resizing**:
  - Use `react-draggable` on the title bar.
  - Use `react-resizable` for window edges.
  - **Auto-Adapt**: Window body must use `display: flex` with `overflow: auto`.
- **Title Bar Controls (O/X Visibility)**:
  - **Replace default 98.css icons with SVG Remix Icons** (`ri-close-line`, `ri-subtract-line`, `ri-checkbox-indeterminate-line`).
  - Increase button size to **18x18px** min for title bar controls.
  - Use `font-weight: bold` for icon strokes to ensure they are visible on high-DPI screens.

### B. Font & Accessibility (High-DPI Support)
- **Global Scaling**: Set base font size to `14px` or `16px` in `win95.css`.
- **Button Sizing**:
  - Increase default button padding (`py-1.5 px-3`).
  - Action buttons (Accept/Reject) must have explicit colors:
    - **Accept (O)**: Green icon (`text-green-700`) + high contrast background.
    - **Reject (X)**: Red icon (`text-red-700`) + high contrast background.
- **Font Rendering**: Use `image-rendering: pixelated` and `text-rendering: optimizeLegibility`.

### C. Radix UI + 98.css Wrapper (Example: Tabs)
```tsx
// Ensure tabs and buttons have enough height for visible text/icons
<Tabs.Trigger className="tabs-tab min-h-[28px] text-base" value="tab1">
  <RiSettings3Line className="size-4 mr-1" /> Grouping
</Tabs.Trigger>
```

---

## Module-Specific Detailed Specs

### 1. Upload Module
- **Validation**: Client-side check for `.xlsx` / `.pdf` headers.
- **Preview**: Show the first 5 rows of the uploaded Excel in a 98.css table.

### 2. Review Module (The "Diff Viewer")
- **High-Visibility Actions**:
  - Use large, bold icons for row actions.
  - **Accept (O)**: `ri-check-fill` (Circle check).
  - **Reject (X)**: `ri-close-fill` (Bold X).
- **Flex-Layout**: Table and Diff areas must expand with window size.

---

## UI/UX Rules
- **Double-Click**: Required for desktop icons to open apps.
- **Resizable Windows**: All functional windows (Review, Generate) must be resizable.
- **High Contrast**: Active title bars use Navy gradient, Inactive use Dark Gray. Symbols (O/X) must remain black/white with high contrast against their button backgrounds.

---

## Implementation Status (Updated: 2026-04-16)

### Phase 1: Foundation (In Progress)
- [x] **Project Setup**: Next.js 15, Tailwind CSS, 98.css.
- [x] **Core Libraries**: Zustand, TanStack Query, Radix UI, Draggable, Resizable, Remix Icon.
- [x] **Store Implementation**:
  - `useWindowStore`: Window lifecycle, positioning, and sizing.
  - `useJobStore`: Data management for TC rows, logs, and stats.
- [x] **Global Styles**: Custom `win95.css` with font-size (16px) and button visibility overrides.
- [ ] **System Components**:
  - [ ] `AppWindow`: Draggable/Resizable container with SVG controls.
  - [ ] `WindowManager`: Root window renderer.
  - [ ] `Taskbar`: Window switcher and clock.
- [ ] **Modules**:
  - [ ] `Upload`: File selection and preview.

---

## Implementation Priority (Phase 1)

1.  **Project Foundation**:
    - Install `zustand`, `@tanstack/react-query`, `@radix-ui/react-*`, `react-draggable`, `react-resizable`, `@remixicon/react`.
2.  **The Shell & Scaling**:
    - Build `win95.css` with font-size and button-size overrides.
    - Create `AppWindow` with **SVG-based title bar buttons**.
3.  **Data Flow**:
    - Build `useJobStore` and the **Upload** module.
