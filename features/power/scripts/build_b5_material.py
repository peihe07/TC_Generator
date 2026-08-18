"""第五批素材（R-P181）—— 逐字原文。

範圍**取自 G121 對帳表**（`data/leaf_batch_reconciliation.tsv`），
依 R-P177(b) **不以 ID 區間表述**：
  （a）Power State 之未產出且未受阻斷者
  （b）Startup Display 全 24 leaf，扣除已於第四批產出之 4 個（R-P177(a) 不重做）
  （c）依 R-P165 扣除撞上 live DR 影響面者，排除清單列明 DR 編號
  （d）`SWE-PM-001`–`010` 不納入（R-P168；其於對帳表中皆為阻斷狀態）

素材前置檢查依 R-P172：於產出前先驗**素材本身** ——
全部 item 於 CFTS 文字層須有內文，缺者依 R-P144(b) 停並上繳。

用法：
    python features/power/scripts/build_b5_material.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402

RECON = DATA / "leaf_batch_reconciliation.tsv"


def scope() -> tuple[list[str], list[tuple[str, str, str]]]:
    """回傳（納入之 leaf 全集、排除清單）。排除清單為 (leaf, test_set, 理由)。"""
    rows = list(csv.DictReader(RECON.open(encoding="utf-8"), delimiter="\t"))
    include, excluded = [], []
    for r in rows:
        ts, leaf = r["test_set"], r["leaf"]
        if ts not in ("Power State", "Startup Display"):
            continue
        if r["batch"] != "未產出":
            if ts == "Startup Display":
                excluded.append((leaf, ts, f"已於第 {r['batch']} 批產出（R-P177(a) 不重做）"))
            continue
        if r["blocking_dr"] != "—":
            excluded.append((leaf, ts, f"受阻斷：{r['blocking_dr']}"))
            continue
        if r["advisory_dr"] != "—":
            excluded.append((leaf, ts,
                             f"撞上 live DR 影響面：{r['advisory_dr']}（R-P165 / R-P181(c)）"))
            continue
        include.append(leaf)
    return include, excluded


def layer3() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    lines = (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t")
    for line in lines[1:]:
        r = dict(zip(head, line.split("\t")))
        out.setdefault(r["leaf"], []).append(r)
    return out


def main() -> None:
    include, excluded = scope()
    l3, bodies = layer3(), anchor_bodies()
    ts = {r["leaf"]: r["test_set"]
          for r in csv.DictReader(RECON.open(encoding="utf-8"), delimiter="\t")}

    out = ["# 第五批素材（R-P181）—— 逐字原文\n",
           "\n> 範圍取自 **G121 對帳表**，依 R-P177(b) **逐一列出 leaf ID 全集，"
           "不以區間表述**。\n",
           f"\n## 納入 —— **{len(include)} leaf**\n\n",
           "".join(f"`{x}` " for x in include), "\n",
           f"\n## 排除 —— {len(excluded)} leaf\n\n"
           "| leaf | Test Set | 理由 |\n|---|---|---|\n"]
    for leaf, t, why in excluded:
        out.append(f"| `{leaf}` | {t} | {why} |\n")

    out.append("\n## 素材前置檢查（R-P172）\n\n")
    blocked = []
    for leaf in include:
        anchors = [a for r in l3.get(leaf, []) for a in r["item_ids"].split(",") if a]
        miss = [a for a in anchors if not bodies.get(a)]
        if miss:
            blocked.append((leaf, miss))
    if blocked:
        out.append("| leaf | 文字層無內文之 item |\n|---|---|\n")
        for leaf, miss in blocked:
            out.append(f"| `{leaf}` | **{'、'.join(miss)}** |\n")
        out.append("\n**依 R-P144(b) 停並上繳，該等 leaf 不得以殘缺原文成條。**\n")
    else:
        out.append("**全部 item 於 CFTS 文字層皆有內文，無 R-P144(b) 之阻斷情形。**\n")

    out.append("\n## 逐字原文\n")
    for leaf in include:
        rows = l3.get(leaf, [])
        anchors = [a for r in rows for a in r["item_ids"].split(",") if a]
        present = [a for a in anchors if bodies.get(a)]
        secs = sorted({r["chapter_num"] for r in rows})
        cfts = sorted({r["cfts"] for r in rows})
        clause = "\n".join("\n".join(bodies[a]) for a in present)
        out.append(f"\n### `{leaf}` —— {ts[leaf]}；CFTS {'、'.join(cfts)}；"
                   f"章節 {'、'.join(secs)}（item {len(anchors)}）\n\n"
                   f"- 錨點：`{','.join(present)}`\n\n```\n{clause}\n```\n")

    (DATA / "b5_material.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'b5_material.md').relative_to(ROOT)}")
    print(f"  納入 {len(include)} leaf、排除 {len(excluded)} leaf")
    print(f"  素材前置檢查：{'**' + str(len(blocked)) + ' leaf 受阻**' if blocked else '全數有內文'}")
    for leaf in include:
        anchors = [a for r in l3.get(leaf, []) for a in r["item_ids"].split(",") if a]
        print(f"    {leaf} ({ts[leaf]}): item {len(anchors)}")


if __name__ == "__main__":
    main()
