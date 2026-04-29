// 共用 shimmer skeleton。背景跟 surface 一致（Papaya 半透明），用 keyframes
// 帶一道 horizontal sweep 的 highlight。

interface SkeletonProps {
  width?: number | string;
  height?: number | string;
  rounded?: number | string;
  className?: string;
  inline?: boolean;
}

export function Skeleton({
  width = "100%",
  height = 16,
  rounded = 6,
  className = "",
  inline = false,
}: SkeletonProps) {
  return (
    <span
      aria-hidden="true"
      className={`tc-skeleton ${className}`}
      style={{
        display: inline ? "inline-block" : "block",
        width,
        height,
        borderRadius: rounded,
      }}
    />
  );
}

export function SkeletonRows({
  rows = 3,
  rowHeight = 14,
  gap = 10,
}: {
  rows?: number;
  rowHeight?: number;
  gap?: number;
}) {
  return (
    <div className="space-y-0" style={{ display: "grid", gap }}>
      {Array.from({ length: rows }).map((_, i) => (
        <Skeleton
          key={i}
          height={rowHeight}
          width={i === rows - 1 ? "60%" : "100%"}
        />
      ))}
    </div>
  );
}

export function SkeletonCard() {
  return (
    <div className="surface p-5 space-y-3">
      <div className="flex items-start gap-3">
        <Skeleton width={40} height={40} rounded={10} />
        <div className="flex-1 space-y-2">
          <Skeleton height={14} width="70%" />
          <Skeleton height={10} width="40%" />
        </div>
      </div>
      <SkeletonRows rows={2} rowHeight={10} />
    </div>
  );
}
