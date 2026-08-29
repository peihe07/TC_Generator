#!/usr/bin/env python3
"""T61a —— `Update Policy` 之逕行起草（下放包 49 §二 #1 之判準）：12 列。

**本組 17 列之分流**（判準見下放包 49 §二 #1）：

| 分流 | 列 | 依據 |
|---|---|---|
| **逕行**（12） | `010`／`011`／`012`／`013`／`014`／`015`／`028`／`030`／`031`／`034`／`035`／`037` | 行為或更新類型與既有 TC 相異 |
| **待裁**（5） | `025`／`026`／**`027`**／**`033`**／**`036`** | 見上繳包 42 §1 |

⚠ **`036` 由「逕行」改列「待裁」** —— 下放包 49 §二 #1 令其逕行，理由為
「其為 Critical 而既有者為 Silent」；**實測 037 `036` 全文明寫
`classified as Silent Update`**，**其類型與 `001`／`002` 相同**，
依 §二 #1 自身之判準（行為同且類型亦同 → 待裁）應列待裁。

⚠ **`027`／`033` 為執行層另行判出之組內相交** —— 二者皆與 `037` 重疊
（`027`：Critical 不得拒絕；`033`：Critical 忽略 bearer 規則；
`037` 二者兼有），依同一判準列待裁。

**bearer 之選擇不可觀測** —— `012`／`014`／`015` 之判定核心繫於
「用哪一條網路」，而該事實於 HU 外部無表徵，**掛第二型 `PENDING`**。
**`010` 例外**：其情境為「無任何已設定之 Wi-Fi」，**TBM 為唯一可用之承載**，
故「更新仍完成」即足以證其走了 TBM。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch5"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "Update Policy"
AUTHOR = "PeiPYHsu"
START_N = 54

FN = "功能測試 (Functional based ; no specific technique)"
ST = "狀態轉換 (State Transition Testing)"
DT = "決策表 (Decision Table Testing)"
NEG = "負向測試 (Negative / Invalid)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
NOWIFI = "1. No previously configured Wi-Fi network is available to the head unit"
BODY = "2. The vehicle is in Body ON mode"

TCS = [
 dict(req="SWE1-FOTA-010", spec="CFTS057-4907825", dm=FN, prio="P1", conf="中",
      note="105 列；TBM 為唯一可用承載，故「更新仍完成」即足以證其走了 TBM",
  item=["If no previously configured Wi-Fi network is available, the WiFi Update Service shall request SWMC to initiate the FOTA package download using the embedded modem (TBM network), and shall use ConnectivityManager to monitor and manage network connectivity.",
        "(Update downloads over the embedded modem when no configured Wi-Fi is available)"],
  pre=[NOWIFI, BODY,
       "3. The embedded modem has mobile network coverage",
       "4. An update package is staged on the OTA Server for this head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after differs from Version_initial while no configured Wi-Fi network is available to the head unit"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and the update is accepted on the head unit",
      "3. Version_after is recorded",
      "4. Version_after differs from Version_initial while no configured Wi-Fi network is available to the head unit"]),
 dict(req="SWE1-FOTA-011", spec="CFTS057-4907826", dm=FN, prio="P2", conf="高", note="",
  item=["The HMI shall navigate to the software download via Wi-Fi screen when the user selects the Wi-Fi software download entry from the Settings menu.",
        "(Wi-Fi software download screen opened from the Settings menu)"],
  pre=[WIFI, BODY,
       "3. The Settings menu is displayed on the head unit"],
  proc=["1. Select the Wi-Fi software download entry in the Settings menu",
        "2. Check that the head unit displays the software download via Wi-Fi screen"],
  er=["1. The Wi-Fi software download entry is selected in the Settings menu",
      "2. The head unit displays the software download via Wi-Fi screen"]),
 dict(req="SWE1-FOTA-012", spec="CFTS057-4907831", dm=ST, prio="P1", conf="低",
      note="105 列；判定核心繫於『用哪一條網路』，而 bearer 於 HU 外部無表徵 —— 第二型",
  item=["If a previously configured Wi-Fi network is available during Body OFF mode, the WiFi Update Service shall request WifiManager to establish Wi-Fi connectivity and shall use ConnectivityManager to monitor and validate network connectivity.",
        "(Critical download switches to Wi-Fi when the vehicle goes to Body OFF)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit",
       "4. The download of the critical update package over the embedded modem is in progress",
       "5. PENDING: DR-SU2 means of observing which network bearer the head unit is using for the download"],
  proc=["1. Set the vehicle to Body OFF mode while the download over the embedded modem is in progress",
        "2. PENDING: DR-SU2 step to observe the network bearer used for the download after the transition to Body OFF mode",
        "3. Check that the download continues after the transition to Body OFF mode"],
  er=["1. The vehicle is in Body OFF mode",
      "2. PENDING: DR-SU2 observable evidence of the network bearer used for the download",
      "3. The download continues after the transition to Body OFF mode"]),
 dict(req="SWE1-FOTA-013", spec="CFTS057-4907832", dm=FN, prio="P1", conf="中",
      note="其判定核心為『無彈窗』，可觀測；bearer 之部分不入 ER",
  item=["During automatic FOTA download resume using a previously configured Wi-Fi network, the WiFi Update Service shall suppress Wi-Fi network configuration pop-up.",
        "(No Wi-Fi configuration pop-up shown while the download resumes automatically)"],
  pre=[WIFI, BODY,
       "3. An update package is staged on the OTA Server for this head unit",
       "4. A suspended FOTA package download session is present on the head unit"],
  proc=["1. Record the head unit screen content as continuous video capture from the moment the previously configured Wi-Fi network becomes available until the software version changes",
        "2. Bring the previously configured Wi-Fi network into range of the head unit",
        "3. Check that no Wi-Fi network configuration pop-up appears in the recorded screen content"],
  er=["1. The head unit screen content from the moment the Wi-Fi network becomes available until the software version changes is recorded as continuous video capture",
      "2. The previously configured Wi-Fi network is available to the head unit",
      "3. The recorded screen content contains no Wi-Fi network configuration pop-up"]),
 dict(req="SWE1-FOTA-014", spec="CFTS057-4907827", dm=ST, prio="P1", conf="低",
      note="105 列；Wi-Fi 可用而仍走 TBM —— 其差別全在 bearer，外部無表徵。第二型",
  item=["If the update type is Critical and the vehicle is in Body ON state, the WiFi Update Service shall request Connectivity Manager to establish network connectivity over the TBM interface.",
        "(Critical update downloads over the embedded modem while in Body ON)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit",
       "4. PENDING: DR-SU2 means of observing which network bearer the head unit is using for the download"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. PENDING: DR-SU2 step to observe the network bearer used for the download while the vehicle is in Body ON mode",
        "3. Check that the download of the critical update package starts while the vehicle is in Body ON mode"],
  er=["1. The update availability check completes and a critical update is reported as available",
      "2. PENDING: DR-SU2 observable evidence of the network bearer used for the download",
      "3. The download of the critical update package starts while the vehicle is in Body ON mode"]),
 dict(req="SWE1-FOTA-015", spec="CFTS057-4907828", dm=ST, prio="P1", conf="低",
      note="105 列；同 `012`／`014` —— bearer 不可觀測。第二型",
  item=["Upon detecting a subsequent transition of $OperationalModeSts$ from Body OFF to Body ON, the WiFi Update Service shall resume the interrupted FOTA download over the TBM network.",
        "(Interrupted critical download resumes at the next Body ON)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit",
       "4. The download of the critical update package was interrupted by a transition to Body OFF mode",
       "5. PENDING: DR-SU2 means of observing which network bearer the head unit is using for the download"],
  proc=["1. Set the vehicle to Body ON mode",
        "2. PENDING: DR-SU2 step to observe the network bearer used for the resumed download",
        "3. Check that the download resumes after the transition to Body ON mode"],
  er=["1. The vehicle is in Body ON mode",
      "2. PENDING: DR-SU2 observable evidence of the network bearer used for the resumed download",
      "3. The download resumes after the transition to Body ON mode"]),
 dict(req="SWE1-FOTA-028", spec="CFTS057-4907462", dm=FN, prio="P2", conf="低",
      note="105 列；其觸發須等待一週之 Wi-Fi 失敗 —— **第四型（觸發手段不可得）**",
  item=["If Wi-Fi connectivity cannot be established or the FOTA package download cannot be completed within one week, the WiFi Update Service shall request SWMC to continue the FOTA package download using the lowest cost supported mobile network method.",
        "(Download falls back to the mobile network after the Wi-Fi attempt period)"],
  pre=[NOWIFI, BODY,
       "3. A non-critical update package is staged on the OTA Server for this head unit",
       "4. PENDING: DR-SU2 means of reaching the end of the one week Wi-Fi attempt period on the test bench",
       "5. PENDING: DR-SU2 means of observing which network bearer the head unit is using for the download"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. PENDING: DR-SU2 step to reach the end of the one week Wi-Fi attempt period",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. PENDING: DR-SU2 step to observe the network bearer used for the download after the Wi-Fi attempt period has elapsed",
        "5. Check that Version_after differs from Version_initial after the Wi-Fi attempt period has elapsed"],
  er=["1. Version_initial is recorded",
      "2. PENDING: DR-SU2 observable state showing that the Wi-Fi attempt period has elapsed",
      "3. Version_after is recorded",
      "4. PENDING: DR-SU2 observable evidence of the network bearer used for the download",
      "5. Version_after differs from Version_initial after the Wi-Fi attempt period has elapsed"]),
 dict(req="SWE1-FOTA-030", spec="CFTS057-4907470", dm=FN, prio="P1", conf="低",
      note="**第三型**：與 `006`（`180`）之判定對象逐字相同，其區分全繫於類型標籤；而類型於 HU 上無標記，可用之區分皆為他列所轄（下放包 51 §一 #2／#3）",
  item=["During Critical Update execution, the WiFi Update Service shall not trigger the SW Update HMI to display a download confirmation screen.",
        "(No download confirmation screen shown for a critical update)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit",
       "4. PENDING: DR-SU2 means of distinguishing a critical update session from a silent update session on the head unit"],
  proc=["1. Record the head unit screen content as continuous video capture from the availability check until the software version changes",
        "2. Trigger an update availability check to the OTA Server",
        "3. PENDING: DR-SU2 step to observe that the session in progress is a critical update session",
        "4. Check that no download confirmation screen appears in the recorded screen content"],
  er=["1. The head unit screen content from the availability check until the software version changes is recorded as continuous video capture",
      "2. The update availability check completes and a critical update is reported as available",
      "3. PENDING: DR-SU2 observable evidence that the session in progress is a critical update session",
      "4. The recorded screen content contains no download confirmation screen"]),
 dict(req="SWE1-FOTA-031", spec="CFTS057-4907471", dm=FN, prio="P1", conf="中",
      note="其更新類型未見於 037 列文，來自錨 `4907471` 之章別（4.7.3.1，GT-B 已裁）",
  item=["Upon receiving deployment package download completion status, the WiFi Update Service shall notify the SW Update HMI to display the deployment confirmation screen.",
        "(Deployment confirmation screen shown after the critical update download completes)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server and wait until the deployment package download completes",
        "2. Check that the head unit displays the deployment confirmation screen for this critical update"],
  er=["1. The deployment package download completes on the head unit",
      "2. The head unit displays the deployment confirmation screen for this critical update"]),
 dict(req="SWE1-FOTA-034", spec="CFTS057-4907457", dm=DT, prio="P1", conf="中",
      note="須同時佈置二個不同類型之 campaign；其判定對象為安裝之先後",
  item=["The WiFi Update Service shall prevent installation of a lower priority update while a higher priority update session is pending or in progress.",
        "(Regular update is withheld while a critical update session is pending)"],
  pre=[WIFI, BODY,
       "3. A critical update package and a regular update package are both staged on the OTA Server for this head unit",
       "4. The critical update session is pending on the head unit"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Record the head unit screen content as continuous video capture from the availability check until the software version changes",
        "3. Trigger an update availability check to the OTA Server",
        "4. Check that the recorded screen content shows the critical update being installed and shows no regular update being installed while the critical update session is pending"],
  er=["1. Version_initial is recorded",
      "2. The head unit screen content from the availability check until the software version changes is recorded as continuous video capture",
      "3. The update availability check completes and both updates are reported as available",
      "4. The recorded screen content shows the critical update being installed and shows no regular update being installed while the critical update session is pending"]),
 dict(req="SWE1-FOTA-035", spec="CFTS057-4907456", dm=FN, prio="P1", conf="中",
      note="Regular 型別為本 feature 首見；其區分在更新類型且已入判定對象",
  item=["For update packages classified as non-silent and non-critical, the WiFi Update Service shall execute the update session using the standard end-user interaction flow through the SW Update HMI.",
        "(Standard user interaction flow shown for a regular update)"],
  pre=[WIFI, BODY,
       "3. A regular update package is staged on the OTA Server for this head unit"],
  proc=["1. Record the head unit screen content as continuous video capture from the availability check until the software version changes",
        "2. Trigger an update availability check to the OTA Server",
        "3. Check that the recorded screen content shows the SW Update opt-in screen for this regular update"],
  er=["1. The head unit screen content from the availability check until the software version changes is recorded as continuous video capture",
      "2. The update availability check completes and a regular update is reported as available",
      "3. The recorded screen content shows the SW Update opt-in screen for this regular update"]),
 dict(req="SWE1-FOTA-037", spec="CFTS057-4907454", dm=NEG, prio="P1", conf="中",
      note="與 `004`（`177`，Silent）之區分在更新類型；`027`／`033` 與本列相交，已列待裁",
  item=["During Critical Update execution, the SW Update HMI shall not provide a Reject option and shall allow the user to postpone installation only until the next vehicle restart.",
        "(No reject option offered for a critical update, postpone only)"],
  pre=[WIFI, BODY,
       "3. A critical update package is staged on the OTA Server for this head unit",
       "4. The SW Update opt-in screen is displayed on the head unit"],
  proc=["1. Check that the SW Update opt-in screen offers no reject control for this critical update",
        "2. Check that the SW Update opt-in screen offers a postpone control"],
  er=["1. The SW Update opt-in screen offers no reject control for this critical update",
      "2. The SW Update opt-in screen offers a postpone control"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T61a：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T61a：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T61a —— `Update Policy` 之逕行起草（12 列）\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TEST_SET,
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

    print("| 列 | TC ID | 037 | **自信度** | PENDING |")
    print("|---|---|---|:--:|---:|")
    for r, tid, req, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | **{cf}** | {pd} |")
    # ── 分層抽驗（下放包 50 §二 #4 ＋ 51 §一 #5 之條件式排除）──
    #
    # **僅當該列 `低` 之理由已逐項由 `PENDING` 承載時，方得排除。**
    # `PENDING` 是**逐行**掛的，自信度標記是**逐列**的 —— 二者粒度不同；
    # 以逐行之物排除逐列之物，**必然漏掉同一列中未被佔位覆蓋的部分**（B-21）。
    LOW_REASONS = {
        "SWE1-FOTA-012": [("bearer 於外部無表徵", True)],
        "SWE1-FOTA-014": [("bearer 於外部無表徵", True)],
        "SWE1-FOTA-015": [("bearer 於外部無表徵", True)],
        "SWE1-FOTA-028": [("一週之等待不可觸發", True),
                          ("bearer 於外部無表徵", True),
                          ("錨 `4907462` 為首選而未經 GT 驗證", False)],
        "SWE1-FOTA-030": [("與 `006` 不可區辨（類型無標記）", True)],
    }
    from collections import Counter
    c = Counter(t["conf"] for t in TCS)
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**")
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [(i, t["req"]) for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    print(f"\n### 分層抽驗（新制：條件式排除 ＋ 訊號只看 `低`）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- **可排除之 `低`（理由已逐項由 `PENDING` 承載）**：{len(excl)} 列 —— "
          + "、".join(f"`SU-{i:03d}`" for i, _, _ in excl))
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— 其 `低` 之理由有 "
              f"{len(un)} 項未由 `PENDING` 承載：" + "、".join(f"**{r}**" for r in un))
    low_after = len(keep)
    print(f"- **抽驗組成** = 全部 `中`（{len(mid)}）＋ 未能排除之 `低`（{low_after}）"
          f" = **{len(mid)+low_after}** 列")
    print(f"- **退回訊號**：扣除後 `低` = **{low_after}** "
          + ("**> 3 → 觸發，該批應退回重檢**" if low_after > 3
             else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
