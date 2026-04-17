'use client';

import React, { ReactNode, useRef } from 'react';
import Draggable from 'react-draggable';
import { ResizableBox } from 'react-resizable';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import 'react-resizable/css/styles.css';
import { TASKBAR_HEIGHT } from './layout';

interface AppWindowProps {
  id: WindowID;
  children: ReactNode;
  icon?: ReactNode;
}

const AppWindow: React.FC<AppWindowProps> = ({ id, children, icon }) => {
  const { windows, focusedWindowId, focusWindow, closeWindow, minimizeWindow, maximizeWindow, updatePosition, updateSize } = useWindowStore();
  const windowData = windows[id];
  const nodeRef = useRef(null);

  if (!windowData || !windowData.isOpen || windowData.isMinimized) return null;

  const isFocused = focusedWindowId === id;
  const isMaximized = windowData.isMaximized;

  const onDragStop = (_e: any, data: { x: number; y: number }) => {
    updatePosition(id, { x: data.x, y: data.y });
  };

  const onResizeStop = (_e: any, data: { size: { width: number; height: number } }) => {
    updateSize(id, { width: data.size.width, height: data.size.height });
  };

  const windowContent = (
    <div className={`window flex flex-col h-full ${isMaximized ? 'border-0' : ''}`}>
      {/* Title Bar */}
      <div className={`title-bar ${isFocused ? '' : 'inactive'}`} onDoubleClick={() => maximizeWindow(id)}>
        <div className="title-bar-text flex items-center gap-2">
          {icon && <span className="flex items-center">{icon}</span>}
          {windowData.title}
        </div>
        <div className="title-bar-controls">
          <button aria-label="Minimize" onClick={(e) => { e.stopPropagation(); minimizeWindow(id); }} />
          <button aria-label="Maximize" onClick={(e) => { e.stopPropagation(); maximizeWindow(id); }} />
          <button aria-label="Close"    onClick={(e) => { e.stopPropagation(); closeWindow(id); }} />
        </div>
      </div>

      {/* Window Body */}
      <div className="window-body flex-1 flex flex-col m-1 overflow-hidden">
        <div className={`flex-1 overflow-auto bg-white border-2 border-sunken shadow-inner ${(id === 'diagrams' || id === 'rules') ? 'p-0' : 'p-4'}`}>
          {children}
        </div>
      </div>
    </div>
  );

  if (isMaximized) {
    return (
      <div
        className="fixed top-0 left-0 right-0 bg-gray-300"
        style={{ zIndex: windowData.zIndex, bottom: TASKBAR_HEIGHT }}
        onClick={() => focusWindow(id)}
      >
        {windowContent}
      </div>
    );
  }

  return (
    <Draggable
      nodeRef={nodeRef}
      handle=".title-bar"
      defaultPosition={windowData.position}
      onStop={onDragStop}
      onStart={() => focusWindow(id)}
      bounds="parent"
    >
      <div
        ref={nodeRef}
        className="absolute top-0 left-0"
        style={{ zIndex: windowData.zIndex }}
        onClick={() => focusWindow(id)}
      >
        <ResizableBox
          width={windowData.size.width}
          height={windowData.size.height}
          minConstraints={[300, 200]}
          maxConstraints={[1600, 1200]}
          onResizeStop={onResizeStop}
          handle={<span className="react-resizable-handle" />}
        >
          {windowContent}
        </ResizableBox>
      </div>
    </Draggable>
  );
};

export default AppWindow;
