import { Suspense } from "react";
import BuilderShell from "../../../src/components/builder/BuilderShell";

export default function RunBuilderPage() {
  return (
    <Suspense
      fallback={<div className="text-secondary">Loading builder...</div>}
    >
      <BuilderShell />
    </Suspense>
  );
}
