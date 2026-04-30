import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import { proxyJsonResponse } from '@/app/api/_lib/backend';
import { DELETE as resetAllData } from '@/app/api/admin/reset/route';
import { GET as aggregateEvents } from '@/app/api/events/aggregate/route';
import { GET as listSpecLibrary } from '@/app/api/spec-library/route';

describe('proxyJsonResponse', () => {
  const originalFetch = global.fetch;

  beforeEach(() => {
    vi.restoreAllMocks();
  });

  afterEach(() => {
    global.fetch = originalFetch;
  });

  it('parses upstream json and applies the mutator', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ jobId: 'job-1', status: 'ready' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      }),
    );

    const response = await proxyJsonResponse('/api/export', undefined, (data) => ({
      ...(data as Record<string, unknown>),
      downloadUrl: '/api/export/download/job-1',
    }));

    expect(response.status).toBe(200);
    await expect(response.json()).resolves.toMatchObject({
      jobId: 'job-1',
      downloadUrl: '/api/export/download/job-1',
    });
  });

  it('preserves non-json upstream failures instead of masking them as proxy errors', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      new Response('Internal Server Error', {
        status: 500,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' },
      }),
    );

    const response = await proxyJsonResponse('/api/export');

    expect(response.status).toBe(500);
    await expect(response.text()).resolves.toBe('Internal Server Error');
    expect(response.headers.get('content-type')).toContain('text/plain');
  });

  it('blocks the reset proxy when the frontend host is not loopback', async () => {
    global.fetch = vi.fn();

    const response = await resetAllData(
      new Request('https://tc-generator.example.com/api/admin/reset', {
        method: 'DELETE',
      }),
    );

    expect(response.status).toBe(403);
    expect(global.fetch).not.toHaveBeenCalled();
  });

  it('proxies the spec library endpoint to the backend', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      Response.json({
        specs: [
          {
            name: 'SWE1',
            sourceFile: 'SWE1.xlsx',
            entriesCount: 42,
            embeddingModel: null,
            updatedAt: null,
          },
        ],
      }),
    );

    const response = await listSpecLibrary(
      new Request('http://localhost/api/spec-library', { method: 'GET' }),
    );

    expect(response.status).toBe(200);
    expect(global.fetch).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/api/spec-library',
      { method: 'GET', headers: {} },
    );
  });

  it('forwards X-Workspace-Id from incoming request to the backend (hard isolation S3)', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      Response.json({ specs: [] }),
    );

    await listSpecLibrary(
      new Request('http://localhost/api/spec-library', {
        method: 'GET',
        headers: { 'X-Workspace-Id': 'ws-frontend-A' },
      }),
    );

    expect(global.fetch).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/api/spec-library',
      { method: 'GET', headers: { 'X-Workspace-Id': 'ws-frontend-A' } },
    );
  });

  it('proxies events aggregate query params to the backend', async () => {
    global.fetch = vi.fn().mockResolvedValue(
      Response.json({
        experiment: 'home_layout_emphasis',
        totalEvents: 0,
        variants: {},
      }),
    );

    const response = await aggregateEvents(
      new Request(
        'http://localhost:3000/api/events/aggregate?experiment=home_layout_emphasis',
      ),
    );

    expect(response.status).toBe(200);
    expect(global.fetch).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/api/events/aggregate?experiment=home_layout_emphasis',
      { method: 'GET' },
    );
    await expect(response.json()).resolves.toMatchObject({
      experiment: 'home_layout_emphasis',
    });
  });
});
