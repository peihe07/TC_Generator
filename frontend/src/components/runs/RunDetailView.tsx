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

interface TimelineEvent {
  kind: string;
  ts: number;
  message?: string;
  rowCount?: number;
  processed?: number;
  cost?: number;
}

interface TimelineResponse {
  jobId: string;
  events: TimelineEvent[];
}

interface ConfigSnapshot {
  jobId: string;
  config: {
    model?: string;
    batchSize?: number;
    budget?: number;
    strictValidation?: boolean;
    regenerateAll?: boolean;
  } | null;
  projectName?: string | null;
  testGroup?: string | null;
  totalRows?: number | null;
  status?: string | null;
}

interface ValidationLogEntry {
  rowId: string;
  reqId?: string | null;
  severity: string;
  field?: string | null;
  message: string;
  ts: number;
}

const KIND_LABEL: Record<string, string> = {
  queued: "Queued",
  running: "Running",
  completed: "Completed",
  failed: "Failed",
};

const KIND_COLOR: Record<string, string> = {
  queued: "var(--color-teal)",
  running: "var(--color-tangerine)",
  completed: "var(--color-teal)",
  failed: "var(--color-brandy)",
};

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
  const [timeline, setTimeline] = useState<TimelineEvent[] | null>(null);
  const [configSnap, setConfigSnap] = useState<ConfigSnapshot | null>(null);
  const [validationLog, setValidationLog] = useState<ValidationLogEntry[] | null>(
    null
  );

  useEffect(() => {
    let cancelled = false;
    setLiveUsage(null);
    setUsageError(null);
    setTimeline(null);
    setConfigSnap(null);
    setValidationLog(null);
    fetch(`/api/jobs/${encodeURIComponent(runId)}/validation-logs`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as { entries: ValidationLogEntry[] };
      })
      .then((data) => {
        if (!cancelled) setValidationLog(data.entries ?? []);
      })
      .catch(() => {
        if (!cancelled) setValidationLog([]);
      });
    fetch(`/api/jobs/${encodeURIComponent(runId)}/config`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as ConfigSnapshot;
      })
      .then((data) => {
        if (!cancelled) setConfigSnap(data);
      })
      .catch(() => {
        // 沒設定就靜默；UI 自然不顯示
      });
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
    fetch(`/api/jobs/${encodeURIComponent(runId)}/timeline`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as TimelineResponse;
      })
      .then((data) => {
        if (!cancelled) setTimeline(data.events ?? []);
      })
      .catch(() => {
        if (!cancelled) setTimeline([]);
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

      <ConfigSnapshotSection snapshot={configSnap} />
      <ValidationLogSection entries={validationLog} />
      <TimelineSection events={timeline} />
    </div>
  );
}

function ValidationLogSection({
  entries,
}: {
  entries: ValidationLogEntry[] | null;
}) {
  if (entries === null) return null;
  if (entries.length === 0) return null;
  const errorCount = entries.filter((e) => e.severity === "error").length;
  const warnCount = entries.filter((e) => e.severity === "warning").length;
  return (
    <section className="surface p-5 space-y-3">
      <header className="flex items-center justify-between gap-2 flex-wrap">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Validation Log
        </h2>
        <span className="text-xs text-muted">
          {errorCount > 0 && (
            <span style={{ color: "var(--color-brandy)" }}>
              {errorCount} error{errorCount > 1 ? "s" : ""}
            </span>
          )}
          {errorCount > 0 && warnCount > 0 && " · "}
          {warnCount > 0 && (
            <span style={{ color: "var(--color-tangerine)" }}>
              {warnCount} warning{warnCount > 1 ? "s" : ""}
            </span>
          )}
        </span>
      </header>
      <ul className="space-y-1.5 max-h-[320px] overflow-y-auto pr-1">
        {entries.map((entry) => (
          <li
            key={entry.rowId + entry.ts}
            className="flex items-start gap-3 text-xs"
          >
            <span
              className="mt-0.5 shrink-0"
              style={{
                color:
                  entry.severity === "error"
                    ? "var(--color-brandy)"
                    : "var(--color-tangerine)",
              }}
            >
              {entry.severity === "error" ? "✕" : "⚠"}
            </span>
            <div className="flex-1 min-w-0">
              <div className="text-primary truncate">
                <span className="font-bold">{entry.reqId ?? entry.rowId}</span>
                {entry.field ? ` · ${entry.field}` : ""}
              </div>
              <div className="text-secondary">{entry.message}</div>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}

function ConfigSnapshotSection({
  snapshot,
}: {
  snapshot: ConfigSnapshot | null;
}) {
  if (!snapshot || !snapshot.config) return null;
  const c = snapshot.config;
  const items: Array<{ label: string; value: string }> = [];
  if (c.model) items.push({ label: "Model", value: c.model });
  if (c.batchSize != null)
    items.push({ label: "Batch Size", value: String(c.batchSize) });
  if (c.budget != null)
    items.push({ label: "Budget", value: `$${c.budget}` });
  if (c.strictValidation != null)
    items.push({
      label: "Strict",
      value: c.strictValidation ? "On" : "Off",
    });
  if (c.regenerateAll)
    items.push({ label: "Regenerate All", value: "On" });
  if (snapshot.projectName)
    items.push({ label: "Project", value: snapshot.projectName });
  if (snapshot.testGroup)
    items.push({ label: "Test Group", value: snapshot.testGroup });

  if (items.length === 0) return null;

  return (
    <section className="surface p-5 space-y-3">
      <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
        Resolved Config
      </h2>
      <dl className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-sm">
        {items.map((item) => (
          <div key={item.label}>
            <dt className="text-[10px] uppercase tracking-wider text-muted">
              {item.label}
            </dt>
            <dd className="text-sm font-bold text-primary truncate">
              {item.value}
            </dd>
          </div>
        ))}
      </dl>
    </section>
  );
}

function TimelineSection({ events }: { events: TimelineEvent[] | null }) {
  return (
    <section className="surface p-5 space-y-3">
      <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
        Timeline
      </h2>
      {events === null ? (
        <p className="text-xs text-muted">Loading timeline…</p>
      ) : events.length === 0 ? (
        <p className="text-xs text-muted">
          No timeline events recorded for this run.
        </p>
      ) : (
        <ol className="space-y-2">
          {events.map((event, idx) => (
            <li
              key={`${event.kind}-${idx}-${event.ts}`}
              className="flex items-start gap-3"
            >
              <span
                className="mt-1.5 inline-block w-2 h-2 rounded-full shrink-0"
                style={{
                  backgroundColor:
                    KIND_COLOR[event.kind] ?? "var(--color-teal)",
                }}
              />
              <div className="flex-1 min-w-0 space-y-0.5">
                <div className="text-sm font-bold text-primary">
                  {KIND_LABEL[event.kind] ?? event.kind}
                </div>
                <div className="text-xs text-muted flex items-center gap-2 flex-wrap">
                  <span>{formatRelativeTime(event.ts)}</span>
                  {event.rowCount != null && (
                    <span>· {event.rowCount} rows</span>
                  )}
                  {event.processed != null && (
                    <span>· {event.processed} processed</span>
                  )}
                  {event.cost != null && (
                    <span>· {formatCost(event.cost)}</span>
                  )}
                </div>
                {event.message && (
                  <div className="text-xs text-secondary">
                    {event.message}
                  </div>
                )}
              </div>
            </li>
          ))}
        </ol>
      )}
    </section>
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
