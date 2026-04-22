import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { TcRow, GenerationConfig, JobLog, JobStats, JobMetadata, UsageSummary } from '../lib/types';

interface JobStore {
  jobMetadata: JobMetadata | null;
  tcRows: TcRow[];
  config: GenerationConfig;
  logs: JobLog[];
  stats: JobStats;
  isProcessing: boolean;
  isRegenerating: boolean;

  // Actions
  setJobMetadata: (data: JobMetadata | null) => void;
  setTcRows: (rows: TcRow[]) => void;
  updateTcRow: (id: string, updates: Partial<TcRow>) => void;
  // 插入一個新的 TC row，接在 parentId 所屬列後面（用於 AI 把一個 req 拆成多筆 TC 時）。
  addTcRowAfter: (parentId: string, row: TcRow) => void;
  deleteTcRows: (ids: string[]) => void;
  renumberTcRows: () => void;
  setAwaitingApply: (id: string, data: TcRow['awaitingApply']) => void;
  applyRegenerated: (id: string, fields: ('steps' | 'expectedResults' | 'preConditions' | 'inputTestData')[]) => void;
  clearAwaitingApply: (id: string) => void;
  updateConfig: (updates: Partial<GenerationConfig>) => void;
  appendLog: (log: JobLog) => void;
  updateStats: (updates: Partial<JobStats>) => void;
  accumulateStats: (usage: UsageSummary) => void;
  setProcessing: (status: boolean) => void;
  setRegenerating: (status: boolean) => void;
  resetJob: () => void;
}

const DEFAULT_CONFIG: GenerationConfig = {
  model: 'gpt-5.4-mini',
  batchSize: 5,
  budgetLimit: 10,
  creditBalance: 0,
  strictValidation: false,
  targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
};

const DEFAULT_STATS: JobStats = {
  total: 0,
  processed: 0,
  success: 0,
  fail: 0,
  cost: 0,
  inputTokens: 0,
  outputTokens: 0,
  cacheCreationTokens: 0,
  cacheReadTokens: 0,
};

function renumberRows(rows: TcRow[]): TcRow[] {
  return rows.map((row, index) => ({
    ...row,
    id: `TC-${String(index + 1).padStart(3, '0')}`,
  }));
}

export const useJobStore = create<JobStore>()(persist((set) => ({
  jobMetadata: null,
  tcRows: [],
  config: DEFAULT_CONFIG,
  logs: [],
  stats: DEFAULT_STATS,
  isProcessing: false,
  isRegenerating: false,

  setJobMetadata: (data) => set({ jobMetadata: data }),
  setTcRows: (rows) => set({ tcRows: rows }),

  updateTcRow: (id, updates) => set((state) => ({
    tcRows: state.tcRows.map((row) =>
      row.id === id ? { ...row, ...updates } : row
    ),
  })),

  addTcRowAfter: (parentId, row) => set((state) => {
    // 若已存在相同 id 直接更新，避免重送事件時重複插入。
    if (state.tcRows.some((r) => r.id === row.id)) {
      return {
        tcRows: state.tcRows.map((r) => (r.id === row.id ? { ...r, ...row } : r)),
      };
    }
    const parentIdx = state.tcRows.findIndex((r) => r.id === parentId);
    if (parentIdx < 0) {
      // 找不到 parent：補到最後，至少不會遺失 TC。
      return { tcRows: [...state.tcRows, row] };
    }
    // 插在同 parent 所有既有子列的最後面，保持順序。
    let insertAt = parentIdx + 1;
    while (
      insertAt < state.tcRows.length &&
      state.tcRows[insertAt].id.startsWith(`${parentId}__tc`)
    ) {
      insertAt += 1;
    }
    return {
      tcRows: [
        ...state.tcRows.slice(0, insertAt),
        row,
        ...state.tcRows.slice(insertAt),
      ],
    };
  }),

  deleteTcRows: (ids) => set((state) => {
    const keep = state.tcRows.filter((row) => !ids.includes(row.id));
    // 刪掉某些 sub-TC 後，同 parent 剩下的兄弟列要重新編號 subIndex／tcCount，
    // 避免 badge 顯示「TC 3/3」但實際只剩 2 筆、或 tcCount 不一致。
    const byParent = new Map<string, number[]>();
    keep.forEach((row, idx) => {
      const parent = row.splitDecision?.parentId ?? row.id;
      if (!byParent.has(parent)) byParent.set(parent, []);
      byParent.get(parent)!.push(idx);
    });
    return {
      tcRows: keep.map((row, idx) => {
        const parentId = row.splitDecision?.parentId ?? row.id;
        const siblings = byParent.get(parentId);
        if (!siblings || siblings.length <= 1 || !row.splitDecision) return row;
        const newSubIdx = siblings.indexOf(idx);
        if (newSubIdx < 0) return row;
        return {
          ...row,
          splitDecision: {
            ...row.splitDecision,
            subIndex: newSubIdx,
            tcCount: siblings.length,
          },
        };
      }),
    };
  }),

  renumberTcRows: () => set((state) => ({
    tcRows: renumberRows(state.tcRows),
  })),

  setAwaitingApply: (id, data) => set((state) => ({
    tcRows: state.tcRows.map((row) =>
      row.id === id ? { ...row, awaitingApply: data } : row
    ),
  })),

  applyRegenerated: (id, fields) => set((state) => ({
    tcRows: renumberRows(state.tcRows.map((row) => {
      if (row.id !== id || !row.awaitingApply) return row;
      const updates: Partial<TcRow> = {};
      if (fields.includes('steps')) updates.steps = row.awaitingApply.steps;
      if (fields.includes('expectedResults')) updates.expectedResults = row.awaitingApply.expectedResults;
      if (fields.includes('preConditions')) updates.preConditions = row.awaitingApply.preConditions;
      if (fields.includes('inputTestData')) updates.inputTestData = row.awaitingApply.inputTestData;
      return { ...row, ...updates, awaitingApply: undefined, status: 'reviewing' };
    })),
  })),

  clearAwaitingApply: (id) => set((state) => ({
    tcRows: state.tcRows.map((row) =>
      row.id === id ? { ...row, awaitingApply: undefined } : row
    ),
  })),

  updateConfig: (updates) => set((state) => ({
    config: { ...state.config, ...updates },
  })),

  appendLog: (log) => set((state) => ({
    logs: [log, ...state.logs].slice(0, 1000),
  })),

  updateStats: (updates) => set((state) => ({
    stats: { ...state.stats, ...updates },
  })),

  accumulateStats: (usage) => set((state) => ({
    stats: {
      ...state.stats,
      cost: Number((state.stats.cost + usage.cost).toFixed(4)),
      inputTokens: state.stats.inputTokens + usage.inputTokens,
      outputTokens: state.stats.outputTokens + usage.outputTokens,
      cacheCreationTokens: state.stats.cacheCreationTokens + usage.cacheCreationTokens,
      cacheReadTokens: state.stats.cacheReadTokens + usage.cacheReadTokens,
    },
  })),

  setProcessing: (status) => set({ isProcessing: status }),
  setRegenerating: (status) => set({ isRegenerating: status }),

  resetJob: () => set((state) => ({
    jobMetadata: null,
    tcRows: [],
    logs: [],
    // 累積 API usage（tokens / cost）跨 job 保留；只有每筆 job 的進度欄位歸零。
    stats: {
      ...state.stats,
      total: 0,
      processed: 0,
      success: 0,
      fail: 0,
    },
    isProcessing: false,
    isRegenerating: false,
  })),
}), {
  name: 'tc-job-session',
  storage: createJSONStorage(() => localStorage),
  // 只持久化資料型欄位；瞬態旗標與 logs 不跨 session 保留
  partialize: (state) => ({
    jobMetadata: state.jobMetadata,
    tcRows: state.tcRows,
    config: state.config,
    stats: state.stats,
  }),
  version: 2,
  migrate: (persistedState: unknown) => {
    const state = persistedState as { config?: Partial<GenerationConfig> } | undefined;
    if (!state) return state;
    const model = state.config?.model;
    if (model === 'gpt-4.1' || model === 'gpt-5.4' || model === undefined) {
      return {
        ...state,
        config: {
          ...state.config,
          model: 'gpt-5.4-mini',
        },
      };
    }
    return state;
  },
}));

// Expose store synchronously in non-production for Playwright E2E tests
if (typeof window !== 'undefined' && process.env.NODE_ENV !== 'production') {
  (window as unknown as Record<string, unknown>).__tcJobStore = useJobStore;
}
