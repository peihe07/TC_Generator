import type { GeneratedTc } from './types';

/**
 * Build a placeholder `GeneratedTc` used when the backend is unreachable
 * so the UI can still be exercised / demoed offline. Pure function — safe
 * to unit test without any React or network context.
 */
export function buildMockTc(
  scenarioId: number,
  scenarioName: string | undefined,
  testItem: string,
): GeneratedTc {
  return {
    scenarioId,
    scenarioName,
    tc: {
      test_item_rewrite: `(${testItem}) → Expected observable outcome is verified.`,
      pre_conditions:
        '1. System is in the required initial state.\n2. All prerequisite conditions are satisfied.',
      input_test_data: 'NA',
      test_procedure:
        '1. Prepare the required initial state.\n2. Execute the target operation.\n3. Verify the observable result matches the expected outcome.',
      expected_result:
        '1. Initial state preparation succeeds.\n2. Target operation is accepted by the system.\n3. Observable result matches the stated requirement.',
      design_method: 'Scenario',
      priority: 'Medium',
    },
  };
}
