# EXEC ASSETS — Security（FW036）

執行資產清單。依 **R-SEC8**（下放包 `_G` §2.2）自 `DATA_REQUESTS.md` 移出：
這些**不阻交付**（TC 寫得出來），**阻實機執行**（沒有資產就跑不了）。
故與 DR 分列，每包上繳附現況。

TC 內之寫法：資產以 **Pre-Condition 一行**點名（R-SEC7(d) 之連線／權限狀態另計），
**不寫 `PENDING`** —— 資產缺席是執行面問題，不是規格面缺件。

**SEC-08 起（R-SEC21）**：原以整行 `PENDING: X-<n> …` 標記之位置，一律改為
**描述性佔位** `<性質 provided by <供給方> (X-<n>)>`；下表「寫法」欄所載之 `PENDING:` 式
為**歷史式**（v03 及以前之工作簿）。v04 之逐行佔位位置見 `data/placeholder_summary.tsv`
（96 行）與 `data/placeholder_by_token.tsv`（11 token）。

---

| 代號 | 資產 | Pre-Condition 寫法（TC 內） | 服務之 SWE1 列 | 找誰 | 急迫 | 現況 |
|---|---|---|---|---|---|---|
| **X-c** | NR1L 正確 OID 之 Code Signing 憑證（leaf ＋ L1 PEM）| `A leaf certificate with the NR1L project-specific critical extension is available` | `SWE1-CertProvider-011` 及全部 CS.98 正式 evidence | STLA 經 Steven | **9/18 Dev-Key build** | 未到 |
| **X-d** | 本機 SSN 之 ECU certificate chain（`ecu.cacert`）| `An ECU certificate chain issued for the DUT SSN is available` | ECUCert 13 列、`SWE1-CertProvider-005` | STLA 經 Samuel | **9/18** | 未到；CS.165 workshop 暫停中 |
| **X-e** | CertProvider 六組憑證（valid／broken／revoked／wrong-subject／wrong-issuer／wrong-OID）＋ RD 預產 `dcl_baseline.json`、`dcl_revoked_l0~l3.json` | 各列點名 | `SWE1-CertProvider-001~005`／`-011` | Steven | 前批（batch 1）| 未到；DCL readiness 對齊 9/18 build、9/20 code freeze |
| **X-e-2**（SEC-03 §3 增）| **wrong-subject 憑證之 DUT 側觸發手段** —— apk 方法或 RD 提供之腳本。現況：`Test_Items.txt` 15 條**無**對應方法；host 端 openssl 不構成 DUT 觸發（R-SEC15(b)）| `PENDING: X-e wrong-subject certificate + trigger` | `SWE1-CertProvider-002` 負向分支 | Steven／RD | 前批 | 未到 |
| **X-e-3**（SEC-03 §3 增）| **wrong-OID 憑證之 DUT 側觸發手段** —— 同上 | `PENDING: X-e OID certificate + trigger` | `SWE1-CertProvider-011` 兩分支 | Steven／RD | 前批 | 未到 |
| **X-f** | KeyInstall 三組 USB 金鑰（valid／non-valid／non-platform R1LRefresh）| `A USB drive containing <組別> keys is available` | `SWE1-KeyInsyall-002`／`-003`／`-007` | KeyInstall 負責人 | 前批 | 未到 |
| **X-f-2**（SEC-03 §3 增）| **KeyInstall status test runner** —— Binder `getStatus()` 之可執行入口。**候選檔（只列檔名，未拆 zip）**：`KeyInstall_IntegrationTests.zip`，76,461 B，sha16 `de46aba5dc9b6e9b`，外部路徑 `2_Architecture/CCVR/To Validation team/Secure Log CS.212/StevenJSHsu/`。**是否含該 runner 未知**（未拆） | `PENDING: X-f KeyInstall status test runner` | `SWE1-KeyInsyall-011` 兩分支 | Steven／KeyInstall 負責人 | 前批 | 未到；檔已定位 |
| **X-g** | SAM 四 SAMType AuthData（`{SSN}_SAM_{SAMType}.json` ＋ `.sig` ＋ cert）；ValidityCounter `0`／`1`／`65535`；TimeStamp 舊於已裝者一組；SAM dongle | 各列點名 | SAM 19 列 | SAM 負責人 | 後批（batch 2 為主）| 未到 |
| **X-g-2**（SEC-04 增）| **SAM 狀態變更之觸發手段**（使 DebugAuth 送出 status 訊息，供 seqId 驗證）—— 037 SAM-0015 之 WHEN | `PENDING: X-g SAM AuthData status change + trigger` | `SWE1-SAM-0015` | SAM 負責人 | 後批 | 未到 |
| **X-h** | CS.212 正式 package（Cybersecurity team review 後）| — | R-SEC5 直連之 11 列 | Steven／Shawn | Revise 時 | 未到；**惟 R-SEC8(k) 已准以 CS.212 draft 之 tag／期望字串逐字落地，故不阻本輪** |
| **X-j**（SEC-04 增）| **OTA／HAL 版本升級之映像檔與升級手段** —— 037 KI-008 之第二 sibling | `PENDING: X-j OTA or HAL upgrade image + trigger` | `SWE1-KeyInsyall-008` sibling 2 | SW 整合 | 後批 | 未到 |
| **X-k**（SEC-04 增）| **Dealer App 對 DUT 之存取**（ECUCert Dealer Service 之 `UI` 通道入口）—— Test Steps PDF 載有 CSR 匯出入口，惟未載金鑰更新操作 | `PENDING: X-k Dealer App access to the DUT` | `SYSAD_SEC_ECUCERT_DEALER`（2 sibling）| Samuel | 後批 | 未到 |
| **X-l**（SEC-04 增）| **SwdlSecureLib 之解密／驗證測試入口**（程式庫介面之可執行 harness）—— 037 SWDL-003/004 為程式庫內部介面，無 apk 對應 | `PENDING: X-l SWDL <decryption|verification> test entry point` | `SWE1-SRA-SECURITY-SWDL-003`／`-004`（各 3 sibling）| SWDL 負責人 | 後批 | 未到 |
| **X-m**（SEC-05 增）| **兩次獨立取樣之 log snapshot ＋ 對稱金鑰比對手段** —— 037 LOGENC-006 4.1.3「compare the symmetric key in different iteration」 | `PENDING: X-m two log snapshots taken in separate iterations + comparison` | `SWE1-LOGENC-006` sibling 3 | LogEncrypt 負責人 | 後批 | 未到 |
| **X-n**（SEC-06 增）| **suspend／resume 之觸發手段** —— 037 SAM-0013 之「resume from suspend」未載觸發方式；VHAL Guide 無對應之 CAN 值（`PowerModeSts` 之 `VAL_` 只有 Standard_Power／Logistic_Mode_*，A-19） | `PENDING: X-n suspend/resume trigger method` | `SWE1-SAM-0013` sibling 3／4（`NR1L-SAM-025`／`-026`）| SAM 負責人 | 後批 | 未到 |

---

## 已結案（不再阻執行）

| 代號 | 結案依據 | 說明 |
|---|---|---|
| **X-i**（SEC-04 增；SEC-08 結）| **CLOSED (R-SEC20)** | 原求 Cert Provider／KeyInstall 之原始碼與建置環境（Android.bp、靜態分析報告、安全掃描報告）。Pei 2026-09-17 裁降為**文件審查**：8 TC（`NR1L-CP-011`~`-014`、`NR1L-CP-017`／`-018`、`NR1L-KI-023`／`-024`）依 R-SEC20 重寫為「取得 artifact ＋ 逐要件審查」式，Pre-Condition 改 `Access to the RD build environment for <component> is granted`。v04 已無 `X-i` 佔位（原 16 行全數消除）。**惟建置環境之存取權仍須 RD 開通**，此為排期事項，不再列為資產缺件 |

---

## 與 DR 之界線（R-SEC8）

- **DR**（`DATA_REQUESTS.md`）= 文件面缺件，向 037／SYS3 作者要；本檔 = 執行面資產，向 RD／STLA 要。
- 本檔任一項未到，**TC 仍照寫**（Procedure／ER 依既有素材逐字落地，R-SEC4）；
  只是該列在實機上跑不起來，屬**執行排期**問題。
- **不得**因本檔之資產未到而在 TC 內寫 `PENDING`（R-SEC8 之總則：canon 只禁造值，不禁佔位）。

## 盲區（R-G11）

本表之「現況」欄為 **2026-09-16 當日之轉述**，來源為下放包 `_G` §2.2 與 9/16 workshop 紀錄，
**非執行層直接查證** —— 執行層無法自 repo 內驗證實體資產之到位與否。
每包上繳時須向 Pei 覆核，不得沿用舊值。
