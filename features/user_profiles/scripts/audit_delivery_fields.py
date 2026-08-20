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


# ── TI-1／TI-2／TI-3（55 包）—— `Test Item` 之兩段結構
#
# **成因不是漏跑，是規格從未落檔。** canon §4.3 之標題逐字為
# `Test Item / tc_title — three acceptable shapes`，即 canon **把兩者視為同一物**；
# 本 feature 之 `R-U6` 與 `G3` 據此把 `test_item` 綁定為 `tc_title`，
# 而 **Comfort 與 Home 之交付件皆為兩段式**（55 輪唯讀實測）——
# 規則只存在於產物，不存在於文字。
#
# 規格（Pei 2026-08-19 確認，55 包 §一）：
#
#     <tc_title>
#     (<一句：本條在測什麼>)
#
# 第二段之來源為該條 `reasoning` 之「驗證目標」句改寫為英文（§1.2），
# **不另行構思** —— 故其正確性已由 189 條之覆核背書。
TI_MODAL = re.compile(r"\b(shall|will|should|would|must|may)\b", re.I)
TI_BANNED_HEAD = re.compile(
    r"^\s*(observe|see if|check whether|confirm whether|verify|watch|monitor|"
    r"inspect)\b", re.I)
TI_CJK = re.compile(r"[一-鿿]")
TI_BRACKET = re.compile(r"\[[^\]\n]*\]")
TI_MAX_WORDS = 25


def _ti_parts(v: str):
    """→ (首段, 第二段之括號內文 或 None)。"""
    lines = [x for x in str(v or "").splitlines() if x.strip()]
    if not lines:
        return "", None
    head = lines[0].strip()
    rest = " ".join(x.strip() for x in lines[1:]).strip()
    if rest.startswith("(") and rest.endswith(")"):
        return head, rest[1:-1].strip()
    return head, None


def audit_test_item(rows=None) -> list:
    rows = corpus() if rows is None else rows
    bad = []
    for t in rows:
        tid = t.get("tc_id", "?")
        v = str(t.get("test_item", "") or "")
        head, part2 = _ti_parts(v)

        # ── TI-1：兩段結構
        if not head:
            bad.append(f"TI-1 {tid}: `test_item` 首段為空")
            continue
        if part2 is None:
            bad.append(f"TI-1 {tid}: `test_item` **無第二段** —— 須為 "
                       f"`<tc_title>` 換行 `(<一句：本條在測什麼>)` "
                       f"→ 現值「{v[:46]}」")
            continue

        # ── TI-2：非空、非重複、非單詞
        if not part2:
            bad.append(f"TI-2 {tid}: 第二段之括號內為空")
            continue
        if len(part2.split()) < 2:
            bad.append(f"TI-2 {tid}: 第二段僅 {len(part2.split())} 詞 "
                       f"→「{part2}」")
        if " ".join(part2.lower().split()) == " ".join(head.lower().split()):
            bad.append(f"TI-2 {tid}: 第二段與首段**逐字相同** —— "
                       f"重複一次不是說明")

        # ── TI-3：欄位紀律
        if TI_CJK.search(part2):
            bad.append(f"TI-3 {tid}: 第二段含中文 → 「{part2[:40]}」")
        if TI_MODAL.search(part2):
            bad.append(f"TI-3 {tid}: 第二段含 modal → 「{part2[:50]}」")
        if TI_BANNED_HEAD.search(part2):
            bad.append(f"TI-3 {tid}: 第二段以 §5.1 之禁用動詞起首 → "
                       f"「{part2[:40]}」")
        if part2.rstrip().endswith("."):
            bad.append(f"TI-3 {tid}: 第二段有行尾句點")
        if TI_BRACKET.search(part2):
            bad.append(f"TI-3 {tid}: 第二段含方括號 → 「{part2[:40]}」")
        n = len(part2.split())
        if n > TI_MAX_WORDS:
            bad.append(f"TI-3 {tid}: 第二段 {n} 詞 > {TI_MAX_WORDS}")
    return bad


def corpus() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append(t)
    return out


def audit(rows=None, pats=None) -> list:
    """DF（措辭）＋ TI（`Test Item` 兩段）之合併結果。"""
    rows = corpus() if rows is None else rows
    return audit_wording(rows, pats) + audit_test_item(rows)


def audit_wording(rows=None, pats=None) -> list:
    """**只驗措辭**（DF-1／DF-2）。

    與 `audit_test_item` 分開之理由：兩者之受檢對象不同 ——
    前者吃**任何欄位之字串**，後者吃**整個 `test_item` 之結構**。
    合在一起時，DF 之方向性案例（其假列只帶一個欄位）會被 TI-1 判成
    「首段為空」而全紅 —— **那是案例被另一項檢查誤傷，不是案例錯**。
    """
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

    case("現行語料 → 綠（DF ＋ TI 合併）", lambda: audit(rows, pats), False)

    # **48 輪之漏網形態** —— 中文夾中文
    case("**注入：`TC-082` 之原形「上游未決事項」（中文夾中文）→ 紅**",
         lambda: audit_wording([{"tc_id": "FAKE-082",
                         "remarks": "**本批唯一帶上游未決事項生成者（R-U27）**："
                                    "DR #4 所缺為 popup 內文"}], pats), True)

    case("注入：英文之 `pending`（48 輪抓得到之形態）→ 紅",
         lambda: audit_wording([{"tc_id": "FAKE-1",
                         "remarks": "由 `pending` 改為具名不配"}], pats), True)

    case("注入：來源類別標記 `[spec-derived]` → 紅",
         lambda: audit_wording([{"tc_id": "FAKE-2",
                         "input_test_data": "Value [spec-derived]"}], pats),
         True)

    # ── DF-2 —— **本組最關鍵**：把中文詞之判準退回 `\b`
    def regressed():
        bad_pats = [(w, re.compile(rf"\b{re.escape(w)}\b"), k)
                    if k == "cjk" else (w, rx, k) for w, rx, k in pats]
        return audit_wording(rows, bad_pats)
    case("**DF-2 注入：中文詞之判準退回 `\\b…\\b` → 紅**（G-I 之形態本身）",
         regressed, True)

    # 護欄：形近而不在詞表者
    case("**護欄**：「未定」不在詞表 → 綠（詞表是枚舉，盲區 1 已具名）",
         lambda: audit_wording([{"tc_id": "FAKE-3",
                         "remarks": "兩者之關係條文未定"}], pats), False)

    # 護欄：`pending` 為英文單字之一部分
    case("**護欄**：`appending`／`impending` 不得誤判 → 綠",
         lambda: audit_wording([{"tc_id": "FAKE-4",
                         "remarks": "appending a row; impending change"}],
                       pats), False)

    # ── TI-1／TI-2／TI-3（55 包）
    T = "Welcome popup shown at ignition on and on activation"
    P2 = ("Verifies that a welcome popup is displayed at ignition on and "
          "each time a Driver Profile is activated")
    case("**TI 紅向：ENTRY 002 之現況（`test_item` 只有 tc_title）→ 紅**",
         lambda: audit_test_item([{"tc_id": "F-1", "test_item": T}]), True)
    case("TI 綠向：兩段齊備 → 綠",
         lambda: audit_test_item([{"tc_id": "F-2",
                                   "test_item": f"{T}\n({P2})"}]), False)
    # **現行形態**（Pei 2026-08-20）：兩段之間空一行。
    # 切段先濾空行，故空行不影響判定 —— 此案即釘住該事實，
    # 使日後有人「順手」把空行拿掉時，不會以為兩種寫法對閘是同一回事。
    case("**TI 綠向：兩段之間空一行（現行交付形態）→ 綠**",
         lambda: audit_test_item([{"tc_id": "F-2b",
                                   "test_item": f"{T}\n\n({P2})"}]), False)
    case("**TI-2 範圍向：第二段僅一詞 → 紅**",
         lambda: audit_test_item([{"tc_id": "F-3",
                                   "test_item": f"{T}\n(Tutorials)"}]), True)
    case("**TI-2 範圍向：第二段與首段逐字相同 → 紅**",
         lambda: audit_test_item([{"tc_id": "F-4",
                                   "test_item": f"{T}\n({T})"}]), True)
    case("TI-3：第二段含 modal → 紅",
         lambda: audit_test_item([{"tc_id": "F-5",
             "test_item": f"{T}\n(Verifies that the popup shall be shown)"}]),
         True)
    case("TI-3：第二段含中文 → 紅",
         lambda: audit_test_item([{"tc_id": "F-6",
             "test_item": f"{T}\n(驗證 welcome popup 於電門開啟時顯示)"}]), True)
    case("TI-3：第二段有行尾句點 → 紅",
         lambda: audit_test_item([{"tc_id": "F-7",
                                   "test_item": f"{T}\n({P2}.)"}]), True)
    case("**護欄**：第二段 25 詞（剛好上限）→ 綠",
         lambda: audit_test_item([{"tc_id": "F-8",
             "test_item": T + "\n(" + " ".join(["word"] * 25) + ")"}]), False)
    case("TI-3：第二段 26 詞 → 紅",
         lambda: audit_test_item([{"tc_id": "F-9",
             "test_item": T + "\n(" + " ".join(["word"] * 26) + ")"}]), True)

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
