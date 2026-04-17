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
  inputTestData: string;
}

export interface TcRow {
  id: string;
  reqId: string;
  testGroup: string;
  testSet: string;
  testItem: string;
  specReference?: string | null;
  preConditions: string;
  inputTestData: string;
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
