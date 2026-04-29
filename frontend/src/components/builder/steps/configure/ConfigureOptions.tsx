"use client";

import {
  MODEL_OPTIONS,
  TARGET_COLUMN_OPTIONS,
} from "../../../modules/configure/constants";
import type { GenerationConfig } from "../../../../lib/types";
import { useJobStore } from "../../../../store/useJobStore";
import {
  Section,
  RadioCard,
  CheckboxCard,
  Slider,
  NumberField,
  Toggle,
} from "./shared";

export default function ConfigureOptions() {
  const config = useJobStore((s) => s.config);
  const updateConfig = useJobStore((s) => s.updateConfig);

  return (
    <Section title="Options">
      <div className="space-y-5">
        <div className="space-y-2">
          <SubLabel>AI Model</SubLabel>
          {MODEL_OPTIONS.map((opt) => (
            <RadioCard
              key={opt.id}
              name="model"
              value={opt.value}
              label={opt.label}
              checked={config.model === opt.value}
              onChange={() =>
                updateConfig({
                  model: opt.value as GenerationConfig["model"],
                })
              }
            />
          ))}
          <p className="text-xs text-muted leading-relaxed">
            Test Set classification always runs on GPT-5 mini internally.
          </p>
        </div>

        <div className="space-y-3">
          <SubLabel>Generation Limits</SubLabel>
          <Slider
            label="Batch Size"
            value={config.batchSize}
            min={1}
            max={10}
            onChange={(v) => updateConfig({ batchSize: v })}
            display={String(config.batchSize)}
          />
          <Slider
            label="Max Budget (USD)"
            value={config.budgetLimit}
            min={1}
            max={50}
            onChange={(v) => updateConfig({ budgetLimit: v })}
            display={`$${config.budgetLimit}`}
          />
          <NumberField
            label="OpenAI Credit Balance (USD)"
            value={config.creditBalance}
            placeholder="0 = hide remaining credit"
            onChange={(v) => updateConfig({ creditBalance: v })}
            displayHint={
              config.creditBalance > 0
                ? `$${config.creditBalance.toFixed(2)} tracked`
                : "Not tracked"
            }
          />
          <Toggle
            label="Strict Validation"
            description="Block generation when critical errors are detected."
            checked={config.strictValidation}
            onChange={(c) => updateConfig({ strictValidation: c })}
          />
        </div>

        <div className="space-y-2">
          <SubLabel>Target Columns</SubLabel>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            {TARGET_COLUMN_OPTIONS.map(({ key, label }) => {
              const checked = config.targetColumns.includes(key);
              return (
                <CheckboxCard
                  key={key}
                  label={label}
                  checked={checked}
                  onChange={(c) => {
                    const cols = c
                      ? [...config.targetColumns, key]
                      : config.targetColumns.filter((col) => col !== key);
                    updateConfig({ targetColumns: cols });
                  }}
                />
              );
            })}
          </div>
        </div>
      </div>
    </Section>
  );
}

function SubLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
      {children}
    </div>
  );
}
