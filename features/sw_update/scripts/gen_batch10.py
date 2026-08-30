#!/usr/bin/env python3
"""T70h —— batch 10：`TBM Reflash` 14 列（下放包 58 §四）。

**選組依據**（配額窗至 batch 11 已滿足，故依 51 §二 #1 取 105 低者）：

| 判準 | 值 |
|---|---|
| 105 比率 | **7%（1／14）** —— 剩餘各組中最低者（`HU FOTA via TBM` 6% 為 36 列，逾批量上限） |
| 偏向量預估 | **18 pt**（現 14 pt）—— **取低 105 之組必然使其上升**，見上繳包 58 §4.1 |
| 機制 3 攔下 | **0 列** —— 本組錨定風險最低 |
| 批量 | 14（12–20） |

**型別**：
- **第二型**：`111`（TBM 存在與否之允許無獨立外部面）、`114` 之參數化半段
- **第三型**：`124` —— 其動作與 `123` 完全相同，差在內部狀態值
- **第四型**：`118`（forced campaign）、`120`／`122`（更新失敗之注入）
- **可寫**：`112`／`113`／`115`／`116`／`117`／`119`／`121`／`123`
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch10"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 136
TS = "TBM Reflash"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"
FI = "基礎故障注入 (Fault Injection Lite)"

B = "1. The vehicle is in Body ON mode"
TBM = "2. The telematics box module is fitted to the vehicle"
TBM2 = "3. The telematics box module is reported as present"
CAMP = "3. A TBM firmware update is staged on the OTA Server for this vehicle"
REC = "2. Record the head unit screen content as continuous video capture until the check in the final step is completed"
ER_REC = "2. The head unit screen content until the check in the final step is completed is recorded as continuous video capture"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-111", "CFTS057-4907776", FN, "P2", "低",
  "**第二型**＋**105 列**：`allow execution` 為內部之允許，其外部後果即 `112`–`124` 之全部，本身無獨立表徵；且移除 TBM 之負向面不可佈置",
  "If $TBM_present$ = [present], the TBM Update Service shall allow execution of TBM-specific FOTA functionalities.",
  "TBM-specific FOTA functions are allowed while the TBM is present",
  [B, TBM, TBM2,
   "3. PENDING: DR-SU2 means of observing that TBM-specific FOTA functionality is allowed, separately from any single TBM FOTA screen",
   "4. PENDING: DR-SU2 means of placing the vehicle in a state where $TBM_present$ does not report the present state"],
  ["1. Read the state reported on $TBM_present$ and record it",
   "2. PENDING: DR-SU2 step to read whether TBM-specific FOTA functionality is allowed"],
  ["1. $TBM_present$ reports the present state",
   "2. PENDING: DR-SU2 observable evidence that TBM-specific FOTA functionality is allowed"]),

 tc("SWE1-FOTA-112", "CFTS057-4907780", FN, "P1", "中",
  "判定核心取彈窗**所載之二項 metadata**（估計安裝時間與 What's New），使其與 `113` 之區分不繫於觸發條件",
  "The TBM Update Service shall retrieve update metadata, including estimated installation time and “What’s New” information, via the TBM FW Service.",
  "TBM update pop-up carries the estimated installation time and What's New text",
  [B, TBM, TBM2, CAMP],
  ["1. Trigger an update availability check for the telematics box module",
   REC,
   "3. Check that the TBM FOTA update available pop-up shows an estimated installation time and What's New information"],
  ["1. The update availability check for the telematics box module completes",
   ER_REC,
   "3. The recorded screen content shows the TBM FOTA update available pop-up carrying an estimated installation time and What's New information"]),

 tc("SWE1-FOTA-113", "CFTS057-4907783", FN, "P1", "中",
  "與 `112` 之別在**觸發條件**：本列驗 Body ON → Body OFF 之轉換，`112` 驗彈窗之內容",
  "If $TBMupdate$ = [Update_Available] and OperationalModeSts transitions from Body ON to Body OFF, the TBM Update Service shall notify the TBM FOTA HMI.",
  "Pop-up appears at the Body ON to Body OFF transition",
  [B, TBM, TBM2, CAMP,
   "4. The TBM FOTA update available pop-up is not currently displayed"],
  ["1. Trigger an update availability check for the telematics box module and leave the vehicle in Body ON mode",
   REC,
   "3. Switch the vehicle from Body ON mode to Body OFF mode",
   "4. Check that the TBM FOTA update available pop-up is displayed after the change to Body OFF mode"],
  ["1. The update availability check completes while the vehicle stays in Body ON mode",
   ER_REC,
   "3. The vehicle is switched from Body ON mode to Body OFF mode",
   "4. The recorded screen content shows the TBM FOTA update available pop-up after the change to Body OFF mode"]),

 tc("SWE1-FOTA-114", "CFTS057-4907784", BV, "P1", "低",
  "**門檻列**（`360 seconds` 逐字取自 037）；其後半（軟體參數化之可組態）於外部無面，掛 `PENDING`",
  "The default estimated update duration shall be 360 seconds.",
  "Displayed estimated duration is 360 seconds before any parameterization",
  [B, TBM, TBM2, CAMP,
   "4. The estimated update duration has not been changed by software parameterization",
   "5. PENDING: DR-SU2 means of changing the estimated update duration through software parameterization"],
  ["1. Trigger an update availability check for the telematics box module",
   REC,
   "3. Read the estimated update duration shown on the head unit and record it as Duration_shown",
   "4. Check that Duration_shown is 360 seconds"],
  ["1. The update availability check for the telematics box module completes",
   ER_REC,
   "3. Duration_shown is recorded",
   "4. Duration_shown is 360 seconds"]),

 tc("SWE1-FOTA-115", "CFTS057-4907785", FN, "P1", "中",
  "`$UpdateAction$` 之設值於外部無面，為統攝殘餘（R-SU37 v2）；判定核心取彈窗關閉後更新隨即開始",
  "The TBM FOTA HMI shall capture user selection when the “Update Now” option is selected and notify the TBM Update Service.",
  "Selecting Update Now starts the telematics box module update",
  [B, TBM, TBM2, CAMP,
   "4. The TBM FOTA update available pop-up is displayed on the head unit"],
  ["1. Select the “Update Now” option on the TBM FOTA update available pop-up",
   REC,
   "3. Check that the head unit shows the telematics box module update starting after the “Update Now” selection"],
  ["1. The “Update Now” option is selected on the TBM FOTA update available pop-up",
   ER_REC,
   "3. The recorded screen content shows the telematics box module update starting after the “Update Now” selection"]),

 tc("SWE1-FOTA-116", "CFTS057-4907786", FN, "P1", "中",
  "⚠ 037 之三個使用者動作（`Update Later`／忽略／關閉）為**三個可獨立觸發之情境**，本 TC 取 `Update Later`；其餘二者為未覆蓋之 facet，記入 COVERAGE_GAPS",
  "The TBM FOTA HMI shall capture user interaction when the user selects “Update Later,” ignores, or closes the update pop-up.",
  "Selecting Update Later leaves the telematics box module update unstarted",
  [B, TBM, TBM2, CAMP,
   "4. The TBM FOTA update available pop-up is displayed on the head unit"],
  ["1. Select the “Update Later” option on the TBM FOTA update available pop-up",
   REC,
   "3. Check that the head unit shows no telematics box module update starting after the “Update Later” selection"],
  ["1. The “Update Later” option is selected on the TBM FOTA update available pop-up",
   ER_REC,
   "3. The recorded screen content shows no telematics box module update starting after the “Update Later” selection"]),

 tc("SWE1-FOTA-117", "CFTS057-4907787", FN, "P1", "中",
  "⚠ 037 該列之句尾併入了一段 `$OperationalModeSts$` 之取值註腳（含 `Iginiton` 之拼寫殘留）—— 登 D-7；`test_item` 上半只取其規範句，逐字",
  "If $TBMupdate$ = [Update_start] and $OperationalModeSts$ indicates Body OFF, the TBM Update Service shall notify the TBM FOTA HMI.",
  "Update screen appears once the update starts with the vehicle in Body OFF",
  [B, TBM, TBM2, CAMP,
   "4. The “Update Now” option has been selected on the TBM FOTA update available pop-up"],
  ["1. Switch the vehicle to Body OFF mode",
   REC,
   "3. Check that the head unit displays the telematics box module update screen after the update has started in Body OFF mode"],
  ["1. The vehicle is switched to Body OFF mode",
   ER_REC,
   "3. The recorded screen content shows the telematics box module update screen after the update has started in Body OFF mode"]),

 tc("SWE1-FOTA-118", "CFTS057-4907788", FN, "P1", "低",
  "**第四型**：`Forced_Update` 之 campaign 不可佈置；其畫面本身可觀測",
  "If $TBMupdate$ = [Forced_Update] and $OperationalModeSts$ indicates Body OFF, the TBM Update Service shall notify the TBM FOTA HMI.",
  "Forced update screen appears for a forced campaign in Body OFF",
  [B, TBM, TBM2,
   "3. PENDING: DR-SU2 means of staging a forced telematics box module update campaign on the OTA Server"],
  ["1. PENDING: DR-SU2 step to stage a forced telematics box module update campaign",
   "2. Switch the vehicle to Body OFF mode",
   "3. PENDING: DR-SU2 check that the head unit displays the forced telematics box module update screen"],
  ["1. PENDING: DR-SU2 observable evidence that a forced telematics box module update campaign is staged",
   "2. The vehicle is switched to Body OFF mode",
   "3. PENDING: DR-SU2 observable evidence of the forced telematics box module update screen"]),

 tc("SWE1-FOTA-119", "CFTS057-4907790", FN, "P1", "中",
  "與 `121` 之別在 **UI 元件**：本列驗成功**彈窗**，`121` 驗結束**畫面**。二者之觸發條件相同（`Update_End`）",
  "Upon detecting $TBMUpdate$ = [Update_End], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM update success pop-up.",
  "Success pop-up appears when the update completes",
  [B, TBM, TBM2, CAMP,
   "4. A telematics box module update has been started with the “Update Now” option"],
  ["1. Wait until the telematics box module update completes",
   REC,
   "3. Check that the head unit displays the telematics box module update success pop-up"],
  ["1. The telematics box module update completes",
   ER_REC,
   "3. The recorded screen content shows the telematics box module update success pop-up"]),

 tc("SWE1-FOTA-120", "CFTS057-4907812", FI, "P1", "低",
  "**第四型**：更新失敗之注入手段不可得；回復成功之彈窗本身可觀測",
  "Upon detecting $TBMUpdate$ = [Update_Fail], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the rollback success pop-up.",
  "Rollback success pop-up appears when the update fails",
  [B, TBM, TBM2, CAMP,
   "4. PENDING: DR-SU2 means of making a telematics box module update fail during its installation"],
  ["1. Start a telematics box module update with the “Update Now” option",
   "2. PENDING: DR-SU2 step to make the telematics box module update fail during its installation",
   "3. PENDING: DR-SU2 check that the head unit displays the rollback success pop-up after the failure"],
  ["1. The telematics box module update starts",
   "2. PENDING: DR-SU2 observable evidence that the telematics box module update failed",
   "3. PENDING: DR-SU2 observable evidence of the rollback success pop-up after the failure"]),

 tc("SWE1-FOTA-121", "CFTS057-4907793", FN, "P2", "中",
  "與 `119` 之別在 **UI 元件**：本列驗結束**畫面**，`119` 驗成功**彈窗**",
  "Upon detecting $TBMupdate$ = [Update_End], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM update end screen.",
  "End screen appears when the update completes",
  [B, TBM, TBM2, CAMP,
   "4. A telematics box module update has been started with the “Update Now” option"],
  ["1. Wait until the telematics box module update completes",
   REC,
   "3. Check that the head unit displays the telematics box module update end screen"],
  ["1. The telematics box module update completes",
   ER_REC,
   "3. The recorded screen content shows the telematics box module update end screen"]),

 tc("SWE1-FOTA-122", "CFTS057-4907812", FI, "P2", "低",
  "**第四型**（同 `120` 之注入）；與 `120` 之別在 UI 元件（失敗**畫面** vs 回復成功**彈窗**）",
  "Upon detecting $TBMupdate$ = [Update_Fail], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM update failure screen.",
  "Failure screen appears when the update fails",
  [B, TBM, TBM2, CAMP,
   "4. PENDING: DR-SU2 means of making a telematics box module update fail during its installation"],
  ["1. Start a telematics box module update with the “Update Now” option",
   "2. PENDING: DR-SU2 step to make the telematics box module update fail during its installation",
   "3. PENDING: DR-SU2 check that the head unit displays the telematics box module update failure screen"],
  ["1. The telematics box module update starts",
   "2. PENDING: DR-SU2 observable evidence that the telematics box module update failed",
   "3. PENDING: DR-SU2 observable evidence of the telematics box module update failure screen"]),

 tc("SWE1-FOTA-123", "CFTS057-4907796", FN, "P2", "中",
  "與 `124` 之別**只在內部狀態值**（`No_Updates_Available` vs `No_Update`），其動作逐字相同 —— 本列為可寫者，`124` 掛第三型",
  "Upon detecting$TBMUpdate$ = [No_Updates_Available], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall clear all active TBM FOTA-related pop-ups and status bar displays.",
  "TBM FOTA pop-ups and status bar entries are cleared when no update is available",
  [B, TBM, TBM2,
   "3. No telematics box module update is staged on the OTA Server for this vehicle",
   "4. A TBM FOTA pop-up and a TBM FOTA status bar entry are displayed on the head unit"],
  ["1. Trigger an update availability check for the telematics box module",
   REC,
   "3. Check that the head unit shows no TBM FOTA pop-up and no TBM FOTA status bar entry after the check completes"],
  ["1. The update availability check for the telematics box module completes with no update available",
   ER_REC,
   "3. The recorded screen content shows no TBM FOTA pop-up and no TBM FOTA status bar entry after the check completes"]),

 tc("SWE1-FOTA-124", "CFTS057-4907797", FN, "P2", "低",
  "⚠ **第三型**：其所令之動作與 `123` **逐字相同**（清除全部 TBM FOTA 彈窗與狀態列），其差為 `$TBMUpdate$` 之二個值 —— 而該值於外部無表徵。入 DR-SU2(c)",
  "Upon detecting $TBMUpdate$ = [No_Update], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall clear all active TBM FOTA-related pop-ups and status bar displays.",
  "Clearing is driven by the No_Update state rather than by No_Updates_Available",
  [B, TBM, TBM2,
   "3. A TBM FOTA pop-up and a TBM FOTA status bar entry are displayed on the head unit",
   "4. PENDING: DR-SU2 means of distinguishing the No_Update state from the No_Updates_Available state on the head unit"],
  ["1. Trigger an update availability check for the telematics box module",
   "2. PENDING: DR-SU2 step to bring $TBMUpdate$ to the No_Update state rather than to the No_Updates_Available state"],
  ["1. The update availability check for the telematics box module completes",
   "2. PENDING: DR-SU2 observable evidence distinguishing this clearing from the one verified for SWE1-FOTA-123"]),
]

LOW_REASONS = {
 "SWE1-FOTA-111": [("允許之本身無獨立外部面", True), ("TBM 不存在之狀態不可佈置", True)],
 "SWE1-FOTA-114": [("參數化之組態無外部面", True)],
 "SWE1-FOTA-118": [("forced campaign 不可佈置", True)],
 "SWE1-FOTA-120": [("更新失敗不可注入", True)],
 "SWE1-FOTA-122": [("更新失敗不可注入", True)],
 "SWE1-FOTA-124": [("與 `123` 不可區辨", True)],
}
MECH3 = []


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T70h：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T70h：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T70h —— batch 10 之產出（`TBM Reflash`，14 列）\n")
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
        pre = [re.sub(r"^\d+\.\s*", "", s) for s in t["pre"]]
        t["pre"] = [f"{k}. {s}" for k, s in enumerate(pre, 1)]
        vals["J"] = "\n".join(t["pre"])
        pend = sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])
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
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    union = sorted({i for i, _, _ in keep} | set(mid))
    deliverable = [r for r in rows if r[4] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- 可排除之 `低`：{len(excl)} 列｜機制 3 攔下：**0 列**（本組錨定風險最低）")
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— " + "、".join(f"**{r}**" for r in un))
    print(f"- **抽驗組成 = {len(union)} 列**")
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
