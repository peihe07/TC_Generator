#!/usr/bin/env python3
"""Phase 4 batch 之 lint —— profile §3 各欄規則 ＋ R-PMH50 之機械檢查。

**R-PMH50 之限度須明說**：本 lint 只驗 `source_clause` **存在且非空**、
且其 `origin` 為 `spec_pdf`。**「是否忠於規格」本身不可機械檢查** ——
須人讀 PDF 原文與 TC 對照。本檢查只保證覆核所需之材料存在，不保證覆核已做。
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"
LAYER3 = ROOT / "data" / "layer3_sections.tsv"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batch")
    a = ap.parse_args()
    d = json.loads((ROOT / a.batch).read_text(encoding="utf-8"))
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    voc = set(cfg["lint"]["design_method_vocabulary"])
    sets = set(cfg["write_back"]["test_set_values"])
    import csv
    l3 = {r["swe_requirement_id"]: r["outline_number"] for r in
          csv.DictReader(LAYER3.open(encoding="utf-8"), delimiter="\t")}

    checks, fails = [], []

    def chk(name, ok, detail=""):
        checks.append((name, ok, detail))
        if not ok:
            fails.append(name)

    tcs = d["tcs"]
    print(f"batch = {d['batch']}；TC 數 = {len(tcs)}；leaf 數 = "
          f"{len({t['leaf_id'] for t in tcs})}\n")

    # --- R-PMH50 ---
    miss = [t["tc_id"] for t in tcs if not str(t.get("source_clause", "")).strip()]
    chk("R-PMH50 每 leaf 有 source_clause 且非空", not miss, str(miss))
    nonpdf = [t["tc_id"] for t in tcs
              if not str(t.get("source_clause_origin", "")).startswith("spec_pdf")]
    chk("R-PMH50 source_clause 取自 PDF（非 SYS1）", not nonpdf, str(nonpdf))

    # --- profile §3.1：test_item 下半括號（硬規則）---
    bad = [t["tc_id"] for t in tcs
           if not re.search(r"\n\n\(.+\)$", t["test_item"], re.S)]
    chk("profile §3.1 test_item 具下半括號（硬規則）", not bad, str(bad))

    # --- profile §3.3：design_method ∈ 9 詞條 ---
    bad = [(t["tc_id"], t["design_method"]) for t in tcs if t["design_method"] not in voc]
    chk("profile §3.3 design_method ∈ 下拉選單 9 詞條", not bad, str(bad))

    # --- profile §3.4：spec_reference 形態 ＋ 與 layer3 對得上 ---
    bad = []
    for t in tcs:
        m = re.fullmatch(re.escape(SPEC) + r"_(\d+(?:\.\d+)*)", t["specification_reference"])
        if not m or l3.get(t["leaf_id"]) != m.group(1):
            bad.append((t["tc_id"], t["specification_reference"], l3.get(t["leaf_id"])))
    chk("profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符", not bad, str(bad))

    # --- profile §3.5：priority ∈ P0–P3 ---
    bad = [(t["tc_id"], t["priority"]) for t in tcs
           if t["priority"] not in {"P0", "P1", "P2", "P3"}]
    chk("profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）", not bad, str(bad))

    # --- profile §3.6 / §3.8：Q 與 T–Z 留白 ---
    chk("profile §3.6 estimated_test_time 留白",
        all(not str(t.get("estimated_test_time", "")).strip() for t in tcs))
    chk("profile §3.8 vehicle_models 留白",
        all(not str(t.get("vehicle_models", "")).strip() for t in tcs))

    # --- profile §3.7：functional_safety = NA ---
    bad = [t["tc_id"] for t in tcs if t.get("functional_safety") != "NA"]
    chk("profile §3.7 functional_safety = NA", not bad, str(bad))

    # --- profile §5 / R-PMH18：三字串之大小寫 ---
    chk("R-PMH18 test_group = 'Disclaimer screen'（小寫 s）",
        all(t["test_group"] == "Disclaimer screen" for t in tcs))
    chk("R-PMH36 test_set = 'Disclaimer Screen'（大寫 S）",
        all(t["test_set"] == "Disclaimer Screen" for t in tcs))
    chk("R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}",
        all(re.fullmatch(r"NR1L-DisclaimerScreen-\d{3}", t["tc_id"]) for t in tcs))
    chk("test_set ∈ Layer 2 定版 8 組", all(t["test_set"] in sets for t in tcs))

    # --- profile §11：方括號禁止（本 feature 無例外）---
    bad = [t["tc_id"] for t in tcs
           if re.search(r"\[[^\]]+\]", t["test_item"] + t["pre_conditions"]
                        + t["test_procedure"] + t["expected_result"])]
    chk("canon §11 方括號禁止（本 feature 無 profile 例外）", not bad, str(bad))

    # --- canon：步數一致、無空欄、無 NA 充當未知 ---
    bad = [(t["tc_id"], len(t["test_procedure"].split("\n")),
            len(t["expected_result"].split("\n"))) for t in tcs
           if len(t["test_procedure"].split("\n")) != len(t["expected_result"].split("\n"))]
    chk("procedure 與 ER 步數一致", not bad, str(bad))
    REQ = ["test_item", "pre_conditions", "test_procedure", "expected_result",
           "specification_reference", "design_method", "priority"]
    bad = [(t["tc_id"], f) for t in tcs for f in REQ if not str(t[f]).strip()]
    chk("必填欄無空", not bad, str(bad))
    bad = [t["tc_id"] for t in tcs if re.search(r"\bNA\b", t["expected_result"])]
    chk("ER 未以 NA 充當未知", not bad, str(bad))

    # --- tc_id 唯一且連號 ---
    ids = [t["tc_id"] for t in tcs]
    chk("tc_id 唯一", len(set(ids)) == len(ids))
    chk("tc_id_status = provisional", d.get("tc_id_status") == "provisional")

    # --- leaf 覆蓋：本批 leaf 須 ⊆ Disclaimer Screen 之 7 leaf ---
    want = {k for k, v in l3.items()
            if v in {"7.1", "7.2", "7.3", "7.4", "10.4"}}
    got = {t["leaf_id"] for t in tcs}
    ds7 = {"SWE1-HMI-PM-001-03", "SWE1-HMI-PM-001-04", "SWE1-HMI-PM-001-05",
           "SWE1-HMI-PM-003", "SWE1-HMI-PM-004", "SWE1-HMI-PM-005",
           "SWE1-HMI-PM-022-02"}
    chk("本批 leaf == Disclaimer Screen 之 7 leaf", got == ds7,
        f"多 {sorted(got-ds7)} 少 {sorted(ds7-got)}")

    w = max(len(n) for n, _, _ in checks)
    for n, ok, det in checks:
        print(f"  {n:<{w}}  {'PASS' if ok else '**FAIL**'}"
              + (f"  {det}" if not ok and det else ""))
    print(f"\n{len(checks)-len(fails)}/{len(checks)} PASS"
          + (f"；FAIL：{fails}" if fails else ""))
    print("\n⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。"
          "\n  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。"
          "\n  本檢查只保證覆核所需之材料存在，不保證覆核已做。")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
