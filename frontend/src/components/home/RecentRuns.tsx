import Link from "next/link";
import {
  formatCost,
  formatDuration,
  formatRelativeTime,
  STATUS_COLOR,
  STATUS_LABEL,
  type Run,
} from "../../services/runAdapter";

export default function RecentRuns({ runs }: { runs: Run[] }) {
  const recent = runs.slice(0, 8);

  return (
    <section className="surface p-5 space-y-4">
      <header className="flex items-center justify-between">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Recent Runs
        </h2>
        <Link
          href="/runs"
          className="text-xs font-bold focus-ring rounded"
          style={{ color: "var(--color-tangerine)" }}
        >
          View all →
        </Link>
      </header>

      {recent.length === 0 ? (
        <p className="text-sm text-muted py-6 text-center">
          No runs yet. Start with{" "}
          <Link
            href="/run-builder"
            className="font-bold"
            style={{ color: "var(--color-tangerine)" }}
          >
            New Run
          </Link>
          .
        </p>
      ) : (
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left text-xs uppercase tracking-wider text-muted">
              <th className="font-normal pb-2">Run</th>
              <th className="font-normal pb-2">Status</th>
              <th className="font-normal pb-2">Duration</th>
              <th className="font-normal pb-2">Cost</th>
              <th className="font-normal pb-2 text-right">Started</th>
            </tr>
          </thead>
          <tbody>
            {recent.map((r) => (
              <tr
                key={r.id}
                className="row-hover"
                style={{ borderRadius: 8 }}
              >
                <td className="py-2 pr-3">
                  <Link
                    href={`/runs/${r.id}`}
                    className="text-primary font-bold hover:underline"
                  >
                    {r.kindLabel}
                  </Link>
                  <div className="text-xs text-muted truncate max-w-[200px]">
                    {r.id}
                  </div>
                </td>
                <td className="py-2 pr-3">
                  <StatusPill status={r.status} />
                </td>
                <td className="py-2 pr-3 text-secondary">
                  {formatDuration(r.durationMs)}
                </td>
                <td className="py-2 pr-3 text-secondary">
                  {formatCost(r.cost)}
                </td>
                <td className="py-2 text-right text-muted text-xs">
                  {formatRelativeTime(r.startedAt)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}

function StatusPill({ status }: { status: Run["status"] }) {
  return (
    <span
      className="inline-flex items-center gap-1.5 text-xs font-bold"
      style={{ color: STATUS_COLOR[status] }}
    >
      <span
        className="inline-block w-1.5 h-1.5 rounded-full"
        style={{ backgroundColor: STATUS_COLOR[status] }}
      />
      {STATUS_LABEL[status]}
    </span>
  );
}
