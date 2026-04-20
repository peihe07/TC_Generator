export type TcStatus =
  | "pending"
  | "generating"
  | "success"
  | "fail"
  | "reviewing"
  | "accepted"
  | "rejected"
  | "flagged";

export interface AwaitingApplyFields {
  steps: string;
  expectedResults: string;
  preConditions: string;
  inputTestData: string;
}

export interface SplitKeyword {
  keyword: string;
  meaning: string;
  coveredBy: number[];
}

export interface SplitDecision {
  reqId: string;
  tcCount: number;
  reasoning: string;
  keywords: SplitKeyword[];
  // 0 = primary（該 req 的第 1 筆 TC），>=1 = sub TC 的序號
  subIndex?: number;
  // sub TC 回指到 primary 的 frontend row.id，用來在 UI 連結到主卡片
  parentId?: string;
}

export interface TcRow {
  id: string;
  rowNum?: number;
  tcId?: string;
  reqId: string;
  testGroup: string;
  testSet: string;
  testItem: string;
  testItemRewrite?: string;
  reviewStatus?: "pending" | "accepted" | "rejected" | "flagged";
  specReference?: string | null;
  preConditions: string;
  inputTestData: string;
  steps: string;
  expectedResults: string;
  status: TcStatus;
  validationErrors?: ValidationError[];
  originalData?: Partial<TcRow>;
  awaitingApply?: AwaitingApplyFields;
  // 由 req.split SSE 事件填入：AI 決定把這個 req 拆成 N 筆的理由 + keyword 分析。
  // 所有 TC（primary + sub）都會帶 splitDecision，但 sub 只有 subIndex/parentId 這種
  // 小資訊欄；完整 reasoning / keywords 僅放在 primary 上。
  splitDecision?: SplitDecision;
  // §1.4 / §1.2 啟發式 warning — AI 沒照規則拆時 backend 會標注，primary 才顯示。
  splitWarning?: string;
}

export interface ValidationError {
  severity: "error" | "warning" | "info";
  message: string;
  column?: string;
}

export interface JobMetadata {
  jobId: string;
  projectName: string;
  createdAt: string;
  totalRows: number;
}

export interface GenerationConfig {
  model: "gpt-5" | "gpt-5-mini" | "gpt-4.1" | "gpt-4.1-mini" | "gpt-4o" | "gpt-4o-mini";
  batchSize: number;
  budgetLimit: number;
  strictValidation: boolean;
  targetColumns: string[];
}

export interface JobLog {
  timestamp: string;
  level: "info" | "warn" | "error" | "success";
  message: string;
}

export interface JobStats {
  total: number;
  processed: number;
  success: number;
  fail: number;
  cost: number;       // USD
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
}
