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
import math
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULINGS = ROOT / "RULINGS.md"

# R-PMH64 逐字之標記清單
MARKS = ["不成立", "作廢", "撤回", "改判", "取代", "推翻", "未套用", "誤用",
         "判錯", "不符", "矛盾", "之錯", "之缺陷", "之瑕疵",
         # --- R-PMH67（18 包）補列：實測偽陰 R-PMH20（「實測全簿為 5 組**而非**
         #     4 組」）未命中，同型可疑者 R-PMH21（「**非**內容差異」）---
         "而非", "並非", "過時", "失效", "無來源", "湊得"]
MARK_RE = [(m, re.compile(re.escape(m))) for m in MARKS]
MARK_RE.append(("由…查出", re.compile(r"由.{0,20}查出")))

# R-PMH67 —— 偽陰之抽樣估計。**補標記不構成本條之滿足**：
# 補完之後仍無人知道還有多少種措詞未被列舉（此即列舉式判準之形態，
# 在本 repo 已第四次出現）。抽樣之作用不在補齊，
# **在於使「不知道還漏多少」變成一個有數字之陳述**。
SAMPLE_N = 10
SAMPLE_SEED = 18          # = 本包編號，固定值，**抽樣可重現**

# 抽樣之人讀判定（R-PMH67）—— 逐條具名，供重跑時比對
SAMPLE_VERDICT: dict[str, tuple[bool, str]] = {
    # --- 19 包：母體由 68 增為 75 條，抽樣重抽，新增四條之判定 ---
    "R-PMH19":
        (False, "定義型 —— 定「已交付件」語料之母體判準；其 (a) 後由 R-PMH24 撤回，**本條為被質疑者而非質疑者**"),
    "R-PMH54":
        (True, "**質疑型（偽陰）** —— 把 13 包之句級雙向 diff **降為輔助**，理由為 marker 枚舉「無門檻、無取樣、無相似度參數」而句級 diff 有。**未命中之因：措詞為「降為輔助」「不受任何可調參數之影響」，無 21 標記中之任一詞**"),
    "R-PMH56":
        (True, "**質疑型（偽陰）** —— 其依據逐節指認 13 包所具名之未涵蓋清單漏列七節，且「漏列使『已具名』產生虛假之完整感」。**未命中之因：措詞為「漏列」「虛假之完整感」，而標記中無「漏列」**"),
    "R-PMH73":
        (False, "新裁定型 —— Pei 提供素材、定其效力；不推翻既有結論。（**其結論之前提於本包實測不成立，見 A-PMH18 —— 惟那是本包之發現，不是本條自身之質疑**）"),
    # --- 18 包之判定（其中六條仍在本輪樣本內） ---
    "R-PMH4":
        (False, "定義型 —— 定「到齊」之定義並排除較弱判準（檔名相符／大小相同），未推翻任何既有結論"),
    "R-PMH6":
        (False, "延後處置型 —— 登記 G/H 兩欄現況（H 欄違 canon §4.2）並禁止 Phase 0/1 改動，不推翻既有裁定"),
    "R-PMH7":
        (False, "新裁定型 —— 定交付基底並給辨識判準；其所引發之作廢由 R-PMH8／R-PMH9 執行，本條自身不質疑"),
    "R-PMH11":
        (False, "要求型 —— 其所指定之實施方式後被 R-PMH15 推翻，故本條為**被質疑者**而非質疑者"),
    "R-PMH18":
        (False, "防禦型 —— 預先禁止一個尚未發生之處理（把兩常數統一），非推翻既有結論"),
    "R-PMH25":
        (True, "**質疑型（偽陰）** —— 推翻「以分頁名認 DV source」之做法，依據為實測：客戶那份之 x14 指向 `Reference!$C$4:$C$12`，`下拉選單` 為孤兒分頁。「以分頁名認 source 會取到未生效之清單」即其結論。**未命中之因：全條無 21 個標記中之任一詞**"),
    "R-PMH29":
        (True, "**質疑型（偽陰）** —— 駁斥「以『測了會有併入之誘惑』為由不測」之理由，並禁止任選一案與擱置。**未命中之因：其反駁以「會讓一個可關閉之不確定性繼續開著」表達**"),
    "R-PMH34":
        (True, "**質疑型（偽陰）** —— 其依據逐字指認 07 包上繳之分母有二錯（0 列工作簿計入、兩候選重複計入）。**未命中之因：措詞為「重複計算」「看起來比實際強」**"),
    "R-PMH35":
        (True, "**質疑型（偽陰）** —— 其依據指認 07 包 §三之六列皆 must-not-hit、門檻不可執行、對 Q11 無鑑別力。**未命中之因：措詞為「不構成門檻」「無法區分」「無鑑別力」**"),
    "R-PMH40":
        (True, "**質疑型（偽陰）** —— 「兩份獨立維護之副本**一律視為缺陷**」，依據為 08 包自陳。**未命中之因：「視為缺陷」不在標記內，而「之缺陷」在**（差一個「之」）"),
}

LIMITS = [
    "**判準為字面標記，不判語意** —— 條文僅引他處之錯為例證者會被列為候選（偽陽），"
    "反之以其他措詞表達之質疑（如「其依據更換如下」）不會命中（偽陰）",
    "只掃 `RULINGS.md` 之 fenced block；**`ANOMALIES.md`／`DECISIONS.md` 之判斷不入母體**",
    "**只判定「是否為質疑型」，不判定「其是否已被雙向自套」** —— 後者須人讀",
    "R-G 系列（跨 feature 通則）不在本檔範圍 —— 其存於他處",
    "**抽樣只估偽陰率，不消滅偽陰** —— 抽中之 10 條外仍可能有質疑型條文未命中",
    "**N = 10 之 Wilson 區間寬達 60 個百分點** —— 區間本身即本檢查之限度；欲收窄須加大 N，本檢查不自行加大",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson 95% 信賴區間（19 包步驟 7）。

    18 §11 第 4 項之自陳：點估計「**使該數字看起來比它應有的樣子確定**」。
    N = 10 之樣本，其區間寬得足以改變結論之性質，故每次執行皆帶區間。
    """
    if n == 0:
        return (0.0, 1.0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


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

    # --- R-PMH67：自**未命中**之母體隨機抽樣，供人讀估偽陰率 ---
    miss = [(cid, body) for cid, body in rs
            if cid not in {c for c, _, _ in hits}]
    rng = random.Random(SAMPLE_SEED)
    n = min(SAMPLE_N, len(miss))
    sample = rng.sample(miss, n)
    print(f"\n=== 偽陰之抽樣（R-PMH67）===")
    print(f"未命中母體 = {len(miss)} 條；抽樣 N = {n}；"
          f"種子 = {SAMPLE_SEED}（`random.Random({SAMPLE_SEED}).sample`，**可重現**）")
    print("**逐條由人讀判其是否應命中**；命中數即偽陰率之估計。\n")
    named, pos = 0, 0
    for cid, body in sorted(sample):
        v = SAMPLE_VERDICT.get(cid)
        first = body.split("\n")[0]
        print(f"  {cid:<10} {first[:64]}")
        if v is None:
            print("     **人讀判定：未具名 ← 抽樣未完成（R-PMH67）**")
            continue
        named += 1
        pos += 1 if v[0] else 0
        print(f"     {'**應命中**' if v[0] else '不應命中'} —— {v[1]}")
    if named == n:
        lo, hi = wilson(pos, n)
        print(f"\n  **偽陰率之點估計 = {pos}/{n} = {pos/n:.0%}**；"
              f"**Wilson 95% 區間 = [{lo:.0%}, {hi:.0%}]**")
        print(f"  推估未命中母體 {len(miss)} 條中之質疑型："
              f"點估計 **{round(len(miss)*pos/n)}** 條，"
              f"**區間 [{round(len(miss)*lo)}, {round(len(miss)*hi)}] 條**")
        print(f"  即真正之質疑型條文約 {len(hits)}（候選，含偽陽）"
              f" ＋ [{round(len(miss)*lo)}, {round(len(miss)*hi)}]（未命中之推估）")
        print(f"  **N = {n} 之區間寬達 {hi-lo:.0%}** —— "
              "點估計不得單獨引用（R-PMH67／18 §11 第 4 項）。")
    else:
        print(f"\n  **抽樣未完成：{n - named} 條未具名人讀判定**")
    print_limits()
    sys.exit(1 if not hits else 0)


if __name__ == "__main__":
    main()
