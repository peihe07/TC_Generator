"""B1 — R-P42 黑名單之自動導出（R-P52(c) / G32）。

R-P42：某 leaf 之 TC 範圍上界為其 `Source Requirement ID` 所實際引用之需求錨點；
未被引用之錨點一律不測。本腳本導出「未被任何 leaf 引用之需求錨點」全集，
供 lint 於 Phase 4 作機械檢查。

**R-P52(c)：黑名單不得人工維護** —— 全集自 `layer3_full.tsv`（被引用集）
與兩份 CFTS 之全部需求錨點導出，故 leaf 增修時自動跟隨。

輸出 `data/unreferenced_anchors.tsv`：
    anchor_id / cfts / chapter_num / chapter_title / chapter_touched / risk_tier

其中 `chapter_touched` = 該錨點所屬章節是否被任一 leaf 觸及
（True 表示同章有其他錨點被引用 —— 這類最容易被誤納）。

`risk_tier`（R-P63）：

    1 = 所屬章節被觸及，**且其父節亦被觸及** —— 最高風險
    2 = 所屬章節被觸及，但父節未被觸及
    3 = 所屬章節未被觸及

> **條文用語之歧義與本包之讀法（執行層登記）**：R-P63 寫
> 「第一層：與任一被引用錨點**同章且同一父節**者」。但「同章」已蘊含「同一父節」，
> 二者若同義則 315 個全屬第一層，第二層將為空集 —— 與條文「分兩層」不符。
> 故本包讀為：第一層額外要求**父節本身亦含被引用錨點**。
> 此讀法滿足條文之計數約束（tier 1 + tier 2 = 315、tier 3 = 499）。
> 若分析層原意不同，請於 09 包訂正。

用法：
    python features/power/scripts/build_blacklist.py
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

# A-PW27 所人工登記者（九章內之子集），用於對照
APW27 = {
    "4941399", "4941429",
    "4941452", "4941454", "4941455", "4941456", "4941457", "4941458", "4941459",
    "4941661", "4941662",
    "4941813", "4941816",
}


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def all_anchors() -> list[tuple[str, str, str, str]]:
    """兩份 CFTS 之全部需求錨點：(anchor_id, cfts, chapter_num, chapter_title)。"""
    out = []
    for tag, path in [("009", find("CFTS_009_Wake-up")),
                      ("010", next(x for x in IN.iterdir() if x.suffix == ".doc"))]:
        chapter = ("（章節錨點之前）", "")
        for plain, bold in paragraphs(path):
            m = SEC_RE.match(plain)
            if m:
                chapter = (m.group(1), m.group(2))
                continue
            for anchor in REQ_RE.findall(bold):
                out.append((anchor, tag, chapter[0], chapter[1]))
    return out


def parent_of(num: str) -> str:
    """章節號之父節（`1.6.2.1.9` → `1.6.2.1`）。頂層回傳空字串。"""
    return num.rsplit(".", 1)[0] if "." in num else ""


def cited_anchors() -> tuple[set[str], set[tuple[str, str]]]:
    """被引用之 anchor id 集合，以及被觸及之 (cfts, chapter) 集合。"""
    anchors: set[str] = set()
    chapters: set[tuple[str, str]] = set()
    for line in (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        chapters.add((parts[1], parts[2]))
        anchors.update(parts[5].split(","))
    return anchors, chapters


def main() -> None:
    everything = all_anchors()
    cited, touched_chapters = cited_anchors()

    unreferenced = [a for a in everything if a[0] not in cited]
    rows = []
    for anchor, cfts, num, title in unreferenced:
        touched = (cfts, num) in touched_chapters
        if not touched:
            tier = "3"
        elif (cfts, parent_of(num)) in touched_chapters:
            tier = "1"
        else:
            tier = "2"
        rows.append((anchor, cfts, num, title, str(touched), tier))

    path = DATA / "unreferenced_anchors.tsv"
    path.write_text(
        "anchor_id\tcfts\tchapter_num\tchapter_title\tchapter_touched\trisk_tier\n"
        + "\n".join("\t".join(r) for r in rows) + "\n",
        encoding="utf-8",
    )

    in_touched = [r for r in rows if r[4] == "True"]
    ids = {r[0] for r in rows}
    missing_from_full = APW27 - ids
    extra_vs_apw27 = len(ids) - len(APW27 & ids)

    print(f"wrote {path.relative_to(ROOT)} — {len(rows)} 列")
    print(f"G32 黑名單全集：")
    print(f"  全部需求錨點            {len(everything)}（009 {sum(1 for a in everything if a[1] == '009')}"
          f" + 010 {sum(1 for a in everything if a[1] == '010')}）")
    print(f"  被引用                  {len(cited & {a[0] for a in everything})}")
    print(f"  **未被引用（黑名單）**  {len(rows)}")
    print(f"  其中所屬章節被觸及者    {len(in_touched)}  ← 最易被誤納")
    print(f"  其中所屬章節未被觸及者  {len(rows) - len(in_touched)}")
    tiers = Counter(r[5] for r in rows)
    print(f"\n  G43 風險分層（R-P63）：")
    for t, label in [("1", "同章且父節亦被觸及 —— 最高風險"),
                     ("2", "同章但父節未被觸及"),
                     ("3", "所屬章節未被觸及")]:
        print(f"    tier {t}  {tiers.get(t, 0):>4}  {label}")
    print(f"    合計 {sum(tiers.values())}（須 = {len(rows)}）")

    print(f"\n  與 A-PW27 之 13 個對照：")
    print(f"    A-PW27 之 13 個是否全在全集內：{'是' if not missing_from_full else '否 ' + str(missing_from_full)}")
    print(f"    全集比 A-PW27 多 {extra_vs_apw27} 個")


if __name__ == "__main__":
    main()
