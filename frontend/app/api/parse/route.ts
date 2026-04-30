import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const wsId = request.headers.get("x-workspace-id");
    return await proxyJsonResponse("/api/parse", {
      method: "POST",
      headers: wsId ? { "X-Workspace-Id": wsId } : undefined,
      body: formData,
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
