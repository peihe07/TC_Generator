import { proxyGetJsonRoute } from "../_lib/backend";

export const runtime = "nodejs";

export async function GET() {
  return proxyGetJsonRoute("/api/spec-library");
}
