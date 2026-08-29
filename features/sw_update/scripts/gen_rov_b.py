#!/usr/bin/env python3
"""T57a —— ROV-B（下放包 44 §二）：`ROV Installation` 強制更新彈窗之互動流程七列。

037 六列 → **7 個 TC**（`100` 依 IN §8.2.2 拆二：逾時／取消）。

**屬性值一律不入 procedure／ER**（下放包 44 §一 #3）：
`$FOTA_Status$`／`$FOTA_Delay$`／`$FOTA_Install$` 皆為 CarPropertyManager 之
車輛屬性，**台架不可觀測**（R-SU25(b)，同 `028` 之成因）。
其於 `test_item` 上半**依 037 逐字保留**（R-S4）——
**上半是需求原文，步驟與 ER 是可執行之描述，二者不必同形。**

**`$FOTA_Delay$` 之 `[Not_Prohibited]`／`[Not Prohibited]` 為同一值之二種寫法**
（下放包 44 §一 #2）—— 037 側 `097`／`101`、CFTS 側 `4907880`／`4907884`
**二側皆有，非單側筆誤**。`test_item` 依各列原文逐字，**不統一**。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "rov_b"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "ROV Installation"
AUTHOR = "PeiPYHsu"
START_N = 32

FN = "功能測試 (Functional based ; no specific technique)"
DT = "決策表 (Decision Table Testing)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
BODY = "2. The vehicle is in Body ON mode"
# **R-9(a)：一行一條件** —— 下放包 44 之原文以 `and` 併二條件於同一行，
# 觸發 lint 之 R 檢查（多條件並列）。**拆為二行為逕行**（不改條件、不改單元）。
POPB = ['3. An ROV forced update campaign is staged for this vehicle',
        '4. The "ROV Forced Update Available B" pop-up is displayed on the head unit']
REC_B = ('1. Record the head unit screen content as continuous video capture '
         'from the moment the pop-up is displayed')
ER_REC_B = ('1. The head unit screen content from the moment the pop-up is displayed '
            'is recorded as continuous video capture')

TCS = [
 dict(req="SWE1-FOTA-097", spec="CFTS057-4907880", dm=DT, prio="P1",
  item=['If FOTA_Status indicates Waiting for HMI Acceptance ($FOTA_Status$ = [Waiting for HMI Acceptance]) and FOTA_Delay indicates Not_Prohibited($FOTA_Delay$ = [Not_Prohibited]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall show “ROV Forced Update Available A” pop-up.',
        "(Forced Update Available A pop-up shown when deferral is permitted)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle with deferral permitted"],
  proc=["1. Trigger the ROV update availability notification to the head unit",
        '2. Check that the head unit displays the "ROV Forced Update Available A" pop-up'],
  er=["1. The ROV update availability notification is delivered to the head unit",
      '2. The head unit displays the "ROV Forced Update Available A" pop-up']),
 dict(req="SWE1-FOTA-099", spec="CFTS057-4907882", dm=FN, prio="P1",
  item=['The ROV FOTA HMI shall capture the user selection from the “ROV Forced Update Available B” pop-up. If the user selects Update Now, the ROV FOTA HMI shall notify the ROV Update Service.',
        "(Installation starts when the user selects Update Now)"],
  pre=[WIFI, BODY, *POPB],
  proc=['1. Select "Update Now" on the "ROV Forced Update Available B" pop-up',
        "2. Record the head unit screen content as continuous video capture until the installation ends",
        '3. Check that the head unit starts the installation after "Update Now" is selected'],
  er=['1. The "ROV Forced Update Available B" pop-up closes',
      "2. The head unit screen content until the installation ends is recorded as continuous video capture",
      '3. The recorded screen content shows the installation starting after "Update Now" is selected']),
 # `100` 拆二 —— s1+s3（逾時）／s1+s2（取消）；s2 委派 TC-35、s3 委派 TC-34
 dict(req="SWE1-FOTA-100", spec="CFTS057-4907883", dm=FN, prio="P1",
  item=['The ROV FOTA HMI shall start a response timer upon displaying the "ROV Forced Update Available B" pop-up. If no user selection is received within the configured timeout, the ROV FOTA HMI shall notify the ROV Update Service.',
        "(Installation withheld after the pop-up closes on timeout)"],
  pre=[WIFI, BODY, *POPB],
  proc=[REC_B,
        '2. Leave the "ROV Forced Update Available B" pop-up without selecting any option until it closes',
        "3. Check that the head unit does not start the installation after the pop-up has closed without any user selection"],
  er=[ER_REC_B,
      '2. The "ROV Forced Update Available B" pop-up closes without any user selection',
      "3. The recorded screen content shows no installation starting after the pop-up has closed without any user selection"]),
 dict(req="SWE1-FOTA-100", spec="CFTS057-4907883", dm=FN, prio="P1",
  item=['The ROV FOTA HMI shall start a response timer upon displaying the "ROV Forced Update Available B" pop-up. If the user cancels the pop-up, the ROV FOTA HMI shall notify the ROV Update Service.',
        "(Installation withheld after the user cancels the pop-up)"],
  pre=[WIFI, BODY, *POPB],
  proc=[REC_B,
        '2. Cancel the "ROV Forced Update Available B" pop-up',
        "3. Check that the head unit does not start the installation after the user has cancelled the pop-up"],
  er=[ER_REC_B,
      '2. The "ROV Forced Update Available B" pop-up closes after being cancelled by the user',
      "3. The recorded screen content shows no installation starting after the user has cancelled the pop-up"]),
 dict(req="SWE1-FOTA-101", spec="CFTS057-4907884", dm=DT, prio="P1",
  item=['The ROV FOTA HMI shall allow the user to cancel or ignore the "ROV Forced Update Available A" popup only when FOTA_Status is equal to Waiting for HMI Acceptance and FOTA_Delay is equal to Not_Prohibited.($FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited])',
        "(Cancel available on the pop-up when deferral is permitted)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle with deferral permitted",
       '4. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=['1. Cancel the "ROV Forced Update Available A" pop-up',
        "2. Check that the pop-up closes and the head unit returns to the screen shown before the pop-up"],
  er=['1. The "ROV Forced Update Available A" pop-up offers a cancel control and closes when it is cancelled',
      "2. The head unit returns to the screen shown before the pop-up"]),
 # `102` —— 首選 `4907884`（分 0.566）述**相反**之規定；錨取候選 #4 `4907885`
 dict(req="SWE1-FOTA-102", spec="CFTS057-4907885", dm=DT, prio="P1",
  item=["The ROV FOTA HMI shall not allow the user to skip, ignore, or dismiss the forced update. The ROV FOTA HMI shall enforce the lockout behavior until the user schedules the update.",
        "(No skip, ignore or dismiss offered when deferral is prohibited)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign has been staged for this vehicle with deferral prohibited",
       "4. The forced update pop-up is displayed on the head unit"],
  proc=["1. Attempt to close the forced update pop-up without selecting the schedule option",
        "2. Check that the pop-up remains displayed and offers no skip control, no ignore control and no dismiss control"],
  er=["1. The forced update pop-up does not close",
      "2. The pop-up remains displayed and offers no skip control, no ignore control and no dismiss control"]),
 dict(req="SWE1-FOTA-103", spec="CFTS057-4907886", dm=FN, prio="P1",
  item=['The ROV FOTA HMI shall capture user selection for "Schedule Update" from the "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up. Upon receiving the user selection, then ROV Update Service shall transition the flow to the Schedule Update HMI.',
        "(Schedule Update screen opened from the forced update pop-up)"],
  pre=[WIFI, BODY,
       "3. An ROV forced update campaign is staged for this vehicle",
       '4. The "ROV Forced Update Available A" pop-up is displayed on the head unit'],
  proc=['1. Select "Schedule Update" on the "ROV Forced Update Available A" pop-up',
        "2. Check that the head unit displays the Schedule Update screen"],
  er=['1. The "ROV Forced Update Available A" pop-up closes',
      "2. The head unit displays the Schedule Update screen"]),
]


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    bad = {t["dm"] for t in TCS} - legal
    if bad:
        sys.exit(f"T57a：`design_method` 有清單外之值 {bad} —— 停（R-SU40(a)）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T57a —— ROV-B 之產出（受檢物，非交付本）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜Test Set：`{TEST_SET}`｜輸出 `sandbox/{TAG}/`\n")
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
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["spec"], t["dm"][:4], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 列 | spec_reference | 設計法 | PENDING |")
    print("|---|---|---|---|---|---:|")
    for r, tid, req, sp, dm, pd in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` | {dm} | {pd} |")
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜涵蓋 037 列 "
          f"**{len({r[2] for r in rows})}**｜TC **{len(rows)}**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
