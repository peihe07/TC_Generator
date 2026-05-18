/**
 * Word-level diff utilities used by RegenDiff.
 * 純函式、無 React 依賴，方便 unit test。
 */

export type DiffToken = { type: 'same' | 'add' | 'del'; text: string };

/**
 * 以空白 / 換行 / 常見標點為分隔符並保留之，讓差異可以 word-level 呈現
 * 而不是 char-level 或 line-level。
 */
export function tokenize(text: string): string[] {
  return text.split(/(\s+|[,.;:!?()\[\]])/).filter((t) => t !== '');
}

/**
 * 用 LCS (Longest Common Subsequence) 算出兩個字串的 word-level 差異。
 * 回傳左右兩個 token stream：
 *   - left  代表舊文本：same / del
 *   - right 代表新文本：same / add
 */
export function diffTokens(
  oldText: string,
  newText: string,
): { left: DiffToken[]; right: DiffToken[] } {
  const a = tokenize(oldText);
  const b = tokenize(newText);
  const m = a.length;
  const n = b.length;

  // dp[i][j] = LCS length of a[i..] and b[j..]
  const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }

  const left: DiffToken[] = [];
  const right: DiffToken[] = [];
  let i = 0;
  let j = 0;
  while (i < m && j < n) {
    if (a[i] === b[j]) {
      left.push({ type: 'same', text: a[i] });
      right.push({ type: 'same', text: b[j] });
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      left.push({ type: 'del', text: a[i] });
      i++;
    } else {
      right.push({ type: 'add', text: b[j] });
      j++;
    }
  }
  while (i < m) left.push({ type: 'del', text: a[i++] });
  while (j < n) right.push({ type: 'add', text: b[j++] });

  return { left, right };
}
