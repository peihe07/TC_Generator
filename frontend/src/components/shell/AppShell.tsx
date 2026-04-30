import CommandPalette from "./CommandPalette";
import DevStoreExposer from "./DevStoreExposer";
import TopNav from "./TopNav";

export default function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <TopNav />
      <main className="mx-auto max-w-[1600px] px-6 py-8">{children}</main>
      <CommandPalette />
      <DevStoreExposer />
    </div>
  );
}
