#!/usr/bin/env python3
"""T55b —— ROV-A（下放包 42 §三）：`ROV Installation` 首四列。

`090`／`092`（可寫）＋ `093`／`094`（**第四型，觸發手段不可得**）。

**選定依據（三軸，下放包 42 §1.1）**：
  可觀測性 佳（105 列 0）／錨定確定性 **無**（GT 0）／觸發可行性 **半**。

**訊號記法依來源逐字**（`$FOTA_Status$ = [值]`）——
本 feature 未綁 DBC，依 R-1 v3(d) 保留來源名稱，不改寫。

**引號**：`test_item` 上半依 037 逐字（彎引號）；
`test_procedure`／`expected_result` 依 IN §11（直引號）。
**二者依據不同條文，其不一致為正確結果**（下放包 42 §1.2）。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "rov_a"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "ROV Installation"
AUTHOR = "PeiPYHsu"
START_N = 28

FN = "功能測試 (Functional based ; no specific technique)"
ST = "狀態轉換 (State Transition Testing)"
FI = "基礎故障注入 (Fault Injection Lite)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
BODY_ON = "3. The vehicle is in Body ON mode"

TCS = [
 dict(req="SWE1-FOTA-090", spec="CFTS057-4907909", dm=ST, prio="P2",
  item=["The ROV FOTA HMI shall display the cached “What’s New” information to the user. The ROV Update Service shall retain the cached data until the next transition to Body ON mode.",
        "(What's New shown at the next Body ON after a successful update)"],
  pre=[WIFI,
       "2. An update package whose deployment package contains What's New details is staged on the OTA Server for this head unit",
       BODY_ON],
  proc=["1. Trigger an ROV update and wait until $FOTA_Status$ = [Successful FOTA Update]",
        "2. Set the vehicle to Body OFF mode",
        "3. Set the vehicle to Body ON mode",
        "4. Check that the head unit displays the What's New details of the deployed package"],
  er=["1. $FOTA_Status$ = [Successful FOTA Update] is reported",
      "2. The vehicle is in Body OFF mode and the head unit screen is off",
      "3. The vehicle is in Body ON mode and the head unit completes start-up",
      "4. The head unit displays the What's New details of the deployed package"]),
 dict(req="SWE1-FOTA-092", spec="CFTS057-4907898", dm=FN, prio="P1",
  item=["If FOTA_Status indicates Installing FOTA Update( $FOTA_Status$ = [Installing FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the installation progress screens corresponding to the active update session.",
        "(Installation screens shown while the update is installing)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       BODY_ON],
  proc=["1. Trigger an ROV update and accept it on the head unit",
        "2. Record the head unit screen content as continuous video capture until the installation ends",
        "3. Check that the recorded screen content shows the installation progress screens while $FOTA_Status$ = [Installing FOTA Update]"],
  er=["1. The ROV update is accepted and the installation starts",
      "2. The head unit screen content until the installation ends is recorded as continuous video capture",
      "3. The recorded screen content shows the installation progress screens for the active update session"]),
 # `093`／`094` —— 第四型（R-SU39）：觀測面（彈窗）明確，缺者為**使更新失敗之手段**
 dict(req="SWE1-FOTA-093", spec="CFTS057-4907901", dm=FI, prio="P1",
  item=["If FOTA_Status indicates FOTA FailureRollback Successful($FOTA_Status$ = [FOTA FailureRollback Successful]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Reverted” pop-up after successful rollback.",
        "(Reverted pop-up shown after a rollback completes)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       BODY_ON,
       "4. PENDING: DR-SU2 means of making an ROV update fail and roll back on the test bench"],
  proc=["1. Trigger an ROV update and accept it on the head unit",
        "2. PENDING: DR-SU2 step to make the update fail so that the rollback completes successfully",
        "3. Check that the head unit displays the \"Reverted\" pop-up"],
  er=["1. The ROV update is accepted and the installation starts",
      "2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA FailureRollback Successful]",
      "3. The head unit displays the \"Reverted\" pop-up"]),
 dict(req="SWE1-FOTA-094", spec="CFTS057-4907902", dm=FI, prio="P1",
  item=["If FOTA_Status indicates FOTA Failure Complete($FOTA_Status$ = [FOTA Failure Complete]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Walk Home Scenario” pop-up.",
        "(Walk Home Scenario pop-up shown after an update failure completes)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       BODY_ON,
       "4. PENDING: DR-SU2 means of making an ROV update fail without a successful rollback on the test bench"],
  proc=["1. Trigger an ROV update and accept it on the head unit",
        "2. PENDING: DR-SU2 step to make the update fail so that the failure completes without rollback",
        "3. Check that the head unit displays the \"Walk Home Scenario\" pop-up"],
  er=["1. The ROV update is accepted and the installation starts",
      "2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA Failure Complete]",
      "3. The head unit displays the \"Walk Home Scenario\" pop-up"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    bad = {t["dm"] for t in TCS} - legal
    if bad:
        sys.exit(f"T55b：`design_method` 有清單外之值 {bad} —— 停（R-SU40(a)）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T55b —— ROV-A 之產出（受檢物，非交付本）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜Test Set：`{TEST_SET}`｜輸出 `sandbox/{TAG}/`\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TEST_SET,
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["spec"], t["prio"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 列 | spec_reference | P | PENDING | 型 |")
    print("|---|---|---|---|---|---:|---|")
    TY = {"SWE1-FOTA-093": "**第四型**（R-SU39）", "SWE1-FOTA-094": "**第四型**（R-SU39）"}
    for r, tid, req, sp, pr, pd in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` | {pr} | {pd} | {TY.get(req,'可寫')} |")
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜可交付 "
          f"**{sum(1 for r in rows if not r[5])}** 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
