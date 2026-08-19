#!/usr/bin/env python3
"""交付欄位之內部字樣掃描（48 包 §1.2）＋ **中文詞界之判準檢查**（G-I，49 包）。

## 為什麼要有這支

48 輪之交付欄位淨化是**臨時腳本**跑的 —— 跑完就只留在那一輪的輸出裡。
**一個只存在於某一輪 shell 歷史裡的檢查，下一輪沒有人會再跑它。**
本檔把它變成常設閘。

## G-I：`\\b` 對中文不成立

48 輪之語料側掃描用 `\\b(pending|TBD|待判|未決)\\b`，回報「命中 2」；
而 `TC-082` 之「上游**未決**事項」**沒有被抓到** ——
`\\b` 是 ASCII 詞界，中文字兩側不構成詞界，該詞永遠比不到。
它是在掃**產出檔**時（那次沒加 `\\b`）才浮出來的。

> **凡判準含 `\\b` 而其詞表有非 ASCII 者，一律改以
> `(?<![\\u4e00-\\u9fff])`／字串包含判定，並附中文命中之方向性案例。**

**本檔之 DF-2 是該規則之機械化**：它不是宣稱「我們沒用 `\\b`」，
而是**對詞表中每個中文詞造一個「夾在中文裡」之探針句，實測其可被命中**。
判準若退回 `\\b`，DF-2 立刻轉紅。

## 兩項

| # | 檢查 | 性質 |
|---|---|---|
| DF-1 | 交付欄位不得含內部狀態字樣／來源類別標記 | 紅 |
| DF-2 | 詞表中每個**非 ASCII** 詞，其判準須能命中「夾在中文裡」之出現 | 紅 |

## 盲區（R-G11）

1. **詞表是枚舉**（G-B 之同型風險）。新的內部字樣若不入表，本檔看不到它。
   **本檔不對詞表自身做對照** —— 其母體（「什麼算內部字樣」）無法自 spec 側重算。
2. **只掃我方所寫之 14 欄**（`COLS`）。母本原有之表頭與樣式不在射程內。
3. **不判「內部指涉」**（`§8.4.1`／`R-U56`／輪次包號）—— 那六類承載覆核依據，
   其去留屬交付形式之裁示（49 包 §二），不是本檔之事。

Usage:
    python3 scripts/audit_delivery_fields.py
    python3 scripts/audit_delivery_fields.py --self-test
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent

# 我方所寫之交付欄位（`write_back.COLS` 之值域）
COLS = ("req_id", "tc_id", "test_group", "test_set", "test_item",
        "pre_conditions", "input_test_data", "test_procedure",
        "expected_result", "specification_reference", "priority",
        "design_method", "functional_safety", "remarks")

# 內部字樣之詞表。**中英混列，故不得用 `\b`。**
#   ascii  —— 以 `(?<![A-Za-z])…(?![A-Za-z])` 作詞界（等價於 `\b` 而不牽涉 CJK）
#   cjk    —— **字串包含判定**（中文無詞界可言）
BANNED_ASCII = ("pending", "TBD", "TODO", "FIXME", "XXX")
BANNED_CJK = ("待判", "未決", "暫定", "待補", "內部用")
BANNED_TAG = r"\[(?:spec-derived|inferred|assumed|derived|internal)\]"


def _ascii_re(word: str) -> re.Pattern:
    return re.compile(rf"(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])", re.I)


def _cjk_re(word: str) -> re.Pattern:
    """**不加詞界。** 中文字兩側不構成 `\\b`，加了等於關掉這條規則。"""
    return re.compile(re.escape(word))


def patterns() -> list:
    out = [(w, _ascii_re(w), "ascii") for w in BANNED_ASCII]
    out += [(w, _cjk_re(w), "cjk") for w in BANNED_CJK]
    out += [("[來源類別標記]", re.compile(BANNED_TAG, re.I), "tag")]
    return out


def corpus() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append(t)
    return out


def audit(rows=None, pats=None) -> list:
    rows = corpus() if rows is None else rows
    pats = patterns() if pats is None else pats
    bad = []

    # ── DF-1
    for t in rows:
        for fld in COLS:
            v = str(t.get(fld, "") or "")
            if not v:
                continue
            for word, rx, kind in pats:
                m = rx.search(v)
                if m:
                    i = m.start()
                    bad.append(f"DF-1 {t.get('tc_id', '?')}（{fld}）: "
                               f"內部字樣 `{word}` → 「…"
                               f"{v[max(0, i - 24):m.end() + 20]}…」")

    # ── DF-2 —— **G-I 之機械化**：對每個中文詞造「夾在中文裡」之探針
    for word, rx, kind in pats:
        if kind != "cjk":
            continue
        probe = f"本條之上游{word}事項尚待處理"
        if not rx.search(probe):
            bad.append(f"DF-2 中文詞 `{word}` 之判準**命中不到夾在中文裡之出現** "
                       f"→ 探針「{probe}」—— 判準若含 `\\b` 即為此形態（G-I）")
    return bad


def self_test() -> int:
    rows, pats = corpus(), patterns()
    ok, cases = True, []

    def case(name, fn, expect_red):
        nonlocal ok
        cases.append(name)
        bad = fn()
        good = bool(bad) == expect_red
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        for b in bad[:2]:
            print(f"      └ {b}")

    case("現行語料 → 綠", lambda: audit(rows, pats), False)

    # **48 輪之漏網形態** —— 中文夾中文
    case("**注入：`TC-082` 之原形「上游未決事項」（中文夾中文）→ 紅**",
         lambda: audit([{"tc_id": "FAKE-082",
                         "remarks": "**本批唯一帶上游未決事項生成者（R-U27）**："
                                    "DR #4 所缺為 popup 內文"}], pats), True)

    case("注入：英文之 `pending`（48 輪抓得到之形態）→ 紅",
         lambda: audit([{"tc_id": "FAKE-1",
                         "remarks": "由 `pending` 改為具名不配"}], pats), True)

    case("注入：來源類別標記 `[spec-derived]` → 紅",
         lambda: audit([{"tc_id": "FAKE-2",
                         "input_test_data": "Value [spec-derived]"}], pats),
         True)

    # ── DF-2 —— **本組最關鍵**：把中文詞之判準退回 `\b`
    def regressed():
        bad_pats = [(w, re.compile(rf"\b{re.escape(w)}\b"), k)
                    if k == "cjk" else (w, rx, k) for w, rx, k in pats]
        return audit(rows, bad_pats)
    case("**DF-2 注入：中文詞之判準退回 `\\b…\\b` → 紅**（G-I 之形態本身）",
         regressed, True)

    # 護欄：形近而不在詞表者
    case("**護欄**：「未定」不在詞表 → 綠（詞表是枚舉，盲區 1 已具名）",
         lambda: audit([{"tc_id": "FAKE-3",
                         "remarks": "兩者之關係條文未定"}], pats), False)

    # 護欄：`pending` 為英文單字之一部分
    case("**護欄**：`appending`／`impending` 不得誤判 → 綠",
         lambda: audit([{"tc_id": "FAKE-4",
                         "remarks": "appending a row; impending change"}],
                       pats), False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    rows = corpus()
    bad = audit(rows)
    print(f"語料 {len(rows)} 條 × 交付欄位 {len(COLS)} 欄 = "
          f"{len(rows) * len(COLS)} 格；詞表 "
          f"{len(BANNED_ASCII)} 英 ＋ {len(BANNED_CJK)} 中 ＋ 1 標記\n")
    print(f"違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
