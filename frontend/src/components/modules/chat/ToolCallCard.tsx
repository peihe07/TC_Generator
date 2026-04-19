'use client';

import React, { useState } from 'react';
import { RiArrowDownSLine, RiArrowRightSLine, RiCheckLine, RiErrorWarningLine, RiLoader4Line } from '@remixicon/react';
import type { UIToolPart } from '../../../services/agentEvents';
import { useWindowStore } from '../../../store/useWindowStore';
import { Button } from '../../ui';


interface Props {
  part: UIToolPart;
}

// Which tools have a corresponding GUI module to jump to
const TOOL_HANDOFF: Record<string, { windowId: string; label: string }> = {
  parse_workbook:  { windowId: 'upload',   label: 'Open in Upload' },
  group_tests:     { windowId: 'configure', label: 'Open in Configure' },
  match_spec:      { windowId: 'configure', label: 'Open in Configure' },
  generate_tc:     { windowId: 'review',    label: 'Open in Review' },
  validate_tc:     { windowId: 'review',    label: 'Open in Review' },
  write_excel:     { windowId: 'export',    label: 'Open in Export' },
};

export default function ToolCallCard({ part }: Props) {
  const [expanded, setExpanded] = useState(false);
  const openWindow = useWindowStore((s) => s.openWindow);
  const windowTitles: Record<string, string> = {
    upload: 'TC Generator - Upload Files',
    configure: 'TC Generator - Configure',
    review: 'TC Generator - Review',
    export: 'TC Generator - Export',
  };

  const handoff = TOOL_HANDOFF[part.tool];
  const handleHandoff = () => {
    if (!handoff) return;
    openWindow(
      handoff.windowId as Parameters<typeof openWindow>[0],
      windowTitles[handoff.windowId] ?? handoff.windowId,
    );
  };

  return (
    <div className="tool-card" data-status={part.status}>
      <div className="tool-card-header" onClick={() => setExpanded((v) => !v)}>
        <span className="tool-card-icon">
          {part.status === 'running' && <RiLoader4Line className="spin" size={14} />}
          {part.status === 'ok' && <RiCheckLine size={14} />}
          {part.status === 'error' && <RiErrorWarningLine size={14} />}
        </span>
        <span className="tool-card-name">{part.tool}</span>
        {part.durationMs !== undefined && (
          <span className="tool-card-duration">{part.durationMs}ms</span>
        )}
        <span className="tool-card-chevron">
          {expanded ? <RiArrowDownSLine size={14} /> : <RiArrowRightSLine size={14} />}
        </span>
      </div>

      {expanded && (
        <div className="tool-card-body">
          <div className="tool-card-section-label">Args</div>
          <pre className="tool-card-pre">{JSON.stringify(part.args, null, 2)}</pre>

          {part.status === 'ok' && part.result !== undefined && (
            <>
              <div className="tool-card-section-label">Result</div>
              <pre className="tool-card-pre">{renderResult(part.tool, part.result)}</pre>
            </>
          )}

          {part.status === 'error' && part.error && (
            <>
              <div className="tool-card-section-label">Error</div>
              <div className="tool-card-error">
                [{part.error.code}] {part.error.message}
              </div>
            </>
          )}
        </div>
      )}

      {part.status === 'ok' && handoff && (
        <div className="tool-card-footer">
          <Button className="btn-small" onClick={handleHandoff}>
            {handoff.label}
          </Button>
        </div>
      )}
    </div>
  );
}

function renderResult(tool: string, result: unknown): string {
  if (typeof result !== 'object' || result === null) return String(result);

  const r = result as Record<string, unknown>;

  switch (tool) {
    case 'parse_workbook':
      return `jobId: ${r.jobId}\nrows: ${r.rowCount}\nfile: ${(r.files as Record<string, unknown>)?.rawFileName}`;
    case 'list_jobs': {
      const jobs = (r.jobs as Array<Record<string, unknown>>) ?? [];
      return jobs.map((j) => `${j.jobId}  ${j.fileName}  ${j.status}  (${j.rowCount} rows)`).join('\n') || '(none)';
    }
    case 'estimate_cost':
      return `$${r.estCostUsd} — ${r.rowCount} rows @ ${r.model}`;
    case 'generate_tc':
      return `Generated ${(r.tcData as unknown[])?.length ?? 0} rows\nCost: $${r.cost}\nModel: ${r.model}`;
    case 'validate_tc': {
      const issues = (r.issues as Array<Record<string, unknown>>) ?? [];
      return issues.map((i) => `[${i.severity}] ${i.field}: ${i.message}`).join('\n') || 'No issues';
    }
    case 'get_job_validation':
      return `Total: ${r.total}  Pass: ${r.pass}  Warnings: ${r.warnings}`;
    case 'match_spec': {
      const s = r.summary as Record<string, unknown>;
      return `Exact: ${s.exact}  Fuzzy: ${s.fuzzy}  Unmatched: ${s.unmatched}`;
    }
    default:
      return JSON.stringify(result, null, 2);
  }
}
