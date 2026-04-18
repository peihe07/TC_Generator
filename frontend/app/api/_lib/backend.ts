const backendBaseUrl =
  process.env.PYTHON_API_BASE?.replace(/\/$/, "") ?? "";

export function getBackendBaseUrl() {
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
