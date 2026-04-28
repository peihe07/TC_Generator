import http from "node:http";
import https from "node:https";

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
  return new Promise<Response>((resolve, reject) => {
    const url = new URL(`${getBackendBaseUrl()}${path}`);
    const transport = url.protocol === "https:" ? https : http;
    const headers = new Headers(init?.headers);
    const body = typeof init?.body === "string" ? init.body : undefined;

    if (body && !headers.has("Content-Length")) {
      headers.set("Content-Length", Buffer.byteLength(body).toString());
    }

    const req = transport.request(
      url,
      {
        method: init?.method ?? "GET",
        headers: Object.fromEntries(headers.entries()),
      },
      (upstream) => {
        const responseHeaders = new Headers();
        for (const [key, value] of Object.entries(upstream.headers)) {
          if (!value || key.toLowerCase() === "transfer-encoding") continue;
          responseHeaders.set(key, Array.isArray(value) ? value.join(", ") : value);
        }

        const stream = new ReadableStream<Uint8Array>({
          start(controller) {
            upstream.on("data", (chunk: Buffer) => {
              controller.enqueue(new Uint8Array(chunk));
            });
            upstream.on("end", () => {
              controller.close();
            });
            upstream.on("error", (error) => {
              controller.error(error);
            });
          },
          cancel() {
            upstream.destroy();
            req.destroy();
          },
        });

        resolve(
          new Response(stream, {
            status: upstream.statusCode ?? 502,
            statusText: upstream.statusMessage,
            headers: responseHeaders,
          }),
        );
      },
    );

    req.on("error", reject);
    init?.signal?.addEventListener("abort", () => {
      req.destroy();
      reject(new DOMException("The operation was aborted.", "AbortError"));
    });

    if (body) req.write(body);
    req.end();
  });
}
