#!/usr/bin/env python3
"""Phase 4 batch 之 lint —— profile §3 各欄規則 ＋ canon 條文層 ＋ R-PMH50。

**13 包擴充（R-PMH52）**：原 20 項全為 profile 欄位層與 id 層，
**零項檢查 canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11** ——
而 batch 1 於該七節共六類違規、涉全部八條，lint 仍 20/20 全綠。
本輪新增七項，並於輸出末尾**具名其仍未涵蓋之 canon 節號**。

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

    # ==================== 13 包新增（R-PMH52）====================

    # C1 §10.5 —— 至少 2 步（Single-step TCs are rejected）
    bad = [(t["tc_id"], len([x for x in t["test_procedure"].split("\n") if x.strip()]))
           for t in tcs
           if len([x for x in t["test_procedure"].split("\n") if x.strip()]) < 2]
    chk("canon §10.5 test_procedure >= 2 步", not bad, str(bad))

    # C2 §5.1 —— 禁用動詞作主動詞
    FORBID = r"\b(observe|see if|check whether|make sure|ensure|watch|look at|try to)\b"
    bad = []
    for t in tcs:
        for ln in t["test_procedure"].split("\n"):
            body = re.sub(r"^\s*\d+[.)]\s*", "", ln)
            for m in re.finditer(FORBID, body, re.I):
                bad.append((t["tc_id"], m.group(0), body[:60]))
    chk("canon §5.1 procedure 無禁用動詞", not bad, f"{len(bad)} 處 {bad[:3]}")

    # C3 §5.2B/§5.5 —— Final Step 須含驗證意圖
    VERIFY = r"\b(check that|confirm that|verify that|record|compare|read)\b|to verify"
    bad = [t["tc_id"] for t in tcs
           if not re.search(VERIFY,
                            [x for x in t["test_procedure"].split("\n") if x.strip()][-1],
                            re.I)]
    chk("canon §5.2B/§5.5 Final Step 含驗證意圖", not bad, str(bad))

    # C4 §4.3.1 —— test_item 上半須為 source_clause 之子字串（正規化後）
    def nz(s):
        s = str(s)
        for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                     ("…", "..."), ("–", "-"), ("—", "-")):
            s = s.replace(a, b)
        return re.sub(r"\s+", " ", s).strip()
    bad = []
    for t in tcs:
        top = nz(t["test_item"].split("\n\n(")[0])
        if top and top not in nz(t.get("source_clause", "")):
            bad.append(t["tc_id"])
    chk("canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）", not bad, str(bad))

    # C5 交付欄位無 markdown 標記
    DELIV = ["test_item", "pre_conditions", "test_procedure", "expected_result",
             "specification_reference", "remarks"]
    bad = [(t["tc_id"], f) for t in tcs for f in DELIV
           if re.search(r"\*\*|__|`", str(t.get(f, "")))]
    chk("交付欄位無 markdown 標記（**／__／`）", not bad, str(bad[:4]))

    # C6 §11 —— 直雙引號、無彎引號；UI 標籤須加引號
    bad = [(t["tc_id"], f) for t in tcs for f in DELIV
           if re.search(r"[“”‘’]", str(t.get(f, "")))]
    chk("canon §11 無彎引號", not bad, str(bad[:4]))
    UI = r"\bthe (Accept|Loading) (button|indicator)\b"
    bad = [t["tc_id"] for t in tcs for f in DELIV
           if re.search(UI, str(t.get(f, "")))]
    chk("canon §11 UI 標籤加直雙引號", not bad, str(sorted(set(bad))))

    # C7 R-PMH53 —— 批內交叉引用：存在性 ＋ **語意相容**
    #
    # 語意相容之機械近似：被引用者之 `distinguishing_axis` 須與**引用者自身之
    # axis** 至少共用一個實詞（長度 >= 2 之 CJK 詞或英文字）。
    # `-005`（配備：未配備 lower comfort screen）引 `-004`（變體：Maserati（無逾時））
    # 二者零共用 → FAIL。**無法機械判定者於下方逐處列出供人讀**（R-PMH53 末段）。
    by_suffix = {t["tc_id"][-3:]: t for t in tcs}

    def toks(s):
        s = str(s)
        return {w for w in re.findall(r"[\u4e00-\u9fff]{2,}|[A-Za-z]{3,}", s)}

    bad, refs = [], []
    for t in tcs:
        for f in ("test_item", "reasoning", "distinguishing_axis"):
            for m in re.finditer(r"`-(\d{3})`", str(t.get(f, ""))):
                sfx = m.group(1)
                refs.append((t["tc_id"], f, m.group(0)))
                tgt = by_suffix.get(sfx)
                if tgt is None:
                    bad.append((t["tc_id"], f, m.group(0), "不存在"))
                    continue
                shared = toks(t.get("distinguishing_axis", "")) & \
                    toks(tgt.get("distinguishing_axis", ""))
                if not shared:
                    bad.append((t["tc_id"], f, m.group(0),
                                f"axis 零共用：{t.get('distinguishing_axis','')!r}"
                                f" vs {tgt.get('distinguishing_axis','')!r}"))
    chk("R-PMH53 交叉引用存在且語意相容", not bad,
        f"{len(bad)} 處 " + str([(a, c, d[:40]) for a, _, c, d in bad[:3]]))
    if refs:
        print(f"  （R-PMH53 末段：本批交叉引用 {len(refs)} 處，逐處列出供人讀）")
        for a, f, r in refs:
            print(f"      {a} .{f} → {r}")

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
    print("\n⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52 之具名義務）**：")
    for s in ("§4.3 tc_title 之形態與字數", "§4.4 Pre-Condition 不得含動作",
              "§5.7 同一觸發之後果是否應合併", "§7 負向案例之配置",
              "§8.2/§8.3 拆分是否恰當", "§8.4.1 造值（推論寫成斷言）",
              "§8.5 Pre-Condition 範圍是否溢出", "§8.7.3 變體條件是否逐字",
              "§10.2 priority 之 rubric 是否切合內容"):
        print(f"    - {s}")
    print("    **以上皆須人讀。** R-PMH52：lint 全綠不得作為 TC 可用之證據。")
    print("\n⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。"
          "\n  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。"
          "\n  本檢查只保證覆核所需之材料存在，不保證覆核已做。")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
