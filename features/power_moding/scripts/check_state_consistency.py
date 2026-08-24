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

TARGETS = ["framework.md", "feature.yaml", "DECISIONS.md", "PLAYBOOK.md"]

# **具名排除，非放寬判準**（R-PMH45 之 11 包 §四步驟 3 末段，停止條件 9）。
#
# `RULINGS.md` 與 `ANOMALIES.md` 為**多對象登記簿** —— 其「PENDING」與
# 「RESOLVED」分屬不同 anomaly，「待裁」與「已結清」分屬不同 Q 項，
# 全檔字串共現是**正常且必然**的，不是不一致。
#
# 要對它們做互斥判定，須先以「同一 `A-PMH{n}` / `R-PMH{n}` / `Q{n}`」為單位
# 切分，而該切分無法由行級掃描乾淨得出（狀態可寫在節標題、表格列、
# 或內文任一處，且一則 anomaly 之內文常引述他則之狀態）。
#
# **故本檢查不納入此二檔，並在每次輸出中具名。**
EXCLUDED = {
    "RULINGS.md": "多對象登記簿 —— 不同條文之狀態字共存為正常；"
                  "互斥判定須先按條號切分，行級掃描無法乾淨得出",
    "ANOMALIES.md": "同上 —— 不同 A-PMH 之 PENDING/RESOLVED 共存為正常",
}

PAIRS = [
    ("定版", [r"(?<!未)定版"], [r"未定版"]),
    ("PENDING/RESOLVED", [r"\bRESOLVED\b"], [r"\bPENDING\b"]),
    ("待裁/已結清", [r"已裁|已結清"], [r"待裁"]),
    ("wired", [r"wired:\s*true"], [r"wired:\s*false"]),
]


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


def run(files: list[Path], label: str = "") -> bool:
    print(f"\n=== 互斥狀態一致性檢查{label} ===")
    print(f"具名排除之檔（R-PMH45，非放寬判準）：")
    for f, why in EXCLUDED.items():
        print(f"    {f} —— {why}")
    ok = True
    for p in files:
        if not p.exists():
            print(f"\n  {p.name:18s} **FAIL** —— 檔不存在")
            ok = False
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
        sys.exit(self_test())
    sys.exit(0 if run([ROOT / f for f in TARGETS]) else 1)


if __name__ == "__main__":
    main()
