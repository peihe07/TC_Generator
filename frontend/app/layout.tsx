import type { Metadata } from "next";
import "98.css"; // 直接引入確保載入
import "./globals.css";
import "../src/styles/win95.css";

export const metadata: Metadata = {
  title: "TC Generator - Windows 95 Edition",
  description: "AI-powered Test Case Generator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased overflow-hidden bg-black">
        {children}
      </body>
    </html>
  );
}
