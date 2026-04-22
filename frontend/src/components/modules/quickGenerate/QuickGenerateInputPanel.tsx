import React from 'react';
import {
  RiArrowRightLine,
  RiCloseFill,
  RiRefreshLine,
} from '@remixicon/react';
import { Button, Select } from '../../ui';
import type { JobPhase } from './types';

const MODEL_OPTIONS = [
  { value: 'gpt-5.4', label: 'GPT-5.4' },
  { value: 'gpt-5.4-mini', label: 'GPT-5.4 mini' },
  { value: 'gpt-5.4-nano', label: 'GPT-5.4 nano' },
  { value: 'gpt-5', label: 'GPT-5' },
  { value: 'gpt-4.1', label: 'GPT-4.1' },
  { value: 'gpt-4.1-mini', label: 'GPT-4.1 mini' },
  { value: 'gpt-4o-mini', label: 'GPT-4o mini' },
];

export interface QuickGenerateInputPanelProps {
  testItem: string;
  context: string;
  model: string;
  phase: JobPhase;
  cost: number;
  onTestItemChange: (value: string) => void;
  onContextChange: (value: string) => void;
  onModelChange: (value: string) => void;
  onGenerate: () => void;
  onStop: () => void;
  onReset: () => void;
}

/**
 * Left column of QuickGenerate: requirement + optional context inputs,
 * model selector, Generate/Stop/Regenerate controls and cost readout.
 *
 * 統一為 auto-split 流程：給需求 → AI 判斷要幾筆 TC → 顯示拆解流程 → 最終總數。
 * 不再有 single / with_context / decompose 模式切換。
 */
export const QuickGenerateInputPanel: React.FC<QuickGenerateInputPanelProps> = ({
  testItem,
  context,
  model,
  phase,
  cost,
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
      {/* Requirement input */}
      <fieldset className="flex-1 flex flex-col overflow-hidden">
        <legend className="text-sm">Requirement</legend>
        <textarea
          className="flex-1 p-2 text-xs resize-none min-h-[120px] border-sunken"
          placeholder="貼上完整的 requirement 文字。預設使用 GPT-5.4 mini；也可切換到更高階或更便宜模型。AI 會依 ASPICE §1.2/§1.4/§1.5 判斷要拆成幾筆 TC。"
          value={testItem}
          onChange={(e) => onTestItemChange(e.target.value)}
          disabled={isRunning}
        />
      </fieldset>

      {/* Optional context */}
      <fieldset className="flex flex-col">
        <legend className="text-sm">Additional Context (optional)</legend>
        <textarea
          className="p-2 text-xs resize-none min-h-[60px] border-sunken"
          placeholder="系統限制、相關需求、測試環境等補充資訊，留空代表沒有額外情境。"
          value={context}
          onChange={(e) => onContextChange(e.target.value)}
          disabled={isRunning}
        />
      </fieldset>

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
            Analyse &amp; Generate
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
