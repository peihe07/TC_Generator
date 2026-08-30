#!/usr/bin/env python3
"""T84a —— batch 23：`116` 之二個未覆蓋 facet（CG-1／CG-2，下放包 72 §三 #2）。

**037 `116` 之三個使用者動作可獨立觸發**：`Update Later`／**忽略**／**關閉** ——
batch 10 之 `SU-141` 只取了 `Update Later`，其餘二支登記於 `COVERAGE_GAPS.md`。
**本批補之，`D-11` 隨之結清。**

**⚠ 三列之 Final Step 各自帶入其觸發動作**（B-24：三支之後果相同，其別全在觸發）。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch23"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 318
TS = "TBM Reflash"
FN = "功能測試 (Functional based ; no specific technique)"

ITEM = ("The TBM FOTA HMI shall capture user interaction when the user selects "
        "“Update Later,” ignores, or closes the update pop-up.")
PRE = ["The vehicle is in Body ON mode",
       "The telematics box module is fitted to the vehicle",
       "The telematics box module is reported as present",
       "A TBM firmware update is staged on the OTA Server for this vehicle",
       "The TBM FOTA update available pop-up is displayed on the head unit"]
REC = ("2. Record the head unit screen content as continuous video capture until "
       "the check in the final step is completed")
ERREC = ("2. The head unit screen content until the check in the final step is completed "
         "is recorded as continuous video capture")

TCS = [
 dict(req="SWE1-FOTA-116", ts=TS, spec="CFTS057-4907786", dm=FN, prio="P2", conf="中",
      note="**CG-1**：`116` 之「**忽略**」支 —— 其觸發為**不作任何操作**，其判定核心為「彈窗自行關閉且更新未啟動」。",
      item=[ITEM, "(Ignoring the pop-up leaves the update unstarted)"],
      pre=PRE,
      proc=["1. Leave the TBM FOTA update available pop-up without selecting any option",
            REC,
            "3. Check that the head unit shows no telematics box module update starting "
            "after the pop-up closes without any user input"],
      er=["1. The TBM FOTA update available pop-up is left without any option being selected",
          ERREC,
          "3. The recorded screen content shows no telematics box module update starting "
          "after the pop-up closes without any user input"]),

 dict(req="SWE1-FOTA-116", ts=TS, spec="CFTS057-4907786", dm=FN, prio="P2", conf="中",
      note="**CG-2**：`116` 之「**關閉**」支 —— 其觸發為**主動關閉彈窗**。**三支之別全在觸發動作**。",
      item=[ITEM, "(Closing the pop-up leaves the update unstarted)"],
      pre=PRE,
      proc=["1. Close the TBM FOTA update available pop-up with its close control",
            REC,
            "3. Check that the head unit shows no telematics box module update starting "
            "after the pop-up is closed with its close control"],
      er=["1. The TBM FOTA update available pop-up is closed with its close control",
          ERREC,
          "3. The recorded screen content shows no telematics box module update starting "
          "after the pop-up is closed with its close control"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T84a: design_method out of list")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T84a: test_item not verbatim: {bad}")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T84a - batch 23 (116 facets, closes D-11)\n")
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        pre = [f"{k}. {s}" for k, s in enumerate(t["pre"], 1)]
        t["pre"] = pre
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": t["ts"],
                "I": "\n".join(t["item"]), "J": "\n".join(pre),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        print(f"- {tcid} <- {t['req']}  {t['item'][1]}")

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
