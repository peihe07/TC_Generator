# 下放包 10 —— 交叉檢查結案、DECISIONS 合併、PROXI 改為需求驅動

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/10_decisions_merge.md`
- 前一包：`09_recon_crosscheck.md`（上繳已覆核，見 §一）

---

## 一、上繳包 09 之覆核

**核可，無退回項。** `recon.py` 跑通、17 項對照 16 相符，
七輪來第一次取得獨立管線之交叉檢查。四項具名。

### 1.1 §3.2 之如實回報 —— 越權的是我的授權書，不是它的改動

執行層報「授權寫**一處**，實際改動落在**四處**」，並逐處說明必要性，
且明白拒絕主張四處等於一處。

**該拒絕正確，而問題出在我。** 參數化在結構上不可能只有一處：
函式簽章、取值處、同函式內之訊息、以及呼叫處 —— 缺第四處則整個改動
惰性化。我寫「一處」時心裡想的是「一個行為」，寫出來的卻是一個
計數，兩者不同。

四處全部在授權之**行為範圍**內，予以追認。條文見 §四 R-G21。

### 1.2 §6 之 ETM 判準 —— 測完就否定，沒有繞路

`Used by` 含 `ETM` 之 100 列，keyword 命中率 **8.0%**；群外 77 列
**9.1%**；倍率 **0.88x**。**群內低於群外。**

執行層依停止條件 25 停手，未自行改判準。並順帶查出自己上輪的兩個錯
（索引錯位使 ETM 由 100 誤報為 50；「互斥且窮盡 69+117+269=446」
實為 455）。

其自評採認並升為條文（§四 R-G22）：

> 這次錯的是一句我親手打在表下的斷言，而那句話沒有任何程式在檢查它。

### 1.3 §5.2 之堅持 —— `[PEI]` 不得被機器降格為 `[PROPOSED]`

recon 標 `spec_reference: [PROPOSED: None]`，執行層維持既有之 `[PEI]`，
理由為「把一個無法提案之項標成已提案，會使它在簽核時無聲通過」。

**完全正確。** 這是本輪最重要的一次拒絕。條文見 §四 R-DM32。

### 1.4 §4.3 第 6 列 —— 我的理由又錯了一次

我在下放包 08 §2.3 寫「Display **無** `sys1_export`」。實測：
**Display 有 `sys1_export`**（SYS2，02 輪即已宣告），recon 回空 map 之
理由是 `no 'Outline Number' column`。

結果相同（空 map），理由不同。**這正是 R-G19 所指之形態**，
且這次是我犯的。若日後有人依「Display 無 sys1_export」推論
「所以不必比對 SYS2」，就會推錯。

---

## 二、三項待裁之處置

### 2.1 字元數 854,333 vs 907,382 —— 取 recon 之值，並記明其用途

兩數皆已由執行層重現，成因為不同抽取器對同一 `.docx` 之不同處理，
非計算錯誤。

**登記值取 854,333（pymupdf，即 `recon.py` 之探針）。** 三項理由：

1. 該數字之**用途是判斷有無文字層**，門檻為 500 字元
   （`survey_spec_text_layer()`）。854,333 與 907,382 皆遠超門檻，
   **兩者導出之結論相同：spec_mode D 成立**。差異不改變任何決定。
2. 跨 feature 之可比性由管線之探針提供；各 feature 各用自己的抽取器，
   數字就不能互相對照。
3. 自寫腳本之 907,382 **不作廢**，改記於 sidecar 之
   `measurement_conditions`，與 854,333 並列，註明兩者之抽取器與差異
   成因。

**同時記明一個命名陷阱**：`feature.yaml` 之欄位名為 `spec_pdf`，
而 Display 之該欄指向一份 `.docx`。欄名與內容不符，
`survey_spec_text_layer()` 之 docstring 亦以 PDF 為前提。
以 `A-DM26` 登記，**不改欄名**（改欄名會動到所有 feature）。

### 2.2 `DECISIONS.md` 與 `DECISIONS.new.md` —— 前者為權威

見 §四 R-DM32。合併為人工逐項，每一處分歧須留處置理由。

### 2.3 `estimated_test_time`（Q 欄）—— 非管線欄位，寫回不觸碰

`recon.py` 自身之註解已定其性質：
「Revision marker, not a pipeline field: present => rev C layout」。

故：**不加入 `feature.yaml` 之 `workbook.columns`，寫回一律不觸碰。**
其地位與 B 欄（公式欄，R-DM15）同 —— 存在、被辨識、不被寫入。
`feature.yaml` 加註一行說明，避免下一個人再問一次。

---

## 三、PROXI —— 由供給驅動改為需求驅動

ETM 判準否定後，執行層 §8 第 4 項之陳述成立：
**現在沒有任何合格的判準可用來排程那 446 列。**

**但這不是缺一個判準，是問錯了問題。**

前三輪的作法都是**從 PROXI 這一側出發**：446 列裡哪些可能跟 Display
有關？這條路要求在不知道需要什麼的情況下，先把 446 列分類完。
keyword、ETM、heading 三種嘗試全部失敗，不是因為判準不夠好，
而是因為**供給側沒有指向需求側的資訊**。

改為需求驅動：**TC 撰寫時，某個 leaf 需要一個前置條件，才去 PROXI
查那一個參數。** 查得即用（值域依 R-VS49 以 PROXI 表為權威），
查不得即依 R-G13 三要件登記 `LOOKUP_MISSES.md` 並開 DR。

三項後果：

1. `proxi_candidates.tsv` 之 446 列**保留為索引**（其 177 列之值域已查得，
   是有用的），但其 `related_leaf` 欄**停止嘗試填寫**，
   全欄語意改標 R-DM23 之 **(2) 未追查**，並註明「本欄不再由供給側填寫」。
2. `docs/proxi_triage_proposal.md` **撤回**（依 R-TM13 保留原文並加註）。
   三梯次、四類分割、停止點提案全部不再適用。
3. 已查得之三個連結（`DCSD_cfg`／`RVC_SK_PRSNT`，以及本輪順帶發現之
   `Splashscreen_Type` 與 `SWE-DM-003` 之相鄰）**保留為線索**，
   於 Phase 2 逐 leaf 判前置條件時優先查證，但**不因此取得
   Pre-Condition 之資格** —— 那仍受 §8.5 拘束（須為規格明載之
   觸發條件，非隱含環境穩定前提）。

DR-DM7（本專案 VF 代碼）**維持 OPEN**，但其急迫性下降：
需求驅動下，VF 只在某個具體參數有多值時才需要用來擇一。

---

## 四、裁決條文

```
R-G21（共用腳本之授權以行為界定，不以處數界定 —— 全域）
授權修改共用腳本時，授權書須以**行為**界定範圍，並列舉該行為所需之
編輯集合；不得以「一處」「一行」等計數表述界定。

理由：參數化在結構上不可能只有一處 —— 函式簽章、取值處、同函式內
之訊息、呼叫處，缺任一則改動惰性化。以計數界定會使忠實執行者
陷入「照做則越權、不照做則無效」之兩難。

授權書之應有形態：
  行為：<一句話描述改動後之行為差異>
  編輯集合：<逐處列舉，或「該行為所必需之最小集合」>
  不得動：<逐項列舉>
  驗收：<回歸範圍與判準>

實例（下放包 09 §二）：分析層寫「得修改之處：一處」，執行層實作為
四處並逐處說明必要性且拒絕主張四處等於一處。**執行層之處置正確，
缺陷在授權書。** 四處經追認皆在授權之行為範圍內。
```

```
R-G22（斷言式表述須由腳本產出 —— R-G20 之延伸，全域）
報告中凡出現「互斥」「窮盡」「合計」「涵蓋全部」「三者相加」等
**斷言式表述**者，其算式與驗證須由腳本輸出，不得以人手寫入。

理由：R-G20 所規制者為謄寫之數字，本條所規制者為**數字之間的關係
主張** —— 後者更危險，因為它讀起來像結論而非數據，讀者不會去驗算。

實例（上繳 09 §6.3）：執行層親手寫下「三梯次互斥且窮盡：
69 + 117 + 269 = 446」，實際三數相加為 **455**；且其中一梯之列數
另因索引錯位而錯（ETM 50 應為 100）。該句無任何程式在檢查。
更正後之互斥分割為 107 / 70 / 9 / 260，四數相加 = 446，
且 `lid_row` 之唯一性已另行驗證。
```

```
R-DM32（`DECISIONS.md` 之權威與 `[PEI]` 之不可降格）
既有之 `features/display/DECISIONS.md` 為**權威**；
`recon.py` 產出之 `DECISIONS.new.md` 為**證據**。
合併為人工逐項，每一處分歧須於合併後之檔中留下處置與理由。

**機器不得將 `[PEI]` 降格為 `[PROPOSED]`。** 兩者之差別不在內容
而在簽核時之行為：`[PROPOSED]` 未經修改即生效（canon §4），
`[PEI]` 必須被回答。把一個無法提案之項標成已提案，
會使它在簽核時無聲通過。

實例（上繳 09 §5.2）：`spec_reference` 一項，`recon.py` 依
`spec_reference_template` 為 null 機械讀出 `[PROPOSED: None]`；
既有 `DECISIONS.md` 標 `[PEI]`，理由為 mode D 要求查得，
而 leaf → CFTS 條號之橋樑不存在（A-DM10b），**故無法提案**。
**維持 `[PEI]`。**

反向亦然：`recon.py` 所提之項若為既有檔所無（本輪之
safety attributes、batch plan、版面 revision），一律以
`[PROPOSED]` 併入，不自動升格為 `[PEI]`。
```

```
R-DM33（PROXI 改為需求驅動）
PROXI 之對照**停止由供給側進行**。`proxi_candidates.tsv` 之
446 列保留為索引（其中 177 列之值域已查得），
`related_leaf` 欄停止填寫，全欄語意標 R-DM23 之 (2) 未追查，
並於 sidecar 註明「本欄不再由供給側填寫」。

改為：TC 撰寫時某 leaf 需要一個前置條件，才去 PROXI 查那一個參數。
查得即用（值域依 R-VS49 以 PROXI 表為權威）；查不得則依 R-G13
三要件登記 `LOOKUP_MISSES.md` 並開 DR。

理由：三輪嘗試（keyword 相鄰、heading、`Used by NODE` 含 ETM）
全部失敗。ETM 之實測為群內命中率 8.0%、群外 9.1%、倍率 0.88x ——
**群內低於群外**。三次失敗不是判準不夠好，是供給側沒有指向需求側
之資訊：在不知道需要什麼之前，446 列分不出來。

`docs/proxi_triage_proposal.md` 撤回，依 R-TM13 保留原文並加註。
已查得之線索（`DCSD_cfg`／`RVC_SK_PRSNT`／`Splashscreen_Type`）
保留供 Phase 2 優先查證，但不因此取得 Pre-Condition 之資格 ——
該資格仍受 §8.5 拘束。
```

```
R-DM34（`estimated_test_time` 與 `spec_pdf` 之兩項記明）
(a) 036 母本之 Q 欄 `Estimated Test Time (mins)` 為版面 revision 標記，
    非管線欄位（`recon.py` 自身註解已定其性質）。
    **不加入 `feature.yaml` 之 `workbook.columns`，寫回一律不觸碰。**
    其地位與 B 欄（公式欄，R-DM15）同：存在、被辨識、不被寫入。

(b) `feature.yaml` 之 `paths.spec_pdf` 於本 feature 指向一份 `.docx`，
    欄名與內容不符；`survey_spec_text_layer()` 之 docstring 亦以 PDF
    為前提。**不改欄名**（會動到所有 feature），以 A-DM26 登記。
    引用該欄時須知其內容未必為 PDF。
```

---

## 五、作業步驟

1. 抄錄 §四五條入指定檔（`R-G21`／`R-G22` 入
   `docs/fw036/RULINGS_LEDGER.md`；`R-DM32`–`R-DM34` 入
   `features/display/RULINGS.md`），核對表依 R-G20 由腳本產出。

2. **合併 `DECISIONS.new.md` 入 `DECISIONS.md`**（R-DM32）：
   - 逐項對照，`recon.py` 多出之項以 `[PROPOSED]` 併入
   - `spec_reference` 維持 `[PEI]`
   - 每一處分歧留處置與理由
   - **合併後 `DECISIONS.new.md` 依 R-TM13 保留**，加註其已併入
   - 合併後之檔**不得含任何未標記之項**：逐項須為
     `[AUTO]`／`[PROPOSED]`／`[PEI]`／`[RULED]` 四者之一

3. **§2.1 之字元數處置**：登記值取 854,333；907,382 記入
   `probe_spec_mode` 之 sidecar `measurement_conditions`，兩者並列
   並註明抽取器與差異成因。以 `A-DM26` 登記 `spec_pdf` 之命名陷阱。

4. **依 R-DM33 處理 PROXI**：`related_leaf` 欄語意改標、sidecar 加註、
   `proxi_triage_proposal.md` 加註撤回（原文保留）。
   `docs/INDEX.md` 標其為 SUPERSEDED。

5. **依 R-DM34(a) 於 `feature.yaml` 加註** Q 欄與 B 欄皆為
   「辨識但不寫入」，各附其理由與條號。

6. **Q2／Q3 之裁定材料整備**（本輪之主要交付）：
   產出 `features/display/docs/Q2_Q3_briefing.md`，供 Pei 裁定用。
   內容為**已量測之事實**，不含提案以外之推論：

   **Q2（驗證範圍）須含**
   - 037 之 8 leaves 全集與其 Sub Categorization
   - SYS2 FR 母體 80 列
   - `candidate_from` 分布：heading 4 列（→ 004／005）、
     glossary 12 列（→ 007／008）、無候選 64 列
   - **64 列無候選之語意為 R-DM23 之 (3) 方法界線**，須逐字寫明
     其不等於「不屬於本 feature 範圍」
   - id 層級對應為 0 列（A-DM2，逐字比對）
   - 其餘四個 leaf（001／002／003／006）候選為 0，且須寫明
     其成因為「無逐字錨」而非「SYS2 無對應需求」
   - 選項 A（僅 8 leaves）與選項 B（含 SYS2 之 80 條）各自之
     交付形態與已知代價，**不含分析層之偏好**

   **Q3（`req_id` 形態）須含**
   - `SWE-DM-001` 於 `SWE1 Requirements` 分頁（需求本體）
   - `SWE1-DM-001` 於 `SYS2 Traceability` 分頁（衍生索引）
   - 兩者於 037 內之出現次數
   - 對 TestRail／036 `Requirement or Design ID` 欄之影響

7. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用既有各條（1–25），另加：

26. 步驟 2 之合併若出現任一項無法歸入
    `[AUTO]`／`[PROPOSED]`／`[PEI]`／`[RULED]` 四者 → 停並回報。
27. 步驟 6 之 briefing 若需要寫入任何未經量測之陳述才能說明清楚
    → 該處標「未量測」，不得補推論。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/10_decisions_merge.md`）

1. §四五條之抄錄核對表（腳本產出）
2. 合併後之 `DECISIONS.md` 全文，逐項標記齊備
3. 分歧處置表（每處之處置與理由）
4. 字元數處置與 A-DM26 全文
5. PROXI 之 R-DM33 處理結果
6. `feature.yaml` 之 Q 欄／B 欄註記
7. `Q2_Q3_briefing.md` 全文
8. **「本包是否仍有該驗而未驗者」之獨立判斷**
9. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-G21 | 共用腳本授權以行為界定，不以處數界定 | 全域 | 是 |
| R-G22 | 斷言式表述（互斥／窮盡／合計）須由腳本產出 | 全域 | 是 |
| R-DM32 | `DECISIONS.md` 為權威；`[PEI]` 不得被機器降格 | Display | 是 |
| R-DM33 | PROXI 改為需求驅動；三梯次提案撤回 | Display | 是 |
| R-DM34 | Q 欄不寫入；`spec_pdf` 命名陷阱記明 | Display | 是 |

五條皆為獨立單一事項。
