#!/usr/bin/env python3
"""T32b —— pilot 批（下放包 19 §四，4 列 → 5 TC）之工作簿產出，供 lint 用。

**本檔為 lint 之受檢物，不是交付本**：輸出落 `sandbox/pilot01/`（R-G25），
`inputs/` 之母本一字不動。TC 內容**逐字取自下放包 19 §四**，
執行層不改寫（T32b：「不得為使其通過而改寫」）。

寫入路徑沿 `scripts/write_back_036.py::_set_row`（R-SU2 之 XML 外科式，
上繳包 16 §5.2 已以實寫探針驗其保全 `<row>` 屬性、儲存格數與 `s=` 樣式）。

TC ID 依 **R-SU24**：`{project}-SU-{NNN}`，`{project}` 取自 036 母本
**D2 實測值**（T32a），不推定。

未寫之欄：`S`（functional_safety —— 其值域未裁，缺項 5）、
`AH`（remarks）。**留空而非填值**，見上繳包 18 §5。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

OUT = FEAT / "sandbox" / "pilot01" / MASTER
TEST_GROUP, TEST_SET = "SW Update", "Silent Update"
AUTHOR = "PeiPYHsu"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"

TCS = [
 dict(req="SWE1-FOTA-175", spec="CFTS057-4907475", dm=FN, prio="P1",
  item=["When the update type is identified as Silent Update, the WiFi Update Service shall automatically execute the update in background mode.",
        "(Silent update runs in background with no HMI interaction)"],
  pre=["1. The head unit is connected to a Wi-Fi network with internet access",
       "2. An update package classified as Silent Update is available on the OTA Server"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Read the update metadata received by the WiFi Update Service and record the update type",
        "3. Record the head unit screen content throughout the update execution",
        "4. Check that the update completes in background and no SW Update HMI prompt or progress notification is displayed"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The recorded update type is Silent Update",
      "3. The head unit screen content throughout the update execution is recorded",
      "4. The update completes in background mode; no SW Update HMI screen, prompt, or progress notification appears on the head unit"]),
 dict(req="SWE1-FOTA-176", spec="CFTS057-4907476", dm=FN, prio="P1",
  item=["During a Silent Update session, the WiFi Update Service shall not trigger the SW Update HMI for update progress notifications.",
        "(No progress notification during a silent session)"],
  pre=["1. The head unit is connected to a Wi-Fi network with internet access",
       "2. An update package classified as Silent Update is available on the OTA Server"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Read the update type received by the WiFi Update Service and record it",
        "3. Record the head unit screen content from download start to installation end",
        "4. Check that no update progress notification is displayed on the head unit during the session"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The recorded update type is Silent Update",
      "3. The head unit screen content from download start to installation end is recorded",
      "4. No update progress notification is displayed on the head unit at any point of the silent session"]),
 dict(req="SWE1-FOTA-176", spec="CFTS057-4907477", dm=FN, prio="P1",
  item=["During a Silent Update session, the WiFi Update Service shall allow user notification only when required to satisfy safety-related requirements.",
        "(Safety-required notification is permitted during a silent session)"],
  pre=["1. The head unit is connected to a Wi-Fi network with internet access",
       "2. An update package classified as Silent Update is available on the OTA Server",
       "3. PENDING: DR-SU1 靜默期間之安全相關通知條件清單"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Read the update type received by the WiFi Update Service and record it",
        "3. PENDING: DR-SU1 觸發一項安全相關條件之步驟",
        "4. Check that the safety-related notification is displayed on the head unit during the silent session"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The recorded update type is Silent Update",
      "3. PENDING: DR-SU1 安全相關條件之成立狀態",
      "4. The safety-related notification is displayed on the head unit while the silent session continues"]),
 dict(req="SWE1-FOTA-177", spec="CFTS057-4907478", dm=NEG, prio="P2",
  item=["If the SW Update HMI is available, the assigned update service shall not present the user with options to opt out of or defer the update.",
        "(No opt-out or defer option offered when HMI is available)"],
  pre=["1. The head unit is connected to a Wi-Fi network with internet access",
       "2. The SW Update HMI is available on the head unit",
       "3. An update package classified as Silent Update is available on the OTA Server"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Read the update type received by the update service and record it",
        "3. Record every SW Update screen displayed on the head unit during the session",
        "4. Check that no screen offers an opt-out control or a defer control to the user"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The recorded update type is Silent Update",
      "3. Every SW Update screen displayed during the session is recorded",
      "4. None of the recorded screens offers an opt-out control or a defer control"]),
 dict(req="SWE1-FOTA-183", spec="CFTS057-4907485", dm=FN, prio="P2",
  item=["When the update completes, the OTA client will display a success notification and what's new details.",
        "(Completion notification with What's New shown after a silent update)"],
  pre=["1. The head unit is connected to a Wi-Fi network with internet access",
       "2. An update package classified as Silent Update is available on the OTA Server"],
  proc=["1. Trigger an update availability check to the OTA Server",
        "2. Wait for the silent update deployment to complete",
        "3. Read the deployment status reported to the update service and record it",
        "4. Check that the head unit displays the update success notification together with the What's New details"],
  er=["1. The update availability check completes and an update is reported as available",
      "2. The silent update deployment completes",
      "3. The recorded deployment status is success",
      "4. The head unit displays the update success notification and the What's New details of the deployed package"]),
]


def project_name():
    """T32a —— 036 母本之專案名稱，實測 D2（標籤 C2）。**不推定**。"""
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(FEAT / "inputs" / MASTER, read_only=True, data_only=True)
    ws = wb[SHEET_NAME]
    label = ws["C2"].value
    val = ws["D2"].value
    return str(val).strip(), str(label).strip()


def main():
    proj, label = project_name()
    src = FEAT / "inputs" / MASTER
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    print("## T32a —— 036 母本之專案名稱（實測）\n")
    print(f"| 儲存格 | 值 |")
    print(f"|---|---|")
    print(f"| `C2`（標籤） | `{label}` |")
    print(f"| **`D2`（值）** | **`{proj}`** |")
    print(f"\n工作表：`{SHEET_NAME}`｜表頭列 {HEADER_ROW}"
          f"｜TC ID 欄為 **F**（`F9` = `Test Case ID 測試用例ID`）\n")

    rows = []
    for n, t in enumerate(TCS, 1):
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TEST_SET,
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + n, vals)
        rows.append((HEADER_ROW + n, tcid, t["req"], t["spec"]))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print(f"## pilot 批之產出（受檢物，非交付本）\n")
    print(f"- 輸出：`sandbox/pilot01/…_ext.xlsx`（R-G25）｜母本未動\n")
    print("| 列 | TC ID | 037 列 | spec_reference |")
    print("|---|---|---|---|")
    for r, tid, req, sp in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` |")
    print(f"\n未寫之欄：`S`（functional_safety，值域未裁）、`AH`（remarks）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
