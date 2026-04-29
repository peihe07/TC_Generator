"use client";

import { useEffect, useMemo } from "react";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { aggregate, toRuns } from "../../services/runAdapter";
import KpiCards from "./KpiCards";
import QuickActions from "./QuickActions";
import RecentRuns from "./RecentRuns";

export default function HomeView() {
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  const runs = useMemo(() => toRuns(records), [records]);
  const agg = useMemo(() => aggregate(runs), [runs]);

  return (
    <div className="space-y-6">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Home</h1>
        <p className="text-secondary text-sm">
          Workflow status overview and quick action paths.
        </p>
      </header>

      <KpiCards agg={agg} />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <RecentRuns runs={runs} />
        </div>
        <div>
          <QuickActions />
        </div>
      </div>
    </div>
  );
}
