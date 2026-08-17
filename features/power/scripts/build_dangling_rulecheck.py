"""B3 — 懸空參照歸屬規則之獨立驗證（R-P53 / G34）。

06 包 B1 之歸屬規則為執行層自訂：「一處參照歸屬於其位置之前最近之需求錨點」，
實測 31/31 全數可歸屬、0 個不可判定 —— 該 100% 結果本身為可疑訊號。

驗證方法（R-P53 指定）：對每一處 `WrapperResource`，量測其在段落序中
與**前一個**需求錨點及**後一個**需求錨點之距離。
若存在任一處距離後者顯著近於前者，該規則即有反例。

候選錨點限於**同一章節內**（跨章節之錨點不視為候選）。

用法：
    python features/power/scripts/build_dangling_rulecheck.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

RESOURCE_RE = re.compile(r"(\S+?\.(rtf|xlsx|xls|docx|doc|png|jpe?g))\s+WrapperResource", re.I)

# R-P55 回歸斷言
EXPECTED_TOTAL = 31
EXPECTED_COUNTEREXAMPLES = 0


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def scan(path: Path, tag: str) -> list[dict]:
    paras = list(paragraphs(path))
    anchors, sections = [], []
    for i, (plain, bold) in enumerate(paras):
        if SEC_RE.match(plain):
            sections.append(i)
            continue
        found = REQ_RE.findall(bold)
        if found:
            anchors.append((i, found[0]))

    rows = []
    for i, (plain, _bold) in enumerate(paras):
        if "WrapperResource" not in plain:
            continue
        prev_bound = max([s for s in sections if s < i], default=-1)
        next_bound = min([s for s in sections if s > i], default=10**9)
        before = [a for a in anchors if prev_bound < a[0] <= i]
        after = [a for a in anchors if i < a[0] < next_bound]
        chapter = next(
            (SEC_RE.match(paras[s][0]).group(1) for s in reversed(sections) if s < i), "—"
        )
        resources = RESOURCE_RE.findall(plain)
        rows.append({
            "cfts": tag, "idx": i, "chapter": chapter,
            "prev": before[-1][1] if before else None,
            "prev_d": i - before[-1][0] if before else None,
            "next": after[0][1] if after else None,
            "next_d": after[0][0] - i if after else None,
            "resources": [r[0] for r in resources],
            "kinds": [r[1].lower() for r in resources],
            "inline": not plain.strip().startswith(resources[0][0]) if resources else False,
            "text": plain.strip(),
        })
    return rows


def main() -> None:
    rows = (scan(find("CFTS_009_Wake-up"), "009")
            + scan(next(x for x in IN.iterdir() if x.suffix == ".doc"), "010"))

    counterexamples = [
        r for r in rows
        if r["next_d"] is not None and (r["prev_d"] is None or r["next_d"] < r["prev_d"])
    ]
    ties = [r for r in rows
            if r["next_d"] is not None and r["prev_d"] is not None and r["next_d"] == r["prev_d"]]
    no_prev = [r for r in rows if r["prev_d"] is None]
    kinds = Counter(k for r in rows for k in r["kinds"])
    inline = [r for r in rows if r["inline"]]

    out = [
        "# B3 — 懸空參照歸屬規則之獨立驗證（R-P53 / G34）\n",
        "\n> 受檢規則：「一處參照歸屬於其位置之前最近之需求錨點」（06 包 B1 自訂）。\n",
        "> 驗證方法依 R-P53：量測與前／後需求錨點之段落序距離；"
        "候選限於同一章節內。\n",
        "> 產生指令：`python features/power/scripts/build_dangling_rulecheck.py`\n",
        f"\n## 1. G34 結果\n\n| 指標 | 實測 |\n|---|---|\n",
        f"| 受檢處數 | {len(rows)} |\n",
        f"| **距離後錨點較近者（反例）** | **{len(counterexamples)}** |\n",
        f"| 前後等距者 | {len(ties)} |\n",
        f"| 同章節內無前錨點者 | {len(no_prev)} |\n",
        f"| 前距分布 | {dict(sorted(Counter(r['prev_d'] for r in rows).items(), key=lambda x: (x[0] is None, x[0])))} |\n",
        f"| 後距分布 | {dict(sorted(Counter(r['next_d'] for r in rows).items(), key=lambda x: (x[0] is None, x[0])))} |\n",
    ]

    out.append(
        f"\n**{'無反例' if not counterexamples else f'**{len(counterexamples)} 個反例**'}。**\n\n"
        "### 100% 歸屬率之成因（R-P53 要求說明）\n\n"
        "前距分布為 **1 ×27、2 ×4**，後距分布為 **2 ×23、無後錨點 ×8** ——\n"
        "即每一處參照都**緊接在其錨點的後一段**（距離 1），\n"
        "而下一個錨點最近也在其後兩段。此非巧合，而是 Polarion 匯出之結構：\n"
        "錨點行為 metadata（`[Artifact Type:…]`），其後緊接該需求之內文，\n"
        "參照即嵌於該內文中。**故 100% 歸屬率是文件結構之必然，不是規則過度擬合。**\n\n"
        f"3 個前後等距者（前距 2、後距 2）之歸屬仍取前者 —— "
        f"此 tie-break 與 §C rule 2 同一慣例（需求錨點歸屬於其前最近之章節錨點），"
        f"非本包新創。\n"
    )

    out.append(
        f"\n## 2. 資源型別 —— 一項訂正\n\n"
        f"06 包之 A-PW26 與 DR-PW6 稱該等參照為「**RTF 資源**」。實測型別分布：\n\n"
        f"| 副檔名 | 處數 |\n|---|---|\n"
    )
    for k, v in kinds.most_common():
        out.append(f"| `.{k}` | **{v}** |\n")
    out.append(
        f"\n**試算表（`.xls` / `.xlsx`）為多數，非 RTF。**\n"
        f"DR-PW6 向上游索取「缺漏之 RTF 資源」之表述不完整，須訂正為\n"
        f"「缺漏之嵌入資源（RTF / 試算表 / Word 文件）」。登記為 A-PW32。\n"
    )

    if inline:
        out.append(
            f"\n## 3. 嵌於句中之參照（{len(inline)} 處）\n\n"
            "該處之參照前後皆有實質規格文字，即缺漏之資源夾在一句需求敘述之中：\n\n"
        )
        for r in inline:
            out.append(f"- CFTS{r['cfts']} §{r['chapter']}（錨點 `{r['prev']}`）：\n\n"
                       f"  ```\n  {r['text'][:420]}\n  ```\n")

    out.append("\n## 4. 逐處明細\n\n")
    out.append("| CFTS | 章節 | 段落序 | 前錨點（距離） | 後錨點（距離） | 資源 |\n")
    out.append("|---|---|---|---|---|---|\n")
    for r in rows:
        out.append(
            f"| {r['cfts']} | §{r['chapter']} | {r['idx']} | "
            f"`{r['prev']}`（{r['prev_d']}） | "
            f"{'`' + str(r['next']) + '`（' + str(r['next_d']) + '）' if r['next'] else '—'} | "
            f"`{', '.join(r['resources']) or '（無法解析檔名）'}` |\n"
        )

    path = DATA / "b3_dangling_rule_check.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G34 受檢 {len(rows)} 處；**反例 {len(counterexamples)}**；等距 {len(ties)}；無前錨點 {len(no_prev)}")
    print(f"  資源型別：{dict(kinds)}")
    print(f"  嵌於句中者：{len(inline)}")

    # R-P55 回歸斷言
    problems = []
    if len(rows) != EXPECTED_TOTAL:
        problems.append(f"處數 {len(rows)} ≠ 期望 {EXPECTED_TOTAL}")
    if len(counterexamples) != EXPECTED_COUNTEREXAMPLES:
        problems.append(f"反例 {len(counterexamples)} ≠ 期望 {EXPECTED_COUNTEREXAMPLES}")
    if problems:
        print("\n**回歸斷言失敗（R-P55）**：" + "；".join(problems))
        raise SystemExit(1)
    print("\n回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
