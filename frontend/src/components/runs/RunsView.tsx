"use client";

import {
  RiArchive2Line,
  RiInbox2Line,
  RiDownload2Line,
  RiCloseLine,
} from "@remixicon/react";
import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useEffect, useMemo, useState } from "react";
import { getExperimentAssignment } from "../../lib/experiments";
import { track } from "../../lib/telemetry";
import {
  formatCost,
  toRuns,
  type RunKind,
  type RunStatus,
} from "../../services/runAdapter";
import { useWorkspaceFilteredRecords } from "../../lib/useWorkspaceFiltered";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import RunFilters, { type RunFilterValue } from "./RunFilters";
import RunsTable from "./RunsTable";

function parseFilters(sp: URLSearchParams): RunFilterValue {
  return {
    status: (sp.get("status") as RunStatus | "all" | null) ?? "all",
    kind: (sp.get("kind") as RunKind | "all" | null) ?? "all",
    q: sp.get("q") ?? "",
    showArchived: sp.get("archived") === "1",
  };
}

function buildQuery(value: RunFilterValue): string {
  const params = new URLSearchParams();
  if (value.status !== "all") params.set("status", value.status);
  if (value.kind !== "all") params.set("kind", value.kind);
  if (value.q.trim()) params.set("q", value.q.trim());
  if (value.showArchived) params.set("archived", "1");
  const s = params.toString();
  return s ? `?${s}` : "";
}

export default function RunsView() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const records = useWorkspaceFilteredRecords();
  const bulkSetArchived = useJobHistoryStore((s) => s.bulkSetArchived);

  // Phase 4: detail-mode experiment exposure. The actual inline panel UI is
  // still being designed; this only registers the assignment so analytics
  // start collecting before the visual variant ships.
  useEffect(() => {
    const assignment = getExperimentAssignment("runs_detail_mode", {
      subjectId: "default-workspace",
    });
    track("experiment_exposure", {
      experiment: assignment.key,
      variant: assignment.variant,
    });
  }, []);

  const filters = useMemo(() => parseFilters(searchParams), [searchParams]);

  const setFilters = useCallback(
    (next: RunFilterValue) => {
      router.replace(`/runs${buildQuery(next)}`, { scroll: false });
    },
    [router]
  );

  const archivedIds = useMemo(
    () => new Set(records.filter((r) => r.archived).map((r) => r.id)),
    [records]
  );

  const allRuns = useMemo(() => toRuns(records), [records]);

  const filtered = useMemo(() => {
    const q = filters.q.toLowerCase();
    return allRuns.filter((r) => {
      const isArchived = archivedIds.has(r.id);
      if (!filters.showArchived && isArchived) return false;
      if (filters.status !== "all" && r.status !== filters.status) return false;
      if (filters.kind !== "all" && r.kind !== filters.kind) return false;
      if (q && !r.id.toLowerCase().includes(q)) return false;
      return true;
    });
  }, [allRuns, filters, archivedIds]);

  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());

  const toggleSelect = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };
  const toggleSelectAll = () => {
    setSelectedIds((prev) => {
      const allChecked = filtered.every((r) => prev.has(r.id));
      if (allChecked) {
        const next = new Set(prev);
        filtered.forEach((r) => next.delete(r.id));
        return next;
      }
      const next = new Set(prev);
      filtered.forEach((r) => next.add(r.id));
      return next;
    });
  };

  const selectionArray = Array.from(selectedIds);
  const selectionAllArchived =
    selectionArray.length > 0 &&
    selectionArray.every((id) => archivedIds.has(id));

  const archiveSelected = () => {
    if (selectionArray.length === 0) return;
    bulkSetArchived(selectionArray, true);
    setSelectedIds(new Set());
  };
  const unarchiveSelected = () => {
    if (selectionArray.length === 0) return;
    bulkSetArchived(selectionArray, false);
    setSelectedIds(new Set());
  };

  const exportMetadata = () => {
    if (selectionArray.length === 0) return;
    const subset = allRuns.filter((r) => selectedIds.has(r.id));
    const lines = [
      [
        "id",
        "kind",
        "model",
        "status",
        "startedAt",
        "finishedAt",
        "rowsTotal",
        "rowsProcessed",
        "cost",
        "durationMs",
      ].join(","),
      ...subset.map((r) =>
        [
          r.id,
          r.kindLabel,
          r.model,
          r.status,
          new Date(r.startedAt).toISOString(),
          r.finishedAt ? new Date(r.finishedAt).toISOString() : "",
          r.rowsTotal,
          r.rowsProcessed,
          formatCost(r.cost).replace(/[^0-9.\-]/g, ""),
          r.durationMs ?? "",
        ]
          .map((v) => `"${String(v ?? "").replace(/"/g, '""')}"`)
          .join(",")
      ),
    ];
    const blob = new Blob([lines.join("\n")], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `runs-metadata-${new Date()
      .toISOString()
      .replace(/[:.]/g, "-")}.csv`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="space-y-6">
      <header className="flex items-end justify-between">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Runs</h1>
          <p className="text-secondary text-sm">
            Operational visibility and job management.
          </p>
        </div>
        <span className="text-xs text-muted">
          {filtered.length} of {allRuns.length} runs
          {archivedIds.size > 0 && !filters.showArchived && (
            <> · {archivedIds.size} archived hidden</>
          )}
        </span>
      </header>

      <RunFilters value={filters} onChange={setFilters} />
      <RunsTable
        runs={filtered}
        archivedIds={archivedIds}
        selectedIds={selectedIds}
        onToggleSelect={toggleSelect}
        onToggleSelectAll={toggleSelectAll}
      />

      {selectedIds.size > 0 && (
        <div
          className="sticky bottom-4 z-30 surface-floating px-4 py-3 flex items-center justify-between gap-3 flex-wrap"
          style={{ borderRadius: 16 }}
        >
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => setSelectedIds(new Set())}
              className="flex items-center justify-center w-7 h-7 rounded-full focus-ring"
              style={{
                backgroundColor: "rgba(21, 97, 109, 0.12)",
                color: "var(--color-teal)",
              }}
              aria-label="Clear selection"
            >
              <RiCloseLine size={16} />
            </button>
            <span className="text-sm text-primary font-bold">
              {selectedIds.size} selected
            </span>
          </div>
          <div className="flex items-center gap-2 flex-wrap">
            {selectionAllArchived ? (
              <button
                type="button"
                onClick={unarchiveSelected}
                className="inline-flex items-center gap-1 text-xs px-3 py-1.5 rounded-md font-bold focus-ring"
                style={{
                  backgroundColor: "rgba(21, 97, 109, 0.12)",
                  color: "var(--color-teal)",
                }}
              >
                <RiInbox2Line size={12} />
                Unarchive
              </button>
            ) : (
              <button
                type="button"
                onClick={archiveSelected}
                className="inline-flex items-center gap-1 text-xs px-3 py-1.5 rounded-md font-bold focus-ring"
                style={{
                  backgroundColor: "rgba(21, 97, 109, 0.12)",
                  color: "var(--color-teal)",
                }}
              >
                <RiArchive2Line size={12} />
                Archive
              </button>
            )}
            <button
              type="button"
              onClick={exportMetadata}
              className="cta inline-flex items-center gap-1 text-xs px-3 py-1.5"
            >
              <RiDownload2Line size={12} />
              Export CSV
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

