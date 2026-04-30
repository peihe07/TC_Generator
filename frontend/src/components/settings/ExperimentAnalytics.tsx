"use client";

import { RiBarChart2Line, RiLoader4Line, RiTrophyLine, RiArrowGoBackLine } from "@remixicon/react";
import { useEffect, useState } from "react";
import {
  EXPERIMENT_DEFINITIONS,
  clearExperimentDecision,
  getExperimentDecision,
  setExperimentDecision,
  type ExperimentDecision,
  type ExperimentKey,
  type ExperimentVariant,
} from "../../lib/experiments";
import { buildWorkspaceHeader } from "../../lib/workspaceHeader";
import { useWorkspaceStore } from "../../store/useWorkspaceStore";

interface VariantBucket {
  eventCount: number;
  exposures: number;
  newRunClicks: number;
  runStarts: number;
  runSuccesses: number;
  runFailures: number;
  completionRate: number;
  failureRate: number;
}

interface AggregateResponse {
  experiment: string | null;
  totalEvents: number;
  malformedLines: number;
  variants: Record<string, VariantBucket>;
  unknownVariant: VariantBucket;
}

const COLUMNS: Array<{ key: keyof VariantBucket; label: string; format?: "percent" }> = [
  { key: "exposures", label: "Exposures" },
  { key: "newRunClicks", label: "New Run" },
  { key: "runStarts", label: "Starts" },
  { key: "runSuccesses", label: "OK" },
  { key: "runFailures", label: "Fail" },
  { key: "completionRate", label: "Completion", format: "percent" },
];

export default function ExperimentAnalytics({
  experiment,
}: {
  experiment: ExperimentKey;
}) {
  const definition = EXPERIMENT_DEFINITIONS[experiment];
  const [data, setData] = useState<AggregateResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [decision, setDecision] = useState<ExperimentDecision | null>(null);

  useEffect(() => {
    setDecision(getExperimentDecision(experiment));
  }, [experiment]);

  const promote = (winner: ExperimentVariant) => {
    const next = setExperimentDecision(experiment, winner);
    setDecision(next);
  };
  const resume = () => {
    clearExperimentDecision(experiment);
    setDecision(null);
  };

  const currentWorkspaceId = useWorkspaceStore((s) => s.currentId);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(
      `/api/events/aggregate?experiment=${encodeURIComponent(experiment)}`,
      { headers: buildWorkspaceHeader() }
    )
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
  }, [experiment, currentWorkspaceId]);

  return (
    <div className="space-y-3">
      <header className="flex items-center justify-between gap-2 flex-wrap">
        <div className="flex items-center gap-2">
          <RiBarChart2Line size={14} className="text-secondary" />
          <span className="text-sm font-bold text-primary">
            {experiment}
          </span>
          {loading && (
            <RiLoader4Line
              size={12}
              className="animate-spin text-secondary"
            />
          )}
        </div>
        <div className="flex items-center gap-2">
          {decision && (
            <span
              className="inline-flex items-center gap-1 text-[10px] uppercase tracking-wider font-bold px-2 py-0.5 rounded"
              style={{
                color: "var(--color-teal)",
                backgroundColor: "rgba(21, 97, 109, 0.12)",
              }}
            >
              <RiTrophyLine size={10} />
              Concluded · {decision.winner}
            </span>
          )}
          {data && (
            <span className="text-xs text-muted">
              {data.totalEvents} events
              {data.malformedLines > 0
                ? ` · ${data.malformedLines} malformed`
                : ""}
            </span>
          )}
        </div>
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
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="text-left text-[10px] uppercase tracking-wider text-muted">
                <th className="font-normal py-1 pr-3">Variant</th>
                {COLUMNS.map((c) => (
                  <th
                    key={c.key}
                    className="font-normal py-1 pr-3 text-right"
                  >
                    {c.label}
                  </th>
                ))}
                <th className="font-normal py-1 pr-3 text-right w-20">
                  {decision ? "" : "Promote"}
                </th>
              </tr>
            </thead>
            <tbody>
              {definition.variants.map((variant) => {
                const bucket = data.variants[variant] ?? null;
                const isWinner = decision?.winner === variant;
                return (
                  <tr key={variant} className="row-hover">
                    <td className="py-1.5 pr-3 font-bold text-primary">
                      {variant}
                      {isWinner && (
                        <RiTrophyLine
                          size={10}
                          className="inline ml-1"
                          style={{ color: "var(--color-teal)" }}
                        />
                      )}
                    </td>
                    {COLUMNS.map((c) => (
                      <td
                        key={c.key}
                        className="py-1.5 pr-3 text-right text-secondary"
                      >
                        {formatCell(bucket?.[c.key], c.format)}
                      </td>
                    ))}
                    <td className="py-1.5 pr-3 text-right">
                      {!decision ? (
                        <button
                          type="button"
                          onClick={() => promote(variant)}
                          className="text-[10px] font-bold px-2 py-0.5 rounded focus-ring"
                          style={{
                            color: "var(--color-teal)",
                            backgroundColor: "rgba(21, 97, 109, 0.08)",
                          }}
                          aria-label={`Promote ${variant} as winner`}
                        >
                          Promote
                        </button>
                      ) : isWinner ? (
                        <button
                          type="button"
                          onClick={resume}
                          className="inline-flex items-center gap-1 text-[10px] font-bold px-2 py-0.5 rounded focus-ring"
                          style={{
                            color: "var(--color-brandy)",
                            backgroundColor: "rgba(120, 41, 15, 0.08)",
                          }}
                          aria-label={`Resume ${experiment} experiment`}
                        >
                          <RiArrowGoBackLine size={10} />
                          Resume
                        </button>
                      ) : null}
                    </td>
                  </tr>
                );
              })}
              {data.unknownVariant.eventCount > 0 && (
                <tr className="row-hover">
                  <td className="py-1.5 pr-3 italic text-muted">
                    (unattributed)
                  </td>
                  {COLUMNS.map((c) => (
                    <td
                      key={c.key}
                      className="py-1.5 pr-3 text-right text-muted"
                    >
                      {formatCell(
                        data.unknownVariant[c.key],
                        c.format
                      )}
                    </td>
                  ))}
                  <td />
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}

      {data && Object.keys(data.variants).length === 0 && (
        <p className="text-xs text-muted">
          No telemetry yet. Trigger a few runs to populate the buckets.
        </p>
      )}
    </div>
  );
}

function formatCell(
  value: number | undefined,
  format?: "percent"
): string {
  if (value == null) return "—";
  if (format === "percent") {
    return `${Math.round(value * 100)}%`;
  }
  return String(value);
}
