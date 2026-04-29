"use client";

import { RiBox3Line, RiArrowDownSLine } from "@remixicon/react";

// Phase 1 placeholder：之後接 useWorkspaceStore
export default function WorkspaceSwitcher() {
  return (
    <button
      type="button"
      className="flex items-center gap-2 px-3 py-2 rounded-md text-[var(--color-papaya)] hover:bg-white/10 focus-ring transition-colors"
    >
      <RiBox3Line size={18} style={{ color: "var(--color-tangerine)" }} />
      <span className="text-sm font-bold tracking-tight">TC Generator</span>
      <RiArrowDownSLine size={16} className="opacity-70" />
    </button>
  );
}
