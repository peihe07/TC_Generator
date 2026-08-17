#!/usr/bin/env python3
"""R-U37 —— 標籤定位與相似度消歧之反向驗證（08b 作業項 3）。

## 為什麼

07 輪發現 `PRACC7.` 被 `4.7`（p6）與 `5.1`（p7）**共用**，06 輪之定位器取
第一個命中，於是把 `5.1` 對到了另一條條文。修法為「行首比對 ＋ 相似度消歧」。

**該修法之結果經人讀過認為正確，而未經注入證明。**
R-U37：注入「故意選錯」之案例，證明機制會挑對；**選錯即改判準，不改案例**。

R-G7-1 明訂對照向亦用於驗證**定位／抽取機制本身** —— 本檔即該用途。

## 判準（與 `audit_xlsx_vs_pdf.py` 共用同一段邏輯）

    一、標籤須在行首（`(?:^|\\n)\\s*<tag>\\)`）
    二、仍多於一處者，取與 xlsx 文字**相似度最高**之那一處
        （`difflib.SequenceMatcher`，`autojunk=False`，**等長窗口**，見 `locate()`）

`autojunk=False` 之必要性：Comfort 3.7.1 實測，預設之 autojunk 於長度 > 200
之序列上把出現率 > 1% 之元素當雜訊丟棄 —— 在英文段落上那是大半個字母表。

Usage:
    python3 features/user_profiles/scripts/verify_locator.py
"""

import difflib
import json
import re
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent
PDF = (FEATURE.parent.parent / "spec-index" / "sources" /
       "Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf")

IMG = re.compile(r"\(image:[^)]*\)")


def norm(s: str) -> str:
    return " ".join(IMG.sub(" ", str(s).replace("_x000D_", " ")).split())


def locate(tag: str, want: str, corpus: str):
    """定位器本體 —— 與稽核腳本同一段判準。回傳選中之 offset。

    **相似度之窗口長度須與 `want` 相同。**
    第一版取 `corpus[c:c+600]` 之前 300 字元與 `want[:300]` 比，
    兩個候選之窗口長度因而不同 —— 落在段落**前面**的候選，其窗口會把後面
    那個候選的文字一起吃進去，`SequenceMatcher` 之 ratio（2M/T）被 T 撐大而
    降低。實測：注入向「正確者在前」與「三候選正確者在中間」皆因此選錯。

    改為**等長窗口**：`corpus[c : c+len(want)]`。兩個候選拿到一樣長的窗口，
    稀釋效應消失。真實案例（`PRACC7.` 之兩處）在兩版判準下皆選對 ——
    **那正是為什麼它需要注入才驗得出來**：語料剛好不會踩到這個缺陷。
    """
    cands = [m.start() for m in
             re.finditer(r"(?:^|\n)\s*" + re.escape(tag) + r"\)", corpus)]
    if not cands:
        cands = [m.start() for m in re.finditer(re.escape(tag) + r"\)", corpus)]
    if not cands:
        return None, 0
    if len(cands) == 1:
        return cands[0], 1
    best = max(cands, key=lambda c: difflib.SequenceMatcher(
        None, want, norm(corpus[c:c + len(want) + 40])[:len(want)],
        autojunk=False).ratio())
    return best, len(cands)


def main() -> int:
    import fitz
    doc = fitz.open(PDF)
    full = "\n".join(doc[i].get_text() for i in range(doc.page_count))
    by = json.loads((FEATURE / "data" / "outline_map.json").read_text("utf-8"))

    ok = True

    def case(name, tag, want, corpus, expect_offset, expect_n=None):
        nonlocal ok
        got, n = locate(tag, norm(want), corpus)
        good = (got == expect_offset) and (expect_n is None or n == expect_n)
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}"
              f"   候選 {n} 個，選中 offset {got}"
              + ("" if good else f"，期望 {expect_offset}"))
        return good

    # ---------------- 對照向（R-G7 / R-G7-1）------------------------------
    print("## 對照向 —— 什麼都沒做\n")
    uniq_tag = "PVALSPK1."
    want = by["13.1"]["text"]
    pos = [m.start() for m in
           re.finditer(r"(?:^|\n)\s*" + re.escape(uniq_tag) + r"\)", full)]
    case("唯一命中之標籤 → 不觸發消歧，選中該處", uniq_tag, want, full,
         pos[0], expect_n=1)
    # 同一段落原樣複製一份語料，結果須不變
    case("語料原樣（未注入）→ 選中同一 offset", uniq_tag, want, full, pos[0])

    # ---------------- 真實案例：PRACC7. 之兩處 ----------------------------
    print("\n## 真實案例 —— `PRACC7.` 為 `4.7`／`5.1` 共用\n")
    hits = [m.start() for m in
            re.finditer(r"(?:^|\n)\s*" + re.escape("PRACC7.") + r"\)", full)]
    print(f"  行首命中 {len(hits)} 處：offset {hits}")
    # 4.7 之內文為導航路線；5.1 之內文為兩分頁
    case("`4.7`（導航路線）→ 須選中前者", "PRACC7.", by["4.7"]["text"],
         full, hits[0], expect_n=2)
    case("`5.1`（兩分頁）→ 須選中後者", "PRACC7.", by["5.1"]["text"],
         full, hits[1], expect_n=2)

    # ---------------- 注入：人工構造之近似段落 ----------------------------
    #
    # 兩個注入方向都要，才排除「機制其實只是總是選最後／最前一個」。
    print("\n## 注入 —— 人工構造之近似段落（兩個方向）\n")
    TAG = "ZZTEST1."
    true_text = ("ZZTEST1.) The system shall display the Valet Mode icon in "
                 "the status bar whenever Valet Mode is active, and shall "
                 "remove it upon deactivation.")
    decoy = ("ZZTEST1.) The system shall display the Profile avatar in the "
             "status bar whenever a Profile is active, and shall replace it "
             "upon switching.")
    want_true = norm(true_text)

    corpus_a = f"HEAD A\n{decoy}\nMIDDLE\n{true_text}\nTAIL"
    off_true_a = corpus_a.index(true_text) - 1      # 前一字元為 \n
    case("正確者在**後** → 須選後者（非『總是選第一個』）",
         TAG, want_true, corpus_a, off_true_a, expect_n=2)

    corpus_b = f"HEAD B\n{true_text}\nMIDDLE\n{decoy}\nTAIL"
    off_true_b = corpus_b.index(true_text) - 1
    case("正確者在**前** → 須選前者（非『總是選最後一個』）",
         TAG, want_true, corpus_b, off_true_b, expect_n=2)

    # 三個候選，正確者夾在中間
    corpus_c = f"H\n{decoy}\nM1\n{true_text}\nM2\n{decoy}\nT"
    off_true_c = corpus_c.index(true_text) - 1
    case("三個候選，正確者在中間 → 須選中間",
         TAG, want_true, corpus_c, off_true_c, expect_n=3)

    # ---------------- 行首規則：`Table CPA2.)` 之內含不得命中 -------------
    print("\n## 行首規則 —— 內含命中須被排除\n")
    inline = "See table CPA2.) for list items."
    real = "CPA2.) [This whole note is not applicable for R1 H] Clicking on the info icon."
    corpus_d = f"H\n{inline}\nM\n{real}\nT"
    off_real = corpus_d.index(real) - 1
    case("`Table CPA2.)` 之內含不得被選中 → 須選行首之真條款",
         "CPA2.", norm(real), corpus_d, off_real, expect_n=1)

    # ---------------- 判準之界線，據實記 ----------------------------------
    print("\n## 判準之界線（不標 PASS —— 這些是本機制**做不到**的事）\n")
    near = ("ZZTEST1.) The system shall display the Valet Mode icon in the "
            "status bar whenever Valet Mode is active, and shall remove it "
            "upon deactivating.")          # 僅末字不同
    corpus_e = f"H\n{true_text}\nM\n{near}\nT"
    got, n = locate(TAG, want_true, corpus_e)
    picked_first = got == corpus_e.index(true_text) - 1
    print(f"  未實測 — 兩候選僅差一個字（`deactivation` vs `deactivating`）："
          f"本機制選中{'前者（正確）' if picked_first else '**後者（錯）**'}，"
          f"惟其正確與否取決於該字之權重，**非本機制所能保證**。"
          f"語料中無此形態（實測重複標籤僅 3 處且內容迥異），故不作閘。")

    n_cases = 8
    print(f"\n{n_cases if ok else '<' + str(n_cases)} / {n_cases} "
          f"directional cases {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
