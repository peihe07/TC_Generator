import { describe, it, expect, vi, beforeEach } from 'vitest';
import { act, renderHook } from '@testing-library/react';

// Mock agentClient before importing the store
vi.mock('../services/agentClient', async (importOriginal) => {
  const actual = await importOriginal<typeof import('../services/agentClient')>();
  return {
    ...actual,
    agentClient: {
      sendTurn: vi.fn(),
      getSession: vi.fn(),
      listSessions: vi.fn().mockResolvedValue([]),
      deleteSession: vi.fn(),
      downloadTrace: vi.fn(),
    },
  };
});

import { useAgentStore } from '../store/useAgentStore';
import { agentClient } from '../services/agentClient';
import type { AgentEvent } from '../services/agentEvents';

function makeEvent(type: AgentEvent['type'], extra: object = {}): AgentEvent {
  return { type, session_id: 'sess-test', ...extra } as AgentEvent;
}

function simulateTurn(events: AgentEvent[]) {
  (agentClient.sendTurn as ReturnType<typeof vi.fn>).mockImplementationOnce(
    async (_req: unknown, onEvent: (e: AgentEvent) => void) => {
      for (const e of events) onEvent(e);
    },
  );
}

describe('useAgentStore', () => {
  beforeEach(() => {
    const store = useAgentStore.getState();
    store.newSession();
    vi.clearAllMocks();
  });

  it('streamState transitions idle → streaming → idle on sendMessage', async () => {
    simulateTurn([
      makeEvent('message', { text: 'hi' }),
      makeEvent('done', { step_count: 1 }),
    ]);

    const { result } = renderHook(() => useAgentStore());

    await act(async () => {
      await result.current.sendMessage('hello');
    });

    expect(result.current.streamState).toBe('idle');
    expect(result.current.messages.some((m) => m.kind === 'user')).toBe(true);
  });

  it('streamState becomes waiting_confirm on require_confirm', async () => {
    simulateTurn([
      makeEvent('require_confirm', { call_id: 'c1', tool: 'generate_tc', args: {}, est_cost_usd: 1.5 }),
    ]);

    const { result } = renderHook(() => useAgentStore());

    await act(async () => {
      await result.current.sendMessage('generate');
    });

    expect(result.current.streamState).toBe('waiting_confirm');
    expect(result.current.pendingConfirm?.callId).toBe('c1');
  });

  it('loadSession restores messages from OpenAI history', async () => {
    (agentClient.getSession as ReturnType<typeof vi.fn>).mockResolvedValue({
      sessionId: 'sess-old',
      history: [
        { role: 'user', content: 'restored question' },
        { role: 'assistant', content: 'restored answer', tool_calls: [] },
      ],
      totalCostUsd: 0.01,
      createdAt: 0,
      updatedAt: 0,
      messageCount: 2,
    });

    const { result } = renderHook(() => useAgentStore());

    await act(async () => {
      await result.current.loadSession('sess-old');
    });

    expect(result.current.sessionId).toBe('sess-old');
    expect(result.current.messages.some((m) => m.kind === 'user')).toBe(true);
    expect(result.current.streamState).toBe('idle');
  });

  it('newSession clears messages and sessionId', () => {
    const { result } = renderHook(() => useAgentStore());

    act(() => result.current.newSession());

    expect(result.current.sessionId).toBeNull();
    expect(result.current.messages).toHaveLength(0);
    expect(result.current.streamState).toBe('idle');
  });
});
