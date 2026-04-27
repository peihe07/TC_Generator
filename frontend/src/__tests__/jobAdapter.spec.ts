import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import {
  exportJob,
  fetchGroupingPreview,
  parseJobFiles,
  regenerateRows,
  startGeneration,
} from '../services/jobAdapter';

describe('exportJob', () => {
  const originalFetch = global.fetch;

  beforeEach(() => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        fileName: 'E2EProject_generated.xlsx',
        downloadUrl: '/api/export/download/job-generate-export-e2e',
        exportedRows: 2,
      }),
    } as Response);
  });

  afterEach(() => {
    global.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  it('maps frontend rows into backend export payload', async () => {
    await exportJob({
      jobId: 'job-generate-export-e2e',
      scope: 'all',
      outputMode: 'new-file',
      includeFrameworkSheet: true,
      selectedColumns: ['TC ID', 'Test Set', 'Pre-Conditions', 'Test Procedure', 'Expected Result'],
      rows: [
        {
          id: 'TC-001',
          rowNum: 10,
          tcId: 'E2EPROJ-AUTH-001',
          reqId: 'REQ-1',
          testGroup: 'Auth',
          testSet: 'Login',
          testItem: 'User logs in with valid credentials',
          tcTitle: '(Valid login -> dashboard opens)',
          reviewStatus: 'pending',
          specReference: 'SPEC-001',
          preConditions: '1. User account exists',
          inputTestData: 'email=admin@test.com',
          steps: '1. Open login page\n2. Enter valid credentials\n3. Submit',
          expectedResults: '1. Login accepted\n2. Dashboard is visible',
          status: 'reviewing',
          validationErrors: [],
          splitDecision: {
            reqId: 'REQ-1',
            tcCount: 1,
            reasoning: 'AI 判定為單一登入行為，不需拆分。',
            keywords: [],
          },
        },
        {
          id: 'TC-002',
          rowNum: 11,
          tcId: 'E2EPROJ-AUTH-002',
          reqId: 'REQ-2',
          testGroup: 'Auth',
          testSet: 'Login',
          testItem: 'User sees an error for invalid password',
          tcTitle: '(Invalid password -> error message appears)',
          reviewStatus: 'accepted',
          specReference: 'SPEC-002',
          preConditions: '1. User account exists',
          inputTestData: 'email=admin@test.com,password=wrong',
          steps: '1. Open login page\n2. Enter invalid password\n3. Submit',
          expectedResults: '1. Login rejected\n2. Error message is shown',
          status: 'accepted',
          validationErrors: [],
        },
      ],
    });

    expect(global.fetch).toHaveBeenCalledTimes(1);
    const [, init] = vi.mocked(global.fetch).mock.calls[0];
    const payload = JSON.parse(String(init?.body)) as {
      jobId: string;
      rows: Array<Record<string, unknown>>;
    };

    expect(payload.jobId).toBe('job-generate-export-e2e');
    expect(payload.rows).toHaveLength(2);
    expect(payload.rows[0]).toMatchObject({
      id: 'TC-001',
      rowNum: 10,
      tcId: 'E2EPROJ-AUTH-001',
      reqId: 'REQ-1',
      reviewStatus: 'pending',
    });
    expect(payload.rows[0].generated).toMatchObject({
      tcTitle: '(Valid login -> dashboard opens)',
      preConditions: '1. User account exists',
      inputTestData: 'email=admin@test.com',
      testProcedure: '1. Open login page\n2. Enter valid credentials\n3. Submit',
      expectedResult: '1. Login accepted\n2. Dashboard is visible',
      specReference: 'SPEC-001',
    });
    expect(payload.rows[0].splitDecision).toEqual({
      reasoning: 'AI 判定為單一登入行為，不需拆分。',
    });
    expect(payload.rows[1]).toMatchObject({
      reviewStatus: 'accepted',
    });
  });

  it('surfaces backend detail messages instead of a generic status error', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: false,
      status: 503,
      clone: () => ({
        json: async () => ({ detail: 'export file not found' }),
      }),
      json: async () => ({ detail: 'export file not found' }),
    } as Response);

    await expect(
      exportJob({
        jobId: 'job-generate-export-e2e',
        scope: 'all',
        outputMode: 'new-file',
        includeFrameworkSheet: true,
        selectedColumns: ['TC ID'],
        rows: [],
      }),
    ).rejects.toThrow('export file not found');
  });
});

describe('regenerateRows', () => {
  const originalFetch = global.fetch;

  afterEach(() => {
    global.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  it('sends the reviewer regenerate reason to the backend stream request', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      body: new ReadableStream({
        start(controller) {
          controller.enqueue(new TextEncoder().encode('data: {"type":"regen.completed","stats":{"total":1,"processed":1,"currentCost":0}}\n\n'));
          controller.close();
        },
      }),
    } as Response);

    await regenerateRows(
      {
        jobId: 'job-regen-reason',
        rowIds: ['TC-001'],
        rows: [
          {
            id: 'TC-001',
            reqId: 'REQ-1',
            testGroup: 'Auth',
            testSet: 'Login',
            testItem: 'User logs in',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
        regenerateReason: 'Missing negative validation path',
      },
      {},
    );

    const [, init] = vi.mocked(global.fetch).mock.calls[0];
    const payload = JSON.parse(String(init?.body)) as Record<string, unknown>;
    expect(payload.regenerateReason).toBe('Missing negative validation path');
  });

  it('does not fall back to local preview when no backend job is active', async () => {
    const onError = vi.fn();
    const onRow = vi.fn();

    await regenerateRows(
      {
        jobId: null,
        rowIds: ['TC-001'],
        rows: [
          {
            id: 'TC-001',
            reqId: 'REQ-1',
            testGroup: 'Auth',
            testSet: 'Login',
            testItem: 'User logs in',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
      },
      { onError, onRow },
    );

    expect(onError).toHaveBeenCalledWith('Regenerate requires an active backend job.');
    expect(onRow).not.toHaveBeenCalled();
  });
});

describe('parseJobFiles', () => {
  const originalFetch = global.fetch;

  afterEach(() => {
    global.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  it('surfaces backend parse errors instead of silently creating a mock job', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: false,
      status: 400,
      clone: () => ({
        json: async () => ({ detail: 'raw_file must be .xlsx or .xlsm' }),
      }),
      json: async () => ({ detail: 'raw_file must be .xlsx or .xlsm' }),
    } as Response);

    await expect(
      parseJobFiles({
        rawFile: new File(['not-an-excel'], 'bad.txt', { type: 'text/plain' }),
      }),
    ).rejects.toThrow('raw_file must be .xlsx or .xlsm');
  });
});

describe('fetchGroupingPreview', () => {
  const originalFetch = global.fetch;

  afterEach(() => {
    global.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  it('sends existing test sets as hints when force-regrouping', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      Response.json({
        groups: [],
        assignments: [],
        cost: 0,
        inputTokens: 0,
        outputTokens: 0,
        cacheCreationTokens: 0,
        cacheReadTokens: 0,
      }),
    );

    await fetchGroupingPreview({
      jobId: 'job-1',
      forceRegroup: true,
      rows: [
        {
          id: 'row-1',
          reqId: 'REQ-1',
          testGroup: 'HMI',
          testSet: 'Original Set',
          testSetHint: 'Workbook Hint',
          testItem: 'Bluetooth connection requirement',
          preConditions: '',
          inputTestData: '',
          steps: '',
          expectedResults: '',
          status: 'pending',
          validationErrors: [],
        },
      ],
    });

    expect(global.fetch).toHaveBeenCalledWith(
      '/api/group',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({
          jobId: 'job-1',
          forceRegroup: true,
          rows: [
            {
              id: 'row-1',
              reqId: 'REQ-1',
              testItem: 'Bluetooth connection requirement',
              testSet: 'Original Set',
              testSetHint: 'Workbook Hint',
            },
          ],
        }),
      }),
    );
  });
});

describe('startGeneration status mapping', () => {
  const originalEventSource = global.EventSource;

  afterEach(() => {
    global.EventSource = originalEventSource;
    vi.restoreAllMocks();
  });

  it('requires an active backend job instead of running local mock generation', async () => {
    const onError = vi.fn();
    const onRow = vi.fn();

    startGeneration(
      {
        jobId: null,
        rows: [
          {
            id: 'TC-001',
            reqId: 'REQ-1',
            testGroup: 'Auth',
            testSet: 'Login',
            testItem: 'User logs in',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
      },
      { onError, onRow },
    );

    await new Promise((resolve) => setTimeout(resolve, 0));

    expect(onError).toHaveBeenCalledWith('Generation requires an active parsed job.');
    expect(onRow).not.toHaveBeenCalled();
  });

  it('maps generated backend rows to pending for first review', async () => {
    const fetchMock = vi
      .spyOn(global, 'fetch')
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          jobId: 'job-status-map',
          totalRows: 1,
          streamUrl: '/api/generate/stream?jobId=job-status-map',
        }),
      } as Response);

    class FakeEventSource {
      onmessage: ((event: MessageEvent<string>) => void) | null = null;
      onerror: (() => void) | null = null;

      constructor(_url: string) {
        queueMicrotask(() => {
          this.onmessage?.({
            data: JSON.stringify({
              type: 'row.completed',
              jobId: 'job-status-map',
              row: {
                id: 'TC-001',
                reqId: 'REQ-1',
                testSet: 'Login',
                testItem: 'User logs in',
                status: 'ready',
                reviewStatus: 'pending',
                generated: {
                  tcTitle: '(Valid login -> dashboard opens)',
                  preConditions: 'NA',
                  inputTestData: 'NA',
                  testProcedure: '1. Do action\n2. Verify result',
                  expectedResult: '1. Action succeeds\n2. Result verified',
                },
                validation: [],
              },
              stats: { total: 1, processed: 1, currentCost: 0.01 },
            }),
          } as MessageEvent<string>);
          this.onmessage?.({
            data: JSON.stringify({
              type: 'job.completed',
              jobId: 'job-status-map',
              stats: { total: 1, processed: 1, currentCost: 0.01 },
            }),
          } as MessageEvent<string>);
        });
      }

      close() {}
    }

    // jsdom test env does not provide a real EventSource implementation.
    global.EventSource = FakeEventSource as unknown as typeof EventSource;

    const onRow = vi.fn();
    const onComplete = vi.fn();

    startGeneration(
      {
        jobId: 'job-status-map',
        rows: [
          {
            id: 'TC-001',
            reqId: 'REQ-1',
            testGroup: 'Auth',
            testSet: 'Login',
            testItem: 'User logs in',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
      },
      {
        onRow,
        onComplete,
      },
    );

    await new Promise((resolve) => setTimeout(resolve, 0));

    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(onRow).toHaveBeenCalledTimes(1);
    expect(onRow.mock.calls[0][0]).toMatchObject({
      status: 'pending',
      tcTitle: '(Valid login -> dashboard opens)',
    });
    expect(onComplete).toHaveBeenCalledTimes(1);
  });

  it('maps failed row events to fail status even when backend row status is not explicit', async () => {
    const fetchMock = vi
      .spyOn(global, 'fetch')
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          jobId: 'job-status-fail',
          totalRows: 1,
          streamUrl: '/api/generate/stream?jobId=job-status-fail',
        }),
      } as Response);

    class FakeEventSource {
      onmessage: ((event: MessageEvent<string>) => void) | null = null;
      onerror: (() => void) | null = null;

      constructor(_url: string) {
        queueMicrotask(() => {
          this.onmessage?.({
            data: JSON.stringify({
              type: 'row.failed',
              jobId: 'job-status-fail',
              row: {
                id: 'TC-001',
                reqId: 'REQ-1',
                testSet: 'Login',
                testItem: 'User logs in',
                status: 'ready',
                reviewStatus: 'pending',
                validation: [],
              },
              stats: { total: 1, processed: 1, currentCost: 0.01 },
            }),
          } as MessageEvent<string>);
          this.onmessage?.({
            data: JSON.stringify({
              type: 'job.completed',
              jobId: 'job-status-fail',
              stats: { total: 1, processed: 1, currentCost: 0.01 },
            }),
          } as MessageEvent<string>);
        });
      }

      close() {}
    }

    global.EventSource = FakeEventSource as unknown as typeof EventSource;

    const onRow = vi.fn();
    const onProgress = vi.fn();

    startGeneration(
      {
        jobId: 'job-status-fail',
        rows: [
          {
            id: 'TC-001',
            reqId: 'REQ-1',
            testGroup: 'Auth',
            testSet: 'Login',
            testItem: 'User logs in',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
      },
      {
        onRow,
        onProgress,
      },
    );

    await new Promise((resolve) => setTimeout(resolve, 0));

    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(onRow).toHaveBeenCalledWith(
      expect.objectContaining({ id: 'TC-001', status: 'fail' }),
      expect.any(String),
    );
    expect(onProgress).toHaveBeenCalledWith(
      expect.objectContaining({
        total: 1,
        processed: 1,
        success: 0,
        fail: 1,
      }),
    );
  });

  it('keeps progress denominator at the original requirement count even when AI splits', async () => {
    const fetchMock = vi
      .spyOn(global, 'fetch')
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          jobId: 'job-split-stats',
          totalRows: 1,
          streamUrl: '/api/generate/stream?jobId=job-split-stats',
        }),
      } as Response);

    class FakeEventSource {
      onmessage: ((event: MessageEvent<string>) => void) | null = null;
      onerror: (() => void) | null = null;

      constructor(_url: string) {
        queueMicrotask(() => {
          this.onmessage?.({
            data: JSON.stringify({
              type: 'row.completed',
              jobId: 'job-split-stats',
              row: {
                id: 'row-10',
                reqId: 'REQ-1',
                testSet: 'Core',
                testItem: 'Requirement',
                status: 'ready',
                generated: {
                  tcTitle: '(Scenario 1)',
                  preConditions: 'NA',
                  inputTestData: 'NA',
                  testProcedure: '1. Do',
                  expectedResult: '1. Done',
                },
              },
              stats: { total: 2, processed: 1, currentCost: 0.01 },
            }),
          } as MessageEvent<string>);
          this.onmessage?.({
            data: JSON.stringify({
              type: 'row.added',
              jobId: 'job-split-stats',
              row: {
                id: 'row-10__tc2',
                parentId: 'row-10',
                reqId: 'REQ-1',
                testSet: 'Core',
                testItem: 'Requirement',
                status: 'ready',
                generated: {
                  tcTitle: '(Scenario 2)',
                  preConditions: 'NA',
                  inputTestData: 'NA',
                  testProcedure: '1. Do other',
                  expectedResult: '1. Other done',
                },
              },
              stats: { total: 2, processed: 2, currentCost: 0.02 },
            }),
          } as MessageEvent<string>);
          this.onmessage?.({
            data: JSON.stringify({
              type: 'job.completed',
              jobId: 'job-split-stats',
              stats: { total: 2, processed: 2, currentCost: 0.02 },
            }),
          } as MessageEvent<string>);
        });
      }

      close() {}
    }

    global.EventSource = FakeEventSource as unknown as typeof EventSource;

    const onProgress = vi.fn();

    startGeneration(
      {
        jobId: 'job-split-stats',
        rows: [
          {
            id: 'row-10',
            reqId: 'REQ-1',
            testGroup: 'DeviceManager',
            testSet: 'Core',
            testItem: 'Requirement',
            preConditions: '',
            inputTestData: '',
            steps: '',
            expectedResults: '',
            status: 'pending',
            validationErrors: [],
          },
        ],
        config: {
          model: 'gpt-5',
          batchSize: 1,
          budgetLimit: 10,
          creditBalance: 0,
          strictValidation: false,
          targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
        },
      },
      { onProgress },
    );

    await new Promise((resolve) => setTimeout(resolve, 0));

    expect(fetchMock).toHaveBeenCalledTimes(1);
    // 1 input req split into 2 TCs by AI — progress stays 1/1 (not 2/2),
    // because the denominator is locked to the original Requirement ID set.
    // success counts row-level outcomes (2 successful TCs), independent of
    // the req-level progress numerator.
    expect(onProgress).toHaveBeenLastCalledWith(
      expect.objectContaining({
        total: 1,
        processed: 1,
        success: 2,
        fail: 0,
      }),
    );
  });
});
