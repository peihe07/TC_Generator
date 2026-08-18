# 上繳 16 — pilot 覆核（第二輪）之修正與第一批取樣清單

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`16_pilot_review2.md`（**無裁決條文**）
- **本輪未執行任何 git**（R-G5／R-G12）；**未寫回工作簿**（R-U14）
- **未生成第一批** —— 取樣清單先回報（作業 6）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 16 條，**違規 0** |
| `lint_tcs.py --self-test` | **37 / 37** |
| `lint_variant_labels.py` 反向 | **9 / 9** |
| `lint_variant_labels.py --check` | 16 條，**違規 0** |
| `build_batch_context.py --selfcheck` | **8 / 8** |
| tamper `drop`／`add`／`misplace` | **三向皆紅** |

---

## 1. F-1 —— TC-013 移除 `11.5`，並全批複核引用來源

### 1.1 修正

| | 修正前 | 修正後 |
|---|---|---|
| `specification_reference` | `…_11.4; …_11.5` | **`…_11.4`** |

`REF_EXTRA` 之該項已刪除，原因逐字寫在程式註解裡：
**頁面共置不是章節歸屬**（§10.7）。
`must_carry` 之 `p17 → ["11.4", "11.5"]` **不動** —— 分析層之判定正確，
那管的是 context 注入，與追溯欄是兩個不同的問題。

### 1.2 全批複核 —— 16 條之每一個引用節次

| 機制 | 條數 | 逐條核對 |
|---|---|---|
| **本節**（該 leaf 自己的 section）| 16 | 全部為受測對象 ✓ |
| **`REF_EXTRA`**（具名增列）| 2 | 見下 |
| **PLP `3.x` 併列**（R-U46）| 2 | 見下 |
| **must_carry 多節掛回而入者** | **0**（F-1 修正後）| —— |

**`REF_EXTRA` 兩條，皆為「其字面值出現在本 TC 之 ER 裡」**：

| tc_id | 增列 | 該節提供什麼 | 是否被驗證 |
|---|---|---|---|
| TC-003 | `5.1.2` | PRACC7.2 之圖示與字串「This icon is associated to settings…」| **ER3 逐字檢查該字串** ✓ |
| TC-011 | `9.3.1` | 訊息字串「Function not available while vehicle in Motion.」| **ER3 逐字檢查該字串** ✓ |

**PLP `3.x` 併列兩條 —— 嚴格讀會有殘留，具名待裁**：

| tc_id | 本節 | 併列 | 實際受測之 PLP 列 | 未受測之列 |
|---|---|---|---|---|
| TC-001 | 4.1 | 3.1–3.5 | 3.1／3.2／3.4（input_test_data 具名）| **3.3、3.5** |
| TC-004 | 5.9 | 3.1–3.5 | 3.5（記憶座椅項）| **3.1–3.4** |

**兩種讀法，答案不同**：

- **嚴格讀（F-1 之字面）**：「真的被該 TC 驗證或倚為 setup」——
  則 TC-001 應只列 3.1／3.2／3.4，TC-004 應只列 3.5。
- **條文對象讀**：4.1 之文為「store **all** profile-linked preferences
  **listed in PLP table**」、5.9 之文為「not required to save **any** of the
  Driver Profile linked preferences」——
  **該需求的對象本來就是整張表**，TC 是對它抽樣。
  依此，五節皆為追溯之正當對象，而「只驗了其中幾列」是**覆蓋深度**問題
  （即 F-4 之同一件事），不是**引用正確性**問題。

**執行層採後者，未改**，理由：若改採前者，`specification_reference`
會隨「這次抽了哪幾列」而變 —— **同一條需求的追溯欄會因抽樣而不同**，
那不是追溯。**惟此與 F-1 之字面有出入，故不自裁定案，列此待覆核。**

---

## 2. F-2 —— 抽圖判讀 Table CPA2 之欄別：**判讀成功**

### 2.1 嘗試方法（逐步記錄）

| 步 | 方法 | 結果 |
|---|---|---|
| 1 | `fitz` 取 p17 之內嵌圖：`page.get_images(full=True)` | **4 張**（558×346、583×521、61×64 ×2）|
| 2 | 讀 583×521 之 HMI 示意圖 | **可判讀**，但表格區**被畫面捲軸裁掉**，只見 4 列且第 5 列不可見 |
| 3 | 讀 558×346 | 為 Edit Profile 分頁截圖（資訊圖示之入口），佐證 TC-013 步驟 1 |
| 4 | 檢查 p16／p18 有無其他狀態圖 | 無捲動後之版本 |
| 5 | **改以整頁向量重繪** `page.get_pixmap(matrix=Matrix(3,3))` | **關鍵一步** —— Table CPA2 **不是圖，是 PDF 之向量表格**；文字層把它攤平，但版面仍在 |
| 6 | 裁切表格區以 6 倍重繪，逐格判讀勾記 | **四列之欄別全部判定** |

**「圖抽不出」與「表被攤平」是兩件事** —— 05 輪證的是前者可解；
本輪真正要解的是後者，而其解法不是抽圖，是**重繪版面**。

### 2.2 判讀結果（Table CPA2，**四列非五列**）

| 列 | Connected ~~FCA~~ Account | Local Profile |
|---|---|---|
| **Personalization**（Presets, Menu Bar Order, App Drawer Favorites, and more）| **✓** | **✓** |
| **App Store Download** | **✓** | （無標記）|
| **Marketplace**（Access to Marketplace）| **✓** | （無標記）|
| **\*\*\*\*Connected Navigation**（Personalized Favorites, Recents, and Predictive Navigation）| **✓** | （無標記）|

**表頭之 `FCA` 有刪除線**，改為 `Connected Account` —— 與 §8.7.3 之
label 覆寫方向一致（HMI 示意圖仍是舊名 `FCA account`，**字面值以條文為準**）。

### 2.3 **三項連帶更正**（讀圖才看得到）

1. **「Connected Profile App (See Connected Personal Account HMI)」不是表列。**
   它是頁面右上**指向截圖之註解框**（紫色箭頭指向 Edit Profile 之 `>` 圖示）。
   14 輪之 ER 把它列為第 e 列 —— **錯，已移除**。
   成因：文字層把註解框與表格文字**連在一起**輸出，看不出版面關係。
2. **中國市場之排除是「列級」，不是「表級」。**
   `****For China market only: do not show this content` 之 `****` 標記
   掛在 **Connected Navigation 那一列**（表下之 `****` 註腳與該列之
   `****` 前綴對應），非整張表。
   14 輪把它當表級而下了整條 TC 之 pre-condition —— **範圍過寬**。
   本輪保留該 pre-condition（使「四列俱全」之預期成立），
   **但於 remarks 載明其真實範圍為該列**。
3. **R1 High 之排除確為表級** —— `**Table CPA2.)` 之 `**` 與
   `**R1 High Only: This table (Table CPA2) is not applicable` 對應。原判正確。

### 2.4 TC-013 之 ER2 修正後

```
The screen titled “What are the benefits of creating an Connected account?”
is displayed with two columns labeled Connected account and Local Profile,
showing “Synchronize your profile between multiple vehicles…” and
“Create a profile specific to this vehicle…”, and the four rows of
Table CPA2 with their column marks:
   a. Personalization (Presets, Menu Bar Order, App Drawer Favorites, and more)
      — marked under **both** Connected Account and Local Profile
   b. App Store Download — marked under Connected Account only
   c. Marketplace (Access to Marketplace) — marked under Connected Account only
   d. Connected Navigation (Personalized Favorites, Recents, and Predictive
      Navigation) — marked under Connected Account only
```

**§8 第 2 項之「永久限制」判定撤回。** 分析層說得對：**能讀而未讀，不是限制。**
我把「文字層還原不了」當成了「讀不到」，而**版面一直都在**。

---

## 3. F-3 —— P0 tie-break 明文化

寫入 `DECISIONS.md` **D-UP16-01**（含四條之逐條對照），
並於 `RULINGS.md` 之 **R-U5 條文末加註**（**條文本身一字未改**，僅附適用釐清）：

```
      —— 適用釐清（F-3，16 包核可；**條文本身未改**）：
      一條 TC 同時落在核心五類與「邊界／非主路徑」兩帶時，
      以失效後果決定 —— 核心能力失效或被繞過 → P0；
      輸入體驗或呈現降級 → P1。逐條依據與其盲區見
      `DECISIONS.md` D-UP16-01。
```

**並聲明其盲區（R-G11）**：「失效後果」無可測形式，須人工判讀。
邊界情形（如：使用者資料因輸入超長而被截斷 —— 是體驗降級還是資料損失？）
**本判準不自動給答案**，遇之逐條判並記於 D-UP16-01。

**現狀不變**：P0×6／P1×6／P2×4。

---

## 4. F-4 —— TC-004 未驗全稱，登記 note

`DECISIONS.md` **D-UP16-02**。要點：這不是「取樣夠不夠」，是
**全稱命題以單例驗證** —— 5.9 說的是「**任何**」，TC-004 只驗了 3.5 一項，
單例通過不能證全稱。真要驗全稱是 PLP 表五列逐項（1 條變 5 條，或 1 條含 5 組資料），
**屬批量規劃，本輪不擴充**（F-4 明文）。

---

## 5. 作業 5 —— 全部 lint 與 selfcheck 之輸出

```
$ python3 scripts/gen_pilot.py
寫出 16 個 leaf 檔，共 16 條 TC → features/user_profiles/generated

$ python3 scripts/lint_tcs.py
掃 16 個 leaf 檔 / 16 條 TC
tc_id 範圍 NR1L-UserProfiles-001 … NR1L-UserProfiles-016
design_method 分布：功能測試×8, 基礎故障注入×1, 情境 / 用例×1, 狀態轉換×1,
                    負向測試×1, 邊界值分析×4
priority 分布：P0×6, P1×6, P2×4
違規 0

$ python3 scripts/lint_tcs.py --self-test
37 / 37 directional cases PASS

$ python3 scripts/lint_variant_labels.py
9 / 9 directional cases PASS

$ python3 scripts/lint_variant_labels.py --check
掃 16 條 TC，違規 0

$ python3 scripts/build_batch_context.py --selfcheck
8 / 8 self-check items PASS

$ … --selfcheck-tamper drop      → <8 / 8 FAIL
$ … --selfcheck-tamper add       → <8 / 8 FAIL
$ … --selfcheck-tamper misplace  → <8 / 8 FAIL
```

---

## 6. 作業 6 —— 第一批正式批次之取樣清單（**先回報，未生成**）

### 6.1 範圍：**ch9 → ch10 → ch11，27 個 leaf**

依 framework Layer 3 之章節連續排序（§4.1.4），自 ch9 起續接 pilot。

### 6.2 批量之理由（具名，四項）

1. **落在 25–35 之建議區間內**：27 個 leaf。
2. **章節連續且不跨斷點**：9 → 10 → 11 為 Layer 3 之連續段。
3. **批次邊界 = 兩個 Test Set 之完成點**（本項為選此範圍之主要理由）：

   | Test Set | 章 | 總 leaf | pilot 已生成 | 本批 | 批後狀態 |
   |---|---|---|---|---|---|
   | **Editing** | 9 ＋ 10 | 25 | 2 | **23** | **100% 完成** |
   | **Connected Account** | 11 | 6 | 2 | **4** | **100% 完成** |

   **一個批次結束時剛好結清兩個 Test Set**，而不是把某個 Test Set 切在半路 ——
   後者會使該 Test Set 之 sibling 一致性（§8.3）要隔批才驗得到。

4. **三項必含全數落在此範圍內**（非為湊而挑）：
   - **T-1（9.1）＋ T-2（p14）** → `PROF-085`（9.1）**一條 leaf 同時覆蓋兩者**
     —— `must_carry_for("9.1")` 現回傳 2 條（9.1 之掉句 ＋ p14 之 Table EDPR1 列項）
   - **`PROF-111` 之 R1 High 反面** → 11.4 在本範圍內
   - 另附帶：`PROF-090`（9.3.1）為 pilot `091-01` 之 sibling、
     `PROF-112-02/03` 為 pilot `112-01` 之 sibling —— **§7 之列舉配對本批內自足**

### 6.3 TC 條數之估計

| 項 | 數 |
|---|---|
| leaf | **27** |
| `PROF-111` 之 R1 High 反面（**非新 leaf**，是既有 leaf 之負向配對）| **＋1** |
| 下限 | **28 條 TC** |
| 可能之上限（§8.2.2：RD sub-id ≠ TC 數；9.5.x 之座椅交換四條、9.7.x 之刪除三條**可能需拆**）| 約 **34 條** |

**估計即估計** —— 實際條數以生成時之切分判斷為準，不預先鎖死。

### 6.4 取樣清單（27 leaf，依章節連續排序）

| # | req_id | sec | Test Set | Sub | 037 Prio | 標題 | 註 |
|---|---|---|---|---|---|---|---|
| 1 | `SWE1-HMI-PROF-085` | 9.1 | Editing | HMI | Medium | Edit Profile Tab Options List Order | **must_carry ×2**／**T-1 ＋ T-2（p14）** |
| 2 | `SWE1-HMI-PROF-086` | 9.1.1 | Editing | HMI | Low | (8.4") Hide Username/Avatar Left of Edit List | — |
| 3 | `SWE1-HMI-PROF-087` | 9.1.2 | Editing | HMI | High | Hide Memory Seat Status if Not Equipped, | — |
| 4 | `SWE1-HMI-PROF-088` | 9.2 | Editing | HMI | High | Hide Connected Account for Unsupported Regions/Vehicles | — |
| 5 | `SWE1-HMI-PROF-089` | 9.3 | Editing | HMI | High | Disable Edit Options While Vehicle in Motion | — |
| 6 | `SWE1-HMI-PROF-090` | 9.3.1 | Editing | HMI | Medium | Bonk Tone & Message for Disabled Functions in Motion | 091-01 之 sibling（§7） |
| 7 | `SWE1-HMI-PROF-091-02` | 9.3.2 | Editing | HMI | Medium | Bonk Tone and Warning for Interrupted Task in Motion | **must_carry ×1** |
| 8 | `SWE1-HMI-PROF-092` | 9.4 | Editing | HMI | Medium | Press Avatar or Change Avatar to Open Selection Screen | — |
| 9 | `SWE1-HMI-PROF-093` | 9.4.1 | Editing | HMI | Low | Highlight Current Avatar and Show Available Options, | — |
| 10 | `SWE1-HMI-PROF-094` | 9.4.2 | Editing | HMI | Medium | Exit without Saving Retains Avatar | — |
| 11 | `SWE1-HMI-PROF-095` | 9.5 | Editing | HMI | High | Swap Seat Preference to Active Profile | — |
| 12 | `SWE1-HMI-PROF-096` | 9.5.1 | Editing | HMI | High | Swap Seat Preference with Previous Profile | — |
| 13 | `SWE1-HMI-PROF-097` | 9.5.2 | Editing | HMI | High | Take New Seat and Unlink Previous Profile | — |
| 14 | `SWE1-HMI-PROF-098` | 9.5.3 | Editing | HMI | Medium | Disable "None" Option Until Profiles Exceed Seats | — |
| 15 | `SWE1-HMI-PROF-099` | 9.6 | Editing | HMI | High | Save Seat Change and Prompt if Not Active Profile | — |
| 16 | `SWE1-HMI-PROF-100` | 9.6.1 | Editing | HMI | Medium | Welcome Popup Size Default and Off Setting | — |
| 17 | `SWE1-HMI-PROF-101` | 9.7 | Editing | HMI | High | Confirmation Popup Before Deleting Profile | — |
| 18 | `SWE1-HMI-PROF-102` | 9.7.1 | Editing | HMI | Medium | Return to All Profiles Tab After Deletion | — |
| 19 | `SWE1-HMI-PROF-103` | 9.7.2 | Editing | HMI | High | Activate User 1 or Last Profile After Deletion | — |
| 20 | `SWE1-HMI-PROF-105` | 9.9 | Editing | HMI | Low | Max 6 Lines of Info on Edit Profile Tab | — |
| 21 | `SWE1-HMI-PROF-106` | 10.2 | Editing | HMI | Low | Display Profile Linked Info Page | R-U51 口徑之受測對象 |
| 22 | `SWE1-HMI-PROF-107` | 10.3 | Editing | HMI | Low | Info Button on All Profiles Tab | — |
| 23 | `SWE1-HMI-PROF-108` | 10.3.1 | Editing | HMI | Low | Driver Profile Linked Info Page Content | R-U51 口徑之受測對象 |
| 24 | `SWE1-HMI-PROF-109` | 11.3 | Connected Account | HMI | Medium | Show Connected Account if Equipped | — |
| 25 | `SWE1-HMI-PROF-110` | 11.3.1 | Connected Account | HMI | Medium | Connected Account Links to Corresponding App | — |
| 26 | `SWE1-HMI-PROF-112-02` | 11.5 | Connected Account | HMI | High | App Update Applies to All Local Users | **must_carry ×2**／112-01 之 sibling（§7） |
| 27 | `SWE1-HMI-PROF-112-03` | 11.5 | Connected Account | HMI | High | App Install Only Shows for Local User | **must_carry ×2**／112-01 之 sibling（§7） |

### 6.5 本批之已知前置與風險（生成前須知）

| # | 事項 | 說明 |
|---|---|---|
| 1 | **`PROF-085`（9.1）之 must_carry 有兩條** | 其一為 9.1 之掉句（Resume Tutorials 之圈號 1），其二為 p14 之 Table EDPR1 列項（含 `“ Stellantis Account”`）。**後者含變體覆寫之字面值** —— R1 High 之 TC 須寫 `Connected Account`，`lint_variant_labels` 會擋 |
| 2 | **`PROF-106`／`PROF-108`（10.2／10.3.1）** | 即 R-U51 判讀口徑之受測對象。其 TC 將**實地檢驗 D-UP12-02 所述之代價** —— PLP 表之覆蓋是否確由此二條之 sibling Req 承擔 |
| 3 | **`PROF-112-02`／`-03`** | 與 pilot 之 `112-01` 同節（11.5），三者構成刪除／更新／安裝之完整列舉。**sibling 之 tc_title 不得雷同**（G5 會擋）|
| 4 | **9.5.x 四條座椅交換** | 語意相近（swap / swap with previous / take new and unlink / disable "None"），**最可能觸發 §8.3 sibling 軸辨識與 G5** |
| 5 | **ch10 僅 3 條且 037 先驗全為 Low** | 依 R-U5 之 rubric 仍須逐條判，**不得因先驗 Low 而機械給 P2**（D-1 之教訓）|
| 6 | **未含 ch12–14（Valet Mode）** | 該 Test Set 有 31 leaf（pilot 已 2），**單獨成批較合適**；本批不切它 |

---

## 7. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **PLP `3.x` 併列之嚴格讀與對象讀** | **待裁** | §1.2：我採「條文對象讀」而未改，但與 F-1 之字面有出入。**若採嚴格讀，TC-001／TC-004 之引用欄要改** |
| 2 | **Table CPA2 之「無標記」與 HMI 之「—」** | note | 印刷表以**空格**表示不適用，HMI 示意圖以 **em dash（—）** 表示。ER 寫「marked under … only」涵蓋兩者，**但未規定測試者該看到空白還是破折號**。實機呈現以 HMI 為準，屬可觀察之細節 |
| 3 | **本輪之判讀依賴 PDF 版面重繪** | note（能力已證，但未成工具）| F-2 之方法有效，**但它是本輪手動跑的**，未落為腳本。日後若再遇攤平之表，得重做一次。**建議落為 `scripts/render_spec_region.py`** |
| 4 | **9.1 之 must_carry 兩條尚未實際注入過任何 TC** | 待第一批 | T-1／T-2 之「覆蓋」在本批生成後才算數；**現在只是排進清單** |
| 5 | **pilot 16 條之 spec 逐字複核仍未完成** | **分析層待辦** | 下放包 §分析層之待辦已自記。**本項不在執行層可自證之範圍** —— 我能證形狀、能證引用、能證字面出自 PDF，**但「這句 ER 是否確為該條 spec 所述」需要第二個人讀** |
| 6 | **第一批之估計條數 28–34 未含拆分之實際判斷** | note | §6.3 之上限為推測，非量測 |
| 7 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01、A-UP10（ACCEPTED）| 承前 | 擋 Phase 6 寫回，不擋第一批 |

**本輪之三項自我更正**（皆為我 14 輪之產出）：
「Connected Profile App」誤列為表列、中國市場排除之範圍過寬、
「永久限制」之判定過早。**前兩者為讀圖才看得到，第三者是我沒去讀。**

---

## 8. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_pilot.py`（F-1 移除 11.5、F-2 之 ER 四列含欄別、pre-condition 與 remarks 之範圍更正、reasoning）| 否 |
| 2 | 檔案追加 | `DECISIONS.md`（**D-UP16-01**／**D-UP16-02**）| 否 |
| 3 | **檔案編輯** | `RULINGS.md`（R-U5 條文**末加註**；**條文一字未改**）| 否 |
| 4 | 檔案重生成 ×16 | `generated/SWE1-HMI-PROF-*.json` | 否 |
| 5 | 檔案新建 | `docs/upstream/16_pilot_review2.md`（本檔）| 否 |
| 6 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 7 | 程式執行 | 生成 ×1、`lint_tcs`（語料＋self-test）、`lint_variant_labels`（反向＋check）、`--selfcheck`（正向＋三向 tamper）| 否 |
| 8 | **唯讀** | `fitz` 讀 spec PDF p16–p18（抽圖 ＋ 版面重繪）；**圖檔寫在 scratchpad，不入 repo** | 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` **皆無**，**唯讀之 `git status` 亦未跑**。

**未動**：工作簿（**未寫回**，R-U14）、`inputs/`、`forms/`、`framework.md`、
`feature.yaml`、`ANOMALIES.md`、`BASELINE.sha256`、`.gitignore`、
`data/` 之任何檔（**含 `pilot_sample.tsv`** —— 第一批之清單本輪只回報，
待覆核後才落檔）、`generated/` 以外之產物、**他 feature 之任何檔**、
`docs/fw036/` 之任何檔。

### 8.1 待 Pei 之 git 指令清單（依 R-G12，**未執行**）

與上繳 14 §9 同一份，另加本輪之改檔（皆已在該清單之路徑內，
`git add features/user_profiles/scripts`／`DECISIONS.md`／`RULINGS.md`／
`docs`／`generated` 已涵蓋）。**canon 與 feature 仍分兩次 commit。**
