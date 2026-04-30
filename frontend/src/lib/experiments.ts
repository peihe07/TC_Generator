export type ExperimentKey =
  | "home_layout_emphasis"
  | "runs_detail_mode"
  | "builder_split_layout";

export type ExperimentVariant =
  | "kpi_first"
  | "action_first"
  | "dedicated_page"
  | "inline_panel"
  | "fixed_preview"
  | "collapsible_preview";

export interface ExperimentDefinition {
  key: ExperimentKey;
  variants: readonly ExperimentVariant[];
  defaultVariant: ExperimentVariant;
}

export interface ExperimentAssignment {
  key: ExperimentKey;
  variant: ExperimentVariant;
  assignedAt: number;
  source: "bucket" | "override" | "default" | "concluded";
}

export interface ExperimentDecision {
  key: ExperimentKey;
  winner: ExperimentVariant;
  decidedAt: number;
  note?: string;
}

export const EXPERIMENT_DEFINITIONS: Record<
  ExperimentKey,
  ExperimentDefinition
> = {
  home_layout_emphasis: {
    key: "home_layout_emphasis",
    variants: ["kpi_first", "action_first"],
    defaultVariant: "kpi_first",
  },
  runs_detail_mode: {
    key: "runs_detail_mode",
    variants: ["dedicated_page", "inline_panel"],
    defaultVariant: "dedicated_page",
  },
  builder_split_layout: {
    key: "builder_split_layout",
    variants: ["fixed_preview", "collapsible_preview"],
    defaultVariant: "fixed_preview",
  },
};

export const EXPERIMENT_STORAGE_KEY = "tc:experiments:v1";
export const EXPERIMENT_DECISIONS_KEY = "tc:experiments:decisions:v1";

function canUseStorage(): boolean {
  return typeof window !== "undefined" && typeof localStorage !== "undefined";
}

function readAssignments(): Partial<Record<ExperimentKey, ExperimentAssignment>> {
  if (!canUseStorage()) return {};
  try {
    const parsed = JSON.parse(
      localStorage.getItem(EXPERIMENT_STORAGE_KEY) ?? "{}"
    );
    if (!parsed || typeof parsed !== "object") return {};
    return parsed as Partial<Record<ExperimentKey, ExperimentAssignment>>;
  } catch {
    return {};
  }
}

function writeAssignments(
  assignments: Partial<Record<ExperimentKey, ExperimentAssignment>>
) {
  if (!canUseStorage()) return;
  localStorage.setItem(EXPERIMENT_STORAGE_KEY, JSON.stringify(assignments));
}

function readDecisions(): Partial<Record<ExperimentKey, ExperimentDecision>> {
  if (!canUseStorage()) return {};
  try {
    const parsed = JSON.parse(
      localStorage.getItem(EXPERIMENT_DECISIONS_KEY) ?? "{}"
    );
    if (!parsed || typeof parsed !== "object") return {};
    return parsed as Partial<Record<ExperimentKey, ExperimentDecision>>;
  } catch {
    return {};
  }
}

function writeDecisions(
  decisions: Partial<Record<ExperimentKey, ExperimentDecision>>
) {
  if (!canUseStorage()) return;
  localStorage.setItem(EXPERIMENT_DECISIONS_KEY, JSON.stringify(decisions));
}

function hashString(value: string): number {
  let hash = 2166136261;
  for (let i = 0; i < value.length; i += 1) {
    hash ^= value.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function isVariant(
  definition: ExperimentDefinition,
  value: string | null | undefined
): value is ExperimentVariant {
  return Boolean(
    value && definition.variants.includes(value as ExperimentVariant)
  );
}

function readUrlOverride(key: ExperimentKey): ExperimentVariant | null {
  if (typeof window === "undefined") return null;
  const definition = EXPERIMENT_DEFINITIONS[key];
  const params = new URLSearchParams(window.location.search);
  const value = params.get(`exp_${key}`);
  return isVariant(definition, value) ? value : null;
}

export function resolveExperimentVariant(
  key: ExperimentKey,
  subjectId: string
): ExperimentVariant {
  const definition = EXPERIMENT_DEFINITIONS[key];
  const bucket = hashString(`${key}:${subjectId}`) % definition.variants.length;
  return definition.variants[bucket];
}

export function getExperimentAssignment(
  key: ExperimentKey,
  options: { subjectId?: string; override?: ExperimentVariant } = {}
): ExperimentAssignment {
  const definition = EXPERIMENT_DEFINITIONS[key];
  const override = options.override ?? readUrlOverride(key);
  if (override && isVariant(definition, override)) {
    const assignment: ExperimentAssignment = {
      key,
      variant: override,
      assignedAt: Date.now(),
      source: "override",
    };
    writeAssignments({ ...readAssignments(), [key]: assignment });
    return assignment;
  }

  // 已 concluded 的實驗：所有人服務 winner，不走 bucket，也不快取進 assignments。
  const decision = readDecisions()[key];
  if (decision && isVariant(definition, decision.winner)) {
    return {
      key,
      variant: decision.winner,
      assignedAt: decision.decidedAt,
      source: "concluded",
    };
  }

  const existing = readAssignments()[key];
  if (existing && isVariant(definition, existing.variant)) return existing;

  const variant = options.subjectId
    ? resolveExperimentVariant(key, options.subjectId)
    : definition.defaultVariant;
  const assignment: ExperimentAssignment = {
    key,
    variant,
    assignedAt: Date.now(),
    source: options.subjectId ? "bucket" : "default",
  };
  writeAssignments({ ...readAssignments(), [key]: assignment });
  return assignment;
}

export function getExperimentAssignments(): Partial<
  Record<ExperimentKey, ExperimentAssignment>
> {
  return readAssignments();
}

export function getExperimentVariantMap(): Partial<
  Record<ExperimentKey, ExperimentVariant>
> {
  const assignments = readAssignments();
  return Object.fromEntries(
    Object.entries(assignments).map(([key, assignment]) => [
      key,
      assignment.variant,
    ])
  ) as Partial<Record<ExperimentKey, ExperimentVariant>>;
}

export function clearExperimentAssignments(): void {
  if (!canUseStorage()) return;
  localStorage.removeItem(EXPERIMENT_STORAGE_KEY);
}

export function getExperimentDecisions(): Partial<
  Record<ExperimentKey, ExperimentDecision>
> {
  return readDecisions();
}

export function getExperimentDecision(
  key: ExperimentKey
): ExperimentDecision | null {
  return readDecisions()[key] ?? null;
}

export function setExperimentDecision(
  key: ExperimentKey,
  winner: ExperimentVariant,
  note?: string
): ExperimentDecision {
  const definition = EXPERIMENT_DEFINITIONS[key];
  if (!isVariant(definition, winner)) {
    throw new Error(`Invalid winner ${winner} for experiment ${key}`);
  }
  const decision: ExperimentDecision = {
    key,
    winner,
    decidedAt: Date.now(),
    ...(note ? { note } : {}),
  };
  writeDecisions({ ...readDecisions(), [key]: decision });
  return decision;
}

export function clearExperimentDecision(key: ExperimentKey): void {
  const next = { ...readDecisions() };
  delete next[key];
  writeDecisions(next);
}
