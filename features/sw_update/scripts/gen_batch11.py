#!/usr/bin/env python3
"""T71h —— batch 11：`Session Flows` 16 列（下放包 59 §四）。

**新配額之窗（batch 11–13）起始剩餘 105 比率 = 42%**（下放包 59 §三 #7）。
本批之 105 比率 **62%（10／16）** —— **窗內第一批即高於目標**，其累計見上繳包 59 §4。

**⚠ 本批揭出一組五列之重複表述**：`274`／`275`／`276`（本批）與
`347`／`348`（batch 9）**五列皆為「輪詢間隔之組態」** —— 入 DR-SU3。

**型別**：
- **可寫**：`019`（105 列而可寫，R-SU32 v2(e) 之又一例）、`189`、`190`
- **伺服器側（DR-SU2(e)）**：`288`／`289`／`290`／`275`／`276`
- **第二型**：`169`／`191`／`273`／`274`／`279`
- **第四型**：`187`（HMI 不可用之狀態不可佈置）、`272`／`277`（推送不可得）
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch11"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 150
TS = "Session Flows"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"

B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
NOPKG = "No update package is staged on the OTA Server for this head unit"
REC = "2. Record the head unit screen content as continuous video capture until the check in the final step is completed"
ER_REC = "2. The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-019", "CFTS057-4907616", DT, "P1", "中",
  "**105 列而可寫**（R-SU32 v2(e) 之又一例）：其外部後果為「下載不啟動」，可觀測",
  "If neither condition is satisfied, the WiFi Update Service shall prevent initiation of firmware download through the embedded modem.",
  "Modem download does not start outside IGN_RUN or engine auto-stop",
  [B, PKG, "The vehicle ignition is set to accessory so that $PowerMode$ is not IGN_RUN",
   "The engine auto-stop state is not active"],
  ["1. Trigger an update availability check to the OTA Server with no Wi-Fi network connected",
   REC,
   "3. Check that no firmware download over the embedded modem starts while the ignition is in accessory and the engine auto-stop state is not active"],
  ["1. The update availability check completes and an update is reported as available",
   ER_REC,
   "3. The recorded screen content shows no firmware download over the embedded modem starting while the ignition is in accessory"]),

 tc("SWE1-FOTA-189", "CFTS057-4907280", FN, "P1", "中",
  "使用者主動之「Check for Update」全程可觀測",
  "The SW Update HMI shall detect a user request for Check for Update and shall send the request to the WiFi Update Service.",
  "Check for Update request is taken from the user and acted on",
  [B, WIFI, PKG, "The software update menu is open on the head unit"],
  ["1. Select the Check for Update option on the head unit",
   REC,
   "3. Check that the head unit reports the result of an update availability check after the selection"],
  ["1. The Check for Update option is selected",
   ER_REC,
   "3. The recorded screen content shows the result of an update availability check after the selection"]),

 tc("SWE1-FOTA-190", "CFTS057-4907360", FN, "P1", "中",
  "與 `189` 之別在**判定對象**：`189` 驗請求被受理，本列驗「無更新」之訊息內容",
  "The SW Update HMI shall display a message indicating that the vehicle software is up to date and that no updates are available.",
  "Up-to-date message is shown when the server reports no update",
  [B, WIFI, NOPKG, "The software update menu is open on the head unit"],
  ["1. Select the Check for Update option on the head unit",
   REC,
   "3. Check that the head unit displays a message stating that the vehicle software is up to date and that no updates are available"],
  ["1. The Check for Update option is selected",
   ER_REC,
   "3. The recorded screen content shows a message stating that the vehicle software is up to date and that no updates are available"]),

 tc("SWE1-FOTA-187", "CFTS057-4907443", FN, "P1", "低",
  "**第四型**：使 SW Update HMI 不可用之狀態不可佈置；其後果（無使用者輸入而下載續行）本身可觀測",
  "When the SW Update HMI is unavailable, the WiFi Update Service shall interact with SWMC to continue deployment package download, installation, retry, and completion processing without user input.",
  "Download continues with no user input while the update HMI is unavailable",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of placing the SW Update HMI in an unavailable state on the head unit"],
  ["1. PENDING: DR-SU2 step to place the SW Update HMI in an unavailable state",
   "2. Trigger an update availability check to the OTA Server",
   "3. PENDING: DR-SU2 check that the deployment package download continues to completion with no user input while the SW Update HMI is unavailable"],
  ["1. PENDING: DR-SU2 observable evidence that the SW Update HMI is unavailable",
   "2. The update availability check completes",
   "3. PENDING: DR-SU2 observable evidence that the download completed with no user input while the SW Update HMI was unavailable"]),

 tc("SWE1-FOTA-169", "CFTS057-4907590", FN, "P2", "低",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.215）：manifest 之解析與安裝器之分派全在服務內部",
  "The WiFi Update Service/USB Update Service shall forward MCPU firmware packages to the Update Engine for installation.",
  "MCPU firmware packages are handed to the Update Engine",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing which installer each component package of the deployment package is handed to"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read which installer received the MCPU firmware package of the deployment package"],
  ["1. The update is accepted and the installation starts on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the MCPU firmware package was handed to the Update Engine"]),

 tc("SWE1-FOTA-191", "CFTS057-4907361", FN, "P2", "低",
  "**第二型**：事件介面之定義與其回應皆在服務之間；其外部後果即各 HMI 列之行為",
  "The WiFi Update Service shall define an event handling interface for communication with the SW Update HMI.",
  "Event handling interface between the HMI and the update service exists",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing the event handling interface between the SW Update HMI and the WiFi Update Service"],
  ["1. Select the Check for Update option on the head unit",
   "2. PENDING: DR-SU2 step to read the event sent from the SW Update HMI to the WiFi Update Service"],
  ["1. The Check for Update option is selected",
   "2. PENDING: DR-SU2 observable evidence of the event sent from the SW Update HMI to the WiFi Update Service"]),

 tc("SWE1-FOTA-272", "CFTS057-4907370", FN, "P2", "低",
  "**第四型**（推送不可得）＋**105 列**；**與 `277` 重複表述**（皆為「經事件介面接收伺服器發起之 session 請求」），入 DR-SU3",
  "SWMC shall support event interface to receive server-initiated session requests from the Server.",
  "Server-initiated session requests are received through the event interface",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of making the OTA Server send a session request to this head unit",
   "PENDING: DR-SU2 means of distinguishing this interface from the one verified by SWE1-FOTA-277"],
  ["1. PENDING: DR-SU2 step to make the OTA Server send a session request to this head unit",
   "2. PENDING: DR-SU2 step to read the session request received through the event interface"],
  ["1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session request",
   "2. PENDING: DR-SU2 observable evidence distinguishing this reception from the one verified for SWE1-FOTA-277"]),

 tc("SWE1-FOTA-277", "CFTS057-4907370", FN, "P2", "低",
  "**第四型**＋**105 列**；**與 `272` 重複表述**，其差為本列另含「通知 WiFiUpdateService」一段（內部）",
  "SWMC shall notify WiFiUpdateService of the received server-initiated session to initiate the update",
  "WiFiUpdateService is notified of the received server-initiated session",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of making the OTA Server send a session request to this head unit",
   "PENDING: DR-SU2 means of observing the notification from SWMC to WiFiUpdateService"],
  ["1. PENDING: DR-SU2 step to make the OTA Server send a session request to this head unit",
   "2. PENDING: DR-SU2 step to read the notification sent from SWMC to WiFiUpdateService"],
  ["1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session request",
   "2. PENDING: DR-SU2 observable evidence of the notification sent from SWMC to WiFiUpdateService"]),

 tc("SWE1-FOTA-273", "CFTS057-4907364", FN, "P2", "低",
  "**第二型**：車輛事件之接收與評估在服務內部；其外部後果（部署被阻）屬他列",
  "SWMC shall evaluate the received vehicle events before initiating or continuing the software deployment process.",
  "Vehicle events are evaluated before deployment continues",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of injecting a vehicle event that blocks software deployment",
   "PENDING: DR-SU2 means of observing that the event was evaluated before deployment"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to inject a vehicle event that blocks software deployment",
   "3. PENDING: DR-SU2 step to read whether the injected event was evaluated before deployment continued"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence that a blocking vehicle event was injected",
   "3. PENDING: DR-SU2 observable evidence that the event was evaluated before deployment continued"]),

 tc("SWE1-FOTA-274", "CFTS057-4907367", FN, "P2", "低",
  "**第二型**＋**105 列**；**與 `347`（batch 9）／`275`／`276` 重複表述** —— 五列皆為輪詢參數之組態，入 DR-SU3",
  "SWMC shall maintain configurable polling parameters and initiate periodic communication with the Server when network connectivity is available.",
  "Polling parameters are held and periodic communication runs while connected",
  [B, WIFI,
   "PENDING: DR-SU2 means of reading the polling parameters held by the SWMC",
   "PENDING: DR-SU2 means of distinguishing this requirement from SWE1-FOTA-347, 275 and 276"],
  ["1. Leave the head unit powered and connected for one polling interval",
   "2. PENDING: DR-SU2 step to read the polling parameters held by the SWMC"],
  ["1. The head unit stays powered and connected for one polling interval",
   "2. PENDING: DR-SU2 observable evidence of the polling parameters held by the SWMC"]),

 tc("SWE1-FOTA-275", "CFTS057-4907579", FN, "P2", "低",
  "**伺服器側（DR-SU2(e)）**＋**105 列**：輪詢間隔之組態自伺服器下發，其兩端皆不在車機畫面",
  "SWMC shall support configuration of the polling interval for periodic vehicle-initiated sessions through parameters received from the server.",
  "Polling interval configured from the server is taken up",
  [B, WIFI,
   "PENDING: DR-SU2 means of sending a polling interval parameter from the OTA Server to this head unit",
   "PENDING: DR-SU2 means of reading the polling interval currently applied by the SWMC"],
  ["1. PENDING: DR-SU2 step to send a new polling interval parameter from the OTA Server",
   "2. PENDING: DR-SU2 step to read the polling interval applied by the SWMC after the parameter is sent"],
  ["1. PENDING: DR-SU2 observable evidence that the polling interval parameter reached this head unit",
   "2. PENDING: DR-SU2 observable evidence that the polling interval applied by the SWMC is the value sent by the OTA Server"]),

 tc("SWE1-FOTA-276", "CFTS057-4907367", FN, "P2", "低",
  "**伺服器側**；**與 `275` 幾乎逐字相同**（其差只在「可更新」與「已更新並套用」之時態），入 DR-SU3",
  "SWMC shall support configurable polling parameters that can be updated from the server and applied during periodic vehicle-initiated sessions.",
  "Polling parameters updated from the server apply to later sessions",
  [B, WIFI,
   "PENDING: DR-SU2 means of updating polling parameters from the OTA Server",
   "PENDING: DR-SU2 means of distinguishing this update from the one verified by SWE1-FOTA-275"],
  ["1. PENDING: DR-SU2 step to update the polling parameters from the OTA Server",
   "2. PENDING: DR-SU2 step to read the polling parameters used in the next vehicle-initiated session"],
  ["1. PENDING: DR-SU2 observable evidence that the polling parameters were updated from the OTA Server",
   "2. PENDING: DR-SU2 observable evidence distinguishing this from the update verified for SWE1-FOTA-275"]),

 tc("SWE1-FOTA-279", "CFTS057-4907355", FN, "P2", "低",
  "**第二型**＋**105 列**：通訊協定之選用於車機無表徵；**其驗證屬網路側之側錄**",
  "SWMC shall support HTTP and TLS protocols when a proprietary communication protocol is configured instead of OMA-DM.",
  "HTTP and TLS are used when a proprietary protocol is configured",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of configuring a proprietary communication protocol instead of OMA-DM",
   "PENDING: DR-SU2 means of observing the protocol used between the head unit and the OTA Server"],
  ["1. PENDING: DR-SU2 step to configure a proprietary communication protocol instead of OMA-DM",
   "2. Trigger an update availability check to the OTA Server",
   "3. PENDING: DR-SU2 step to read the protocol used for the communication with the OTA Server"],
  ["1. PENDING: DR-SU2 observable evidence that a proprietary communication protocol is configured",
   "2. The update availability check completes",
   "3. PENDING: DR-SU2 observable evidence that HTTP and TLS were used for the communication"]),

 tc("SWE1-FOTA-288", "CFTS057-4907449", FN, "P2", "低",
  "**伺服器側**＋**105 列**：命令之下發與其套用兩端皆不在車機畫面",
  "SWMC shall retrieve, interpret, and apply configuration parameters received from the server, including session-specific and global configuration settings.",
  "Configuration parameters from the server are applied",
  [B, WIFI,
   "PENDING: DR-SU2 means of sending a configuration command from the OTA Server to this head unit",
   "PENDING: DR-SU2 means of reading the configuration parameters applied by the SWMC"],
  ["1. PENDING: DR-SU2 step to send a session-specific configuration parameter from the OTA Server",
   "2. PENDING: DR-SU2 step to read the configuration parameters applied by the SWMC"],
  ["1. PENDING: DR-SU2 observable evidence that the configuration command reached this head unit",
   "2. PENDING: DR-SU2 observable evidence that the SWMC applied the parameter that was sent"]),

 tc("SWE1-FOTA-289", "CFTS057-4907451", FN, "P2", "低",
  "**伺服器側**＋**105 列**；其與 `290` 之別在**方向**：本列驗套用新設定，`290` 驗其還原",
  "SWMC shall apply the updated server configuration for subsequent communication sessions",
  "Updated server URL and port are used by later sessions",
  [B, WIFI,
   "PENDING: DR-SU2 means of sending a server URL and port configuration command to this head unit",
   "PENDING: DR-SU2 means of reading the server address used by the head unit for its sessions"],
  ["1. PENDING: DR-SU2 step to send a new server URL and port from the OTA Server",
   "2. PENDING: DR-SU2 step to read the server address used by the next communication session"],
  ["1. PENDING: DR-SU2 observable evidence that the new server URL and port reached this head unit",
   "2. PENDING: DR-SU2 observable evidence that the next session used the updated server address"]),

 tc("SWE1-FOTA-290", "CFTS057-4907451", NEG, "P2", "低",
  "**伺服器側**＋**105 列**；與 `289` 互為正負面：本列驗無效設定之還原",
  "SWMC shall validate the updated server configuration and restore the previously stored URL and port number if the new configuration is invalid",
  "Invalid server configuration is rolled back to the stored one",
  [B, WIFI,
   "PENDING: DR-SU2 means of sending an invalid server URL and port configuration to this head unit",
   "PENDING: DR-SU2 means of reading the server address stored and used by the head unit"],
  ["1. PENDING: DR-SU2 step to send an invalid server URL and port from the OTA Server",
   "2. PENDING: DR-SU2 step to read the server address used by the head unit after the invalid configuration is sent"],
  ["1. PENDING: DR-SU2 observable evidence that an invalid server configuration reached this head unit",
   "2. PENDING: DR-SU2 observable evidence that the head unit kept the previously stored server address"]),
]

LOW_REASONS = {
 "SWE1-FOTA-187": [("HMI 不可用之狀態不可佈置", True)],
 "SWE1-FOTA-169": [("解析與分派無外部面", True),
                   ("錨為機制 3 攔下之首選（0.215），未經 GT 驗證", False)],
 "SWE1-FOTA-191": [("事件介面無外部面", True)],
 "SWE1-FOTA-272": [("推送不可得", True), ("與 `277` 不可區辨", True)],
 "SWE1-FOTA-277": [("推送不可得", True), ("與 `272` 不可區辨", True)],
 "SWE1-FOTA-273": [("車輛事件不可注入", True), ("評估本身無外部面", True)],
 "SWE1-FOTA-274": [("輪詢參數無外部面", True), ("與 `347`／`275`／`276` 不可區辨", True)],
 "SWE1-FOTA-275": [("兩端皆在伺服器側", True)],
 "SWE1-FOTA-276": [("兩端皆在伺服器側", True), ("與 `275` 不可區辨", True)],
 "SWE1-FOTA-279": [("協定之選用無車機表徵", True)],
 "SWE1-FOTA-288": [("兩端皆在伺服器側", True)],
 "SWE1-FOTA-289": [("兩端皆在伺服器側", True)],
 "SWE1-FOTA-290": [("兩端皆在伺服器側", True)],
}
MECH3 = ["SWE1-FOTA-169", "SWE1-FOTA-187", "SWE1-FOTA-190"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T71h：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T71h：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T71h —— batch 11 之產出（`Session Flows`，16 列）\n")
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
    c = Counter(t["conf"] for t in TCS)
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _, _ in keep} | set(mid) | set(m3))
    deliverable = [r for r in rows if r[4] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- 可排除之 `低`：{len(excl)} 列")
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— " + "、".join(f"**{r}**" for r in un))
    print(f"- 機制 3 攔下：" + "、".join(f"`SU-{i:03d}`" for i in m3))
    print(f"- **抽驗組成 = {len(union)} 列**")
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
