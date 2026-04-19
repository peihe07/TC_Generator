import React from 'react';
import type { GenerationConfig } from '../../../lib/types';
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
  <div className="flex flex-col gap-4">
    <fieldset>
      <legend>AI Model</legend>
      {MODEL_OPTIONS.map((opt) => (
        <div key={opt.id} className="field-row">
          <input
            type="radio"
            id={opt.id}
            name="model"
            checked={config.model === opt.value}
            onChange={() => onUpdateConfig({ model: opt.value as GenerationConfig['model'] })}
          />
          <label htmlFor={opt.id}>{opt.label}</label>
        </div>
      ))}
    </fieldset>

    <fieldset>
      <legend>Generation Limits</legend>
      <div className="flex flex-col gap-3">
        <div className="field-row-stacked">
          <label htmlFor="batch-size">Batch Size: {config.batchSize}</label>
          <input
            id="batch-size"
            type="range"
            min="1"
            max="10"
            value={config.batchSize}
            onChange={(e) => onUpdateConfig({ batchSize: parseInt(e.target.value, 10) })}
          />
        </div>
        <div className="field-row-stacked">
          <label htmlFor="budget">Max Budget (USD): ${config.budgetLimit}</label>
          <input
            id="budget"
            type="range"
            min="1"
            max="50"
            value={config.budgetLimit}
            onChange={(e) => onUpdateConfig({ budgetLimit: parseInt(e.target.value, 10) })}
          />
        </div>
        <div className="field-row">
          <input
            type="checkbox"
            id="strict-validation"
            checked={config.strictValidation}
            onChange={(e) => onUpdateConfig({ strictValidation: e.target.checked })}
          />
          <label htmlFor="strict-validation">Strict Validation</label>
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Target Columns</legend>
      <div className="flex flex-col gap-1">
        {TARGET_COLUMN_OPTIONS.map(({ key, label }) => (
          <div key={key} className="field-row">
            <input
              type="checkbox"
              id={key}
              checked={config.targetColumns.includes(key)}
              onChange={(e) => {
                const cols = e.target.checked
                  ? [...config.targetColumns, key]
                  : config.targetColumns.filter((c) => c !== key);
                onUpdateConfig({ targetColumns: cols });
              }}
            />
            <label htmlFor={key}>{label}</label>
          </div>
        ))}
      </div>
    </fieldset>
  </div>
);

export default OptionsTab;
