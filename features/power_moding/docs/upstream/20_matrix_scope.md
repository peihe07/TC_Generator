# 上繳包 20 —— State Matrix 之效力範圍、Off Road+ 之互補分支與 ch 10 之一處牴觸

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/20_matrix_scope.md](../handoff/20_matrix_scope.md)
- 前一包上繳：[19_broken_source.md](19_broken_source.md)
- **本包零寫回工作簿；未撰寫任何 TC**

**19 包之提交狀態**：已於 2026-08-24 經 Pei 授權並提交（`89d87f5`，19 路徑）。

---

## ⚠ 本包之三項須先看

1. **停止條件 7 依其字面觸發** —— Excel 與 outline **`10.3`（PITA6）** 之間
   有一處**字面牴觸**（§4.2）。**惟 `-008` 所引之 `10.4` 本身無牴觸**，
   batch 1 不受影響。依 R-PMH77(c) **兩面回報並繼續，不自行以目的覆蓋字面**。
2. **`-027` 之 Pre-Condition 必須含「車輛已處於 Off Road state」** ——
   否則其 ER「不喚醒」與矩陣列 16 之 `Radio Wakes Up and mutes` 直接衝突（§3）。
3. **`build_layer3_sections.py` 重跑與現值 `diff` 為 0** ——
   19 §14 第 4 項結清（§6）。

---

## 一、§六三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH76 | State Matrix 之效力範圍更正；素材效力須由內容決定 | 823 | `71bb5693d2b9d86f` | `71bb5693d2b9d86f` | ✅ |
| R-PMH77 | 停止條件須寫成可判之形式（「新的」vs「任一」） | 448 | `203077bcec41e483` | `203077bcec41e483` | ✅ |
| R-PMH78 | R-PMH71 之 must-hit 撤回並改寫為二值形式 | 538 | `9c193ffb5c31d6fc` | `9c193ffb5c31d6fc` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH73`／`R-PMH75` SHA256 皆相符。

---

## 二、`DR-PMH5` 之開立與 A-PMH18 之補記（步驟 2）

`DR-PMH5` 已登記，**未結 DR 由 0 回到 1 筆**，`OPEN`，**阻斷 ch 9 開批**。
其問題全文含 §2.1 之結構對照表、十三個逐字探針之 0 命中、
**語意層之對照結論**，以及版本落差（Excel `DCR21421`／2022-08-03 早於
PDF `DCR22412`／2023-01-24，其 Change Log 末筆為 2021-10-20 未及其自稱日期）。

**A-PMH18 之補記**（原文一字未改，補記置後）：
語意層對照亦不涵蓋 —— `HU on`／`HU off` 於 Excel 中是**情境條件**，
不是 p9 之「受控對象在該電源狀態下是否可用」；
**Excel 全簿無任何一格描述 `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`
三者之可用性**。**逐字不對應與語意不涵蓋，二者皆已驗。**

**19 §14 第 1 項之自陳自此結清** —— 其疑慮方向正確（我當時只驗了逐字），
而補驗之結論與原結論相同。

`DECISIONS.md` 記 **ch 9 不得開批**。

---

## 三、`Off Road Plus` 之矩陣對照（步驟 3）

### 3.1 Excel 列 16 之十二欄逐欄內容與其軸

**軸之讀法先更正下放包一處**：`Power Button OFF`（合併 `J3:M3`）
**不在** `Turn Off @ door opening Disabled`（合併 `F2:I2`，只到 I 欄）之下 ——
`J2:M2` **未合併**，故該組**無 `Turn Off @ door opening` 之限定**。

| 欄 | `Turn Off @ door opening` | `HU` 狀態 | `Call` | `Door` | 格內容 |
|---|---|---|---|---|---|
| c2 | Enabled | HU on | Active | Open | `-` |
| c3 | Enabled | HU on | Active | Closed | `-` |
| c4 | Enabled | HU on | Not Active | Open | `-` |
| c5 | Enabled | HU on | Not Active | Closed | `-` |
| c6 | Disabled | HU on | Active | Open | `-` |
| c7 | Disabled | HU on | Active | Closed | `-` |
| c8 | Disabled | HU on | Not Active | Open | `-` |
| c9 | Disabled | HU on | Not Active | Closed | `-` |
| c10 | **（無限定）** | **Power Button OFF** | Active | Open | `-` |
| c11 | **（無限定）** | **Power Button OFF** | Active | Closed | `-` |
| **c12** | **（無限定）** | **Power Button OFF** | **Not Active** | **Open** | **`Radio Wakes Up and rmutes`** |
| **c13** | **（無限定）** | **Power Button OFF** | **Not Active** | **Closed** | **`Radio Wakes Up and mutes`** |

**下放包記「其餘十欄（`HU on` 之各情境）皆為 `-`」須修正**：
`-` 者為十欄，**其中八欄為 `HU on`、兩欄為 `Power Button OFF × Call Active`**。

**`rmutes`（c12）為 `mutes` 之打字損壞** —— 與 c13 對稱位置之值僅差一字母。
依 **R-PMH26** 之精神只登記不開 DR；**不代為改寫**。

### 3.2 `OFF1.)`／`OFF3.)` 與該列之關係

**`OFF1.)`（outline 12.1，SYS1 逐字）**：

> `If vehicle is in Off Road state prior to pressing Off Road+ hard control
> head unit will not initiate wake up (Power Button On).`

**`OFF3.)`（outline 12.3，SYS1 逐字）**：

> `Head unit is muted when launching app from Power Off State.`

| 關係 | 判定 |
|---|---|
| `OFF1.)` ↔ 列 16 c12/c13 | **互補之兩支，不衝突** —— `OFF1.)` 之適用條件為「按壓前已在 Off Road state」→ 不喚醒；列 16 之軸（Power Button／Call／Door）**未含 Off Road state** → 喚醒並靜音。**二者為同一按鍵在兩個不同前提下之行為** |
| `OFF3.)` ↔ 列 16 c12/c13 之 `mutes` | **互相印證** —— `OFF3.)` 只說「靜音」而未言「喚醒」；**喚醒之來源在矩陣裡**。`Radio Wakes Up and mutes` 是「喚醒 ＋ 靜音」之完整敘述 |

### 3.3 **`-027` 之 Pre-Condition 是否須含「車輛已處於 Off Road state」—— 須**

**依據三項**：

1. `OFF1.)` 之條件句**逐字即為該前提**（`If vehicle is in Off Road state
   prior to pressing…`）—— 不設該前提，TC 所驗者即非 `OFF1.)` 所述之情形；
2. 矩陣列 16 對「非 Off Road state」之同一按鍵給出**相反結果**
   （`Radio Wakes Up and mutes`）；若 `-027` 之 ER 為「不喚醒」而未設該前提，
   **其斷言與規範性文件直接牴觸**（該矩陣為 `shall not be developed
   without following` 所指者）；
3. canon §8.5（Pre-Condition Scope Drift）—— 該前提是**使既有 leaf 之驗證
   正確**所必需者，非額外收窄。

**本輪只回報依據，未撰寫任何 TC。**

### 3.4 該 Excel 是否另有與 ch 12 相關之列 —— **`SRT` 以外無直接相關者**

全簿 43 非空列、362 非空格，以 `Off Road`／`SRT`／`Road+` 三個正規式掃描，
**命中僅 `r16c1` 一格**（即列 16 之列標籤本身）。

**間接相關者一項**：`r45c11`（`Mute Button Pressed` × `Power Button State ON`）
＝ `Mute becomes active if previously unmuted, unmute if previously muted`
—— 與 `OFF3.)` 之「靜音」屬同一主題，**惟其情境為 `Key On, Gear = Reverse`**，
與 ch 12 之 Off Road+ 情境不同。**不列為 ch 12 之對照材料。**

---

## 四、ch 10 之矩陣對照（步驟 4）

### 4.1 逐項對照

| outline | 規格逐字（節錄） | 矩陣之對應 | 判定 |
|---|---|---|---|
| **10.1** `PITA4` | `Screen Off and HU Power button selections shall be ignored while backup cam is being shown.` | `r44`（Screen Off Button Pressed）c6–c11＝**`Event ignored`**；`r40`（ON/OFF button pressed）c6–c11＝**`Event ignored`**，皆於 `Key On, Gear = Reverse` 區塊 | **一致**，且矩陣把「backup cam being shown」具體化為 `Gear = Reverse` |
| **10.2** `PITA5` | 第三句 `Once the backup cam is dismissed, the Power Button Off state shall be reinstated.` | `r43`（Gear changes to not-Reverse）c10（Power Button State OFF）＝**`Return to Power OFF state`** | **一致**（第三句直接印證）。第一、二句無直接對應列，**無矛盾** |
| **10.3** `PITA6` | `HVAC pop-ups **shall be** temporarily displayed during Power Button Off state.` | `r48`（HVAC Hard Control Adjustment）c10（`Gear = Reverse` × Power Button State OFF）＝**`Popup not displayed over RVC`** | **⚠ 字面牴觸** —— 見 §4.2 |
| **10.4** `PITA6.1` | `If radio is in Power Button Off state upon going from ignition in OFF position to ignition in ACC or RUN, HVAC popups shall display…` | **無對應列** —— 矩陣第三區塊皆為 `Key On`，未涵蓋 `ignition OFF → ACC/RUN` 之轉移 | **無矛盾**（batch 1 之 `-008` 引此，**不受影響**） |
| **10.5** `PITA8` | Key OFF（無 ACC）、HU power ON 時功能同 key on | `Key-off` 區塊有 `HU on` 欄軸 | **一致**（軸層面），無格級牴觸 |
| **10.6** `PITA9` | `Phone call popups **can be displayed over** Power Button Off state.` | `r41`（Incoming or Active Call）c10（Power Button State OFF）＝**`HU Powers on`**；`Key-on` 區塊 `r9`（Incoming Call）c12/c13＝**`Head Unit Power ON`** | **措詞差異，非牴觸** —— 見 §4.3 |
| **10.7** `PITA10` | SOS 與 ASSIST 可使頭端重新開機 | 無對應列 | 無矛盾 |

### 4.2 ⚠ **`10.3`（PITA6）與 `r48c10` 之字面牴觸 —— 停止條件 7 觸發**

- 規格：`HVAC pop-ups **shall be** temporarily displayed during Power Button Off state.`
  —— **全稱句，無例外**；
- 矩陣：`Key On, Gear = Reverse` × `Power Button State = OFF` 之格為
  **`Popup not displayed over RVC`**。

**二者在字面上不能同時成立**：規格說「Power Button Off 期間顯示」，
矩陣說「Power Button Off 且倒車影像顯示中 → 不顯示」。

**可能之調和**：`PITA4`／`PITA5` 已建立「倒車影像優先」之原則
（RVC 顯示中，Screen Off 與 Power button 皆被忽略；RVC 不取消 Power Button Off
狀態）。若把 `PITA6` 讀為「不含 RVC 情境之通則」，二者即為通則與例外。

**本層不裁。** 依 **R-PMH77(c)**「字面與目的分歧時，執行層據實兩面回報並繼續，
由分析層裁；**不得由執行層自行以目的覆蓋字面**」——
**同一紀律適用於此**：規格之字面與其可能之意圖分歧，本層只回報。

**停止條件 7 之兩面**：

| | 判定 |
|---|---|
| **字面**（「發現 Excel 與 outline `10.x` 有矛盾」） | **觸發** —— `10.3` |
| **其括號所示之關切**（`batch 1 之 -008 引 10.4`） | **不觸發** —— `10.4` 無對應列、無牴觸 |

**未改任何 TC。** `-008` 不受影響。

**須一併記明**：此為 **R-PMH77 之形態第四次出現** ——
停止條件寫「發現矛盾」，而其括號透露所欲攔截者是「**影響 batch 1 之**矛盾」。
R-PMH77 才剛立於本包 §六，**其所指之缺陷在同一包之停止條件裡又出現了一次**。

### 4.3 `10.6`（PITA9）之措詞差異 —— **判為非牴觸，惟據實列出**

規格說 popup「**can be displayed over** Power Button Off state」，
且「忽略該 popup 即**返回** Power Button Off state」；
矩陣說來電時 `HU Powers on`／`Head Unit Power ON`。

**判為非牴觸**：要在螢幕上顯示 popup，螢幕必須亮 ——
`HU Powers on` 與「popup displayed over Power Button Off state」
描述的是同一件事之兩個層面（矩陣講電源、規格講畫面），
且規格之「返回」與矩陣未言之後續不衝突。

**惟其為判斷而非量測**，據實列出供人讀。

### 4.4 規格未載而矩陣有載者（只列不改）

| 項 | 矩陣所載 | 規格 |
|---|---|---|
| `Turn Off @ door opening` 之開關 | `Enabled`／`Disabled` 兩組完全不同之行為（`Key-on`／`Key-off` 兩區塊共 8 欄軸） | **全文未提** |
| `Projection` 之影響 | `Plug in Projection`／`VR button long press at Projection`／`Projection call ends` 三列 | 僅 `VRLP1` 提 VR 長按，**未提 Projection** |
| `SRT or Off Road+` 之喚醒 | `Radio Wakes Up and mutes` | `OFF3.)` 只說靜音，**未說喚醒** |
| `Gear` 與 `Screen Off`／`Mute` 之交互 | 第三區塊全部（r40–r48，9 列 × 10 欄） | `PITA4`／`PITA5` 只覆蓋其中兩列之一部 |

**此四項即 R-PMH76 所稱之「其真正之效力範圍」之實測內容。**

---

## 五、`--source-must-hit` 之改寫（步驟 5，R-PMH78）

```
=== R-PMH78 —— 改寫後之 must-hit（二值，不涉門檻）===
探針（取自 `RESIDUE_VERDICT` 之 A-PMH16 一則）：['for 60 seconds up to 2.5 minutes', 'within 60 seconds the timeout', 'the radio should shut Off the popup']

範圍向（預設 `block`）：3/3 命中 → PASS
  **結論之量測可由預設重現** —— 此即 R-PMH71 所要求者。

must-hit（替身來源 = SYS1 側文字）：0/3 命中 → **攔下**
  替身之殘餘必為空集（自身對自身逐字全命中），故探針必然 0 命中。

must-hit B（替身來源 = 章 8 之 PDF 段，**殘餘非空**）：殘餘 8 句、探針 0/3 命中 → **攔下**
  **A 之替身其殘餘必為空集，故其攔下是保證而非證明** —— B 補之。

對照（`--source layout`）：3/3 命中 —— **19 包所指定之 must-hit 前提即在此為假**（R-PMH78 已撤回）。
  block 層之價值不在「查得出／查不出」，在於**使字級 diff 可行**：
    layout   章 9 段對 SYS1 `9.1` 之字級 diff：差異段 26 個
    block    章 9 段對 SYS1 `9.1` 之字級 diff：差異段 10 個

==================================================================
範圍向: True；must-hit A 被攔下: True；must-hit B（非平凡）被攔下: True
```

### 5.1 兩項實跑

| 項 | 結果 |
|---|---|
| **範圍向**（預設 `block`） | **3/3 命中 → PASS** —— 結論之量測可由預設重現，此即 R-PMH71 之本文主張 |
| **must-hit A**（替身＝SYS1 側文字） | **0/3 → 攔下** |
| **must-hit B**（替身＝章 8 之 PDF 段，**殘餘非空**） | 殘餘 8 句、**0/3 → 攔下** |

**must-hit B 為本層自加，其理由須明說**：A 之替身（SYS1 對自身）
**其殘餘必為空集**（自身對自身逐字全命中），
**故 A 之「攔下」是保證而非證明** —— 它無法區分
「探針之命中來自章 9 之內容」與「殘餘恰好非空」。
B 取章 8 之 PDF 段，殘餘 8 句**非空**而探針仍 0 命中，方為證明。

### 5.2 對照（只回報，不參與判定）

`--source layout` 之三探針 **3/3 命中** —— **19 包所指定之 must-hit 前提
即在此為假**。block 層之價值不在「查得出／查不出」，
在於**使字級 diff 可行**：章 9 段對 SYS1 `9.1` 之差異段
`layout` **26** 個 → `block` **10** 個。

**`--source-must-hit` 自此轉綠，且非因調整期望值而轉綠** ——
其所驗之命題已由「一個不成立者」換為「R-PMH71 之本文主張」。

---

## 六、`build_layer3_sections.py` 之重跑與 diff（步驟 6）

新增 `--out` 參數，使重跑之產物落於暫存檔，**不覆寫現值**。

```
leaf 48；對應到規格自身 section id 者 48/48
wrote …/l3_rebuild.tsv —— 回讀 48 列 × 8 欄，結構自檢通過

$ diff data/layer3_sections.tsv <重跑產物>
（無輸出）
```

**逐列逐字相同，0 差異。** `section_title` 之 120 字元截斷行為亦一致。
`git status -- data/layer3_sections.tsv` 無異動。

**19 §14 第 4 項結清** —— TSV 之現值與其產生程式之輸出已經比對。
**停止條件 9 未觸發。**

---

## 七、步驟 7 —— `RESIDUE_VERDICT` 之第二來源（本輪不做，已登記）

依下放包明令，**本輪不做**，於 `DECISIONS.md` 具名登記為
**已知未完成**（非疏漏、非 RESOLVED，通則 8）：

> `chapter_bidirectional.py` 之 20 條殘餘人讀結論，其中 **13 條為執行層本人所寫**，
> **既是判準之作者也是那個「人」**。其正解為分析層人讀，已排入下一輪。

並於 `chapter_bidirectional.py` 之 `LIMITS` 增兩列具名之。

---

## 八、lint 全跑輸出

**本輪未動 `generated/batch01.json`，未撰寫任何 TC。**

```
batch = batch01；TC 數 = 8；leaf 數 = 7

  R-PMH50 每 leaf 有 source_clause 且非空                       PASS
  R-PMH50 source_clause 取自 PDF（非 SYS1）                     PASS
  profile §3.1 test_item 具下半括號（硬規則）                        PASS
  profile §3.3 design_method ∈ 下拉選單 9 詞條                   PASS
  profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符  PASS
  profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）             PASS
  profile §3.6 estimated_test_time 留白                      PASS
  profile §3.8 vehicle_models 留白                           PASS
  profile §3.7 functional_safety = NA                      PASS
  R-PMH18 test_group = 'Disclaimer screen'（小寫 s）           PASS
  R-PMH36 test_set = 'Disclaimer Screen'（大寫 S）             PASS
  R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}             PASS
  test_set ∈ Layer 2 定版 8 組                                PASS
  canon §11 方括號禁止（本 feature 無 profile 例外）                  PASS
  procedure 與 ER 步數一致                                      PASS
  必填欄無空                                                    PASS
  ER 未以 NA 充當未知                                            PASS
  canon §10.5 test_procedure >= 2 步                        PASS
  canon §5.1 procedure 無禁用動詞                               PASS
  canon §5.2B/§5.5 Final Step 含驗證意圖                        PASS
  canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）      PASS
  交付欄位無 markdown 標記（**／__／`）                               PASS
  canon §11 無彎引號                                           PASS
  canon §11 UI 標籤加直雙引號                                     PASS
  canon §5.2 步驟字數（normal <=12／final <=18）                  PASS
  R-PMH53 交叉引用存在且語意相容                                      PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

30/30 PASS

⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：
    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 `COVERED` 產生，**不手寫**。
    執行：`python scripts/canon_coverage.py`
    本 lint 宣告涵蓋 10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**
    R-PMH52：lint 全綠不得作為 TC 可用之證據。

⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。
  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  本檢查只保證覆核所需之材料存在，不保證覆核已做。
```

**must-hit 兩份 fixture 仍 FAIL**：`batch01_prerework` 21/30／`batch01_r2` 29/30。

---

## 九、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| `chapter_bidirectional.py 7～12` | **六章全 PASS** |
| `chapter_bidirectional.py --partition` | **PASS** |
| **`chapter_bidirectional.py --source-must-hit`** | **PASS（改寫後）** —— 範圍向 3/3、must-hit A・B 皆攔下 |
| `check_granularity.py --self-test`／`--check-doc-sync`／`--doc-sync-must-hit` | **PASS**（分母 47） |
| `challenge_rulings.py` | **PASS** |
| `tsv_vs_pdf.py --truncation` | **PASS** |
| `marker_coverage.py --self-test`／`canon_coverage.py`／`check_state_consistency.py`／`check_write_back.py --self-test` | **PASS** |
| `bidirectional_spec_diff.py` | **拒跑（退出碼 2）** —— 已停用 |
| `build_layer3_sections.py --out` vs 現值 | **diff = 0** |

---

## 十、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 之能力矩陣仍無來源（`DR-PMH5`） |
| 2 | 判準衝突未決 | **是** —— `10.3`（PITA6）與矩陣 `r48c10` 字面牴觸（§4.2） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 步驟 4 發現 Excel 與 outline `10.x` 有矛盾 | `10.3` **字面牴觸**；`10.4`（`-008` 所引）**無牴觸** | **字面觸發／括號所示之關切不觸發**（§4.2，交裁） |
| 8 | 替身未 FAIL 或預設未 PASS | 範圍向 3/3 PASS；替身 A・B 皆 0/3 攔下 | **否** |
| 9 | 重跑使 `section_title` 改變且未具名即寫入 | **diff = 0**，且以 `--out` 產出至暫存檔，未覆寫 | **否** |

**本包觸發者：canon 1、canon 2、canon 5、本包 7（字面）。**
**本包之全部步驟已完成，未因觸發而中止** —— 觸發項皆為
「ch 9 開批」與「`10.3` 之裁定」之前置，本輪不開批、不撰 TC。

---

## 十一、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH5** | **PDF p9 之能力矩陣**之來源文件 | `OPEN`（20 包開立，R-PMH76） | **ch 9 開批** |

**合計未結 1 筆。** DR-PMH1／2／3／4 皆已於 19 包結清。

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **§4 之七項對照，其「一致／無矛盾」之判定全部是我讀出來的。**
   `10.1`／`10.2` 有格級之逐字印證（`Event ignored`／`Return to Power OFF state`），
   **那兩項站得住**；`10.5`／`10.7` 之「無矛盾」**只是「沒找到對應列」** ——
   **「無對應列」與「無矛盾」不是同一件事**，我把後者寫在判定欄裡。

2. **`10.6` 之「非牴觸」是我調和出來的，不是量測出來的。**
   §4.3 已具名其為判斷，**但它與 §4.2 之處置不一致** ——
   同樣是「規格字面 vs 矩陣格」，`10.3` 我判牴觸並上呈，`10.6` 我自行調和。
   **二者之差別只在於我覺得後者比較好解釋。這是一個我不該自己做的區分。**

3. **矩陣之 362 個非空格，我只逐格讀了與 ch 10／ch 12 相關之 9 列。**
   `Key-on`／`Key-off` 兩區塊之 `Projection`／`Door`／`Call Ended` 等列
   與 ch 7（Startup）之關係**完全未查** —— 而 batch 1 之 8 條全部出自 ch 7。
   **§4.4 說「規格未載而矩陣有載」有四項，那是我掃出來的，不是窮舉出來的。**

4. **`Radio Wakes Up and rmutes` 我判為打字損壞並依 R-PMH26 只登記。**
   **但 R-PMH26 之範圍是「上游 037 報告之檔名」**，我把它的精神外推到
   「規範性素材之格內容」。**該外推未經裁定。**

5. **`--source-must-hit` 之探針只取 A-PMH16 一則所引之三段字。**
   `RESIDUE_VERDICT` 現有 **20 條**結論，**其餘 19 條之可重現性未驗**。
   已寫入 `LIMITS`，但那只是具名，不是驗證。

6. **R-PMH77 剛立，而本包之停止條件 7 又犯同一形態（§4.2 末段）。**
   我指出了它，**但我沒有對本包其餘兩條停止條件（8、9）做同樣的檢查** ——
   8 與 9 是否也有字面／目的之落差，我沒看。

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 20 — state matrix scope corrected, Off Road+ complement branch, PITA6 conflict reported
```

**pathspec（9 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/DECISIONS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/20_matrix_scope.md \
  features/power_moding/docs/upstream/20_matrix_scope.md \
  features/power_moding/scripts/build_layer3_sections.py \
  features/power_moding/scripts/chapter_bidirectional.py
```

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json`／任何 TC | **未動、未撰寫** |
| `data/layer3_sections.tsv` | **未動** —— 重跑以 `--out` 落暫存檔，`git status` 無異動 |
| State Matrix xlsx | **只讀**（`data_only=True`，未 `save`） |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH5`（p9 之能力矩陣）之發出** | **ch 9 開批** |
| 2 | **`10.3`（PITA6）與矩陣 `r48c10` 之字面牴觸如何裁**（§4.2） | `Power Off Behavior` 組（10.3 屬之） |
| 3 | §12 第 2 項 —— `10.6` 我自行調和而 `10.3` 上呈，**該區分是否應由我做** | 否 |
| 4 | §12 第 4 項 —— R-PMH26 之精神外推至「素材格內容」是否成立（`rmutes`） | 否 |
| 5 | 20 之 commit 授權（9 路徑，見 §13） | 否 |
| 6 | 9.1 之 `source_clause` 例外是否寫入 profile（須核可，R-PMH46 已用畢） | `Power Transitions` 開批前 |
| 7 | 17 §5.4 其餘五項；Q10、`PROFILE_INTEGRATION.md` | 否 |

---

## 勘誤（21 包補記 —— **§4.1 原表一字未改**，R-PMH44）

### 勘誤 1 —— §4.1 之七項判定須依 **R-PMH79** 之三種記法重記

R-PMH79 定：對照結果只得記為 `牴觸`／`印證`／`未對照`，
**「無對應列」不得記為「無矛盾」；「不同謂詞」不得記為「非牴觸」** ——
二者皆會使讀者以為已比對而通過，而該命題實際上從未被素材檢驗過。

§4.1 原表之判定欄有四項不合該記法，重記如下（**謂詞逐項具名**）：

| outline | 原記 | **重記** | 謂詞 |
|---|---|---|---|
| **10.1** `PITA4` | 一致 | **印證** | `Screen Off／Power 鍵之輸入是否被忽略` —— 規格「shall be ignored while backup cam is being shown」／矩陣 `r40`・`r44` 之 `Gear = Reverse` 欄皆為 `Event ignored`，**同一謂詞取相同值** |
| **10.2** `PITA5` | 一致 | **印證**（第三句）＋ **未對照**（第一、二句） | 印證之謂詞：`RVC 解除後 Power Button Off 是否回復` —— 規格「shall be reinstated」／矩陣 `r43c10` = `Return to Power OFF state`。第一、二句（RVC 於 Power Button OFF 期間是否顯示、是否取消該狀態）**無對應列** |
| **10.3** `PITA6` | ⚠ 字面牴觸 | **牴觸**（不變） | `HVAC pop-up 是否顯示` —— 規格 `shall be … displayed`／矩陣 `r48c10` `not displayed over RVC`。**同一謂詞取相反值** |
| **10.4** `PITA6.1` | 無矛盾 | **未對照** | **無對應列** —— 矩陣第三區塊皆為 `Key On`，未涵蓋 `ignition OFF → ACC/RUN` 之轉移 |
| **10.5** `PITA8` | 一致（軸層面） | **未對照** | **無對應列** —— `Key-off` 區塊雖有 `HU on` 欄軸，惟無任何格斷言「功能與 key on 相同」。**「有同名之軸」不等於「有對應之敘述」** |
| **10.6** `PITA9` | 措詞差異，非牴觸 | **未對照（不同謂詞）** | 規格：`popup 是否顯示於 Power Button Off 之上`；矩陣 `r41c10`／`r9`：`head unit 電源是否開啟`。**無共同謂詞，故矩陣既未支持亦未否定該敘述** |
| **10.7** `PITA10` | 無矛盾 | **未對照** | **無對應列** —— 矩陣無 SOS／ASSIST 之列 |

**重記後之計數**：`印證` **2**（10.1、10.2 之第三句）／`牴觸` **1**（10.3）／
`未對照` **5**（10.2 之第一、二句、10.4、10.5、10.6、10.7）。

**原表之措詞使 `10.5`／`10.7` 看起來像「查過而通過」，實際上是「沒有可查者」。**
此即 20 §12 第 1、2 項之自陳，R-PMH79 已立條收之。

### 勘誤 2 —— §3.4 之 `rmutes` 處置，其依據由 R-PMH26 改為 **R-PMH81**

§3.4 記「依 **R-PMH26** 之精神只登記不開 DR」。
**R-PMH26 之適用範圍為上游 037 報告之檔名，不及於素材格內容**（20 §12 第 4 項自陳）。
**R-PMH81 已立**，其 (a)(b)(c) 三項為該處置之正式依據；
`rmutes` 之判定（對稱位置為 `mutes`、與 `OFF3.)` 印證、**不影響斷言**，
故只登記不開 DR）**結論不變，依據更換**。

**§3、§4 之原文一字未改，其 SHA256 不受本節影響。**
