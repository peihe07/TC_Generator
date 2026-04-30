import { create } from "zustand";

const LS_KEY = "tc-generator-workspaces";
const DEFAULT_ID = "default";

export interface Workspace {
  id: string;
  name: string;
  createdAt: number;
}

interface WorkspaceStore {
  workspaces: Workspace[];
  currentId: string;
  loaded: boolean;
  loadFromStorage: () => void;
  switchWorkspace: (id: string) => void;
  createWorkspace: (name: string) => Workspace;
  renameWorkspace: (id: string, name: string) => void;
  removeWorkspace: (id: string) => void;
}

interface PersistedShape {
  workspaces: Workspace[];
  currentId: string;
}

function persist(state: PersistedShape) {
  if (typeof localStorage === "undefined") return;
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(state));
  } catch {
    /* quota / disabled */
  }
}

function defaultWorkspace(): Workspace {
  return { id: DEFAULT_ID, name: "Default", createdAt: Date.now() };
}

function generateId(): string {
  return `ws_${Date.now().toString(36)}_${Math.random()
    .toString(36)
    .slice(2, 8)}`;
}

function ensureDefault(state: PersistedShape): PersistedShape {
  if (state.workspaces.length === 0) {
    const ws = defaultWorkspace();
    return { workspaces: [ws], currentId: ws.id };
  }
  const known = new Set(state.workspaces.map((w) => w.id));
  return {
    workspaces: state.workspaces,
    currentId: known.has(state.currentId)
      ? state.currentId
      : state.workspaces[0].id,
  };
}

export const useWorkspaceStore = create<WorkspaceStore>((set, get) => ({
  workspaces: [defaultWorkspace()],
  currentId: DEFAULT_ID,
  loaded: false,

  loadFromStorage: () => {
    if (typeof localStorage === "undefined") {
      set({ loaded: true });
      return;
    }
    try {
      const raw = localStorage.getItem(LS_KEY);
      if (!raw) {
        const seed = ensureDefault({
          workspaces: [defaultWorkspace()],
          currentId: DEFAULT_ID,
        });
        persist(seed);
        set({ ...seed, loaded: true });
        return;
      }
      const parsed = JSON.parse(raw) as Partial<PersistedShape>;
      const fixed = ensureDefault({
        workspaces: Array.isArray(parsed.workspaces)
          ? parsed.workspaces.filter(
              (w): w is Workspace =>
                typeof w?.id === "string" && typeof w?.name === "string"
            )
          : [defaultWorkspace()],
        currentId:
          typeof parsed.currentId === "string"
            ? parsed.currentId
            : DEFAULT_ID,
      });
      persist(fixed);
      set({ ...fixed, loaded: true });
    } catch {
      const seed = ensureDefault({
        workspaces: [defaultWorkspace()],
        currentId: DEFAULT_ID,
      });
      persist(seed);
      set({ ...seed, loaded: true });
    }
  },

  switchWorkspace: (id) => {
    const cur = get();
    if (!cur.workspaces.some((w) => w.id === id)) return;
    const next = { workspaces: cur.workspaces, currentId: id };
    persist(next);
    set({ currentId: id });
  },

  createWorkspace: (name) => {
    const cur = get();
    const ws: Workspace = {
      id: generateId(),
      name: name.trim() || "Untitled",
      createdAt: Date.now(),
    };
    const next = {
      workspaces: [...cur.workspaces, ws],
      currentId: ws.id,
    };
    persist(next);
    set(next);
    return ws;
  },

  renameWorkspace: (id, name) => {
    const cur = get();
    const updated = cur.workspaces.map((w) =>
      w.id === id ? { ...w, name: name.trim() || w.name } : w
    );
    const next = { workspaces: updated, currentId: cur.currentId };
    persist(next);
    set({ workspaces: updated });
  },

  removeWorkspace: (id) => {
    const cur = get();
    if (cur.workspaces.length <= 1) return; // 至少留一個
    const updated = cur.workspaces.filter((w) => w.id !== id);
    const nextCurrent =
      cur.currentId === id ? updated[0].id : cur.currentId;
    const next = { workspaces: updated, currentId: nextCurrent };
    persist(next);
    set(next);
  },
}));

export const DEFAULT_WORKSPACE_ID = DEFAULT_ID;
