import { test, expect } from '@playwright/test';

test.describe('Quick TC Generator (mock mode)', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.getByText('Quick TC', { exact: true }).dblclick();
    await expect(page.getByText('Quick TC Generator').first()).toBeVisible();
  });

  test('shows three mode options', async ({ page }) => {
    await expect(page.getByText('Single TC')).toBeVisible();
    await expect(page.getByText('With Context')).toBeVisible();
    await expect(page.getByText('Decompose')).toBeVisible();
  });

  test('generate button disabled when input is empty', async ({ page }) => {
    const btn = page.getByRole('button', { name: /Generate TC/i });
    await expect(btn).toBeDisabled();
  });

  test('single mode — generates one TC card (mock)', async ({ page }) => {
    await page.locator('textarea').first().fill('User can log in with valid credentials');
    await page.getByRole('button', { name: /Generate TC/i }).click();

    // Wait for TC card (mock takes ~800ms) then expand it
    await expect(page.getByText('TC 1')).toBeVisible({ timeout: 3000 });
    await expect(page.getByText('Test Item Rewrite')).toBeVisible();
    await expect(page.getByText('Expected Result')).toBeVisible();
  });

  test('single mode — copy button works', async ({ page }) => {
    await page.locator('textarea').first().fill('System rejects invalid password');
    await page.getByRole('button', { name: /Generate TC/i }).click();
    await expect(page.getByText('TC 1')).toBeVisible({ timeout: 3000 });

    // Copy button becomes "Copied" after click
    await page.getByRole('button', { name: /Copy/i }).click();
    await expect(page.getByText('Copied')).toBeVisible();
  });

  test('with context mode — shows context textarea', async ({ page }) => {
    // Click the label text to select the radio (input is wrapped inside label)
    await page.getByText('With Context', { exact: true }).click();
    // Two textareas should be visible
    const textareas = page.locator('textarea');
    await expect(textareas).toHaveCount(2);
  });

  test('decompose mode — shows analysis block with scenarios (mock)', async ({ page }) => {
    await page.getByText('Decompose', { exact: true }).click();
    await page.locator('textarea').first().fill('The system must handle user authentication including login, logout, and session management');
    await page.getByRole('button', { name: /Analyse & Generate/i }).click();

    // Analysis block appears (mock takes ~900ms)
    await expect(page.getByText(/scenarios identified/i)).toBeVisible({ timeout: 3000 });
    await expect(page.getByText('Normal flow').first()).toBeVisible();
    await expect(page.getByText('Boundary condition').first()).toBeVisible();
    await expect(page.getByText('Error handling').first()).toBeVisible();

    // Wait for all 3 TCs
    await expect(page.getByText('TC 3')).toBeVisible({ timeout: 5000 });
  });

  test('stop button aborts generation', async ({ page }) => {
    await page.getByText('Decompose', { exact: true }).click();
    await page.locator('textarea').first().fill('Complex multi-scenario requirement');
    await page.getByRole('button', { name: /Analyse & Generate/i }).click();

    // Stop quickly
    await page.getByRole('button', { name: /Stop/i }).click();
    // Should return to idle or stop — no crash
    await expect(page.locator('body')).not.toContainText('error');
  });
});
