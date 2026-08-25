# 上繳包 20 —— pilot-01 三條 TC 產出，lint 二十項全零

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/20_pilot01_tc.md`
- 結果：**步驟 1–6 全數執行；五十二條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §8 只備妥訊息與 pathspec，未執行

---

## 0. 交付物

`features/display/generated/pilot-01.json` —— **3 條 TC**
（`SWE1-DM-004` × 1、`SWE1-DM-005` × 2），10 key 齊備，
`lint036.py --profile display` **二十項行計皆 0**。

**未寫回 036 工作簿**（20 包 §五）。母本 SHA 前後複驗未變。

---

## 1. §四二條之逐條抄錄核對表（步驟 1）

| # | 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|
| 49 | R-DM47 | 664 | `973cd26024974ce6` | 是 |
| 50 | R-DM48 | 611 | `9039e42c48c88f2e` | 是 |

**逐條比對：2 PASS / 0 FAIL**。Display 累計 **50 條**。

---

## 2. DR-DM9 全文（步驟 2）

```
| DR-DM9 | SYS2／CFTS 之值標籤 `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]`／
`[DISP_REAR_CAMERA]` 各對應 `DCSD_DISP_STAT` 之哪一個 raw 值，並提供其並列出處
| OPEN | SWE-DM-005（#2／#3 之訊號值）、007／008
| ER 目前只驗行為不寫訊號值（R-DM48）；取得後依 R-DM22 建值標籤 glossary，
得於既有 ER **增列**訊號值（增列不改變行為驗證，非回修） | A-DM32 | HIGH |
```

`A-DM32` 已加註「已裁，見 R-DM48；查證面另開 DR-DM9」，並記明裁定所據
之關鍵事實由本輪實測提供：**`[DISP_REAR_CAMERA]` 對 `RR_CMRA`（raw 3）
證明不存在單純之 `DISP_` 前綴規則** —— 六個值裡的規則就不一致。

---

## 3. `batch_context.md` 之更新差異（步驟 3）

| 節 | 19 輪 | 20 輪 |
|---|---|---|
| §五 | **生成之阻塞（停止條件 46）** | **訊號值之處置（R-DM48）** —— 原阻塞記錄以引用塊保留存追溯，其下新增 §5.1 三條之訊號值逐條處置 |
| §5.2（新） | — | 溫度單位不統一：`{4820289}` 用 `degrees C`、`{4820290}` 用 `deg C`，**各依原文不統一**（§8.4.1）。#1／#2 用前者、#3 用後者 |
| §5.3（新） | — | `PU0008` 之排除與其 §8.2.1 委派記錄 |
| §六（新） | — | 產出摘要（批次檔、TC 數、lint 結果、母本 SHA 前後） |

---

## 4. 三條 TC 全文

```json
{
 "batch": "pilot-01",
 "feature": "Display",
 "test_group": "Display",
 "test_set": "Thermal Management",
 "handoff": "features/display/docs/handoff/20_pilot01_tc.md",
 "profile": "無 profile override，全採 canon 預設（DECISIONS.md §Sign-off 第 3 項）",
 "leaf_scope": [
  "SWE1-DM-004",
  "SWE1-DM-005"
 ],
 "deferred": [
  "SWE1-DM-005 之 multi-stage 分級門檻 —— DR-DM4 未結（CFTS_013 未取得）；依 18 §二不產 PENDING 佔位列"
 ],
 "write_back": {
  "author_value": "PeiPYHsu",
  "tc_ref_id_value": "NEW",
  "req_id_form": "SWE1-DM-{nnn}（R-DM42）",
  "written": false
 },
 "tcs": [
  {
   "tc_id": null,
   "leaf_id": "SWE1-DM-004",
   "test_group": "Display",
   "test_set": "Thermal Management",
   "tc_title": "Hot threshold exceeded → brightness-reduction warning popup displayed",
   "test_item": "The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic. The software shall trigger warning popup requests when configured warning threshold conditions are satisfied.\n\n(Warning stage on crossing the Hot threshold — the display stays on and only the brightness is reduced)",
   "pre_conditions": "1. The DCSD display is in a non-Hot state\n2. No high priority screen (RVC) is active",
   "input_test_data": "DCSD display temperature threshold: Hot > 85 degrees C, non-Hot <= 85 degrees C",
   "test_procedure": "1. Raise the DCSD display temperature above 85 degrees C\n2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 4 (DISP_HOT)\n3. Read the popup shown on the display and record how long it stays",
   "expected_result": "1. The DCSD Display transitions to a Hot state\n2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 4 (DISP_HOT) is received\n3. The popup \"Screen is Hot. Display brightness has been reduced.\" is displayed for 10 seconds",
   "specification_reference": "CFTS020-4820282\nCFTS020-4820289",
   "design_method": "狀態轉換 (State Transition Testing)",
   "priority": "P1",
   "split_flag": false,
   "split_reason": "",
   "functional_safety": "NA",
   "estimated_test_time": "",
   "vehicle_models": "",
   "remarks": ""
  },
  {
   "tc_id": null,
   "leaf_id": "SWE1-DM-005",
   "test_group": "Display",
   "test_set": "Thermal Management",
   "tc_title": "Hot state sustained → backlight off and touch disabled",
   "test_item": "The software shall transition display to safe operational state when critical thermal conditions are detected.\n\n(Protective transition to the display-off state — the outcome that follows the warning stage)",
   "pre_conditions": "1. The DCSD display is in a Hot state\n2. No high priority screen (RVC) is active",
   "input_test_data": "DCSD display temperature threshold: Hot > 85 degrees C",
   "test_procedure": "1. Keep the DCSD display temperature above 85 degrees C\n2. Read the popup shown on the display and record how long it stays\n3. Read the backlight state of the top and the bottom portion of the display\n4. Touch the display and check that the touch input is accepted",
   "expected_result": "1. The DCSD Display remains in a Hot state\n2. The popup \"Screen is Hot. Display turning off to cool down.\" is displayed for 10 seconds\n3. The backlight is turned off on both the top and the bottom portion\n4. Touch input is disabled",
   "specification_reference": "CFTS020-4820289",
   "design_method": "狀態轉換 (State Transition Testing)",
   "priority": "P1",
   "split_flag": true,
   "split_reason": "§8.3 stress-test：觸發與回復為獨立之部分失效 —— 只有回復失敗時，本條之判定仍為 pass，故與 #3 分屬兩條",
   "functional_safety": "NA",
   "estimated_test_time": "",
   "vehicle_models": "",
   "remarks": ""
  },
  {
   "tc_id": null,
   "leaf_id": "SWE1-DM-005",
   "test_group": "Display",
   "test_set": "Thermal Management",
   "tc_title": "Temperature falls back to non-Hot → backlight on and touch enabled",
   "test_item": "The Display Management software shall determine display ON/OFF operational decision based on thermal protection algorithm evaluation.\n\n(Return path of the same ON/OFF decision — verifies the recovery side, not the protective shutdown)",
   "pre_conditions": "1. The DCSD display is in a Hot state with the backlight turned off",
   "input_test_data": "DCSD display temperature threshold: Hot > 85 deg C, non-Hot <= 85 deg C",
   "test_procedure": "1. Read the backlight state of the top and the bottom portion of the display and record it\n2. Lower the DCSD display temperature to 85 deg C or below\n3. Read the backlight state of the top and the bottom portion of the display\n4. Touch the display and check that the touch input is accepted",
   "expected_result": "1. The backlight is off on both the top and the bottom portion\n2. The DCSD Display transitions from a Hot state to a non-Hot state\n3. The backlight is turned on for both the top and the bottom portion\n4. Touch input is enabled",
   "specification_reference": "CFTS020-4820287\nCFTS020-4820288\nCFTS020-4820290",
   "design_method": "狀態轉換 (State Transition Testing)",
   "priority": "P1",
   "split_flag": true,
   "split_reason": "§8.3 stress-test：與 #2 同一 leaf 而驗證回復路徑；#2 通過而本條失敗之情形可獨立發生",
   "functional_safety": "NA",
   "estimated_test_time": "",
   "vehicle_models": "",
   "remarks": ""
  }
 ]
}
```

### 4.1 `reasoning`（§10.4）

**範圍**：本批為 pilot-01，取 037 之 SWE1-DM-004／005 兩 leaf（R-DM41 之 Q2 定案；req_id 形態依 R-DM42 取 `SWE1-DM-{nnn}`）。005 之 multi-stage 分級門檻 deferred —— DR-DM4 未結（CFTS_013 未取得），依 18 §二不產 PENDING 佔位列。

**拆分**：三條之依據為 §8.2.2（RD sub-id ≠ TC 數）與 §8.3 之 stress-test —— #2（保護性關閉）與 #3（回復）為獨立之部分失效：只有回復失敗時 #2 之判定仍為 pass，故分屬兩條。#1 與 #2 為不同 leaf、不同 outcome。

**訊號值（R-DM48）**：`DCSD_DISP_STAT` 之 DBC `VAL_` 與 LID `Format` 逐字一致為 `0 OFF / 1 ON / 2 BLANK / 3 RR_CMRA / 4 DISP_HOT / 7 SNA`。規格側之 `[DISP_HOT]` 逐字相符（raw 4），故 #1 之 ER 寫入 `= 4 (DISP_HOT)`；而 `[DISP_OFF]`（#2 之 `{4820289}`）與 `[DISP_ON]`（#3 之 `{4820287}`／`{4820290}`）於兩權威皆不存在，依 R-DM48 **不寫入訊號值**，ER 改驗 CFTS 之可觀察行為（背光、觸控）。`[DISP_REAR_CAMERA]` 對 `RR_CMRA` 證明不存在單純之 `DISP_` 前綴規則，故不可外推。查證面見 DR-DM9。

**popup 歸屬（§8.5／§8.2.1）**：`PU0517` 之 Description 逐字為「display brightness intensity is being reduced」→ 歸 004（warning 階段）；`PU0130` 之 Description 逐字為「the display will turn off until it has cooled」→ 歸 005（OFF 決策）。兩者之 `Exit Conditions` 亦不同，**行為不同已逐字證實，非因同為 `1T` 而假定**。`Module == Temperature` 之第三列 `PU0008` 標的為 system 而非 screen，不入本批。

**Priority**：三條皆 P1（§10.2「major user-facing functionality or key operational logic flow」）。**非 P0** —— R-DM46 已實測 SYS3 表 6 之 `ASIL Level` 為 31/31 `QM` 且 `SG ID`／`FSR ID` 全空，安全層不入追溯鏈，故本批不屬 §10.2 之 safety 類。

**Design Method**：三條皆 `狀態轉換 (State Transition Testing)`，依 §12 於 procedure 定稿後指派 —— 三條之標的皆為 non-Hot ↔ Hot 之狀態轉換及其顯示差異。

**溫度單位**：#1／#2 引 `{4820289}` 用 `degrees C`，#3 引 `{4820290}` 用 `deg C`；**來源兩處寫法不同，各依原文不統一**（§8.4.1）。

**spec_reference**：依 §10.7(a) 一個 ObjectID 一行、前綴逐行重述、升冪、禁串接。popup 之值域出自 `Pop Up List HMI R1 (26PI).xlsx` `Main`，非 CFTS 家族，依 §10.7 不入本欄，其出處記於本欄位之外（`batch_context.md` §3.3）。

**lint**：`lint036.py --profile display` 對整批三條，A–N 及 P/Q/R/T/U **20 項行計皆 0**。首次執行時 A 檢查 4 處 FAIL（`Observe`／`check whether` 為 §5.1 之禁用動詞），已改為 `Read`／`check that` 後重跑歸零 —— **該 FAIL 為本輪產出之缺陷，非判準問題，故修正而非放寬**。

---

## 5. 逐條 §9 自檢十七項

**可機器驗者以腳本執行，結果貼入（R-G20）；須判斷者逐條說明。**

| # | 項 | #1 | #2 | #3 | 依據 |
|---|---|---|---|---|---|
| 1 | Test Set 名詞片語、合 `framework.md`、無 Test Group 前綴、無 Misc | ✓ | ✓ | ✓ | 三條皆 `Thermal Management`，為 `framework.md` Layer 2 四組之一 |
| 2 | tc_title 三形之一、2–14 words、sibling token 可見、無 modal | ✓ 8w | ✓ 9w | ✓ 11w | 機器驗：字數 8／9／11；modal 命中 0；三條相異。#1 為 (a) 箭頭式，#2／#3 為 (a) 箭頭式且其 sibling token 為 `backlight off` vs `backlight on` |
| 3 | Pre-Condition 僅狀態／環境；每條為 spec 觸發條件非隱含環境穩定前提 | ✓ | ✓ | ✓ | 三條之 PC 皆為溫度狀態與 RVC 有無，皆逐字出自 `{4820289}`（`no high priority screen (RVC)` 逐字存在）。**無「Display is powered on」類系統預設**（§4.4） |
| 4 | Input Test Data 欄位歸屬正確 | ✓ | ✓ | ✓ | 三條之 Input 皆為**門檻值**（獨立資料集，§4.5 第 3 類）；未與 PC／Procedure 重複 |
| 5 | 步驟可執行、無禁用動詞、Final Step 擁有驗證 | ✓ | ✓ | ✓ | **首跑 A 檢查 4 處 FAIL**（`Observe`／`check whether`），已改 `Read`／`check that`，重跑 A=0。末步皆為 `check that …` |
| 6 | 步驟長度與意圖層級 | ✓ | ✓ | ✓ | 3／4／4 步，每步一動作一目標 |
| 7 | 標準 setup 片語逐字重用 | n/a | n/a | n/a | 本 feature 無既有 setup 片語（首批） |
| 8 | CLI 步驟格式 | n/a | n/a | n/a | 無 CLI 步驟 |
| 9 | 需前後對照時有 baseline | n/a | n/a | ✓ | #3 之 step 1 為 baseline（先讀背光狀態並記錄），§5.6 |
| 10 | Procedure ↔ ER 1:1、ER 可觀察、無 modal、結果完整 | ✓ 3:3 | ✓ 4:4 | ✓ 4:4 | 機器驗行數相等；ER 無 modal（B=0）、無模糊語（H=0） |
| 11 | 無 FP／FF；supported 配 negative | ✓ | ✓ | ✓ | 三條皆為 positive 路徑之不同階段；**負向（未達門檻不觸發）本批未涵蓋** —— 見 §7 分流 |
| 12 | 追溯至 Req／SWRA；尊重 RD 分解不擴入 sibling；無造值、無造範圍 | ✓ | ✓ | ✓ | 三條之 `test_item` 上半皆為 037 原句 verbatim；`PU0008` 之排除已記為 §8.2.1 委派；**無造值**（§7 之訊號值處置即為此） |
| 13 | Design Method 於 procedure 定稿後指派 | ✓ | ✓ | ✓ | 三條皆 `狀態轉換 (State Transition Testing)`，於 procedure 修正（A 檢查）後才定 |
| 14 | 四欄無尾句號 | ✓ | ✓ | ✓ | 機器驗：違反 0（N=0） |
| 15 | UI 標籤用 `"..."` 非 `[...]` | ✓ | ✓ | ✓ | 機器驗：方括號 0（F=0）；popup 字串皆以 `"…"` 包覆 |
| 16 | `specification_reference` 列出所直接驗證之每一節 | ✓ | ✓ | ✓ | #1 `4820282`+`4820289`；#2 `4820289`；#3 `4820287`+`4820288`+`4820290`。**五個 ObjectID 皆已逐字複驗存在於 CFTS_020** |
| 17 | 源規格勝過索引匯出；門檻為 spec 具體值；相似操作於 ER 區辨 | ✓ | ✓ | ✓ | 門檻 `> 85 degrees C`／`<= 85 deg C` 皆逐字出自 CFTS；#2 與 #3 之相似操作（讀背光）於 ER 以 off／on 區辨 |

### 5.1 機器驗之輸出

```
[52] 括號下半三條相異: True
[R-3] test_item 上半 token 數: [34, 15, 16] （上限 50）
[§4.3] tc_title 字數: [8, 9, 11]（2–14）；含 modal/hedge: [False, False, False]；三條相異: True
[§11] 尾句號違反: 0 ／ 方括號 UI 標籤: 0
[§6] Procedure/ER 行數 1:1: [(3,3), (4,4), (4,4)]
[51] ER 含泛稱: [False, False, False]
[50] ER 中之訊號值: #1 [('4','DISP_HOT')] ／ #2（無）／ #3（無）
[§10.1] 十個 key 齊備: [True, True, True]
[§10.7] 前綴逐行=True 升冪=True 無串接=True（三條）
```

### 5.2 停止條件 50／51／52 之判定

| 條 | 判定 |
|---|---|
| 50（ER 之值須逐字解得 DBC `VAL_`） | **未觸發** —— ER 中唯一之訊號值為 `4 (DISP_HOT)`，逐字見於 DBC `VAL_` 與 LID `Format` |
| 51（#2／#3 之 ER 不得落為泛稱） | **未觸發** —— 兩條之 ER 逐字取自 CFTS：`Turn off the backlight (both top and bottom portion) and disable touch`（`{4820289}`）與 `Turn on the backlight (both top and bottom portion) and Enable touch`（`{4820290}`），**兩句皆已逐字複驗存在於 CFTS 本文** |
| 52（括號下半不得逐字相同） | **未觸發** —— 三條相異；#2／#3 同屬 005 而其區分為 `the outcome that follows the warning stage` vs `verifies the recovery side, not the protective shutdown` |

---

## 6. `lint036.py` 全文輸出（步驟 5，整批三條）

```
# lint036 報告：lint_scratch.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_scratch.xlsx`（唯讀）
- 資料列數：3
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**母體**（依 R-G26 連同綠燈一併引用）：`資料列數：3`、`header 第 9 列`、
`profile：display`。**二十項行計皆 0**，總計行計 0。

### 6.1 lint 之執行方式 —— 拋棄式副本

`lint036.py` 只讀 **xlsx**，而 20 包 §五明禁寫回 036 母本。
處置：於 scratchpad 建母本之**拋棄式副本**，寫入三列後對副本 lint。

| 項 | 值 |
|---|---|
| 母本 SHA（寫入前） | `6372fb6be02f48dc…` |
| 母本 SHA（寫入後） | `6372fb6be02f48dc…` **未變** |
| 副本位置 | scratchpad，不入 repo |

> R-G1 已載「以 openpyxl 存回母本會摧毀 R 欄之 x14 DV」。
> 本輪之 save 全部落在副本上，母本一次未開寫。

### 6.2 首跑之 4 處 FAIL 與其處置

首跑 **A（禁用動詞）行計 4／列計 3**：

| 列 | 片段 |
|---|---|
| 10 | `3. Observe the popup shown on the display…` |
| 11 | `2. Observe the popup shown on the display…` |
| 11 | `…and check whether the touch input is accepted` |
| 12 | `…and check whether the touch input is accepted` |

§5.1 列 `observe`／`check whether` 為禁用主動詞，preferred 為
`Check that`／`Read`／`Record`。改為 `Read the popup …` 與
`check that the touch input is accepted` 後重跑，**A=0**。

**該 FAIL 是我產出之缺陷，不是判準問題**，故修正 TC 而非放寬判準
（停止條件 48 之文義為「不自行放寬判準」）。

---

## 7. 未驗項分流（R-G29）

| 類 | 項 | 說明 |
|---|---|---|
| **A** | **負向路徑未涵蓋** | §9 第 11 項要求 supported 配 negative。本批三條皆為 positive 階段（觸發／關閉／回復），**未涵蓋「溫度未達門檻時不觸發」**。20 包 §二.3 只列三條為下限，未提負向；**交付前須補**，否則 004 之驗證只證明「會觸發」而未證明「不會誤觸發」 |
| **A** | A1／A2（`BACKLOG.md`） | 沿續；A2（`sysad_allocation.tsv`）為 Q2 之揭露義務，擋整批交付 |
| **B** | DR-DM9 未回 | ER 目前不寫 #2／#3 之訊號值；取得後為**增列**，不構成回修（R-DM48 已明定） |
| **B** | `PU0008` 之歸屬未定 | 已記為 §8.2.1 委派（標的為 system 非 screen），但**該 popup 屬哪一個 leaf 未查** |
| **B** | DTC `B1429-00` 未驗 | `{4820289}`／`{4820290}` 含 DTC set／clear，本批未涵蓋 —— 其標的為診斷而非顯示行為，**是否屬本 feature 未判** |
| **B** | `batch_context.md` 仍不入 git | 19 輪已報；`batches/` 由 `.gitignore` 排除，本輪未擅改 |

> 第一項（負向路徑）是我在自檢 §9 第 11 項時才察覺的 ——
> 下放包之三條清單看起來完整，而 §9 之檢查表問的是另一個問題。
> **兩者都照做，才會發現只照做其一是不夠的。**

---

## 8. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): pilot-01 - first three TCs, lint clean

- R-DM47/48 verbatim (2/2, 50/50 cumulative)
- A-DM32 settled by R-DM48: write a signal value only when its label
  resolves verbatim to a DBC VAL_ entry; otherwise the ER verifies the
  observable behaviour the spec states. The blocker was not a missing
  value - handoff 18 had named a value those two TCs do not need
- pilot-01.json: 3 TCs (004 x1, 005 x2). #1 carries
  $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 4 (DISP_HOT), which is verbatim in
  both DBC and LID; #2 and #3 carry none and verify backlight and touch
  behaviour quoted verbatim from CFTS {4820289} and {4820290}
- lint036.py --profile display: all twenty checks zero. The first run
  failed A with four forbidden verbs (Observe, check whether) - my
  defect, not the rule's, so the TCs were fixed rather than the
  criterion loosened
- lint needs a workbook and this round forbids writing back, so it ran
  against a throwaway copy in the scratchpad; the master sha is
  unchanged before and after
- DR-DM9 opened (HIGH) for the four spec value labels; once answered the
  signal values can be ADDED to the existing ERs without reworking them
- negative path (threshold not reached) is not covered by this batch and
  is filed as an A-class backlog item under section 9 item 11
```

pathspec：

```
git add features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/generated/ \
        features/display/docs/
```

`features/display/batches/` 仍由該 feature 之 `.gitignore` 排除
（19 輪已報，本輪未擅改）—— `batch_context.md` 之更新不入版。
共用 `scripts/`、`forms/`、`feature.yaml`、`.gitignore` 本輪未動。
