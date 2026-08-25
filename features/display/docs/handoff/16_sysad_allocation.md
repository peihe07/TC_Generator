# 下放包 16 —— SYS3 之分派表：十四輪來第一條 id 層級橋樑

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display
- 對應上繳：`features/display/docs/upstream/16_sysad_allocation.md`
- 前一包：`15_scope_settled.md`（其上繳未回；本包不取代 14／15，三包並行）

---

## 一、緣起

Pei 2026-08-25 指向 `SYS3_CFTS_020_display_…SYSAD_v1.0.docx`。
分析層實測結果分兩半：**答不了 DR-DM3，但答了一個十四輪來沒人回答的問題。**

---

## 二、分析層實測（對照向，執行層須獨立重算）

量測條件：`python-docx` 1.2.0；文字取自 `document.paragraphs`
與全部 `tables` 之 `cell.text`；比對逐字、區分大小寫。

### 2.1 整體

| 項 | 值 |
|---|---|
| 段落 | 311 |
| 表格 | **44** |
| 表格儲存格 | 1,361 |
| 純文字總長 | 58,426 字元 |

id 命名空間逐字清點：

| 樣式 | 出現次數 |
|---|---|
| `SYS-RA-DISP` | **0** |
| `SYS-DISP` | **0** |
| `SWE-DM` / `SWE1-DM` | **0 / 0** |
| `SYS2-RA` | **0** |
| **`SYS-RA-DM`** | **68** |
| `{7 位 ObjectID}` | **0** |
| `{CFTSnnn-mmm}` 外部引用 | **0** |

### 2.2 DR-DM3 —— 不答

DR-DM3 求「`SYS-RA-DISP-*` ↔ SYS2 之對應表，或含 `DISP` id 之
SYS2 版本」。本檔之 `SYS-RA-DISP` 為 **0 次**。**DR-DM3 維持 OPEN。**

> 本 feature 至此第三次「檔名對而內容不答該題」：
> 02 輪之連字號（R-DM11）、CFTS043 之 HVAC（A-DM31）、本次。
> 三次之成因各異，共同點是**若不逐字驗 id 命名空間就會誤結案**。

### 2.3 但本檔有兩張表，是十四輪來第一條 id 層級橋樑

**表 31 —— 分派表**（10 列 × 4 欄）

欄名逐字：`System Requirement ID`／`SYSAD-ID`／`% of allocation`／`Comments`

九個 SYSAD 元件，分派逐字如下（`% of allocation` 皆為 `100%`）：

| SYSAD-ID | n | SYS-RA-DM ids |
|---|---|---|
| `SYSAD-DCSD` | 12 | 012, 025, 027, 031, 032, 053, 057, 058, 059, 060, 066, 068 |
| `SYSAD-TMS` | 4 | **030, 031, 032, 033** |
| `SYSAD-RVC-STREAM` | 6 | 036, 040, 041, 043, 051, 052 |
| `SYSAD-HMI` | 5 | 038, 044, 046, 048, 055 |
| `SYSAD-LVDS` | 3 | 016, 064, 070 |
| `SYSAD-TOUCH` | 3 | 065, 067, 068 |
| `SYSAD-WMS` | 2 | 038, 040 |
| `SYSAD-VCPU` | 1 | 017 |
| `SYSAD-DISPLAY-HMI-WARNINGS` | 1 | 030 |

相異 id **31**。

**表 6 —— 需求屬性表**（32 列 × 6 欄）

欄名逐字：`SG ID`／`FSR ID`／`Requirement ID (Sys-RA-Feature-ID)`／
`Requirement Title`／`Categorization`／`ASIL Level`

| 項 | 實測 |
|---|---|
| 資料列 | **31**（與表 31 之 id 集合相同） |
| `Categorization` | `Functional` **31/31** |
| **`ASIL Level`** | **`QM` 31/31** |
| `SG ID` 非空 | **0** |
| `FSR ID` 非空 | **0** |

### 2.4 與 SYS2 之交叉 —— 完全含攝

31 個被分派之 id 對 SYS2 `Basic Report`：

| 項 | 值 |
|---|---|
| 落在 **80 列 FR 母體**內 | **31 / 31** |
| 存在於 SYS2 但非 FR | **0** |
| SYS2 中查無 | **0** |

**完全含攝，無一例外。**

### 2.5 與 16 個候選列之交叉

| 候選列 | SYS2 id | 在分派表中 | `SW/HW/System` |
|---|---|---|---|
| r31–r34（heading 錨，→ 004／005） | SYS-RA-DM-030…033 | **YES ×4** | System |
| r37/41/42/44/45/52/53/54（glossary 錨，→ 007／008） | SYS-RA-DM-036/040/041/043/044/051/052/053 | **YES ×8** | System |
| r213/217/219/226（glossary 錨） | SYS2-RA-212/216/218/225 | **no ×4** | System |

**16 個候選中 12 個被分派至軟體元件**；未被分派之 4 個全部落在
`SYS2-RA-*` 區段（即上繳 06 §5.1 所指之「後半段節點名大量重複」之處，
其是否為前半段之副本仍未查證）。

**且 r31–r34 之四個 id 恰為 `SYSAD-TMS`（Thermal management service）
之全部分派**——這與 heading 錨（`'Hot Algorithm'` 逐字）之結果
**由完全獨立之路徑得到同一組列**。

---

## 三、三項後果

### 3.1 Q2 之揭露義務取得更好的量（R-DM41(c)）

R-DM41(c) 要求交付時揭露 SYS2 之涵蓋狀況，其中一項為
`SW/HW/System` 欄之 System 47／HW 26／SW 7 —— 而該欄之語意為
「由誰實現」，**不能單獨論證測試層級歸屬**（我在 R-DM41(c) 已加此限定）。

SYS3 之分派表提供一個**更直接、且為 id 層級逐字**的量：
**80 列 FR 中有 31 列被明確分派至軟體架構元件，分派比例皆為 100%。**

此量不受「System 表示 HW+SW 共同實現」之語意問題影響 ——
分派表講的就是軟體架構元件。

**惟仍有其限定**：分派表所列者為「哪些 SYS 需求由哪個 SW 元件實現」，
**不等於「哪些應由 SWE.6 驗證」**。其餘 49 列未出現於分派表，
其成因（未分派 / 分派給硬體 / 本表不完整）**未量測**。

### 3.2 `Safety attributes` 一項之依據須更正

`DECISIONS.md` §3 之 `Safety attributes (ASIL/FTTI): [PROPOSED]` 記
「**受裁之來源不帶 ASIL／FTTI 欄**，故 SYS2／SYSRA 之安全層不進入
追溯鏈」。

該敘述對 037 成立，對 **SYS3 不成立** —— SYS3 表 6 有 `ASIL Level` 欄，
31/31 為 `QM`，另有 `SG ID`／`FSR ID` 兩欄（皆空）。

**結論可能不變**（`QM` 表示無安全需求，`SG ID`／`FSR ID` 全空
表示無安全目標與功能安全需求掛在這些條上），**但依據錯了**：
不是「來源不帶該欄」，而是「來源帶該欄且其值為 QM」。

兩者之差別在於：前者是「查不到」，後者是「查到了，答案是沒有」。
依 R-G19，理由與數字須分別成立。

### 3.3 SYSAD 元件名與 037 之 Sub Categorization —— **不得作為錨**

九個 SYSAD 元件名與 037 八個 leaf 之 Sub Categorization 語意上明顯相鄰
（如 `SYSAD-TMS` ↔ `Thermal Management`、`SYSAD-RVC-STREAM` ↔
`RVC Management`）。

**但兩者逐字不等**，且無 `(...)` 並列出處可依 R-DM22 建 glossary 條目。
依 R-DM13／R-G27，**不得以語意相近建立映射**。

本包**只記其存在，不建映射**。若 Phase 2 需要該映射，
須先有逐字依據（例如上游確認之對照表 → 新 DR）。

---

## 四、裁決條文

```
R-DM45（SYS3 之地位：軟體分派之 id 層級證據）
`SYS3_CFTS_020_display_…SYSAD_v1.0.docx` 表 31（`System Requirement
ID` → `SYSAD-ID` → `% of allocation`）為本 feature 目前**唯一**
id 層級逐字之軟體分派證據。

實測（分析層 2026-08-25，執行層須獨立重算）：
  9 個 SYSAD 元件、31 個相異 `SYS-RA-DM-*` id、分派比例皆 100%
  31/31 落在 SYS2 之 80 列 FR 母體內，0 查無、0 非 FR
  16 個候選列中 12 個在分派表內（未在者 4 個皆為 `SYS2-RA-*` 區段）

用途二項：
(a) 供 R-DM41(c) 之揭露 —— 以「80 列中 31 列明確分派至軟體元件」
    取代（並非廢止）`SW/HW/System` 欄之 System 47／HW 26／SW 7。
    兩個量並列揭露，因其回答的是不同的問題。
(b) 供 Phase 2 判定某 SYS2 列之內容是否可取用於某 leaf 之 TC ——
    **僅為佐證，非授權**。取用之正當性仍依 R-DM41(a)(b)。

三項不得為之：
(1) 不得以 SYSAD 元件名與 037 之 Sub Categorization 語意相近
    建立 leaf ↔ 元件映射（R-DM13／R-G27）
(2) 不得以「未出現於分派表」推論該列不屬軟體範圍 ——
    未出現之 49 列其成因未量測
(3) 不得以本表取代 037 之範圍界定（R-DM41 已定範圍為 8 leaf）
```

```
R-DM46（`Safety attributes` 之依據更正）
`DECISIONS.md` §3 之 `Safety attributes (ASIL/FTTI)` 一項，
其敘述「受裁之來源不帶 ASIL／FTTI 欄」**須更正**。

實測：037 確無該欄；**SYS3 表 6 有 `ASIL Level` 欄，31/31 為 `QM`**，
另有 `SG ID`／`FSR ID` 兩欄，兩欄之非空列數皆為 **0**。

更正後之敘述：
  037（受裁之範圍界定來源）不帶 ASIL／FTTI 欄；
  SYS3 帶 `ASIL Level` 欄，其值於 31 個被分派之需求上皆為 `QM`，
  且 `SG ID`／`FSR ID` 全空 ——
  即安全目標與功能安全需求未掛於這些條上。
  故安全層不進入追溯鏈。

`[PROPOSED]` 之結論不變，**依據由「查不到」改為「查到了，答案是沒有」**。
依 R-G19，理由與數字須分別成立；一個正確的結論配一個錯誤的理由，
會使下一個人依那個理由去推論別的事。
```

---

## 五、作業步驟

1. 抄錄 §四二條入 `features/display/RULINGS.md`，核對表由腳本產出。

2. **獨立重算 §2**：SYS3 之段落／表格／儲存格數、id 命名空間逐字清點、
   表 31 與表 6 之全文抽取。**量測條件自行宣告**（docx 之文字如何取、
   表格是否含巢狀）。

3. **產出 `data/sysad_allocation.tsv`** 與其 sidecar：
   欄位 `sysad_id | sys_ra_dm_id | pct | sys2_row | in_fr_population |
   is_candidate_row | candidate_leaf | comments`。
   `candidate_leaf` 欄之值一律取自既有之
   `coverage_sys2_vs_swe_dm.tsv`，**不得於本表新建任何映射**。

4. **依 R-DM46 更正 `DECISIONS.md`** 之 `Safety attributes` 敘述。
   `[PROPOSED]` 之結論不動。

5. **`A-DM31` 之更新**：DR-DM3 現有兩份被指定過而皆不答之檔
   （CFTS043 SYSRA、SYS3 SYSAD）。兩者性質不同：前者為他 feature 之
   文件（HVAC），後者為本 feature 之素材且有其他用途。
   **A-DM31 只記前者；SYS3 不登為異常**，其「不答 DR-DM3」一事
   記於 DR-DM3 之 Status 欄。

6. **SYS3 納入 `reference:` 已於 R-DM38 完成**（`sys3_sysad` 為九項之一），
   本步驟只需複驗其 sha256 仍相符。

7. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用既有各條（1–39），另加：

40. 步驟 3 若在 `sysad_allocation.tsv` 中出現任何**新建**之
    leaf ↔ 元件或 leaf ↔ SYS2 列映射 → 停並回報。
    本表之 `candidate_leaf` 只能是既有覆蓋表之搬運。
41. 步驟 2 之重算若 31 個 id 對 80 列 FR 母體之含攝**不是 31/31**
    → 停並回報。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/16_sysad_allocation.md`）

1. §四二條之抄錄核對表（腳本產出）
2. §2 之獨立重算（含量測條件自行宣告）
3. `data/sysad_allocation.tsv` 全文與 sidecar
4. `DECISIONS.md` 之 `Safety attributes` 更正後全文
5. DR-DM3 之 Status 更新
6. **「本包是否仍有該驗而未驗者」之獨立判斷**
7. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-DM45 | SYS3 分派表為唯一 id 層級軟體分派證據；三項不得為之 | 是 |
| R-DM46 | `Safety attributes` 之依據由「查不到」改為「查到了，答案是沒有」 | 是 |

兩條皆為獨立單一事項。
