# EXEC ASSETS — Security（FW036）

執行資產清單。依 **R-SEC8**（下放包 `_G` §2.2）自 `DATA_REQUESTS.md` 移出：
這些**不阻交付**（TC 寫得出來），**阻實機執行**（沒有資產就跑不了）。
故與 DR 分列，每包上繳附現況。

TC 內之寫法：資產以 **Pre-Condition 一行**點名（R-SEC7(d) 之連線／權限狀態另計），
**不寫 `PENDING`** —— 資產缺席是執行面問題，不是規格面缺件。

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
| **X-h** | CS.212 正式 package（Cybersecurity team review 後）| — | R-SEC5 直連之 11 列 | Steven／Shawn | Revise 時 | 未到；**惟 R-SEC8(k) 已准以 CS.212 draft 之 tag／期望字串逐字落地，故不阻本輪** |

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
