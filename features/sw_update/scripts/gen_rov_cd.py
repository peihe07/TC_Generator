#!/usr/bin/env python3
"""T59b —— ROV-C ＋ ROV-D（下放包 45 §三、46 §二§三）：七列，**執行層自行起草**。

**本批為新分工（下放包 45）之首次自行起草** —— 依既有 38 個 TC 之模式，
不待逐列下放。**(a)–(d) 四類事項列為待裁清單，見上繳包 40。**

**ROV-C**：`089`／`098`／`107`／`108`／`109`（可直接觸發）
**ROV-D**：`088`／`095`（須一次真實更新成功；其彈窗已在案）

**屬性之可觀測性逐個判**（下放包 46 §二 #3，**不按批次一律排除**）：

| 屬性 | 判 | 於本批之用法 |
|---|---|---|
| `$Speedometer$`（`089`） | **可觀測**（儀表板即其顯示） | ER 以車速表所示表述 |
| `$OperationalModeSts$`（`088`） | **可觀測**（Body ON／OFF 為車輛模式） | pre／proc 以模式表述 |
| `$Cellsignal$`／`$LTE_Status$`（`108`） | 可觀測（**以狀態列之表徵**） | ER 以狀態列所示之無訊號表述 |
| `$HU_Scheduled_Install$`（`107`） | 可觀測（**以排程畫面所示之時間**） | **不得寫任何秒數或誤差**（§8.4.1） |
| `$FOTA_Status$`（`109`／`088`／`095`） | **不可觀測** | ER 改以其對應之彈窗／畫面表述 |
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "rov_cd"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "ROV Installation"
AUTHOR = "PeiPYHsu"
START_N = 39

FN = "功能測試 (Functional based ; no specific technique)"
ST = "狀態轉換 (State Transition Testing)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
BODY = "2. The vehicle is in Body ON mode"

TCS = [
 # ── ROV-C ──────────────────────────────────────────────────────────
 # `089` —— 鎖定行為本身屬 CFTS022 `4915105`（外部規格，IN §8.4.2 不涵蓋）；
 #          本列所擁有者為「車速 > 0 時判定為行進中並通知 HMI」。
 dict(req="SWE1-FOTA-089", spec="CFTS057-4907907", dm=ST, prio="P1",
  item=["The ROV Update Service shall retrieve the $Speedometer$ vehicle property using CarPropertyManager. If the Speedometer value is greater than zero, the ROV Update Service shall determine that the vehicle is in motion and enforce the vehicle speed lockout behavior.",
        "(ROV update flow does not proceed while the vehicle is in motion)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       '4. The "ROV Forced Update Available A" pop-up is displayed on the head unit',
       "5. The vehicle speed shown on the instrument cluster is zero"],
  proc=["1. Move the vehicle so that the speed shown on the instrument cluster is greater than zero",
        '2. Select "Update Now" on the "ROV Forced Update Available A" pop-up',
        "3. Check that the head unit does not start the installation while the speed shown on the instrument cluster is greater than zero"],
  er=["1. The speed shown on the instrument cluster is greater than zero",
      '2. The "Update Now" selection is made on the head unit',
      "3. The head unit does not start the installation while the speed shown on the instrument cluster is greater than zero"]),
 # `098`
 dict(req="SWE1-FOTA-098", spec="CFTS057-4907881", dm=ST, prio="P2",
  item=["If the vehicle power mode indicates transition to Standby or Sleep mode, the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall dismiss any active FOTA-related pop-up.",
        "(Active FOTA pop-up dismissed when the head unit enters Standby)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       '4. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=["1. Record the head unit screen content as continuous video capture from the moment the pop-up is displayed",
        "2. Set the vehicle to Body OFF mode so that the head unit enters Standby mode",
        "3. Set the vehicle to Body ON mode",
        "4. Check that the recorded screen content shows the pop-up dismissed when the head unit entered Standby mode"],
  er=["1. The head unit screen content from the moment the pop-up is displayed is recorded as continuous video capture",
      "2. The head unit enters Standby mode",
      "3. The head unit returns from Standby mode",
      "4. The recorded screen content shows the pop-up dismissed when the head unit entered Standby mode"]),
 # `107` —— 其外部表徵為排程畫面所示之剩餘時間；**不得寫任何秒數或誤差**
 dict(req="SWE1-FOTA-107", spec="CFTS057-4907894", dm=FN, prio="P2",
  item=["The ROV Update Service shall calculate the time difference between the scheduled installation time and the current system time. The ROV Update Service shall set $HU_Scheduled_Install$ with the calculated remaining time value using CarPropertyManager.",
        "(Remaining time shown matches the interval to the scheduled installation time)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       "4. The Schedule Update screen is displayed on the head unit"],
  proc=["1. Schedule the installation for a time later on the same day and record the selected time as Time_scheduled",
        "2. Read the remaining time shown on the schedule screen and record it as Time_remaining, and record the current time as Time_now",
        "3. Check that Time_remaining equals the difference between Time_scheduled and Time_now, compared at the time unit shown on the screen"],
  er=["1. The installation is scheduled and Time_scheduled is recorded",
      "2. Time_remaining and Time_now are recorded",
      "3. Time_remaining equals the difference between Time_scheduled and Time_now, compared at the time unit shown on the screen"]),
 # `108` —— **不拆**，其理由見上繳包 40 之待裁 (a)
 dict(req="SWE1-FOTA-108", spec="CFTS057-4907895", dm=NEG, prio="P1",
  item=['If ROV Update Service receives $LTE_Status$ <> [3G OR 4G OR H_Plus] OR $Cellsignal$ = [0 OR 1 OR SNA], the ROV Update HMI shall display the "No Connectivity" pop-up and prevent update initiation.',
        "(No Connectivity pop-up shown and installation withheld when there is no usable connectivity)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       '4. The "ROV Forced Update Available B" pop-up is displayed on the head unit',
       "5. The head unit status bar shows no cellular signal"],
  proc=['1. Select "Update Now" on the "ROV Forced Update Available B" pop-up',
        '2. Check that the head unit displays the "No Connectivity" pop-up',
        "3. Check that the head unit does not start the installation while the status bar shows no cellular signal"],
  er=['1. The "Update Now" selection is made on the head unit',
      '2. The head unit displays the "No Connectivity" pop-up',
      "3. The head unit does not start the installation while the status bar shows no cellular signal"]),
 # `109` —— **不拆**：多分支只在 s3，而 s3 已委派 `092`–`095`（下放包 46 §三）
 dict(req="SWE1-FOTA-109", spec="CFTS057-4907896", dm=ST, prio="P1",
  item=["During the pre-installation flow, if $FOTA_Status$ <> [Waiting for HMI Acceptance], the ROV Update Service shall interrupt the current pre-installation flow and shall notify the ROV FOTA HMI.",
        "(Pre-installation flow interrupted when the update status changes)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       '4. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=["1. Record the head unit screen content as continuous video capture from the moment the pop-up is displayed",
        "2. Trigger the update to start installing from the OTA Server while the pop-up is still displayed",
        "3. Check that the recorded screen content shows the pop-up replaced by another SW Update screen"],
  er=["1. The head unit screen content from the moment the pop-up is displayed is recorded as continuous video capture",
      "2. The update starts installing while the pop-up is still displayed",
      "3. The recorded screen content shows the pop-up replaced by another SW Update screen"]),
 # ── ROV-D（須一次真實更新成功）─────────────────────────────────────
 dict(req="SWE1-FOTA-088", spec="CFTS057-4907906", dm=ST, prio="P1",
  item=["If FOTA_Status indicates successful FOTA update ( $FOTA_Status$ = [Successful FOTA Update]) completion and OperationalModeSts indicates Body ON mode, the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the PU0303 success pop-up.",
        "(PU0303 success pop-up shown at Body ON after a successful update)"],
  pre=[WIFI, BODY,
       "3. An update package is staged on the OTA Server for this head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an ROV update and accept it on the head unit",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after differs from Version_initial and that the head unit displays the PU0303 success pop-up"],
  er=["1. Version_initial is recorded",
      "2. The ROV update is accepted and the installation completes",
      "3. Version_after is recorded",
      "4. Version_after differs from Version_initial; the head unit displays the PU0303 success pop-up"]),
 dict(req="SWE1-FOTA-095", spec="CFTS057-4907904", dm=FN, prio="P1",
  item=["If FOTA_Status indicates Successful FOTA Update($FOTA_Status$ = [Successful FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the software update completion pop-up PU0416.",
        "(PU0416 completion pop-up shown when the update completes)"],
  pre=[WIFI, BODY,
       "3. An update package is staged on the OTA Server for this head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an ROV update and accept it on the head unit",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after differs from Version_initial and that the head unit displays the PU0416 software update completion pop-up"],
  er=["1. Version_initial is recorded",
      "2. The ROV update is accepted and the installation completes",
      "3. Version_after is recorded",
      "4. Version_after differs from Version_initial; the head unit displays the PU0416 software update completion pop-up"]),
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
        sys.exit(f"T59b：`design_method` 有清單外之值 {bad} —— 停（R-SU40(a)）")

    # 上半逐字自檢（R-S4）—— 不符即停，不吐半份簿
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad_item = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad_item:
        sys.exit(f"T59b：`test_item` 上半非逐字：{bad_item} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T59b —— ROV-C ＋ ROV-D 之產出（**執行層自行起草**）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜輸出 `sandbox/{TAG}/`")
    print("- **產出前二道停止條件**：`design_method` 對母本清單；"
          "`test_item` 上半對 037 全文逐字 —— 任一不符即 `sys.exit`\n")
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

    print("| 列 | TC ID | 037 列 | spec_reference | P | PENDING |")
    print("|---|---|---|---|---|---:|")
    for r, tid, req, sp, pr, pd in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` | {pr} | {pd} |")
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**"
          f"｜涵蓋 037 列 **{len({r[2] for r in rows})}**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
