'use client';

import React, { useEffect, useState } from 'react';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import { RiWindowsFill, RiTimeLine } from '@remixicon/react';

const Taskbar: React.FC = () => {
  const { windows, focusedWindowId, focusWindow } = useWindowStore();
  const [time, setTime] = useState('');

  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date();
      setTime(now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const openWindows = Object.values(windows).filter(win => win.isOpen);

  return (
    <footer className="fixed bottom-0 left-0 right-0 h-10 bg-gray-300 border-t-2 border-white shadow-[inset_1px_1px_0px_rgba(255,255,255,1)] flex items-center px-1 z-[9999]">
      {/* Start Button */}
      <button className="flex items-center gap-1 font-bold px-2 h-8 border-2 border-gray-400 active:border-inset">
        <RiWindowsFill className="size-4" />
        <span>Start</span>
      </button>

      <div className="w-[1px] h-6 bg-gray-500 mx-2 shadow-[1px_0_0_white]" />

      {/* Window Tabs */}
      <div className="flex-1 flex gap-1 overflow-x-auto">
        {openWindows.map((win) => (
          <button
            key={win.id}
            onClick={() => focusWindow(win.id as WindowID)}
            className={`flex items-center gap-1 px-2 h-8 min-w-[120px] max-w-[200px] border-2 text-sm text-left truncate ${
              focusedWindowId === win.id
                ? 'border-sunken bg-gray-200 font-bold'
                : 'border-white border-b-gray-800 border-r-gray-800'
            }`}
          >
            <span className="truncate">{win.title}</span>
          </button>
        ))}
      </div>

      <div className="w-[1px] h-6 bg-gray-500 mx-2 shadow-[1px_0_0_white]" />

      {/* Clock Area */}
      <div className="status-bar-field flex items-center gap-2 px-3 h-8 border-2 border-sunken text-sm">
        <RiTimeLine className="size-4" />
        <span>{time}</span>
      </div>
    </footer>
  );
};

export default Taskbar;
