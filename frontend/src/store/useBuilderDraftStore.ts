import { create } from "zustand";
import type { BuilderStep } from "../components/builder/types";
import { DEFAULT_WORKSPACE_ID, useWorkspaceStore } from "./useWorkspaceStore";

const LS_KEY = "tc-generator-builder-draft";

export interface BuilderDraft {
  id: string;
  createdAt: number;
  updatedAt: number;
  currentStep: BuilderStep;
  /** Workspace tag (Phase C-S1)，draft 開新時抓當前 workspace。 */
  workspaceId?: string;
  /** 由 Run Detail 的 Rerun / Edit & Rerun 帶過來的來源 runId */
  sourceRunId?: string;
  /** rerun mode：'rerun' 直接執行同樣設定；'edit' 允許在 builder 中調整再執行 */
  rerunMode?: "rerun" | "edit";
  data?: {
    datasetId?: string;
    fileName?: string;
    rowCount?: number;
  };
  configure?: {
    templateId?: string;
    overrides?: Record<string, unknown>;
  };
  validation?: {
    okAt?: number;
    issueCount?: number;
  };
  // 每個 step 是否「完成」的標記，用來解 stepper guards
  completed?: Partial<Record<BuilderStep, boolean>>;
}

interface DraftStore {
  draft: BuilderDraft | null;
  loaded: boolean;
  loadFromStorage: () => void;
  startNew: () => BuilderDraft;
  update: (patch: Partial<BuilderDraft>) => void;
  markStepComplete: (step: BuilderStep, complete?: boolean) => void;
  clear: () => void;
}

function persist(draft: BuilderDraft | null) {
  if (typeof localStorage === "undefined") return;
  try {
    if (draft) localStorage.setItem(LS_KEY, JSON.stringify(draft));
    else localStorage.removeItem(LS_KEY);
  } catch {
    // ignore quota / disabled
  }
}

function generateId(): string {
  return `draft_${Date.now().toString(36)}_${Math.random()
    .toString(36)
    .slice(2, 8)}`;
}

export const useBuilderDraftStore = create<DraftStore>((set, get) => ({
  draft: null,
  loaded: false,

  loadFromStorage: () => {
    if (typeof localStorage === "undefined") {
      set({ loaded: true });
      return;
    }
    try {
      const raw = localStorage.getItem(LS_KEY);
      const draft = raw ? (JSON.parse(raw) as BuilderDraft) : null;
      set({ draft, loaded: true });
    } catch {
      set({ draft: null, loaded: true });
    }
  },

  startNew: () => {
    const now = Date.now();
    const draft: BuilderDraft = {
      id: generateId(),
      createdAt: now,
      updatedAt: now,
      currentStep: "data",
      workspaceId:
        useWorkspaceStore.getState().currentId ?? DEFAULT_WORKSPACE_ID,
      completed: {},
    };
    persist(draft);
    set({ draft, loaded: true });
    return draft;
  },

  update: (patch) => {
    const cur = get().draft;
    if (!cur) return;
    const next: BuilderDraft = {
      ...cur,
      ...patch,
      updatedAt: Date.now(),
    };
    persist(next);
    set({ draft: next });
  },

  markStepComplete: (step, complete = true) => {
    const cur = get().draft;
    if (!cur) return;
    const completed = { ...(cur.completed ?? {}), [step]: complete };
    const next: BuilderDraft = {
      ...cur,
      completed,
      updatedAt: Date.now(),
    };
    persist(next);
    set({ draft: next });
  },

  clear: () => {
    persist(null);
    set({ draft: null });
  },
}));
