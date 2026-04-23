'use client';

import React from 'react';

const DiagramsModule: React.FC = () => (
  <iframe
    src="/diagrams.html"
    style={{ width: '100%', height: '100%', border: 'none', display: 'block' }}
    title="Workflow Diagrams"
  />
);

export default DiagramsModule;
