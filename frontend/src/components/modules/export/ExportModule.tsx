'use client';

import React, { useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { attachRawWorkbook, exportJob, fetchSourceStatus } from '../../../services/jobAdapter';
import {
  RiDownload2Line,
  RiFileExcel2Fill,
  RiCheckDoubleLine,
  RiSettings4Line,
  RiArrowLeftLine
} from '@remixicon/react';
import { Button, Checkbox, Radio, Win95Dialog } from '../../ui';

const ExportModule: React.FC = () => {
  const { tcRows, jobMetadata, appendLog, resetJob, config } = useJobStore();
  const { advanceWindow } = useWindowStore();
  const [isExporting, setIsExporting] = useState(false);
  const [exportComplete, setExportComplete] = useState(false);
  const [attachPrompt, setAttachPrompt] = useState<null | { reason: 'pre-check' | 'post-export' }>(null);
  const [attaching, setAttaching] = useState(false);
  const attachInputRef = useRef<HTMLInputElement>(null);
  const [scope, setExportScope] = useState<'all' | 'accepted'>('all');
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);
  const [includeSteps, setIncludeSteps] = useState(true);
  const [includeExpected, setIncludeExpected] = useState(true);
  const [includeMeta, setIncludeMeta] = useState(true);
  const [includeFrameworkSheet, setIncludeFrameworkSheet] = useState(true);

  const acceptedCount = tcRows.filter((r) => r.status === 'accepted').length;
  const selectedColumns = [
    'TC Title',
    ...(includeMeta ? ['TC ID', 'Test Set'] : []),
    ...(config.targetColumns.includes('preConditions') ? ['Pre-Conditions'] : []),
    ...(config.targetColumns.includes('inputTestData') ? ['Input Test Data'] : []),
    ...(includeSteps && config.targetColumns.includes('steps') ? ['Test Procedure'] : []),
    ...(includeExpected && config.targetColumns.includes('expectedResults') ? ['Expected Result'] : []),
    ...(includeMeta ? ['Priority', 'Design Method'] : []),
  ];

  const runExport = async () => {
    setIsExporting(true);
    try {
      const result = await exportJob({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
        scope,
        outputMode: 'new-file',
        includeFrameworkSheet,
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

      // Export 已成功但 backend 用了空白範本 → 事後補救：詢問是否要補原始 Excel
      if (result.fallbackTemplate && jobMetadata?.jobId) {
        setAttachPrompt({ reason: 'post-export' });
      }
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

  const handleExport = async () => {
    if (!jobMetadata?.jobId) {
      appendLog(createJobLog('warn', 'Export requires an active parsed job. Upload or merge into a current job first.'));
      return;
    }
    if (tcRows.length === 0) {
      appendLog(createJobLog('warn', 'No rows available for export.'));
      return;
    }
    if (scope === 'accepted' && acceptedCount === 0) {
      appendLog(createJobLog('warn', 'No accepted rows available for export. Switch scope to All Generated Cases or accept rows first.'));
      return;
    }

    // Pre-check：有 jobId 但 backend 已遺失 rawBytes 時，先 prompt 補上傳
    const jobId = jobMetadata?.jobId;
    if (jobId) {
      try {
        const status = await fetchSourceStatus(jobId);
        if (!status.hasSource) {
          setAttachPrompt({ reason: 'pre-check' });
          return;
        }
      } catch {
        // source-status 掛了不阻擋，繼續 export 走 fallback 流程
      }
    }

    await runExport();
  };

  const handleAttachClick = () => attachInputRef.current?.click();

  const handleAttachFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    e.target.value = '';
    if (!file) return;
    const jobId = jobMetadata?.jobId;
    if (!jobId) {
      window.alert('沒有作用中的 job，無法掛回原始 Excel。');
      return;
    }
    setAttaching(true);
    try {
      const result = await attachRawWorkbook(jobId, file);
      appendLog(
        createJobLog('success', `Attached original Excel: ${result.rawFileName} (${result.size} bytes).`),
      );
      const reason = attachPrompt?.reason;
      setAttachPrompt(null);
      // Pre-check 補上傳後直接跑 export；post-export 則讓使用者自己再按一次
      if (reason === 'pre-check') {
        await runExport();
      } else {
        window.alert('原始 Excel 已掛回 job，請再按一次 Export 重新產生含樣式的檔案。');
        setExportComplete(false);
        setDownloadUrl(null);
      }
    } catch (error) {
      appendLog(
        createJobLog(
          'error',
          error instanceof Error ? error.message : 'Attach original Excel failed.',
        ),
      );
    } finally {
      setAttaching(false);
    }
  };

  const handleAttachSkip = () => {
    const reason = attachPrompt?.reason;
    setAttachPrompt(null);
    if (reason === 'pre-check') {
      // 使用者選擇不補 → 直接用 blank template export
      void runExport();
    }
  };

  return (
    <div className="flex flex-col h-full gap-4">
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
                  <Checkbox
                    id="inc-steps"
                    label="Include Steps"
                    checked={includeSteps}
                    onChange={(event) => setIncludeSteps(event.target.checked)}
                  />
                  <Checkbox
                    id="inc-expected"
                    label="Include Expected"
                    checked={includeExpected}
                    onChange={(event) => setIncludeExpected(event.target.checked)}
                  />
                </div>
                <div className="flex flex-col gap-2">
                  <Checkbox
                    id="inc-meta"
                    label="Include Metadata"
                    checked={includeMeta}
                    onChange={(event) => setIncludeMeta(event.target.checked)}
                  />
                  <Checkbox
                    id="inc-framework"
                    label="Update Framework Sheet"
                    checked={includeFrameworkSheet}
                    onChange={(event) => setIncludeFrameworkSheet(event.target.checked)}
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
            <Button className="flex items-center gap-1" onClick={() => advanceWindow('export', 'review', 'Review Results')}>
              <RiArrowLeftLine className="size-4" /> Back to Review
            </Button>
            <Button
              className="flex items-center gap-2 default min-w-[120px] justify-center"
              disabled={isExporting || !jobMetadata?.jobId || tcRows.length === 0}
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
                advanceWindow('export', 'upload', 'Upload Files');
              }}
            >
              Start New Job
            </Button>
          </div>
        </div>
      )}

      <input
        ref={attachInputRef}
        type="file"
        accept=".xlsx,.xlsm"
        style={{ display: 'none' }}
        onChange={handleAttachFile}
      />
      <Win95Dialog
        open={Boolean(attachPrompt)}
        variant="warning"
        title="原始 Excel 遺失"
        message={
          <div className="flex flex-col gap-2 text-xs">
            <p>
              目前這個 job（<span className="font-mono">{jobMetadata?.jobId ?? ''}</span>
              ）在 backend 已經找不到原始 Excel。直接 export 會得到一份
              <b>空白範本</b>，不會保留原本的樣式、欄寬與其他分頁。
            </p>
            <p>請重新選擇當初 upload 的那份 .xlsx / .xlsm 掛回 job，再執行 export 即可還原樣式。</p>
            {attaching && <p className="italic">Uploading...</p>}
          </div>
        }
        actions={[
          {
            label: attaching ? 'Uploading…' : 'Attach original Excel…',
            onClick: handleAttachClick,
            variant: 'default',
          },
          {
            label: attachPrompt?.reason === 'pre-check' ? 'Skip (blank template)' : 'Close',
            onClick: handleAttachSkip,
            variant: 'cancel',
          },
        ]}
        onClose={handleAttachSkip}
      />
    </div>
  );
};

export default ExportModule;
