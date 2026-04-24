/**
 * Shared types for the QuickGenerate module. Kept separate so that pure
 * helpers (mockTc, constants) and UI sub-components can import them
 * without pulling the orchestrator's React state.
 */

export type JobPhase = 'idle' | 'decomposing' | 'generating' | 'done' | 'error';

export interface GeneratedTc {
  scenarioId: number;
  scenarioName?: string;
  tc: {
    tc_title: string;
    pre_conditions: string;
    input_test_data: string;
    test_procedure: string;
    expected_result: string;
    design_method: string;
    priority: string;
  };
}

export interface Scenario {
  id: number;
  name: string;
  description: string;
  test_item: string;
}

export interface Keyword {
  keyword: string;
  meaning: string;
  scenarios: number[];
}

export interface DecomposeAnalysis {
  reasoning: string;
  scenarios: Scenario[];
  keywords: Keyword[];
}
