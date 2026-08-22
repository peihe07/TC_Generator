"""canon §9 十七項自檢之可機械化部分（W-53；18 輪依 R-VS41 更新）。

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


def _dbc_vals() -> dict[str, dict[str, str]]:
    """自基線 DBC 讀 `VAL_` 表（檔為 ISO-8859，須以 latin-1 讀）。"""
    out: dict[str, dict[str, str]] = {}
    for f in ("PDT27_E2A_R4_BHCAN.dbc", "PDT27_E2A_R5_FDCAN8.dbc"):
        text = (FEAT / "inputs" / f).read_text(encoding="latin-1")
        for m in re.finditer(r"^VAL_\s+\d+\s+(\w+)\s+(.*?);", text, re.M | re.S):
            out.setdefault(m.group(1), {}).update(
                dict(re.findall(r'(\d+)\s+"([^"]*)"', m.group(2))))
    return out


DBC_VALS = _dbc_vals()
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
    # R-VS41(1)：訊號採 `$<MESSAGE>.<Signal>$ = <raw> (<label>)`。
    # R-VS9(5) 仍禁**規格 token** 之 `$var$`（無 `.` 者）入 procedure／ER。
    for it in items(tc["test_procedure"]) + items(tc["expected_result"]):
        for tok in re.findall(r"\$([^$]+)\$", it):
            if "." not in tok:
                e.append(f"R-VS9(5) {tid}: procedure/ER 出現規格 token ${tok}$")
        if re.search(r"\b\w+ in [A-Z0-9_]+ on (CAN-B|BH-CAN|CAN-FD)\b", it):
            e.append(f"R-VS41(1) {tid}: 殘留已撤回之三件組 —— {it.strip()[:50]}")
        if re.search(r"\$[A-Z0-9_]+\.", it):
            e.append(f"R-VS52 {tid}: 訊號名仍以 `$` 包夾 —— {it.strip()[:50]}")
        if "is registered without a bus error" in it:
            e.append(f"R-VS52 {tid}: 送出型 ER 仍用已撤回之措辭 —— {it.strip()[:50]}")
    # 56 包 §2（35 輪 W-95）：record 子句之處置
    for it in items(tc["test_procedure"]):
        if re.search(r"\brecord\b(?!ed)", it, re.I) and not re.search(
                r"\brecord\b[^\n]*\bas\s+[A-Z][A-Za-z0-9_]*", it):
            e.append(f"56§2(a) {tid}: procedure 有 record 子句而無變數名 —— {it.strip()[:50]}")
    for it in items(tc["test_procedure"]) + items(tc["expected_result"]):
        if re.search(r"recorded in step \d+", it, re.I):
            e.append(f"R-VS52(4) {tid}: 仍以「recorded in step N」比較 —— {it.strip()[:50]}")
    for it in items(tc["test_procedure"]) + items(tc["expected_result"]):
        # R-VS52（34 輪）：訊號名不再以 `$` 包夾 —— 舊式 regex 於新形態下靜默失效
        m = re.search(r"\b[A-Z][A-Z0-9_]+\.(\w+)\s*=\s*(\d+)\s*\(([^)]+)\)", it)
        if m and m.group(1) not in DBC_VALS:
            e.append(f"L-VS2 {tid}: signal {m.group(1)} 不在基線 DBC")
        elif m and DBC_VALS[m.group(1)].get(m.group(2)) != m.group(3):
            e.append(f"R-VS39 {tid}: {m.group(1)} 之 {m.group(2)} 標籤非 DBC VAL_ 逐字 —— "
                     f"見 {m.group(3)!r}，DBC 為 {DBC_VALS[m.group(1)].get(m.group(2))!r}")
    return e


def main() -> None:
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "generated/batch01_v2.json"
    d = json.loads((FEAT / name).read_text(encoding="utf-8"))
    print(f"檢查 {name}")
    errs = [x for tc in d["tcs"] for x in check(tc)]
    print(f"TC {len(d['tcs'])} 條，機械檢查發現 {len(errs)} 項：")
    for x in errs:
        print("  ", x)


if __name__ == "__main__":
    main()
