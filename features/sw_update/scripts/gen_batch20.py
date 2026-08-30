#!/usr/bin/env python3
"""T80f —— batch 20：`HU FOTA via TBM` 餘 14 列（下放包 68 §四）。

**本批使 `HU FOTA via TBM` 收尾；其後未起草者僅 `Bearer Selection` 16 ＋ `057` 1。**

**⚠ 本批發現一個門檻衝突**：`246` 之 `$IBS_SOC$` **less than 65 percent** 即阻擋安裝，
**而 `145`（batch 17）為 `$IBS_SOC$ < [80]` 即阻擋安裝** ——
**二列皆為「安裝前之 SOC 門檻」，其值不同（65 vs 80）。** 見上繳包 68 §4.1。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch20"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 287
TS = "HU FOTA via TBM"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
DL = "A deployment package has been downloaded on the head unit"
DL2 = "The downloaded deployment package is ready for installation"
TBM = "A TBM firmware update is staged on the OTA Server for this vehicle"
REC = "Record the head unit screen content as continuous video capture until the check in the final step is completed"
ERREC = "The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, spec, prio, note, item, paren, what, extra=()):
    return tc(req, spec, FN, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server and let the flow run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The update flow runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


TCS = [
 internal("SWE1-FOTA-237", "CFTS057-4907900", "P2",
  "**第二型**；同 `229`／`232` 之族（`SGW_FOTA_HMI_ETM.4215` 之 Ethernet 訊息）",
  "The ROV Update Service shall receive installation progress status information from SGW_FOTA_HMI_ETM.4215 through CarProperty Manager.",
  "Installation progress arrives on the SGW Ethernet message",
  "the installation progress information carried on the Ethernet message SGW_FOTA_HMI_ETM.4215"),

 internal("SWE1-FOTA-238", "CFTS057-4907891", "P2",
  "**值來自他 ECU 之子形態**（同 `225`–`230`）：`$FOTA_Cancellation_Reason$` 之設定手段未確立",
  "The ROV Update Service shall receive $FOTA_Cancellation_Reason$ through CarProperty Manager.",
  "Cancellation reason is received on the vehicle property interface",
  "the cancellation reason value the ROV Update Service received",
  ("PENDING: DR-SU2 means of making the FOTA Master report a cancellation reason",)),

 tc("SWE1-FOTA-239", "CFTS057-4907882", FN, "P1", "中",
  "**可寫**：接受動作與其後之更新啟動皆在畫面；其 `TELEM…` 之設值為殘餘（R-SU37 v2）",
  "The TBM FOTA HMI shall detect when the user selects the 'Accept' option for the FOTA update notification.",
  "Accepting the TBM notification starts the update",
  [B, WIFI, TBM, "The TBM FOTA update notification is displayed on the head unit"],
  [f"1. {REC}",
   "2. Select the 'Accept' option on the TBM FOTA update notification",
   "3. Check that the head unit shows the telematics box module update starting after the accept action"],
  [f"1. {ERREC}",
   "2. The 'Accept' option is selected on the TBM FOTA update notification",
   "3. The recorded screen content shows the telematics box module update starting after the accept action"]),

 tc("SWE1-FOTA-240", "CFTS057-4907883", FN, "P2", "低",
  "**值未載**：`configured response handling period` 之值 037 未給（同 `329` 之重試次數）",
  "When no user action is detected within the configured response handling period, the TBM FOTA AppService shall set TELEMATIC_FD_10.HU_Install_Acceptance = [Nothing to Report] through TBM FW Service.",
  "Notification counts as unacknowledged after the configured period",
  [B, WIFI, TBM, "The TBM FOTA update notification is displayed on the head unit",
   "PENDING: DR-SU2 value of the configured response handling period"],
  ["1. Leave the TBM FOTA update notification untouched",
   "2. PENDING: DR-SU2 step to wait for the configured response handling period and read the notification state"],
  ["1. The TBM FOTA update notification is left untouched",
   "2. PENDING: DR-SU2 observable evidence that the notification is treated as not acknowledged"]),

 internal("SWE1-FOTA-241", "CFTS057-4907806", "P2",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.266）：三個 Boolean 旗標於車機無表徵",
  "The TBM Update Service shall maintain FOTA_TBM_Notification, FOTA_TBM_Forced, and FOTA_TBM_Silent as Boolean status indicators for TBM update processing.",
  "Three Boolean indicators are maintained for TBM processing",
  "the values of FOTA_TBM_Notification, FOTA_TBM_Forced and FOTA_TBM_Silent"),

 tc("SWE1-FOTA-242", "CFTS057-4907787", FN, "P1", "低",
  "⚠ 錨為機制 3 攔下之首選（0.238）；**其旗標之設定手段未確立**（同 `241`），而其畫面後果可觀測",
  "When FOTA_TBM_Notification = True and valid Body ON conditions are detected through $OperationalModeSts$ evaluation using CarProperty Manager, the TBM Update Service shall trigger the TBM FOTA HMI to visualize the update popup through FOTA_Visual_Instructions.Info.",
  "Notification appears when its flag is set and the vehicle is in Body ON",
  [B, WIFI, TBM,
   "PENDING: DR-SU2 means of setting the FOTA_TBM_Notification indicator"],
  ["1. PENDING: DR-SU2 step to set the FOTA_TBM_Notification indicator while the vehicle is in Body ON mode",
   f"2. {REC}",
   "3. PENDING: DR-SU2 check that the head unit displays the TBM update notification in that state"],
  ["1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Notification indicator is set",
   f"2. {ERREC}",
   "3. PENDING: DR-SU2 observable evidence of the TBM update notification"]),

 tc("SWE1-FOTA-243", "CFTS057-4907788", FN, "P2", "低",
  "同 `242` 之型，其旗標為 `FOTA_TBM_Forced`；**二列之差僅在旗標名稱與所顯示之畫面**",
  "When FOTA_TBM_Forced = True and valid Body ON conditions are detected through $OperationalModeSts$ evaluation using CarProperty Manager, the TBM Update Service shall trigger the TBM FOTA HMI to visualize the Forced Update popup through FOTA_Visual_Instructions.Info",
  "Forced screen appears when the forced flag is set in Body ON",
  [B, WIFI, TBM,
   "PENDING: DR-SU2 means of setting the FOTA_TBM_Forced indicator"],
  ["1. PENDING: DR-SU2 step to set the FOTA_TBM_Forced indicator while the vehicle is in Body ON mode",
   f"2. {REC}",
   "3. PENDING: DR-SU2 check that the head unit displays the forced TBM update screen in that state"],
  ["1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Forced indicator is set",
   f"2. {ERREC}",
   "3. PENDING: DR-SU2 observable evidence of the forced TBM update screen"]),

 tc("SWE1-FOTA-244", "CFTS057-4907907", FN, "P3", "低",
  "**DR-SU6**：`in accordance with the defined HMI logic and flow specifications` 為**合規命題** —— 一次執行不能證實其全部",
  "The SW Update HMI shall implement the FOTA user interface in accordance with the defined HMI logic and flow specifications.",
  "FOTA user interface follows the HMI logic and flow specification",
  [B, WIFI, PKG,
   "PENDING: DR-SU6 criterion by which conformance to the HMI logic and flow specification is judged in one bench run"],
  ["1. Trigger an update availability check to the OTA Server and let the flow run to completion",
   "2. PENDING: DR-SU6 step to establish that the user interface followed the HMI logic and flow specification"],
  ["1. The update flow runs to completion on the head unit",
   "2. PENDING: DR-SU6 observable evidence of conformance to the HMI logic and flow specification"]),

 tc("SWE1-FOTA-245", "CFTS057-4907659", FN, "P2", "低",
  "**統攝列**：其所列之各階段畫面（session 起始／下載中／下載成功／安裝中／完成）分屬各 HMI 列，入 DR-SU3",
  "The SW Update HMI shall render phase-specific UI states based on session lifecycle events received from the WiFi Update Service, including session initiation, download in progress, download success, and download failure.",
  "Each session phase has its own UI state",
  [B, WIFI, PKG,
   "PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the individual phase rows"],
  ["1. Trigger an update availability check to the OTA Server and let the flow run to completion",
   "2. PENDING: DR-SU3 step to verify this requirement separately from the individual phase rows"],
  ["1. The update flow runs to completion on the head unit",
   "2. PENDING: DR-SU3 observable evidence separating this requirement from the individual phase rows"]),

 tc("SWE1-FOTA-246", "CFTS057-4907398", NEG, "P1", "中",
  "**門檻列**＋**105 列**；⚠ **其 65% 與 `145`（batch 17）之 `< [80]` 衝突** —— 二列皆為安裝前之 SOC 門檻，列待裁",
  "The WiFi Update Service shall read $IBS_SOC$ through CarProperty Manager before installation start and shall block installation when $IBS_SOC$ is less than 65 percent.",
  "Installation is blocked below 65 percent state of charge",
  [B, WIFI, DL, DL2, "The battery state of charge reported on $IBS_SOC$ is set to 60%"],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off so that the installation preconditions are evaluated",
   "3. Check that no installation starts while the battery state of charge reported on $IBS_SOC$ is 60%"],
  [f"1. {ERREC}",
   "2. The vehicle ignition is switched off and the installation preconditions are evaluated",
   "3. The recorded screen content shows no installation starting while the battery state of charge is 60%"]),

 tc("SWE1-FOTA-247", "CFTS057-4907565", FN, "P1", "低",
  "**第四型**：NIA 之推送（MQTT 或 SMS）不可得；同 `323`／`272` 之族",
  "The SWMC shall detect a valid New Installation Announcement (NIA) received from the OTA server through MQTT or SMS transport and shall automatically trigger a server-initiated OTA update session through the WiFi Update Service without requiring user interaction.",
  "A server NIA starts a session by itself",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of sending a New Installation Announcement to this head unit over MQTT or SMS"],
  ["1. PENDING: DR-SU2 step to send a New Installation Announcement to this head unit",
   "2. PENDING: DR-SU2 check that an OTA update session started without any action on the head unit"],
  ["1. PENDING: DR-SU2 observable evidence that a New Installation Announcement reached this head unit",
   "2. PENDING: DR-SU2 observable evidence that a session started without any action on the head unit"]),

 internal("SWE1-FOTA-248", "CFTS057-4907567", "P2",
  "**第二型**；**與 `363`／`365`（Telematics Client）同族** —— 皆為 TC client 之介面維持與轉送",
  "The WiFi Update Service shall maintain a communication interface with the TC client and shall receive server-initiated update session trigger notifications forwarded from the OTA server through the TC communication channel, then notify the to start server initiated session.",
  "Session triggers arrive through the TC client interface",
  "the session trigger notifications received through the TC client interface",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-363 and 365",)),

 tc("SWE1-FOTA-249", "CFTS057-4907515", NEG, "P1", "低",
  "**第四型**＋**105 列**；**與 `171`／`297` 同族** —— 使完整性驗證失敗之套件不可佈置",
  "The WiFi Update Service shall invoke the SWDL Secure Library immediately before installation start to validate the integrity of the downloaded deployment package and shall block installation when package verification fails.",
  "Installation is blocked when the package fails its integrity check",
  [B, WIFI, DL, DL2,
   "PENDING: DR-SU2 means of staging a deployment package whose integrity validation fails"],
  ["1. PENDING: DR-SU2 step to stage a deployment package whose integrity validation fails",
   "2. Switch the vehicle ignition off so that the installation would start",
   "3. PENDING: DR-SU2 check that no installation started for the package that fails its integrity check"],
  ["1. PENDING: DR-SU2 observable evidence that the staged package fails its integrity validation",
   "2. The vehicle ignition is switched off",
   "3. PENDING: DR-SU2 observable evidence that no installation started"]),

 tc("SWE1-FOTA-250", "CFTS057-4907368", FN, "P2", "低",
  "**第四型**：VIN 變更／proxy 組態更新／手動診斷 reflash／元件更換之事件皆不可於台架產生",
  "The WiFi Update Service shall receive ECU configuration change events, including VIN change, proxy configuration update, manual diagnostic reflash detection, or component replacement notifications through the vehicle event interface.",
  "Configuration change events reach the update service",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of producing an ECU configuration change event such as a VIN change or a component replacement"],
  ["1. PENDING: DR-SU2 step to produce an ECU configuration change event",
   "2. PENDING: DR-SU2 step to read whether the WiFi Update Service received the event"],
  ["1. PENDING: DR-SU2 observable evidence that an ECU configuration change event occurred",
   "2. PENDING: DR-SU2 observable evidence that the event reached the WiFi Update Service"]),
]

LOW_REASONS = {
 "SWE1-FOTA-237": [("Ethernet 訊息需注入與側錄", True)],
 "SWE1-FOTA-238": [("值來自他 ECU，設定手段未確立", True)],
 "SWE1-FOTA-240": [("回應期間之值未載", True)],
 "SWE1-FOTA-241": [("Boolean 旗標無外部表徵", True), ("錨為機制 3 之首選（0.266）", "anchor")],
 "SWE1-FOTA-242": [("旗標之設定手段未確立", True), ("錨為機制 3 之首選（0.238）", "anchor")],
 "SWE1-FOTA-243": [("同 `242`", True)],
 "SWE1-FOTA-244": [("合規命題不可由單次執行證實（DR-SU6）", True)],
 "SWE1-FOTA-245": [("統攝，其各階段畫面分屬他列", True)],
 "SWE1-FOTA-247": [("NIA 之推送不可得", True)],
 "SWE1-FOTA-248": [("介面維持無外部面", True), ("與 `363`／`365` 同族", True)],
 "SWE1-FOTA-249": [("完整性驗證失敗之套件不可佈置", True)],
 "SWE1-FOTA-250": [("組態變更事件不可產生", True)],
}


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T80f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T80f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T80f —— batch 20 之產出（`HU FOTA via TBM` 餘 14，本組收尾）\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        pre = [f"{k}. {s}" for k, s in enumerate(t["pre"], 1)]
        t["pre"] = pre
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TS,
                "I": "\n".join(t["item"]), "J": "\n".join(pre),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in pre + t["proc"] + t["er"])
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["conf"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 | 自信度 | PENDING |")
    print("|---|---|---|:--:|---:|")
    for r, tid, req, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | **{cf}** | {pd} |")
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {sum(1 for r in rows if r[4]==0)}**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
