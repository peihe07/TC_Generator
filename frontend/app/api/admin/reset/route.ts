import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../../_lib/backend";

export const runtime = "nodejs";

export async function DELETE() {
  try {
    const response = await fetch(`${getBackendBaseUrl()}/api/admin/reset`, {
      method: "DELETE",
    });
    const data = await response.json();
    return NextResponse.json(data, { status: response.status });
  } catch (error) {
    return NextResponse.json(
      {
        detail:
          error instanceof Error ? error.message : "Reset request failed.",
      },
      { status: 503 },
    );
  }
}
