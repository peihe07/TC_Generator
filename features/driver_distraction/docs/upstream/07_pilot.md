# 上繳包 07 —— T14a–c、T15 pilot（組 3，4 TC）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`09_pilot_spec.md` §五（T14a–c、T15）
- 本輪**未寫回工作簿、未執行 git**；產物置 `generated/`
- 共用路徑：**未寫入一字**（T14a 停於此，理由見 §1）

> **三句話**：
> **T14a 停** —— 該 tsv 是 `scripts/rulings_hash.py` 的**產物**，不是手抄簿；
> 追加列會在下次重跑時被抹掉，且本檔無錨點標題，其 sha 之定義域不存在（§1）。
> **T14b 清白** —— `Speedometer`／`PresentGear` 於 `CAN Mapping` 皆唯一，
> 下放包所引之 r1738／r1397 回核 A 欄相符（§2）。**pilot 閘開。**
> **T15 交 4 TC，13 檢全綠**；過程中自檢抓到一個真缺並已修（§5.2）。

---

## 1. T14a —— **停**，不追加

### 1.1 為何停

下放包 §五 T14a 令「讀既有 schema，**照其形制**以 `edit_file` 追加」。
schema 讀得到，但**照其形制追加**這件事做不到，三個獨立理由：

#### (一) 該 tsv 是產物，不是簿

`docs/fw036/FEATURE_ONBOARDING.md` R-G13 逐字：

```
`scripts/rulings_hash.py` 產生 `RULINGS.sha.tsv`（ruling_id → 條文本體 sha256），該 tsv 入版控。
```

該工具存在（`scripts/rulings_hash.py`），且其**預設範圍早已涵蓋本檔**：

```python
# R-POP11（Pei 2026-08-27）：預設範圍納入**全部** `features/*/RULINGS.md`。
```

**手工追加之列，下次任何人重跑該工具即被覆蓋消滅**；
且其 `--check` 為逐位元比對（`out_path.read_text() != body`），
追加後 `--check` 必 FAIL。

#### (二) 本檔無錨點，sha 之定義域不存在

工具對「條文本體」之定義（其 docstring 逐字）：

```
自錨點標題之**次行**起，至下一個同級或更高級標題之**前一行**止；
首尾空行去除，行尾空白去除，行間以 `\n` 接合，UTF-8 編碼後取 sha256。
標題文字本身**不入雜湊**
```

錨點正則為 `^(#{2,4})\s*(R-[A-Z]{0,3}\d+…)`，即 **`### R-DD6` 這種標題**。
**本 feature 之 `RULINGS.md` 用 ` ``` ` 圍籬，一個標題錨點都沒有。**

**實測**（輸出導向 scratchpad，未碰共用檔）：

```
$ python3 scripts/rulings_hash.py --target features/driver_distraction/RULINGS.md --out <scratch>
寫入 …：0 錨點（），來源 1 檔

$ python3 scripts/rulings_hash.py --target features/popup/RULINGS.md --out <scratch>
寫入 …：20 錨點（ruling 20），來源 1 檔
```

**沒有錨點就沒有「次行」，也沒有「下一個同級標題」** —— 本體之起訖無從界定。
要填 sha 就得自己發明一個本體範圍，**那正是拘束二所禁之「猜」。**

#### (三) 這是全域形態，不是本 feature 之個案

以工具全域重生一份到 scratchpad，逐 feature 對照
（**母體 = `features/*/RULINGS.md` 共 15 檔**）：

| feature | tsv 收錄 | 標題錨點 | 圍籬條文 |
|---|---|---|---|
| vehicle_setting | 217 | 217 | 163 |
| power_moding | 153 | 153 | 154 |
| time_management | 88 | 88 | 85 |
| comfort | 40 | 40 | 50 |
| popup | 20 | 20 | 0 |
| audio_mgmt | 7 | 7 | 0 |
| user_profiles | 3 | 3 | 0 |
| **display** | **0** | **0** | **59** |
| **sw_update** | **0** | **0** | **31** |
| **vehicle_category** | **0** | **0** | **30** |
| **bed_lowering** | **0** | **0** | **17** |
| **driver_distraction** | **0** | **0** | **11** |
| amfm／power／privacy | 0 | 0 | 0 |

**收錄數恰等於標題錨點數，與圍籬條文數無關。**
**5 個 feature、合計 148 條圍籬體例之條文，工具全部看不見**
（display 59／sw_update 31／vehicle_category 30／bed_lowering 17／driver_distraction 11）。

> **「tsv 少了 R-DD」不是漏登，是體例不合。**
> 補登 11 列只治本 feature 之症，另外 4 個 feature 的 137 條照樣看不見，
> 而且補的列下次重跑就沒了。

### 1.2 真正的修法（屬分析層／Pei）

**把 `RULINGS.md` 改為標題錨點體例，再以工具重生 tsv。** 二事皆非執行層可逕為：

1. **改體例**牽動條文區塊之呈現，而 R-DD6 v1 等留存條文須「不刪不改」
   （R-TM13）—— 加標題算不算「改」，須裁
2. **重生 tsv** 是整檔覆寫共用路徑之產物檔。A-DD4 允局部追加，
   但這個檔**沒有「局部」可言** —— 它是工具一次寫全的
3. 若 5 個 feature 一起改，那是全域政策，不在本線裁

### 1.3 另一件實測到的事 —— tsv 現已與條文不符

```
$ python3 scripts/rulings_hash.py --check
FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
```

**成因非本線**：重生版比現行版多 3 列，全為 `R-POP18`／`R-POP19`／`R-POP20`
（popup 線本輪新增，其 `RULINGS.md` 已改而 tsv 未重生）。
**逐行差異 13 行，R-DD 相關 0 行。**

**未動該檔。** 記此以免日後 `--check` FAIL 被歸因於本輪。

---

## 2. T14b —— **清白**，pilot 閘開

母體判準（R-DD10(c)）：`LID CAN Mapping`，**r4 起至 r2629**
（r1 表題／r2 架構帶／r3 欄名，排除）；A 欄非空者計入。

```
非空 Logical Identifier 列數 = 2626；unique = 2548
重複之 LID 名 = 68，佔 146 列
重複組之列數分布：2 列 × 59 組／3 列 × 8 組／4 列 × 1 組
```

> **該分頁之重複比 `Proxi & Configuration` 嚴重得多**（68 組 vs 17 組，
> 且有 3 列組與 4 列組）。**這正是本閘存在的理由。**

### 2.1 閘之判定

| 訊號 | 完全相等之列 | 含該字串但不相等者 | 判 |
|---|---|---|---|
| `Speedometer` | **[1738]** | **無** | **唯一 ✓** |
| `PresentGear` | **[1397]** | **無** | **唯一 ✓** |

「含該字串但不相等」一項是刻意加的 —— 只比完全相等，
會漏掉 `Speedometer_2`／`PresentGearDisplay` 這類變體。**實測二者皆無。**

### 2.2 下放包所引列號之回核（§九 `ACV_FailType` 案例之防線）

| 引用 | A 欄實測 | 期待 | 判 |
|---|---|---|---|
| `LID CAN Mapping r1738` | `'Speedometer'` | `Speedometer` | **相符 ✓** |
| `LID CAN Mapping r1397` | `'PresentGear'` | `PresentGear` | **相符 ✓** |

下放包 §四-4 稱該覆核「當輪已做」——**本輪重跑，結果相符**。
重跑的成本遠低於指錯列的成本。

### 2.3 ⚠ 順帶量到的兩件事（非閘之判準，但影響 profile 之讀法）

**`CAN Mapping` 之架構帶與 `Proxi & Configuration` 不同：**

```
CAN Mapping          ：A=LID Information／F=Powernet／K=CUSW／P=Atlantis／
                       U=Compact／Z=Atlantis High／AE=Comments
Proxi & Configuration：A=LID Information／F=Powernet／K=CUSW／
                       P=Atlantis & Atlantis High／U=Compact／Z=Comments
```

**前者 `Atlantis` 與 `Atlantis High` 是兩個分開的帶（P 與 Z）；後者合為一帶（P）。**
R-DD6 v2(b)（「二欄不同字時取 Atlantis High」）**只在 `CAN Mapping` 上有分辨力**。

**(a) `Speedometer` 之 Atlantis High 欄載有兩個訊號名**：

```
Z  [Atlantis High · Signal Name] = "STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts
                                    BRAKE_FD_2.VehicleSpeedVSOSig"
AA [Atlantis High · CAN]         = 'CAN-B\n\n\nFD'
P  [Atlantis · Signal Name]      = "STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts"
```

profile §3 取 `STATUS_CCAN3.VehicleSpeedVSOSig`（CAN-B 側）。
**`BRAKE_FD_2.VehicleSpeedVSOSig`（FD 側）同在 Atlantis High 欄而未取。**
R-DD6 v2 **未規定一格內載多名時如何取** —— 本輪依 profile 既定值，
**不自行擇一**，記此待裁。

**(b) `PresentGear` 之 Atlantis High 欄亦載二名**，但該列 AE 欄自陳：

```
'VDCM_PWT2.GearEngagedForDisplay_VDCM
This signal is used only for the M182BEV program. …'
```

**故 profile 取 `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT` 有來源側之根據**，非擇一。
**(a) 沒有這樣的註記** —— 二者狀況不同，不可一併看待。

### 2.4 profile §3 之回讀確認（下放包 §四-3 所命）

已回讀 profile（**唯讀，未寫一字**）：§3 三列已解除、§3.1 raw 表與
§3.2 fail-safe 形態均在、`$VC_Trans_Equipped$` 維持 SUSPENDED。**與下放包所述相符。**

其所載之訊號事實，本輪對 DBC **獨立重測**：

| profile 所載 | DBC 實測 | 判 |
|---|---|---|
| `STATUS_CCAN3`、msg 994、13 bit、factor 0.0625、offset 0、Km/h | `BO_ 994 STATUS_CCAN3`；`SG_ VehicleSpeedVSOSig : 47\|13@0+ (0.0625,0) [0\|511.9375] "Km/h"` | **相符 ✓** |
| 失效值 `= 8191 (SNA)` | `VAL_ 994 … 8191 "SNA"` | **相符 ✓** |
| `PT_SYSTEM_FD_1`、msg 263、5 bit、factor 1 | `BO_ 263 PT_SYSTEM_FD_1`；`SG_ GearEngagedForDisplay_PT : 12\|5@0+ (1,0) [0\|31]` | **相符 ✓** |
| Park = `12 (Park)` | `VAL_ 263 … 12 "Park"` | **相符 ✓** |

（`GearEngagedForDisplay_PT` 之 SNA 為 **31**，非 8191 ——
本輪 4 TC 未用及該值，記之備後用。）

---

## 3. T14c

| 項 | 動作 | 結果 |
|---|---|---|
| **DR-DD5** | **保留號 → 正式條目** | DRAFTED；§二文稿逐字 **1528 字元，落檔 1 次** |
| **DR-DD6** | **版本號改正** | `v1_78` → `v1_76`，**一處，僅版本號**；改後回讀 `v1_78` 殘留 **0**、`v1_76` **1** |
| 二者關係 | 台帳明記 | 摘要表註記 ＋ DR-DD5 節末對照表 |

---

## 4. T15 —— pilot 4 TC

**產物**：`features/driver_distraction/generated/pilot_group3.json`
**生成器**：`scripts/gen_pilot_group3.py`（`test_item` 上半自 037 **機器擷取**，不手打）
**自檢**：`scripts/selfcheck_pilot_group3.py`

### 4.1 上半之擷取規則（R-S4）

| leaf | 037 全文 token | 模式 | 落檔 token |
|---|---|---|---|
| `-009` | 55 | `excerpt(Case..Then)` | **25** |
| `-010` | 47 | `full` | **47** |
| `-011` | 55 | `excerpt(Case..Then)` | **25** |
| `-012` | 47 | `full` | **47** |

逾 50 token 者取 `Case`／`Then` **二行之連續摘句** —— 該二行為條文之操作性內容，
**且為 `-009`／`-011` 之相異處**（其 `When`／`And` 二行逐字全等，取之無分辨力）。
生成器對每一則 `assert 摘句 in 原文`，**非子串即中止**。

### 4.2 取樣 feature 之選定（profile §2.1）

HMI spec p7 `Driver Lockout Tables` —— **黃標項以 PDF 填色實測定位**，非目視：

```
黃色 rect 3 個（RGB (1.0, 1.0, 0.0)）：
  (61,109)-(132,123) : 'Player / RSE'
  (61,263)-(132,289) : 'Messaging'
  (61,341)-(132,354) : 'SRT Options'
```

**故該三類不取樣。** 另依 p7 註記逐字
`Embedded NAV for R1L is applicable to LATAM region only`，
**NAV 系（含 profile §2.1 所舉之 `Destination Entry`）亦不取**
—— 該項雖非黃標，但 R1L 基線未必具備。

取樣二項：`Pairing (1st time)`（Phone，top=304）／
`Reconfigurable menu bar`（Menu Bar，top=356）——
**皆落在黃色 rect 之垂直範圍外**，且非 NAV 系。

> 一個易誤之處：`SRT Options` 之黃 rect 縱向 341–354，
> 而 `Reconfigurable menu bar` 在 top=356 —— **差 2 pt**。
> 第一版比對用了 ±2 容差，把它誤判為黃標。**已收緊為嚴格區間。**

### 4.3 四則 TC

### newR1L-DD-001 —— `SWE1-RA-Driver_Distraction-009`（P0）

> 上半出處：037 Analysis Report r17 c3 (Requirement Description)；模式 `excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-001",
  "req_id": "SWE1-RA-Driver_Distraction-009",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the user attempts to access a restricted feature in the lockout table\nThen DD Service outputs RESTRICTED and HMI prevents access to the feature\n(Access attempt on \"Pairing (1st time)\" with the speed signal held at the lock threshold)",
  "pre_conditions": "1. The head unit is powered on and the Driver Distraction service is running\n2. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)\n3. The Phone screen is displayed and \"Pairing (1st time)\" is offered on it",
  "input_test_data": "$STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h = 5.0097 MPH) [ASSUMPTION A-DD6]",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h) and keep the message cycling\n2. On the Phone screen, attempt to start \"Pairing (1st time)\"\n3. Read the Phone screen and check whether the pairing flow has been entered",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h and 5.0097 MPH, the first representable step at or above the 5 MPH threshold [ASSUMPTION A-DD6]\n2. The \"Pairing (1st time)\" entry does not act as an available control and the pairing flow does not start\n3. The pairing flow is not entered and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "情境 / 用例 (Scenario / Use Case Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：速度達上鎖門檻時，Lockout Table 所列之受限 feature 其存取被阻 —— 斷言錨取 profile §2.1 觀察面 A（存取阻擋），取樣 feature 具名為 \"Pairing (1st time)\"。關鍵情境條件：$STATUS_CCAN3.VehicleSpeedVSOSig$ 由 0 送至 raw 129（8.0625 km/h＝5.0097 MPH），該值為 profile §3.1 依 R-DD7(c) 所定之上鎖側第一個可表示格，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條常態路徑（施加受限狀態 → 存取被阻），無獨立可分之部分失效（IN §8.2.2 未成立）。刻意略過：解鎖方向（raw 77／78）屬 -013／-015，門檻下側 raw 128 之不應鎖屬 BVA 之另一半，本列不擴入（IN §8.2.1）；p7 黃標三項（Player / RSE、Messaging、SRT Options）不取樣，Embedded NAV 系（含 Destination Entry）因僅適用 LATAM 亦不取。"
}
```

### newR1L-DD-002 —— `SWE1-RA-Driver_Distraction-010`（P1）

> 上半出處：037 Analysis Report r18 c3 (Requirement Description)；模式 `full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-002",
  "req_id": "SWE1-RA-Driver_Distraction-010",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Pairing (1st time)\" is retried after the timeout)",
  "pre_conditions": "1. The head unit is powered on and the Driver Distraction service is running\n2. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)\n3. The Phone screen is displayed and \"Pairing (1st time)\" can be started",
  "input_test_data": "$STATUS_CCAN3.VehicleSpeedVSOSig$ = 0 (0.0000 km/h) up to the moment the carrying message is stopped",
  "test_procedure": "1. On the Phone screen, start \"Pairing (1st time)\", confirm the pairing screen appears, then leave it and return to the Phone screen\n2. Stop transmitting the message \"STATUS_CCAN3\" that carries $STATUS_CCAN3.VehicleSpeedVSOSig$, and let the signal timeout elapse\n3. Attempt to start \"Pairing (1st time)\" again and read the Phone screen",
  "expected_result": "1. The \"Pairing (1st time)\" pairing screen is shown, and the Phone screen is displayed again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The \"Pairing (1st time)\" pairing flow does not start and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：失效形態取「匯流排逾時」而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，而本列 AC2 逐字為 `the signal simulation tool stops transmitting a vehicle message`，其驗證方法欄亦書 `After the signal timeout`，故為停送非送 SNA。步驟 1 先確認該 feature 在訊號正常時可啟動，否則步驟 3 之「不可啟動」分不出「fail-safe 生效」與「本來就不可用」（IN §5.6 基準）。刻意略過：SNA（raw 8191）之路徑本列不涵蓋 —— 037 本列未書該形態，寫入即造值。"
}
```

### newR1L-DD-003 —— `SWE1-RA-Driver_Distraction-011`（P0）

> 上半出處：037 Analysis Report r19 c3 (Requirement Description)；模式 `excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-003",
  "req_id": "SWE1-RA-Driver_Distraction-011",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the state becomes RESTRICTED while the user is using a restricted feature\nThen DD Service reports RESTRICTED and HMI displays the driver-distraction lockout notification\n(Lockout notification raised while \"Reconfigurable menu bar\" is being edited)",
  "pre_conditions": "1. The head unit is powered on and the Driver Distraction service is running\n2. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)\n3. The menu-bar configuration view for \"Reconfigurable menu bar\" can be opened",
  "input_test_data": "$STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h = 5.0097 MPH) [ASSUMPTION A-DD6]",
  "test_procedure": "1. Open the menu-bar configuration view and begin editing \"Reconfigurable menu bar\"\n2. While that view is still open, send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h) and keep the message cycling\n3. Read the screen and check the notification that is presented to the user",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input\n2. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h and 5.0097 MPH, the first representable step at or above the 5 MPH threshold [ASSUMPTION A-DD6]\n3. The Standard Lockout Popup is displayed, showing \"Feature not available while the vehicle is in motion.\"",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：受限 feature 使用中而車速跨越門檻時，HMI 呈現 lockout 通知 —— 斷言錨取 profile §2.2 觀察面 B，字串逐字取 HMI spec p4。關鍵情境條件：與 -009 之別在於**施加順序** —— 本列先進入 feature 再跨門檻，故設計方法取狀態轉換；raw 129 同 profile §3.1，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條轉換路徑，無獨立可分之部分失效。刻意略過：通知關閉後之後續行為、以及 popup 之逾時形態，037 本列未書，不擴入；取樣 feature 取 \"Reconfigurable menu bar\"（Menu Bar 列，非黃標、非 NAV 系），與同源之 -012 一致，使 -118 家族之二列可對讀。"
}
```

### newR1L-DD-004 —— `SWE1-RA-Driver_Distraction-012`（P1）

> 上半出處：037 Analysis Report r20 c3 (Requirement Description)；模式 `full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-004",
  "req_id": "SWE1-RA-Driver_Distraction-012",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Reconfigurable menu bar\" is retried after the timeout)",
  "pre_conditions": "1. The head unit is powered on and the Driver Distraction service is running\n2. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)\n3. The menu-bar configuration view for \"Reconfigurable menu bar\" can be opened",
  "input_test_data": "$STATUS_CCAN3.VehicleSpeedVSOSig$ = 0 (0.0000 km/h) up to the moment the carrying message is stopped",
  "test_procedure": "1. Open the menu-bar configuration view for \"Reconfigurable menu bar\", confirm it accepts editing input, then leave the view\n2. Stop transmitting the message \"STATUS_CCAN3\" that carries $STATUS_CCAN3.VehicleSpeedVSOSig$, and let the signal timeout elapse\n3. Attempt to open the menu-bar configuration view again and read the screen",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The menu-bar configuration view does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：訊號逾時之 fail-safe 對 -118 家族之取樣 feature 同樣使其不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：形態同 -010 取匯流排逾時，依 profile §3.2 逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書停送與 signal timeout。**本列之 037 Requirement Description 與 -010 逐字全等**（見 A-DD7），其 Then 句書 `HMI keeps the corresponding feature locked` 而非 -118 之通知面；本 TC 依原文斷言存取阻擋，**不代上游改寫為通知**（IN §8.4.2）。區別二列者為取樣 feature 與 spec_reference，非斷言內容。"
}
```

---

## 5. 逐條自檢對照（§6.2 八項）

**13 檢全綠。** 機器輸出逐字：

```
==============================================================================
T15 逐條自檢 —— 下放包 09 §6.2
==============================================================================
[PASS] §6.2-1  來源：上半 verbatim 子串 ＋ token ≤ 50
        009: 子串 ✓ / 25 token；010: 子串 ✓ / 47 token；011: 子串 ✓ / 25 token；012: 子串 ✓ / 47 token
[PASS] §6.2-1.1  同一 Requirement ID 衍生之列下半不逐字相同
        無重複
[PASS] §6.2-2  spec_reference：值正確、一行一 ObjectID、無串接
        009=CFTS022-4915108／010=CFTS022-4915108／011=CFTS022-4915109／012=CFTS022-4915109
[PASS] §6.2-3  ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked
        0 命中
[PASS] §6.2-3.1  觀察面 A 取樣具名／觀察面 B 字串逐字；無泛稱
        具名 True；泛稱命中 無
[PASS] §6.2-4  訊號寫法 profile §3；用及 §3.1 raw 者標 [ASSUMPTION A-DD6]
        raw129 於 ['009', '011']；A-DD6 標於 ['009', '011']
[PASS] §6.2-5  priority：009／011 = P0，010／012 = P1
        009=P0／010=P1／011=P0／012=P1
[PASS] §6.2-6  §8.4.2 界線：安全帶／乘客偵測／乘客確認／UF1-2／ADAS 分支 未引入
        0 命中
[PASS] §6.2-7  fail-safe 形態逐 leaf 依 037 AC2 原文（未統一指定）
        010: 037 書停送 True／書 timeout True → 用逾時 True、未用 SNA True；012: 037 書停送 True／書 timeout True → 用逾時 True、未用 SNA True
[PASS] §6.2-8  IN §10.5 步驟 ≥ 2；§6 Procedure↔ER 1:1
        步驟 {'newR1L-DD-001': 3, 'newR1L-DD-002': 3, 'newR1L-DD-003': 3, 'newR1L-DD-004': 3}／ER {'newR1L-DD-001': 3, 'newR1L-DD-002': 3, 'newR1L-DD-003': 3, 'newR1L-DD-004': 3}
[PASS] §6.2-8.1  IN §11 四欄無行尾句號；UI 標籤用雙引號非方括號
        行尾句號 無；方括號 無
[PASS] §6.2-8.2  IN §6 ER 無 modal verb
        無
[PASS] §6.2-+  R-DD9(b) 連續量寫 `= <raw> (<物理值與單位>)`
        009／011 皆合
==============================================================================
RESULT: ALL PASS  （13 檢）
```

### 5.1 §6.2 八項之逐條對照

| §6.2 | 拘束 | 檢 | 結果 |
|---|---|---|---|
| 1 | 上半 verbatim、token ≤ 50；同源下半不逐字相同 | 1、1.1 | PASS（子串 4/4；25/47/25/47 token） |
| 2 | spec_reference 一行一 ObjectID | 2 | PASS（`4915108`×2、`4915109`×2，無串接） |
| 3 | ER 錨：觀察面 A 具名／B 逐字；四詞不入 ER | 3、3.1 | PASS（四詞 0 命中；具名 4/4；泛稱 0） |
| 4 | 訊號寫法 profile §3；用及 §3.1 raw 者標 A-DD6 | 4、+ | PASS（raw129 於 009/011，marker 同集合） |
| 5 | priority 009/011=P0、010/012=P1 | 5 | PASS |
| 6 | §8.4.2 界線不得引入 | 6 | PASS（10 個禁詞 0 命中） |
| 7 | fail-safe 逐 leaf 依 037 AC2 原文 | 7 | PASS（二列皆書停送＋timeout → 用逾時、未用 SNA） |
| 8 | IN §9／§10／§11 | 8、8.1、8.2 | PASS（步驟 3、ER 3、1:1；行尾句號 0；方括號 0；modal 0） |

**第 6 項之禁詞表**（逐字，掃 `test_item` ＋ 四欄）：
`seat belt`／`seatbelt`／`passenger detection`／`Are you the passenger`／
`occupant`／`ADAS`／`Level 3`／`per-key-cycle`／`key cycle`／`Fullscreen`。

**第 7 項不是照抄下放包，是回頭查 037**：二列之 AC2 逐字含
`stops transmitting a vehicle message`，其驗證方法欄含 `After the signal timeout`
—— **故取逾時而非 SNA，是 037 說的，不是我選的**。

### 5.2 ⚠ 自檢抓到一個真缺（已修）

第一版 `-010`（`newR1L-DD-002`）之 `expected_result` **從頭到尾沒有具名取樣 feature**：

```
1. The pairing screen is shown and the Phone screen is displayed again after leaving it
3. The pairing flow does not start and the Phone screen stays as it was before the attempt
```

`"Pairing (1st time)"` 只出現在 `pre_conditions` 與 `test_procedure`。

**profile §2.1 之字面是「取樣 feature **於 TC 內**具名」—— TC 全域，非 ER 專屬。
故嚴格說第一版並未違規。** 但我把自檢寫成 ER 層級的檢，它就 FAIL 了。

**處置：修 TC，不放寬檢。** 理由：ER 是判 pass/fail 的那一欄，
**執行者只讀 ER 也要能知道在看哪個 feature**；「the pairing flow」在
ER 裡沒有先行詞。已於二處補為 `"Pairing (1st time)"`，重跑全綠。

> 自檢比規則嚴，於是抓到一個規則沒禁但確實該修的東西。**這是自檢該有的樣子。**

---

## 6. 一項本輪新登之異常 —— A-DD7

**`-010` 與 `-012` 之 20 欄中 18 欄逐字全等**，僅 leaf id 與 Source Requirement ID 相異。

| 比較對 | 相異欄數／全欄 | 相異之欄 |
|---|---|---|
| **`-010` vs `-012`** | **2 / 20** | c0 leaf id、c1 Source Req ID |
| 對照：`-009` vs `-011` | **4 / 20** | c0、c1、**c3 Description**、**c17 VC** |

**AC1 之一對隨 source 分化，AC2 之一對沒有。** 而二 source 之斷言面不同：

- `-117` → `HMI prevents access to the feature`（存取阻擋）
- `-118` → `HMI displays the driver-distraction lockout notification`（通知呈現）

`-012` 源自 `-118`，其 AC2 之 Then 句卻是
`HMI keeps the corresponding feature locked` —— **是 `-117` 的面。**

**處置：依 037 原文斷言存取阻擋，不代上游改寫為通知面**（IN §8.4.2）。
`newR1L-DD-004` 與 `newR1L-DD-002` 之區別落在**取樣 feature 與 spec_reference**，
非斷言內容 —— 這是 037 現狀之忠實反映，**不是生成之疏漏**。

**Tier 1 登記（record + propose），處置屬 Tier 2。是否另立 DR 由分析層定，執行層不代登。**

---

## 7. 未結 DR 清單

| DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|
| **DR-DD1** | DRAFTED（未發送）| `-025`~`-028`（4）| **凍結** |
| **DR-DD2** | DRAFTED（未發送）| `-021`~`-024`（4）| 不阻斷；保留 `$PARK_BRK_EGD$` |
| **DR-DD3** | ANSWERED-PENDING-CONFIRM | `-017`~`-028`（12）| 不阻斷；值 `91`，標 A-DD5 |
| **DR-DD4** | DRAFTED（未發送）| 9 列書 MPH 者 | 不阻斷；raw 邊界標 A-DD6 |
| **DR-DD5** | **DRAFTED（本輪由保留號轉正式）** | `-017`~`-024`（8）| **不入 pilot** |
| **DR-DD6** | DRAFTED（未發送；本輪改正版本號）| `-017`~`-024`（8）| **不入 pilot** |

**六筆皆未發送。** DD1／DD3 獨立；DD5／DD6 獨立。

### 阻斷疊圖

```
-001 ~ -002  (2)   無阻斷
-003 ~ -008  (6)   -003/-005/-007 帶 A-DD6
-009 ~ -012  (4)   **本輪 pilot 已生成**；-009/-011 帶 A-DD6；-010/-012 另見 A-DD7
-013 ~ -016  (4)   -013/-015 帶 A-DD6
-017 ~ -024  (8)   A-DD5 ＋ DR-DD5 ＋ DR-DD6（+DR-DD2 於 021-024）→ 不入 pilot
-025 ~ -028  (4)   A-DD1 凍結 ＋ A-DD5
```

---

## 8. 獨立自評

### 8.1 我做對的

- **T14a 停了。** 追加 11 列很容易，交出去看起來也像做完了 ——
  而它會在下次任何人跑 `rulings_hash.py` 時消失，且中間 `--check` 全紅。
  **先去找有沒有產生器**，是這一項唯一重要的動作。
- **T14b 的「含該字串但不相等」那一欄是多加的。** 下放包只問「是否唯一」，
  只比完全相等就答得出來 —— 但 `Speedometer_2` 這種東西比完全相等答不到。
- **黃標是量出來的，不是看出來的。** PDF 填色 `(1.0, 1.0, 0.0)` 抓 rect 座標，
  再與文字行之 top 比對。而且第一版容差 ±2 把 `Reconfigurable menu bar`
  誤判成黃標（差 2 pt），收緊後才對 —— **目視根本分不出這 2 pt。**
- **A-DD7 是生成過程逼出來的。** 寫 `-012` 的下半時發現無論怎麼寫都跟
  `-010` 像，回頭逐欄一比才看到 18/20 全等。**「寫不出差異」是個訊號。**

### 8.2 我做糙的

- **`-010` 的 ER 沒具名，是我寫漏的**，不是規則沒說。自檢救回來了，
  但那是第二道防線，第一道（寫的時候）沒守住。
- **§4.2 的 ±2 容差**是隨手寫的，沒想過 PDF 的列距本來就是 13 pt 左右，
  ±2 會吃掉相鄰列的邊緣。**寫比對就該先想清楚容差的物理意義。**

### 8.3 我拒絕做的

- **不追加 tsv 列**（§1）。
- **不改 `-012` 的斷言面為通知**（§6）。看起來 `-118` 應該是通知面，
  改了「更合理」—— 但 037 白紙黑字寫的是存取阻擋，**改它就是我在替上游決定需求**。
- **不自行擇 `Speedometer` 之 Atlantis High 欄二名其一**（§2.3(a)）。
  profile 已取 `STATUS_CCAN3`，我照用；但 R-DD6 v2 沒說一格多名怎麼取，
  **這個洞我報，不補。**

### 8.4 一件我原本會漏的

`CAN Mapping` 與 `Proxi & Configuration` 的**架構帶不一樣**（§2.3）。
前者 Atlantis 與 Atlantis High 分開兩帶，後者合成一帶。

我的腳本是從 r2 讀帶名的（沿 T13a 之法），所以**自動就對了** ——
但如果當初照 `Proxi & Configuration` 硬編 `P = Atlantis & Atlantis High`，
在 `CAN Mapping` 上 P 欄會被讀成「Atlantis High」而其實是「Atlantis」，
**取到的是 `STATUS_CCAN3` 而非 `BRAKE_FD_2` 那一格 —— 值還會剛好對**，
因為兩帶前綴相同。**錯的方法配對的答案**，正是 R-G19 所指的那件事。

---

## 9. 量測條件揭露（R-G8）

### 9.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| `CAN Mapping` 重複 68 組 | A 欄出現 ≥2 次之相異名數 | unique LID 名 2548（自非空列 2626 去重）|
| 佔 146 列 | 上列 68 名所涵列數 | 非空 LID 列 2626（母體 = r4–r2629）|
| tsv 收錄 0 條（本 feature）| `source` 欄為本檔之列數 | 重生全表 557 列（表頭外）|
| 圍籬條文 11 | `^```\nR-DD\d` 之命中數 | 本檔全文 |
| 148 條看不見 | display 59＋sw_update 31＋vehicle_category 30＋bed_lowering 17＋driver_distraction 11 | 15 個 `features/*/RULINGS.md` |
| 黃色 rect 3 | `non_stroking_color == (1.0, 1.0, 0.0)` 之 rect 數 | p7 全部有填色 rect 41 |
| 自檢 13 檢全綠 | PASS 之檢項數 | 本輪自檢共 13 項（§6.2 八項展開）|
| `-010` vs `-012` 相異 2 欄 | `str(a[j]) != str(b[j])` 之欄數 | 037 `Analysis Report` 全 20 欄 |

### 9.2 檔與開啟方式

| 標的 | 檔 | 開啟 |
|---|---|---|
| LID | `features/vehicle_setting/inputs/…v1_76.xlsx` | `openpyxl`, `read_only=True`, `data_only=True` |
| DBC | `…PDT27_E2A_R4_BHCAN.dbc`／`…R5_FDCAN8.dbc` | `read_text('utf-8', errors='replace')` |
| 037 | `features/driver_distraction/inputs/DD_SWE1_0807_EN.xlsx` | 唯讀 |
| HMI spec | `features/driver_distraction/inputs/Driver Lockout HMI Logic and Flow R1 SR24 1A (May 3 2021).pdf` | `pdfplumber`，唯讀 |
| profile | `docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md` | **唯讀**（拘束四）|
| 台帳 tsv | `docs/fw036/RULINGS.sha.tsv` | **唯讀**；重生輸出一律導向 scratchpad |

### 9.3 T14b 之界線

- 唯一性以 **A 欄字串完全相等**判（`str(v)`，**未 strip**）。
  若某列之 LID 名帶前後空白，會被判為不同名 —— **本輪未查該分頁是否有此現象**。
- 「含該字串但不相等」以 **substring、大小寫不敏感**查，母體同上。
- **只掃 `CAN Mapping` 一分頁**（下放包 T14b 之標的）。

### 9.4 T15 之界線

- **黃標偵測依賴 PDF 之 rect 填色**。若某列改以字元底色（`chars` 之
  `non_stroking_color`）而非 rect 標黃，**本法看不到**。
  本輪 p7 之三處皆為 rect，**但這是本頁之事實，非一般保證**。
- **黃 rect 只覆蓋「類別欄」（x 61–132）**，不覆蓋該類別下的各功能列。
  我以**垂直區間**判該類別之列是否落入 —— 即認定
  「類別標黃 = 該類別整列不適用」。**該讀法未經上游確認。**
- **`test_item` 上半之 token 計數用 `str.split()`**（空白切分），
  非任何 tokenizer。R-S4 之「token ≤ 50」若指他種計法，數字會不同。
- **037 之 Requirement Description 取 c3 欄**。該欄無表頭字面
  （037 之 r7 只有 c0 有值），**欄位歸屬係依既有各輪之一致用法**，
  本輪未另行驗證其表頭。

### 9.5 本輪未量測者

- **`-013`~`-016` 及其他 leaf** —— 非本輪範圍。
- **`generated/pilot_group3.json` 未經工作簿寫回驗證** ——
  拘束三明令不寫回；**故欄位是否為工作簿所接受，本輪無從得知**。
- **`design_method` 四值取自 `下拉選單` 分頁之 9 項清單**（實測），
  但**其與 IN §12「procedure 定稿後指派」之判準是否相符，未經第三方覆核**。
- **IN §10.1 之鍵名與本產物不同**：IN 書 `tc_title`／`specification_reference`／
  `split_flag`／`split_reason`，本產物依下放包 §6.2 之措辭與
  `features/popup/generated/pilot_01.json` 之既有形制用
  `test_item`／`spec_reference`，且未輸出 `split_flag`／`split_reason`。
  **二制並存，本輪未裁，照既有 pilot 形制辦並揭露於此。**

---

## 10. 待分析層者

| # | 事項 | 現況 |
|---|---|---|
| 1 | **`RULINGS.md` 是否改標題錨點體例**（連帶 5 feature 148 條）| T14a 停於此；tsv 之修法繫於此 |
| 2 | **`RULINGS.sha.tsv` 由誰重生** | 現行 `--check` 已 FAIL（popup 線之 3 列），非本線 |
| 3 | **一格載多名時如何取**（`Speedometer` 之 Atlantis High 欄）| R-DD6 v2 未規定；本輪依 profile 既定值 |
| 4 | **A-DD7：`-012` 之 AC2 是否應為 `-118` 之通知面** | 已登記；是否立 DR 待裁 |
| 5 | **輸出鍵名二制**（IN §10.1 vs pilot 既有形制）| 依既有形制辦並揭露 |
| 6 | pilot 4 TC 之審查 | 13 檢全綠，待分析層判 |
