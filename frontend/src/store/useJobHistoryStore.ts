import { create } from 'zustand';

// 單一 job 的歷史紀錄；留下足夠欄位讓 UI 顯示成本與 token 分佈
export interface JobRecord {
  id: string;              // 後端 jobId 或前端 fallback id
  kind: 'generate' | 'quick' | 'regenerate';
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
      set({ records: raw ? JSON.parse(raw) : [], loaded: true });
    } catch {
      set({ records: [], loaded: true });
    }
  },

  appendRecord: (record) => {
    const next = [record, ...get().records].slice(0, MAX_RECORDS);
    persist(next);
    set({ records: next });
  },

  clearHistory: () => {
    persist([]);
    set({ records: [] });
  },

  totalCost: () => get().records.reduce((sum, r) => sum + (r.cost || 0), 0),
}));
