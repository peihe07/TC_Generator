#!/usr/bin/env python3
"""T77e —— batch 17：`Deployment Flow` 前 16 列（下放包 65 §五）。

**下窗（17–19）目標 27%。`Bearer Selection` 16 列仍待 DR-SU2(a)**（下放包 51 §二 #6），
**故本批自 `Deployment Flow` 取，依列序前 16 列**（拆組常規）。

**本批之門檻列四**：`145`（`$IBS_SOC$ < [80]`）、`146`（`$IBS_SOC_ACCURACY$ = [0]／[SNA]`）、
`147`（`$PowerMode$ = [IGN_OFF]`）、`150`（**彈窗解除計數 20 次**）。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch17"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 239
TS = "Deployment Flow"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"
DT = "決策表 (Decision Table Testing)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
DL = "A deployment package has been downloaded on the head unit"
DL2 = "The downloaded deployment package is ready for installation"
REC = "Record the head unit screen content as continuous video capture until the check in the final step is completed"
ERREC = "The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, spec, prio, note, item, paren, what, extra=()):
    return tc(req, spec, FN, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server, accept the update and let the flow run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The update flow runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


TCS = [
 internal("SWE1-FOTA-138", "CFTS057-4907605", "P2",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.210）；**「解析 manifest 並分派」之第七次**（`169`／`371`／`209`／`253`／`264`／`265` 之後）",
  "The WiFi Update Service shall extract the component packages and determine the appropriate installation method for each component type.",
  "Component packages are extracted and their target types determined",
  "the component packages extracted from the deployment package and the target type determined for each",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-169, 371, 209, 253, 264 and 265",)),

 internal("SWE1-FOTA-139", "CFTS057-4907606", "P2",
  "**第二型**＋**105 列**：安裝器之狀態回報在服務之間；其外部後果（失敗畫面）屬他列",
  "The Update Engine shall report MCPU installation status information to the WiFi Update Service during the installation process.",
  "MCPU installation status reaches the WiFi Update Service",
  "the MCPU installation status the Update Engine reported during the installation"),

 tc("SWE1-FOTA-140", "CFTS057-4907609", FN, "P1", "中",
  "**可寫**：使用者核可之取得可觀測；其前半（決定何時進入部署）為統攝，記於 REASONING",
  "The WiFi Update Service shall verify that user approval is received through the HMI when user approval is required.",
  "Installation waits for the user's approval when approval is required",
  [B, WIFI, DL, DL2, DL2],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off without giving any approval on the head unit",
   "3. Check that no installation starts while no approval has been given on the head unit"],
  [f"1. {ERREC}",
   "2. The vehicle ignition is switched off with no approval given",
   "3. The recorded screen content shows no installation starting while no approval has been given"]),

 tc("SWE1-FOTA-141", "CFTS057-4907614", FN, "P1", "中",
  "**可寫**：更新訊息文字與安裝通知同時顯示，二者皆在畫面上",
  "The SW Update HMI shall display the update message together with the installation notification and installation action options when HMI interaction is supported.",
  "Update message text appears with the installation notification",
  [B, WIFI, DL, DL2, DL2],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off so that the installation notification is shown",
   "3. Check that the head unit shows the update message text together with the installation notification"],
  [f"1. {ERREC}",
   "2. The installation notification is shown on the head unit",
   "3. The recorded screen content shows the update message text together with the installation notification"]),

 tc("SWE1-FOTA-142", "CFTS057-4907618", FN, "P1", "中",
  "**可寫**（否定式）：背景下載期間畫面無進度呈現，可由連續錄影驗；**與 `036` 之靜默不同**（本列限於下載階段）",
  "The WiFi Update Service shall not trigger SW Update HMI to present customer-facing progress of deployment package download process.",
  "No download progress is shown to the customer during a background download",
  [B, WIFI, PKG],
  ["1. Record the head unit screen content as continuous video capture from the update availability check until the deployment package download completes",
   "2. Trigger an update availability check to the OTA Server and leave the head unit untouched",
   "3. Check that the recorded screen content contains no customer-facing progress of the deployment package download"],
  ["1. The head unit screen content from the update availability check until the download completes is recorded as continuous video capture",
   "2. The deployment package download completes without the head unit being touched",
   "3. The recorded screen content contains no customer-facing progress of the deployment package download"]),

 tc("SWE1-FOTA-143", "CFTS057-4907619", BV, "P1", "中",
  "**門檻列**（`a maximum period of 30 minutes after key-off` 逐字取自 037）＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.264）。⚠ **其 30 分鐘與 `057` 之 30 分鐘不同**：本列自 key-off 起算，`057` 自 session 起算",
  "When an active deployment package download session,$PowerMode$ transitions to IGN_OFF state, the WiFi Update Service shall request extended wake mode to continue the package download for a maximum period of 30 minutes after key-off.",
  "Download continues for at most 30 minutes after key-off",
  [B, WIFI, PKG,
   "The deployment package is large enough that its download cannot finish within 30 minutes"],
  ["1. Trigger an update availability check to the OTA Server so that the deployment package download starts",
   "2. Record the head unit download progress as continuous video capture until the check in the final step is completed",
   "3. Switch the vehicle ignition off while the download is running and record the time as Time_keyoff",
   "4. Read from the recording the time at which the download progress stops advancing and record it as Time_stop",
   "5. Check that Time_stop is not later than 30 minutes after Time_keyoff"],
  ["1. The deployment package download starts",
   "2. The head unit download progress until the check in the final step is completed is recorded as continuous video capture",
   "3. Time_keyoff is recorded",
   "4. Time_stop is recorded",
   "5. Time_stop is not later than 30 minutes after Time_keyoff"]),

 tc("SWE1-FOTA-144", "CFTS057-4907619", FN, "P1", "低",
  "**DR-SU6**：`shall not impact other systems, screens or vehicle functions` 為全稱否定，**無判準**（同 `283`／`284`）",
  "The WiFi Update Service ensure that the deployment package download process shall not impact other systems, screens or indicators in the vehicle.",
  "Other systems are unaffected while the download continues after key-off",
  [B, WIFI, PKG,
   "PENDING: DR-SU6 criterion by which `not impact other systems, screens, or vehicle functions` is judged in one bench run"],
  ["1. Trigger an update availability check to the OTA Server and switch the vehicle ignition off while the download is running",
   "2. PENDING: DR-SU6 step to establish that the download did not impact other systems, screens or vehicle functions"],
  ["1. The download continues after the ignition is switched off",
   "2. PENDING: DR-SU6 observable evidence that no other system, screen or vehicle function was impacted"]),

 tc("SWE1-FOTA-145", "CFTS057-4907623", BV, "P1", "中",
  "**門檻列**（`$IBS_SOC$ < [80]` 逐字）；其值與 `069` 之 `> [65]` 不同 —— **二列之門檻分屬下載與安裝**。⚠ 037 原文有斷字缺陷（`the WiFi Update Servic/USB Update Service e`）—— **逐字保留，登 D-8**",
  "If $IBS_SOC$ < [80], the WiFi Update Servic/USB Update Service e shall not allow installation and maintain the deployment in deferred state until the battery state of charge is restored to the configured threshold or higher.",
  "Installation does not start while the battery state of charge is below 80%",
  [B, WIFI, DL, DL2, "The battery state of charge reported on $IBS_SOC$ is set to 70%"],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off so that the installation preconditions are evaluated",
   "3. Check that no installation starts while the battery state of charge reported on $IBS_SOC$ is 70%"],
  [f"1. {ERREC}",
   "2. The vehicle ignition is switched off and the installation preconditions are evaluated",
   "3. The recorded screen content shows no installation starting while the battery state of charge is 70%"]),

 tc("SWE1-FOTA-146", "CFTS057-4907626", DT, "P1", "中",
  "**門檻列**＋**105 列**：`$IBS_SOC_ACCURACY$ = [0] or [SNA]` 為二值之析取，逐字取自 037",
  "If $IBS_SOC_ACCURACY$ = [0] or IBS_SOC_ACCURACY$ = [SNA], the WiFi Update Service shall treat battery state of charge data as invalid and shall block installation initiation until a valid accuracy level is available.",
  "Installation does not start while the state-of-charge accuracy is invalid",
  [B, WIFI, DL, DL2, "The value reported on $IBS_SOC_ACCURACY$ is set to 0"],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off so that the installation preconditions are evaluated",
   "3. Check that no installation starts while the value reported on $IBS_SOC_ACCURACY$ is 0"],
  [f"1. {ERREC}",
   "2. The vehicle ignition is switched off and the installation preconditions are evaluated",
   "3. The recorded screen content shows no installation starting while the value reported on $IBS_SOC_ACCURACY$ is 0"]),

 tc("SWE1-FOTA-147", "CFTS057-4907807", NEG, "P1", "中",
  "**門檻列**＋**105 列**：`only when $PowerMode$ = [IGN_OFF]` —— 取其否定面（IGN_RUN 時不啟動）",
  "The WiFi Update Service/USB Update Service shall permit installation start only when $PowerMode$ = [IGN_OFF].",
  "Installation does not start while the vehicle is running",
  [B, WIFI, DL, DL2, "The vehicle ignition is on so that $PowerMode$ is not IGN_OFF"],
  [f"1. {REC}",
   "2. Accept the installation on the head unit while the vehicle ignition is on",
   "3. Check that no installation starts while the vehicle ignition is on"],
  [f"1. {ERREC}",
   "2. The installation is accepted while the vehicle ignition is on",
   "3. The recorded screen content shows no installation starting while the vehicle ignition is on"]),

 tc("SWE1-FOTA-148", "CFTS057-4907629", FN, "P1", "中",
  "**可寫**；⚠ **`PU0304` 只出現於 037 之標題欄，其 Description 只寫 `the pop-up`** —— 故 ER 不引該編號（同下放包 43 §二 #2 之處置）",
  "The SW Update HMI shall populate the estimated time for install in the pop-up.",
  "The installation pop-up shows the estimated installation time",
  [B, WIFI, DL, DL2, DL2],
  [f"1. {REC}",
   "2. Switch the vehicle ignition off so that the installation notification popup is shown",
   "3. Check that the installation notification popup shows an estimated installation time"],
  [f"1. {ERREC}",
   "2. The installation notification popup is shown on the head unit",
   "3. The recorded screen content shows the installation notification popup carrying an estimated installation time"]),

 tc("SWE1-FOTA-149", "CFTS057-4907630", FN, "P1", "中",
  "**可寫**：彈窗之關閉可觀測；其觸發（IGN_RUN）可佈置",
  "If the installation has not been accepted or scheduled, and the $PowerMode$ changes to IGN_RUN or the MCPU platform exits power accessory delay mode, the WiFi Update Service shall notify the SW Update HMI to dismiss the installation popup.",
  "Installation popup is dismissed when the vehicle is started",
  [B, WIFI, DL, DL2, "The installation notification popup is displayed",
   "The installation has not been accepted or scheduled"],
  [f"1. {REC}",
   "2. Start the vehicle so that $PowerMode$ changes to IGN_RUN",
   "3. Check that the head unit no longer shows the installation popup after the change to IGN_RUN"],
  [f"1. {ERREC}",
   "2. The vehicle is started and $PowerMode$ changes to IGN_RUN",
   "3. The recorded screen content shows that the installation popup is no longer displayed after the change to IGN_RUN"]),

 tc("SWE1-FOTA-150", "CFTS057-4907631", BV, "P1", "低",
  "**門檻列**（`20 occurrences` 逐字取自 037）；**其觸發須解除彈窗 20 次** —— 可行而昂貴，故掛 `PENDING` 之非其觀測面而係其成本，記於 REASONING",
  "When the dismissal counter reaches 20 occurrences, the SW Update HMI shall display the “Forced Update Available 2” popup.",
  "Forced Update Available 2 appears on the twentieth dismissal",
  [B, WIFI, DL, DL2, "The installation popup dismissal counter of the head unit has been cleared"],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Dismiss the installation popup and repeat the ignition cycle until the popup has been dismissed twenty times",
   "3. Check that the head unit displays the “Forced Update Available 2” popup on the twentieth dismissal"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The installation popup has been dismissed twenty times",
   "3. The recorded screen content shows the “Forced Update Available 2” popup on the twentieth dismissal"]),

 tc("SWE1-FOTA-151", "CFTS057-4907500", NEG, "P1", "低",
  "**可寫之核心**（下載中不得啟動安裝）＋⚠ 錨為機制 3 攔下之首選（0.195）：其前半（SWMC 之通知）為內部，記為殘餘",
  "Upon receiving an active download session indication from SWMC, the WiFi Update Service shall prevent software installation initiation.",
  "Installation cannot start while a download session is running",
  [B, WIFI, PKG],
  ["1. Trigger an update availability check to the OTA Server so that a deployment package download starts",
   f"2. {REC}",
   "3. Switch the vehicle ignition off while the download is still running",
   "4. Check that no installation starts while the download session is still running"],
  ["1. The deployment package download starts",
   f"2. {ERREC}",
   "3. The vehicle ignition is switched off while the download is still running",
   "4. The recorded screen content shows no installation starting while the download session is still running"]),

 tc("SWE1-FOTA-152", "CFTS057-4907633", FN, "P1", "低",
  "⚠ 錨為機制 3 攔下之首選（0.178）；其後半（請求 MCPU 轉入 active 狀態）為內部，掛 `PENDING`；**排程之設定與到時執行可觀測**",
  "When the scheduled installation time is reached, the WiFi Update Service shall request the MCPU platform to transition to an active operational state if the platform is in sleep or low-power mode.",
  "Installation starts at the scheduled time",
  [B, WIFI, DL, DL2,
   "PENDING: DR-SU2 means of observing the transition request the WiFi Update Service made to the MCPU platform"],
  ["1. Schedule the installation on the head unit for a time five minutes ahead",
   f"2. {REC}",
   "3. Wait until the scheduled time is reached",
   "4. Check that the installation starts at the scheduled time"],
  ["1. The installation is scheduled for a time five minutes ahead",
   f"2. {ERREC}",
   "3. The scheduled time is reached",
   "4. The recorded screen content shows the installation starting at the scheduled time"]),

 tc("SWE1-FOTA-153", "CFTS057-4907634", FN, "P1", "中",
  "**可寫**：What's New 之選取與其內容顯示皆在畫面上；**與 `183`（batch 1）之別在時點**（下載後 vs 安裝完成後）",
  "When the user selects the “What’s New” option in the SW Update HMI, the SW Update HMI shall request the WiFi Update Service/USB Update Service to provide the “What’s New” details associated with the downloaded deployment package.",
  "What's New details are shown for the downloaded package",
  [B, WIFI, DL, DL2, DL2],
  [f"1. {REC}",
   "2. Select the “What’s New” option on the head unit",
   "3. Check that the head unit shows the What's New details of the downloaded deployment package"],
  [f"1. {ERREC}",
   "2. The “What’s New” option is selected on the head unit",
   "3. The recorded screen content shows the What's New details of the downloaded deployment package"]),
]

LOW_REASONS = {
 "SWE1-FOTA-138": [("解析與分派無外部面", True), ("與六列重複", True),
                   ("錨為機制 3 之首選（0.210）", "anchor")],
 "SWE1-FOTA-139": [("服務間之狀態回報無外部面", True)],
  "SWE1-FOTA-144": [("`not impact` 無判準（DR-SU6）", True)],
 "SWE1-FOTA-150": [("其觸發須解除彈窗 20 次，成本高而可行", True)],
 "SWE1-FOTA-151": [("SWMC 之通知為殘餘", True), ("錨為機制 3 之首選（0.195）", "anchor")],
 "SWE1-FOTA-152": [("MCPU 狀態轉換之請求無外部面", True), ("錨為機制 3 之首選（0.178）", "anchor")],
}
MECH3 = ["SWE1-FOTA-138", "SWE1-FOTA-143", "SWE1-FOTA-151", "SWE1-FOTA-152"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T77e：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T77e：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T77e —— batch 17 之產出（`Deployment Flow` 前 16 列）\n")
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
    q, a, excl = [], [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        un = [(r, k) for r, k in rs if k is not True]
        (excl if not un else (a if all(k == "anchor" for _, k in un) else q)).append(i)
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {sum(1 for r in rows if r[4]==0)}**")
    print(f"- 品質訊號 **{len(q)}**｜錨定訊號 **{len(a)}**｜可排除 {len(excl)}"
          f"｜抽驗組成 {len(set(q)|set(a)|set(mid)|set(m3))} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
