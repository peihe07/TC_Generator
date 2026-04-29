import CommandPalette from "./CommandPalette";
import TopNav from "./TopNav";

export default function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div
      className="min-h-screen"
      style={{ backgroundColor: "var(--color-papaya)" }}
    >
      <TopNav />
      <main className="mx-auto max-w-[1600px] px-6 py-8">{children}</main>
      <CommandPalette />
    </div>
  );
}
