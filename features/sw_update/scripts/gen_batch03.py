#!/usr/bin/env python3
"""T53c —— batch 3（下放包 40 §三）之工作簿產出：`Update HMI` 6 列 → 10 個 TC。

沿革：
- **v1**（下放包 40 §三）：10 個 TC，`PENDING` 0。
- **v2**（下放包 41 §三，T54a）：**三份更正** ——
  `022` 之上半由 s2＋s4 改 **s3＋s4**（其 s3 即 ER 之驗證點，原不在上半內）；
  `025` 刪除自 s2 移接之時間子句（**造句非摘句**，原文中該子句主詞為 SWMC）；
  **`021` 改判掛 `PENDING: DR-SU5`** —— 其「還原至更新前版本」在台架上
  不可行且不可確認（上繳包 35 §7），措辭改為「回到**可比之起始狀態**」，
  **不預設其手段為降版**。

⚠ **`025` 之引號依下放包 41 §3.2 逐字照抄**：`test_item` 為彎引號（037 原文），
而 `test_procedure`／`expected_result` 為**直引號**（下放包之措辭）——
**同一 TC 內同一標籤二種寫法**。執行層依 T32b 不改寫分析層所定之 TC 內容，
**記於上繳包 36 §2.2 待裁**。

TC 內容逐字取自下放包 40 §三，執行層不改寫（T32b）。**二處例外，皆為逐字還原**
（凍結第 3 條之逕行條件：不改驗證單元、不改錨、不增刪 `PENDING`、
理由可自 R-4／§8.4.1 直接導出）：

- **`134`（TC-25）**：037 原文之 `“Install”`／`“Schedule Later”` 為**彎引號**
  （U+201C／U+201D），下放包誤植為直引號。**還原為彎引號。**
- **`136`（TC-27／TC-26）**：037 原文為 `… Silent Install flag ␣.`
  （句點前有一空格），下放包刪去該空格。**還原該空格。**
  同型之空格另見 `134` 之 `to the user ␣.`，一併還原。

**未逕行而留待裁者**（見上繳包 35 §FAIL-1）：`131`／`132`／`134` 之
`test_item` 上半為**非相鄰句之拼接**，且 `132` 之驗證點（037 第 3 句）
**不在其 test_item 內**。其涉驗證單元之界定，不在逕行條件內。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch03"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "Update HMI"
AUTHOR = "PeiPYHsu"
START_N = 18                       # batch 1 001–010、batch 2a 011–017

FN = "功能測試 (Functional based ; no specific technique)"
ST = "狀態轉換 (State Transition Testing)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"

WIFI = "1. The head unit is connected to a Wi-Fi network with internet access"
PKG = "2. An update package is staged on the OTA Server for this head unit"

# `130` 之三語言 —— 肯定式全稱，依 R-SU33(d) 需逐 X 確認，不適用觀測窗法
I130 = ("The MCPU platform software shall provide localization support for the three "
        "languages required for the NAFTA region. The supported languages shall include "
        "English, North American French, and North American Spanish.")


def lang_tc(lang: str, paren: str) -> dict:
    return dict(
        req="SWE1-FOTA-130", spec="CFTS057-4907653", dm=FN, prio="P2",
        item=[I130, f"({paren})"],
        pre=[WIFI, PKG, f"3. The head unit language setting is set to {lang}"],
        proc=["1. Trigger an update availability check to the OTA Server",
              "2. Open the SW Update screen on the head unit",
              f"3. Check that the update-related text and messages on the SW Update screen are shown in {lang}"],
        er=["1. The update availability check completes and an update is reported as available",
            "2. The SW Update screen is displayed on the head unit",
            f"3. The update-related text and messages on the SW Update screen are shown in {lang}"])


TCS = [
 lang_tc("English", "Update text shown in English when English is the configured language"),
 lang_tc("North American French",
         "Update text shown in North American French when that language is configured"),
 lang_tc("North American Spanish",
         "Update text shown in North American Spanish when that language is configured"),
 # TC-21 —— 驗證單元為「伺服器所設之類型決定所適用之流程」，非各類型自身之行為
 dict(req="SWE1-FOTA-131", spec="CFTS057-4907453\nCFTS057-4907656", dm=ST, prio="P1",
  item=["The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The WiFi Update Service shall control the applicable update flow according to the server-defined update type configuration.",
        "(Update flow follows the update type configured on the server)"],
  pre=[WIFI,
       "2. An update campaign configured on the OTA Server with update type Regular is available for this head unit",
       "3. PENDING: DR-SU5 bench procedure for running the same head unit against two update campaigns of different update types from a comparable starting state"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Record the SW Update screens shown on the head unit as continuous video capture until the update finishes",
        "3. PENDING: DR-SU5 step to return the head unit to a comparable starting state and set the campaign to update type Silent",
        "4. Trigger an update availability check to the OTA Server",
        "5. Check that the recorded screen content of the first run contains the opt-in screen and that no opt-in screen is shown in the second run"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The SW Update screens shown until the update finishes are recorded as continuous video capture",
      "3. PENDING: DR-SU5 observable state showing the head unit is back at a comparable starting state and the campaign type is Silent",
      "4. The update availability check completes and an update is reported as available",
      "5. The recorded screen content of the first run contains the opt-in screen; the second run shows no opt-in screen"]),
 dict(req="SWE1-FOTA-132", spec="CFTS057-4907657", dm=NEG, prio="P1",
  item=["If the customer has not accepted the required terms and conditions, the SWMC shall provide SW Update HMI guidance describing how the customer can complete the acceptance process. The SWMC shall block update download initiation until terms and conditions acceptance is confirmed.",
        "(Download blocked and guidance shown when terms and conditions are not accepted)"],
  pre=[WIFI,
       "2. An update package whose Download Descriptor requires terms and conditions acceptance is staged on the OTA Server for this head unit",
       "3. The customer preference record for this vehicle shows the terms and conditions as not accepted"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that the SW Update screen shows guidance on how to accept the terms and conditions and that Version_after equals Version_initial"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. Version_after is recorded",
      "4. The SW Update screen shows guidance on how to accept the terms and conditions; Version_after equals Version_initial"]),
 dict(req="SWE1-FOTA-133", spec="CFTS057-4907660", dm=FN, prio="P2",
  item=["The SW Update HMI shall display the release notes information, update-related information, and associated links during the opt-in and download screens.",
        "(Release notes and links shown on the opt-in and download screens)"],
  pre=[WIFI,
       "2. An update package whose Download Descriptor contains release notes and at least one link is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Open the opt-in screen on the head unit",
        "3. Open the download screen on the head unit",
        "4. Check that both the opt-in screen and the download screen show the release notes text and the link contained in the Download Descriptor"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The opt-in screen is displayed on the head unit",
      "3. The download screen is displayed on the head unit",
      "4. The opt-in screen and the download screen both show the release notes text and the link contained in the Download Descriptor"]),
 dict(req="SWE1-FOTA-133", spec="CFTS057-4907660", dm=FN, prio="P2",
  item=["The SW Update HMI shall support user interaction with embedded links displayed as part of the update information.",
        "(Embedded link responds when selected by the user)"],
  pre=[WIFI,
       "2. An update package whose Download Descriptor contains release notes and at least one link is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Open the opt-in screen on the head unit",
        "3. Select the link shown in the update information",
        "4. Check that the head unit opens the content referenced by the selected link"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The opt-in screen is displayed on the head unit",
      "3. The link shown in the update information is selected",
      "4. The head unit opens the content referenced by the selected link"]),
 # TC-25 —— 彎引號與 ` .` 之空格為 037 原文，**逐字還原**（R-4）
 dict(req="SWE1-FOTA-134", spec="CFTS057-4907662", dm=FN, prio="P1",
  item=["The SW Update HMI shall display the deployment package details to the user . The SW Update HMI shall provide opt-in options including “Install” and “Schedule Later”.",
        "(Install and Schedule Later offered after download completes)"],
  pre=[WIFI,
       "2. An update package configured as a non-silent update is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Accept the update on the opt-in screen and wait until the download completes",
        "3. Check that the head unit shows the deployment package details together with an \"Install\" option and a \"Schedule Later\" option"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The download completes and the post-download screen is displayed on the head unit",
      "3. The post-download screen shows the deployment package details, an \"Install\" option and a \"Schedule Later\" option"]),
 # TC-26／27 —— `flag .` 之空格為 037 原文，**逐字還原**（R-4）
 dict(req="SWE1-FOTA-136", spec="CFTS057-4907600", dm=DT, prio="P1",
  item=["The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag . The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.",
        "(Rejection option offered when the flags permit rejection)"],
  pre=[WIFI,
       "2. An update campaign with the Critical Update flag not set and the Silent Install flag not set is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Open the SW Update opt-in screen on the head unit",
        "3. Check that the opt-in screen offers the user an option to reject the deployment"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The SW Update opt-in screen is displayed on the head unit",
      "3. The opt-in screen offers the user an option to reject the deployment"]),
 dict(req="SWE1-FOTA-136", spec="CFTS057-4907600", dm=DT, prio="P1",
  item=["The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag . The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.",
        "(Rejection option withheld when the Critical Update flag is set)"],
  pre=[WIFI,
       "2. An update campaign with the Critical Update flag set is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Open the SW Update opt-in screen on the head unit",
        "3. Check that the opt-in screen offers the user no option to reject the deployment"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The SW Update opt-in screen is displayed on the head unit",
      "3. The opt-in screen offers the user no option to reject the deployment"]),
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
        sys.exit(f"T53c：`design_method` 有清單外之值 {bad} —— 停（R-SU40(a)）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T53c —— batch 3 之產出（`Update HMI`，受檢物非交付本）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜Test Set：`{TEST_SET}`｜輸出 `sandbox/{TAG}/`")
    print(f"- `design_method` 四種值**皆經母本清單比對**（不符即停，R-SU40(a)）\n")
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
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["spec"].replace("\n", " ＋ "),
                     t["prio"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 列 | spec_reference | P | PENDING |")
    print("|---|---|---|---|---|---:|")
    for r, tid, req, sp, pr, pd in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` | {pr} | {pd} |")
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜涵蓋 037 列 "
          f"**{len({r[2] for r in rows})}**｜TC **{len(rows)}**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
