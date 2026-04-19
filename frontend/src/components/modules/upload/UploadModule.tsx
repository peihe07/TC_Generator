'use client';

import React, { useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { parseJobFiles } from '../../../services/jobAdapter';
import { RiFileLine, RiFileExcel2Line, RiFileSearchLine, RiArrowRightLine } from '@remixicon/react';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import { Button } from '../../ui';

const UploadModule: React.FC = () => {
  const { setJobMetadata, setTcRows, updateStats, appendLog } = useJobStore();
  const { openWindow } = useWindowStore();
  const [isParsing, setIsParsing] = useState(false);
  const [files, setFiles] = useState<{ tc?: File; referenceWorkbook?: File; spec?: File }>({});
  const [draggingZone, setDraggingZone] = useState<'tc' | 'referenceWorkbook' | 'spec' | null>(null);
  const tcInputRef = useRef<HTMLInputElement | null>(null);
  const referenceWorkbookInputRef = useRef<HTMLInputElement | null>(null);
  const specInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileDrop = (e: React.DragEvent, type: 'tc' | 'referenceWorkbook' | 'spec') => {
    e.preventDefault();
    setDraggingZone(null);
    const file = e.dataTransfer.files[0];
    if (file) {
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
      setFiles((prev) => ({ ...prev, [type]: file }));
    }
  };

  const handleNext = async () => {
    if (!files.tc || isParsing) {
      return;
    }

    setIsParsing(true);
    appendLog(
      createJobLog(
        'info',
        `Parsing ${files.tc.name} through the shared job adapter.`,
      ),
    );

    try {
      const result = await parseJobFiles({
        rawFile: files.tc,
        referenceWorkbookFile: files.referenceWorkbook,
        specFile: files.spec,
      });

      setJobMetadata(result.jobMetadata);
      setTcRows(result.rows);
      updateStats(result.stats);
      appendLog(
        createJobLog(
          'success',
          `Loaded ${result.rows.length} row(s) for ${result.jobMetadata.projectName}.`,
        ),
      );
      openWindow('configure', 'TC Generator - Configuration');
    } catch (error) {
      appendLog(
        createJobLog(
          'error',
          error instanceof Error ? error.message : 'Failed to parse the selected workbook.',
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

  return (
    <div className="flex flex-col h-full gap-4">
      <div className="flex justify-end">
        <HelpFromAgentButton contextPrompt={buildContext()} title="求助 AI" />
      </div>
      <div className="flex-1 flex flex-col gap-6">
        <fieldset className="p-4 border-2 border-sunken">
          <legend className="px-2 font-bold">TC Specification (.xlsx)</legend>
          <div
            className={`dropzone-sunken h-32 ${draggingZone === 'tc' ? 'dragging' : ''} ${files.tc ? 'bg-white' : ''}`}
            onClick={() => tcInputRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDragEnter={(e) => handleDragEnter(e, 'tc')}
            onDragLeave={(e) => handleDragLeave(e, 'tc')}
            onDrop={(e) => handleFileDrop(e, 'tc')}
          >
            <RiFileExcel2Line className="size-10 text-gray-600" />
            <span className="text-xs">
              {files.tc ? files.tc.name : 'Drag & Drop TC Spec Excel here'}
            </span>
            {files.tc && <span className="text-[10px] text-gray-500">[READY]</span>}
          </div>
          <input
            ref={tcInputRef}
            hidden
            type="file"
            accept=".xlsx,.xlsm"
            onChange={(event) => handleFileSelect(event, 'tc')}
          />
        </fieldset>

        <div className="grid grid-cols-2 gap-4">
          <fieldset className="p-4 border-2 border-sunken">
            <legend className="px-2 font-bold">Reference Workbook (Optional)</legend>
            <div
              className={`dropzone-sunken h-20 ${draggingZone === 'referenceWorkbook' ? 'dragging' : ''}`}
              onClick={() => referenceWorkbookInputRef.current?.click()}
              onDrop={(e) => handleFileDrop(e, 'referenceWorkbook')}
              onDragOver={(e) => e.preventDefault()}
              onDragEnter={(e) => handleDragEnter(e, 'referenceWorkbook')}
              onDragLeave={(e) => handleDragLeave(e, 'referenceWorkbook')}
            >
              <RiFileSearchLine className="size-6 text-gray-500" />
              <span className="text-[10px] truncate px-2 w-full text-center">
                {files.referenceWorkbook ? files.referenceWorkbook.name : 'Drop Reference Excel'}
              </span>
            </div>
            <input
              ref={referenceWorkbookInputRef}
              hidden
              type="file"
              accept=".xlsx,.xlsm"
              onChange={(event) => handleFileSelect(event, 'referenceWorkbook')}
            />
          </fieldset>

          <fieldset className="p-4 border-2 border-sunken">
            <legend className="px-2 font-bold">Reference PDF/DOCX</legend>
            <div
              className={`dropzone-sunken h-20 ${draggingZone === 'spec' ? 'dragging' : ''}`}
              onClick={() => specInputRef.current?.click()}
              onDrop={(e) => handleFileDrop(e, 'spec')}
              onDragOver={(e) => e.preventDefault()}
              onDragEnter={(e) => handleDragEnter(e, 'spec')}
              onDragLeave={(e) => handleDragLeave(e, 'spec')}
            >
              <RiFileLine className="size-6 text-gray-500" />
              <span className="text-[10px] truncate px-2 w-full text-center">
                {files.spec ? files.spec.name : 'Drop Reference Doc'}
              </span>
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
      </div>

      <div className="flex justify-end pt-4 border-t border-gray-400">
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
