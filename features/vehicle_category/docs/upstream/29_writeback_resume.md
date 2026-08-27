# 上繳包 29 —— Vehicle Category：丙″ 全過 ＋ 台帳交叉索引（T152–T156）

- 日期：2026-08-27
- 對應下放：`docs/handoff/29_writeback_resume.md`
  （SHA256 `3c6604affc4a1eb8e2c99bf4c5d18ef1fb594b72bce3deabab235c49d16a799f`，225 行）
- **結論：T152–T156 全數完成。丙″ 六項全過。**
- 未寫回交付本、**母本 SHA256 前後未變**、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T152 | 丙″ 續驗 | ✅ **6 checked / 0 failed**；圖片降級之前提**已實測成立** |
| T153 | R-VC28 ＋ `feature.yaml` | ✅ `tc_id_format: "newR1L-VC-{n:03d}"` |
| T154 | A-VC21 | ✅ 逐字 ＋ 執行層實測補充 |
| T155 | `ledger_xref.py` | ✅ 標的 **182**、提及 **1055**、跨檔候選 **107** |
| T156 | DR-VC6 加註 | ✅ 並繫連為 T155 之 self-test 已知標的 |

**三件請你先看**：
1. **丙″ 過了，而且 §2.2 的降級前提我實測過，不是接受它** ——
   母本 2 圖確為版面元素（TC 分頁那張錨在 **row 0、col 1–2**，即標題列）。見 §1.3。
2. **又一個更正：openpyxl 沒有重新編碼圖片。** 包 27 §3.4 我寫「圖片被重新編碼」
   —— **錯的**。內容逐位元組相同，它做的是**複製與更名**。見 §1.4。
3. **`ledger_xref` 首跑：107 個跨檔候選。** 我抽查了最可能出問題的四個標的，
   **未發現新的牴觸** —— 但 107 個我沒有逐一讀完，這一點要講清楚。見 §4.3。

---

## 1. T152 —— 丙″

### 1.1 完整輸出

```
步驟 1 —— openpyxl 開副本、寫入 14 欄、save
  母本  x14=1 extLst=1 std=3 printer=5 media=2 size=200650
  step1 x14=0 extLst=0 std=3 printer=0 media=9 size=207050
步驟 2 —— 解壓輸出檔與母本
  母本 48 項；step1 47 項
步驟 3 —— 注入 extLst ＋ printerSettings（**不動 media 與 drawing**）
  extLst 注入：是；自母本補回 printerSettings 相關 5 項
步驟 4 —— 於輸出之 <worksheet> 根元素補宣告 xmlns:xr（取母本同一字串）
  已補：xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
步驟 5 —— 重打包
  step5_repacked.xlsx  208398 bytes

步驟 6 —— 六項驗收
 #  項                                              判
------------------------------------------------------------------------------------
 1  x14:dataValidation 1 條                         PASS
    母本 1 → 修復後 1
 2  extLst 1 個                                     PASS
    母本 1 → 修復後 1
 3  標準 dataValidation 3 條                          PASS
    母本 3 → 修復後 3
 4  printerSettings 5 個                            PASS
    母本 5 → 修復後 5
 5  資料 14 欄 × 3 筆逐格與 JSON 相符（B10 公式 '=IF(ISBLANK($D10),"",ROW()-9)'） PASS
    不符 0 格 無
 6  可被 openpyxl 開啟                                 PASS
    無例外
------------------------------------------------------------------------------------
第二讀者 LibreOffice headless：返回碼 0；產出 ['step5_repacked.csv']
  ⚠ **此非 Excel** —— 其通過只證明套件結構可被另一個實作讀出，**不證明 Excel 開啟不報修復**。

步驟 7 —— 圖片之變化與實害評估（§2.2）
  母本 media ['xl/media/image1.png', 'xl/media/image2.jpeg']
  修復後 media ['xl/media/image1.png', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']
  檔案大小 母本 200650 → 修復後 208398 （+7748）

母本 SHA256 前 6372fb6be02f48dc → 後 6372fb6be02f48dc  **未變**
6 checked / 0 failed
```

### 1.2 六項全過

| # | 項 | 結果 |
|---|---|---|
| 1 | x14:dataValidation 1 條 | 母本 1 → 修復後 **1** |
| 2 | extLst 1 個 | 母本 1 → 修復後 **1** |
| 3 | 標準 dataValidation 3 條 | 母本 3 → 修復後 **3** |
| 4 | printerSettings 5 個 | 母本 5 → 修復後 **5** |
| 5 | 資料 14 欄 × 3 筆逐格與 JSON 相符 | 不符 **0** 格；**B10 公式未動** |
| 6 | 可被 openpyxl 開啟 | 無例外 |

**第二讀者**：LibreOffice headless 轉檔返回碼 0。
**⚠ 此非 Excel** —— 其通過只證明套件結構可被另一個實作讀出，
**不證明 Excel 開啟不報修復**。§2.4 第 6 步之「可被 Excel 開啟而不報修復」
**仍未驗**（環境有 Excel.app，但我不啟動 GUI 應用程式）。

### 1.3 §2.2 之降級前提 —— **我實測過，不是接受它**

下放包 §2.2 把圖片降級為「可接受」，其前提是「母本 2 圖為版面元素」，
並要求「若實測發現該 2 圖承載了資料性內容，**停並回報**」。

**實測**：

| 圖 | 尺寸 | 被幾個 drawing 引用 | 位置 |
|---|---|---|---|
| `image1.png` | **443 × 76** | drawing1／2（sheet1／2，二個 `_old` 分頁）| — |
| `image2.jpeg` | **820 × 121** | drawing3／4／5／6 | **TC 分頁之 drawing6：`twoCellAnchor`，`col 1→2`、`row 0→0`** |

TC 分頁那張之名稱為 `圖片 2`，**無 `descr`（替代文字）**，
錨定於**第 1 列、B–C 欄** —— 即標題列之橫幅。二圖之長寬比皆為扁長條。

**判：版面元素，非資料性內容。不觸發停止條件。**

### 1.4 ⚠ 更正上繳包 27 §3.4 之第二個錯

包 27 §3.4 我寫「圖片 `image2.jpeg` → `image2.png` ＋ 7 個新 jpeg（**重新編碼**）」。
**「重新編碼」是錯的。**

逐檔 SHA256 實測：

```
母本   image1.png   17084e4334868895
母本   image2.jpeg  e6e32dc1ec4e625b
輸出   image1.png   17084e4334868895   ← 同
輸出   image2.png   17084e4334868895   ← 同（image1 之內容）
輸出   image3–9.jpeg e6e32dc1ec4e625b  ← 同（image2 之內容 ×7）

母本之相異內容 2 種；輸出之相異內容 2 種；輸出全部內容皆見於母本：True
```

**openpyxl 做的是「按引用次數各存一份並更名」，不是重新編碼。**
母本以 2 個檔供 6 個 drawing 共用，openpyxl 不去重，故 2 → 9。
**內容零損失**，代價只是體積（整包 +7747 bytes）。

**這是我對同一節的第二次更正**（第一次是 x14 DV 的 2 → 1，包 28 §1.4）。
二次都是**同一種**：**把工具的行為描述得比實測更嚴重**。
`x14 DV 2` 是正則數到開閉標籤，`重新編碼` 是看到副檔名變了就下判斷 ——
**都沒有回去比內容**。記明。

> 對結論之影響：**無**。丙″ 之六項不含圖片，且降級判斷不因「複製而非重編碼」
> 而改變 —— 反而更站得住（內容零損失）。

---

## 2. T153 —— R-VC28

`newR1L-VC-001` … `newR1L-VC-120`，逐字抄入 `RULINGS.md`（條文依 §三 成文），
`feature.yaml` 補 `tc_id_format: "newR1L-VC-{n:03d}"` 並載其取值理由。

**條文明載未主張者**：**跨 feature 之序號唯一性**。
本裁定之「1 起算連續」係依三份交付本之各自形態，
`amfm`／`home`／`comfort` 等未見 `output/` 之 xlsx，其實際值未量到。

---

## 3. T154／T156

- **A-VC21** 逐字抄入 `ANOMALIES.md`，並補執行層之實測來源
  （16 個 yaml、三份交付本之 F 欄、五份工作簿之 D2）與**未量到者**之揭露。
- **DR-VC6** 之「實測佐證」欄加註，正式列為 A-VC20 之成因補充：

  | | 寫於 | 內容 | 來源 |
  |---|---|---|---|
  | **正解** | DR-VC6 該欄（T17）| §10.1／10.2 存有二句文字 ＋ 圖佔位 | SYS1 `Description` |
  | **錯解** | R-VC12 二(a)、表 B | 「SYS1 匯出未帶文字」| 衍生 PDF 之判讀 |

  並繫連為 T155 之 self-test 已知標的。

---

## 4. T155 —— 台帳交叉索引

### 4.1 首跑

```
ledger_xref —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  (b) §10.1 應同時出現於 DATA_REQUESTS 與 RULINGS  PASS  命中 23 處，檔 ['ANOMALIES.md', 'DATA_REQUESTS.md', 'RULINGS.md', 'data/tableB_draft.md', 'docs/REVISIONS.md']
  self-test 2  (a) 反向 §99.99 應零命中                        PASS  命中 0 處
  self-test 3  (b) R-VC12 應跨 ≥2 個台帳                       PASS  檔 ['ANOMALIES.md', 'DATA_REQUESTS.md', 'RULINGS.md', 'data/tableB_draft.md', 'docs/REVISIONS.md', 'framework.md']
  → 三個斷言全過，開始跑正式母體

標的 182 個（{'section': 88, 'ruling': 28, 'dr': 10, 'anomaly': 21, 'leaf': 21, 'revision': 14}）；提及 1055 處
→ data/ledger_xref.tsv
**跨 ≥2 個台帳之候選 107 個** → data/ledger_conflicts_candidates.tsv
  其中 `bare_section=yes`（至少一處為裸 §，非 canon 引用）100 個；全為 canon 引用者 7 個

**本檔不判斷是否牴觸** —— 只並列。判斷由人做。
```

- **標的 182 個**（section 88／ruling 28／anomaly 21／leaf 21／revision 14／dr 10）
- **提及 1055 處**，跨 9 份台帳
  （RULINGS／ANOMALIES／DATA_REQUESTS／DECISIONS／REVISIONS／framework／
  表 A／表 B／profile）
- **跨 ≥2 個台帳之候選 107 個** → `data/ledger_conflicts_candidates.tsv`

### 4.2 self-test 為**三**個斷言，第三個是我加的

下放包 §4.1 列了二個（已知標的 §10.1、反向不存在之節號）。**我加第三個**：

```
self-test 3  (b) R-VC12 應跨 ≥2 個台帳
```

**理由**：若本檔把「並列」誤寫成「每個標的只取第一處」，
**斷言 1 仍會過**（§10.1 之第一處恰在 DATA_REQUESTS，第二處在 RULINGS ——
只取第一處就只會看到一個檔，斷言 1 之「應同時出現於二檔」就會 FAIL）。
…實際上斷言 1 抓得到。但**只取「每檔第一處」**這個變體斷言 1 抓不到，
斷言 3 抓得到（它驗的是**跨檔之數**）。
**二個斷言打的是同一支程式路徑之不同面。**

### 4.3 ⚠ 我抽查了四個，**沒有逐一讀完 107 個**

| 標的 | 提及 | 結果 |
|---|---|---|
| `§10.1`／`§10.2` | 23／24 處，跨 5 檔 | **已知牴觸（A-VC20）**，已由 R-VC27 解 |
| `§15` | 19 處，跨 6 檔 | **一致** —— R-VC12 之原摘要、A-VC20 之實測、DR-VC6 之三問、framework #7、表 B 皆不相斥 |
| `SWE1-HMI-VC-033-01` | 7 處，跨 3 檔 | **一致** —— DR-VC8 之阻斷範圍、R-VC23 之引號保留、A-VC14 之二欄相差一次，三者互補不互斥 |
| `DR-VC6` | 9 處，跨 5 檔 | **一致**（其問法之改寫已同步至表 B 註 2 與 A-VC20）|

**其餘 103 個未逐一讀。** 本包不主張「已無牴觸」——
只主張**材料已經在桌上了**。

### 4.4 已知限制

- **本檔不偵測矛盾**，只並列。判斷由人做（§4.1 明文）。
- **`owner` 欄之降噪有限**：`IN §7`／`FO §3` 之類 canon 引用與本 feature 之
  規格節混在一起。加了 `owner` 欄後，107 個候選中**只有 7 個**被判為
  「全部提及皆帶擁有者」（即幾乎必為 canon 引用）。
  **其餘 100 個仍混著二類** —— 因為同一個 `§3` 在某處是 `IN §3`、
  在另一處是裸 `§3`。**降噪 7/107，不算成功。**
- **母體限於 9 份台帳**。下放包／上繳包（`docs/handoff/`、`docs/upstream/`）
  **不在母體內** —— 它們是往來紀錄非台帳，但**牴觸也可能只存在於那裡**。
- 同一檔內之多次提及**不入候選** —— 只看跨檔。
  A-VC20 之形態是跨檔（DR 檔記對、RULINGS 記錯），但**同檔內之牴觸看不到**。

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

1. **丙″ 是否即為寫回方案** —— 六項全過，惟「Excel 開啟不報修復」未驗
2. **107 個候選之處置** —— 逐一讀？抽樣？或只留作日後查詢之材料
3. **`ledger_xref` 之母體是否納入下放包／上繳包**（§4.4）
4. Tier 3：同批 A（六項）、DR-VC3、DR-VC9(一)、DR-VC10、
   `QS Suggestion` 第 4 項之狀態查詢

---

## 7. 量測條件揭露（R-G8）

### T152

- 全程 `/tmp/vc_writeback_c2/`；母本只做 `read_bytes()` 與唯讀載入，
  SHA256 前後實測 `6372fb6be02f48dc` 未變。
- **3 筆假資料**，非 120 筆 —— 資料量對本驗證之六項無影響，
  但**未驗大量寫入之行為**（記憶體、時間、儲存格樣式之繼承）。
- **「可被 Excel 開啟而不報修復」未驗** —— 環境有 Excel.app 與 LibreOffice，
  我只用了後者之 headless 轉檔。**二者不等價。**
- 圖片之判定依**尺寸、錨點、引用關係、有無替代文字**四項；
  **未開啟圖片檢視其像素內容** —— 若圖內畫的是資料表，本判定會錯。

### T155

- 母體 9 份台帳，**不含下放包／上繳包**。
- `owner` 之判定為**正則前綴比對**，非語意 —— 見 §4.4 之降噪率。
- **107 個候選中我只讀了 4 個**（§4.3）。
- 節號樣式為 `§(\d+(\.\d+)*)`，**不含 `§8.4.3` 之類三段以上者以外之形態**
  （如 `§11.9.1` 可，`§A.1` 不可）—— 本 feature 無字母節號，實害為零。

---

## 8. 進度

**117 leaf 中 112 筆已收斂，TC 累計 120 筆。生成側仍停於 DR-VC3／DR-VC9(二)。**

出貨門檻二表：表 A 完成、表 B 草稿（四處待 DR-VC3）。
`reasoning` 側檔 120 筆。TC ID 已裁（R-VC28）。**寫回方案待你確認丙″。**

**十筆 DR ＋ A-VC21 未結；A-VC20 已解（R-VC27）。**
