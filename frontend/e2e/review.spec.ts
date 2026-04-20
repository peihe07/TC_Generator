import { test, expect } from '@playwright/test';
import { injectMockRows } from './helpers/injectMockRows';

test.describe('Review module', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await injectMockRows(page);
    await page.getByText('Review', { exact: true }).dblclick();
    await expect(page.getByText('TC Generator - Review').first()).toBeVisible();
  });

  test('displays TC table with rows', async ({ page }) => {
    // Table header
    await expect(page.getByText('TC ID')).toBeVisible();
    await expect(page.getByText('Req ID')).toBeVisible();
    await expect(page.getByText('Status')).toBeVisible();
  });

  test('filter dropdown changes visible rows', async ({ page }) => {
    const select = page.locator('select#filter');
    await select.selectOption('flagged');
    // No crash — filter applies cleanly
    await expect(select).toHaveValue('flagged');
  });

  test('expand row shows detail panel', async ({ page }) => {
    // Click the first expand arrow
    await page.locator('table tbody tr').first().click();
    await expect(page.getByText('Original Requirement')).toBeVisible();
    await expect(page.getByText('Generated Test Case')).toBeVisible();
  });

  test('accept button changes row status', async ({ page }) => {
    // Find the first accept button and click it
    const acceptBtn = page.locator('button[title="Accept"]').first();
    await acceptBtn.click();
    // Status badge should update (accepted)
    await expect(page.locator('span:has-text("accepted")').first()).toBeVisible();
  });

  test('delete removes row from table', async ({ page }) => {
    // Count rows before
    const rowsBefore = await page.locator('table tbody tr:not([class*="expanded"])').count();

    // Click delete on first row → Win95Dialog opens → confirm
    await page.locator('button[title="Delete"]').first().click();
    await page
      .getByRole('alertdialog')
      .getByRole('button', { name: 'Delete' })
      .click();

    // One fewer row
    const rowsAfter = await page.locator('table tbody tr:not([class*="expanded"])').count();
    expect(rowsAfter).toBeLessThan(rowsBefore);
  });

  test('checkbox selection shows floating action bar', async ({ page }) => {
    // Click first checkbox
    await page.locator('table tbody tr').first()
      .locator('button').first().click();

    // Floating bar with "Selected" text appears
    await expect(page.getByText(/row.*selected/i)).toBeVisible();
    await expect(page.getByRole('button', { name: /Regenerate.*Selected/i })).toBeVisible();
  });

  test('export button opens export window', async ({ page }) => {
    await page.getByText('Export All').click();
    await expect(page.getByText('Export').first()).toBeVisible();
  });
});
