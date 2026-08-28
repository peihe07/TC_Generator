#!/usr/bin/env python3
"""併簿探針 —— 下放包 26 §七-6 之機械側佐證（**下放包未要求**）。

問題：batch01 之 lint `I-sibling=0`，**其範圍只到本簿之 4 列**。
而 §七-6 所問（`184` 與 `175` 是否不可區辨）之二列**分屬二本**
（`175` 在 `sandbox/pilot03`、`184` 在 `sandbox/batch01`），
**sibling 檢查在任一本內都比不到它們** —— 該 0 對本問題無發言權。

本探針把 pilot 5 列與 batch 1 之 4 列寫進同一本（共 9 列）再跑 lint，
使 sibling 檢查首次能跨批比對。

**本簿為探針，不是交付本、不是受檢物** —— 落 `sandbox/probe_sibling9/`。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402
from gen_pilot import TCS as PILOT_TCS, TEST_GROUP, TEST_SET, AUTHOR       # noqa: E402
from gen_batch01 import TCS as BATCH_TCS                                   # noqa: E402

OUT = FEAT / "sandbox" / "probe_sibling9" / MASTER


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, t in enumerate(list(PILOT_TCS) + list(BATCH_TCS), 1):
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TEST_SET,
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + n, vals)
        rows.append((HEADER_ROW + n, tcid, t["req"]))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("## 併簿探針 —— pilot 5 列 + batch 1 之 4 列 = 9 列\n")
    print("| 列 | TC ID | 037 列 |")
    print("|---|---|---|")
    for r, tid, req in rows:
        print(f"| {r} | `{tid}` | `{req}` |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
