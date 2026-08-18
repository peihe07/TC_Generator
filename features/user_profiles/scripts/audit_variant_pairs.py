#!/usr/bin/env python3
"""變體對造之一致判準 V-1 與其稽核（22 包 L-3）。

## 判準 V-1

**凡 spec 有明文之變體覆寫註記，其所涉之字面值出現於某條 TC 之 ER 者，
須配該變體之對造；不配者須具名理由，且該理由須不適用於已配者。**

### 觸發要件是「明文覆寫」，不是「另有一種配置」

這一句是判準的全部重量所在。若把觸發要件寫成「ER 之內容隨配置而異」，
則 `(if applicable)` 之 Navigation、8.4 吋螢幕、有無連網……全部都要配對造，
**判準會擴張到不可能執行，然後被整個放棄**。

故觸發母體取 `data/pdf_starred_notes.tsv` 之 `kind == 變體覆寫註記` ——
**那是 spec 自己標出來的覆寫，條數固定、可逐條點名、新增時本閘會紅**。

### 三個不觸發之例，逐一說明它們為何不是漏網

| 情形 | 為何不觸發 |
|---|---|
| `Navigation (if applicable)`（10.3.1）| `(if applicable)` 是**適用條件**，不是覆寫 —— 該列在無 Navigation 車上不顯示，spec 未指定另一個字面值 |
| 8.4 吋螢幕（9.1.1）| 9.1.1 **本身即是該尺寸之條文**，非對他節之覆寫；spec 未給另一尺寸之對應字面值 |
| 有無連網（11.3）| 同上 —— 條件式顯示，非字面值覆寫 |

**這三者仍可能各自有覆蓋缺口**（例：9.1.1 之另一側版面），
但那是取樣範圍之問題，不是變體對造之問題。**混為一談會使兩者都查不清。**

## 本檔之閘（四項）

1. TSV 之每一條 `變體覆寫註記` 都已登記於 `AXES` —— **spec 側新增覆寫時轉紅**
2. `AXES` 所點名之每個 tc_id 都在語料內 —— 對造被刪時轉紅
3. 每個 axis 若非 paired，須有 `reason`
4. **`reason` 之判準須不適用於已配者** —— 逐條以述詞實測，
   而非以人工宣稱。**這是 L-3 之核心要求，也是唯一無法用文字含混過去的一項。**

Usage:
    python3 scripts/audit_variant_pairs.py              # 掃語料
    python3 scripts/audit_variant_pairs.py --self-test  # 方向性案例
"""

import argparse
import json
import re
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent
NOTES_TSV = FEATURE / "data" / "pdf_starred_notes.tsv"
OVERRIDE_KIND = "變體覆寫註記"


# ─────────────────────────────────────────────── 述詞（reason 之可測形式）

NEGATOR = re.compile(r"\b(no|not|never|hidden|absent|without)\b", re.I)


def absence_only(tc: dict, literal: str) -> bool:
    """該 TC 之 ER 對 `literal` **只作缺席斷言**。

    逐**子句**判：ER 中每一個提到 `literal` 之子句都帶否定詞 → True。
    只要有一句是**在場斷言**（「清單第四項為 X」）→ False。

    **為什麼這個述詞就是 TC-020 之理由本身**：一條驗「那個按鈕不在」之 TC，
    其判定不取決於該按鈕在另一變體上叫什麼名字（J-7）。
    而一條驗「清單第四項寫著 X」之 TC，X 是什麼**正是它在驗的東西**。

    ## 本述詞首跑即被自身之閘 4 抓出兩處錯，皆為**判準錯**

    1. **以句為單位太粗。** v1 切句（`.` `;` 換行），於是 074 之 ER 那一長句
       裡的 `Resume Setup (only if **not** complete)` 讓整句被讀成否定 ——
       **一個在場斷言被判成缺席斷言**，而 074 正是已配對造者，
       閘 4 遂報「該理由同樣適用於已配者」。**閘沒壞，是述詞壞了。**
       v2 改切**子句**（併切逗號），否定詞須與該字面值同一子句。
    2. **`literal` 寫死單一字串比對不到。** 覆寫註記寫的是
       `"Stellantis Account"`，而 9.2 之本文寫 `Stellantis Connected Account`、
       R1 High 側寫 `Connected Account` —— **同一個 axis 之兩側本來就是不同字串**。
       v2 改以**正則涵蓋該 axis 之各側寫法**。
    """
    er = tc.get("expected_result", "")
    pat = re.compile(literal, re.I)
    hits = [seg for seg in re.split(r"[.;,\n]", er) if pat.search(seg)]
    if not hits:
        return False                      # 根本沒提到 —— 不適用本理由
    return all(NEGATOR.search(seg) for seg in hits)


PREDICATES = {"absence-only": absence_only}


# ─────────────────────────────────────────────────────────── 登記表

# 每個 axis：spec 之覆寫註記 → 受其影響之 TC，及其配對狀態。
# `note_key` 須為 TSV 中該列 `text` 之前綴（比對用）。
AXES = [
    dict(
        axis="p14 / Table EDPR1 之帳號 label",
        note_key='R1 High Only: "Stellantis Account" to',
        # 同一 axis 之兩側寫法不同 —— base 為 `Stellantis (Connected) Account`、
        # R1 High 為 `Connected Account`。**兩側都要涵蓋**，否則述詞比對不到。
        literal=r"Stellantis Connected Account|Stellantis Account|Connected Account",
        members=[
            dict(tc="NR1L-UserProfiles-017", side="R1 High", paired_with="074"),
            dict(tc="NR1L-UserProfiles-074", side="base", paired_with="017"),
            # 同一覆寫所涉，但**只作缺席斷言** —— 具名不配，理由須可測
            dict(tc="NR1L-UserProfiles-020", side="區域無 app",
                 reason="absence-only",
                 why="其 ER 為「該按鈕不顯示」之缺席斷言 —— label 之形式"
                     "不影響判定（J-7）。**同一理由對 017／074 不成立**："
                     "那兩條斷言的正是第四項寫著哪一個 label"),
            dict(tc="NR1L-UserProfiles-077", side="不支援該功能",
                 reason="absence-only",
                 why="同 020 —— 缺席斷言"),
        ],
    ),
    dict(
        axis="p16 / Table PIP1 之 Connected Account 列描述",
        note_key='R1 High Only: for the "Connected Account" category title (if',
        literal=r"Save your preferences to the cloud",
        members=[
            dict(tc="NR1L-UserProfiles-039", side="base", paired_with="075"),
            dict(tc="NR1L-UserProfiles-075", side="R1 High", paired_with="039"),
        ],
    ),
    dict(
        axis="p17 / Table CPA2 整張表之適用性",
        note_key="R1 High Only: This table (Table CPA2) is not applicable. There will",
        literal=r"info icon|info button",
        members=[
            dict(tc="NR1L-UserProfiles-013", side="base", paired_with="044"),
            dict(tc="NR1L-UserProfiles-044", side="R1 High", paired_with="013"),
        ],
    ),
    dict(
        axis="p17 / Table CPA2 之 Connected Navigation 列",
        note_key="For China market only: do not show this content",
        literal=r"Connected Navigation",
        members=[
            dict(tc="NR1L-UserProfiles-013", side="非中國", paired_with="076"),
            dict(tc="NR1L-UserProfiles-076", side="中國", paired_with="013"),
        ],
    ),
]


def corpus() -> dict:
    out = {}
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out[t["tc_id"]] = t
    return out


def override_notes() -> list:
    rows = []
    for ln in NOTES_TSV.read_text(encoding="utf-8").splitlines():
        if not ln or ln.startswith("#") or ln.startswith("page\t"):
            continue
        parts = ln.split("\t")
        if len(parts) >= 3 and parts[2] == OVERRIDE_KIND:
            rows.append((parts[0], parts[1]))
    return rows


def audit(tcs: dict) -> list:
    bad = []

    # 閘 1 —— TSV 之每條覆寫註記都已登記
    keys = [a["note_key"] for a in AXES]
    for page, text in override_notes():
        if not any(text.startswith(k) or k.startswith(text) for k in keys):
            bad.append(f"V1-1: {page} 之覆寫註記未登記於 AXES → 「{text[:60]}」")

    for a in AXES:
        for m in a["members"]:
            tid = m["tc"]
            # 閘 2 —— 點名之 TC 須在語料內
            if tid not in tcs:
                bad.append(f"V1-2: {a['axis']} 點名之 {tid} 不在語料內")
                continue
            # 閘 3 —— 非 paired 者須有 reason
            if "paired_with" not in m and "reason" not in m:
                bad.append(f"V1-3: {a['axis']} 之 {tid} 既未配對造亦無具名理由")
                continue
            # 閘 4 —— reason 之述詞須為真，且**對已配者為假**
            if "reason" in m:
                pred = PREDICATES.get(m["reason"])
                if pred is None:
                    bad.append(f"V1-4: {tid} 之 reason `{m['reason']}` 無述詞實作")
                    continue
                if not pred(tcs[tid], a["literal"]):
                    bad.append(f"V1-4: {tid} 之理由 `{m['reason']}` 述詞不成立 "
                               f"—— 宣稱不配對造，但它並非該形態")
                for other in a["members"]:
                    if "paired_with" not in other or other["tc"] not in tcs:
                        continue
                    if pred(tcs[other["tc"]], a["literal"]):
                        bad.append(
                            f"V1-4: {tid} 之理由 `{m['reason']}` **同樣適用於已配之 "
                            f"{other['tc']}** —— 該理由不成立"
                            f"（若成立，{other['tc']} 就不該配）")
    return bad


def report(tcs: dict) -> None:
    print(f"語料 {len(tcs)} 條；spec 之變體覆寫註記 {len(override_notes())} 條\n")
    print("## V-1 登記表\n")
    for a in AXES:
        print(f"### {a['axis']}")
        for m in a["members"]:
            if "paired_with" in m:
                print(f"  [配] {m['tc']}（{m['side']}）↔ …-{m['paired_with']}")
            else:
                print(f"  [不配] {m['tc']}（{m['side']}）—— {m['reason']}："
                      f"{m.get('why', '')[:70]}")
        print()


def self_test() -> int:
    """方向性案例 —— **每一條都是拿掉某個保護後，本閘該不該紅**。"""
    ok, cases = True, []
    real = corpus()

    def case(name, fn, expect_red):
        nonlocal ok
        bad = fn()
        good = bool(bad) == expect_red
        ok &= good
        cases.append(name)
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        for b in bad[:2]:
            print(f"      └ {b}")

    case("現行語料 → 綠", lambda: audit(real), False)

    # 閘 2：對造被刪
    case("刪掉 074（9.1 之對造）→ 紅",
         lambda: audit({k: v for k, v in real.items()
                        if k != "NR1L-UserProfiles-074"}), True)

    # 閘 4 之前半：宣稱「缺席斷言」而其 ER 其實是在場斷言
    def fake_presence():
        t = dict(real["NR1L-UserProfiles-020"])
        t["expected_result"] = ("1. The tab is displayed\n"
                                "2. The fourth item reads Stellantis Account")
        return audit({**real, "NR1L-UserProfiles-020": t})
    case("020 之 ER 改為在場斷言（理由不再成立）→ 紅", fake_presence, True)

    # 閘 4 之後半 —— **本組最關鍵的一條**
    # 把 017 之 ER 改成缺席斷言：此時「缺席斷言」這個理由對它也成立，
    # 而它是**已配對造**者 —— 判準遂自相矛盾，須紅。
    # 它守的是 L-3 之原話：**不配之理由須不適用於已配者**。
    def reason_leaks():
        t = dict(real["NR1L-UserProfiles-017"])
        t["expected_result"] = ("1. The tab is displayed\n"
                                "2. No Stellantis Account item is shown")
        return audit({**real, "NR1L-UserProfiles-017": t})
    case("017 改為缺席斷言 → 該理由同樣適用於已配者 → 紅", reason_leaks, True)

    # 閘 1：spec 側新增一條覆寫註記而未登記
    def unregistered_note():
        g = globals()
        orig = g["override_notes"]
        g["override_notes"] = lambda: orig() + [("p99", "R1 Mid Only: fake note")]
        try:
            return audit(real)
        finally:
            g["override_notes"] = orig
    case("spec 新增未登記之覆寫註記 → 紅", unregistered_note, True)

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
    tcs = corpus()
    report(tcs)
    bad = audit(tcs)
    print(f"違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
