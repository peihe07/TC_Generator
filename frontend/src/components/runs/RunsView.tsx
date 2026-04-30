"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useMemo } from "react";
import {
  toRuns,
  type RunKind,
  type RunStatus,
} from "../../services/runAdapter";
import { useWorkspaceFilteredRecords } from "../../lib/useWorkspaceFiltered";
import RunFilters, { type RunFilterValue } from "./RunFilters";
import RunsTable from "./RunsTable";

function parseFilters(sp: URLSearchParams): RunFilterValue {
  return {
    status: (sp.get("status") as RunStatus | "all" | null) ?? "all",
    kind: (sp.get("kind") as RunKind | "all" | null) ?? "all",
    q: sp.get("q") ?? "",
  };
}

function buildQuery(value: RunFilterValue): string {
  const params = new URLSearchParams();
  if (value.status !== "all") params.set("status", value.status);
  if (value.kind !== "all") params.set("kind", value.kind);
  if (value.q.trim()) params.set("q", value.q.trim());
  const s = params.toString();
  return s ? `?${s}` : "";
}

export default function RunsView() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const records = useWorkspaceFilteredRecords();

  const filters = useMemo(
    () => parseFilters(searchParams),
    [searchParams]
  );

  const setFilters = useCallback(
    (next: RunFilterValue) => {
      router.replace(`/runs${buildQuery(next)}`, { scroll: false });
    },
    [router]
  );

  const allRuns = useMemo(() => toRuns(records), [records]);

  const filtered = useMemo(() => {
    const q = filters.q.toLowerCase();
    return allRuns.filter((r) => {
      if (filters.status !== "all" && r.status !== filters.status) return false;
      if (filters.kind !== "all" && r.kind !== filters.kind) return false;
      if (q && !r.id.toLowerCase().includes(q)) return false;
      return true;
    });
  }, [allRuns, filters]);

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
        </span>
      </header>

      <RunFilters value={filters} onChange={setFilters} />
      <RunsTable runs={filtered} />
    </div>
  );
}
