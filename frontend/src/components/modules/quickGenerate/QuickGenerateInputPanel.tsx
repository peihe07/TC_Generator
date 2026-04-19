import React from 'react';
import {
  RiArrowRightLine,
  RiCloseFill,
  RiRefreshLine,
} from '@remixicon/react';
import { Button } from '../../ui';
import { MODE_CONFIG } from './constants';
import type { JobPhase, Mode } from './types';

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
        <legend className="font-bold text-sm">Mode</legend>
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
        <legend className="font-bold text-sm">
          {mode === 'decompose' ? 'Requirement Description' : 'Test Item'}
        </legend>
        <textarea
          className="flex-1 p-2 text-xs resize-none min-h-[100px] border-2 border-sunken"
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
          <legend className="font-bold text-sm">Additional Criteria / Context</legend>
          <textarea
            className="p-2 text-xs resize-none min-h-[80px] border-2 border-sunken"
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
        <select
          value={model}
          onChange={(e) => onModelChange(e.target.value)}
          disabled={isRunning}
        >
          <option value="gpt-5">GPT-5</option>
          <option value="gpt-4.1">GPT-4.1</option>
          <option value="gpt-4.1-mini">GPT-4.1 mini</option>
          <option value="gpt-4o-mini">GPT-4o mini</option>
        </select>
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
            className="flex-1 py-2 flex items-center justify-center gap-2 text-sm font-bold default"
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
        <div className="text-[10px] text-gray-500 text-right font-mono">
          Cost: ${cost.toFixed(4)}
        </div>
      )}
    </div>
  );
};

export default QuickGenerateInputPanel;
