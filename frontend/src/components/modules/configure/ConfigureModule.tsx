'use client';

import React from 'react';
import * as Tabs from '@radix-ui/react-tabs';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { 
  RiNodeTree, 
  RiLinkM, 
  RiSettings4Line,
  RiArrowLeftLine,
  RiPlayFill
} from '@remixicon/react';

const ConfigureModule: React.FC = () => {
  const { tcRows, config, updateConfig, stats } = useJobStore();
  const { openWindow } = useWindowStore();

  const handleStartGenerate = () => {
    openWindow('generate', 'TC Generator - Generating...');
  };

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <Tabs.Root className="flex-1 flex flex-col" defaultValue="tab1">
        <Tabs.List className="tabs" aria-label="Configuration steps">
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab1">
            <RiNodeTree className="size-4" /> Grouping
          </Tabs.Trigger>
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab2">
            <RiLinkM className="size-4" /> Spec Matching
          </Tabs.Trigger>
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab3">
            <RiSettings4Line className="size-4" /> Options
          </Tabs.Trigger>
        </Tabs.List>

        <div className="flex-1 mt-2 overflow-hidden flex flex-col">
          {/* Tab 1: Grouping Preview */}
          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-2" value="tab1">
            <p className="mb-3 text-sm">AI-suggested test sets based on requirements:</p>
            <table className="w-full text-sm border-collapse">
              <thead>
                <tr className="bg-gray-200 border-b border-gray-400">
                  <th className="text-left p-1 border-r border-gray-300">Test Set</th>
                  <th className="text-left p-1">Requirement IDs</th>
                </tr>
              </thead>
              <tbody>
                {tcRows.length > 0 ? (
                  tcRows.map((row) => (
                    <tr key={row.id} className="border-b border-gray-200 hover:bg-blue-50">
                      <td className="p-1 border-r border-gray-300 font-mono">{row.testSet}</td>
                      <td className="p-1 text-gray-600">{row.reqId}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={2} className="p-4 text-center text-gray-400 italic">No data imported yet.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </Tabs.Content>

          {/* Tab 2: Spec Matching */}
          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-2" value="tab2">
            <div className="flex flex-col gap-2">
              <div className="status-bar-field p-2 bg-blue-50 text-blue-800 text-xs">
                Layer 1: Exact matches found for {tcRows.length} items. AI Layer 2 ready for remaining.
              </div>
              <table className="w-full text-xs border-collapse">
                <thead>
                  <tr className="bg-gray-200 border-b border-gray-400">
                    <th className="p-1 border-r text-left">Req ID</th>
                    <th className="p-1 border-r text-left">Test Item</th>
                    <th className="p-1 text-left">Matched Spec</th>
                  </tr>
                </thead>
                <tbody>
                  {tcRows.map(row => (
                    <tr key={row.id} className="border-b">
                      <td className="p-1 border-r font-mono">{row.reqId}</td>
                      <td className="p-1 border-r truncate max-w-[150px]">{row.testItem}</td>
                      <td className="p-1 text-green-700">SPEC_REF_{row.reqId} (Exact)</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </Tabs.Content>

          {/* Tab 3: Options */}
          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-4" value="tab3">
            <div className="flex flex-col gap-6">
              <fieldset>
                <legend>AI Model Settings</legend>
                <div className="flex flex-col gap-2">
                  <div className="field-row">
                    <input 
                      type="radio" id="m1" name="model" 
                      checked={config.model === 'claude-3-5-sonnet'} 
                      onChange={() => updateConfig({ model: 'claude-3-5-sonnet' })}
                    />
                    <label htmlFor="m1">Claude 3.5 Sonnet (High Accuracy)</label>
                  </div>
                  <div className="field-row">
                    <input 
                      type="radio" id="m2" name="model" 
                      checked={config.model === 'claude-3-haiku'} 
                      onChange={() => updateConfig({ model: 'claude-3-haiku' })}
                    />
                    <label htmlFor="m2">Claude 3 Haiku (Fast & Cheap)</label>
                  </div>
                </div>
              </fieldset>

              <fieldset>
                <legend>Generation Limits</legend>
                <div className="field-row-stacked">
                  <label htmlFor="budget">Max Budget (USD): ${config.budgetLimit}</label>
                  <input 
                    id="budget" type="range" min="1" max="50" 
                    value={config.budgetLimit} 
                    onChange={(e) => updateConfig({ budgetLimit: parseInt(e.target.value) })}
                  />
                </div>
              </fieldset>

              <fieldset>
                <legend>Target Columns</legend>
                <div className="grid grid-cols-2 gap-2">
                  {['preConditions', 'steps', 'expectedResults'].map(col => (
                    <div key={col} className="field-row">
                      <input 
                        type="checkbox" id={col} 
                        checked={config.targetColumns.includes(col)}
                        onChange={(e) => {
                          const cols = e.target.checked 
                            ? [...config.targetColumns, col]
                            : config.targetColumns.filter(c => c !== col);
                          updateConfig({ targetColumns: cols });
                        }}
                      />
                      <label htmlFor={col}>{col.charAt(0).toUpperCase() + col.slice(1)}</label>
                    </div>
                  ))}
                </div>
              </fieldset>
            </div>
          </Tabs.Content>
        </div>
      </Tabs.Root>

      {/* Footer Actions */}
      <div className="flex justify-between items-center pt-4 border-t border-gray-400 mt-2">
        <button className="flex items-center gap-1" onClick={() => openWindow('upload', 'Upload Files')}>
          <RiArrowLeftLine className="size-4" /> Back
        </button>
        <div className="text-xs text-gray-500">
          Estimated tokens: ~45k | Estimated Cost: <span className="text-black font-bold font-mono">$0.15</span>
        </div>
        <button className="flex items-center gap-1 font-bold default" onClick={handleStartGenerate}>
          Start Generate <RiPlayFill className="size-4 text-green-700" />
        </button>
      </div>
    </div>
  );
};

export default ConfigureModule;
