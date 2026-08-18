#!/usr/bin/env python3
"""號碼指派之檢查（37 包作業 2）—— `tc_id` ↔ leaf 之對映，**不靠人眼**。

## 為什麼要有這支

36 輪之自檢抓到兩處**指錯目標**：

| 宣稱者 | 原指 | 原指者實為 | 正確者 |
|---|---|---|---|
| `TC-096`（`009`）| `NR1L-UserProfiles-104` | `016`（4.6.3）| `105`（`009-neg`）|
| `TC-127`（`030-01`）| `NR1L-UserProfiles-133` | `034-03`（5.10.1）| `134`（`030-01-neg`）|

**兩處都是在 `tc_id` 尚未指派時寫下的號碼** ——
生成器之 `remarks` 是先寫的，而號碼由 `TC_START` ＋ 取樣序決定，
**兩者之間沒有任何檢查**。

Y-1 掃描抓得到**跨 leaf 群**之誤指，**抓不到同群內指錯**
（如 `030-01` 誤指 `030-02`）—— 本檔補之。

## 三項

| # | 檢查 | 性質 |
|---|---|---|
| A-1 | **號碼指派表**（自生成器重建）與 `generated/` 之 `tc_id`↔`req_id` 相符 | 紅 |
| A-2 | 文內同時出現 `tc_id` 與 leaf id 之句子，兩者須在指派表中對應 | 紅 |
| A-3 | 文內單獨出現之 `tc_id` 須存在於指派表 | 紅 |

**A-1 是本檔之地基**：指派表由**生成器之取樣清單與 `TC_START` 重算**，
不讀 `generated/`。若兩者不符，代表**產物與生成器已經分岔** ——
那種情形下，任何以產物為據之檢查都不可信。

## 盲區（R-G11）

1. **A-2 只在同一句同時出現兩者時才驗**。
   若句中只寫 `NR1L-UserProfiles-133` 而未附 leaf id，本檔驗不出它指錯 ——
   **36 輪之兩處正是此形態**（只寫號碼）。
   那一類由 Y-1（leaf 群）與人工覆核承擔；**本檔擋的是「寫了兩者而互不相符」**。
2. **不驗語意關係**（該句所稱之「正向／反向／承擔」是否為真）——
   那是 Y-1 與 `audit_delegation` 之事。

Usage:
    python3 scripts/audit_assignment.py
    python3 scripts/audit_assignment.py --self-test
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
TCID = re.compile(r"NR1L-UserProfiles-(\d{3})")
LEAF = re.compile(r"SWE1-HMI-PROF-(\d{3}(?:-\d{2})?(?:-[a-z]+)?)")
SENT = re.compile(r"[^。；\n]+")


def assignment_table() -> dict:
    """`tc_id` → `req_id`，**自生成器之取樣清單與 `TC_START` 重算**。"""
    import gen_pilot, gen_batch01, gen_batch02          # noqa: E401
    import gen_batch03, gen_batch04, gen_batch05        # noqa: E401
    import gen_batch06                                 # noqa: E401
    import gen_pairs                                   # noqa: E401
    t, n = {}, 1
    for rid in gen_pilot.SAMPLE_IDS:                    # pilot 自 1 起
        t[f"NR1L-UserProfiles-{n:03d}"] = rid
        n += 1
    n = gen_batch01.TC_START
    for rid in gen_batch01.sample():
        t[f"NR1L-UserProfiles-{n:03d}"] = rid
        n += 1
    t[f"NR1L-UserProfiles-{n:03d}"] = gen_batch01.NEG_111["req_id"]
    n = gen_batch02.TC_START
    for ln in (FEATURE / "data" / "batch02_sample.tsv").read_text(
            encoding="utf-8").splitlines():
        if not ln or ln.startswith(("#", "req_id")):
            continue
        t[f"NR1L-UserProfiles-{n:03d}"] = ln.split("\t")[0]
        n += 1
    n = gen_pairs.TC_START
    for item in gen_pairs.PAIRS:
        t[f"NR1L-UserProfiles-{n:03d}"] = item["req_id"]
        n += 1
    for mod in (gen_batch03, gen_batch04, gen_batch05, gen_batch06):
        n = mod.TC_START
        for rid in mod.SAMPLE:
            t[f"NR1L-UserProfiles-{n:03d}"] = rid
            n += 1
        for item in getattr(mod, "EXTRAS", []):
            t[f"NR1L-UserProfiles-{n:03d}"] = item["req_id"]
            n += 1
    return t


def _base(req: str) -> str:
    m = re.search(r"PROF-(\d{3}(?:-\d{2})?)", req or "")
    return m.group(1) if m else ""


def corpus() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append((d, t))
    return out


def audit(table=None, rows=None) -> list:
    table = assignment_table() if table is None else table
    rows = corpus() if rows is None else rows
    bad = []

    # ── A-1：指派表 vs 產物
    for d, t in rows:
        exp = table.get(t["tc_id"])
        if exp is None:
            bad.append(f"A-1 {t['tc_id']}: 不在號碼指派表內 —— "
                       f"**產物與生成器已分岔**")
        elif exp != t["req_id"]:
            bad.append(f"A-1 {t['tc_id']}: 指派表為 `{exp}`，"
                       f"產物為 `{t['req_id']}`")

    # ── A-2／A-3：文內之引用
    for d, t in rows:
        for fld, blob in (("reasoning", d.get("reasoning", "")),
                          ("remarks", t.get("remarks", ""))):
            for sm in SENT.finditer(str(blob or "")):
                snt = " ".join(sm.group(0).split())
                tcs_ = TCID.findall(snt)
                lfs = LEAF.findall(snt)
                for num in tcs_:
                    tid = f"NR1L-UserProfiles-{num}"
                    if tid not in table:
                        bad.append(f"A-3 {t['tc_id']}（{fld}）: 提及之 `{tid}` "
                                   f"不在號碼指派表內")
                        continue
                    if len(tcs_) == 1 and len(lfs) == 1:
                        want = _base(table[tid])
                        got = _base("PROF-" + lfs[0])
                        if want and got and want != got:
                            bad.append(
                                f"A-2 {t['tc_id']}（{fld}）: 同句稱 `{tid}` 與 "
                                f"`SWE1-HMI-PROF-{lfs[0]}`，而指派表中 {tid} "
                                f"之 leaf 為 `{table[tid]}` —— 兩者不符"
                                f" → 「{snt[:60]}」")
    return bad


def self_test() -> int:
    table = assignment_table()
    ok, cases = True, []

    def case(name, rows, expect, tbl=None):
        nonlocal ok
        cases.append(name)
        bad = audit(tbl or table, rows)
        good = bool(bad) == expect
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect else '綠'}")
        for b in bad[:2]:
            print(f"      └ {b}")

    def _tc(**kw):
        t = {"tc_id": "NR1L-UserProfiles-096",
             "req_id": "SWE1-HMI-PROF-009", "remarks": ""}
        t.update(kw)
        return [({"reasoning": kw.pop("reasoning", "")}, t)]

    case("現行語料 → 綠", corpus(), False)
    # A-1：產物之 req_id 與指派表不符
    case("A-1 注入：`096` 之 req_id 改為 `016` → 紅",
         [({"reasoning": ""},
           {"tc_id": "NR1L-UserProfiles-096",
            "req_id": "SWE1-HMI-PROF-016", "remarks": ""})], True)
    # A-2：同句之 tc_id 與 leaf id 不符（**36 輪兩處若當時附了 leaf id 即會被此擋下**）
    case("A-2 注入：同句稱 `104`＋`SWE1-HMI-PROF-009` → 紅",
         [({"reasoning": ""},
           {"tc_id": "NR1L-UserProfiles-096",
            "req_id": "SWE1-HMI-PROF-009",
            "remarks": "反向為 `NR1L-UserProfiles-104`（`SWE1-HMI-PROF-009`）"})],
         True)
    case("A-2 範圍：同句稱 `105`＋`SWE1-HMI-PROF-009` → 綠",
         [({"reasoning": ""},
           {"tc_id": "NR1L-UserProfiles-096",
            "req_id": "SWE1-HMI-PROF-009",
            "remarks": "反向為 `NR1L-UserProfiles-105`（`SWE1-HMI-PROF-009`）"})],
         False)
    # A-3：提及不存在之號碼
    case("A-3 注入：提及 `NR1L-UserProfiles-999` → 紅",
         [({"reasoning": "由 `NR1L-UserProfiles-999` 承擔"},
           {"tc_id": "NR1L-UserProfiles-096",
            "req_id": "SWE1-HMI-PROF-009", "remarks": ""})], True)
    # 護欄：同句只有 tc_id、無 leaf id → A-2 不適用（本檔之盲區 1）
    case("**護欄（盲區 1）**：同句只寫號碼而無 leaf id → 綠（A-2 驗不到）",
         [({"reasoning": ""},
           {"tc_id": "NR1L-UserProfiles-096",
            "req_id": "SWE1-HMI-PROF-009",
            "remarks": "反向為 `NR1L-UserProfiles-104`"})], False)

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
    table = assignment_table()
    bad = audit(table)
    print(f"號碼指派表 {len(table)} 條；語料 {len(corpus())} 條\n")
    print(f"違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
