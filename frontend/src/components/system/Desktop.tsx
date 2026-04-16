'use client';

import React, { useEffect, useState } from 'react';
import { useWindowStore } from '../../store/useWindowStore';
import WindowManager from './WindowManager';
import Taskbar from './Taskbar';
import {
  RiFolderUploadLine,
  RiSettings3Line,
  RiPlayCircleLine,
  RiFileList3Line,
  RiDownload2Line,
  RiFlashlightLine,
} from '@remixicon/react';
import { WindowID } from '../../store/useWindowStore';

const DESKTOP_ICONS: { id: WindowID; label: string; icon: React.ReactNode }[] = [
  { id: 'upload',        label: 'Upload',        icon: <RiFolderUploadLine className="size-12 text-white group-active:opacity-50" /> },
  { id: 'configure',     label: 'Configure',     icon: <RiSettings3Line    className="size-12 text-white group-active:opacity-50" /> },
  { id: 'generate',      label: 'Generate',      icon: <RiPlayCircleLine   className="size-12 text-white group-active:opacity-50" /> },
  { id: 'review',        label: 'Review',        icon: <RiFileList3Line    className="size-12 text-white group-active:opacity-50" /> },
  { id: 'export',        label: 'Export',        icon: <RiDownload2Line    className="size-12 text-white group-active:opacity-50" /> },
  { id: 'quickGenerate', label: 'Quick TC',      icon: <RiFlashlightLine   className="size-12 text-yellow-300 group-active:opacity-50" /> },
];

const WINDOW_TITLES: Record<WindowID, string> = {
  upload:        'TC Generator - Upload Files',
  configure:     'TC Generator - Configure',
  generate:      'TC Generator - Generate',
  review:        'TC Generator - Review',
  export:        'TC Generator - Export',
  quickGenerate: 'Quick TC Generator',
};

const Desktop: React.FC = () => {
  const { openWindow } = useWindowStore();
  const [hasMounted, setHasMounted] = useState(false);

  useEffect(() => {
    setHasMounted(true);
  }, []);

  if (!hasMounted) return null;

  return (
    <div className="desktop-bg relative w-screen h-screen overflow-hidden select-none">
      {/* Desktop Icons */}
      <div className="grid grid-cols-1 gap-4 p-4 w-fit relative z-0">
        {DESKTOP_ICONS.map(({ id, label, icon }) => (
          <div
            key={id}
            className="flex flex-col items-center justify-center gap-1 w-24 cursor-pointer group p-2 hover:bg-white/10 rounded-sm"
            onDoubleClick={() => openWindow(id, WINDOW_TITLES[id])}
          >
            <div className="p-1 group-active:bg-blue-900 rounded-sm">
              {icon}
            </div>
            <span className="text-white text-sm bg-black/40 px-2 py-0.5 text-center font-sans shadow-sm">
              {label}
            </span>
          </div>
        ))}
      </div>

      {/* Actual Windows */}
      <WindowManager />

      {/* Taskbar */}
      <Taskbar />
    </div>
  );
};

export default Desktop;
