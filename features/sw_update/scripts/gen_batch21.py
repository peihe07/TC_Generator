#!/usr/bin/env python3
"""T81f —— batch 21：`Bearer Selection` 16 列（下放包 69 §四 #1，收尾階段第一批）。

**⚠ 本組之名稱與其內容不符**（上繳包 68 §1.1）：**十六列中只有 `292` 與 bearer 有關**，
其餘十五列為 **DDF 判讀**與**安全／認證**（TLS 1.2、HMAC、伺服器認證、埠管理、簽章）。

**故其阻斷理由分二**：
- `292` → **DR-SU2(a)**（bearer 之觀測手段）
- 其餘 → **DR-SU7**（安全與認證之觀測手段，本輪新開）

**其可交付性預估為 0／16**（上繳包 68 §1）—— **本批之產出即該預估之實現。**
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch21"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 301
TS = "Bearer Selection"
FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
B = "The vehicle is in Body ON mode"
WIFI = "The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "An update package is staged on the OTA Server for this head unit"


def sec(req, spec, prio, note, item, paren, what, dr="DR-SU7", extra=()):
    """安全／認證型之共通形態 —— **其 Final Step 逐列帶入 `what`**（B-24）。"""
    return dict(req=req, ts=TS, spec=spec, dm=FN, prio=prio, conf="低", note=note,
                item=[item, f"({paren})"],
                pre=[B, WIFI, PKG, f"PENDING: {dr} means of observing {what}", *extra],
                proc=["1. Trigger an update availability check to the OTA Server and let the OTA session run",
                      f"2. PENDING: {dr} step to read {what}"],
                er=["1. The OTA session runs on the head unit",
                    f"2. PENDING: {dr} observable evidence of {what}"])


TCS = [
 sec("SWE1-FOTA-292", "CFTS057-4907292", "P1",
  "**本組唯一與 bearer 有關之列** —— 其阻斷理由為 **DR-SU2(a)**（bearer 於外部無表徵），與其餘十五列不同",
  "WiFiUpdateService shall manage the configured network priority and select the appropriate network for OTA communication.",
  "Network is chosen by the configured priority",
  "the network the WiFiUpdateService selected and the priority it applied", dr="DR-SU2"),

 sec("SWE1-FOTA-293", "CFTS057-4907293", "P2",
  "**第二型**：DDF 參數之判讀在服務內部；其外部後果（更新型別之行為差異）屬 `Update Policy` 各列",
  "WiFiUpdateService shall evaluate the DDF parameters to determine the update type.",
  "Update type is determined from the DDF parameters",
  "the update type the WiFiUpdateService determined from the DDF", dr="DR-SU2"),

 sec("SWE1-FOTA-294", "CFTS057-4907294", "P2",
  "**第二型**；與 `293` 之別在其所判之物（更新**模式** vs 更新**型別**）",
  "WiFiUpdateService shall read the DDF parameters and determine the update mode.",
  "Update mode is determined from the DDF parameters",
  "the update mode the WiFiUpdateService determined from the DDF", dr="DR-SU2"),

 sec("SWE1-FOTA-295", "CFTS057-4907295", "P2",
  "**第二型**：`./Ext/FCA/SilentInstall` 之節點值為 DM Tree 之內部狀態",
  "If the ./Ext/FCA/SilentInstall parameter is set to 1, WiFiUpdateService shall classify the update session as a silent update.",
  "Session is classified silent when the DDF parameter is 1",
  "the classification the service applied when ./Ext/FCA/SilentInstall is 1", dr="DR-SU2"),

 sec("SWE1-FOTA-297", "CFTS057-4907297", "P1",
  "**第四型**＋**105 列**；**與 `171`／`249` 同族** —— 使簽章驗證失敗之套件不可佈置",
  "WiFiUpdateService shall use SWDLSecureLib to verify the digital signature and integrity of the deployment package.",
  "Package signature and integrity are verified before use",
  "the signature and integrity verification the SWDLSecureLib performed"),

 sec("SWE1-FOTA-298", "CFTS057-4907298", "P2",
  "**第二型**＋**105 列**：專有協定之選用與其實作於車機無表徵，**需網路側錄**",
  "SWMC shall support OTA communication using the configured proprietary communication protocol.",
  "Proprietary protocol is used for OTA communication",
  "the protocol used between the head unit and the OTA Server"),

 sec("SWE1-FOTA-299", "CFTS057-4907299", "P2",
  "**DR-SU6**：`enforce the OTA client security requirements` 為**合規命題** —— 單次執行不能證實其全部",
  "SWMC shall enforce the OTA client security requirements and provide only validated OTA update information to WiFiUpdateService.",
  "Only validated update information is passed on",
  "the validation the SWMC applied before passing update information on", dr="DR-SU6"),

 sec("SWE1-FOTA-300", "CFTS057-4907300", "P1",
  "**第二型**＋**105 列**：TLS 1.2 之握手於車機無表徵，**其驗證需網路側錄**",
  "SWMC shall support server authentication using TLS 1.2 before establishing OTA communication.",
  "Server is authenticated over TLS 1.2 before the session",
  "the TLS handshake between the head unit and the OTA Server"),

 sec("SWE1-FOTA-301", "CFTS057-4907301", "P1",
  "**第二型**＋**105 列**；與 `300` 之別在其述為**認證之時序**（session 起始前）而非其協定版本",
  "SWMC shall authenticate the OTA Server before initiating an OTA communication session.",
  "Authentication happens before the session starts",
  "the order of the authentication and the session initiation"),

 sec("SWE1-FOTA-302", "CFTS057-4907302", "P2",
  "**第二型**＋**105 列**：認證資訊之提供在安全通道內，**其內容不可於車機觀察**",
  "SWMC shall provide the required authentication information when requested by the OTA server.",
  "Authentication information is supplied on request",
  "the authentication information the SWMC transmitted"),

 sec("SWE1-FOTA-303", "CFTS057-4907303", "P2",
  "**第二型**＋**105 列**：車輛資訊之取得（Vehicle Integration Layer）與其用於應用層認證皆在內部",
  "WiFiUpdateService shall retrieve the required vehicle details through the Vehicle Integration Layer and provide them to SWMC.",
  "Vehicle details reach the SWMC for authentication",
  "the vehicle details the WiFiUpdateService provided to the SWMC"),

 sec("SWE1-FOTA-304", "CFTS057-4907304", "P2",
  "**第二型**：訊息來源之真確性驗證在協定層",
  "SWMC shall validate the authenticity of the message source before processing any received message.",
  "Message source is validated before processing",
  "the source validation the SWMC performed on received messages"),

 sec("SWE1-FOTA-305", "CFTS057-4907305", "P1",
  "**第二型**＋**105 列**；其否定面（拒絕未授權伺服器）需佈置一個未授權之伺服器 —— **其手段亦未確立**",
  "SWMC shall verify that the target OTA Server is an authorized server before initiating communication.",
  "Only an authorised server is talked to",
  "the authorisation check the SWMC performed on the target server",
  extra=("PENDING: DR-SU7 means of presenting an unauthorised OTA Server to the head unit",)),

 sec("SWE1-FOTA-306", "CFTS057-4907306", "P2",
  "**第二型**＋**105 列**：埠之開關需自外部掃描，**其工具與權限未確立**",
  "SWMC shall close communication ports and listening interfaces when they are no longer required.",
  "Ports are closed once they are not needed",
  "the communication ports the head unit keeps open before and after an OTA session"),

 sec("SWE1-FOTA-307", "CFTS057-4907307", "P1",
  "**第二型**＋**105 列**：HMAC 之演算法選用於車機無表徵，**其驗證需側錄與密碼學檢視**",
  "SWMC shall authenticate OTA communication at the application protocol layer using HMAC-MD5 or a stronger authentication algorithm.",
  "Application layer authentication uses HMAC-MD5 or stronger",
  "the authentication algorithm applied at the application protocol layer"),

 sec("SWE1-FOTA-308", "CFTS057-4907308", "P2",
  "**第二型**＋**105 列**；與 `298` 之別在其述為**安全機制之等價要求**而非協定之支援",
  "If a proprietary communication protocol is used, SWMC shall apply equivalent security mechanisms.",
  "Equivalent security applies to the proprietary protocol",
  "the security mechanisms applied when a proprietary protocol is configured"),
]

LOW_REASONS = {t["req"]: [("其觀測手段未確立（DR-SU7／DR-SU2）", True)] for t in TCS}


def main():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T81f：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T81f：`test_item` 上半非逐字：{bad} —— 停（R-S4）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T81f —— batch 21 之產出（`Bearer Selection` 16 列，**其名不符其實**）\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        pre = [f"{k}. {s}" for k, s in enumerate(t["pre"], 1)]
        t["pre"] = pre
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TS,
                "I": "\n".join(t["item"]), "J": "\n".join(pre),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in pre + t["proc"] + t["er"])
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 | PENDING |")
    print("|---|---|---|---:|")
    for r, tid, req, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | {pd} |")
    dl = sum(1 for r in rows if r[3] == 0)
    print(f"\n- **`PENDING` 合計 {sum(r[3] for r in rows)}**｜TC **{len(rows)}**"
          f"｜**無 `PENDING` 之可交付列 {dl}** —— **與上繳包 68 §1 之預估（0／16）"
          + ("相符**" if dl == 0 else f"不符（預估 0，實得 {dl}）**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
