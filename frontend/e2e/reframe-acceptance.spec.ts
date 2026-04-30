import { expect, test, type Page } from "@playwright/test";

const DRAFT_KEY = "tc-generator-builder-draft";
const HISTORY_KEY = "tc-generator-job-history";
const EXPERIMENT_KEY = "tc:experiments:v1";

function jobRecord(id: string, overrides: Record<string, unknown> = {}) {
  const now = Date.now();
  return {
    id,
    kind: "generate",
    model: "gpt-5",
    startedAt: now - 60_000,
    finishedAt: now - 30_000,
    rowsTotal: 4,
    rowsProcessed: 4,
    cost: 0.12,
    inputTokens: 1000,
    outputTokens: 500,
    cacheReadTokens: 100,
    cacheCreationTokens: 25,
    ...overrides,
  };
}

async function seedLocalStorage(page: Page, values: Record<string, unknown>) {
  await page.addInitScript((seed) => {
    for (const [key, value] of Object.entries(seed)) {
      window.localStorage.setItem(key, JSON.stringify(value));
    }
  }, values);
}

async function mockSpecLibrary(page: Page) {
  await page.route("**/api/spec-library", async (route) => {
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        specs: [
          {
            name: "body-control",
            sourceFile: "BodyControl.md",
            entriesCount: 12,
            embeddingModel: "text-embedding-3-small",
            updatedAt: "2026-04-29",
          },
        ],
      }),
    });
  });
  await page.route("**/api/spec-library/body-control/usage", async (route) => {
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        name: "body-control",
        usageCount: 0,
        lastUsedAt: null,
        recentRunIds: [],
      }),
    });
  });
}

async function mockOutputCompare(page: Page) {
  await page.route("**/api/outputs/compare", async (route) => {
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        a: "run-a",
        b: "run-b",
        summary: {
          total: 2,
          added: 1,
          removed: 0,
          changed: 1,
          unchanged: 0,
        },
        rows: [
          {
            tcId: "TC-001",
            reqId: "REQ-1",
            status: "changed",
            changes: [
              {
                field: "expectedResult",
                label: "Expected Result",
                before: "Old",
                after: "New",
              },
            ],
          },
        ],
      }),
    });
  });
}

test.describe("Reframe acceptance", () => {
  test("Home A/B override persists assignment and records exposure", async ({
    page,
  }) => {
    await page.goto("/?exp_home_layout_emphasis=action_first");

    await expect(page.getByText("Quick Actions")).toBeVisible();
    await expect
      .poll(async () => {
        const assignment = await page.evaluate((key) => {
          return JSON.parse(window.localStorage.getItem(key) ?? "{}");
        }, EXPERIMENT_KEY);
        return assignment.home_layout_emphasis?.variant;
      })
      .toBe("action_first");

    const events = await page.evaluate(() => {
      return (window as unknown as { __tcEvents?: Array<Record<string, unknown>> })
        .__tcEvents;
    });
    expect(events?.some((event) => event.name === "experiment_exposure")).toBe(
      true
    );
  });

  test("Run Builder restores draft after refresh", async ({ page }) => {
    await seedLocalStorage(page, {
      [DRAFT_KEY]: {
        id: "draft_acceptance",
        createdAt: Date.now() - 10_000,
        updatedAt: Date.now() - 1_000,
        currentStep: "configure",
        completed: { data: true },
      },
    });

    await page.goto("/run-builder");
    await expect(
      page.getByRole("heading", { level: 1, name: "Configure Rules" })
    ).toBeVisible();
    await expect(page.getByText("draft_acceptance")).toBeVisible();

    await page.reload();
    await expect(
      page.getByRole("heading", { level: 1, name: "Configure Rules" })
    ).toBeVisible();
    await expect(page.getByText("draft_acceptance")).toBeVisible();
  });

  test("Template detail can start a template-backed run", async ({ page }) => {
    await mockSpecLibrary(page);
    await page.goto("/templates/body-control");

    await expect(
      page.getByRole("heading", { level: 1, name: "body-control" })
    ).toBeVisible();
    await page.getByRole("link", { name: /Use in New Run/i }).click();

    await expect(page).toHaveURL(/\/run-builder\?templateId=body-control/);
    await expect(page.getByText("Using template")).toBeVisible();
    await expect(
      page.locator("code", { hasText: "body-control" }).first()
    ).toBeVisible();
  });

  test("Outputs can select two runs and open compare view", async ({ page }) => {
    await seedLocalStorage(page, {
      [HISTORY_KEY]: [
        jobRecord("run-a"),
        jobRecord("run-b", { kind: "rerun", cost: 0.2 }),
      ],
    });
    await mockOutputCompare(page);

    await page.goto("/outputs");
    await page.getByLabel("Select run-a").check();
    await page.getByLabel("Select run-b").check();
    await page.getByRole("link", { name: /Compare/i }).click();

    await expect(page).toHaveURL(/\/outputs\/compare\?a=run-a&b=run-b/);
    await expect(
      page.getByRole("heading", { level: 1, name: "Compare Outputs" })
    ).toBeVisible();
    await expect(page.getByText("Total TCs")).toBeVisible();
    await expect(page.getByText("Expected Result")).toBeVisible();
  });

  test("Run Detail exposes edit-and-rerun path for failed runs", async ({
    page,
  }) => {
    await seedLocalStorage(page, {
      [HISTORY_KEY]: [
        jobRecord("run-failed", {
          rowsTotal: 4,
          rowsProcessed: 0,
          cost: 0.04,
        }),
      ],
    });

    await page.goto("/runs/run-failed");
    await expect(
      page.getByRole("heading", { level: 1, name: "Generate" })
    ).toBeVisible();
    await expect(page.getByText("Failed", { exact: true })).toBeVisible();

    await page.getByRole("link", { name: /Edit & Rerun/i }).click();
    await expect(page).toHaveURL(/\/run-builder\?edit=run-failed/);
    await expect(page.getByText("Editing run")).toBeVisible();
    await expect(page.getByText("run-failed")).toBeVisible();
  });
});
