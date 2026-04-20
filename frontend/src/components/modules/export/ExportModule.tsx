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
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import { Button, Checkbox, Radio } from '../../ui';

const ExportModule: React.FC = () => {
  const { tcRows, jobMetadata, appendLog, resetJob, config } = useJobStore();
  const { openWindow } = useWindowStore();
  const [isExporting, setIsExporting] = useState(false);
  const [exportComplete, setExportComplete] = useState(false);
  const [scope, setExportScope] = useState<'all' | 'accepted'>('all');
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);

  const acceptedCount = tcRows.filter((r) => r.status === 'accepted').length;
  const selectedColumns = [
    'TC ID',
    'Test Set',
    ...(config.targetColumns.includes('preConditions') ? ['Pre-Conditions'] : []),
    ...(config.targetColumns.includes('inputTestData') ? ['Input Test Data'] : []),
    ...(config.targetColumns.includes('steps') ? ['Test Procedure'] : []),
    ...(config.targetColumns.includes('expectedResults') ? ['Expected Result'] : []),
    'Priority',
  ];

  const handleExport = async () => {
    if (scope === 'accepted' && acceptedCount === 0) {
      appendLog(createJobLog('warn', 'No accepted rows available for export. Switch scope to All Generated Cases or accept rows first.'));
      return;
    }
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
      <div className="flex justify-end">
        <HelpFromAgentButton
          contextPrompt={`[context: 目前在 Export Module, job=${jobMetadata?.jobId ?? '未開啟 job'}]\n`}
          title="求助 AI"
        />
      </div>
      {!exportComplete ? (
        <>
          <div className="flex-1 flex flex-col gap-4">
            <fieldset className="p-4">
              <legend>Export Scope</legend>
              <div className="flex flex-col gap-2">
                <Radio
                  id="scope-all"
                  name="scope"
                  label={`All Generated Cases (${tcRows.length})`}
                  checked={scope === 'all'}
                  onChange={() => setExportScope('all')}
                />
                <Radio
                  id="scope-accepted"
                  name="scope"
                  label={`Accepted Only (${acceptedCount})`}
                  checked={scope === 'accepted'}
                  onChange={() => setExportScope('accepted')}
                />
              </div>
            </fieldset>

            <fieldset className="p-4">
              <legend>Output Settings</legend>
              <div className="grid grid-cols-2 gap-4">
                <div className="flex flex-col gap-2">
                  <Checkbox id="inc-steps" label="Include Steps" defaultChecked />
                  <Checkbox id="inc-expected" label="Include Expected" defaultChecked />
                </div>
                <div className="flex flex-col gap-2">
                  <Checkbox id="inc-meta" label="Include Metadata" defaultChecked />
                  <Checkbox
                    id="inc-framework"
                    label="Update Framework Sheet"
                    defaultChecked
                  />
                </div>
              </div>
            </fieldset>

            <div className="status-bar-field p-3 text-xs leading-relaxed border-sunken">
              <RiSettings4Line className="size-4 inline mr-2 mb-1" />
              Final file will be named: <span className="font-bold font-mono">{jobMetadata?.projectName || 'results'}_generated.xlsx</span>
            </div>
          </div>

          <div
            className="flex justify-between items-center pt-4"
            style={{ borderTop: '1px solid var(--win95-gray-mid)' }}
          >
            <Button className="flex items-center gap-1" onClick={() => openWindow('review', 'Review Results')}>
              <RiArrowLeftLine className="size-4" /> Back to Review
            </Button>
            <Button
              className="flex items-center gap-2 default min-w-[120px] justify-center"
              disabled={isExporting}
              onClick={() => void handleExport()}
            >
              {isExporting ? (
                <span className="italic" style={{ animation: 'agent-pulse 1s ease-in-out infinite' }}>Exporting...</span>
              ) : (
                <>
                  Export to Excel{' '}
                  <RiFileExcel2Fill
                    className="size-4"
                    style={{ color: 'var(--status-accept-dark)' }}
                  />
                </>
              )}
            </Button>
          </div>
        </>
      ) : (
        <div className="flex-1 flex flex-col items-center justify-center gap-6 py-8 text-center">
          <div
            style={{
              width: 64,
              height: 64,
              background: 'var(--win95-gray)',
              border: '2px solid',
              borderColor: 'var(--win95-white) var(--win95-gray-mid) var(--win95-gray-mid) var(--win95-white)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <RiCheckDoubleLine size={36} style={{ color: 'var(--status-accept-dark)' }} />
          </div>
          <div>
            <h2 className="type-h1 mb-2">Export Successful!</h2>
            <p className="text-xs" style={{ color: 'var(--text-muted)' }}>
              Your test cases have been processed and are ready for download.
            </p>
          </div>

          <div className="flex flex-col gap-3 w-64">
            <a
              href={downloadUrl ?? '#'}
              className="button default py-3 flex items-center justify-center gap-2 no-underline"
              onClick={(e) => {
                if (!downloadUrl) {
                  e.preventDefault();
                }
              }}
            >
              <RiDownload2Line className="size-5" /> Download File
            </a>
            <Button
              className="py-2"
              onClick={() => {
                setExportComplete(false);
                setDownloadUrl(null);
                resetJob();
                openWindow('upload', 'Upload Files');
              }}
            >
              Start New Job
            </Button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExportModule;
