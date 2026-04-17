import { test, expect } from '@playwright/test';

test.describe('Window clamp behavior', () => {
  test('window dragged off-screen is pulled back', async ({ page }) => {
    await page.goto('/');
    await page.getByText('Upload', { exact: true }).dblclick();
    await expect(page.getByText('Upload Files').first()).toBeVisible();

    const titleBar = page.locator('.title-bar', { hasText: 'Upload Files' }).first();
    const before = await titleBar.boundingBox();
    expect(before).not.toBeNull();

    // 嘗試把視窗拖到右下角畫面外
    const viewport = page.viewportSize()!;
    await titleBar.hover();
    await page.mouse.down();
    await page.mouse.move(viewport.width + 500, viewport.height + 500, { steps: 10 });
    await page.mouse.up();

    const after = await titleBar.boundingBox();
    expect(after).not.toBeNull();

    // 標題列必須仍有部分在 viewport 內 (≥80px)
    expect(after!.x).toBeLessThan(viewport.width - 40);
    expect(after!.y).toBeLessThan(viewport.height);
  });

  test('window remains reachable after viewport resize', async ({ page }) => {
    await page.setViewportSize({ width: 1400, height: 900 });
    await page.goto('/');
    await page.getByText('Configure', { exact: true }).dblclick();

    const titleBar = page.locator('.title-bar', { hasText: 'Configure' }).first();
    await expect(titleBar).toBeVisible();

    // 把視窗拖到右下角靠邊
    await titleBar.hover();
    await page.mouse.down();
    await page.mouse.move(1300, 800, { steps: 5 });
    await page.mouse.up();

    // 縮小 viewport — clamp 應將視窗拉回
    await page.setViewportSize({ width: 800, height: 600 });
    await page.waitForTimeout(200);

    const after = await titleBar.boundingBox();
    expect(after).not.toBeNull();
    expect(after!.x).toBeLessThan(800 - 40);
    expect(after!.y).toBeLessThan(600);
  });
});

test.describe('CostMeter', () => {
  test('renders API Usage panel', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByText('API Usage', { exact: true })).toBeVisible();
    await expect(page.getByText('Total Cost', { exact: true })).toBeVisible();
    await expect(page.getByText('Model', { exact: true })).toBeVisible();
  });

  test('shows zero cost when no activity', async ({ page }) => {
    await page.goto('/');
    // 預設無任務 → 應顯示 $0.0000
    await expect(page.getByText(/\$0\.0000/)).toBeVisible();
  });
});

test.describe('Diagrams & Rules modules', () => {
  test('Diagrams module opens with iframe content', async ({ page }) => {
    await page.goto('/');
    await page.getByText('Diagrams', { exact: true }).dblclick();
    await expect(page.getByText('Architecture Diagrams').first()).toBeVisible();
    // 內嵌的 iframe（diagrams.html）
    await expect(page.locator('iframe').first()).toBeVisible();
  });

  test('TC Rules module opens', async ({ page }) => {
    await page.goto('/');
    await page.getByText('TC Rules', { exact: true }).dblclick();
    await expect(page.getByText('TC Writing Rules').first()).toBeVisible();
  });
});
