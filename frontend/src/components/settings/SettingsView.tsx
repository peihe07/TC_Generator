"use client";

import { RiResetLeftLine, RiCheckLine } from "@remixicon/react";
import { useEffect, useMemo, useState } from "react";
import { MODEL_OPTIONS } from "../modules/configure/constants";
import {
  Section,
  RadioCard,
  Slider,
  NumberField,
  Toggle,
} from "../builder/steps/configure/shared";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { useWorkspaceSettingsStore } from "../../store/useWorkspaceSettingsStore";
import {
  aggregate,
  formatCost,
  formatDuration,
  formatPercent,
  toRuns,
} from "../../services/runAdapter";
import type { GenerationConfig } from "../../lib/types";

export default function SettingsView() {
  const settings = useWorkspaceSettingsStore((s) => s.settings);
  const loaded = useWorkspaceSettingsStore((s) => s.loaded);
  const loadFromStorage = useWorkspaceSettingsStore((s) => s.loadFromStorage);
  const update = useWorkspaceSettingsStore((s) => s.update);
  const reset = useWorkspaceSettingsStore((s) => s.reset);

  const records = useJobHistoryStore((s) => s.records);
  const historyLoaded = useJobHistoryStore((s) => s.loaded);
  const loadHistory = useJobHistoryStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!loaded) loadFromStorage();
    if (!historyLoaded) loadHistory();
  }, [loaded, loadFromStorage, historyLoaded, loadHistory]);

  const [savedFlash, setSavedFlash] = useState(false);
  const flash = () => {
    setSavedFlash(true);
    setTimeout(() => setSavedFlash(false), 1500);
  };

  const agg = useMemo(() => aggregate(toRuns(records)), [records]);

  return (
    <div className="space-y-6">
      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Settings</h1>
          <p className="text-secondary text-sm">
            Workspace defaults applied to new runs and overall stats.
          </p>
        </div>
        {savedFlash && (
          <span
            className="text-xs font-bold inline-flex items-center gap-1"
            style={{ color: "var(--color-teal)" }}
          >
            <RiCheckLine size={12} />
            Saved
          </span>
        )}
      </header>

      <Section title="Workspace Stats" defaultOpen hint="Aggregated from local job history.">
        <dl className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-sm">
          <Stat label="Total runs" value={String(agg.total)} />
          <Stat
            label="Success rate"
            value={agg.total > 0 ? formatPercent(agg.successRate) : "—"}
          />
          <Stat
            label="Avg duration"
            value={formatDuration(agg.avgDurationMs)}
          />
          <Stat label="Total spent" value={formatCost(agg.totalCost)} />
        </dl>
      </Section>

      <Section title="Run Defaults" hint="Applied when starting a new draft.">
        <div className="space-y-5">
          <div className="space-y-2">
            <SubLabel>Default Model</SubLabel>
            {MODEL_OPTIONS.map((opt) => (
              <RadioCard
                key={opt.id}
                name="default-model"
                value={opt.value}
                label={opt.label}
                checked={settings.defaultModel === opt.value}
                onChange={() => {
                  update({
                    defaultModel: opt.value as GenerationConfig["model"],
                  });
                  flash();
                }}
              />
            ))}
          </div>

          <Slider
            label="Default Batch Size"
            value={settings.defaultBatchSize}
            min={1}
            max={10}
            onChange={(v) => {
              update({ defaultBatchSize: v });
              flash();
            }}
            display={String(settings.defaultBatchSize)}
          />

          <Slider
            label="Default Max Budget (USD)"
            value={settings.defaultBudgetLimit}
            min={1}
            max={50}
            onChange={(v) => {
              update({ defaultBudgetLimit: v });
              flash();
            }}
            display={`$${settings.defaultBudgetLimit}`}
          />

          <NumberField
            label="Default Credit Balance (USD)"
            value={settings.defaultCreditBalance}
            placeholder="0 = hide remaining credit"
            onChange={(v) => {
              update({ defaultCreditBalance: v });
              flash();
            }}
            displayHint={
              settings.defaultCreditBalance > 0
                ? `$${settings.defaultCreditBalance.toFixed(2)} tracked`
                : "Not tracked"
            }
          />

          <Toggle
            label="Default Strict Validation"
            description="New runs start with strict validation enabled."
            checked={settings.defaultStrictValidation}
            onChange={(c) => {
              update({ defaultStrictValidation: c });
              flash();
            }}
          />
        </div>
      </Section>

      <Section title="Reset" defaultOpen={false}>
        <div className="flex items-center justify-between gap-3 flex-wrap">
          <p className="text-sm text-secondary">
            Restore all defaults to the original workspace values.
          </p>
          <button
            type="button"
            onClick={() => {
              if (window.confirm("Reset all settings?")) {
                reset();
                flash();
              }
            }}
            className="inline-flex items-center gap-1.5 px-3 py-2 rounded-md text-sm font-bold focus-ring transition-all"
            style={{
              backgroundColor: "rgba(120, 41, 15, 0.1)",
              color: "var(--color-brandy)",
            }}
          >
            <RiResetLeftLine size={14} />
            Reset to defaults
          </button>
        </div>
      </Section>
    </div>
  );
}

function SubLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
      {children}
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold text-primary truncate">{value}</dd>
    </div>
  );
}
