import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function GET(
  _request: Request,
  context: { params: Promise<{ name: string }> },
) {
  try {
    const { name } = await context.params;
    return await proxyJsonResponse(
      `/api/spec-library/${encodeURIComponent(name)}/usage`,
      { method: "GET" },
    );
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
