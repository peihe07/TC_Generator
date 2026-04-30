"use client";

import {
  RiAlertLine,
  RiArrowLeftLine,
  RiArrowRightLine,
  RiCheckboxCircleFill,
  RiDatabase2Line,
} from "@remixicon/react";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

interface DatasetRow {
  id?: string;
  rowNum?: number;
  reqId?: string;
  testItem?: string;
  testSet?: string;
  testGroup?: string;
  preConditions?: string;
  inputTestData?: string;
  steps?: string;
  expectedResults?: string;
  specReference?: string | null;
  status?: string;
}

interface DatasetResponse {
  jobId: string;
  rowCount: number;
  projectName?: string | null;
  testGroup?: string | null;
  rows: DatasetRow[];
}

interface QualityAlert {
  level: "error" | "warning" | "info";
  message: string;
  count?: number;
}

const PREVIEW_FIELDS: Array<{ key: keyof DatasetRow; label: string }> = [
  { key: "reqId", label: "Req ID" },
  { key: "testItem", label: "Test Item" },
  { key: "testSet", label: "Test Set" },
  { key: "specReference", label: "Spec Reference" },
  { key: "preConditions", label: "Pre-Conditions" },
  { key: "inputTestData", label: "Input Test Data" },
  { key: "steps", label: "Test Procedure" },
  { key: "expectedResults", label: "Expected Result" },
];

function isFilled(value: unknown): boolean {
  if (value == null) return false;
  if (typeof value !== "string") return Boolean(value);
  return value.trim().length > 0;
}

function computeAlerts(rows: DatasetRow[]): QualityAlert[] {
  if (rows.length === 0) return [];
  const alerts: QualityAlert[] = [];

  const missingReq = rows.filter((r) => !isFilled(r.reqId)).length;
  if (missingReq > 0) {
    alerts.push({
      level: "error",
      message: `${missingReq} row(s) missing Req ID`,
      count: missingReq,
    });
  }

  const reqCounts = new Map<string, number>();
  for (const r of rows) {
    if (!isFilled(r.reqId)) continue;
    const k = r.reqId as string;
    reqCounts.set(k, (reqCounts.get(k) ?? 0) + 1);
  }
  const dupReqs = [...reqCounts.entries()].filter(([, n]) => n > 1);
  if (dupReqs.length > 0) {
    const total = dupReqs.reduce((a, [, n]) => a + n, 0);
    alerts.push({
      level: "warning",
      message: `${dupReqs.length} Req ID(s) appear in ${total} rows`,
      count: dupReqs.length,
    });
  }

  const missingTestItem = rows.filter((r) => !isFilled(r.testItem)).length;
  if (missingTestItem > 0) {
    alerts.push({
      level: "warning",
      message: `${missingTestItem} row(s) missing Test Item`,
      count: missingTestItem,
    });
  }

  const missingTestSet = rows.filter((r) => !isFilled(r.testSet)).length;
  if (missingTestSet > 0) {
    alerts.push({
      level: "info",
      message: `${missingTestSet} row(s) have no Test Set assigned (will fall through to AI grouping)`,
      count: missingTestSet,
    });
  }

  return alerts;
}

function computeSchema(rows: DatasetRow[]) {
  if (rows.length === 0) return [];
  return PREVIEW_FIELDS.map(({ key, label }) => {
    const filled = rows.filter((r) => isFilled(r[key])).length;
    const sample =
      rows.find((r) => isFilled(r[key]))?.[key] ?? null;
    return {
      key,
      label,
      filled,
      coverage: rows.length > 0 ? filled / rows.length : 0,
      sample: typeof sample === "string" ? sample.slice(0, 80) : sample,
    };
  });
}

export default function DatasetDetailView({ jobId }: { jobId: string }) {
  const [data, setData] = useState<DatasetResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/jobs/${encodeURIComponent(jobId)}/dataset`)
      .then(async (res) => {
        if (!res.ok) {
          const body = await res.json().catch(() => ({}));
          throw new Error(body.detail ?? `Status ${res.status}`);
        }
        return (await res.json()) as DatasetResponse;
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
  }, [jobId]);

  const schema = useMemo(
    () => (data ? computeSchema(data.rows) : []),
    [data],
  );
  const alerts = useMemo(
    () => (data ? computeAlerts(data.rows) : []),
    [data],
  );

  return (
    <div className="space-y-6">
      <Link
        href="/data"
        className="inline-flex items-center gap-1.5 text-sm text-secondary hover:text-primary focus-ring rounded"
      >
        <RiArrowLeftLine size={16} />
        Back to Data
      </Link>

      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="flex items-center gap-3">
          <span
            className="flex items-center justify-center w-12 h-12 rounded-lg shrink-0"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            <RiDatabase2Line size={24} />
          </span>
          <div>
            <h1 className="text-3xl font-bold text-primary">
              {data?.projectName ?? jobId}
            </h1>
            <code className="text-xs text-muted">{jobId}</code>
          </div>
        </div>
        <Link
          href={`/run-builder?dataset=${encodeURIComponent(jobId)}`}
          className="cta inline-flex items-center gap-1.5 text-sm"
        >
          Use in New Run <RiArrowRightLine size={16} />
        </Link>
      </header>

      {loading && (
        <div className="surface p-6 text-sm text-secondary">
          Loading dataset…
        </div>
      )}
      {error && (
        <div
          className="surface p-4 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          {error}
        </div>
      )}

      {data && (
        <>
          <section className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <Stat label="Rows" value={String(data.rowCount)} />
            <Stat
              label="Unique Req IDs"
              value={String(
                new Set(
                  data.rows
                    .map((r) => (isFilled(r.reqId) ? r.reqId : null))
                    .filter(Boolean),
                ).size,
              )}
            />
            <Stat
              label="Test Sets"
              value={String(
                new Set(
                  data.rows
                    .map((r) => (isFilled(r.testSet) ? r.testSet : null))
                    .filter(Boolean),
                ).size,
              )}
            />
            <Stat
              label="Test Group"
              value={data.testGroup ?? "—"}
            />
          </section>

          <section className="surface p-5 space-y-3">
            <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
              Quality Alerts
            </h2>
            {alerts.length === 0 ? (
              <div
                className="flex items-center gap-2 text-sm"
                style={{ color: "var(--color-teal)" }}
              >
                <RiCheckboxCircleFill size={16} />
                Schema looks clean — no missing identifiers or duplicates.
              </div>
            ) : (
              <ul className="space-y-2">
                {alerts.map((a, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-sm"
                    style={{ color: levelColor(a.level) }}
                  >
                    <RiAlertLine size={16} className="shrink-0 mt-0.5" />
                    <span className="text-primary">
                      <strong>{a.level.toUpperCase()}:</strong> {a.message}
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </section>

          <section className="surface p-5 space-y-3">
            <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
              Schema Preview
            </h2>
            <div className="overflow-x-auto">
              <table className="w-full text-xs">
                <thead>
                  <tr className="text-left text-[10px] uppercase tracking-wider text-muted">
                    <th className="font-normal py-1 pr-3">Column</th>
                    <th className="font-normal py-1 pr-3 w-24">Coverage</th>
                    <th className="font-normal py-1 pr-3 w-20 text-right">
                      Filled
                    </th>
                    <th className="font-normal py-1 pr-3">Sample</th>
                  </tr>
                </thead>
                <tbody>
                  {schema.map((col) => {
                    const pct = Math.round(col.coverage * 100);
                    return (
                      <tr key={String(col.key)} className="row-hover">
                        <td className="py-1.5 pr-3 text-primary font-bold">
                          {col.label}
                        </td>
                        <td className="py-1.5 pr-3">
                          <div className="flex items-center gap-2">
                            <div
                              className="h-1.5 rounded-full overflow-hidden flex-1"
                              style={{
                                backgroundColor: "rgba(21, 97, 109, 0.15)",
                              }}
                            >
                              <div
                                className="h-full"
                                style={{
                                  width: `${pct}%`,
                                  backgroundColor:
                                    pct >= 90
                                      ? "var(--color-teal)"
                                      : pct >= 50
                                      ? "var(--color-tangerine)"
                                      : "var(--color-brandy)",
                                }}
                              />
                            </div>
                            <span className="text-secondary text-xs">
                              {pct}%
                            </span>
                          </div>
                        </td>
                        <td className="py-1.5 pr-3 text-right text-secondary">
                          {col.filled}/{data.rowCount}
                        </td>
                        <td className="py-1.5 pr-3 text-muted truncate max-w-0">
                          {col.sample ?? "—"}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </section>
        </>
      )}
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="surface p-4 space-y-1">
      <div className="text-[10px] uppercase tracking-wider text-secondary">
        {label}
      </div>
      <div className="text-lg font-bold text-primary truncate">{value}</div>
    </div>
  );
}

function levelColor(level: QualityAlert["level"]): string {
  switch (level) {
    case "error":
      return "var(--color-brandy)";
    case "warning":
      return "var(--color-tangerine)";
    default:
      return "var(--color-teal)";
  }
}
