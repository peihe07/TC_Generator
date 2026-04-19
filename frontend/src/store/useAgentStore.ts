import { create } from 'zustand';
import {
  agentClient,
  historyToMessages,
  getPendingConfirmPart,
} from '../services/agentClient';
import type {
  UIMessage,
  UIPart,
  UIToolPart,
  UIConfirmPart,
  AgentEvent,
  SessionSummary,
} from '../services/agentEvents';

export type StreamState = 'idle' | 'sending' | 'streaming' | 'waiting_confirm' | 'error';

export interface AgentStateUpdate {
  jobId: string;
  tool: string;
  ts: number;
}

interface AgentStore {
  // Current session
  sessionId: string | null;
  messages: UIMessage[];
  pendingConfirm: UIConfirmPart | null;
  streamState: StreamState;
  lastError: { code: string; message: string } | null;

  // Last job state mutation from agent (for conflict toast in GUI modules)
  lastStateUpdate: AgentStateUpdate | null;

  // Session list
  recentSessions: SessionSummary[];
  recentSessionsLoadedAt: number | null;

  // Cost tracking
  currentSessionCost: number;

  // Actions
  sendMessage: (text: string) => Promise<void>;
  acceptConfirm: () => Promise<void>;
  declineConfirm: () => void;
  loadSession: (sessionId: string) => Promise<void>;
  newSession: () => void;
  deleteSession: (sessionId: string) => Promise<void>;
  refreshRecentSessions: () => Promise<void>;
  clearError: () => void;
}

// ---- Internal helpers ----

let _abortController: AbortController | null = null;

function makeAgentMessage(): Extract<UIMessage, { kind: 'agent' }> {
  return { kind: 'agent', id: `agent-${Date.now()}`, parts: [], ts: Date.now() };
}

function applyEvent(
  messages: UIMessage[],
  event: AgentEvent,
): { messages: UIMessage[]; pendingConfirm: UIConfirmPart | null; sessionId: string | null } {
  const msgs = [...messages];
  let pendingConfirm: UIConfirmPart | null = getPendingConfirmPart(msgs);
  let sessionId: string | null = event.session_id ?? null;

  const lastMsg = msgs[msgs.length - 1];
  const ensureAgent = (): Extract<UIMessage, { kind: 'agent' }> => {
    if (lastMsg?.kind === 'agent') return lastMsg as Extract<UIMessage, { kind: 'agent' }>;
    const newMsg = makeAgentMessage();
    msgs.push(newMsg);
    return newMsg;
  };

  switch (event.type) {
    case 'message': {
      const agent = ensureAgent();
      const parts: UIPart[] = [...agent.parts, { kind: 'text', text: event.text }];
      msgs[msgs.length - 1] = { ...agent, parts };
      break;
    }

    case 'tool_call': {
      const agent = ensureAgent();
      const part: UIToolPart = {
        kind: 'tool',
        callId: event.call_id,
        tool: event.tool,
        args: event.args,
        status: 'running',
      };
      msgs[msgs.length - 1] = { ...agent, parts: [...agent.parts, part] };
      break;
    }

    case 'tool_result': {
      const agent = ensureAgent();
      const parts = agent.parts.map((p): UIPart => {
        if (p.kind === 'tool' && p.callId === event.call_id) {
          return { ...p, status: 'ok', result: event.result, durationMs: event.duration_ms };
        }
        return p;
      });
      msgs[msgs.length - 1] = { ...agent, parts };
      break;
    }

    case 'tool_error': {
      const agent = ensureAgent();
      const parts = agent.parts.map((p): UIPart => {
        if (p.kind === 'tool' && p.callId === event.call_id) {
          return { ...p, status: 'error', error: event.error };
        }
        return p;
      });
      msgs[msgs.length - 1] = { ...agent, parts };
      break;
    }

    case 'require_confirm': {
      const agent = ensureAgent();
      const confirmPart: UIConfirmPart = {
        kind: 'confirm',
        callId: event.call_id,
        tool: event.tool,
        args: event.args,
        estCostUsd: event.est_cost_usd,
        status: 'pending',
      };
      msgs[msgs.length - 1] = { ...agent, parts: [...agent.parts, confirmPart] };
      pendingConfirm = confirmPart;
      break;
    }
  }

  return { messages: msgs, pendingConfirm, sessionId };
}

// ---- Store ----

export const useAgentStore = create<AgentStore>((set, get) => ({
  sessionId: null,
  messages: [],
  pendingConfirm: null,
  streamState: 'idle',
  lastError: null,
  lastStateUpdate: null,
  recentSessions: [],
  recentSessionsLoadedAt: null,
  currentSessionCost: 0,

  sendMessage: async (text: string) => {
    const { sessionId, messages, streamState } = get();
    if (streamState === 'sending' || streamState === 'streaming') return;

    // Add user message to UI immediately
    const userMsg: UIMessage = {
      kind: 'user',
      id: `user-${Date.now()}`,
      text,
      ts: Date.now(),
    };

    set({
      messages: [...messages, userMsg],
      streamState: 'sending',
      lastError: null,
    });

    _abortController = new AbortController();

    try {
      let resolvedSessionId = sessionId;

      await agentClient.sendTurn(
        { session_id: sessionId, message: text },
        (event) => {
          // Capture session_id from first event
          if (!resolvedSessionId && event.session_id) {
            resolvedSessionId = event.session_id;
            set({ sessionId: resolvedSessionId });
          }

          set((state) => {
            const { messages: newMsgs, pendingConfirm, sessionId: sid } = applyEvent(
              state.messages,
              event,
            );

            if (event.type === 'require_confirm') {
              return { messages: newMsgs, pendingConfirm, sessionId: sid ?? state.sessionId, streamState: 'waiting_confirm' };
            }
            if (event.type === 'done') {
              return { messages: newMsgs, streamState: 'idle', sessionId: sid ?? state.sessionId };
            }
            if (event.type === 'error') {
              return {
                messages: newMsgs,
                streamState: 'error',
                lastError: { code: event.code, message: event.message },
                sessionId: sid ?? state.sessionId,
              };
            }
            if (event.type === 'state_update') {
              return {
                messages: newMsgs,
                streamState: 'streaming',
                sessionId: sid ?? state.sessionId,
                lastStateUpdate: { jobId: event.job_id, tool: event.tool, ts: Date.now() },
              };
            }
            return { messages: newMsgs, streamState: 'streaming', sessionId: sid ?? state.sessionId };
          });
        },
        _abortController.signal,
      );
    } catch (err) {
      if ((err as Error).name === 'AbortError') {
        set({ streamState: 'idle' });
        return;
      }
      set({
        streamState: 'error',
        lastError: { code: 'network', message: (err as Error).message },
      });
    }
  },

  acceptConfirm: async () => {
    const { pendingConfirm, sessionId } = get();
    if (!pendingConfirm || !sessionId) return;

    // Mark confirm as accepted in UI
    set((state) => ({
      messages: state.messages.map((msg) => {
        if (msg.kind !== 'agent') return msg;
        return {
          ...msg,
          parts: msg.parts.map((p) => {
            if (p.kind === 'confirm' && p.callId === pendingConfirm.callId) {
              return { ...p, status: 'accepted' as const };
            }
            return p;
          }),
        };
      }),
      pendingConfirm: null,
      streamState: 'sending',
    }));

    _abortController = new AbortController();

    try {
      await agentClient.sendTurn(
        { session_id: sessionId, message: '', approved_call_ids: [pendingConfirm.callId] },
        (event) => {
          set((state) => {
            const { messages: newMsgs, pendingConfirm: pc, sessionId: sid } = applyEvent(
              state.messages,
              event,
            );
            if (event.type === 'require_confirm') {
              return { messages: newMsgs, pendingConfirm: pc, streamState: 'waiting_confirm', sessionId: sid ?? state.sessionId };
            }
            if (event.type === 'done') {
              return { messages: newMsgs, streamState: 'idle', sessionId: sid ?? state.sessionId };
            }
            if (event.type === 'error') {
              return {
                messages: newMsgs,
                streamState: 'error',
                lastError: { code: event.code, message: event.message },
                sessionId: sid ?? state.sessionId,
              };
            }
            if (event.type === 'state_update') {
              return {
                messages: newMsgs,
                streamState: 'streaming',
                sessionId: sid ?? state.sessionId,
                lastStateUpdate: { jobId: event.job_id, tool: event.tool, ts: Date.now() },
              };
            }
            return { messages: newMsgs, streamState: 'streaming', sessionId: sid ?? state.sessionId };
          });
        },
        _abortController.signal,
      );
    } catch (err) {
      set({
        streamState: 'error',
        lastError: { code: 'network', message: (err as Error).message },
      });
    }
  },

  declineConfirm: () => {
    const { pendingConfirm } = get();
    if (!pendingConfirm) return;

    set((state) => ({
      messages: state.messages.map((msg) => {
        if (msg.kind !== 'agent') return msg;
        return {
          ...msg,
          parts: msg.parts.map((p) => {
            if (p.kind === 'confirm' && p.callId === pendingConfirm.callId) {
              return { ...p, status: 'declined' as const };
            }
            return p;
          }),
        };
      }),
      pendingConfirm: null,
      streamState: 'idle',
    }));
  },

  loadSession: async (targetSessionId: string) => {
    try {
      const detail = await agentClient.getSession(targetSessionId);
      const messages = historyToMessages(detail.history);
      set({
        sessionId: targetSessionId,
        messages,
        pendingConfirm: getPendingConfirmPart(messages),
        streamState: 'idle',
        lastError: null,
        currentSessionCost: detail.totalCostUsd,
      });
    } catch (err) {
      set({
        streamState: 'error',
        lastError: { code: 'load_failed', message: (err as Error).message },
      });
    }
  },

  newSession: () => {
    _abortController?.abort();
    set({
      sessionId: null,
      messages: [],
      pendingConfirm: null,
      streamState: 'idle',
      lastError: null,
      lastStateUpdate: null,
      currentSessionCost: 0,
    });
  },

  deleteSession: async (targetSessionId: string) => {
    await agentClient.deleteSession(targetSessionId);
    set((state) => ({
      recentSessions: state.recentSessions.filter((s) => s.sessionId !== targetSessionId),
      // If deleting current session, clear it
      ...(state.sessionId === targetSessionId
        ? { sessionId: null, messages: [], pendingConfirm: null, streamState: 'idle' as StreamState }
        : {}),
    }));
  },

  refreshRecentSessions: async () => {
    try {
      const sessions = await agentClient.listSessions(20);
      set({ recentSessions: sessions, recentSessionsLoadedAt: Date.now() });
    } catch {
      // Non-critical; silently fail
    }
  },

  clearError: () => set({ lastError: null, streamState: 'idle' }),
}));
