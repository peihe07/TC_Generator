#!/usr/bin/env python3
"""T60c —— ROV-E ＋ `USB Update`（下放包 47 §五）：八列，執行層自行起草。

**本批範圍已依下放包 47 §五之明文縮減** —— 原令 25 列（ROV-E 3 ＋
`Update Policy` 17 ＋ `USB Update` 5）。`Update Policy` **本批不做**，
其成因非難度三軸，而是**範圍委派之邊界未定**（見上繳包 41 §1）——
該組 17 列中至少 6 列與 batch 1 之已產出 TC 重疊，
**而委派邊界屬分析層之職責**（下放包 45 §2.2-1）。

**ROV-E（3）**：`104`／`105`／`106` —— ER **以彈窗之功能描述指稱，不引編號**
（下放包 43 §二 #2：`PUXXX3`／`PUxxx1` 於 037 與彈窗清單**二側皆為佔位**）。

**`USB Update`（5）**：`080`／`081`／`082`／`083`／`084`。
⚠ **`083`／`084` 掛 `PENDING`（第三型）** —— 其與 `081`／`082` **僅內部路由不同**
（`081`：二服務各自送 Arbiter；`083`：二者先送 WiFi Update Service 再轉送），
**外部後果完全相同**。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch4"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 46

FN = "功能測試 (Functional based ; no specific technique)"
DT = "決策表 (Decision Table Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
BODY = "2. The vehicle is in Body ON mode"

TCS = [
 # ── ROV-E ─────────────────────────────────────────────────────────
 dict(req="SWE1-FOTA-104", ts="ROV Installation", spec="CFTS057-4907887", dm=DT, prio="P2",
      conf="中", note="與 `105` 之區分在動力系型別之取值",
  item=["If $Hybrid_Type$ = [BEV] or [PHEV]and the user selects Schedule Update, the ROV FOTA HMI shall display the “Schedule Update pop-up (PUXXX3)”.",
        "(Schedule update pop-up shown on a BEV or PHEV vehicle)"],
  pre=[WIFI, BODY,
       "3. The vehicle is a BEV or a PHEV",
       "4. An ROV forced update campaign has been staged for this vehicle",
       '5. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=['1. Select "Schedule Update" on the "ROV Forced Update Available A" pop-up',
        "2. Check that the head unit displays the schedule update pop-up on this BEV or PHEV vehicle"],
  er=['1. The "ROV Forced Update Available A" pop-up closes',
      "2. The head unit displays the schedule update pop-up on this BEV or PHEV vehicle"]),
 dict(req="SWE1-FOTA-105", ts="ROV Installation", spec="CFTS057-4907888", dm=DT, prio="P2",
      conf="低", note="其動力系集合為 `104` 之超集；本 TC 取 `104` 所無之 FCEV／REPB 以求可區辨 —— 待裁",
  item=["If $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB]Band the user selects Schedule Update, then ROV FOTA HMI shall display the “Schedule Update pop-up (PUXXX3)” .",
        "(Schedule update pop-up shown on an FCEV or REPB vehicle)"],
  pre=[WIFI, BODY,
       "3. The vehicle is an FCEV or an REPB",
       "4. An ROV forced update campaign has been staged for this vehicle",
       '5. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=['1. Select "Schedule Update" on the "ROV Forced Update Available A" pop-up',
        "2. Check that the head unit displays the schedule update pop-up on this FCEV or REPB vehicle"],
  er=['1. The "ROV Forced Update Available A" pop-up closes',
      "2. The head unit displays the schedule update pop-up on this FCEV or REPB vehicle"]),
 dict(req="SWE1-FOTA-106", ts="ROV Installation",
      spec="CFTS057-4907890\nCFTS057-4907891", dm=FN, prio="P2",
      conf="中", note="其錨為二個同分（0.640）且文字幾乎相同之物件，取二者；待抽驗確認",
  item=["The ROV FOTA HMI shall display the “Conditions Not Met” (PUxxx1) pop-up with the corresponding cancellation reason text.",
        "(Conditions Not Met pop-up shows the cancellation reason text)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle",
       "4. The vehicle does not meet the installation preconditions for the staged update"],
  proc=["1. Trigger the ROV update availability notification to the head unit",
        "2. Check that the head unit displays the conditions not met pop-up and that the pop-up shows a cancellation reason text"],
  er=["1. The ROV update availability notification is delivered to the head unit",
      "2. The head unit displays the conditions not met pop-up and the pop-up shows a cancellation reason text"]),
 # ── USB Update ────────────────────────────────────────────────────
 dict(req="SWE1-FOTA-080", ts="USB Update", spec="CFTS057-4907256", dm=FN, prio="P1",
      conf="中", note="105 列；其外部後果為「無 Wi-Fi 而更新仍完成」，非內部之 USB 介面",
  item=["The SWMC shall utilize the TBM as a network bearer through the USB 2.0 interface for OTA firmware update download when Wi-Fi connectivity is unavailable.",
        "(Update downloads over the TBM USB connection when no Wi-Fi is available)"],
  pre=["1. No Wi-Fi network is configured on the head unit",
       "2. The TBM is connected to the head unit through the USB 2.0 interface",
       "3. An update package is staged on the OTA Server for this head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after differs from Version_initial while no Wi-Fi network is configured on the head unit"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. Version_after is recorded",
      "4. Version_after differs from Version_initial while no Wi-Fi network is configured on the head unit"]),
 dict(req="SWE1-FOTA-081", ts="USB Update", spec="CFTS057-4907246", dm=EP, prio="P1",
      conf="高", note="",
  item=["When multiple update methods provide update packages with different software versions, the Arbiter Service shall select the update package with the highest software version for deployment processing.",
        "(Higher version package is the one deployed when FOTA and USB versions differ)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       "3. A USB storage device holding an update package of a lower software version is connected to the head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after equals the version of the package staged on the OTA Server"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and the update is accepted on the head unit",
      "3. Version_after is recorded",
      "4. Version_after equals the version of the package staged on the OTA Server"]),
 dict(req="SWE1-FOTA-082", ts="USB Update", spec="CFTS057-4907247", dm=DT, prio="P1",
      conf="高", note="",
  item=["If two update methods provide update packages with the same software version number, the Arbiter Service shall prioritize the update package downloaded via FOTA for deployment processing.",
        "(FOTA package is the one deployed when both methods offer the same version)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       "3. A USB storage device holding an update package of the same software version is connected to the head unit"],
  proc=["1. Record the head unit screen content as continuous video capture from the availability check until the software version changes",
        "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "3. Check that the recorded screen content shows the update being deployed from the OTA Server and not from the USB storage device"],
  er=["1. The head unit screen content from the availability check until the software version changes is recorded as continuous video capture",
      "2. The update availability check completes and the update is accepted on the head unit",
      "3. The recorded screen content shows the update being deployed from the OTA Server and not from the USB storage device"]),
 # `083`／`084` —— 第三型：與 `081`／`082` 僅內部路由不同，外部後果相同
 dict(req="SWE1-FOTA-083", ts="USB Update", spec="CFTS057-4907247", dm=EP, prio="P2",
      conf="低", note="與 `081` 不可區辨（僅內部路由不同），掛第三型 `PENDING`",
  item=["The Arbiter Service shall compare the version information of update packages available from FOTA and USB update methods.",
        "(Version comparison routed through the WiFi Update Service)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       "3. A USB storage device holding an update package of a lower software version is connected to the head unit",
       "4. PENDING: DR-SU2 means of distinguishing this routing path from the one verified by SWE1-FOTA-081"],
  proc=["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "2. PENDING: DR-SU2 step to observe which service forwarded the version information to the Arbiter Service"],
  er=["1. The update availability check completes and the update is accepted on the head unit",
      "2. PENDING: DR-SU2 observable evidence of the routing path taken by the version information"]),
 dict(req="SWE1-FOTA-084", ts="USB Update", spec="CFTS057-4907247", dm=DT, prio="P2",
      conf="低", note="與 `082` 不可區辨（僅內部路由不同），掛第三型 `PENDING`",
  item=["If two or more update methods provide update packages with the same version number, the Arbiter Service shall prioritize the update package download via FOTA.",
        "(Same-version prioritisation routed through the WiFi Update Service)"],
  pre=[WIFI,
       "2. An update package is staged on the OTA Server for this head unit",
       "3. A USB storage device holding an update package of the same software version is connected to the head unit",
       "4. PENDING: DR-SU2 means of distinguishing this routing path from the one verified by SWE1-FOTA-082"],
  proc=["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "2. PENDING: DR-SU2 step to observe which service forwarded the version information to the Arbiter Service"],
  er=["1. The update availability check completes and the update is accepted on the head unit",
      "2. PENDING: DR-SU2 observable evidence of the routing path taken by the version information"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T60c：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T60c：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T60c —— ROV-E ＋ `USB Update` 之產出（**執行層自行起草**）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜輸出 `sandbox/{TAG}/`")
    print("- **範圍已縮**：原令 25 列，`Update Policy` 17 列本批不做（見上繳包 41 §1）\n")
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

    print("| 列 | TC ID | 037 | Test Set | **自信度** | PENDING |")
    print("|---|---|---|---|:--:|---:|")
    for r, tid, req, ts, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | `{ts}` | **{cf}** | {pd} |")
    from collections import Counter
    c = Counter(t["conf"] for t in TCS)
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**")
    print(f"- **自信度分布**：高 {c['高']}／中 {c['中']}／**低 {c['低']}**"
          f" —— 分層抽驗之組成為「全部低 ＋ 全部中」= **{c['低']+c['中']} 列**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
