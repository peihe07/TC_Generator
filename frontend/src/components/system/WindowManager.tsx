'use client';

import React from 'react';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import AppWindow from './AppWindow';
import UploadModule from '../modules/upload/UploadModule';
import ConfigureModule from '../modules/configure/ConfigureModule';
import GenerateModule from '../modules/generate/GenerateModule';
import ReviewModule from '../modules/review/ReviewModule';
import ExportModule from '../modules/export/ExportModule';
import QuickGenerateModule from '../modules/quickGenerate/QuickGenerateModule';
import DiagramsModule from '../modules/diagrams/DiagramsModule';
import RulesModule from '../modules/rules/RulesModule';
import AuditModule from '../modules/review/AuditModule';
import {
  RiFolderUploadLine,
  RiSettings3Line,
  RiPlayCircleLine,
  RiFileList3Line,
  RiDownload2Line,
  RiFlashlightLine,
  RiFlowChart,
  RiBookOpenLine,
  RiShieldCheckLine,
} from '@remixicon/react';

const ICON_MAP: Record<WindowID, React.ReactNode> = {
  upload: <RiFolderUploadLine className="size-4" />,
  configure: <RiSettings3Line className="size-4" />,
  generate: <RiPlayCircleLine className="size-4" />,
  review: <RiFileList3Line className="size-4" />,
  export: <RiDownload2Line className="size-4" />,
  quickGenerate: <RiFlashlightLine className="size-4" />,
  diagrams: <RiFlowChart className="size-4" />,
  rules: <RiBookOpenLine className="size-4" />,
  audit: <RiShieldCheckLine className="size-4" />,
};

const CONTENT_MAP: Record<WindowID, React.ReactNode> = {
  upload: <UploadModule />,
  configure: <ConfigureModule />,
  generate: <GenerateModule />,
  review: <ReviewModule />,
  export: <ExportModule />,
  quickGenerate: <QuickGenerateModule />,
  diagrams: <DiagramsModule />,
  rules: <RulesModule />,
  audit: <AuditModule />,
};

const WindowManager: React.FC = () => {
  const { windows } = useWindowStore();
  const windowIds = Object.keys(windows) as WindowID[];

  return (
    <>
      {windowIds.map((id) => {
        const win = windows[id];
        if (!win.isOpen) return null;

        return (
          <AppWindow key={id} id={id} icon={ICON_MAP[id]}>
            {CONTENT_MAP[id]}
          </AppWindow>
        );
      })}
    </>
  );
};

export default WindowManager;
