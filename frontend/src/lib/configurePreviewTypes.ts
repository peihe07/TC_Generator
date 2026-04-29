// Configure step API 回傳的 preview 型別，供 Builder grouping / spec matching 共用。

export type GroupPreviewState = {
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

export type MatchPreviewState = {
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
