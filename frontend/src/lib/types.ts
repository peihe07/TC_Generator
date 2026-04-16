export type WindowId =
  | "upload"
  | "configure"
  | "generate"
  | "review"
  | "export";

export type WindowPosition = {
  x: number;
  y: number;
};

export type WindowSize = {
  width: number;
  height: number;
};

export type WindowDefinition = {
  id: WindowId;
  title: string;
  description: string;
  icon: string;
  position: WindowPosition;
  size: WindowSize;
};

export type WindowState = WindowDefinition & {
  isOpen: boolean;
  isMinimized: boolean;
  zIndex: number;
};

export type LogLevel = "info" | "error";

export type JobLog = {
  timestamp: string;
  level: LogLevel;
  message: string;
};

export type TcPreviewRow = Record<string, string | number | null>;

export type TcRow = {
  id: string;
  rowNum?: number;
  tcId?: string;
  reqId: string;
  testItem: string;
  originalRequirement?: string;
  testSet?: string;
  specReference?: string;
  priority?: string;
  status?: "draft" | "ready" | "error";
  reviewStatus?: "pending" | "accepted" | "rejected" | "flagged";
  generated?: {
    testItemRewrite: string;
    preConditions: string;
    inputTestData?: string;
    testProcedure: string;
    expectedResult: string;
    designMethod: string;
    priority: string;
    specReference?: string;
  };
  validation?: ValidationIssue[];
};

export type ValidationSeverity = "critical" | "warning" | "passing";

export type ValidationIssue = {
  id: string;
  severity: ValidationSeverity;
  field: string;
  message: string;
};

export type JobFiles = {
  raw: File | null;
  spec: File | null;
  parsed: boolean;
};

export type JobConfig = {
  model: string;
  batchSize: number;
  budget: number;
  strictValidation: boolean;
};

export type JobStats = {
  total: number;
  processed: number;
  currentCost: number;
};
