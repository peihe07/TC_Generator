'use client';

import React, { useState } from 'react';

type RulesTab = 'aspice' | 'ai' | 'design';

const TABS: { id: RulesTab; label: string }[] = [
  { id: 'aspice', label: 'ASPICE SWE.6 Writing Rules' },
  { id: 'ai',     label: 'ASPICE SWE.6 AI Instruction' },
  { id: 'design', label: 'Design Method Decision Rules' },
];

const SRC: Record<RulesTab, string> = {
  aspice: '/rules-aspice.html',
  ai:     '/rules-ai-instruction.html',
  design: '/rules-design-method.html',
};

const RulesModule: React.FC = () => {
  const [activeTab, setActiveTab] = useState<RulesTab>('aspice');

  return (
    <div className="flex flex-col h-full">
      {/* Tab bar */}
      <menu role="tablist" style={{ marginBottom: -1, zIndex: 1, position: 'relative' }}>
        {TABS.map((t) => (
          <li key={t.id} role="tab" aria-selected={activeTab === t.id}>
            <a onClick={() => setActiveTab(t.id)} style={{ cursor: 'pointer' }}>
              {t.label}
            </a>
          </li>
        ))}
      </menu>

      {/* Content — frame comes from AppWindow's outer .border-sunken; no
       * inline bezel here (nested sunken borders read as too heavy, per
       * MIGRATION.md §P13). */}
      <div
        role="tabpanel"
        style={{
          flex: 1,
          overflow: 'hidden',
          minHeight: 0,
        }}
      >
        <iframe
          key={activeTab}
          src={SRC[activeTab]}
          style={{ width: '100%', height: '100%', border: 'none', display: 'block' }}
          title={TABS.find(t => t.id === activeTab)?.label}
        />
      </div>
    </div>
  );
};

export default RulesModule;
