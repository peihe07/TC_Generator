"""canon §9 十七項自檢之可機械化部分（W-53）。

不可機械化者（1 之 capability 判斷、3 之 trigger vs 環境前提、
7 之 snippet 適用性、11 之 FP/FF、12 之上游分解、13 之方法適配、
17 之來源優先）由人讀，於上繳包逐項記明。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
KEYS = ("tc_title", "pre_conditions", "input_test_data", "test_procedure",
        "expected_result", "specification_reference", "design_method",
        "priority", "split_flag", "split_reason")
NO_TRAIL = ("pre_conditions", "input_test_data", "test_procedure", "expected_result")
MODALS = re.compile(r"\b(shall|will|should|would)\b", re.I)
TITLE_MODALS = re.compile(r"\b(should|will|shall|properly|successfully)\b", re.I)


def items(field: str) -> list[str]:
    """以編號行切出 numbered item（續行併入其 item）——§11 之規制單位。"""
    out: list[str] = []
    for line in field.split("\n"):
        if re.match(r"^\s*\d+\.", line) or not out:
            out.append(line)
        else:
            out[-1] += "\n" + line
    return out


def check(tc: dict) -> list[str]:
    e = []
    tid = tc["leaf_id"]
    for k in KEYS:
        if k not in tc:
            e.append(f"§10.1 {tid}: 缺鍵 {k}")
    w = len(tc["tc_title"].split())
    if not 2 <= w <= 14:
        e.append(f"§4.3 {tid}: tc_title {w} 字，超出 2–14")
    if TITLE_MODALS.search(tc["tc_title"]):
        e.append(f"§4.3 {tid}: tc_title 含模態或含糊詞")
    if "(" not in tc["test_item"] or not tc["test_item"].rstrip().endswith(")"):
        e.append(f"§4.3.1 {tid}: test_item 缺括號下半")
    for k in NO_TRAIL:
        for it in items(tc[k]):
            if it.strip().endswith((".", "。")):
                e.append(f"§11 {tid}.{k}: item 有尾句號 —— {it.strip()[-40:]}")
    for k in NO_TRAIL + ("tc_title",):
        if re.search(r"\[[^\]]*\]", tc[k]):
            e.append(f"§11 {tid}.{k}: 出現方括號")
        if re.search(r"(?<![\w])'[^']+'(?![\w])", tc[k]):
            e.append(f"§11 {tid}.{k}: 出現單引號")
    for it in items(tc["expected_result"]):
        if MODALS.search(it):
            e.append(f"§6 {tid}: ER 含模態動詞 —— {it.strip()[:50]}")
    p, r = items(tc["test_procedure"]), items(tc["expected_result"])
    if len(p) < 2:
        e.append(f"§10.5 {tid}: procedure 少於 2 步")
    if len(p) != len(r):
        e.append(f"§6 {tid}: procedure {len(p)} 步 vs ER {len(r)} 條，非 1:1")
    if tc["priority"] not in ("P0", "P1", "P2", "P3"):
        e.append(f"§10.2 {tid}: priority 非 P0–P3")
    for ln in tc["specification_reference"].split("\n"):
        if not re.fullmatch(r"CFTS044-\d{7}", ln.strip()):
            e.append(f"§10.7 {tid}: spec_ref 格式 —— {ln}")
    fin = p[-1]
    if not re.search(r"\b(check that|to verify|confirm that)\b", fin, re.I):
        e.append(f"§5.5 {tid}: 末步驟無驗證意圖")
    for it in p:
        if re.match(r"^\s*\d+\.\s*(observe|see if|verify|watch|monitor|inspect)\b", it, re.I):
            e.append(f"§5.1 {tid}: 禁用動詞為主動詞 —— {it.strip()[:40]}")
    if "$" in tc["test_procedure"] or "$" in tc["expected_result"]:
        for it in items(tc["test_procedure"]) + items(tc["expected_result"]):
            if "$" in it and "PENDING" not in it:
                e.append(f"R-VS9(5) {tid}: procedure/ER 出現 $var$ —— {it.strip()[:40]}")
    return e


def main() -> None:
    d = json.loads((FEAT / "generated/batch01.json").read_text(encoding="utf-8"))
    errs = [x for tc in d["tcs"] for x in check(tc)]
    print(f"TC {len(d['tcs'])} 條，機械檢查發現 {len(errs)} 項：")
    for x in errs:
        print("  ", x)


if __name__ == "__main__":
    main()
