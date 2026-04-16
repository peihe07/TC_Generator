import { create } from 'zustand';
import { TcRow, GenerationConfig, JobLog, JobStats, JobMetadata } from '../lib/types';

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
  deleteTcRows: (ids: string[]) => void;
  setPendingRegenerated: (id: string, data: TcRow['pendingRegenerated']) => void;
  applyRegenerated: (id: string, fields: ('steps' | 'expectedResults' | 'preConditions')[]) => void;
  clearPendingRegenerated: (id: string) => void;
  updateConfig: (updates: Partial<GenerationConfig>) => void;
  appendLog: (log: JobLog) => void;
  updateStats: (updates: Partial<JobStats>) => void;
  setProcessing: (status: boolean) => void;
  setRegenerating: (status: boolean) => void;
  resetJob: () => void;
}

const DEFAULT_CONFIG: GenerationConfig = {
  model: 'claude-3-5-sonnet',
  batchSize: 5,
  budgetLimit: 10,
  targetColumns: ['preConditions', 'steps', 'expectedResults'],
};

const DEFAULT_STATS: JobStats = {
  total: 0,
  processed: 0,
  success: 0,
  fail: 0,
  cost: 0,
};

export const useJobStore = create<JobStore>((set) => ({
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

  deleteTcRows: (ids) => set((state) => ({
    tcRows: state.tcRows.filter((row) => !ids.includes(row.id)),
  })),

  setPendingRegenerated: (id, data) => set((state) => ({
    tcRows: state.tcRows.map((row) =>
      row.id === id ? { ...row, pendingRegenerated: data } : row
    ),
  })),

  applyRegenerated: (id, fields) => set((state) => ({
    tcRows: state.tcRows.map((row) => {
      if (row.id !== id || !row.pendingRegenerated) return row;
      const updates: Partial<TcRow> = {};
      if (fields.includes('steps')) updates.steps = row.pendingRegenerated.steps;
      if (fields.includes('expectedResults')) updates.expectedResults = row.pendingRegenerated.expectedResults;
      if (fields.includes('preConditions')) updates.preConditions = row.pendingRegenerated.preConditions;
      return { ...row, ...updates, pendingRegenerated: undefined, status: 'reviewing' };
    }),
  })),

  clearPendingRegenerated: (id) => set((state) => ({
    tcRows: state.tcRows.map((row) =>
      row.id === id ? { ...row, pendingRegenerated: undefined } : row
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

  setProcessing: (status) => set({ isProcessing: status }),
  setRegenerating: (status) => set({ isRegenerating: status }),

  resetJob: () => set({
    jobMetadata: null,
    tcRows: [],
    logs: [],
    stats: DEFAULT_STATS,
    isProcessing: false,
    isRegenerating: false,
  }),
}));
