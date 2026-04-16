import type { Metadata } from "next";
import "./globals.css";

import { Providers } from "@/src/components/system/Providers";

export const metadata: Metadata = {
  title: "TC Generator Desktop",
  description: "Windows-style desktop shell for ASPICE SWE.6 test case generation.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full">
      <body className="min-h-full">
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
