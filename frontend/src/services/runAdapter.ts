// Run view-model layer
//
// 後端目前以 JobRecord 為單位（見 useJobHistoryStore），UI 改用 Top-Nav 工作流後
// 一律透過 `Run` 概念呈現，避免直接依賴 JobRecord。後端 API 路徑保持 /api/jobs，
// rename 推遲到後續 phase。

import type { JobRecord, JobRecordKind } from "../store/useJobHistoryStore";

export type RunStatus = "running" | "completed" | "failed" | "partial";

export type RunKind = JobRecordKind;

export interface Run {
  id: string;
  kind: RunKind;
  kindLabel: string;
  model: string;
  status: RunStatus;
  startedAt: number;
  finishedAt: number | null;
  durationMs: number | null;
  rowsTotal: number;
  rowsProcessed: number;
  progress: number; // 0..1
  cost: number;
  tokens: {
    input: number;
    output: number;
    cacheRead: number;
    cacheCreation: number;
  };
  note?: string;
}

const KIND_LABEL: Record<RunKind, string> = {
  generate: "Generate",
  quick: "Quick Generate",
  group: "Group",
  regenerate: "Regenerate",
  rerun: "Rerun",
  "suggest-fix": "Suggest Fix",
  export: "Export",
};

// 顯示用 status 顏色 token（對應 design-tokens.md）
export const STATUS_COLOR: Record<RunStatus, string> = {
  running: "var(--color-tangerine)",
  completed: "var(--color-teal)",
  failed: "var(--color-brandy)",
  partial: "var(--color-tangerine)",
};

export const STATUS_LABEL: Record<RunStatus, string> = {
  running: "Running",
  completed: "Completed",
  failed: "Failed",
  partial: "Partial",
};

export function deriveStatus(record: JobRecord): RunStatus {
  const finished = Number(record.finishedAt) > 0;
  if (!finished) return "running";
  const total = record.rowsTotal ?? 0;
  const processed = record.rowsProcessed ?? 0;
  if (total > 0 && processed === 0) return "failed";
  if (total > 0 && processed < total) return "partial";
  return "completed";
}

export function toRun(record: JobRecord): Run {
  const status = deriveStatus(record);
  const finishedAt = record.finishedAt > 0 ? record.finishedAt : null;
  const durationMs =
    finishedAt && record.startedAt ? finishedAt - record.startedAt : null;
  const total = record.rowsTotal ?? 0;
  const processed = record.rowsProcessed ?? 0;
  const progress = total > 0 ? Math.min(1, processed / total) : 0;

  return {
    id: record.id,
    kind: record.kind,
    kindLabel: KIND_LABEL[record.kind] ?? record.kind,
    model: record.model,
    status,
    startedAt: record.startedAt,
    finishedAt,
    durationMs,
    rowsTotal: total,
    rowsProcessed: processed,
    progress,
    cost: record.cost ?? 0,
    tokens: {
      input: record.inputTokens ?? 0,
      output: record.outputTokens ?? 0,
      cacheRead: record.cacheReadTokens ?? 0,
      cacheCreation: record.cacheCreationTokens ?? 0,
    },
    note: record.note,
  };
}

export function toRuns(records: JobRecord[]): Run[] {
  return records.map(toRun);
}

// ---------- Aggregates for KPI cards ----------

export interface RunAggregates {
  total: number;
  finishedCount: number;
  successCount: number;
  failCount: number;
  partialCount: number;
  issueCount: number;
  runningCount: number;
  successRate: number; // 0..1，分母排除 running
  avgDurationMs: number | null;
  completedAvgDurationMs: number | null;
  recent7dTotal: number;
  recent7dSuccessRate: number;
  totalCost: number;
}

const RECENT_WINDOW_MS = 7 * 86_400_000;

export function aggregate(runs: Run[], now = Date.now()): RunAggregates {
  const total = runs.length;
  let successCount = 0;
  let failCount = 0;
  let partialCount = 0;
  let runningCount = 0;
  let durationSum = 0;
  let durationN = 0;
  let completedDurationSum = 0;
  let completedDurationN = 0;
  let recent7dTotal = 0;
  let recent7dFinished = 0;
  let recent7dSuccessCount = 0;
  let totalCost = 0;

  for (const r of runs) {
    totalCost += r.cost;
    if (r.status === "completed") {
      successCount += 1;
      if (r.durationMs && r.durationMs > 0) {
        completedDurationSum += r.durationMs;
        completedDurationN += 1;
      }
    } else if (r.status === "failed") failCount += 1;
    else if (r.status === "partial") partialCount += 1;
    else if (r.status === "running") runningCount += 1;

    if (r.durationMs && r.durationMs > 0) {
      durationSum += r.durationMs;
      durationN += 1;
    }

    const activityTs = r.finishedAt ?? r.startedAt;
    if (activityTs >= now - RECENT_WINDOW_MS) {
      recent7dTotal += 1;
      if (r.status !== "running") recent7dFinished += 1;
      if (r.status === "completed") recent7dSuccessCount += 1;
    }
  }

  const finishedDenom = total - runningCount;
  const successRate = finishedDenom > 0 ? successCount / finishedDenom : 0;
  const avgDurationMs = durationN > 0 ? durationSum / durationN : null;
  const completedAvgDurationMs =
    completedDurationN > 0 ? completedDurationSum / completedDurationN : null;
  const recent7dSuccessRate =
    recent7dFinished > 0 ? recent7dSuccessCount / recent7dFinished : 0;

  return {
    total,
    finishedCount: finishedDenom,
    successCount,
    failCount,
    partialCount,
    issueCount: failCount + partialCount,
    runningCount,
    successRate,
    avgDurationMs,
    completedAvgDurationMs,
    recent7dTotal,
    recent7dSuccessRate,
    totalCost,
  };
}

// ---------- Formatters ----------

export function formatDuration(ms: number | null): string {
  if (ms == null) return "—";
  if (ms < 1000) return `${ms}ms`;
  const sec = ms / 1000;
  if (sec < 60) return `${sec.toFixed(1)}s`;
  const min = Math.floor(sec / 60);
  const remSec = Math.round(sec - min * 60);
  return `${min}m ${remSec}s`;
}

export function formatCost(cost: number): string {
  if (cost === 0) return "$0";
  if (cost < 0.01) return `$${cost.toFixed(4)}`;
  return `$${cost.toFixed(2)}`;
}

export function formatRelativeTime(ts: number): string {
  if (!ts) return "—";
  const diff = Date.now() - ts;
  if (diff < 60_000) return "just now";
  if (diff < 3_600_000) return `${Math.floor(diff / 60_000)}m ago`;
  if (diff < 86_400_000) return `${Math.floor(diff / 3_600_000)}h ago`;
  return `${Math.floor(diff / 86_400_000)}d ago`;
}

export function formatPercent(ratio: number): string {
  return `${Math.round(ratio * 100)}%`;
}
