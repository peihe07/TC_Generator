#!/usr/bin/env python3
"""T72f —— batch 12：`Update Agent` 14 列（下放包 60 §四）。

**窗（batch 11–13）目標 42%｜本批 105 比率 57%（8／14）｜窗內累計見上繳包 60 §4。**

**⚠ 本批之特徵：其多數列所述者為「安裝機制之能力」而非「一次可觀察之行為」**
—— 能力之否定（「永不 brick」）不可由任一次執行證實，
**其判定核心若寫成肯定式即為 R-SU43(f) 所指之「永遠通過之 ER」。**

**型別**：
- **可寫**：`380`（斷電可注入，其後果為析取式：回復或安全終止）
- **第二型**：`370`／`371`／`372`／`373`／`374`／`381`／`383`
- **第四型**：`376`（UA 自身之 campaign 不可佈置）、`377`／`378`
- **不可判定之全稱否定**（R-SU43(f)）：`375`／`379`／`382` 之後半
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch12"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 166
TS = "Update Agent"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
FI = "基礎故障注入 (Fault Injection Lite)"

B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, ts=TS, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 tc("SWE1-FOTA-370", "CFTS057-4907539", FN, "P2", "低",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.256）：部署方式之組態於車機無表徵",
  "The WiFiUpdateService shall provide the configuration that defines the update deployment method to be used for each target module.",
  "Deployment method configuration is provided per target module",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of reading the update deployment method configured for each target module"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read the deployment method configured for each target module"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the deployment method configured for each target module"]),

 tc("SWE1-FOTA-371", "CFTS057-4907483", FN, "P2", "低",
  "**第二型**＋⚠ 錨為機制 3 攔下之首選（0.174，至今最低）；**與 `169`（batch 11）重複表述** —— 皆為「依 metadata 選定安裝器」，入 DR-SU3",
  "The WiFiUpdateService shall identify the target components for update and select the appropriate installer for each target based on the deployment metadata.",
  "Installer is selected per target component from the deployment metadata",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of reading which installer was selected for each target component",
   "PENDING: DR-SU2 means of distinguishing this selection from the dispatch verified by SWE1-FOTA-169"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read the installer selected for each target component"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence distinguishing this selection from the dispatch verified for SWE1-FOTA-169"]),

 tc("SWE1-FOTA-372", "CFTS057-4907537", FN, "P2", "低",
  "**第二型**＋**105 列**：相依序之驗證與安裝順序皆在服務內部",
  "The WiFiUpdateService shall ensure that software components are installed in the correct order based on their defined dependencies.",
  "Components are installed in their dependency order",
  [B, WIFI, "An update package containing at least two dependent components is staged on the OTA Server",
   "PENDING: DR-SU2 means of reading the order in which the components of a deployment package are installed"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read the order in which the components were installed"],
  ["1. The update is accepted and the installation runs on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the components were installed in their dependency order"]),

 tc("SWE1-FOTA-373", "CFTS057-4907333", FN, "P2", "低",
  "**第二型**＋**105 列**＋⚠ 錨為機制 3 攔下之首選（0.234）：progress API 為程式介面，其外部表徵（畫面之進度）屬他列",
  "The SW updater HAL and FW shall provide an update progress API to retrieve the progress of IOC, GNSS, and tuner update",
  "Progress API returns the progress of the IOC, GNSS and tuner updates",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of calling the update progress API of the SW updater HAL and FW"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the installation start",
   "2. PENDING: DR-SU2 step to call the update progress API for the IOC, GNSS and tuner updates"],
  ["1. The installation starts on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the progress API returned the progress of the IOC, GNSS and tuner updates"]),

 tc("SWE1-FOTA-374", "CFTS057-4907535", FN, "P3", "低",
  "**第二型**＋**105 列**：API 介面之存在為設計事實，**其於系統測層級無任何表徵**",
  "The Redbend SWMC shall provide a platform-independent API interface to enable integration with the Update Agent (UA) for OTA update operations.",
  "Platform-independent API for Update Agent integration exists",
  [B, WIFI,
   "PENDING: DR-SU2 means of observing the API interface provided by the Redbend SWMC to the Update Agent"],
  ["1. PENDING: DR-SU2 step to read the API interface provided by the Redbend SWMC for Update Agent integration"],
  ["1. PENDING: DR-SU2 observable evidence of the API interface provided for Update Agent integration"]),

 tc("SWE1-FOTA-375", "CFTS057-4907534", FN, "P1", "低",
  "⚠ **R-SU43(f) 之案例**：`identical to the reference deployment image` 之比對需取出已安裝之映像，其手段不可得；**若改寫為「版本相同」則該 ER 永遠通過**（版本本來就會相同）",
  "The WIFI update service shall ensure that the installed software image for a given target version is identical to the reference deployment image provided by the OTA server, so that the updated unit is equivalent to a freshly provisioned unit for the same target version.",
  "Installed image is identical to the reference image for the same version",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of extracting the installed software image from the head unit",
   "PENDING: DR-SU2 means of obtaining the reference deployment image for the same target version"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let it complete",
   "2. PENDING: DR-SU2 step to extract the installed software image and compare it with the reference deployment image"],
  ["1. The update completes on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the installed image is identical to the reference deployment image"]),

 tc("SWE1-FOTA-376", "CFTS057-4907309", FN, "P1", "低",
  "**第四型**＋**105 列**：Update Agent 自身之 campaign 不可佈置",
  "The Redbend SWMC shall support the ability to update its own software components (Update Agent) through the OTA update mechanism.",
  "Update Agent updates itself through the OTA mechanism",
  [B, WIFI,
   "PENDING: DR-SU2 means of staging a campaign whose target is the Update Agent itself",
   "PENDING: DR-SU2 means of reading the Update Agent version on the head unit"],
  ["1. PENDING: DR-SU2 step to stage a campaign whose target is the Update Agent itself",
   "2. PENDING: DR-SU2 step to read the Update Agent version before and after the update"],
  ["1. PENDING: DR-SU2 observable evidence that a campaign targeting the Update Agent is staged",
   "2. PENDING: DR-SU2 observable evidence that the Update Agent version changed after the update"]),

 tc("SWE1-FOTA-377", "CFTS057-4907527", FN, "P1", "低",
  "**第四型**：A/B 之槽位切換於車機無表徵，且選用 A/B 之組態不可佈置",
  "The WiFiUpdateService shall select the A/B update mechanism for applicable target components based on update configuration and it shall support the A/B update mechanism to ensure safe updates and prevent permanent disabling of target components such as IOC and SOC.",
  "A/B mechanism is selected for the components configured for it",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of configuring a target component to use the A/B update mechanism",
   "PENDING: DR-SU2 means of observing which slot a component was installed into"],
  ["1. PENDING: DR-SU2 step to configure a target component to use the A/B update mechanism",
   "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "3. PENDING: DR-SU2 step to read which slot the component was installed into"],
  ["1. PENDING: DR-SU2 observable evidence that the component is configured for the A/B mechanism",
   "2. The update is accepted and the installation runs on the head unit",
   "3. PENDING: DR-SU2 observable evidence of the slot the component was installed into"]),

 tc("SWE1-FOTA-378", "CFTS057-4907526", FI, "P1", "低",
  "**第四型**＋**與 DR-SU4 同族**：`consistent state` 之判準與 Table 4-6 之階段界線同一問題",
  "The WifiUpdate service shall implement a failsafe mechanism to handle update interruptions to ensure the system can recover to a consistent state and installers also shall about to support for the recovery mechanism.",
  "System returns to a consistent state after an interrupted update",
  [B, WIFI, PKG,
   "PENDING: DR-SU4 criterion by which a consistent state is judged after an interrupted update"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the installation start",
   "2. Switch the vehicle power off while the installation is running",
   "3. Switch the vehicle power on again and read the software version shown on the head unit",
   "4. PENDING: DR-SU4 check that the head unit is in a consistent state after the interrupted installation"],
  ["1. The installation starts on the head unit",
   "2. The vehicle power is switched off while the installation is running",
   "3. The software version shown after the power is switched on again is recorded",
   "4. PENDING: DR-SU4 observable evidence that the head unit is in a consistent state"]),

 tc("SWE1-FOTA-379", "CFTS057-4907527", FN, "P1", "低",
  "⚠ **R-SU43(f) 之案例**：`prevent … from becoming permanently disabled` 為**全稱否定** —— 任一次執行皆不能證實它，**其肯定式 ER 永遠通過**",
  "The Redbend Update Agent shall implement update safety mechanisms to prevent SOC components from becoming permanently disabled (“bricked”) during the update process.",
  "SOC is not permanently disabled by an update",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 criterion by which the safety mechanism is judged present in one bench run"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the installation run",
   "2. PENDING: DR-SU2 step to exercise the safety mechanism that prevents the SOC from being permanently disabled"],
  ["1. The installation runs on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the safety mechanism prevented the SOC from being permanently disabled"]),

 tc("SWE1-FOTA-380", "CFTS057-4907526", FI, "P1", "中",
  "**本批唯一可寫之列**：斷電可注入，其後果為**析取式**（回復或安全終止）—— 依 R-SU43 v2，ER 不得只斷言其一",
  "The Redbend Update Agent shall implement a recovery mechanism to resume or safely terminate SOC updates in the event of power failure, communication loss, or any other interruption during the update process.",
  "After a power cut the update either resumes or ends without leaving the unit unusable",
  [B, WIFI, PKG,
   "The vehicle power supply can be cut and restored at the bench"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the installation start",
   "2. Cut the vehicle power supply while the installation is running",
   "3. Restore the vehicle power supply and wait until the head unit has started",
   "4. Check that the head unit starts and either shows the installation continuing or shows the software version it held before the update"],
  ["1. The installation starts on the head unit",
   "2. The vehicle power supply is cut while the installation is running",
   "3. The vehicle power supply is restored and the head unit starts",
   "4. The head unit starts and either shows the installation continuing or shows the software version it held before the update"]),

 tc("SWE1-FOTA-381", "CFTS057-4907525", FN, "P3", "低",
  "**第二型**＋**105 列**＋**值未載**：`smallest approved differential technology, as configured by FCA approval` —— 其所核准之技術清單 037 未載",
  "The Redbend Update Agent shall support the use of the smallest approved differential update technology, as configured by FCA approval, in order to minimize data usage and update time.",
  "Approved differential update technology is used",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 list of differential update technologies approved by FCA and the configuration that selects one",
   "PENDING: DR-SU2 means of reading which differential technology was used for a deployment package"],
  ["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
   "2. PENDING: DR-SU2 step to read which differential update technology was used"],
  ["1. The update is accepted on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the differential update technology that was used"]),

 tc("SWE1-FOTA-382", "CFTS057-4907517", NEG, "P1", "低",
  "其前半**與 `172`（batch 6）重複**（來源版本不符即拒絕）；其後半為 R-SU43(f) 之案例（結果映像與目標映像之比對不可得）",
  "The WiFi update service shall verify that the resulting firmware image after applying a differential update matches the target firmware image defined in the update package by validating the integrity information (such as hash, checksum, or digital signature) provided in the update package.",
  "Resulting image is checked against the target image of the package",
  [B, WIFI, "A differential update package is staged on the OTA Server for this head unit",
   "PENDING: DR-SU2 means of reading the integrity information validated after a differential update is applied"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let the differential update be applied",
   "2. PENDING: DR-SU2 step to read the integrity information validated for the resulting firmware image"],
  ["1. The differential update is applied on the head unit",
   "2. PENDING: DR-SU2 observable evidence that the resulting firmware image was validated against the target image"]),

 tc("SWE1-FOTA-383", "CFTS057-4907516", FN, "P2", "低",
  "**第二型**＋**105 列**：安裝後之有效性驗證在服務內部，其外部後果（成功通知）屬 `183`",
  "For SOC, Redbend Update Agent shall verify the validity of the deployed software after installation to ensure that the software has been correctly and successfully applied.",
  "Deployed SOC software is verified after installation",
  [B, WIFI, PKG,
   "PENDING: DR-SU2 means of observing the validity check the Update Agent performs after installation"],
  ["1. Trigger an update availability check to the OTA Server, accept the update and let it complete",
   "2. PENDING: DR-SU2 step to read the result of the validity check performed after the installation"],
  ["1. The update completes on the head unit",
   "2. PENDING: DR-SU2 observable evidence of the validity check performed after the installation"]),
]

LOW_REASONS = {
 "SWE1-FOTA-370": [("組態無外部面", True), ("錨為機制 3 攔下之首選（0.256）", False)],
 "SWE1-FOTA-371": [("選定無外部面", True), ("與 `169` 不可區辨", True),
                   ("錨為機制 3 攔下之首選（0.174）", False)],
 "SWE1-FOTA-372": [("安裝順序無外部面", True)],
 "SWE1-FOTA-373": [("API 無外部面", True), ("錨為機制 3 攔下之首選（0.234）", False)],
 "SWE1-FOTA-374": [("介面之存在無系統測表徵", True)],
 "SWE1-FOTA-375": [("已安裝映像不可取出", True)],
 "SWE1-FOTA-376": [("UA 自身之 campaign 不可佈置", True)],
 "SWE1-FOTA-377": [("A/B 之組態與槽位皆無外部面", True), ("錨為機制 3 攔下之首選（0.200）", False)],
 "SWE1-FOTA-378": [("`consistent state` 無判準（DR-SU4）", True), ("錨為機制 3 攔下之首選（0.259）", False)],
 "SWE1-FOTA-379": [("全稱否定不可由單次執行證實", True)],
 "SWE1-FOTA-381": [("核准技術清單未載", True)],
 "SWE1-FOTA-382": [("完整性資訊不可讀", True)],
 "SWE1-FOTA-383": [("驗證在服務內部", True)],
}
MECH3 = ["SWE1-FOTA-370", "SWE1-FOTA-371", "SWE1-FOTA-373",
         "SWE1-FOTA-377", "SWE1-FOTA-378"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T72f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T72f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T72f —— batch 12 之產出（`Update Agent`，14 列）\n")
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
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [i for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _, _ in keep} | set(mid) | set(m3))
    deliverable = [r for r in rows if r[4] == 0]
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {len(deliverable)}**")
    print(f"\n### 分層抽驗\n- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}"
          f"\n- 可排除之 `低`：{len(excl)} 列")
    for i, req, rs in keep:
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— "
              + "、".join(f"**{r}**" for r, ok in rs if not ok))
    print(f"- 機制 3 攔下：{len(m3)} 列 —— " + "、".join(f"`SU-{i:03d}`" for i in m3))
    print(f"- **抽驗組成 = {len(union)} 列**")
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
