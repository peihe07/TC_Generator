import { NextResponse } from "next/server";

import { proxyJsonResponse ,  workspaceHeaderFrom } from "../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  try {
    return await proxyJsonResponse("/api/spec-library", {
      method: "GET",
      headers: workspaceHeaderFrom(request),
    });
  } catch (error) {
    return NextResponse.json(
      {
        detail:
          error instanceof Error ? error.message : "Proxy request failed.",
      },
      { status: 503 },
    );
  }
}
