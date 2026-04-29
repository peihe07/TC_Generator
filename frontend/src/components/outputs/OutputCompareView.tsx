"use client";

import { RiArrowLeftLine, RiDownload2Line } from "@remixicon/react";
import Link from "next/link";
import { useEffect, useMemo } from "react";
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
          Side-by-side metadata. File-content diff coming in a later phase.
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <RunPanel run={runA} otherRun={runB} title="Output A" />
        <RunPanel run={runB} otherRun={runA} title="Output B" />
      </div>

      <ComparisonSummary runA={runA} runB={runB} />
    </div>
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
