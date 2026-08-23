"""W-118（67 包）—— pilot #3＋#4 之合併 review sheet。

母體 **43 條**（batch14 10／15 13／16 10／17 10）—— batch18 於本輪產出，
**不在本次抽樣之母體內**（其 10 條之 pilot 時機另定）。

抽樣（15 條）：
  **必檢 8**（新形態，不抽樣）：batch16／17 之 `Fail_Present` 類各取 4
  **分層 7**：維度 = batch × `dr_dependent`（有／無），交叉格內取 reqid 最小者；
             不足 7 時自條數最多之格補足
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]
POP = {"batch14": "generated/batch14_v2.json", "batch15": "generated/batch15.json",
       "batch16": "generated/batch16.json", "batch17": "generated/batch17.json"}
COLS = ["tc_title", "test_item", "pre_conditions", "input_test_data", "test_procedure",
        "expected_result", "specification_reference", "design_method", "priority",
        "split_flag"]


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}

    pop = []
    for b, f in POP.items():
        for tc in json.loads((FEAT / f).read_text(encoding="utf-8"))["tcs"]:
            reqid = re.findall(r"\d{7}", (l2r.get(tc["leaf_id"], {}).get("reqid_list") or ""))
            pop.append({"batch": b, "tc": tc, "reqid": reqid[0] if reqid else "9999999",
                        "fail": "Fail_Present" in tc["test_item"],
                        "dep": "有" if tc.get("dr_dependent") else "無"})
    assert len(pop) == 43, len(pop)

    must = []
    for b in ("batch16", "batch17"):
        fp = sorted((r for r in pop if r["batch"] == b and r["fail"]),
                    key=lambda r: r["reqid"])
        must += fp[:4]

    cells = collections.defaultdict(list)
    for r in pop:
        cells[(r["batch"], r["dep"])].append(r)
    for v in cells.values():
        v.sort(key=lambda r: r["reqid"])
    chosen = {id(r["tc"]) for r in must}
    strat = []
    for key in sorted(cells):
        for r in cells[key]:
            if id(r["tc"]) not in chosen:
                strat.append(r)
                chosen.add(id(r["tc"]))
                break
    biggest = max(cells.values(), key=len)
    for r in biggest:
        if len(strat) >= 7:
            break
        if id(r["tc"]) not in chosen:
            strat.append(r)
            chosen.add(id(r["tc"]))
    strat = strat[:7]

    items = [(r, "必檢（新形態，不抽樣）") for r in must] + \
            [(r, f"分層（{r['batch']} × `dr_dependent` {r['dep']}）") for r in strat]

    out = ["# pilot #3＋#4 合併 review sheet", "",
           "執行層產出（W-118，42 輪）。依 67 包之抽樣裁定。", "",
           "## 1. 母體與抽樣", "",
           f"母體 **{len(pop)} 條**（batch14 10／15 13／16 10／17 10）——",
           "**batch18 之 10 條於本輪產出，不在本次抽樣之母體內。**", "",
           "### 抽樣之交叉格矩陣（使抽法可複現）", "",
           "| batch \\ `dr_dependent` | 有 | 無 | 小計 |", "|---|---:|---:|---:|"]
    for b in POP:
        y = len(cells[(b, "有")])
        n = len(cells[(b, "無")])
        out.append(f"| `{b}` | {y} | {n} | {y + n} |")
    out += ["", f"必檢 **{len(must)}**（batch16／17 之 `Fail_Present` 各 4，reqid 升冪）；"
            f"分層 **{len(strat)}**（各交叉格取 reqid 最小者；不足時自最大格補足）；"
            f"**合計 {len(items)}**。", "",
            "## 2. pilot #3 之 13 條（只列清單，全文見 `pilot3_sheet.md`）", "",
            "| # | batch | leaf_id |", "|---:|---|---|"]
    p3 = json.loads((FEAT / "generated/batch13_v2.json").read_text(encoding="utf-8"))["tcs"]
    for i, tc in enumerate(p3, 1):
        out.append(f"| {i} | `batch13_v2` | `{tc['leaf_id']}` |")
    for i, extra in enumerate(["SWE1-VC-ThirdRowHeadrestDump-025",
                               "SWE1-VC-TwoStagesHeatedSeat-057",
                               "SWE1-VC-ThirdRowHeadrestDump-030"], 11):
        out.append(f"| {i} | （W-101 之 Priority 變動） | `{extra}` |")
    out += ["", "## 3. pilot #4 之 15 條 —— 十欄全文", ""]

    for i, (r, why) in enumerate(items, 1):
        tc, leaf = r["tc"], r["tc"]["leaf_id"]
        row = l2r.get(leaf, {})
        out += [f"### {i}. `{leaf}`", "",
                "| 項 | 值 |", "|---|---|",
                f"| 來源批次 | `{r['batch']}` |", f"| 納入理由 | {why} |",
                f"| `priority` | **{tc['priority']}** |",
                f"| Priority 所依類別（R-VS56） | {tc.get('reasoning', '（未記）')} |",
                f"| `dr_dependent` | {tc.get('dr_dependent') or '（無）'} |",
                f"| `screen_source` | {tc.get('screen_source') or '（未標）'} |",
                f"| `design_method` | {tc['design_method']} |",
                f"| 章節 | {row.get('section', '')} |", "",
                "**來源條文逐字**", ""]
        for rid in (row.get("reqid_list") or "").split(";"):
            blk = blocks.get(rid.strip().replace("CFTS044-", ""))
            if blk:
                body = "\n".join(blk["text"].split("\n")[1:]).strip()
                out += [f"`{rid.strip()}`（`EE Architecture: "
                        f"{blk['attrs'].get('EE Architecture', '?')}`）：", "",
                        "> " + body.replace("\n", "\n> "), ""]
        out.append("**十欄全文**")
        out.append("")
        for c in COLS:
            v = tc[c]
            if isinstance(v, str) and "\n" in v:
                out += [f"**{c}**", "", "```", v, "```", ""]
            else:
                out.append(f"**{c}**：{v}")
        out += ["", "### 覆核欄（分析層填）", "", "| 項 | 建議分類 | 理由 |", "|---|---|---|",
                "| 內容正確性 | | |", "| Priority 判定 | | |",
                "| 畫面層 `PENDING` 之處置 | | |", "", "---", ""]

    (FEAT / "docs/reports/pilot4_sheet.md").write_text("\n".join(out), encoding="utf-8")
    print(f"pilot4_sheet.md：必檢 {len(must)} ＋ 分層 {len(strat)} = {len(items)} 條")
    print("交叉格：", {f"{k[0]}/{k[1]}": len(v) for k, v in sorted(cells.items())})
    for r, why in items:
        print(f"  {r['batch']:9s} {r['tc']['priority']} {r['tc']['leaf_id']:46s} {why[:24]}")


if __name__ == "__main__":
    main()
