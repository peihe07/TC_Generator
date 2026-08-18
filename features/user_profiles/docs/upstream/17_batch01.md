# 上繳 17（A、C）— J-1／J-2 落地與第一批生成

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`17_batch01.md`（**無裁決條文**）
- 另一份上繳：`17_er_provenance.md`（作業 B，**55 句 ER 逐句對照**）
- **本輪未執行任何 git**（R-G5／R-G12）；**未寫回工作簿**（R-U14）

## 0. 全閘現況（**44 條 TC**）

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | **44 條，違規 0** |
| `lint_tcs.py --self-test` | 37 / 37 |
| `lint_variant_labels.py` 反向 | 9 / 9 |
| `lint_variant_labels.py --check` | 44 條，**違規 0**（**修正前為 2，見 §3.1**）|
| `build_batch_context.py --selfcheck` | 8 / 8 |
| **`render_spec_region.py --regression`** | **7 / 7**（本輪新建）|

```
掃 44 個 leaf 檔 / 44 條 TC
tc_id 範圍 NR1L-UserProfiles-001 … NR1L-UserProfiles-044（44 條）
design_method 分布：功能測試×26, 基礎故障注入×1, 情境 / 用例×3,
                    狀態轉換×6, 負向測試×2, 邊界值分析×6
priority 分布：P0×9, P1×15, P2×18, P3×2
違規 0
```

---

## 1. 作業 A-1 —— J-1 之代價句落地

`DECISIONS.md` **D-UP17-01**（口徑、駁回嚴格讀之理由、與 F-1 之區別表、代價）。

**並依 J-1 明文寫入覆蓋稽核之判準處** —— `framework.md` 新增 **§4.1**：

> ### 4.1 覆蓋率不得以 `specification_reference` 推定（J-1，17 包）
>
> 一條 TC 之 `specification_reference` 列了某節，**不等於該節已被驗證**。
> …**故覆蓋稽核之分子一律取「實際被驗之節／列」，不取引用欄。**

**放在 §4 之理由**：§4 就是「135 與 133 不得互換」那一節 ——
**同一種病的第二個病例**（一個數看起來像覆蓋率的分子，其實不是）。
放在那裡，算分子的人會在同一頁上讀到兩者。

## 2. 作業 A-2 —— `render_spec_region.py`（J-2）

### 2.1 它比「重繪」多做一件事

16 輪之判讀是**肉眼看重繪圖**。本輪落為工具時發現：**欄別可機器判定**。

| 物 | API | 本表之值 |
|---|---|---|
| 格線 | `page.get_drawings()` | 水平 6 條、垂直 4 條 |
| 勾記 | `page.get_image_rects(xref)` | 同一張 61×64 PNG **置放 5 次** |
| 文字 | `page.get_text("dict")` | 列標題與欄標題 |

勾記之中心座標落在哪一格 → **哪一列屬哪一欄**，不必靠眼睛。

### 2.2 回歸案例：**7 / 7 PASS**

```
$ python3 scripts/render_spec_region.py --regression
  格線：水平 [300.6, 341.4, 395.4, 436.2, 477.0, 531.0]
        垂直 [25.0, 203.3, 284.6, 333.6]
  勾記置放數：5

  PASS — 列數 × 欄數
  PASS — 欄標題
  PASS — 列「Personalization」之欄別 [True, True]
  PASS — 列「App Store」之欄別 [True, False]
  PASS — 列「Marketplace」之欄別 [True, False]
  PASS — 列「****Connected Navigation」之欄別 [True, False]
  PASS — App Store × Local 由『無』改『有』→ 偵測出不符
7 / 7 checks PASS
```

**16 輪之肉眼判讀，本輪以座標量測獨立複驗，逐格相符。**

### 2.3 建工具時踩到的三個坑（**都是判準錯，不是資料錯**）

| # | 現象 | 成因 | 修法 |
|---|---|---|---|
| 1 | 列數讀成 5（應 4）| 表格頂線由**兩條幾乎重合之線段**構成（300.2 與 300.6），被當成兩個列界 → 每列往下錯一格 | 格線去重，容差 1pt |
| 2 | 勾記數 10（應 5）| 同一勾記**以兩個 xref 疊放**（99 與 101，位置完全相同，各 177 bytes）| 依座標去重 |
| 3 | 又多一條列界 | **表頭 `FCA` 之刪除線**（25pt 寬之填色矩形）被當成格線 | 判準改為「**須橫跨表寬之過半**」——格線與刪除線之別不在細長，在跨不跨整張表 |

**三者若不修，讀出來的欄別會全錯**，而它「看起來」像是判讀不一致。

## 3. 作業 C —— 第一批生成（28 條）

`data/batch01_sample.tsv`（27 leaf）＋ `scripts/gen_batch01.py`。
tc_id **017–044**；`PROF-111` 之負向配對存為 `SWE1-HMI-PROF-111-neg.json`
（**非新 leaf**，加 `-neg` 以免覆寫該 leaf 之 pilot 產物）。

### 3.1 風險① `PROF-085` 之 `Stellantis Account` —— **lint 確實擋下，而且擋的是我**

**擋下了，違規 2 條：**

```
掃 44 條 TC，違規 2
  NR1L-UserProfiles-017.remarks: variant `R1 High` 之字面值出現 `Stellantis Account`，
    應為 `Connected Account`（spec 9.3.2 (PDF p14)，R-U35 (c)）
  NR1L-UserProfiles-023.remarks: 同上
```

**兩條都不是 ER 寫錯，是我在 `remarks` 裡寫了
「label 為 Connected Account（**非 Stellantis Account**）」** ——
語氣是「不要用那個」，但字面值確實出現在 `remarks` 欄裡。

**判為真陽性，改案例不改判準**：`remarks` 是工作簿之 AH 欄，**測試員看得到**。
在測試員看得到的欄位裡寫出被禁用之 label，本身就違反 R-U35 (c) 之目的 ——
規則不必、也無法分辨「用 X 不要用 Y」與「用 Y」。

修正後 **44 條違規 0**；另以注入複驗規則仍有效
（把 `Stellantis Account` 塞回 TC-017 之 remarks → **仍轉紅**）。

**判為 R1 High 之 TC（5 條）**：`011`（pilot）／`017`／`020`／`023`／`044`。
N-1 之否定判讀生效 —— TC-040（`PROF-111` 正向，pre-condition 為
「**not** an R1 High variant」）**未被誤判**。

### 3.2 風險② 9.5.x 四條之 sibling 軸（§8.3）

| tc_id | sec | tc_title | 軸 |
|---|---|---|---|
| 027 | 9.5 | Active Profile linked to the swapped memory seat position | **通則**（交換後連結至新位置）|
| 028 | 9.5.1 | Seat preferences swapped when the active Profile **was linked** | 前置狀態：**已**連結 |
| 029 | 9.5.2 | Previous Profile unlinked when the active Profile **had none** | 前置狀態：**未**連結 |
| 030 | 9.5.3 | None option greyed out until Profiles outnumber memory seats | **選項可用性**（非連結行為）|

**028 與 029 之分野只有一個變數**：pre-condition 中 Profile A 是否已連結座椅。
兩條之其餘設置**刻意保持相同**（皆為 Profile B 連 seat 2、皆選 seat 2）——
使失敗時可歸因於前置狀態，而不是別的差異。

**G5（sibling tc_title 雷同）未觸發**：四條之標題各自帶其軸之具體 token
（`swapped` / `was linked` / `had none` / `None option`）。

### 3.3 風險③ ch10 三條之 priority —— **逐條判，未機械給 P2**

037 先驗**三條皆為 Low**，本輪判出**兩個不同等級**：

| tc_id | sec | 037 | 判 | 依據 |
|---|---|---|---|---|
| 037 | 10.2 | Low | **P2** | linked-info 頁之開啟；輔助功能 |
| 038 | 10.3 | Low | **P3** | **同一頁之第二入口** —— 失效時仍可由 Edit Profile 進入，影響有限 |
| 039 | 10.3.1 | Low | **P2** | 該頁之內容；失效即內容錯誤，非入口重複 |

**P3 之判給 038 是本批唯二之 P3**（另一為 105，單頁 6 行之版面上限）。
若三條都給 P2，就是把 037 之 Low 換個名字寫一次 —— D-1 之教訓正是那個。

### 3.4 風險④⑤⑥（16 輪 §6.5 之其餘三項）

| # | 事項 | 實際結果 |
|---|---|---|
| ④ | `112-02`／`-03` 與 pilot 之 `112-01` 之列舉完整性 | **三條齊備**（刪除／更新／安裝），tc_title 各帶其動作 token，G5 未觸發。三者之 pre-condition 互斥（未裝／已裝），不重複覆蓋 |
| ⑤ | `PROF-085` 之 must_carry 兩條是否真的注入 | **是** —— `--selfcheck` 第 2 項顯示 9.1 → 2 條（9.1 之掉句 ＋ p14 之 Table EDPR1 列項）。**T-1／T-2 於本批首次被實際注入**，其覆蓋自此成立 |
| ⑥ | ch12–14（Valet 31 leaf）未納入 | 維持未納入，另成一批 |

### 3.5 本批之 priority 分布與其變化

| | pilot（16）| 本批（28）| 合計（44）|
|---|---|---|---|
| P0 | 6 | 3（095／099／101）| **9** |
| P1 | 6 | 9 | **15** |
| P2 | 4 | 14 | **18** |
| P3 | 0 | **2**（105／107）| **2** |

**P0 三條之依據**：`095`（記憶座椅連結＝PLP 3.5 之偏好，規則本身）、
`099`（座椅位置之儲存與其歸屬）、`101`（**刪除前之確認 —— 資料遺失風險之防線本身**）。

---

## 4. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **R-U5 之 rubric 沒有安全帶** | **待裁** | `PROF-089`（行車中限制）失效之後果是**行車中可操作受限功能** —— 那既非「核心能力被繞過」也非「輸入體驗降級」，D-UP16-01 之兩分法接不住它。本輪判 P1（非主路徑分支），**但那是就近歸類，不是判準給的答案** |
| 2 | **28 條之 ER 出處未做逐句對照** | note | 作業 B 只涵蓋 pilot 16 條。本批 28 條之對照**未做** —— 若該表是覆核之必要輸入，本批也該有一份 |
| 3 | **`PROF-085` 之列項順序取自 p14 之 Table EDPR1** | note | 該表之**順序**由文字層之出現次序推得（p14 文字層依版面由上而下）。**未以 `render_spec_region.py` 之座標複驗** —— 本輪工具只驗了 CPA2，未驗 EDPR1 |
| 4 | **`PROF-103` 之 ER 為二擇一** | note | 條文寫「“User 1” **或**最後已知 profile」，ER 照錄其二擇一（§8.4.1）。**這樣的 ER 無法判 FAIL** —— 只要其中之一成立就通過。要收斂須先問清楚哪一個 |
| 5 | **`PROF-110` 之 App 內行為以 `etc.` 帶過** | note | 條文為 `connect to an online account, save and download from account, etc.` —— ER 只驗其開啟。**`etc.` 之內容無可驗之明文** |
| 6 | **9.5.x 之座椅編號（seat 1／seat 2）為測試設置，非 spec 值** | note | 條文只說「memory seat position」，未給編號。ER 用 seat 1／2 是為了可執行，**其具體編號無 spec 依據**（同 17(B) §3.1 之 `ignition cycle` 形態）|
| 7 | **本批未含 §7 之其他負向候選** | note | 13 輪 §5.4 列三個候選，本批只補了 `PROF-111`；`PROF-021-01`（刪除後按鈕回復）與 `PROF-053`（有連網 → 登入畫面）仍未配對 |
| 8 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01、A-UP10（ACCEPTED）| 承前 | 擋 Phase 6 寫回，不擋本批 |

**本輪之自我更正一項**：`remarks` 內寫出被禁用之 label 字面值（TC-017／023）——
由 `lint_variant_labels` 擋下，非我自查發現。

---

## 5. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/render_spec_region.py`（J-2；含回歸與對照向）| 否 |
| 2 | **檔案新建** | `scripts/gen_batch01.py`（第一批之單一來源）| 否 |
| 3 | **檔案新建** | `data/batch01_sample.tsv`（27 leaf）| 否 |
| 4 | **檔案新建 ×28** | `generated/`（017–044，含 `SWE1-HMI-PROF-111-neg.json`）| 否 |
| 5 | 檔案編輯 | `scripts/gen_pilot.py`（作業 B 之發現：補列 `5.1.1`）| 否 |
| 6 | 檔案編輯 | `scripts/lint_tcs.py`（tc_id 範圍改取最小最大，不取檔案順序）| 否 |
| 7 | 檔案追加 | `DECISIONS.md`（**D-UP17-01**）| 否 |
| 8 | **檔案編輯** | `framework.md`（新增 **§4.1** 覆蓋率判準）| 否 |
| 9 | 檔案新建 | `docs/upstream/17_er_provenance.md`、`docs/upstream/17_batch01.md` | 否 |
| 10 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 11 | 程式執行 | 生成 ×2、`lint_tcs`（語料＋self-test）、`lint_variant_labels`（反向＋check）、`--selfcheck`、`render_spec_region --regression` | 否 |
| 12 | **唯讀** | `fitz` 讀 spec PDF p16–p18 | 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` 皆無，**唯讀之 `git status` 亦未跑**。

**未動**：工作簿（**未寫回**，R-U14）、`inputs/`、`forms/`、`feature.yaml`、
`RULINGS.md`（本包無裁決條文）、`ANOMALIES.md`、`BASELINE.sha256`、`.gitignore`、
`data/` 之其餘檔、**他 feature 之任何檔**、`docs/fw036/` 之任何檔。

**pilot 之 16 條產物**：除 `SWE1-HMI-PROF-070.json`（補列 5.1.1）外未變動。

---

## 6. 第一批 28 條 TC 全文

> `test_group` 皆為 `User Profiles`；`test_item` 依 R-U6 等同 `tc_title`；
> `functional_safety` 全批 `NA`；`estimated_test_time` 全批留空；`split_flag` 全批 false。
> 檔案路徑：`features/user_profiles/generated/<req_id>.json`
> （負向配對為 `SWE1-HMI-PROF-111-neg.json`）。

### NR1L-UserProfiles-017 — SWE1-HMI-PROF-085（9.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit Profile tab lists options in Table EDPR1 order |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A Driver Profile is active and setup assistant is not completed for it |
| input_test_data | NA |
| test_procedure | 1. Open the Profile section and select the “Edit Profile” tab<br>2. Read the option list and check that the items appear in the Table EDPR1 order |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. The options are listed in the Table EDPR1 order: Resume Setup (only if not complete), Edit Name, Edit Avatar, Connected Account, Memory Seat (if applicable), Welcome Pop Up, Delete Profile, What is linked to my Profile?, Tutorials, More Settings; and a circled number 1 is shown next to Resume Tutorials |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1 |
| priority | **P2** — Edit Profile 清單之順序；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | R1 High：清單第四項之 label 依 spec 9.3.2 之變體覆寫，採 Connected Account（R-U35 (c)）。列項順序取自 must_carry 之 Table EDPR1（PDF p14） |

**reasoning**：驗證目標：9.1（EDPR1）—— Edit Profile 分頁之選項須依 Table EDPR1 之順序列出，且 Resume Tutorials 旁有圈號 1。關鍵情境條件：圈號 1 之顯示以「setup assistant 未完成」為前提，故列 pre-condition；列項字串取自補句表之 Table EDPR1（PDF p14），非自擬。為什麼這樣切：本 leaf 之單位為「順序」，各項之連結去向（Connected Account → app、More Settings → My Profile）屬 9.1 之其他斷言與 11.3.1／9.8 之 leaf，本 TC 不代測。刻意略過：**本 TC 以 R1 High 為條件**，故 label 用 Connected Account；非 R1 High 車上該項為 Stellantis Account，其對照未生成（取樣單位為 leaf）。

### NR1L-UserProfiles-018 — SWE1-HMI-PROF-086（9.1.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Username and avatar hidden left of the 8.4-inch edit list |
| pre_conditions | 1. The vehicle has an 8.4-inch screen<br>2. A Driver Profile with a username is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the screen and check that no username or avatar is shown left of the list |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No username or avatar is shown to the left of the Edit Profile List, and the username appears in the Edit Username line as “Edit username: [username]” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1.1 |
| priority | **P2** — 8.4 吋版面之呈現差異 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.1.1（EDPR1.1）—— 8.4 吋螢幕不在清單左側顯示 username 與 avatar，改於 Edit Username 該行顯示。關鍵情境條件：螢幕尺寸為條件本身，列 pre-condition；兩個觀察點（左側不顯示／該行顯示）為同一條件之兩個結果，併為一條 ER。為什麼這樣切：其他尺寸之版面屬 9.1 之常態，本 leaf 只管 8.4 吋之差異。

### NR1L-UserProfiles-019 — SWE1-HMI-PROF-087（9.1.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat status hidden when seats are not equipped |
| pre_conditions | 1. The vehicle is not equipped with memory seats<br>2. A Driver Profile is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that no memory seat status is shown |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No memory seat status is available in the list |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1.2 |
| priority | **P2** — 未配備時之呈現隱藏 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.1.2（EDPR1.2）—— 未配備記憶座椅之車輛不顯示記憶座椅狀態。關鍵情境條件：車輛配置為條件本身，列 pre-condition。為什麼這樣切：已配備車輛之記憶座椅狀態與其操作屬 9.5.x 之 leaf，本 TC 只驗其不存在。

### NR1L-UserProfiles-020 — SWE1-HMI-PROF-088（9.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected Account hidden for unsupported regions |
| pre_conditions | 1. The vehicle is in a region without the brand app<br>2. A Driver Profile is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that no Connected Account button or Connected Profile info is shown |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No Connected Profile options or info and no Connected Account button are shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.2 |
| priority | **P1** — 區域／車型配置之非主路徑分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | R1 High：label 為 Connected Account（spec 本節寫 Stellantis Connected Account）—— R-U35 (c) |

**reasoning**：驗證目標：9.2（EDPR2）—— 無 <Brand> app 之區域不顯示 Connected Profile 之選項／資訊與 Connected Account 按鈕。關鍵情境條件：條文有兩個獨立條件（區域無 app／車輛不支援），本 TC 取「區域」一側；車輛不支援一側之條件相同而觸發不同，由 11.3（CPA1）之 leaf 承擔（其文為 do not show if the vehicle does not support connectivity）。為什麼這樣切：兩個條件若併於一條 TC，失敗時分不出是哪一個條件沒生效。

### NR1L-UserProfiles-021 — SWE1-HMI-PROF-089（9.3 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit options greyed out while the vehicle is in motion |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Read the option list and record which items are selectable<br>2. Bring the vehicle into motion<br>3. Read the option list and check that the restricted items are greyed out |
| expected_result | 1. The options recorded in step 1 are selectable while stationary<br>2. The vehicle is in motion<br>3. Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info of what is linked to a Profile are greyed out and cannot be selected |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3 |
| priority | **P1** — 行車中之限制分支 —— **rubric 無安全帶，見上繳 17 §3** |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：9.3（EDPR3）—— 行車中六個項目變灰且不可選取。關鍵情境條件：判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換），故以步驟 1 之靜止狀態為基準線（§5.6）。為什麼這樣切：六個項目為同一觸發之同一結果，依 §5.7 併為一條 ER；選取時之 bonk 與訊息屬 9.3.1、進行中被中斷屬 9.3.2，兩者觸發不同。

### NR1L-UserProfiles-022 — SWE1-HMI-PROF-090（9.3.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Bonk tone and message when a restricted item is selected |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is in motion on a test track |
| input_test_data | NA |
| test_procedure | 1. Select the greyed-out “Delete Profile” item<br>2. Read the screen and check that the bonk tone and the message are presented |
| expected_result | 1. The selection is not accepted<br>2. A bonk tone is played and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3 |
| priority | **P2** — 限制之回饋（音效與訊息）呈現 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：9.3.1（EDPR3.1）—— 行車中選取受限項目時播放 bonk 音並顯示指定訊息。關鍵情境條件：受測動作為對已變灰項目之選取，屬不被允許之操作（§12 首匹配 → 負向測試）；受限項目之清單出自 9.3，故併列該節。為什麼這樣切：本 leaf 之單位為「回饋」，項目是否變灰屬 9.3、進行中被中斷屬 9.3.2。

### NR1L-UserProfiles-023 — SWE1-HMI-PROF-091-02（9.3.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Bonk tone and message accompany the interruption in motion |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and start editing the Profile username<br>2. Bring the vehicle into motion<br>3. Read the screen and check that the bonk tone and the message are presented |
| expected_result | 1. The username editing page is displayed<br>2. The vehicle is in motion and the task is interrupted<br>3. A bonk tone is played and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1 |
| priority | **P2** — 同上；本條之單位為回饋本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | R1 High：label 依 9.3.2 之變體覆寫採 Connected Account（R-U35 (c)）。sibling 軸：本條驗**回饋**，091-01 驗**返回前一頁** —— 同一觸發之兩個結果，分屬兩個 037 leaf（§8.2.1） |

**reasoning**：驗證目標：9.3.2（EDPR3.2）之回饋部分 —— 進行中被中斷時播 bonk 並顯示訊息。關鍵情境條件：同 091-01 之狀態轉換（靜止→行進），差別在觀察點：091-01 觀察頁面返回，本條觀察音效與訊息。為什麼這樣切：037 為 9.3.2 切出兩個 leaf，一葉一 TC（§8.2.1）；訊息字串出自 9.3.1，故併列該節。

### NR1L-UserProfiles-024 — SWE1-HMI-PROF-092（9.4 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar selection screen opens from avatar or Change Avatar |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press anywhere on the avatar<br>2. Read the screen and check that the avatar selection screen is displayed<br>3. Return to the “Edit Profile” tab<br>4. Press anywhere on the “Change Avatar” line and check that the same screen is displayed |
| expected_result | 1. The avatar is pressed<br>2. The avatar selection screen is displayed<br>3. The “Edit Profile” tab is displayed<br>4. The avatar selection screen is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4 |
| priority | **P2** — avatar 選擇畫面之開啟 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4（EDPR5）—— 按 avatar 或按「Change Avatar」該行皆開啟 avatar 選擇畫面。關鍵情境條件：條文明列兩個入口，兩者為**不同觸發同一結果**，故於一條 TC 內各驗一次（非拆兩條 —— 拆了會產生兩條除入口外全同之 TC）。為什麼這樣切：該畫面之內容屬 9.4.1、離開不存之行為屬 9.4.2。

### NR1L-UserProfiles-025 — SWE1-HMI-PROF-093（9.4.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Current avatar highlighted among the available avatars |
| pre_conditions | 1. A Driver Profile with a selected avatar is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen from the “Edit Profile” tab<br>2. Read the screen and check that the current avatar is highlighted |
| expected_result | 1. The avatar selection screen is displayed<br>2. The currently selected avatar is highlighted and all other available avatars are offered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4.1 |
| priority | **P2** — avatar 畫面之呈現細節 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4.1（EDPR5.1）—— 選擇畫面須標示目前 avatar，並提供其餘可用 avatar。關鍵情境條件：pre-condition 要求該 profile 已有 avatar，否則「目前之 avatar」無從觀察。為什麼這樣切：畫面之開啟屬 9.4，本 leaf 只管其內容。

### NR1L-UserProfiles-026 — SWE1-HMI-PROF-094（9.4.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar unchanged when the screen is exited without saving |
| pre_conditions | 1. A Driver Profile with a selected avatar is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen and record the current avatar<br>2. Select a different avatar without saving<br>3. Exit the screen without saving<br>4. Read the “Edit Profile” tab and check that the avatar recorded in step 1 is still in use |
| expected_result | 1. The avatar selection screen is displayed and the current avatar is recorded<br>2. The different avatar is selected on the screen<br>3. The screen is exited without saving<br>4. The avatar recorded in step 1 is still in use |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4.2 |
| priority | **P1** — 未存即離開不得改動 avatar —— **失效即使用者資料被意外變更** |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4.2（EDPR5.2）—— 未儲存即離開不得造成 avatar 變更。關鍵情境條件：須先在畫面上選了別的 avatar 才有「未存即離開」可言，故步驟 2 為必要之設置，非多餘。為什麼這樣切：儲存後之變更屬 9.4 之正向路徑，本 leaf 只管未儲存之路徑；失效之後果是使用者資料被意外變更，故判 P1 而非 P2。

### NR1L-UserProfiles-027 — SWE1-HMI-PROF-095（9.5 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Active Profile linked to the swapped memory seat position |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Two Driver Profiles exist and Profile A is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and read the memory seat linked to Profile A<br>2. Swap the memory seat preference to another position<br>3. Read the memory seat status and check that Profile A is linked to the new position |
| expected_result | 1. The memory seat currently linked to Profile A is recorded<br>2. The memory seat preference is swapped<br>3. Profile A is linked to the newly selected memory seat position |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.5 |
| priority | **P0** — 記憶座椅連結＝PLP 3.5 之偏好；本條為其規則本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | sibling 軸（9.5.x 四條）：本條＝**交換之通則**；9.5.1＝前置**已**連結之分支；9.5.2＝前置**未**連結之分支；9.5.3＝「none」選項之可用性 |

**reasoning**：驗證目標：9.5（EDPR6）—— 交換記憶座椅偏好後，現用 profile 連結至該座椅位置，直到下一次變更。關鍵情境條件：判準為連結狀態之轉換（§12 首匹配 → 狀態轉換），以步驟 1 之原連結為基準線（§5.6）。為什麼這樣切：本條為通則，9.5.1／9.5.2 為其依前置狀態分出之兩個分支，037 已為三者各切一 leaf，一葉一 TC（§8.2.1）。

### NR1L-UserProfiles-028 — SWE1-HMI-PROF-096（9.5.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Seat preferences swapped when the active Profile was linked |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Profile A is active and linked to memory seat 1<br>3. Profile B is linked to memory seat 2<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Select memory seat 2 for Profile A<br>3. Read the memory seat status of both Profiles and check that the two preferences are swapped |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. Memory seat 2 is selected for Profile A<br>3. Profile A is linked to memory seat 2 and Profile B is linked to memory seat 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.5.1 |
| priority | **P1** — 同上之分支（前置已連結）—— 依 D-UP16-01，分支歸 P1 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | sibling 軸：前置狀態＝active Profile **已**連結座椅（對照 9.5.2） |

**reasoning**：驗證目標：9.5.1（EDPR6.1）—— 現用 profile 原已連結座椅時，與新座椅之原持有者**互換**。關鍵情境條件：pre-condition 明訂兩個 profile 各有連結，否則「互換」無從成立 —— 這也是本條與 9.5.2 之唯一分野。為什麼這樣切：前置未連結之情形由 9.5.2 承擔，兩者之 pre-condition 互斥，不會重複覆蓋。

### NR1L-UserProfiles-029 — SWE1-HMI-PROF-097（9.5.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Previous Profile unlinked when the active Profile had none |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Profile A is active and is not linked to any memory seat<br>3. Profile B is linked to memory seat 2<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Select memory seat 2 for Profile A<br>3. Read the memory seat status of both Profiles and check that Profile B is no longer linked |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. Memory seat 2 is selected for Profile A<br>3. Profile A is linked to memory seat 2 and Profile B is not linked to any memory seat position |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.5.2 |
| priority | **P1** — 同上之分支（前置未連結） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | sibling 軸：前置狀態＝active Profile **未**連結座椅（對照 9.5.1） |

**reasoning**：驗證目標：9.5.2（EDPR6.2）—— 現用 profile 原無連結時，直接接管該座椅，原持有者變為無連結。關鍵情境條件：pre-condition 明訂 Profile A 無連結 ——此即與 9.5.1 之分野；兩條之其餘設置刻意保持相同，使失敗時可歸因於前置狀態而非別的差異。為什麼這樣切：037 已為兩個前置狀態各切一 leaf。

### NR1L-UserProfiles-030 — SWE1-HMI-PROF-098（9.5.3 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | None option greyed out until Profiles outnumber memory seats |
| pre_conditions | 1. The vehicle is equipped with two memory seats<br>2. Two Driver Profiles exist on the vehicle<br>3. The vehicle is stationary |
| input_test_data | Profile count vs memory seat count: 2 vs 2 (equal) → 3 vs 2 (exceeds) |
| test_procedure | 1. Open the memory seat option list and read the “none” option<br>2. Create a third Driver Profile<br>3. Open the memory seat option list and check that the “none” option is available |
| expected_result | 1. The “none” option is greyed out and not available while two Profiles exist<br>2. The third Driver Profile is created<br>3. The “none” option is available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.5.3 |
| priority | **P2** — 「none」選項之可用性邊界；呈現層 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | （空） |

**reasoning**：驗證目標：9.5.3（EDPR6.3）——「none」在 profile 數超過記憶座椅數之前不可用。關鍵情境條件：以 2 vs 2（相等，仍不可用）與 3 vs 2（超過，可用）構成邊界前後（§5.6），故取邊界值分析；條文之「exceeds」為嚴格大於，相等時仍不可用即為本 TC 之界前基準線。為什麼這樣切：座椅連結之交換規則屬 9.5–9.5.2，本 leaf 只管該選項之可用性。

### NR1L-UserProfiles-031 — SWE1-HMI-PROF-099（9.6 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Saved seat position updates the Profile linked to that seat |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Profile A is active and Profile B is linked to memory seat 2<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Change the seat position<br>2. Save the position to memory seat 2<br>3. Read the popup and check that it names the Profile the seat was saved to |
| expected_result | 1. The seat position is changed<br>2. The position is saved to memory seat 2 and the seat position stored for Profile B is updated<br>3. PU0588 is displayed and informs the user that the seat was saved to Profile B |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.6 |
| priority | **P0** — 座椅位置之儲存與其歸屬 —— 偏好之儲存與回復 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.6（EDPR7）—— 儲存座椅位置會更新**該座椅所連 profile** 之位置；若該座椅非現用 profile 所連，儲存時顯示 PU0588 告知存到誰。關鍵情境條件：pre-condition 令現用者為 A 而該座椅連 B，否則 PU0588 之觸發條件不成立。為什麼這樣切：兩項為同一觸發（按儲存）之兩個結果，依 §5.7 併為一條 TC。刻意略過：座椅連結之變更屬 9.5.x，本條之連結關係固定不動。

### NR1L-UserProfiles-032 — SWE1-HMI-PROF-100（9.6.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup size defaults to small and can be turned off |
| pre_conditions | 1. A newly created Driver Profile exists and has not had its Welcome Popup size changed<br>2. The vehicle is stationary |
| input_test_data | Welcome Popup size setting: default → Off |
| test_procedure | 1. Open the “Edit Profile” tab and read the Welcome Popup size setting<br>2. Set the Welcome Popup size to Off<br>3. Activate another Profile and then reactivate this Profile<br>4. Read the screen and check that no welcome popup is shown |
| expected_result | 1. The Welcome Popup size setting reads Small<br>2. The Welcome Popup size is set to Off<br>3. The Profile becomes active again<br>4. No welcome popup is shown for that Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.6.1 |
| priority | **P2** — welcome popup 尺寸之預設值 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.6.1（EDPR7.1）—— 尺寸設定預設為 small；設為 off 後該 profile 成為現用時不顯示 welcome popup。關鍵情境條件：預設值須在未被改過之 profile 上讀，故 pre-condition 明訂為新建且未調整過。為什麼這樣切：兩項為同一設定之兩個面向（預設值與關閉後之效果），且第二項須先讀第一項才有基準線。刻意略過：large 為全螢幕 popup 之呈現屬 7.2.1 之 leaf。

### NR1L-UserProfiles-033 — SWE1-HMI-PROF-101（9.7 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Verification popup shown before a Profile is deleted |
| pre_conditions | 1. Two Driver Profiles exist and Profile A is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and select “Delete Profile”<br>2. Read the screen and check that a verification popup is displayed before any deletion |
| expected_result | 1. “Delete Profile” is selected<br>2. A verification popup asking to confirm the delete is displayed and the Profile is not yet deleted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.7 |
| priority | **P0** — 刪除前之確認 —— **資料遺失風險之防線本身** |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.7（EDPR8）—— 選擇刪除後、實際刪除前須有確認 popup。關鍵情境條件：ER 明寫「尚未刪除」—— 若只驗 popup 出現而不驗資料仍在，一個「先刪再問」之實作也會通過（§7 false pass）。為什麼這樣切：刪除後之導覽屬 9.7.1、刪除後之 active profile 屬 9.7.2；本條為資料遺失風險之防線本身，故判 P0。

### NR1L-UserProfiles-034 — SWE1-HMI-PROF-102（9.7.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | All Profiles tab shown after a Profile is deleted |
| pre_conditions | 1. Two Driver Profiles exist and Profile A is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and delete Profile A<br>2. Confirm the deletion in the verification popup<br>3. Read the screen and check that the “All Profiles” tab is displayed |
| expected_result | 1. The deletion of Profile A is started<br>2. The deletion is confirmed<br>3. The “All Profiles” tab is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.7.1 |
| priority | **P2** — 刪除後之導覽落點 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.7.1（EDPR8.1）—— 自 Edit Profile 分頁刪除 profile 後回到 All Profiles 分頁。關鍵情境條件：須先通過 9.7 之確認 popup 才會真的刪除，故確認列為步驟 2 而非略過。為什麼這樣切：哪一個 profile 成為現用屬 9.7.2，本條只管導覽落點。

### NR1L-UserProfiles-035 — SWE1-HMI-PROF-103（9.7.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | User 1 or the last known Profile becomes active after deletion |
| pre_conditions | 1. Three Driver Profiles exist and Profile A is active<br>2. Profile A is not linked to any memory seat<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record which Profile was active before Profile A<br>2. Delete Profile A and confirm the deletion<br>3. Read the Profile List and check which Profile is active |
| expected_result | 1. The Profile active before Profile A is recorded<br>2. Profile A is deleted<br>3. “User 1” or the Profile recorded in step 1 is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.7.2 |
| priority | **P1** — 刪除後之 active profile 接續；失效即無現用 profile |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.7.2（EDPR8.2）—— 刪除未連結記憶座椅之 profile 後，「User 1」或前一個已知 profile 成為現用。關鍵情境條件：pre-condition 明訂被刪者未連結座椅 ——已連結者之行為條文未述，不在本 TC。為什麼這樣切：條文以「或」給出兩個可接受結果，ER 照錄其二擇一，不自行選定其一（§8.4.1）。

### NR1L-UserProfiles-036 — SWE1-HMI-PROF-105（9.9 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit Profile tab shows at most six lines per page |
| pre_conditions | 1. A Driver Profile is active with all optional items available<br>2. The vehicle is stationary |
| input_test_data | Line count per page: 6 (limit) |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Count the information lines shown and check that no more than six are on the page |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. At most six lines of information are shown on the page |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.9 |
| priority | **P3** — 單頁最多 6 行 —— 版面上限，失效僅影響該頁可讀性 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | （空） |

**reasoning**：驗證目標：9.9（EDPR10）—— Edit Profile 分頁每頁最多 6 行資訊。關鍵情境條件：須在選項最多之情況下才驗得到上限，故 pre-condition 要求各選用項目皆可用。為什麼這樣切：清單之順序屬 9.1，本 leaf 只管每頁行數之上限。

### NR1L-UserProfiles-037 — SWE1-HMI-PROF-106（10.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile linked info page opens from the info line |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the “What is linked to my Profile” line<br>2. Read the screen and check that the linked info page is displayed |
| expected_result | 1. The “What is linked to my Profile” line is pressed<br>2. A page of general info of what is linked to a Driver Profile is displayed and no “Memory Seat” section is shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_10.2 |
| priority | **P2** — linked-info 頁之開啟（**037 先驗 Low，本判為 P2**） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：10.2（PRINFO1）—— 按該行（含「i」圖示）開啟 linked-info 頁，且該頁移除「Memory Seat」段。關鍵情境條件：條文之 Remove “Memory Seat” section for all vehicles 為無條件要求，故列為 ER 之一部分而非另條。為什麼這樣切：該頁之文字內容屬 10.3.1、All Profiles 分頁之入口屬 10.3。刻意略過：條文之「see example above」指頁內示意圖，依 R-U51 之口徑（指涉所指之物）不併列 PLP 表。

### NR1L-UserProfiles-038 — SWE1-HMI-PROF-107（10.3 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Info button on the All Profiles tab opens the same page |
| pre_conditions | 1. A Driver Profile is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the info button on the “Edit Profile” tab<br>2. Record the page shown<br>3. Open the “All Profiles” tab<br>4. Press the info button and check that the page recorded in step 2 is displayed |
| expected_result | 1. The linked info page is displayed<br>2. The page is recorded<br>3. The “All Profiles” tab is displayed with an info button<br>4. The same page as recorded in step 2 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_10.3<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_10.2 |
| priority | **P3** — 同一頁之**第二入口**；失效時仍可由 Edit Profile 進入 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：10.3（PRINFO2）—— All Profiles 分頁亦有資訊按鈕，且顯示與 Edit Profile 分頁相同之頁面。關鍵情境條件：「相同」須以比對驗之，故步驟 1 先記錄另一入口之頁面。為什麼這樣切：該頁之內容屬 10.3.1；本條之單位是「第二入口與其同一性」，故判 P3 —— 失效時仍可由 Edit Profile 進入。

### NR1L-UserProfiles-039 — SWE1-HMI-PROF-108（10.3.1 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Driver Profile info page shows the intro text and examples |
| pre_conditions | 1. The vehicle is equipped with Navigation<br>2. A Driver Profile is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the Driver Profile info page<br>2. Read the page and check that the intro text and the applicable examples are shown |
| expected_result | 1. The Driver Profile Info Page is displayed<br>2. The page reads “Your Driver Profile will remember your personal preferences for many of the features you use in your vehicle everyday. Below are some examples.” followed by the applicable examples, including the Navigation examples |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_10.3.1 |
| priority | **P2** — linked-info 頁之內容（**037 先驗 Low，本判為 P2**） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之「the info in the chart above」指**頁內之 chart**（R-U51 口徑，D-UP12-02），非 PLP 表；Navigation 之有無為條文明列之適用條件，故列 pre-condition |

**reasoning**：驗證目標：10.3.1（PRINFO2.1）—— 資訊頁之引言字串與其後之適用範例。關鍵情境條件：條文明言「若車輛無 Navigation 則不顯示 Navigation 範例」，故 pre-condition 指定為有 Navigation 之車，使該範例確實可觀察。為什麼這樣切：R1 High 之 Connected Account 類別描述為變體覆寫，屬同節之另一斷言，未併入本 TC。刻意略過：無 Navigation 車輛之對照未生成 —— 取樣單位為 leaf（§8.4.2）。

### NR1L-UserProfiles-040 — SWE1-HMI-PROF-109（11.3 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected Account line shown when the vehicle has connectivity |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. A Driver Profile is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that the Connected Account line item is displayed |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. The Connected Account line item is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.3 |
| priority | **P1** — 連網配置之非主路徑分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 不支援連網之對照（條文第二句）屬同節之反面，其覆蓋由 9.2（EDPR2）之 leaf 承擔 |

**reasoning**：驗證目標：11.3（CPA1）—— 具連網能力之車輛，Edit Profile 分頁一律顯示 Connected Account 項目。關鍵情境條件：車輛配置為條件本身，列 pre-condition。為什麼這樣切：條文另有「不支援則不顯示」之反面，其形態與 9.2 之區域／車型隱藏相同，由該 leaf 承擔，本條不重複。

### NR1L-UserProfiles-041 — SWE1-HMI-PROF-110（11.3.1 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected Account opens the Connected Account App |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. A Driver Profile is active and the “Edit Profile” tab is displayed<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Connected Account line item<br>2. Read the screen and check that the Connected Account App is displayed |
| expected_result | 1. The Connected Account line item is pressed<br>2. The Connected Account App is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.3.1 |
| priority | **P2** — Connected Account 之導向 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：11.3.1（CPA1.2）—— 按下 Connected Account 進入其 App。關鍵情境條件：需具連網能力之車輛，否則該項目不存在（11.3）。為什麼這樣切：該 App 內之連線／存取行為條文以 etc. 帶過，無可驗之明文，故 ER 只驗其開啟（§8.4.1 不造值）。

### NR1L-UserProfiles-042 — SWE1-HMI-PROF-112-02（11.5 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | App Store update applies to every user with it installed |
| pre_conditions | 1. Two Driver Profiles exist, each with its own Connected Account<br>2. The same App Store app is installed locally for both Profiles<br>3. An update for that app is available |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A and record the app version<br>2. Update the app from Driver Profile A<br>3. Activate Driver Profile B<br>4. Read the app version and check that it matches the updated version |
| expected_result | 1. The app version in Driver Profile A is recorded<br>2. The app is updated for Driver Profile A<br>3. Driver Profile B is active<br>4. The app in Driver Profile B is at the updated version |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.5 |
| priority | **P1** — app 更新之範圍；跨使用者之分支 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| remarks | sibling 軸（11.5 三條）：刪除＝只對執行者（112-01）／更新＝對全部已安裝者（本條）／安裝＝只對安裝者（112-03） |

**reasoning**：驗證目標：11.5（CPA3）第二句 —— app 更新對所有本機已安裝之使用者生效。關鍵情境條件：兩個 profile 皆須先裝有該 app，否則「對全部生效」無從觀察。為什麼這樣切：037 為 11.5 切出三個 leaf（刪除／更新／安裝），三者觸發不同，一葉一 TC（§8.2.1）；三條合起來即該列舉之完整覆蓋（§7）。

### NR1L-UserProfiles-043 — SWE1-HMI-PROF-112-03（11.5 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Installed App Store app appears only in the installer app tray |
| pre_conditions | 1. Two Driver Profiles exist, each with its own Connected Account<br>2. The App Store app under test is not installed for either Profile |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A and install the app from the App Store<br>2. Read the app tray of Driver Profile A<br>3. Activate Driver Profile B<br>4. Open the app tray and check that the app is not present |
| expected_result | 1. The app is installed for Driver Profile A<br>2. The app is present in Driver Profile A’s app tray<br>3. Driver Profile B is active<br>4. The app is not present in Driver Profile B’s app tray |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.5 |
| priority | **P1** — app 安裝之範圍；跨使用者之分支 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| remarks | sibling 軸：安裝＝只對安裝者（對照 112-01 刪除、112-02 更新） |

**reasoning**：驗證目標：11.5（CPA3）第三句 —— 安裝之 app 只出現在安裝者之 app tray。關鍵情境條件：pre-condition 明訂兩者皆未安裝，否則 B 之 app tray 有該 app 時分不出是本次安裝造成還是原本就有。為什麼這樣切：正反兩個觀察點（A 有、B 無）為同一觸發之兩個結果，併於一條 TC（§5.7）。

### NR1L-UserProfiles-044 — SWE1-HMI-PROF-111（11.4 / Connected Account）　**§7 負向配對**

| 欄 | 值 |
|---|---|
| tc_title / test_item | No info button next to Connected Account on R1 High |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A Driver Profile is active and the “Edit Profile” tab is available |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the Connected Account line and check that no info button is shown next to it |
| expected_result | 1. The “Edit Profile” tab is displayed with the Connected Account line<br>2. No info button is shown next to the Connected Account button, and the Local vs Connected Profile screen cannot be opened |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.4 |
| priority | **P2** — R1 High 變體之呈現（資訊按鈕不存在） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | §7 之負向配對：正向為 NR1L-UserProfiles-013（非 R1 High）。依據為 Table CPA2 之表級註記「**R1 High Only: This table (Table CPA2) is not applicable. There will be no info button showed nextto the Connected Account button.」（PDF p17） |

**reasoning**：驗證目標：11.4 之 R1 High 變體 —— 該表不適用，且 Connected Account 旁沒有資訊按鈕。關鍵情境條件：變體為條件本身（§8.7.3），列 pre-condition。為什麼這樣切：本條與 TC-013 構成 §7 之列舉配對 —— TC-013 驗「非 R1 High 有該畫面與其四列」，本條驗「R1 High 沒有入口」。**只有正向會使一個「永遠顯示該畫面」之實作通過**。刻意略過：R1 High 之其他變體差異（如 9.3.2 之 label 覆寫）屬各自之 leaf。

