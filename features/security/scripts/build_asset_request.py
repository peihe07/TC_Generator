#!/usr/bin/env python3
"""資產請求單（SEC-08 §3(c)）—— 自 `placeholder_summary.tsv` 產生，不手抄計數。

R-SEC21(f)：首段須明寫本本含 RD 資產佔位之數量與「執行前須補值」。
各 token 另附「佔位位置」欄（欄位分佈 ＋ 前二例之逐行位置），
使 RD 拿到單子即可對照交付本之行。
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features" / "security" / "data"
OUT = ROOT / "features" / "security" / "sandbox" / "delivery" / "asset_request.md"

# 缺什麼／找誰 —— 取自 EXEC_ASSETS.md 之指派（R-G11：非執行層查證）
ASSET = {
    "X-c": ("NR1L 正確 OID 之 Code Signing 憑證（leaf ＋ L1 PEM）", "STLA 經 Steven"),
    "X-d": ("本機 SSN 之 ECU certificate chain（`ecu.cacert`）。"
            "Samuel: also confirm ECU cert partition paths (A-SEC-16) and "
            "item 1/10/11/13/14 scope (A-SEC-17)", "STLA 經 Samuel"),
    "X-e": ("CertProvider 六組憑證（valid／broken／revoked／wrong-subject／wrong-issuer／"
            "wrong-OID）＋ RD 預產 `dcl_baseline.json`、`dcl_revoked_l0~l3.json`", "Steven"),
    "X-f-2": ("**KeyInstall status test runner** —— Binder `getStatus()` 之可執行入口"
              "（SEC-07 內查後僅餘 6 行）。"
              "Steven to confirm CertProvider apk file name (A-SEC-15)",
              "Steven／KeyInstall 負責人"),
    "X-g": ("SAM 四 SAMType AuthData（`{SSN}_SAM_{SAMType}.json` ＋ `.sig` ＋ cert）；"
            "ValidityCounter `0`／`1`／`65535`；TimeStamp 舊於已裝者一組；SAM dongle",
            "SAM 負責人"),
    "X-h": ("CS.212 正式 package（Cybersecurity team review 後）之逐字 log 關鍵字",
            "Steven／Shawn"),
    "X-j": ("**OTA／HAL 版本升級之映像檔與升級手段** —— 037 KI-008 之第二 sibling",
            "JY／Rivers"),
    "X-k": ("**Dealer App 對 DUT 之存取**（ECUCert Dealer Service 之 `UI` 通道入口）",
            "Samuel"),
    "X-l": ("**SwdlSecureLib 之解密／驗證測試入口**（程式庫介面之可執行 harness）",
            "JY／Rivers"),
    "X-m": ("**兩次獨立取樣之 log snapshot ＋ 對稱金鑰比對手段** —— 037 LOGENC-006 4.1.3",
            "LogEncrypt 負責人"),
    "X-n": ("**suspend／resume 之觸發手段** —— 037 SAM-0013 未載觸發方式", "SAM 負責人"),
}
KIND_ZH = {"trigger": "觸發型", "exec": "步驟型", "value": "值型", "outcome": "結果型"}

TAIL = """
## `X-i` 已裁降（不在本表）

Pei 2026-09-17 裁降為**文件審查**（R-SEC20）：原 16 行佔位全數消除，
8 TC（`NR1L-CP-011`~`-014`、`NR1L-CP-017`／`-018`、`NR1L-KI-023`／`-024`）改為
「取得 artifact ＋ 逐要件審查」式。**惟仍須 RD 開通建置環境之存取權**
（Pre-Condition `Access to the RD build environment for <component> is granted`），
此為排期事項，不再列為資產缺件。

## SEC-07 內查已解之代號（不再請求）

| 代號 | 解前行數 | 解後 | 依據 |
|---|---:|---:|---|
| `X-f-2` | 18 | **6** | Z1 `test_java_integration.py` 之 \
`KeyInstallDiagServiceManagerTests#getInstalledKeysStatus` 與 \
`KeyMasterWrapperAesTests#encryptDecryptNormalFlow`；`keys_install_helper.py` 之 \
`installstate` 路徑與狀態值 |
| `X-l` | 12 | **8** | CCVR `Auth-Prog CS.93` evidence 之 `31 01 F0 00` → \
`71 01 F0 00 00/01`；bit field 語意依 CS.00102 `SYS-RA-CS00102-685` |

## 急迫序

1. **9/18 Dev-Key build**：`X-c`（NR1L 正確 OID 憑證）、`X-d`（ECU certificate chain）
2. **前批**：`X-e`、`X-f-2`
3. **後批**：`X-g`／`X-n`／`X-j`／`X-k`／`X-m`／`X-h`

## 三點限度（R-G11）

- 「找誰」取自下放包之指派，非執行層查證。
- `X-e` **內查未解**：Z2／Z3 只含 CertProvider 之 15 條方法驅動腳本，
  **無 wrong-subject／wrong-issuer／wrong-OID／revoked 憑證，亦無對應方法**。
- 佔位之「性質」逐字取自 v03 之原 `PENDING` 文字（`placeholder_summary.tsv` 之
  `original_pending` 欄），執行層未自行加註 TC 專屬之細節。
"""


def main() -> int:
    src = (DATA / "placeholder_summary_v09.tsv"
           if (DATA / "placeholder_summary_v09.tsv").exists()
           else DATA / "placeholder_summary.tsv")
    rows = list(csv.DictReader(src.open(encoding="utf-8"), delimiter="\t"))
    for r in rows:                       # R-SEC25(e)：TC 稱謂為 `<Component>/<新 ID>`
        if r.get("workbook"):
            r["tc_id"] = f'{r["workbook"]}/{r["tc_id"]}'
    by_tok: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_tok[r["x_token"]].append(r)
    order = sorted(by_tok, key=lambda k: (-len(by_tok[k]), k))
    lines = [
        "# 資產請求單 —— Security（SEC-08 佔位化版）",
        "",
        "產生日：2026-09-17。對應交付候選：`security_v04` 之封面填值本。",
        "",
        f"**本本含 {len(rows)} 處 RD 資產佔位，執行前須依本清單補值。**"
        "佔位式為 `<性質 provided by <供給方> (X-<n>)>`；"
        "工作簿內不再有 `PENDING` 字樣（R-SEC21），追溯代號保留於各列 Remarks 之 "
        "`asset: X-<n> — <原 PENDING 全文>`。"
        "逐行位置見 `data/placeholder_summary.tsv`（"
        f"{len(rows)} 行）與 `data/placeholder_by_token.tsv`（{len(by_tok)} token）。",
        "",
        f"合併本 100 TC：v03 之 112 行 `PENDING` = **16** 行 `X-i`（R-SEC20 裁降為文件審查，"
        f"已消除）＋ **{len(rows)}** 行資產佔位（本表 {len(by_tok)} 個代號）。",
        "",
        "| # | 代號 | 缺什麼 | 行數 | 佔位位置 | 涉及 TC | 找誰 |",
        "|---:|---|---|---:|---|---|---|",
    ]
    for i, tok in enumerate(order, 1):
        rs = by_tok[tok]
        what, who = ASSET.get(tok, ("（未登錄於 EXEC_ASSETS）", "—"))
        flds = Counter(r["field"] for r in rs)
        kinds = Counter(KIND_ZH.get(r["kind"], r["kind"]) for r in rs)
        ex = "；".join(f'{r["tc_id"]} {r["field"]} L{r["line"]}' for r in rs[:2])
        pos = (" ".join(f"{k}={v}" for k, v in sorted(flds.items()))
               + "（" + "／".join(f"{k} {v}" for k, v in kinds.most_common()) + "）"
               + f"；例 {ex}")
        tcs = sorted({r["tc_id"] for r in rs})
        tc_txt = "、".join(tcs[:4]) + (f"…（共 {len(tcs)}）" if len(tcs) > 4 else "")
        lines.append(f"| {i} | **{tok}** | {what} | {len(rs)} | {pos} | {tc_txt} | {who} |")
    OUT.write_text("\n".join(lines) + "\n" + TAIL, encoding="utf-8")
    print(f"asset_request.md：{len(rows)} 佔位／{len(by_tok)} token → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
