# 下放包 15 —— Q2／Q3 定案、四項 DR 之處置、素材落地

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display
- 對應上繳：`features/display/docs/upstream/15_scope_settled.md`
- 前一包：`14_mapping_audit.md`（其上繳尚未回；本包不取代該包，兩包並行）

> **本包解除等待狀態。** 下放包 14 §六之三項拘束於本包生效後解除。
> 惟 14 包之作業步驟仍須完成，其上繳與本包之上繳可合併為一份。

---

## 一、Pei 2026-08-25 之裁定（逐項落條）

### 1.1 Q2 —— 定案

Pei 原話：

> 037 也界定要不要測才對啊，因為有可能 SYS2 的範圍已經判給 SYSTEM 測試，
> 而我這裡是 software

裁定內容見 §三 R-DM41。**選項 B 排除；範圍取 037 之 8 個 leaf。**

### 1.2 Q3 —— 定案

`req_id` 形態取 **`SWE1-DM-001`**（`SYS2 Traceability` 分頁之寫法）。
見 §三 R-DM42。

### 1.3 DR-DM8 —— 定案

「以訊號名稱為主」。見 §三 R-DM43。

### 1.4 素材落地

| DR | Pei 所指之檔 | 分析層實測 | 處置 |
|---|---|---|---|
| DR-DM2 | `forms/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`<br>`forms/Pop Up List HMI R1 (26PI).xlsx` | **兩檔皆存在**；內容切中（見 §二） | **可望結案**，待執行層完成 §四步驟 5 |
| DR-DM7 | `forms/PROXI_HDCC27_R3_20250424.xlsx` | 為格式／標準文件，非已填值之實例 | **建議結案**，理由見 §三 R-DM44 |
| DR-DM3 | `features/display/inputs/SYS2_CFTS043_…SYSRA_CFTS043_V01.xlsx` | **內容為 HVAC，非 Display** | **不結案**，見 §二 2.3 |

---

## 二、分析層之實測（對照向，執行層須獨立重算）

量測條件：`openpyxl`、`read_only=True`、`data_only=True`；
字串比對逐字、區分大小寫。

### 2.1 SYS2 自帶之 `SW/HW/System` 欄 —— Q2 之判準已在資料裡

Pei 之推理「SYS2 的範圍可能已判給 SYSTEM 測試」**可量測**：
SYS2 `Basic Report` 之第 13 欄欄名逐字為

```
SYS2 SW/HW/System (如果是HW+SW，就選System)
( software, hardware, or system (both software and hardware).)
```

對 80 列 FR 母體之交叉：

| 值 | 列數 |
|---|---|
| `System` | **47** |
| `HW` | **26** |
| `SW` | **7** |

7 個 `SW` 列之列號：r17、r18、r245–r249。

**且 16 個產生候選之列全部為 `System`，無一為 `SW`**
（heading 錨之 r31–r34、glossary 錨之 r37/41/42/44/45/52/53/54/
213/217/219/226）。

> ⚠ **一項不得跨過的限定**：該欄之語意依其欄名為「由 SW／HW／
> 兩者共同實現」，**不是「由哪一個測試層級驗證」**。
> `System` 表示 HW 與 SW 皆涉入，故 47 列**不因此自動排除於軟體測試之外**。
>
> 可據以確定者只有一項：**26 列標 `HW`**，其為硬體實現，
> 與 SWE.6 之標的無涉。其餘 54 列（47 System + 7 SW）之測試層級歸屬
> **未量測** —— 該資訊不在四份素材內。

### 2.2 Pop Up List 兩檔 —— DR-DM2 之內容切中

`forms/Pop Up List HMI R1 (26PI).xlsx`，分頁 `Main`／`Templates`／
`Drop Down Fields`。`Main` 之表頭在 r2，資料自 r3 起，
符合 `PU\d{4}` 之列 **1,331**。

欄位含 **`Timeout (sec)`**（非 `N/A` 者 **538** 列）與 **`Category`**。
`Category` 之詞彙自 `Drop Down Fields` 分頁取得，含
`1P`／`1T`／`2`…`12`／`RVC`／`X`／`VR`／`SL`／`Custom` ——
**即 popup 之優先序分類**。分布：`2` 1104、`3` 73、`RVC` 27、`SL` 26、
`VR` 15、`X` 9、`1P` 6、`RVC-X` 5、`1T` 3。

與 Display 直接相關者（逐字命中，非推定）：

| PU | Module | Timeout | Category | 訊息（節錄） | 相關 leaf |
|---|---|---|---|---|---|
| **PU0130** | Temperature | **10** | **1T** | `Screen is Hot.` / `Display turning off to cool down.` | SWE-DM-005 |
| **PU0517** | Temperature | **10** | **1T** | `Screen is Hot.` / `Display brightness has been reduced.` | SWE-DM-004 |
| PU0008 | Temperature | N/A | 1T | `System is Hot.` … | SWE-DM-004／005 |
| **PU1322** | **FPDM** | **3** | 2 | `System is Hot.` … | 與 A-DM15 之 FPDM 相關 |

`Category` 另有 **`RVC`** 一個獨立類別（27 列），與 SWE-DM-007／008 相關。

> **上表為線索，不是裁定。** 哪一個 PU 屬哪一個 leaf 之驗證範圍，
> 須依 §8.5（前置條件之資格）與 §8.2.1（不得擴入 sibling Req）
> 於 Phase 2 逐條判定。**本輪不得將任何 PU id 或 timeout 值寫入 TC。**

Priority Matrix PDF 之內容**本輪未讀** —— 其為 `Category` 之排序依據，
由執行層於 §四步驟 5 讀取。

### 2.3 DR-DM3 所指之檔 —— **內容為 HVAC，不答本 DR**

`features/display/inputs/SYS2_CFTS043_FM-WI-FSM-035-A02 …SYSRA_CFTS043_V01.xlsx`

| 項 | 實測 |
|---|---|
| 分頁 | `Basic Report`（408 列 × 63 欄）／`Polarion`／`_polarion` |
| 資料列 | **406** |
| `SYS2 Sys-RA-Feature-ID` 形態 | **`SYS-RA-HVAC-{n}` × 405**（另 1 列為空） |
| 全檔逐字出現 `SYS-RA-DISP` | **0** |
| 全檔逐字出現 `SYS-DISP` | **0** |
| 全檔逐字出現 `SWE-DM` / `SWE1-DM` | **0 / 0** |
| 全檔逐字出現 `DISP` | **0** |
| `Category` | Functional Requirement 311／Heading 63／Information 30／Out of Scope 1 |
| `SW/HW/System` | System 245／SW 66 |
| `VF章節`／`VF後綴`／`EE Architecture` 三欄 | **406 列全空** |
| ASIL／FTTI／Safety 相關欄名 | **0 個** |

**`Display` 一字出現 477 次，但全部在 Description 之散文中**，
與 id 命名空間無關。

**結論：該檔為 CFTS_043（HVAC）之技術安全需求分析報告，
不含 Display 之任何 id。DR-DM3 所求者為
「`SYS-RA-DISP-*` ↔ SYS2 之對應表，或含 `DISP` id 之 SYS2 版本」，
本檔兩者皆非。DR-DM3 維持 OPEN。**

執行層**不得**將該檔納入 `paths:`／`reference:`／素材台帳，
亦不得自其取任何值。其存在以 **A-DM31** 登記（見 §四步驟 4）。

> 記此事之理由：這是本 feature 第二次「檔名看起來對而內容不是」——
> 第一次是 02 輪之 037 檔名連字號（R-DM11）。差別在於這次
> **檔名確實是一份真實存在且相關領域的文件**，只是 CFTS 號不同。
> 若不逐字驗 id 命名空間就收下，DR-DM3 會被錯誤結案，
> 而追溯鏈仍然是斷的。

### 2.4 PROXI R3 —— 為格式文件，非已填值之實例

`Cover` 分頁逐字載：`FCA US LLC`／`Support Document`／
`27MY HDCC SPECIFIC PROXI TABLE`；`Header` 分頁載 `HDCC27 - Draft`。
`Help` 分頁為各欄之填寫規則（義／英雙語）。

即：本檔定義**參數配置與其值域**，不含任一具體車輛之已填值，
亦不載本專案之 VF 代碼。`Used by NODE(VFXXX)` 欄所列之 VF 為
「哪些 VF 會用到此參數」之通則，非「本專案是哪個 VF」。

處置見 §三 R-DM44。

---

## 三、裁決條文

```
R-DM41（Q2 定案 —— 範圍取 037 之 8 個 leaf）
Pei 2026-08-25 裁定：驗證範圍取 037 之 8 個 leaf
（`SWE-DM-001`…`008`）。**選項 B（以 SYS2 之 80 列 FR 為母體）排除。**

裁定理由（Pei 原話）：「037 也界定要不要測才對啊，因為有可能 SYS2
的範圍已經判給 SYSTEM 測試，而我這裡是 software」。

即：037 為 SWE.1 之交付物，其界定者不只「測什麼」，亦包含
**「要不要測」** —— 一條 SYS 層需求未進入 037，可能正是因為它已
分派給系統測試層級，而 SWE.6 之標的是軟體。

三項隨附拘束：

(a) **SYS2 仍為內容來源**，不因本條而失效。R-DM14（值域來源）、
    R-DM17（三段解析鏈）、R-DM8 再判定（hot 行為之併讀）皆維持有效。
    037 界定「測什麼／要不要測」，SYS2 供給「怎麼測」。

(b) **借用 SYS2 某列之內容，不得使該列之驗證目的進入 TC。**
    TC 之驗證目標一律為其所屬之 SWE-DM leaf；SYS2 列僅供其訊號名、
    值域、狀態轉換之取材（§8.2.1、§8.4.2）。

(c) **揭露義務不因範圍縮小而消失**（R-DM7 之揭露義務未廢止）。
    交付時須附「037 leaf ↔ SYS2 列」之對照表，並載明：
      - 以 id 為據之對應 **0 列**（A-DM2）
      - 候選：004／005 各 4 列、007／008 各 12 列、其餘四 leaf **0 列**
      - **64 列無候選之語意為 R-DM23 之 (3) 方法界線**，
        不等於「不屬於本 feature 範圍」
      - SYS2 之 `SW/HW/System` 欄對 80 列 FR 之分布：
        System 47／HW 26／SW 7；**該欄之語意為「由誰實現」，
        非「由哪個測試層級驗證」**，故不得以其單獨論證範圍
```

```
R-DM42（Q3 定案 —— req_id 形態）
Pei 2026-08-25 裁定：`req_id` 取 **`SWE1-DM-{nnn}`** 形態
（037 `SYS2 Traceability` 分頁之寫法），填入 036 之 D 欄
`Requirement or Design ID`。

八個值為 `SWE1-DM-001` … `SWE1-DM-008`。

三項隨附：
(a) `SWE-DM-{nnn}`（`SWE1 Requirements` 分頁之寫法）**不入任何交付欄位**；
    其於 `reasoning`、`ANOMALIES.md`、內部資料檔中之引用不受限制，
    但須與 `SWE1-DM-` 明確區分，不得混用。
(b) **A-DM1 不因本裁定結案** —— 該條記的是「037 兩個分頁對同一物件
    使用兩種寫法」，屬上游文件內部不一致，與「我們採哪一個」是兩件事。
    仍須向上游反映。
(c) `recon_assertions` 之 `functional_requirement_count: 8` 不受影響
    （leaf 數未變，僅書寫形態改變）。
```

```
R-DM43（DR-DM8 定案 —— 以訊號名稱為主）
Pei 2026-08-25 裁定：037 之 `DISPLAY_ON`／`DISPLAY_OFF`
與 SYS2／DBC 之 `DISP_ON`／`DISP_OFF`，**以訊號名稱為主**。

即：TC 之 Procedure 與 Expected Result 一律採 `DISP_ON`／`DISP_OFF`
（DBC `DCSD_DISP_STAT` 之 `VAL_` 標籤側）。

本條與 R-6 之既有規定一致：「訊號名以 DBC 為準；來源文件與 DBC
大小寫不一致時，步驟採 DBC 寫法，verbatim 上半仍保留來源原文」。
**037 原文於 `test_item` 上半之 verbatim 摘句中仍寫 `DISPLAY_ON`**，
不得改寫 —— 本條規制的是步驟與預期結果，不是引文。

DR-DM8 **結案**。A-DM18 之該項隨之結案；A-DM18 之其餘部分
（八條無值、八條併句）不受影響。
```

```
R-DM44（DR-DM7 結案 —— 需求已由 R-DM33 消滅）
`forms/PROXI_HDCC27_R3_20250424.xlsx` 經實測為**格式／標準文件**
（`Cover`：`27MY HDCC SPECIFIC PROXI TABLE`、`Support Document`；
`Header`：`HDCC27 - Draft`），不含任一具體車輛之已填值，
亦不載本專案之 VF 代碼。

DR-DM7 原求「本專案之 VF 代碼，或已填值之 PROXI 實例檔」，
其目的為**收斂 446 列之供給側母體**（`Used by NODE(VFXXX)` 之篩選）。
**該目的已由 R-DM33 消滅** —— PROXI 改為需求驅動後，
不再需要對 446 列分類，只在某 leaf 需要某參數時查該一個參數。

處置：**DR-DM7 結案**，理由記為「所求之用途已由 R-DM33 取消，
非取得所求之物」。A-DM20 改標 RESOLVED-BY-SCOPE-CHANGE，
不標 RESOLVED。

**重開條件**：若 Phase 2 之逐 leaf 查詢中，某參數之值域在
PROXI 中依 VF 而異，則 VF 代碼重新成為必要，DR-DM7 以新編號重開。
```

---

## 四、作業步驟

1. 抄錄 §三四條入 `features/display/RULINGS.md`，核對表由腳本產出。

2. **`DECISIONS.md` 依裁定更新**：
   - Q2／Q3 自 `[PEI]` 改為已裁，記其裁定日期與原話
   - `Contested attributions`（Q3）隨之結案
   - `spec_reference` 一項：分析層另提案
     **`CFTS020-{7位ObjectID}`**（canon §10.7(a)；CFTS_020 本文之條號
     `{4820281}` 等實測為 7 位）。該項自 `[PEI]` 改為
     `[PROPOSED: CFTS020-{ObjectID}，逐 leaf 之 ObjectID 於 Phase 2 查得]`
   - **不動 Sign-off 區塊** —— 簽核為 Pei 之動作

3. **Pop Up List 兩檔納入素材**（DR-DM2）：
   - 依 R-DM38 之判準，兩檔之變動會使 popup 之 timeout 與優先序失效，
     故**納入 `reference:` 節**並登台帳
   - `feature.yaml` 之 `paths.popup_list` 自 `null` 改為該 xlsx
   - 重跑 `verify_reference_binding.py`，**十一項**逐項回報
   - `lint.popup_ids` 暫維持 `[]`，待 Phase 2 逐 leaf 判定後填入

4. **`SYS2_CFTS043 …SYSRA` 一檔以 A-DM31 登記**：
   - 記 §2.3 之全部實測值
   - **不納入 `paths:`／`reference:`／素材台帳，不自其取值**
   - DR-DM3 維持 OPEN，其 `Status` 欄加註「2026-08-25 曾指定
     CFTS043 SYSRA，實測為 HVAC（`SYS-RA-HVAC-*` × 405，`DISP` 0 次），
     不答本 DR」
   - **該檔現位於 `inputs/` 而不受任何綁定檢查** —— 此本身為一項風險
     （日後有人以為它是本 feature 之素材）。處置提案入上繳包，
     **不自行搬動或刪除**（檔案動作屬 Pei）

5. **Priority Matrix PDF 與 Pop Up List 之併讀**（DR-DM2 之結案條件）：
   - 讀 `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`，
     取 `Category` 詞彙（`1P`／`1T`／`2`…／`RVC`／`X`／`VR`／`SL`）之
     **排序關係**
   - 與 xlsx 之 `Drop Down Fields` 分頁逐字比對其詞彙是否一致；
     不一致者登記，**不擇一**
   - 輸出 `data/popup_priority.tsv`（欄位：`category`／`rank`／
     `source_locator`／`note`）與其 sidecar
   - **不得將任何 PU id 或 timeout 值寫入 TC**；本步驟為建立索引

6. **重跑 `recon.py`**，確認 `functional_requirement_count: 8` 仍 PASS，
   且 `req_id` 形態之改變未影響任何 `[AUTO]` 值。

7. 完成下放包 14 之作業步驟（若尚未完成），其上繳可與本包合併。

8. 更新 `docs/INDEX.md`。

---

## 五、停止條件

沿用既有各條（1–36），另加：

37. 步驟 5 若發現 PDF 之 `Category` 詞彙與 xlsx 之 `Drop Down Fields`
    **不一致** → 兩者並列登記並停手回報，不得擇一。
38. 步驟 3 之十一項綁定若任一項不符 → 停並回報，不得更新宣告值。
39. 任何步驟若需要自 `SYS2_CFTS043 …SYSRA` 檔取值才能繼續 →
    停並回報（該檔不在本 feature 之素材內，R-DM41 之範圍亦不含 HVAC）。

**全部 git 操作屬 Pei。檔案之搬動、刪除、改名亦屬 Pei。**

---

## 六、上繳包要求（`docs/upstream/15_scope_settled.md`）

1. §三四條之抄錄核對表（腳本產出）
2. `DECISIONS.md` 更新後之 §1–§7 與待裁清單
3. `verify_reference_binding.py` 十一項輸出（含 `entries: 11`，R-G26）
4. `A-DM31` 全文與 SYS2_CFTS043 之獨立重算
5. `data/popup_priority.tsv` 與 PDF／xlsx 詞彙比對結果
6. `recon.py` 重跑結果
7. 下放包 14 各步驟之產出（若合併上繳）
8. **「本包是否仍有該驗而未驗者」之獨立判斷**
9. 建議之 commit 訊息與 pathspec（不執行）

---

## 七、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-DM41 | Q2 定案：範圍取 8 leaf；SYS2 仍為內容來源；揭露義務不變 | 是 |
| R-DM42 | Q3 定案：`req_id` 取 `SWE1-DM-{nnn}`；A-DM1 不結案 | 是 |
| R-DM43 | DR-DM8 定案：以訊號名稱為主；verbatim 引文不改寫 | 是 |
| R-DM44 | DR-DM7 結案：所求之用途已由 R-DM33 取消 | 是 |

四條皆為獨立單一事項。
