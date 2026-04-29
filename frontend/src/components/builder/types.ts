export const BUILDER_STEPS = [
  "data",
  "configure",
  "validate",
  "execute",
  "review",
] as const;

export type BuilderStep = (typeof BUILDER_STEPS)[number];

export interface StepDefinition {
  id: BuilderStep;
  label: string;
  description: string;
}

export const STEP_DEFINITIONS: Record<BuilderStep, StepDefinition> = {
  data: {
    id: "data",
    label: "Select Data",
    description: "Pick a dataset or upload a new file.",
  },
  configure: {
    id: "configure",
    label: "Configure Rules",
    description: "Pick a template, tweak overrides.",
  },
  validate: {
    id: "validate",
    label: "Validate",
    description: "Confirm schema and rule compatibility.",
  },
  execute: {
    id: "execute",
    label: "Execute",
    description: "Run generation and observe progress.",
  },
  review: {
    id: "review",
    label: "Review",
    description: "Inspect outputs and decide next action.",
  },
};

export function isBuilderStep(value: string): value is BuilderStep {
  return (BUILDER_STEPS as readonly string[]).includes(value);
}

export function nextStep(step: BuilderStep): BuilderStep | null {
  const idx = BUILDER_STEPS.indexOf(step);
  return idx >= 0 && idx < BUILDER_STEPS.length - 1
    ? BUILDER_STEPS[idx + 1]
    : null;
}

export function prevStep(step: BuilderStep): BuilderStep | null {
  const idx = BUILDER_STEPS.indexOf(step);
  return idx > 0 ? BUILDER_STEPS[idx - 1] : null;
}
