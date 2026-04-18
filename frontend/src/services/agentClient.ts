import type {
  AgentEvent,
  SessionDetail,
  SessionSummary,
  UIMessage,
  UIPart,
  UIToolPart,
  UIConfirmPart,
} from './agentEvents';

const API_BASE = '/api/agent';

// ---- SSE client ----

export interface SendTurnRequest {
  session_id: string | null;
  message: string;
  approved_call_ids?: string[];
}

export class AgentClient {
  private _inFlight = false;

  async sendTurn(
    req: SendTurnRequest,
    onEvent: (event: AgentEvent) => void,
    signal?: AbortSignal,
  ): Promise<void> {
    if (this._inFlight) {
      throw new Error('A turn is already in flight. Wait for it to complete.');
    }
    this._inFlight = true;
    try {
      await this._streamTurn(req, onEvent, signal);
    } finally {
      this._inFlight = false;
    }
  }

  private async _streamTurn(
    req: SendTurnRequest,
    onEvent: (event: AgentEvent) => void,
    signal?: AbortSignal,
  ): Promise<void> {
    const response = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req),
      signal,
    });

    if (!response.ok) {
      throw new Error(`Agent chat failed: ${response.status}`);
    }

    const reader = response.body?.getReader();
    if (!reader) throw new Error('Response has no body');

    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const events = buffer.split('\n\n');
      // Last element may be incomplete; keep it in buffer
      buffer = events.pop() ?? '';

      for (const raw of events) {
        const parsed = parseSSEEvent(raw);
        if (parsed) onEvent(parsed);
      }
    }

    // Flush any remaining buffer content
    if (buffer.trim()) {
      const parsed = parseSSEEvent(buffer);
      if (parsed) onEvent(parsed);
    }
  }

  async getSession(sessionId: string): Promise<SessionDetail> {
    const res = await fetch(`${API_BASE}/sessions/${sessionId}`);
    if (!res.ok) throw new Error(`Session not found: ${sessionId}`);
    const data = await res.json();
    return {
      sessionId: data.sessionId,
      history: data.history ?? [],
      totalCostUsd: data.totalCostUsd ?? 0,
      createdAt: data.createdAt,
      updatedAt: data.updatedAt,
      messageCount: (data.history ?? []).length,
    };
  }

  async listSessions(limit = 20): Promise<SessionSummary[]> {
    const res = await fetch(`${API_BASE}/sessions?limit=${limit}`);
    if (!res.ok) throw new Error('Failed to list sessions');
    const data = await res.json();
    return data.sessions ?? [];
  }

  async deleteSession(sessionId: string): Promise<void> {
    const res = await fetch(`${API_BASE}/sessions/${sessionId}`, { method: 'DELETE' });
    if (!res.ok) throw new Error(`Failed to delete session: ${sessionId}`);
  }

  async downloadTrace(sessionId: string): Promise<Blob> {
    const res = await fetch(`${API_BASE}/sessions/${sessionId}/trace`);
    if (!res.ok) throw new Error('Failed to download trace');
    return res.blob();
  }
}

// ---- SSE parsing ----

function parseSSEEvent(raw: string): AgentEvent | null {
  let eventType = '';
  let dataLine = '';

  for (const line of raw.split('\n')) {
    if (line.startsWith('event: ')) {
      eventType = line.slice('event: '.length).trim();
    } else if (line.startsWith('data: ')) {
      dataLine = line.slice('data: '.length).trim();
    }
  }

  if (!eventType || !dataLine) return null;

  try {
    const data = JSON.parse(dataLine);
    return { type: eventType, ...data } as AgentEvent;
  } catch {
    return null;
  }
}

// ---- OpenAI history → UIMessage[] conversion ----

type OpenAIMessage = {
  role: 'user' | 'assistant' | 'tool' | 'system';
  content?: string | null;
  tool_calls?: Array<{
    id: string;
    type: string;
    function: { name: string; arguments: string };
  }>;
  tool_call_id?: string;
};

export function historyToMessages(history: Array<Record<string, unknown>>): UIMessage[] {
  const messages: UIMessage[] = [];
  let currentAgent: Extract<UIMessage, { kind: 'agent' }> | null = null;

  const flushAgent = () => {
    if (currentAgent) {
      messages.push(currentAgent);
      currentAgent = null;
    }
  };

  for (const raw of history as OpenAIMessage[]) {
    if (raw.role === 'system') continue;

    if (raw.role === 'user') {
      flushAgent();
      messages.push({
        kind: 'user',
        id: `user-${messages.length}`,
        text: typeof raw.content === 'string' ? raw.content : '',
        ts: Date.now(),
      });
      continue;
    }

    if (raw.role === 'assistant') {
      flushAgent();
      const parts: UIPart[] = [];

      if (raw.content) {
        parts.push({ kind: 'text', text: raw.content });
      }

      for (const call of raw.tool_calls ?? []) {
        let args: Record<string, unknown> = {};
        try { args = JSON.parse(call.function.arguments || '{}'); } catch { /* ignore */ }
        const part: UIToolPart = {
          kind: 'tool',
          callId: call.id,
          tool: call.function.name,
          args,
          status: 'ok', // history entries are completed turns
        };
        parts.push(part);
      }

      if (parts.length > 0) {
        currentAgent = {
          kind: 'agent',
          id: `agent-${messages.length}`,
          parts,
          ts: Date.now(),
        };
      }
      continue;
    }

    if (raw.role === 'tool' && raw.tool_call_id) {
      // Fill in the result for the matching tool part
      if (currentAgent) {
        const part = currentAgent.parts.find(
          (p): p is UIToolPart =>
            p.kind === 'tool' && p.callId === raw.tool_call_id,
        );
        if (part) {
          try {
            const parsed = JSON.parse(typeof raw.content === 'string' ? raw.content : '{}');
            part.result = parsed.result;
          } catch { /* ignore */ }
        }
      }
    }
  }

  flushAgent();
  return messages;
}

// ---- Helpers ----

export function getSessionPreview(messages: UIMessage[]): string {
  const first = messages.find((m) => m.kind === 'user');
  if (!first || first.kind !== 'user') return '(empty session)';
  return first.text.slice(0, 40) + (first.text.length > 40 ? '…' : '');
}

// Determine which tool part needs confirmation from a list of confirm parts
export function getPendingConfirmPart(
  messages: UIMessage[],
): UIConfirmPart | null {
  for (let i = messages.length - 1; i >= 0; i--) {
    const msg = messages[i];
    if (msg.kind !== 'agent') continue;
    for (const part of msg.parts) {
      if (part.kind === 'confirm' && part.status === 'pending') return part;
    }
  }
  return null;
}

export const agentClient = new AgentClient();
