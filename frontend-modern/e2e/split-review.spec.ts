import { test, expect } from '@playwright/test';
import type { Page } from '@playwright/test';

/**
 * E2E: 多筆 TC 拆分流程在 Review UI 的顯示。
 *
 * 驗證：
 * - Primary row（subIndex 0）展開後顯示「AI 拆分決策」卡片，內有 reasoning 文字
 * - Sub row（subIndex >= 1）展開後顯示「屬於 REQ-xxx 的 TC k/N」小 badge
 * - splitWarning 會在 primary row 展開面板頂部呈現黃框警示
 */

const SPLIT_ROWS = [
  {
    id: 'row-10',
    rowNum: 10,
    tcId: 'newR1L-DMR-001',
    reqId: 'REQ-ENUM-01',
    testGroup: 'Feature',
    testSet: 'Formats',
    testItem: 'System shall support upload of .mp4, .avi, .mpg video files.',
    preConditions: 'Dev build only.',
    steps: '1. Open upload dialog\n2. Select .mp4 file\n3. Verify upload',
    expectedResults: '1. Dialog opens\n2. File selected\n3. Upload succeeds',
    status: 'pending',
    validationErrors: [],
    splitDecision: {
      reqId: 'REQ-ENUM-01',
      tcCount: 3,
      subIndex: 0,
      parentId: 'row-10',
      reasoning:
        'Per §1.4 (Mistake #4), the requirement enumerates 3 supported formats — one TC per format to avoid False Pass.',
      keywords: [
        { keyword: 'supported formats', meaning: '系統允許的影片格式', coveredBy: [1, 2, 3] },
      ],
    },
  },
  {
    id: 'row-10__tc2',
    rowNum: 10,
    tcId: 'newR1L-DMR-013',
    reqId: 'REQ-ENUM-01',
    testGroup: 'Feature',
    testSet: 'Formats',
    testItem: 'System shall support upload of .mp4, .avi, .mpg video files.',
    preConditions: 'Dev build only.',
    steps: '1. Open upload dialog\n2. Select .avi file\n3. Verify upload',
    expectedResults: '1. Dialog opens\n2. File selected\n3. Upload succeeds',
    status: 'pending',
    validationErrors: [],
    splitDecision: {
      reqId: 'REQ-ENUM-01',
      tcCount: 3,
      subIndex: 1,
      parentId: 'row-10',
      reasoning: '',
      keywords: [],
    },
  },
  {
    id: 'row-20',
    rowNum: 20,
    tcId: 'newR1L-DMR-020',
    reqId: 'REQ-BOUND-02',
    testGroup: 'Feature',
    testSet: 'Limits',
    testItem: 'Phonebook shall store a maximum of 5000 entries.',
    preConditions: 'A PBAP-supported device is available.',
    steps: '1. Sync\n2. Check count',
    expectedResults: '1. Sync ok\n2. Count <= 5000',
    status: 'pending',
    validationErrors: [],
    splitDecision: {
      reqId: 'REQ-BOUND-02',
      tcCount: 1,
      subIndex: 0,
      parentId: 'row-20',
      reasoning: '',
      keywords: [],
    },
    splitWarning:
      '需求提及 maximum / minimum / 上下限字眼（§1.2 & BVA），建議至少拆成「= 上限」「> 上限」「< 上限」等獨立情境。',
  },
];

async function injectSplitRows(page: Page) {
  await page.waitForFunction(
    () => (window as unknown as Record<string, unknown>).__tcJobStore !== undefined,
  );
  await page.evaluate((rows) => {
    const store = (window as unknown as Record<string, unknown>).__tcJobStore as {
      setState: (s: Record<string, unknown>) => void;
    };
    store.setState({ tcRows: rows });
  }, SPLIT_ROWS);
}

test.describe('Review — AI split decision UI', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await injectSplitRows(page);
    await page.getByText('Review', { exact: true }).dblclick();
    await expect(page.getByText('TC Generator - Review').first()).toBeVisible();
  });

  test('primary row shows AI 拆分決策 card with reasoning', async ({ page }) => {
    await page.locator('table tbody tr').first().click();
    // Header label with tc count
    await expect(page.getByText(/AI 拆分決策 — 3 TCs/)).toBeVisible();
    // Reasoning text
    await expect(page.getByText(/§1\.4.*Mistake #4/)).toBeVisible();
    // Keyword coverage section
    await expect(page.getByText('Keyword coverage (§1.3)')).toBeVisible();
  });

  test('sub row shows belongs-to badge instead of full decision', async ({ page }) => {
    // Click the sub row (2nd row in the table since it's row-10__tc2)
    const rows = page.locator('table tbody tr');
    await rows.nth(1).click();
    await expect(page.getByText(/屬於.*REQ-ENUM-01.*TC 2\/3/)).toBeVisible();
    // Sub row must NOT show the full AI 拆分決策 header
    await expect(page.getByText(/AI 拆分決策 — 3 TCs/)).toHaveCount(0);
  });

  test('row with splitWarning shows yellow warning banner', async ({ page }) => {
    // The 3rd row (row-20) has splitWarning; click to expand
    const rows = page.locator('table tbody tr');
    await rows.nth(2).click();
    await expect(page.getByText(/Split warning/)).toBeVisible();
    await expect(page.getByText(/maximum \/ minimum \/ 上下限/)).toBeVisible();
  });
});
