// SSE event types emitted by POST /api/agent/chat
// Source of truth: backend/routes/agent.py + agent_dispatcher.py

export interface BaseAgentEvent {
  session_id: string;
}

export interface MessageEvent extends BaseAgentEvent {
  type: 'message';
  text: string;
}

export interface ToolCallEvent extends BaseAgentEvent {
  type: 'tool_call';
  call_id: string;
  tool: string;
  args: Record<string, unknown>;
}

export interface ToolResultEvent extends BaseAgentEvent {
  type: 'tool_result';
  call_id: string;
  tool: string;
  duration_ms: number;
  result: unknown;
}

export interface ToolErrorEvent extends BaseAgentEvent {
  type: 'tool_error';
  call_id: string;
  tool: string;
  error: { code: string; message: string; details?: unknown };
}

export interface RequireConfirmEvent extends BaseAgentEvent {
  type: 'require_confirm';
  call_id: string;
  tool: string;
  args: Record<string, unknown>;
  est_cost_usd: number;
}

export interface StateUpdateEvent extends BaseAgentEvent {
  type: 'state_update';
  job_id: string;
  tool: string;
}

export interface DoneEvent extends BaseAgentEvent {
  type: 'done';
  step_count: number;
}

export interface ErrorEvent extends BaseAgentEvent {
  type: 'error';
  code: string;
  message: string;
}

export type AgentEvent =
  | MessageEvent
  | ToolCallEvent
  | ToolResultEvent
  | ToolErrorEvent
  | RequireConfirmEvent
  | StateUpdateEvent
  | DoneEvent
  | ErrorEvent;

// ---- Tool result payload types (verified against backend/tools/*.py) ----

export interface ParseWorkbookResult {
  jobId: string;
  project: string;
  testGroup: string;
  rowCount: number;
  previewHeaders: string[];
  previewRows: Array<Record<string, unknown>>;
  rows: Array<Record<string, unknown>>;
  columnFillStatus: Record<string, number>;
  files: {
    rawFileName: string;
    referenceWorkbookName: string | null;
    specFileName: string | null;
    specFormat: string | null;
  };
}

export interface ListJobsResult {
  jobs: Array<{
    jobId: string;
    fileName: string;
    status: string;
    rowCount: number;
    testGroup: string | null;
    project: string | null;
  }>;
  total: number;
}

export interface EstimateCostResult {
  jobId: string;
  rowCount: number;
  model: string;
  batchSize: number;
  estCostUsd: number;
}

export interface GenerateTcResult {
  tcData: unknown[];
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
  model: string;
}

export interface ValidateTcResult {
  issues: Array<{
    id: string;
    severity: 'warning' | 'passing';
    field: string;
    message: string;
  }>;
  hasWarnings: boolean;
}

export interface MatchSpecResult {
  summary: {
    total: number;
    exact: number;
    fuzzy: number;
    unmatched: number;
    hasReferenceWorkbook: boolean;
  };
  matches: Array<{
    id: string | null;
    reqId: string | null;
    testItem: string | null;
    specReference: string | null;
    matchType: string | null;
    matchScore: number | null;
  }>;
}

export interface GroupTestsResult {
  groups: Array<{ testSet: string; count: number; reqIds: string[] }>;
  framework: Record<string, string[]>;
  assignments: Array<{
    id: string | null;
    reqId: string | null;
    testSet: string;
    source: 'existing' | 'derived';
  }>;
}

export interface WriteExcelResult {
  outputPath: string;
  rowsWritten: number;
  frameworkSheetWritten: boolean;
}

export interface InspectWorkbookResult {
  path: string;
  fileName: string;
  fileSizeBytes: number;
  sheets: string[];
  testGroup: string | null;
  rowsEstimate: number;
  hasTcSheet: boolean;
}

export interface GetJobValidationResult {
  total: number;
  pass: number;
  warnings: number;
  errors: 0;
  // Note: perRow uses snake_case — matches validate_tc input schema
  perRow: Array<{
    tc_id: string;
    test_item: string;
    pre_conditions: string;
    test_procedure: string;
    expected_result: string;
    design_method: string;
    priority: string;
  }>;
}

export type ToolResultByName = {
  parse_workbook: ParseWorkbookResult;
  group_tests: GroupTestsResult;
  match_spec: MatchSpecResult;
  generate_tc: GenerateTcResult;
  validate_tc: ValidateTcResult;
  write_excel: WriteExcelResult;
  inspect_workbook: InspectWorkbookResult;
  list_jobs: ListJobsResult;
  estimate_cost: EstimateCostResult;
  get_job_validation: GetJobValidationResult;
};

// ---- UI message model ----

export type UIMessage =
  | { kind: 'user'; id: string; text: string; ts: number }
  | { kind: 'agent'; id: string; parts: UIPart[]; ts: number };

export type UIPart = UITextPart | UIToolPart | UIConfirmPart;

export interface UITextPart {
  kind: 'text';
  text: string;
}

export interface UIToolPart {
  kind: 'tool';
  callId: string;
  tool: string;
  args: Record<string, unknown>;
  status: 'running' | 'ok' | 'error';
  result?: unknown;
  error?: { code: string; message: string };
  durationMs?: number;
}

export interface UIConfirmPart {
  kind: 'confirm';
  callId: string;
  tool: string;
  args: Record<string, unknown>;
  estCostUsd: number;
  status: 'pending' | 'accepted' | 'declined';
}

// ---- Session types ----

export interface SessionSummary {
  sessionId: string;
  totalCostUsd: number;
  createdAt: number;
  updatedAt: number;
  messageCount: number;
}

export interface SessionDetail extends SessionSummary {
  // OpenAI-format message history; converted to UIMessage[] by historyToMessages()
  history: Array<Record<string, unknown>>;
}
