# 上繳包 13 — pilot rev3：BLOCKED-SPEC ＋ 系統性 ER 修正

執行層 → 分析層。2026-08-15。回應下放包 `21_blocked_spec_ruling.md` §5。

**結論：九項作業全部完成。lint 由 29 gate 擴為 31，全 PASS；
BLOCKED 豁免以具名回報行輸出，並經三種反向驗證。** 未寫回 workbook。

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **21 §2 之第五項發現，實際影響 7 條而非 2 條** —— 我 rev2 之修法把 `readable` 換成 `is recorded`，**主詞仍在觀察者身上**，只是從「可以被讀」變成「已經被讀」。全批掃描四種謂語命中 **7 條**（005/006/007/009/010/011/012），其中 5 條改寫、2 條轉 BLOCKED row |
| **乙** | **BLOCKED 之豁免我加了兩道自身的 gate** —— 只做「豁免 proc-min-steps／proc-er-1to1」會讓 BLOCKED row 變成一個**不被任何檢查覆蓋的洞**。新增 `blocked-row-empty`（BLOCKED row 之 procedure/ER 必須**空**，不是「短」）與 `blocked-remarks`（marker 須為開頭 token、且不得含內部 ruling id）|
| **丙** | **`split_flag` 已恢復其本義** —— rev2 我用它承載裁定說明，21 §1.4 指出那不是它的用途。現 010/012 之 `split_flag=False`，說明移入 Remarks |

---

## 1. R-C23／R-C24 貼入 ＋ profile §5 改寫

`RULINGS.md` 現載 **R-C1 ~ R-C24 + R-C4-1 + R-C5-1**，共 **26 條**。

profile §5 由「目前無 marker」改寫為兩節：

- **§5.1 `[BLOCKED-SPEC]`** —— 適用條件、BLOCKED row 之欄位表、
  Remarks 之外部可見限制、lint 豁免須具名，以及**與 `[BLOCKED-ECU]` 之
  三欄對照表**（成因／本 ECU 有無可觀察端／解除條件）
- **§5.2 不產生 workbook 列者** —— 16.1、18.2–18.4 四節依 R-C16 為 RD-1
  覆蓋缺口項

**三者之區別已寫成可查的表**，因為它們外觀相近而成因不同：

| | `[BLOCKED-ECU]` | `[BLOCKED-SPEC]` | R-C16 覆蓋缺口項 |
|---|---|---|---|
| 產生 workbook 列？ | ✅ BLOCKED 列 | ✅ BLOCKED 列 | ❌ **連列都不產** |
| 本 ECU 有可觀察端？ | ❌ 無 | ✅ 有 | —（037 未產出 leaf） |
| 成因 | 行為由另一 ECU 執行 | 規範內容由另一份 spec 擁有 | 037 未對該節產出需求 |

見到空 procedure 時須讀 Remarks 之 marker 方知類別 —— 此句已寫入 profile。

---

## 2. TC-010／TC-012 —— BLOCKED row

### 2.1 接受三選一皆不採

21 §1.1 之兩項排除我接受，且第二項是我原本沒想到的：

> 「維持現狀並於 remarks 標記」不可行 —— 扣除委派後餘留為 ∅，該 TC 之
> procedure 只能複製 -01。**一條會通過但不驗證其 leaf 所要求之事的 TC，
> 即 §7 之 False Pass**，且 remarks 之標記不會使它停止通過。

我 rev2 提出那個選項時，只想到「標記使人知道它未定案」，
**沒想到標記不會改變它的通過行為** —— 一條複製 sibling procedure 的 TC，
在任何實測中都會綠燈，而它綠燈這件事本身就是假訊息。

### 2.2 兩列之內容

| | `NR1L-ComfortHMI-010` | `NR1L-ComfortHMI-012` |
|---|---|---|
| req_id | `SWE1-HVAC-080-02` | `SWE1-HVAC-081-02` |
| `test_procedure` / `expected_result` | **空** | **空** |
| `specification_reference` | `…_13.4`（照常填） | `…_13.5`（照常填） |
| Remarks | `[BLOCKED-SPEC] Long-press logic is defined by HMI Core Logic and Flow requirement N0. With that delegation removed this requirement has no content left that can be verified against the Comfort HMI specification alone` | `[BLOCKED-SPEC] The equivalence to the previous 4-way rocker hard control is defined by CFTS044. With that delegation removed this requirement has no content left that can be verified against the Comfort HMI specification alone` |
| `split_flag` | `False`（恢復本義） | `False` |
| `distinguishing_axis` | `delegated-only` **已移除** | 已移除 |

`tc_title` 亦改寫，使其陳述該 leaf 真正的內容（`Long press logic follows
HMI Core Logic and Flow` / `Short press is equivalent to the previous 4-way
rocker`），不再是 rev2 那個虛構的觸控面分支。

**Remarks 為外部可見**：兩句皆為英文、具名擁有文件、無 ruling id、
無 `A-CF` 編號 —— 且此點現由 `blocked-remarks` gate 機械強制。

### 2.3 coverage

**403 leaves 分母不變；14 條 pilot 不變；無 leaf 遺失。**
兩條為 BLOCKED row，`specification_reference` 照常指向其 outline，
traceability 表上不留空洞。

---

## 3. 第五項發現 —— 我 rev2 的修法只走了一半

### 3.1 全批掃描結果

掃描四種謂語（`is recorded` / `is readable` / `is noted` / `can be read`）
於全 14 條之 `expected_result`：

| 謂語 | rev2 命中 | rev3 |
|---|---|---|
| `is recorded` | **7 條** | 0 |
| `is readable` | 0（rev2 已修） | 0 |
| `is noted` | 0 | 0 |
| `can be read` | 0 | 0 |

**命中之 7 條**：`005`、`006`、`007`、`009`、`010`、`011`、`012`。
其中 `010`／`012` 轉 BLOCKED row（ER 清空），**實際改寫 5 條**：
`005`、`006`、`007`、`009`、`011`。

### 3.2 改法

| 位置 | rev2 | rev3 |
|---|---|---|
| baseline ER（005/006/009/011） | `The lumbar/bolster state shown before the adjustment **is recorded**` | `The lumbar/bolster state before the adjustment **is shown**` |
| baseline ER（007） | `The selected option shown before the keycycle **is recorded**` | `The selected option before the keycycle **is shown**` |
| 回復比對（011 步驟 3） | `…back to the state **recorded in** step 1` | `…back to the state **shown in** step 1` |
| 回復比對（007 步驟 3） | `The selected option is the one **recorded in** step 1` | `…is the one **shown in** step 1` |

後兩列不在 21 §2 之四種謂語清單內（它們是名詞片語不是謂語），
但**屬同一形態** —— 主詞仍是觀察者的動作。一併改。

### 3.3 這個錯誤為什麼會重複一次

rev1 是 `is readable`（可以被讀），rev2 是 `is recorded`（已經被讀），
**兩者都把主詞放在觀察者身上**。我 rev2 改的時候，以為問題是「readable
這個字」，**實際問題是「ER 的主詞是誰」** —— 換字沒有換主詞，所以錯誤原樣
搬了家。

21 §2 的措辭把這件事講清楚了：「§5.6 明定記錄步驟 describes **what is
read**」—— 讀到什麼，不是讀了沒有。這是判準，不是用詞禁令；用詞禁令
（禁 `readable`）我可以繞過而不自知，判準不行。

---

## 4. 變動後之 7 條逐條內容

（其餘 7 條 001/002/003/004/008/013/014 本輪未變動，不列）

#### NR1L-ComfortHMI-005 — SWE1-HVAC-078-01 — `13.3`

| 欄 | 值 |
|---|---|
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Press "+" once on the door seat control |
| M expected_result | 1. The lumbar/bolster state before the adjustment is shown<br>2. The popup or the tab change is shown, and the adjustment is not reflected |

#### NR1L-ComfortHMI-006 — SWE1-HVAC-078-02 — `13.3`

| 欄 | 值 |
|---|---|
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Press "+" a second time on the door seat control |
| M expected_result | 1. The lumbar/bolster state before the adjustment is shown<br>2. The adjustment is reflected |

#### NR1L-ComfortHMI-007 — SWE1-HVAC-079-01 — `13.3.1`

| 欄 | 值 |
|---|---|
| L test_procedure | 1. Record which lumbar/bolster adjustment type is the selected option<br>2. Run a keycycle<br>3. Open the Seats tab and read the selected option |
| M expected_result | 1. The selected option before the keycycle is shown<br>2. The head unit completes the keycycle<br>3. The selected option is the one shown in step 1 |

#### NR1L-ComfortHMI-009 — SWE1-HVAC-080-01 — `13.4`

| 欄 | 值 |
|---|---|
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Long press "+" on the door seat control<br>3. Release "+" |
| M expected_result | 1. The lumbar/bolster state before the adjustment is shown<br>2. The lumbar/bolster increases faster than it does for a single short press<br>3. The lumbar/bolster stops increasing |

#### NR1L-ComfortHMI-010 — SWE1-HVAC-080-02 — `13.4`  **[BLOCKED-SPEC]**

| 欄 | 值 |
|---|---|
| I test_item | The user will be able to long press on the touch screen itself to initiate fast increases/decreases, with the long-press logic as per HMI Core Logic and Flow (requirement N0) |
| L test_procedure | **（空）** |
| M expected_result | **（空）** |
| N spec_reference | `…_13.4`（照常填） |
| AH Remarks | [BLOCKED-SPEC] Long-press logic is defined by HMI Core Logic and Flow requirement N0. With that delegation removed this requirement has no content left that can be verified against the Comfort HMI specification alone |

#### NR1L-ComfortHMI-011 — SWE1-HVAC-081-01 — `13.5`

| 欄 | 值 |
|---|---|
| L test_procedure | 1. Record the lumbar/bolster state shown before the adjustment<br>2. Short press "+" on the door seat control<br>3. Short press "-" on the door seat control |
| M expected_result | 1. The lumbar/bolster state before the adjustment is shown<br>2. The lumbar/bolster is increased<br>3. The lumbar/bolster is decreased back to the state shown in step 1 |

#### NR1L-ComfortHMI-012 — SWE1-HVAC-081-02 — `13.5`  **[BLOCKED-SPEC]**

| 欄 | 值 |
|---|---|
| I test_item | A short press will increase the lumbar/bolster by a small set amount, that would be equivalent to a short press of the previous 4-way rocker hard control |
| L test_procedure | **（空）** |
| M expected_result | **（空）** |
| N spec_reference | `…_13.5`（照常填） |
| AH Remarks | [BLOCKED-SPEC] The equivalence to the previous 4-way rocker hard control is defined by CFTS044. With that delegation removed this requirement has no content left that can be verified against the Comfort HMI specification alone |

---

## 5. lint —— 29 → 31 gate，含具名豁免行

```
files: 7   TCs: 14   vocabulary: 9 strings   valid outlines: 129

（原 29 gate 全 PASS，略）
- PASS — blocked-row-empty
- PASS — blocked-remarks
- PASS — rows exempted as BLOCKED-SPEC (proc-min-steps, proc-er-1to1):
         ['NR1L-ComfortHMI-010', 'NR1L-ComfortHMI-012']

31 / 31 gates PASS; 0 finding(s) across 14 TCs
```

### 5.1 乙 —— 豁免不是免檢，是換一組檢查

R-C24 只要求豁免 `proc-min-steps` 與 `proc-er-1to1`。**只做這件事會讓
BLOCKED row 成為不被任何 gate 覆蓋的洞** —— 它可以帶半條 procedure、
可以把 marker 寫在句中、可以在外部可見欄位寫 `A-CF12`，而全部綠燈。

故另加兩個 gate：

| gate | 檢查 |
|---|---|
| `blocked-row-empty` | BLOCKED row 之 procedure／ER 必須**空**。「短」不算 —— 帶一步就是半寫成，不是 blocked |
| `blocked-remarks` | marker 須為 Remarks **開頭 token**；且 Remarks 不得含 `A-CF\d+`／`R-C\d+`／`§\d`（外部可見，AMFM R10-4） |

### 5.2 三種反向驗證

| 情形 | 期望 | 實測 |
|---|---|---|
| **非 BLOCKED row 單步** | `proc-min-steps` 仍 FAIL | ✅ `[FAIL] proc-min-steps: NR1L-ComfortHMI-004: 1 numbered step(s)` |
| BLOCKED row 帶殘留 procedure | `blocked-row-empty` FAIL | ✅ `[FAIL] blocked-row-empty: NR1L-ComfortHMI-010: … not empty (R-C24)` |
| BLOCKED Remarks 含 ruling id | `blocked-remarks` FAIL | ✅ `[FAIL] blocked-remarks: NR1L-ComfortHMI-012: … must not carry an internal ruling id` |

第一項是 21 §5.4 指定之驗證：**豁免未擴散到非 BLOCKED row。**
三次還原後皆回到 31/31。

---

## 6. §9 self-check —— 依 R-C23 重做，僅列變動項

**R-C23 之落實**：每項依據須獨立於 lint 之涵蓋範圍。故下表之「依據」欄
**不得只寫 gate 名** —— 凡依據為 gate 者，另註該 gate 檢查的是什麼、
以及**它不檢查什麼**。無獨立依據者標「未實測」。

| # | §9 項目 | rev2 | rev3 | 獨立依據（R-C23） |
|---|---|---|---|---|
| 5 | 步驟可執行、Final Step 擁有驗證 | PASS | **PASS（12 條）／N/A（2 條 BLOCKED）** | 逐條讀 procedure 末步與其 ER。BLOCKED row 無 procedure，該項對其不適用 —— **標 N/A 而非 PASS**（R-C23：無對象即無依據） |
| 10 | Procedure ↔ ER 1:1、**ER 可觀察** | PASS | **PASS（12 條）／N/A（2 條）** | 逐條讀 ER 主詞：現全為系統可觀察之物（`is shown`／`is reflected`／`is increased`／`is greyed out`／`is played`）。`proc-er-1to1` gate 只驗**列數相等**，不驗主詞是誰 —— 主詞之判定為人工逐條 |
| 11 | 無 FP／FF | PASS | **PASS，且理由改變** | rev2 之依據為「014 為負向、與 011/013 配對」。rev3 另加一項：**010/012 若照 rev2 維持，即為 §7 之 False Pass**（21 §1.1）—— 現已轉 BLOCKED row，該風險消除 |
| 12 | 追溯 RD、不擴張、無造範圍 | PASS | **PASS** | rev2 已移除虛構之觸控面分支；rev3 另移除 `delegated-only` 軸與 `split_flag` 之誤用。逐條核對 14 個 req_id ↔ 14 個 leaf，無合併、無遺漏 |
| 16 | `specification_reference` 列全每個直接驗證之節 | PASS | **PASS，含 BLOCKED row** | BLOCKED row 之 `spec_ref` **照常填**（R-C24），故 traceability 表無空洞。`spec-ref-outline` gate 驗其在 129 節內，但**不驗 BLOCKED row 是否該有 ref** —— 該判定依 R-C24 條文 |

**其餘 12 項自評不變**（1、2、3、4、6、7、8、9、13、14、15、17）。

### 6.1 R-C23 對自評本身的影響

依 R-C23 重做後，**兩項由 PASS 改為部分 N/A**（第 5、10 項對 BLOCKED row）。
rev2 若沿用舊寫法會直接報 PASS —— 因為 lint 對 BLOCKED row 豁免了那兩個
gate，而「lint 沒報」正是 R-C23 禁止作為依據的東西。

**這是 R-C23 生效的第一個實例**，且它改變的不是判定對錯，是**判定的粒度**：
14 條一律 PASS 掩蓋了「其中 2 條根本沒有 procedure 可判」這件事。

---

## 7. DATA_REQUESTS #16（21 §1.4）

Core N0 與 CFTS044 之**涵蓋**問題，與 #13／#14 是**不同的問題**：

| | 問的是 | 答 |
|---|---|---|
| #13／#14 | 要不要取得該文件？ | **不需要**（已判 out of scope，取得反誘使越界，19 §4.3） |
| **#16** | 那些行為在本專案**有沒有任何 SWE 需求涵蓋**？ | **未知 —— 待上游確認** |

**若無，即為真實 coverage hole**（§8.4.2），而那不是範圍界定能解決的 ——
範圍界定只說明「不由 Comfort 驗」，不保證「有人驗」。
Urgency Medium，**不阻塞**（兩 leaf 已產 BLOCKED row，未遺失）。

---

## 8. 未做者

- **未寫回 workbook**（21 §5.8）—— `output/` 未動，`DELIVERY.sha256` 仍 2 筆。
- 未擴大 BLOCKED 之適用（僅 R-C24 所裁之二列；profile §5.1 已具名列出）。
- 未動 `framework.md`、`RULINGS.md` 既有條文（R-C23／R-C24 為新增，
  profile §5 為 21 §5.2 指定之改寫）。
- 未動 home 之任何檔案；未重跑既有 feature 之 recon（R-C8）。
- 未執行 git。

---

## 9. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 9.1 已驗

1. 四種謂語之全批掃描（rev2 命中 7 條 → rev3 為 0）。
2. 兩個 BLOCKED row 之六個欄位（procedure/ER 空、spec_ref 照填、
   Remarks marker 開頭且無 ruling id、split_flag 復位、axis 移除）。
3. 三種反向驗證，含 21 §5.4 指定之「非 BLOCKED 單步仍 FAIL」。
4. profile §5 之三者對照（`[BLOCKED-ECU]`／`[BLOCKED-SPEC]`／R-C16 缺口項）。
5. §9 自評依 R-C23 重做，兩項改為部分 N/A。

### 9.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **BLOCKED row 於 workbook 之呈現** | 未寫回（本包禁止） | 中 —— 空 procedure 欄與 Remarks 之長字串在 xlsx 內之換行行為未驗；寫回時須確認 |
| 2 | **其餘 12 條是否另有 rev1/rev2 未察之 defect** | 檢查者仍是被檢查者 | **中** —— rev1 四項、rev2 一項皆由 review 端發現，**非我自查所得**。第五項（`is recorded`）我 rev2 才剛改過那幾行仍未察覺 |
| 3 | **`[BLOCKED-SPEC]` 是否會被濫用** | 本批僅二列，皆經裁定 | 中 —— profile §5 已寫「新增 marker 須先裁決」，但**無 gate 阻止未經裁定之列自行掛 marker**。可加「marker 白名單」gate，本包未加因未指示 |
| 4 | §10.4 四段順序 | 21 §4 已採納不加 gate | 低 |

**第 2 項需要具體說明，因為它有一個新事實**：rev2 我改寫了 005/006/007/009/
011 那幾行 ER，**改完之後那些行仍帶 `is recorded`** —— 我當時盯著 `readable`
這個字，沒看主詞。同一段文字我親手改過又漏掉，這比「沒看過所以沒發現」
更值得記：**改動點不等於審視點。**

### 9.3 執行層對「本包可否結案」之判斷

**可送 review。** 兩個 defect 已依裁定處置、31 gate 全 PASS 且新增者皆經
反向驗證、§9 自評已依 R-C23 重做並暴露出兩項粒度問題。

**review 時建議優先看**：
1. §3.2 之 ER 改法是否已真正把主詞換到系統上（`is shown` 仍是被動語態，
   主詞是狀態不是觀察者 —— 但這判斷是我做的，需獨立複核）
2. 兩個 BLOCKED row 之 Remarks 措辭是否合外部可見之要求
3. §9.2 第 3 項 —— 是否需要 marker 白名單 gate
