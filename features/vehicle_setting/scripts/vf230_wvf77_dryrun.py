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
B_START = 238                      # R-VF83
PROJECT, ABBR = "NR1L", "VS"
AUTHOR = "PeiPYHsu"

COLS = {
    "B": "No.#", "C": "Requirement or Design", "D": "Requirement or Design ID",
    "F": "Test Case ID", "G": "Test Group", "H": "Test Set", "I": "Test Item",
    "J": "Pre-Conditions", "K": "Input Test Data", "L": "Test procedure",
    "M": "Expected Result", "N": "Specification Reference", "P": "Test Case Priority",
    "R": "Test Case Design", "AA": "Test Case Author", "AH": "Remarks",
}


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


def rows_from(files: list[Path]) -> list[dict]:
    titles = {r["swe_id"]: r["title"].replace("\\n", " ")
              for r in csv.DictReader(
                  (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"),
                  delimiter="\t")}
    out, b = [], B_START
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
    files = sources()
    print(f"來源：`data/vf230_batches.tsv` 之 {len(files)} 檔")
    rows = rows_from(files)
    n = len(rows)
    print(f"\n列數 **{n}**；B 欄 **{rows[0]['B']} – {rows[-1]['B']}**"
          f"（期望 {B_START} – {B_START + n - 1}）")
    ok_b = [r["B"] for r in rows] == list(range(B_START, B_START + n))
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
