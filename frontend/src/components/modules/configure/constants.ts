import type { ConfigureTabId } from './types';

/** Tab bar definitions rendered in the 98.css `menu[role="tablist"]`. */
export const TABS: { id: ConfigureTabId; label: string }[] = [
  { id: 'tab1', label: 'Grouping' },
  { id: 'tab2', label: 'Spec Matching' },
  { id: 'tab3', label: 'Options' },
];

/** Approximate per-row cost used for the budget ceiling estimate. */
export const MODEL_PRICING: Record<string, number> = {
  'gpt-5': 0.03,
  'gpt-4.1': 0.015,
  'gpt-4.1-mini': 0.004,
  'gpt-4o': 0.02,
  'gpt-4o-mini': 0.002,
};

/** Default fallback when a model is not in the pricing table. */
export const MODEL_PRICING_FALLBACK = 0.01;

/** Target column checkboxes rendered in the Options tab. */
export const TARGET_COLUMN_OPTIONS: { key: string; label: string }[] = [
  { key: 'preConditions', label: 'Pre-Conditions' },
  { key: 'inputTestData', label: 'Input Test Data' },
  { key: 'steps', label: 'Test Procedure' },
  { key: 'expectedResults', label: 'Expected Result' },
];

/** Model radio options for the Options tab. */
export const MODEL_OPTIONS: { id: string; value: string; label: string }[] = [
  { id: 'm-gpt5', value: 'gpt-5', label: 'GPT-5 (Top Quality)' },
  { id: 'm-gpt41', value: 'gpt-4.1', label: 'GPT-4.1 (Quality, Stable)' },
  { id: 'm-gpt41m', value: 'gpt-4.1-mini', label: 'GPT-4.1 mini (Balanced)' },
  { id: 'm-gpt4om', value: 'gpt-4o-mini', label: 'GPT-4o mini (Cheapest)' },
];

/** Pure helper — compute the estimated cost ceiling for N rows on a model. */
export function estimateBudget(
  rowCount: number,
  model: string,
  budgetLimit: number,
): number {
  const perRow = MODEL_PRICING[model] ?? MODEL_PRICING_FALLBACK;
  const raw = Number((rowCount * perRow).toFixed(2));
  return Math.min(budgetLimit, raw);
}
