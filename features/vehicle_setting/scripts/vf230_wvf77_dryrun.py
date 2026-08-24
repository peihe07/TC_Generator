"""W-VF77 §3.2 —— VF230 之 036 寫回 **dry-run**（**不寫任何檔**）。

**其與 `writeback_036.py` 之別，須先具名**：
  `writeback_036.py` 之 `BOOK` 為**寫死之絕對路徑，指向 CFTS044**，
  且**不讀 `feature.yaml`**。**逕以其寫 VF230 會寫進 CFTS044 之工作簿** ——
  而 CFTS044 之 B 欄 1–237 為 `R-VF83` 明令之凍結欄，
  且 `R-VF109`（V43 §1）明文將 Part 1 排除於解凍之外。
  **故本檔另立，其 BOOK 取自 `feature.yaml` 之 `paths.workbook_vf230`。**

**本檔恆不寫檔**（無 `--write`）。實寫須另一次獨立裁定（`R-VF110`）。

B 欄之序（W-VF77 §3.1-3 之具名處置）：
  **依「量產 seq 序 → pilot #3 序」連號**，B 欄 238 起。
  量產 437 條（seq 268–704）→ B 238–674；pilot #3 3 條（seq 901–903）→ B 675–677。
  **pilot #3 之 seq 901–903 不入 B 欄** —— 其為 pilot 專用號段，
  與量產號段不連續；B 欄為工作簿之流水號，二者不必相同（R-VF83 只令其自 238 起）。
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT.parents[1] / "scripts"))

SHEET = "Test Case Specification 測試用例規範"
HEADER_ROW, FIRST_DATA_ROW = 9, 10
# ---- B 欄起始號：**由實測導出，不寫死**（Pei 裁定 2026-08-24：自 244 起）----
# **R-VF83 寫死 238，其前提「CFTS044 佔 1–237」於本輪實測為假** ——
# 交付路徑之 CFTS044 已增長至 **243**（repo 內副本仍為 237，二者分岔）。
# **寫死一個依賴他本狀態之數，其過時不會被任何檢查攔下** —— 本輪即其實例。
# 故改為每跑一次即實測，並取 **二本之最大末號 + 1**（保守：同時避開二者）。
# 現行實測 max(237, 243) + 1 = **244**，與裁定相符。
B_START_RULED = 244                # Pei 裁定之值，用以與實測交叉驗證
PROJECT, ABBR = "NR1L", "VS"
AUTHOR = "PeiPYHsu"

COLS = {
    "B": "No.#", "C": "Requirement or Design", "D": "Requirement or Design ID",
    "F": "Test Case ID", "G": "Test Group", "H": "Test Set", "I": "Test Item",
    "J": "Pre-Conditions", "K": "Input Test Data", "L": "Test procedure",
    "M": "Expected Result", "N": "Specification Reference", "P": "Test Case Priority",
    "R": "Test Case Design", "AA": "Test Case Author", "AH": "Remarks",
}


def cfts044_last_b() -> tuple[int, dict]:
    """實測 CFTS044 二本之 B 欄末號 —— repo 內副本與交付路徑對應本。

    **二者分岔已知**（W-VF78 實測 237 vs 243）；取其**最大值**以同時避開。
    交付路徑不存在時只取 repo 內者並具名。
    """
    import openpyxl
    seen = {}
    cands = [("repo", next(iter(sorted((FEAT / "inputs").glob("*036*CFTS044*.xlsx"))), None))]
    d = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
             "Vehicle Settings/CFTS044")
    if d.exists():
        cands.append(("delivery", next(iter(sorted(d.glob("*036*.xlsx"))), None)))
    for tag, p in cands:
        if p is None or not p.exists():
            seen[tag] = None
            continue
        wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
        ws = wb[SHEET]
        last = 0
        for r in ws.iter_rows(min_row=FIRST_DATA_ROW, min_col=2, max_col=2,
                              values_only=True):
            if isinstance(r[0], int):
                last = max(last, r[0])
        wb.close()
        seen[tag] = last
    vals = [v for v in seen.values() if v]
    return (max(vals) + 1 if vals else B_START_RULED), seen


def book() -> Path:
    """自 `feature.yaml` 取 VF230 之 036 —— **不寫死路徑**（R-VF33 之對治）。"""
    import yaml
    cfg = yaml.safe_load((FEAT / "feature.yaml").read_text(encoding="utf-8"))
    p = Path(cfg["paths"]["workbook_vf230"])
    return p if p.is_absolute() else FEAT / p


def sources() -> list[Path]:
    """寫回之來源 —— **`data/vf230_batches.tsv` 為單一權威**（R-VF105 之延伸）。
    清單所列而檔案不存在者即停。"""
    man = FEAT / "data" / "vf230_batches.tsv"
    rows = list(csv.DictReader(man.open(encoding="utf-8"), delimiter="\t"))
    out = []
    for r in rows:
        q = FEAT / r["file"]
        if not q.exists():
            raise SystemExit(f"來源清單所列而檔案不存在：{r['batch']} ({r['file']})，停")
        out.append(q)
    return out


def rows_from(files: list[Path], b_start: int) -> list[dict]:
    titles = {r["swe_id"]: r["title"].replace("\\n", " ")
              for r in csv.DictReader(
                  (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"),
                  delimiter="\t")}
    out, b = [], b_start
    for f in files:
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            leaf = tc["leaf_id"]
            out.append({
                "B": b, "C": titles.get(leaf, ""), "D": leaf,
                "F": "", "G": "Vehicle Setting",          # F：R-VF83 令維持不寫
                "H": tc["test_set"], "I": tc["test_item"], "J": tc["pre_conditions"],
                "K": tc["input_test_data"], "L": tc["test_procedure"],
                "M": tc["expected_result"], "N": tc["specification_reference"],
                "P": tc["priority"], "R": tc["design_method"], "AA": AUTHOR,
                "AH": str(tc.get("remarks", "")).strip(),
                "_seq": tc["seq"], "_src": f.name,
            })
            b += 1
    return out


def main() -> None:
    bk = book()
    print(f"=== W-VF77 dry-run（**不寫任何檔**）===")
    print(f"目標工作簿（自 feature.yaml `paths.workbook_vf230`）：\n  {bk}")
    print(f"  存在：{bk.exists()}")
    b_start, seen = cfts044_last_b()
    print(f"\nB 欄起始號（**實測導出，不寫死**）：")
    print(f"  CFTS044 之 B 欄末號 —— repo 內 {seen.get('repo')}／"
          f"交付路徑 {seen.get('delivery')}"
          + ("  ⚠ **二者分岔**" if seen.get('repo') != seen.get('delivery') else ""))
    print(f"  取其最大 + 1 = **{b_start}**（Pei 裁定之值 {B_START_RULED}）"
          f"  {'✅ 相符' if b_start == B_START_RULED else '❌ 不符 —— 停'}")
    if b_start != B_START_RULED:
        raise SystemExit(f"B 欄起始號之實測（{b_start}）與裁定（{B_START_RULED}）不符，"
                         "其一已過時，停")
    files = sources()
    print(f"來源：`data/vf230_batches.tsv` 之 {len(files)} 檔")
    rows = rows_from(files, b_start)
    n = len(rows)
    print(f"\n列數 **{n}**；B 欄 **{rows[0]['B']} – {rows[-1]['B']}**"
          f"（期望 {b_start} – {b_start + n - 1}）")
    ok_b = [r["B"] for r in rows] == list(range(b_start, b_start + n))
    print(f"  B 欄連號：{'✅' if ok_b else '❌'}")

    print(f"\n--- 四項驗證 ---")
    print(f"1) D／H／I／N 四欄非空數（期望皆 {n}）：")
    for k in ("D", "H", "I", "N"):
        c = sum(1 for r in rows if str(r[k]).strip())
        print(f"     {k} {COLS[k]:26} {c:>4}  {'✅' if c == n else '❌'}")

    pend = [r for r in rows if "PENDING" in str(r["K"]) or "PENDING" in str(r["M"])
            or "PENDING" in str(r["J"])]
    print(f"2) 含 `PENDING: DR-n` 之列：**{len(pend)}**")
    for r in pend[:5]:
        w = next(c for c in ("J", "K", "M") if "PENDING" in str(r[c]))
        print(f"     B{r['B']} seq {r['_seq']}  欄 {w}")

    ah = [r for r in rows if str(r["AH"]).strip()]
    print(f"3) AH（Remarks）非空數：**{len(ah)}**")
    for r in ah[:4]:
        print(f"     B{r['B']} seq {r['_seq']}  {str(r['AH'])[:70]}")

    k_non_na = [r for r in rows if str(r["K"]).strip() != "NA"]
    print(f"4) K（Input Test Data）非 `NA` 之列：**{len(k_non_na)}**"
          f"  ← R-VF101 之佔位式")
    print(f"     其形式抽驗：{k_non_na[0]['K'][:64] if k_non_na else '（無）'}")

    print(f"\n--- 其餘欄之分布 ---")
    print(f"  P（Priority）：{dict(collections.Counter(r['P'] for r in rows))}")
    print(f"  R（Design）  ：{dict(collections.Counter(r['R'] for r in rows))}")
    print(f"  G 全為 `Vehicle Setting`："
          f"{'✅' if all(r['G'] == 'Vehicle Setting' for r in rows) else '❌'}")
    print(f"  F（TC ID）全空（R-VF83）："
          f"{'✅' if all(not r['F'] for r in rows) else '❌'}")

    prev = FEAT / "docs/reports/vf230_writeback_preview.tsv"
    with prev.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["B", "_seq", "_src", "C", "D", "G", "H",
                                           "I", "J", "K", "L", "M", "N", "P", "R",
                                           "AA", "AH", "F"], delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"\n預覽表 → {prev.relative_to(FEAT)}（{n} 列）")
    print(f"**未寫入任何工作簿。實寫須獨立裁定（R-VF110）。**")


if __name__ == "__main__":
    main()
