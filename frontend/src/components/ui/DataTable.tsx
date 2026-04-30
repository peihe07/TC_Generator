"use client";

import { RiArrowDownSLine, RiArrowUpSLine } from "@remixicon/react";
import { useMemo, useState, type ReactNode } from "react";

export interface DataTableColumn<T> {
  /** Stable key for React + sort state. */
  id: string;
  header: ReactNode;
  /** Render cell content for a row. */
  cell: (row: T) => ReactNode;
  /** Sort accessor — return value used for comparison. Omit to disable sort. */
  sortBy?: (row: T) => number | string | null | undefined;
  /** Optional `width` style applied to th + td. */
  width?: string | number;
  align?: "left" | "right" | "center";
}

export interface DataTableProps<T> {
  rows: T[];
  columns: DataTableColumn<T>[];
  /** Stable id for each row (defaults to index). */
  rowKey?: (row: T, index: number) => string;
  /** Initial sort. Omit for unsorted. */
  defaultSort?: { columnId: string; direction: "asc" | "desc" };
  /** Empty-state node when rows.length === 0. */
  empty?: ReactNode;
  /** Extra className on the surface wrapper. */
  className?: string;
  /** Style hook for individual rows (e.g. archived dim). */
  rowStyle?: (row: T) => React.CSSProperties | undefined;
}

export default function DataTable<T>({
  rows,
  columns,
  rowKey,
  defaultSort,
  empty,
  className = "",
  rowStyle,
}: DataTableProps<T>) {
  const [sortColumnId, setSortColumnId] = useState<string | null>(
    defaultSort?.columnId ?? null,
  );
  const [sortDir, setSortDir] = useState<"asc" | "desc">(
    defaultSort?.direction ?? "desc",
  );

  const sortColumn = sortColumnId
    ? columns.find((c) => c.id === sortColumnId)
    : null;

  const displayRows = useMemo(() => {
    if (!sortColumn || !sortColumn.sortBy) return rows;
    const accessor = sortColumn.sortBy;
    const sorted = [...rows].sort((a, b) => {
      const av = accessor(a);
      const bv = accessor(b);
      if (av == null && bv == null) return 0;
      if (av == null) return 1;
      if (bv == null) return -1;
      if (typeof av === "number" && typeof bv === "number") return av - bv;
      return String(av).localeCompare(String(bv));
    });
    if (sortDir === "desc") sorted.reverse();
    return sorted;
  }, [rows, sortColumn, sortDir]);

  const toggleSort = (col: DataTableColumn<T>) => {
    if (!col.sortBy) return;
    if (col.id === sortColumnId) {
      setSortDir((d) => (d === "asc" ? "desc" : "asc"));
    } else {
      setSortColumnId(col.id);
      setSortDir("desc");
    }
  };

  if (rows.length === 0) {
    return (
      <div className={`surface p-10 text-center ${className}`}>
        {empty ?? <p className="text-sm text-muted">No rows.</p>}
      </div>
    );
  }

  return (
    <div className={`surface p-2 overflow-x-auto ${className}`}>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wider text-muted">
            {columns.map((col) => {
              const active = col.id === sortColumnId;
              const isSortable = !!col.sortBy;
              return (
                <th
                  key={col.id}
                  className="font-normal px-3 py-2"
                  style={{
                    width: col.width,
                    textAlign: col.align ?? "left",
                  }}
                >
                  {isSortable ? (
                    <button
                      type="button"
                      onClick={() => toggleSort(col)}
                      className="inline-flex items-center gap-1 uppercase text-xs tracking-wider focus-ring rounded"
                      style={{
                        color: active
                          ? "var(--color-ink)"
                          : "var(--color-teal)",
                        opacity: active ? 1 : 0.7,
                      }}
                    >
                      {col.header}
                      {active &&
                        (sortDir === "asc" ? (
                          <RiArrowUpSLine size={14} />
                        ) : (
                          <RiArrowDownSLine size={14} />
                        ))}
                    </button>
                  ) : (
                    col.header
                  )}
                </th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {displayRows.map((row, i) => {
            const key = rowKey ? rowKey(row, i) : String(i);
            const style = rowStyle?.(row);
            return (
              <tr key={key} className="row-hover" style={style}>
                {columns.map((col) => (
                  <td
                    key={col.id}
                    className="px-3 py-2.5"
                    style={{ textAlign: col.align ?? "left" }}
                  >
                    {col.cell(row)}
                  </td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
