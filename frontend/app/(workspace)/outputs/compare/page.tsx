import { Suspense } from "react";
import OutputCompareView from "../../../../src/components/outputs/OutputCompareView";

export default async function OutputComparePage({
  searchParams,
}: {
  searchParams: Promise<{ a?: string; b?: string }>;
}) {
  const { a = "", b = "" } = await searchParams;
  return (
    <Suspense
      fallback={<div className="text-secondary text-sm">Loading...</div>}
    >
      <OutputCompareView a={a} b={b} />
    </Suspense>
  );
}
