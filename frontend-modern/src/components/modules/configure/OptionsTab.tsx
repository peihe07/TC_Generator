import React from 'react';
import type { GenerationConfig } from '../../../lib/types';
import { Checkbox, Radio } from '../../ui';
import { MODEL_OPTIONS, TARGET_COLUMN_OPTIONS } from './constants';

export interface OptionsTabProps {
  config: GenerationConfig;
  onUpdateConfig: (partial: Partial<GenerationConfig>) => void;
}

/**
 * Tab 3 — Options. Model radios, batch/budget sliders, strict-validation
 * toggle, and target-column checkboxes.
 */
export const OptionsTab: React.FC<OptionsTabProps> = ({ config, onUpdateConfig }) => (
  <div className="modern-configure-tab modern-options-tab">
    <section className="modern-configure-section modern-options-model-section">
      <div className="modern-configure-section-head">
        <p className="font-bold text-xs uppercase">AI Model</p>
        <span>{config.model}</span>
      </div>
      <div className="modern-options-model-grid">
        {MODEL_OPTIONS.map((opt) => (
          <label
            key={opt.id}
            className="modern-options-model-card"
            data-active={config.model === opt.value}
            htmlFor={opt.id}
          >
            <Radio
              id={opt.id}
              name="model"
              value={opt.value}
              label={null}
              checked={config.model === opt.value}
              onChange={() =>
                onUpdateConfig({ model: opt.value as GenerationConfig['model'] })
              }
              wrapperClassName="modern-options-radio"
            />
            <strong>{opt.label}</strong>
            <span>
              {opt.value === 'gpt-5.4'
                ? 'Higher reasoning budget for larger or ambiguous specs.'
                : 'Default generation model for normal TC batches.'}
            </span>
          </label>
        ))}
      </div>
      <p className="modern-options-note">
        Test Set classification uses a smaller internal model to keep grouping cheap.
      </p>
    </section>

    <section className="modern-configure-section">
      <div className="modern-configure-section-head">
        <p className="font-bold text-xs uppercase">Generation Limits</p>
        <span>Batch {config.batchSize}</span>
      </div>
      <div className="modern-options-limits-grid">
        <div className="modern-options-meter">
          <div>
            <span>Batch</span>
            <strong>{config.batchSize}</strong>
          </div>
          <div>
            <span>Budget</span>
            <strong>${config.budgetLimit}</strong>
          </div>
          <div>
            <span>Credits</span>
            <strong>{config.creditBalance > 0 ? `$${config.creditBalance.toFixed(2)}` : '-'}</strong>
          </div>
        </div>
        <div className="modern-options-controls">
          <label className="modern-options-control" htmlFor="batch-size">
            <span>Batch Size</span>
            <input
              id="batch-size"
              type="range"
            min="1"
            max="10"
              value={config.batchSize}
              onChange={(e) => onUpdateConfig({ batchSize: parseInt(e.target.value, 10) })}
            />
          </label>
          <label className="modern-options-control" htmlFor="budget">
            <span>Max Budget (USD)</span>
          <input
            id="budget"
            type="range"
            min="1"
            max="50"
            value={config.budgetLimit}
            onChange={(e) => onUpdateConfig({ budgetLimit: parseInt(e.target.value, 10) })}
          />
          </label>
          <label className="modern-options-control" htmlFor="credit-balance">
            <span>OpenAI Credit Balance (USD)</span>
          <input
            id="credit-balance"
            type="number"
            min="0"
            step="0.01"
            placeholder="0 = 不顯示剩餘額度"
            value={config.creditBalance || ''}
            onChange={(e) => {
              const v = parseFloat(e.target.value);
              onUpdateConfig({ creditBalance: Number.isFinite(v) && v > 0 ? v : 0 });
            }}
          />
          </label>
          <Checkbox
            id="strict-validation"
            label="Strict Validation"
            checked={config.strictValidation}
            onChange={(e) => onUpdateConfig({ strictValidation: e.target.checked })}
            wrapperClassName="modern-options-toggle"
          />
        </div>
      </div>
    </section>

    <section className="modern-configure-section">
      <div className="modern-configure-section-head">
        <p className="font-bold text-xs uppercase">Target Columns</p>
        <span>{config.targetColumns.length}/{TARGET_COLUMN_OPTIONS.length} selected</span>
      </div>
      <div className="modern-options-column-grid">
        {TARGET_COLUMN_OPTIONS.map(({ key, label }) => (
          <Checkbox
            key={key}
            id={key}
            label={label}
            checked={config.targetColumns.includes(key)}
            onChange={(e) => {
              const cols = e.target.checked
                ? [...config.targetColumns, key]
                : config.targetColumns.filter((c) => c !== key);
              onUpdateConfig({ targetColumns: cols });
            }}
            wrapperClassName="modern-options-column"
          />
        ))}
      </div>
    </section>
  </div>
);

export default OptionsTab;
