#!/usr/bin/env python3
"""待判清單之時效閘（G-A，42 包 §二）。

> **同一條待判連續三輪判為「不成立」者，須改判準或除役，不得續留。**

## 為什麼「除役」不是這裡的正解

V-1／U-1／W-1／Q-1 四支之 docstring 都自陳其為
「**縮小人工判讀範圍**之工具」，硬判會把正確的判紅。
把它們除役，等於把它們**當初被建立的那個理由**也一起丟掉。

但「每輪列同樣的 43 條、每輪判同樣的結論」也確實是 G-A 要治的病 ——
PU0588 那兩處誤報就是這樣活了六輪。

**故本檔改的是判準之形，不是判準之內容**：

| | 舊 | 新 |
|---|---|---|
| 掃描輸出 | **所有命中者** | **尚未判過，或判過而內容已變者** |
| 已判者 | 每輪重列 | 登記於 `data/pending_judgements.tsv`，自清單移除 |
| 回歸保護 | 靠人每輪重讀 | 靠 **digest** —— 該 TC 之受檢欄位一變，它自動回到清單 |

**digest 是本設計的重量所在。** 沒有它，「已判過」就是一張永久豁免名單，
而那比每輪重列更糟：一條被改壞的 TC 會靜靜留在名單上。

## 四項

| # | 檢查 | 性質 |
|---|---|---|
| PJ-1 | 現行待判之每一條，須為**新命中**或**登記在案且 digest 相符** | 報表 |
| PJ-2 | 登記在案而 **digest 已變**者 → **須重判**（其舊判定不再適用） | 紅 |
| PJ-3 | 登記之 `verdict` 為 `不成立` 且 `rounds_carried ≥ 3` 而**未登記處置**者 → **G-A 逾期** | 紅 |
| PJ-4 | 登記表中已不在任何掃描命中內之條目 → **僵屍條目**，須除役 | 紅 |

`rounds_carried` 由**掃描之立案輪**與**該 TC 之生成輪**兩者之較晚者算至本輪，
不由人填 —— 填的欄位只有 `verdict`、`disposition` 與 `reason`。

Usage:
    python3 scripts/audit_pending.py
    python3 scripts/audit_pending.py --self-test
"""

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
LEDGER = FEATURE / "data" / "pending_judgements.tsv"
ROUND = 47

# 各掃描之立案輪（見各該 docstring 之包號）
SCAN_ROUND = {"Q-1": 25, "U-1": 31, "V-1": 32, "W-1": 33, "Y-1": 36,
              "AB-1": 45, "AC-1": 47,
              "X-1": 35, "K-4a": 21, "Z-1": 38, "K-3": 21, "T-1": 30,
              "U-2": 31}
# 各批之生成輪
BATCH_ROUND = {"pilot": 12, "batch01": 17, "batch02": 19, "batch03": 28,
               "batch04": 34, "batch05": 40, "batch06": 41}
# 受 digest 保護之欄位 —— **待判所讀的就是這些欄**
DIGEST_FIELDS = ("pre_conditions", "test_procedure", "expected_result",
                 "remarks", "specification_reference", "design_method")


def scans():
    import audit_consistency as A
    rows = A.tcs()
    return {
        "Y-1": A.y1_pair_claims(rows), "X-1": A.x1_unhandled_popup(rows),
        "W-1": A.w1_perfect_pre(rows), "V-1": A.v1_timing(rows),
        "U-1": A.u1_multi_trigger(rows), "Q-1": A.q1_unquoted(rows),
        "AB-1": A.ab1_compare_ends(rows),
        "AC-1": A.ac1_intra_field(rows),
        "K-4a": A.k4a(rows), "Z-1": A.z1_ru56_scope(rows), "K-3": A.k3(rows),
        "T-1": A.t1_step_refs(rows), "U-2": A.u2_unused_record(rows),
    }


def corpus() -> dict:
    out = {}
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out[t["tc_id"]] = (d.get("batch", "pilot"), t)
    return out


def digest(tc: dict) -> str:
    blob = "␟".join(" ".join(str(tc.get(f, "")).split())
                         for f in DIGEST_FIELDS)
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


def carried(scan: str, batch: str) -> int:
    start = max(SCAN_ROUND.get(scan, ROUND), BATCH_ROUND.get(batch, ROUND))
    return max(0, ROUND - start + 1)


def ledger() -> dict:
    if not LEDGER.exists():
        return {}
    with LEDGER.open(encoding="utf-8") as fh:
        rd = csv.DictReader((l for l in fh if not l.startswith("#")),
                            delimiter="\t")
        return {(r["scan"], r["tc_id"]): r for r in rd if r.get("scan")}


def audit(hits=None, led=None, corp=None) -> tuple:
    hits = scans() if hits is None else hits
    led = ledger() if led is None else led
    corp = corpus() if corp is None else corp
    bad, new, suppressed = [], [], []
    live = set()

    for scan, items in sorted(hits.items()):
        for item in items:
            tid = item[0]
            live.add((scan, tid))
            batch, tc = corp.get(tid, ("pilot", {}))
            dg = digest(tc)
            row = led.get((scan, tid))
            n = carried(scan, batch)
            if row is None:
                new.append((scan, tid, n))
                continue
            if row.get("digest") != dg:
                bad.append(f"PJ-2 {scan} {tid}: 登記之 digest `{row.get('digest')}`"
                           f" 與現況 `{dg}` 不符 —— **內容已變，舊判定不再適用，"
                           f"須重判**")
                continue
            if (row.get("verdict") == "不成立" and n >= 3
                    and not (row.get("disposition") or "").strip()):
                bad.append(f"PJ-3 {scan} {tid}: 判為不成立而已帶 {n} 輪，"
                           f"**未登記處置** —— G-A 逾期")
                continue
            suppressed.append((scan, tid, n, row.get("disposition", "")))

    for (scan, tid), row in sorted(led.items()):
        if (scan, tid) not in live:
            bad.append(f"PJ-4 {scan} {tid}: 登記在案而已不在掃描命中內 "
                       f"—— **僵屍條目**，須自登記表除役")
    return bad, new, suppressed


def self_test() -> int:
    hits, led, corp = scans(), ledger(), corpus()
    ok, cases = True, []

    def case(name, fn, expect_red):
        nonlocal ok
        cases.append(name)
        bad = fn()[0]
        good = bool(bad) == expect_red
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        for b in bad[:2]:
            print(f"      └ {b}")

    case("現行語料 ＋ 現行登記表 → 綠", lambda: audit(hits, led, corp), False)

    # PJ-2 —— **本組最關鍵**：已判之 TC 內容被改動，須回到清單
    def content_changed():
        c = {k: (b, dict(t)) for k, (b, t) in corp.items()}
        any_key = next(iter(led))[1]
        c[any_key][1]["expected_result"] = "1. tampered"
        return audit(hits, led, c)
    case("**PJ-2 注入：已判之 TC 其 ER 被改動 → 紅（digest 不符）**",
         content_changed, True)

    # PJ-3 —— 判為不成立、已逾三輪、而未登記處置
    def overdue():
        l2 = {k: dict(v) for k, v in led.items()}
        k = next(iter(l2))
        l2[k]["verdict"] = "不成立"
        l2[k]["disposition"] = ""
        return audit(hits, l2, corp)
    case("PJ-3 注入：不成立且逾三輪而無處置 → 紅", overdue, True)

    # PJ-4 —— 僵屍條目
    def zombie():
        l2 = {k: dict(v) for k, v in led.items()}
        l2[("V-1", "NR1L-UserProfiles-999")] = {
            "scan": "V-1", "tc_id": "NR1L-UserProfiles-999",
            "verdict": "不成立", "digest": "x", "disposition": "已判"}
        return audit(hits, l2, corp)
    case("PJ-4 注入：登記表留著已不再命中之條目 → 紅", zombie, True)

    # 護欄：新命中不轉紅（它只是還沒判，不是違規）
    def fresh_hit():
        l2 = {k: v for k, v in led.items()}
        l2.pop(next(iter(l2)))
        return audit(hits, l2, corp)
    case("**護欄**：某條自登記表移除（＝新命中）→ 綠，僅列為待判",
         fresh_hit, False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main() -> int:
    bad, new, sup = audit()
    print(f"待判登記表 {len(ledger())} 條；本輪掃描命中 "
          f"{sum(len(v) for v in scans().values())} 條\n")
    print(f"## 新命中（尚未判） —— {len(new)} 條\n")
    for scan, tid, n in new:
        print(f"  {scan} {tid}（已帶 {n} 輪）")
    print(f"\n## 已判且內容未變（自清單抑制） —— {len(sup)} 條\n")
    by = {}
    for scan, tid, n, dis in sup:
        by.setdefault(scan, []).append(tid[-3:])
    for scan, ids in sorted(by.items()):
        print(f"  {scan}：{len(ids)} 條 —— {' '.join(ids)}")
    print(f"\n違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    sys.exit(self_test() if a.self_test else main())
