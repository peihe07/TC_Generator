'use client';

import React, { ReactNode, useEffect, useRef } from 'react';
import Draggable, { DraggableData, DraggableEvent } from 'react-draggable';
import { ResizableBox } from 'react-resizable';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import 'react-resizable/css/styles.css';
import { TASKBAR_HEIGHT } from './layout';

// react-resizable 的型別由本地 stub 宣告為 any；此處內聯最小可用型別。
type ResizeData = { size: { width: number; height: number } };

// 至少保留多少像素的標題列必須可見，避免視窗被拖到完全看不見
const MIN_VISIBLE = 80;
const TITLE_BAR_H = 28;

function clampPosition(
  pos: { x: number; y: number },
  size: { width: number; height: number },
): { x: number; y: number } {
  if (typeof window === 'undefined') return pos;
  const vw = window.innerWidth;
  const vh = window.innerHeight - TASKBAR_HEIGHT;
  const maxX = vw - MIN_VISIBLE;
  const maxY = vh - TITLE_BAR_H;
  const minX = -(size.width - MIN_VISIBLE);
  const minY = 0;
  return {
    x: Math.min(Math.max(pos.x, minX), maxX),
    y: Math.min(Math.max(pos.y, minY), maxY),
  };
}

interface AppWindowProps {
  id: WindowID;
  children: ReactNode;
  icon?: ReactNode;
}

const AppWindow: React.FC<AppWindowProps> = ({ id, children, icon }) => {
  const { windows, focusedWindowId, focusWindow, closeWindow, minimizeWindow, maximizeWindow, updatePosition, updateSize } = useWindowStore();
  const windowData = windows[id];
  const nodeRef = useRef(null);

  // 視窗開啟時與瀏覽器尺寸變動時，將位置夾回可視範圍（避免拖出畫面外無法拉回）
  useEffect(() => {
    if (!windowData || !windowData.isOpen || windowData.isMaximized) return;
    const ensureVisible = () => {
      const clamped = clampPosition(windowData.position, windowData.size);
      if (clamped.x !== windowData.position.x || clamped.y !== windowData.position.y) {
        updatePosition(id, clamped);
      }
    };
    ensureVisible();
    window.addEventListener('resize', ensureVisible);
    return () => window.removeEventListener('resize', ensureVisible);
  }, [id, windowData?.isOpen, windowData?.isMaximized, windowData?.position.x, windowData?.position.y, windowData?.size.width, windowData?.size.height, updatePosition]);

  if (!windowData || !windowData.isOpen || windowData.isMinimized) return null;

  const isFocused = focusedWindowId === id;
  const isMaximized = windowData.isMaximized;

  const onDragStop = (_e: DraggableEvent, data: DraggableData) => {
    updatePosition(id, clampPosition({ x: data.x, y: data.y }, windowData.size));
  };

  const onResizeStop = (_e: React.SyntheticEvent, data: ResizeData) => {
    updateSize(id, { width: data.size.width, height: data.size.height });
  };

  const windowContent = (
    <div className={`window flex flex-col h-full min-h-0 min-w-0 ${isMaximized ? 'border-0' : ''}`}>
      {/* Title Bar */}
      <div className={`title-bar flex-shrink-0 ${isFocused ? '' : 'inactive'}`} onDoubleClick={() => maximizeWindow(id)}>
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
      <div
        className="window-body flex-1 min-h-0 min-w-0 flex flex-col m-1 overflow-hidden"
        data-testid={`app-window-${id}-body`}
      >
        <div
          className={`flex-1 min-h-0 min-w-0 overflow-auto bg-white border-2 border-sunken shadow-inner ${(id === 'diagrams' || id === 'rules') ? 'p-0' : 'p-4'}`}
          data-testid={`app-window-${id}-scroller`}
        >
          {children}
        </div>
      </div>
    </div>
  );

  if (isMaximized) {
    return (
      <div
        className="fixed top-0 left-0 right-0 min-h-0 overflow-hidden bg-gray-300"
        data-testid={`app-window-${id}-maximized`}
        style={{ zIndex: windowData.zIndex, height: `calc(100dvh - ${TASKBAR_HEIGHT}px)` }}
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
      position={windowData.position}
      onStop={onDragStop}
      onStart={() => focusWindow(id)}
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
