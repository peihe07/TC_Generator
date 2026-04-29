"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import {
  RiArrowLeftLine,
  RiPlayCircleLine,
  RiPencilLine,
} from "@remixicon/react";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { track } from "../../lib/telemetry";
import {
  formatCost,
  formatDuration,
  formatRelativeTime,
  STATUS_COLOR,
  STATUS_LABEL,
  toRun,
} from "../../services/runAdapter";
import { Skeleton, SkeletonRows } from "../shell/Skeleton";

interface UsageResponse {
  cost?: number;
  inputTokens?: number;
  outputTokens?: number;
  cacheReadTokens?: number;
  cacheCreationTokens?: number;
}

export default function RunDetailView({ runId }: { runId: string }) {
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  const record = useMemo(
    () => records.find((r) => r.id === runId),
    [records, runId]
  );
  const run = record ? toRun(record) : null;

  const [liveUsage, setLiveUsage] = useState<UsageResponse | null>(null);
  const [usageError, setUsageError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLiveUsage(null);
    setUsageError(null);
    fetch(`/api/jobs/${encodeURIComponent(runId)}/usage`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as UsageResponse;
      })
      .then((data) => {
        if (!cancelled) setLiveUsage(data);
      })
      .catch((err) => {
        if (!cancelled)
          setUsageError(err instanceof Error ? err.message : "Failed");
      });
    return () => {
      cancelled = true;
    };
  }, [runId]);

  if (!loaded) {
    return (
      <div className="space-y-6">
        <BackLink />
        <header className="space-y-2">
          <Skeleton height={32} width="40%" />
          <Skeleton height={12} width="55%" />
        </header>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          {[0, 1, 2, 3].map((i) => (
            <div key={i} className="surface p-4 space-y-2">
              <Skeleton height={10} width="40%" />
              <Skeleton height={20} width="60%" />
            </div>
          ))}
        </div>
        <div className="surface p-5 space-y-3">
          <Skeleton height={12} width="20%" />
          <SkeletonRows rows={2} />
        </div>
      </div>
    );
  }

  if (!run) {
    return (
      <div className="space-y-6">
        <BackLink />
        <div className="surface p-10 text-center space-y-2">
          <h1 className="text-xl font-bold text-primary">Run not found</h1>
          <p className="text-sm text-muted">
            No local history for{" "}
            <code className="text-secondary">{runId}</code>.
          </p>
        </div>
      </div>
    );
  }

  const cost = liveUsage?.cost ?? run.cost;
  const tokens = {
    input: liveUsage?.inputTokens ?? run.tokens.input,
    output: liveUsage?.outputTokens ?? run.tokens.output,
    cacheRead: liveUsage?.cacheReadTokens ?? run.tokens.cacheRead,
    cacheCreation: liveUsage?.cacheCreationTokens ?? run.tokens.cacheCreation,
  };
  const totalTokens =
    tokens.input + tokens.output + tokens.cacheRead + tokens.cacheCreation;

  return (
    <div className="space-y-6">
      <BackLink />

      <header className="flex items-start justify-between gap-4 flex-wrap">
        <div className="space-y-2">
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-bold text-primary">
              {run.kindLabel}
            </h1>
            <span
              className="inline-flex items-center gap-1.5 text-sm font-bold"
              style={{ color: STATUS_COLOR[run.status] }}
            >
              <span
                className="inline-block w-2 h-2 rounded-full"
                style={{ backgroundColor: STATUS_COLOR[run.status] }}
              />
              {STATUS_LABEL[run.status]}
            </span>
          </div>
          <div className="text-sm text-secondary flex items-center gap-3 flex-wrap">
            <span className="font-bold">{run.model}</span>
            <span className="text-muted">·</span>
            <code className="text-xs">{run.id}</code>
            <span className="text-muted">·</span>
            <span>{formatRelativeTime(run.startedAt)}</span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Link
            href={`/run-builder?from=${encodeURIComponent(run.id)}`}
            onClick={() =>
              track("run_retry_click", { runId: run.id, mode: "rerun" })
            }
            className="cta inline-flex items-center gap-1.5 text-sm"
          >
            <RiPlayCircleLine size={16} />
            Rerun
          </Link>
          <Link
            href={`/run-builder?edit=${encodeURIComponent(run.id)}`}
            onClick={() =>
              track("run_retry_click", { runId: run.id, mode: "edit" })
            }
            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-lg text-sm font-bold focus-ring transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            <RiPencilLine size={16} />
            Edit & Rerun
          </Link>
        </div>
      </header>

      <section className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <Stat label="Duration" value={formatDuration(run.durationMs)} />
        <Stat label="Cost" value={formatCost(cost)} />
        <Stat
          label="Rows"
          value={`${run.rowsProcessed} / ${run.rowsTotal || "—"}`}
          hint={
            run.rowsTotal > 0
              ? `${Math.round(run.progress * 100)}% complete`
              : undefined
          }
        />
        <Stat label="Total Tokens" value={totalTokens.toLocaleString()} />
      </section>

      <section className="surface p-5 space-y-3">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Token Breakdown
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-sm">
          <TokenItem label="Input" value={tokens.input} />
          <TokenItem label="Output" value={tokens.output} />
          <TokenItem label="Cache Read" value={tokens.cacheRead} />
          <TokenItem label="Cache Creation" value={tokens.cacheCreation} />
        </div>
        {usageError && (
          <p className="text-xs text-muted">
            Live usage unavailable: {usageError} (showing cached values)
          </p>
        )}
      </section>

      {run.note && (
        <section className="surface p-5 space-y-2">
          <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
            Note
          </h2>
          <p className="text-sm text-secondary whitespace-pre-wrap">
            {run.note}
          </p>
        </section>
      )}

      <section className="surface p-5 space-y-3">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Coming Soon
        </h2>
        <ul className="space-y-1.5 text-sm text-secondary">
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Timeline (queued → running → completed/failed)</span>
          </li>
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Resolved config snapshot (template + overrides)</span>
          </li>
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Validation logs and error context</span>
          </li>
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Output artifacts and download links</span>
          </li>
        </ul>
      </section>
    </div>
  );
}

function BackLink() {
  return (
    <Link
      href="/runs"
      className="inline-flex items-center gap-1.5 text-sm text-secondary hover:text-primary focus-ring rounded"
    >
      <RiArrowLeftLine size={16} />
      Back to runs
    </Link>
  );
}

function Stat({
  label,
  value,
  hint,
}: {
  label: string;
  value: string;
  hint?: string;
}) {
  return (
    <div className="surface p-4 space-y-1">
      <span className="text-xs uppercase tracking-wider text-secondary">
        {label}
      </span>
      <div className="text-2xl font-bold text-primary">{value}</div>
      {hint && <span className="text-xs text-muted">{hint}</span>}
    </div>
  );
}

function TokenItem({ label, value }: { label: string; value: number }) {
  return (
    <div className="space-y-0.5">
      <div className="text-xs text-muted uppercase tracking-wider">
        {label}
      </div>
      <div className="text-base font-bold text-primary">
        {value.toLocaleString()}
      </div>
    </div>
  );
}
