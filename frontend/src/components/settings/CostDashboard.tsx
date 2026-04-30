"use client";

import { RiLoader4Line, RiRefreshLine } from "@remixicon/react";
import { useCallback, useEffect, useState } from "react";
import { buildWorkspaceHeader } from "../../lib/workspaceHeader";
import { useWorkspaceStore } from "../../store/useWorkspaceStore";

interface AggregateMetrics {
  jobCount: number;
  totalRowCount: number;
  totalCostUsd: number | null;
  avgCostUsd: number | null;
  avgRowCount: number | null;
  matchRate: number | null;
  jobsWithCost: number;
  jobsWithMatch: number;
}

function formatUsd(value: number | null): string {
  if (value == null) return "—";
  return `$${value.toFixed(4)}`;
}

function formatPercent(value: number | null): string {
  if (value == null) return "—";
  return `${Math.round(value * 100)}%`;
}

function formatNumber(value: number | null): string {
  if (value == null) return "—";
  return Math.round(value).toLocaleString();
}

export default function CostDashboard() {
  const [data, setData] = useState<AggregateMetrics | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const currentWorkspaceId = useWorkspaceStore((s) => s.currentId);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/metrics/aggregate", {
        headers: buildWorkspaceHeader(),
      });
      if (!res.ok) throw new Error(`Status ${res.status}`);
      const json = (await res.json()) as AggregateMetrics;
      setData(json);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Fetch failed");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void load();
  }, [load, currentWorkspaceId]);

  return (
    <div className="space-y-3">
      <header className="flex items-center justify-between gap-2 flex-wrap">
        <p className="text-xs text-muted">
          Cross-job cost aggregate from <code>/api/metrics/aggregate</code>.
          Scoped to the current workspace.
        </p>
        <button
          type="button"
          onClick={() => void load()}
          disabled={loading}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-bold focus-ring disabled:opacity-40"
          style={{
            backgroundColor: "rgba(21, 97, 109, 0.12)",
            color: "var(--color-teal)",
          }}
        >
          {loading ? (
            <RiLoader4Line size={12} className="animate-spin" />
          ) : (
            <RiRefreshLine size={12} />
          )}
          Refresh
        </button>
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

      {data && (
        <dl className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-sm">
          <Stat label="Jobs" value={formatNumber(data.jobCount)} />
          <Stat
            label="Total cost"
            value={formatUsd(data.totalCostUsd)}
            sub={`${data.jobsWithCost}/${data.jobCount} priced`}
          />
          <Stat label="Avg cost / job" value={formatUsd(data.avgCostUsd)} />
          <Stat label="Avg rows / job" value={formatNumber(data.avgRowCount)} />
          <Stat label="Total rows" value={formatNumber(data.totalRowCount)} />
          <Stat
            label="Match rate"
            value={formatPercent(data.matchRate)}
            sub={`${data.jobsWithMatch}/${data.jobCount} matched`}
          />
        </dl>
      )}

      {data && data.jobCount === 0 && (
        <p className="text-xs text-muted">
          No jobs in this workspace yet — run a generation to populate metrics.
        </p>
      )}
    </div>
  );
}

function Stat({
  label,
  value,
  sub,
}: {
  label: string;
  value: string;
  sub?: string;
}) {
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold text-primary truncate">{value}</dd>
      {sub && <div className="text-[10px] text-muted">{sub}</div>}
    </div>
  );
}
