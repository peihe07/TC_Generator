#!/usr/bin/env python3
"""T64a —— batch 8：`Status Reporting`(7) ＋ `FOTA Overview`(6) = 13 列。

**本批為配額批**（下放包 52 §二 #5(c)：必含 `Status Reporting`，71% 為 105 列）——
其執行順延一批之成因見上繳包 47 §8。

**⚠ 本批揭出 105 分類之第三種結局**：`Status Reporting` 之七列中六列，
其表徵**存在，但在 OTA 伺服器側而非車機側** —— 037 之 `Verification Criteria`
明白寫 `reported to the OTA server`，**而伺服器側之可及性從未確立**。
其既非「無表徵」（第二型），亦非「表徵為他列所轄」（第三型）。

**型別**：
- **伺服器側表徵**（新）：`330`／`331`／`333`／`334`／`339`／`358`
- **第三型**（不可區辨）：`332` —— 其外部後果與 `331` 完全相同
- **第四型**（觸發不可得）：`008`（7 個連續日）、`334`（ECU reflash 失敗之注入）
- **第二型**：`005`（點火循環計數器無外部表徵）
- **可寫**：`003`／`004`／`006`／`007`
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch8"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 110
SR, FO = "Status Reporting", "FOTA Overview"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"
FI = "基礎故障注入 (Fault Injection Lite)"

B = "1. The vehicle is in Body ON mode"
WIFI = "2. The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "3. An update package is staged on the OTA Server for this head unit"
# 伺服器側觀測之佔位（六列共用之請求，措辭逐列不同以免製造不可區辨）
SRV = "PENDING: DR-SU2 means of reading, on the OTA Server side, "


def tc(req, ts, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=ts, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 # ── Status Reporting（配額組）────────────────────────────────────
 tc("SWE1-FOTA-330", SR, "CFTS057-4907686", DT, "P1", "低",
  "伺服器側表徵：037 之 VC 明寫 `reported to the OTA server`，而其可及性未確立",
  "The SWMC shall send the OTA update session result to the OTA server upon completion of the session, regardless of whether the session completes successfully or fails.",
  "Session result reaches the server for a successful and for a failed session",
  [B, WIFI, PKG, "4. " + SRV + "the session result of a completed OTA session"],
  ["1. Trigger an update availability check and let the OTA session complete successfully",
   "2. PENDING: DR-SU2 step to read the session result recorded on the OTA Server for the successful session",
   "3. Repeat the OTA session with the update package removed from the OTA Server so that the session fails",
   "4. PENDING: DR-SU2 step to read the session result recorded on the OTA Server for the failed session"],
  ["1. The OTA session completes successfully on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA Server for the successful session",
   "3. The repeated OTA session fails on the head unit",
   "4. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA Server for the failed session"]),

 tc("SWE1-FOTA-331", SR, "CFTS057-4907687", FN, "P1", "低",
  "伺服器側表徵＋中斷之佈置；其與 `332` 之外部後果相同（見 `332` 之註）",
  "The SWMC shall save the OTA session report when an interruption occurs before the report is successfully sent to and acknowledged by the OTA server, and shall resend the report when the interruption is resolved.",
  "Report saved during the outage arrives at the server after the connection returns",
  [B, WIFI, PKG, "4. " + SRV + "the session reports received for this head unit"],
  ["1. Trigger an update availability check and let the OTA session run to completion",
   "2. Disconnect the head unit from the network before the session report is acknowledged",
   "3. Reconnect the head unit to the saved Wi-Fi access point",
   "4. PENDING: DR-SU2 step to read whether the session report of the interrupted session was received by the OTA Server after the reconnection"],
  ["1. The OTA session runs to completion on the head unit",
   "2. The head unit is disconnected from the network",
   "3. The head unit is reconnected to the saved Wi-Fi access point",
   "4. PENDING: DR-SU2 observable evidence that the session report of the interrupted session was received by the OTA Server after the reconnection"]),

 tc("SWE1-FOTA-332", SR, "CFTS057-4907688", FN, "P2", "低",
  "⚠ **第三型**：其外部後果（中斷解除後報告送達）與 `331` 完全相同；`331` 之條文已含 `shall resend the report when the interruption is resolved`。入 DR-SU3（重複表述）",
  "The SWMC shall resend the saved OTA session report when the cause of the interruption is resolved.",
  "Saved report is resent once the cause of the interruption is gone",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU3 confirmation whether this requirement and SWE1-FOTA-331 are two statements of the same requirement"],
  ["1. Trigger an update availability check and let the OTA session run to completion with the network disconnected before the report is acknowledged",
   "2. PENDING: DR-SU2 step to distinguish the resend verified here from the resend already verified for SWE1-FOTA-331"],
  ["1. The OTA session runs to completion while the head unit is disconnected from the network",
   "2. PENDING: DR-SU2 observable evidence distinguishing this resend from the one verified for SWE1-FOTA-331"]),

 tc("SWE1-FOTA-333", SR, "CFTS057-4907561", FN, "P2", "低",
  "⚠ 037 原文於 `not know` 處**截斷且缺字**（應為 `not known`）—— 逐字保留，登 D-6；另 `configured retry parameter` 之值未載",
  "The SWMC shall retry sending the OTA session report to the OTA server when the interruption and service resumption status are not know",
  "Report is retried while the outage lasts",
  [B, WIFI, PKG, "4. " + SRV + "the retry attempts made for one session report",
   "5. PENDING: DR-SU2 value of the configured retry parameter that governs the number and spacing of the retries"],
  ["1. Trigger an update availability check and let the OTA session run to completion",
   "2. Keep the head unit disconnected from the network so that the session report cannot be acknowledged",
   "3. PENDING: DR-SU2 step to read the retry attempts made for the unacknowledged session report"],
  ["1. The OTA session runs to completion on the head unit",
   "2. The head unit stays disconnected from the network",
   "3. PENDING: DR-SU2 observable evidence of the retry attempts made for the unacknowledged session report"]),

 tc("SWE1-FOTA-334", SR, "CFTS057-4907690", FI, "P1", "低",
  "**第四型**（ECU reflash 失敗之注入手段不可得）＋伺服器側表徵；二者皆掛",
  "The SWMC shall report the reflash failure to the OTA server, including the deployment package status code, ECU fault codes, and CAN communication log associated with the failure.",
  "Failure report carries the package status code, ECU fault codes and CAN log",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU2 means of making an ECU reflash fail during the installation",
   "5. " + SRV + "the failure report received for this head unit"],
  ["1. Trigger an update availability check and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to make the ECU reflash fail during the installation",
   "3. PENDING: DR-SU2 step to read the deployment package status code, the ECU fault codes and the CAN communication log in the failure report received by the OTA Server"],
  ["1. The update is accepted and the installation starts on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the ECU reflash failed during the installation",
   "3. PENDING: DR-SU2 observable evidence of the deployment package status code, the ECU fault codes and the CAN communication log in the failure report received by the OTA Server"]),

 tc("SWE1-FOTA-339", SR, "CFTS057-4907607", FN, "P1", "低",
  "backchannel 之中斷可佈置（斷網），惟其判定核心（狀態碼與版本資訊之送達）在伺服器側",
  "The SWMC shall transmit the OTA update status codes and software version information to the OTA server when the backchannel is available.",
  "Status codes and version information reach the server once the link is back",
  [B, WIFI, PKG, "4. " + SRV + "the update status codes and software version information received for this head unit"],
  ["1. Disconnect the head unit from every network so that no channel to the OTA Server is available",
   "2. Trigger an update availability check on the head unit and let it complete",
   "3. Reconnect the head unit to the saved Wi-Fi access point",
   "4. PENDING: DR-SU2 step to read the update status codes and software version information received by the OTA Server after the reconnection"],
  ["1. No channel to the OTA Server is available on the head unit",
   "2. The update availability check completes on the head unit",
   "3. The head unit is reconnected to the saved Wi-Fi access point",
   "4. PENDING: DR-SU2 observable evidence of the update status codes and software version information received by the OTA Server after the reconnection"]),

 tc("SWE1-FOTA-358", SR, "CFTS057-4907592", FN, "P2", "低",
  "⚠ 與 `330` 相交（皆為「完成後送出最終結果」）—— 其別在本列另含 WifiUpdateservice → SWMC 之內部回報，而該段無外部面。列待裁",
  "The SWMC shall send the final software update result to the OTA server upon completion of the update process.",
  "Final update result reaches the server after the update process ends",
  [B, WIFI, PKG,
   "4. " + SRV + "the final software update result received for this head unit",
   "5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-330"],
  ["1. Trigger an update availability check, accept the update and let the update process finish on the head unit",
   "2. PENDING: DR-SU2 step to read the final software update result received by the OTA Server for the finished update process"],
  ["1. The update process finishes on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the final software update result received by the OTA Server for the finished update process"]),

 # ── FOTA Overview（門檻密度最高之組）──────────────────────────────
 tc("SWE1-FOTA-003", FO, "CFTS057-4907817", BV, "P1", "中",
  "**門檻列**（`5 consecutive minutes` 逐字取自 037）；其與 `006` 之別在**後果**：本列為「至下次 Ignition ON 前不再下載」",
  "If no FOTA data is received for 5 consecutive minutes while the Wi-Fi signal strength remains above the configured threshold, the WiFi Update Service shall terminate the active FOTA download sessions until the next Ignition ON event.",
  "Download does not resume before the next Ignition ON after a five-minute stall",
  [B, WIFI, PKG,
   "4. The saved Wi-Fi access point is placed close to the head unit so that the head unit shows it at full signal strength"],
  ["1. Trigger an update availability check and let the FOTA package download start over Wi-Fi",
   "2. Block the access point from reaching the internet while leaving the head unit connected to it at full signal strength",
   "3. Wait for 10 minutes without switching the ignition off",
   "4. Restore the internet access of the access point and wait a further 5 minutes",
   "5. Check that the download progress shown on the head unit does not advance after the internet access is restored and before the next Ignition ON event"],
  ["1. The FOTA package download over Wi-Fi starts",
   "2. The access point cannot reach the internet and the head unit stays connected to it at full signal strength",
   "3. Ten minutes pass with the ignition on",
   "4. The internet access of the access point is restored",
   "5. The download progress shown on the head unit does not advance after the internet access is restored and before the next Ignition ON event"]),

 tc("SWE1-FOTA-004", FO, "CFTS057-4907818", BV, "P1", "低",
  "**門檻列**（`7 ignition cycles` 逐字取自 037）＋⚠ 錨為機制 3 攔下之首選（0.261）",
  "If the FOTA package download is not completed within 7 ignition cycles, the WiFi Update Service shall request SW Update HMI to display a pop-up notification prompting the user to connect to a Wi-Fi network for software download.",
  "Pop-up prompting a Wi-Fi connection appears after seven incomplete ignition cycles",
  [B, PKG,
   "2. A saved Wi-Fi access point without internet access is the only Wi-Fi network in range",
   "4. The FOTA download retry counter of the head unit has been cleared by a completed download"],
  ["1. Trigger an update availability check so that a FOTA package download is pending",
   "2. Switch the ignition off and on again, leaving the download unable to complete, and repeat until seven ignition cycles have passed",
   "3. Check that the head unit displays a pop-up notification prompting the user to connect to a Wi-Fi network for software download"],
  ["1. A FOTA package download is pending on the head unit",
   "2. Seven ignition cycles pass without the FOTA package download completing",
   "3. The head unit displays a pop-up notification prompting the user to connect to a Wi-Fi network for software download"]),

 tc("SWE1-FOTA-005", FO, "CFTS057-4907819", FN, "P2", "低",
  "**第二型**＋**105 列**：計數器無外部表徵，其重置之唯一外部後果（第 7 循環後之彈窗不出現）屬 `004` 之驗證單元",
  "When Wi-Fi connectivity is established and FOTA package data is actively received, the WiFi Update Service shall reset the ignition cycle counter.",
  "Ignition cycle counter is reset while FOTA data is being received",
  [B, WIFI, PKG,
   "4. PENDING: DR-SU2 means of reading the ignition cycle counter associated with FOTA download retry attempts"],
  ["1. Trigger an update availability check and let the FOTA package download start over Wi-Fi",
   "2. PENDING: DR-SU2 step to read the ignition cycle counter while FOTA package data is being received"],
  ["1. The FOTA package download over Wi-Fi starts and FOTA package data is being received",
   "2. PENDING: DR-SU2 observable evidence of the ignition cycle counter while FOTA package data is being received"]),

 tc("SWE1-FOTA-006", FO, "CFTS057-4907817", BV, "P1", "中",
  "**門檻列**（同 `003` 之 5 分鐘）；其與 `003` 之別在**後果**：本列為 Host Mode 之切回，外部表徵為熱點恢復可用",
  "If no FOTA data is received for 5 consecutive minutes while the Wi-Fi signal strength remains above the configured threshold, the WiFi Update Service shall terminate the active download session for the current ignition cycle and request Connectivity Manager to transition the M-CPU platform to Host Mode.",
  "Hotspot becomes available again after a five-minute stall in the same ignition cycle",
  [B, WIFI, PKG,
   "4. The head unit Wi-Fi hotspot is not available to a companion device while the download is active"],
  ["1. Trigger an update availability check and let the FOTA package download start over Wi-Fi",
   "2. Block the access point from reaching the internet while leaving the head unit connected to it at full signal strength",
   "3. Wait for 10 minutes without switching the ignition off",
   "4. Check that the head unit Wi-Fi hotspot is available to the companion device again within the same ignition cycle"],
  ["1. The FOTA package download over Wi-Fi starts and the hotspot is not available to the companion device",
   "2. The access point cannot reach the internet and the head unit stays connected to it at full signal strength",
   "3. Ten minutes pass with the ignition on",
   "4. The head unit Wi-Fi hotspot is available to the companion device again within the same ignition cycle"]),

 tc("SWE1-FOTA-007", FO, "CFTS057-4907821", DT, "P1", "中",
  "⚠ 與 `056`（batch 7）相交：`056` 驗「無已存網路」之支，**本列取另一支（下載嘗試次數 ≥ 7）**，故二列之判定核心不同",
  "If: the software package classification is Non-Critical, IgnitionStatus = OFF, and either no previously configured Wi-Fi network is available or the FOTA package download attempt count is greater than or equal to 7, the WiFi Update Service shall request SW Update HMI to display the Wi-Fi pop-up notification.",
  "Pop-up appears at IGN_OFF on the seventh failed attempt even though a network is saved",
  [B, "2. A Non-Critical update package is staged on the OTA Server for this head unit",
   "3. A saved Wi-Fi access point without internet access is in range of the head unit"],
  ["1. Trigger an update availability check and let the FOTA package download attempt fail on the saved access point",
   "2. Repeat the failing download attempt until seven attempts have been made",
   "3. Record the head unit screen content as continuous video capture until the head unit screen turns off",
   "4. Switch the vehicle ignition off",
   "5. Check that the head unit displays the Wi-Fi pop-up notification after the seventh failed attempt while a Wi-Fi network is saved"],
  ["1. The FOTA package download attempt fails on the saved access point",
   "2. Seven failed download attempts have been made",
   "3. The head unit screen content until the head unit screen turns off is recorded as continuous video capture",
   "4. The vehicle ignition is switched off",
   "5. The recorded screen content shows the Wi-Fi pop-up notification after the seventh failed attempt while a Wi-Fi network is saved"]),

 tc("SWE1-FOTA-008", FO, "CFTS057-4907822", NEG, "P1", "低",
  "**第四型**（`7 consecutive days` 之等待不可觸發，同 `028` 之一週）＋⚠ 錨為機制 3 攔下之首選（0.247）＋**105 列**",
  "If Wi-Fi connection establishment is unsuccessful or cannot download FOTA package over Wi-Fi for 7 consecutive days, the WiFi Update Service shall request SWMC to continue the FOTA package download using the embedded modem.",
  "Download continues over the embedded modem after seven days without Wi-Fi",
  [B, PKG,
   "2. A saved Wi-Fi access point without internet access is the only Wi-Fi network in range",
   "4. PENDING: DR-SU2 means of reaching the state in which the FOTA package could not be downloaded over Wi-Fi for 7 consecutive days"],
  ["1. Trigger an update availability check so that a FOTA package download is pending",
   "2. PENDING: DR-SU2 step to reach the state in which the FOTA package could not be downloaded over Wi-Fi for 7 consecutive days",
   "3. Check that the download progress shown on the head unit advances while no Wi-Fi network provides internet access"],
  ["1. A FOTA package download is pending on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the FOTA package could not be downloaded over Wi-Fi for 7 consecutive days",
   "3. The download progress shown on the head unit advances while no Wi-Fi network provides internet access"]),
]

LOW_REASONS = {
 "SWE1-FOTA-330": [("表徵在伺服器側，其可及性未確立", True)],
 "SWE1-FOTA-331": [("表徵在伺服器側，其可及性未確立", True)],
 "SWE1-FOTA-332": [("與 `331` 不可區辨", True)],
 "SWE1-FOTA-333": [("表徵在伺服器側", True), ("重試參數之值未載", True),
                   ("037 原文截斷（`not know`）", False)],
 "SWE1-FOTA-334": [("ECU reflash 失敗不可注入", True), ("表徵在伺服器側", True)],
 "SWE1-FOTA-339": [("表徵在伺服器側", True)],
 "SWE1-FOTA-358": [("表徵在伺服器側", True), ("與 `330` 之別未確認", True)],
 "SWE1-FOTA-004": [("錨為機制 3 攔下之首選（0.261），未經 GT 驗證", False)],
 "SWE1-FOTA-005": [("計數器無外部表徵", True)],
 "SWE1-FOTA-008": [("7 個連續日不可觸發", True),
                   ("錨為機制 3 攔下之首選（0.247），未經 GT 驗證", False)],
}
MECH3 = ["SWE1-FOTA-004", "SWE1-FOTA-008"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T64a：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T64a：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T64a —— batch 8 之產出（**配額批**：`Status Reporting` ＋ `FOTA Overview`）\n")
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
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _, _ in keep} | set(mid) | set(m3))
    deliverable = [r for r in rows if r[5] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗（含下放包 54 §二 #4 之加重）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- 可排除之 `低`：{len(excl)} 列 —— "
          + ("、".join(f"`SU-{i:03d}`" for i, _, _ in excl) or "**無**"))
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— 未由 `PENDING` 承載者："
              + "、".join(f"**{r}**" for r in un))
    print(f"- 機制 3 攔下：" + "、".join(f"`SU-{i:03d}`" for i in m3))
    print(f"- **抽驗組成 = 低 ∪ 中 ∪ 機制 3 = {len(union)} 列** —— "
          + "、".join(f"`SU-{i:03d}`" for i in union))
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
