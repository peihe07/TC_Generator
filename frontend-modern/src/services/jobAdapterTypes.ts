import type {
  AwaitingApplyFields,
  TcRow,
  UsageSummary,
} from "@/src/lib/types";

export type ParseJobResult = {
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

export type GenerateCallbacks = {
  onStart?: (total: number) => void;
  onRow?: (row: TcRow, message: string) => void;
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  onReqSplit?: (info: ReqSplitInfo) => void;
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

export type RegenerateCallbacks = {
  onRow?: (rowId: string, data: AwaitingApplyFields) => void;
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  onReqSplit?: (info: ReqSplitInfo) => void;
  onProgress?: (usage: UsageSummary) => void;
  onFail?: (rowId: string, message: string) => void;
  onComplete?: () => void;
  onError?: (message: string) => void;
};

export type RerunCallbacks = {
  onPrimary?: (row: TcRow, message: string) => void;
  onRowAdded?: (row: TcRow, parentId: string, message: string) => void;
  onReqSplit?: (info: ReqSplitInfo) => void;
  onProgress?: (usage: UsageSummary) => void;
  onFail?: (rowId: string, message: string) => void;
  onComplete?: (summary: RerunSummary) => void;
  onError?: (message: string) => void;
};

export type ReqSplitInfo = {
  rowId: string;
  reqId: string;
  tcCount: number;
  reasoning: string;
  keywords: Array<{ keyword: string; meaning: string; covered_by: number[] }>;
  message: string;
};

export interface RerunSummary {
  rowsUpdated: number;
  rowsAdded: number;
  rowsFailed: number;
}

export type ExportJobInput = {
  jobId: string | null;
  rows: TcRow[];
  scope: "all" | "accepted";
  outputMode: "new-file" | "overwrite";
  includeFrameworkSheet: boolean;
  selectedColumns: string[];
};

export type GroupPreview = {
  groups: Array<{
    testSet: string;
    count: number;
    reqIds: string[];
  }>;
  assignments: Array<{
    id: string;
    reqId: string;
    testSet: string;
    source: "existing" | "derived" | "fallback";
    needsReview?: boolean;
  }>;
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
  model?: string;
};

export type MatchPreview = {
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

export interface SpecLibraryEntry {
  name: string;
  sourceFile: string | null;
  entriesCount: number | null;
  embeddingModel: string | null;
  updatedAt: string | null;
}

export interface ReviewFixSuggestion {
  problemRootCause: string;
  affectedFields: string[];
  proposedChange: string;
  suggestedReason: string;
  model: string;
  cost: number;
  usage?: {
    input?: number;
    output?: number;
    cache_creation?: number;
    cache_read?: number;
  };
}
