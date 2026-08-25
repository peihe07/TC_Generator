# 上繳包 05 —— `[VALUE]` 定案、PROXI 開工、LID 版本比對

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/05_proxi_and_values.md`
- 結果：**步驟 1–9 全數執行；十五條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §10 只備妥訊息與 pathspec，未執行

---

## 1. §四五條之抄錄核對表（步驟 1）

抄錄方式同前輪：機器抽取原樣寫入，未經人工轉錄；抄畢反向抽取並與原檔
逐字元 `==` 比對。

**Display 四條 → `features/display/RULINGS.md`**：

| # | 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|
| 20 | R-DM18 | 855 | `8db2178577562eb2` | 是 |
| 21 | R-DM19 | 681 | `0939e0a7878cbc2e` | 是 |
| 22 | R-DM20 | 576 | `6caf121fb4de2e7f` | 是 |
| 23 | R-DM21 | 270 | `d384fa5b99e34cf7` | 是 |

**全域一條 → `docs/fw036/RULINGS_LEDGER.md`**：

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G15 | 561 | `9b4512a26c55e0e9` | 是 |

**5/5 逐字元相符**；Display 累計 **23/23**（01 包 8、02 包 5、03 包 4、
04 包 2、05 包 4）。R-DM16 依 R-TM13 原文保留、未刪除，並於核對表下方
新增「廢止與取代之對照」表逐項記其被 R-DM18 取代。

> 驗證時發現我自己的核對式有瑕疵：`R-DM\d+（` 這個式子匹配不到
> `R-DM2′`（編號後接 `′` 而非全形括號），一度報出 22 vs 23。
> 已改以各包原本之抽取方式重驗，**23/23 相符**。錯的是驗證式，不是檔案。

---

## 2. 59 vs 44 之調和（步驟 2）

**兩次擷取都是 59。差異不在擷取，在聚合。**

| 量法 | 相異 token |
|---|---|
| RAW（未正規化）`\[([^\]]+)\]` | **59** |
| NORM（空白正規化後）同 regex | **59** |
| 差集（只在其中一邊出現者） | **空** |
| 含 `_x000D_` 之 token | **0** |

換行、`_x000D_`、儲存格合併**皆非成因**（逐項排除，見上表）。

真正的成因：上繳 04 之 `coverage_map.py` 把每列的 token **以逗號串成字串**
寫入 TSV 之 `values` 欄，統計時再 `split(",")` 切回去。而 token 本身可以
含逗號 —— `[Radio:R1M, VP5R120, R1H]`、`[EE Architecture:Atlantis Mid,
PowerNet]` 等 —— 切碎後與其他片段去重，才塌成 44。上繳 04 §0.2 所列之
`' Atlantis High'`、`' R1H'` 等**前導空白的碎片**就是切壞的殘骸，
我當時把它們當成「多出來的 metadata token」照單報出。

**調和後之數字：59。** 分隔符已改為 ` ¦ `（資料中不出現之字元），
`values`／`signals`／`documents` 三欄一律改用之。

> 這是第三次同型錯誤：不是量錯，是**量完之後那一步**錯。
> 上繳 04 §5.3 是 DBC 選錯、本次是分隔符切錯，兩者都通過了「看起來合理」
> 這一關。

---

## 3. `[VALUE]` 重出（步驟 3）與 A-DM11 數字更正

依 R-DM18：寬式擷取後扣除 token 中含 `:` 者。

```
  [VALUE] 擷取（R-DM18）——
    寬式 \[([^\]]+)\] 相異        : 59
    其中含 ':'（Polarion metadata）: 43
    不含 ':'                      : 16
      -> 值 token (kind=value)    : 13
             出現次數     列數  token
               20     19  0% Intensity
               15     13  DISP_OFF
               12     12  DISP_NORMAL
                8      8  current non-zero value
                5      5  DISP_REAR_CAMERA
                4      3  DISP_HOT
                4      4  pressed
                1      1  DISP_ON
                1      1  Idle
                1      1  OFF
                1      1  ON_BLANK
                1      1  RR_CMRA
                1      1  SNA
      -> 文件／協定名 (kind=document): 3
                1      1  DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts
                1      1  DCSD_and_HU_LVDS_Backchannel_Protocol
                1      1  SD.xxxxx DCSD LVDS VIDEO COMMUNICATION INTERFACE
    至少含一個不含 ':' token 之 FR 列: 35
  values_narrow_REPEALED 欄：R-DM16 之定義，已由 R-DM18 廢止，保留供稽核（R-TM13），不得作為值域來源
```

與下放包 §2.2 之對照：**59／43／16／35 四項逐項相符**；16 個 token 之
**出現次數**（20/15/12/8/5/4/4/1×6）亦與條文所列逐項相符。

> **計數口徑須並列**：條文列的是「出現次數」，而 TSV 每列去重後累計得到的
> 是「列數」，兩者不同（如 `0% Intensity` 出現 20 次但分布於 19 列，
> `DISP_OFF` 15 次／13 列）。腳本現已兩欄並印。

`kind=document` 三者依 R-DM18 另標，不計入值域，改置於獨立之 `documents`
欄：`DCSD_and_HU_LVDS_Backchannel_Protocol`、
`DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts`、
`SD.xxxxx DCSD LVDS VIDEO COMMUNICATION INTERFACE`。

`values_narrow_REPEALED` 欄依 R-TM13 保留供稽核，欄名已帶 `_REPEALED`
以免被誤用（R-DM12 之精神：欄名會活得比正文久）。

**A-DM11 之更正**：原記「含 `[value]` 34 列」→ 現為 **33 列**
（R-DM18 扣除後）；「相異 44」→ **59／43／16／13＋3** 之分解。
`candidate_leaf` 與 `anchor_kind` 之分布不受影響（值錨在優先序中排第二，
其上位之 signal 錨已覆蓋 43 列）：候選仍為 `SWE-DM-004`／`005` 各 4 列
（r31–r34），76 列無候選。

---

## 4. `feature.yaml` 之 `reference:` 節（步驟 4，R-G15）

```yaml
# R-G15（2026-08-24，全域）：參考資料庫之版本綁定。逐項記檔名與 SHA256，
# 使跨 feature 之版本差異可見 —— vehicle_setting 用 LID v1_76、display 用
# v1_78，在本節出現前沒有任何條文在追這件事。
# 選定依據見 R-DM19（B-CAN = BHCAN2，Pei 2026-08-24 指示並親自置檔）。
# 檔案本身不入 git（R-G12）；台帳見 forms/FORMS.md。
reference:
  dbc_b:
    file: "forms/PDT27_E2A_R1_BHCAN2.dbc"
    sha256: "46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60"
  dbc_fd:
    file: "forms/PDT27_E2A_R1_FDCAN8.dbc"
    sha256: "2a86c4bf3e670d71b362d430b446d8d157c74b94429e833362f81f4a48f6a22e"
  lid:
    file: "forms/Logical Identifiers and CAN Mapping v1_78.xlsx"
    sha256: "a01e1679c706cd454daf82573a732fe5ad5eedb3865083897cb18c970b312433"
  proxi:
    file: "forms/PROXI_HDCC27_R3_20250424.xlsx"
    sha256: "e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2"
```

`forms/FORMS.md` 之四個條目已各加「使用中之 feature（R-G15 反向記載）」
一行。四份檔案本身仍不入 git（複驗：`git ls-files forms/` 只有
`.gitkeep`／`FORMS.md`／`LOOKUP_MISSES.md`）。

---

## 5. PROXI `Format` 分頁之結構實測（步驟 5）

```
# R-DM20 PROXI candidate survey
PROXI `Format`: 1060 列 × 24 欄；r1 標題、r2 欄名、資料自 r3 起
  欄名: ['Parameter Group', 'Start Byte', 'Stop Byte', 'Start Bit', 'Stop Bit', 'Parameter Name', 'Annotation', 'Coding', 'Table', 'Offset', 'Resolution', 'Unit', 'Min', 'Max', 'Used by NODE(VFXXX)', 'Checked by NODE(CHECK)', 'Sales Code', 'Pattern Code', 'Comments', 'Rule Reason', 'Rule Comments', 'Main Responsible', 'Co Responsible', 'Notes']
  `Parameter Name` 非空之資料列: 1058；相異參數名 1052
  `Atlantis & Atlantis High` 欄組起於 c16；其 r3 欄名 ['Signal Name', 'CAN', 'Format']

LID `Proxi & Configuration`: 資料列 446（r4 起）
  `Primary CFTS Usage` 非空: 68/446 —— **該欄多數為空，故其未載 CFTS020 不構成「與本 feature 無關」之證據**

## anchor_kind 分布
  leaf_phrase: 0
  cfts_usage: 1
```

- `r1` 為標題列（`PROXI STANDARD FORMAT - 29 BIT`），**`r2` 為欄名列，
  資料自 `r3` 起**
- `Parameter Name` 非空之資料列 **1,058**；相異參數名 **1,052**
  （即有 6 個重複名）
- 值域欄為 `Table`（c9），形態為 `0 = Absent 1 = Present` 之列舉字串；
  另有 `Coding`(c8)／`Offset`(c10)／`Resolution`(c11)／`Unit`(c12)／
  `Min`(c13)／`Max`(c14) 供數值型參數用
- `Used by NODE(VFXXX)`(c15) 與 `Checked by NODE(CHECK)`(c16) 載其使用者

---

## 6. `proxi_candidates.tsv` 與其錨種類分布（步驟 5）

```
## anchor_kind 分布
  leaf_phrase: 0
  cfts_usage: 1
  proxi_param: 176
  none: 269
  合計 446

  於 PROXI Format 逐字查得定義者: 177/446
  keyword 命中（僅揭露）: 23

## A-DM16 之三個起點 —— 逐字查其 PROXI 列與值域

### DCSD_cfg
  LID r51 | Function: DCSD Present
  Atlantis Signal Name: CAN node 31 (DCSD) | 命中之查詢鍵: Atlantis Signal Name=CAN node 31 (DCSD)
  PROXI Format 列: 37
  值域: 0 = Absent 1 = Present
  anchor_kind: proxi_param
  note: 無 leaf 片語逐字命中；PROXI Format 定義於 r37（Parameter Group: （空）；查詢鍵 Atlantis Signal Name=CAN node 31 (DCSD)）

### DSP_SK_PRSNT
  LID r63 | Function: （空）
  Atlantis Signal Name: Display_OFF_SoftKey_Prsnt | 命中之查詢鍵: （無）
  PROXI Format 列: （查無）
  值域: （無）
  anchor_kind: none
  note: 無 leaf 片語逐字命中；PROXI Format `Parameter Name` 逐字查無；已試之鍵 ['Display_OFF_SoftKey_Prsnt', 'EC_AudTel2-<DSP_SK_PRSNT>', 'DSP_SK_PRSNT']

### RVC_SK_PRSNT
  LID r170 | Function: Rear Camera soft key present
  Atlantis Signal Name: Rear_View_Camera Rear_View_Camera_Soft_Button | 命中之查詢鍵: Atlantis Signal Name=Rear_View_Camera ¦ Atlantis Signal Name=Rear_View_Camera_Soft_Button
  PROXI Format 列: 401,494
  值域: 0 = Absent 1 = Present ¦ 0 = Absent 1 = Present
  anchor_kind: proxi_param
  note: 無 leaf 片語逐字命中；PROXI Format 定義於 r401,494（Parameter Group: Adas_Configuration_1；查詢鍵 Atlantis Signal Name=Rear_View_Camera ¦ Atlantis Signal Name=Rear_View_Camera_Soft_Button）

```

### 6.1 一處實作缺陷之自我更正 —— R-G13 在 PROXI 上重演

首版以 **Logical Identifier** 直接查 PROXI `Parameter Name`，得
**70/446**，且 `DCSD_cfg`／`DSP_SK_PRSNT`／`RVC_SK_PRSNT` **三個起點全部
查無**。

那是錯的，而且是上一輪剛學過的同一型錯誤：LID 之左欄是 Logical
Identifier，PROXI 側之參數名在 LID 之 `Atlantis & Atlantis High` 欄組
`Signal Name`（該欄組之 `CAN` 欄值為 `PROXI`）——
例 LID `ACN_Hardwired` → PROXI `ACN_Hardwire`。
改以該欄為查詢鍵（並保留 `Object Text`、Logical Identifier 為後備，
逐鍵記錄何者命中）後得 **177/446**。

再修兩處：多值儲存格未拆（`Rear_View_Camera` 與
`Rear_View_Camera_Soft_Button` 被 `norm()` 併成一行）、以及拆行後未做
欄內空白正規化（`CAN node 31  (DCSD)` 雙空格）。

| 查詢鍵 | 逐字查得 |
|---|---|
| 僅 Logical Identifier | 70 / 446 |
| ＋ Atlantis Signal Name（多值逐值拆分、空白正規化） | **177 / 446** |

**漏 107 列，佔 60%。** 已以 **A-DM17** 登記。

### 6.2 三個起點之結果

| LID | Atlantis Signal Name | PROXI 列 | 值域 |
|---|---|---|---|
| r51 `DCSD_cfg` | `CAN node 31 (DCSD)` | **r37** | `0 = Absent 1 = Present` |
| r170 `RVC_SK_PRSNT` | `Rear_View_Camera` ／ `Rear_View_Camera_Soft_Button` | **r401、r494** | 兩者皆 `0 = Absent 1 = Present` |
| r63 `DSP_SK_PRSNT` | `Display_OFF_SoftKey_Prsnt` | **查無** | — |

`DSP_SK_PRSNT` 為 R-G13 三要件齊備之真查無，且**涵蓋範圍明確應含**：
同分頁有 `FCW_Soft_Button`(r436)、`Rear_View_Camera_Soft_Button`(r494)、
**`Display_OFF_SoftKey`(r692)**、`Glove_Box_Soft_Button`(r803)。

**r692 只差一個 `_Prsnt` 尾綴，而我不認定它們是同一物** —— 依 §六第 14 條，
不逐字即不得猜。登記為 `LOOKUP_MISSES.md` M-3、開 **DR-DM6**、
以 **A-DM17** 記其命名不一致。

### 6.3 `related_leaf` 全部為空 —— 且這是方法的界線

`leaf_phrase` 錨在 446 列中 **0 命中**，故 `related_leaf` 欄全空。
成因與覆蓋對照中 `SWE-DM-007`／`008` 候選為 0 完全相同：037 用
`RVC`／`Display RVC Handling`，LID／PROXI 用 `Rear_View_Camera`。

**不得讀成「PROXI 與本 feature 無關」。** 逐字比對接不上而已，
且 6.2 之三個參數在語意上顯然相關。是否開放一份逐字的縮寫對照表
（`RVC` = `Rear View Camera`）作為錨，此問自上繳 03 §4.4 提出後尚未裁示，
**本輪再次受其所限**。

`cfts_usage` 僅 1 列（r95 `Head_Unit_Screen_Size`），且該欄
**378/446 為空** —— 其未載 `CFTS020` **不構成**「與本 feature 無關」之
證據（R-G13 第 (3) 要件之反面）。

**未寫入任何 TC 欄位**（R-DM20 末段）。

---

## 7. LID v1.78 vs v1.76（步驟 7）

```
# LID v1.78 vs v1.76 — Atlantis High `Signal Name` 比對
v1_78: /Users/peihe/Work_Projects/TC_Generator/forms/Logical Identifiers and CAN Mapping v1_78.xlsx
       CAN Mapping 2627 列；Atlantis High 起於 c26；資料列 2624；相異 LID 2548
v1_76: /Users/peihe/Work_Projects/TC_Generator/features/vehicle_setting/inputs/Logical Identifiers and CAN Mapping v1_76.xlsx
       CAN Mapping 2629 列；Atlantis High 起於 c26；資料列 2626；相異 LID 2548
v1_78 架構分組: ['LID Information', 'Powernet', 'CUSW', 'Atlantis', 'Compact', 'Atlantis High', 'Comments']
v1_76 架構分組: ['LID Information', 'Powernet', 'CUSW', 'Atlantis', 'Compact', 'Atlantis High', 'Comments']

## 三分（以 Logical Identifier 為鍵，Signal Name 為值）
  皆有且 Signal Name 相同 : 2546
  皆有但 Signal Name 不同 : **2**
  僅 v1_78 有             : 0
  僅 v1_76 有             : 0

## Signal Name 相異者 —— 逐筆

### CallAction
  v1_78 (r207): ['TELEMATIC_VEHICLE_SETUP.CallAction']
  v1_76 (r207): （空）
  僅 v1_78: ['TELEMATIC_VEHICLE_SETUP.CallAction']
  僅 v1_76: —

### EngineRPM
  v1_78 (r658): ['ENGINE_FD_2.EngineSpeed_W', 'ENGINE_FD_2.EngineSts_W', 'STATUS_CCAN3.EngineSts', 'STATUS_CCAN5.EngineSpeed', 'STATUS_CCAN5.EngineSpeedFailSts', 'Signals for MASAH:']
  v1_76 (r658,659,660): ['ENGINE_FD_2.EngRPM', 'ENGINE_FD_2.EngineSpeed_W', 'ENGINE_FD_2.EngineSts_W', 'STATUS_CCAN3.EngineSts', 'STATUS_CCAN5.EngineSpeed', 'STATUS_CCAN5.EngineSpeed', 'STATUS_CCAN5.EngineSpeedFailSts', 'Signals for MASAH:']
  僅 v1_78: —
  僅 v1_76: ['ENGINE_FD_2.EngRPM']

## 本 feature 之 15 個 $Signal$ 在兩版之一致性
  Back_Button: 相同
  CCDMF_RQ_DISP_INTS: 相同
  CM_TCH_STAT: 相同
  DCSD_DISP_STAT: 相同
  Enter_Button: 相同
  ICSMuteButton: 相同
  ICSPowerButton: 相同
  ICSScreenOffButton: 相同
  ICS_KNOB1_DIR: 相同
  ICS_KNOB1_VAL: 相同
  ICS_KNOB2_DIR: 相同
  ICS_KNOB2_VAL: 相同
  RQ_DISP_INTS: 相同
  TGW_DISP_STAT: 相同
  Telematic_Power: 相同

  -> 本 feature 受影響之訊號: 無

wrote /Users/peihe/Work_Projects/TC_Generator/features/display/data/lid_v178_vs_v176.tsv
```

### 7.1 停止條件 15 之判定：**未觸發**

兩個相異之 Logical Identifier 是否出現於任何 feature 之已交付 TC ——
逐字搜尋 `features/*/generated`、`features/*/batches`、`features/*/output`
與 `output/`：

| 查詢字串 | 命中 |
|---|---|
| `CallAction` | **0** |
| `EngineRPM` | **0** |
| `EngRPM` | **0** |
| `EngineSpeed` | **0** |
| `TELEMATIC_VEHICLE_SETUP` | 20+ 檔（vehicle_setting 之各 batch） |

**訊息名 `TELEMATIC_VEHICLE_SETUP` 確實被 vehicle_setting 用到，但相異的
是其下之 `CallAction` 訊號，而該訊號 0 命中。** 故條件未成立，未停手。

> 此處差一點就誤判：若只查訊息名就會報「有命中 → 停」。
> 相異之單位是**訊號**，查詢也必須以訊號為單位。

### 7.2 v1_76 未被搬動

全程以 `openpyxl` 唯讀開啟 `features/vehicle_setting/inputs/…v1_76.xlsx`，
未 `save()`、未複製、未移動（步驟 7 之拘束）。

### 7.3 結論

2,548 個 Logical Identifier 中相異僅 **2**，單側有 **0**，
本 feature 之 15 個 `$Signal$` **全部相同**。R-G15 之版本綁定仍必要 ——
本次差異小是事實，但「差異小」是量測結果，不是可以省略綁定的理由。

---

## 8. R-DM21 之複查（步驟 6）

逐處補上「解得／查得／resolved」所止之段：

| 出處 | 原文 | 補註後 |
|---|---|---|
| `scripts/signal_resolution.py` 統計節 | 「resolved=Y 24/26」「至少解得一列 14/15」 | 改為三段分列：段 1 LID **15/15**、段 2 解出 **26** 值、段 3 DBC **24/26 列、14/15 訊號**，並加一行「僅寫『解得 15/15』是段 1 之數字，不得表示 TC 可用之 CAN 名已備齊」 |
| `forms/LOOKUP_MISSES.md` 查詢範圍聲明 | 「resolved = Y 24/26」 | 新增「R-DM21：上列各數字所止之段」段落 |
| `ANOMALIES.md` A-DM10a | 「訊號側之 id 橋樑已解」 | 加註「本條之『已解』指段 1 與段 2 之橋樑已建立，不表示段 3 已全數備齊」 |
| `forms/LOOKUP_MISSES.md`（PROXI 新段） | — | 新增之 PROXI 查詢範圍聲明本身即以段別書寫（LID → Atlantis Signal Name → PROXI Format），並明記「未登記 ≠ 已查無」 |

`A-DM10b`（章節側）本輪無進展，維持 PENDING，其文字本就未用「解得」。

---

## 9. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 7 項。**

1. **PROXI 之 269 列狀態是「未追查」而非「查無」。** 本輪只追了 A-DM16
   指名的三個起點。`LOOKUP_MISSES.md` 已明記此區別，但**沒有任何條文
   在追那 269 列何時會被追**。
2. **縮寫對照表之問題已第三次受阻。** `RVC` ↔ `Rear_View_Camera` 使
   覆蓋對照（03 輪）、PROXI 對照（本輪）兩處之 `related_leaf` 皆為 0。
   自上繳 03 §4.4 提出至今未裁示，**每多一輪就多一份被這條界線截斷的
   產物**。
3. **BHCAN2 之選定已由 R-DM19 記為 [PROPOSED]，尚未簽核。** 其承載範圍
   涵蓋 `signal_resolution.tsv` 全 26 列與此後所有 TC 之訊號欄。
   在簽核前，這些產出仍掛在一個 [PROPOSED] 上。
4. **PROXI 之 `Used by NODE(VFXXX)` 欄完全未用。** 該欄可能可判定某參數
   是否適用於本專案之 VF，而我只讀了 `Table` 欄取值域。
5. **037 之 `Requirement Description` 全文仍未逐條精讀**（01、03、04
   三輪皆未清，本輪第四次）。
6. **SYS2 之 `Polarion`／`_polarion` 兩分頁仍未看**（同樣第四次）。
7. **`recon.py` 仍未跑通**（A-DM8，Q5 未裁）。本 feature 至今十支腳本
   全為自寫，**無一項經 repo 既有管線複核**。本輪三處自我更正
   （分隔符、PROXI 查詢鍵、多值拆分）全靠事後自查抓到 ——
   三次都通過了「輸出看起來合理」這一關。

另記本輪**已驗而下放包未要求**者：`[VALUE]` 之出現次數與列數兩種口徑；
PROXI `Format` 之 6 個重複參數名；`Display_OFF_SoftKey`(r692) 等四個
同類 soft-key 參數之存在（作為 R-G13 第 (3) 要件之證據）；
`TELEMATIC_VEHICLE_SETUP` 訊息名在既有交付件中之命中（用以說明
停止條件 15 為何不觸發）。

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
fix(display): settle [VALUE] extraction, open PROXI, diff LID versions

- R-DM18/19/20/21 + R-G15 verbatim (5/5, 23/23 cumulative); R-DM16 kept
  and marked repealed per R-TM13
- 59 vs 44 reconciled: extraction was always 59, the aggregation split on
  a comma that occurs inside tokens. Separator is now U+00A6
- [VALUE] per R-DM18: 59 wide -> 43 with ':' dropped -> 16, of which 13
  values and 3 document names, across 35 FR rows
- feature.yaml gains reference: (R-G15) binding all four databases by
  sha256; FORMS.md records the using feature per entry
- proxi_candidates.tsv: 446 LID rows, 176 resolved in PROXI Format,
  related_leaf empty because RVC vs Rear_View_Camera is not a verbatim tie
- A-DM17: querying PROXI by Logical Identifier finds 70/446; via the
  Atlantis signal-name column it finds 177/446
- lid_v178_vs_v176.tsv: 2 of 2548 identifiers differ, neither appears in
  any delivered TC, so the stop condition does not fire
- DR-DM6 and LOOKUP_MISSES M-3 for Display_OFF_SoftKey_Prsnt
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        forms/FORMS.md \
        forms/LOOKUP_MISSES.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/feature.yaml \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

本輪未改 `.gitignore`（04 輪已改妥）。四份參考素材仍不入 git。
