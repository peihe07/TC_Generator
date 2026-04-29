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
        hint={`${agg.successCount}/${agg.finishedCount} finished`}
        accent="var(--color-teal)"
      />
      <KpiCard
        label="Avg Successful Duration"
        value={formatDuration(agg.completedAvgDurationMs)}
        hint={agg.total === 0 ? "No runs yet" : "Completed runs only"}
      />
      <KpiCard
        label="Needs Attention"
        value={String(agg.issueCount)}
        hint={`${agg.failCount} failed · ${agg.partialCount} partial`}
        accent={
          agg.failCount > 0 ? "var(--color-brandy)" : "var(--color-ink)"
        }
      />
      <KpiCard
        label="7d Success"
        value={agg.recent7dTotal === 0 ? "—" : formatPercent(agg.recent7dSuccessRate)}
        hint={
          agg.runningCount > 0
            ? `${agg.runningCount} running now`
            : `${agg.recent7dTotal} recent runs`
        }
        accent="var(--color-tangerine)"
      />
    </div>
  );
}
