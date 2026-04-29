"use client";

import { RiSearchLine } from "@remixicon/react";
import { useCommandPaletteStore } from "../../store/useCommandPaletteStore";

export default function GlobalSearch() {
  const setOpen = useCommandPaletteStore((s) => s.setOpen);
  return (
    <button
      type="button"
      onClick={() => setOpen(true)}
      className="flex items-center gap-2 px-3 py-2 rounded-md bg-white/10 hover:bg-white/15 text-[var(--color-papaya)]/80 focus-ring transition-colors min-w-[220px]"
    >
      <RiSearchLine size={16} />
      <span className="text-sm flex-1 text-left">Search...</span>
      <span className="text-xs opacity-60 px-1.5 py-0.5 rounded bg-white/10">
        ⌘K
      </span>
    </button>
  );
}
