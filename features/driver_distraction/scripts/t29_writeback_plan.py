#!/usr/bin/env python3
"""寫回列計畫之試算（**只讀，不動工作簿**）。

Pei 2026-08-29 裁**乙案**（即寫回 24 則，marker 隨簿，DR 照發，回覆後機械回修）。
本檔只把「寫回會寫成什麼」算出來供覆核 —— **不寫任何一格**。

R-DD2：`tc_id_format = newR1L-DD-{n:03d}`。現行產物之 `B/C/D` 前綴**不合該格式**
（`{n:03d}` 只產生數字），故寫回必須先做最終 tc_id 指派。
本檔以 **leaf 升冪** 為序試算（與盤點表、framework、profile 各表一致），
**該序未經裁定** —— 見上繳 20 §二。
"""
import json
import warnings
from pathlib import Path

import yaml

warnings.filterwarnings("ignore")
import openpyxl                                                    # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "feature.yaml").read_text("utf-8"))["workbook"]
ARTS = ["pilot_group3.json", "batch_b1.json", "batch_b2.json",
        "batch_body_off_init.json"]

tcs = []
for a in ARTS:
    tcs += json.loads((ROOT / "generated" / a).read_text("utf-8"))
tcs.sort(key=lambda t: t["req_id"][-3:])

wb = openpyxl.load_workbook(ROOT / "workbook" / "driver_distraction_00.xlsx")
ws = wb[CFG["sheet"]]
occupied = [r for r in range(CFG["first_data_row"], CFG["last_template_row"] + 1)
            if any(ws.cell(r, c).value not in (None, "") for c in range(3, 35))]
wb.close()

print("=" * 92)
print("T29 —— 寫回列計畫（只讀試算；**未寫入任何一格**）")
print("=" * 92)
print(f"目標分頁：{CFG['sheet']}")
print(f"表頭列 {CFG['header_row']}／首資料列 {CFG['first_data_row']}／"
      f"末模板列 {CFG['last_template_row']}")
print(f"現有非空資料列：{len(occupied)}（{occupied[:5] or '無'}）—— "
      f"{'**全空，無覆寫之虞**' if not occupied else '**非空，須先裁處置**'}")
print(f"寫回方式：{CFG['writeback_method']}／不得寫入之欄：{CFG['do_not_write']}")
print()
r0 = CFG["first_data_row"]
print(f"{'列':>5}  {'新 tc_id':<16}{'現行 tc_id':<16}{'leaf':<6}{'Test Set':<22}{'pri':<5}marker")
print("-" * 92)
for i, t in enumerate(tcs):
    import re
    mk = sorted(set(re.findall(r"\[ASSUMPTION (A-DD\d+)\]",
                               " ".join(t[f] for f in ("pre_conditions", "input_test_data",
                                                       "test_procedure", "expected_result")))))
    print(f"{r0+i:>5}  {'newR1L-DD-%03d' % (i+1):<16}{t['tc_id']:<16}"
          f"{t['req_id'][-3:]:<6}{t['test_set']:<22}{t['priority']:<5}"
          f"{'／'.join(mk) or '（無）'}")
print("-" * 92)
print(f"共 {len(tcs)} 列，佔 {r0}–{r0+len(tcs)-1}；tc_id 由 001 至 {len(tcs):03d}")
chg = [t for i, t in enumerate(tcs) if t["tc_id"] != "newR1L-DD-%03d" % (i + 1)]
print(f"**tc_id 須改者 {len(chg)} 則**（現行 B/C/D 前綴不合 R-DD2 之 `{{n:03d}}`）")
print()
print("無來源可填之欄（產物未載）：", [k for k in CFG["columns"]
                                      if k not in tcs[0] and k != "remarks"])
print("=" * 92)
