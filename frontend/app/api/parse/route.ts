import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const response = await fetch(`${getBackendBaseUrl()}/api/parse`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    return NextResponse.json(data, { status: response.status });
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
