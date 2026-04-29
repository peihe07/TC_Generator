import {
  formatDuration,
  formatPercent,
  type RunAggregates,
} from "../../services/runAdapter";
import KpiCard from "./KpiCard";

export default function KpiCards({ agg }: { agg: RunAggregates }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <KpiCard
        label="Success Rate"
        value={agg.total === 0 ? "—" : formatPercent(agg.successRate)}
        hint={`${agg.successCount}/${agg.total - agg.runningCount} finished`}
        accent="var(--color-teal)"
      />
      <KpiCard
        label="Avg Duration"
        value={formatDuration(agg.avgDurationMs)}
        hint={agg.total === 0 ? "No runs yet" : undefined}
      />
      <KpiCard
        label="Fail Count"
        value={String(agg.failCount + agg.partialCount)}
        hint={`${agg.failCount} failed · ${agg.partialCount} partial`}
        accent={
          agg.failCount > 0 ? "var(--color-brandy)" : "var(--color-ink)"
        }
      />
      <KpiCard
        label="Total Runs"
        value={String(agg.total)}
        hint={
          agg.runningCount > 0 ? `${agg.runningCount} running now` : undefined
        }
        accent="var(--color-tangerine)"
      />
    </div>
  );
}
