#!/usr/bin/env python3
"""T63d —— batch 6：`Integrity Verification`(8) ＋ `Deployment Conditions`(8) = 16 列。

**本批為新分工下執行層首次自選標的**（下放包 51 §二）。其挑選依據見上繳包 44 §1。

**型別分佈**：
- **第二型**（無外部面）：`173`／`311`／`343` —— 其行為全在內部（簽章模組之介面、
  DM Tree 之儲存格式、服務間之條件請求），**無任何外部後果**。
- **第四型**（觸發手段不可得）：`171`／`172`／`174`／`310`／`312`／`338` ——
  其外部後果**可觀測**（拒絕安裝、版本未變），缺者為**使驗證失敗之手段**
  （簽章無效之套件、來源版本不符之差分包、內容毀損之檔案、格式錯誤之 OMA-DM 訊息）。
- **可寫**：`336`／`337`／`340`／`341`／`344`／`345`／`346`。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch6"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 66

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"
IV, DC = "Integrity Verification", "Deployment Conditions"

W = "1. The head unit is connected to a Wi-Fi network with internet access"
B = "2. The vehicle is in Body ON mode"


def neg_verify(req, spec, item, paren, trig, obs, conf, note, ts=IV):
    """第四型之共通形態：外部後果可觀測（拒絕安裝），而使驗證失敗之手段不可得。"""
    return dict(req=req, ts=ts, spec=spec, dm=NEG, prio="P1", conf=conf, note=note,
        item=[item, f"({paren})"],
        pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
             f"4. PENDING: DR-SU2 means of staging {trig} on the OTA Server"],
        proc=["1. Read the software version shown on the head unit and record it as Version_initial",
              f"2. PENDING: DR-SU2 step to stage {trig}",
              "3. Trigger an update availability check to the OTA Server and accept the update on the head unit",
              "4. Read the software version shown on the head unit and record it as Version_after",
              f"5. Check that Version_after equals Version_initial while {obs}"],
        er=["1. Version_initial is recorded",
            f"2. PENDING: DR-SU2 observable evidence that {obs}",
            "3. The update availability check completes and the update is accepted on the head unit",
            "4. Version_after is recorded",
            f"5. Version_after equals Version_initial while {obs}"])


def internal(req, spec, item, paren, what, conf, note, ts=IV):
    """第二型之共通形態：行為全在內部，無外部後果。"""
    return dict(req=req, ts=ts, spec=spec, dm=FN, prio="P2", conf=conf, note=note,
        item=[item, f"({paren})"],
        pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
             f"4. PENDING: DR-SU2 means of observing {what}"],
        proc=["1. Trigger an update availability check to the OTA Server",
              f"2. PENDING: DR-SU2 step to observe {what}"],
        er=["1. The update availability check completes and an update is reported as available",
            f"2. PENDING: DR-SU2 observable evidence of {what}"])


TCS = [
 neg_verify("SWE1-FOTA-171", "CFTS057-4907519",
   "If signature verification or certificate validation fails, the WiFi Update Service/USB Update Service shall reject the deployment package and prevent installation processing.",
   "Package with an invalid signature is not installed",
   "a deployment package whose digital signature or certificate chain is invalid",
   "the staged deployment package has an invalid signature or certificate chain",
   "低", "第四型：拒絕安裝可觀測，而簽章無效之套件不可佈置"),
 neg_verify("SWE1-FOTA-172", "CFTS057-4907517",
   "If a source version mismatch is detected for any differential update component, the WiFi Update Service/USB Update Service shall reject the deployment package and prevent installation.",
   "Differential package with a mismatched source version is not installed",
   "a differential deployment package whose declared source version does not match the installed version",
   "the staged differential package declares a source version other than the installed one",
   "低", "第四型：同 `171`，差分包之來源版本不符不可佈置"),
 internal("SWE1-FOTA-173", "CFTS057-4907519",
   "The SWMC shall interact with a signature verification module to validate deployment package signatures.",
   "Signature verification module is invoked for the deployment package",
   "the invocation of the signature verification module",
   "低", "**第二型**：其行為為服務與模組間之介面呼叫，無任何外部後果"),
 neg_verify("SWE1-FOTA-174", "CFTS057-4907520",
   "If integrity or authenticity verification fails for any contained update file, the WiFi Update Service/USB Update Service shall reject the deployment package and prevent installation.",
   "Multi-file package with one corrupt file is not installed",
   "a deployment package containing multiple update files of which one fails integrity verification",
   "one contained update file of the staged package fails integrity verification",
   "低", "第四型：同 `171`；⚠ 其錨 `4907520` 為候選 #2（首選 `4907604` 述簽章而非逐檔）"),
 neg_verify("SWE1-FOTA-310", "CFTS057-4907509",
   "SWMC shall reject messages that fail the integrity verification.",
   "OMA-DM message failing integrity verification is rejected",
   "an OMA-DM message that fails integrity verification",
   "the head unit received an OMA-DM message that fails integrity verification",
   "低", "第四型：訊息層之注入手段不可得"),
 internal("SWE1-FOTA-311", "CFTS057-4907510",
   "SWMC shall store the DM Tree in an encrypted format to prevent plaintext access.",
   "DM Tree is stored in an encrypted format",
   "the stored format of the DM Tree",
   "低", "**第二型**：儲存格式無外部表徵"),
 neg_verify("SWE1-FOTA-312", "CFTS057-4907514",
   "WiFiUpdateService shall perform the integrity verification of the deployment package immediately after receiving the package",
   "Corrupt deployment package is not installed after download",
   "a deployment package whose content fails integrity verification",
   "the staged deployment package fails integrity verification",
   "中", "第四型；其錨 `4907514` 為候選 #2 —— 首選 `4907483` 述部署立即開始，與本列之驗證無關"),
 neg_verify("SWE1-FOTA-338", "CFTS057-4907604",
   "The WiFiUpdateService shall verify the authenticity of the deployment package after user acceptance or when the scheduled installation time is reached, before initiating the deployment.",
   "Package failing authenticity verification is not deployed after acceptance",
   "a deployment package that fails authenticity verification",
   "the staged deployment package fails authenticity verification",
   "中", "第四型；驗證之時點（使用者接受後）已入 procedure"),
 # ── Deployment Conditions ──────────────────────────────────────────
 dict(req="SWE1-FOTA-336", ts=DC, spec="CFTS057-4907663", dm=FN, prio="P1",
      conf="高", note="",
  item=["When OTA updates are disabled, the WiFiUpdateService shall stop automatic update polling.",
        "(No update is reported after OTA updates are disabled in settings)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. OTA updates are enabled in the vehicle settings"],
  proc=["1. Disable OTA updates in the vehicle settings",
        "2. Record the head unit screen content as continuous video capture until the head unit returns to the home screen",
        "3. Check that no software update notification appears in the recorded screen content while OTA updates are disabled"],
  er=["1. The vehicle settings show OTA updates as disabled",
      "2. The head unit screen content until the head unit returns to the home screen is recorded as continuous video capture",
      "3. The recorded screen content contains no software update notification while OTA updates are disabled"]),
 dict(req="SWE1-FOTA-337", ts=DC, spec="CFTS057-4907483", dm=FN, prio="P1",
      conf="中", note="⚠ 與 `181`（`010`）之「下載完成後立即部署」相交 —— 待裁 (d)",
  item=["The WiFiUpdateService shall receive the deployment notification from the SWMC and initiate the deployment workflow.",
        "(Deployment workflow starts after the download completes)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit"],
  proc=["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "2. Record the head unit screen content as continuous video capture from the moment the download completes",
        "3. Check that the head unit shows the deployment starting after the download completes"],
  er=["1. The update is accepted and the download starts on the head unit",
      "2. The head unit screen content from the moment the download completes is recorded as continuous video capture",
      "3. The recorded screen content shows the deployment starting after the download completes"]),
 dict(req="SWE1-FOTA-340", ts=DC, spec="CFTS057-4907610", dm=FN, prio="P2",
      conf="中", note="其外部後果為「改組態檔即改行為，而軟體未更動」—— 版本號不變而條件生效",
  item=["The SWMC shall support dynamically configurable installation conditions using an external configuration or script file without requiring modifications to the SWMC software.",
        "(Changed condition file takes effect without a software change)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. The installation condition configuration file in use permits the deployment"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Replace the installation condition configuration file with one that does not permit the deployment",
        "3. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "4. Read the software version shown on the head unit and record it as Version_after",
        "5. Check that the deployment does not proceed and that Version_after equals Version_initial"],
  er=["1. Version_initial is recorded",
      "2. The installation condition configuration file that does not permit the deployment is in use",
      "3. The update availability check completes and the update is accepted on the head unit",
      "4. Version_after is recorded",
      "5. The deployment does not proceed and Version_after equals Version_initial"]),
 dict(req="SWE1-FOTA-341", ts=DC, spec="CFTS057-4907611", dm=DT, prio="P1",
      conf="中", note="105 列而可寫：其外部後果為「條件不滿足則部署不進行」",
  item=["The SWMC shall evaluate the logical combination of deployment conditions and verify that the configured values or value ranges are satisfied before proceeding with the deployment.",
        "(Deployment is withheld while one configured condition is not satisfied)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. The installation condition configuration file requires two conditions to be satisfied together"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Bring one of the two configured conditions into a state that does not satisfy it",
        "3. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "4. Read the software version shown on the head unit and record it as Version_after",
        "5. Check that Version_after equals Version_initial while one of the two configured conditions is not satisfied"],
  er=["1. Version_initial is recorded",
      "2. One of the two configured conditions is not satisfied",
      "3. The update availability check completes and the update is accepted on the head unit",
      "4. Version_after is recorded",
      "5. Version_after equals Version_initial while one of the two configured conditions is not satisfied"]),
 internal("SWE1-FOTA-343", "CFTS057-4907613",
   "The WiFiUpdateService shall provide the vehicle conditions specified in the deployment configuration file to the SWMC.",
   "Vehicle conditions are provided to the SWMC",
   "the vehicle conditions passed from the WiFiUpdateService to the SWMC",
   "低", "**第二型**：服務間之條件傳遞，無外部後果", ts=DC),
 dict(req="SWE1-FOTA-344", ts=DC, spec="CFTS057-4907615", dm=FN, prio="P1",
      conf="高", note="",
  item=["The WiFiUpdateService shall notify the end user of the deployment conditions preventing the software update through the HMI upon receiving the notification from the SWMC.",
        "(User is told which condition is preventing the update)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. One of the configured deployment conditions is not satisfied"],
  proc=["1. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "2. Check that the head unit displays a message naming the deployment condition that is preventing the update"],
  er=["1. The update availability check completes and the update is accepted on the head unit",
      "2. The head unit displays a message naming the deployment condition that is preventing the update"]),
 dict(req="SWE1-FOTA-345", ts=DC, spec="CFTS057-4907617", dm=ST if False else FN, prio="P1",
      conf="中", note="105 列而可寫：暫停與續傳於下載進度上可觀測",
  item=["The SWMC shall pause the deployment package download when one or more configured download conditions are not satisfied and shall resume the download when the conditions are satisfied.",
        "(Download pauses while a download condition is not satisfied and resumes afterwards)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. The deployment package download is in progress on the head unit"],
  proc=["1. Record the head unit screen content as continuous video capture from the moment the download is in progress until the download completes",
        "2. Bring one of the configured download conditions into a state that does not satisfy it",
        "3. Bring that condition back into a state that satisfies it",
        "4. Check that the recorded screen content shows the download progress stopping while the condition is not satisfied and advancing again afterwards"],
  er=["1. The head unit screen content from the moment the download is in progress until the download completes is recorded as continuous video capture",
      "2. The configured download condition is not satisfied",
      "3. The configured download condition is satisfied again",
      "4. The recorded screen content shows the download progress stopping while the condition is not satisfied and advancing again afterwards"]),
 dict(req="SWE1-FOTA-346", ts=DC, spec="CFTS057-4907646", dm=NEG, prio="P1",
      conf="高", note="⚠ 037 原文為 `he WiFiUpdateService`（缺 `T`）—— **逐字保留**，登 D-5；lint 之 `J=1` 為該缺字之後果",
  item=["he WiFiUpdateService shall ensure that sufficient physical storage space is available to store the latest firmware package before initiating the download.",
        "(Download does not start when storage space is insufficient)"],
  pre=[W, B, "3. An update package is staged on the OTA Server for this head unit",
       "4. The head unit storage is filled so that the space left is smaller than the staged package"],
  proc=["1. Read the software version shown on the head unit and record it as Version_initial",
        "2. Trigger an update availability check to the OTA Server and accept the update on the head unit",
        "3. Read the software version shown on the head unit and record it as Version_after",
        "4. Check that Version_after equals Version_initial while the space left on the head unit is smaller than the staged package"],
  er=["1. Version_initial is recorded",
      "2. The update availability check completes and the update is accepted on the head unit",
      "3. Version_after is recorded",
      "4. Version_after equals Version_initial while the space left on the head unit is smaller than the staged package"]),
]

# `低` 之理由 × 是否由 `PENDING` 承載（下放包 51 §一 #5）
LOW_REASONS = {
 "SWE1-FOTA-171": [("使驗證失敗之套件不可佈置", True)],
 "SWE1-FOTA-172": [("來源版本不符之差分包不可佈置", True)],
 "SWE1-FOTA-173": [("無任何外部後果", True)],
 "SWE1-FOTA-174": [("內容毀損之檔案不可佈置", True),
                   ("錨為候選 #2，首選述簽章而非逐檔", False)],
 "SWE1-FOTA-310": [("格式錯誤之 OMA-DM 訊息不可注入", True)],
 "SWE1-FOTA-311": [("儲存格式無外部表徵", True)],
 "SWE1-FOTA-343": [("服務間之傳遞無外部後果", True)],
}


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T63d：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T63d：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T63d —— batch 6 之產出（**執行層自選標的**）\n")
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

    print("| 列 | TC ID | 037 | Test Set | 自信度 | PENDING |")
    print("|---|---|---|---|:--:|---:|")
    for r, tid, req, ts, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | `{ts}` | **{cf}** | {pd} |")
    from collections import Counter
    c = Counter(t["conf"] for t in TCS)
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [i for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    print(f"\n- **`PENDING` 合計 {sum(r[5] for r in rows)}**｜TC **{len(rows)}**")
    print(f"\n### 分層抽驗（新制）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- **可排除之 `低`**：{len(excl)} 列 —— " + "、".join(f"`SU-{i:03d}`" for i, _, _ in excl))
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— 未由 `PENDING` 承載者："
              + "、".join(f"**{r}**" for r in un))
    print(f"- **抽驗組成** = 中 {len(mid)} ＋ 未排除之低 {len(keep)} = **{len(mid)+len(keep)}** 列")
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
