"""Layer 2 Test Set 指派與 §E 定版驗證（G21 / G22）。

指派規則（依裁決，非演算法）：

  R-P15(a)  解析至單一章節之 leaf → 自動歸屬該章節所屬 Test Set。
  R-P15(b)  解析至多章節之 leaf → 由 Pei 逐條裁定，見 RULED_MULTI。
            其中九條之全部候選章節同屬一個 Test Set，Test Set 層無歧義，
            仍逐一驗證其無歧義性並回報。
  R-P33     SWE-PM-008 → Power State
  R-P34     SWE-PM-057 → Timeout Settings

**本腳本不含任何 tie-break。** 若某多章節 leaf 之候選章節橫跨多個
Test Set 且未列於 RULED_MULTI，直接報錯停止 —— 不猜。

用法：
    python features/power/scripts/build_testsets.py
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# R-P35 定版期望值
LOCKED = {
    "Power State": 63,
    "Startup Display": 24,
    "Branding and Theme": 16,
    "Timeout Settings": 8,
    "Power Down": 3,
}

# R-P33 / R-P34：Pei 逐條裁定者
RULED_MULTI = {
    "SWE-PM-008": ("Power State", "R-P33"),
    "SWE-PM-057": ("Timeout Settings", "R-P34"),
}


def test_set_of(domain: str, num: str) -> str:
    """§E Layer 3 章節 → Test Set。無對應者回傳 '未歸類 …'。"""
    if domain == "010":
        return "Power Down" if num.startswith(("1.7.1", "1.7.2")) else f"未歸類 010 §{num}"
    if num.startswith("1.6.2.1."):
        parts = num.split(".")
        k = int(parts[4]) if len(parts) > 4 else 0
        if 1 <= k <= 15:
            return "Power State"
        if k == 16:
            return "Startup Display"
        return f"未歸類 009 §{num}"
    prefixes = [
        ("1.3.5", "Startup Display"), ("1.9.8", "Startup Display"),
        ("1.9.9", "Startup Display"), ("1.9.10", "Startup Display"),
        ("1.9.15", "Branding and Theme"), ("1.9.16", "Branding and Theme"),
        ("1.9.17", "Branding and Theme"),
        ("1.6.3", "Timeout Settings"), ("1.6.4", "Timeout Settings"),
        ("1.6.7", "Timeout Settings"),
        ("1.7.1", "Power State"), ("1.8.1", "Power State"),
        ("1.9.3", "Power State"), ("1.9.4", "Power State"),
        ("1.9.5", "Power State"), ("1.9.12", "Power State"),
    ]
    for prefix, name in prefixes:
        if num == prefix or num.startswith(prefix + "."):
            return name
    return f"未歸類 009 §{num}"


def main() -> None:
    rows = [
        line.split("\t")
        for line in (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()[1:]
        if line.strip()
    ]
    chapters: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for leaf, cfts, num, *_ in rows:
        chapters[leaf].append((cfts, num))

    assigned: dict[str, tuple[str, str]] = {}
    ambiguous = []
    unmapped: dict[str, list[str]] = defaultdict(list)
    for leaf, chs in chapters.items():
        raw = {test_set_of(d, n) for d, n in chs}
        # 「未歸類」表示 §E Layer 3 清單未涵蓋該章節，不是一個 Test Set 候選。
        # 逐一登記，但不參與歧義判定 —— 否則會把「清單缺漏」誤報為「待裁」。
        for label in raw:
            if label.startswith("未歸類"):
                unmapped[label].append(leaf)
        candidates = {x for x in raw if not x.startswith("未歸類")}
        if leaf in RULED_MULTI:
            ts, ruling = RULED_MULTI[leaf]
            assigned[leaf] = (ts, ruling)
            print(f"  裁定 {leaf}: {ts}（{ruling}），候選 = {sorted(raw)}")
        elif len(candidates) == 1:
            assigned[leaf] = (candidates.pop(), "R-P15(a)" if len(chs) == 1 else "多章節但 Test Set 無歧義")
        else:
            ambiguous.append((leaf, sorted(candidates)))

    if unmapped:
        print("\n§E Layer 3 清單未涵蓋之章節（登記，不參與指派）：")
        for label, leaves in sorted(unmapped.items()):
            print(f"  {label}  ← {len(leaves)} leaf: {sorted(leaves)}")

    if ambiguous:
        for leaf, cands in ambiguous:
            print(f"  **未裁定且跨 Test Set**: {leaf} → {cands}")
        raise SystemExit("有 leaf 跨多個 Test Set 且未經裁定；依 R-P15(b) 不得自動指派，停止。")

    counts = Counter(ts for ts, _ in assigned.values())

    print(f"\nG22 逐條裁定驗證：")
    for leaf, (ts, ruling) in RULED_MULTI.items():
        got = assigned[leaf][0]
        print(f"  {leaf:12} → {got:18} 期望 {ts:18} "
              f"{'PASS' if got == ts else '**MISMATCH**'}  （{ruling}）")

    print(f"\nG21 §E 定版分布（R-P35）：")
    ok = True
    for name, expected in LOCKED.items():
        got = counts.get(name, 0)
        flag = "PASS" if got == expected else "**MISMATCH**"
        ok &= got == expected
        print(f"  {name:20} 實測 {got:>3}  定版 {expected:>3}  {flag}")
    stray = {k: v for k, v in counts.items() if k not in LOCKED}
    if stray:
        ok = False
        print(f"  **未歸類**: {stray}")
    print(f"  合計 {sum(counts.values())}  定版 114  "
          f"{'PASS' if sum(counts.values()) == 114 else '**MISMATCH**'}")
    print(f"\nG21 整體: {'PASS' if ok and sum(counts.values()) == 114 else '**MISMATCH**'}")

    out = DATA / "leaf_testset.tsv"
    out.write_text(
        "leaf\ttest_set\t依據\n" + "\n".join(
            f"{leaf}\t{ts}\t{why}"
            for leaf, (ts, why) in sorted(
                assigned.items(), key=lambda kv: int(re.match(r"SWE-PM-(\d+)", kv[0]).group(1))
            )
        ) + "\n",
        encoding="utf-8",
    )
    print(f"\nwrote {out.relative_to(ROOT)} — {len(assigned)} 列")


if __name__ == "__main__":
    main()
