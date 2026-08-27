# 上繳包 28 —— Vehicle Category：R-VC27 ＋ 交付形態五項（T145–T150）

- 日期：2026-08-27
- 對應下放：`docs/handoff/28_writeback_prep.md`
  （SHA256 `bfe1e75f6f77d7a58a1c5c1bcf373c78eb83499fb6cb25a63c5da968ab095e23`，194 行）
- **結論：T146–T150 完成。T145 停於第 3 步之二個障礙，第 5 步未執行。**
- 未寫回工作簿、**母本 SHA256 前後未變**、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T145 | 丙′ 可行性 | ⚠ **停** —— 二個障礙皆在第 3 步，**第 5 步無從執行**。見 §1 |
| T146 | TC ID 形態勘查 | ⚠ **三種 `{project}` 前綴並存，其二與工作簿自己的 D2 相牴觸**。見 §2 |
| T147 | R-VC27 抄錄 ＋ R-VC12 二(a) 加註 | ✅ byte-level `diff -q` 相同（`82c5188d06eb53d2`）|
| T148 | 表 B 三列逐字引錄／四處／DR-VC6 三問 | ✅ **且發現 DR-VC6 自己早就記對了**。見 §3 |
| T149 | A-VC20 補記成因 | ✅ |
| T150 | `reasoning` 側檔 120 筆 | ✅ 對應驗證雙向實測 |

**三件請你先看**：
1. **丙′ 的兩個障礙都不是「能不能修」，是「修的範圍超出 §2.3 第 3 步所列」** ——
   我依「不自行調整方案」停住，二個候選處置列在 §1.3，**未選**。
2. **DR-VC6 的「實測佐證（T17）」欄，自始就逐字記著那兩句話。**
   同一個 repo 裡，正解與錯解並存了 24 個包。這改變了 A-VC20 的教訓。見 §3.2。
3. **TC ID 三種前綴**，而**五份工作簿的 D2（專案名稱）全是 `newR1L`** ——
   `NR1L-`（8 個 feature）與 `TC-`（display）都與自己檔案裡的那格不符。見 §2。

---

## 1. ⚠ T145 —— 丙′ 停於第 3 步

### 1.1 完整輸出

```
步驟 1 —— openpyxl 開副本、寫入 14 欄、save
  母本   : x14_dv=1 extLst=1 std_dv=3 printer=5 media=['xl/media/image1.png', 'xl/media/image2.jpeg']
  step1  : x14_dv=0 extLst=0 std_dv=3 printer=0 media=['xl/media/image1.png', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']
步驟 2 —— 解壓輸出檔與母本
  母本 48 項；step1 47 項；消失 11 項
步驟 3／4 —— 自母本取出遭毀之結構，注入並重打包
  注入 extLst：是
  變體 A（含圖片還原）／變體 B（不還原圖片）各產一檔
  變體 A 可被 openpyxl 開啟：**否** —— KeyError: "There is no item named 'xl/media/image2.png' in the archive"
  變體 B 可被 openpyxl 開啟：**否** —— ParseError: unbound prefix: line 66, column 1451338

步驟 5 —— **未執行**。二變體皆不可開啟，停點如下。

障礙 1（變體 A）—— 圖片不可單獨搬回
  openpyxl 已把 drawing 之 rels 改指向其重新編碼後之檔名
  （母本 ['xl/media/image1.png', 'xl/media/image2.jpeg']
    → openpyxl ['xl/media/image1.png', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']）。
  只換 `xl/media/` 而不換 drawing 與其 rels，套件即缺檔。
  **修復範圍大於 §2.3 第 3 步所列**（該步只列「原始 image2.jpeg」）。

障礙 2（變體 B）—— extLst 逐字注入產生 unbound prefix
  片段所用之前綴 ['x14', 'xm', 'xr']；其自帶宣告者 ['x14', 'xm']。
  **`xr` 無自帶宣告** —— 其 xmlns 在母本 <worksheet> 根元素上，
  而 openpyxl 之輸出根元素只宣告預設 namespace。
  片段內 `xr` 之唯一用途為 `xr:uid="{GUID}"`（裝飾性）。

二個候選處置（**本檔不選**，待分析層裁）：
  (甲) 於輸出之 <worksheet> 根元素補宣告 xmlns:xr
       —— 片段保持逐字，但改動了輸出之根元素
  (乙) 自片段剝除 xr:uid 屬性
       —— 不動輸出，但**搬回之結構不再與母本逐字相同**

已量得之五項（步驟 1 之破壞，與上繳包 27 §3.4 一致）：
    x14:dataValidation       母本 1 → openpyxl 0
    extLst                   母本 1 → openpyxl 0
    標準 dataValidation        母本 3 → openpyxl 3
    printerSettings          母本 5 → openpyxl 0
    xl/media 檔數              母本 2 → openpyxl 9

母本 SHA256 前 6372fb6be02f48dc → 後 6372fb6be02f48dc  **未變**
產物在 /tmp/vc_writeback_c（/tmp，非交付本）

**丙′ 於本輪未被證實可行，亦未被證偽** —— 停於第 3 步之二個障礙，待裁。
```

### 1.2 二個障礙

| # | 障礙 | 為何超出 §2.3 第 3 步 |
|---|---|---|
| 1 | **圖片不可單獨搬回** —— openpyxl 已把 drawing 之 rels 改指向其重編碼後之檔名（母本 2 檔 → openpyxl 9 檔）。只換 `xl/media/` 套件即缺檔 | §2.3 第 3 步只列「原始 image2.jpeg」；實需連 **drawing XML 與其 rels** 一併搬 |
| 2 | **`extLst` 逐字注入產生 unbound prefix** —— 片段用 `x14`／`xm`／**`xr`** 三個前綴，前二者自帶宣告，**`xr` 的宣告在母本 `<worksheet>` 根元素上**，而 openpyxl 的輸出根元素只宣告預設 namespace | 修復須動**輸出之根元素**或**片段本身**，二者皆非「自母本取出、注入」之字面 |

### 1.3 二個候選處置 —— **未選**

```
(甲) 於輸出之 <worksheet> 根元素補宣告 xmlns:xr
     —— 片段保持逐字，但改動了輸出之根元素
(乙) 自片段剝除 xr:uid 屬性（其為 GUID，裝飾性）
     —— 不動輸出，但搬回之結構不再與母本逐字相同
```

**依 §2.3「若第 5 步任一項不符，停並回報，不自行調整方案」停住。**
二者都是一行的事，正因為如此才更該由你裁 ——
**一行就能讓它「過」，而那正是這條規則要防的。**

### 1.4 ⚠ 更正上繳包 27 §3.4 之一個數

我在包 27 寫 `x14:dataValidation 2 → 0`。**正確是 1 條。**
原先的 2 是正則 `x14:dataValidation[ >]` 同時數到開標籤與閉標籤。
**其餘各項（extLst 1→0、printerSettings 5→0、圖片重編碼）不變，
結論亦不變** —— `R10:R1411` 之設計方法下拉仍是「開了再存就沒了」。

### 1.5 已證實者

- **步驟 1／2／3／4 皆可執行**；14 欄 × 3 筆之寫入本身無礙。
- **步驟 1 之破壞與包 27 §3.4 逐項一致**（除 §1.4 之更正）。
- **母本 SHA256 前後未變**，全程在 `/tmp/vc_writeback_c/` 副本上。

**丙′ 未被證實可行，亦未被證偽。**

---

## 2. ⚠ T146 —— TC ID：三種前綴，兩種與工作簿自己的那一格不符

### 2.1 各 feature 之宣告（逐一列，不歸納 —— §2.4 明文）

| feature | `feature.yaml` 之宣告 |
|---|---|
| `amfm` | `tc_id_format: "newR1L-AMFM-{n:03d}"` |
| `audio_mgmt` | `tc_id_format: "NR1L-AMM-{n:03d}"` |
| `bed_lowering` | `tc_id_format: "newR1L-BLM-{n:03d}"` |
| `comfort` | `tc_id_format: "NR1L-ComfortHMI-{n:03d}"` |
| `display` | **未宣告**（其 `feature.yaml` 無 tc_id 鍵）|
| `home` | **未宣告** |
| `power` | `tc_id_format: "NR1L-PowerManagement-{NNN}"` |
| `power_moding` | `tc_id_format: "NR1L-DisclaimerScreen-{NNN}"` |
| `privacy` | `tc_id_format: "NR1L-Privacy-{n:03d}"` |
| `projection` | **未宣告** |
| `sw_update` | **未宣告** |
| `sxm` | `tc_id_format: "NR1L-SXM-{n:03d}"` |
| `time_management` | `tc_id_format: "NR1L-TimeManagement-{n:03d}"` |
| `user_profiles` | `tc_id_pattern: "NR1L-UserProfiles-{NNN}"`（**鍵名不同**：`_pattern` 非 `_format`）|
| `vehicle_category` | **未宣告** |
| `vehicle_setting` | **未宣告** |

### 2.2 已交付工作簿之實際值

| feature | `F` 欄實測 | 筆數 | 序號 |
|---|---|---|---|
| `display` | `TC-DM-001` … `TC-DM-023` | 23／24 列 | 1–23，**連續** |
| `privacy` | `NR1L-Privacy-001` … `-011` | 11／11 | 1–11，**連續** |
| `sxm` | `NR1L-SXM-001` … `-215` | 215／215 | 1–215，**連續** |

**`E`（Test Case ID (TestRail)）三者皆 0 筆有值。**

### 2.3 ⚠ 五份工作簿之 D2（專案名稱）**全部是 `newR1L`**

| 工作簿 | `C2` | `D2` |
|---|---|---|
| VC 母本（空模板）| `專案名稱 Project  Name：` | **`newR1L`** |
| `display` 交付本 | 同 | **`newR1L`** |
| `privacy` 交付本 | 同 | **`newR1L`** |
| `sxm` 交付本 | 同 | **`newR1L`** |
| `forms/` 之母本 | 同 | **`newR1L`** |

**三種 `{project}` 前綴**：`newR1L-`（amfm／bed_lowering）、
`NR1L-`（8 個 feature）、`TC-`（display）。

**其中 `NR1L-` 與 `TC-` 都與該檔自己的 D2 不符。**
`privacy` 與 `sxm` 之交付本，其 D2 寫 `newR1L` 而其 `F` 欄寫 `NR1L-`。

`bed_lowering` 之 `feature.yaml` 註解逐字記著這件事：
> 「全案之 project 前綴為 `newR1L`，其權威為工作簿 D2 儲存格
> （本包實測 = "newR1L"），amfm 交付本之 `newR1L-AMFM-001…143` 為既有實例。」

**即：有一個 feature 已經量過並寫下權威來源，而多數 feature 用的是別的值。**

**依 §2.4「若各 feature 不一致，逐一列出，不歸納」——
以上為列舉，本包不提案、不歸納、不推薦。**

---

## 3. T147／T148／T149 —— R-VC27 與 A-VC20

### 3.1 落實

- **R-VC27** 逐字抄入 `RULINGS.md`，`diff -q` byte-level 相同（`82c5188d06eb53d2`）。
- **R-VC12 二(a)** 加註作廢（fence 外，原文不刪，R-TM13），
  加註載明 §1.2 之成因：**該款是它自己所禁之方法的產物**。
- **表 B 三列**改為逐字引錄 SYS1 `Description`（§15 另加一句說明其為標題句＋三圖佔位）。
- **待 DR-VC3 之處更正為四處**（§11.9 群，下放包 28 §2.1 追認）。
- **DR-VC6 改為三問**（§15 之三圖／§10.1–10.2 之四圖／`All four Aux switches` 一句之地位）。
- **A-VC20** 補記成因，狀態改為**已解（R-VC27）**。

### 3.2 ⚠ 而 DR-VC6 自己早就記對了

`DATA_REQUESTS.md` 之 DR-VC6，其「**實測佐證（T17）**」欄逐字寫著：

> 「§10.1／10.2 僅存『Refer to the HMI Settings list』
> 『All four Aux switches … simultaneously』與 image9–12 佔位」

**那是對的。而 R-VC12 二(a) 與表 B 同期寫成「未帶文字」。**

**同一個 repo 裡，正解與錯解並存了 24 個包**，而被引用的是錯的那一份。

**這改變了 A-VC20 的教訓**：
不是「沒人讀過那三格」—— **讀了、記對了，然後沒有任何機制去比對二者**。

> 光是「回到權威素材重測」不夠。
> **既有台帳之互相牴觸也要有人看見** —— 而現在沒有東西在看。
> 已逐字記入 DR-VC6 該欄之下。

---

## 4. T150 —— `reasoning` 側檔

`docs/REASONING_sidecar.md`，**120 筆**，隨工作簿一併交付。

- 鍵為 `leaf_id#n`，`n` 為該 leaf 於其批內之 TC 序 ——
  **拆分筆據此區分**（`SWE1-HMI-VC-038-03#1`／`#2`），實測 9 個第 2 筆以上。
- 內容為該 TC 之 `reasoning` 全文 ＋ `distinguishing_axis`。
- `split_flag`／`split_reason` 不入（profile §11）。

### 4.1 對應驗證為**雙向**，且雙向實測過

```
對應驗證：鍵 120 個（其中拆分之第 2 筆以上 9 個）；PASS
```

```
(a) 反向 1：刪去一個拆分筆之鍵 → **FAIL** ["側檔缺少之鍵 ['SWE1-HMI-VC-038-03#2']"]
(a) 反向 2：憑空加一個鍵       → **FAIL** ["側檔多出之鍵 ['SWE1-HMI-VC-999#1']"]
(b) 正向：還原後               → PASS
```

**多一鍵與少一鍵都要 FAIL** —— 只驗「側檔涵蓋了工作簿」會漏掉前者。

### 4.2 未機器化者

側檔與**工作簿**之對應**尚未驗**（工作簿未產出）。
現驗的是側檔對**六批 JSON**。
寫回實作時須補「側檔鍵集合 == 工作簿 D 欄 ∪ 拆分序」之驗證 ——
§2.2 第三項要的是那一個，本輪只能做到前半。**記明。**

---

## 5. 六批回歸（本包未動生成物）

```
pilot_glovebox                     22 checked / 0 failed
batch1_category_structure          22 checked / 0 failed
batch2_settings_list               22 checked / 0 failed
batch3_controls                    22 checked / 0 failed
batch4_settings_behavior           22 checked / 0 failed
batch5_ignition_availability       22 checked / 0 failed
```

---

## 6. 待你裁

1. **丙′ 之二個障礙**（§1.3）—— 甲／乙，或第四條路
2. **TC ID 之取值**（§2）—— 三種前綴並存，且多數與 D2 不符；
   本包不提案
3. `QS Suggestion` 第 4 項之狀態查詢（Tier 3，與 IN §10.2 直接衝突）
4. 同批 A（六項）、DR-VC3、DR-VC9(一)、DR-VC10（Tier 3）

---

## 7. 量測條件揭露（R-G8）

### T145

- 全程 `/tmp/vc_writeback_c/`；**母本只做 `read_bytes()` 與唯讀載入**，
  SHA256 前後實測未變。
- 3 筆假資料取自 `pilot_glovebox.json` 前三筆 ＋ recon 表之 `polarion_id`。
- **步驟 5 未執行** —— 其六項驗收無任何結果，不得引用為「丙′ 部分可行」。
- 二個障礙為**本次實作路徑**所遇；不排除另有實作方式不觸及它們。

### T146

- 宣告值取自 16 個 `feature.yaml`，逐檔讀。
- 實際值取自三份 `output/` 交付本之 `F` 欄，逐列讀。
  **`amfm`／`home`／`comfort` 等其餘已 tag 之 feature 未見 `output/` 之 xlsx**，
  故其實際值**未量到** —— 本節之「已交付工作簿」僅三份。
- D2 取自五份工作簿，逐檔讀。
- **未查**：TC ID 是否跨 feature 連續、是否有保留區段 ——
  三份交付本各自 1 起算且各自連續，**跨 feature 之關係無從由此三份判定**。

### T150

側檔之鍵與內容**自六批 JSON 推導**，非人工填 ——
故「側檔與 JSON 相符」對本輪而言必然成立，**其保護力自下一次 JSON 變動起才是真的**。
