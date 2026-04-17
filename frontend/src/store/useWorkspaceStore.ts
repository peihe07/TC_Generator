import { create } from 'zustand';
import { useJobStore } from './useJobStore';
import { TcRow, GenerationConfig, JobLog, JobStats, JobMetadata } from '../lib/types';

// 工作區快照：對應 useJobStore 中可序列化的主要欄位
export interface WorkspaceSnapshot {
  jobMetadata: JobMetadata | null;
  tcRows: TcRow[];
  config: GenerationConfig;
  logs: JobLog[];
  stats: JobStats;
}

export interface Workspace {
  id: string;
  name: string;
  createdAt: number;
  updatedAt: number;
  snapshot: WorkspaceSnapshot;
}

interface WorkspaceStore {
  workspaces: Workspace[];
  activeId: string | null;
  loaded: boolean;

  loadFromStorage: () => void;
  saveCurrentAs: (name: string) => Workspace;
  overwriteActive: () => Workspace | null;
  loadWorkspace: (id: string) => void;
  deleteWorkspace: (id: string) => void;
  renameWorkspace: (id: string, name: string) => void;
  exportWorkspace: (id: string) => string | null;
  importWorkspace: (json: string) => Workspace;
}

const EXPORT_VERSION = 1;

const LS_KEY = 'tc-generator-workspaces';
const LS_ACTIVE_KEY = 'tc-generator-active-workspace';

function captureSnapshot(): WorkspaceSnapshot {
  const s = useJobStore.getState();
  return {
    jobMetadata: s.jobMetadata,
    tcRows: s.tcRows,
    config: s.config,
    logs: s.logs,
    stats: s.stats,
  };
}

function applySnapshot(snap: WorkspaceSnapshot) {
  const s = useJobStore.getState();
  s.setJobMetadata(snap.jobMetadata);
  s.setTcRows(snap.tcRows);
  s.updateConfig(snap.config);
  // logs / stats 透過 setState 直接覆寫（避免逐筆 append）
  useJobStore.setState({ logs: snap.logs, stats: snap.stats });
}

function persist(workspaces: Workspace[], activeId: string | null) {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(workspaces));
    if (activeId) localStorage.setItem(LS_ACTIVE_KEY, activeId);
    else localStorage.removeItem(LS_ACTIVE_KEY);
  } catch {
    // 容量不足或停用時忽略
  }
}

export const useWorkspaceStore = create<WorkspaceStore>((set, get) => ({
  workspaces: [],
  activeId: null,
  loaded: false,

  loadFromStorage: () => {
    if (typeof window === 'undefined') return;
    try {
      const raw = localStorage.getItem(LS_KEY);
      const activeId = localStorage.getItem(LS_ACTIVE_KEY);
      const workspaces: Workspace[] = raw ? JSON.parse(raw) : [];
      set({ workspaces, activeId, loaded: true });
    } catch {
      set({ workspaces: [], activeId: null, loaded: true });
    }
  },

  saveCurrentAs: (name) => {
    const ws: Workspace = {
      id: `ws-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`,
      name: name.trim() || 'Untitled',
      createdAt: Date.now(),
      updatedAt: Date.now(),
      snapshot: captureSnapshot(),
    };
    const next = [...get().workspaces, ws];
    persist(next, ws.id);
    set({ workspaces: next, activeId: ws.id });
    return ws;
  },

  overwriteActive: () => {
    const { activeId, workspaces } = get();
    if (!activeId) return null;
    const idx = workspaces.findIndex((w) => w.id === activeId);
    if (idx === -1) return null;
    const updated: Workspace = {
      ...workspaces[idx],
      snapshot: captureSnapshot(),
      updatedAt: Date.now(),
    };
    const next = [...workspaces];
    next[idx] = updated;
    persist(next, activeId);
    set({ workspaces: next });
    return updated;
  },

  loadWorkspace: (id) => {
    const ws = get().workspaces.find((w) => w.id === id);
    if (!ws) return;
    applySnapshot(ws.snapshot);
    persist(get().workspaces, id);
    set({ activeId: id });
  },

  deleteWorkspace: (id) => {
    const next = get().workspaces.filter((w) => w.id !== id);
    const nextActive = get().activeId === id ? null : get().activeId;
    persist(next, nextActive);
    set({ workspaces: next, activeId: nextActive });
  },

  renameWorkspace: (id, name) => {
    const next = get().workspaces.map((w) =>
      w.id === id ? { ...w, name: name.trim() || w.name, updatedAt: Date.now() } : w,
    );
    persist(next, get().activeId);
    set({ workspaces: next });
  },

  exportWorkspace: (id) => {
    const ws = get().workspaces.find((w) => w.id === id);
    if (!ws) return null;
    return JSON.stringify({ version: EXPORT_VERSION, workspace: ws }, null, 2);
  },

  importWorkspace: (json) => {
    const parsed = JSON.parse(json);
    if (!parsed || typeof parsed !== 'object') throw new Error('Invalid workspace file');
    const raw = parsed.workspace ?? parsed; // 接受裸 Workspace 或包裝過的格式
    if (!raw.snapshot || !raw.name) throw new Error('Workspace missing required fields');
    // 重新指派 id 與時間戳，避免覆蓋既有工作區
    const ws: Workspace = {
      id: `ws-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`,
      name: String(raw.name),
      createdAt: Date.now(),
      updatedAt: Date.now(),
      snapshot: raw.snapshot,
    };
    const next = [...get().workspaces, ws];
    persist(next, get().activeId);
    set({ workspaces: next });
    return ws;
  },
}));
