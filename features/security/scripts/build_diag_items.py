#!/usr/bin/env python3
"""DID／RID／DTC 拆解表（下放包 _B §3 ＋ _C §3 ＋ _D §1.1，任務 3-D）。

三份下放包之清單合併去重；`definition_source` 依 _D §4 之優先序決定：
    CS00102:SYS-RA-CS00102-nnn  >  CFTS004:SYS-RA-DIAG-nnn  >  R1L-SWQT:<Test ID>
    >  VHAL-R5:§2.4  >  PENDING:<DR>
CS.00102 側之 `support_status`／`roles` 一律**現查** `sources/raw/sys2_cs00102_swad/`，
不照抄下放包（_D 明令「執行層以 `Basic Report` 複驗」）。

產物：features/security/data/diag_items.tsv
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve()
OUT = HERE.parents[1] / "data"
_spec = importlib.util.spec_from_file_location("btm", HERE.parent / "build_trace_matrix.py")
btm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(btm)

# (kind, id, name, used_by, cs00102_ids, other_source, note)
# `cs00102_ids` 空者表示 CS.00102 無定義；`other_source` 為次優先來源。
ITEMS = [
    # ---- _D §1.1（CS.00102 為定義本；22 項）----
    ("DID", "F18C", "ECU Serial Number", "ECUCert 全部（Test Steps PDF Step 1）；SAM-0006（SSN 比對 ECUId）", "144,145,146", "R1L-SWQT:22103/22179/22255", "5.2.1.25；讀有前例，寫（2E F1 8C）無前例"),
    ("DID", "F111", "Public Certificates – Regional Support", "CertProvider-009", "046,047,048", "", "5.2.1.2；只可讀，經 Authenticated FW update 寫入；區域由 Certificate Store UUID（SD.00045）決定"),
    ("DID", "F1B6", "ECU Identity L0 Root certificate", "ECUCert R19 匯出憑證", "209,210", "", "5.2.1.44"),
    ("DID", "F1BD", "ECU Signature Type", "CertProvider-011（OID，CS.00098/02）", "216", "", "5.2.1.47"),
    ("DID", "F1C2", "HSM/HTA version", "Auth-Boot 第 3；KeyInstall-013", "223", "", "5.2.1.50；**OutofScope** → KeyInstall-013 不以 DID 驗"),
    ("DID", "0108", "ADA Active Roles", "讀 2965 等 ADA+ DID 之前提", "241,242", "", "5.2.2.3"),
    ("DID", "2010", "Programming Status", "Auth-Prog", "311,312", "", "5.2.2.29；header 列為 Information"),
    ("DID", "201F", "Boot Failure Reason", "Auth-Boot 第 5/6/11 之 ER", "332,333,334", "", "5.2.2.37"),
    ("DID", "2031", "Disavowed Certificate List (DCL)", "Cert Val 第 1/2/5~8；CertProvider-004", "343,344", "", "5.2.2.43；回最後 42 筆；DCL 依 SD.00015/03；與 DR-SEC-j 相關"),
    ("DID", "2954", "Policy Type", "—", "388,389", "", "5.2.2.61"),
    ("DID", "2955", "Certificate Store Header Info", "Cert Val 第 1 項；CertProvider-007/009", "390,391", "", "5.2.2.62；供應商擇 2955+295D+295E 或 295F，未用者停用或回 0x20"),
    ("DID", "295D", "DCL Header Info", "Cert Val 第 1/2/5~8", "406,407", "", "5.2.2.70"),
    ("DID", "295E", "DCL UUID", "同上", "408,409", "", "5.2.2.71"),
    ("DID", "295F", "DCL + Certstore Header", "—", "410,411", "", "5.2.2.72；**OutofScope** → NR1L 走三分式"),
    ("DID", "2965", "CSR Read (1000 bytes)", "ECUCert R18；Test Steps PDF Step 2", "415,416,417,418", "R1L-SWQT:22403/22404", "5.2.2.75；**ADA+ 保護**；與 R1L SWQT 之 ≤2048 bytes 不同（A-SEC-3）"),
    ("DID", "2966", "ECU Identity Cert Error Enable (1 byte)", "ECUCert R11 online；CS.165 DTC 條件", "419", "", "5.2.2.76"),
    ("DID", "2967", "CSR Count", "ECUCert R21 下載重試（totalRetrialMax 300）", "420", "", "5.2.2.77；**OutofScope** → 不經 DID 讀"),
    ("DID", "2969", "ECU Identity L1 cert 讀寫", "ECUCert R20 匯入憑證", "423,424,425", "", "5.2.2.78；**OutofScope** → 不走 DID，與 PDF 之 adb push 一致"),
    ("DID", "2991", "ECU Identity L2 cert 讀寫", "ECUCert R20", "536,537,538,539", "", "5.2.2.116；**OutofScope**"),
    ("DID", "2992", "ECU Identity L3 cert 讀寫", "ECUCert R20", "540,541,542,543", "", "5.2.2.117；**OutofScope**"),
    ("DID", "2032", "Secure log", "CS.212 全部", "456,457", "", "5.2.2.93；**OutofScope** → CS.212 證據只能靠 logcat，無 DID 面"),
    ("RID", "D00A", "CSR Trigger", "ECUCert R18", "678,679", "", "5.2.7.18；**OutofScope** → CSR 開機自動產生（PDF Step 2）"),
    ("RID", "F000", "Check Program（31 01 F0 00）", "Auth-Prog 第 2/4/5/6/7；SWDL-003/004", "683,684,685", "", "5.2.7.19；Authenticated Reprogramming 不帶資料，簽章嵌於下載資料（SD.00015）"),
    ("RID", "FF01", "Check Programming Dependencies – Validate Application", "Auth-Prog", "695,696,697,698", "", "5.2.7.23；**FF01 在 NR1L 是 RID，不是 SSN DID**"),
    # ---- _D §1.2：SSN DID 之正解 ----
    ("DID", "2975", "HU ID (SSN)", "SAM-0006（SSN vs ECUId）；KeyInstall-003", "", "CFTS004:SYS-RA-DIAG-008", "NA 內部工程用；_C §3 之 FF01 列作廢，以 2975 為準（DR-SEC-o）"),
    # ---- _B §3 中 CS.00102 未涵蓋者 ----
    ("DID", "F180", "Boot Software version", "Auth-Prog 第 6/7 rollback", "084", "", "SYS2_Mapped `DID CS.102`；CS.00102 現查見下表"),
    ("DID", "F181", "Application Software version", "Auth-Prog 第 6/7 rollback", "091", "", "5.2.1.12-6"),
    ("RID", "9001", "金鑰佈建 transport key 握手（CAN）", "KeyInstall-007/011；SYSAD_IF_KI_DIAG；CS.212 第 10/12 項", "", "", "**CS.00102 查無、R1L SWQT 查無** → PENDING: DR-SEC-k"),
    ("RID", "9003", "金鑰佈建 payload 注入（CAN）", "同上（injectKeysFromJson）", "", "", "同上 → PENDING: DR-SEC-k"),
    ("RID", "1902FF", "Read DTC by status mask", "Auth-Boot 第 6/11", "", "UDS-STD:ISO14229 $19 02", "UDS 標準服務，無需專屬定義本"),
    ("DTC", "U3033-00", "Control Module Security Certificate Missing/Invalid", "CertProvider-004/005 之撤銷失敗", "", "CS00098:§5.4.10（碼已定，規格本未投遞）", "CS.00098/01 §5.4.10；碼已定"),
    ("DTC", "U160B-45", "ECU Boot Software 1 Missing/Invalid", "Auth-Boot 第 11/12", "", "CS00093:§5.2.8（碼已定，規格本未投遞）", "CS.00093 §5.2.8；碼已定"),
    ("DTC", "C221C-00", "Boot failure 系列", "Auth-Boot 第 11/12", "", "CS00093:§5.2.8（碼已定，規格本未投遞）", "CS.00093 §5.2.8"),
    ("DTC", "B2250", "Boot failure 系列", "Auth-Boot 第 11/12", "", "CS00093:§5.2.8（碼已定，規格本未投遞）", "CS.00093 §5.2.8"),
    ("DTC", "P0602-00", "ECU Not Programmed / Flash Required", "Auth-Boot 第 12", "", "DTCMatrix:r110（CS.00101 RQMT-37~41；CFTS084-2178/2180）", "CS.00093 §5.2.8"),
    ("DTC", "A2500 00F", "bootloader DTC（原文 `0xA2 50 00 0F`）", "SWDL（Auth-Prog 第 2/4/5 evidence 欄）", "", "PENDING:DR-SEC-l", "格式非標準 DTC，逐字回報"),
    ("DTC", "(空)", "Certificate validation failure from Stellantis service", "ECUCert R11；CS.165 DTC 條件", "", "", "CS.00165 §5.6；**sheet 未給碼** → PENDING: DR-SEC-m"),
    ("DTC", "(空)", "Identity certificate not installed due to verification failure", "ECUCert R20", "", "", "SD.00125 §5.1；**未給碼** → PENDING: DR-SEC-m"),
    ("DTC", "B22A9-00", "ECU Internal Failure", "內部失效類", "", "DTCMatrix:r（`DTC's in CFTS's`）", "_F §4；Security 直接可用之第二碼"),
    # ---- _C §3（R1L Diag SWQT 前例本 ＋ VHAL）----
    ("DID", "FF02", "SecurityKeyInstallStatus", "KeyInstall-011", "", "R1L-SWQT:22345/22346", "`62 FF 02 01`=未裝、`00`=已裝；**兩態 vs 037 四態** → DR-SEC-o；CS.00102 查無"),
    ("DID", "FF01(R1L)", "SSN（R1L 舊號，NR1L 已改）", "SAM-0006；KeyInstall-003", "", "R1L-SWQT:22341~22344", "**作廢**：NR1L 之 FF01 為 RID；SSN 改用 2975（DR-SEC-o）"),
    ("DID", "2951", "Software Inventory（R1L 前例本）", "CertProvider-007/009；Cert Val 第 1 項", "", "R1L-SWQT:22031/22032/22081/22157", "**CS.00102 查無 2951** → DR-SEC-p 結案：改用 2955/295D/295E；CCVR sheet 之「2951 Certificate Store UUID」登 A-SEC-1"),
    ("SVC", "$27", "SecurityAccess", "Auth-Prog 第 8/10 session 鎖；SYSAD_IF_KI_DIAG", "", "R1L-SWQT:27001~", "`27 05` seed／`27 06` key；default session NRC `7F 27 7F`"),
    ("SVC", "$2850", "Arch type 設定", "Vehicle Model 前提", "", "VHAL-R5:§2.4", "`2E 28 50 03`=Atl-Mid／`05`=Atl-Hi；診斷 CAN ID Hi 0x7BF/0x53F、Mid 0x18DA87F1/0x18DAF187"),
    ("OPS", "KeyInstallDiagService 重連", "服務可用性（Fault Injection 型）", "KeyInstall-011", "", "R1L-SWQT:Diag基本機能 00053", "`ps -A | grep keyinstall` → kill → `10 60` → `22 FF 02` 得 PR"),
    ("OPS", "ECUCertDiagManager connected", "DiagService 啟動 log 關鍵字", "ECUCert R12", "", "R1L-SWQT:Diag基本機能 00056", "ER 之 log 關鍵字"),
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # CS.00102 現查（_D 明令複驗）
    wb = openpyxl.load_workbook(btm.only("sys2_cs00102_swad", "*.xlsx"), read_only=True, data_only=True)
    grid = list(wb["Basic Report"].iter_rows(values_only=True))
    hdr = [str(c or "").strip() for c in grid[0]]
    i_cat = hdr.index("SYS2 分類 Category")
    i_desc = hdr.index("Description")
    cs = {}
    for r in grid[1:]:
        if not r[1]:
            continue
        cs[str(r[1]).strip()] = {
            "cat": str(r[i_cat] or "").strip(),
            "desc": str(r[i_desc] or "").replace("_x000D_", " ").strip(),
        }
    wb.close()

    rows, missing = [], []
    for kind, ident, name, used_by, ids, other, note in ITEMS:
        sids = [f"SYS-RA-CS00102-{n.zfill(3)}" for n in ids.split(",") if n]
        gone = [s for s in sids if s not in cs]
        missing += gone
        cats = sorted({cs[s]["cat"] for s in sids if s in cs})
        if sids and not gone:
            src = "CS00102:" + ",".join(sids)
        elif other:
            src = other
        else:
            src = "PENDING:" + ("DR-SEC-k" if ident in ("9001", "9003")
                                else "DR-SEC-m" if kind == "DTC" and ident == "(空)"
                                else "DR-SEC-n")
        rows.append([kind, ident, name, ";".join(cats) or "-", "", used_by, src, note])

    with (OUT / "diag_items.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["kind", "id", "name", "support_status", "roles",
                    "used_by", "definition_source", "note"])
        w.writerows(rows)

    c = Counter(r[0] for r in rows)
    src = Counter(r[6].split(":")[0] for r in rows)
    print(f"diag_items.tsv {len(rows)} 列 | kind: {dict(c)}")
    print(f"  definition_source: {dict(src)}")
    print(f"  CS.00102 現查查無之 SYS2 ID: {missing or '無'}")
    pend = [r[1] for r in rows if r[6].startswith("PENDING")]
    print(f"  「定義文件未在手上」{len(pend)} 項: {pend}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
