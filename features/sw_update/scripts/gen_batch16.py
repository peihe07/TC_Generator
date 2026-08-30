#!/usr/bin/env python3
"""T76f —— batch 16：`Client Architecture` 末 7 ＋ `Update Policy` 5 ＋ `Configurable Parameters` 2 = 14 列。

**下窗（14–16）第 3 批。`Wi-Fi Download` 之 `057` 仍不起草**
（其 30 分鐘之起算點於 037 與 `4908702` 不一致，下放包 54 §二 #1）。

**⚠ 本批使三個組全部收尾**：`Client Architecture`（35 列跨三批）、
`Update Policy`（其五列自下放包 49／50 起列待裁，本批依已裁之判準起草）、
`Configurable Parameters`。

**型別**：
- **可寫**：`025`（Critical 自動啟動）、`027`（Critical 無 opt-out）
- **DR-SU6**：`282`（`minimize` 無判準）、`283`／`284`（`not adversely affected`／`not impacted` 無判準）、
  `269`／`270`（`independently of any high-level operating system`）
- **重複表述**：`283`／`284`／`361`（背景執行，第三列）、`286`／`330`／`358`（完成後之狀態回報）
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch16"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 225
CA, UP, CP = "Client Architecture", "Update Policy", "Configurable Parameters"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"
CRIT = "A Critical Update package is staged on the OTA Server for this head unit"


def tc(req, ts, spec, prio, conf, note, item, paren, pre, proc, er, dm=FN):
    return dict(req=req, ts=ts, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


def internal(req, ts, spec, prio, note, item, paren, what, extra=()):
    return tc(req, ts, spec, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU2 means of observing {what}", *extra],
              ["1. Trigger an update availability check to the OTA Server and let the OTA session run",
               f"2. PENDING: DR-SU2 step to read {what}"],
              ["1. The OTA session runs on the head unit",
               f"2. PENDING: DR-SU2 observable evidence of {what}"])


def capability(req, ts, spec, prio, note, item, paren, what):
    return tc(req, ts, spec, prio, "低", note, item, paren,
              [B, WIFI, PKG, f"PENDING: DR-SU6 criterion by which {what} is judged in one bench run"],
              ["1. Trigger an update availability check to the OTA Server and let the OTA session run",
               f"2. PENDING: DR-SU6 step to establish that {what}"],
              ["1. The OTA session runs on the head unit",
               f"2. PENDING: DR-SU6 observable evidence that {what}"])


TCS = [
 capability("SWE1-FOTA-269", CA, "CFTS057-4907351", "P3",
  "**DR-SU6**＋**105 列**；⚠ 其為掃描候選清單之首位（與 `270` 之 Jaccard 0.846）—— **經起草覆核：二列之動作不同（映像 vs 檔案系統），非重複**",
  "The Redbend Update Agent(RBUA) shall perform the image update independently of any high-level operating system.",
  "Image update runs without depending on a high-level operating system",
  "the image update ran independently of any high-level operating system"),

 capability("SWE1-FOTA-270", CA, "CFTS057-4907352", "P3",
  "**DR-SU6**；與 `269` 之別在**其所更新之物**（檔案系統 vs 映像）—— **候選清單之高分不蘊含重複**",
  "The Redbend Update Agent(RBUA) shall perform the file-system update independently of any high-level operating system.",
  "File-system update runs without depending on a high-level operating system",
  "the file-system update ran independently of any high-level operating system"),

 internal("SWE1-FOTA-281", CA, "CFTS057-4907437", "P3",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.214）：idle 狀態於車機無表徵",
  "SWMC shall enter an idle state when there is no session, software update operation, server communication, or trigger event is active.",
  "SWMC goes idle when nothing is active",
  "whether the SWMC is in its idle state"),

 capability("SWE1-FOTA-282", CA, "CFTS057-4907438", "P3",
  "**DR-SU6**＋**105 列**：`minimize CPU and RAM utilization` **無判準** —— 任何用量皆可稱已最小化",
  "SWMC shall minimize CPU and RAM utilization while in the idle state.",
  "CPU and RAM use is minimised while idle",
  "the CPU and RAM utilisation while idle counts as minimised"),

 capability("SWE1-FOTA-283", CA, "CFTS057-4907566", "P2",
  "**DR-SU6**＋⚠ 錨為機制 3 攔下之首選（0.197）；**與 `361`（batch 9）／`284` 為同一件事之第二、三次** —— `not adversely affected` 無判準",
  "WiFiUpdateService shall execute deployment package downloads as background operations to ensure that HMI performance is not adversely affected.",
  "HMI performance is not hurt by a background download",
  "the HMI performance during a background download counts as not adversely affected"),

 capability("SWE1-FOTA-284", CA, "CFTS057-4907440", "P2",
  "**DR-SU6**；**與 `283`／`361` 同一件事之第三次**，其差在本列另指名 navigation 與 radio",
  "WiFiUpdateService shall execute SWMC as a low-priority background process while OTA communication is active, ensuring that normal host system functions such as HMI, navigation, and radio are not impacted.",
  "Navigation and radio are not impacted while OTA communication runs",
  "navigation and radio count as not impacted during OTA communication"),

 internal("SWE1-FOTA-286", CA, "CFTS057-4907447", "P2",
  "**105 列**；**與 `330`／`358` 為同一件事之第三次**（完成後之狀態回報）—— 其表徵在伺服器側（DR-SU2(e)）",
  "SWMC shall generate and send a status report upon completion of each session or update flow.",
  "Status report leaves the head unit when a flow completes",
  "the status report the SWMC sent on completion, read on the OTA Server side",
  ("PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1-FOTA-330 and 358",)),

 tc("SWE1-FOTA-025", UP, "CFTS057-4907453", "P1", "中",
  "**可寫**：Critical 之自動啟動可觀測（無使用者互動而下載開始）；其 campaign 之佈置同 batch 5 之先例",
  "When the update type is identified as Critical Update, the WiFi Update Service shall automatically initiate deployment package download and deployment processing in background mode on the host system.",
  "Critical update starts downloading with no user acceptance",
  [B, WIFI, CRIT],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server",
   "3. Check that the deployment package download starts without any user acceptance being given"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The update availability check completes and the update is reported as available",
   "3. The recorded screen content shows the deployment package download starting without any user acceptance being given"]),

 internal("SWE1-FOTA-026", UP, "CFTS057-4907586", "P2",
  "**第二型**＋**105 列**：分類之結果於車機無表徵，其外部後果（自動啟動）屬 `025`",
  "When the server command in the Download Descriptor (DD) indicates the update session as Critical Update, the WiFi Update Service shall classify the active update session as Critical Update.",
  "Session is classified as Critical from the DD server command",
  "the classification the WiFi Update Service applied to the active update session"),

 tc("SWE1-FOTA-027", UP, "CFTS057-4907454", "P1", "中",
  "**可寫**：無 opt-out 控制項可觀測（同 `177` 之先例）；其後二句（延後至安全前提滿足、執行中之限制）為殘餘，記於 REASONING",
  "The WiFi Update Service shall prevent user rejection or opt-out of an update package classified as Critical Update.",
  "No control to reject or opt out is offered for a critical update",
  [B, WIFI, CRIT],
  ["1. Record the head unit screen content as continuous video capture until the deployment package download completes",
   "2. Trigger an update availability check to the OTA Server",
   "3. Check that the head unit offers no control to reject the update and no control to opt out of it"],
  ["1. The head unit screen content until the deployment package download completes is recorded as continuous video capture",
   "2. The update availability check completes and the update is reported as available",
   "3. The recorded screen content shows no control to reject the update and no control to opt out of it"]),

 internal("SWE1-FOTA-033", UP, "CFTS057-4907464", "P2",
  "**第二型**：bearer 之偏好規則與其忽略皆無外部表徵（DR-SU2(a) 之族，同 `012`／`014`／`015`）",
  "The WiFi Update Service shall ignore configured bearer preference rules when the update type is identified as Critical Update.",
  "Bearer preference rules are ignored for a critical update",
  "the bearer the head unit used for a critical update and the preference rules it held"),

 tc("SWE1-FOTA-036", UP, "CFTS057-4907455", "P1", "中",
  "**可寫**；⚠ **與 `175`／`176`／`180`／`182`（Silent Update 組）相交** —— 本列為其統攝式表述，入 DR-SU3",
  "During Silent Update execution, the WiFi Update Service shall not trigger the SW Update HMI for notifications, progress prompts, or reject interaction flows.",
  "No notification, progress prompt or reject flow appears during a silent update",
  [B, WIFI, "A Silent Update package is staged on the OTA Server for this head unit",
   "PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1-FOTA-175, 176, 180 and 182"],
  ["1. Record the head unit screen content as continuous video capture from the update availability check until the update completes",
   "2. Trigger an update availability check to the OTA Server and leave the head unit untouched until the update completes",
   "3. Check that the recorded screen content contains no update notification, no progress prompt and no reject interaction flow"],
  ["1. The head unit screen content from the update availability check until the update completes is recorded as continuous video capture",
   "2. The update completes without the head unit being touched",
   "3. The recorded screen content contains no update notification, no progress prompt and no reject interaction flow"]),

 internal("SWE1-FOTA-126", CP, "CFTS057-4907742", "P2",
  "**伺服器側（DR-SU2(e)）**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.221）：參數之下發與其套用兩端皆不在車機",
  "The SWMC shall support receiving updated parameter values from the OTA server.",
  "Updated parameter values from the server are taken up",
  "the parameter values the SWMC received from the OTA Server and applied"),

 internal("SWE1-FOTA-128", CP, "CFTS057-4907744", "P2",
  "**第二型**：Download Descriptor 之解析（XML）與其參數抽取皆在服務內部",
  "The SWMC shall process the Download Descriptor as an XML file.",
  "Download Descriptor is processed as XML",
  "the Download Descriptor the SWMC parsed and the parameters it extracted"),
]

LOW_REASONS = {
 "SWE1-FOTA-269": [("架構命題不可否證（DR-SU6）", True)],
 "SWE1-FOTA-270": [("架構命題不可否證（DR-SU6）", True)],
 "SWE1-FOTA-281": [("idle 狀態無表徵", True), ("錨為機制 3 之首選（0.214）", "anchor")],
 "SWE1-FOTA-282": [("`minimize` 無判準（DR-SU6）", True)],
 "SWE1-FOTA-283": [("`not adversely affected` 無判準（DR-SU6）", True),
                   ("錨為機制 3 之首選（0.197）", "anchor")],
 "SWE1-FOTA-284": [("`not impacted` 無判準（DR-SU6）", True)],
 "SWE1-FOTA-286": [("表徵在伺服器側", True), ("與 `330`／`358` 重複", True)],
 "SWE1-FOTA-026": [("分類無外部表徵", True)],
 "SWE1-FOTA-033": [("bearer 無外部表徵", True)],
 "SWE1-FOTA-126": [("兩端皆在伺服器側", True), ("錨為機制 3 之首選（0.221）", "anchor")],
 "SWE1-FOTA-128": [("解析在服務內部", True)],
}
MECH3 = ["SWE1-FOTA-281", "SWE1-FOTA-283", "SWE1-FOTA-126"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T76f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T76f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")
    if any(t["req"] == "SWE1-FOTA-057" for t in TCS):
        sys.exit("T76f：`057` 於門檻裁定前不得起草 —— 停")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T76f —— batch 16 之產出（三組收尾，14 列）\n")
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
    print(f"- 品質訊號 **{len(q)}** ≤ 3 → 不退回｜錨定訊號 **{len(a)}** 列全數納入抽驗"
          f"｜可排除之 `低` {len(excl)} 列｜抽驗組成 {len(set(q)|set(a)|set(mid)|set(m3))} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
