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

# 受檢之欄位 —— 字面值會被測試員讀到的那些
CHECKED_FIELDS = ("tc_title", "test_item", "pre_conditions",
                  "test_procedure", "expected_result", "remarks")


def variant_of(tc: dict) -> str:
    """該 TC 適用之 variant。取 `variant` 欄；無則自文字推定。"""
    if tc.get("variant"):
        return tc["variant"]
    blob = " ".join(str(tc.get(f, "")) for f in CHECKED_FIELDS)
    return "R1 High" if re.search(r"\bR1\s*High\b", blob) else ""


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
    case("**R1 Low** ＋ 同一字串 → 不得轉紅（該車上 label 確為此）", {
        "tc_id": "SCOPE-001", "variant": "R1 Low",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=False)
    case("variant 未指明且文字未提 R1 High → 不得轉紅", {
        "tc_id": "SCOPE-002",
        "expected_result": "1. The Stellantis Account item is listed",
    }, expect_fail=False)

    n = 7
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
