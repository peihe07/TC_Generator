# 上繳 20 — 第一批覆核之修正（C-1 ～ C-6）

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`20_batch01_review.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）
- 語料：**73 條 TC**（未變動條數；本輪修改其中 5 條之內容）

## 0. **執行順序與 20 包所設不同 —— 先講清楚**

20 包 §開頭載「19 之作業 1–4 照跑，作業 5–6 於本包之 C-1／C-2 修正完成後同輪進行」。

**實際順序**：**19 包之作業 1–6 已於上一輪全部完成並提交**（`378cce5`），
其上繳為 `docs/upstream/19_batch02.md`＋`19_provenance3.md`。
即 **第二批（29 條）之生成早於本包之 C-1／C-2 修正**。

**此差異之實際影響，逐項查證**：

| 項 | 影響 | 查證 |
|---|---|---|
| C-1（TC-039 之 ER）| **無** | 屬 batch01 之單條；第二批無同型（ch12–14 無表格）|
| C-2（BVA 自檢）| **有，且對本包有利** | 自檢範圍由 20 包所設之 **6 條**變為 **7 條**（第二批之 `TC-066` 亦為 BVA）。**先生成使自檢母體更完整** |
| C-3／C-4／C-5 | **無** | 皆為 batch01 之單條或文件 |

**故未重跑 19 包之任何作業**，亦未回退第二批。**若分析層認為順序本身須遵守，
可退回本包；但重做之產出會與現況逐字相同**，故未主動重做。

## 1. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 73 條，**違規 0** |
| `lint_tcs.py --self-test` | 51 / 51 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 73 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |

```
design_method 分布：功能測試×41, 基礎故障注入×2, 情境 / 用例×3,
                    狀態轉換×10, 負向測試×11, 邊界值分析×6
priority 分布：P0×17, P1×25, P2×28, P3×3
```

（design_method 之變化：功能測試 40→41、邊界值分析 7→6 —— 即 C-2 之改判。）

---

## 2. C-1 —— TC-039 之 ER 補完（**工具首次用在它為之而建的第二個案例上**）

### 2.1 chart 之複位

`10.3.1` 之「the info in the chart above」經複位為 **PDF p16 之
`Table PIP1.) Profile Info Display Text`** —— 兩欄（Category Title／Description）、
**15 列**，以 `render_spec_region.py --page 16 --table 467,60,766,532` 機器讀出：

```
格線：水平 17 條  垂直 3 條
  Screen Customization                  | Home Screen Customization
  Screen Customization                  | Menu Bar Order
  Screen Customization                  | Status Bar Customization
  Apps                                  | App Drawer Favorites
  Apps                                  | Recently Used Apps
  Media                                 | Your Presets
  Media                                 | Last Media Source
  Media                                 | Audio Settings
  Rear Steering Wheel Controls (if applicable) | Audio Control Selections
  Navigation (if applicable)            | Favorite Destinations
  Navigation (if applicable)            | Recent Destinations
  Navigation (if applicable)            | Nav Settings
  ****Connected Account (if applicable) | Save your preferences to the cloud and
                                          access them from vehicle to vehicle
                                          (with a Uconnect.com subscription)
  Bluetooth                             | Favorite Devices
  Electric Vehicle                      | Creep Selection
```

15 列已逐列補入 ER（§6.1 之 `a.`–`o.` 子層）。

### 2.2 連帶發現：`****` 為**列級**變體，故本 TC 加一條 pre-condition

p16 之註記：`****R1 High Only: for the "Connected Account" category title
(if applicable) the Description is the following: "Save your preferences to the
cloud and access them from vehicle to vehicle."` ——
其 `****` 對應 **`****Connected Account` 那一列**，即 **R1 High 車上第 m 列之
Description 少了「(with a Uconnect.com subscription)」那一段**。

故 TC-039 新增 pre-condition `The vehicle is not an R1 High variant`，
使 15 列之預期（含第 m 列之完整字串）成立。**若不加，該 TC 在 R1 High 車上假失敗。**

### 2.3 **工具本身在本案例上紅了兩次 —— 皆為判準錯**

| # | 現象 | 成因 | 修法 |
|---|---|---|---|
| 1 | 垂直線讀成 **0 條** → 欄數 0 → **整張表讀不出來** | 判準要求線段之**起點落在框內**；PIP1 表之垂直線起於 y=59.7 而我給的框自 y=60 起 —— **差 0.3pt 整條被排除** | 改以**重疊**判定 |
| 2 | 改用 `Rect &`／`.intersects()` 後**仍為 0** | **格線是零寬矩形，PyMuPDF 一律視其為 empty**，兩者皆回 False | 以座標自行判重疊 |

**第 1 項之危險在於它的失敗形狀**：不是報錯，是**回報「這張表沒有欄」**——
若不去看渲染圖對照，會被讀成「該表無法判讀」而寫進限制。

### 2.4 工具擴充：文字表之格內文字

`read_table` 原只回報「哪一格有勾記」（為 CPA2 之打勾表而建）。
PIP1 為**文字表**，格內無勾記 —— 原樣輸出會是一整片 `False`。
已擴充為同時回報**格內文字**；CPA2 之回歸 **7/7 未受影響**。

---

## 3. C-2 —— TC-036 改 design_method，並自檢全批 BVA

### 3.1 TC-036（9.9）：**BVA → 功能測試**

`input_test_data` 為 `Line count per page: 6 (limit)`，procedure 只驗「不超過六行」——
**無 limit±1，亦無界前基準線**。§12 之 BVA 為 `Boundary (=limit, limit±1)`，
首匹配落在「單一功能檢查 → 功能測試」。

**18 輪 §1 自陳「036 只驗上限，無界前基準線」而 design_method 仍掛 BVA** ——
兩處記載互相矛盾，本輪以其實際形態為準。

### 3.2 全批 BVA 自檢 —— **母體 7 條（非 20 包所載之 6 條）**

20 包寫「現為 6 條」是以 batch01 為止之語料計；**第二批之 `TC-066` 亦為 BVA**，
故實際母體為 7。改判 1 條後餘 **6 條**，逐條列其邊界對：

| tc_id | sec | 邊界對 | 界前基準線 | 判 |
|---|---|---|---|---|
| 003 | 5.2 | 4（未達）→ 5（上限）| ER1「四個時按鈕在」| **維持 BVA** |
| 008 | 7.4 | 29 s → 30 s | ER2「29 秒仍在」| **維持** |
| 009 | 8.7 | 11 → 12 → 第 13 字元 | ER1「11 字元」| **維持** |
| 015 | 12.9 | 第 9 次 → 第 10 次 | ER3「第 9 次後仍受理」| **維持** |
| 030 | 9.5.3 | 2 vs 2（相等）→ 3 vs 2（超過）| ER1「相等時不可用」| **維持** |
| 066 | 12.9 | 29 min → 30 min | ER2「29 分仍鎖定」| **維持** |
| ~~036~~ | 9.9 | **無** | **無** | **改功能測試** |

**六條皆有邊界對且皆有界前基準線**（其中三條之界前為「方法」來源，已於 19 輪標示）。

---

## 4. C-3 —— TC-044 之 ER2 後半改寫

| | 內容 |
|---|---|
| 前 | `No info button is shown next to the Connected Account button, **and the Local vs Connected Profile screen cannot be opened**` |
| 後 | `No info button is shown next to the Connected Account button **and no entry point to the Local vs Connected Profile screen is present**` |

**採改寫而非刪除**：刪除後 ER 只剩「該按鈕不在」，
而條文之 `There will be no info button showed nextto the Connected Account button`
與「該畫面無從進入」是同一件事之兩面；
改寫後兩者皆為**可觀察之缺席**，負向配對之效力不減。

---

## 5. C-4 —— priority 分野寫入 `DECISIONS.md`

`D-UP16-01` 新增「附一 — 『偏好之儲存與回復』之邊界」：

> | | 判 | 例 |
> |---|---|---|
> | **儲存與回復之機制本身** | **P0** | TC-004（5.9）、TC-031（9.6）、TC-001（4.1）|
> | **個別設定項之值與其呈現** | **P2** | TC-032（9.6.1）、TC-046（12.1.1）|
>
> **判別問法**：失效時壞掉的是「東西存不存得住」，還是「某一項的值是什麼」？

**並聲明其灰帶**（R-G11）：「某設定項之值在 key cycle 後遺失」兩邊都沾 ——
處置為**以該 TC 之受測單位定**：驗該項之值 → P2；驗儲存本身（以任一項為載體）→ P0。

**未動 D-UP16-01 之 tie-break**（J-9）。

---

## 6. C-5 —— TC-040 之 reasoning 改述（**判級不動**）

| | 內容 |
|---|---|
| 前 | 「連網配置之**非主路徑分支**」 |
| 後 | 「具連網車輛之**主要功能呈現**（C-5：非分支）」；reasoning 內另註 `will always be displayed` 為主路徑 |

`priority` **維持 P1** —— 其為主要功能之呈現，不屬 R-U5 核心五類。

---

## 7. C-6 —— TC-017 ～ TC-027 之全文仍未逐條讀

**照錄，不推定已覆核。** 20 包已具名：該 11 條僅經 18 輪之出處對照覆核，
其 `pre_conditions`／`procedure`／`reasoning` **未逐條讀**。
第三批開批前補齊 —— **本包之核可不及於它們**。

---

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **TC-039 之 15 列未在實機上驗過其「applicable」之判定** | note | ER 列出 15 列並以 pre-condition 固定 Navigation 有、R1 High 無；**但 `Rear Steering Wheel Controls`／`Electric Vehicle` 兩列之適用條件未於 pre-condition 指定** —— 該車若無後座方向盤控制或非電動車，該二列不顯示而 TC 會假失敗 |
| 2 | **C-1 之同型是否還有第三例** | **未掃** | D-3（Table CPA2）、C-1（Table PIP1）為同型之第一、二例。**未全量掃描 `pdf_text` 中「以指代詞引用表格內容」之 ER** —— 現行 G18 只查字面值，不查「這句 ER 是否在指代一張表」 |
| 3 | **`render_spec_region` 之判準又改兩次** | note | 17 輪三次、本輪兩次，累計五次。**每次都是判準錯而非資料錯**，且**每次都以「讀不出來」之形狀出現** —— 這類失敗不會報錯，只會回報空結果 |
| 4 | **C-2 揭示之記載矛盾可能不只一處** | note | 18 輪 §1 之文字與 design_method 欄互相矛盾而無人察覺，直到本包點名。**未查其他欄位與 reasoning 之一致性** |
| 5 | **TC-017 ～ TC-027 未覆核**（C-6）| **分析層待辦** | 加上第二批 29 條之內容覆核，**未經第二人讀過者現為 40 條** |
| 6 | **A-UP11 之全量掃描仍未做** | 承前（19 輪）| 037 之 title↔description 對齊只查過 12.8／12.8.1 七條 |
| 7 | **R-U5 無安全帶** | **待裁（第四次）** | 本包未涉，但 116／135／089 三條仍掛著 |
| 8 | A-UP09／R-U14、DR #3／#4／#5、R-U17、N-XF01、A-UP10 | 承前 | 擋 Phase 6 寫回 |

---

## 9. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch01.py`（C-1 之 ER 15 列＋pre-condition＋remarks、C-2 之 design_method、C-3 之 ER2、C-5 之 reasoning 與 priority_basis）| 否 |
| 2 | 檔案編輯 | `scripts/render_spec_region.py`（格線判準改重疊、零寬矩形之處置、格內文字）| 否 |
| 3 | 檔案追加 | `DECISIONS.md`（D-UP16-01 附一）| 否 |
| 4 | 檔案重生成 ×28 | `generated/`（batch01；**內容變動者 5 條**：036／039／040／044 與 109 之 basis）| 否 |
| 5 | 檔案新建 | `docs/upstream/20_batch01_review_fixes.md`（本檔）| 否 |
| 6 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 7 | 程式執行 | 生成 ×1、全部閘、`render_spec_region --table`／`--regression` | 否 |
| 8 | **唯讀** | `fitz` 讀 spec PDF p16 | 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` 皆無，**唯讀之 `git status` 亦未跑**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`.gitignore`、
`data/`、`scripts/gen_pilot.py`、`scripts/gen_batch02.py`、`scripts/lint_*.py`、
**他 feature 之任何檔**、`docs/fw036/`。

---

## 10. 修改後之五條 TC 全文

### NR1L-UserProfiles-036 — SWE1-HMI-PROF-105（9.9）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit Profile tab shows at most six lines per page |
| pre_conditions | 1. A Driver Profile is active with all optional items available<br>2. The vehicle is stationary |
| input_test_data | Line count per page: 6 (limit) |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Count the information lines shown and check that no more than six are on the page |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. At most six lines of information are shown on the page |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.9 |
| priority | **P3** — 單頁最多 6 行 —— 版面上限，失效僅影響該頁可讀性 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.9（EDPR10）—— Edit Profile 分頁每頁最多 6 行資訊。關鍵情境條件：須在選項最多之情況下才驗得到上限，故 pre-condition 要求各選用項目皆可用。為什麼這樣切：清單之順序屬 9.1，本 leaf 只管每頁行數之上限。

### NR1L-UserProfiles-039 — SWE1-HMI-PROF-108（10.3.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Driver Profile info page shows the intro text and examples |
| pre_conditions | 1. The vehicle is equipped with Navigation<br>2. The vehicle is not an R1 High variant<br>3. A Driver Profile is active<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the Driver Profile info page<br>2. Read the page and check that the intro text and the applicable examples are shown |
| expected_result | 1. The Driver Profile Info Page is displayed<br>2. The page reads “Your Driver Profile will remember your personal preferences for many of the features you use in your vehicle everyday. Below are some examples.” followed by the applicable rows of Table PIP1:<br>   a. Screen Customization — Home Screen Customization<br>   b. Screen Customization — Menu Bar Order<br>   c. Screen Customization — Status Bar Customization<br>   d. Apps — App Drawer Favorites<br>   e. Apps — Recently Used Apps<br>   f. Media — Your Presets<br>   g. Media — Last Media Source<br>   h. Media — Audio Settings<br>   i. Rear Steering Wheel Controls (if applicable) — Audio Control Selections<br>   j. Navigation (if applicable) — Favorite Destinations<br>   k. Navigation (if applicable) — Recent Destinations<br>   l. Navigation (if applicable) — Nav Settings<br>   m. Connected Account (if applicable) — Save your preferences to the cloud and access them from vehicle to vehicle (with a Uconnect.com subscription)<br>   n. Bluetooth — Favorite Devices<br>   o. Electric Vehicle — Creep Selection |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_10.3.1 |
| priority | **P2** — linked-info 頁之內容（**037 先驗 Low，本判為 P2**） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之「the info in the chart above」指**頁內之 chart**（R-U51 口徑，D-UP12-02），非 PLP 表 —— 該 chart 經複位為 PDF p16 之 **Table PIP1「Profile Info Display Text」**，15 列以 `render_spec_region.py --table` 機器讀出。Navigation 之有無為條文明列之適用條件，故列 pre-condition。R1 High 車上第 m 列之 Description 無 Uconnect.com 訂閱那一句（p16 之 `****` 註記，**列級**）—— 本 TC 以非 R1 High 為前提 |

**reasoning**：驗證目標：10.3.1（PRINFO2.1）—— 資訊頁之引言字串與其後之適用範例。關鍵情境條件：條文明言「若車輛無 Navigation 則不顯示 Navigation 範例」，故 pre-condition 指定為有 Navigation 之車，使該範例確實可觀察。為什麼這樣切：R1 High 之 Connected Account 類別描述為**列級**變體覆寫（p16 之 `****`），故以 pre-condition 排除該變體，使 15 列之預期成立。**C-1（20 包）**：原 ER 以「applicable examples」指代 chart 內容 ——同 D-3 之形狀。本輪以 `render_spec_region.py` 讀出 Table PIP1 之 15 列，逐列補入 ER（§6.1 子層）。刻意略過：無 Navigation 車輛之對照未生成 —— 取樣單位為 leaf（§8.4.2）。

### NR1L-UserProfiles-040 — SWE1-HMI-PROF-109（11.3）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected Account line shown when the vehicle has connectivity |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. A Driver Profile is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that the Connected Account line item is displayed |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. The Connected Account line item is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.3 |
| priority | **P1** — 具連網車輛之主要功能呈現（C-5：非分支） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 不支援連網之對照（條文第二句）屬同節之反面，其覆蓋由 9.2（EDPR2）之 leaf 承擔 |

**reasoning**：驗證目標：11.3（CPA1）—— 具連網能力之車輛，Edit Profile 分頁**一律顯示** Connected Account 項目 —— 該行為為**主要功能之呈現**，非分支（C-5：原述「非主路徑分支」與條文之 `will always be displayed` 不符；**判級 P1 不變**，其為主要功能之呈現而非核心五類）。關鍵情境條件：車輛配置為條件本身，列 pre-condition。為什麼這樣切：條文另有「不支援則不顯示」之反面，其形態與 9.2 之區域／車型隱藏相同，由該 leaf 承擔，本條不重複。

### NR1L-UserProfiles-044 — SWE1-HMI-PROF-111（11.4）

| 欄 | 值 |
|---|---|
| tc_title / test_item | No info button next to Connected Account on R1 High |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A Driver Profile is active and the “Edit Profile” tab is available |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the Connected Account line and check that no info button is shown next to it |
| expected_result | 1. The “Edit Profile” tab is displayed with the Connected Account line<br>2. No info button is shown next to the Connected Account button and no entry point to the Local vs Connected Profile screen is present |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.4 |
| priority | **P2** — R1 High 變體之呈現（資訊按鈕不存在） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | §7 之負向配對：正向為 NR1L-UserProfiles-013（非 R1 High）。依據為 Table CPA2 之表級註記「**R1 High Only: This table (Table CPA2) is not applicable. There will be no info button showed nextto the Connected Account button.」（PDF p17） |

**reasoning**：驗證目標：11.4 之 R1 High 變體 —— 該表不適用，且 Connected Account 旁沒有資訊按鈕。關鍵情境條件：變體為條件本身（§8.7.3），列 pre-condition。為什麼這樣切：本條與 TC-013 構成 §7 之列舉配對 —— TC-013 驗「非 R1 High 有該畫面與其四列」，本條驗「R1 High 沒有入口」。**只有正向會使一個「永遠顯示該畫面」之實作通過**。刻意略過：R1 High 之其他變體差異（如 9.3.2 之 label 覆寫）屬各自之 leaf。

