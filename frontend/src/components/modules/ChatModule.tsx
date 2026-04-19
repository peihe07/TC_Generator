'use client';

import React, { useEffect, useRef } from 'react';
import { RiAddLine, RiHistoryLine, RiDownloadLine } from '@remixicon/react';
import { useAgentStore } from '../../store/useAgentStore';
import { agentClient } from '../../services/agentClient';
import { IconButton } from '../ui';
import MessageList from './chat/MessageList';
import InspectorPanel from './chat/InspectorPanel';
import InputArea from './chat/InputArea';

export default function ChatModule() {
  const {
    messages,
    streamState,
    lastError,
    sessionId,
    newSession,
    refreshRecentSessions,
    clearError,
  } = useAgentStore();

  const didMount = useRef(false);

  useEffect(() => {
    if (didMount.current) return;
    didMount.current = true;
    refreshRecentSessions();
  }, [refreshRecentSessions]);

  const handleExportTrace = async () => {
    if (!sessionId) return;
    try {
      const blob = await agentClient.downloadTrace(sessionId);
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `trace-${sessionId}.jsonl`;
      a.click();
      URL.revokeObjectURL(url);
    } catch {
      // ignore
    }
  };

  return (
    <div className="chat-module">
      {/* Header */}
      <div className="chat-header">
        <span className="chat-header-title">Agent Co-pilot</span>
        <div className="chat-header-actions">
          <IconButton label="New Session" onClick={newSession}>
            <RiAddLine size={14} />
          </IconButton>
          <IconButton label="Sessions" onClick={refreshRecentSessions}>
            <RiHistoryLine size={14} />
          </IconButton>
          {sessionId && (
            <IconButton label="Export Trace" onClick={handleExportTrace}>
              <RiDownloadLine size={14} />
            </IconButton>
          )}
        </div>
      </div>

      {/* Body */}
      <div className="chat-body">
        <div className="chat-main">
          {/* Error banner */}
          {streamState === 'error' && lastError && (
            <div className="chat-error-banner">
              [{lastError.code}] {lastError.message}
              <button className="chat-error-dismiss" onClick={clearError}>×</button>
            </div>
          )}

          {/* Messages */}
          <div className="chat-scroll">
            <MessageList messages={messages} />
          </div>

          {/* Input */}
          <InputArea />
        </div>

        {/* Inspector sidebar */}
        <InspectorPanel />
      </div>
    </div>
  );
}
