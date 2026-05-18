import { proxyTextStreamRoute } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  return proxyTextStreamRoute(request, "/api/quick-generate/stream");
}
