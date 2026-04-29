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
