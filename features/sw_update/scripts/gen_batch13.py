#!/usr/bin/env python3
"""T73f —— batch 13：`Interruption Handling`(12) ＋ `Telematics Client`(5) = 17 列。

**窗（batch 11–13）之第 3 批，目標 42%；本批 105 比率 76%（13／17）** ——
其為窗內最高，**且二組於本批全部起草完畢**（`Interruption Handling` 之前六列
已於 batch 2a 起草，`Telematics Client` 為 DR-SU2(a) 之初始清單）。

**型別**：
- **可寫**：`322`（儲存不足可佈置）、`328`（網路恢復可觸發）、`359`（併發請求可觀測）
- **DR-SU4 族**（中斷之階段判準）：`321`／`325`／`357`／`360`
- **第二型**：`323`／`324`／`326`／`363`／`364`／`366`／`367`
- **統攝**（DR-SU3 (i)）：`327`
- **值未載**：`329`（`configured retry count`）
- **三列重複表述**：`365`／`366`／`367` 皆含同一句「自 TC client 收受並轉送」
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch13"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 180
IH, TC_ = "Interruption Handling", "Telematics Client"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
FI = "基礎故障注入 (Fault Injection Lite)"

B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"


def tc(req, ts, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=ts, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-321", IH, "CFTS057-4907673", FN, "P1", "低",
  "**DR-SU4 族**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.220）：`gracefully handle` 之判準即 DR-SU4 請求 1",
  "The WiFiUpdateService shall detect the resolution of an interruption and notify SWMC to continue the OTA update session based on the current session state.",
  "Session continues from its state once the interruption is resolved",
  [B, WIFI, PKG,
   "PENDING: DR-SU4 observable indication on the head unit that the OTA client continued operation after an interruption"],
  ["1. Trigger an update availability check to the OTA Server and let the deployment package download start",
   "2. Disconnect the head unit from the network for one minute and reconnect it",
   "3. PENDING: DR-SU4 check that the session continued from the state it held when the interruption occurred"],
  ["1. The deployment package download starts",
   "2. The head unit is disconnected from the network and reconnected",
   "3. PENDING: DR-SU4 observable evidence that the session continued from its previous state"]),

 tc("SWE1-FOTA-322", IH, "CFTS057-4907676", NEG, "P1", "中",
  "⚠ 與 `346`（batch 6）相交：`346` 驗「空間不足則不啟動下載」，**本列驗「偵測後中止並回報」** —— 其回報之半在伺服器側，掛 `PENDING`",
  "The WiFiUpdateService shall detect insufficient storage space on the target unit before or during the software update process and notify SWMC.",
  "Update session aborts when storage runs out during the update",
  [B, WIFI, PKG,
   "The head unit storage is filled so that the space left is smaller than the staged package",
   "PENDING: DR-SU2 means of reading, on the OTA Server side, the failure reported for this session"],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "3. Check that the head unit shows the update session ending without the installation starting while the space left is smaller than the staged package"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The update is accepted on the head unit",
   "3. The recorded screen content shows the update session ending without the installation starting while the space left is smaller than the staged package"]),

 tc("SWE1-FOTA-323", IH, "CFTS057-4907677", FN, "P2", "低",
  "**第二型**＋**105 列**：NIA 之佇列於車機無表徵，且 NIA 之推送不可得",
  "The SWMC shall queue an incoming NIA received during an active OTA update session without interrupting the current session and shall process the queued NIA after the active session is completed.",
  "Incoming NIA waits until the active session ends",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of sending an NIA to this head unit during an active session",
   "PENDING: DR-SU2 means of observing the queue of received NIAs"],
  ["1. Trigger an update availability check to the OTA Server and let an OTA update session run",
   "2. PENDING: DR-SU2 step to send an NIA to the head unit while the session is active",
   "3. PENDING: DR-SU2 step to read whether the NIA was processed only after the session completed"],
  ["1. An OTA update session is running on the head unit",
   "2. PENDING: DR-SU2 observable evidence that an NIA arrived during the active session",
   "3. PENDING: DR-SU2 observable evidence that the NIA was processed after the session completed"]),

 tc("SWE1-FOTA-324", IH, "CFTS057-4907679", FN, "P2", "低",
  "**第二型**＋**105 列**：已下載之部分保留於儲存區，其存在於車機無表徵；**其外部後果（續傳）屬 `328`／`360`**",
  "The SWMC shall preserve the partially downloaded deployment package when an interruption occurs before the download is completed to support continuation of the OTA update session.",
  "Partially downloaded package survives the interruption",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing the partially downloaded deployment package held on the head unit"],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. Disconnect the head unit from the network",
   "3. PENDING: DR-SU2 step to read whether the partially downloaded package is still held on the head unit"],
  ["1. The download reaches part of its progress",
   "2. The head unit is disconnected from the network",
   "3. PENDING: DR-SU2 observable evidence that the partially downloaded package is still held"]),

 tc("SWE1-FOTA-325", IH, "CFTS057-4907680", FN, "P2", "低",
  "**DR-SU4 族**：`suspend` 與 `record the interruption in the log` 二者於車機皆無表徵",
  "The SWMC shall suspend the OTA update session, record the interruption in the log, and wait until the download can be resumed when an interruption occurs before the download is completed.",
  "Session is suspended and logged while the download cannot continue",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of reading the log entry recorded for an interruption",
   "PENDING: DR-SU4 observable indication that the session is suspended rather than aborted"],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. Disconnect the head unit from the network and leave it disconnected",
   "3. PENDING: DR-SU2 step to read the log entry recorded for the interruption"],
  ["1. The download reaches part of its progress",
   "2. The head unit stays disconnected from the network",
   "3. PENDING: DR-SU2 observable evidence of the log entry recorded for the interruption"]),

 tc("SWE1-FOTA-326", IH, "CFTS057-4907681", FN, "P2", "低",
  "**第二型**：比對之結果與 `HTTP byte-range` 之使用皆在網路側，**其觀測需側錄**（同 `279`）",
  "When the verification is successful and the interruption condition is resolved, the SWMC shall resume the download using an HTTP byte-range request.",
  "Resumed download continues from the byte it stopped at",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing the HTTP request used when a download is resumed"],
  ["1. Trigger an update availability check to the OTA Server, let the download reach part of its progress and disconnect the head unit",
   "2. Reconnect the head unit to the saved Wi-Fi access point",
   "3. PENDING: DR-SU2 step to read the HTTP request the head unit used to resume the download"],
  ["1. The download is interrupted part way through",
   "2. The head unit is reconnected to the saved Wi-Fi access point",
   "3. PENDING: DR-SU2 observable evidence that the resumed download used an HTTP byte-range request"]),

 tc("SWE1-FOTA-327", IH, "CFTS057-4907682", FN, "P2", "低",
  "**統攝列**（DR-SU3 (i)）＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.249）：其條件由 `328`／`329` 二列定義",
  "The SWMC shall resume the interrupted download when the interruption type satisfies the resume conditions defined in System Requirements 4907683 and 4907684.",
  "Download resumes for the interruption types that allow it",
  [B, WIFI, PKG,
   "PENDING: DR-SU3 confirmation whether this requirement is verified by SWE1-FOTA-328 and SWE1-FOTA-329 together"],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. PENDING: DR-SU3 step to verify this requirement separately from SWE1-FOTA-328 and SWE1-FOTA-329"],
  ["1. The download reaches part of its progress",
   "2. PENDING: DR-SU3 observable evidence separating this requirement from SWE1-FOTA-328 and SWE1-FOTA-329"]),

 tc("SWE1-FOTA-328", IH, "CFTS057-4907683", FN, "P1", "中",
  "**可寫**：內部網路中斷之清除可佈置（斷開再接回），續傳之外部表徵為下載進度再前進",
  "The SWMC shall resume the interrupted download upon receiving a data access resume or tethered phone connection event after the internal network interruption is cleared.",
  "Download progress advances again once the network returns",
  [B, WIFI, PKG],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "3. Disconnect the head unit from the Wi-Fi access point for one minute and then reconnect it",
   "4. Check that the download progress shown on the head unit advances beyond the value it held while the head unit was disconnected"],
  ["1. The download reaches part of its progress",
   "2. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "3. The head unit is disconnected from the Wi-Fi access point and reconnected",
   "4. The recorded screen content shows the download progress advancing beyond the value it held while the head unit was disconnected"]),

 tc("SWE1-FOTA-329", IH, "CFTS057-4907684", FN, "P1", "低",
  "**值未載**（`configured retry count` 之值 037 未給，同 `333`）＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.267）",
  "The SWMC shall attempt to resume the interrupted download according to the configured retry count. If the maximum retry count is reached, the SWMC shall log the failure and abort the OTA update session.",
  "Session aborts once the configured retry count is exhausted",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 value of the configured retry count for resuming an interrupted download",
   "PENDING: DR-SU2 means of reading the logged failure after the retry count is reached"],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. Disconnect the head unit from every network and keep it disconnected",
   "3. PENDING: DR-SU2 step to wait until the configured retry count is reached and read the logged failure"],
  ["1. The download reaches part of its progress",
   "2. The head unit stays disconnected from every network",
   "3. PENDING: DR-SU2 observable evidence that the session was aborted after the configured retry count was reached"]),

 tc("SWE1-FOTA-357", IH, "CFTS057-4907591", FI, "P1", "低",
  "**DR-SU4 族**＋**105 列**：安裝狀態之儲存與其回報皆在服務之間；**中斷本身可注入（斷電）**",
  "The Wifi Update service shall save the installation state when an interruption occurs before successful completion of the installation and shall resume the installation when the interruption condition is cleared.",
  "Installation resumes from its saved state after a power cut",
  [B, WIFI, PKG,
   "The vehicle power supply can be cut and restored at the bench",
   "PENDING: DR-SU4 criterion by which a resumed installation is distinguished from a restarted one"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the installation start",
   "2. Cut the vehicle power supply while the installation is running, then restore it",
   "3. PENDING: DR-SU4 check that the installation resumed from its saved state rather than starting again"],
  ["1. The installation starts on the head unit",
   "2. The vehicle power supply is cut and restored",
   "3. PENDING: DR-SU4 observable evidence that the installation resumed from its saved state"]),

 tc("SWE1-FOTA-359", IH, "CFTS057-4907553", FN, "P1", "中",
  "**可寫**：第二個請求之無效果可觀測（畫面不另起新流程，且原 session 之進度不中斷）",
  "The SWMC shall ignore any request to start a new OTA update flow when an OTA update session is already active and shall ensure that the current session is not interrupted.",
  "A second update request during an active session changes nothing",
  [B, WIFI, PKG],
  ["1. Trigger an update availability check to the OTA Server and let the deployment package download start",
   "2. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "3. Select the Check for Update option on the head unit while the download is running",
   "4. Check that the head unit starts no second update flow and that the download progress keeps advancing"],
  ["1. The deployment package download starts",
   "2. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "3. The Check for Update option is selected while the download is running",
   "4. The recorded screen content shows no second update flow starting and shows the download progress still advancing"]),

 tc("SWE1-FOTA-360", IH, "CFTS057-4907554", FN, "P2", "低",
  "**DR-SU4 族**＋**105 列**；⚠ **與 `324`／`325`／`328` 三列相交** —— 其為「偵測、保存、續傳」之統攝式表述，入 DR-SU3",
  "The SWMC shall detect interruptions occurring during any step of the download process before completion, shall save the current download state, and shall resume the download when the interruption condition is cleared.",
  "Interruption at any download step is detected, saved and resumed",
  [B, WIFI, PKG,
   "PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1-FOTA-324, 325 and 328",
   "PENDING: DR-SU2 means of observing the saved download state"],
  ["1. Trigger an update availability check to the OTA Server and let the download reach part of its progress",
   "2. PENDING: DR-SU2 step to interrupt the download at a step other than the one used for SWE1-FOTA-328 and read the saved download state"],
  ["1. The download reaches part of its progress",
   "2. PENDING: DR-SU2 observable evidence of the saved download state for an interruption at another step"]),

 tc("SWE1-FOTA-363", TC_, "CFTS057-4907569", FN, "P2", "低",
  "**第二型**（DR-SU2(a) 之初始清單）＋**105 列**：與 TC client 之通訊維持於車機無表徵",
  "The WiFiUpdateService shall establish and maintain communication with the TC client for OTA update operations.",
  "Communication with the TC client is established and kept up",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the communication between the WiFiUpdateService and the TC client"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read whether communication with the TC client is established and maintained"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU2 observable evidence that communication with the TC client is established and maintained"]),

 tc("SWE1-FOTA-364", TC_, "CFTS057-4907570", FN, "P2", "低",
  "**第二型**＋**105 列**：`registerCallbackExt(...)` 為程式介面之呼叫，**其參數於系統測層級不可見**",
  "The WiFiUpdateService shall register a callback with the TC client using registerCallbackExt(String applied, ITCApplication cb, String[] topics, String intent) with the topic set to “FOTA” and the intent parameter left empty.",
  "Callback is registered with the FOTA topic and an empty intent",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the callback registration made with the TC client and its parameters"],
  ["1. Restart the head unit and let the update services start",
   "2. PENDING: DR-SU2 step to read the callback registration parameters used with the TC client"],
  ["1. The head unit restarts and the update services start",
   "2. PENDING: DR-SU2 observable evidence that the callback was registered with the topic FOTA and an empty intent"]),

 tc("SWE1-FOTA-365", TC_, "CFTS057-4907559", FN, "P2", "低",
  "**第四型**（推送不可得）；**與 `366`／`367` 三列共用同一句「自 TC client 收受並轉送」** —— 入 DR-SU3",
  "The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the session request to the SWMC for execution.",
  "Session request from the TC client is forwarded for execution",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of making the OTA Server send a session request through the TC client",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-366 and 367"],
  ["1. PENDING: DR-SU2 step to make the OTA Server send a session request through the TC client",
   "2. PENDING: DR-SU2 step to read that the request was forwarded to the SWMC for execution"],
  ["1. PENDING: DR-SU2 observable evidence that a session request arrived through the TC client",
   "2. PENDING: DR-SU2 observable evidence that the request was forwarded to the SWMC for execution"]),

 tc("SWE1-FOTA-366", TC_, "CFTS057-4907559", FN, "P2", "低",
  "**第四型**＋**105 列**；其與 `365` 之別**僅在後半**（SWMC 收到後向伺服器查詢可用更新）",
  "The SWMC shall check the OTA server for an available FOTA update upon receiving a session request from the WiFiUpdateService.",
  "Server is checked for an update after the forwarded request arrives",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of making the OTA Server send a session request through the TC client",
   "PENDING: DR-SU2 means of reading, on the OTA Server side, the availability check made after the request"],
  ["1. PENDING: DR-SU2 step to make the OTA Server send a session request through the TC client",
   "2. PENDING: DR-SU2 step to read the availability check the SWMC made towards the OTA Server"],
  ["1. PENDING: DR-SU2 observable evidence that a session request arrived through the TC client",
   "2. PENDING: DR-SU2 observable evidence of the availability check made towards the OTA Server"]),

 tc("SWE1-FOTA-367", TC_, "CFTS057-4907559", FN, "P2", "低",
  "**第四型**＋**105 列**；其與 `365`／`366` 之別**僅在後半**（無法立即執行時入佇列）—— 三列同源，入 DR-SU3",
  "The SWMC shall queue the received OTA update session request when it cannot be executed immediately.",
  "Session request that cannot run yet is queued",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of making the OTA Server send a session request that cannot be executed immediately",
   "PENDING: DR-SU2 means of observing the queue of received session requests"],
  ["1. PENDING: DR-SU2 step to make the OTA Server send a session request while it cannot be executed",
   "2. PENDING: DR-SU2 step to read the queue of received session requests"],
  ["1. PENDING: DR-SU2 observable evidence that a session request could not be executed immediately",
   "2. PENDING: DR-SU2 observable evidence that the request is held in the queue"]),
]

# `低` 之成因分類（下放包 61 §三 #4）：True = 由 `PENDING` 承載；`anchor` = 錨定成因
LOW_REASONS = {
 "SWE1-FOTA-321": [("`gracefully handle` 無判準（DR-SU4）", True), ("錨為機制 3 之首選（0.220）", "anchor")],
 "SWE1-FOTA-323": [("NIA 不可推送且佇列無表徵", True)],
 "SWE1-FOTA-324": [("保留之部分檔無表徵", True)],
 "SWE1-FOTA-325": [("log 不可讀", True)],
 "SWE1-FOTA-326": [("HTTP 請求需側錄", True)],
 "SWE1-FOTA-327": [("統攝，其條件由他列定義", True), ("錨為機制 3 之首選（0.249）", "anchor")],
 "SWE1-FOTA-329": [("重試次數之值未載", True), ("錨為機制 3 之首選（0.267）", "anchor")],
 "SWE1-FOTA-357": [("續傳與重啟不可區辨（DR-SU4）", True)],
 "SWE1-FOTA-360": [("與 `324`／`325`／`328` 相交", True)],
 "SWE1-FOTA-363": [("通訊維持無表徵", True)],
 "SWE1-FOTA-364": [("介面呼叫之參數不可見", True)],
 "SWE1-FOTA-365": [("推送不可得", True), ("與 `366`／`367` 不可區辨", True)],
 "SWE1-FOTA-366": [("推送不可得", True), ("與 `365` 僅後半不同", True)],
 "SWE1-FOTA-367": [("推送不可得", True), ("與 `365` 僅後半不同", True)],
}
MECH3 = ["SWE1-FOTA-321", "SWE1-FOTA-327", "SWE1-FOTA-329"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T73f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T73f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T73f —— batch 13 之產出（`Interruption Handling` ＋ `Telematics Client`，17 列）\n")
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
    c = Counter(t["conf"] for t in TCS)
    # 退回訊號拆二（下放包 61 §三 #4）
    q_keep, a_keep, excl = [], [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        unborne = [(r, k) for r, k in rs if k is not True]
        if not unborne:
            excl.append((i, t["req"]))
        elif all(k == "anchor" for _, k in unborne):
            a_keep.append((i, t["req"]))
        else:
            q_keep.append((i, t["req"]))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _ in q_keep} | {i for i, _ in a_keep} | set(mid) | set(m3))
    deliverable = [r for r in rows if r[5] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗（**退回訊號拆二**，下放包 61 §三 #4）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}｜可排除之 `低`：{len(excl)} 列")
    print(f"- **品質訊號**（`低` 之未承載理由**非**錨定）：**{len(q_keep)}** 列 "
          + ("**> 3 → 退回**" if len(q_keep) > 3 else "≤ 3 → **不退回**"))
    print(f"- **錨定訊號**（其未承載理由為機制 3 之錨）：**{len(a_keep)}** 列 —— "
          + ("、".join(f"`SU-{i:03d}`" for i, _ in a_keep) or "無")
          + "，**不觸發退回，改以抽驗加重承擔**")
    print(f"- **抽驗組成 = 中 ∪ 未排除之低 ∪ 機制 3 = {len(union)} 列**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
