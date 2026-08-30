#!/usr/bin/env python3
"""T74d —— batch 14：`Client Architecture` 之前 16 列（下放包 62 §六）。

**下窗（batch 14–16）目標 33%；本批 105 比率見產出。**

**⚠ 本批為首次「拆組起草」** —— `Client Architecture` 共 35 列，逾批量上限 20，
故取其**列序之前 16 列**，其餘 19 列隨後續二批。**拆法為列序，不依內容挑選**
（免得又一次「挑容易的」）。

**型別**：
- **可寫**：`203`／`213`（HMI 之顯示）
- **DR-SU6（能力／架構型）**：`195`（不得依賴特定匯流排實作）、`212`（HMI 之可移植性）、
  `198`（`no unintended DTCs` 之全稱否定，其 `unintended` 亦無界）
- **第二型**：`199`／`201`／`206`／`207`／`208`／`252`
- **重複表述**（入 DR-SU3）：`209`（與 `169`／`371` 第三次）、`210`（與 `372`）、
  `253`（與 `209`）、`207`／`208`（同一資訊之二來源）、`205`／`211`（統攝）
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch14"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 197
TS = "Client Architecture"

FN = "功能測試 (Functional based ; no specific technique)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"


def tc(req, spec, prio, conf, note, item, paren, pre, proc, er, dm=FN):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-195", "CFTS057-4907386", "P3", "低",
  "**DR-SU6**：`shall not directly depend on …` 為**全稱否定之架構命題** —— 任一次成功之更新皆不能證實它",
  "The SWMC and WiFi Update Service shall not directly depend on specific physical bus communication stack implementations such as CAN, Ethernet, or LIN.",
  "OTA client does not depend on a specific bus stack",
  [B, WIFI,
   "PENDING: DR-SU6 criterion by which the absence of a dependency on a specific bus stack is judged in one bench run"],
  ["1. PENDING: DR-SU6 step to establish that the OTA client does not depend on a specific physical bus stack"],
  ["1. PENDING: DR-SU6 observable evidence that the OTA client does not depend on a specific physical bus stack"]),

 tc("SWE1-FOTA-198", "CFTS057-4907368", "P1", "低",
  "**DR-SU6**＋⚠ 錨為機制 3 攔下之首選（0.188）：`no unintended DTCs` 為全稱否定，**且 `unintended` 之界未載**",
  "The SWMC and WiFi Update Service shall coordinate OTA reflash sequencing with Update Engine, SW Updater Manager, and SW Updater Service such that no unintended diagnostic trouble codes (DTCs) are triggered during normal OTA reflash execution.",
  "No unintended DTC is stored by a normal reflash",
  [B, WIFI, PKG,
   "The diagnostic trouble code memory of the vehicle is cleared before the update",
   "PENDING: DR-SU6 list of the diagnostic trouble codes that count as intended during a reflash"],
  ["1. Read the stored diagnostic trouble codes and record them as DTC_before",
   "2. Trigger an update availability check to the OTA Server, accept the update and let the reflash complete",
   "3. Read the stored diagnostic trouble codes again and record them as DTC_after",
   "4. PENDING: DR-SU6 check that DTC_after contains no code outside the list of codes that count as intended"],
  ["1. DTC_before is recorded",
   "2. The reflash completes on the head unit",
   "3. DTC_after is recorded",
   "4. PENDING: DR-SU6 observable evidence that DTC_after contains no unintended code"]),

 tc("SWE1-FOTA-199", "CFTS057-4907393", "P2", "低",
  "**第二型**：Tester Present 為匯流排上之週期訊息，**其觀測需匯流排側錄**（同 `279`／`326`）",
  "The ROV Update Service shall transmit periodic diagnostic Tester Present messages to external ECUs through the vehicle communication interface during any active reflash operation to maintain the diagnostic programming session.",
  "Tester Present messages run while an external ECU is being reflashed",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of recording the diagnostic messages on the vehicle communication interface"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let an external ECU reflash start",
   "2. PENDING: DR-SU2 step to read the diagnostic messages sent to the external ECU during the reflash"],
  ["1. An external ECU reflash starts",
   "2. PENDING: DR-SU2 observable evidence of periodic Tester Present messages during the reflash"]),

 tc("SWE1-FOTA-201", "CFTS057-4907340", "P3", "低",
  "**第二型**：分散式元件間之介面於車機無表徵；其後半（獨立於主機平台）另為架構命題",
  "The SWMC shall exchange OTA session information, deployment package status, workflow events, and control messages through standardized communication interfaces between distributed OTA client components.",
  "Session information and events pass through the defined interfaces",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing the messages exchanged between distributed OTA client components"],
  ["1. Trigger an update availability check to the OTA Server and let an OTA session run",
   "2. PENDING: DR-SU2 step to read the session information and workflow events exchanged between the components"],
  ["1. An OTA session runs on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the messages exchanged between the components"]),

 tc("SWE1-FOTA-203", "CFTS057-4907316", "P1", "中",
  "**可寫**：判定核心取畫面上之二項資訊（套件文字說明與更新大小）",
  "The SW Update HMI shall display available update information including package text description and update size.",
  "Update screen shows the package description and its size",
  [B, WIFI, PKG],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server",
   "3. Check that the head unit shows a text description of the package and the size of the update"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The update availability check completes and an update is reported as available",
   "3. The recorded screen content shows a text description of the package and the size of the update"]),

 tc("SWE1-FOTA-205", "CFTS057-4907320", "P2", "低",
  "**統攝列**＋**105 列**：其所列之各信號（點火、電壓、車速、電流）之個別判定分屬 `069`／`019` 等列，入 DR-SU3",
  "The WiFi Update Service shall evaluate the received diagnostic signals against the configured update preconditions and shall permit software update download or installation only when all required preconditions are satisfied.",
  "Update proceeds only when every configured precondition holds",
  [B, WIFI, PKG,
   "PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1-FOTA-069, 019 and the other precondition rows",
   "PENDING: DR-SU2 list of the vehicle-specific preconditions and their configured values"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU3 step to verify this requirement separately from the individual precondition rows"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU3 observable evidence separating this requirement from the individual precondition rows"]),

 tc("SWE1-FOTA-206", "CFTS057-4907321", "P2", "低",
  "**第二型**＋**105 列**：VIN 之讀取與其用於 workflow 皆在服務內部",
  "The WiFi Update Service shall read the $VIN_DATA$ vehicle property through CarProperty Manager and shall extract the vehicle identification number (VIN) for OTA workflow",
  "VIN is read from the vehicle property for the OTA workflow",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the VIN the WiFi Update Service read for the OTA workflow"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read the VIN the service used for the OTA workflow"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU2 observable evidence of the VIN used for the OTA workflow"]),

 tc("SWE1-FOTA-207", "CFTS057-4907322", "P2", "低",
  "**第二型**＋**105 列**；**與 `208` 為同一資訊之二來源**（`VC_VEH_BRAND` vs proxi 參數）—— 入 DR-SU3",
  "The WiFi Update Service shall read the VC_VEH_BRAND vehicle property through CarProperty Manager and shall provide the vehicle brand information to SWMC for OTA server registration, campaign eligibility checks, and update session requests.",
  "Vehicle brand from the VC_VEH_BRAND property reaches the SWMC",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the vehicle brand the service provided to the SWMC",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-208"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the VC_VEH_BRAND property"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU2 observable evidence of the brand value taken from the VC_VEH_BRAND property"]),

 tc("SWE1-FOTA-208", "CFTS057-4907322", "P3", "低",
  "**第二型**＋**105 列**；**其錨與 `207` 同一物件（`4907322`）** —— 二列同源之機器證據",
  "The WiFi Update Service shall read the vehicle brand information from the <Brand_Configuration_2> proxi parameter through CarProperty Manager and shall provide the retrieved brand value to SWMC for OTA workflow",
  "Vehicle brand from the proxi parameter reaches the SWMC",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the brand value the service read from the proxi parameter",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-207"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the proxi parameter"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU2 observable evidence of the brand value taken from the proxi parameter"]),

 tc("SWE1-FOTA-209", "CFTS057-4907590", "P2", "低",
  "⚠ **與 `169`（batch 11）／`371`（batch 12）第三次重複** —— 三列皆為「依 metadata 選定並呼叫安裝器」；⚠ 錨為機制 3 攔下之首選（0.219）",
  "The WiFi Update Service shall route MCPU firmware packages to the Update Engine for firmware installation processing.",
  "MCPU firmware packages are routed to the Update Engine",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of reading which installer each component package was routed to",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-169 and 371"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read the installer that received the MCPU firmware package"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence distinguishing this routing from the one verified for SWE1-FOTA-169 and 371"]),

 tc("SWE1-FOTA-210", "CFTS057-4907327", "P2", "低",
  "**105 列**＋⚠ 錨為機制 3 攔下之首選（0.264）；**與 `372`（batch 12）重複** —— 皆為相依序之控制",
  "The WiFi Update Service shall prevent installation of dependent components until prerequisite component installation is successfully completed based on installer status feedback.",
  "Dependent components wait for their prerequisites",
  [B, WIFI, "An update package containing at least two dependent components is staged on the OTA Server",
   "PENDING: DR-SU2 means of reading the installation order and the installer status feedback",
   "PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-372"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read whether a dependent component waited for its prerequisite"],
  ["1. The update is accepted and the installation runs on the head unit",
   "2. PENDING: DR-SU2 observable evidence that a dependent component waited for its prerequisite"]),

 tc("SWE1-FOTA-211", "CFTS057-4907333", "P2", "低",
  "**統攝列**：其所列之各事件（狀態、進度、提示、完成結果、錯誤）之個別畫面分屬各 HMI 列，入 DR-SU3",
  "The SW Update HMI shall receive update status, progress, prompts, completion results, and error events from the WiFi Update Service and shall present the appropriate user interface flow for OTA update operations when HMI is available.",
  "HMI presents the flow for each kind of OTA event",
  [B, WIFI, PKG,
   "PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the individual HMI rows"],
  ["1. Trigger an update availability check to the OTA Server and let an OTA session run to completion",
   "2. PENDING: DR-SU3 step to verify this requirement separately from the individual HMI rows"],
  ["1. An OTA session runs to completion on the head unit",
   "2. PENDING: DR-SU3 observable evidence separating this requirement from the individual HMI rows"]),

 tc("SWE1-FOTA-212", "CFTS057-4907330", "P3", "低",
  "**DR-SU6**：可移植性為架構屬性，**於單一台架之單一 HMI 框架上不可能被否證**",
  "The SW Update HMI shall be implemented using an architecture that supports portability across multiple HMI frameworks and operating systems.",
  "HMI architecture is portable across frameworks and operating systems",
  [B, WIFI,
   "PENDING: DR-SU6 criterion by which portability across frameworks is judged on a single bench"],
  ["1. PENDING: DR-SU6 step to establish that the HMI architecture supports portability across frameworks and operating systems"],
  ["1. PENDING: DR-SU6 observable evidence that the HMI architecture supports portability"]),

 tc("SWE1-FOTA-213", "CFTS057-4907333", "P1", "中",
  "**可寫**：下載進度之顯示可觀測；與 `203` 之別在**所顯示之物**（可用更新之資訊 vs 下載進度）",
  "The SW Update HMI shall display the current OTA package download progress, including percentage or status indication, when the HMI is available.",
  "Download progress is shown while the package downloads",
  [B, WIFI, PKG],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server and accept the download on the head unit",
   "3. Check that the head unit shows the download progress as a percentage or as a status indication while the package downloads"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The download is accepted and starts on the head unit",
   "3. The recorded screen content shows the download progress as a percentage or as a status indication"]),

 tc("SWE1-FOTA-252", "CFTS057-4907323", "P2", "低",
  "**第二型**＋**105 列**：OMA-DM SCOMO 之合規性於車機無表徵，**其觀測需網路側錄**（同 `279`）",
  "SWMC shall implement the OMA-DM SCOMO specification to support interoperability with standard-based OTA Servers.",
  "SCOMO specification is used towards the server",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of recording the protocol exchange between the head unit and the OTA Server"],
  ["1. Trigger an update availability check to the OTA Server",
   "2. PENDING: DR-SU2 step to read the protocol exchange between the head unit and the OTA Server"],
  ["1. The update availability check completes",
   "2. PENDING: DR-SU2 observable evidence that the exchange follows the OMA-DM SCOMO specification"]),

 tc("SWE1-FOTA-253", "CFTS057-4907590", "P2", "低",
  "⚠ 錨為機制 3 攔下之首選（0.260）；**其後半與 `209`／`169`／`371` 同一句**（依更新型別呼叫安裝器）—— 入 DR-SU3",
  "SWMC shall support the management of multiple software components using the SCOMO specification.",
  "Multiple software components are managed through SCOMO",
  [B, WIFI, "An update package containing at least two software components is staged on the OTA Server",
   "PENDING: DR-SU2 means of reading the SCOMO management of the individual components"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read how the individual components were managed through SCOMO"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the SCOMO management of the individual components"]),
]

LOW_REASONS = {
 "SWE1-FOTA-195": [("架構命題不可由單次執行否證（DR-SU6）", True)],
 "SWE1-FOTA-198": [("`unintended` 之界未載（DR-SU6）", True), ("錨為機制 3 之首選（0.188）", "anchor")],
 "SWE1-FOTA-199": [("匯流排訊息需側錄", True)],
 "SWE1-FOTA-201": [("元件間介面無車機表徵", True)],
 "SWE1-FOTA-205": [("統攝，其各信號分屬他列", True)],
 "SWE1-FOTA-206": [("VIN 之使用無外部面", True)],
 "SWE1-FOTA-207": [("品牌值無外部面", True), ("與 `208` 同源", True)],
 "SWE1-FOTA-208": [("品牌值無外部面", True), ("與 `207` 同源", True)],
 "SWE1-FOTA-209": [("路由無外部面", True), ("與 `169`／`371` 重複", True),
                   ("錨為機制 3 之首選（0.219）", "anchor")],
 "SWE1-FOTA-210": [("安裝順序無外部面", True), ("錨為機制 3 之首選（0.264）", "anchor")],
 "SWE1-FOTA-211": [("統攝，其各畫面分屬他列", True)],
 "SWE1-FOTA-212": [("可移植性於單一台架不可否證（DR-SU6）", True)],
 "SWE1-FOTA-252": [("協定合規需側錄", True)],
 "SWE1-FOTA-253": [("SCOMO 管理無外部面", True), ("錨為機制 3 之首選（0.260）", "anchor")],
}
MECH3 = ["SWE1-FOTA-198", "SWE1-FOTA-209", "SWE1-FOTA-210", "SWE1-FOTA-253"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T74d：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T74d：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T74d —— batch 14 之產出（`Client Architecture` 前 16 列，**首次拆組**）\n")
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
    q_keep, a_keep, excl = [], [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        un = [(r, k) for r, k in rs if k is not True]
        if not un:
            excl.append(i)
        elif all(k == "anchor" for _, k in un):
            a_keep.append((i, t["req"]))
        else:
            q_keep.append((i, t["req"]))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _ in q_keep} | {i for i, _ in a_keep} | set(mid) | set(m3))
    deliverable = [r for r in rows if r[4] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗（訊號拆二）\n- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}"
          f"｜可排除之 `低`：{len(excl)} 列")
    print(f"- **品質訊號**：**{len(q_keep)}** 列 "
          + ("**> 3 → 退回**" if len(q_keep) > 3 else "≤ 3 → **不退回**"))
    print(f"- **錨定訊號**：**{len(a_keep)}** 列 —— "
          + ("、".join(f"`SU-{i:03d}`" for i, _ in a_keep) or "無") + "，全數納入抽驗")
    print(f"- **抽驗組成 = {len(union)} 列**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
