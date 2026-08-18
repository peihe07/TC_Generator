#!/usr/bin/env python3
"""覆核用全文 ＋ ER 出處對照之產生器（40 包作業 5）。

21／23／29／34／35 輪之 review pack 皆為**手打**。手打的代價在 35 輪已經
出現過一次：拆兩檔時要逐條搬運欄位，而**搬運本身沒有閘**。
本檔把該格式變成一支程式 —— 內容一律自 `generated/*.json` 讀出，
**不經人手轉錄**。

出處對照併入同一檔（每條之引號字面值 → 其來源節），
判準與 `lint_tcs` 之 G18 同一支：`_pool()` 取被引之節之 `pdf_text`
加其 must_carry，`UI_LOCATORS` 之登記另計。
**兩者若分歧，是 G18 或本檔其一寫錯了** —— 故本檔直接呼叫 G18 之資料源，
不另抄一份判準。

Usage:
    python3 scripts/build_review_pack.py 135 145 > out.md
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
import lint_tcs as L                                  # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
FIELDS = [
    ("tc_title / test_item", "tc_title"),
    ("pre_conditions", "pre_conditions"),
    ("input_test_data", "input_test_data"),
    ("test_procedure", "test_procedure"),
    ("expected_result", "expected_result"),
    ("specification_reference", "specification_reference"),
    ("design_method", "design_method"),
]


def _cell(v: str) -> str:
    return " ".join(str(v).split("\n")).replace("|", "\\|") if "\n" not in str(v) \
        else "<br>".join(x.strip() for x in str(v).splitlines() if x.strip()) \
                 .replace("|", "\\|")


def records(lo: int, hi: int) -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            n = int(t["tc_id"].rsplit("-", 1)[1])
            if lo <= n <= hi:
                out.append((n, d, t))
    return [x[1:] for x in sorted(out)]


def pool_for(t: dict) -> tuple:
    cited = [x.strip().replace(B.SPEC_STEM + "_", "")
             for x in str(t["specification_reference"]).split("; ")]
    pool = " ".join(B.spec_body(c) for c in cited)
    for c in cited:
        for r in B.must_carry_for(c):
            pool += " " + (r.get("text") or "")
    return cited, " ".join(pool.split())


def provenance(rows: list) -> list:
    out = []
    for d, t in rows:
        cited, pool = pool_for(t)
        for field, raw in (("ER", t["expected_result"]),
                           ("pre", t["pre_conditions"])):
            for lit in L.QUOTED_RE.findall(str(raw)):
                if " ".join(lit.split()) in pool:
                    src = f"逐字見於 **{'／'.join(cited)}**"
                elif lit.strip() in L.UI_LOCATORS:
                    src = (f"`UI_LOCATORS` 登記：其來源為 "
                           f"**{L.UI_LOCATORS[lit.strip()]}**")
                else:
                    src = "**未溯得 —— 須處置**"
                out.append((t["tc_id"], d["outline"], lit, field, src))
    return out


BATCH = "第五批"


def emit(lo: int, hi: int, title: str, other: str) -> None:
    rows = records(lo, hi)
    prov = provenance(rows)
    unresolved = [x for x in prov if "未溯得" in x[4]]
    verbatim = [x for x in prov if x[4].startswith("逐字")]
    loc = [x for x in prov if "UI_LOCATORS" in x[4]]

    print(f"# 覆核用全文 ＋ ER 出處對照 — {BATCH} {title}"
          f"（`{lo:03d}`–`{hi:03d}`）\n")
    print(f"- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**")
    print(f"- 本檔 **{len(rows)} 條**；另半在 `{other}`")
    print(f"- 由 `scripts/build_review_pack.py` 產生，不經人手轉錄\n")
    print("> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——")
    print("> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。\n")

    print("## 0. ER 出處對照\n")
    print("| 項 | 數 |")
    print("|---|---|")
    print(f"| 引號字面值（ER ＋ pre_conditions）| **{len(prov)}** |")
    print(f"| 逐字溯得到被引之節或其 must_carry | **{len(verbatim)}** |")
    print(f"| 經 `UI_LOCATORS` 登記表溯源 | **{len(loc)}** |")
    print(f"| **未溯得者** | **{len(unresolved)}** |")
    n_none = sum(1 for d, t in rows
                 if not L.QUOTED_RE.findall(str(t["expected_result"])
                                            + str(t["pre_conditions"])))
    print(f"| 全條無引號字面值者 | **{n_none} 條** |\n")
    print("| tc_id | 節 | 字面值 | 欄位 | 出處 |")
    print("|---|---|---|---|---|")
    for tid, sec, lit, field, src in prov:
        print(f"| `{tid}` | {sec} | 「{lit}」| {field} | {src} |")
    print("\n---\n")

    print("## 1. 逐條全文\n")
    for d, t in rows:
        print(f"### {t['tc_id']} — {t['req_id']}"
              f"（{d['outline']} / {d['test_set']}）\n")
        print("**spec 原文（`pdf_text`）**：\n")
        print("> " + " ".join(str(d["source_clause"]).split()) + "\n")
        print("**037 description**：" +
              " ".join(str(d["leaf_desc_037"]).split()) + "\n")
        print("| 欄 | 值 |")
        print("|---|---|")
        for label, key in FIELDS:
            print(f"| {label} | {_cell(t[key])} |")
        print(f"| priority | **{t['priority']}** — {t['priority_basis']} |")
        print(f"| remarks | {_cell(t['remarks'])} |")
        print(f"\n**reasoning**：{' '.join(str(d['reasoning']).split())}\n")
        print("---\n")


if __name__ == "__main__":
    if len(sys.argv) > 5:
        globals()['BATCH'] = sys.argv[5]
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    emit(lo, hi, sys.argv[3], sys.argv[4])
