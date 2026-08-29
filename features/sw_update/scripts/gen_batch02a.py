#!/usr/bin/env python3
"""T47b —— batch 2a（下放包 33 §四、下放包 34 §三）之工作簿產出。

`Interruption Handling` 之探針批：`315`–`320` 六列 + 統攝列 `313`。

TC 內容**逐字取自下放包 33 §四**，執行層不改寫（T32b）。
下放包 34 §三之**唯一更正**已套用：`design_method` 由
`故障注入 (Fault Injection)`（**不在母本清單內**）改為母本
`下拉選單!$A$9` 之逐字值 —— **不自譯、不自造格式**（R-SU40）。

**四型之分佈**（本批首次出現第四型）：

- `011`（`315`）／`014`（`318`）—— **第四型：觸發手段不可得**（R-SU39）。
  其外部後果**可觀測**（版本未變、HU 可操作），缺者為**使該條件發生之手段**。
  DR 之請求為**觸發手段**，非觀測手段。
- `017`（`313`）—— **統攝列，餘量為空**（R-SU37 v2(b)）。全欄掛 `DR-SU3`，
  其請求為**需求單元之合併確認**，與 DR-SU2 不同類。
- `012`／`013`／`015`／`016` —— 可寫。

**範圍紀律（IN §8.2.1）**：本六列所擁有者為「偵測並處理該中斷條件」；
**中斷解除後之復原屬 `321`（`4907673`），本批不涵蓋** ——
故 ER 之終點為「更新未完成且系統未損毀」，不寫「恢復後續行」。

預期 lint：**U=9**（`011` 3 + `014` 3 + `017` 3）。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch02a"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP, TEST_SET = "SW Update", "Interruption Handling"
AUTHOR = "PeiPYHsu"
START_N = 11                       # batch 1 已用 001–010

# R-SU40：**逐字取自母本 `下拉選單!$A$9`**，於 main() 以實測覆核
FI_LITE = "基礎故障注入 (Fault Injection Lite)"

PRE_STD = [
    "1. The head unit is connected to a Wi-Fi network with internet access",
    "2. An update package with update type Silent Update is staged on the OTA Server for this head unit",
]
TAIL = ["4. Read the software version shown on the head unit and record it as Version_after",
        "5. Check that Version_after equals Version_initial and that the head unit remains operable"]
ER_TAIL = ["4. Version_after is recorded",
           "5. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input"]

TCS = [
 dict(req="SWE1-FOTA-315", spec="CFTS057-4907667", prio="P1",
  item=["The SWMC shall detect and handle socket read/write errors during OTA server communication, flashing, or software component update, and shall report the error status to WiFiUpdateService.",
        "(Socket read or write error during an update session)"],
  pre=PRE_STD + ["3. PENDING: DR-SU2 means of injecting a socket read or write error during OTA server communication"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. PENDING: DR-SU2 step to inject a socket read or write error during the update session"] + TAIL,
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. PENDING: DR-SU2 observable evidence that the socket error has occurred"] + ER_TAIL),
 dict(req="SWE1-FOTA-316", spec="CFTS057-4907668", prio="P1",
  item=["The SWMC shall detect network loss conditions, including network errors, no data coverage, loss of Wi-Fi connection, phone tether disconnection, and embedded modem roaming, during OTA server communication, flashing, or software component update, and shall report the network loss status to WiFiUpdateService.",
        "(Wi-Fi access point switched off during an update session)"],
  pre=PRE_STD,
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Switch off the Wi-Fi access point while the update session is in progress"] + TAIL,
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. The Wi-Fi access point is switched off and the head unit shows no Wi-Fi connection"] + ER_TAIL),
 dict(req="SWE1-FOTA-317", spec="CFTS057-4907669", prio="P1",
  item=["The WiFiUpdateService shall handle user-initiated deactivation of mobile data usage or an active Wi-Fi connection reported by SWMC during OTA server communication, flashing, or software component update.",
        "(User switches off the Wi-Fi connection during an update session)"],
  pre=PRE_STD,
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Switch off the Wi-Fi connection in the head unit settings while the update session is in progress"] + TAIL,
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. The Wi-Fi connection is switched off and the head unit settings show Wi-Fi as disabled"] + ER_TAIL),
 dict(req="SWE1-FOTA-318", spec="CFTS057-4907670", prio="P1",
  item=["The WiFiUpdateService shall handle the vehicle emergency state (accident detection) notified by the appropriate system component during OTA server communication, flashing, or software component update.",
        "(Vehicle enters emergency state during an update session)"],
  pre=PRE_STD + ["3. PENDING: DR-SU2 means of placing the vehicle into the emergency state (accident detection) on the test bench"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. PENDING: DR-SU2 step to place the vehicle into the emergency state while the update session is in progress"] + TAIL,
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. PENDING: DR-SU2 observable evidence that the vehicle is in the emergency state"] + ER_TAIL),
 # `319` —— test_item 上半 verbatim 保留 D-1 之缺字（`the handling of condition`）
 dict(req="SWE1-FOTA-319", spec="CFTS057-4907671", prio="P1",
  item=["The WiFiUpdateService shall coordinate the handling of condition during OTA server communication, flashing, or software component update by interacting with SWMC and the appropriate installer component.",
        "(Power loss during an update session)"],
  pre=PRE_STD,
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Disconnect the head unit battery supply while the update session is in progress",
        "4. Reconnect the battery supply and wait until the head unit completes start-up",
        "5. Read the software version shown on the head unit and record it as Version_after",
        "6. Check that Version_after equals Version_initial and that the head unit remains operable"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. The head unit powers off",
      "4. The head unit completes start-up and its home screen is displayed",
      "5. Version_after is recorded",
      "6. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input"]),
 dict(req="SWE1-FOTA-320", spec="CFTS057-4907672", prio="P1",
  item=["The WiFiUpdateService shall detect end-user physical disconnection of the host system (HU/TBM) during OTA server communication, flashing, or software component update and notify SWMC.",
        "(Host system physically disconnected during an update session)"],
  pre=PRE_STD,
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server",
        "3. Physically disconnect the host system connector while the update session is in progress",
        "4. Reconnect the host system connector and wait until the head unit completes start-up",
        "5. Read the software version shown on the head unit and record it as Version_after",
        "6. Check that Version_after equals Version_initial and that the head unit remains operable"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and an update is reported as available",
      "3. The head unit loses the host system connection",
      "4. The head unit completes start-up and its home screen is displayed",
      "5. Version_after is recorded",
      "6. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input"]),
 # `313` —— 統攝列，餘量為空（R-SU37 v2(b)）；全欄 PENDING: DR-SU3
 dict(req="SWE1-FOTA-313",
      spec="CFTS057-4907667 / 4907668 / 4907669 / 4907670 / 4907671 / 4907672",
      prio="P1",
  item=["The WiFiUpdateService shall coordinate the handling of the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 by interacting with SWMC and the appropriate installer component during the software update process.",
        "(Coordination of the six interruption conditions across the update process)"],
  pre=PRE_STD + ["3. PENDING: DR-SU3 upstream confirmation whether this requirement's verification is covered by the six conditions it coordinates"],
  proc=["1. PENDING: DR-SU3 step to exercise the coordination behaviour separately from the six individual conditions"],
  er=["1. PENDING: DR-SU3 observable outcome attributable to the coordination behaviour alone"]),
]


def dropdown_a9():
    """R-SU40(a)：`design_method` 之值**逐字取自母本清單實測**，不推定。"""
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(FEAT / "inputs" / MASTER, read_only=True, data_only=True)
    return str(wb["下拉選單"]["A9"].value)


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()

    a9 = dropdown_a9()
    if a9 != FI_LITE:
        sys.exit(f"T47b：`下拉選單!$A$9` 實測為 {a9!r}，"
                 f"與本檔所寫之 {FI_LITE!r} 不符 —— 停並回報（R-SU40(a)）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T47b —— batch 2a 之產出（受檢物，非交付本）\n")
    print(f"- 專案名稱（實測 `D2`）：**`{proj}`**｜輸出 `sandbox/{TAG}/`（母本未動）")
    print(f"- **`design_method` 逐字取自 `下拉選單!$A$9`**：`{a9}` "
          f"—— 產出前已比對，不符即停（R-SU40(a)）\n")

    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TEST_SET,
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": a9,
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["spec"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    TYPE = {"SWE1-FOTA-315": "**第四型**（觸發手段不可得，R-SU39）",
            "SWE1-FOTA-318": "**第四型**（觸發手段不可得，R-SU39）",
            "SWE1-FOTA-313": "**統攝列・餘量為空**（R-SU37 v2(b)），DR-SU3",
            }
    print("| 列 | TC ID | 037 列 | spec_reference | PENDING | 型 |")
    print("|---|---|---|---|---:|---|")
    for r, tid, req, sp, pd in rows:
        print(f"| {r} | `{tid}` | `{req}` | `{sp}` | {pd} | {TYPE.get(req, '可寫')} |")
    print(f"\n- **PENDING 合計 {sum(r[4] for r in rows)}**"
          f"（`011` 之 3 + `014` 之 3 + `017` 之 3）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
