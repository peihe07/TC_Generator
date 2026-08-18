"""第四批素材（R-P174）—— `SWE-PM-033`–`063` 之逐字原文。

R-P174 令第四批為 `SWE-PM-033`–`063`（31 leaf）。
**其中 6 leaf 已於第二批產出**（`038` / `057` / `060`–`063`，Timeout Settings），
故實際待產出者為 **25 leaf**（見上繳 §五之落差回報）。

本腳本自 `layer3_full.tsv` 取各 leaf 之章節與 item，
自 CFTS 文字層（`lint_tcs.anchor_bodies()`，R-P17）取**逐字原文**，
供 TC 撰寫。`source_clause` 即由此串接而成（G94 逐字比對之對象）。

用法：
    python features/power/scripts/build_b4_material.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from protect_products import guard_write  # R-P233：(c) 型產物之寫入保護
from lint_tcs import anchor_bodies  # noqa: E402

RANGE = [f"SWE-PM-{i:03d}" for i in range(33, 64)]


def layer3() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    rows = (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()
    head = rows[0].split("\t")
    for line in rows[1:]:
        r = dict(zip(head, line.split("\t")))
        out.setdefault(r["leaf"], []).append(r)
    return out


def already_done() -> dict[str, str]:
    out = {}
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        for leaf in b.get("leaves", []):
            out[leaf["parent"]] = b.get("batch", "?")
    return out


def main() -> None:
    l3, done, bodies = layer3(), already_done(), anchor_bodies()
    todo = [x for x in RANGE if x not in done]
    out = ["# 第四批素材（R-P174）—— 逐字原文\n",
           f"\n> R-P174 之範圍 `SWE-PM-033`–`063` 共 **{len(RANGE)}** leaf；\n",
           f"> **已於第二批產出者 {len(RANGE) - len(todo)}**"
           f"（{'、'.join('`' + x + '`' for x in RANGE if x in done)}），\n",
           f"> **本批實際待產出 {len(todo)} leaf**。落差見上繳 §五。\n",
           "\n> 原文取自 CFTS 文字層（R-P17），**未經任何改寫**；"
           "`source_clause` 即此串接（G94 之比對對象）。\n"]
    for leaf in todo:
        rows = l3.get(leaf, [])
        anchors = [a for r in rows for a in r["item_ids"].split(",") if a]
        present = [a for a in anchors if bodies.get(a)]
        missing = [a for a in anchors if not bodies.get(a)]
        secs = sorted({r["chapter_num"] for r in rows})
        clause = "\n".join("\n".join(bodies[a]) for a in present)
        out.append(f"\n## `{leaf}` —— 章節 {'、'.join(secs)}"
                   f"（item {len(anchors)}，有內文 {len(present)}"
                   f"{'，**無內文 ' + str(len(missing)) + '**' if missing else ''}）\n\n"
                   f"- 錨點：`{','.join(present)}`\n")
        if missing:
            out.append(f"- **文字層無內文之錨點：`{','.join(missing)}`** —— "
                       "依 R-P144(b) 須停並上繳，不得以殘缺原文成條\n")
        out.append(f"\n```\n{clause}\n```\n")
    guard_write(DATA / "b4_material.md") or (DATA / "b4_material.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'b4_material.md').relative_to(ROOT)}")
    print(f"  範圍 {len(RANGE)}、已產出 {len(RANGE)-len(todo)}、待產出 {len(todo)}")
    for leaf in todo:
        rows = l3.get(leaf, [])
        anchors = [a for r in rows for a in r["item_ids"].split(",") if a]
        miss = [a for a in anchors if not bodies.get(a)]
        flag = f"  **無內文 {miss}**" if miss else ""
        print(f"    {leaf}: item {len(anchors)}{flag}")


if __name__ == "__main__":
    main()
