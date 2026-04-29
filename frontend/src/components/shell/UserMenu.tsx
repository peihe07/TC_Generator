"use client";

import { RiUser3Line } from "@remixicon/react";

// Phase 1 placeholder
export default function UserMenu() {
  return (
    <button
      type="button"
      className="flex items-center justify-center w-9 h-9 rounded-full bg-white/10 hover:bg-white/15 text-[var(--color-papaya)] focus-ring transition-colors"
      aria-label="User menu"
    >
      <RiUser3Line size={18} />
    </button>
  );
}
