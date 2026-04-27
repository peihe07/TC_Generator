'use client';

import React, { useEffect, useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import {
  fetchSpecLibrary,
  parseJobFiles,
  type SpecLibraryEntry,
} from '../../../services/jobAdapter';
import { RiFileLine, RiFileExcel2Line, RiFileSearchLine, RiArrowRightLine } from '@remixicon/react';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import { Button, Select } from '../../ui';

export function formatSpecLibraryLabel(name: string): string {
  const matches = [...name.matchAll(/(?:^|[_\s])HMI(?=$|[_\s])/g)];
  if (matches.length === 0) return name;

  const first = matches[0];
  const firstIndex = first.index ?? 0;
  const contentStart = firstIndex + first[0].length;
  const contentEnd =
    matches[1]?.index ??
    name.search(/_R\d(?:_|$)|_\([^)]*\)$/);
  const rawLabel = name.slice(
    contentStart,
    contentEnd > contentStart ? contentEnd : undefined,
  );
  const label = rawLabel.replace(/^[_\s]+|[_\s]+$/g, '').replace(/_/g, ' ').trim();
  return label || name;
}

const UploadModule: React.FC = () => {
  const { setJobMetadata, setTcRows, updateStats, appendLog } = useJobStore();
  const { advanceWindow } = useWindowStore();
  const [isParsing, setIsParsing] = useState(false);
  const [parseError, setParseError] = useState('');
  const [files, setFiles] = useState<{ tc?: File; referenceWorkbook?: File; spec?: File }>({});
  const [draggingZone, setDraggingZone] = useState<'tc' | 'referenceWorkbook' | 'spec' | null>(null);
  const [specLibrary, setSpecLibrary] = useState<SpecLibraryEntry[]>([]);
  const [selectedSpecName, setSelectedSpecName] = useState<string>('');
  const [libraryError, setLibraryError] = useState('');

  useEffect(() => {
    let cancelled = false;
    fetchSpecLibrary()
      .then((list) => {
        if (!cancelled) setSpecLibrary(list);
      })
      .catch((err) => {
        if (!cancelled) {
          const message =
            err instanceof Error ? err.message : 'Failed to load spec library.';
          setLibraryError(message);
        }
      });
    return () => {
      cancelled = true;
    };
  }, []);
  const tcInputRef = useRef<HTMLInputElement | null>(null);
  const referenceWorkbookInputRef = useRef<HTMLInputElement | null>(null);
  const specInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileDrop = (e: React.DragEvent, type: 'tc' | 'referenceWorkbook' | 'spec') => {
    e.preventDefault();
    setDraggingZone(null);
    const file = e.dataTransfer.files[0];
    if (file) {
      setParseError('');
      setFiles((prev) => ({ ...prev, [type]: file }));
    }
  };

  const handleDragEnter = (e: React.DragEvent, type: 'tc' | 'referenceWorkbook' | 'spec') => {
    e.preventDefault();
    setDraggingZone(type);
  };
  const handleDragLeave = (e: React.DragEvent, type: 'tc' | 'referenceWorkbook' | 'spec') => {
    e.preventDefault();
    // 只有當離開的目標即為 dropzone 本體時才重設，避免子元素觸發誤判
    if (e.currentTarget === e.target) setDraggingZone((z) => (z === type ? null : z));
  };

  const handleFileSelect = (
    event: React.ChangeEvent<HTMLInputElement>,
    type: 'tc' | 'referenceWorkbook' | 'spec',
  ) => {
    const file = event.target.files?.[0];
    if (file) {
      setParseError('');
      setFiles((prev) => ({ ...prev, [type]: file }));
    }
  };

  const handleNext = async () => {
    if (!files.tc || isParsing) {
      return;
    }

    setIsParsing(true);
    setParseError('');
    appendLog(
      createJobLog(
        'info',
        `Parsing ${files.tc.name} through the shared job adapter.`,
      ),
    );

    try {
      const result = await parseJobFiles({
        rawFile: files.tc,
        referenceWorkbookFile: selectedSpecName ? undefined : files.referenceWorkbook,
        specFile: files.spec,
        selectedSpecName: selectedSpecName || undefined,
      });

      setJobMetadata(result.jobMetadata);
      setTcRows(result.rows);
      // 只覆寫每筆 job 的進度欄位；token/cost 累積值保留。
      updateStats({
        total: result.stats.total,
        processed: 0,
        success: 0,
        fail: 0,
      });
      appendLog(
        createJobLog(
          'success',
          `Loaded ${result.rows.length} row(s) for ${result.jobMetadata.projectName}.`,
        ),
      );
      advanceWindow('upload', 'configure', 'TC Generator - Configuration');
    } catch (error) {
      const message =
        error instanceof Error ? error.message : 'Failed to parse the selected workbook.';
      setParseError(message);
      appendLog(
        createJobLog(
          'error',
          message,
        ),
      );
    } finally {
      setIsParsing(false);
    }
  };

  const buildContext = () => {
    const fileName = files.tc?.name ?? '未上傳';
    return `[context: 目前在 Upload Module]\n[目前檔案: ${fileName}]\n`;
  };
  const dropzoneStyle: React.CSSProperties = { height: 112 };

  return (
    <div className="flex flex-col h-full min-h-0 gap-3 overflow-hidden">
      <div className="flex justify-end shrink-0">
        <HelpFromAgentButton contextPrompt={buildContext()} title="求助 AI" />
      </div>
      <div className="flex-1 min-h-0 overflow-auto flex flex-col gap-3 pr-1">
        <fieldset className="p-3 border-sunken min-w-0 [min-inline-size:0]">
          <legend className="px-2 max-w-full truncate">TC Specification (.xlsx)</legend>
          <div
            className={`dropzone-sunken h-28 ${draggingZone === 'tc' ? 'dragging' : ''} ${files.tc ? 'bg-white' : ''}`}
            onClick={() => tcInputRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDragEnter={(e) => handleDragEnter(e, 'tc')}
            onDragLeave={(e) => handleDragLeave(e, 'tc')}
            onDrop={(e) => handleFileDrop(e, 'tc')}
            style={dropzoneStyle}
          >
            <RiFileExcel2Line className="size-10" style={{ color: 'var(--text-muted)' }} />
            <span className="text-xs truncate px-2 w-full text-center">
              {files.tc ? files.tc.name : 'Drag & Drop TC Spec Excel here'}
            </span>
            {files.tc && (
              <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>[READY]</span>
            )}
          </div>
          <input
            ref={tcInputRef}
            hidden
            type="file"
            accept=".xlsx,.xlsm"
            onChange={(event) => handleFileSelect(event, 'tc')}
          />
        </fieldset>

        <div
          className="grid gap-3 min-w-0"
          style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(min(220px, 100%), 1fr))' }}
        >
          <fieldset className="p-3 border-sunken min-w-0 [min-inline-size:0] overflow-hidden">
            <legend className="px-2 max-w-full truncate">Reference Workbook (Optional)</legend>
            <div className="flex flex-col gap-2 mb-2 min-h-[52px]">
              <label className="text-xs flex flex-col items-stretch gap-1 min-w-0">
                <span className="whitespace-nowrap">From library:</span>
                <Select
                  className="w-full min-w-0"
                  value={selectedSpecName}
                  onChange={(e) => {
                    setSelectedSpecName(e.target.value);
                    setParseError('');
                  }}
                >
                  <option value="">— None (use upload below) —</option>
                  {specLibrary.map((spec) => (
                    <option key={spec.name} value={spec.name}>
                      {formatSpecLibraryLabel(spec.name)}
                      {spec.entriesCount != null ? ` (${spec.entriesCount})` : ''}
                    </option>
                  ))}
                </Select>
              </label>
              {libraryError && (
                <span className="text-[10px]" style={{ color: 'var(--status-reject-dark)' }}>
                  {libraryError}
                </span>
              )}
            </div>
            <div
              className={`dropzone-sunken h-28 min-w-0 overflow-hidden ${draggingZone === 'referenceWorkbook' ? 'dragging' : ''} ${files.referenceWorkbook && !selectedSpecName ? 'bg-white' : ''}`}
              onClick={() => {
                if (selectedSpecName) return;
                referenceWorkbookInputRef.current?.click();
              }}
              onDrop={(e) => {
                if (selectedSpecName) return;
                handleFileDrop(e, 'referenceWorkbook');
              }}
              onDragOver={(e) => e.preventDefault()}
              onDragEnter={(e) => handleDragEnter(e, 'referenceWorkbook')}
              onDragLeave={(e) => handleDragLeave(e, 'referenceWorkbook')}
              style={
                selectedSpecName
                  ? { ...dropzoneStyle, opacity: 0.5, cursor: 'not-allowed' }
                  : dropzoneStyle
              }
            >
              <RiFileSearchLine className="size-10" style={{ color: 'var(--text-muted)' }} />
              <span className="text-xs truncate px-2 w-full text-center">
                {selectedSpecName
                  ? 'Library spec selected'
                  : files.referenceWorkbook
                    ? files.referenceWorkbook.name
                    : 'Drop Reference Excel'}
              </span>
              {files.referenceWorkbook && !selectedSpecName && (
                <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>[READY]</span>
              )}
            </div>
            <input
              ref={referenceWorkbookInputRef}
              hidden
              type="file"
              accept=".xlsx,.xlsm"
              onChange={(event) => handleFileSelect(event, 'referenceWorkbook')}
            />
          </fieldset>

          <fieldset className="p-3 border-sunken min-w-0 [min-inline-size:0] overflow-hidden">
            <legend className="px-2 max-w-full truncate">Reference PDF/DOCX</legend>
            <div className="mb-2 min-h-[52px]" aria-hidden="true" />
            <div
              className={`dropzone-sunken h-28 min-w-0 overflow-hidden ${draggingZone === 'spec' ? 'dragging' : ''} ${files.spec ? 'bg-white' : ''}`}
              onClick={() => specInputRef.current?.click()}
              onDrop={(e) => handleFileDrop(e, 'spec')}
              onDragOver={(e) => e.preventDefault()}
              onDragEnter={(e) => handleDragEnter(e, 'spec')}
              onDragLeave={(e) => handleDragLeave(e, 'spec')}
              style={dropzoneStyle}
            >
              <RiFileLine className="size-10" style={{ color: 'var(--text-muted)' }} />
              <span className="text-xs truncate px-2 w-full text-center">
                {files.spec ? files.spec.name : 'Drop Reference Doc'}
              </span>
              {files.spec && (
                <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>[READY]</span>
              )}
            </div>
            <input
              ref={specInputRef}
              hidden
              type="file"
              accept=".pdf,.docx,.xlsx"
              onChange={(event) => handleFileSelect(event, 'spec')}
            />
          </fieldset>
        </div>

        {files.tc && (
          <div className="status-bar-field p-2 text-xs flex items-center gap-2">
            <span className="font-bold">[READY]</span>
            Workbook staged. Parse the job to populate the shared desktop state.
          </div>
        )}
        {parseError && (
          <div
            className="status-bar-field p-2 text-xs"
            style={{ color: 'var(--status-reject-dark)' }}
            role="alert"
          >
            <span className="font-bold">[PARSE ERROR]</span> {parseError}
          </div>
        )}
      </div>

      <div
        className="flex justify-end pt-4"
        style={{ borderTop: '1px solid var(--win95-gray-mid)' }}
      >
        <Button
          className="flex items-center gap-2"
          disabled={!files.tc || isParsing}
          onClick={() => void handleNext()}
        >
          {isParsing ? 'Parsing...' : 'Parse & Next'} <RiArrowRightLine className="size-4" />
        </Button>
      </div>
    </div>
  );
};

export default UploadModule;
