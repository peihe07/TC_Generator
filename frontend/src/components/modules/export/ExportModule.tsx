'use client';

import React, { useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { exportJob } from '../../../services/jobAdapter';
import {
  RiDownload2Line,
  RiFileExcel2Fill,
  RiCheckDoubleLine,
  RiSettings4Line,
  RiArrowLeftLine
} from '@remixicon/react';

const ExportModule: React.FC = () => {
  const { tcRows, jobMetadata, appendLog, resetJob, config } = useJobStore();
  const { openWindow } = useWindowStore();
  const [isExporting, setIsExporting] = useState(false);
  const [exportComplete, setExportComplete] = useState(false);
  const [scope, setExportScope] = useState<'all' | 'accepted'>('accepted');
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);

  const acceptedCount = tcRows.filter((r) => r.status === 'accepted').length;
  const selectedColumns = [
    'TC ID',
    'Test Set',
    ...(config.targetColumns.includes('preConditions') ? ['Pre-Conditions'] : []),
    ...(config.targetColumns.includes('steps') ? ['Test Procedure'] : []),
    ...(config.targetColumns.includes('expectedResults') ? ['Expected Result'] : []),
    'Priority',
  ];

  const handleExport = async () => {
    setIsExporting(true);
    try {
      const result = await exportJob({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
        scope,
        outputMode: 'new-file',
        includeFrameworkSheet: true,
        selectedColumns,
      });

      setDownloadUrl(result.downloadUrl);
      setExportComplete(true);
      appendLog(
        createJobLog(
          result.simulated ? 'warn' : 'success',
          result.simulated
            ? `Prepared local export preview for ${result.exportedRows} row(s).`
            : `Export ready: ${result.fileName} (${result.exportedRows} row(s)).`,
        ),
      );
    } catch (error) {
      appendLog(
        createJobLog(
          'error',
          error instanceof Error ? error.message : 'Export failed.',
        ),
      );
    } finally {
      setIsExporting(false);
    }
  };

  return (
    <div className="flex flex-col h-full gap-4">
      {!exportComplete ? (
        <>
          <div className="flex-1 flex flex-col gap-4">
            <fieldset className="p-4">
              <legend className="font-bold">Export Scope</legend>
              <div className="flex flex-col gap-2">
                <div className="field-row">
                  <input
                    type="radio"
                    id="scope-all"
                    name="scope"
                    checked={scope === 'all'}
                    onChange={() => setExportScope('all')}
                  />
                  <label htmlFor="scope-all">All Generated Cases ({tcRows.length})</label>
                </div>
                <div className="field-row">
                  <input
                    type="radio"
                    id="scope-accepted"
                    name="scope"
                    checked={scope === 'accepted'}
                    onChange={() => setExportScope('accepted')}
                  />
                  <label htmlFor="scope-accepted">Accepted Only ({acceptedCount})</label>
                </div>
              </div>
            </fieldset>

            <fieldset className="p-4">
              <legend className="font-bold">Output Settings</legend>
              <div className="grid grid-cols-2 gap-4">
                <div className="flex flex-col gap-2">
                  <div className="field-row">
                    <input type="checkbox" id="inc-steps" defaultChecked />
                    <label htmlFor="inc-steps">Include Steps</label>
                  </div>
                  <div className="field-row">
                    <input type="checkbox" id="inc-expected" defaultChecked />
                    <label htmlFor="inc-expected">Include Expected</label>
                  </div>
                </div>
                <div className="flex flex-col gap-2">
                  <div className="field-row">
                    <input type="checkbox" id="inc-meta" defaultChecked />
                    <label htmlFor="inc-meta">Include Metadata</label>
                  </div>
                  <div className="field-row">
                    <input type="checkbox" id="inc-framework" defaultChecked />
                    <label htmlFor="inc-framework">Update Framework Sheet</label>
                  </div>
                </div>
              </div>
            </fieldset>

            <div className="status-bar-field p-3 text-xs leading-relaxed border-2 border-sunken">
              <RiSettings4Line className="size-4 inline mr-2 mb-1" />
              Final file will be named: <span className="font-bold font-mono">{jobMetadata?.projectName || 'results'}_generated.xlsx</span>
            </div>
          </div>

          <div className="flex justify-between items-center pt-4 border-t border-gray-400">
            <button className="flex items-center gap-1" onClick={() => openWindow('review', 'Review Results')}>
              <RiArrowLeftLine className="size-4" /> Back to Review
            </button>
            <button
              className={`flex items-center gap-2 font-bold default min-w-[120px] justify-center ${isExporting ? 'bg-gray-200' : ''}`}
              disabled={isExporting}
              onClick={() => void handleExport()}
            >
              {isExporting ? (
                <span className="animate-pulse italic">Exporting...</span>
              ) : (
                <>Export to Excel <RiFileExcel2Fill className="size-4 text-green-700" /></>
              )}
            </button>
          </div>
        </>
      ) : (
        <div className="flex-1 flex flex-col items-center justify-center gap-6 py-8 text-center">
          <div
            style={{
              width: 64,
              height: 64,
              background: '#c0c0c0',
              border: '2px solid',
              borderColor: '#ffffff #808080 #808080 #ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <RiCheckDoubleLine size={36} style={{ color: '#006400' }} />
          </div>
          <div>
            <h2 className="text-xl font-bold mb-2">Export Successful!</h2>
            <p className="text-xs text-gray-600">Your test cases have been processed and are ready for download.</p>
          </div>

          <div className="flex flex-col gap-3 w-64">
            <a
              href={downloadUrl ?? '#'}
              className="button default py-3 flex items-center justify-center gap-2 no-underline text-black"
              onClick={(e) => {
                if (!downloadUrl) {
                  e.preventDefault();
                }
              }}
            >
              <RiDownload2Line className="size-5" /> Download File
            </a>
            <button
              className="py-2"
              onClick={() => {
                setExportComplete(false);
                setDownloadUrl(null);
                resetJob();
                openWindow('upload', 'Upload Files');
              }}
            >
              Start New Job
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExportModule;
