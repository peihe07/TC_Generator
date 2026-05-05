import { proxyGetJsonRoute } from "../../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const qs = url.searchParams.toString();
  const suffix = qs ? `?${qs}` : "";
  return proxyGetJsonRoute(`/api/metrics/aggregate${suffix}`);
}
