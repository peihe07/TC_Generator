"use client";

import Link from "next/link";
import { useState } from "react";
import { RiArrowDownSLine, RiArrowUpSLine } from "@remixicon/react";
import {
  formatCost,
  formatDuration,
  formatRelativeTime,
  STATUS_COLOR,
  STATUS_LABEL,
  type Run,
} from "../../services/runAdapter";

type SortKey = "startedAt" | "durationMs" | "cost";
type SortDir = "asc" | "desc";

export default function RunsTable({ runs }: { runs: Run[] }) {
  const [sortKey, setSortKey] = useState<SortKey>("startedAt");
  const [sortDir, setSortDir] = useState<SortDir>("desc");

  const sorted = [...runs].sort((a, b) => {
    const av = (a[sortKey] as number | null) ?? 0;
    const bv = (b[sortKey] as number | null) ?? 0;
    return sortDir === "asc" ? av - bv : bv - av;
  });

  const toggleSort = (key: SortKey) => {
    if (sortKey === key) {
      setSortDir(sortDir === "asc" ? "desc" : "asc");
    } else {
      setSortKey(key);
      setSortDir("desc");
    }
  };

  if (runs.length === 0) {
    return (
      <div className="surface p-10 text-center">
        <p className="text-sm text-muted">
          No runs match current filters.
        </p>
      </div>
    );
  }

  return (
    <div className="surface p-2 overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wider text-muted">
            <th className="font-normal px-3 py-2">Run</th>
            <th className="font-normal px-3 py-2">Status</th>
            <th className="font-normal px-3 py-2">Model</th>
            <SortableTh
              label="Duration"
              active={sortKey === "durationMs"}
              dir={sortDir}
              onClick={() => toggleSort("durationMs")}
            />
            <SortableTh
              label="Cost"
              active={sortKey === "cost"}
              dir={sortDir}
              onClick={() => toggleSort("cost")}
            />
            <SortableTh
              label="Started"
              active={sortKey === "startedAt"}
              dir={sortDir}
              onClick={() => toggleSort("startedAt")}
            />
            <th className="font-normal px-3 py-2 text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((r) => (
            <tr
              key={r.id}
              className="row-hover"
              style={{ borderRadius: 8 }}
            >
              <td className="px-3 py-2.5">
                <Link
                  href={`/runs/${r.id}`}
                  className="text-primary font-bold hover:underline"
                >
                  {r.kindLabel}
                </Link>
                <div className="text-xs text-muted truncate max-w-[260px]">
                  {r.id}
                </div>
              </td>
              <td className="px-3 py-2.5">
                <span
                  className="inline-flex items-center gap-1.5 text-xs font-bold"
                  style={{ color: STATUS_COLOR[r.status] }}
                >
                  <span
                    className="inline-block w-1.5 h-1.5 rounded-full"
                    style={{ backgroundColor: STATUS_COLOR[r.status] }}
                  />
                  {STATUS_LABEL[r.status]}
                </span>
              </td>
              <td className="px-3 py-2.5 text-secondary text-xs">
                {r.model}
              </td>
              <td className="px-3 py-2.5 text-secondary">
                {formatDuration(r.durationMs)}
              </td>
              <td className="px-3 py-2.5 text-secondary">
                {formatCost(r.cost)}
              </td>
              <td className="px-3 py-2.5 text-muted text-xs">
                {formatRelativeTime(r.startedAt)}
              </td>
              <td className="px-3 py-2.5 text-right">
                <Link
                  href={`/runs/${r.id}`}
                  className="text-xs font-bold focus-ring rounded px-2 py-1"
                  style={{ color: "var(--color-tangerine)" }}
                >
                  View →
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function SortableTh({
  label,
  active,
  dir,
  onClick,
}: {
  label: string;
  active: boolean;
  dir: SortDir;
  onClick: () => void;
}) {
  return (
    <th className="font-normal px-3 py-2">
      <button
        type="button"
        onClick={onClick}
        className="inline-flex items-center gap-1 uppercase text-xs tracking-wider focus-ring rounded"
        style={{
          color: active ? "var(--color-ink)" : "var(--color-teal)",
          opacity: active ? 1 : 0.7,
        }}
      >
        {label}
        {active &&
          (dir === "asc" ? (
            <RiArrowUpSLine size={14} />
          ) : (
            <RiArrowDownSLine size={14} />
          ))}
      </button>
    </th>
  );
}
