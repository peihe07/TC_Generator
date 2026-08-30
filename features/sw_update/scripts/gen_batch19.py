#!/usr/bin/env python3
"""T79d —— batch 19：`HU FOTA via TBM` 餘 30 之前 16 列（下放包 67 §五）。

**⚠ 本批之 105 比率其上限已知為 6%** —— 依下放包 67 §四 #3，
**本窗（17–19）記為「因可選組窮盡而未達標」，不記為偏向**。

**⚠ `233`／`234` 為 `DUP_CANDIDATES.md` 之第二高分對（0.882），且其錨同為 `4907779`**
—— **候選清單於本批首次被起草驗證：二列確為同源。**
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch19"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 271
TS = "HU FOTA via TBM"
FN = "功能測試 (Functional based ; no specific technique)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
ROV = "An ROV forced update campaign has been staged for this vehicle"
REV = "The reverse camera view can be selected by engaging reverse gear"
REC = "Record the head unit screen content as continuous video capture until the check in the final step is completed"
ERREC = "The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, spec, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=FN, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, spec, prio, note, item, paren, what, extra=()):
    return tc(req, spec, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server and let the flow run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The update flow runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


def prop(req, spec, prio, note, item, paren, val, screen):
    """`$FOTA_MASTER.*` 之值不可由台架設定 —— 其設定手段掛 `PENDING`，畫面後果可觀測。"""
    return tc(req, spec, prio, "低", note, item, paren,
              [B, WIFI, ROV, f"PENDING: DR-SU2 means of making {val}"],
              [f"1. PENDING: DR-SU2 step to make {val}",
               f"2. {REC}",
               f"3. PENDING: DR-SU2 check that the head unit {screen} in that state"],
              [f"1. PENDING: DR-SU2 observable evidence of {val}",
               f"2. {ERREC}",
               f"3. PENDING: DR-SU2 observable evidence that the head unit {screen}"])


TCS = [
 internal("SWE1-FOTA-221", "CFTS057-4907251", "P2",
  "**第二型**：版本相容性之比對在服務內部；其外部後果（不安裝）與 `172` 相交",
  "The WiFi Update Service shall analyze deployment package metadata received through SWMC and shall verify that the target software package version is compatible with the detected MCPU hardware platform before installation is permitted.",
  "Package version is checked against the MCPU hardware variant",
  "the compatibility check the service performed between the package version and the MCPU hardware variant"),

 tc("SWE1-FOTA-222", "CFTS057-4907245", "P1", "低",
  "**第四型**；**與 `217`（batch 18）同族** —— 皆需同時佈置二種更新類型",
  "When both software update and map update sessions are available at the same time, the Arbiter Service shall prioritize the software update session.",
  "Software update runs before a map update",
  [B, WIFI,
   "PENDING: DR-SU2 means of making a software update and a map update available at the same time"],
  ["1. PENDING: DR-SU2 step to make a software update and a map update available at the same time",
   "2. PENDING: DR-SU2 check that the software update session runs before the map update session"],
  ["1. PENDING: DR-SU2 observable evidence that both update types are available",
   "2. PENDING: DR-SU2 observable evidence that the software update ran first"]),

 tc("SWE1-FOTA-223", "CFTS057-4907244", "P1", "中",
  "**可寫**；與 `220`（batch 18）之別：`220` 驗影像不中斷，本列驗**疊層之抑制**",
  "The SW Update HMI and WiFi Update Service logic shall preserve backup camera display priority and suppress non-safety-critical update overlays during a radio reflash event irrespective of update method, including USB Update, WiFi FOTA, and MOTA when equipped.",
  "Update overlays are suppressed while the backup camera is shown",
  [B, WIFI, PKG, REV],
  ["1. Trigger an update availability check to the OTA Server and let the deployment package download run",
   f"2. {REC}",
   "3. Engage reverse gear while the download is running",
   "4. Check that the head unit shows no update overlay on top of the backup camera view"],
  ["1. The deployment package download runs on the head unit",
   f"2. {ERREC}",
   "3. Reverse gear is engaged while the download is running",
   "4. The recorded screen content shows the backup camera view with no update overlay on top of it"]),

 tc("SWE1-FOTA-224", "CFTS057-4907243", "P2", "中",
  "**可寫**；與 `223` 之別在**其所抑制之物**（彈窗、進度畫面、互動疊層 vs 疊層）—— **二列之相交列 DR-SU3**",
  "The SW Update HMI shall suppress all non-safety-critical software update pop-ups, progress screens, and user interaction overlays when reverse gear status is detected and the backup camera display is active.",
  "No update pop-up or progress screen appears while reversing",
  [B, WIFI, PKG, REV],
  ["1. Trigger an update availability check to the OTA Server so that update pop-ups would normally be shown",
   f"2. {REC}",
   "3. Engage reverse gear so that the backup camera display is active",
   "4. Check that the head unit shows no update pop-up and no update progress screen while the backup camera display is active"],
  ["1. The update availability check completes on the head unit",
   f"2. {ERREC}",
   "3. Reverse gear is engaged and the backup camera display is active",
   "4. The recorded screen content shows no update pop-up and no update progress screen while the backup camera display is active"]),

 prop("SWE1-FOTA-225", "CFTS057-4907884", "P2",
  "`$FOTA_MASTER.*` 之值由 FOTA Master 送出，**台架設定其值之手段未確立**；其畫面後果可觀測",
  'When the received value isFOTA_MASTER.FOTA_Status = "No FOTA Event" , the ROV Update Service shall suppress propagation of forced update triggers to the ROV FOTA HMI.',
  "Forced update HMI stays hidden while no FOTA event is signalled",
  "the FOTA Master to report no FOTA event on its status property",
  "shows no forced update HMI"),

 prop("SWE1-FOTA-226", "CFTS057-4907891", "P2",
  "同 `225` 之型；其顯示之內容為**已儲存之取消原因**",
  "The ROV FOTA HMI shall display software update was cancelled along with the corresponding cancellation reason.",
  "Stored cancellation reason appears at the next ignition cycle",
  "the FOTA Master to report a cancellation reason other than no error",
  "displays the stored cancellation reason at the next ignition cycle"),

 prop("SWE1-FOTA-227", "CFTS057-4907885", "P2",
  "同 `225` 之型；其後果為**強制排程**（無 delay 選項）",
  "When the received value indicates $FOTA_MASTER.Delay_Prohibited$ = [Prohibited], the ROV Update Service shall instruct the ROV FOTA HMI to restrict all user interaction flows except update scheduling.",
  "User is forced to schedule when delay is prohibited",
  "the FOTA Master to report that delaying the update is prohibited",
  "offers no delay option and requires the user to schedule the update"),

 internal("SWE1-FOTA-228", "CFTS057-4907880", "P2",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.232）：其述為**訊號之來源**（SGW vs FOTA Master），而來源於畫面無表徵",
  "The ROV FOTA AppService shall receive $FOTA_MASTER.FOTA_Status$ from the Secure Gateway (SGW) through the vehicle property interface using CarProperty Manager.",
  "FOTA_Status is taken from the Secure Gateway",
  "the source from which the ROV FOTA AppService received $FOTA_MASTER.FOTA_Status$"),

 internal("SWE1-FOTA-229", "CFTS057-4907899", "P2",
  "**第二型**：`SGW_FOTA_HMI_ETM.4215` 為 Ethernet 訊息，**其注入與側錄手段皆未確立**",
  "The ROV Update Service shall receive HMI information through the Ethernet message SGW_FOTA_HMI_ETM.4215 using CarProperty Manager.",
  "HMI information arrives on the SGW Ethernet message",
  "the HMI information carried on the Ethernet message SGW_FOTA_HMI_ETM.4215"),

 prop("SWE1-FOTA-230", "CFTS057-4907880", "P1",
  "同 `225` 之型；其後果為**三選一之提示**（接受／延後／排程）",
  "The ROV FOTA HMI shall provide the user with options to accept, delay, or schedule the FOTA.",
  "User is prompted to accept, delay or schedule",
  "the FOTA Master to report that it is waiting for HMI acceptance",
  "prompts the user to accept, delay or schedule the update"),

 tc("SWE1-FOTA-231", "CFTS057-4907908", "P1", "中",
  "**可寫**：ROV campaign 之佈置有先例（batch ROV-A／B），What's New 之選取與顯示皆在畫面",
  "The ROV FOTA HMI shall capture the user selection event for the “What’s New” option from the HMI input handler.",
  "What's New selection is taken and its content shown",
  [B, WIFI, ROV, "The ROV forced update pop-up is displayed on the head unit"],
  [f"1. {REC}",
   "2. Select the “What’s New” option on the ROV forced update pop-up",
   "3. Check that the head unit shows the What's New content after the selection"],
  [f"1. {ERREC}",
   "2. The “What’s New” option is selected on the ROV forced update pop-up",
   "3. The recorded screen content shows the What's New content after the selection"]),

 internal("SWE1-FOTA-232", "CFTS057-4907900", "P2",
  "**第二型**：進度資訊來自 `SGW_FOTA_HMI_ETM.4215`（同 `229`），其抽取在服務內部",
  "The ROV Update Service shall monitor update progress information received through the SGW_FOTA_HMI_ETM.4215 through CarPropertyManager interface.",
  "Progress information is taken from the SGW Ethernet message",
  "the update progress information the service extracted from the Ethernet message"),

 internal("SWE1-FOTA-233", "CFTS057-4907779", "P2",
  "⚠ **`DUP_CANDIDATES.md` 第二高分對（0.882）之一，且與 `234` 同錨 `4907779`** —— **候選清單於本批首次被起草驗證：二列確為同源**",
  "The TBM Update Service shall receive the download descriptor (DD) file from SWMC and shall extract the estimated TBM software update time information from the DD metadata received from the GSDP.",
  "Estimated TBM update time is extracted from the DD",
  "the estimated TBM update time the service extracted from the Download Descriptor",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-234",)),

 internal("SWE1-FOTA-234", "CFTS057-4907779", "P3",
  "⚠ **與 `233` 同錨同義**，其差在本列另抽出 `WhatsNew`",
  "The TBM Update Service shall extract the \"WhatsNew\" information and 'Estimated time' from the DD metadata.",
  "WhatsNew and estimated time are extracted from the DD",
  "the WhatsNew information the service extracted from the Download Descriptor",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-233",)),

 internal("SWE1-FOTA-235", "CFTS057-4907778", "P2",
  "**第二型**：MQTT 之訂閱與其主題名於車機無表徵，**其驗證需網路側錄**（同 `279`／`252`）",
  "The SWMC shall subscribe to the MQTT FOTA topic \"FOTA\" to receive OTA-related messages and deployment information for software update processing.",
  "SWMC subscribes to the FOTA MQTT topic",
  "the MQTT subscription the SWMC made towards the GSDP"),

 tc("SWE1-FOTA-236", "CFTS057-4907889", "P1", "中",
  "**可寫**；與 `231` 之別在**其來源之彈窗**（Forced Update Available A／B vs 一般 ROV 彈窗）",
  "The ROV FOTA HMI shall detect when the user selects the \"What's New\" option from the \"ROV Forced Update Available A\" or \"ROV Forced Update Available B\" pop-up.",
  "What's New can be opened from either forced update pop-up",
  [B, WIFI, ROV, "The \"ROV Forced Update Available A\" pop-up is displayed on the head unit"],
  [f"1. {REC}",
   "2. Select the \"What's New\" option on the \"ROV Forced Update Available A\" pop-up",
   "3. Check that the head unit shows the What's New content after the selection from that pop-up"],
  [f"1. {ERREC}",
   "2. The \"What's New\" option is selected on the \"ROV Forced Update Available A\" pop-up",
   "3. The recorded screen content shows the What's New content after the selection from that pop-up"]),
]

LOW_REASONS = {
 "SWE1-FOTA-221": [("相容性比對無外部面", True)],
 "SWE1-FOTA-222": [("二類型同時可用不可佈置", True)],
 "SWE1-FOTA-225": [("`$FOTA_MASTER.*` 之值不可設定", True)],
 "SWE1-FOTA-226": [("同上", True)],
 "SWE1-FOTA-227": [("同上", True)],
 "SWE1-FOTA-228": [("訊號來源無畫面表徵", True), ("錨為機制 3 之首選（0.232）", "anchor")],
 "SWE1-FOTA-229": [("Ethernet 訊息需注入與側錄", True)],
 "SWE1-FOTA-230": [("`$FOTA_MASTER.*` 之值不可設定", True)],
 "SWE1-FOTA-232": [("同 `229`", True)],
 "SWE1-FOTA-233": [("DD 抽取無外部面", True), ("與 `234` 同源", True)],
 "SWE1-FOTA-234": [("同上", True)],
 "SWE1-FOTA-235": [("MQTT 需側錄", True)],
}
MECH3 = ["SWE1-FOTA-228"]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T79d：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T79d：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T79d —— batch 19 之產出（`HU FOTA via TBM` 前 16／餘 30）\n")
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
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {sum(1 for r in rows if r[4]==0)}**")
    print(f"- 品質訊號 **{len(q)}**｜錨定訊號 **{len(a)}**｜可排除 {len(excl)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
