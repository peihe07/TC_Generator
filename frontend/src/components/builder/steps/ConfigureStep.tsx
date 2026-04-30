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
  const budgetUsedPct =
    config.budgetLimit > 0
      ? Math.min(100, (estimatedCost / config.budgetLimit) * 100)
      : 0;
  const overBudget = estimatedCost > config.budgetLimit && config.budgetLimit > 0;

  return (
    <section className="surface p-5 space-y-4">
      <header className="flex items-start justify-between gap-4 flex-wrap">
        <div className="space-y-1">
          <h3 className="text-sm font-bold text-primary">Generation Summary</h3>
          <p className="text-xs text-secondary">
            Estimated calls and budget pressure before execution.
          </p>
        </div>
        <span
          className="text-[10px] uppercase tracking-wider font-bold px-2.5 py-1 rounded-md"
          style={{
            color: overBudget ? "var(--color-brandy)" : "var(--color-teal)",
            backgroundColor: overBudget
              ? "rgba(120, 41, 15, 0.1)"
              : "rgba(21, 97, 109, 0.1)",
          }}
        >
          {overBudget ? "Budget risk" : "Ready"}
        </span>
      </header>

      <div className="grid grid-cols-2 lg:grid-cols-4 gap-2.5 text-sm">
        <SummaryItem label="Rows loaded" value={String(tcRows.length)} />
        <SummaryItem label="Model" value={config.model} tone="teal" />
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
          tone="teal"
        />
        <SummaryItem
          label="Est. cost ceiling"
          value={`$${estimatedCost.toFixed(2)}`}
          tone={overBudget ? "brandy" : "tangerine"}
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

      {config.budgetLimit > 0 && (
        <div className="space-y-1.5">
          <div className="h-2 rounded-full overflow-hidden bg-[rgba(21,97,109,0.14)]">
            <div
              className="h-full rounded-full transition-all"
              style={{
                width: `${budgetUsedPct}%`,
                backgroundColor: overBudget
                  ? "var(--color-brandy)"
                  : "var(--color-tangerine)",
              }}
            />
          </div>
          <div className="flex items-center justify-between gap-3 text-[10px] uppercase tracking-wider text-muted">
            <span>Estimated budget use</span>
            <span>{budgetUsedPct.toFixed(0)}%</span>
          </div>
        </div>
      )}

      {overBudget && (
        <div
          className="text-xs px-3 py-2 rounded-md leading-relaxed"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          Estimated cost ${estimatedCost.toFixed(2)} exceeds the budget cap
          ${config.budgetLimit.toFixed(2)}. Generation will halt early when
          the cap is reached.
        </div>
      )}
    </section>
  );
}

function SummaryItem({
  label,
  value,
  tone = "ink",
}: {
  label: string;
  value: string;
  tone?: "ink" | "teal" | "tangerine" | "brandy";
}) {
  const color =
    tone === "teal"
      ? "var(--color-teal)"
      : tone === "tangerine"
      ? "var(--color-tangerine)"
      : tone === "brandy"
      ? "var(--color-brandy)"
      : "var(--color-ink)";
  return (
    <div
      className="rounded-md px-3 py-2.5 min-w-0"
      style={{ backgroundColor: "rgba(226, 222, 214, 0.5)" }}
    >
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold truncate" style={{ color }}>
        {value}
      </dd>
    </div>
  );
}
