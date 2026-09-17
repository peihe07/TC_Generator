# DATA REQUESTS — Security (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/security/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

> **本表已依 R-SEC8（下放包 `_G` §2）重分類**，取代 `_D` §5 之 DR 總表：
> - **2.1 文件 DR**（送 037／SYS3 作者，**不阻交付**）：`a`／`b`／`i`／`r`／`s` —— `a`／`b`／`i` 已從寬結，仍送上游要正式件。
> - **R-SEC14(a)**：`DR-SEC-j2` 改號 **`DR-SEC-r`**；新增 **`DR-SEC-s`**。舊號 `j2` 不再使用（保留於 SEC-01 上繳包備查）。
> - **2.2 執行資產**（**移出本表**，見 `features/security/EXEC_ASSETS.md`）：`c`／`d`／`e`／`f`／`g`／`h` → `X-c`~`X-h`。
> - **2.3 已結／降級**：`j`／`k`／`l`／`m`／`n`／`o`／`q`／`h` 記 `CLOSED (R-SEC8(x))`，**不刪**（R-TM13）。
> - **2.4 A 系列**（回饋，不阻）：見 `ANOMALIES.md`。

## 2.1　文件 DR（不阻交付）

| # | 缺件 — 全名 | Status | Leaves served | Batch impact | Anomaly |
|---|---|---|---|---|---|
| DR-SEC-a | ECUCert 037 之 `SWE-Requirement ID` 補號 | **CLOSED (R-SEC8(a))**，仍送上游 | ECUCert 13 列 | 不阻。ID 用 `Source Requirement ID` 首值，Remarks `SWE ID pending; SYSAD used per R-SEC8(a)`；補號後依 R-G72 發 Revise | `[A-SE01]` |
| DR-SEC-b | `SWE1-KeyInsyall` 拼字更正 | **CLOSED (R-SEC8(b))**，順帶通知 | KeyInstall 13 列 | 不阻。原字入 ID 欄，Remarks `RD ID spelling as delivered` | `[A-SE02]` |
| DR-SEC-i | SYS3 SAM 之 `SYSAD_SAM_PACKAGE_INTF` 補 `Mapped SYSRA-ID`（**元件表存在而該列未填**，非 Table 11 漏列）| **CLOSED (R-SEC8(c))**，順帶通知 | `SWE1-SAM-0005~0008` | 不阻。去尾綴回退基底名為合法對應。**本 feature 實測 70/70 `exact`，`base` 未被觸發** | — |
| **DR-SEC-r** | `SWE1-SAM-0017` 之 `Verification Method` 補值（六本 70 列中唯一空白）| OPEN | `SWE1-SAM-0017` | 該列已依 review 三-3／R-SEC11(a) 入 Testing 群（CONVERT），**不阻產出**；只待上游補欄值 | `[A-SE03]` |
| **DR-SEC-s** | 其餘五本 037 之 Polarion 匯出（KeyInstall／SAM／ECUCert／SwdlSecureLib／libLogEncrypt）| OPEN（低優先，不阻）| 59 列 | 該 59 列之 `nrl_swe1` 填 `-`，Remarks 無 `Polarion:` 行；CertProvider 11 列已有（R-SEC9）| — |

## 2.3　已結／降級（R-SEC8；不刪，備查）

| # | 原缺件 | 處置 | 執行層複驗 |
|---|---|---|---|
| DR-SEC-h | CS.212 五情境 package | **CLOSED (R-SEC8(k))** —— 第 1/7/10/11/12 項之 tag 與期望字串以 `Secure Log CS.212` sheet 逐字，Remarks `per CS.212 draft 20260826`；第 2~6/8/9/13 項無 037 對應，不入本輪 | ✅ 五項之 tag 逐字複驗成立（`CertProviderServiceManagerTest`／`invalidKeyBlobEncryptRSAErrorFlow`／`sec_pki_ki_installer_lib`／`KeyMasterWrapperService`），已入 `step_assets.tsv`。資產面轉列 `X-h` |
| DR-SEC-j | CRL vs DCL | **CLOSED (R-SEC8(f))** —— 兩機制並存，各依母體原文；004／005 寫 **CRL**，CS.98 側寫 **DCL**，兩側不互相改寫 | ✅ CertProfile r40 之 HTTP CDP（CRL）與 CS.00102 5.2.2.43 之 DCL（DID `2031`）並存已證。`_F` §3 之改題文字保留備查。`step_sources` 之 `TERM:CRL\|DCL` 標記**保留**，用途轉為提示 Remarks 互註 |
| DR-SEC-k | RID `0x9001`／`0x9003` 金鑰佈建規格 | **降級為 reference (R-SEC8(g))** —— 037 KeyInstall-007 原文為 USB/SDCard 匯入，CAN 注入不在 037 範圍（IN §8.4.2）| ✅ CS.00102 與 R1L Diag SWQT **兩本皆全表現查、皆查無**。CS.212 第 10/12 項之 logcat 行逐字可用（已入 `step_assets.tsv`）|
| DR-SEC-l | `0x31 01 F0 00` 之回應碼 | **CLOSED (R-SEC8(i))** —— ER 逐字引 CCVR Auth-Prog 實測欄 | ✅ 三值逐字複驗成立。**須加限定**：r7 與 r8 同稱「lower rollback id」而回值不同（`01` vs `02`），引用時須連 `row <n>` 標明，否則同一敘述對到兩個值（`[A-SE11]`）。另 `image249.png` 不可得（1-5），惟語意已由 CS.00102 RQMT 文字取得（byte 4 bit field）|
| DR-SEC-m | CS.00165 §5.6／SD.00125 §5.1 之 DTC 碼 | **CLOSED (R-SEC8(j))** —— 主斷言改為 log `ECU_INSTALLATION_STATUS value : 2 -> 1` ＋ DID `22 29 66`；DTC 碼以 `<DTC per CS.00165 §5.6>` 佔位 | ✅ `SYS2_CS.00099`（5 sheet／258 非空列）之 `U3033`／`U3034`／`U160B`／`C221C` 命中 **0**；`CS.00165` 命中 1，為 REFERENCES 表之文件列舉非 DTC 定義。`DTCs Matrix Core List Rev. 1.6`（139＋100 列）四者亦 **0**（R-G13 記明） ｜**owner 提示（SEC-16 §5）**：CCVR v2.7 工作中版 `DTC-CS.99` 新增 owner 欄 —— `seure boot(harman)`（item 2/3）／`steven(DCL?)`（item 11）／`samuel`（item 12/13）；DTC 碼之現行負責人依此詢問 |
| DR-SEC-n | NR1L CDD（DID 實作本）| **CLOSED (R-SEC8(d))** —— 走 `2955 + 295D + 295E` 三分式；`2965` ER 寫 `up to 1000 bytes (CS.00102 5.2.2.75, SYS-RA-CS00102-415)`，R1L SWQT 之 2048 只入 Remarks | ✅ CS.00102 `SYS-RA-CS00102-410/411`（`295F`）之 `SYS2 分類 Category` 現查確為 **OutofScope**；`-415` 現查存在。`[A-SEC-3]` 併入此處 |
| DR-SEC-o | DID `0xFF02` 兩態 vs 037 四態 | **CLOSED (R-SEC8(e))** —— ER 以 Binder／log 面為準（四態依 037 KeyInstall-006 逐字）；DID `22 FF 02` 只入 Remarks，不作 pass/fail 判準 | ✅ 037 KeyInstall-011 原文確為 Binder `getStatus()`，未提 DID。另 SSN DID = `0x2975`（CFTS004 `SYS-RA-DIAG-008`），`FF01` 在 NR1L 為 RID（CS.00102 `-695~698`）|
| DR-SEC-p | DID `0x2951` 語意 | **CLOSED**（_D §1.2）| ✅ CS.00102 全 **731** 個 SYS2 ID 現查，**無 `2951`**。Cert Val 第 1 項改以 `2955`／`295D`／`295E`；Certificate Store UUID 指 SD.00045。CCVR sheet 之 2951 列登 `[A-SEC-1]` |
| DR-SEC-q | SAM 樹與 ECU Identity 樹之 cert profile | **降級為 reference (R-SEC8(h))** —— SAM-0007 ER 寫至 037 原文粒度；ECU Identity 樹名以 CS.165 sheet 逐字（`VHL_ROOT_G1`／`ECUID_SUBCA_G1`）；欄位細節只在 Code Signing 場景依 CertProfile 寫 | ✅ `trace_matrix` 之 16 列 `PENDING:DR-SEC-q` 標記**依本裁定改為 reference**，不再作 PENDING 理由（見上繳包 §9-1）|

## 2.2　執行資產 —— **已移出本表**

見 **`features/security/EXEC_ASSETS.md`**（`X-c`／`X-d`／`X-e`／`X-f`／`X-g`／`X-h`）。

**已結（不登）**：SYS3 六本 SYSAD、SYS2 CFTS084、CCVR SYS2_Mapped、
ECU Cert Test Steps PDF、`Test_Items.txt`、CS.00102 SWAD、CFTS004、SD.00049、
CS.00099／00100／00101、CS.000148、R1L Diag SWQT、VHAL User Guide R5、
CertProfile、DTC Matrix —— 皆已於 SEC-01 登錄（`sources/raw/` 或 `forms/`）。
