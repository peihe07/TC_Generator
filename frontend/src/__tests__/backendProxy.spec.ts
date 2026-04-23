import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import { proxyJsonResponse } from '@/app/api/_lib/backend';

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
});
