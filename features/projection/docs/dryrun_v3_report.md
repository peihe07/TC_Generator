# Projection — Dry-run v3 報告（檢查表 v3）

> 依 R-P59 ~ R-P66
> 執行日期：2026-08-12
> 腳本：`features/projection/scripts/dryrun_v3.py`
> 明細：`features/projection/data/dryrun_v3.json`
> **未寫回交付用 xlsx、未執行任何 git 操作。** §1 之寫入實測在 scratchpad 複本上進行。

## 總結

| 項 | 結果 | 關鍵數據 |
|---|---|---|
| D-1 | PASS | PRE 23／PROC 42／ER 6（窄口），聯集 63；非授權欄變更 0 |
| D-2 | PASS | 凍結欄不符 0；**公式軌 775 個全數比對**；**值軌標「未實測」**（A-PJ56） |
| D-3 | PASS | 分支 A；565 列，末列 r568；**列身分＝凍結欄雜湊扣 ER，558 列唯一**；被移動 0 |
| D-4 | PASS | 7 條，未補 0 |
| D-5 | PASS | 不重複 75 列，無編號可指 0 |
| D-6 | PASS | 7 條有誤 0；ID `NR1L-PROJ-560~566`；**既有違反 DV 之列 r372／r376** |
| D-7 | PASS | 35 列更新 29 列（v2 已完成） |
| D-8 | PASS | 16 份標記（v2 已完成） |
| D-9 | PASS | 維持空白（`A1:A1`），寫回後出現內容即 ABORT |
| D-10 | PASS | 八項全數命中；補列納入後無位移 |

**整體 PASS。** 惟 §1 的實測翻出四條新 anomaly，其中兩條各推翻一條裁決的事實前提。

---

## 1. R-P59 複本寫入實測（上繳第 1、2 項）

**這一步是本輪最有價值的動作。** 靜態讀取看不到公式、資料驗證範圍與值域強制
來源 —— 四條新 anomaly 全部只在複本寫入後才浮現。

複本：`scratchpad/formula_test/{base,destroyed,written}.xlsx`。

### 1.1 全簿公式普查 —— 不是 99 個，是 775 個（A-PJ60）

| 分頁 | 公式數 |
|---|---|
| `TestResults` | **559** |
| `TestProgress` | **189** |
| `BugList` | 27 |
| **合計** | **775** |

包內 N-1 所述「99 個公式」是 `TestProgress` 中**參照 `TestResults` 者**的數量
（我上一輪的說法），189 才是該分頁的公式總數。

**`TestResults` 自身有 559 個公式，此前無人提及** —— 即 c2 `No.#` 的 `=ROW()-3`，
每列一個。**R-P59 的風險因此比包內描述更大**：毀掉的不是 99 個，是 775 個，
其中包含主表每一列的序號。

### 1.2 反證：`data_only=True` 載入後存檔

```
openpyxl.load_workbook(base.xlsx, data_only=True).save(destroyed.xlsx)
→ 公式總數 775 → 0
```

**R-P59 之風險屬實且已實證。**

### 1.3 保留公式之寫入（`load_workbook(path)` 不帶 `data_only`）

寫入內容：63 列之 71 個儲存格 + 刪除 r562 + 表尾補 7 列（`No.#` 寫公式
`=ROW()-3` 而非字面值）。

**寫回前後公式比對**

| 分頁 | 前 | 後 | 判定 |
|---|---|---|---|
| `TestProgress` | 189 | 189 | **內容完全相同** |
| `BugList` | 27 | 27 | **內容完全相同** |
| `TestResults` | 559 | **565** | 全部為 `=ROW()-3`；559 − 1 + 7 = 565，符合預期 |
| 其餘 6 分頁 | 0 | 0 | 相同 |

**R-P59 判定：PASS —— 公式全數保全。**

`TestProgress` 的 `SUMPRODUCT` 範圍為 `TestResults!$F$4:$F$597`，補列落在
r562–r568，**仍在範圍內**，統計會自動涵蓋，公式不需修改。

### 1.4 R-P60 雙軌雜湊實測

| 軌 | 狀態 |
|---|---|
| **公式軌** | 8 分頁 + `TestResults` 全數比對，**內容完全相同**（`TestResults` 之數量變動為刪 1 補 7 之預期） |
| **值軌** | **不可量測** —— 見下 |

**值軌的實測結果與 R-P60 的假設不同**：以保留公式模式存檔後，openpyxl
**不寫入快取值**。以 `data_only=True` 重讀 `written.xlsx`：

```
原檔     TestProgress D12/E12/F12 快取值 = [53, 43, 3]
寫回後   TestProgress D12/E12/F12 快取值 = [None, None, None]
```

**不是「值改變了」，是「值不存在了」。** 檔案裡只有公式，等 Excel 開啟時才
重算。

推論：R-P60 的值軌**無法以 openpyxl 驗證**，需 Excel／LibreOffice 實際開啟
重算後才有值可比。**這一項本輪標「未實測」**，且在 Phase 7 也需要一個
openpyxl 以外的手段，否則它會永遠停在「未實測」。

### 1.5 其他保全面向（包內未要求，一併實測）

| 面向 | 前 | 後 |
|---|---|---|
| 資料驗證（`TestResults`） | 4 組 | 4 組，sqref 與 formula1 全同 |
| 合併儲存格（`TestResults`） | 3 | 3，範圍全同 |
| 條件格式（`TestProgress`） | 1 | 1 |

**但「範圍全同」在此是問題而非好消息** —— 見 A-PJ59 / §4.3。

---

## 2. R-P65 量測條件收編（上繳第 3 項）

`lint_defs` 新增四區塊，`dryrun_v3.py` 全部改為 `import`：

| 區塊 | 內容 |
|---|---|
| `COL` | 18 個欄索引，表頭 row 2 實測。含註記「`author` 為 c26，v2 曾誤設 c35」 |
| `EDITABLE_COLS` / `FROZEN_COLS` / `DATA_FIRST` / `DATA_LAST` | 由 `COL` 導出，不再各腳本重算 |
| `MEASURE` | 9 個 gate 的 `{unit, cols}`。`unit` 明分 `hit`（逐次）與 `row`（逐列） |
| `ROW_IDENTITY` / `ROW_IDENTITY_COLS` / `ROW_IDENTITY_REJECTED` | 列身分與四個被否決候選之理由 |
| `VALIDATION_SOURCE` | 三個受控欄的 sqref 與**實際強制來源** |

`dryrun_v3.py` 中 `COL_PRE` / `COL_PROC` / `COL_ER` / `COL_AUTHOR` /
`frozen_cols` / `DATA_FIRST` / `DATA_LAST` 全部改為取自 `lint_defs`。

**重跑確認**：收編後 D-1 ~ D-10 結果與 v2 完全相同（D-10 八項基線、D-1 之
23/42/6、D-5 之 75 列皆逐字不變），**收編未改變任何量測結果** —— 這正是應有
的結果：收編是消除重複假設，不是改變條件。

---

## 3. 補列七條之最終內容（上繳第 4、5 項）

### 3.1 既有重複 / 空白 `Test Case ID`（R-P64 前置）

| 值 | 列 |
|---|---|
| `NR1L-PROJ-415` | **r415, r416** |
| `NR1L-PROJ-540` | **r541, r542** |
| （空白） | **r48, r53, r562** |

r562 於分支 A 刪除，故寫回後仍有 **2 組重複 + 2 列空白**。四列皆在凍結欄
（c5），**不得修改**，登記並入 RD-1。

相異值 554 個（格式全部符合 `NR1L-PROJ-NNN`），**最大序號 559**，
1..559 之中有 **5 個空號**，依 R-P64 不填補。

### 3.2 續編結果

**起點 = 559 + 1 = 560**（以最大值為基準，不受重複影響）。

| ID | leaf | Test Group | Test Set | Priority | Design Method | 型態 |
|---|---|---|---|---|---|---|
| `NR1L-PROJ-560` | SWE1-PROJ-133 | WiFi | Disconnection | P1 | 狀態轉換 | 完整 TC |
| `NR1L-PROJ-561` | SWE1-PROJ-167-001 | Device Manager | Device Manager | P1 | 功能測試 | 完整 TC |
| `NR1L-PROJ-562` | SWE1-PROJ-167-002 | Device Manager | Device Manager | P1 | 功能測試 | 完整 TC |
| `NR1L-PROJ-563` | SWE1-PROJ-184 | Audio Management | Projection Audio | P1 | 功能測試 | 完整 TC |
| `NR1L-PROJ-564` | SWE1-PROJ-190 | GPS | Cluster Navigation | P3 | 功能測試 | **BLOCKED** |
| `NR1L-PROJ-565` | SWE1-PROJ-195 | GPS | Cluster Navigation | P3 | 功能測試 | **BLOCKED** |
| `NR1L-PROJ-566` | SWE1-PROJ-227 | Carplay Wired and Wireless | Projection Apps | P2 | 功能測試 | 完整 TC |

全欄內容見 `features/projection/batches/append_uncovered_leaves.json`。
`No.#` 寫公式 `=ROW()-3`（A-PJ57）；`Test Case Author = PeiPYHsu`；
`tc_ref_id = NEW`；`Test Result` 留空（R-P63）。

### 3.3 R-P61 佔位列 Remarks（逐字引用，含原文拼寫與標點）

- `NR1L-PROJ-564`：`Invalid demand, only need to display TBT`
- `NR1L-PROJ-565`：`Mobile phone behavior does not require development.`

兩者皆註明 A-PJ54 與 DR#16，並載明「引文忠實，含原文拼寫與標點」。
第二條原文句末有句號、第一條沒有，**照原樣保留**。

### 3.4 R-P62 設計決策登記

`SWE1-PROJ-133` 之「無 ByeBye 斷線」實現手段（手機關機）已登記於
`DECISIONS.md §0.19`，附三個替代手段（關 Wi-Fi 不可靠、USB 拔除不適用於無線
場景、工具抑制需具名工具且會命中 L-PJ9）與選擇理由，狀態 **RD-1 待確認**。

---

## 4. 檢查表 v3 重跑（上繳第 6 項）

### 4.1 D-2 雙軌

| 軌 | 結果 |
|---|---|
| 凍結欄逐列 | 34 欄 × 559 列，不符 **0** |
| 公式軌 | **775** 個，內容雜湊記錄於 `dryrun_v3.json` |
| 值軌 | **未實測**（A-PJ56：未開寫入時該項不可能失敗，不得計為 PASS 證據） |

授權例外：`Expected Result` r424–r429（6 列）、`Test Case Author` **41 列空白
待補 40 列**（r562 為追溯列不補）。

### 4.2 D-3 列身分（A-PJ57 推翻 R-P66 之指定欄）

R-P66 定 `No.#` 為列身分。**實測該欄 559 列全部是公式 `=ROW()-3`**，其值恆等
於列位置 —— 任何重排後 `No.#` 跟著改，**兩側比對永遠相等，偵測不到移動**。

558 列 558 個相異值看起來像唯一鍵，實際是位置標籤。**唯一 ≠ 穩定。**

四候選實測：

| 候選 | 相異值 | 判定 |
|---|---|---|
| `No.#` (c2) | 558 | ❌ 位置標籤 |
| Polarion ID (c3) | 162 | ❌ 不唯一 |
| Req/Design ID (c4) | 163 | ❌ 不唯一（v2 用過，同樣不合格） |
| Test Case ID (c5) | 555 | ❌ 2 組重複 + 3 空白 |
| **凍結欄雜湊扣 ER** | **558** | ✅ **採用** |

**扣除 ER 是必要的**：首次改版把 ER 算進身分，r424–r429 因 R-P12 窄口的授權
變更被誤判為「被移動」，D-3 直接 FAIL 6 列。身分基底必須排除**有授權例外的
欄**。扣除後 558 列仍為 558 個相異值。

**R-P66 的意圖（列身分須為唯一鍵）成立且已實現；指定的欄不成立。**

### 4.3 D-6 值域（A-PJ58 / A-PJ59）

`Design Method` 的資料驗證指向 **`Reference!$C$4:$C$12`，不是 `下拉選單` 分頁**。
兩份各 9 項，八項相同，第九項拼法不同：

| 來源 | 逐字 |
|---|---|
| `Reference!C4:C12`（強制） | `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)` |
| `下拉選單!A`（v2 使用） | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` |

**dry-run v2 的 D-6 驗的是沒有被強制的那一份** —— gate 通過不代表 Excel 會接受。

既有 **r372（NR1L-PROJ-370）與 r376（NR1L-PROJ-374）用下拉選單那個拼法**，
違反本簿自身的資料驗證。二列在凍結欄內，**不修改**，登記並入 RD-1
（r376 同時在 `FROZEN_ROWS` 內）。

補列僅用「功能測試」與「狀態轉換」，兩份清單皆相同，未受影響。

**資料驗證範圍問題（A-PJ59）**：複本寫入後四組 sqref **未隨補列延伸**：

| 欄 | sqref（前 = 後） | 補列覆蓋 |
|---|---|---|
| Priority (O) | `O4:O562` | 僅 r562；**r563–r568 無下拉** |
| Design Method (Q) | `Q4:Q152 Q167:Q190 Q219:Q562` | 同上 |
| Test Result (AD:AH) | `AD4:AH562` | 同上 |

值本身正確（D-6 已驗），但人工填寫時最後 6 列無選單，Excel 也不會阻擋錯值。
**範圍延伸至 r568 須明文納入 Phase 7 寫回步驟。**

**連帶更正 R-P63 的事實前提**：`Test Result` 值域由資料驗證強制，實為
`Pass, Fail, Block, NA, Pending` —— **`NA` 與 `Block` 都在**。該清單是資料驗證
的 inline 值，不在 `下拉選單` 分頁，故「分頁凍結不得新增值」對它不適用。
本輪仍依裁決留空；DR#17 的問法已據此改寫。

### 4.4 D-9

`Test Case Framework` 維度 `A1:A1`、非空格 0 —— **維持空白，PASS**。
寫回後若出現內容即 ABORT。

### 4.5 D-10

八項全數精確命中（1／4／17／5／8／30／3／0），補列納入後無一位移，
依 R-P56 無需裁決。

---

## 5. R-P41 掃描條件揭露（上繳第 7 項）

**本輪起，全部條件取自 `lint_defs.MEASURE`，本報告只是它的呈現。**

| 項 | 單位 | 掃描欄 |
|---|---|---|
| L-PJ5 禁詞 | 次 | 9, 11 |
| L-PJ6 模糊語 | 次 | 9, 11, 12 |
| L-PJ9 泛稱工具 | **列** | 9, 11（兩條件同時成立） |
| L-PJ10 缺陷類 | **列** | 9, 11, **12** |
| L-PJ10 參數類 | **列** | 9, 11, **12** |
| 步驟交叉指涉 | 列 | 11 |
| 步數 != ER | 列 | 11 vs 12 |
| 前向循環指涉 | 次 | 11 |
| L-PJ1 訊號 | 次 | `SCAN_RISK` 六欄，先移除 `$...$`，豁免 3 項 |

列範圍：實體列 4–561。`CAN` 字樣比對**大小寫敏感**（A-PJ37）。
列身分：`ROW_IDENTITY_COLS`（凍結 34 欄扣 `Expected Result`）。
值域：`VALIDATION_SOURCE`（以資料驗證實際指向者為準）。

---

## 6. 上繳第 8 項｜本包是否仍有該驗而未驗者（執行層獨立判斷）

前兩輪此項各產出實質發現（首輪五點成為 D-6 ~ D-10；次輪 N-1 攔下不可逆毀損）。
本輪五點。

### M-1｜R-P60 的值軌在 openpyxl 下永遠無法實測

§1.4 已證：保留公式模式存檔後，快取值不寫入（`[53, 43, 3]` → `[None, None, None]`）。
**值軌不是「會變」，是「不存在」。**

R-P60 要求「其餘 7 分頁之值雜湊仍須不變」—— 這 7 個分頁若含任何公式就同樣
取不到值（`BugList` 有 27 個）。

**判斷**：值軌需要一個 openpyxl 以外的重算手段（LibreOffice headless
`--convert-to xlsx` 可重算），否則該項會永遠停在「未實測」，而 A-PJ56 的通則
正是要避免這種項目被當成 PASS。**這是 A-PJ56 通則的第一個實際應用對象，
且它指向的是包內剛立的 R-P60 自身。**

### M-2｜寫回步驟清單本身尚未成文，而它已知至少有五個必要動作

本輪實測累積出五個 Phase 7 寫回**必須做**的動作，目前散在五條 anomaly 裡，
沒有一份清單：

1. 以保留公式模式載入（R-P59）
2. 補列的 `No.#` 寫公式 `=ROW()-3` 而非字面值（A-PJ57）
3. 資料驗證 sqref 延伸至 r568（A-PJ59）
4. 刪 r562 後確認 `TestProgress` 的 `$597` 範圍仍涵蓋（已驗，但寫回時要再確認）
5. 寫回後以重算手段驗值軌（M-1）

**判斷**：Phase 7 下放包需要一份寫回步驟清單，且第 2、3 項若遺漏**不會被任何
現行檢查項抓到** —— D-2 比對凍結欄內容，不比對儲存格型別；D-6 比對值，不比對
該值有沒有下拉。

### M-3｜`Input Test Data` 我全填 `NA`，但未驗證那是不是正確慣例

補列七條的 c10 我填 `NA`。實測既有 558 列：`NA` 538 列、空白 19 列、有實質
內容 1 列（r?? 的 `Gear position sequence…`）。

`NA` 是壓倒性多數，但**19 列空白與 1 列有內容代表這欄不是純樣板**。我沒有
查證那 19 列空白是慣例還是缺漏，就沿用了多數值。

**判斷**：影響小（值域正確、不影響 gate），但這是一個**未經查證的沿用**，
按 canon §5a 第九條（單一來源之覆蓋率不等於其類別）應該先問再填。登記於此。

### M-4｜補列的 `Specification Reference` 錨點只驗了格式，沒驗指向的章節真的存在

D-6 的 `Specification Reference` 檢查實作是**格式比對**（`CFTS085-\d{7}`），
不是**解析**。R-P53 的原文是「錨點須存在於 `inputs/` 且可解析」。

我為補列寫的 `CFTS085-4935517` / `4935526` / `4935397` / `4935546` / `4935519`
取自同 Test Set 既有列，**沿用既有列的錨點而非自行查證該章節涵蓋補列的內容**。

**判斷**：這是 D-6 的一個實作缺口，且我在 v2 報告裡把它寫成「7/7 通過」，
**那個 7/7 只證明格式對**。`data/cfts085_sections.json` 有章節索引，可以真正
解析，本輪未做。應補。

### M-5｜r372／r376 的 DV 違規可能不只 Design Method 一欄

A-PJ58 找到 2 列違反 `Design Method` 的資料驗證，那是因為我**恰好**比對了
該欄。另外三組資料驗證（Priority `O4:O562`、Test Result `AD4:AH562`、
Vehicle Model `S4:Y6`）**本輪沒有逐列比對既有值是否落在值域內**。

**判斷**：既有列是否還有其他 DV 違規，目前未知。這類違規改不了（凍結欄），
但**該登記而未登記**，且 D-6 只驗補列、不驗既有列，沒有任何檢查項涵蓋。
建議升為一次性全簿掃描。

---

## 7. 兩項數字差異（照實記錄，不調和）

| 項 | 包內 | 實測 | 處置 |
|---|---|---|---|
| `data/` artifact 份數 | 13 | **16** | 包內已認以實測為準 |
| D-5 不重複列數 | 73 | **75** | 新增 r177／r188，預期內 |
| **全簿公式數** | **99** | **775** | **本輪新增**：99 是 `TestProgress` 中參照 `TestResults` 者，非全簿數（A-PJ60） |

---

## 8. 仍在阻塞

- **DR#14 (b)** —— Atlantis Mid 五車型是否在 R1LR SWQT 範圍內，擋 B5 的 42 列。全案唯一阻塞。
- 待答不阻塞：**DR#15**（227 之 dedicated phone APP）、**DR#16**（190／195）、
  **DR#17**（BLOCKED 列統計口徑，問法已依 A-PJ59 改寫）

## 9. 本輪未觸及者

- **未寫回交付用 xlsx** —— §1 之寫入僅在 scratchpad 複本
- **未執行任何 git 操作**
- **未修改任何既有 TC**
- **未修改來源原檔**
