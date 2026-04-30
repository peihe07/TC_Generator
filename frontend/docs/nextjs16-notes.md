# Next.js 16 Notes (Project-Specific)

Source: `node_modules/next/dist/docs/`

## Critical changes vs older training data

### params / searchParams are Promises (since v15)
`page.tsx` and `layout.tsx` receive `params` / `searchParams` as `Promise`. Must `await`.

```tsx
// app/runs/[runId]/page.tsx
export default async function RunDetailPage({
  params,
}: {
  params: Promise<{ runId: string }>;
}) {
  const { runId } = await params;
  return <div>{runId}</div>;
}
```

Legacy synchronous access is removed. A codemod exists for migration.

### Root layout requires `<html>` and `<body>`
Standard. Already present in `app/layout.tsx`.

### File conventions in use
- `app/layout.tsx` — root layout (one per route segment)
- `app/page.tsx` — route page
- `app/(group)/...` — route groups (no URL segment)
- `app/[param]/...` — dynamic segment
- `app/loading.tsx`, `app/error.tsx`, `app/not-found.tsx` — UI states
- `app/template.tsx` — re-mounts on navigation (rarely needed)

### Fonts
Use `next/font/google` for zero-CLS font loading:

```tsx
import { Space_Mono } from "next/font/google";

const spaceMono = Space_Mono({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-space-mono",
});

<html lang="en" className={spaceMono.variable}>
```

### Tailwind v4
- Project uses `tailwindcss@^4` with `@tailwindcss/postcss`
- Recommended directive: `@import "tailwindcss";` (CSS-first config via `@theme`)
- Current `globals.css` still uses v3 `@tailwind base/components/utilities` — works through compatibility but should be migrated.

## Project-specific gotchas
- Legacy 98.css 與 `/legacy` 路由都已移除。`globals.css` 仍用 v3 `@tailwind` 指令，遇到 Tailwind v4 行為差異時優先檢查這裡。
- `body` 不再 `overflow: hidden`；workspace 滾動由 `AppShell` 內的容器負責。
- Stores 在 `src/store/`，每個都用 zustand + localStorage；測試前用 `setState` 重置 + `localStorage.clear()`。
