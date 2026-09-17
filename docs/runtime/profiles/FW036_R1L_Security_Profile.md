# FW036 R1L Security — Profile（**定稿**，SEC-02）

- 設立依據：下放包 **SEC-01 §4 任務 5** ＋ addendum **_A §3**／**_B §3**／**_C §2**／**_D §4**／**_E §3**
  （`docs/fw036/handoff/down/20260916_SEC-01*.md`）。
- 命名依既有慣例（CamelCase 無分隔，同 `VehicleCategory`／`PowerModing`）。
- **SEC-02 定稿**：SEC-01 之 `[PEI]`／`[PROPOSED]` 項已由 Pei 於 SEC-02 裁定（R-SEC9~R-SEC14），
  本檔隨之改為定值；仍未鎖定者（`SS` 判準面）明標待覆核。
- `framework.md` 已 **LOCKED 2026-09-16 (R-SEC10)**；此後變更走 R-G72 Revise。
- **母體標註**：本檔凡引用計數必標母體，限下列五者 ——
  037 六本合計 `70 列`／`ccvr_batch=1` `49 列`、`=2` `21 列`／產出群 `51`／D 群 `19`／
  鏈上 `SYS-RA-SEC` 併集 `161` 個／`SYS2 traceability` SEC 列 `737`／
  `step_assets.tsv` `152 列`／`diag_items.tsv` `46 列`／`apk_pairing.tsv` `15 列`。

---

## 0. 適用範圍

| 項 | 值 | 權威 |
|---|---|---|
| feature | `Security` | SEC-01 §4 任務 1 |
| slug | `security` | 同上 |
| Req 母體 | 六本 037（SWRA）共 70 列 | **R-SEC1(a)**；本包實測 |
| 一本 workbook 或六本 | **一本**（六個 Test Group）| **R-SEC10(a)** |
| `test_group`（工作簿 G 欄）| `Cert Provider`／`Key Install`／`SAM`／`ECU Cert`／`SWDL Secure Lib`／`Log Encrypt` | **R-SEC10(a)** |
| Layer 2 Test Set（H 欄）| **30 組**，leaf 70／產出 51／D 19 | **R-SEC10(a)**、**R-SEC11(c)**；`framework.md` LOCKED |
| Layer 3 | **不入工作簿**（IN §4.1.5），以 SYSAD ID 為單位 | SEC-01 §5 Layer 3 |
| ABBR（TC ID `NR1L-{ABBR}-{nnn}`，R-G42）| `CP`／`KI`／`SAM`／`ECUC`／`SWDL`／`LOGENC`，各組自 001 升冪；batch 1 先占號、batch 2 接續、不交錯 | **R-SEC10(b)** |
| `specification_reference`（N 欄）| `{037 token}_{SWE1-ID}`，六個 token 見 3.2 | **R-SEC10(c)** |
| 生成順序 | `ccvr_batch=1`（**49**）→ `ccvr_batch=2`（**21**）；D 群 **19** 不產 | **R-SEC1(b)(c)**、**R-SEC5(a) amend**、**R-SEC11(b)**、**R-SEC12** |
| Vehicle Model 七欄 | 五個有效車型全 `1`、`598`／`5210` 全 `0`（**70 列一律相同**）| R-CAM2 承接；本包 grep 實測見 2 節 |
| spec_mode | **`F`**（037-SWRA 母體）—— 新型別 | **R-SEC10(d)** |

---

## 1. lint 啟用（R-G70／R-G71）

依 R-G71，新 feature 之 profile **一律啟用 `X` 與 `P`(v4)**。
`P=0`／`X=0` 在未啟用時是沉默，不是核可。

| 代號 | 本 profile | 依據 |
|---|---|---|
| `P`(v4) | **啟用** | R-G70／R-G71 |
| `X`（導航路徑無固定入口）| **啟用**，惟**固定入口點清單須先擴增**（見 3 節 [ADD §5.8]）| R-G71；本 feature 無 HMI 入口 |
| `Y` | 隨 `P` 連動 | 既有慣例 |
| `Z`（Vehicle Model 七欄）| **啟用**（`FEATURE_CHECKS["security"]` 未含 `Z`；如需啟用須另加）—— 70 列七欄值一律相同 | R-CAM2 承接，見 2 節 |
| **`SC`**（channel／observe）| **已實作並啟用**，只入 `FEATURE_CHECKS["security"]` —— 對既有語料假陽性率 Procedure **98.4%**／ER **74.9%**（九本 1,700 列實測），**絕不可入 `PROFILE_CHECKS`** | **R-SEC7**、**R-SEC13(a)(b)**，見 3.4 |
| **`SS`**（`source:` 標記）| **已實作並啟用**，同上 | **R-SEC4(a)**、**R-SEC13**，見 3.4 |

呼叫形式：`python scripts/lint036.py --profile security <xlsx…>`。
**現況如實回報**：`lint036.py` 之 `--profile` 只作真值使用，不讀本檔內容
（VehicleCategory／Camera profile 已各自實測並記錄同一事實）。
故本檔 3 節之新檢查項**必須另行實作於 `lint036.py`** 才會生效，
不會因寫在本檔而自動啟用。`Z` 之啟用面亦須在 `FEATURE_CHECKS` 加 `"security"`。

---

## 2. Vehicle Model 七欄（R-CAM2 承接）—— 實測依據

下放包 §3 之預判：Security 六本為 middleware，與車型無關，七欄全列相同。

**實測（本包任務 4）**：以
`HDCC|DT27|DT28|Atl|platform|vehicle line|Commander|Renegade|Regengade|ProMaster|Toro|Fastback|598|5210|2261|376|637`
（不分大小寫）grep 70 列之 `Requirement Title` ＋ `Verification Criteria`：

- 命中 **1 列**：`SWE1-KeyInsyall-003`，命中詞為 `platform`／`Platform`。
- 逐字核該列原文：`put non-platform raw keys on USB flash` —— 指**金鑰之平台歸屬**
  （platform key vs non-platform key），非車型／EE 平台條件。
- 其餘 69 列 0 命中。

→ **預判成立**：70 列之 Vehicle Model 七欄一律相同，五個有效車型 `1`、`598`／`5210` `0`。
**不拆車型 sibling**（R-CAM3 之拆分判準於本 feature 不觸發）。

---

## 3. `[ADD]` 候選 —— 尚未實作，待 Pei 裁

### 3.0　欄位形制（SEC-03 §1 量測；**兩本一致，無須以 SWC 0708 仲裁**）

母體：**SWC 0708**（R-1 v2 基準本，286 資料列）＋ **pm_29**（389 資料列）。
規則（SEC-03 §1）：取兩本之**多數值**；不一致者以 SWC 0708 為準 —— **本次七欄皆一致**。

| 欄 | SWC 0708 | pm_29 | **Security 之寫法** |
|---|---|---|---|
| `Test Case Priority` | `P1` 190／`P2` 68／`P0` 27／空 1 | `P0` 260／`P1` 78／`P3` 42／`P2` 9 | **`P0`~`P3`**（不用 High/Medium/Low）|
| `Test Case Design Methods` | 中英雙語全文 7 值 | 中英雙語全文 4 值 | **`下拉選單` sheet 之雙語全文逐字** |
| `Input Test Data` | `NA` **285／286** | `NA` **389／389** | **一律 `NA`**（證實 R-SEC15(e)）|
| `Test Case Reference ID` | `NEW` 285／286 | `NEW` 389／389 | **`NEW`** |
| `Estimated Test Time` | **空 286／286** | **空 389／389** | **留空** |
| `Test Item` 上半 | 需求句（`HW supplier shall notify the … signal via the VHAL interface.`）| 條件句（`All TLM, AMP/ICS/DTV functionalities are available.`）| **037 `Requirement Description` 首句 verbatim**（R-SEC15(f)）|
| ER 內字面引號 | `"…"` **50**／`'…'` **0**／反引號 **0** | 三者皆 **0** | **只用 `"…"`**（證實 R-SEC15(d)）|

**Design Method 之可用值**（逐字＝ `下拉選單` sheet，9 值）：

```
功能測試 (Functional based ; no specific technique)
狀態轉換 (State Transition Testing)
決策表 (Decision Table Testing)
等價劃分 (Equivalence Partitioning, EP)
邊界值分析 (Boundary Value Analysis, BVA)
組合測試 (Combinatorial Testing ; Pairwise / t-wise)
情境 / 用例 (Scenario / Use Case Testing)
負向測試 (Negative / Invalid)
基礎故障注入 (Fault Injection Lite)
```

SWC 0708 之實際用值與上表**逐字相符**（7 值皆在其中），可證該欄取自下拉選單、非自由輸入。

> **Priority 之逐列值未定**：兩本之**格式**一致（`P0`~`P3`），但**分佈相反**
> （SWC 以 `P1` 為主、pm_29 以 `P0` 為主）—— 那是各 feature 之風險判斷，非形制。
> pilot02 一律用 **`P1`**（SWC 0708 多數值）。**逐列 priority 之 rubric 待 Pei 裁**（DECISIONS）。

> **`Test Item` 上半之語料差異**：SWC 為需求句、pm_29 為條件句，**兩本不同型**。
> 此欄不由「多數值」定 —— **R-SEC15(f) 已直接裁定**取 037 `Requirement Description` 首句，
> 與 SWC 之型態同族（需求句）。量測結果支持該裁定。

### 3.1 `[ADD §5.8]` 固定入口點擴增（`X` 之前提）

本 feature 無 HMI 入口，現行 `§5.8` 之固定入口點清單對其全不適用。候選新增四項：

| 入口 | 形態 | 素材依據 |
|---|---|---|
| `adb shell` | 指令列 | `step_assets.tsv` `cmd_adb` 14 筆（VC／APK／CS98／PDF） |
| `USB drive` | 實體介入 | `SWE1-KeyInsyall-002/003/007` VC；`SWE1-LOGENC-006` VC |
| `DIAG tester` | 診斷介面 | `SYSAD_SEC_ECUCERT_DIAG` VC；`ECU ID CS.165` Test steps |
| `Dealer App` | 應用程式 | `SYSAD_SEC_ECUCERT_DEALER` VC；ECU Cert Test Steps PDF 之 CSR 匯出 |

並允許 `$` 開頭之指令行作主流程（IN §5.4 兩行式；`$` 行不編號 —— **R-SEC4(d)**）。

### 3.2 `[ADD §10.7(c)]` `specification_reference` —— **定稿（R-SEC10(c)）**

格式 `{037 token}_{SWE1-ID}`，一行一筆。token 推導：檔名去副檔名、去前綴
`FM-WI-FSM-037-A03-N1L-`、去尾綴 ` STLA 報告_SWRA STLA Report_SWRA`、空白→底線。
**六值（執行層逐檔複驗吻合）**：

| Test Group | token |
|---|---|
| Cert Provider | `SWE1-CertProvider-SWE1R1-V1.0` |
| Key Install | `SWE1-KeyInstall-SWE1R1-V1.0` |
| SAM | `SWE1-SAM-SWE1R1-V1.1` |
| ECU Cert | `SWE1_ECUCert_FM-WI-FSM-037-A03` |
| SWDL Secure Lib | `SWE1_SwdlSecureLib_FM-WI-FSM-037-A03` |
| Log Encrypt | `SWE1_libLogEncrypt_FM-WI-FSM-037-A03` |

例：`SWE1-CertProvider-SWE1R1-V1.0_SWE1-CertProvider-004`。
ECUCert 依 **R-SEC3(b)** 以 SYSAD 首值代入，例
`SWE1_ECUCert_FM-WI-FSM-037-A03_SYSAD_SEC_ECUCERT_ECUCERT_API`。

**`spec_mode` `F` 之 lint 判準（R-SEC10(d)）**：只驗「token ∈ 上表六值 ＋ `_` ＋
SWE1-ID ∈ 70 列（ECUCert 為其 13 個 SYSAD）」，不查章節錨。

### 3.3 `[ADD §5.3]` 常數候選

由 `features/security/data/step_assets.tsv`（106 列）產出，
`build_step_assets.py` 可重跑。分佈：
`path` 24／`state_value` 23／`junit_method` 18／`cmd_adb` 14／`filename` 11／
`placeholder` 6／`cmd_openssl` 4／`cmd_shell` 4／`cmd_od` 1／`hex_blob` 1。

首批常數候選（逐字自來源，未改寫）：

| 常數名（候選）| 值 | 來源 |
|---|---|---|
| `RUN_CP_INSTRUMENT_TEST` | `adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#<method> com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | `Test_Items.txt`、`Cert Val CS.98` STEPS |
| `RUN_CP_INSTRUMENT_ALL` | `adb shell am instrument -w com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | `Test_Items.txt` |
| `READ_ECUCERTSTATUS` | `adb shell "od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus"` | ECU Cert Test Steps PDF |
| `PATH_CERT_STORE` | `/vendor/odm/etc/cert_store/` | `Cert Val CS.98` STEPS |
| `PATH_OEM_KEYS` | `/mnt/vendor/oemkeys` | `SWE1-KeyInsyall-003` VC |
| `PATH_ECU_IDENTITY` | `/data/misc/ecuidentity/ecu.crt` | ECU Cert Test Steps PDF、`ECU ID CS.165` |
| `PATH_DAUTH_SEQID` | `/data/vendor/dauth/seqId` | `SWE1-SAM-0017` VC |
| `KEYINSTALL_ERROR_STATUS` | `0900 0000 0000 0000` | `SWE1-KeyInsyall-003` VC |
| `LOG_DECRYPT_TOOL` | `$ ./logdecrypt_Ver2.sh HUssss_YYYYMMDD_HHMMSS_XXXX.enc HUssss_YYYYMMDD_HHMMSS_XXXX_enckey.enc` | `SWE1-LOGENC-006` VC |
| `ENTER_SUPPLIER_SESSION` | `Send UDS request DiagnosticSessionControl` ＋ `$ 10 60` | **R-SEC6(c)**；`R1L-SWQT` 前例 |
| `SET_ARCH_TYPE_HI` | `$ 2E 28 50 05` | `VHAL_User_Guide_R5` §2.4（Atl-Hi）|
| `SET_ARCH_TYPE_MID` | `$ 2E 28 50 03` | 同上（Atl-Mid）|
| `ADB_ROOT_READY` | `DUT is connected via ADB with root permission (Dev/Eng build)` | **R-SEC7(d)** |
| `DIAG_SESSION_<xx>` | `Diagnostic session is <Extended (03) \| SystemSupplierSpecific (60)>` | **R-SEC7(d)**／R-SEC6(c) |
| `CP_TEST_RUNNER_INSTALLED` | `Test runner CertProviderAndroidInstrumentalTest.apk is installed` | **R-SEC7(d)**；**R-SEC24**（SEC-13 更正檔名，A-33）|

**表內 4 列為雜訊候選，待 Pei 裁剔除**：`step_assets.tsv` 之
`/cfgs`、`/odm`、`/write`、`/r/sites/newR1LAllMDmembers/_layouts/15/Doc.aspx`
（末者為 PDF 內之 SharePoint 連結片段，非受測路徑）。

### 3.4 `[ADD]` lint 候選 —— 兩項

**候選一：`source:` 標記（_A §3）**

- **判準**：Procedure 之最終步驟含 `Verify`／`Check`／`Confirm`，而該列 reasoning
  無 `source:` 標記者，報 **WARN**。
- 依據：**R-SEC4(a)** —— 每一步驟須能回指五類既有來源之一並於 reasoning 註明。

**候選二：`C`（channel／observe，_E §3）**

- **判準（Procedure）**：每一編號步驟其後必有 `$` 指令行，
  或步驟句以 `Insert`／`Press`／`Power cycle`／`Disconnect`／`Select "` 起首；否則 **FAIL**。
- **判準（ER）**：每行須含 R-SEC7(c) 七類觀察手段之一的標記；否則 **FAIL**。
- 依據：**R-SEC7(a)(c)**。

**_E §3 要求之 pilot 前假陽性實測（已做）** —— 對既有九本交付本 1,700 列：

| 交付本 | 有 Procedure 之列 | Procedure FAIL | ER FAIL |
|---|---:|---:|---:|
| SWC 0708（R-1 v2 基準本）| 286 | 285（99.7%）| 64（22.4%）|
| DealerMode 20260417(done) | 125 | 107（85.6%）| 117（93.6%）|
| power `pm_29` | 389 | 389（100.0%）| 373（95.9%）|
| power `pm_73` | 287 | 287（100.0%）| 283（98.6%）|
| sw_update 20260830 | 319 | 319（100.0%）| 311（97.5%）|
| ics_management 20260830 | 31 | 31（100.0%）| 31（100.0%）|
| vehicle_setting CFTS044 | 241 | 233（96.7%）| 74（30.7%）|
| vsm_v42 20260902 | 17 | 17（100.0%）| 15（88.2%）|
| popup 20260908 | 5 | 5（100.0%）| 5（100.0%）|
| **合計** | **1,700** | **1,673（98.4%）** | **1,273（74.9%）** |

> **此數字之讀法（R-G8：比率須載明分子與分母；R-G11：須聲明盲區）**：
> 既有交付本**不受 R-SEC7 拘束**，故其 FAIL 全數為假陽性 —— 分母是「既有語料」，
> 不是「Security 之 70 列」。此表**不證明 `C` 判準有缺陷**，
> 它證明的是：**`C` 一旦入 `PROFILE_CHECKS`（隨任意 `--profile` 生效），
> 既有十本交付簿會整批 FAIL**。故 `C` 必須入 `FEATURE_CHECKS["security"]`。
> `C` 對 Security 自身之假陽性率，須待 pilot 產出後才測得到，**本包無法給**。

### 3.4-a　代號與實作狀態（SEC-02 定稿）

**代號 —— `SC`／`SS`（R-SEC13(b)）**。R-SEC13(b) 要求「若只支援單字元，回報現行占用表」：

- **單字母 `C` 已被既有檢查佔用** —— `CHECK_TITLES["C"] = "hedge (test_item 括號下半)"`，
  在 `CHECK_ORDER` 內，對所有 feature 生效。**故 `C` 不可用。**
- `lint036.py` 之代號為 dict key（字串），**多字元有既有先例**（`I-cross`、`I-sibling`），
  故依 R-SEC13(b) 之首選取 **`SC`**（channel）與 **`SS`**（source:）。
- 現行占用（`CHECK_ORDER` ＋ `PROFILE_CHECKS` ＋ `FEATURE_CHECKS`）：
  `A B C D E F G H I I-sibling J K L M N P` ＋ `Q R T U V I-cross W X Y` ＋ `Z`(camera)。
  單字母剩餘：`O S`（`O` 易與 0 混淆）。**`SC`／`SS` 不佔用單字母空間。**

**實作 —— 已落於 `scripts/lint036.py`**：

```python
FEATURE_CHECKS: dict[str, list[str]] = {"camera": ["Z"], "security": ["SC", "SS"]}
```

＋ `check_security_channel()`（`SC`）、`check_security_source()`（`SS`），
於 `lint_sheet()` 內以 `if "SC" in enabled` ／ `if "SS" in enabled` 逐列施檢。

**回歸（R-SEC13(a) 之保證面）**：`pm_29.xlsx` 三條既有呼叫路徑之輸出 **byte 相同**
（`--profile` 無／`--profile camera`／`--profile power`，sha16 `e2ffac8eb9fd6838`／
`0bd777a9334105d1`／`45b56a6eeca86a29`，前後不變）；`tests/test_lint036_z.py` 27 項全過。

### 3.4-b　**`SS` 之判準面偏差（待 Pei 覆核）**

R-SEC4(a) 原文為「於 **reasoning** 註明來源與位置」，而 reasoning 在生成側 JSON、
**不在工作簿**；`lint036.py` 之施檢面是 xlsx。

→ `SS` 改以 **`Remarks` 欄（AH）之 `source:` 標記**為判準面。
判準：Procedure 之**最後一個編號步驟**含 `Verify`／`Check`／`Confirm`，
而該列 `Remarks` 無 `source:` 者記一筆（每列一筆）。
**R-SEC14(c)**：`<…>` 佔位不報。

**此為執行層之落地選擇，非條文所載**，已於 SEC-02 上繳包自報；
若 Pei 認為應改為對 JSON reasoning 施檢，則 `SS` 須移出 `lint036.py`、
另掛於生成側之 selfcheck。

### 3.5 `[ADD §5.4]` DID／RID 步驟定式（R-SEC6）—— 本專案首例

**R-G13 查證**：九本既有交付本 1,700 列，`Procedure` 欄與 `Expected Result` 欄
**UDS 樣式命中 0 列**（bytes 式與 `ReadDataByIdentifier` 等服務名皆然）；
唯一命中為 SWC 0708 `Pre-Condition` 欄 32 列之需求敘述文字，非步驟。
→ **無既有格式可沿用**，R-SEC6(a)~(e) 為本專案首例之定式。

### 3.6 `[ADD §8.7.5]` VHAL → CAN 之橋（_C §5）

VHAL 層訊號**不是** CAN 訊號，不得直接以 VHAL property 名寫 `Send CAN:`。
限用於 **SAM-0013**（boot／resume 通知 OFF）與 **SAM-0017**（IGN ON 時 seqId 歸 0）：

| VHAL property | CAN 訊號 | 訊息／CAN ID／通道 |
|---|---|---|
| `IGNITION_STATE` (0x11400409) | `CmdIgnSts` | Atl-Hi `BCM_FD_10` 0x481 (AH_FDCAN8)；Atl-Mi `STATUS_BH_BCM2` 0x46C (AH_BHCAN2) |
| `POWER_MODE_STS` | `PowerModeSts` | `BCM_FD_9` 0x42A (AH_FDCAN8) |

raw／label 逐字取 `forms/` DBC（R-7、R-17）；VHAL Guide 只定訊號名與通道。
Atl-Hi／Atl-Mi 訊息不同 → 依 R-CAM3(e) 同型處理。**其餘五本 037 不引用 VHAL Guide。**

---

## 4. Layer 2 對帳（任務 4 回填）

`features/security/data/layer2_assign.tsv` —— 70 列全數歸屬，
**30 組 Test Set 之 leaf 數與下放包 §5 表逐組相符**（`build_layer2_assign.py` 自動對帳）。
`ccvr_batch` 回填見該檔與上繳包 §5。

---

## 5. 盲區（R-G11：可測判準須同時聲明其盲區）

1. **無 SYS1 HMI 匯出** —— 本 feature 之 `specification_reference` 不走章節錨，
   3.2 之格式若 Pei 不採，現無替代錨源。
2. **CCVR 為 reference-only** —— 不得作 `specification_reference` 錨、不得作 Req 來源
   （IN §8.1／§8.4.2）。其 STEPS 只作 **步驟素材**（R-SEC4(a)4）。
3. **`step_sources` 非空 ≠ 可執行** —— 70 列中 20 列僅有 `VC` 一種來源；
   測試資產（DR-SEC-c～h）未到前，該 20 列之 Procedure 仍會掛
   `PENDING: DR-SEC-{n}`（R-SEC4(b)）。
4. **`X` 在入口點擴增前不可判綠** —— 3.1 未實作前，`X` 對本 feature 之 70 列
   會整批報 WARN，該批 WARN **不構成品質訊號**。
5. **`C` 之假陽性率只對既有語料測得** —— 3.4 之 98.4%／74.9% 其分母是既有交付本，
   不是 Security 之 70 列。`C` 對本 feature 之真實假陽性率**本包給不出**，須待 pilot。
6. **`channel_feasible` 是預判不是驗證** —— `trace_summary.md` 4b 節之 `Y` 42／`部分` 8／`N` 20
   由「有無外部可執行素材」推得，**未逐步驗證**。實際能否逐步配到通道，
   要到 Phase 2 寫出步驟才知道。
7. **DID 值以 R1L 前例本代用** —— NR1L CDD 未到（DR-SEC-n），`diag_items.tsv` 中
   6 項 `definition_source = R1L-SWQT:*`，其值與 NR1L 現行值**可能不同**
   （已知 `2965` 長度 1000 vs 2048、`FF01`／`FF02` 之語意變動）。
   依 R-SEC6(e) 逐列標 Remarks，CDD 到手後發 Revise。
