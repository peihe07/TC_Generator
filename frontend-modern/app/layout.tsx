import type { Metadata } from "next";
import "./globals.css";
import "../src/styles/win95.css";
import "../src/styles/modern-theme.css";

export const metadata: Metadata = {
  title: "TC Generator Modern",
  description: "AI-powered Test Case Generator - Modern UI",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
