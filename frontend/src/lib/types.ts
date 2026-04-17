export type TcStatus =
  | "pending"
  | "generating"
  | "success"
  | "fail"
  | "reviewing"
  | "accepted"
  | "rejected"
  | "flagged";

export interface PendingRegeneratedFields {
  steps: string;
  expectedResults: string;
  preConditions: string;
}

export interface TcRow {
  id: string;
  reqId: string;
  testGroup: string;
  testSet: string;
  testItem: string;
  preConditions: string;
  steps: string;
  expectedResults: string;
  status: TcStatus;
  validationErrors?: ValidationError[];
  originalData?: Partial<TcRow>;
  pendingRegenerated?: PendingRegeneratedFields;
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
  model: "claude-sonnet-4-6" | "claude-haiku-4-5-20251001";
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
}
