# 上繳包 12 — B2 覆核執行、-008 BLOCKED 列、P6 前置兩項

執行層 → 分析層。2026-08-13。回應 `docs/handoff/12_b2_review.md` §4 之八項。

**九項作業全部完成。四項停手條件皆未觸發。**

| 停手條件 | 結果 |
|---|---|
| #1 三個以上 gate 缺負向對照 | **未觸發** —— 16 個 gate 全部具備雙對照，缺對照數 **0** |
| #2 PC 與 CFTS022 語意不符 | **未觸發** —— 十葉皆語意相符；措辭差異七項，逐項見 §5 |
| #3 spec-reference 指向不對應之條文 | **未觸發** —— 十葉對應全部成立，見 §6 |
| #4 台帳 FAILED | **未觸發** —— 兩條指令四次全綠 |

---

## 1. §4.1 —— -008 BLOCKED 列全文

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-008",
 "batch": "Speed-Controlled Volume",
 "reasoning": "**本葉排除於本交付件之驗證範圍，產出 BLOCKED 列（R34-2 / R34-3）。**依 R34-1 之兩層判準：ECU tag 含本 ECU（`ETM, AMP, RRM, LTM` 含 LTM）為必要條件成立，但充分條件不成立 —— CFTS022-4915173 之 trigger 主詞為 AMP、outcome 主詞為 AMP、條文全文不提 HU，且 HU 在該行為之訊號鏈上無可觀察之一端。四項證據同向，其中 (d) 為十片葉子中**唯一** ECU tag 含 `AMP` 者。**與 -005 之對照**：-005 之 outcome 主詞同為 AMP，但 HU 是 $VolumeSCV$ 之**發送端**，訊號鏈上有可觀察之一端，故留在本交付件（改以輸出集合封閉性驗之，R33-1）；本葉則無此一端 —— 同一判準給出不同結果。**不略去而產出 BLOCKED 列**：交付件若直接少一片葉子，追溯表會出現沒有說明的缺口；BLOCKED 列使缺口可見、可審。上游確認見 A-PV18 / RD-1 #12。",
 "keywords": [
  "AMP wakes up",
  "Interior CAN",
  "recall",
  "BLOCKED-ECU"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "none",
  "delta": ""
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-008",
   "placeholder": true,
   "tc_title": "AMP recalls the speed controlled volume state on Interior CAN wake-up — out of scope for this ECU",
   "test_group": "Privacy",
   "test_set": "Speed-Controlled Volume",
   "test_item": "When the AMP wakes up on the Interior CAN, the AMP shall recall the state of the speed controlled volume",
   "pre_conditions": "BLOCKED - see Remarks",
   "input_test_data": "BLOCKED - see Remarks",
   "test_procedure": "BLOCKED - see Remarks",
   "expected_result": "BLOCKED - see Remarks",
   "specification_reference": "CFTS022-4915173",
   "priority": "",
   "design_method": "",
   "remarks": "[BLOCKED-ECU] Out of scope for this deliverable: both the trigger and the outcome of CFTS022-4915173 are performed by the AMP; the HU has no observable behaviour in this clause. Verification belongs to the AMP ECU. Pending upstream confirmation of the leaf allocation (A-PV18 / RD-1 #12)."
  }
 ]
}
```

**Remarks 逐字照抄 R34-3**，未改一字。

**一項實作決定需分析層知悉**：BLOCKED 列會讓既有 lint gate 全面誤報 ——
`design_method` 空、`priority` 空、步驟 < 2、步驟與 ER 不對等，四項同時觸發。
**處置不是放寬既有 gate**（那會為了一列而鈍化其餘十列的檢查），
而是於 TC 加 `placeholder: true` 旗標，對該類列改用一組 **placeholder 專屬
gate**：`placeholder-body`（四個驗證欄位須恰為 `BLOCKED - see Remarks`）、
`placeholder-blank`（priority 與 design_method 須空）、
`placeholder-remarks`（Remarks 不得為空）。
旗標名與 AMFM `write_back.py` 之 `placeholder` 慣例同名同義。

---

## 2. §4.2 —— profile 之兩處落點

### 2.1 §1.1 ECU attribution（R34-1 判準條文）—— 新增節

落於 §1 之後、SYSAD context-only 條款之前。內容為兩層判準
（必要條件 = tag 含本 ECU；充分條件 = trigger 或 outcome 主詞含本 ECU，
或本 ECU 在訊號鏈上有可觀察之一端），並附**兩個先例對照表**：

| leaf | outcome 主詞 | 本 ECU 之位置 | 結果 |
|---|---|---|---|
| **-005** | AMP | HU 為 `$VolumeSCV$` 之**發送端** —— 訊號鏈上有可觀察之一端 | **留下**，改寫為輸出集合封閉性 |
| **-008** | AMP | 無 —— 條文完全不提 HU | **排除**，BLOCKED 列 |

條文末段亦寫明 -008 之 ECU tag **同時含 `AMP` 與 `LTM`**，並指出
「這正是為什麼條件 (1) 單獨不能決定」。

### 2.2 §5 marker 表（R34-3 連動）

由「本 feature 目前無 marker」改寫為表格，登記 `[BLOCKED-ECU]` 之定義、
出現位置（**Remarks 之開頭 token**）、與唯一用例（-008）。

同時寫明**這是 R10-4 之例外，且例外很窄**：Remarks 對外，一般不帶內部 id；
此 marker 在那裡是因為讀追溯表的人需要知道**為什麼**一片葉子沒有程序。
其他 marker 仍一律進 `reasoning` / `assumptions`，且新增 marker 需裁決。

---

## 3. §4.3 —— -006／-007 之 ER 收斂 diff（R34-4）

### -006

```diff
- 3. The HU has adjusted the output volume according to the speed controlled level
+ 3. The output volume has changed
- 5. The HU has adjusted the output volume according to the speed controlled level
+ 5. The output volume has changed
```

### -007

ER **未改動**（原文即止於「The volume level is the level read in step 1」，
本就未斷言任何音量與車速之關係）。

### 兩葉之 reasoning 皆新增

> ER 已收斂：不得斷言任何「音量 vs 車速」之具體關係、比例、階數或門檻
> —— 該行為曲線屬 CFTS019（本條 Note 明將 speed controlled audio behavior
> 交予該 spec，§8.4.2）。本條擁有的是**歸屬**（amp 不在時由 HU 執行調整），
> 不是行為曲線。速度激勵僅作為觸發手段；可驗證之差異是**誰在調整**，
> 不是調得對不對。

**收斂前之 -006 ER 3/5 說的是「HU 已依 speed controlled level 調整」**——
那句同時斷言了「有調整」與「依該 level 調整」，後半屬 CFTS019。
收斂後只留前半。

---

## 4. §4.4 —— lint 兩項新 gate 與 16 gate 之雙對照盤點

### 4.1 新增 gate

| gate | 內容 |
|---|---|
| `remarks-marker` | Remarks 非空時，開頭 token 須為 profile §5 marker 表內已登記者。未登記之 token 視為 finding，**不視為新詞彙** —— 生成時創設 marker 是停手事項 |
| `placeholder-*` 三項 | 見 §1 之實作決定 |

### 4.2 雙對照輸出（R34-5）

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

positive control — every gate is deliberately violated once:

  baseline TC: clean (0 findings)

  TRIGGERED      design-method
  TRIGGERED      test-group
  TRIGGERED      test-set
  TRIGGERED      priority
  TRIGGERED      spec-reference
  TRIGGERED      er-modal
  TRIGGERED      step-er-parity
  TRIGGERED      step-count
  TRIGGERED      step-actions
  TRIGGERED      precondition-banned
  TRIGGERED      trailing-period
  TRIGGERED      negative-scope
  TRIGGERED      remarks-marker
  TRIGGERED      placeholder-body
  TRIGGERED      placeholder-blank
  TRIGGERED      placeholder-remarks

all 16 gates verified reachable

negative controls — a compliant, similar input must NOT fire:

  PASS           design-method
  PASS (baseline) test-group
  PASS           test-set
  PASS           priority
  PASS           spec-reference
  PASS           er-modal
  PASS (baseline) step-er-parity
  PASS (baseline) step-count
  PASS           step-actions
  PASS           precondition-banned
  PASS           trailing-period
  PASS           negative-scope
  PASS           remarks-marker
  PASS           placeholder-body
  PASS           placeholder-blank
  PASS           placeholder-remarks

every gate has both controls
```

### 4.3 盤點結果 —— 缺負向對照者 **0**

| gate | 陽性對照 | 負向對照 | 標示 |
|---|---|---|---|
| design-method | ✓ | ✓ 另一個合法詞條 | PASS |
| test-group | ✓ | ✓ baseline | PASS |
| test-set | ✓ | ✓ 另一個合法 Set | PASS |
| priority | ✓ | ✓ `P0` | PASS |
| spec-reference | ✓ | ✓ 另一個存在之 artifact | PASS |
| **er-modal** | ✓ | ✓ **`Interior CAN` 必須不觸發** | PASS |
| step-er-parity | ✓ | ✓ baseline | PASS |
| step-count | ✓ | ✓ baseline | PASS |
| **step-actions** | ✓ | ✓ **`Read the signal and its timestamp` 必須不觸發**（R33-5）| PASS |
| precondition-banned | ✓ | ✓ 合法 PC | PASS |
| trailing-period | ✓ | ✓ 無尾點之句 | PASS |
| negative-scope | ✓ | ✓ 真的注入非法輸入者 | PASS |
| remarks-marker | ✓ | ✓ 已登記 marker | PASS |
| placeholder-body | ✓ | ✓ 合規 BLOCKED 列 | PASS |
| placeholder-blank | ✓ | ✓ 合規 BLOCKED 列 | PASS |
| placeholder-remarks | ✓ | ✓ 合規 BLOCKED 列 | PASS |

**三個 gate 之負向對照即為 baseline 本身**（`test-group` /
`step-er-parity` / `step-count`）—— 乾淨的 TC 已是「合規之相似輸入」，
另造一個不會增加鑑別力。此點於程式內標為 `PASS (baseline)` 而非隱去。

### 4.4 全批回跑

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
NOT MEASURED at this stage: column S = NA (profile §3.8), columns T–Z blank (profile §3.9) — generation emits neither; they are write-back gates

PASS — no findings
```

---

## 5. §4.5 —— R34-10(a) 全 10 葉 Pre-Condition 回溯 CFTS022（逐葉）

**結論：十葉皆語意相符，停手條件 2 未觸發。** 但發現**七項措辭來源問題**，
全部屬「PC 之措辭非取自本葉條文」而非「語意不符」，逐項如下。

| leaf | PC | 回溯結果 |
|---|---|---|
| -001 | `The A&T System is in 'SLEEP MODE'` | ✅ 條文 `exits 'SLEEP MODE'` 之前置狀態；**引號形式與條文一致** |
| -002 | `The Interior CAN is asleep` | ✅ 條文 `Each time the Interior CAN wakes up` 之前置 |
| -003 | `The HU is asleep` | ✅ 條文 `When the HU wakes up on Interior CAN` 之前置 |
| -004 | `The HU is asleep` | ✅ 條文 `When the HU wakes up` 之前置 |
| -006/-007 | `An external amplifier is present / is not present on the vehicle` | ⚠️ **措辭來源為 profile §3.2，非條文** —— 條文寫 `the amp` / `the AMP`，無 `external`、無 `on the vehicle`。語意相符 |
| -009/-010 | 同上 | ⚠️ 同上；且條文寫 `the HU has determined that the amplifier is not present`，PC 只陳述客觀組態，未涵蓋「HU 已判定」這個中間狀態 |
| -002/-003 | `set to states other than their default states` | ⚠️ **條文未提 default state** —— 此為使結果可觀察之測試設計，非條文陳述 |
| -006/-007 | `The speed controlled volume is set to a state other than [Off]` | ⚠️ **`[Off]` 之值域來自 4915170（-005 之條文），非本葉條文** —— 跨條文借用值域 |
| -006/-007 | `An audio source is playing over the cabin speakers` | ⚠️ **完全不在任何條文內** —— 純測試設定（無音訊則音量不可觀察）|
| -009/-010 | `The speed controlled volume personalization entry is displayed on the HU` | ⚠️ **措辭來自 4915167**，而該 artifact 是 framework Part VI 所列之**未分配 clause**（無 leaf）。作為前置設定合法，但需知悉其出處 |
| -001/-004/-005/-010 | `A CAN interface tool is connected …` | ⚠️ 測試環境，非規格 —— 已登 A-PV16 |
| -008 | `BLOCKED - see Remarks` | — 不適用 |

**七項皆非語意不符**，故未觸發停手條件 2。但其中兩項值得單獨裁定：

1. **`[Off]` 跨條文借用**（-006/-007）：值域定義在 -005 之條文。
   若分析層認為 PC 不得引用他條之值域，-006/-007 之 PC 2 需改為
   不指名具體值（例如「set to a state in which the speed controlled volume
   is active」）。
2. **`the HU has determined that…`**（-009/-010）：條文之觸發含「HU 已判定
   amplifier 不存在」這個中間狀態，而 PC 只設定客觀組態。
   兩者是否等同，屬規格解讀，執行層不自裁。

---

## 6. §4.6 —— R34-10(b) 全 10 葉語意對應覆核（逐葉）

**方法**：逐葉取 `specification_reference` 之 artifact，
自 CFTS022 抽出該 artifact 之條文全文，與 037 之 Requirement Title
及本 TC 之驗證目標三者對照。**不以 lint 之「id 查得」代替。**

| leaf | artifact | 037 Requirement Title | CFTS022 條文要旨 | 對應 |
|---|---|---|---|---|
| -001 | 4914955 | Input Monitoring – Resume After Sleep Mode Exit | 退出 SLEEP MODE 後 HU 監測按鍵按壓狀態 | ✅ |
| -002 | 4915158 | Personalization Display – Restore on Interior CAN Wake-Up | Interior CAN 每次喚醒時 HU 召回個人化功能之最後狀態以供顯示 | ✅ |
| -003 | 4915168 | Speed-Controlled Volume – Restore on HU Wake-Up | HU 於 Interior CAN 喚醒時召回 SCV 狀態 | ✅ |
| -004 | 4915169 | SCV Signal – Transmission on HU Wake-Up | HU 喚醒時於 `<Tsend>` 內以 `$VolumeSCV$` 送出 SCV 狀態 | ✅ |
| -005 | 4915170 | SCV Signal – Valid Value Handling | `$VolumeSCV$` 之有效值集合，其餘為無效 | ✅ |
| -006 | 4915171 | SCV – Local Adjustment Without AMP | amp 不存在時 HU 依 speed controlled level 調整輸出音量 | ✅ |
| -007 | 4915172 | SCV – No Adjustment With AMP Present | AMP 存在時 HU 不改變音量 level | ✅ |
| -008 | 4915173 | SCV – Restore on AMP Wake-Up | AMP 於 Interior CAN 喚醒時召回 SCV 狀態 | ✅ **對應成立**（爭點在 ECU 歸屬，不在對映）|
| -009 | 4915174 | SCV – Update and Store Without AMP | 無 amp + 使用者改 level → HU 改顯示、改 level、存記憶體 | ✅ |
| -010 | 4915175 | SCV – Update and Transmit With AMP Present | 有 amp + 使用者改 level → HU 改顯示、送 `$VolumeSCV$` | ✅ |

**十葉全部對應成立，停手條件 3 未觸發。**

**-008 之對應特別註記**：其 artifact 與 leaf 之語意**完全對應**
（037 標題 `Restore on AMP Wake-Up` 與條文 `the AMP shall recall` 一致）。
本葉之問題**不是對映錯誤，而是 ECU 歸屬** —— 這兩件事必須分開，
否則日後會被誤讀成「-008 的 spec_reference 也有問題」。

**與 B1-GATE-1 之關係**：那次抓到的兩筆錯（-001 指向不存在之 id、
-002 指向 splash screen 條款）皆已於 R30-1 更正並反映於此表；
本次覆核為更正後之全量複驗，兩筆現皆對應成立。

---

## 7. §4.7 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=1  FAILED=0
```

本批未寫回，未新增 DELIVERY ENTRY（R27-2）。

---

## 8. §4.8 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。第 1 項為本輪新增之未辦，且已是其第一次出現。**

### 8.1 §5 之七項措辭來源問題中，兩項需裁定而非僅登記

`[Off]` 之跨條文借用、與 `the HU has determined that…` 之中間狀態，
兩者都不是「回溯完成即可」的項目 —— 它們需要一個關於
「PC 得否引用他條之值域」與「客觀組態是否等同 HU 已判定」的裁定。
**本輪已回溯完成（R34-10(a) 之要求已滿足），但這兩項是回溯的產物，
不是回溯的遺留**。依 R34-10 之精神，它們應直接進入裁決佇列而非未辦清單。

### 8.2 profile §3.2 之三組 Pre-Condition 措辭仍未回溯

§5 已查明 `An external amplifier is present on the vehicle` 等措辭出自
**profile §3.2**，而 profile §3.2 是我在下放包 04 起草的，
**其措辭當時即未回溯 CFTS022**（上繳包 04 §6.3 已自陳）。
本輪回溯的是 TC 的 PC，**不是 profile 的 PC 詞彙表** ——
兩者是不同的東西，前者已辦，後者未辦。若要 PC 措辭完全溯源，
profile §3.2 本身需要一次修訂。

### 8.3 lint 仍不驗語意，本輪之語意覆核是一次性人工作業

§6 那張表是我逐葉讀出來的，**沒有任何機制會在下次生成時重跑它**。
R34-10(b) 把它定為 P6 硬性前置，但它現在是一次性的 ——
若 P6 之後有任何葉子的 `specification_reference` 被改動，
沒有東西會要求重做這張表。

### 8.4 `-008` 之 BLOCKED 列尚未經寫回驗證

`placeholder` 旗標、空白 priority／design_method、以及 Remarks 內的
marker 文字，都還沒有經過 `write_back` 路徑。AMFM 的 writer 對
placeholder 列有專門的檢查（priority 與 design_method 須空、
procedure／ER 須為固定字串），但 **Privacy 的寫回腳本尚未建立**（R20-5）。
BLOCKED 列在寫回時的實際行為未驗。

<!-- UPSTREAM-COVERS: 12 -->
