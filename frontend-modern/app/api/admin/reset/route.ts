import { NextResponse } from "next/server";

import { proxyErrorResponse, proxyJsonResponse } from "../../_lib/backend";

export const runtime = "nodejs";

function isLoopbackHost(hostname: string) {
  return hostname === "localhost" || hostname === "127.0.0.1" || hostname === "::1" || hostname === "[::1]";
}

export async function DELETE(request: Request) {
  try {
    const url = new URL(request.url);
    if (!isLoopbackHost(url.hostname)) {
      return NextResponse.json(
        { detail: "reset only allowed from localhost" },
        { status: 403 },
      );
    }

    return await proxyJsonResponse("/api/admin/reset", {
      method: "DELETE",
    });
  } catch (error) {
    return proxyErrorResponse(error, "Reset request failed.");
  }
}
