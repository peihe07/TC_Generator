import "98.css";
import "../../src/styles/win95.css";

export default function LegacyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="legacy-shell w-full h-screen overflow-hidden bg-black">
      {children}
    </div>
  );
}
