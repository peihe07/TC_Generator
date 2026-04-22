import { test, expect } from '@playwright/test';

async function seedJob(page: import('@playwright/test').Page) {
  await page.waitForFunction(() => (window as unknown as Record<string, unknown>).__tcJobStore !== undefined);
  await page.evaluate(() => {
    const store = (window as unknown as {
      __tcJobStore?: { setState: (s: Record<string, unknown>) => void };
    }).__tcJobStore;
    if (!store) {
      throw new Error('__tcJobStore not exposed');
    }

    store.setState({
      jobMetadata: {
        jobId: 'job-generate-export-e2e',
        projectName: 'E2EProject',
        createdAt: '2026-04-19T00:00:00Z',
        totalRows: 2,
      },
      config: {
        model: 'gpt-5.4-mini',
        batchSize: 5,
        budgetLimit: 10,
        strictValidation: false,
        targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
      },
      tcRows: [
        {
          id: 'TC-001',
          rowNum: 10,
          tcId: 'E2EPROJ-AUTH-001',
          reqId: 'REQ-1',
          testGroup: 'Auth',
          testSet: 'Login',
          testItem: 'User logs in with valid credentials',
          preConditions: '',
          inputTestData: '',
          steps: '',
          expectedResults: '',
          status: 'pending',
          validationErrors: [],
        },
        {
          id: 'TC-002',
          rowNum: 11,
          tcId: 'E2EPROJ-AUTH-002',
          reqId: 'REQ-2',
          testGroup: 'Auth',
          testSet: 'Login',
          testItem: 'User sees an error for invalid password',
          preConditions: '',
          inputTestData: '',
          steps: '',
          expectedResults: '',
          status: 'pending',
          validationErrors: [],
        },
      ],
      logs: [],
      stats: {
        total: 2,
        processed: 0,
        success: 0,
        fail: 0,
        cost: 0,
        inputTokens: 0,
        outputTokens: 0,
        cacheCreationTokens: 0,
        cacheReadTokens: 0,
      },
      isProcessing: false,
      isRegenerating: false,
    });
  });
}

test.describe('Generate to Review flow', () => {
  test('preserves test item rewrite after generation', async ({ page }) => {
    await page.route('/api/generate', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          jobId: 'job-generate-export-e2e',
          totalRows: 2,
          streamUrl: '/api/generate/stream?jobId=job-generate-export-e2e',
        }),
      });
    });

    await page.route('/api/generate/stream?jobId=job-generate-export-e2e', async (route) => {
      const sse = [
        'data: {"type":"job.started","jobId":"job-generate-export-e2e","stats":{"total":2,"processed":0,"currentCost":0},"message":"started"}',
        '',
        'data: {"type":"row.completed","jobId":"job-generate-export-e2e","row":{"id":"TC-001","rowNum":10,"tcId":"E2EPROJ-AUTH-001","reqId":"REQ-1","testItem":"User logs in with valid credentials","testSet":"Login","reviewStatus":"pending","status":"ready","generated":{"testItemRewrite":"(Valid login -> dashboard opens)","preConditions":"1. User account exists","inputTestData":"email=admin@test.com","testProcedure":"1. Open login page\\n2. Enter valid credentials\\n3. Submit","expectedResult":"1. Login accepted\\n2. Dashboard is visible","priority":"Medium","designMethod":"Scenario","specReference":"SPEC-001"},"validation":[]},"stats":{"total":2,"processed":1,"currentCost":0.01},"message":"row 1 done"}',
        '',
        'data: {"type":"row.completed","jobId":"job-generate-export-e2e","row":{"id":"TC-002","rowNum":11,"tcId":"E2EPROJ-AUTH-002","reqId":"REQ-2","testItem":"User sees an error for invalid password","testSet":"Login","reviewStatus":"pending","status":"ready","generated":{"testItemRewrite":"(Invalid password -> error message appears)","preConditions":"1. User account exists","inputTestData":"email=admin@test.com,password=wrong","testProcedure":"1. Open login page\\n2. Enter invalid password\\n3. Submit","expectedResult":"1. Login rejected\\n2. Error message is shown","priority":"Medium","designMethod":"Scenario","specReference":"SPEC-002"},"validation":[]},"stats":{"total":2,"processed":2,"currentCost":0.02},"message":"row 2 done"}',
        '',
        'data: {"type":"job.completed","jobId":"job-generate-export-e2e","stats":{"total":2,"processed":2,"currentCost":0.02},"message":"Generation complete"}',
        '',
      ].join('\n');

      await route.fulfill({
        status: 200,
        contentType: 'text/event-stream',
        body: sse,
      });
    });

    await page.goto('/');
    await seedJob(page);

    await page.getByText('Generate', { exact: true }).dblclick();
    await expect(page.getByText('TC Generator - Generate').first()).toBeVisible();
    await page.getByRole('button', { name: /Start Run/i }).click();

    await page.waitForFunction(() => {
      const store = (window as unknown as {
        __tcJobStore?: { getState: () => { tcRows: Array<{ testItemRewrite?: string }> } };
      }).__tcJobStore;
      const rows = store?.getState().tcRows ?? [];
      return rows.length >= 2 && rows.every((row) => !!row.testItemRewrite);
    });

    await page.getByText('Review', { exact: true }).dblclick();
    await expect(page.getByText('TC Generator - Review').first()).toBeVisible();
    await expect(page.getByText('REQ-1')).toBeVisible();

    await page.locator('table tbody tr').first().click();
    await expect(page.getByText('Test Item Rewrite')).toBeVisible();
    await expect(page.getByText('(Valid login -> dashboard opens)')).toBeVisible();
  });
});
