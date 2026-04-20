'use client';

import React from 'react';
import { RiTimeLine, RiHistoryLine, RiRefreshLine } from '@remixicon/react';
import { useAgentStore } from '../../../store/useAgentStore';
import { useJobStore } from '../../../store/useJobStore';
import type { UIToolPart } from '../../../services/agentEvents';
import { getSessionPreview } from '../../../services/agentClient';
import { Button } from '../../ui';

export default function InspectorPanel() {
  const {
    messages,
    recentSessions,
    sessionId,
    currentSessionCost,
    loadSession,
    deleteSession,
    refreshRecentSessions,
  } = useAgentStore();
  const { jobMetadata: currentJob, stats } = useJobStore();

  // Collect last 20 tool parts from current session
  const toolParts: UIToolPart[] = [];
  for (const msg of messages) {
    if (msg.kind !== 'agent') continue;
    for (const part of msg.parts) {
      if (part.kind === 'tool') toolParts.push(part);
    }
  }
  const recentTools = toolParts.slice(-20);

  return (
    <div className="inspector-panel">
      {/* Current Job */}
      <section className="inspector-section">
        <div className="inspector-section-title">作用中 Job</div>
        {currentJob ? (
          <div className="inspector-job-box">
            <div className="inspector-row">
              <span className="inspector-label">Job ID</span>
              <span className="inspector-value">{currentJob.jobId}</span>
            </div>
            <div className="inspector-row">
              <span className="inspector-label">Project</span>
              <span className="inspector-value">{currentJob.projectName}</span>
            </div>
            <div className="inspector-row">
              <span className="inspector-label">Rows</span>
              <span className="inspector-value">{currentJob.totalRows}</span>
            </div>
            {stats.cost > 0 && (
              <div className="inspector-row">
                <span className="inspector-label">費用</span>
                <span className="inspector-value">${stats.cost.toFixed(4)}</span>
              </div>
            )}
          </div>
        ) : (
          <div className="inspector-empty">無作用中 Job</div>
        )}
      </section>

      {/* Cost */}
      {sessionId && (
        <section className="inspector-section">
          <div className="inspector-section-title">本次費用</div>
          <div className="inspector-cost">${currentSessionCost.toFixed(4)}</div>
        </section>
      )}

      {/* Tool trace */}
      {recentTools.length > 0 && (
        <section className="inspector-section">
          <div className="inspector-section-title">
            <RiTimeLine size={12} /> Tool Trace
          </div>
          <div className="inspector-trace-list">
            {recentTools.map((p) => (
              <div key={p.callId} className={`inspector-trace-item status-${p.status}`}>
                <span className="trace-tool">{p.tool}</span>
                {p.durationMs !== undefined && (
                  <span className="trace-dur">{p.durationMs}ms</span>
                )}
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Recent sessions */}
      <section className="inspector-section">
        <div className="inspector-section-title">
          <RiHistoryLine size={12} />
          <span className="flex-1">近期 Sessions</span>
          <button
            type="button"
            className="inspector-section-refresh"
            onClick={refreshRecentSessions}
            title="重新整理 Sessions"
            aria-label="重新整理 Sessions"
          >
            <RiRefreshLine size={12} />
          </button>
        </div>
        {recentSessions.length === 0 ? (
          <div className="inspector-empty">無記錄</div>
        ) : (
          <div className="inspector-session-list">
            {recentSessions.slice(0, 10).map((s) => (
              <div
                key={s.sessionId}
                className={`inspector-session-item ${s.sessionId === sessionId ? 'active' : ''}`}
              >
                <Button
                  className="inspector-session-btn"
                  onClick={() => loadSession(s.sessionId)}
                  title={s.sessionId}
                >
                  <span className="session-preview">
                    {getSessionPreview(s.sessionId === sessionId ? messages : [])}
                  </span>
                  <span className="session-cost">${s.totalCostUsd.toFixed(4)}</span>
                </Button>
                <Button
                  className="inspector-session-delete"
                  onClick={() => deleteSession(s.sessionId)}
                  title="刪除"
                  aria-label="刪除"
                >
                  ×
                </Button>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
