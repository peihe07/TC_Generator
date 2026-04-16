"use client";

import { create } from "zustand";

import { DEFAULT_JOB_CONFIG } from "@/src/lib/constants";
import type {
  JobConfig,
  JobFiles,
  JobLog,
  JobStats,
  TcPreviewRow,
  TcRow,
} from "@/src/lib/types";

type JobStore = {
  jobId: string | null;
  files: JobFiles;
  previewRows: TcPreviewRow[];
  previewHeaders: string[];
  tcRows: TcRow[];
  config: JobConfig;
  logs: JobLog[];
  stats: JobStats;
  setJobId: (jobId: string | null) => void;
  setFiles: (files: Partial<JobFiles>) => void;
  setPreview: (headers: string[], rows: TcPreviewRow[]) => void;
  setRows: (rows: TcRow[]) => void;
  updateRow: (id: string, updates: Partial<TcRow>) => void;
  updateConfig: (updates: Partial<JobConfig>) => void;
  appendLog: (log: Omit<JobLog, "timestamp"> & { timestamp?: string }) => void;
  setStats: (updates: Partial<JobStats>) => void;
  resetJob: () => void;
};

const initialFiles: JobFiles = {
  raw: null,
  spec: null,
  parsed: false,
};

const initialStats: JobStats = {
  total: 0,
  processed: 0,
  currentCost: 0,
};

const initialLogs: JobLog[] = [
  {
    timestamp: new Date().toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
    }),
    level: "info",
    message: "Desktop booted. Upload a workbook to start a generation session.",
  },
];

export const useJobStore = create<JobStore>((set) => ({
  jobId: null,
  files: initialFiles,
  previewRows: [],
  previewHeaders: [],
  tcRows: [],
  config: DEFAULT_JOB_CONFIG,
  logs: initialLogs,
  stats: initialStats,
  setJobId: (jobId) => set({ jobId }),
  setFiles: (files) =>
    set((state) => ({
      files: {
        ...state.files,
        ...files,
      },
    })),
  setPreview: (previewHeaders, previewRows) =>
    set((state) => ({
      previewHeaders,
      previewRows,
      files: {
        ...state.files,
        parsed: previewRows.length > 0,
      },
    })),
  setRows: (tcRows) =>
    set({
      tcRows,
      stats: {
        total: tcRows.length,
        processed: 0,
        currentCost: 0,
      },
    }),
  updateRow: (id, updates) =>
    set((state) => ({
      tcRows: state.tcRows.map((row) =>
        row.id === id ? { ...row, ...updates } : row,
      ),
    })),
  updateConfig: (updates) =>
    set((state) => ({
      config: {
        ...state.config,
        ...updates,
      },
    })),
  appendLog: (log) =>
    set((state) => ({
      logs: [
        ...state.logs,
        {
          timestamp:
            log.timestamp ??
            new Date().toLocaleTimeString("en-US", {
              hour: "2-digit",
              minute: "2-digit",
            }),
          level: log.level,
          message: log.message,
        },
      ],
    })),
  setStats: (updates) =>
    set((state) => ({
      stats: {
        ...state.stats,
        ...updates,
      },
    })),
  resetJob: () =>
    set({
      jobId: null,
      files: initialFiles,
      previewRows: [],
      previewHeaders: [],
      tcRows: [],
      config: DEFAULT_JOB_CONFIG,
      logs: initialLogs,
      stats: initialStats,
    }),
}));
