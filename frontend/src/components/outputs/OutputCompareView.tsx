"use client";

import { RiArrowLeftLine, RiDownload2Line } from "@remixicon/react";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import {
  formatCost,
  formatDuration,
  formatRelativeTime,
  STATUS_COLOR,
  STATUS_LABEL,
  toRun,
  type Run,
} from "../../services/runAdapter";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";

interface DiffChange {
  field: string;
  label: string;
  before: string;
  after: string;
}

interface DiffRow {
  tcId: string;
  reqId?: string;
  status: "added" | "removed" | "changed" | "unchanged";
  changes: DiffChange[];
}

interface DiffSummary {
  total: number;
  added: number;
  removed: number;
  changed: number;
  unchanged: number;
}

interface DiffResponse {
  a: string;
  b: string;
  summary: DiffSummary;
  rows: DiffRow[];
}

export default function OutputCompareView({
  a,
  b,
}: {
  a: string;
  b: string;
}) {
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  const [diff, setDiff] = useState<DiffResponse | null>(null);
  const [diffError, setDiffError] = useState<string | null>(null);
  const [diffLoading, setDiffLoading] = useState(false);

  useEffect(() => {
    if (!a || !b) return;
    let cancelled = false;
    setDiff(null);
    setDiffError(null);
    setDiffLoading(true);
    fetch("/api/outputs/compare", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ a, b }),
    })
      .then(async (res) => {
        if (!res.ok) {
          const body = await res.json().catch(() => ({}));
          throw new Error(body.detail ?? `Status ${res.status}`);
        }
        return (await res.json()) as DiffResponse;
      })
      .then((data) => {
        if (!cancelled) setDiff(data);
      })
      .catch((err) => {
        if (!cancelled)
          setDiffError(err instanceof Error ? err.message : "Diff failed");
      })
      .finally(() => {
        if (!cancelled) setDiffLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [a, b]);

  const runA = useMemo(() => {
    const rec = records.find((r) => r.id === a);
    return rec ? toRun(rec) : null;
  }, [records, a]);

  const runB = useMemo(() => {
    const rec = records.find((r) => r.id === b);
    return rec ? toRun(rec) : null;
  }, [records, b]);

  return (
    <div className="space-y-6">
      <Link
        href="/outputs"
        className="inline-flex items-center gap-1.5 text-sm text-secondary hover:text-primary focus-ring rounded"
      >
        <RiArrowLeftLine size={16} />
        Back to outputs
      </Link>

      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Compare Outputs</h1>
        <p className="text-secondary text-sm">
          Side-by-side metadata + per-row TC content diff.
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <RunPanel run={runA} otherRun={runB} title="Output A" />
        <RunPanel run={runB} otherRun={runA} title="Output B" />
      </div>

      <ComparisonSummary runA={runA} runB={runB} />

      <DiffSection
        diff={diff}
        loading={diffLoading}
        error={diffError}
      />
    </div>
  );
}

function DiffSection({
  diff,
  loading,
  error,
}: {
  diff: DiffResponse | null;
  loading: boolean;
  error: string | null;
}) {
  return (
    <section className="surface p-5 space-y-3">
      <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
        TC Content Diff
      </h2>
      {loading && <p className="text-xs text-muted">Diffing workbooks…</p>}
      {error && (
        <p className="text-sm" style={{ color: "var(--color-brandy)" }}>
          {error}
        </p>
      )}
      {diff && (
        <>
          <dl className="grid grid-cols-2 sm:grid-cols-5 gap-3 text-sm">
            <DiffStat label="Total TCs" value={diff.summary.total} />
            <DiffStat
              label="Added"
              value={diff.summary.added}
              tone="add"
            />
            <DiffStat
              label="Removed"
              value={diff.summary.removed}
              tone="remove"
            />
            <DiffStat
              label="Changed"
              value={diff.summary.changed}
              tone="change"
            />
            <DiffStat label="Unchanged" value={diff.summary.unchanged} />
          </dl>

          {diff.rows.filter((r) => r.status !== "unchanged").length === 0 ? (
            <p className="text-xs text-muted">
              No content differences between the two workbooks.
            </p>
          ) : (
            <ul className="space-y-2">
              {diff.rows
                .filter((r) => r.status !== "unchanged")
                .map((row) => (
                  <DiffRowItem key={row.tcId} row={row} />
                ))}
            </ul>
          )}
        </>
      )}
    </section>
  );
}

function DiffStat({
  label,
  value,
  tone,
}: {
  label: string;
  value: number;
  tone?: "add" | "remove" | "change";
}) {
  const color =
    tone === "add"
      ? "var(--color-teal)"
      : tone === "remove"
      ? "var(--color-brandy)"
      : tone === "change"
      ? "var(--color-tangerine)"
      : "var(--color-ink)";
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold" style={{ color }}>
        {value}
      </dd>
    </div>
  );
}

function DiffRowItem({ row }: { row: DiffRow }) {
  const tone =
    row.status === "added"
      ? "var(--color-teal)"
      : row.status === "removed"
      ? "var(--color-brandy)"
      : "var(--color-tangerine)";
  return (
    <li className="space-y-1.5 px-3 py-2 rounded" style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.12)" }}>
      <div className="flex items-center gap-2 flex-wrap">
        <span
          className="text-[10px] uppercase tracking-wider font-bold"
          style={{ color: tone }}
        >
          {row.status}
        </span>
        <span className="text-sm font-bold text-primary">{row.tcId}</span>
        {row.reqId && (
          <span className="text-xs text-muted">{row.reqId}</span>
        )}
      </div>
      {row.changes.length > 0 && (
        <ul className="space-y-1.5 text-xs">
          {row.changes.map((change) => (
            <li key={change.field} className="space-y-0.5">
              <div className="text-[10px] uppercase tracking-wider text-secondary font-bold">
                {change.label}
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-1">
                <div
                  className="px-2 py-1 rounded text-secondary"
                  style={{
                    backgroundColor: "rgba(120, 41, 15, 0.06)",
                    whiteSpace: "pre-wrap",
                  }}
                >
                  {change.before || "—"}
                </div>
                <div
                  className="px-2 py-1 rounded text-secondary"
                  style={{
                    backgroundColor: "rgba(21, 97, 109, 0.08)",
                    whiteSpace: "pre-wrap",
                  }}
                >
                  {change.after || "—"}
                </div>
              </div>
            </li>
          ))}
        </ul>
      )}
    </li>
  );
}

function RunPanel({
  run,
  otherRun,
  title,
}: {
  run: Run | null;
  otherRun: Run | null;
  title: string;
}) {
  if (!run) {
    return (
      <section className="surface p-6 space-y-2">
        <header className="text-xs uppercase tracking-wider text-muted">
          {title}
        </header>
        <p className="text-sm text-muted">Not found in local history.</p>
      </section>
    );
  }

  return (
    <section className="surface p-6 space-y-4">
      <header className="space-y-1">
        <div className="text-xs uppercase tracking-wider text-muted">
          {title}
        </div>
        <h2 className="text-xl font-bold text-primary">{run.kindLabel}</h2>
        <code className="text-xs text-muted">{run.id}</code>
      </header>

      <div className="grid grid-cols-2 gap-2 text-sm">
        <Field
          label="Status"
          value={
            <span
              className="inline-flex items-center gap-1.5 font-bold text-xs"
              style={{ color: STATUS_COLOR[run.status] }}
            >
              <span
                className="inline-block w-1.5 h-1.5 rounded-full"
                style={{ backgroundColor: STATUS_COLOR[run.status] }}
              />
              {STATUS_LABEL[run.status]}
            </span>
          }
        />
        <Field
          label="Model"
          value={run.model}
          highlight={otherRun ? run.model !== otherRun.model : false}
        />
        <Field
          label="Duration"
          value={formatDuration(run.durationMs)}
          highlight={
            otherRun ? run.durationMs !== otherRun.durationMs : false
          }
        />
        <Field
          label="Cost"
          value={formatCost(run.cost)}
          highlight={otherRun ? run.cost !== otherRun.cost : false}
        />
        <Field
          label="Rows"
          value={`${run.rowsProcessed} / ${run.rowsTotal || "—"}`}
          highlight={
            otherRun
              ? run.rowsTotal !== otherRun.rowsTotal ||
                run.rowsProcessed !== otherRun.rowsProcessed
              : false
          }
        />
        <Field
          label="Started"
          value={formatRelativeTime(run.startedAt)}
        />
      </div>

      <div className="grid grid-cols-2 gap-2 text-sm pt-2">
        <Field label="Input tokens" value={run.tokens.input.toLocaleString()} />
        <Field
          label="Output tokens"
          value={run.tokens.output.toLocaleString()}
        />
        <Field
          label="Cache read"
          value={run.tokens.cacheRead.toLocaleString()}
        />
        <Field
          label="Cache creation"
          value={run.tokens.cacheCreation.toLocaleString()}
        />
      </div>

      <div className="flex items-center gap-2 pt-1">
        <a
          href={`/api/export/download/${encodeURIComponent(run.id)}`}
          className="inline-flex items-center gap-1 text-xs font-bold focus-ring rounded px-2 py-1"
          style={{ color: "var(--color-tangerine)" }}
        >
          <RiDownload2Line size={12} />
          Download
        </a>
        <Link
          href={`/runs/${run.id}`}
          className="text-xs font-bold focus-ring rounded px-2 py-1 text-secondary"
        >
          Open run →
        </Link>
      </div>
    </section>
  );
}

function ComparisonSummary({
  runA,
  runB,
}: {
  runA: Run | null;
  runB: Run | null;
}) {
  if (!runA || !runB) return null;

  const costDelta = runB.cost - runA.cost;
  const durationDelta =
    (runB.durationMs ?? 0) - (runA.durationMs ?? 0);

  return (
    <section className="surface p-5 space-y-3">
      <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
        Delta
      </h2>
      <dl className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-sm">
        <div>
          <dt className="text-xs text-muted uppercase tracking-wider">
            Cost
          </dt>
          <dd
            className="text-base font-bold"
            style={{
              color:
                costDelta > 0
                  ? "var(--color-brandy)"
                  : costDelta < 0
                  ? "var(--color-teal)"
                  : "var(--color-ink)",
            }}
          >
            {costDelta > 0 ? "+" : ""}
            {formatCost(costDelta)}
          </dd>
        </div>
        <div>
          <dt className="text-xs text-muted uppercase tracking-wider">
            Duration
          </dt>
          <dd
            className="text-base font-bold"
            style={{
              color:
                durationDelta > 0
                  ? "var(--color-brandy)"
                  : durationDelta < 0
                  ? "var(--color-teal)"
                  : "var(--color-ink)",
            }}
          >
            {durationDelta > 0 ? "+" : ""}
            {formatDuration(durationDelta)}
          </dd>
        </div>
        <div>
          <dt className="text-xs text-muted uppercase tracking-wider">
            Rows processed
          </dt>
          <dd className="text-base font-bold text-primary">
            {runB.rowsProcessed - runA.rowsProcessed >= 0 ? "+" : ""}
            {runB.rowsProcessed - runA.rowsProcessed}
          </dd>
        </div>
        <div>
          <dt className="text-xs text-muted uppercase tracking-wider">
            Total tokens
          </dt>
          <dd className="text-base font-bold text-primary">
            {(
              runB.tokens.input +
              runB.tokens.output -
              runA.tokens.input -
              runA.tokens.output
            ).toLocaleString()}
          </dd>
        </div>
      </dl>
    </section>
  );
}

function Field({
  label,
  value,
  highlight,
}: {
  label: string;
  value: React.ReactNode;
  highlight?: boolean;
}) {
  return (
    <div
      className="space-y-0.5 px-2 py-1 rounded"
      style={
        highlight
          ? {
              boxShadow: "inset 0 0 0 1px rgba(255, 125, 0, 0.4)",
              backgroundColor: "rgba(255, 125, 0, 0.05)",
            }
          : undefined
      }
    >
      <div className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </div>
      <div className="text-sm text-primary">{value}</div>
    </div>
  );
}
