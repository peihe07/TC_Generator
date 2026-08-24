#!/usr/bin/env python3
"""R-PMH64 —— 質疑型條文之母體，由判準自 `RULINGS.md` 產生，不得人工挑選。

R-PMH62 要求「提出某一判準以質疑某項結論時，須將同一判準回頭套用於
支持該質疑之其他項」。**其回溯之母體先前為人工挑選**（16 包只查了四條，
而執行層自陳「沒有一個可以自動判定哪些條文屬於質疑型之判準」）。

本檔實施 R-PMH64 之判準：條文含下列任一標記者，即列為**候選**。
**判準會有偽陽**（條文僅引他處之錯為例證者），故其輸出為候選清單，
逐條由人確認 —— 與 `VERDICT` 之處理相同（R-PMH57／R-PMH61）。

**候選數為 0 者視為判準失效**，不得視為「無質疑型條文」。

用法:
    python scripts/challenge_rulings.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULINGS = ROOT / "RULINGS.md"

# R-PMH64 逐字之標記清單
MARKS = ["不成立", "作廢", "撤回", "改判", "取代", "推翻", "未套用", "誤用",
         "判錯", "不符", "矛盾", "之錯", "之缺陷", "之瑕疵"]
MARK_RE = [(m, re.compile(re.escape(m))) for m in MARKS]
MARK_RE.append(("由…查出", re.compile(r"由.{0,20}查出")))

LIMITS = [
    "**判準為字面標記，不判語意** —— 條文僅引他處之錯為例證者會被列為候選（偽陽），"
    "反之以其他措詞表達之質疑（如「其依據更換如下」）不會命中（偽陰）",
    "只掃 `RULINGS.md` 之 fenced block；**`ANOMALIES.md`／`DECISIONS.md` 之判斷不入母體**",
    "**只判定「是否為質疑型」，不判定「其是否已被雙向自套」** —— 後者須人讀",
    "R-G 系列（跨 feature 通則）不在本檔範圍 —— 其存於他處",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def rulings() -> list[tuple[str, str]]:
    """回傳 [(條號, 條文全文)]，自 fenced block 抽出。"""
    txt = RULINGS.read_text(encoding="utf-8")
    out = []
    for b in re.findall(r"```\n(.*?)\n```", txt, re.S):
        m = re.match(r"(R-[A-Z]+\d+[a-z]?)（", b)
        if m:
            out.append((m.group(1), b))
    return out


def main() -> None:
    rs = rulings()
    hits = []
    for cid, body in rs:
        found = sorted({name for name, rx in MARK_RE if rx.search(body)})
        if found:
            hits.append((cid, found, body))
    print("=== 質疑型條文之候選清單（R-PMH64）===")
    print(f"`RULINGS.md` 之條文總數 = **{len(rs)}**；"
          f"判準標記 = {len(MARK_RE)} 個；**候選 = {len(hits)}**")
    print(f"命中率 = {len(hits)/len(rs):.1%}\n")
    print(f"{'條號':<10} 命中之標記")
    for cid, found, _ in hits:
        print(f"{cid:<10} {'／'.join(found)}")
    if not hits:
        print("\n**候選數為 0 —— 依 R-PMH64 視為判準失效**，"
              "不得視為「無質疑型條文」。")
    print_limits()
    sys.exit(1 if not hits else 0)


if __name__ == "__main__":
    main()
