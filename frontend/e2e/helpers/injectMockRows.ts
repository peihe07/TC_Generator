import type { Page } from '@playwright/test';

export const MOCK_TC_ROWS = [
  {
    id: 'TC-001', reqId: 'REQ-LOG-01', testGroup: 'Auth', testSet: 'Login',
    testItem: 'User should be able to login with valid credentials.',
    preConditions: 'User is on the login page.',
    steps: '1. Enter "admin@test.com"\n2. Enter "Password123"\n3. Click Login',
    expectedResults: 'User is redirected to the dashboard.',
    status: 'accepted',
    validationErrors: [],
  },
  {
    id: 'TC-002', reqId: 'REQ-LOG-02', testGroup: 'Auth', testSet: 'Login',
    testItem: 'User should see error with invalid password.',
    preConditions: 'User is on the login page.',
    steps: '1. Enter "admin@test.com"\n2. Enter "WrongPass"\n3. Click Login',
    expectedResults: 'Error message is displayed.',
    status: 'pending',
    validationErrors: [],
  },
  {
    id: 'TC-003', reqId: 'REQ-DASH-05', testGroup: 'Dashboard', testSet: 'Stats',
    testItem: 'Dashboard should display real-time sales statistics.',
    preConditions: 'User is logged in.',
    steps: '1. Navigate to Dashboard\n2. Locate the Sales Chart\n3. Verify data',
    expectedResults: 'Chart renders correctly.',
    status: 'reviewing',
    validationErrors: [{ severity: 'warning', message: 'Verification step is ambiguous.' }],
  },
  {
    id: 'TC-004', reqId: 'REQ-USER-12', testGroup: 'User Mgmt', testSet: 'Profiles',
    testItem: 'Administrator can update any user profile.',
    preConditions: 'Logged in as Administrator.',
    steps: '1. Go to User List\n2. Select user\n3. Update email\n4. Save',
    expectedResults: 'Profile updated successfully.',
    status: 'flagged',
    validationErrors: [{ severity: 'error', message: 'Pre-condition too vague.' }],
  },
  {
    id: 'TC-005', reqId: 'REQ-SEC-09', testGroup: 'Security', testSet: 'MFA',
    testItem: 'MFA prompt appears for users with 2FA enabled.',
    preConditions: 'User account has 2FA active.',
    steps: '1. Enter credentials\n2. Click Login',
    expectedResults: 'MFA verification page shown.',
    status: 'pending',
    validationErrors: [],
  },
];

/** Inject mock TC rows into the Zustand store via window.__tcJobStore */
export async function injectMockRows(page: Page) {
  await page.waitForFunction(() => (window as unknown as Record<string, unknown>).__tcJobStore !== undefined);
  await page.evaluate((rows) => {
    const store = (window as unknown as Record<string, unknown>).__tcJobStore as {
      setState: (s: Record<string, unknown>) => void;
    };
    store.setState({ tcRows: rows });
  }, MOCK_TC_ROWS);
}
