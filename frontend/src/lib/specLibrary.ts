// Spec library 名稱顯示助手。原本住在 legacy UploadModule 裡，抽出供新 Builder
// 與 Templates / Command Palette 共用。

/**
 * 從 spec library 完整檔名（例如 `Project_HMI_RegionA_R1_(latest)`）抽出
 * 第一個 `HMI` 標記後的可讀標籤；沒有命中模式時直接回傳原字串。
 */
export function formatSpecLibraryLabel(name: string): string {
  const matches = [...name.matchAll(/(?:^|[_\s])HMI(?=$|[_\s])/g)];
  if (matches.length === 0) return name;

  const first = matches[0];
  const firstIndex = first.index ?? 0;
  const contentStart = firstIndex + first[0].length;
  const contentEnd =
    matches[1]?.index ?? name.search(/_R\d(?:_|$)|_\([^)]*\)$/);
  const rawLabel = name.slice(
    contentStart,
    contentEnd > contentStart ? contentEnd : undefined
  );
  const label = rawLabel
    .replace(/^[_\s]+|[_\s]+$/g, "")
    .replace(/_/g, " ")
    .trim();
  return label || name;
}
