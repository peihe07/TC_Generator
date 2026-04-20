import { test, expect } from '@playwright/test';

test.describe('Desktop shell', () => {
  test('loads Win95 desktop with all icons', async ({ page }) => {
    await page.goto('/');
    // Teal desktop background
    const desktop = page.locator('.desktop-bg');
    await expect(desktop).toBeVisible();

    // 8 desktop icons visible
    const icons = ['Upload', 'Configure', 'Generate', 'Review', 'Export', 'Quick TC', 'Diagrams', 'TC Rules'];
    for (const label of icons) {
      await expect(page.getByText(label, { exact: true })).toBeVisible();
    }

    // Taskbar at bottom
    await expect(page.getByRole('contentinfo')).toBeVisible();
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
    // The Upload window's default position (x=140, y=60) overlaps the
    // Configure desktop icon to the left, so a plain dblclick on the
    // icon times out. Open Configure via the Start menu instead — the
    // taskbar is always on top at z-index 9999. Scope to contentinfo
    // (the Taskbar) since "Configure" text also exists on the desktop.
    await page.getByRole('button', { name: /Start/ }).click();
    await page
      .getByRole('contentinfo')
      .getByText('Configure', { exact: true })
      .click();

    await expect(page.getByText('Upload Files').first()).toBeVisible();
    await expect(page.getByText('TC Generator - Configure').first()).toBeVisible();
  });
});
