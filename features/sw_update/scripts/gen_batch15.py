#!/usr/bin/env python3
"""T75f —— batch 15：`Client Architecture` 其餘 19 列之前 12 列（下放包 63 §四）。

**拆分依 037 之列序**（下放包 63 §三 #4 之常規），本批為第 17–28 列；
其餘 7 列隨 batch 16（與 `Update Policy` 5 ＋ `Configurable Parameters` 2 併批）。

**⚠ 本批之重複表述密度為至今最高**：
- `255`／`256` —— **其錨為同一物件 `4907332`**（同 `207`／`208` 之形）
- `260`／`268` —— 皆為 OMA-DM 之平台無關通訊支援
- `264`／`265` —— **「依 metadata／ECU 參照選定安裝器」之第五、六次**
  （前四次：`169`／`371`／`209`／`253`）

**型別**：
- **DR-SU6（架構／可移植性）**：`257`（獨立於 OS 與 flash driver）、`267`（RBUA 之可移植性）
- **第二型**：其餘各列
- **可寫**：無 —— **本批 12 列全部掛 `PENDING`**
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch15"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 213
TS = "Client Architecture"
FN = "功能測試 (Functional based ; no specific technique)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"


def tc(req, spec, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=FN, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, spec, prio, note, item, paren, what, extra=()):
    """第二型之共通形態 —— **其 Final Step 逐列帶入 `what`，不共用措辭**（B-24）。"""
    return tc(req, spec, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server and let the OTA session run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The OTA session runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


TCS = [
 internal("SWE1-FOTA-254", "CFTS057-4907301", "P2",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.257）：平台 socket 介面之連線建立與其通知皆在服務內部",
  "WiFiUpdateService shall establish network connectivity through the platform socket interface and notify SWMC when the network is available.",
  "Network availability is signalled to the SWMC",
  "the network availability notification sent from the WiFiUpdateService to the SWMC"),

 internal("SWE1-FOTA-255", "CFTS057-4907332", "P2",
  "**第二型**＋**105 列**；**與 `256` 之錨為同一物件 `4907332`** —— 二列同源之機器證據（同 `207`／`208`）",
  "SWMC shall reliably download the deployment package using the URL obtained from the Download Descriptor.",
  "Package is downloaded from the URL carried by the Download Descriptor",
  "the URL the SWMC used to download the deployment package",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-256",)),

 internal("SWE1-FOTA-256", "CFTS057-4907332", "P3",
  "**第二型**＋**105 列**；**與 `255` 同錨同義**，其差僅在「讀取並抽出 URL」一段之明寫",
  "SWMC shall read the Download Descriptor, extract the deployment package URL, and download the deployment package from the specified URL.",
  "Download Descriptor is read and its URL used for the download",
  "the Download Descriptor the SWMC read and the URL it extracted",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-255",)),

 tc("SWE1-FOTA-257", "CFTS057-4907334", "P3", "低",
  "**DR-SU6**：`independent of the operating system and flash driver` 為架構命題 —— 單一台架之單一 OS 上不可能被否證",
  "WiFiUpdateService shall store the deployment package on the host module through the abstract file system/flash interface, independent of the operating system and flash driver.",
  "Package storage goes through the abstract interface, not the OS or driver",
  [B, WIFI, PKG,
   "PENDING: DR-SU6 criterion by which independence from the operating system and flash driver is judged on a single bench"],
  ["1. Trigger an update availability check to the OTA Server and let the deployment package be stored on the head unit",
   "2. PENDING: DR-SU6 step to establish that the storage went through the abstract interface"],
  ["1. The deployment package is stored on the head unit",
   "2. PENDING: DR-SU6 observable evidence that the storage was independent of the operating system and flash driver"]),

 internal("SWE1-FOTA-258", "CFTS057-4907335", "P2",
  "**第二型**＋**105 列**：RBUA 之呼叫與其與 bootloader 之介接皆在服務內部",
  "USBUpdateService/WiFiUpdateService shall invoke the Redbend Update Agent (RBUA) to perform the ECU firmware update.",
  "RBUA is invoked to carry out the ECU firmware update",
  "the invocation of the Redbend Update Agent for the ECU firmware update"),

 internal("SWE1-FOTA-260", "CFTS057-4907504", "P2",
  "**第二型**＋**105 列**；**與 `268` 重複**（皆為 OMA-DM 之通訊支援），入 DR-SU3",
  "SWMC shall establish and manage communication with the OTA Server using the OMA-DM protocol.",
  "Communication with the server runs over OMA-DM",
  "the protocol the SWMC used to communicate with the OTA Server",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-268",)),

 internal("SWE1-FOTA-261", "CFTS057-4907315", "P2",
  "**第二型**＋**105 列**：Download Descriptor 之處理於車機無表徵；其專有協定分支另需組態",
  "When a proprietary communication protocol is used, theSWMC shall support processing of an equivalent Download Descriptor containing the required deployment package information.",
  "An equivalent Download Descriptor is processed for a proprietary protocol",
  "the Download Descriptor processed when a proprietary protocol is configured",
  ("PENDING: DR-SU2 means of configuring a proprietary communication protocol",)),

 internal("SWE1-FOTA-262", "CFTS057-4907317", "P2",
  "**第二型**＋**105 列**：車輛屬性之取得路徑（CarPropertyManager → VHAL）為內部呼叫鏈",
  "WiFiUpdateService shall retrieve the required vehicle properties through CarPropertyManager.",
  "Vehicle properties are retrieved through CarPropertyManager",
  "the vehicle properties the WiFiUpdateService retrieved through CarPropertyManager"),

 internal("SWE1-FOTA-264", "CFTS057-4907896", "P2",
  "⚠ **「選定安裝器」之第五次**（`169`／`371`／`209`／`253` 之後）＋錨為機制 3 攔下之首選（0.194）",
  "WiFiUpdateService shall invoke the appropriate installer based on the installation method provided by SWMC.",
  "Installer is invoked according to the installation method",
  "the installer invoked for the installation method provided by the SWMC",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-169, 371, 209 and 253",)),

 internal("SWE1-FOTA-265", "CFTS057-4907343", "P3",
  "⚠ **「選定安裝器」之第六次**，其差在以 ECU 參照 ID（料號／CAN 位址）為關聯依據",
  "WiFiUpdateService/USBUpdateService shall retrieve or use the configured ECU reference IDs (such as part number, CAN address, or equivalent identifiers) to associate the deployment package update file with the appropriate installer and invoke the selected installer.",
  "ECU reference IDs associate the package with its installer",
  "the ECU reference IDs used to associate the update file with its installer"),

 tc("SWE1-FOTA-267", "CFTS057-4907304", "P3", "低",
  "**DR-SU6**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.188，與 `198` 並列最低）：`must be portable with the android operating system` 為可移植性命題（同 `212`）",
  "RBUA must be portable with the android operating system.",
  "RBUA is portable with the Android operating system",
  [B, WIFI, PKG,
   "PENDING: DR-SU6 criterion by which portability with the Android operating system is judged on a single bench"],
  ["1. PENDING: DR-SU6 step to establish that the Redbend Update Agent is portable with the Android operating system"],
  ["1. PENDING: DR-SU6 observable evidence that the Redbend Update Agent is portable with the Android operating system"]),

 internal("SWE1-FOTA-268", "CFTS057-4907347", "P3",
  "**第二型**；**與 `260` 重複**，其差在本列明寫「平台無關」與專有協定之分支",
  "SWMC shall communicate with the OTA Server using platform-independent OMA-DM compliant protocols.",
  "Server communication uses platform-independent OMA-DM protocols",
  "the OMA-DM protocol stack the SWMC used towards the OTA Server",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-260",)),
]

LOW_REASONS = {
 "SWE1-FOTA-254": [("socket 介面無外部面", True), ("錨為機制 3 之首選（0.257）", "anchor")],
 "SWE1-FOTA-255": [("下載之 URL 無外部面", True), ("與 `256` 同錨同義", True)],
 "SWE1-FOTA-256": [("同上", True), ("與 `255` 同錨同義", True)],
 "SWE1-FOTA-257": [("架構命題不可否證（DR-SU6）", True)],
 "SWE1-FOTA-258": [("RBUA 之呼叫無外部面", True)],
 "SWE1-FOTA-260": [("協定需側錄", True), ("與 `268` 重複", True)],
 "SWE1-FOTA-261": [("DD 處理無外部面", True)],
 "SWE1-FOTA-262": [("屬性取得鏈無外部面", True)],
 "SWE1-FOTA-264": [("安裝器之選定無外部面", True), ("與四列重複", True),
                   ("錨為機制 3 之首選（0.194）", "anchor")],
 "SWE1-FOTA-265": [("ECU 參照 ID 無外部面", True)],
 "SWE1-FOTA-267": [("可移植性不可否證（DR-SU6）", True), ("錨為機制 3 之首選（0.188）", "anchor")],
 "SWE1-FOTA-268": [("協定需側錄", True), ("與 `260` 重複", True)],
}
MECH3 = ["SWE1-FOTA-254", "SWE1-FOTA-264", "SWE1-FOTA-267"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T75f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T75f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T75f —— batch 15 之產出（`Client Architecture` 第 17–28 列）\n")
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
    q, a, excl = [], [], []
    for i, t in enumerate(TCS, START_N):
        rs = LOW_REASONS.get(t["req"], [])
        un = [(r, k) for r, k in rs if k is not True]
        (excl if not un else (a if all(k == "anchor" for _, k in un) else q)).append((i, t["req"]))
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {sum(1 for r in rows if r[4]==0)}**")
    print(f"- **品質訊號 {len(q)}** ≤ 3 → 不退回｜**錨定訊號 {len(a)}** 列全數納入抽驗"
          f"｜可排除之 `低` {len(excl)} 列")
    print(f"- 機制 3 攔下：" + "、".join(f"`SU-{i:03d}`" for i in m3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
