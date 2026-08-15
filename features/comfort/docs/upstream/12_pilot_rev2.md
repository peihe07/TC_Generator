# 上繳包 12 — pilot rev2：四個 defect 修正 ＋ gate 覆蓋補齊

執行層 → 分析層。2026-08-15。回應下放包 `20_pilot_review.md` §7。

**結論：九項作業全部完成。lint 由 25 gate 擴為 29，全 PASS，四個新 gate
皆經注入缺陷反向驗證。** 未寫回 workbook。

**但 §2.1 之證據把 DEFECT-2 導向第二分支 —— 兩條 TC 需回報停下，見 §0 甲。**

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **-02 兩個 leaf 確為委派內容，非觸控面分支，且扣除後無餘留** —— 037 之 `-080-01` Verification Criteria 已寫 `Long press (-, +) hard button **or touchscreen control**`，**兩個操作面本就同在 -01**。我上一輪把 -02 寫成「觸控面分支」是**憑空造出 037 未作之區分**。依 20 §2.1 第二分支：`duplicate_of` 已移除，但扣除委派後無餘留 → **回報停下，TC-010／TC-012 待裁** |
| **乙** | **gate 覆蓋核對找到的洞不只 §10.5** —— §10.1（十個必要 key）與 §10.4（reasoning 2–5 句）**同樣無 gate，且兩者當時皆為實際違反**：14 條全缺 `split_flag`／`split_reason`，7 份 reasoning 全部超長。§10.6 有 gate 但我原本的 `duplicate_of` 值（`SWE1-HVAC-080-01`）**本身就違反其 digits-only 規定** |
| **丙** | **`readable` 之後設語不只出現在 TC-005** —— 20 §4 指定複查 011／012／014，實際掃描發現 **TC-007 亦有**（`The selected option is readable`）。依同一原則一併修 |

---

## 1. DEFECT-1 —— TC-004 修正 ＋ gate 覆蓋補齊

### 1.1 TC-004 已修

PC2 之 `[test-setup] The Seats tab is open and its lumbar and bolster
controls are reachable` **下放為 procedure 第 1 步**（`Open the Seats tab`），
`Read the list…` 成為第 2 步，ER 相應成為兩行。

此舉同時解決三件事：§10.5 之最少兩步、PC2 之 `reachable` 措辭含糊、
§4.4 之 step-controlled state 不得入 Pre-Condition。修正後 PC 只剩
`PC_SCREEN` 一行（第九軸），無 test-setup 類條目。

### 1.2 乙 —— §10.1／§10.4／§10.5／§10.6 逐條核對，補 **4 個** gate

| canon | 要求 | 原有 gate | 處置 |
|---|---|---|---|
| **§10.1** | 每個 TC 物件須含 **10 個 key**（含 `split_flag`／`split_reason`） | **無** | **新增 `required-keys`** |
| **§10.4** | `reasoning` **2–5 句**、繁中、四段順序 | **無** | **新增 `reasoning-sentences`**（句數；段落順序仍屬人工審閱） |
| **§10.5** | `test_procedure` **至少 2 個編號步驟** | **無** | **新增 `proc-min-steps`** |
| **§10.6** | `duplicate_of` 為 **digits-only 列號**字串 | **無** | **新增 `duplicate-of-format`** |

**四個 gate 當時皆為實際違反，非預防性補強**：

1. `required-keys` —— 14 條**全部**缺 `split_flag` 與 `split_reason`。
2. `reasoning-sentences` —— 7 份 reasoning **全部超過 5 句**（原為多段長文）。
   已全數改寫為 4–5 句，四段順序（驗證目標／關鍵情境條件／為什麼這樣切／
   刻意略過）保留。
3. `proc-min-steps` —— TC-004 一步。
4. `duplicate-of-format` —— 我原本填 `SWE1-HVAC-080-01`／`SWE1-HVAC-081-01`，
   **兩者皆非 digits-only 列號**，即使 DEFECT-2 不成立，此格式亦錯。

**20 §1.1 之診斷完全正確**：`proc-er-1to1` 只驗兩者列數相等，**單步對單步
照樣 1:1**。「25/25 PASS」為真，其涵蓋範圍不等於 §9／§10 之全集 ——
與 A-CF05（intake 報 346 實為 403）同型：輸出正常，只是少驗了一項。

### 1.3 四個新 gate 之反向驗證

注入四種缺陷後重跑：

```
[FAIL] required-keys: NR1L-ComfortHMI-004: missing §10.1 key(s) ['split_reason']
[FAIL] proc-min-steps: NR1L-ComfortHMI-004: 1 numbered step(s), §10.5 requires >= 2
[FAIL] reasoning-sentences: SWE1-HVAC-078: reasoning has 0 sentence(s), §10.4 requires 2-5
[FAIL] duplicate-of-format: SWE1-HVAC-078: duplicate_of 'SWE1-HVAC-078-01' is not
       a digits-only row number (§10.6)
[FAIL] sibling-axis: （連帶觸發，證明 §4.6 與 §10.6 之交互也被涵蓋）

24 / 29 gates PASS; 5 finding(s)   →  還原後  29 / 29 PASS; 0 finding(s)
```

**`reasoning-sentences` 之判準本身也修過一次**：首版正則要求終止符後接空白，
而中文 `。` 後直接接字 —— 該 gate 因此把七份多句 reasoning 全報成「1 句」。
**它抓對了「有問題」，卻抓錯了原因**。判準改為 `[。！？]` 直接計數 ＋
拉丁句號需後接空白，方為正確。此為「gate 會失敗」與「gate 失敗的理由正確」
是兩件事之實例。

---

## 2. DEFECT-2 ＋ §2.1 —— 證據導向第二分支

### 2.1 四個 leaf 之 Requirement Description 全文（20 §7.3 待補證據）

| leaf | Requirement Description（全文，不截斷） |
|---|---|
| `SWE1-HVAC-080-01` | `The system shall fast increase/decrease of lumbar/bolster level initiated` |
| `SWE1-HVAC-080-02` | `The system shall logic as per HMI Core Logic and Flow (requirement N0)` |
| `SWE1-HVAC-081-01` | `The system shall small increment increase/decrease of lumbar/bolster` |
| `SWE1-HVAC-081-02` | `The system shall equivalent to short press of previous 4-way rocker hard control` |

**併附其 Verification Criteria（此欄為判定關鍵）**：

| leaf | Action | Expected Result |
|---|---|---|
| `-080-01` | **Long press (-, +) hard button or touchscreen control** | Fast increase/decrease of lumbar/bols… |
| `-080-02` | **Long press (-, +) hard button or touchscreen control** | Logic as per HMI Core Logic and Flow |
| `-081-01` | Short press (-, +) button | Small increment increase/decrease of lumbar/bolster |
| `-081-02` | Short press (-, +) button | Equivalent to short press of previous 4-way rocker hard control |

### 2.2 判定：**第二分支** —— -02 為委派內容，且無餘留

**`-01` 之 Action 已同時涵蓋 hard button 與 touchscreen control。**
故我上一輪把 -02 寫成「長按觸控螢幕」**是憑空造出 037 未作之區分** ——
20 §2 指出的「兩個判斷互相否定」不只是敘述矛盾，其中「操作面不同」那一半
根本沒有 037 依據。

依 20 §2.1 第二分支處置：

- **`duplicate_of` 已移除**（兩種分支下皆須移除）✅
- **未改填 `axis="mode"`／操作面** —— 那正是被推翻的那個區分，
  填它等於把同一個錯誤換個欄位再犯一次
- `distinguishing_axis.axis` 改填 **`delegated-only`**，`delta` 記載全文證據
- **驗證目標須改為扣除委派後之餘留** —— **實測餘留為 ∅**：
  - `-080-02` 全部內容 = 「logic as per Core N0」，而 Core N0 之門檻／速率／
    加速曲線已判 out of scope（19 §4.1）→ 扣除後無任何本 feature 可觀察者
  - `-081-02` 全部內容 = 「equivalent to previous 4-way rocker」，而該等效性
    之基準由 CFTS044 擁有（19 §4.2）→ 同上
- 依 20 §2.1 末句：**「若扣除後無餘留，回報停下，屆時才是 BLOCKED 之候選」**
  → **TC-010／TC-012 回報停下，待裁**

### 2.3 現況與待裁

兩條 TC **仍存在於 JSON**（leaf 不遺失），但以 canon 自身欄位標明其未定案：

```
split_flag   : true
split_reason : 037 將本節拆為兩個 leaf，本 leaf 之區別內容純為委派至外部
               spec，於本 feature 範圍內扣除後無餘留。依 20 §2.1 回報停下，
               待裁；本 TC 之驗證目標暫同其 -01 sibling，不得視為已定案
```

**未自行決定**：未標 BLOCKED（20 §2.1：那是回報後才成為候選）、
未刪除該 leaf、未虛構區分。三個可能的處置（BLOCKED／併入 -01 之 coverage／
維持現狀並於 remarks 標記）皆屬 Tier 2。

**其餘 12 條不受影響**，可獨立進行 review。

---

## 3. DEFECT-3 / DEFECT-4 修正 ＋ 丙

### 3.1 DEFECT-3 —— TC-001 之 PC4 已刪

13.2 未以「當前顯示何 tab」為分支條件，該狀態係為使結果可觀察而設置，
非 spec trigger。刪 PC4 後，該事實只留在 procedure 第 1 步與 ER 第 1 步
（§5.6 之 baseline 建立與其 ER，合法），§4.5「資料只屬於一個欄位」回復。

**TC-002／TC-003 之 PC4 未動** —— 兩者為 13.2 第二、第三分支之區辨條件，
確為 spec trigger，20 §3 已確認標註正確。

### 3.2 DEFECT-4 ＋ 丙 —— ER 之後設語已全數移除

20 §4 之診斷精準：**規避假定之正解是改用條文自己的動詞，不是改用後設語。**

| 節 | 條文自身之動詞／名詞 | ER 主詞改為 |
|---|---|---|
| 13.3 | `reflected` | `the adjustment is (not) reflected` |
| 13.3.1 | `the selected option` | `the selected option ... is recorded` / `is the one recorded in step 1` |
| 13.4 | `fast increase/decrease` | `the lumbar/bolster increases faster than ...` |
| 13.5 | `increase` | `the lumbar/bolster is increased` / `is decreased back to ...` |
| 13.6 | `level`、`greyed out`、`error tone` | **保留 `level`** —— 本節為 ch13 唯一使用該詞者 |

**丙 —— 20 §4 指定複查 011／012／014，實測另有 TC-007 同型**
（`The selected option is readable`）。依同一原則一併修。
修正後全批 `readable` 出現次數 **0**；`level` 僅出現於 TC-013／TC-014。

---

## 4. 變動後之 11 條逐條內容

下列為 rev1 → rev2 有實際欄位變動者（TC-002／003／008 未變動，不列）。

#### NR1L-ComfortHMI-001 — SWE1-HVAC-076-01 — `13.2`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-verbatim] The lower screen is not in the stowed position (13.2) |
| L test_procedure | 1. Note which tab is currently shown on the lower screen<br>2. Press "-" on the door seat control |
| M expected_result | 1. The tab shown on the lower screen is not the Seats tab<br>2. The lower screen switches to the Seats tab |

#### NR1L-ComfortHMI-004 — SWE1-HVAC-077 — `13.2.1`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2) |
| L test_procedure | 1. Open the Seats tab<br>2. Read the list of lumbar and bolster adjustment types offered on the Seats tab |
| M expected_result | 1. The Seats tab is shown<br>2. The offered adjustment types are "Lumbar In/Out", "Lumbar Up/Down", "Back Bolster" and "Thigh Bolster" |

#### NR1L-ComfortHMI-005 — SWE1-HVAC-078-01 — `13.3`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is not currently shown, and the lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Press "+" once on the door seat control |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The popup or the tab change is shown, and the adjustment is not reflected |

#### NR1L-ComfortHMI-006 — SWE1-HVAC-078-02 — `13.3`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The first press has already triggered the popup or the tab change (13.3)<br>4. [test-setup] The lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Press "+" a second time on the door seat control |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The adjustment is reflected |

#### NR1L-ComfortHMI-007 — SWE1-HVAC-079-01 — `13.3.1`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] A lumbar/bolster adjustment type is currently the selected option (13.3.1) |
| L test_procedure | 1. Record which lumbar/bolster adjustment type is the selected option<br>2. Run a keycycle<br>3. Open the Seats tab and read the selected option |
| M expected_result | 1. The selected option shown before the keycycle is recorded<br>2. The head unit completes the keycycle<br>3. The selected option is the one recorded in step 1 |

#### NR1L-ComfortHMI-009 — SWE1-HVAC-080-01 — `13.4`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Long press "+" on the door seat control<br>3. Release "+" |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The lumbar/bolster increases faster than it does for a single short press<br>3. The lumbar/bolster stops increasing |

#### NR1L-ComfortHMI-010 — SWE1-HVAC-080-02 — `13.4`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Long press "+" on the door seat control<br>3. Release "+" |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The lumbar/bolster increases faster than it does for a single short press<br>3. The lumbar/bolster stops increasing |
| split_flag / split_reason | `True` — 037 將本節拆為兩個 leaf，本 leaf 之區別內容純為委派至外部 spec，於本 feature 範圍內扣除後無餘留。依 20 §2.1 回報停下，待裁；本 TC 之驗證目標暫同其 -01 sibling，不得視為已定案 |

#### NR1L-ComfortHMI-011 — SWE1-HVAC-081-01 — `13.5`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The popup or tab change has already been triggered, so the next press is applied (13.3)<br>4. [test-setup] The lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Short press "+" on the door seat control<br>3. Short press "-" on the door seat control |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The lumbar/bolster is increased<br>3. The lumbar/bolster is decreased back to the state recorded in step 1 |

#### NR1L-ComfortHMI-012 — SWE1-HVAC-081-02 — `13.5`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Short press "+" on the door seat control<br>3. Short press "-" on the door seat control |
| M expected_result | 1. The lumbar/bolster state shown before the adjustment is recorded<br>2. The lumbar/bolster is increased<br>3. The lumbar/bolster is decreased back to the state recorded in step 1 |
| split_flag / split_reason | `True` — 037 將本節拆為兩個 leaf，本 leaf 之區別內容純為委派至外部 spec，於本 feature 範圍內扣除後無餘留。依 20 §2.1 回報停下，待裁；本 TC 之驗證目標暫同其 -01 sibling，不得視為已定案 |

#### NR1L-ComfortHMI-013 — SWE1-HVAC-082-01 — `13.6`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| L test_procedure | 1. Press "+" repeatedly until the lumbar/bolster level stops increasing<br>2. Read how the "+" control is presented<br>3. Press "-" repeatedly until the lumbar/bolster level stops decreasing<br>4. Read how the "-" control is presented |
| M expected_result | 1. The lumbar/bolster reaches its maximum level and stops changing<br>2. The "+" control is greyed out<br>3. The lumbar/bolster reaches its minimum level and stops changing<br>4. The "-" control is greyed out |

#### NR1L-ComfortHMI-014 — SWE1-HVAC-082-02 — `13.6`

| 欄 | 值 |
|---|---|
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The lumbar/bolster level is already at its maximum (13.6)<br>4. [test-setup] The cabin is quiet enough for a tone to be heard |
| L test_procedure | 1. Press "+" repeatedly until the lumbar/bolster stops increasing<br>2. Press "+" once more on the door seat control |
| M expected_result | 1. The lumbar/bolster is at its maximum level<br>2. An error tone is played and the lumbar/bolster stays at its maximum level |

---

## 5. A-CF15 已登（20 §6）

**ch13 從未說明腰靠／側靠調整量顯示於何處。** 已命名之可觀察量
（`Seat Control Popup`／`Seats tab`／`selected option`／`level`／
`greyed out`／`error tone`）皆不含顯示位置。

**與 DATA_REQUESTS #14 之區別已寫入條目**：CFTS044 擁有的是級距**量值**，
本條所指是**顯示位置**，後者無任何 spec 明載、亦無指定之擁有者。
列 `DATA_REQUESTS` #15（Medium）、RD-1 候選。

**不阻塞** —— §4 之修法已使 ER 不依賴該資訊。
**R-C22 之界線照記**：若日後實機驗證顯示確無任何可讀之狀態呈現，
13.5 方回到 BLOCKED 之候選，屆時之理由才是「本 ECU 無任何可觀察端」。

---

## 6. 全批重跑 —— 僅回報變動項（20 §7.7）

### 6.1 lint

```
files: 7   TCs: 14   vocabulary: 9 strings   valid outlines: 129
29 / 29 gates PASS; 0 finding(s) across 14 TCs
```

**變動**：gate 數 25 → **29**（新增 `required-keys`、`proc-min-steps`、
`reasoning-sentences`、`duplicate-of-format`）。原 25 個維持 PASS。

### 6.2 §9 self-check —— 僅列自評改變者

| # | §9 項目 | rev1 | rev2 | 變動理由 |
|---|---|---|---|---|
| 3 | Pre-Condition 為 spec trigger、非 step-controlled state | PASS | **PASS（實際曾為 FAIL）** | rev1 之 TC-001 PC4 與 TC-004 PC2 皆為 step-controlled state，我當時自評 PASS **是錯的**。兩者已刪／下放，現為真 PASS |
| 5 | 步驟可執行、Final Step 擁有驗證 | PASS | **PASS（實際曾為 FAIL）** | TC-004 單步無 Setup，違反 §10.5。自評當時未察，現已修 |
| 10 | Procedure ↔ ER 1:1、**ER 可觀察** | PASS | **PASS（實際曾為 FAIL）** | rev1 之 5 條 ER 以 `readable` 為謂語，屬後設陳述非觀察結果。現全數改用各節自身動詞 |
| 12 | 追溯 RD、不擴張、無造範圍 | PASS | **PASS（實際曾為 FAIL）** | rev1 把 -080-02／-081-02 寫成觸控面分支，**是 037 未作之區分**，屬 §8.4.2 造範圍。現已移除該敘述 |

**其餘 13 項自評不變**（1、2、4、6、7、8、9、11、13、14、15、16、17）。

### 6.3 §9 自評本身之可靠性 —— 一句自我批評

rev1 之 §9 自評**四項報 PASS 而實際為 FAIL**，而 lint 當時 25/25 全綠。
**兩者同時錯，且錯在同一處**：我用「lint 沒抓到」當成「自評通過」的依據，
於是自評沒有獨立於 lint 提供任何保障 —— 它複述了 lint 的涵蓋範圍，
而那正是有洞的地方。

20 §8 首句「**不以 §9 自評為判定依據**」因此不是形式要求。本輪之自評已改為
逐項具名其依據（gate 名或條文位置），但**該改進無法自我驗證** ——
它仍需 review 端獨立讀 TC 內容。

---

## 7. 未做者

- **未寫回 workbook**（20 §7.8）—— `output/` 未動，`DELIVERY.sha256` 仍 2 筆。
- **未對 TC-010／TC-012 自行決定處置**（未標 BLOCKED、未刪 leaf、未虛構區分）。
- 未改 `framework.md`、profile、`RULINGS.md` 之既有條文（本包無新條文，
  20 §8 亦記無）。
- 未動 home 之任何檔案；未重跑既有 feature 之 recon（R-C8）。
- 未執行 git。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 8.1 已驗

1. 四個 leaf 之 Requirement Description 與 Verification Criteria 全文。
2. 四個新 gate 之反向驗證（注入 → FAIL → 還原 → 29/29）。
3. `readable` 全批掃描（rev1 有 5 條，含 20 §4 未指名之 TC-007；現 0 條）。
4. `level` 之出現範圍（現僅 TC-013／TC-014，即 13.6 —— ch13 唯一使用該詞之節）。
5. 四段 reasoning 順序與句數（4–5 句）。
6. TC-001 PC 由 4 行降為 3 行；TC-004 由 1 步升為 2 步。

### 8.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **TC-010／TC-012 之最終處置** | 依 20 §2.1 回報停下，屬 Tier 2 | **高** —— 兩條 TC 未定案 |
| 2 | **§10.4 之四段順序** | 新 gate 只驗句數，段落順序屬語義 | 中 —— 可加關鍵詞 gate（「驗證目標」「關鍵情境條件」…），但那是形式檢查非內容檢查，可能製造新的假綠燈 |
| 3 | **其餘 12 條是否另有 rev1 未察之 defect** | 我用同一套判斷寫成、又用同一套判斷複查 | **中** —— rev1 之四項自評誤判即此形態。**只有 review 端獨立讀能解**，我無法自證 |
| 4 | **`Seat Control Popup` 之顯示位置** | ch13 未定義（A-CF15） | 低 —— ER 已不依賴 |
| 5 | 其餘 14 組之同型問題（`readable`、缺 key、超長 reasoning） | 本批只有 Seat Control Tab | **中** —— 四個新 gate 自此對全部批次生效，但**已生成者僅本批**，故無回溯負擔 |

**第 3 項是本包最誠實的限制**：rev1 的四個 defect 全部通過了我自己的 §9
自評與 25 個 gate。rev2 補了 gate、修了 defect，但**檢查者仍是被檢查者**。
新 gate 能擋住結構性缺漏（缺 key、單步、超長、格式錯），擋不住判斷錯誤
（如把 -02 寫成觸控面分支 —— 那條在 rev1 通過所有 gate）。

### 8.3 執行層對「本包可否結案」之判斷

**12 條可送 review；2 條待裁。**

四個 defect 已修、四個 gate 已補並反向驗證、A-CF15 已登。
**TC-010／TC-012 依 20 §2.1 停下**，其處置需分析層裁示三選一：
BLOCKED／併入 -01 之 coverage／維持並於 remarks 標記。

**review 時建議優先看**：
1. §2.2 之「餘留為 ∅」判定是否成立 —— 若分析層認為尚有餘留，請指出其為何
2. 12 條之 ER 主詞是否已完全錨定各節自身動詞（§8.2 第 3 項之限制）
3. §6.2 之四項自評翻轉 —— 是否還有我未察覺的第五項
