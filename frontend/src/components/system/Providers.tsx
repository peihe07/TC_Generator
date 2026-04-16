"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { useJobStore } from "../../store/useJobStore";

// Expose the Zustand store on window in non-production builds so Playwright
// tests can inject mock data via page.evaluate.
function DevStoreExposer() {
  useEffect(() => {
    if (process.env.NODE_ENV !== "production") {
      (window as unknown as Record<string, unknown>).__tcJobStore = useJobStore;
    }
  }, []);
  return null;
}

export function Providers({ children }: { children: React.ReactNode }) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: 30_000,
            refetchOnWindowFocus: false,
          },
        },
      }),
  );

  return (
    <QueryClientProvider client={queryClient}>
      <DevStoreExposer />
      {children}
    </QueryClientProvider>
  );
}
