import { create } from 'zustand';

import { DEFAULT_WORKSPACE_ID, useWorkspaceStore } from './useWorkspaceStore';

// 單一 job 的歷史紀錄；留下足夠欄位讓 UI 顯示成本與 token 分佈
export type JobRecordKind =
  | 'generate'
  | 'quick'
  | 'group'
  | 'regenerate'
  | 'rerun'
  // Review module ValidationPanel「詢問 AI」呼叫 /api/review/suggest-fix。
  | 'suggest-fix'
  // Export 階段對缺 testSet 的 row 補跑 classify_test_sets。cost 為 0 時不記錄。
  | 'export';

export interface JobRecord {
  id: string;              // 後端 jobId 或前端 fallback id
  kind: JobRecordKind;
  model: string;
  startedAt: number;
  finishedAt: number;
  rowsTotal: number;
  rowsProcessed: number;
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  cacheCreationTokens: number;
  note?: string;
  /** Workspace tag (Phase C-S1). 舊紀錄缺失時視為 default。 */
  workspaceId?: string;
  /** Archive flag — hidden from Runs list by default; data preserved. */
  archived?: boolean;
}

interface JobHistoryStore {
  records: JobRecord[];
  loaded: boolean;

  loadFromStorage: () => void;
  appendRecord: (record: JobRecord) => void;
  clearHistory: () => void;
  totalCost: () => number;
  setArchived: (id: string, archived: boolean) => void;
  bulkSetArchived: (ids: string[], archived: boolean) => void;
}

const LS_KEY = 'tc-generator-job-history';
const MAX_RECORDS = 500;
const MAX_AGE_MS = 90 * 24 * 60 * 60 * 1000; // 保留 90 天

function persist(records: JobRecord[]) {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(records));
  } catch {
    // 容量不足或停用時忽略
  }
}

export const useJobHistoryStore = create<JobHistoryStore>((set, get) => ({
  records: [],
  loaded: false,

  loadFromStorage: () => {
    if (typeof window === 'undefined') return;
    try {
      const raw = localStorage.getItem(LS_KEY);
      const parsed: JobRecord[] = raw ? JSON.parse(raw) : [];
      // 開啟時執行 TTL 過濾，清掉超過 MAX_AGE_MS 的舊紀錄
      const cutoff = Date.now() - MAX_AGE_MS;
      const kept = parsed.filter((r) => (r.finishedAt ?? r.startedAt ?? 0) >= cutoff);
      if (kept.length !== parsed.length) persist(kept);
      set({ records: kept, loaded: true });
    } catch {
      set({ records: [], loaded: true });
    }
  },

  appendRecord: (record) => {
    // 自動帶上目前 workspace id（caller 沒指定的話）
    const tagged: JobRecord = {
      ...record,
      workspaceId:
        record.workspaceId ??
        useWorkspaceStore.getState().currentId ??
        DEFAULT_WORKSPACE_ID,
    };
    // 保留最新 MAX_RECORDS 筆，同時汰換 MAX_AGE_MS 之外的舊紀錄
    const cutoff = Date.now() - MAX_AGE_MS;
    const next = [tagged, ...get().records]
      .filter((r) => (r.finishedAt ?? r.startedAt ?? 0) >= cutoff)
      .slice(0, MAX_RECORDS);
    persist(next);
    set({ records: next });
  },

  clearHistory: () => {
    persist([]);
    set({ records: [] });
  },

  totalCost: () => get().records.reduce((sum, r) => sum + (r.cost || 0), 0),

  setArchived: (id, archived) => {
    const next = get().records.map((r) =>
      r.id === id ? { ...r, archived } : r,
    );
    persist(next);
    set({ records: next });
  },

  bulkSetArchived: (ids, archived) => {
    const ids_set = new Set(ids);
    const next = get().records.map((r) =>
      ids_set.has(r.id) ? { ...r, archived } : r,
    );
    persist(next);
    set({ records: next });
  },
}));

/** 依 workspace 過濾。舊紀錄 workspaceId 缺失視為 default workspace。 */
export function filterRecordsByWorkspace(
  records: JobRecord[],
  workspaceId: string,
): JobRecord[] {
  return records.filter(
    (r) => (r.workspaceId ?? DEFAULT_WORKSPACE_ID) === workspaceId,
  );
}
