"""B1 — 懸空 `WrapperResource` 參照之 leaf 層交叉（R-P45 / G29）。

05 包 G24 已測得 31 處懸空參照分布於 16 章，但未知牽連幾個 leaf、
幾個被引用錨點。本腳本補齊 leaf 層影響面。

歸屬規則：一處懸空參照歸屬於**其位置之前最近之需求錨點**
（與 §C rule 2 之「需求錨點歸屬於其前最近之章節錨點」同構）。
若該處位於章節錨點之後、任何需求錨點之前，則無所屬錨點，明示為「不可判定」。

**不解析任何 RTF 或 OLE stream 之內容**（R-P39 / R-P48）。

用法：
    python features/power/scripts/build_dangling.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

WRAPPER_RE = re.compile(r"(\S+?\.(?:rtf|xlsx|xls|docx|doc))\s+WrapperResource", re.I)

# R-P55 回歸斷言（06 包 G29 基線）
EXPECTED_HITS = 31
EXPECTED_CHAPTERS = 16
EXPECTED_ANCHORS = 2
EXPECTED_LEAVES = 9


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def scan(path: Path, tag: str) -> list[dict]:
    """逐段掃描，記錄每一處 WrapperResource 及其所在章節與所屬錨點。"""
    hits = []
    chapter = ("（章節錨點之前）", "")
    anchor = None
    for plain, bold in paragraphs(path):
        m = SEC_RE.match(plain)
        if m:
            chapter = (m.group(1), m.group(2))
            anchor = None
            continue
        found = REQ_RE.findall(bold)
        if found:
            anchor = found[0]
        for occurrence in range(plain.count("WrapperResource")):
            names = WRAPPER_RE.findall(plain)
            hits.append({
                "cfts": tag,
                "chapter": chapter[0],
                "title": chapter[1],
                "anchor": anchor,
                "resource": names[occurrence] if occurrence < len(names) else "（無法解析檔名）",
            })
    return hits


def cited_map() -> tuple[dict[str, list[str]], dict[str, str]]:
    """item id → 引用之 leaf；leaf → Test Set。"""
    cited: dict[str, list[str]] = defaultdict(list)
    for line in (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        for item in parts[5].split(","):
            if parts[0] not in cited[item]:
                cited[item].append(parts[0])
    test_set = {}
    for line in (DATA / "leaf_testset.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            leaf, ts, _ = line.split("\t")
            test_set[leaf] = ts
    return cited, test_set


def leaf_key(leaf: str) -> int:
    m = re.match(r"SWE-PM-(\d+)", leaf)
    return int(m.group(1)) if m else 10**9


def main() -> None:
    cited, test_set = cited_map()
    hits = (scan(find("CFTS_009_Wake-up"), "009")
            + scan(next(x for x in IN.iterdir() if x.suffix == ".doc"), "010"))

    affected_anchors: set[str] = set()
    affected_leaves: set[str] = set()
    for h in hits:
        leaves = cited.get(h["anchor"], []) if h["anchor"] else []
        h["leaves"] = sorted(leaves, key=leaf_key)
        h["cited"] = bool(leaves)
        if leaves:
            affected_anchors.add(h["anchor"])
            affected_leaves.update(leaves)

    ts_dist = Counter(test_set.get(l, "（未指派）") for l in affected_leaves)
    per_chapter = Counter((h["cfts"], h["chapter"]) for h in hits)

    out = [
        "# B1 — 懸空 `WrapperResource` 參照之 leaf 層交叉（R-P45 / G29）\n",
        "\n> 05 包 G24 測得 31 處分布於 16 章，未知 leaf 層影響面。本檔補齊。\n",
        "> 歸屬規則：一處參照歸屬於其位置之前最近之**需求錨點**"
        "（與 §C rule 2 同構）；位於章節錨點後、任何需求錨點前者，明示為「不可判定」。\n",
        "> **不解析任何 RTF 或 OLE stream 之內容**（R-P39 / R-P48）。\n",
        "> 產生指令：`python features/power/scripts/build_dangling.py`\n",
        f"\n## 1. 彙總（G29）\n\n| 指標 | 實測 |\n|---|---|\n",
        f"| 懸空參照總處數 | **{len(hits)}** |\n",
        f"| ├ CFTS009 | {sum(1 for h in hits if h['cfts'] == '009')} |\n",
        f"| └ CFTS010 | {sum(1 for h in hits if h['cfts'] == '010')} |\n",
        f"| 分布章節數 | **{len(per_chapter)}** |\n",
        f"| 可歸屬至某需求錨點者 | {sum(1 for h in hits if h['anchor'])} |\n",
        f"| 不可判定（無所屬錨點） | {sum(1 for h in hits if not h['anchor'])} |\n",
        f"| **受影響之被引用錨點數** | **{len(affected_anchors)}** |\n",
        f"| **受影響之 leaf 數** | **{len(affected_leaves)}** / 114 |\n",
    ]
    out.append(f"\n**受影響之 leaf 清單**："
               f"{', '.join('`' + l + '`' for l in sorted(affected_leaves, key=leaf_key)) or '無'}\n")
    out.append("\n**受影響之 Test Set 分布**：\n\n| Test Set | 受影響 leaf 數 |\n|---|---|\n")
    for ts, n in ts_dist.most_common():
        out.append(f"| {ts} | {n} |\n")

    out.append("\n## 2. 逐處明細（31 處）\n\n")
    out.append("| # | CFTS | 章節 | 章節標題 | 所屬錨點 | 被引用 | 引用之 leaf | 參照之資源檔名 |\n")
    out.append("|---|---|---|---|---|---|---|---|\n")
    for i, h in enumerate(hits, 1):
        out.append(
            f"| {i} | {h['cfts']} | §{h['chapter']} | {h['title'][:34]} | "
            f"{'`' + h['anchor'] + '`' if h['anchor'] else '**不可判定**'} | "
            f"{'**是**' if h['cited'] else '否'} | "
            f"{', '.join('`' + l + '`' for l in h['leaves']) or '—'} | "
            f"`{h['resource']}` |\n"
        )

    out.append("\n## 3. 逐章彙總\n\n| CFTS | 章節 | 標題 | 參照處數 | 受影響之被引用錨點 | 受影響 leaf 數 |\n")
    out.append("|---|---|---|---|---|---|\n")
    for (cfts, chapter), n in sorted(per_chapter.items()):
        rows = [h for h in hits if h["cfts"] == cfts and h["chapter"] == chapter]
        anchors = sorted({h["anchor"] for h in rows if h["cited"]})
        leaves = sorted({l for h in rows for l in h["leaves"]}, key=leaf_key)
        out.append(
            f"| {cfts} | §{chapter} | {rows[0]['title'][:34]} | {n} | "
            f"{', '.join('`' + a + '`' for a in anchors) or '—'} | {len(leaves)} |\n"
        )

    path = DATA / "b1_dangling_refs.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G29 懸空參照 {len(hits)} 處 / {len(per_chapter)} 章；"
          f"受影響被引用錨點 {len(affected_anchors)}、leaf {len(affected_leaves)} / 114")
    print(f"  Test Set 分布：{dict(ts_dist)}")
    print(f"  受影響 leaf：{sorted(affected_leaves, key=leaf_key)}")

    # R-P55 回歸斷言
    problems = []
    for label, got, want in [("處數", len(hits), EXPECTED_HITS),
                             ("章節數", len(per_chapter), EXPECTED_CHAPTERS),
                             ("受影響被引用錨點", len(affected_anchors), EXPECTED_ANCHORS),
                             ("受影響 leaf", len(affected_leaves), EXPECTED_LEAVES)]:
        if got != want:
            problems.append(f"{label} {got} ≠ 期望 {want}")
    if problems:
        print("\n**回歸斷言失敗（R-P55）**：" + "；".join(problems))
        raise SystemExit(1)
    print("\n回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
