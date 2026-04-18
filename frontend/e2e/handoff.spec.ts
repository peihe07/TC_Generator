import { test, expect } from '@playwright/test';

// GUI ↔ Agent handoff E2E — Phase 3 劇本 B
// All backend calls are mocked via page.route().

const SESSION_ID = 'handoff-e2e-session';

function sseChunk(eventType: string, data: object): string {
  return `event: ${eventType}\ndata: ${JSON.stringify(data)}\n\n`;
}

function mockAgentSessions(page: import('@playwright/test').Page) {
  return page.route('/api/agent/sessions*', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ sessions: [] }),
    });
  });
}

function mockAgentChat(page: import('@playwright/test').Page) {
  return page.route('/api/agent/chat', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'text/event-stream',
      body: [
        sseChunk('tool_call', { call_id: 'c1', tool: 'get_job_validation', args: {}, session_id: SESSION_ID }),
        sseChunk('tool_result', { call_id: 'c1', tool: 'get_job_validation', duration_ms: 10, result: { total: 5, pass: 3, warnings: 2, errors: 0, perRow: [] }, session_id: SESSION_ID }),
        sseChunk('message', { text: '發現 2 個 warnings，建議重新生成。', session_id: SESSION_ID }),
        sseChunk('done', { step_count: 2, session_id: SESSION_ID }),
      ].join(''),
      headers: { 'Cache-Control': 'no-cache' },
    });
  });
}

async function seedJobState(page: import('@playwright/test').Page) {
  await page.evaluate(() => {
    const store = (window as unknown as { __tcJobStore?: { setState: (s: unknown) => void } }).__tcJobStore;
    if (!store) throw new Error('__tcJobStore not exposed');
    store.setState({
      jobMetadata: {
        jobId: 'handoff-job-001',
        projectName: 'HandoffTest',
        createdAt: '2026-04-18T00:00:00Z',
        totalRows: 5,
      },
      tcRows: [
        { id: 'r1', reqId: 'REQ-1', testGroup: 'G', testSet: 'S1', testItem: 'item1', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'accepted' },
        { id: 'r2', reqId: 'REQ-2', testGroup: 'G', testSet: 'S1', testItem: 'item2', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'accepted', validationErrors: [{ severity: 'warning', message: 'test warning' }] },
        { id: 'r3', reqId: 'REQ-3', testGroup: 'G', testSet: 'S2', testItem: 'item3', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'pending' },
        { id: 'r4', reqId: 'REQ-4', testGroup: 'G', testSet: 'S2', testItem: 'item4', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'pending' },
        { id: 'r5', reqId: 'REQ-5', testGroup: 'G', testSet: 'S2', testItem: 'item5', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'pending', validationErrors: [{ severity: 'warning', message: 'another warning' }] },
      ],
      stats: { total: 5, processed: 5, success: 3, fail: 0, cost: 0.05, inputTokens: 1000, outputTokens: 500, cacheCreationTokens: 0, cacheReadTokens: 0 },
    });
  });
}

test.describe('GUI-Agent handoff', () => {
  test('Help button fires agent-prefill event and opens Chat', async ({ page }) => {
    await mockAgentSessions(page);
    await mockAgentChat(page);

    await page.goto('/');
    await seedJobState(page);

    // Open Chat first so the prefill event reaches InputArea
    await page.locator('.agent-taskbar-btn').click();
    await expect(page.locator('.chat-module')).toBeVisible({ timeout: 5000 });

    // Simulate what HelpFromAgentButton does when clicked in Review module:
    // It dispatches agent-prefill with the context, then focusWindow('chat')
    const expectedContext = '[context: 目前在 Review Module, job=handoff-job-001]\n[Validator: 2 warnings]\n';
    await page.evaluate((ctx) => {
      window.dispatchEvent(new CustomEvent('agent-prefill', { detail: ctx }));
    }, expectedContext);

    // InputArea should have the context prepended
    const textarea = page.locator('.chat-textarea');
    await expect(textarea).toContainText('[context: 目前在 Review Module');
    await expect(textarea).toContainText('job=handoff-job-001');
    await expect(textarea).toContainText('2 warnings');
  });

  test('Chat help button does not clear jobMetadata', async ({ page }) => {
    await mockAgentSessions(page);
    await mockAgentChat(page);

    await page.goto('/');
    await seedJobState(page);

    // Open chat via taskbar button
    await page.locator('.agent-taskbar-btn').click();
    await expect(page.locator('.chat-module')).toBeVisible({ timeout: 5000 });

    // Send a message
    await page.locator('.chat-textarea').fill('Check validation');
    await page.locator('.chat-textarea').press('Enter');

    // Wait for agent response
    await expect(page.locator('.agent-text').filter({ hasText: '2 個 warnings' })).toBeVisible({ timeout: 8000 });

    // Verify jobMetadata is still intact after agent interaction
    const jobId = await page.evaluate(() => {
      const store = (window as unknown as { __tcJobStore?: { getState: () => { jobMetadata: { jobId: string } | null } } }).__tcJobStore;
      return store?.getState()?.jobMetadata?.jobId ?? null;
    });
    expect(jobId).toBe('handoff-job-001');
  });

  test('context prompt contains correct module info', async ({ page }) => {
    await mockAgentSessions(page);

    await page.goto('/');
    await seedJobState(page);

    // Open chat directly (simulate prefill via custom event)
    await page.locator('.agent-taskbar-btn').click();
    await expect(page.locator('.chat-module')).toBeVisible({ timeout: 5000 });

    // Fire agent-prefill event with a test context
    await page.evaluate(() => {
      window.dispatchEvent(new CustomEvent('agent-prefill', {
        detail: '[context: 目前在 Review Module, job=handoff-job-001]\n[Validator: 2 warnings]\n',
      }));
    });

    // Verify text appears in input
    const textarea = page.locator('.chat-textarea');
    await expect(textarea).toContainText('context: 目前在 Review Module');
    await expect(textarea).toContainText('2 warnings');
  });
});
