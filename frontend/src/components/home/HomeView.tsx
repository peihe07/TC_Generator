"use client";

import { useEffect, useMemo, useState } from "react";
import { aggregate, toRuns } from "../../services/runAdapter";
import { getExperimentAssignment } from "../../lib/experiments";
import { track } from "../../lib/telemetry";
import { useWorkspaceFilteredRecords } from "../../lib/useWorkspaceFiltered";
import ContinueDraft from "./ContinueDraft";
import KpiCards from "./KpiCards";
import QuickActions from "./QuickActions";
import RecentRuns from "./RecentRuns";

export default function HomeView() {
  const records = useWorkspaceFilteredRecords();
  const [homeLayoutVariant, setHomeLayoutVariant] = useState<
    "kpi_first" | "action_first"
  >("kpi_first");

  useEffect(() => {
    const assignment = getExperimentAssignment("home_layout_emphasis", {
      subjectId: "default-workspace",
    });
    setHomeLayoutVariant(assignment.variant);
    track("experiment_exposure", {
      experiment: assignment.key,
      variant: assignment.variant,
    });
  }, []);

  const runs = useMemo(() => toRuns(records), [records]);
  const agg = useMemo(() => aggregate(runs), [runs]);
  const actionFirst = homeLayoutVariant === "action_first";

  return (
    <div className="space-y-6">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Home</h1>
        <p className="text-secondary text-sm">
          Workflow status overview and quick action paths.
        </p>
      </header>

      {actionFirst ? (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div>
            <QuickActions />
          </div>
          <div className="lg:col-span-2 space-y-6">
            <ContinueDraft />
            <KpiCards agg={agg} />
          </div>
        </div>
      ) : (
        <>
          <KpiCards agg={agg} />
          <ContinueDraft />
        </>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className={actionFirst ? "lg:col-span-3" : "lg:col-span-2"}>
          <RecentRuns runs={runs} />
        </div>
        {!actionFirst && (
          <div>
            <QuickActions />
          </div>
        )}
      </div>
    </div>
  );
}
