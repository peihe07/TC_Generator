# 上繳包 04 —— R-PMH10 證據基礎之更正、母體判準與機器檢查補實

- 日期：2026-08-23
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/04_corpus_and_assertions.md`
- 前一包：[upstream/03_testgroup_and_dv.md](03_testgroup_and_dv.md)
- 執行狀態：**步驟 1–7 全部執行完畢。** 九條停止條件全未觸發。
  **零寫回工作簿**；git 指令零次。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH19 | 已交付件語料之母體判準 | 354 | `cbdeed8b8bc0774b` | `cbdeed8b8bc0774b` | 逐字相符 |
| R-PMH20 | 量詞與量測範圍須一致 | 269 | `786c9662722e59ac` | `786c9662722e59ac` | 逐字相符 |
| R-PMH21 | 規格文字量不作完整性判準 | 255 | `7224a21216886aab` | `7224a21216886aab` | 逐字相符 |
| R-PMH22 | `write_back` 之機器檢查 | 445 | `c9930caa2cfc8567` | `c9930caa2cfc8567` | 逐字相符 |
| R-PMH23 | 客戶那份之封面五頁禁用 | 427 | `70982925ea302e53` | `70982925ea302e53` | 逐字相符 |

### 1.1 R-PMH10 之 `[PEI-REOPEN]` 標記落實證明

標記以引用段落置於 R-PMH10 之 fenced block **之外**。落地後獨立再抽取：

| 條號 | SHA256（前 16） | 與 02 包所記 |
|---|---|---|
| R-PMH10 | **`885070968235b262`** | **相同** |

標記內容含：漏取之 AMFM 20260810、其 `D5` 之逐字值、母體從未定義之事實、
「現狀維持有效但不得自行改判」之處置，以及「重裁前行為不變故不阻斷」。

---

## 2. D3／D4／D5 全母體實測（步驟 2）—— **R-PMH10 之依據確不成立**

### 2.1 母體之建立（R-PMH19，自行重掃）

掃描式：`ASW-R2` 全樹 `**/*036*.xlsx`，排除 `~$` 開頭之 Excel 暫存檔。

| 階段 | 檔數 |
|---|---|
| 候選全集 | **28**（與分析層所報相符） |
| 排除 (a) 非交付夾根層 | **14** |
| 排除 (b) 檔名含中間態標記 | **1** |
| 排除 (c) 同夾舊版 | **2** |
| **母體** | **11** |

**母體 11 ≥ 5，停止條件 7 未觸發。**

**(a) 非根層之 14 檔**（`Core HMI/*` 5、`Engineering Mode/App Team Effort/*` 4、
`Vehicle Settings/*` 5 —— 後者含 `REF/036_pre_writeback_20260823.xlsx` 與
`VF230_V1_R5/output/`、`output/validation/` 各一）。

> ⚠ **值得回報之副作用**：(a) 之「根層」規則排除了 **Home**、**AppDrawer**、
> **Notifications HMI**、**Vehicle Settings（CFTS044）**、**VF230** 五個
> feature 之交付件 —— 它們並非中間態，只是交付夾多了一層。
> **本包照條文執行，不自行放寬**，但若 Pei 之意圖是「所有已交付件」，
> 此規則會漏掉這五個。列入 §8 之該驗而未驗者。

**(b) 中間態標記之 1 檔**（根層者）：
`Engineering Mode/…_EngMode_20260816_Rebuilt.xlsx`。
另有 3 檔同時觸犯 (a)(b)（`(Review)`／`(Refine)`／`(Revise)`／`(done)`），
已計入 (a)。

**(c) 同夾舊版之 2 檔，具名排除**：

| 檔 | 取代者 |
|---|---|
| `Engineering Mode/…_EngMode_20260429.xlsx` | `…_EngeeringMode_20260816.xlsx` |
| `Power Management/…_PowerManagement_20260820.xlsx` | `…_PowerManagement_20260821.xlsx` |

### 2.2 母體 11 檔之逐檔全路徑與三欄實測

根目錄 `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/`

| # | 交付夾 | 檔名 | 分頁 | 欄數 | `Cover!D6` | 資料列 | D3 | D4 | **D5** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `AM:FM/` | `…_AMFM_20260810.xlsx` | `…測試用例規範` | 34 | `C` | 298 | 空 | 空 | **非空** |
| 2 | `Audio Management /` | `…_Audio(AACP)_20260624.xlsx` | `…&Result` | 34 | `C` | 43 | 空 | 空 | 空 |
| 3 | `Climate Control Interface/` | `…_Comfort_20260817.xlsx` | `…測試用例規範` | 34 | `C` | 466 | 空 | 空 | 空 |
| 4 | `Connection Manager/` | `…_CONNECTIVITY_20260819.xlsx` | `…測試用例規範` | 34 | `A` | 123 | 空 | 空 | 空 |
| 5 | `Disclaimer screen/` | `…_PowerModingHMI_20260819.xlsx` | `…測試用例規範` | **35** | `A` | 48 | 空 | 空 | 空 |
| 6 | `Engineering Mode/` | `…_EngeeringMode_20260816.xlsx` | `…&Result` | **35** | `A` | 211 | 空 | 空 | 空 |
| 7 | `Power Management/` | `…_PowerManagement_20260821.xlsx` | `…&Result` | 34 | `A` | 284 | 空 | 空 | 空 |
| 8 | `Privacy Mode/` | `…_Privacy_20260813.xlsx` | `…測試用例規範` | 34 | `C` | 11 | 空 | 空 | **非空** |
| 9 | `SiriusXM/` | `…_SXM_20260813.xlsx` | `…測試用例規範` | 34 | `C` | 215 | 空 | 空 | **非空** |
| 10 | `Time Management/` | `…_20260822.xlsx` | `…測試用例規範` | 34 | `C` | 59 | 空 | 空 | 空 |
| 11 | `User Profiles/` | `…_UserProfiles_20260820.xlsx` | `…測試用例規範` | 34 | `C` | 189 | 空 | 空 | 空 |

### 2.3 計數

| 欄 | 空 | 非空 | 比率（分母 = R-PMH19 母體 11） |
|---|---|---|---|
| `D3` | **11** | 0 | 11/11 空 |
| `D4` | **11** | 0 | 11/11 空 |
| **`D5`** | 8 | **3** | **8/11 空、3/11 非空** |

**R-PMH10 之依據句「語料 5/5 無一填寫」確不成立。**
`D3`／`D4` 之結論不受影響（全母體皆空）；**變動者只有 `D5`**。

### 2.4 三個非空 `D5` 之逐字全文與其指向

| # | 交付夾 | `D5` 逐字 | 指向 |
|---|---|---|---|
| 1 | `AM:FM/` | `SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323` | **SWRA（037）報告全名**，前綴 `SWE1_{feature 縮寫}_`，後綴日期 |
| 8 | `Privacy Mode/` | `SWE1_CFTS_022-Privacy_Features` | **CFTS 規格條目 id**（`CFTS_022`），非報告名、非檔名 |
| 9 | `SiriusXM/` | `SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406` | **SWRA（037）報告全名**，同 #1 之形態，日期不同 |

**三者之形態**：2 份指向 037 報告全名（同一模板，僅 feature 縮寫與日期不同）、
1 份指向 CFTS 規格條目 id。三者皆以 `SWE1_` 起首。

**與 01 包 Q3 之原提案對照**：Q3 曾提案填「規格文件全名」
（`Power Moding HMI Logic and Flow R1 SR24 2A`）。
**該形態在母體中零個** —— 三個非空者無一指向規格文件本身。

**未觀察到相關性**：三個非空者之 `Cover!D6` 皆為 `C`，但另有四個 `C` 版
（Comfort、TM、UP、Audio）之 `D5` 為空；欄數 34 之十份中三份非空、
欄數 35 之兩份皆空。**樣本不支持任何以版本或欄數為條件之規則。**

> **執行層不提案、不歸納慣例**（下放包步驟 2 明載）。**Q3 之重裁屬 Pei。**
> 在重裁前 `D3`／`D4`／`D5` 一律不寫入，行為與現行 R-PMH10 相同。

---

## 3. `write_back` 之機器檢查（步驟 3，R-PMH22）

**程式路徑**：`features/power_moding/scripts/check_write_back.py`
（本 feature 專屬；**未改動 `scripts/recon.py` 或任何共用腳本**）。

三項函式對應 R-PMH22 之 (a)(b)(c)：
`check_blank_precondition`／`check_start_row_source`／`check_row_count_delta`。
任一失敗即拋 `CheckFailed`，呼叫端據此中止寫回。本檔**只讀工作簿，
連 `openpyxl.save()` 都不呼叫**（R-G3／停止條件 9）。

**自我測試指令**：`python scripts/check_write_back.py --feature . --self-test`

### 3.1 三次故意失敗之實際輸出

```
=== R-PMH22 故意失敗測試（三項）===

[a] 攔下 ✅
    (a) blank_precondition FAILED — 自 r10 起 D 欄應全空，實測 1 列非空：[10]。
        workbook_state 已非 BLANK，append 會覆蓋既有資料。

[b] 攔下 ✅
    (b) start_row_source FAILED — 起始列 44 != feature.yaml write_back.first_row 10
        —— 且該值出現在 data/outline_map.json 的 row_036_customer 內，
        該欄記的是客戶那份的列號，不是寫回目標列

[c] 攔下 ✅
    (c) row_count_delta FAILED — 寫回前 0 列，本批 48 筆，預期 48 列，
        實測 47 列（差 -1）
```

**三項全部被攔下，停止條件 8 未觸發。**

各項之注入方式：
- **(a)** 以假的 worksheet 物件模擬 `r10` 已有 `SWE1-HMI-PM-999`
  —— **不動真實工作簿**（本包零寫回）；
- **(b)** 起始列取 **44**，該值刻意選自 `outline_map.json` 之
  `row_036_customer`（即 `SWE1-HMI-PM-022-02` 在客戶那份之列號）
  —— 檢查不僅擋下，還**認出該值的來源並在訊息中指出**；
- **(c)** 令寫回後列數為 `before + 48 - 1`。

### 3.2 範圍向（R-G9 —— 證明正常情形不轉紅）

```
=== 範圍向 —— 正常情形不得轉紅 ===
    (a) blank_precondition PASS — 自 r10 起 D 欄 0 列非空
    (b) start_row_source PASS — 起始列 10 == first_row
    (c) row_count_delta PASS — 0 + 48 == 48
    範圍向 PASS ✅ —— 三項在正常輸入下皆通過

三項故意失敗全部被攔下: True；範圍向: True
exit=0
```

**R-PMH22 之 RESOLVED 條件已滿足**：檢查已實作、三項各以一次故意失敗
證明其會攔下、且證明其在正常輸入下不會誤報。
`feature.yaml` 新增 `write_back_checks` 節記錄程式路徑與自測指令。

> 03 包 §9 第 5 項自陳「目前只是文字修補」，**本包已將其轉為實跑之機器檢查**。

---

## 4. `data/uncited_sections.tsv`（步驟 4）

**程式路徑**：`features/power_moding/scripts/classify_uncited_sections.py`
（新寫；**未改動任何共用腳本**）。分類欄以規則產生，先命中先取：

| 規則 | 判準 |
|---|---|
| `chapter_node` | outline 無 `.`（第 1 層） |
| `image_placeholder` | `Description` 含 `Please refer to the diagram` |
| `assumptions` | 所屬章之 `Description` 逐字為 `Assumptions` |
| `other` | 以上皆非 —— **帶實質文字而未被引用者會落在這裡** |

**餘數驗證（R-G10）**：`52 − 29 − 23 = 0`，程式內以 `assert` 強制。

### 4.1 分類計數

| 分類 | 筆數 |
|---|---|
| `chapter_node` | 12 |
| `image_placeholder` | 6 |
| `assumptions` | 5 |
| **`other`** | **0** |
| 合計 | **23** |

### 4.2 與 03 包 §7.3C 人讀結論之比對

| 項 | 結果 |
|---|---|
| **集合是否相同** | **相同** —— 同 23 個成員，逐項一致 |
| **「無一項帶實質需求文字」之結論** | **成立** —— 機器分類之 `other` = **0** |
| 分類邊界 | **有一處不同**（見下） |

**唯一差異**：outline `1`（`Assumptions`）。03 包人讀時歸入
「Assumptions 全章」，機器規則因 `chapter_node` 先於 `assumptions` 求值
而歸為 `chapter_node`。

**這是分類邊界之差異，不是集合之差異** —— 23 個成員完全相同，
且 `other` 為 0。**依下放包「不符者以機器產出為準」，採機器分類。**

**停止條件 9 未觸發** —— 差異不涉及「帶實質需求文字之節點被判為未引用」。

---

## 5. 全簿 DV 複掃（步驟 5，A-PMH11）

### 5.1 母本 —— **全簿 5 組**（legacy 4 ＋ x14 1）

| 分頁 | 型別 | sqref | type | allowBlank | `formula1` |
|---|---|---|---|---|---|
| **`Product Document 記錄封面頁`** | legacy | **`B7:C7`** | list | 1 | **`"Confidential, Top Secret"`** |
| `Test Case Specification 測試用例規範` | legacy | `P10:Q1411` | list | 1 | `"P0,P1,P2,P3"` |
| `Test Case Specification 測試用例規範` | legacy | `T10:Z1411` | list | 1 | `"0,1"` |
| `Test Case Specification 測試用例規範` | legacy | `AF10:AF1411` | list | 1 | `"Pass, Fail, Pending,Block,NA"` |
| `Test Case Specification 測試用例規範` | x14 | `R10:R1411` | list | 1 | `下拉選單!$A$1:$A$9` |

**分析層之複驗相符**：遺漏之一組確為 `Product Document!B7:C7`。

### 5.2 客戶那份 —— **全簿 5 組**（legacy 4 ＋ x14 1）

| 分頁 | 型別 | sqref | `formula1` |
|---|---|---|---|
| `Product Document 記錄封面頁` | legacy | `B7:C7` | `"Confidential, Top Secret"` |
| `Test Case Specification 測試用例規範` | legacy | **`Q10:Q221 R10:R11 P10:P11`** | `"P0,P1,P2,P3"` |
| `Test Case Specification 測試用例規範` | legacy | `U10:AA221` | `"0,1"` |
| `Test Case Specification 測試用例規範` | legacy | **`AG10:AG13`** | `"Pass, Fail, Pending,Block,NA"` |
| `Test Case Specification 測試用例規範` | x14 | `S10:S221` | **`Reference!$C$4:$C$12`** |

### 5.3 二者差異

`Product Document!B7:C7` 二檔**完全相同**。
`Test Case Specification` 之四組**全部不同**：

| 語意 | 母本 | 客戶 |
|---|---|---|
| priority | `P10:Q1411`（跨兩欄，連續） | `Q10:Q221 R10:R11 P10:P11`（**三段破碎多範圍**） |
| vehicle_models | `T10:Z1411` | `U10:AA221`（欄右移 1，列上界 221） |
| test_result | `AF10:AF1411`（1402 列） | **`AG10:AG13`（僅 4 列）** |
| design_method（x14） | `R10:R1411` → **`下拉選單!$A$1:$A$9`** | `S10:S221` → **`Reference!$C$4:$C$12`** |

欄位之位移與 35 欄版面一致；列上界 221 對 1411 反映其容量較小。

### 5.4 **本輪最重要之發現 —— A-PMH10 之證據須更正**

**兩檔之 x14 DV 指向不同的 source 分頁**：

| 檔 | x14 source | 第 6 項之值 |
|---|---|---|
| 母本 | `下拉選單!$A$1:$A$9` | `組合測試 (Combinatorial Testing ; **Pairwise / t-wise**)` |
| 客戶 | `Reference!$C$4:$C$12` | `組合測試 (Combinatorial Testing ; **Pair-wise / N-wise**)` |

實測 `Reference!C4:C12` 與 `下拉選單!A1:A9` 之九項：**八項逐字相同，
僅第 6 項不同**。

**03 包 §6 之陳述「母本與客戶那份兩檔皆同 → 表單層瑕疵」不正確。**
成因：03 包只讀了兩檔之 `下拉選單` **分頁內容**（確實相同）便下結論，
**未查該分頁是不是各該檔之 DV source**。客戶那份之 `下拉選單` 是
**孤兒分頁** —— 存在、內容與母本相同、但沒有任何 DV 指向它。

**教訓與 R-PMH20 同型**：比對兩個值之前，先確認兩邊指的是不是同一個東西。
（與 03 包 §3 之 priority 假衝突、02 包 §3.3 之列號位移推算，同一形狀。）

**對本 feature 之效力不變**：R-PMH7 已定母本為交付基底，其 x14 DV 指向
`下拉選單!$A$1:$A$9`，故 `feature.yaml` 之 `design_method_vocabulary`
9 項**維持不變**。03 包之逸出檢查 0 亦不受影響 —— 四份交付件之 996 個
R 欄值全部落在母本清單內，**無任何交付件用過 `Pair-wise / N-wise`**。

### 5.5 依 R-PMH20 改寫之結論句

03 包 §2.2 末句原為
「母本之 DV 總數 = 4 組（legacy 3 ＋ x14 1），除此之外無其他 DV」。
**改寫為**：

> **母本之 `Test Case Specification 測試用例規範` 分頁**之 DV 為 **4 組**
> （legacy 3 ＋ x14 1）；**全簿**為 **5 組**（另有
> `Product Document 記錄封面頁!B7:C7`，legacy list
> `"Confidential, Top Secret"`）。

`feature.yaml` 之 `workbook.data_validation` 節已加註同義說明。

---

## 6. A-PMH11／A-PMH12 之登記（步驟 6）

| 條號 | 主旨 | 狀態 |
|---|---|---|
| **A-PMH11** | 量詞與量測範圍不一致：分頁層量測寫成全簿結論（實測全簿 5 組） | **RESOLVED**（R-PMH20 立條，證據已補齊，結論句已改寫） |
| **A-PMH12** | `Q` 套用 `"P0,P1,P2,P3"` 下拉；`AF` 列舉含前導空白 | **PENDING** —— Phase 6／7 之前置阻斷項 |

**A-PMH12 之兩項**（母本）：
1. priority DV 之 `sqref` 為 `P10:Q1411`，**跨 P、Q 兩欄**。`Q` 欄為
   `Estimated Test Time (mins)`，其合法值應為分鐘數，卻套用 `P0/P1/P2/P3`
   —— **任何寫入 `Q` 之數值都會被 Excel 擋下**。`allowBlank=1` 是它至今
   未被發現的原因。
2. `AF` 之 `formula1` 逐字為 `"Pass, Fail, Pending,Block,NA"`，以 `,` 切開後
   `Fail` 與 `Pending` **各帶一個前導空格**，`Block` 與 `NA` 沒有。
   **寫入 `Fail`（無空格）會被擋下**；任何對測試結果做 `.strip()` 的程式
   都會產出無法通過 DV 的值。

客戶那份另有獨立瑕疵（test_result DV 只涵蓋 `AG10:AG13` 四列），
因 R-PMH7 已改用母本，**對本 feature 無效力，僅登記**。

**本包不提解法**（下放包步驟 6 明載）。**已於 `DECISIONS.md` §7 標為
Phase 6／7 之前置阻斷項**，並於 `feature.yaml` 之
`workbook.data_validation` 節加註。

### 6.1 A-PMH09／A-PMH10 之狀態更新

- **A-PMH09 → RESOLVED**（R-PMH23）。內文已依 §2.3 更正結論：
  「衍生自 AMFM **交付件**」不成立（該件 34 欄、履歷未被覆寫、`D5` 已填），
  成立者為「帶 AMFM **中繼產物**之血緣」。**執行層原提案 (c)（回報 AMFM）
  不執行**，理由已記入。
- **A-PMH10 維持 PENDING**，證據段全面更正（見 §5.4）。

---

## 7. `INDEX.md`／`PLAYBOOK.md` §6 之更新（步驟 7）

`PLAYBOOK.md` §6 狀態板已改寫：

- **P0 ✅**（素材 5 份 `shasum -c` 全 OK，DR-PMH 零筆）
- **P1 ✅**（`BLANK`／48 leaf／48 targets／assertion 1/1 PASS）
- **P2 待簽核**（`DECISIONS.md` 已預填 ＋ 8 項 `[RULED]` ＋ 本包新增 2 項）
- **下一步：Phase 2／3（framework），無阻斷項**
- 新增 **Open rulings** 表：`[PEI-REOPEN]` 之 Q3 列首，並註明「行為維持
  不寫入，不阻斷」；H 欄與 Part N／profile 之 `[PEI]` 各一列
- 新增 **Open PENDING anomalies** 表：A-PMH03／04（Phase 4）、A-PMH10（不阻斷）、
  **A-PMH12（Phase 6／7 前置阻斷項）**、A-PMH06 附項（PENDING-CANON）

`docs/INDEX.md` 已補 04 輪次列與要點。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **R-PMH19 之 (a)「根層」規則排除了五個 feature 之交付件** ——
   Home、AppDrawer、Notifications HMI、Vehicle Settings(CFTS044)、VF230。
   它們並非中間態，只是交付夾多了一層（`Core HMI/HomeHMI/`、
   `Vehicle Settings/CFTS044/`）。**本包照條文執行，未自行放寬。**
   若 Pei 之意圖是「所有已交付件」，則母體應為 16 而非 11，
   而 `D5` 之比率會改變。**Q3 重裁前建議先確認此點** —— 否則會重蹈
   「母體未定義」之覆轍，只是這次母體有定義但可能定錯。
   **本項為五項中最該優先處理者。**

2. **未查那五個被排除之檔的 `D5`。** 承上 —— 我沒有順手量它們，
   因為量了就會有把它們併入比率的誘惑。若 Pei 決定放寬 (a)，
   下一包補測即可（成本極低）。

3. **`check_write_back.py` 尚未被任何寫回路徑呼叫。** 三項檢查已實作
   並經故意失敗驗證，但**目前沒有任何程式會去呼叫它** ——
   `feature.yaml` 之 `write_back_checks` 節只是宣告。R-PMH22 要求
   「於每次寫回前自動驗證」，該「自動」尚未接上，**要到 Phase 6
   實作寫回時才能接**。本項是**已知的未完成**，非疏漏。

4. **`Product Document!B7:C7` 之 DV 未查其是否影響交付。** 該分頁在母本為
   「僅標籤、值全空」，但**客戶那份之該分頁有值**（`B7 = Confidential`）。
   若 Phase 7 要求填寫產品文件封面頁，該 DV 之列舉（僅 `Confidential`／
   `Top Secret` 兩項）就會生效。本包只登記其存在，未評估其影響。

5. **A-PMH12 (2) 之前導空白，未查四份交付件以外之母體九檔。**
   §5 之全簿掃描只做了母本與客戶那份兩檔。母體 11 檔中其餘九檔之
   `AF` DV 是否同樣帶前導空白、其 x14 source 指向 `下拉選單` 或
   `Reference`，**皆未量**。若要判定「這是表單各版本的通病」還是
   「只有某幾份如此」，需要那一步 —— 而 R-PMH20 正是禁止我在沒量之前
   說前者。

---

## 9. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 —— `BLANK` 未變 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回；故意失敗測試以假物件注入，未動工作簿 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— §2.4 只列語料與其指向，不提案、不歸納慣例 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | R-PMH19 母體 < 5 | **未觸發** —— 母體 **11** |
| 8 | 三項故意失敗有任一未被攔下 | **未觸發** —— **三項全部攔下**，且範圍向亦通過 |
| 9 | 機器分類與人讀結論不符且涉及「帶實質需求文字之節點被判為未引用」 | **未觸發** —— 集合完全相同、`other` = 0；唯一差異為 outline `1` 之分類邊界 |

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 04 — corpus criterion, write-back guards, full-workbook DV
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/PLAYBOOK.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/scripts/check_write_back.py \
           features/power_moding/scripts/classify_uncited_sections.py \
           features/power_moding/data/uncited_sections.tsv \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/04_corpus_and_assertions.md \
           features/power_moding/docs/upstream/04_corpus_and_assertions.md

git commit -- features/power_moding/ANOMALIES.md \
              features/power_moding/DECISIONS.md \
              features/power_moding/PLAYBOOK.md \
              features/power_moding/RULINGS.md \
              features/power_moding/feature.yaml \
              features/power_moding/scripts/check_write_back.py \
              features/power_moding/scripts/classify_uncited_sections.py \
              features/power_moding/data/uncited_sections.tsv \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/04_corpus_and_assertions.md \
              features/power_moding/docs/upstream/04_corpus_and_assertions.md
```

- 本輪**未觸及本 feature 目錄以外之任何檔案**（03 包之
  `features/comfort/ANOMALIES.md` 屬該輪）。
- `data/uncited_sections.tsv` 入版控（同 `recon_leaf_to_section.tsv` 之理由：
  它是可重跑之追溯產物，diff 即為 spec 匯出變動之訊號）。
- `scripts/new_feature.py` **未改**（03a §四之禁止項，仍在）。
- pathspec 逐項寫全名，未用萬用字元（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 10.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

本輪未執行任何 git 指令。

---

## 11. 本輪之全部工作區動作

| # | 動作 | 對象 |
|---|---|---|
| 1 | heredoc 追加 ＋ 就地改寫 | `RULINGS.md` —— 04 五條 ＋ 核對表 ＋ R-PMH10 之 `[PEI-REOPEN]` 標記（原文未動） |
| 2 | heredoc 新建 | `scripts/check_write_back.py`（本 feature 專屬） |
| 3 | 執行 | `check_write_back.py --self-test` —— 三次故意失敗 ＋ 一次範圍向 |
| 4 | heredoc 新建 | `scripts/classify_uncited_sections.py`（本 feature 專屬） |
| 5 | 執行 | `classify_uncited_sections.py` → `data/uncited_sections.tsv`（23 列） |
| 6 | Python 就地改寫 | `feature.yaml` —— `[PEI-REOPEN]` 註記、全簿 DV 說明、A-PMH10／12 警語、新增 `write_back_checks` 節 |
| 7 | Python 就地改寫 | `DECISIONS.md` —— 前言三欄改標 `[PEI-REOPEN]`、新增 Phase 6／7 前置阻斷項與寫回前檢查 |
| 8 | Python 就地改寫 | `PLAYBOOK.md` §6 —— 狀態板、Open rulings 表、Open PENDING anomalies 表 |
| 9 | heredoc 寫檔 | `ANOMALIES.md` —— A-PMH09 更正並 RESOLVED、A-PMH10 證據更正、新增 A-PMH11／12 |
| 10 | heredoc 寫檔 | `docs/upstream/04_corpus_and_assertions.md`（本檔） |
| 11 | heredoc 寫檔 | `docs/INDEX.md` 補本輪次列 |

**對任何工作簿之儲存格寫入：無。**
**對唯讀來源（`forms/`、`ASW-R2` 全樹）之寫入：無** ——
步驟 2 對 11 個交付件、步驟 5 對 2 個檔案皆為唯讀開啟。
**`scripts/new_feature.py` 未改。**
