"use client";

import { useMutation, useQuery } from "@tanstack/react-query";

import type {
  ExportRequest,
  ExportResponse,
  GenerateRequest,
  GenerateResponse,
  ParseResponse,
} from "@/src/lib/api-contract";
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
      apiRequest<ParseResponse>(`${backendBaseUrl}/api/parse`, {
        method: "POST",
        body: payload,
      }),
  });
}

export function useTriggerGenerate() {
  return useMutation({
    mutationFn: async (payload: GenerateRequest) =>
      apiRequest<GenerateResponse>(`${backendBaseUrl}/api/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      }),
  });
}

export function useTriggerExport() {
  return useMutation({
    mutationFn: async (payload: ExportRequest) =>
      apiRequest<ExportResponse>(`${backendBaseUrl}/api/export`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      }),
  });
}

export function useBackendBaseUrl() {
  return backendBaseUrl;
}
