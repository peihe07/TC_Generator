"use client";

import { useEffect, useMemo, useState } from "react";
import {
  estimateCallCount,
  estimateGenerationCost,
} from "../../../lib/configureConstants";
import { getExperimentAssignment } from "../../../lib/experiments";
import { track } from "../../../lib/telemetry";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../store/useJobStore";
import ConfigureGrouping from "./configure/ConfigureGrouping";
import ConfigureOptions from "./configure/ConfigureOptions";
import ConfigureSpecMatching from "./configure/ConfigureSpecMatching";

export default function ConfigureStep() {
  const tcRows = useJobStore((s) => s.tcRows);
  const config = useJobStore((s) => s.config);
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);
  const [splitVariant, setSplitVariant] = useState<
    "fixed_preview" | "collapsible_preview"
  >("fixed_preview");

  useEffect(() => {
    markStepComplete("configure", true);
  }, [markStepComplete]);

  useEffect(() => {
    const assignment = getExperimentAssignment("builder_split_layout", {
      subjectId: "default-workspace",
    });
    setSplitVariant(
      assignment.variant === "collapsible_preview"
        ? "collapsible_preview"
        : "fixed_preview",
    );
    track("experiment_exposure", {
      experiment: assignment.key,
      variant: assignment.variant,
    });
  }, []);

  // fixed_preview: all sections open by default. collapsible_preview: only
  // ConfigureOptions stays open; Grouping + SpecMatching collapse so the
  // step feels lighter on first arrival.
  const sectionsOpenByDefault = splitVariant === "fixed_preview";

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h2 className="text-xl font-bold text-primary">Configure Rules</h2>
        <p className="text-sm text-secondary">
          Set the model and limits, classify rows into Test Sets, and check
          spec traceability.
        </p>
      </header>

      <ConfigureOptions />
      <ConfigureGrouping defaultOpen={sectionsOpenByDefault} />
      <ConfigureSpecMatching defaultOpen={sectionsOpenByDefault} />

      <ConfigureSummary />
    </div>
  );
}

function ConfigureSummary() {
  const tcRows = useJobStore((s) => s.tcRows);
  const config = useJobStore((s) => s.config);
  const estimatedCost = useMemo(
    () => estimateGenerationCost(tcRows.length, config.model),
    [tcRows.length, config.model]
  );
  const estimatedCalls = estimateCallCount(tcRows.length);

  return (
    <section className="surface p-5 space-y-3">
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-sm">
        <SummaryItem label="Rows loaded" value={String(tcRows.length)} />
        <SummaryItem label="Model" value={config.model} />
        <SummaryItem
          label="Target columns"
          value={String(config.targetColumns.length)}
        />
        <SummaryItem
          label="Strict mode"
          value={config.strictValidation ? "On" : "Off"}
        />
        <SummaryItem
          label="Est. calls"
          value={String(estimatedCalls)}
        />
        <SummaryItem
          label="Est. cost ceiling"
          value={`$${estimatedCost.toFixed(2)}`}
        />
        <SummaryItem
          label="Budget cap"
          value={`$${config.budgetLimit.toFixed(2)}`}
        />
        <SummaryItem
          label="Batch size"
          value={String(config.batchSize)}
        />
      </div>
      {estimatedCost > config.budgetLimit && config.budgetLimit > 0 && (
        <div
          className="text-xs px-3 py-2 rounded-md"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          Estimated cost ${estimatedCost.toFixed(2)} exceeds the budget cap
          ${config.budgetLimit.toFixed(2)} — generation will halt early when
          the cap is reached.
        </div>
      )}
    </section>
  );
}

function SummaryItem({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold text-primary truncate">{value}</dd>
    </div>
  );
}
