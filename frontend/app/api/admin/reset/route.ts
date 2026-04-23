import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../../_lib/backend";

export const runtime = "nodejs";

export async function DELETE() {
  try {
    return await proxyJsonResponse("/api/admin/reset", {
      method: "DELETE",
    });
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
