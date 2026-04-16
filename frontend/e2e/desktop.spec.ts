import { test, expect } from '@playwright/test';

test.describe('Desktop shell', () => {
  test('loads Win95 desktop with 6 icons', async ({ page }) => {
    await page.goto('/');
    // Teal desktop background
    const desktop = page.locator('.desktop-bg');
    await expect(desktop).toBeVisible();

    // All 6 icons visible
    const icons = ['Upload', 'Configure', 'Generate', 'Review', 'Export', 'Quick TC'];
    for (const label of icons) {
      await expect(page.getByText(label, { exact: true })).toBeVisible();
    }

    // Taskbar at bottom (rendered as <footer>)
    await expect(page.locator('footer').first()).toBeVisible();
  });

  test('double-click icon opens window', async ({ page }) => {
    await page.goto('/');
    const uploadIcon = page.getByText('Upload', { exact: true });
    await uploadIcon.dblclick();

    // Window title appears in taskbar or title bar
    await expect(page.getByText('Upload Files').first()).toBeVisible();
  });

  test('window can be closed', async ({ page }) => {
    await page.goto('/');
    await page.getByText('Upload', { exact: true }).dblclick();
    await expect(page.getByText('Upload Files').first()).toBeVisible();

    // Click the close button (aria-label="Close")
    await page.getByRole('button', { name: 'Close' }).first().click();
    await expect(page.getByText('Upload Files').first()).not.toBeVisible();
  });

  test('multiple windows can be opened simultaneously', async ({ page }) => {
    await page.goto('/');
    await page.getByText('Upload', { exact: true }).dblclick();
    await page.getByText('Configure', { exact: true }).dblclick();

    await expect(page.getByText('Upload Files').first()).toBeVisible();
    await expect(page.getByText('TC Generator - Configure').first()).toBeVisible();
  });
});
