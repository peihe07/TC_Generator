import { NextResponse } from "next/server";

import { proxyJsonResponse ,  workspaceHeaderFrom } from "../../_lib/backend";

export const runtime = "nodejs";

export async function PATCH(
  request: Request,
  context: { params: Promise<{ name: string }> },
) {
  try {
    const { name } = await context.params;
    const body = await request.text();
    return await proxyJsonResponse(
      `/api/spec-library/${encodeURIComponent(name)}`,
      {
        method: "PATCH",
        headers: {
        "Content-Type": "application/json",
        ...workspaceHeaderFrom(request),
      },
        body,
      },
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
