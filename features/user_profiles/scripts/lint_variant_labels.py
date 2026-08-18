#!/usr/bin/env python3
"""R-U35 (c) —— variant label 之 lint 規則，含其反向驗證（08b 作業項 4）。

## 規則

`9.3.2` 之變體覆寫（PDF p14，**xlsx 側掉句**，見 `data/xlsx_missing_clauses.tsv`）：

    ****R1 High Only: "Stellantis Account" to be replaced with "Connected Account"

**於 R1 High 適用之 TC，其字面值不得出現 `Stellantis Account`。**

§8.7.3 管轄 —— 屬**字面值錯誤**（market/variant label override），
**非風格分歧**，故違反者為 defect 而非 style-divergence。

## 為什麼這條規則存在

該覆寫**不在 xlsx Description 裡**。若生成階段只讀 xlsx（06 輪之前的作法），
`9.2` 之條文寫的是 `Stellantis Connected Account`，TC 會照抄 —— 而 R1 High
車上那個 label 是 `Connected Account`。**掉了一句註記，就寫出錯的字面值。**

## 適用範圍

`variant` 欄含 `R1 High`（或 TC 之 pre_conditions／test_item 指明 R1 High）者。
**R1 Low 不適用** —— 那些車上 label 確實是 `Stellantis Account`，
規則對它們轉紅會是誤報。

Usage:
    python3 features/user_profiles/scripts/lint_variant_labels.py          # 反向驗證
    python3 features/user_profiles/scripts/lint_variant_labels.py --check  # 掃現有 TC
"""

import argparse
import json
import re
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent

# profile 之 variant 清單（R-U35 (c)）。鍵為 variant，值為該 variant 下
# **禁止出現於字面值**之字串，及其正確替代。
VARIANT_LABEL_OVERRIDES = {
    "R1 High": [
        {"forbidden": "Stellantis Account",
         "replacement": "Connected Account",
         "source": "spec 9.3.2 (PDF p14)",
         "ruling": "R-U35 (c)",
         "why": ("該覆寫僅存於 PDF；xlsx Description 側掉句，"
                 "見 data/xlsx_missing_clauses.tsv")},
    ],
}

# 受檢之欄位 —— 字面值會被測試員讀到的那些（**含 remarks，14 輪之判定不變**）
CHECKED_FIELDS = ("tc_title", "test_item", "pre_conditions",
                  "test_procedure", "expected_result", "remarks")

# J-11（19 包）—— **variant 之判定**只掃條件陳述之欄位。
#
# 兩件事拆開：
#   判定「這條 TC 適用哪個變體」→ 只看 `pre_conditions`／`test_procedure`
#   判定「哪些欄位不得出現禁用字串」→ 仍為 CHECKED_FIELDS（含 remarks）
#
# 成因：TC-020 之 remarks 以中文討論「R1 High 之覆寫是否及於本節」，
# 被判為 R1 High —— **說明散文不是條件陳述**。
VARIANT_SCAN_FIELDS = ("pre_conditions", "test_procedure")


# N-1（14 包）—— 否定之排除。
#
# v1 只認 `R1 High` 之出現，於是「the vehicle is **not** an R1 High variant」
# 也被判為 R1 High。本批無害（該 TC 未含禁用字串），但它是**誤報源**，
# 而誤報之規則終將被關掉（R-G9 之立條理由）。
NEG_R1H = re.compile(r"\b(?:not|non|except|excluding)\s+(?:an?\s+)?"
                     r"R1\s*High\b", re.I)
POS_R1H = re.compile(r"\bR1\s*High\b", re.I)


def variant_of(tc: dict) -> str:
    """該 TC 適用之 variant。取 `variant` 欄；無則自文字推定。

    推定時**先剔除否定式**：`not an R1 High variant` 說的是它不適用，
    不是它適用。剔除後若仍有 `R1 High` 之出現才判為 R1 High。
    """
    if tc.get("variant"):
        return tc["variant"]
    blob = " ".join(str(tc.get(f, "")) for f in VARIANT_SCAN_FIELDS)
    stripped = NEG_R1H.sub(" ", blob)
    return "R1 High" if POS_R1H.search(stripped) else ""


def check_tc(tc: dict) -> list:
    """回傳違規清單。空 = 通過。"""
    v = variant_of(tc)
    out = []
    for rule in VARIANT_LABEL_OVERRIDES.get(v, []):
        for f in CHECKED_FIELDS:
            val = str(tc.get(f, ""))
            if rule["forbidden"] in val:
                out.append(
                    f"{tc.get('tc_id', '?')}.{f}: variant `{v}` 之字面值出現 "
                    f"`{rule['forbidden']}`，應為 `{rule['replacement']}` "
                    f"（{rule['source']}，{rule['ruling']}）")
    return out


# --------------------------------------------------------------- 反向驗證

def reverse_verify() -> int:
    ok = True

    def case(name, tc, expect_fail):
        nonlocal ok
        bad = check_tc(tc)
        good = bool(bad) == expect_fail
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'FAIL' if bad else 'clean'}，期望 "
              f"{'FAIL' if expect_fail else 'clean'}")
        for b in bad:
            print(f"      └ {b}")
        return good

    print("## 對照向 —— 什麼都沒做（R-G7）\n")
    case("乾淨之 R1 High TC（用正確 label）→ 不得轉紅", {
        "tc_id": "CTRL-001", "variant": "R1 High",
        "tc_title": "Connected Account routes to the Connected Profile app",
        "expected_result": "1. The Connected Account item is displayed",
    }, expect_fail=False)
    case("空 TC → 不得轉紅", {"tc_id": "CTRL-002", "variant": "R1 High"},
         expect_fail=False)

    print("\n## 注入 —— 造一條含 `Stellantis Account` 之假 TC（08b 明文）\n")
    case("R1 High ＋ ER 含禁用 label → **須 FAIL**", {
        "tc_id": "FAKE-001", "variant": "R1 High",
        "tc_title": "Edit Profile tab lists the account item",
        "expected_result": ("1. The Edit Profile tab is displayed\n"
                            "2. The Stellantis Account item is listed"),
    }, expect_fail=True)
    case("R1 High ＋ tc_title 含禁用 label → **須 FAIL**", {
        "tc_id": "FAKE-002", "variant": "R1 High",
        "tc_title": "Stellantis Account item routes to the app",
    }, expect_fail=True)
    case("variant 欄空，而文字自陳 R1 High → **須 FAIL**（推定生效）", {
        "tc_id": "FAKE-003",
        "pre_conditions": "1. The vehicle is an R1 High variant",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=True)

    print("\n## 範圍向 —— 不得誤報（規則之另一半）\n")
    case("pre-condition 為「**not** an R1 High variant」→ 不得轉紅（N-1）", {
        "tc_id": "SCOPE-003",
        "pre_conditions": "1. The vehicle is not an R1 High variant",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=False)
    case("否定與肯定並存（別條 TC 之情形）→ 仍判 R1 High → **須 FAIL**", {
        "tc_id": "FAKE-004",
        "pre_conditions": "1. The vehicle is not an R1 High variant",
        "test_procedure": "1. Repeat the step on an R1 High vehicle",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=True)
    case("**R1 Low** ＋ 同一字串 → 不得轉紅（該車上 label 確為此）", {
        "tc_id": "SCOPE-001", "variant": "R1 Low",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=False)
    case("**remarks 之中文討論**提到 R1 High → **不得**改變 variant 判定（J-11）", {
        "tc_id": "SCOPE-004",
        "pre_conditions": "1. The vehicle is in a region without the brand app",
        "remarks": "R1 High 之覆寫是否及於本節之 label 未定 —— 見上繳 18 §2.3",
        "expected_result": "1. No Stellantis Account button is shown",
    }, expect_fail=False)
    case("判定為 R1 High 後，**remarks** 之禁用字串仍轉紅（J-11 之另一半）", {
        "tc_id": "FAKE-005",
        "pre_conditions": "1. The vehicle is an R1 High variant",
        "remarks": "label 用 Stellantis Account",
    }, expect_fail=True)
    case("variant 未指明且文字未提 R1 High → 不得轉紅", {
        "tc_id": "SCOPE-002",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=False)

    n = 11
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def check_corpus() -> int:
    gen = FEATURE / "generated"
    tcs = []
    for p in sorted(gen.glob("*.json")):
        tcs += json.loads(p.read_text(encoding="utf-8")).get("tcs", [])
    if not tcs:
        print("generated/ 為空 —— 本 feature 尚未生成任何 TC（Phase 1）。"
              "規則已就位，待 Phase 2 起生效。")
        return 0
    bad = [b for tc in tcs for b in check_tc(tc)]
    print(f"掃 {len(tcs)} 條 TC，違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    sys.exit(check_corpus() if a.check else reverse_verify())
