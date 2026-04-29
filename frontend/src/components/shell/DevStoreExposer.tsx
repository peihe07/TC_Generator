"use client";

import { useEffect } from "react";
import { useBuilderDraftStore } from "../../store/useBuilderDraftStore";
import { useCommandPaletteStore } from "../../store/useCommandPaletteStore";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { useJobStore } from "../../store/useJobStore";
import { useWorkspaceSettingsStore } from "../../store/useWorkspaceSettingsStore";

// Non-production builds expose stores on window so Playwright can seed state
// via page.evaluate(). 不在 production 暴露，避免外洩內部狀態。
export default function DevStoreExposer() {
  useEffect(() => {
    if (process.env.NODE_ENV === "production") return;
    const w = window as unknown as Record<string, unknown>;
    w.__tcJobStore = useJobStore;
    w.__tcJobHistoryStore = useJobHistoryStore;
    w.__tcDraftStore = useBuilderDraftStore;
    w.__tcCommandPaletteStore = useCommandPaletteStore;
    w.__tcWorkspaceSettingsStore = useWorkspaceSettingsStore;
  }, []);
  return null;
}
