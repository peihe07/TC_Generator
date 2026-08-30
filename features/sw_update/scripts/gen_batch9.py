#!/usr/bin/env python3
"""T69g —— batch 9：`Session Management` 13 列（下放包 57 §三）。

**選組依據**（下放包 51 §二 之判準，惟其優先序第 1 條被配額覆蓋）：
其 105 比率 **38%**（母體 34%）—— **依 51 §二 優先序第 1 條（105 低者優先）
本不該選它**，而下放包 52 §二 #5(b) 之配額令「每三批至少一個高難度組
（105 ≥ 33%）」。**本批於配額窗之第一批即滿足之**，其理由見上繳包 57 §5。

**⚠ 本組之特徵：三對重複表述**（`350`／`368`、`351`／`369`、`353`／`337`）——
其外部後果相同而條文分列二處，入 DR-SU3。

**型別**：
- **伺服器側表徵**（DR-SU2(e)）：`347`／`352`
- **第二型**（無外部面）：`348`／`349`／`350`／`353`／`355`／`356`／`368`
- **第四型**（server-initiated 之推送不可得）：`351`／`361`／`369`
- **可寫**：`354`（下載接受請求之畫面）
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch9"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 123
TS = "Session Management"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"

B = "1. The vehicle is in Body ON mode"
WIFI = "2. The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "3. An update package is staged on the OTA Server for this head unit"
PUSH = "PENDING: DR-SU2 means of making the OTA Server start a session towards this head unit"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-347", "CFTS057-4907579", BV, "P1", "低",
  "**門檻列**（`24 hours` 逐字取自 037）＋伺服器側表徵：輪詢本身於車機無畫面，其到達之表徵在伺服器",
  "The SWMC shall support a configurable polling interval for vehicle-initiated OTA update sessions with a default value of 24 hours.",
  "Vehicle polls the server once per 24 hours by default",
  [B, WIFI, "3. The polling interval of the head unit is left at its default value",
   "4. PENDING: DR-SU2 means of reading, on the OTA Server side, the times at which this head unit polls"],
  ["1. Leave the head unit powered and connected for 48 hours without changing the polling interval",
   "2. PENDING: DR-SU2 step to read the polling times recorded on the OTA Server for this head unit"],
  ["1. The head unit stays powered and connected for 48 hours",
   "2. PENDING: DR-SU2 observable evidence that the polling times recorded on the OTA Server are 24 hours apart"]),

 tc("SWE1-FOTA-348", "CFTS057-4907579", FN, "P2", "低",
  "**第二型**：組態參數之設定與生效皆在服務內部，於車機無外部面",
  "The SWMC shall support configuration and reconfiguration of the vehicle-initiated OTA polling interval using a configuration parameter expressed in hours.",
  "Polling interval can be set and changed through its configuration parameter",
  [B, WIFI,
   "3. PENDING: DR-SU2 means of setting and of reading the polling interval configuration parameter"],
  ["1. PENDING: DR-SU2 step to set the polling interval configuration parameter to a value in hours",
   "2. PENDING: DR-SU2 step to change the polling interval configuration parameter to a different value in hours"],
  ["1. PENDING: DR-SU2 observable evidence that the polling interval configuration parameter holds the value that was set",
   "2. PENDING: DR-SU2 observable evidence that the polling interval configuration parameter holds the changed value"]),

 tc("SWE1-FOTA-349", "CFTS057-4907582", FN, "P2", "低",
  "**第二型**＋**105 列**：`queue a session` 為內部佇列，其外部後果（session 實際發起）屬 `347`",
  "The SWMC shall monitor the configured polling timer and queue a vehicle-initiated OTA session when the polling timer expires.",
  "Session is queued when the polling timer expires",
  [B, WIFI,
   "3. PENDING: DR-SU2 means of observing the queue of vehicle-initiated OTA sessions held by the SWMC"],
  ["1. Leave the head unit powered and connected until the configured polling timer expires",
   "2. PENDING: DR-SU2 step to read the queue of vehicle-initiated OTA sessions after the polling timer expires"],
  ["1. The configured polling timer expires while the head unit stays powered and connected",
   "2. PENDING: DR-SU2 observable evidence that a vehicle-initiated OTA session is held in the queue after the polling timer expires"]),

 tc("SWE1-FOTA-350", "CFTS057-4907378", FN, "P1", "低",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.201）；**與 `368` 重複表述**，入 DR-SU3",
  "If one or more preconditions are not satisfied, the SWMC shall queue the OTA update session until the preconditions are satisfied.",
  "Session waits in the queue while a precondition is not satisfied",
  [B, WIFI, PKG,
   "4. The battery state of charge reported on $IBS_SOC$ is set to 60% so that a download precondition is not satisfied",
   "5. PENDING: DR-SU2 means of observing the queue of OTA update sessions held by the SWMC"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read the queue of OTA update sessions while the battery state of charge is 60%",
   "3. Raise the battery state of charge reported on $IBS_SOC$ to 80%",
   "4. PENDING: DR-SU2 step to read the queue of OTA update sessions after the battery state of charge is 80%"],
  ["1. The update availability check completes and an update is reported as available",
   "2. PENDING: DR-SU2 observable evidence that the session is held in the queue while the precondition is not satisfied",
   "3. The battery state of charge reported on $IBS_SOC$ is 80%",
   "4. PENDING: DR-SU2 observable evidence that the session leaves the queue once the precondition is satisfied"]),

 tc("SWE1-FOTA-351", "CFTS057-4907559", FN, "P1", "低",
  "**第四型**：server-initiated session 之推送手段不可得；**與 `369` 重複表述**，入 DR-SU3",
  "The SWMC shall execute the server-initiated OTA update session using the same workflow as the vehicle user-initiated OTA update session after precondition validation is completed.",
  "Server-started session shows the same screens as a user-started one",
  [B, WIFI, PKG, "4. " + PUSH],
  ["1. Trigger an update availability check from the head unit and record the screens shown until the update is accepted",
   "2. PENDING: DR-SU2 step to make the OTA Server start a session towards this head unit",
   "3. Check that the screens shown for the server-started session are the same as those recorded for the head-unit-started session"],
  ["1. The screens shown for the head-unit-started session are recorded",
   "2. PENDING: DR-SU2 observable evidence that the OTA Server started a session towards this head unit",
   "3. PENDING: DR-SU2 comparison of the screens of the server-started session with those of the head-unit-started session"]),

 tc("SWE1-FOTA-352", "CFTS057-4907585", FN, "P1", "低",
  "伺服器側表徵（DR-SU2(e)）：清單之請求與回傳兩端皆在伺服器與服務之間",
  "The SWMC shall receive complete or partial software inventory requests from the OTA server, request the required software inventory from the WiFiUpdateService, and transmit the retrieved software inventory to the OTA server.",
  "Requested software inventory reaches the server",
  [B, WIFI,
   "3. PENDING: DR-SU2 means of sending a software inventory request from the OTA Server to this head unit",
   "4. PENDING: DR-SU2 means of reading, on the OTA Server side, the software inventory received from this head unit"],
  ["1. PENDING: DR-SU2 step to send a complete software inventory request from the OTA Server",
   "2. PENDING: DR-SU2 step to read the software inventory received by the OTA Server"],
  ["1. PENDING: DR-SU2 observable evidence that the software inventory request reached this head unit",
   "2. PENDING: DR-SU2 observable evidence of the software inventory received by the OTA Server"]),

 tc("SWE1-FOTA-353", "CFTS057-4907300", FN, "P2", "低",
  "**第二型**：DD 與 package 之下載次序於車機無表徵；**其後半與 `337` 相交**（部署流程於下載完成後啟動），入 DR-SU3",
  "The SWMC shall download the Deployment Description (DD) before downloading the associated deployment package.",
  "Deployment Description is downloaded before the package",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU2 means of observing the order in which the Deployment Description and the deployment package are downloaded"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read the order in which the Deployment Description and the deployment package were downloaded"],
  ["1. The update is accepted and the download starts on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the Deployment Description was downloaded before the deployment package"]),

 tc("SWE1-FOTA-354", "CFTS057-4907588", FN, "P1", "中",
  "**本組唯一可寫之列**：下載接受請求之呈現與使用者決定皆在畫面上",
  "The WiFiUpdateService shall present the download acceptance request to the user through the HMI when all download preconditions are satisfied and shall provide the user's decision to the SWMC.",
  "Download acceptance request is shown and the user's decision is taken",
  [B, WIFI, PKG,
   "4. The battery state of charge reported on $IBS_SOC$ is set to 80%"],
  ["1. Record the head unit screen content as continuous video capture until the download starts",
   "2. Trigger an update availability check to the OTA Server",
   "3. Check that the head unit shows a request to accept the download",
   "4. Accept the download on the head unit",
   "5. Check that the download starts after the acceptance is given"],
  ["1. The head unit screen content until the download starts is recorded as continuous video capture",
   "2. The update availability check completes and an update is reported as available",
   "3. The recorded screen content shows a request to accept the download",
   "4. The download is accepted on the head unit",
   "5. The recorded screen content shows the download starting after the acceptance is given"]),

 tc("SWE1-FOTA-355", "CFTS057-4907396", FN, "P2", "低",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.179，本 feature 至今最低）：服務間之資料供給無外部面",
  "The WiFiUpdateService shall provide the vehicle and system data required by the SWMC to validate the download preconditions.",
  "Vehicle and system data is handed to the SWMC for precondition validation",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU2 means of observing the vehicle and system data handed from the WiFiUpdateService to the SWMC"],
  ["1. Trigger an update availability check to the OTA Server and accept the download on the head unit",
   "2. PENDING: DR-SU2 step to read the vehicle and system data handed to the SWMC for precondition validation"],
  ["1. The download is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the vehicle and system data handed to the SWMC for precondition validation"]),

 tc("SWE1-FOTA-356", "CFTS057-4907483", FN, "P2", "低",
  "**第二型**：套件之驗證與其可用通知皆在服務之間；其外部後果（安裝開始）屬 `337`",
  "The SWMC shall notify the WiFiUpdateService that the validated deployment package is available for deployment.",
  "WiFiUpdateService is notified that the validated package is available",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU2 means of observing the notification sent from the SWMC to the WiFiUpdateService"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the deployment package download finish",
   "2. PENDING: DR-SU2 step to read the notification sent to the WiFiUpdateService after the deployment package is validated"],
  ["1. The deployment package download finishes on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the notification sent to the WiFiUpdateService after the deployment package is validated"]),

 tc("SWE1-FOTA-361", "CFTS057-4907566", FN, "P1", "低",
  "**第四型**（推送不可得）＋**105 列**；**其可觀測面存在** —— 前景操作於更新期間仍可用",
  "The SWMC and wifiupdateservice shall execute server-initiated OTA update flows in the background without blocking foreground system operations.",
  "Radio and settings stay usable while a server-started update runs",
  [B, WIFI, PKG, "4. " + PUSH],
  ["1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head unit",
   "2. While the server-started update flow is running, tune the radio to a different station and open the settings menu",
   "3. Check that the radio changes station and that the settings menu opens while the server-started update flow is running"],
  ["1. PENDING: DR-SU2 observable evidence that a server-started update flow is running",
   "2. The radio station is changed and the settings menu is opened",
   "3. The radio changes station and the settings menu opens while the server-started update flow is running"]),

 tc("SWE1-FOTA-368", "CFTS057-4907559", FN, "P2", "低",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.254）；**與 `350` 重複表述**（其差全在 TC client 之轉送一段），入 DR-SU3",
  "The SWMC shall evaluate the configured preconditions upon receiving an OTA session request and shall queue the session request if one or more preconditions are not satisfied.",
  "Session request from the TC client is queued while a precondition fails",
  [B, WIFI, PKG, "4. " + PUSH,
   "5. PENDING: DR-SU2 means of distinguishing this queueing from the one verified by SWE1-FOTA-350"],
  ["1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head unit while a download precondition is not satisfied",
   "2. PENDING: DR-SU2 step to read the queue of OTA session requests received through the TC client"],
  ["1. PENDING: DR-SU2 observable evidence that a session request arrived through the TC client",
   "2. PENDING: DR-SU2 observable evidence distinguishing this queued request from the one verified for SWE1-FOTA-350"]),

 tc("SWE1-FOTA-369", "CFTS057-4907559", FN, "P2", "低",
  "**第四型**＋**105 列**；**與 `351` 重複表述**（其差全在 TC client 之轉送一段），入 DR-SU3",
  "The SWMC shall execute server-initiated OTA update sessions using the same workflow as the vehicle-initiated OTA update flow after successful session initiation.",
  "Session started through the TC client runs the vehicle-initiated workflow",
  [B, WIFI, PKG, "4. " + PUSH,
   "5. PENDING: DR-SU2 means of distinguishing this session from the one verified by SWE1-FOTA-351"],
  ["1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head unit through the TC client",
   "2. PENDING: DR-SU2 step to compare the screens of that session with those of a head-unit-started session"],
  ["1. PENDING: DR-SU2 observable evidence that the session was started through the TC client",
   "2. PENDING: DR-SU2 observable evidence distinguishing this session from the one verified for SWE1-FOTA-351"]),
]

LOW_REASONS = {
 "SWE1-FOTA-347": [("輪詢之表徵在伺服器側", True), ("48 小時之等待成本高但可行", True)],
 "SWE1-FOTA-348": [("組態參數無外部面", True)],
 "SWE1-FOTA-349": [("內部佇列無外部面", True)],
 "SWE1-FOTA-350": [("內部佇列無外部面", True),
                   ("錨為機制 3 攔下之首選（0.201），未經 GT 驗證", False)],
 "SWE1-FOTA-351": [("server-initiated 之推送不可得", True)],
 "SWE1-FOTA-352": [("兩端皆在伺服器側", True)],
 "SWE1-FOTA-353": [("下載次序無外部面", True)],
 "SWE1-FOTA-355": [("服務間之資料供給無外部面", True),
                   ("錨為機制 3 攔下之首選（0.179），未經 GT 驗證", False)],
 "SWE1-FOTA-356": [("服務間之通知無外部面", True)],
 "SWE1-FOTA-361": [("推送不可得", True)],
 "SWE1-FOTA-368": [("推送不可得", True), ("與 `350` 不可區辨", True),
                   ("錨為機制 3 攔下之首選（0.254），未經 GT 驗證", False)],
 "SWE1-FOTA-369": [("推送不可得", True), ("與 `351` 不可區辨", True)],
}
MECH3 = ["SWE1-FOTA-350", "SWE1-FOTA-355", "SWE1-FOTA-368"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T69g：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T69g：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T69g —— batch 9 之產出（`Session Management`，13 列，**配額批**）\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": t["ts"],
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])
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
    print(f"\n### 分層抽驗（含加重規則）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- 可排除之 `低`：{len(excl)} 列")
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— 未由 `PENDING` 承載者："
              + "、".join(f"**{r}**" for r in un))
    print(f"- 機制 3 攔下：" + "、".join(f"`SU-{i:03d}`" for i in m3))
    print(f"- **抽驗組成 = 低 ∪ 中 ∪ 機制 3 = {len(union)} 列**")
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
