# 資產請求單 —— Security（SEC-08 佔位化版）

產生日：2026-09-17。對應交付候選：`security_v04` 之封面填值本。

**本本含 94 處 RD 資產佔位，執行前須依本清單補值。**佔位式為 `<性質 provided by <供給方> (X-<n>)>`；工作簿內不再有 `PENDING` 字樣（R-SEC21），追溯代號保留於各列 Remarks 之 `asset: X-<n> — <原 PENDING 全文>`。逐行位置見 `data/placeholder_summary.tsv`（94 行）與 `data/placeholder_by_token.tsv`（11 token）。

合併本 100 TC：v03 之 112 行 `PENDING` = **16** 行 `X-i`（R-SEC20 裁降為文件審查，已消除）＋ **94** 行資產佔位（本表 11 個代號）。

| # | 代號 | 缺什麼 | 行數 | 佔位位置 | 涉及 TC | 找誰 |
|---:|---|---|---:|---|---|---|
| 1 | **X-g** | SAM 四 SAMType AuthData（`{SSN}_SAM_{SAMType}.json` ＋ `.sig` ＋ cert）；ValidityCounter `0`／`1`／`65535`；TimeStamp 舊於已裝者一組；SAM dongle | 36 | er=18 proc=18（觸發型 18／結果型 17／值型 1）；例 SAM/NR1L-SAM-003 er L1；SAM/NR1L-SAM-004 proc L1 | SAM/NR1L-SAM-003、SAM/NR1L-SAM-004、SAM/NR1L-SAM-006、SAM/NR1L-SAM-007…（共 19） | SAM 負責人 |
| 2 | **X-h** | CS.212 正式 package（Cybersecurity team review 後）之逐字 log 關鍵字 | 18 | er=18（值型 18）；例 CertProvider/NR1L-CP-002 er L3；CertProvider/NR1L-CP-005 er L3 | CertProvider/NR1L-CP-002、CertProvider/NR1L-CP-005、CertProvider/NR1L-CP-007、CertProvider/NR1L-CP-014…（共 17） | Steven／Shawn |
| 3 | **X-l** | **SwdlSecureLib 之解密／驗證測試入口**（程式庫介面之可執行 harness） | 8 | er=4 proc=4（步驟型 4／值型 4）；例 SwdlSecureLib/NR1L-SWDL-004 proc L1；SwdlSecureLib/NR1L-SWDL-004 er L1 | SwdlSecureLib/NR1L-SWDL-004、SwdlSecureLib/NR1L-SWDL-005、SwdlSecureLib/NR1L-SWDL-006、SwdlSecureLib/NR1L-SWDL-007 | JY／Rivers |
| 4 | **X-e** | CertProvider 六組憑證（valid／broken／revoked／wrong-subject／wrong-issuer／wrong-OID）＋ RD 預產 `dcl_baseline.json`、`dcl_revoked_l0~l3.json` | 6 | proc=6（觸發型 6）；例 CertProvider/NR1L-CP-005 proc L5；CertProvider/NR1L-CP-007 proc L5 | CertProvider/NR1L-CP-005、CertProvider/NR1L-CP-007、CertProvider/NR1L-CP-014、CertProvider/NR1L-CP-021…（共 6） | Steven |
| 5 | **X-f-2** | **KeyInstall status test runner** —— Binder `getStatus()` 之可執行入口（SEC-07 內查後僅餘 6 行）。Steven to confirm CertProvider apk file name (A-SEC-15) | 6 | er=3 proc=3（步驟型 2／值型 2／觸發型 1／結果型 1）；例 KeyInstall/NR1L-KI-018 proc L1；KeyInstall/NR1L-KI-018 er L1 | KeyInstall/NR1L-KI-018、KeyInstall/NR1L-KI-019、KeyInstall/NR1L-KI-022 | Steven／KeyInstall 負責人 |
| 6 | **X-k** | **Dealer App 對 DUT 之存取**（ECUCert Dealer Service 之 `UI` 通道入口） | 6 | er=3 proc=3（步驟型 3／值型 3）；例 ECUCert/NR1L-ECUC-014 proc L1；ECUCert/NR1L-ECUC-014 er L1 | ECUCert/NR1L-ECUC-014、ECUCert/NR1L-ECUC-015、ECUCert/NR1L-ECUC-021 | Samuel |
| 7 | **X-d** | 本機 SSN 之 ECU certificate chain（`ecu.cacert`）。Samuel: also confirm ECU cert partition paths (A-SEC-16) and item 1/10/11/13/14 scope (A-SEC-17) | 5 | er=3 proc=2（結果型 3／觸發型 2）；例 ECUCert/NR1L-ECUC-001 proc L3；ECUCert/NR1L-ECUC-001 er L2 | ECUCert/NR1L-ECUC-001、ECUCert/NR1L-ECUC-013、ECUCert/NR1L-ECUC-023 | STLA 經 Samuel |
| 8 | **X-n** | **suspend／resume 之觸發手段** —— 037 SAM-0013 未載觸發方式 | 4 | er=2 proc=2（步驟型 2／值型 2）；例 SAM/NR1L-SAM-024 proc L1；SAM/NR1L-SAM-024 er L1 | SAM/NR1L-SAM-024、SAM/NR1L-SAM-025 | SAM 負責人 |
| 9 | **X-j** | **OTA／HAL 版本升級之映像檔與升級手段** —— 037 KI-008 之第二 sibling | 2 | er=1 proc=1（觸發型 1／結果型 1）；例 KeyInstall/NR1L-KI-015 proc L1；KeyInstall/NR1L-KI-015 er L1 | KeyInstall/NR1L-KI-015 | JY／Rivers |
| 10 | **X-m** | **兩次獨立取樣之 log snapshot ＋ 對稱金鑰比對手段** —— 037 LOGENC-006 4.1.3 | 2 | er=1 proc=1（步驟型 1／值型 1）；例 libLogEncrypt/NR1L-LOGENC-009 proc L5；libLogEncrypt/NR1L-LOGENC-009 er L3 | libLogEncrypt/NR1L-LOGENC-009 | LogEncrypt 負責人 |
| 11 | **X-c** | NR1L 正確 OID 之 Code Signing 憑證（leaf ＋ L1 PEM） | 1 | proc=1（觸發型 1）；例 CertProvider/NR1L-CP-025 proc L7 | CertProvider/NR1L-CP-025 | STLA 經 Steven |

## `X-i` 已裁降（不在本表）

Pei 2026-09-17 裁降為**文件審查**（R-SEC20）：原 16 行佔位全數消除，
8 TC（`NR1L-CP-011`~`-014`、`NR1L-CP-017`／`-018`、`NR1L-KI-023`／`-024`）改為
「取得 artifact ＋ 逐要件審查」式。**惟仍須 RD 開通建置環境之存取權**
（Pre-Condition `Access to the RD build environment for <component> is granted`），
此為排期事項，不再列為資產缺件。

## SEC-07 內查已解之代號（不再請求）

| 代號 | 解前行數 | 解後 | 依據 |
|---|---:|---:|---|
| `X-f-2` | 18 | **6** | Z1 `test_java_integration.py` 之 `KeyInstallDiagServiceManagerTests#getInstalledKeysStatus` 與 `KeyMasterWrapperAesTests#encryptDecryptNormalFlow`；`keys_install_helper.py` 之 `installstate` 路徑與狀態值 |
| `X-l` | 12 | **8** | CCVR `Auth-Prog CS.93` evidence 之 `31 01 F0 00` → `71 01 F0 00 00/01`；bit field 語意依 CS.00102 `SYS-RA-CS00102-685` |

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
