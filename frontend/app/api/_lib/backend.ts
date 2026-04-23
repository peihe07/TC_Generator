const configuredBackendBaseUrl = process.env.PYTHON_API_BASE?.replace(/\/$/, "") ?? "";
const fallbackBackendBaseUrl =
  process.env.NODE_ENV === "production" ? "" : "http://127.0.0.1:8000";

export function getBackendBaseUrl() {
  const backendBaseUrl = configuredBackendBaseUrl || fallbackBackendBaseUrl;
  if (!backendBaseUrl) {
    throw new Error("Backend base URL is not configured.");
  }
  return backendBaseUrl;
}

export async function proxyJson(
  path: string,
  init?: RequestInit,
): Promise<Response> {
  const response = await fetch(`${getBackendBaseUrl()}${path}`, init);
  return response;
}

export async function proxyJsonResponse(
  path: string,
  init?: RequestInit,
  mutateJson?: (data: unknown) => unknown,
): Promise<Response> {
  const response = await fetch(`${getBackendBaseUrl()}${path}`, init);
  const contentType = response.headers.get("content-type") ?? "";
  const bodyText = await response.text();

  if (bodyText) {
    try {
      const parsed = JSON.parse(bodyText) as unknown;
      const data = mutateJson ? mutateJson(parsed) : parsed;
      return Response.json(data, { status: response.status });
    } catch {
      // Upstream returned a non-JSON body. Preserve its status/body instead of
      // masking it as a generic proxy failure.
    }
  }

  return new Response(bodyText, {
    status: response.status,
    statusText: response.statusText,
    headers: contentType ? { "Content-Type": contentType } : undefined,
  });
}

export async function proxyStream(
  path: string,
  init?: RequestInit,
): Promise<Response> {
  const response = await fetch(`${getBackendBaseUrl()}${path}`, init);
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers: response.headers,
  });
}
