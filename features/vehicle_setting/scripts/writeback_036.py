"""W-120（67 包）—— 036 工作簿之寫回器 ＋ **dry-run**。

母本：`.../CFTS044/FM-WI-FSM-036-A01 …_CFTS044_Vehicle Controls_20260819.xlsx`
分頁 `Test Case Specification 測試用例規範`；**表頭列 9；資料列 10 起**。

**本檔預設只做 dry-run。實寫須 `--write` 且待 Pei 核可（67 包之閘）。**

欄位對映（66 包 §3）：只寫下列 16 欄，其餘一格不動。
`reasoning` 不入工作簿；E／O／Q／S／T–Z／AB–AG 留空。
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
BOOK = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
            "Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
            "STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx")
SHEET = "Test Case Specification 測試用例規範"
HEADER_ROW, FIRST_DATA_ROW = 9, 10

COLS = {  # 欄字母 → (欄名, 取值來源)
    "B": "No.#", "C": "Requirement or Design", "D": "Requirement or Design ID",
    "F": "Test Case ID", "G": "Test Group", "H": "Test Set", "I": "Test Item",
    "J": "Pre-Conditions", "K": "Input Test Data", "L": "Test procedure",
    "M": "Expected Result", "N": "Specification Reference", "P": "Test Case Priority",
    "R": "Test Case Design", "AA": "Test Case Author", "AH": "Remarks",
}
CONTROLLED = {
    "功能測試 (Functional based ; no specific technique)", "狀態轉換 (State Transition Testing)",
    "決策表 (Decision Table Testing)", "等價劃分 (Equivalence Partitioning, EP)",
    "邊界值分析 (Boundary Value Analysis, BVA)",
    "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
    "情境 / 用例 (Scenario / Use Case Testing)", "負向測試 (Negative / Invalid)",
    "基礎故障注入 (Fault Injection Lite)",
}
PROJECT, ABBR = "NR1L", "VS"
# **D-4（47 輪，Pei 2026-08-23）**：`AA` 欄之作者姓名。46 輪以 `<AUTHOR>` 佔位。
AUTHOR = "PeiPYHsu"


def latest_batches() -> list[Path]:
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    return [max(v)[1] for k, v in sorted(groups.items())]


def req_title() -> dict[str, str]:
    """C 欄之來源 —— 037 之 `Requirement Title`（本 repo 已解為 leaf → title）。"""
    p = FEAT / "data/leaves.tsv"
    out = {}
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            key = r.get("swe_id") or r.get("leaf_id") or r.get("id")
            title = r.get("title") or r.get("requirement_title") or ""
            if key:
                out[key] = title
    return out


def rows_from_json(files: list[Path]) -> list[dict]:
    titles = req_title()
    disclosure = {}
    p = FEAT / "docs/reports/delivery_disclosure.md"
    if p.exists():
        for line in p.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"\| `batch\d+\w*` \| `([^`]+)` \| ([^|]*)\|", line)
            if m:
                disclosure[m.group(1)] = m.group(2).strip()
    out, seq = [], 0
    for f in files:
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            seq += 1
            leaf = tc["leaf_id"]
            pending = "PENDING" in tc["expected_result"]
            out.append({
                "B": seq, "C": titles.get(leaf, ""), "D": leaf,
                "F": f"{PROJECT}-{ABBR}-{seq:03d}", "G": "Vehicle Setting",
                "H": tc["test_set"], "I": tc["test_item"], "J": tc["pre_conditions"],
                "K": tc["input_test_data"], "L": tc["test_procedure"],
                "M": tc["expected_result"], "N": tc["specification_reference"],
                "P": tc["priority"], "R": tc["design_method"], "AA": AUTHOR,
                "AH": (f"BLOCKED: {tc.get('dr_dependent', 'DR-?')}；"
                       f"待補來源：TLM HMI Document／DR-5-B" if pending else ""),
            })
    return out


def dry_run(rows: list[dict], label: str) -> dict:
    n = len(rows)
    nonempty = {k: sum(1 for r in rows if str(r[k]).strip()) for k in COLS}
    nlines = collections.Counter(len(str(r["N"]).split("\n")) for r in rows)
    two_part = sum(1 for r in rows if "\n\n" in str(r["I"]))
    paren = sum(1 for r in rows if str(r["I"]).rstrip().endswith(")"))
    k_bad = sum(1 for r in rows if str(r["K"]).strip() != "NA")
    n_bad = sum(1 for r in rows if re.search(r"[,;] *CFTS", str(r["N"])))
    p_cnt = collections.Counter(r["P"] for r in rows)
    r_bad = sum(1 for r in rows if r["R"] not in CONTROLLED)
    ah = sum(1 for r in rows if str(r["AH"]).strip())
    return {"label": label, "rows": n, "nonempty": nonempty, "n_lines": dict(nlines),
            "I_two_part": two_part, "I_paren": paren, "K_not_NA": k_bad,
            "N_comma_joined": n_bad, "P": dict(p_cnt), "R_out_of_domain": r_bad,
            "AH_nonempty": ah}


def main() -> None:
    if "--write" in sys.argv:
        raise SystemExit("實寫之閘未開（67 包）：dry-run 通過且 Pei 核可後方得執行。")
    files = latest_batches()
    rows = rows_from_json(files)
    subj = dry_run(rows, "正常輸入")

    # ── R-VS54 錨點：刻意違規之 JSON（四處植入）──────────────────
    bad = [dict(r) for r in rows]
    bad[0]["K"] = "None"                                   # K 欄非 NA
    # N 欄逗號串接 —— 須挑**多值列**植入，否則單值列改不出違規
    multi = next((i for i, r in enumerate(rows) if "\n" in str(r["N"])), 1)
    bad[multi]["N"] = str(bad[multi]["N"]).replace("\n", ", ")
    bad[2]["I"] = str(bad[2]["I"]).replace("\n\n", " ")    # I 欄無空行
    bad[3]["R"] = "State Transition"                        # R 欄純英文
    anch = dry_run(bad, "刻意違規之錨點")

    out = ["# writeback dry-run（W-120，42 輪）", "",
           f"母本：`{BOOK.name}`", f"分頁：`{SHEET}`；表頭列 {HEADER_ROW}；"
           f"資料列 {FIRST_DATA_ROW} 起", "",
           "**本輪不實寫**（67 包之閘：dry-run 通過 ＋ Pei 核可 ＋ 母本備份）。", "",
           "## (1) 將寫入之列數", "",
           f"| 項 | 值 |", "|---|---:|",
           f"| 將寫入 | **{subj['rows']}** |", f"| 對照（交付累計） | 139 |",
           f"| 差 | **{subj['rows'] - 139}** |", "",
           "## (2) 逐欄非空數（16 欄）", "",
           "| 欄 | 欄名 | 非空 | 應為 |", "|---|---|---:|---:|"]
    for k, name in COLS.items():
        out.append(f"| `{k}` | {name} | {subj['nonempty'][k]} | "
                   f"{subj['rows'] if k not in ('AH',) else 21} |")
    out += ["", "## (3) N 欄之多值列 —— 行數分布", "", "| 行數 | 列數 |", "|---:|---:|"]
    for k in sorted(subj["n_lines"]):
        out.append(f"| {k} | {subj['n_lines'][k]} |")
    out += ["", "## (4)–(7) 判準檢查（正常輸入 vs 錨點並列）", "",
            "| 判準 | 應為 | 正常輸入 | 錨點（刻意違規） | 判 |", "|---|---|---:|---:|---|",
            f"| (4) I 欄含空行 | {subj['rows']} | {subj['I_two_part']} | "
            f"{anch['I_two_part']} | "
            f"{'PASS，可失敗' if subj['I_two_part'] == subj['rows'] and anch['I_two_part'] < subj['rows'] else '⚠'} |",
            f"| (4) I 欄括號收尾 | {subj['rows']} | {subj['I_paren']} | {anch['I_paren']} | "
            f"{'PASS' if subj['I_paren'] == subj['rows'] else '⚠'} |",
            f"| (5) K 欄非 `NA` | 0 | {subj['K_not_NA']} | {anch['K_not_NA']} | "
            f"{'PASS，可失敗' if subj['K_not_NA'] == 0 and anch['K_not_NA'] > 0 else '⚠'} |",
            f"| (6) R 欄不在受控 9 值 | 0 | {subj['R_out_of_domain']} | "
            f"{anch['R_out_of_domain']} | "
            f"{'PASS，可失敗' if subj['R_out_of_domain'] == 0 and anch['R_out_of_domain'] > 0 else '⚠'} |",
            f"| （附）N 欄逗號串接 | 0 | {subj['N_comma_joined']} | "
            f"{anch['N_comma_joined']} | "
            f"{'PASS，可失敗' if subj['N_comma_joined'] == 0 and anch['N_comma_joined'] > 0 else '⚠'} |",
            f"| (7) AH 欄非空 | 21 | {subj['AH_nonempty']} | {anch['AH_nonempty']} | "
            f"{'PASS' if subj['AH_nonempty'] == 21 else '⚠ 見上繳 37 §2'} |", "",
            "## (6) P 欄之三級計數", "", "| 級 | 列數 |", "|---|---:|"]
    for k in sorted(subj["P"]):
        out.append(f"| {k} | {subj['P'][k]} |")
    out += ["", "## (8) 母本現有列將被清空之欄範圍", ""]
    try:
        import openpyxl
        ws = openpyxl.load_workbook(BOOK, read_only=True, data_only=True)[SHEET]
        cnt, tot = collections.Counter(), 0
        for i, row in enumerate(ws.iter_rows(min_row=FIRST_DATA_ROW, values_only=True),
                                start=FIRST_DATA_ROW):
            if not any(c is not None for c in row):
                continue
            tot += 1
            for k in COLS:
                idx = (ord(k[-1]) - 65) + (26 if len(k) == 2 else 0)
                if idx < len(row) and row[idx] is not None and str(row[idx]).strip():
                    cnt[k] += 1
        out += [f"母本現有資料列：**{tot}**（清空範圍 B–AH）", "",
                "| 欄 | 清空前非空 |", "|---|---:|"]
        for k in COLS:
            out.append(f"| `{k}` | {cnt[k]} |")
    except Exception as e:                     # noqa: BLE001
        out.append(f"**母本讀取失敗**：{e}")
    (FEAT / "docs/reports/writeback_dryrun.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out[:4]))
    print(f"\n將寫入 {subj['rows']} 列；I 兩段 {subj['I_two_part']}／"
          f"K 非 NA {subj['K_not_NA']}／R 出域 {subj['R_out_of_domain']}／"
          f"AH 非空 {subj['AH_nonempty']}")
    print(f"錨點：I 兩段 {anch['I_two_part']}／K 非 NA {anch['K_not_NA']}／"
          f"R 出域 {anch['R_out_of_domain']}／N 逗號 {anch['N_comma_joined']}")


if __name__ == "__main__":
    main()
