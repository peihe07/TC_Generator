#!/usr/bin/env python3
"""`tc_id` 之單次指派（R-PMH143，38 包步驟 4）。

**其四項規則**：
  (a) **連續編號，不留空** —— provisional 期間之空位（`-024` 依 R-PMH129 撤除
      所遺者）**不保留**；provisional 本為暫號，其連續性無保存價值；
  (b) 順序依 **Test Set 之 Layer 2 定版順序**（R-PMH36），組內依其 leaf 之
      **037 列序**；
  (c) 格式 `NR1L-DisclaimerScreen-{NNN}`（R-PMH16），`NNN` 自 `001` 起；
  (d) 產出 provisional → final 之映射表，落檔於 `data/tc_id_map.tsv`。

**產出寫入 `generated/final/`，不覆寫 `generated/batchNN.json`。**
其理由：`generated/batchNN.json` 為 `gen_batchNN.py` 之產物，
**就地改寫會在下一次執行產生器時被無聲還原**；分處二地使該風險不存在。
**寫回工作簿之來源為 `generated/final/`。**

**本檔非檢查程式** —— 其不判定任何事、不產生 PASS／FAIL；
不在 R-PMH104 之凍結範圍內（R-PMH107 之判別法）。
"""
import json
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

# R-PMH36 之 Layer 2 定版順序
ORDER = ["Splash Screen", "Disclaimer Screen", "Startup Animation", "Startup Sounds",
         "Power Transitions", "Power Off Behavior", "Voice Assistant Key", "Off Road Plus"]
A03 = ("inputs/FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1 STLA 報告.xlsx")


def row_order_037() -> dict:
    """037 `Analysis Report` 之列序 —— 組內排序之依據（R-PMH143(b)）。"""
    wb = openpyxl.load_workbook(ROOT / A03, read_only=True, data_only=True)
    ws = wb["Analysis Report"]
    out = {}
    for i, r in enumerate(ws.iter_rows(min_row=8, values_only=True), 8):
        sid = str(r[0] or "").strip()
        if sid.startswith("SWE1-HMI-PM-") and sid not in out:
            out[sid] = i
    wb.close()
    return out


def collect() -> list:
    out = []
    for p in sorted((ROOT / "generated").glob("batch*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for k, tc in enumerate(d["tcs"]):
            out.append((tc, d, p.stem, k))
    return out


def main() -> None:
    r037 = row_order_037()
    items = collect()
    unknown = sorted({t["leaf_id"] for t, *_ in items if t["leaf_id"] not in r037})
    if unknown:
        raise SystemExit(f"leaf 不在 037 之列序內：{unknown}")
    items.sort(key=lambda x: (ORDER.index(x[0]["test_set"]),
                              r037[x[0]["leaf_id"]], x[2], x[3]))
    rows, by_batch = [], {}
    for n, (tc, d, batch, k) in enumerate(items, 1):
        final = f"NR1L-DisclaimerScreen-{n:03d}"
        rows.append((tc["tc_id"], final, tc["leaf_id"], tc["test_set"], batch))
        new = dict(tc)
        new["tc_id"] = final
        new["provisional_tc_id"] = tc["tc_id"]
        by_batch.setdefault(batch, (d, []))[1].append(new)

    m = ROOT / "data" / "tc_id_map.tsv"
    m.write_text("provisional_tc_id\tfinal_tc_id\tleaf_id\ttest_set\tbatch\n"
                 + "\n".join("\t".join(r) for r in rows) + "\n", encoding="utf-8")

    outdir = ROOT / "generated" / "final"
    outdir.mkdir(exist_ok=True)
    for batch, (d, tcs) in by_batch.items():
        doc = dict(d)
        doc["tcs"] = tcs
        # R-PMH143：指派後狀態改 `final` —— `check_write_back` 之 (d) 據此放行。
        doc["tc_id_status"] = "final"
        doc["tc_id_assignment"] = ("R-PMH143（38 包步驟 4）—— 連續編號不留空；"
                                   "順序依 Test Set 之 R-PMH36 定版順序，組內依 037 列序。"
                                   "映射表：data/tc_id_map.tsv")
        (outdir / f"{batch}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")

    # 停止條件 9：映射表之 provisional 與 final 筆數須相等且各自無重複
    prov, fin = {r[0] for r in rows}, {r[1] for r in rows}
    ok = len(prov) == len(fin) == len(rows)
    print(f"指派 {len(rows)} 條；provisional 相異 {len(prov)}；final 相異 {len(fin)}；"
          f"{'一致 ✅' if ok else '❌ 不一致'}")
    print(f"映射表：{m.relative_to(ROOT)}")
    print(f"final 批次檔：{len(by_batch)} 份於 generated/final/")
    gaps = [n for n in range(1, len(rows) + 1)
            if f"NR1L-DisclaimerScreen-{n:03d}" not in fin]
    print(f"編號空位 = {len(gaps)}（R-PMH143(a)：應為 0）")
    sys.exit(0 if (ok and not gaps) else 1)


if __name__ == "__main__":
    main()
