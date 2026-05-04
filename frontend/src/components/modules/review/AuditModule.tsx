'use client';

import React, { useCallback, useMemo, useState } from 'react';
import {
  RiUpload2Line,
  RiPlayLine,
  RiDownload2Line,
  RiAlertLine,
} from '@remixicon/react';
import { Button } from '../../ui';

// ASPICE SWE.6 Audit module — runs the review pipeline against an uploaded
// workbook and renders the §9-shaped findings report. Self-contained on
// purpose: not wired into the Win95 job store, since audit is a one-shot
// synchronous request rather than a streaming generation job.

type Severity = 'Critical' | 'Major' | 'Minor' | 'Info';

interface PerReqFinding {
  req_id: string;
  tier: number;
  rule_ref: string;
  severity: Severity;
  scope_tcs: string[];
  issue: string;
  evidence_req_spec?: string;
  suggestion_note?: string;
}

interface PerTcFinding {
  tier: number;
  field: string;
  step_index?: number | null;
  rule_ref: string;
  severity: Severity;
  issue: string;
  evidence?: string;
  evidence_req_spec?: string;
  original?: string;
  revised?: string;
  suggestion_note?: string;
}

interface PerTcEntry {
  tc_id: string;
  row: number;
  overall_verdict: 'pass' | 'pass_with_issues' | 'fail';
  findings: PerTcFinding[];
}

interface AuditReport {
  batch_meta: {
    source_file: string;
    sheet: string;
    total_tcs: number;
    total_req_groups: number;
    reviewed_at: string;
  };
  per_req_findings: PerReqFinding[];
  per_tc_findings: PerTcEntry[];
  batch_summary: {
    verdict_counts: { pass: number; pass_with_issues: number; fail: number };
    tier_summary: {
      tier1: { req_groups_total: number; req_groups_with_critical: number; req_groups_skipped: number };
      tier2: { tcs_with_critical: number };
      tier3: { tcs_with_findings: number };
    };
    reasoning: string;
  };
}

const SEVERITY_RANK: Record<Severity, number> = {
  Info: 0,
  Minor: 1,
  Major: 2,
  Critical: 3,
};

const SEVERITY_COLOR: Record<Severity, string> = {
  Critical: '#c0392b',
  Major: '#d68910',
  Minor: '#7d6608',
  Info: '#566573',
};

type Tab = 'per_req' | 'per_tc';

const AuditModule: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [dryRun, setDryRun] = useState(true);
  const [running, setRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [report, setReport] = useState<AuditReport | null>(null);
  const [tab, setTab] = useState<Tab>('per_req');
  const [minSeverity, setMinSeverity] = useState<Severity>('Info');
  const fileInputRef = React.useRef<HTMLInputElement>(null);

  const handleFile = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    const next = event.target.files?.[0] ?? null;
    setFile(next);
    setError(null);
    setReport(null);
  }, []);

  const triggerFilePicker = useCallback(() => {
    fileInputRef.current?.click();
  }, []);

  const runAudit = useCallback(async () => {
    if (!file) return;
    setRunning(true);
    setError(null);
    setReport(null);
    try {
      const form = new FormData();
      form.append('workbook', file);
      form.append('dry_run', dryRun ? 'true' : 'false');
      const resp = await fetch('/api/audit', { method: 'POST', body: form });
      if (!resp.ok) {
        const text = await resp.text();
        throw new Error(text || `Audit failed (${resp.status})`);
      }
      const data = (await resp.json()) as AuditReport;
      setReport(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Audit failed.');
    } finally {
      setRunning(false);
    }
  }, [file, dryRun]);

  const downloadJson = useCallback(() => {
    if (!report) return;
    const blob = new Blob([JSON.stringify(report, null, 2)], {
      type: 'application/json',
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${report.batch_meta.source_file.replace(/\.[^.]+$/, '')}_findings.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }, [report]);

  const filteredPerReq = useMemo<PerReqFinding[]>(() => {
    if (!report) return [];
    return report.per_req_findings.filter(
      (f) => SEVERITY_RANK[f.severity] >= SEVERITY_RANK[minSeverity],
    );
  }, [report, minSeverity]);

  const filteredPerTc = useMemo<PerTcEntry[]>(() => {
    if (!report) return [];
    return report.per_tc_findings
      .map((entry) => ({
        ...entry,
        findings: entry.findings.filter(
          (f) => SEVERITY_RANK[f.severity] >= SEVERITY_RANK[minSeverity],
        ),
      }))
      .filter((entry) => entry.findings.length > 0);
  }, [report, minSeverity]);

  return (
    <div style={{ padding: 16, display: 'flex', flexDirection: 'column', gap: 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, flexWrap: 'wrap' }}>
        <input
          ref={fileInputRef}
          type="file"
          accept=".xlsx,.xlsm"
          onChange={handleFile}
          disabled={running}
          style={{ display: 'none' }}
        />
        <Button onClick={triggerFilePicker} disabled={running}>
          <RiUpload2Line size={16} /> 選擇 .xlsx
        </Button>
        <span
          style={{
            fontSize: 13,
            color: file ? '#1a5f1a' : '#888',
            fontStyle: file ? 'normal' : 'italic',
          }}
        >
          {file ? `已選：${file.name}（${(file.size / 1024).toFixed(0)} KB）` : '尚未選擇檔案'}
        </span>
        <label style={{ marginLeft: 12, fontSize: 13 }}>
          <input
            type="checkbox"
            checked={dryRun}
            onChange={(e) => setDryRun(e.target.checked)}
            disabled={running}
          />{' '}
          Dry run（僅 regex pre-pass，不呼叫 LLM）
        </label>
        <Button
          onClick={runAudit}
          disabled={!file || running}
          style={{
            marginLeft: 'auto',
            ...(!file || running ? { opacity: 0.5, cursor: 'not-allowed' } : {}),
          }}
          title={!file ? '請先選擇 .xlsx 檔' : running ? '審核進行中' : '開始審核'}
        >
          <RiPlayLine size={16} /> {running ? '審核中…' : '開始審核'}
        </Button>
      </div>

      {error && (
        <div style={{ color: '#c0392b', display: 'flex', gap: 8, alignItems: 'center' }}>
          <RiAlertLine size={18} /> {error}
        </div>
      )}

      {report && (
        <>
          <SummaryPanel report={report} />
          <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
            <TabButton active={tab === 'per_req'} onClick={() => setTab('per_req')}>
              Per Requirement ({report.per_req_findings.length})
            </TabButton>
            <TabButton active={tab === 'per_tc'} onClick={() => setTab('per_tc')}>
              Per TC ({report.per_tc_findings.length})
            </TabButton>
            <label style={{ marginLeft: 'auto' }}>
              最低嚴重度：
              <select
                value={minSeverity}
                onChange={(e) => setMinSeverity(e.target.value as Severity)}
              >
                <option value="Info">Info+</option>
                <option value="Minor">Minor+</option>
                <option value="Major">Major+</option>
                <option value="Critical">Critical only</option>
              </select>
            </label>
            <Button onClick={downloadJson}>
              <RiDownload2Line size={16} /> 下載 findings.json
            </Button>
          </div>

          {tab === 'per_req' ? (
            <PerReqTable findings={filteredPerReq} />
          ) : (
            <PerTcTable entries={filteredPerTc} />
          )}
        </>
      )}
    </div>
  );
};

const SummaryPanel: React.FC<{ report: AuditReport }> = ({ report }) => {
  const { batch_meta: meta, batch_summary: summary } = report;
  return (
    <div style={{ border: '1px solid #888', padding: 12 }}>
      <div style={{ fontWeight: 600, marginBottom: 8 }}>
        {meta.source_file} · {meta.total_tcs} TCs · {meta.total_req_groups} Req groups
      </div>
      <div style={{ display: 'flex', gap: 24, marginBottom: 8 }}>
        <span>Pass: {summary.verdict_counts.pass}</span>
        <span>With issues: {summary.verdict_counts.pass_with_issues}</span>
        <span style={{ color: '#c0392b' }}>Fail: {summary.verdict_counts.fail}</span>
      </div>
      <div style={{ fontSize: 13, color: '#444' }}>{summary.reasoning}</div>
    </div>
  );
};

const TabButton: React.FC<React.PropsWithChildren<{ active: boolean; onClick: () => void }>> = ({
  active,
  onClick,
  children,
}) => (
  <button
    onClick={onClick}
    style={{
      padding: '6px 12px',
      border: '1px solid #888',
      background: active ? '#cdd0d4' : '#f4f4f4',
      fontWeight: active ? 600 : 400,
      cursor: 'pointer',
    }}
  >
    {children}
  </button>
);

const PerReqTable: React.FC<{ findings: PerReqFinding[] }> = ({ findings }) => {
  if (findings.length === 0) {
    return <div style={{ padding: 12, color: '#666' }}>沒有 Tier 1 findings。</div>;
  }
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
      <thead>
        <tr style={{ background: '#e8e8e8' }}>
          <Th>Req ID</Th>
          <Th>Rule</Th>
          <Th>Severity</Th>
          <Th>Issue</Th>
          <Th>Affected TCs</Th>
        </tr>
      </thead>
      <tbody>
        {findings.map((f, i) => (
          <tr key={`${f.req_id}-${f.rule_ref}-${i}`}>
            <Td>{f.req_id}</Td>
            <Td>{f.rule_ref}</Td>
            <Td>
              <SeverityBadge severity={f.severity} />
            </Td>
            <Td>{f.issue}</Td>
            <Td>{f.scope_tcs.join(', ')}</Td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

const PerTcTable: React.FC<{ entries: PerTcEntry[] }> = ({ entries }) => {
  if (entries.length === 0) {
    return <div style={{ padding: 12, color: '#666' }}>沒有 per-TC findings。</div>;
  }
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
      <thead>
        <tr style={{ background: '#e8e8e8' }}>
          <Th>Row</Th>
          <Th>TC ID</Th>
          <Th>Verdict</Th>
          <Th>Tier</Th>
          <Th>Rule</Th>
          <Th>Severity</Th>
          <Th>Field</Th>
          <Th>Issue</Th>
        </tr>
      </thead>
      <tbody>
        {entries.flatMap((entry) =>
          entry.findings.map((f, i) => (
            <tr key={`${entry.tc_id}-${f.rule_ref}-${i}`}>
              <Td>{entry.row}</Td>
              <Td>{entry.tc_id}</Td>
              <Td>{entry.overall_verdict}</Td>
              <Td>{f.tier}</Td>
              <Td>{f.rule_ref}</Td>
              <Td>
                <SeverityBadge severity={f.severity} />
              </Td>
              <Td>{f.field}</Td>
              <Td title={f.evidence ?? ''}>{f.issue}</Td>
            </tr>
          )),
        )}
      </tbody>
    </table>
  );
};

const Th: React.FC<React.PropsWithChildren> = ({ children }) => (
  <th style={{ textAlign: 'left', padding: '6px 8px', borderBottom: '1px solid #aaa' }}>{children}</th>
);

const Td: React.FC<React.PropsWithChildren & { title?: string }> = ({ children, title }) => (
  <td title={title} style={{ padding: '6px 8px', borderBottom: '1px solid #ddd', verticalAlign: 'top' }}>
    {children}
  </td>
);

const SeverityBadge: React.FC<{ severity: Severity }> = ({ severity }) => (
  <span
    style={{
      display: 'inline-block',
      padding: '2px 6px',
      background: SEVERITY_COLOR[severity],
      color: '#fff',
      fontSize: 11,
      fontWeight: 600,
    }}
  >
    {severity}
  </span>
);

export default AuditModule;
