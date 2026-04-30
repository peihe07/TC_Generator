"use client";

import { RiBarChart2Line, RiLoader4Line } from "@remixicon/react";
import { useEffect, useState } from "react";
import { buildWorkspaceHeader } from "../../lib/workspaceHeader";
import { useWorkspaceStore } from "../../store/useWorkspaceStore";

interface AggregateBucket {
  eventCount: number;
  newRunClicks: number;
  runStarts: number;
  runSuccesses: number;
  runFailures: number;
  templateUses: number;
  templateSaves: number;
  retryClicks: number;
  comparesOpened: number;
  builderStepNexts: number;
  validationFails: number;
  completionRate: number;
  failureRate: number;
  templateReuseRate: number;
  rerunConversionRate: number;
  validationErrorRate: number;
  compareEngagementRate: number;
}

interface AggregateResponse {
  totalEvents: number;
  malformedLines: number;
  variants: Record<string, AggregateBucket>;
}

const KPI_ITEMS: Array<{
  key: keyof AggregateBucket;
  label: string;
  hint: string;
  format: "percent" | "count";
  decisionGoal?: "up" | "down";
}> = [
  {
    key: "completionRate",
    label: "Run completion rate",
    hint: "successes / (successes + failures)",
    format: "percent",
    decisionGoal: "up",
  },
  {
    key: "templateReuseRate",
    label: "Template reuse rate",
    hint: "template_use_click / run_execute_start",
    format: "percent",
    decisionGoal: "up",
  },
  {
    key: "rerunConversionRate",
    label: "Rerun conversion",
    hint: "run_retry_click / run_execute_fail",
    format: "percent",
    decisionGoal: "up",
  },
  {
    key: "validationErrorRate",
    label: "Validation error rate",
    hint: "builder_validation_fail / builder_step_next",
    format: "percent",
    decisionGoal: "down",
  },
  {
    key: "compareEngagementRate",
    label: "Output compare engagement",
    hint: "output_compare_open / run_execute_success",
    format: "percent",
    decisionGoal: "up",
  },
  {
    key: "templateSaves",
    label: "Template edits",
    hint: "template_save events",
    format: "count",
  },
];

export default function KpiDashboard() {
  const [data, setData] = useState<AggregateResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const wsId = useWorkspaceStore((s) => s.currentId);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/events/aggregate`, { headers: buildWorkspaceHeader() })
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as AggregateResponse;
      })
      .then((d) => {
        if (!cancelled) setData(d);
      })
      .catch((err) => {
        if (!cancelled)
          setError(err instanceof Error ? err.message : "Fetch failed");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [wsId]);

  const bucket: AggregateBucket | null = data?.variants?.all ?? null;

  return (
    <div className="space-y-3">
      <header className="flex items-center justify-between gap-2 flex-wrap">
        <div className="flex items-center gap-2">
          <RiBarChart2Line size={14} className="text-secondary" />
          <span className="text-sm font-bold text-primary">
            Workflow KPIs
          </span>
          {loading && (
            <RiLoader4Line
              size={12}
              className="animate-spin text-secondary"
            />
          )}
        </div>
        {data && (
          <span className="text-xs text-muted">
            {data.totalEvents} events
          </span>
        )}
      </header>

      {error && (
        <div
          className="text-xs px-3 py-2 rounded-md"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          {error}
        </div>
      )}

      {bucket ? (
        <dl className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {KPI_ITEMS.map((item) => {
            const value = bucket[item.key];
            const display =
              item.format === "percent"
                ? `${Math.round((value as number) * 100)}%`
                : String(value);
            return (
              <div key={String(item.key)} className="space-y-0.5 px-3 py-2">
                <dt className="text-[10px] uppercase tracking-wider text-secondary">
                  {item.label}
                </dt>
                <dd className="text-2xl font-bold text-primary">
                  {display}
                </dd>
                <dd className="text-[10px] text-muted">{item.hint}</dd>
              </div>
            );
          })}
        </dl>
      ) : (
        !loading &&
        !error && (
          <p className="text-xs text-muted">
            No telemetry yet. Fire a few runs to populate the KPIs.
          </p>
        )
      )}
    </div>
  );
}
