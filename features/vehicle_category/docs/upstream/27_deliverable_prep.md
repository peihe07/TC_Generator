# 上繳包 27 —— Vehicle Category：出貨門檻二表 ＋ Phase 6 前置勘查（T142–T144）

- 日期：2026-08-27
- 對應下放：`docs/handoff/27_deliverable_prep.md`
  （SHA256 `3823f9f2b3237463205d4d99f9a552c421c70fc6374e4d099473192f3dd5de30`，145 行）
- **結論：T142–T144 全數完成。二個新發現皆為既有敘述之實測不符。**
- 未寫回工作簿、**未對 036 母本做任何寫入**、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T142 | 表 A（FROP 跨域）| ✅ `docs/TABLE_A_frop_crossdomain.md` —— **13 leaf / 17 TC**；另標二個 17 之陷阱 |
| T143 | 表 B 草稿更新 | ⚠ **A-VC20 —— 三節之「未帶文字」實測不成立**，其中二節藏了一句需求敘述 |
| T144 | Phase 6 前置勘查 | ⚠ **`R` 欄之下拉是 openpyxl 看不見、且開了再存就會毀的 x14 擴充** |

**三件請你先看**：
1. **表 B 有二列在反向作用** —— §10.1／§10.2 寫「內容僅存於圖」，
   而該二節的 SYS1 文字裡有一句 `All four Aux switches … can be used
   simultaneously`。**表 B 的用途是揭露落差，那句話被它自己藏起來了。** 見 §2。
2. **只是開了再存，設計方法的下拉就消失** —— 母本 `R10:R1411` 之下拉為
   x14 擴充（指向 `下拉選單!$A$1:$A$9`），openpyxl 讀不到、
   `load→save` 實測歸零。**而 `R` 欄正是我方要寫的欄之一。** 見 §3.4。
3. **表 A 出現兩個 17，落在不同母體** —— 跨域列 17（145 列母體）、
   跨域 leaf 之 TC 17（120 TC 母體）。**其相等是巧合。**
   REV-11／REV-14 兩次教訓都始於兩個相同的數字，故在它們出現時就標。見 §1.2。

---

## 1. T142 —— 表 A

`docs/TABLE_A_frop_crossdomain.md`，由 `scripts/build_table_a.py` 編製（可重跑）。

### 1.1 承 REV-14：全部重測，不引用任何既有敘述之數字

| FROP | 145 列母體 | 117 leaf 母體 |
|---|---|---|
| `Vehicle Settings`（歸屬域）| 128 | 104 |
| `Power Management` **（跨域）** | 16 | **12** |
| `Audio Management` **（跨域）** | 1 | 1 |
| 合計 | 145 | 117 |

**FROP 欄無空值**（145 列全部有值），故跨域之判定不涉缺值處置。
**跨域 = 13 leaf → 17 TC。**

`DECISIONS.md` 簽署時所載之「145 列中之 17 列（PM 16 ＋ Audio 1）」
**經實測正確**，其母體標註亦正確。

### 1.2 ⚠ 兩個 17

| 量 | 母體 | 值 |
|---|---|---|
| 跨域**列**數 | 145 列 | **17** |
| 跨域 leaf 所產出之 **TC** 數 | 120 TC | **17** |
| 跨域 **leaf** 數 | 117 leaf | 13 |

**前二者皆為 17，而它們不是同一件事。** 第二個 17 是本輪新算出來的 ——
`REV-11`（兩個 16）與 `REV-14`（同一件事再犯）**都始於兩個相同的數字**，
故本表在它們出現的當下就把母體標上，不等到有人拿去互援。

### 1.3 表 A 之逐筆（全表見該檔）

## 1. 跨域 leaf 逐筆（117 leaf 母體）

**13 leaf → 17 TC。**

| req_id | section | FROP | Test Set | 批次 | P | TC 數 | TC 標題 |
|---|---|---|---|---|---|---|---|
| `VC-048-02` | 12.3.2 | **Audio Management** | Settings List | `batch2_settings_list` | P2 | 2 | 1. Confirmation tone plays on a settings change<br>2. Exception settings play no confirmation tone |
| `VC-057` | 13.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Settings tab unavailable in three ignition states |
| `VC-058-01` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Pop-up on a blocked Settings tab attempt |
| `VC-058-02` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P2 | 1 | 1. Blocked-tab pop-up does not time out |
| `VC-058-03` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P2 | 2 | 1. Closing the blocked-tab pop-up with X<br>2. Closing the blocked-tab pop-up with OK |
| `VC-059-01` | 13.2 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Phone settings reached through the Phone screens |
| `VC-059-02` | 13.2 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Phone settings available in Key Off and ACC |
| `VC-060-01` | 13.3 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Audio settings reached through the Media |
| `VC-060-02` | 13.3 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Audio settings available in Key Off and ACC |
| `VC-061` | 13.4 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Software Updates available in Key Off and ACC |
| `VC-064-01` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 2 | 1. Transition to Key Off with the Settings tab open<br>2. Transition to ACC with a Settings category open |
| `VC-064-02` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Transition pop-up neither times out nor closes |
| `VC-064-03` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 2 | 1. Returning to Run clears the transition pop-up<br>2. Returning to Key On clears the transition pop-up |

---

### 1.4 表 A 之已知限制（已寫在表上）

- **FROP 值取自 037 第 8 欄，未與任何 FROP 主檔核對** ——
  本表只能證明「037 這樣寫」，**不能證明 FROP 計畫確實如此分派**。
  **DR-VC5 未結**，其回覆可能改變本表之解讀。
- 若 DR-VC3 回覆「應補」，`Test Set` 欄須隨 framework 由 8 組變 9 組重編。
- 尾段 6 leaf 之 TC 數為 0，標 `(未生成)` —— **非「該 leaf 不需 TC」**。

---

## 2. ⚠ T143 —— 表 B：A-VC20

### 2.1 我先對 17 節重跑了 SYS1 對照，然後停下來

更新之前先驗既有草稿（PLAYBOOK §7.3 之台帳交叉檢，本輪第一次實際動用）：
14 節之內容為 SYS1`Description` 之逐字前綴 ✅；**三個「圖片節」不成立**。

| 節 | SYS1 `Description` 之逐字（`/` 表換行）|
|---|---|
| §15 | `Electronic Park Brake Service Mode Pop-up / (image: image20.png) / (image: image21.png) / (image: image22.png)` |
| §10.1 | `The flow of pressing the Aux settings from Controls / (image: image9.png) / (image: image10.png) / **Refer to the HMI Settings list for settings location.** / **All four Aux switches (Aux 1 Aux 2, Aux 3, and Aux 4) can be used simultaneously** / Graphics are visual aids only. Please see PDO release for official graphics` |
| §10.2 | 同上，首句作 `…from **Apps**`，圖檔為 `image11`／`image12`；**其餘三句逐字相同** |

### 2.2 三節之嚴重程度**不同**，須分開看

| 節 | 判 |
|---|---|
| **§15** | 僅標題句 ＋ 三個圖佔位 —— 原措辭**實質成立**，惟字面「未帶文字」不精確 |
| **§10.1／§10.2** | **原措辭不成立** —— 其文字含一句實質需求敘述 |

**為什麼 §10.1／§10.2 這一項要緊**：表 B 之用途正是揭露覆蓋落差，
而該二列之原措辭**把一句可讀、可測的需求敘述整句藏起來**。
**在這個位置，那句措辭反向作用**——它讓讀表的人以為那裡沒有文字可看。

### 2.3 本輪之處置 —— 未改裁定用語

- **R-VC12 二(a) 之措辭保留不改**（其修訂屬 Tier 2）。
- 於表 B 該三列**並列實測逐字**（引用非摘要，**同 R-VC12 二(c) 對 §8.3 之作法**）。
- 登記 **A-VC20** 待裁。
- **DR-VC6 之前提亦受影響** —— 該 DR 為索取「僅存於圖」三節之可讀來源，
  而其中二節本就有文字，**其問法宜隨之調整**。

### 2.4 本項之由來值得記

該三節之措辭自下放包 03 起沿用至今，**歷經 24 個包無人重測** ——
它被當成已實測之事實引用（**R-VC12 二(a) 即以它為據立條**），
而本輪是第一次有人回去讀那三格。

**與 REV-14 同族**：台帳上的一筆，久到沒人記得它是量出來的還是抄來的。
差別在 REV-14 是台帳寫對而沒人讀，**本次是台帳本身就寫錯了**。

### 2.5 表 B 之其餘更新

- **R-VC12 二(d) 之效力限制自註腳提到表頭**（下放包 §2.2 之明文要求：
  「須寫在表上，不是只寫在上繳包」）。
- **待 DR-VC3 之處以欄位標於每一列**，並列出四處之後果表。
- ⚠ **第四處為執行層補列**：下放包 §2.2 列三處，
  但 **R-VC16(d) 明文「11.9 群歸 #5 …條件性生效，待 DR-VC3」** ——
  §11.9 群（表 B 第 10–13 列）亦待該 DR。已補列並記於註 5。

---

## 3. T144 —— Phase 6 前置勘查

全文見 `docs/PHASE6_writeback_survey.md`（210 行）。**母本未被寫入。**

### 3.1 (a)(c) 母本為**空模板**

9 個分頁（含二個 `_old` 殘留）。TC 本體為第 6 頁，表頭 **row 9**、
資料自 **row 10** 起、預備至 **row 1411**。

**C–AH 欄自 row 10 至 1411 全空**（逐格掃描，0 格有值）；
`B` 欄 1402 列只有公式 `=IF(ISBLANK($D{r}),"",ROW()-9)`。
**無既有 TC、無既有序號**，寫回不涉與他人資料併存。

凍結窗格**無**、條件式格式**無**、資料區合併儲存格**無**。
資料格樣式已預設（`wrap_text`、垂直置中、細框線）——**逐格寫入可直接繼承**。

### 3.2 (b) 欄位映射：**14 欄有來源，13 欄無**

有來源：`C`(polarion_id，⚠ **不在 TC JSON 內**，須自 recon 表帶)、`D`(leaf_id)、
`G`–`N`（test_group／test_set／test_item／pre_conditions／input_test_data／
test_procedure／expected_result／specification_reference）、
`P`(priority)、`R`(design_method)、`S`(functional_safety)。

**無來源者**：`E`／`F`（TC ID 二欄）、`O`、`Q`（預估時間）、
`T`–`Z`（7 個車型）、`AA`（作者）、`AB`–`AH`（執行階段）。

**值域相符實測**：`design_method` 我方 6 種**皆在 `下拉選單!A1:A9` 內**（逐字）；
`priority` 之 `P0`–`P3` **與 P 欄 DV 逐字相符**。

### 3.3 ⚠ (b.1) `reasoning` 在母本裡**沒有位置**

| JSON 欄 | 狀態 |
|---|---|
| `reasoning` | **無對應欄**（唯一形式上可能之去處 `AH 備註` 屬執行階段欄位）|
| `distinguishing_axis` | **無對應欄** |
| `split_flag`／`split_reason` | **無對應欄**（profile §11 已裁本 feature 恆 `False`／空）|

**`reasoning` 是這 120 筆之主要判讀紀錄** —— 每一筆的取材依據、
PENDING 之理由、拆分之判準、R-VC24／R-VC25／R-VC26 之逐筆適用，全在那裡。
**而母本沒有它的位置。** 其去處須裁：併入 `AH`、另立側檔、或不隨工作簿交付。

### 3.4 ⚠⚠ (d)(g) 本項之核心：`R` 欄之下拉是「開了再存就沒了」

母本 `sheet6.xml` 之 `<extLst>` 內，逐字：

```xml
<x14:dataValidation type="list" ...>
  <x14:formula1><xm:f>下拉選單!$A$1:$A$9</xm:f></x14:formula1>
  <xm:sqref>R10:R1411</xm:sqref>
</x14:dataValidation>
```

**`R` 欄（Test Case Design Methods）之下拉為 x14 擴充，跨分頁指向 `下拉選單`。**
`openpyxl` **讀不到它**（`ws.data_validations` 只回報 3 條），
且載入時直接警告 `Data Validation extension is not supported and will be removed`。

**實測（母本副本，不改任何一格，只 load→save）**：

| 量 | 母本 | load→save 後 |
|---|---|---|
| 標準 `<dataValidation>` | 4 | 4（保留）|
| **`x14:dataValidation`** | **2** | **0（全毀）** |
| **`<extLst>`** | **1** | **0（全毀）** |
| `xl/printerSettings/*.bin` | 5 | **0** |
| 圖片 | `image2.jpeg` | `image2.png` ＋ 7 個新 jpeg（重新編碼）|
| 大小 | 200,650 | 205,856 |

**即：什麼都不改、只是開了再存，`R` 欄的設計方法下拉就消失了。
而 `R` 欄正是我方要寫入的欄之一。**

> 這與下放包 §2.3 所述之「PM 線曾因下拉毀損而需外科式修改」**同一成因**。
> 本次是在寫回之前先量到，不是寫壞之後才知道。

**三個候選只列不選**（下放包 §2.3(g) 之要求）：
甲（openpyxl 全量重寫）與乙（逐格寫入後仍 `save()`）**後果相同** ——
破壞發生在 load／save，與寫幾格無關；
丙（解壓改 XML 重打包）**未實測，本包不主張它可行**。

### 3.5 (d.3) 三個模板缺陷（非我方造成，記明）

1. **`P10:Q1411` 共用同一條 DV** —— `Q` 欄是「預估測試時間（分鐘）」，
   卻掛著 `"P0,P1,P2,P3"` 的下拉。**該欄之 DV 顯為誤設。**
2. `Reference` 分頁第 6 項作 `Pair-wise / N-wise`，`下拉選單` 作
   `Pairwise / t-wise` —— **同一份活頁簿內二種寫法**。我方未用該項。
3. ⚠ **`QS Suggestion` 第 4 項**：「Priority 與 SWRA 分法統一呈現，
   高 High、中 Medium、低 Low、不適用 NA」——
   **若採納，P 欄值域將由 `P0–P3` 改為 `High/Medium/Low/NA`，
   我方 120 筆之 `priority` 全數須重映射。** 該建議註記日期 25/10/15，狀態不明。

### 3.6 (f) TC ID 未定

`E`／`F` 皆空、無既有最大序號。IN §10.3 之 `{project}-{abbr}-{NNN}` 中
`{project}`／`{abbr}` **未定**；六批 JSON 之 `tc_id_status` 皆 `provisional`
且**無 `tc_id` 欄**。**TC ID 之編定為寫回之前置，本包未做、未提案。**

---

## 4. 六批回歸（本包未動生成物，回歸為確認）

```
pilot_glovebox                     22 checked / 0 failed
batch1_category_structure          22 checked / 0 failed
batch2_settings_list               22 checked / 0 failed
batch3_controls                    22 checked / 0 failed
batch4_settings_behavior           22 checked / 0 failed
batch5_ignition_availability       22 checked / 0 failed
```

---

## 5. 待你裁

1. **A-VC20**（§2）—— R-VC12 二(a) 之措辭修訂、DR-VC6 問法之調整
2. **表 B 之第四處待 DR-VC3**（§2.5，§11.9 群）—— 覆核我的補列
3. **`reasoning` 之去處**（§3.3）—— 併入 `AH`／另立側檔／不隨工作簿交付
4. **寫回方式**（§3.4）—— 三案只列不選；若要往下走，
   **丙案之可行性驗證**應為下一個獨立任務
5. **TC ID 之編定規則**（§3.6）
6. **`QS Suggestion` 第 4 項之狀態**（§3.5）—— 其採納與否決定 `priority` 之值域
7. 同批 A（六項）、DR-VC3、DR-VC9(一)、DR-VC10（Tier 3）—— **仍全未結**

---

## 6. 量測條件揭露（R-G8）

### 表 A

037 第 8 欄**逐列讀，非抽樣**；`Test Set` 取自 `data/test_set_map.tsv`；
TC 數取自六批 JSON 之 `tcs`。**未與任何 FROP 主檔核對。**

### 表 B 之 SYS1 對照

17 節逐節比對。**草稿中之截斷格（末尾 `…`）只驗其未截斷部分為 SYS1 之子串**
—— 依 PLAYBOOK §7.2，不以截斷字串作為判斷之依據，
故本次之結論為「**前綴相符**」，非「內容完全相符」。

### Phase 6 勘查

- 以 `openpyxl` 讀取 ＋ **直接解 zip 讀 XML** 為之。
  **(d.2) 之 x14 DV 只有在我另外去讀 XML 時才出現** ——
  故**不能排除還有其他 openpyxl 不解析、而本次也沒想到要去 XML 裡找的結構**。
- (g.2) 之實測為**本 repo `.venv` 之該版 openpyxl** 之行為，非通則。
- 母本 SHA256 `6372fb6be02f48dc…`，實測前後未變；**所有寫入實測皆在
  `/tmp/036_probe.xlsx` 副本上**。

---

## 7. 進度

**117 leaf 中 112 筆已收斂，TC 累計 120 筆。生成側仍停。**

出貨門檻二表：**表 A 完成**、**表 B 草稿（措辭待 DR-VC3，且新增 A-VC20 待裁）**。

**十筆 DR ＋ A-VC20 全未結。**
本包之三項做完後，不倚賴 DR 之工作剩下：
`reasoning` 去處之裁定、TC ID 規則、丙案之可行性驗證 —— **三者皆須你先裁**。
