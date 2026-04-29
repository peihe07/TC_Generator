import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "TC Generator",
  description: "AI-powered Test Case Generator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
