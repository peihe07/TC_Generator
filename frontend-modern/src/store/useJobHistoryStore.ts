import { create } from 'zustand';

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
}

interface JobHistoryStore {
  records: JobRecord[];
  loaded: boolean;

  loadFromStorage: () => void;
  appendRecord: (record: JobRecord) => void;
  clearHistory: () => void;
  totalCost: () => number;
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
    // 保留最新 MAX_RECORDS 筆，同時汰換 MAX_AGE_MS 之外的舊紀錄
    const cutoff = Date.now() - MAX_AGE_MS;
    const next = [record, ...get().records]
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
}));
