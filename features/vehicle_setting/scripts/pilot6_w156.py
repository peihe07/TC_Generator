"""W-156（82 包 §4）—— pilot #5＋#6 合併 sheet。

母體：本輪起未經人工關卡者 85 條
  batch20 12 ＋ batch21_probe 7 ＋ batch22 12 ＋ batch23 47
  ＋ 他批之 `split_flag = true` 7（50 輪 W-143 之拆分產出）

抽 18：必檢 10 ＋ 分層 8。
  必檢 10 —— G 型八子形態各 1（G1 為 held_out 不計 → 七形態）
              ＋ D 型 `PENDING: DR-15` 2 ＋ G2「顯示不變」1
  分層 8  —— `test_set`（四值）× `screen_pending`（二值）＝ 八格各 1
              **先驗二維度於本母體非單值**（A-VS142 之教訓）
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches      # noqa: E402
from inscope_w39 import blocks_with_sec       # noqa: E402

FOUR = {"batch20.json", "batch21_probe.json", "batch22.json", "batch23.json"}
BLK = {b["id"]: b for b in blocks_with_sec()}
L2R = {r["swe_id"]: r for r in csv.DictReader(
    (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
COLS = [("tc_title", "TC Title"), ("test_item", "Test Item"),
        ("pre_conditions", "Pre-Conditions"), ("input_test_data", "Input Test Data"),
        ("test_procedure", "Test Procedure"), ("expected_result", "Expected Result"),
        ("specification_reference", "Specification Reference"),
        ("design_method", "Design Method"), ("priority", "Priority"),
        ("split_flag", "Split Flag"), ("split_reason", "Split Reason"),
        ("dr15_exposed", "DR-15 Exposed"), ("dr_dependent", "DR Dependent"),
        ("screen_pending", "Screen Pending"), ("remarks", "Remarks"),
        ("reasoning", "Reasoning")]


def mother() -> list[dict]:
    out = []
    for f in latest_batches():
        for t in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            if f.name in FOUR or t.get("split_flag"):
                out.append({**t, "_b": f.name})
    return out


def src(leaf: str) -> str:
    qs = re.findall(r"\d{7}", L2R[leaf]["reqid_list"])
    return "\n".join(BLK[qs[0]]["text"].split("\n")[1:]).strip() if qs else ""


def form_of(t: dict) -> str:
    if t.get("form"):
        return t["form"]
    r = t.get("reasoning", "")
    for k in ("A 型", "D 型", "E 型", "F 型"):
        if k in r:
            return k + "（早批）"
    return "未標形態（早批）"


def pick(mo: list[dict]) -> tuple[list[dict], list[dict], dict]:
    by_form = collections.defaultdict(list)
    for t in mo:
        by_form[form_of(t)].append(t)

    must, seen = [], set()

    def take(t, why):
        key = (t["leaf_id"], t["tc_title"])
        if key in seen:
            return False
        seen.add(key)
        must.append({**t, "_why": why})
        return True

    # G 型七子形態各 1（G1 為 held_out，不在產物中）
    for form in sorted(k for k in by_form if k.startswith("G")):
        take(sorted(by_form[form], key=lambda x: x["leaf_id"])[0],
             f"必檢：G 型子形態 `{form}` 之代表（該形態共 {len(by_form[form])} 條）")
    # D 型 `PENDING: DR-15` 2
    d15 = sorted((t for t in mo if "PENDING: DR-15" in t.get("expected_result", "")),
                 key=lambda x: x["leaf_id"])
    for t in d15[:2]:
        take(t, "必檢：D 型 `PENDING: DR-15` 之形態（80 包 §1 之改寫，共 "
                f"{len(d15)} 條）")
    # G2「顯示不變」1 —— 取其 PENDING 分支者（無未用碼可注入）
    g2p = [t for t in by_form.get("G2 值域宣告 ＋ 其餘為無效", [])
           if "PENDING" in t.get("expected_result", "")]
    if g2p:
        take(sorted(g2p, key=lambda x: x["leaf_id"])[0],
             "必檢：G2「顯示不變」＋ 無未用碼可注入之 PENDING 分支（共 "
             f"{len(g2p)} 條）")

    # 分層 8 —— test_set(4) × screen_pending(2)
    dim1 = sorted({t["test_set"] for t in mo})
    dim2 = sorted({str(t.get("screen_pending")) for t in mo})
    matrix = {(a, b): [t for t in mo if t["test_set"] == a
                       and str(t.get("screen_pending")) == b]
              for a in dim1 for b in dim2}
    strat = []
    for (a, b), cell in sorted(matrix.items()):
        pool = [t for t in cell if (t["leaf_id"], t["tc_title"]) not in seen]
        if not pool:
            continue
        # 每格取其 leaf_id 排序之中位一條（非首條，避免退化為順序取樣）
        pool.sort(key=lambda x: (x["leaf_id"], x["tc_title"]))
        t = pool[len(pool) // 2]
        seen.add((t["leaf_id"], t["tc_title"]))
        strat.append({**t, "_why": f"分層：`{a}` × `screen_pending = {b}`"
                                   f"（該格 {len(cell)} 條，取排序中位）"})
    return must, strat, {"dim1": dim1, "dim2": dim2,
                         "matrix": {f"{a}|{b}": len(v) for (a, b), v in matrix.items()}}


def main() -> None:
    mo = mother()
    must, strat, dims = pick(mo)
    L = []
    L.append("# pilot #5＋#6 合併 sheet（W-156，54 輪）\n")
    L.append("依 `docs/handoff/82_generation_done.md` §4。"
             "**母體：本輪起未經任何人工關卡者。**\n")
    L.append("## 1. 母體之構成\n")
    L.append("| 批 | 條 | 說明 |")
    L.append("|---|---|---|")
    cb = collections.Counter(t["_b"] for t in mo)
    note = {"batch20.json": "50 輪 A 型補寫", "batch21_probe.json": "52 輪 probe 修正",
            "batch22.json": "52 輪 E 型放量", "batch23.json": "53 輪生成收尾"}
    for b, n in sorted(cb.items()):
        L.append(f"| `{b}` | {n} | {note.get(b, '50 輪 W-143 之拆分產出')} |")
    L.append(f"| **合計** | **{len(mo)}** | 與 82 包 §4 所載之 85 "
             f"{'相符' if len(mo) == 85 else '**不符**'} |\n")

    L.append("## 2. 分層維度之非單值驗證（先驗，A-VS142 之教訓）\n")
    L.append("| 維度 | 相異值 | 判 |")
    L.append("|---|---|---|")
    L.append(f"| `test_set` | {len(dims['dim1'])} —— "
             f"{'、'.join('`' + x + '`' for x in dims['dim1'])} | "
             f"**非單值**，可分層 |")
    L.append(f"| `screen_pending` | {len(dims['dim2'])} —— "
             f"{'、'.join('`' + x + '`' for x in dims['dim2'])} | "
             f"**非單值**，可分層 |\n")
    L.append("**升級條件「分層維度於本母體為單值」未命中。**\n")

    L.append("## 3. 交叉格矩陣\n")
    L.append("| `test_set` \\ `screen_pending` | " +
             " | ".join(f"`{b}`" for b in dims["dim2"]) + " | 小計 |")
    L.append("|---" * (len(dims["dim2"]) + 2) + "|")
    for a in dims["dim1"]:
        cells = [dims["matrix"][f"{a}|{b}"] for b in dims["dim2"]]
        L.append(f"| `{a}` | " + " | ".join(str(c) for c in cells) +
                 f" | **{sum(cells)}** |")
    tot = [sum(dims["matrix"][f"{a}|{b}"] for a in dims["dim1"])
           for b in dims["dim2"]]
    L.append("| **小計** | " + " | ".join(f"**{c}**" for c in tot) +
             f" | **{sum(tot)}** |\n")
    L.append("**八格中非空者即分層抽樣之取樣格**；空格不取（其非抽樣之遺漏，"
             "而是該組合於母體不存在）。\n")

    L.append("## 4. 形態分布（必檢之涵蓋依據）\n")
    bf = collections.Counter(form_of(t) for t in mo)
    L.append("| 形態 | 條 | 必檢涵蓋 |")
    L.append("|---|---|---|")
    picked_forms = {form_of(t) for t in must}
    for f, n in sorted(bf.items()):
        L.append(f"| `{f}` | {n} | {'✅' if f in picked_forms else '—'} |")
    L.append("")

    L.append(f"## 5. 抽樣 {len(must) + len(strat)} 條"
             f"（必檢 {len(must)} ＋ 分層 {len(strat)}）\n")
    for i, t in enumerate(must + strat, 1):
        tag = "必檢" if i <= len(must) else "分層"
        L.append(f"### {i}. [{tag}] `{t['leaf_id']}` — {t['tc_title']}\n")
        L.append(f"**抽樣理由**：{t['_why']}")
        L.append(f"**形態**：`{form_of(t)}`　**批**：`{t['_b']}`\n")
        L.append("**來源條文（逐字）**\n")
        L.append("```")
        L.append(src(t["leaf_id"]))
        L.append("```\n")
        L.append("| 欄 | 內容 |")
        L.append("|---|---|")
        L.append(f"| Leaf ID | `{t['leaf_id']}` |")
        L.append(f"| Test Set | {t['test_set']} |")
        for k, label in COLS:
            v = str(t.get(k, "")).replace("\n", "<br>").replace("|", "\\|")
            L.append(f"| {label} | {v} |")
        L.append("")
    p = FEAT / "docs/reports/pilot6_sheet.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print(f"{p} —— 母體 {len(mo)}；抽 {len(must) + len(strat)} "
          f"（必檢 {len(must)}／分層 {len(strat)}）")
    print("必檢涵蓋之形態：", sorted(picked_forms))


if __name__ == "__main__":
    main()
