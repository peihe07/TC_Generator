import React from 'react';
import {
  RiArrowRightLine,
  RiCloseFill,
  RiRefreshLine,
} from '@remixicon/react';
import { Button, Select } from '../../ui';
import { MODE_CONFIG } from './constants';
import type { JobPhase, Mode } from './types';

const MODEL_OPTIONS = [
  { value: 'gpt-5', label: 'GPT-5' },
  { value: 'gpt-4.1', label: 'GPT-4.1' },
  { value: 'gpt-4.1-mini', label: 'GPT-4.1 mini' },
  { value: 'gpt-4o-mini', label: 'GPT-4o mini' },
];

export interface QuickGenerateInputPanelProps {
  mode: Mode;
  testItem: string;
  context: string;
  model: string;
  phase: JobPhase;
  cost: number;
  onModeChange: (mode: Mode) => void;
  onTestItemChange: (value: string) => void;
  onContextChange: (value: string) => void;
  onModelChange: (value: string) => void;
  onGenerate: () => void;
  onStop: () => void;
  onReset: () => void;
}

/**
 * Left column of QuickGenerate: mode picker + text inputs + model +
 * Generate / Stop / Regenerate / Clear buttons + cost readout.
 */
export const QuickGenerateInputPanel: React.FC<QuickGenerateInputPanelProps> = ({
  mode,
  testItem,
  context,
  model,
  phase,
  cost,
  onModeChange,
  onTestItemChange,
  onContextChange,
  onModelChange,
  onGenerate,
  onStop,
  onReset,
}) => {
  const isRunning = phase === 'decomposing' || phase === 'generating';

  return (
    <div className="w-[320px] flex flex-col gap-2 shrink-0">
      {/* Mode selector */}
      <fieldset>
        <legend className="text-sm">Mode</legend>
        <div className="flex flex-col gap-1 p-1">
          {MODE_CONFIG.map((m) => {
            const active = mode === m.id;
            return (
              <label
                key={m.id}
                className="flex items-start gap-2 p-1 cursor-pointer"
                style={
                  active
                    ? {
                        background: 'var(--win95-select-bg)',
                        color: 'var(--win95-select-text)',
                      }
                    : {}
                }
              >
                <input
                  type="radio"
                  name="mode"
                  value={m.id}
                  checked={active}
                  onChange={() => onModeChange(m.id)}
                  className="mt-0.5"
                />
                <div>
                  <div className="flex items-center gap-1 text-xs font-bold">
                    {m.icon} {m.label}
                  </div>
                  <div
                    className="text-[10px]"
                    style={{
                      color: active
                        ? 'rgba(255,255,255,0.7)'
                        : 'var(--win95-gray-mid)',
                    }}
                  >
                    {m.desc}
                  </div>
                </div>
              </label>
            );
          })}
        </div>
      </fieldset>

      {/* Test Item input */}
      <fieldset className="flex-1 flex flex-col overflow-hidden">
        <legend className="text-sm">
          {mode === 'decompose' ? 'Requirement Description' : 'Test Item'}
        </legend>
        <textarea
          className="flex-1 p-2 text-xs resize-none min-h-[100px] border-sunken"
          placeholder={
            mode === 'decompose'
              ? 'Paste full requirement text. AI will identify distinct test scenarios...'
              : 'Enter the test item or condition to generate a TC for...'
          }
          value={testItem}
          onChange={(e) => onTestItemChange(e.target.value)}
          disabled={isRunning}
        />
      </fieldset>

      {/* Context input (only for with_context) */}
      {mode === 'with_context' && (
        <fieldset className="flex flex-col">
          <legend className="text-sm">Additional Criteria / Context</legend>
          <textarea
            className="p-2 text-xs resize-none min-h-[80px] border-sunken"
            placeholder="System constraints, related requirements, environment details..."
            value={context}
            onChange={(e) => onContextChange(e.target.value)}
            disabled={isRunning}
          />
        </fieldset>
      )}

      {/* Model selector */}
      <div className="field-row">
        <label className="text-xs font-bold">Model:</label>
        <Select
          value={model}
          onChange={(e) => onModelChange(e.target.value)}
          disabled={isRunning}
          options={MODEL_OPTIONS}
        />
      </div>

      {/* Generate / Stop buttons */}
      <div className="flex gap-2">
        {isRunning ? (
          <Button
            className="flex-1 flex items-center justify-center gap-2 font-bold"
            onClick={onStop}
          >
            <RiCloseFill className="size-4" /> Stop
          </Button>
        ) : (
          <Button
            className="flex-1 py-2 flex items-center justify-center gap-2 text-sm default"
            disabled={!testItem.trim()}
            onClick={onGenerate}
          >
            <RiArrowRightLine className="size-4" />
            {mode === 'decompose' ? 'Analyse & Generate' : 'Generate TC'}
          </Button>
        )}
        {(phase === 'done' || phase === 'error') && (
          <>
            <Button
              className="px-3 py-2 text-sm flex items-center gap-1 font-bold"
              onClick={onGenerate}
              disabled={!testItem.trim()}
              title="Regenerate with same input"
            >
              <RiRefreshLine className="size-4" /> Regenerate
            </Button>
            <Button
              className="px-3 py-2 text-sm flex items-center gap-1"
              onClick={onReset}
              title="Clear results"
              aria-label="Clear results"
            >
              <RiCloseFill className="size-4" />
            </Button>
          </>
        )}
      </div>

      {/* Cost display */}
      {cost > 0 && (
        <div
          className="text-[10px] text-right font-mono"
          style={{ color: 'var(--text-muted)' }}
        >
          Cost: ${cost.toFixed(4)}
        </div>
      )}
    </div>
  );
};

export default QuickGenerateInputPanel;
