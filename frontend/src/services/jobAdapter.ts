"use client";

import type {
  GenerationConfig,
  AwaitingApplyFields,
  TcRow,
  UsageSummary,
  ValidationError,
} from "@/src/lib/types";
import { useJobHistoryStore } from "@/src/store/useJobHistoryStore";

const appApiBase = "/api";

type ParseJobResult = {
  jobMetadata: {
    jobId: string;
    projectName: string;
    createdAt: string;
    totalRows: number;
  };
  rows: TcRow[];
  stats: {
    total: number;
    processed: number;
    success: number;
    fail: number;
    cost: number;
  };
};

type GenerateCallbacks = {
  onStart?: (total: number) => void;
  onRow?: (row: TcRow, message: string) => void;
  // 當 AI 把一個 requirement 拆成多筆 TC 時，會針對 TC 2..N 各發一次 onRowAdded。
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  // AI 決定此 req 要拆成 N 筆，帶出拆分 reasoning（§1.2/§1.4/§1.5）與 keyword 分析。
  onReqSplit?: (info: {
    rowId: string;
    reqId: string;
    tcCount: number;
    reasoning: string;
    keywords: Array<{ keyword: string; meaning: string; covered_by: number[] }>;
    message: string;
  }) => void;
  onProgress?: (stats: {
    total: number;
    processed: number;
    success: number;
    fail: number;
    cost: number;
    inputTokens: number;
    outputTokens: number;
    cacheCreationTokens: number;
    cacheReadTokens: number;
  }) => void;
  onComplete?: (message: string) => void;
  onError?: (message: string) => void;
};

type RegenerateCallbacks = {
  onRow?: (rowId: string, data: AwaitingApplyFields) => void;
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  onReqSplit?: (info: {
    rowId: string;
    reqId: string;
    tcCount: number;
    reasoning: string;
    keywords: Array<{ keyword: string; meaning: string; covered_by: number[] }>;
    message: string;
  }) => void;
  onProgress?: (usage: UsageSummary) => void;
  onFail?: (rowId: string, message: string) => void;
  onComplete?: () => void;
  onError?: (message: string) => void;
};

type RerunCallbacks = {
  // Primary TC：覆蓋既有列（含 generated block + splitDecision metadata）
  onPrimary?: (row: TcRow, message: string) => void;
  // AI 把一筆需求拆成多筆 TC 時，TC 2..N 各發一次；前端依 parentId 插在 primary 之後
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  // 拆分 reasoning / keyword 分析
  onReqSplit?: (info: {
    rowId: string;
    reqId: string;
    tcCount: number;
    reasoning: string;
    keywords: Array<{ keyword: string; meaning: string; covered_by: number[] }>;
    message: string;
  }) => void;
  onProgress?: (usage: UsageSummary) => void;
  onFail?: (rowId: string, message: string) => void;
  onComplete?: () => void;
  onError?: (message: string) => void;
};

type ExportJobInput = {
  jobId: string | null;
  rows: TcRow[];
  scope: "all" | "accepted";
  outputMode: "new-file" | "overwrite";
  includeFrameworkSheet: boolean;
  selectedColumns: string[];
};

type GroupPreview = {
  groups: Array<{
    testSet: string;
    count: number;
    reqIds: string[];
  }>;
  assignments: Array<{
    id: string;
    reqId: string;
    testSet: string;
    source: "existing" | "derived";
  }>;
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
  model?: string;
};

type MatchPreview = {
  summary: {
    total: number;
    exact: number;
    fuzzy: number;
    unmatched: number;
    hasReferenceWorkbook: boolean;
  };
  matches: Array<{
    id: string;
    reqId: string;
    testItem: string;
    specReference: string | null;
    matchType: "exact" | "fuzzy" | "unmatched";
    matchScore?: number | null;
  }>;
};

function mapValidationErrors(
  validation: Array<Record<string, unknown>> | undefined,
): ValidationError[] {
  if (!validation?.length) {
    return [];
  }

  return validation
    .filter((issue) => issue.severity !== "passing")
    .map((issue) => ({
      severity: issue.severity === "warning" ? "warning" : "error",
      message: String(issue.message ?? "Validation issue."),
      column:
        typeof issue.field === "string" && issue.field.length
          ? issue.field
          : undefined,
    }));
}

function mapApiRowToTcRow(
  row: Record<string, unknown>,
  testGroup: string,
): TcRow {
  const generated =
    (row.generated as Record<string, unknown> | null | undefined) ?? null;
  const rawStatus = String(row.status ?? "");
  const status =
    rawStatus === "error"
      ? "fail"
      : generated
        ? "pending"
        : "pending";
  return {
    id: String(row.id ?? crypto.randomUUID()),
    rowNum:
      typeof row.rowNum === "number" ? row.rowNum : undefined,
    tcId: typeof row.tcId === "string" ? row.tcId : undefined,
    reqId: String(row.reqId ?? ""),
    testGroup,
    testSet: String(row.testSet ?? ""),
    testItem: String(row.testItem ?? ""),
    tcTitle: String(generated?.tcTitle ?? ""),
    reviewStatus:
      typeof row.reviewStatus === "string"
        ? (row.reviewStatus as TcRow["reviewStatus"])
        : "pending",
    specReference: (row.specReference ?? generated?.specReference ?? null) as string | null,
    preConditions: String(generated?.preConditions ?? ""),
    inputTestData: String(generated?.inputTestData ?? ""),
    steps: String(generated?.testProcedure ?? ""),
    expectedResults: String(generated?.expectedResult ?? ""),
    designMethod: String(
      generated?.designMethod ?? generated?.design_method ?? row.designMethod ?? "",
    ) || undefined,
    priority: String(generated?.priority ?? row.priority ?? "") || undefined,
    status,
    validationErrors: mapValidationErrors(
      row.validation as Array<Record<string, unknown>> | undefined,
    ),
    splitDecision: parseSplitDecision(row.splitDecision),
    splitWarning: typeof row.splitWarning === "string" ? row.splitWarning : undefined,
  };
}

function parseSplitDecision(raw: unknown): TcRow["splitDecision"] {
  if (!raw || typeof raw !== "object") return undefined;
  const obj = raw as Record<string, unknown>;
  const kwsRaw = Array.isArray(obj.keywords) ? obj.keywords : [];
  return {
    reqId: String(obj.reqId ?? ""),
    tcCount: Number(obj.tcCount ?? 1),
    reasoning: String(obj.reasoning ?? ""),
    keywords: kwsRaw.map((k) => {
      const o = k as Record<string, unknown>;
      return {
        keyword: String(o.keyword ?? ""),
        meaning: String(o.meaning ?? ""),
        coveredBy: Array.isArray(o.covered_by)
          ? (o.covered_by as unknown[]).map((n) => Number(n)).filter((n) => !Number.isNaN(n))
          : Array.isArray(o.coveredBy)
            ? (o.coveredBy as unknown[]).map((n) => Number(n)).filter((n) => !Number.isNaN(n))
            : [],
      };
    }),
    subIndex: typeof obj.subIndex === "number" ? obj.subIndex : undefined,
    parentId: typeof obj.parentId === "string" ? obj.parentId : undefined,
  };
}

function buildMockGeneratedRow(row: TcRow, index: number): TcRow {
  const hasWarning = index % 4 === 1;
  return {
    ...row,
    tcTitle: `(${row.testItem}) → Expected observable outcome is verified.`,
    reviewStatus: "pending",
    preConditions: hasWarning
      ? "1. Feature state prepared\n2. Operator logged in"
      : "1. Required feature enabled\n2. System idle",
    inputTestData: "NA",
    steps:
      "1. Prepare the source state.\n2. Trigger the target behavior.\n3. Verify the visible outcome.",
    expectedResults:
      "1. Preparation succeeds.\n2. Triggered behavior is accepted.\n3. Observable result matches the requirement.",
    status: "pending",
    validationErrors: hasWarning
      ? [
          {
            severity: "warning",
            message: "Verification wording should be tightened before export.",
            column: "steps",
          },
        ]
      : [],
  };
}

async function parseJsonResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let message = `Request failed with status ${response.status}.`;
    try {
      const body = (await response.clone().json()) as { detail?: unknown; message?: unknown };
      if (typeof body.detail === "string" && body.detail.trim()) {
        message = body.detail;
      } else if (typeof body.message === "string" && body.message.trim()) {
        message = body.message;
      }
    } catch {
      try {
        const text = await response.text();
        if (text.trim()) {
          message = text.trim();
        }
      } catch {
        // Keep the fallback status-only message.
      }
    }
    throw new Error(message);
  }
  return (await response.json()) as T;
}

export function isBackendConfigured() {
  return true;
}

export interface SpecLibraryEntry {
  name: string;
  sourceFile: string | null;
  entriesCount: number | null;
  embeddingModel: string | null;
  updatedAt: string | null;
}

export async function fetchSpecLibrary(): Promise<SpecLibraryEntry[]> {
  const response = await parseJsonResponse<{ specs: SpecLibraryEntry[] }>(
    await fetch(`${appApiBase}/spec-library`, { method: "GET" }),
  );
  return response.specs ?? [];
}

export async function parseJobFiles(input: {
  rawFile: File;
  referenceWorkbookFile?: File;
  specFile?: File;
  selectedSpecName?: string;
}): Promise<ParseJobResult> {
  const payload = new FormData();
  payload.append("raw_file", input.rawFile);
  if (input.referenceWorkbookFile) {
    payload.append("reference_file", input.referenceWorkbookFile);
  }
  if (input.specFile) {
    payload.append("spec_file", input.specFile);
  }
  if (input.selectedSpecName) {
    payload.append("selected_spec_name", input.selectedSpecName);
  }

  const response = await parseJsonResponse<{
    jobId: string;
    project: string | null;
    testGroup: string | null;
    rowCount: number;
    rows: Array<Record<string, unknown>>;
  }>(await fetch(`${appApiBase}/parse`, { method: "POST", body: payload }));

  const testGroup = response.testGroup ?? "Parsed";
  return {
    jobMetadata: {
      jobId: response.jobId,
      projectName:
        response.project ??
        input.rawFile.name.replace(/\.(xlsx|xlsm)$/i, "") ??
        "Parsed Project",
      createdAt: new Date().toISOString(),
      totalRows: response.rowCount,
    },
    rows: response.rows.map((row) => mapApiRowToTcRow(row, testGroup)),
    stats: {
      total: response.rowCount,
      processed: 0,
      success: 0,
      fail: 0,
      cost: 0,
    },
  };
}

export async function fetchGroupingPreview(input: {
  jobId: string | null;
  rows: TcRow[];
}): Promise<GroupPreview> {
  if (!input.jobId) {
    throw new Error("A parsed job is required before grouping preview can run.");
  }

  return parseJsonResponse<GroupPreview>(
    await fetch(`${appApiBase}/group`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jobId: input.jobId,
        rows: input.rows.map((row) => ({
          id: row.id,
          reqId: row.reqId,
          testItem: row.testItem,
          testSet: row.testSet,
        })),
      }),
    }),
  );
}

export async function fetchMatchPreview(input: {
  jobId: string | null;
  rows: TcRow[];
}): Promise<MatchPreview> {
  if (!input.jobId) {
    throw new Error("A parsed job is required before spec matching preview can run.");
  }

  return parseJsonResponse<MatchPreview>(
    await fetch(`${appApiBase}/match`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jobId: input.jobId,
        rows: input.rows.map((row) => ({
          id: row.id,
          reqId: row.reqId,
          testItem: row.testItem,
          testSet: row.testSet,
        })),
      }),
    }),
  );
}

export function startGeneration(
  input: {
    jobId: string | null;
    rows: TcRow[];
    config: GenerationConfig;
  },
  callbacks: GenerateCallbacks,
) {
  let stopped = false;
  let source: EventSource | null = null;
  let mockTimer: ReturnType<typeof setInterval> | null = null;

  // 追蹤 job 最新 stats 供 job.completed 時一次寫入歷史
  const startedAt = Date.now();
  const latestStats = {
    total: input.rows.length,
    processed: 0,
    cost: 0,
    inputTokens: 0,
    outputTokens: 0,
    cacheCreationTokens: 0,
    cacheReadTokens: 0,
  };
  const baseUsage = {
    cost: 0,
    inputTokens: 0,
    outputTokens: 0,
    cacheCreationTokens: 0,
    cacheReadTokens: 0,
  };
  let baseCaptured = false;
  const rowOutcomes = new Map<string, "success" | "fail">();
  let completedJobId: string | null = null;

  const recordHistory = () => {
    if (!completedJobId) return;
    useJobHistoryStore.getState().appendRecord({
      id: completedJobId,
      kind: 'generate',
      model: input.config.model,
      startedAt,
      finishedAt: Date.now(),
      rowsTotal: latestStats.total,
      rowsProcessed: latestStats.processed,
      cost: Number((latestStats.cost - baseUsage.cost).toFixed(4)),
      inputTokens: Math.max(latestStats.inputTokens - baseUsage.inputTokens, 0),
      outputTokens: Math.max(latestStats.outputTokens - baseUsage.outputTokens, 0),
      cacheReadTokens: Math.max(latestStats.cacheReadTokens - baseUsage.cacheReadTokens, 0),
      cacheCreationTokens: Math.max(latestStats.cacheCreationTokens - baseUsage.cacheCreationTokens, 0),
    });
  };

  const stop = () => {
    stopped = true;
    if (source) {
      source.close();
      source = null;
    }
    if (mockTimer) {
      clearInterval(mockTimer);
      mockTimer = null;
    }
  };

  const run = async () => {
    if (!input.rows.length) {
      callbacks.onError?.("No rows available for generation.");
      return;
    }

    callbacks.onStart?.(input.rows.length);

    if (input.jobId) {
      try {
        const createJobResponse = await parseJsonResponse<{
          jobId: string;
          totalRows: number;
          streamUrl: string;
        }>(
          await fetch(`${appApiBase}/generate`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              jobId: input.jobId,
              rows: input.rows.map((row) => ({
                id: row.id,
                // rowNum 必須一路帶到 backend，否則 SQLite 存成 null，export 時對不到 Excel 列。
                rowNum: row.rowNum ?? null,
                tcId: row.tcId ?? null,
                reqId: row.reqId,
                testItem: row.testItem,
                originalRequirement: row.testItem,
                testSet: row.testSet,
                specReference: row.specReference ?? null,
                priority: row.priority || undefined,
              })),
              config: {
                model: input.config.model,
                batchSize: input.config.batchSize,
                budget: input.config.budgetLimit,
                strictValidation: input.config.strictValidation,
                regenerateAll: Boolean(input.config.regenerateAll),
              },
            }),
          }),
        );

        source = new EventSource(createJobResponse.streamUrl);
        source.onmessage = (event) => {
          if (stopped) {
            return;
          }

          const data = JSON.parse(event.data) as Record<string, unknown>;
          const eventType = typeof data.type === "string" ? data.type : "";
          const eventRow =
            data.row && typeof data.row === "object"
              ? (data.row as Record<string, unknown>)
              : undefined;
          if (
            eventRow &&
            typeof eventRow.id === "string" &&
            (eventType === "row.completed" || eventType === "row.failed" || eventType === "row.added")
          ) {
            rowOutcomes.set(eventRow.id, eventType === "row.failed" ? "fail" : "success");
          }
          const stats = data.stats as Record<string, number> | undefined;
          if (stats) {
            if (!baseCaptured) {
              baseUsage.cost = Number(stats.currentCost ?? 0);
              baseUsage.inputTokens = Number(stats.inputTokens ?? 0);
              baseUsage.outputTokens = Number(stats.outputTokens ?? 0);
              baseUsage.cacheCreationTokens = Number(stats.cacheCreationTokens ?? 0);
              baseUsage.cacheReadTokens = Number(stats.cacheReadTokens ?? 0);
              baseCaptured = true;
            }
            let success = 0;
            let fail = 0;
            for (const outcome of rowOutcomes.values()) {
              if (outcome === "success") success += 1;
              else fail += 1;
            }
            latestStats.total = Number(stats.total ?? input.rows.length);
            latestStats.processed = Number(stats.processed ?? 0);
            latestStats.cost = Number(stats.currentCost ?? 0);
            latestStats.inputTokens = Number(stats.inputTokens ?? 0);
            latestStats.outputTokens = Number(stats.outputTokens ?? 0);
            latestStats.cacheCreationTokens = Number(stats.cacheCreationTokens ?? 0);
            latestStats.cacheReadTokens = Number(stats.cacheReadTokens ?? 0);
            callbacks.onProgress?.({
              total: latestStats.total,
              processed: latestStats.processed,
              success,
              fail,
              cost: latestStats.cost,
              inputTokens: latestStats.inputTokens,
              outputTokens: latestStats.outputTokens,
              cacheCreationTokens: latestStats.cacheCreationTokens,
              cacheReadTokens: latestStats.cacheReadTokens,
            });
          }

          if (typeof data.jobId === 'string') completedJobId = data.jobId;

          if ((data.type === "row.completed" || data.type === "row.failed") && data.row) {
            const apiRow = data.row as Record<string, unknown>;
            const row = mapApiRowToTcRow(
              data.type === "row.failed" ? { ...apiRow, status: "error" } : apiRow,
              input.rows.find((item) => item.id === apiRow.id)?.testGroup ?? "Generated",
            );
            callbacks.onRow?.(row, String(data.message ?? "Row updated."));
          }

          if (data.type === "row.added" && data.row) {
            // AI 把一個 req 拆成多筆 TC 時的第 2..N 筆。
            const apiRow = data.row as Record<string, unknown>;
            const parentId = String(apiRow.parentId ?? "");
            const parentRow = input.rows.find((item) => item.id === parentId);
            const row = mapApiRowToTcRow(
              apiRow,
              parentRow?.testGroup ?? "Generated",
            );
            callbacks.onRowAdded?.(row, parentId, String(data.message ?? "TC added."));
          }

          if (data.type === "req.split") {
            callbacks.onReqSplit?.({
              rowId: String(data.rowId ?? ""),
              reqId: String(data.reqId ?? ""),
              tcCount: Number(data.tcCount ?? 1),
              reasoning: String(data.reasoning ?? ""),
              keywords: Array.isArray(data.keywords)
                ? (data.keywords as Array<{ keyword: string; meaning: string; covered_by: number[] }>)
                : [],
              message: String(data.message ?? ""),
            });
          }

          if (data.type === "job.completed") {
            recordHistory();
            callbacks.onComplete?.(String(data.message ?? "Generation complete."));
            stop();
          }
        };

        source.onerror = () => {
          callbacks.onError?.("Live backend stream disconnected.");
          stop();
        };
        return;
      } catch {
        callbacks.onError?.("Backend generation failed. Falling back to local mock mode.");
      }
    }

    let processed = 0;
    let success = 0;
    let fail = 0;
    let cost = 0;

    mockTimer = setInterval(() => {
      if (stopped) {
        return;
      }

      const next = input.rows[processed];
      if (!next) {
        callbacks.onComplete?.("Mock generation complete.");
        stop();
        return;
      }

      const updated = buildMockGeneratedRow(next, processed);
      processed += 1;
      success += updated.validationErrors?.some((issue) => issue.severity === "error") ? 0 : 1;
      fail += updated.validationErrors?.some((issue) => issue.severity === "error") ? 1 : 0;
      cost = Number((cost + 0.018).toFixed(4));
      callbacks.onRow?.(updated, `Generated ${updated.reqId} in local preview mode.`);
      callbacks.onProgress?.({
        total: input.rows.length,
        processed,
        success,
        fail,
        cost,
        inputTokens: 0,
        outputTokens: 0,
        cacheCreationTokens: 0,
        cacheReadTokens: 0,
      });

      if (processed >= input.rows.length) {
        callbacks.onComplete?.("Mock generation complete.");
        stop();
      }
    }, 700);
  };

  void run();
  return { stop };
}

export async function regenerateRows(
  input: {
    jobId: string | null;
    rowIds: string[];
    rows: TcRow[];
    config: GenerationConfig;
    regenerateReason?: string;
  },
  callbacks: RegenerateCallbacks,
) {
  if (!input.rowIds.length) {
    return;
  }

  if (input.jobId) {
    const startedAt = Date.now();
    const latest = {
      total: input.rowIds.length, processed: 0, cost: 0,
      inputTokens: 0, outputTokens: 0,
      cacheCreationTokens: 0, cacheReadTokens: 0,
    };
    const baseUsage = {
      cost: 0,
      inputTokens: 0,
      outputTokens: 0,
      cacheCreationTokens: 0,
      cacheReadTokens: 0,
    };
    let baseCaptured = false;

    try {
      const response = await fetch(
        `${appApiBase}/jobs/${input.jobId}/regenerate/stream`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            rowIds: input.rowIds,
            rows: input.rows,
            regenerateReason: input.regenerateReason ?? "",
            config: {
              model: input.config.model,
              batchSize: input.config.batchSize,
              budget: input.config.budgetLimit,
              strictValidation: input.config.strictValidation,
            },
          }),
        },
      );

      if (!response.ok || !response.body) {
        throw new Error("Regenerate request failed.");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          break;
        }

        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split("\n\n");
        buffer = parts.pop() ?? "";

        for (const part of parts) {
          const line = part.replace(/^data: /, "").trim();
          if (!line) {
            continue;
          }

          const event = JSON.parse(line) as Record<string, unknown>;
          const stats = event.stats as Record<string, number> | undefined;
          if (stats) {
            if (!baseCaptured) {
              baseUsage.cost = Number(stats.currentCost ?? 0);
              baseUsage.inputTokens = Number(stats.inputTokens ?? 0);
              baseUsage.outputTokens = Number(stats.outputTokens ?? 0);
              baseUsage.cacheCreationTokens = Number(stats.cacheCreationTokens ?? 0);
              baseUsage.cacheReadTokens = Number(stats.cacheReadTokens ?? 0);
              baseCaptured = true;
            }
            latest.total = Number(stats.total ?? latest.total);
            latest.processed = Number(stats.processed ?? latest.processed);
            latest.cost = Number(stats.currentCost ?? latest.cost);
            latest.inputTokens = Number(stats.inputTokens ?? latest.inputTokens);
            latest.outputTokens = Number(stats.outputTokens ?? latest.outputTokens);
            latest.cacheCreationTokens = Number(stats.cacheCreationTokens ?? latest.cacheCreationTokens);
            latest.cacheReadTokens = Number(stats.cacheReadTokens ?? latest.cacheReadTokens);
            callbacks.onProgress?.({
              cost: latest.cost,
              inputTokens: latest.inputTokens,
              outputTokens: latest.outputTokens,
              cacheCreationTokens: latest.cacheCreationTokens,
              cacheReadTokens: latest.cacheReadTokens,
            });
          }

          if (event.type === "row.regenerated" && event.row) {
            const row = event.row as Record<string, unknown>;
            const generated =
              (row.generated as Record<string, unknown> | undefined) ?? {};
            callbacks.onRow?.(String(row.id), {
              preConditions: String(generated.preConditions ?? ""),
              inputTestData: String(generated.inputTestData ?? ""),
              steps: String(generated.testProcedure ?? ""),
              expectedResults: String(generated.expectedResult ?? ""),
            });
          } else if (event.type === "row.added" && event.row) {
            const apiRow = event.row as Record<string, unknown>;
            const parentId = String(apiRow.parentId ?? "");
            const parentRow = input.rows.find((item) => item.id === parentId);
            const row = mapApiRowToTcRow(apiRow, parentRow?.testGroup ?? "Generated");
            callbacks.onRowAdded?.(row, parentId, String(event.message ?? "TC added."));
          } else if (event.type === "req.split") {
            callbacks.onReqSplit?.({
              rowId: String(event.rowId ?? ""),
              reqId: String(event.reqId ?? ""),
              tcCount: Number(event.tcCount ?? 1),
              reasoning: String(event.reasoning ?? ""),
              keywords: Array.isArray(event.keywords)
                ? (event.keywords as Array<{ keyword: string; meaning: string; covered_by: number[] }>)
                : [],
              message: String(event.message ?? ""),
            });
          } else if (event.type === "row.regen_failed" && event.row) {
            const row = event.row as Record<string, unknown>;
            const validation =
              (row.validation as Array<Record<string, unknown>> | undefined) ?? [];
            callbacks.onFail?.(
              String(row.id),
              String(validation[0]?.message ?? "Re-generation failed."),
            );
          }
        }
      }

      // 寫入 history
      useJobHistoryStore.getState().appendRecord({
        id: `regen-${Date.now().toString(36)}`,
        kind: 'regenerate',
        model: input.config.model,
        startedAt,
        finishedAt: Date.now(),
        rowsTotal: latest.total,
        rowsProcessed: latest.processed,
        cost: Number((latest.cost - baseUsage.cost).toFixed(4)),
        inputTokens: Math.max(latest.inputTokens - baseUsage.inputTokens, 0),
        outputTokens: Math.max(latest.outputTokens - baseUsage.outputTokens, 0),
        cacheReadTokens: Math.max(latest.cacheReadTokens - baseUsage.cacheReadTokens, 0),
        cacheCreationTokens: Math.max(latest.cacheCreationTokens - baseUsage.cacheCreationTokens, 0),
      });

      callbacks.onComplete?.();
      return;
    } catch {
      callbacks.onError?.("Backend regenerate failed. Falling back to local preview mode.");
    }
  }

  input.rowIds.forEach((rowId, index) => {
    const row = input.rows.find((item) => item.id === rowId);
    if (!row) {
      return;
    }

    callbacks.onRow?.(rowId, {
      preConditions: row.preConditions || "1. Local preview environment ready",
      inputTestData: row.inputTestData || "NA",
      steps: `${row.steps || "1. Prepare the feature"}\n2. Re-run the targeted behavior`,
      expectedResults:
        row.expectedResults || "Visible output remains consistent after regeneration.",
    });

    if (index === input.rowIds.length - 1) {
      callbacks.onComplete?.();
    }
  });
}

/**
 * Re-run selected rows through the full generation pipeline（含需求解讀 / 拆分判斷）。
 * 和 regenerateRows 的差別：
 *   - 每筆 row 可能產生多筆 TC：primary 覆蓋原列，其餘以 row.added 事件接在 parent 之後
 *   - 會 emit req.split（讓 UI 顯示拆分 reasoning）
 *   - 不走 diff-apply preview：primary 直接覆寫
 */
export async function rerunRows(
  input: {
    jobId: string | null;
    rowIds: string[];
    rows: TcRow[];
    config: GenerationConfig;
    project?: string | null;
  },
  callbacks: RerunCallbacks,
) {
  if (!input.rowIds.length || !input.jobId) {
    callbacks.onError?.("Re-run requires an active backend job.");
    return;
  }

  // 後端 JOB_REGISTRY 可能已無此 job（backend 重啟 / DB 清空）—— 這兩個欄位
  // 讓 backend 在找不到 job 時仍能重建 context 繼續跑。
  const firstRow = input.rows.find((row) => input.rowIds.includes(row.id)) ?? input.rows[0];
  const fallbackTestGroup = firstRow?.testGroup ?? "";

  const startedAt = Date.now();
  const latest = {
    total: input.rowIds.length, processed: 0, cost: 0,
    inputTokens: 0, outputTokens: 0,
    cacheCreationTokens: 0, cacheReadTokens: 0,
  };
  const baseUsage = {
    cost: 0,
    inputTokens: 0,
    outputTokens: 0,
    cacheCreationTokens: 0,
    cacheReadTokens: 0,
  };
  let baseCaptured = false;

  try {
    const response = await fetch(
      `${appApiBase}/jobs/${input.jobId}/rerun/stream`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          rowIds: input.rowIds,
          rows: input.rows,
          project: input.project ?? null,
          testGroup: fallbackTestGroup,
          config: {
            model: input.config.model,
            batchSize: input.config.batchSize,
            budget: input.config.budgetLimit,
            strictValidation: input.config.strictValidation,
          },
        }),
      },
    );

    if (!response.ok || !response.body) {
      throw new Error("Re-run request failed.");
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split("\n\n");
      buffer = parts.pop() ?? "";

      for (const part of parts) {
        const line = part.replace(/^data: /, "").trim();
        if (!line) continue;

        const event = JSON.parse(line) as Record<string, unknown>;
        const stats = event.stats as Record<string, number> | undefined;
        if (stats) {
          if (!baseCaptured) {
            baseUsage.cost = Number(stats.currentCost ?? 0);
            baseUsage.inputTokens = Number(stats.inputTokens ?? 0);
            baseUsage.outputTokens = Number(stats.outputTokens ?? 0);
            baseUsage.cacheCreationTokens = Number(stats.cacheCreationTokens ?? 0);
            baseUsage.cacheReadTokens = Number(stats.cacheReadTokens ?? 0);
            baseCaptured = true;
          }
          latest.total = Number(stats.total ?? latest.total);
          latest.processed = Number(stats.processed ?? latest.processed);
          latest.cost = Number(stats.currentCost ?? latest.cost);
          latest.inputTokens = Number(stats.inputTokens ?? latest.inputTokens);
          latest.outputTokens = Number(stats.outputTokens ?? latest.outputTokens);
          latest.cacheCreationTokens = Number(stats.cacheCreationTokens ?? latest.cacheCreationTokens);
          latest.cacheReadTokens = Number(stats.cacheReadTokens ?? latest.cacheReadTokens);
          callbacks.onProgress?.({
            cost: latest.cost,
            inputTokens: latest.inputTokens,
            outputTokens: latest.outputTokens,
            cacheCreationTokens: latest.cacheCreationTokens,
            cacheReadTokens: latest.cacheReadTokens,
          });
        }

        if (event.type === "row.regenerated" && event.row) {
          // Rerun primary：用完整 TcRow 覆蓋既有列
          const apiRow = event.row as Record<string, unknown>;
          const parentRow = input.rows.find((item) => item.id === String(apiRow.id ?? ""));
          const row = mapApiRowToTcRow(apiRow, parentRow?.testGroup ?? "Generated");
          callbacks.onPrimary?.(row, String(event.message ?? "Row re-run."));
        } else if (event.type === "row.added" && event.row) {
          const apiRow = event.row as Record<string, unknown>;
          const parentId = String(apiRow.parentId ?? "");
          const parentRow = input.rows.find((item) => item.id === parentId);
          const row = mapApiRowToTcRow(apiRow, parentRow?.testGroup ?? "Generated");
          callbacks.onRowAdded?.(row, parentId, String(event.message ?? "TC added."));
        } else if (event.type === "req.split") {
          callbacks.onReqSplit?.({
            rowId: String(event.rowId ?? ""),
            reqId: String(event.reqId ?? ""),
            tcCount: Number(event.tcCount ?? 1),
            reasoning: String(event.reasoning ?? ""),
            keywords: Array.isArray(event.keywords)
              ? (event.keywords as Array<{ keyword: string; meaning: string; covered_by: number[] }>)
              : [],
            message: String(event.message ?? ""),
          });
        } else if (event.type === "row.regen_failed" && event.row) {
          const row = event.row as Record<string, unknown>;
          const validation =
            (row.validation as Array<Record<string, unknown>> | undefined) ?? [];
          callbacks.onFail?.(
            String(row.id),
            String(validation[0]?.message ?? "Re-run failed."),
          );
        }
      }
    }

    useJobHistoryStore.getState().appendRecord({
      id: `rerun-${Date.now().toString(36)}`,
      kind: 'rerun',
      model: input.config.model,
      startedAt,
      finishedAt: Date.now(),
      rowsTotal: latest.total,
      rowsProcessed: latest.processed,
      cost: Number((latest.cost - baseUsage.cost).toFixed(4)),
      inputTokens: Math.max(latest.inputTokens - baseUsage.inputTokens, 0),
      outputTokens: Math.max(latest.outputTokens - baseUsage.outputTokens, 0),
      cacheReadTokens: Math.max(latest.cacheReadTokens - baseUsage.cacheReadTokens, 0),
      cacheCreationTokens: Math.max(latest.cacheCreationTokens - baseUsage.cacheCreationTokens, 0),
    });

    callbacks.onComplete?.();
  } catch {
    callbacks.onError?.("Backend re-run failed.");
  }
}

export async function exportJob(input: ExportJobInput) {
  if (input.jobId) {
    const exportRows = input.rows.map((row) => ({
      id: row.id,
      rowNum: row.rowNum,
      tcId: row.tcId ?? row.id,
      reqId: row.reqId,
      testGroup: row.testGroup,
      testSet: row.testSet,
      testItem: row.testItem,
      specReference: row.specReference ?? null,
      reviewStatus:
        row.status === "accepted" || row.status === "rejected" || row.status === "flagged"
          ? row.status
          : (row.reviewStatus ?? "pending"),
      generated: row.tcTitle || row.preConditions || row.inputTestData || row.steps || row.expectedResults
        ? {
            tcTitle: row.tcTitle ?? "",
            preConditions: row.preConditions,
            inputTestData: row.inputTestData,
            testProcedure: row.steps,
            expectedResult: row.expectedResults,
            priority: row.priority ?? "",
            designMethod: row.designMethod ?? "",
            specReference: row.specReference ?? null,
          }
        : null,
    }));

    const response = await parseJsonResponse<{
      fileName: string;
      downloadUrl: string;
      exportedRows: number;
      fallbackTemplate?: boolean;
    }>(
      await fetch(`${appApiBase}/export`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          jobId: input.jobId,
          rows: exportRows,
          scope: input.scope,
          outputMode: input.outputMode,
          includeFrameworkSheet: input.includeFrameworkSheet,
          selectedColumns: input.selectedColumns,
        }),
      }),
    );

    return {
      status: "ready" as const,
      fileName: response.fileName,
      downloadUrl: response.downloadUrl,
      exportedRows: response.exportedRows,
      fallbackTemplate: Boolean(response.fallbackTemplate),
      simulated: false,
    };
  }

  await new Promise((resolve) => setTimeout(resolve, 900));
  const scopedRows =
    input.scope === "accepted"
      ? input.rows.filter((row) => row.status === "accepted")
      : input.rows;

  return {
    status: "ready" as const,
    fileName: `${input.jobId ?? "tc-generator"}_generated.xlsx`,
    downloadUrl: null,
    exportedRows: scopedRows.length,
    fallbackTemplate: false,
    simulated: true,
  };
}

export async function attachRawWorkbook(jobId: string, file: File): Promise<{
  rawFileName: string;
  size: number;
}> {
  const formData = new FormData();
  formData.append("raw_file", file);
  return parseJsonResponse<{ rawFileName: string; size: number }>(
    await fetch(`${appApiBase}/jobs/${encodeURIComponent(jobId)}/attach-raw`, {
      method: "POST",
      body: formData,
    }),
  );
}

export async function fetchSourceStatus(jobId: string): Promise<{
  hasSource: boolean;
  rawFileName: string | null;
}> {
  return parseJsonResponse<{ hasSource: boolean; rawFileName: string | null }>(
    await fetch(`${appApiBase}/jobs/${encodeURIComponent(jobId)}/source-status`, {
      method: "GET",
    }),
  );
}
