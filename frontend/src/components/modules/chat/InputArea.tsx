'use client';

import React, { useRef, useState, useCallback, useEffect } from 'react';
import { RiSendPlaneLine, RiAttachmentLine, RiLoader4Line } from '@remixicon/react';
import { useAgentStore } from '../../../store/useAgentStore';
import { parseJobFiles } from '../../../services/jobAdapter';
import { Button, IconButton } from '../../ui';

export default function InputArea() {
  const [text, setText] = useState('');
  const [isParsing, setIsParsing] = useState(false);
  const [isDragOver, setIsDragOver] = useState(false);
  const [parseError, setParseError] = useState('');
  const { streamState, sendMessage } = useAgentStore();
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const isDisabled = streamState === 'sending' || streamState === 'streaming';

  useEffect(() => {
    const handler = (e: Event) => {
      const prompt = (e as CustomEvent<string>).detail;
      setText((prev) => prompt + prev);
      textareaRef.current?.focus();
    };
    window.addEventListener('agent-prefill', handler);
    return () => window.removeEventListener('agent-prefill', handler);
  }, []);

  const handleSend = async () => {
    const trimmed = text.trim();
    if (!trimmed || isDisabled) return;
    setText('');
    await sendMessage(trimmed);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleFile = useCallback(async (file: File) => {
    if (!file.name.match(/\.(xlsx|xlsm)$/i)) {
      setParseError('只支援 .xlsx / .xlsm 附件。');
      return;
    }
    setIsParsing(true);
    setParseError('');
    try {
      const result = await parseJobFiles({ rawFile: file });
      const preview = `附件：${file.name} (job=${result.jobMetadata.jobId}，${result.jobMetadata.totalRows} rows)\n`;
      setText((prev) => preview + prev);
      textareaRef.current?.focus();
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Parse failed.';
      setParseError(message);
      setText((prev) => `[Parse 失敗：${file.name} - ${message}]\n` + prev);
    } finally {
      setIsParsing(false);
    }
  }, []);

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
    e.target.value = '';
  };

  return (
    <div
      className={`chat-input-area ${isDragOver ? 'drag-over' : ''}`}
      onDragOver={(e) => { e.preventDefault(); setIsDragOver(true); }}
      onDragLeave={() => setIsDragOver(false)}
      onDrop={handleDrop}
    >
      <textarea
        ref={textareaRef}
        className="chat-textarea"
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={
          isDragOver
            ? '拖放 xlsx 檔案…'
            : isDisabled
            ? 'Agent 處理中…'
            : '輸入訊息（Enter 送出，Shift+Enter 換行）'
        }
        disabled={isDisabled}
        rows={3}
      />

      <div className="chat-input-btns">
        <input
          ref={fileInputRef}
          type="file"
          accept=".xlsx,.xlsm"
          style={{ display: 'none' }}
          onChange={handleFileInput}
        />
        <IconButton
          label="附加 xlsx 檔案"
          onClick={() => fileInputRef.current?.click()}
          disabled={isDisabled || isParsing}
        >
          {isParsing ? <RiLoader4Line size={14} className="spin" /> : <RiAttachmentLine size={14} />}
        </IconButton>
        <Button
          className="chat-send-btn"
          onClick={handleSend}
          disabled={!text.trim() || isDisabled}
        >
          <RiSendPlaneLine size={16} />
        </Button>
      </div>
      {parseError && (
        <div className="chat-attach-error" role="alert">
          {parseError}
        </div>
      )}
    </div>
  );
}
