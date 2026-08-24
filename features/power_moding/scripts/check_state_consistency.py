#!/usr/bin/env python3
"""R-PMH45 —— 同檔內互斥狀態陳述之一致性檢查。

抓的是**替換未命中之結果**，而非替換之過程 —— 歷史上已無 before 可查之
替換，其殘留仍會被它抓到（`framework.md` 第 7 行「未定版」與第 24 行
「定版」跨兩輪並存即為其標的）。

四組互斥對（R-PMH45 所列之最低限度）：
    定版 / 未定版
    PENDING / RESOLVED
    待裁 / 已裁·已結清
    wired: true / wired: false

判定：同一檔內同時出現互斥對之兩側者即 FAIL，並列出行號與逐字內容。
**不得以「總數為 0」代替**（R-PMH41 末段）。

`RULINGS.md` 與 `ANOMALIES.md` 之處理見 `EXCLUDED` 之說明。

用法:
    python scripts/check_state_consistency.py --feature .
    python scripts/check_state_consistency.py --feature . --self-test
"""

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 有效範圍：**狀態板**三檔（其內容為欄位值與勾選項，非散文）。
TARGETS = ["framework.md", "feature.yaml", "PLAYBOOK.md"]

# **R-PMH49(b) —— 按條號切分已實作**，故 `RULINGS.md`／`ANOMALIES.md`
# 不再具名排除；其互斥判定以「同一條號之段」為單位，見 `scan_sectioned()`。
# 切分式保留供追溯；二檔皆已具名排除，故本表為空。
SECTIONED: dict[str, str] = {}
SECTIONED_ATTEMPTED = {"RULINGS.md": r"^#{1,3}\s*(R-PMH\d+)",
                       "ANOMALIES.md": r"^#{1,3}\s*(A-PMH\d+)"}

# **R-PMH49(b) 之實作結果 —— 按條號切分已實作並實跑，惟判準對「散文檔」不可用。**
#
# 切分本身可行（`RULINGS.md` 51 段、`ANOMALIES.md` 13 段）。
# **不可用者為判準**：本檢查以「互斥字串共現」判定，而
# **「引述狀態字」與「斷言狀態」在字面與上下文形態上完全相同**。
#
# 實跑所見（12 包步驟 4）：
#   `RULINGS.md`   —— 10 命中、**10 皆誤報**。R-PMH43/45/49 之條文本身即逐字
#                     列舉互斥對兩側（R-PMH45：「最低限度之互斥對：`定版`/
#                     `未定版`、`PENDING`/`RESOLVED`…」）。**定義本檢查之
#                     條文，其字面必然含兩側。**
#   `ANOMALIES.md` —— 段外 2 命中為**檔頭之詞彙說明**（"PENDING entries block
#                     their batch … RESOLVED entries record the ruling
#                     verbatim"）；段內 1 命中為 A-PMH13 之**歷史引述**與
#                     **規則敘述**（「含 PENDING 之工作簿不得出貨」）。
#   `DECISIONS.md` —— 兩側皆為**規則敘述**：「含 PENDING 之工作簿不得出貨」
#                     與「通則 8：文字修補不構成 RESOLVED」。
#
# **可修與不可修之界線**（本輪已修前者，未動後者）：
#   可修  —— pattern 之**精確度**：`PENDING-CANON` 為另一狀態值、
#            `PENDING: DR-` 為欄位佔位標記、`非 RESOLVED` 為否定式。已加 lookaround。
#   不可修 —— **散文提及 vs 狀態斷言**。再加 lookaround 即是把判準往資料上調，
#            正是 R-PMH49(b) 所禁之「放寬判準後宣稱通過」。
#
# **故三個散文檔具名排除；本檢查之有效範圍為「狀態板」三檔。**
# **此範圍窄於 R-PMH49(b) 所期，據實記載，未宣稱通過。**
#
# **本輪之實跑仍有實益**：它在 A-PMH13 段內查出一句**已過時之狀態陳述**
# （07 包所寫「本則之 PENDING 狀態僅繫於 -028 之處置」，而 12 包已裁 RESOLVED），
# 已改標為當時陳述。**該項為真缺陷。**
EXCLUDED = {
    "RULINGS.md": "散文檔 —— 條文本身列舉互斥對兩側（切分 51 段，10/10 誤報）",
    "ANOMALIES.md": "散文檔 —— 檔頭詞彙說明 ＋ 歷史引述 ＋ 規則敘述（切分 13 段）",
    "DECISIONS.md": "散文檔 —— 兩側皆為規則敘述（§8.4.3 與通則 8）",
}

PAIRS = [
    ("定版/未定版", [r"(?<!未)定版"], [r"未定版"]),
    # pattern 之**精確化**（非放寬，12 包步驟 4）：
    #   `PENDING-CANON` 是**另一個狀態值**，不是 `PENDING`；
    #   `PENDING: DR-…` 是**欄位佔位標記**（§8.4.3），不是 anomaly 之狀態；
    #   `非 RESOLVED`／`not RESOLVED` 是**否定式**，其斷言與 `RESOLVED` 相反。
    ("PENDING/RESOLVED",
     [r"(?<!非 )(?<!非)\bRESOLVED\b"],
     [r"\bPENDING\b(?!-CANON)(?!:\s*DR-)(?!-CANON)"]),
    ("待裁/已結清", [r"已裁|已結清"], [r"待裁"]),
    ("wired", [r"wired:\s*true"], [r"wired:\s*false"]),
    # R-PMH49(a) 新增四組
    ("已授權/未授權", [r"已授權"], [r"未授權"]),
    ("已接上/wired:false", [r"已接上"], [r"wired:\s*false"]),
    ("已定案/待裁", [r"已定案"], [r"待裁"]),
    ("workbook_state", [r"\bFULL\b"], [r"\bBLANK\b"]),
]
PAIRS_IS_ENUMERATION_NOT_TOTAL = True  # R-PMH49(a) 明載


# --- R-PMH52 之擴及（17 包步驟 4）---
# 本檢查已以 `EXCLUDED` 具名其排除之檔，**格式與他支對齊**如下。
LIMITS = [
    "**互斥對 8 組為列舉而非全集** —— 未列舉之互斥形態不會被發現",
    "有效範圍只及三個狀態板（`framework.md`／`feature.yaml`／`PLAYBOOK.md`）；`RULINGS.md`／`ANOMALIES.md`／`DECISIONS.md` 已具名排除（散文檔，按條號切分之判準實測不可用）",
    "**只驗同檔內之互斥**；**跨檔之矛盾不看** —— 如 `framework.md` 稱定版而上繳包稱未定版，本檢查全綠",
    "只比對**字面**之狀態詞；語意等價之不同措詞（「已鎖」vs「定版」）不視為同一狀態",
    "被排除之散文檔中之矛盾（如 16 包所查出之 A-PMH14）**須人讀**，本檢查看不見",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for _x in LIMITS:
        print(f"  - {_x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def scan(path: Path) -> list[tuple[str, list, list]]:
    """回傳該檔中**兩側同時出現**之互斥對及其行號。"""
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for name, a_pats, b_pats in PAIRS:
        a = [(i, l.strip()) for i, l in enumerate(lines, 1)
             if any(re.search(p, l) for p in a_pats)]
        b = [(i, l.strip()) for i, l in enumerate(lines, 1)
             if any(re.search(p, l) for p in b_pats)]
        if a and b:
            out.append((name, a, b))
    return out


def scan_sectioned(path: Path, head_re: str) -> tuple[list, list]:
    """R-PMH49(b) —— 以條號切段，段內判互斥。

    回傳 (違反清單, 落在任何段外之狀態陳述)。**切分失敗者須具名列出，
    不得靜默歸入前段。**
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    rx = re.compile(head_re)
    # 切段：(條號, 起始行, 結束行)
    marks = [(m.group(1), i) for i, l in enumerate(lines, 1)
             if (m := rx.match(l))]
    segs = [(cid, s, (marks[k + 1][1] - 1 if k + 1 < len(marks) else len(lines)))
            for k, (cid, s) in enumerate(marks)]
    first = marks[0][1] if marks else len(lines) + 1

    bad, orphan = [], []
    for name, a_pats, b_pats in PAIRS:
        # 段外（首個條號之前）之狀態陳述 —— 具名，不歸入任何段
        for i, l in enumerate(lines[:first - 1], 1):
            if any(re.search(p, l) for p in a_pats + b_pats):
                orphan.append((i, name, l.strip()))
        for cid, s, e in segs:
            body = list(enumerate(lines[s - 1:e], s))
            a = [(i, l.strip()) for i, l in body if any(re.search(p, l) for p in a_pats)]
            b = [(i, l.strip()) for i, l in body if any(re.search(p, l) for p in b_pats)]
            if a and b:
                bad.append((cid, name, a, b))
    return bad, orphan


def run(files: list[Path], label: str = "") -> bool:
    print(f"\n=== 互斥狀態一致性檢查{label} ===")
    print(f"互斥對 {len(PAIRS)} 組（R-PMH49(a)）—— "
          f"**本清單為列舉而非全集，未列舉者不會被發現**")
    print(f"有效範圍（狀態板）：{', '.join(TARGETS)}")
    print(f"按條號切分之嘗試（R-PMH49(b)）：{', '.join(SECTIONED_ATTEMPTED)} "
          f"—— 已實作實跑，判準對散文檔不可用，具名排除如下")
    for f, why in EXCLUDED.items():
        print(f"    具名排除 {f} —— {why}")
    ok = True
    for p in files:
        if not p.exists():
            print(f"\n  {p.name:18s} **FAIL** —— 檔不存在")
            ok = False
            continue
        if p.name in SECTIONED:
            bad, orphan = scan_sectioned(p, SECTIONED[p.name])
            n_seg = len(re.findall(SECTIONED[p.name], p.read_text(encoding="utf-8"), re.M))
            tag = f"（按條號切分，{n_seg} 段）"
            if orphan:
                print(f"\n  {p.name:18s} **段外之狀態陳述 {len(orphan)} 處（具名，"
                      f"未歸入任何段）**{tag}")
                for i, nm, l in orphan[:6]:
                    print(f"      L{i:<5d} [{nm}] {l[:78]}")
                if len(orphan) > 6:
                    print(f"      … 另 {len(orphan)-6} 處")
            if not bad:
                print(f"\n  {p.name:18s} PASS {tag}")
                continue
            ok = False
            print(f"\n  {p.name:18s} **FAIL** —— {len(bad)} 個條號段內互斥{tag}")
            for cid, name, a, b in bad:
                print(f"      [{cid} / {name}]")
                for i, l in a[:2]:
                    print(f"         L{i:<5d} (A 側) {l[:80]}")
                for i, l in b[:2]:
                    print(f"         L{i:<5d} (B 側) {l[:80]}")
            continue
        bad = scan(p)
        if not bad:
            print(f"\n  {p.name:18s} PASS")
            continue
        ok = False
        print(f"\n  {p.name:18s} **FAIL** —— {len(bad)} 組互斥對兩側並存")
        for name, a, b in bad:
            print(f"      [{name}]")
            for i, l in a[:4]:
                print(f"         L{i:<5d} (A 側) {l[:88]}")
            for i, l in b[:4]:
                print(f"         L{i:<5d} (B 側) {l[:88]}")
    return ok


def self_test() -> int:
    print("=== R-PMH45 之範圍向（R-G9）—— 現行四檔須全 PASS ===")
    scope_ok = run([ROOT / f for f in TARGETS], "（範圍向）")
    print(f"\n  範圍向 {'PASS ✅' if scope_ok else 'FAIL ❌'}")

    print("\n" + "=" * 72)
    print("=== 故意失敗 —— 於**暫存副本**上把 framework.md:7 改回「未定版」 ===")
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for f in TARGETS:
            shutil.copy2(ROOT / f, tmp / f)
        fm = tmp / "framework.md"
        lines = fm.read_text(encoding="utf-8").splitlines()
        # 把第 7 行之「定版」改回「未定版」，模擬 08a 之未命中結果
        for i, l in enumerate(lines):
            if "**狀態：定版**" in l:
                lines[i] = ("- **狀態：未定版。** Test Set #2 之名為 "
                            "`Disclaimer Screen`，待 Pei 裁定（06 §5.4）")
                print(f"    注入於 L{i+1}：{lines[i]}")
                break
        else:
            print("    ❌ 找不到注入點，測試無效")
            return 1
        fm.write_text("\n".join(lines) + "\n", encoding="utf-8")
        bad_ok = run([tmp / f for f in TARGETS], "（故意失敗）")
    print(f"\n  故意失敗 {'**未被攔下** ❌' if bad_ok else '被攔下 ✅'}")
    print("  （注入僅在暫存副本上；ROOT 之檔案未被改動）")

    print("\n" + "=" * 72)
    caught = not bad_ok
    print(f"範圍向 PASS: {scope_ok}；故意失敗被攔下: {caught}")
    return 0 if (scope_ok and caught) else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--feature", default=".")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        rc = self_test()
        print_limits()
        sys.exit(rc)
    ok = run([ROOT / f for f in TARGETS])
    print_limits()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
