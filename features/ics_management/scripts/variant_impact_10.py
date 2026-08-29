#!/usr/bin/env python3
"""下放包 10 作業 B —— 二種變體結論之影響估（純量測，零寫入 TC）。

**只估不改**（下放包 10 §1）：本腳本對 `generated/**` 只讀不寫，
對 `scripts/` 之既有檔只以 importlib 唯讀載入，不修改任何一行。

輸入（全部唯讀）：
  - `inputs/…CFTS_020…docx` —— 經 `cfts020_probe.parse()`（importlib 載入）
  - `generated/b0{1..6}/b0*_tcs.json` —— 27 條 TC 之全欄

演算法：`可重錨／無錨可重` 之判準比照 08 報告 §5（`s118_compare_08.has_counterpart`），
但**本檔自行複驗**：行為標籤表 `BEHAVIORS` 由 `s118_compare_08` 唯讀匯入
（保證同一算法），母數改以 **27 條**（b01~b06）重算，不沿用 08 之 25 條結果。

用法：
  python3 features/ics_management/scripts/variant_impact_10.py          # 印量測結果
  python3 features/ics_management/scripts/variant_impact_10.py --json   # JSON 形式
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts" / "cfts020_probe.py"
CMP08 = ROOT / "scripts" / "s118_compare_08.py"
GEN = ROOT / "generated"

# 本輪之母數：27 條（含 b06 之 2 條），下放包 10 明定
BATCHES = ("b01", "b02", "b03", "b04", "b05", "b06")


def _load(path: Path, name: str):
    """以 importlib 唯讀載入既有腳本，不修改其原始碼（禁區 5）。"""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_tcs() -> tuple[list[dict], "OrderedDict[str, list[str]]"]:
    """讀 27 條 TC 與其錨。錨之計數法：`specification_reference` 逐行切分、
    去空白、以字串相等去重（相異錨＝去重後之集合大小）。"""
    tcs: list[dict] = []
    for f in sorted(GEN.glob("b0*/b0*_tcs.json")):
        d = json.loads(f.read_text())
        if d["batch"] not in BATCHES:
            continue
        for i, t in enumerate(d["tcs"], 1):
            refs = [r.strip() for r in t["specification_reference"].split("\n") if r.strip()]
            tcs.append({
                "batch": d["batch"],
                "seq": f'{d["batch"]}-{i:02d}',
                "req_id": t["req_id"],
                "title": t.get("tc_title", ""),
                "refs": refs,
                "raw": t,
                # 「驗證文字」同 09 報告 §0-3 之定義（不含 pre_conditions／reasoning）
                "core": "\n".join([t.get("test_item", ""), t.get("test_procedure", ""),
                                   t.get("expected_result", "")]),
                "pre": t.get("pre_conditions", ""),
            })
    anchors: "OrderedDict[str, list[str]]" = OrderedDict()
    for t in tcs:
        for r in t["refs"]:
            anchors.setdefault(r, []).append(t["seq"])
    return tcs, anchors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    probe = _load(PROBE, "cfts020_probe")
    cmp08 = _load(CMP08, "s118_compare_08")  # 只取 BEHAVIORS／tags，不執行其 main

    objs = probe.parse()
    by_id = {o["id"]: o for o in objs}

    def pick(prefix: str) -> list[dict]:
        return [o for o in objs
                if o["section_no"] == prefix or o["section_no"].startswith(prefix + ".")]

    s18, s118 = pick("1.8"), pick("1.18")
    s18_ap = [o for o in s18 if o["verdict"] == "適用"]
    s118_ap = [o for o in s118 if o["verdict"] == "適用"]

    tcs, anchors = read_tcs()
    a020 = [k for k in anchors if k.startswith("CFTS020-")]
    a022 = [k for k in anchors if k.startswith("CFTS022-")]
    other = [k for k in anchors if k not in a020 and k not in a022]

    def has_counterpart(ref: str) -> bool:
        """比照 08 §5：錨物件之行為標籤集與任一 §1.18 適用物件之標籤集有交集。"""
        o = by_id.get(ref.split("-", 1)[1])
        if o is None:
            return False
        t = set(cmp08.tags(o["text"]))
        return bool(t) and any(t & set(cmp08.tags(c["text"])) for c in s118_ap)

    a020_hit = sorted(k for k in a020 if has_counterpart(k))
    a020_miss = sorted(k for k in a020 if not has_counterpart(k))
    tc_020 = [t for t in tcs if any(r.startswith("CFTS020-") for r in t["refs"])]
    tc_022_only = [t for t in tcs if not any(r.startswith("CFTS020-") for r in t["refs"])]
    tc_all_hit = [t for t in tc_020
                  if all(has_counterpart(r) for r in t["refs"] if r.startswith("CFTS020-"))]
    tc_part = [t for t in tc_020
               if any(not has_counterpart(r) for r in t["refs"] if r.startswith("CFTS020-"))]

    # --- 敏感度：NBSP 正規化（A-ICS? 之機械層缺陷，見報告 §0-4） ---
    # 08 之 `ACT_*` 主詞正則含字面空格，而 docx 之部分物件以 U+00A0 分詞，
    # 導致該物件之主詞列全不命中。本檔**不修改 08 之算法**，另跑一組
    # 「\xa0 → 空格」之敏感度，二組數並報，由分析層定其讀法。
    def tags_nb(text: str) -> list[str]:
        return cmp08.tags(text.replace("\xa0", " "))

    def has_counterpart_nb(ref: str) -> bool:
        o = by_id.get(ref.split("-", 1)[1])
        if o is None:
            return False
        t = set(tags_nb(o["text"]))
        return bool(t) and any(t & set(tags_nb(c["text"])) for c in s118_ap)

    a020_hit_nb = sorted(k for k in a020 if has_counterpart_nb(k))
    a020_miss_nb = sorted(k for k in a020 if not has_counterpart_nb(k))
    tc_all_hit_nb = [t for t in tc_020
                     if all(has_counterpart_nb(r) for r in t["refs"] if r.startswith("CFTS020-"))]
    tc_part_nb = [t for t in tc_020
                  if any(not has_counterpart_nb(r) for r in t["refs"] if r.startswith("CFTS020-"))]
    nbsp_s118 = [o["id"] for o in s118_ap if "\xa0" in o["text"]]
    nbsp_s18 = [o["id"] for o in s18_ap if "\xa0" in o["text"]]

    # --- DCSD 依賴之逐條實測（欄二第 2 項） ---
    DCSD_PAT = re.compile(r"DCSD", re.I)
    dcsd_rows = []
    for t in tcs:
        anchor_txt = " ".join(by_id.get(r.split("-", 1)[1], {}).get("text", "")
                              for r in t["refs"] if r.startswith("CFTS020-"))
        dcsd_rows.append({
            "seq": t["seq"],
            "pre": len(DCSD_PAT.findall(t["pre"])),
            "core": len(DCSD_PAT.findall(t["core"])),
            "anchor": len(DCSD_PAT.findall(anchor_txt)),
            "anchor_dispstat": "$DCSD_DISP_STAT$" in anchor_txt,
            "refs": t["refs"],
        })

    # --- CFTS020-4819541 之牽連（欄二第 3 項） ---
    dep541 = sorted(t["seq"] for t in tcs if "CFTS020-4819541" in t["refs"])

    # --- b07 回填之 6 處佔位（欄二第 4 項）：R-ICS27(b) 之二組定值 ---
    # 判準：回填處＝「該行含 R-ICS27(b) 之三個定值字面之一」∧
    #       「該 TC 之錨含 CFTS020-4819541」（R-ICS27(b) 令回填時錨行增此錨）。
    #       此二條件同時成立方計入 —— 排除 b01-01/02/03 之 120 s
    #       （其來源為 CFTS022-4914956 之 DTC mature time，非 4819541，R-ICS9(d)）。
    FILL = [("120 second", "DR-ICS10"), ("50 msec", "DR-ICS12"), ("20 msec", "DR-ICS12")]
    fills, fills_excluded = [], []
    for t in tcs:
        tgt = fills if "CFTS020-4819541" in t["refs"] else fills_excluded
        for field in ("pre_conditions", "test_procedure", "expected_result",
                      "input_test_data", "test_item"):
            v = t["raw"].get(field) or ""
            for line in v.split("\n"):
                for lit, dr in FILL:
                    if lit in line:
                        tgt.append({"seq": t["seq"], "field": field, "dr": dr,
                                    "lit": lit, "line": line.strip()})

    out = {
        "tc_total": len(tcs),
        "anchors_distinct": len(anchors),
        "cfts020_distinct": len(a020),
        "cfts022_distinct": len(a022),
        "other_distinct": other,
        "anchor_use": {k: v for k, v in anchors.items()},
        "tc_with_020": [t["seq"] for t in tc_020],
        "tc_022_only": [t["seq"] for t in tc_022_only],
        "a020_hit": a020_hit,
        "a020_miss": a020_miss,
        "tc_rehostable": [t["seq"] for t in tc_all_hit],
        "tc_no_host": [t["seq"] for t in tc_part],
        "s18_total": len(s18), "s18_applicable": len(s18_ap),
        "s118_total": len(s118), "s118_applicable": len(s118_ap),
        "dcsd": dcsd_rows,
        "dep_4819541": dep541,
        "backfills": fills,
        "backfills_excluded": fills_excluded,
        # 每一 CFTS020 錨之所屬節（驗「27 條之錨是否全落在 §1.8」）
        "anchor_sections": {k: by_id.get(k.split("-", 1)[1], {}).get("section_no", "查無")
                            for k in a020},
        "anchor_verdicts": {k: by_id.get(k.split("-", 1)[1], {}).get("verdict", "查無")
                            for k in a020},
        "nbsp": {
            "s118_ap_with_nbsp": len(nbsp_s118), "s18_ap_with_nbsp": len(nbsp_s18),
            "a020_hit": a020_hit_nb, "a020_miss": a020_miss_nb,
            "tc_rehostable": [t["seq"] for t in tc_all_hit_nb],
            "tc_no_host": [t["seq"] for t in tc_part_nb],
        },
    }
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    print(f"TC 總數 {out['tc_total']}；相異錨 {out['anchors_distinct']}"
          f"（CFTS020 {out['cfts020_distinct']} + CFTS022 {out['cfts022_distinct']}"
          f" + 其他 {len(other)}）")
    print(f"§1.8 物件 {out['s18_total']}（適用 {out['s18_applicable']}）；"
          f"§1.18 物件 {out['s118_total']}（適用 {out['s118_applicable']}）")
    print(f"含 CFTS020 錨之 TC {len(tc_020)}；純 CFTS022 {len(tc_022_only)} "
          f"= {out['tc_022_only']}")
    print(f"CFTS020 錨有對應 {len(a020_hit)}：{a020_hit}")
    print(f"CFTS020 錨無對應 {len(a020_miss)}：{a020_miss}")
    print(f"可重錨 {len(tc_all_hit)}：{out['tc_rehostable']}")
    print(f"無錨可重 {len(tc_part)}：{out['tc_no_host']}")
    print(f"用 4819541 之 TC {len(dep541)}：{dep541}")
    print("DCSD 依賴（pre/core/anchor 之命中數）：")
    for r in dcsd_rows:
        if r["pre"] or r["core"] or r["anchor"]:
            print(f"  {r['seq']}: pre={r['pre']} core={r['core']} anchor={r['anchor']} "
                  f"DISP_STAT={r['anchor_dispstat']} refs={r['refs']}")
    print(f"[NBSP 敏感度] §1.18 適用含 NBSP {len(nbsp_s118)}／{len(s118_ap)}；"
          f"§1.8 適用含 NBSP {len(nbsp_s18)}／{len(s18_ap)}")
    print(f"[NBSP 敏感度] 錨有對應 {len(a020_hit_nb)}／無對應 {len(a020_miss_nb)} {a020_miss_nb}；"
          f"可重錨 {len(tc_all_hit_nb)}／無錨可重 {len(tc_part_nb)}")
    print(f"b07 回填實測 {len(fills)} 處：")
    for f in fills:
        print(f"  {f['seq']} [{f['field']}] {f['dr']} → {f['lit']} :: {f['line'][:90]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
