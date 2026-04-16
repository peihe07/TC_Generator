"use client";

import { useMutation, useQuery } from "@tanstack/react-query";

import { apiRequest } from "@/src/services/apiClient";

const backendBaseUrl =
  process.env.NEXT_PUBLIC_PYTHON_API_BASE?.replace(/\/$/, "") ?? "";

export function useHealthcheck() {
  return useQuery({
    queryKey: ["python-api", "health"],
    queryFn: async () =>
      apiRequest<{ status: string }>(`${backendBaseUrl}/api/health`),
    enabled: Boolean(backendBaseUrl),
    retry: false,
  });
}

export function useTriggerParse() {
  return useMutation({
    mutationFn: async (payload: FormData) =>
      apiRequest<{ jobId: string }>(`${backendBaseUrl}/api/parse`, {
        method: "POST",
        body: payload,
      }),
  });
}

export function useBackendBaseUrl() {
  return backendBaseUrl;
}
