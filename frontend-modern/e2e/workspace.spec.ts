import { test, expect } from '@playwright/test';

// Workspace manager — Save / Export / Import round-trip.
// Runs purely in the browser (localStorage); no backend required.

async function setSeedState(page: import('@playwright/test').Page) {
  await page.evaluate(() => {
    const store = (window as unknown as { __tcJobStore?: { setState: (s: unknown) => void } }).__tcJobStore;
    if (!store) throw new Error('__tcJobStore not exposed (dev mode required)');
    store.setState({
      jobMetadata: {
        jobId: 'job-ws-e2e-42',
        projectName: 'WorkspaceRoundtrip',
        createdAt: '2026-04-17T00:00:00Z',
        totalRows: 2,
      },
      tcRows: [
        { id: 'r1', reqId: 'REQ-1', testGroup: 'Group', testSet: 'Alpha', testItem: 'first', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'pending' },
        { id: 'r2', reqId: 'REQ-2', testGroup: 'Group', testSet: 'Beta',  testItem: 'second', preConditions: '', inputTestData: '', steps: '', expectedResults: '', status: 'pending' },
      ],
      stats: { total: 2, processed: 0, success: 0, fail: 0, cost: 0.125, inputTokens: 1234, outputTokens: 321, cacheCreationTokens: 0, cacheReadTokens: 999 },
    });
  });
}

async function readJobState(page: import('@playwright/test').Page) {
  return page.evaluate(() => {
    const store = (window as unknown as { __tcJobStore?: { getState: () => unknown } }).__tcJobStore;
    if (!store) throw new Error('__tcJobStore not exposed');
    const s = store.getState() as { jobMetadata: unknown; tcRows: unknown[]; stats: unknown };
    return { jobMetadata: s.jobMetadata, tcRows: s.tcRows, stats: s.stats };
  });
}

test.describe('Workspace manager', () => {
  test('save current state, export to JSON, import back', async ({ page }) => {
    await page.goto('/');
    // 清空 localStorage 以確保測試乾淨
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    // 1. 注入種子 state
    await setSeedState(page);
    const seed = await readJobState(page);
    expect((seed.tcRows as unknown[]).length).toBe(2);

    // 2. 打開 Workspace 選單
    await page.getByRole('button', { name: /Workspace/ }).click();

    // 3. 點 Save As…（會跳 prompt，播放腳本自動填名字）
    page.once('dialog', (d) => d.accept('roundtrip-ws'));
    await page.getByRole('button', { name: 'Save As…' }).click();

    // 4. 列表出現該 workspace
    await expect(page.getByTitle(/Load "roundtrip-ws"/)).toBeVisible();

    // 5. 匯出下載
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      page.getByTitle('Export to JSON').first().click(),
    ]);
    const exportedPath = await download.path();
    expect(exportedPath).toBeTruthy();

    // 6. 新建（清空 current state）
    page.once('dialog', (d) => d.accept());
    await page.getByRole('button', { name: 'New' }).click();
    const cleared = await readJobState(page);
    expect((cleared.tcRows as unknown[]).length).toBe(0);

    // 7. 再匯入剛才的 JSON
    const importBtn = page.getByRole('button', { name: 'Import…' });
    const [fileChooser] = await Promise.all([
      page.waitForEvent('filechooser'),
      importBtn.click(),
    ]);
    await fileChooser.setFiles(exportedPath!);
    page.once('dialog', (d) => d.accept()); // "Imported 'roundtrip-ws'." alert

    // 8. 從列表點 Load 恢復 state
    // 選單在前面所有動作都沒被關閉（WorkspaceMenu 的 setOpen(false)
    // 只綁在 "Reset All Data" 按鈕與 document mousedown-outside 上，
    // 其他動作都維持開啟），所以不必再點 Workspace button toggle —
    // toggle 反而會關閉選單讓 Load 按鈕不可見。
    await page.getByTitle(/Load "roundtrip-ws"/).first().click();

    // 9. 驗證 state 與原始一致
    const restored = await readJobState(page);
    expect((restored.tcRows as Array<{ reqId: string }>).map((r) => r.reqId)).toEqual(['REQ-1', 'REQ-2']);
    expect((restored.stats as { cost: number }).cost).toBeCloseTo(0.125);
    expect((restored.jobMetadata as { jobId: string }).jobId).toBe('job-ws-e2e-42');
  });

  test('workspace JSON does not contain agent session state', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    await setSeedState(page);

    // Inject fake agent state into localStorage to verify it won't leak into workspace export
    await page.evaluate(() => {
      localStorage.setItem('agent-session-id', 'fake-session-abc');
      localStorage.setItem('agent-messages', JSON.stringify([{ kind: 'user', text: 'hello' }]));
    });

    // Open Workspace and save
    await page.getByRole('button', { name: /Workspace/ }).click();
    page.once('dialog', (d) => d.accept('no-agent-leak'));
    await page.getByRole('button', { name: 'Save As…' }).click();

    // Export to JSON — the per-workspace Export button's accessible name
    // comes from its title attribute ("Export to JSON"), not "Export JSON".
    // Menu stays open between actions so no re-toggle needed.
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      page.getByRole('button', { name: 'Export to JSON' }).first().click(),
    ]);

    const content = await download.createReadStream();
    const chunks: Buffer[] = [];
    for await (const chunk of content) chunks.push(chunk as Buffer);
    const json = JSON.parse(Buffer.concat(chunks).toString());

    // Agent state should not appear in workspace export
    const jsonStr = JSON.stringify(json);
    expect(jsonStr).not.toContain('fake-session-abc');
    expect(jsonStr).not.toContain('agent-session');
    expect(jsonStr).not.toContain('agentStore');
  });
});
