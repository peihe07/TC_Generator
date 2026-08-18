"""G145 —— 閘門觸發數彙整（R-P212）。

R-P212 併記之制度缺口：**上繳文件未載閘門觸發紀錄，致事後無從查核**
（28 包回查 16–26 包時只能以「lint 皆 exit=0」反推，非直接紀錄）。
往後上繳包須載明各閘之觸發數（**含 0**）。

本腳本**自動彙整**（非人工填表）——
其數字直接取自各閘門腳本之執行結果，避免抄錄誤差。

含 B5（R-P213）之白名單命中統計：
  - **命中數** —— 因命中「測試選用量」白名單而被排除之純數值 token 數
  - **未命中數** —— 未命中白名單而觸發之純數值 token 數
R-P213 所慮之**反向風險**（規格閾值所在行恰不含規格參數跡象而被誤排除）
其發生率仍無法由本統計直接量得 —— 據實標明。

用法：
    python features/power/scripts/gate_trigger_report.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(SCRIPTS))


def run(script: str, *args: str) -> str:
    r = subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                       capture_output=True, text=True)
    return r.stdout + r.stderr


def lint_counts() -> dict:
    out = run("lint_tcs.py")
    blocking = 0 if "【阻斷類】PASS" in out else int(
        re.search(r"【阻斷類】\*\*(\d+) 項", out).group(1))
    adj = int(re.search(r"(\d+) 項待裁", out).group(1))
    by_rule: dict[str, int] = {}
    for m in re.finditer(r"^\s+(R-P\S+|§\S+)\s", out, re.M):
        by_rule[m.group(1)] = by_rule.get(m.group(1), 0) + 1
    return {"blocking": blocking, "adjudicate": adj, "by_rule": by_rule}


def whitelist_stats() -> dict:
    """B5 / R-P213 —— 白名單之命中與未命中。"""
    import lint_tcs as L
    hit = miss = 0
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        clause = {l["parent"]: L._fold_ident(str(l.get("source_clause", "")))
                  for l in b["leaves"]}
        for tc in b.get("tcs", []):
            raw = str(tc.get("input_test_data", ""))
            src = clause.get(tc["req_id"], "")
            for tok in sorted(set(L.ER_PROPER_RE.findall(L._fold_ident(raw)))):
                if not tok.isdigit() or tok in L.ER_PROPER_SKIP:
                    continue
                if tok in src:
                    continue                       # 見於 clause，本就不觸發
                if L._numeric_is_test_quantity("input_test_data", raw, tok):
                    hit += 1
                else:
                    miss += 1
    return {"hit": hit, "miss": miss}


GATES = [
    ("G0", "verify_gates.py", None, r"G0 素材身分: (\d+ / \d+)"),
    ("G70 lint", None, None, None),
    ("G94", "verify_source_clause.py", None, r"G94：(\S+ 相符)"),
    ("G99", "verify_anchor_set.py", None, r"G99：(\S+ 相等)"),
    ("G103", "verify_layer3.py", None, r"G103：(\S+ 相等)"),
    ("G108", "check_edit_integrity.py", None, r"G108：(\S+ 完整)"),
    ("G113", "or_branch_coverage.py", "--self-test", r"五項中重現 \*\*(\S+)\*\*"),
    ("G121", "build_reconciliation.py", None, r"G121：(\S+)"),
    ("G129", "verify_reasoning.py", None, r"G129：(\d+ / \d+)"),
    ("G136", "audit_pattern_variants.py", None, r"未涵蓋者 (\d+)"),
    # G137 之輸出於 30 包依 R-P219 改為並列二口徑；本式取**齊備率**。
    # 舊式 `三項皆涵蓋 (\d+)` 於該改動後失配而顯示「（未匹配）」——
    # 該回歸由 R-P220 之重跑比對當場揭出（30 包）。
    ("G137（齊備率）", "assess_reasoning.py", None,
     r"齊備率（第 1\+2\+3 同時成立）\*\*：(\d+ / \d+)"),
    ("G137（第 2 項單項率）", "assess_reasoning.py", None,
     r"2 關鍵情境條件 (\d+ / \d+)"),
    ("G146", "verify_ledger_dup.py", None, r"G146：(\S+)"),
    ("G142", "audit_precond_state.py", None, r"\(a\) (\d+)、\*\*\(b\) (\d+)\*\*"),
]


def main() -> None:
    rows = []
    for name, script, arg, pat in GATES:
        if script is None:
            continue
        out = run(script, *( [arg] if arg else [] ))
        m = re.search(pat, out) if pat else None
        rows.append((name, m.group(0) if m else "（未匹配）"))

    lc = lint_counts()
    ws = whitelist_stats()

    md = ["# G145 —— 閘門觸發數彙整（R-P212）\n",
          "\n> **自動彙整**：數字直接取自各閘門腳本之執行結果，非人工填表。\n",
          "> R-P212 之制度缺口 —— 上繳未載觸發紀錄致事後無從查核 —— 自本包起以本表補之。\n",
          "\n## 1. lint（G70）之觸發\n\n"
          f"| 類 | 數 |\n|---|---|\n"
          f"| **阻斷類** | **{lc['blocking']}** |\n"
          f"| 待人工裁決類 | {lc['adjudicate']} |\n\n"
          "### 逐 rule（含 0）\n\n| rule | 觸發數 |\n|---|---|\n"]
    for rule in ("R-P42(b)", "R-P96(a)", "R-P96(b)", "R-P142",
                 "R-P104", "R-P107", "R-P109", "R-P109(擴充)"):
        md.append(f"| `{rule}` | **{lc['by_rule'].get(rule, 0)}** |\n")
    md.append("\n> `R-P104` / `R-P107` / `R-P109` 為批次層閘門（G79 / G81 / G82）——\n"
              "> 其觸發數自本包起逐包記錄，即 28 包 R-P208 回查所缺者。\n")

    md.append("\n## 2. 其餘閘門\n\n| 閘 | 實測 |\n|---|---|\n")
    for name, val in rows:
        md.append(f"| {name} | {val} |\n")

    md.append("\n## 3. 白名單命中統計（B5 / R-P213）\n\n"
              f"| 項 | 數 |\n|---|---|\n"
              f"| **命中白名單而排除**（測試選用量）| **{ws['hit']}** |\n"
              f"| **未命中而觸發** | **{ws['miss']}** |\n"
              "\n**R-P213(b) 之反向風險仍未量得** —— "
              "「某規格閾值所在行恰不含規格參數跡象而被誤排除」之發生率，"
              "**本統計無法直接量測**：其需知道每個被排除之數值是否實為規格閾值，"
              "而該判斷正是白名單所要取代者。**據實標明，未以命中數充作其代理。**\n")

    (DATA / "g145_gate_triggers.md").write_text("".join(md), encoding="utf-8")
    print(f"wrote {(DATA / 'g145_gate_triggers.md').relative_to(ROOT)}")
    print(f"  lint 阻斷 {lc['blocking']}、待裁 {lc['adjudicate']}")
    print(f"  批次層閘門：R-P104 {lc['by_rule'].get('R-P104',0)}、"
          f"R-P107 {lc['by_rule'].get('R-P107',0)}、"
          f"R-P109 {lc['by_rule'].get('R-P109',0)}、"
          f"R-P109(擴充) {lc['by_rule'].get('R-P109(擴充)',0)}")
    print(f"  白名單：命中 {ws['hit']}、未命中 {ws['miss']}")


if __name__ == "__main__":
    main()
