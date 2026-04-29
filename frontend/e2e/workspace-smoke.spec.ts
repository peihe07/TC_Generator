import { test, expect } from "@playwright/test";

// Smoke test for the new workspace shell. Verifies: top nav navigation,
// command palette toggle, builder routes & stepper, run detail fallback.
// Does NOT require backend; uses seeded localStorage to drive runs list.

test.describe("Workspace shell", () => {
  test("home renders top nav with primary destinations", async ({ page }) => {
    await page.goto("/");
    await expect(
      page.getByRole("heading", { level: 1, name: "Home" })
    ).toBeVisible();
    for (const label of ["Home", "Runs", "Templates", "Outputs", "Data"]) {
      await expect(page.getByRole("link", { name: label }).first()).toBeVisible();
    }
    // CTA visible（Home 頁有多個 "New Run" 連結，TopNav / Quick Actions / Recent Runs 空狀態）
    await expect(
      page.getByRole("link", { name: /New Run/i }).first()
    ).toBeVisible();
  });

  test("primary nav navigates between destinations", async ({ page }) => {
    await page.goto("/");
    await page.getByRole("link", { name: "Runs" }).first().click();
    await expect(
      page.getByRole("heading", { level: 1, name: "Runs" })
    ).toBeVisible();

    await page.getByRole("link", { name: "Templates" }).first().click();
    await expect(
      page.getByRole("heading", { level: 1, name: "Templates" })
    ).toBeVisible();

    await page.getByRole("link", { name: "Outputs" }).first().click();
    await expect(
      page.getByRole("heading", { level: 1, name: "Outputs" })
    ).toBeVisible();

    await page.getByRole("link", { name: "Data" }).first().click();
    await expect(
      page.getByRole("heading", { level: 1, name: "Data" })
    ).toBeVisible();
  });

  test("Cmd/Ctrl+K opens command palette", async ({ page }) => {
    await page.goto("/");
    await page.keyboard.press("ControlOrMeta+k");
    await expect(
      page.getByPlaceholder(/Type a command/i)
    ).toBeVisible();
    await page.keyboard.press("Escape");
    await expect(
      page.getByPlaceholder(/Type a command/i)
    ).not.toBeVisible();
  });

  test("Run Builder shows 5-step stepper", async ({ page }) => {
    await page.goto("/run-builder");
    // Run Builder 標頭 + 第一步 "Select Data" 標題與描述總是在
    await expect(
      page.getByRole("heading", { level: 1, name: "Select Data" })
    ).toBeVisible();
    // Stepper labels 在 md+ 才顯示；用 attached 而非 visible
    for (const label of [
      "Select Data",
      "Configure Rules",
      "Validate",
      "Execute",
      "Review",
    ]) {
      await expect(
        page.getByText(label, { exact: true }).first()
      ).toBeAttached();
    }
  });

  test("Run Detail shows not-found state for missing run", async ({ page }) => {
    await page.goto("/runs/non-existent-id");
    await expect(
      page.getByRole("heading", { name: /Run not found/i })
    ).toBeVisible();
    await expect(page.getByText("non-existent-id")).toBeVisible();
  });
});
