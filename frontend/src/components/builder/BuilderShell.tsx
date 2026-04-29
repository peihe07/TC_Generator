"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useEffect, useMemo, useState } from "react";
import { useBuilderDraftStore } from "../../store/useBuilderDraftStore";
import { useJobStore } from "../../store/useJobStore";
import { useWorkspaceSettingsStore } from "../../store/useWorkspaceSettingsStore";
import BuilderActionBar from "./BuilderActionBar";
import BuilderStepper from "./BuilderStepper";
import ConfigureStep from "./steps/ConfigureStep";
import DataStep from "./steps/DataStep";
import ExecuteStep from "./steps/ExecuteStep";
import ReviewStep from "./steps/ReviewStep";
import ValidateStep from "./steps/ValidateStep";
import {
  BUILDER_STEPS,
  isBuilderStep,
  nextStep,
  prevStep,
  STEP_DEFINITIONS,
  type BuilderStep,
} from "./types";

function renderStepPanel(
  step: BuilderStep,
  onAdvance: () => void
): React.ReactNode {
  if (step === "data") return <DataStep onAdvance={onAdvance} />;
  if (step === "execute") return <ExecuteStep onAdvance={onAdvance} />;
  if (step === "configure") return <ConfigureStep />;
  if (step === "validate") return <ValidateStep />;
  if (step === "review") return <ReviewStep />;
  return null;
}

export default function BuilderShell() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const draft = useBuilderDraftStore((s) => s.draft);
  const loaded = useBuilderDraftStore((s) => s.loaded);
  const loadFromStorage = useBuilderDraftStore((s) => s.loadFromStorage);
  const startNew = useBuilderDraftStore((s) => s.startNew);
  const update = useBuilderDraftStore((s) => s.update);
  const clearDraft = useBuilderDraftStore((s) => s.clear);

  const wsSettings = useWorkspaceSettingsStore((s) => s.settings);
  const wsSettingsLoaded = useWorkspaceSettingsStore((s) => s.loaded);
  const loadWsSettings = useWorkspaceSettingsStore((s) => s.loadFromStorage);
  const updateJobConfig = useJobStore((s) => s.updateConfig);

  useEffect(() => {
    if (!wsSettingsLoaded) loadWsSettings();
  }, [wsSettingsLoaded, loadWsSettings]);

  const stepFromUrl = searchParams.get("step");

  const fromRunId = searchParams.get("from");
  const editRunId = searchParams.get("edit");
  const templateIdParam = searchParams.get("templateId");
  const sourceRunId = fromRunId || editRunId || null;
  const rerunMode: "rerun" | "edit" | null = fromRunId
    ? "rerun"
    : editRunId
    ? "edit"
    : null;

  // 載入 draft；沒有就開新的
  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  // 開新 draft 時把 workspace defaults 套到 job config
  const applyDefaults = () => {
    if (!wsSettingsLoaded) return;
    updateJobConfig({
      model: wsSettings.defaultModel,
      batchSize: wsSettings.defaultBatchSize,
      budgetLimit: wsSettings.defaultBudgetLimit,
      creditBalance: wsSettings.defaultCreditBalance,
      strictValidation: wsSettings.defaultStrictValidation,
    });
  };

  useEffect(() => {
    if (!loaded) return;
    // 從 Run Detail 帶 source runId 來：若不是當前 draft 的來源 → 開新 draft
    if (sourceRunId && draft?.sourceRunId !== sourceRunId) {
      startNew();
      applyDefaults();
      update({ sourceRunId, rerunMode: rerunMode ?? undefined });
      return;
    }
    // 從 Templates 帶 templateId 來：套到 configure
    if (
      templateIdParam &&
      draft?.configure?.templateId !== templateIdParam
    ) {
      if (!draft) startNew();
      update({
        configure: {
          ...(draft?.configure ?? {}),
          templateId: templateIdParam,
        },
      });
      return;
    }
    if (!draft) {
      startNew();
      applyDefaults();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [loaded, draft, sourceRunId, rerunMode, templateIdParam, startNew, update, wsSettingsLoaded]);

  const current: BuilderStep = useMemo(() => {
    if (stepFromUrl && isBuilderStep(stepFromUrl)) return stepFromUrl;
    return draft?.currentStep ?? "data";
  }, [stepFromUrl, draft]);

  // URL 與 draft.currentStep 同步：URL 為主，回填到 draft
  useEffect(() => {
    if (!draft) return;
    if (draft.currentStep !== current) {
      update({ currentStep: current });
    }
  }, [current, draft, update]);

  const [savedFlash, setSavedFlash] = useState(false);

  const goTo = useCallback(
    (step: BuilderStep) => {
      const params = new URLSearchParams(searchParams);
      params.set("step", step);
      router.replace(`/run-builder?${params.toString()}`, { scroll: false });
    },
    [router, searchParams]
  );

  const onNext = useCallback(() => {
    const n = nextStep(current);
    if (n) goTo(n);
  }, [current, goTo]);

  const onBack = useCallback(() => {
    const p = prevStep(current);
    if (p) goTo(p);
  }, [current, goTo]);

  const onSaveDraft = useCallback(() => {
    update({}); // touch updatedAt
    setSavedFlash(true);
    setTimeout(() => setSavedFlash(false), 1500);
  }, [update]);

  const onFinish = useCallback(() => {
    clearDraft();
    router.push("/runs");
  }, [clearDraft, router]);

  const def = STEP_DEFINITIONS[current];
  const panel = useMemo(
    () => renderStepPanel(current, onNext),
    [current, onNext]
  );

  // highest visited 從 completed flag 推
  const highestVisited = useMemo<BuilderStep>(() => {
    if (!draft?.completed) return current;
    let highest: BuilderStep = current;
    for (const s of BUILDER_STEPS) {
      if (draft.completed[s]) highest = s;
    }
    const hIdx = BUILDER_STEPS.indexOf(highest);
    const cIdx = BUILDER_STEPS.indexOf(current);
    return cIdx > hIdx ? current : highest;
  }, [draft, current]);

  if (!loaded || !draft) {
    return <div className="text-secondary">Loading builder...</div>;
  }

  return (
    <div className="space-y-4">
      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <div className="text-xs uppercase tracking-wider text-muted">
            Run Builder
          </div>
          <h1 className="text-3xl font-bold text-primary">{def.label}</h1>
          <p className="text-sm text-secondary">{def.description}</p>
        </div>
        <div className="text-xs text-muted text-right">
          <div>
            Draft <code>{draft.id}</code>
          </div>
          <div>
            {savedFlash
              ? "Saved ✓"
              : `Updated ${formatTime(draft.updatedAt)}`}
          </div>
        </div>
      </header>

      {draft.sourceRunId && (
        <div
          className="surface px-4 py-2 text-xs flex items-center gap-2"
          style={{ color: "var(--color-teal)" }}
        >
          <span className="font-bold uppercase tracking-wider">
            {draft.rerunMode === "edit" ? "Editing run" : "Rerunning run"}
          </span>
          <code className="text-primary">{draft.sourceRunId}</code>
        </div>
      )}

      {draft.configure?.templateId && (
        <div
          className="surface px-4 py-2 text-xs flex items-center gap-2"
          style={{ color: "var(--color-teal)" }}
        >
          <span className="font-bold uppercase tracking-wider">
            Using template
          </span>
          <code className="text-primary">{draft.configure.templateId}</code>
        </div>
      )}

      <BuilderStepper
        current={current}
        highestVisited={highestVisited}
        onJump={goTo}
      />

      <div>{panel}</div>

      <BuilderActionBar
        current={current}
        blocked={
          current === "validate" && draft.completed?.validate === false
        }
        blockReason={
          current === "validate" && draft.completed?.validate === false
            ? "Resolve blocking checks first"
            : undefined
        }
        onBack={onBack}
        onNext={onNext}
        onSaveDraft={onSaveDraft}
        onFinish={onFinish}
      />
    </div>
  );
}

function formatTime(ts: number): string {
  const diff = Date.now() - ts;
  if (diff < 5_000) return "just now";
  if (diff < 60_000) return `${Math.floor(diff / 1000)}s ago`;
  if (diff < 3_600_000) return `${Math.floor(diff / 60_000)}m ago`;
  return new Date(ts).toLocaleString();
}
