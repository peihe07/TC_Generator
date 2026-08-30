#!/usr/bin/env python3
"""T82a —— batch 22：`SWE1-FOTA-057` 一列（下放包 70 §3.2）。

**依 Pei 2026-08-30 之出貨裁定（帶 `PENDING` 出貨），`057` 得起草並帶 `PENDING: DR-SU4`** ——
其 30 分鐘之起算點於 037（session 起）與嵌入物件 `4908702`（timed mode 到期起）不一致，
**下放包 54 §二 #1 裁「二者皆為上游文件，我方無權擇一」，故其判定核心掛起。**

**本列使 037 覆蓋達 311／311 = 100%。**
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch22"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 317
TS = "Wi-Fi Download"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"

TCS = [
 dict(req="SWE1-FOTA-057", ts=TS, spec="CFTS057-4907415", dm=BV, prio="P1", conf="低",
      note="**門檻列**＋**105 列**；⚠ **其 30 分鐘之起算點二來源不一致** —— 037 自 session 起算、"
           "嵌入物件 `4908702` 自 timed mode 到期起算（下放包 54 §二 #1：我方無權擇一）。"
           "**依出貨裁定帶 `PENDING: DR-SU4` 交付。**",
      item=["If the Wi-Fi download session duration exceeds 30 minutes during the current ignition cycle, "
            "the WiFi Update Service shall terminate the active FOTA download session and request WifiManager "
            "to transition the M-CPU platform from Client Mode to Host Mode.",
            "(Download session ends after 30 minutes in the ignition cycle)"],
      pre=["The vehicle is in Body ON mode",
           "The head unit is connected to a saved Wi-Fi access point with internet access",
           "An update package large enough that its download cannot finish within 30 minutes is staged on the OTA Server",
           "Timed download mode is active on the head unit",
           "PENDING: DR-SU4 which start point the 30 minutes is counted from: the start of the "
           "download session (037) or the expiry of timed mode (embedded object 4908702)"],
      proc=["1. Record the head unit download progress and the companion device hotspot list as continuous "
            "video capture until the check in the final step is completed",
            "2. Trigger an update availability check to the OTA Server and let the deployment package download start",
            "3. Switch the vehicle ignition off so that the download continues in timed download mode",
            "4. PENDING: DR-SU4 step to record the start point from which the 30 minutes is counted",
            "5. PENDING: DR-SU4 check that the download session ends and the head unit hotspot becomes available "
            "again no later than 30 minutes after that start point"],
      er=["1. The head unit download progress and the companion device hotspot list until the check in the final "
          "step is completed are recorded as continuous video capture",
          "2. The deployment package download starts",
          "3. The vehicle ignition is switched off and the download continues in timed download mode",
          "4. PENDING: DR-SU4 observable evidence of the start point from which the 30 minutes is counted",
          "5. PENDING: DR-SU4 observable evidence that the download session ended and the hotspot became available "
          "again no later than 30 minutes after that start point"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T82a：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T82a：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T82a —— batch 22 之產出（`057`，**037 覆蓋達 100%**）\n")
    rows = []
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
        pend = sum(s.count("PENDING:") for s in pre + t["proc"] + t["er"])
        rows.append((tcid, t["req"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    for tid, req, pd in rows:
        print(f"- `{tid}` ← `{req}`｜`PENDING` {pd} 行")
    return 0


if __name__ == "__main__":
    sys.exit(main())
