import type { ConfigureTabId } from './types';

/** Tab bar definitions rendered in the 98.css `menu[role="tablist"]`. */
export const TABS: { id: ConfigureTabId; label: string }[] = [
  { id: 'tab1', label: 'Grouping' },
  { id: 'tab2', label: 'Spec Matching' },
  { id: 'tab3', label: 'Options' },
];

const MODEL_TOKEN_PRICING: Record<string, { input: number; output: number }> = {
  'gpt-5.4': { input: 2.5, output: 15 },
  'gpt-5.4-mini': { input: 0.75, output: 4.5 },
  'gpt-5.4-nano': { input: 0.2, output: 1.25 },
  'gpt-5': { input: 5, output: 15 },
  'gpt-4.1': { input: 2, output: 8 },
  'gpt-4.1-mini': { input: 0.4, output: 1.6 },
  'gpt-4o': { input: 2.5, output: 10 },
  'gpt-4o-mini': { input: 0.15, output: 0.6 },
};

const MODEL_TOKEN_PRICING_FALLBACK = { input: 0.75, output: 4.5 };
const AVG_TCS_PER_REQ = 2.5;
const AVG_INPUT_TOKENS_PER_REQ = 1500;
const AVG_OUTPUT_TOKENS_PER_TC = 800;

/** Target column checkboxes rendered in the Options tab. */
export const TARGET_COLUMN_OPTIONS: { key: string; label: string }[] = [
  { key: 'preConditions', label: 'Pre-Conditions' },
  { key: 'inputTestData', label: 'Input Test Data' },
  { key: 'steps', label: 'Test Procedure' },
  { key: 'expectedResults', label: 'Expected Result' },
];

/** Model radio options for the Options tab. */
export const MODEL_OPTIONS: { id: string; value: string; label: string }[] = [
  { id: 'm-gpt54m', value: 'gpt-5.4-mini', label: 'GPT-5.4 mini (Default, Balanced)' },
  { id: 'm-gpt54', value: 'gpt-5.4', label: 'GPT-5.4 (Best Quality)' },
  { id: 'm-gpt54n', value: 'gpt-5.4-nano', label: 'GPT-5.4 nano (Cheap)' },
  { id: 'm-gpt5', value: 'gpt-5', label: 'GPT-5 (Legacy Top Quality)' },
  { id: 'm-gpt41', value: 'gpt-4.1', label: 'GPT-4.1 (Legacy Stable)' },
  { id: 'm-gpt41m', value: 'gpt-4.1-mini', label: 'GPT-4.1 mini (Legacy Balanced)' },
  { id: 'm-gpt4om', value: 'gpt-4o-mini', label: 'GPT-4o mini (Cheapest)' },
];

/** Pure helper — compute the estimated cost ceiling for N rows on a model. */
export function estimateBudget(
  rowCount: number,
  model: string,
  budgetLimit: number,
  extraCost = 0,
): number {
  const pricing = MODEL_TOKEN_PRICING[model] ?? MODEL_TOKEN_PRICING_FALLBACK;
  const estInput = AVG_INPUT_TOKENS_PER_REQ * rowCount;
  const estOutput = Math.trunc(AVG_OUTPUT_TOKENS_PER_TC * AVG_TCS_PER_REQ * rowCount);
  const raw = Number((
    extraCost +
    (estInput / 1_000_000) * pricing.input +
    (estOutput / 1_000_000) * pricing.output
  ).toFixed(4));
  return budgetLimit > 0 ? raw : raw;
}
