/**
 * Pre-action cost estimators.
 *
 * Configure already had `estimateBudget` for the Generate path; this module
 * extracts the same model + per-req averages so Generate / Regenerate /
 * Re-run can all surface a "Est. ~$X for N reqs" hint before the user
 * commits to a real AI call. Numbers are intentionally rough — they exist
 * so the reviewer has a sanity-check ballpark, not a billing contract.
 *
 * Pricing source: `backend/generator.py:MODEL_PRICING` (USD per 1M tokens).
 * If a model is not in the table we fall back to the gpt-5 rates so we
 * over-estimate rather than under-estimate.
 */

const PRICING: Record<string, { input: number; output: number }> = {
  'gpt-5':      { input: 5,    output: 15 },
  'gpt-5.4':    { input: 2.5,  output: 15 },
  'gpt-5-mini': { input: 0.25, output: 2 },
  'gpt-4.1':    { input: 2,    output: 8 },
  'gpt-4o':     { input: 2.5,  output: 10 },
};
const PRICING_FALLBACK = PRICING['gpt-5'];

// Empirical averages tuned for ASPICE TC generation prompts.
const AVG_INPUT_TOKENS_PER_REQ = 1500;
const AVG_OUTPUT_TOKENS_PER_TC = 800;
const AVG_TCS_PER_REQ_GENERATE = 2.5;   // 拆分常見 1.5–4，2.5 是中位數估值
const AVG_TCS_PER_REQ_REGENERATE = 1.2; // regenerate 多半維持原拆數，略保守

function priceFor(model: string) {
  return PRICING[model] ?? PRICING_FALLBACK;
}

function compute(reqCount: number, model: string, avgTcsPerReq: number): number {
  if (reqCount <= 0) return 0;
  const p = priceFor(model);
  const input = AVG_INPUT_TOKENS_PER_REQ * reqCount;
  const output = AVG_OUTPUT_TOKENS_PER_TC * avgTcsPerReq * reqCount;
  return Number(
    ((input / 1_000_000) * p.input + (output / 1_000_000) * p.output).toFixed(4),
  );
}

/**
 * Generate / first run estimate. Each requirement may be split into ~2.5 TCs
 * on average; output token count scales with that.
 */
export function estimateGenerateCost(reqCount: number, model: string): number {
  return compute(reqCount, model, AVG_TCS_PER_REQ_GENERATE);
}

/**
 * Regenerate estimate. Operates on already-split rows; output stays close
 * to ~1 TC per requested row, hence a smaller multiplier.
 */
export function estimateRegenerateCost(rowCount: number, model: string): number {
  return compute(rowCount, model, AVG_TCS_PER_REQ_REGENERATE);
}

/** Format helper used by callers to keep "Est. ~$X" copy consistent. */
export function formatEstimate(usd: number): string {
  if (usd <= 0) return '$0.0000';
  if (usd < 0.01) return `$${usd.toFixed(4)}`;
  if (usd < 1) return `$${usd.toFixed(3)}`;
  return `$${usd.toFixed(2)}`;
}
