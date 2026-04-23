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

// 測試案例設計方法 — 與 backend `validator.VALID_DESIGN_METHODS` 對齊。
// 修改這個清單前請先同步改 backend，否則 export 會在 validator 標 warning。
export const DESIGN_METHODS = [
  '功能測試 (Functional based ; no specific technique)',
  '狀態轉換 (State Transition Testing)',
  '決策表 (Decision Table Testing)',
  '等價劃分 (Equivalence Partitioning, EP)',
  '邊界值分析 (Boundary Value Analysis, BVA)',
  '組合測試 (Combinatorial Testing ; Pairwise / t-wise)',
  '情境 / 用例 (Scenario / Use Case Testing)',
  '負向測試 (Negative / Invalid)',
  '基礎故障注入 (Fault Injection Lite)',
] as const;

export type DesignMethod = (typeof DESIGN_METHODS)[number];

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
  // ASPICE §2 測試設計方法；型別故意寬鬆用 string 允許 AI 回傳 fuzzy 值，
  // UI 下拉選單會收斂到 DESIGN_METHODS 列表。
  designMethod?: string;
  priority?: string;
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
  model:
    | "gpt-5"
    | "gpt-5.4";
  batchSize: number;
  budgetLimit: number;
  /**
   * OpenAI credit balance (USD). 0 = 未設定（不顯示剩餘額度）。
   * CostMeter 會用 `creditBalance - stats.cost` 顯示剩下多少可用。
   */
  creditBalance: number;
  strictValidation: boolean;
  targetColumns: string[];
  // true 時強制對每列都叫 AI，即使 template 已有 pre/procedure/expected 也重跑。
  // 給使用者手動覆寫 RULES.md §499「preserve existing content」行為用。
  regenerateAll?: boolean;
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

export interface UsageSummary {
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
}
