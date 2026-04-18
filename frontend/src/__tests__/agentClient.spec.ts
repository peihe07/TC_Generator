import { describe, it, expect, vi, beforeEach } from 'vitest';
import { AgentClient, historyToMessages, getSessionPreview } from '../services/agentClient';

// ---- SSE stream helper ----

function makeStream(chunks: string[]): ReadableStream<Uint8Array> {
  const encoder = new TextEncoder();
  let i = 0;
  return new ReadableStream({
    pull(controller) {
      if (i < chunks.length) {
        controller.enqueue(encoder.encode(chunks[i++]));
      } else {
        controller.close();
      }
    },
  });
}

function sseChunk(eventType: string, data: object): string {
  return `event: ${eventType}\ndata: ${JSON.stringify(data)}\n\n`;
}

// ---- Tests ----

describe('AgentClient.sendTurn — SSE parsing', () => {
  let client: AgentClient;

  beforeEach(() => {
    client = new AgentClient();
  });

  it('parses multiple events from a single stream', async () => {
    const sid = 'sess-1';
    const chunks = [
      sseChunk('message',     { text: 'hello',  session_id: sid }),
      sseChunk('tool_call',   { call_id: 'c1', tool: 'list_jobs', args: {}, session_id: sid }),
      sseChunk('tool_result', { call_id: 'c1', tool: 'list_jobs', duration_ms: 50, result: {}, session_id: sid }),
      sseChunk('done',        { step_count: 1, session_id: sid }),
    ];

    const mockFetch = vi.fn().mockResolvedValue({
      ok: true,
      body: makeStream(chunks),
    });
    vi.stubGlobal('fetch', mockFetch);

    const received: string[] = [];
    await client.sendTurn({ session_id: null, message: 'test' }, (e) => received.push(e.type));

    expect(received).toEqual(['message', 'tool_call', 'tool_result', 'done']);
  });

  it('handles event data split across chunks', async () => {
    const sid = 'sess-2';
    const full = sseChunk('message', { text: 'hi', session_id: sid });
    // Split mid-stream
    const chunks = [full.slice(0, 20), full.slice(20)];

    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({
      ok: true,
      body: makeStream(chunks),
    }));

    const received: string[] = [];
    await client.sendTurn({ session_id: null, message: 'test' }, (e) => received.push(e.type));

    expect(received).toContain('message');
  });

  it('throws on non-ok response', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false, status: 500 }));

    await expect(
      client.sendTurn({ session_id: null, message: 'test' }, () => {}),
    ).rejects.toThrow('500');
  });

  it('sends approved_call_ids in confirm-resume request', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({
      ok: true,
      body: makeStream([sseChunk('done', { step_count: 1, session_id: 's' })]),
    }));

    await client.sendTurn(
      { session_id: 'abc', message: '', approved_call_ids: ['call-1'] },
      () => {},
    );

    const body = JSON.parse((fetch as ReturnType<typeof vi.fn>).mock.calls[0][1].body);
    expect(body.approved_call_ids).toEqual(['call-1']);
    expect(body.message).toBe('');
  });
});

// ---- historyToMessages ----

describe('historyToMessages', () => {
  it('converts user messages', () => {
    const history = [{ role: 'user', content: 'hello' }];
    const msgs = historyToMessages(history);
    expect(msgs).toHaveLength(1);
    expect(msgs[0]).toMatchObject({ kind: 'user', text: 'hello' });
  });

  it('converts assistant text to agent message', () => {
    const history = [
      { role: 'user', content: 'hi' },
      { role: 'assistant', content: 'there', tool_calls: [] },
    ];
    const msgs = historyToMessages(history);
    expect(msgs[1]).toMatchObject({ kind: 'agent' });
    expect((msgs[1] as { parts: unknown[] }).parts[0]).toMatchObject({ kind: 'text', text: 'there' });
  });

  it('converts tool_call + tool result pair', () => {
    const history = [
      { role: 'user', content: 'go' },
      {
        role: 'assistant',
        content: '',
        tool_calls: [{ id: 'tc1', type: 'function', function: { name: 'list_jobs', arguments: '{}' } }],
      },
      { role: 'tool', tool_call_id: 'tc1', content: JSON.stringify({ ok: true, result: { jobs: [] } }) },
    ];
    const msgs = historyToMessages(history);
    const agentMsg = msgs[1] as { parts: Array<{ kind: string; callId?: string; result?: unknown }> };
    const toolPart = agentMsg.parts.find((p) => p.kind === 'tool');
    expect(toolPart?.callId).toBe('tc1');
    expect(toolPart?.result).toEqual({ jobs: [] });
  });

  it('skips system messages', () => {
    const history = [{ role: 'system', content: 'rules' }, { role: 'user', content: 'hi' }];
    expect(historyToMessages(history)).toHaveLength(1);
  });
});

// ---- getSessionPreview ----

describe('getSessionPreview', () => {
  it('returns first user message up to 40 chars', () => {
    const msgs = [{ kind: 'user' as const, id: '1', text: 'short', ts: 0 }];
    expect(getSessionPreview(msgs)).toBe('short');
  });

  it('truncates long messages', () => {
    const long = 'a'.repeat(50);
    const msgs = [{ kind: 'user' as const, id: '1', text: long, ts: 0 }];
    const preview = getSessionPreview(msgs);
    expect(preview.length).toBe(41); // 40 + ellipsis
    expect(preview.endsWith('…')).toBe(true);
  });

  it('returns fallback for empty messages', () => {
    expect(getSessionPreview([])).toBe('(empty session)');
  });
});
