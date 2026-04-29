import { create } from "zustand";
import type { GenerationConfig } from "../lib/types";

const LS_KEY = "tc-generator-workspace-settings";

export interface WorkspaceSettings {
  defaultModel: GenerationConfig["model"];
  defaultBatchSize: number;
  defaultBudgetLimit: number;
  defaultCreditBalance: number;
  defaultStrictValidation: boolean;
}

const FALLBACK: WorkspaceSettings = {
  defaultModel: "gpt-5",
  defaultBatchSize: 5,
  defaultBudgetLimit: 10,
  defaultCreditBalance: 0,
  defaultStrictValidation: false,
};

interface WorkspaceSettingsStore {
  settings: WorkspaceSettings;
  loaded: boolean;
  loadFromStorage: () => void;
  update: (patch: Partial<WorkspaceSettings>) => void;
  reset: () => void;
}

function persist(settings: WorkspaceSettings) {
  if (typeof localStorage === "undefined") return;
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(settings));
  } catch {
    // ignore
  }
}

export const useWorkspaceSettingsStore = create<WorkspaceSettingsStore>(
  (set, get) => ({
    settings: { ...FALLBACK },
    loaded: false,

    loadFromStorage: () => {
      if (typeof localStorage === "undefined") {
        set({ loaded: true });
        return;
      }
      try {
        const raw = localStorage.getItem(LS_KEY);
        if (raw) {
          const parsed = JSON.parse(raw) as Partial<WorkspaceSettings>;
          set({
            settings: { ...FALLBACK, ...parsed },
            loaded: true,
          });
        } else {
          set({ loaded: true });
        }
      } catch {
        set({ loaded: true });
      }
    },

    update: (patch) => {
      const next = { ...get().settings, ...patch };
      persist(next);
      set({ settings: next });
    },

    reset: () => {
      persist(FALLBACK);
      set({ settings: { ...FALLBACK } });
    },
  })
);
