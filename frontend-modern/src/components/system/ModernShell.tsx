'use client';

import React, { useEffect } from 'react';
import {
  RiBookOpenLine,
  RiDownload2Line,
  RiFileList3Line,
  RiFlashlightLine,
  RiFlowChart,
  RiFolderUploadLine,
  RiPlayCircleLine,
  RiSettings3Line,
  RiShieldCheckLine,
} from '@remixicon/react';
import { useJobStore } from '../../store/useJobStore';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import UploadModule from '../modules/upload/UploadModule';
import ConfigureModule from '../modules/configure/ConfigureModule';
import GenerateModule from '../modules/generate/GenerateModule';
import ModernReviewModule from '../modules/review/ModernReviewModule';
import ExportModule from '../modules/export/ExportModule';
import QuickGenerateModule from '../modules/quickGenerate/QuickGenerateModule';
import DiagramsModule from '../modules/diagrams/DiagramsModule';
import RulesModule from '../modules/rules/RulesModule';
import AuditModule from '../modules/review/AuditModule';
import ModernSessionControls from './ModernSessionControls';

type NavItem = {
  id: WindowID;
  label: string;
  description: string;
  group: 'flow' | 'tools';
  icon: React.ReactNode;
};

const NAV_ITEMS: NavItem[] = [
  { id: 'upload', label: 'Upload', description: 'Import workbook', group: 'flow', icon: <RiFolderUploadLine /> },
  { id: 'configure', label: 'Configure', description: 'Group and match', group: 'flow', icon: <RiSettings3Line /> },
  { id: 'generate', label: 'Generate', description: 'Run AI generation', group: 'flow', icon: <RiPlayCircleLine /> },
  { id: 'review', label: 'Review', description: 'Inspect and approve', group: 'flow', icon: <RiFileList3Line /> },
  { id: 'export', label: 'Export', description: 'Write workbook', group: 'flow', icon: <RiDownload2Line /> },
  { id: 'quickGenerate', label: 'Quick TC', description: 'Single requirement', group: 'tools', icon: <RiFlashlightLine /> },
  { id: 'audit', label: 'Audit', description: 'SWE.6 review', group: 'tools', icon: <RiShieldCheckLine /> },
  { id: 'rules', label: 'Rules', description: 'Writing guidance', group: 'tools', icon: <RiBookOpenLine /> },
  { id: 'diagrams', label: 'Diagrams', description: 'Workflow reference', group: 'tools', icon: <RiFlowChart /> },
];

const CONTENT_MAP: Record<WindowID, React.ReactNode> = {
  upload: <UploadModule />,
  configure: <ConfigureModule />,
  generate: <GenerateModule />,
  review: <ModernReviewModule />,
  export: <ExportModule />,
  quickGenerate: <QuickGenerateModule />,
  diagrams: <DiagramsModule />,
  rules: <RulesModule />,
  audit: <AuditModule />,
};

const TITLES: Record<WindowID, string> = {
  upload: 'Upload Files',
  configure: 'Configure',
  generate: 'Generate',
  review: 'Review Results',
  export: 'Export',
  quickGenerate: 'Quick TC Generator',
  diagrams: 'Workflow Diagrams',
  rules: 'TC Writing Rules',
  audit: 'ASPICE SWE.6 Audit',
};

function formatCost(value: number): string {
  return `$${value.toFixed(4)}`;
}

export default function ModernShell() {
  const { focusedWindowId, openWindow } = useWindowStore();
  const { jobMetadata, tcRows, stats, config, isProcessing, isRegenerating } = useJobStore();
  const activeId = focusedWindowId ?? 'upload';
  const activeItem = NAV_ITEMS.find((item) => item.id === activeId) ?? NAV_ITEMS[0];

  useEffect(() => {
    openWindow('upload', TITLES.upload);
  }, [openWindow]);

  const accepted = tcRows.filter((row) => row.status === 'accepted').length;
  const flagged = tcRows.filter((row) => row.status === 'flagged').length;
  const pending = tcRows.filter((row) => row.status === 'pending' || row.status === 'reviewing').length;
  const flowItems = NAV_ITEMS.filter((item) => item.group === 'flow');
  const toolItems = NAV_ITEMS.filter((item) => item.group === 'tools');

  return (
    <div className="modern-shell">
      <aside className="modern-sidebar" aria-label="Modules">
        <div className="modern-brand">
          <div className="modern-brand-mark">TC</div>
          <div>
            <div className="modern-brand-title">TC Generator</div>
          </div>
        </div>

        <div className="modern-workflow-label">Workflow</div>
        <nav className="modern-nav modern-nav-flow" aria-label="Primary workflow">
          {flowItems.map((item, index) => (
            <button
              key={item.id}
              className="modern-nav-item"
              data-active={item.id === activeId}
              data-step={String(index + 1).padStart(2, '0')}
              onClick={() => openWindow(item.id, TITLES[item.id])}
              type="button"
            >
              <span className="modern-nav-node" aria-hidden="true">
                {String(index + 1).padStart(2, '0')}
              </span>
              <span className="modern-nav-copy">
                <span className="modern-nav-label">{item.label}</span>
                <span className="modern-nav-description">{item.description}</span>
              </span>
              <span className="modern-nav-icon">{item.icon}</span>
            </button>
          ))}
        </nav>

        <div className="modern-tools-panel">
          <div className="modern-nav-section">Tools</div>
          <nav className="modern-nav modern-nav-tools" aria-label="Supporting tools">
            {toolItems.map((item) => (
              <button
                key={item.id}
                className="modern-nav-item"
                data-active={item.id === activeId}
                onClick={() => openWindow(item.id, TITLES[item.id])}
                type="button"
              >
                <span className="modern-nav-icon">{item.icon}</span>
                <span className="modern-nav-copy">
                  <span className="modern-nav-label">{item.label}</span>
                  <span className="modern-nav-description">{item.description}</span>
                </span>
              </button>
            ))}
          </nav>
        </div>
      </aside>

      <main className="modern-main">
        <header className="modern-topbar">
          <div className="modern-topbar-primary">
            <div>
              <div className="modern-kicker">Active Module</div>
              <h1>{activeItem.label}</h1>
            </div>
            <ModernSessionControls />
          </div>
          <div className="modern-status-strip" aria-label="Workspace status">
            <span className="modern-status-job" title={jobMetadata?.jobId ?? 'No job loaded'}>
              {jobMetadata?.jobId ?? 'No job'}
            </span>
            <span className="modern-status-metrics">
              <span>
                <strong>{tcRows.length}</strong>
                <small>Rows</small>
              </span>
              <span>
                <strong>{accepted}</strong>
                <small>Accepted</small>
              </span>
              <span>
                <strong>{flagged}</strong>
                <small>Flagged</small>
              </span>
              <span>
                <strong>{pending}</strong>
                <small>Pending</small>
              </span>
            </span>
            <span className="modern-status-runtime">
              <span>{config.model}</span>
              <strong>{formatCost(stats.cost)}</strong>
            </span>
            {(isProcessing || isRegenerating) && <span className="modern-status-running">Running</span>}
          </div>
        </header>

        <section className="modern-module-panel" aria-label={activeItem.label}>
          {CONTENT_MAP[activeId]}
        </section>
      </main>
    </div>
  );
}
