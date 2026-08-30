#!/usr/bin/env python3
"""T78f —— batch 18：`Deployment Flow` 餘 10 ＋ `HU FOTA via TBM` 前 6 = 16 列（下放包 66 §五）。

**⚠ 本批之 105 比率 19%（3／16），低於下窗目標 27%** ——
其成因為**可取之組已窮**：`Bearer Selection`（16 列／62%）仍待 DR-SU2(a)（下放包 51 §二 #6），
**扣除之後剩餘各組之 105 比率為 `Deployment Flow` 餘 10 之 30% 與 `HU FOTA via TBM` 之 6%。**
**其算術見上繳包 66 §5.1。**

**⚠ 三列同源**：`157`／`162`／`167` 皆為「安裝失敗狀態經 installer callback 回報」——
**「同一件事之第 N 次」之最大一組（三列同組同批）。**
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch18"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 255
DF, HU = "Deployment Flow", "HU FOTA via TBM"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
FI = "基礎故障注入 (Fault Injection Lite)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
DL = "A deployment package has been downloaded on the head unit"
DL2 = "The downloaded deployment package is ready for installation"
REC = "Record the head unit screen content as continuous video capture until the check in the final step is completed"
ERREC = "The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, ts, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=ts, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, ts, spec, prio, note, item, paren, what, extra=()):
    return tc(req, ts, spec, FN, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server, accept the update and let the flow run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The update flow runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


TCS = [
 internal("SWE1-FOTA-154", DF, "CFTS057-4907635", "P2",
  "**統攝列**：其所列之各信號（`$PowerMode$`／`$IBS_SOC$`／`$IBS_SOC_ACCURACY$`）之個別判定分屬 `145`／`146`／`147`，入 DR-SU3",
  "The WiFi Update Service shall evaluate scheduled installation preconditions before initiating the scheduled installation process.",
  "Scheduled installation checks its preconditions first",
  "the precondition evaluation the service performed before the scheduled installation",
  ("PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1-FOTA-145, 146 and 147",)),

 tc("SWE1-FOTA-155", DF, "CFTS057-4907636", NEG, "P1", "中",
  "**可寫**：排程後使前提不滿足（SOC 降至 70%），其取消可觀測",
  "The SW Update HMI shall display the “Conditions Not Met” pop-up with the cancellation reason text received from the WiFi Update Service",
  "Conditions Not Met pop-up carries a cancellation reason text",
  [B, WIFI, DL, DL2, "The installation is scheduled on the head unit for a time five minutes ahead"],
  [f"1. {REC}",
   "2. Set the battery state of charge reported on $IBS_SOC$ to 70% before the scheduled time is reached",
   "3. Wait until the scheduled time has passed",
   "4. Check that the head unit shows the scheduled update as cancelled and shows no installation running"],
  [f"1. {ERREC}",
   "2. The battery state of charge reported on $IBS_SOC$ is 70%",
   "3. The scheduled time passes",
   "4. The recorded screen content shows the scheduled update as cancelled and shows no installation running"]),

 tc("SWE1-FOTA-156", DF, "CFTS057-4907638", FN, "P1", "中",
  "**可寫**＋⚠ 錨為機制 3 攔下之首選（0.214）：顯示保持點亮，可由連續錄影驗",
  "The WiFi Update Service/USB Update Service shall request the system power management interface using CarPower Manager to keep the radio display in ON state after installation acceptance and throughout the installation-in-progress state.",
  "Display stays on from acceptance until the installation ends",
  [B, WIFI, DL, DL2],
  ["1. Record the head unit display as continuous video capture from the installation acceptance until the installation ends",
   "2. Accept the installation on the head unit and switch the vehicle ignition off",
   "3. Check that the head unit display stays on from the acceptance until the installation ends"],
  ["1. The head unit display from the acceptance until the installation ends is recorded as continuous video capture",
   "2. The installation is accepted and the vehicle ignition is switched off",
   "3. The recorded content shows the head unit display on throughout the installation"]),

 internal("SWE1-FOTA-157", DF, "CFTS057-4907639", "P2",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.229）；**與 `162`／`167` 三列同源** —— 皆為「安裝失敗狀態經 installer callback 回報」，入 DR-SU3",
  "The Update Engine and SW Updater Service shall report installation failure status to the WiFi Update Service//USB Update Service through the installer status callback interface.",
  "Installer failure status reaches the update service",
  "the installation failure status reported through the installer status callback interface",
  ("PENDING: DR-SU2 means of making an installation fail",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-162 and 167")),

 tc("SWE1-FOTA-160", DF, "CFTS057-4907642", FN, "P1", "低",
  "**DR-SU6**：`remains operational` 為能力命題 —— 一次未撥打之更新不證明 eCall 可用；且緊急呼叫不可於台架實撥",
  "The Connectivity Service shall ensure that emergency call (eCall) functionality remains operational with the help of the TBM Update Service during FOTA download and post-installation phases.",
  "eCall stays available across the update",
  [B, WIFI, PKG,
   "PENDING: DR-SU6 criterion by which eCall availability during an update is judged in one bench run",
   "PENDING: DR-SU2 means of exercising eCall on the bench without placing an emergency call"],
  ["1. Trigger an update availability check to the OTA Server and let the download and installation run",
   "2. PENDING: DR-SU6 step to establish that eCall functionality remained operational during and after the update"],
  ["1. The download and installation run on the head unit",
   "2. PENDING: DR-SU6 observable evidence that eCall functionality remained operational"]),

 tc("SWE1-FOTA-161", DF, "CFTS057-4907643", FN, "P1", "中",
  "**可寫**：安裝中之警示彈窗可觀測，其內容（不宜駕駛）為畫面文字",
  "The SW Update HMI shall display a warning pop-up indicating user that the vehicle should not be driven during installation.",
  "Warning not to drive appears while the installation runs",
  [B, WIFI, DL, DL2],
  [f"1. {REC}",
   "2. Accept the installation on the head unit and switch the vehicle ignition off",
   "3. Check that the head unit displays a warning pop-up whose text tells the user not to drive the vehicle during the installation"],
  [f"1. {ERREC}",
   "2. The installation is accepted and the vehicle ignition is switched off",
   "3. The recorded screen content shows a warning pop-up whose text tells the user not to drive the vehicle during the installation"]),

 internal("SWE1-FOTA-162", DF, "CFTS057-4907606", "P3",
  "**與 `157` 逐字同一句起首**（`The Update Engine and SW Updater Service shall report installation failure status…`）——**其差僅在後半之 session 狀態更新**；⚠ 錨為機制 3 攔下之首選（0.210）",
  "The WiFi Update Service shall update the OTA session state when installation failure is detected.",
  "OTA session status is set to failed after an installer failure",
  "the OTA session status the service set after an installation failure",
  ("PENDING: DR-SU2 means of making an installation fail",)),

 tc("SWE1-FOTA-163", DF, "CFTS057-4907645", FI, "P1", "低",
  "**第四型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.211）：安裝進行中使車輛移動，台架不可為",
  "If software installation is already in progress and a vehicle motion condition is detected, the WiFi Update Service shall continue the ongoing installation without interruption until completion and shall not abort or pause the installation process due to vehicle movement.",
  "Installation continues if the vehicle starts moving",
  [B, WIFI, DL, DL2,
   "PENDING: DR-SU2 means of producing a vehicle motion event while an installation is in progress"],
  ["1. Accept the installation on the head unit and let it start",
   "2. PENDING: DR-SU2 step to produce a vehicle motion event while the installation is in progress",
   "3. PENDING: DR-SU2 check that the installation continued without interruption"],
  ["1. The installation starts on the head unit",
   "2. PENDING: DR-SU2 observable evidence of a vehicle motion event during the installation",
   "3. PENDING: DR-SU2 observable evidence that the installation continued without interruption"]),

 tc("SWE1-FOTA-165", DF, "CFTS057-4907648", FN, "P1", "中",
  "**可寫**；⚠ **我首版把本列讀成「成功通知」，其實不是** —— 037 之判定核心為完成後依 `$PowerMode$` 決定續行或入睡",
  "If $PowerMode$ ≠ [IGN_RUN], the WiFi Update Service shall initiate transition of the HU to sleep mode.",
  "Head unit goes to sleep after an installation that ends with the ignition off",
  [B, WIFI, DL, DL2],
  ["1. Accept the installation on the head unit and switch the vehicle ignition off",
   "2. Record the head unit display as continuous video capture until the check in the final step is completed",
   "3. Wait until the installation completes with the vehicle ignition still off",
   "4. Check that the head unit display turns off after the installation completes"],
  ["1. The installation is accepted and the vehicle ignition is switched off",
   "2. The head unit display until the check in the final step is completed is recorded as continuous video capture",
   "3. The installation completes with the vehicle ignition still off",
   "4. The recorded content shows the head unit display turning off after the installation completes"]),

 internal("SWE1-FOTA-167", DF, "CFTS057-4907650", "P3",
  "**與 `157`／`162` 三列同源之第三列**；其差在本列之回報者為 Update Engine **Manager**",
  "The Update Engine Manager and SW Updater Manager shall report installation failure status to the WiFi Update Service/USB Update Service.",
  "Manager-level installer failure status reaches the update service",
  "the installation failure status reported by the Update Engine Manager and SW Updater Manager",
  ("PENDING: DR-SU2 means of making an installation fail",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-157 and 162")),

 internal("SWE1-FOTA-215", HU, "CFTS057-4907281", "P2",
  "**第二型**：`$HUFOTACheck$` 之設值與其經 TBM FW Service 之傳送皆在服務之間",
  "Upon trigger, the TBM Update Service shall set $HUFOTACheck$ = [Check for updates] and transmit the signal to TBM through TBM FW Service.",
  "HUFOTACheck is set and sent to the TBM",
  "the value set on $HUFOTACheck$ and its transmission to the TBM"),

 internal("SWE1-FOTA-216", HU, "CFTS057-4907279", "P2",
  "**伺服器側（DR-SU2(e)）**：TBM 更新之可用性查詢在伺服器與 SWMC 之間",
  "When the OTA server reports an available TBM update, the SWMC shall notify the TBM Update Service.",
  "Available TBM update is passed to the TBM Update Service",
  "the availability response the SWMC received from the OTA Server for the TBM update"),

 tc("SWE1-FOTA-217", HU, "CFTS057-4907258", FN, "P1", "低",
  "**第四型**：須同時佈置二種以上之更新類型（ROV／HU／TBM／Map），其 campaign 之組合不可佈置",
  "The Arbiter Service shall permit execution of only the highest priority update session and shall defer lower priority update sessions until the active higher priority update is completed or cleared.",
  "Priority order decides which update type runs first",
  [B, WIFI,
   "PENDING: DR-SU2 means of staging two or more update types simultaneously for this vehicle",
   "PENDING: DR-SU2 configured priority order between the update types"],
  ["1. PENDING: DR-SU2 step to stage two update types simultaneously",
   "2. PENDING: DR-SU2 check that the update type with the higher configured priority runs first"],
  ["1. PENDING: DR-SU2 observable evidence that two update types are available simultaneously",
   "2. PENDING: DR-SU2 observable evidence that the higher priority update type ran first"]),

 tc("SWE1-FOTA-218", HU, "CFTS057-4907255", FN, "P1", "中",
  "**可寫**＋⚠ 錨為機制 3 攔下之首選（0.221）：倒車影像於更新期間之可用性可觀測（掛倒檔）",
  "The SW Update HMI and WiFi Update Service logic shall ensure that rear-visibility related software functions required for FMVSS 111 compliance, including backup camera display availability, video continuity, and mandatory overlays, remain operational during all phases of software update execution.",
  "Backup camera stays available during an update",
  [B, WIFI, PKG, "The reverse camera view can be selected by engaging reverse gear"],
  ["1. Trigger an update availability check to the OTA Server and let the deployment package download run",
   f"2. {REC}",
   "3. Engage reverse gear while the download is running",
   "4. Check that the head unit shows the backup camera view with its overlays while the download is running"],
  ["1. The deployment package download runs on the head unit",
   f"2. {ERREC}",
   "3. Reverse gear is engaged while the download is running",
   "4. The recorded screen content shows the backup camera view with its overlays while the download is running"]),

 tc("SWE1-FOTA-219", HU, "CFTS057-4907243", FN, "P1", "中",
  "**可寫**：倒檔期間之重開機延後可觀測（畫面不重啟）",
  "The SW Update HMI and WiFi Update Service logic shall defer non-emergency reboot execution requested during software update when reverse gear is active.",
  "Reboot waits while reverse gear is engaged",
  [B, WIFI, DL, DL2, "The reverse camera view can be selected by engaging reverse gear"],
  ["1. Accept the installation on the head unit so that a reboot is requested",
   f"2. {REC}",
   "3. Engage reverse gear before the reboot takes place and hold it for one minute",
   "4. Check that the head unit does not reboot while reverse gear is engaged"],
  ["1. The installation is accepted and a reboot is requested",
   f"2. {ERREC}",
   "3. Reverse gear is engaged and held for one minute",
   "4. The recorded screen content shows no reboot while reverse gear is engaged"]),

 tc("SWE1-FOTA-220", HU, "CFTS057-4907252", FN, "P2", "中",
  "**可寫**；與 `218` 之別在**其所驗之時點**：`218` 驗下載期間之可用性，本列驗 reflash 不中斷已在顯示中之影像",
  "The SW Update HMI and WiFi Update Service logic shall prevent software reflash activities from interrupting the active backup camera video feed and shall preserve backup camera display priority while the reverse camera view is active during a radio reflash event.",
  "Reflash does not interrupt a backup camera view already on screen",
  [B, WIFI, DL, DL2, "The reverse camera view can be selected by engaging reverse gear"],
  ["1. Engage reverse gear so that the backup camera view is displayed",
   f"2. {REC}",
   "3. Accept the installation on the head unit while the backup camera view is displayed",
   "4. Check that the backup camera video feed continues without interruption while the reverse camera view is active"],
  ["1. The backup camera view is displayed",
   f"2. {ERREC}",
   "3. The installation is accepted while the backup camera view is displayed",
   "4. The recorded screen content shows the backup camera video feed continuing without interruption"]),
]

LOW_REASONS = {
 "SWE1-FOTA-154": [("統攝，其各信號分屬他列", True)],
 "SWE1-FOTA-157": [("失敗不可注入", True), ("與 `162`／`167` 同源", True),
                   ("錨為機制 3 之首選（0.229）", "anchor")],
 "SWE1-FOTA-160": [("能力命題無判準（DR-SU6）", True), ("eCall 不可於台架實撥", True)],
 "SWE1-FOTA-162": [("失敗不可注入", True), ("錨為機制 3 之首選（0.210）", "anchor")],
 "SWE1-FOTA-163": [("行駛中安裝不可為", True), ("錨為機制 3 之首選（0.211）", "anchor")],
 "SWE1-FOTA-167": [("失敗不可注入", True), ("與 `157`／`162` 同源", True)],
 "SWE1-FOTA-215": [("服務間之設值無外部面", True)],
 "SWE1-FOTA-216": [("查詢在伺服器側", True)],
 "SWE1-FOTA-217": [("多類型 campaign 不可佈置", True)],
}
MECH3 = ["SWE1-FOTA-156", "SWE1-FOTA-157", "SWE1-FOTA-162",
         "SWE1-FOTA-163", "SWE1-FOTA-218"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T78f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T78f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T78f —— batch 18 之產出（`Deployment Flow` 餘 10 ＋ `HU FOTA via TBM` 前 6）\n")
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
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["ts"], t["conf"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 | Test Set | 自信度 | PENDING |")
    print("|---|---|---|---|:--:|---:|")
    for r, tid, req, ts, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | `{ts}` | **{cf}** | {pd} |")
    q, a, excl = [], [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        un = [(r, k) for r, k in rs if k is not True]
        (excl if not un else (a if all(k == "anchor" for _, k in un) else q)).append(i)
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {sum(1 for r in rows if r[5]==0)}**")
    print(f"- 品質訊號 **{len(q)}**｜錨定訊號 **{len(a)}**｜可排除 {len(excl)}"
          f"｜抽驗組成 {len(set(q)|set(a)|set(mid)|set(m3))} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
