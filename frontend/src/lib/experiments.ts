export type ExperimentKey = "home_layout_emphasis";

export type ExperimentVariant = "kpi_first" | "action_first";

export interface ExperimentDefinition {
  key: ExperimentKey;
  variants: readonly ExperimentVariant[];
  defaultVariant: ExperimentVariant;
}

export interface ExperimentAssignment {
  key: ExperimentKey;
  variant: ExperimentVariant;
  assignedAt: number;
  source: "bucket" | "override" | "default";
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
};

export const EXPERIMENT_STORAGE_KEY = "tc:experiments:v1";

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
