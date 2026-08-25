#!/usr/bin/env python3
"""22 包步驟 7 —— 停止條件 8 之**偽陰抽樣**（R-PMH67）。

21 包之停止條件 8 為：「步驟 2 之重記後，仍有任一項記為
**『無矛盾』或『非牴觸』**」—— **列舉式判準，只攔兩個詞**。
21 包 §6 之自檢已具名該弱點：**若改寫成「相容」「未發現問題」，本條攔不下。**

R-PMH67 要求列舉式判準附偽陰之抽樣估計：
自**未被該判準攔下**之母體隨機抽 N >= 10，人讀判其是否「應被攔而未被攔」，
命中數即偽陰率之估計，**與判準、偽陽數及 Wilson 區間一併回報**。

母體：`docs/upstream/*.md` 中含「對照結論型措詞」而**不含該二詞**之行。

================================================================================
**⚠ 本檔自 24 包起停用（R-PMH91）**
================================================================================

**停用之理由**：本檔之形態為**攔截式列舉** —— 攔「無矛盾」「非牴觸」二詞，
並以抽樣估其偽陰率。**兩層抽樣之偽陰率為 10% → 20%，未見收斂**，
且其漏網者「**非漏**」正是 `RESIDUE_VERDICT` 20 條中**最常用之起首詞**
（23 包 §7.2）。

**補上「非漏」只會使本檢查再通過一次，然後在下一個措詞上再漏一次。**

**取代者**：`scripts/verdict_form.py` —— **正向**檢查
「對照結論是否以四詞之一（`牴觸`／`印證`／`未對照`／`待定義`）作結」。
其判準與母體皆非列舉：四詞由 R-PMH79／R-PMH85 定義；
母體為各檢查之**判定表**，其每一項依構造即為一個對照結論。

**本檔不刪**（其兩層抽樣之數據為 R-PMH91 之立條依據），
**執行時拒跑並印本說明**；`--acknowledge-deprecated` 可強制執行，
**其輸出不得引為結論**。

用法:
    python scripts/wording_sample.py --acknowledge-deprecated
"""
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from challenge_rulings import wilson          # noqa: E402  —— 19 包所建，不另維護副本

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "docs" / "upstream"

CAUGHT = ["無矛盾", "非牴觸"]                    # 停止條件 8 所攔者
CANDIDATE = ["一致", "相容", "符合", "吻合", "不衝突", "無衝突",
             "無牴觸", "未發現問題"]              # 可能之同義措詞（**本身亦為列舉**）

# --- 第二層（23 包步驟 7）---
# 22 §12 第 5 項自陳：`CANDIDATE` 之八詞**本身是列舉**，其外之措詞不入母體，
# **故本抽樣之母體亦有偽陰**。第二層即量該層之偽陰。
#
# 第二層母體之界定**仍須某種識別方式** —— 此處取「對照語境之標記」
# （`矩陣`／`規格`／`素材`／`vs`／`×`／`謂詞`）而**不含** `CAUGHT + CANDIDATE`
# 之十詞者。**該識別方式本身又是列舉 —— 第三層未量，已具名。**
CONTEXT = ["矩陣", "規格", "素材", " vs ", " × ", "謂詞", "State Matrix"]

SAMPLE_N = 10
SAMPLE_SEED = 22                                # = 本包編號，可重現

LIMITS = [
    "**母體之界定本身是列舉** —— `CANDIDATE` 之八詞為人工列舉，"
    "其外之措詞（如「二者並存」「無此問題」）不入母體，**故本抽樣之母體亦有偽陰**",
    "只掃 `docs/upstream/*.md`；`ANOMALIES.md`／`DECISIONS.md`／程式輸出不入母體",
    "**行級抽樣** —— 一行可能同時是對照結論與別的敘述；其是否為「對照結論」由人讀判",
    "N = 10 之 Wilson 區間寬達數十個百分點 —— **點估計不得單獨引用**",
    "⚠ **母體隨每包新增之上繳文件而變** —— 種子固定**不保證樣本固定**："
    "22 包之母體為 124 行，23 包已為 130 行，抽樣遂全數更換。"
    "**故本檔之抽樣結果須與其執行時之母體大小併讀。**",
    "**第二層之母體亦以列舉界定**（`CONTEXT` 六個標記）—— **第三層未量**；"
    "R-PMH67 之形態在此只套了兩層，其收斂與否未知",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


# 抽樣之人讀判定 —— 鍵為 (檔名, 行號)
SAMPLE_VERDICT_L2: dict[tuple[str, int], tuple[bool, str]] = {
    ("03_testgroup_and_dv.md", 182):
        (True, "**應被攔** —— 此為**對照結論**（`Pairwise / t-wise` vs `Pair-wise / N-wise` 兩組字串）而以「**未造成任何逸出**」作結。該措詞不在八個候選詞內，**亦不在停止條件 8 之二詞內**"),
    ("11_claim_evidence.md", 34):
        (False, "R-PMH41 之命中數驗證，非對照結論"),
    ("13_batch1_rework.md", 365):
        (False, "自問表之合規判定（「是否越界 §8.4.2」→「否」），非規格×素材之對照"),
    ("15_marker_prefix_and_priority.md", 51):
        (False, "規則之敘述（未在表中 → FAIL），非對照結論"),
    ("18_break_the_circle.md", 107):
        (True, "**應被攔，且為本層最重要之一項** —— 此為 `RESIDUE_VERDICT` 之**對照結論**（PDF vs SYS1）而以「**非漏（散文側）**」作結。**「非漏」是一整類對照結論之措詞，而停止條件 8 完全攔不到** —— `RESIDUE_VERDICT` 現有 20 條，其中多數以「非漏」起首"),
    ("19_broken_source.md", 218):
        (False, "敘述性文字（`-layout` 之交錯現象），非對照結論"),
    ("20_matrix_scope.md", 256):
        (False, "程式輸出之同值查核（`48/48`），identity"),
    ("21_predicate_criterion.md", 61):
        (False, "章節標題"),
    ("22_popup_conflict.md", 184):
        (False, "must-hit 錨點之**謂詞**陳述；其記法（牴觸）在別行，已被三分類涵蓋"),
    ("22_popup_conflict.md", 188):
        (False, "同上"),
}

SAMPLE_VERDICT: dict[tuple[str, int], tuple[bool, str]] = {
    ("02_baseline_switch.md", 121):
        (True, "**應被攔** —— 此為**對照結論**（037 之 `Priority` 實測值 vs `High` 等）而以「二者一致」作結。其後接「本包未實測母本」—— **一個以「一致」作結而其一造未實測之陳述**"),
    ("03_testgroup_and_dv.md", 349):
        (False, "章 ↔ FROP 之**分布統計**（「完全一致區」），非規格×素材之對照結論"),
    ("05_corpus_fix_and_framework_prep.md", 472):
        (False, "Pei 裁定之逐字引述（「037 的報告命名不一致…」），非本層之對照結論"),
    ("06_framework_proposal.md", 312):
        (False, "待決事項之敘述（「是否須一致、由誰主導，**未查**」）—— **其自陳未查，未以「一致」作結**"),
    ("11_claim_evidence.md", 30):
        (False, "抄錄核對表之條文主旨欄（R-PMH43 之描述），非對照結論"),
    ("14_marker_enumeration.md", 211):
        (False, "程式輸出之**同值查核**（`八條全部一致: True`），identity"),
    ("15_marker_prefix_and_priority.md", 279):
        (False, "節標題（「一致性自檢已落為程式之固定步驟」）"),
    ("15_marker_prefix_and_priority.md", 409):
        (False, "程式輸出之同值查核（靜態彙集 vs 執行期），identity"),
    ("19_broken_source.md", 95):
        (False, "停止條件之**自檢**敘述（字面與目的不一致），非規格×素材之對照"),
    ("21_predicate_criterion.md", 50):
        (False, "**重記表之「原記」欄** —— 其「一致（軸層面）」正是被本表改判為「未對照」者。**該行本身即是更正之記錄，不是仍在流通之結論**"),
}


def population(layer: int = 1) -> list[tuple[str, int, str]]:
    out = []
    for f in sorted(UPSTREAM.glob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if any(c in line for c in CAUGHT):
                continue                       # 已被停止條件 8 攔下者不入母體
            if layer == 1:
                if any(c in line for c in CANDIDATE):
                    out.append((f.name, i, line.strip()))
            else:
                # 第二層：**不含**八個候選詞，惟具對照語境之標記
                if any(c in line for c in CANDIDATE):
                    continue
                if any(c in line for c in CONTEXT) and len(line.strip()) >= 20:
                    out.append((f.name, i, line.strip()))
    return out


DEPRECATED = True


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--acknowledge-deprecated", action="store_true",
                    help="強制執行已停用之本檔；其輸出不得引為結論（R-PMH91）")
    ap.add_argument("--layer2", action="store_true",
                    help="23 包步驟 7 —— 第二層抽樣（母體為不含八候選詞者）")
    a = ap.parse_args()
    if DEPRECATED and not a.acknowledge_deprecated:
        print(__doc__)
        print("**拒跑** —— 本檔已停用（R-PMH91）。"
              "請改用 `scripts/verdict_form.py`。")
        sys.exit(2)
    layer = 2 if a.layer2 else 1
    verdicts = SAMPLE_VERDICT_L2 if layer == 2 else SAMPLE_VERDICT
    seed = SAMPLE_SEED + (100 if layer == 2 else 0)
    pop = population(layer)
    print(f"=== 停止條件 8 之偽陰抽樣 —— **第 {layer} 層**（R-PMH67）===")
    print(f"停止條件 8 所攔之詞：{CAUGHT}（**2 個**）")
    if layer == 1:
        print(f"母體：`docs/upstream/*.md` 中含 {CANDIDATE} 之一"
              f"**而不含上列二詞**之行 = **{len(pop)}**")
    else:
        print(f"**第二層母體**：**不含**上列二詞**亦不含** {CANDIDATE} 八詞，"
              f"惟具對照語境標記 {CONTEXT} 之一且長度 >= 20 之行 = **{len(pop)}**")
        print("  ⚠ **該識別方式本身又是列舉** —— 第三層未量，已具名於 LIMITS。")
    rng = random.Random(seed)
    n = min(SAMPLE_N, len(pop))
    sample = sorted(rng.sample(pop, n))
    print(f"抽樣 N = {n}；種子 = {seed}"
          f"（`random.Random({seed}).sample`，**可重現**）\n")
    named, pos = 0, 0
    for f, i, line in sample:
        v = verdicts.get((f, i))
        print(f"  {f}:{i}")
        print(f"    {line[:150]}")
        if v is None:
            print("    **人讀判定：未具名 ← 抽樣未完成**")
            continue
        named += 1
        pos += 1 if v[0] else 0
        print(f"    {'**應被攔**' if v[0] else '不應被攔'} —— {v[1]}")
    if named == n:
        lo, hi = wilson(pos, n)
        print(f"\n  **偽陰率之點估計 = {pos}/{n} = {pos/n:.0%}**；"
              f"**Wilson 95% 區間 = [{lo:.0%}, {hi:.0%}]**")
        print(f"  推估母體 {len(pop)} 行中應被攔者："
              f"點估計 **{round(len(pop)*pos/n)}** 行，"
              f"**區間 [{round(len(pop)*lo)}, {round(len(pop)*hi)}] 行**")
    else:
        print(f"\n  **抽樣未完成：{n - named} 行未具名人讀判定**")
    print_limits()
    sys.exit(0 if named == n else 1)


if __name__ == "__main__":
    main()
