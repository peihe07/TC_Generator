import { Suspense } from "react";
import RunsView from "../../../src/components/runs/RunsView";

export default function RunsPage() {
  return (
    <Suspense fallback={<div className="text-secondary">Loading runs...</div>}>
      <RunsView />
    </Suspense>
  );
}
