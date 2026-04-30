// Configure step 用的選項常數，供 Builder ConfigureOptions / Settings 共用。

export const TARGET_COLUMN_OPTIONS: { key: string; label: string }[] = [
  { key: "preConditions", label: "Pre-Conditions" },
  { key: "inputTestData", label: "Input Test Data" },
  { key: "steps", label: "Test Procedure" },
  { key: "expectedResults", label: "Expected Result" },
];

export const MODEL_OPTIONS: { id: string; value: string; label: string }[] = [
  { id: "m-gpt5", value: "gpt-5", label: "GPT-5 (Default)" },
  { id: "m-gpt54", value: "gpt-5.4", label: "GPT-5.4" },
];

// 平均每筆 req 的 prompt input token 數 + 每筆 TC 平均 output token 數，
// 跟後端 utils._estimate_token_cost 的常數對齊。
const MODEL_TOKEN_PRICING: Record<string, { input: number; output: number }> = {
  "gpt-5.4": { input: 2.5, output: 15 },
  "gpt-5": { input: 5, output: 15 },
};
const MODEL_TOKEN_PRICING_FALLBACK = { input: 5, output: 15 };
const AVG_TCS_PER_REQ = 2.5;
const AVG_INPUT_TOKENS_PER_REQ = 1500;
const AVG_OUTPUT_TOKENS_PER_TC = 800;

/** Estimate the cost ceiling for generating N rows on the given model. */
export function estimateGenerationCost(
  rowCount: number,
  model: string,
  extraCost = 0
): number {
  const pricing = MODEL_TOKEN_PRICING[model] ?? MODEL_TOKEN_PRICING_FALLBACK;
  const estInput = AVG_INPUT_TOKENS_PER_REQ * rowCount;
  const estOutput = Math.trunc(
    AVG_OUTPUT_TOKENS_PER_TC * AVG_TCS_PER_REQ * rowCount
  );
  const raw =
    extraCost +
    (estInput / 1_000_000) * pricing.input +
    (estOutput / 1_000_000) * pricing.output;
  return Number(raw.toFixed(4));
}

/** Estimated number of generation calls (1 per row, before splitting). */
export function estimateCallCount(rowCount: number): number {
  return rowCount;
}
