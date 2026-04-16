'use client';

import React, { useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { parseJobFiles } from '../../../services/jobAdapter';
import { RiFileLine, RiFileExcel2Line, RiFileSearchLine, RiArrowRightLine } from '@remixicon/react';

const UploadModule: React.FC = () => {
  const { setJobMetadata, setTcRows, updateStats, appendLog } = useJobStore();
  const { openWindow } = useWindowStore();
  const [isParsing, setIsParsing] = useState(false);
  const [files, setFiles] = useState<{ tc?: File; sys1?: File; spec?: File }>({});
  const tcInputRef = useRef<HTMLInputElement | null>(null);
  const sys1InputRef = useRef<HTMLInputElement | null>(null);
  const specInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileDrop = (e: React.DragEvent, type: 'tc' | 'sys1' | 'spec') => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      setFiles((prev) => ({ ...prev, [type]: file }));
    }
  };

  const handleFileSelect = (
    event: React.ChangeEvent<HTMLInputElement>,
    type: 'tc' | 'sys1' | 'spec',
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

  return (
    <div className="flex flex-col h-full gap-4">
      <div className="flex-1 flex flex-col gap-6">
        <fieldset className="p-4 border-2 border-sunken">
          <legend className="px-2 font-bold">TC Specification (.xlsx)</legend>
          <div
            className={`h-24 border-2 border-dashed flex flex-col items-center justify-center gap-2 cursor-pointer transition-colors ${
              files.tc ? 'bg-green-50 border-green-500' : 'bg-gray-50 border-gray-400'
            }`}
            onClick={() => tcInputRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => handleFileDrop(e, 'tc')}
          >
            <RiFileExcel2Line className={`size-8 ${files.tc ? 'text-green-600' : 'text-gray-400'}`} />
            <span className="text-sm font-sans">
              {files.tc ? files.tc.name : 'Drag & Drop TC Spec Excel here'}
            </span>
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
            <legend className="px-2 font-bold text-sm">SYS1 Spec (Optional)</legend>
            <div
              className="h-20 border-2 border-dashed flex flex-col items-center justify-center gap-1 cursor-pointer bg-gray-50 border-gray-400"
              onClick={() => sys1InputRef.current?.click()}
              onDrop={(e) => handleFileDrop(e, 'sys1')}
              onDragOver={(e) => e.preventDefault()}
            >
              <RiFileSearchLine className="size-6 text-gray-400" />
              <span className="text-xs font-sans truncate px-2 w-full text-center">
                {files.sys1 ? files.sys1.name : 'Drop SYS1 Excel'}
              </span>
            </div>
            <input
              ref={sys1InputRef}
              hidden
              type="file"
              accept=".xlsx,.xlsm"
              onChange={(event) => handleFileSelect(event, 'sys1')}
            />
          </fieldset>

          <fieldset className="p-4 border-2 border-sunken">
            <legend className="px-2 font-bold text-sm">Reference PDF/DOCX</legend>
            <div
              className="h-20 border-2 border-dashed flex flex-col items-center justify-center gap-1 cursor-pointer bg-gray-50 border-gray-400"
              onClick={() => specInputRef.current?.click()}
              onDrop={(e) => handleFileDrop(e, 'spec')}
              onDragOver={(e) => e.preventDefault()}
            >
              <RiFileLine className="size-6 text-gray-400" />
              <span className="text-xs font-sans truncate px-2 w-full text-center">
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
          <div className="status-bar-field p-2 bg-gray-100 text-sm font-sans flex items-center gap-2">
            <span className="text-green-700 font-bold">[READY]</span>
            Workbook staged. Parse the job to populate the shared desktop state.
          </div>
        )}
      </div>

      <div className="flex justify-end pt-4 border-t border-gray-400">
        <button
          className="flex items-center gap-2"
          disabled={!files.tc || isParsing}
          onClick={() => void handleNext()}
        >
          {isParsing ? 'Parsing...' : 'Parse & Next'} <RiArrowRightLine className="size-4" />
        </button>
      </div>
    </div>
  );
};

export default UploadModule;
