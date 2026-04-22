/**
 * Shared types for the Configure module tab previews. Kept separate so
 * hooks, tab panels, and the orchestrator share one source of truth.
 */

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
    source: 'existing' | 'derived';
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
    matchType: 'exact' | 'fuzzy' | 'unmatched';
    matchScore?: number | null;
  }>;
};

export type ConfigureTabId = 'tab1' | 'tab2' | 'tab3';
