#!/usr/bin/env python3
"""T17a（下放包 11 §一 R-DD14）—— 為 `RULINGS.md` 之每一圍籬條文加標題錨點。

**加標題為新增行，非對條文本體之刪改**（R-DD14(b)）：
圍籬符號與其內文字一字不動。本檔以「移除所插入之行後，須與改動前
逐位元全等」為證，非以目視。

錨點形制（R-DD14(a)）：現行版 `## R-DDn`；留存版 `## R-DDn v1`，
其標題文字與索引表之留存列一致。

`--apply` 方寫入；預設為 dry-run。**只動 driver_distraction 一檔**（§二）。
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "RULINGS.md"

# 圍籬起首之條文標題行 → 錨點文字
RE_OPEN = re.compile(r"^```$")
RE_HEAD = re.compile(r"^(R-DD\d+(?: v\d)?)（")

# R-DD14(a) 之明示對照 —— **不由圍籬首行推導**。
# 該條明定：現行版為裸 `## R-DDn`；**留存版**加 `## R-DDn v1`，
# 且其標題文字須與索引表之留存列（`R-DD6`（v1））一致。
# 圍籬首行之字面恰與此相反（v1 之首行為 `R-DD6（…）`、v2 之首行為
# `R-DD6 v2（…）`），故若由首行推導會得出相反之結果。
ANCHOR_OVERRIDE = {
    "R-DD6": "R-DD6 v1",     # 留存版（圍籬首行 `R-DD6（訊號名之架構軸）`）
    "R-DD6 v2": "R-DD6",     # 現行版（圍籬首行 `R-DD6 v2（訊號名之架構軸）`）
    # 下放包 17 §二 → 19 §二：R-DD20 已成 v1／v2／v3 三版
    "R-DD20": "R-DD20 v1",      # 留存（圍籬首行 `R-DD20（…丁案…）`）
    "R-DD20 v2": "R-DD20 v2",   # 留存（識別式，與 R-DD6 之二版式不同）
    "R-DD20 v3": "R-DD20",      # 現行版（圍籬首行 `R-DD20 v3（…）`）
    # 下放包 22 §二：R-DD26 成 v1／v2 二版
    "R-DD26": "R-DD26 v1",      # 留存（圍籬首行 `R-DD26（…）`）
    "R-DD26 v2": "R-DD26",      # 現行版（圍籬首行 `R-DD26 v2（…）`）
}


def plan(lines):
    """回傳 [(插入位置索引, 錨點文字)]；位置為該 ``` 行之索引。"""
    out = []
    for i, l in enumerate(lines):
        if not RE_OPEN.match(l):
            continue
        if i + 1 >= len(lines):
            continue
        m = RE_HEAD.match(lines[i + 1])
        if m:
            out.append((i, ANCHOR_OVERRIDE.get(m.group(1), m.group(1))))
    return out


def build(lines, ins):
    """自後往前插入，避免位移。插入內容固定為 `## <id>` ＋ 一空行。"""
    new = list(lines)
    for i, anchor in reversed(ins):
        new[i:i] = [f"## {anchor}", ""]
    return new


def strip_back(new_lines, ins):
    """把插入之行移除，還原為改動前之形。用於逐位元回證。"""
    drop = set()
    off = 0
    for i, _ in ins:
        drop.add(i + off)
        drop.add(i + off + 1)
        off += 2
    return [l for k, l in enumerate(new_lines) if k not in drop]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    orig = TARGET.read_text("utf-8")
    lines = orig.split("\n")
    ins = plan(lines)

    print("=" * 74)
    print(f"T17a —— {TARGET.relative_to(ROOT.parent.parent)}")
    print("=" * 74)
    print(f"擬加錨點 {len(ins)} 個：")
    for i, a in ins:
        print(f"  行 {i + 1:>4}  ## {a}")

    new_lines = build(lines, ins)
    new = "\n".join(new_lines)

    # ── 回證一：移除所插入之行後，須與原檔逐位元全等 ──────────────
    back = "\n".join(strip_back(new_lines, ins))
    same = (back == orig)
    print(f"\n[回證 1] 移除插入行後與原檔逐位元比對："
          f"{'全等 ✓' if same else '**不等 ✗**'}")
    print(f"          原檔 sha256 {hashlib.sha256(orig.encode()).hexdigest()[:16]}")
    print(f"          還原   sha256 {hashlib.sha256(back.encode()).hexdigest()[:16]}")
    if not same:
        for k, (a, b) in enumerate(zip(orig.split("\n"), back.split("\n"))):
            if a != b:
                print(f"          首處差異於行 {k + 1}：{a!r} vs {b!r}")
                break
        return 1

    # ── 回證二：新增之行全部為 `## R-DD…` 或空行，且無刪除、無改寫 ──
    import difflib
    diff = list(difflib.unified_diff(lines, new_lines, lineterm="", n=0))
    removed = [l for l in diff if l.startswith("-") and not l.startswith("---")]
    added = [l[1:] for l in diff if l.startswith("+") and not l.startswith("+++")]
    bad = [a for a in added if a != "" and not re.fullmatch(r"## R-DD\d+(?: v\d)?", a)]
    print(f"[回證 2] diff：刪除 {len(removed)} 行／新增 {len(added)} 行")
    print(f"          新增行中非「錨點或空行」者：{bad or '無'}")
    print(f"          條文本體之差異：{'0 ✓' if not removed and not bad else '**有 ✗**'}")
    if removed or bad:
        return 1

    # ── 回證三：圍籬與其內文字之字元數不變 ────────────────────────
    def fenced(s):
        return "".join(re.findall(r"^```\n(.*?)\n```$", s, re.S | re.M))
    fo, fn = fenced(orig), fenced(new)
    print(f"[回證 3] 圍籬內文字：原 {len(fo)} 字元／新 {len(fn)} 字元；"
          f"{'逐字元全等 ✓' if fo == fn else '**不等 ✗**'}")
    if fo != fn:
        return 1

    if args.apply:
        TARGET.write_text(new, "utf-8")
        print(f"\n**已寫入** —— {len(ins)} 錨點")
    else:
        print("\n（dry-run；加 --apply 方寫入）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
