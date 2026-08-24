# 下放包 12 —— profile 落檔、A-PMH13 定案與 Phase 4 首批

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/12_phase4_batch1.md`
- 前一包：[11_claim_evidence.md](11_claim_evidence.md)
  （上繳 [../upstream/11_claim_evidence.md](../upstream/11_claim_evidence.md)，已覆核）

---

## 一、11 包之覆核結果

**通過。** 九條停止條件逐條有實據。四項特別記明：

1. **`check_state_consistency.py` 之故意失敗精準指出 L7 與 L24 兩行** ——
   即 08a／09 兩輪間之實際不一致狀態。該檢查**不依賴標記清單**，
   只依賴「兩個互斥狀態同時存在」，故 10 包 §6 第 1 項所自陳之
   「回掃只抓找得到的標記」之限制，由它從另一側補上。
2. **`RULINGS.md`／`ANOMALIES.md` 採具名排除而非放寬判準** ——
   理由（多對象登記簿，全檔字串共現是正常且必然）成立，且其排除理由
   **每次執行皆印出**。停止條件 9 之設計意圖被正確理解。
3. **`--check-doc-sync` 之強化又在真實情境下攔下自己一次**（第二次）——
   改動該函式即改了程式，檢查當場 FAIL。**一個會抓到自己的檢查。**
4. **勘誤節之 R-PMH44(c) 驗證**：原句於檔內出現 **2** 次（原文 1 ＋ 勘誤引用 1），
   原文一字未改，並自載追加前後之兩個檔案雜湊。

**§6 第 1、2、5 三項自陳，全部採納為條文**（§三 R-PMH48／R-PMH49）。

---

## 二、Pei 之裁定（2026-08-24，逐字）

> 「上繳了 兩項都核可」

即：**profile 草案核可**（10 包 §四）＋ **A-PMH13 核可**（分析層提案
(ii)＋(iii) 併行）。**Phase 4 之兩項前置解除。**

---

## 三、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH46（profile 落檔授權 —— 一次性）
Pei 於 2026-08-24 核可 10 包 §四之 profile 草案。

授權執行層將該草案寫入
`docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md`，**一次**。

**寫入內容須為 10 包 §四之 markdown 區塊逐字**，另加 R-PMH47 所定之
兩處連帶修改（§0 與 §2 之「48 leaf」加註）。除該兩處外不得增刪改。

**明文不授權**：`docs/runtime/` 下任何其他檔案（含 canon、其他 feature
之 profile、`PROFILE_INTEGRATION.md`）。若 `PROFILE_INTEGRATION.md`
需登錄本 profile，**列為待裁，不逕行修改**。

驗證義務：寫入後以逐字比對證明其與 10 包 §四之區塊（加上兩處連帶）相同，
並附行數與 SHA256。本授權用畢即失效。
```

```
R-PMH47（A-PMH13 定案 —— (ii)＋(iii) 併行）
`SWE1-HMI-PM-028` 之處置如下：

(a) **判為 out of scope**（canon §8.4.2）—— 其內文逐字為
    `OFF2.) Please refer to CFTS009 for complete behavior.`，本身無可驗證
    行為；其行為定義於 CFTS009，屬他規格。**不得為其撰寫驗證 CFTS009
    行為之 TC**。
(b) **該列仍寫入工作簿並揭露**，不靜默丟棄（比照 R-VF12：460/1087
    out of SWE.1 scope 須揭露）。其欄位處置：
      `Test Set` = `Off Road Plus`（維持 R-PMH36 之分組）
      `Test Item` = 037 之 `Requirement Title` 逐字（`CFTS009 Behavior
        Reference`）＋ 括號下半（R-PMH36 之 profile §3.1 硬規則）
      `Test Procedure` / `Expected Result` = `PENDING: DR-PMH1 CFTS009
        所定之 Off Road+ power moding 行為`（§8.4.3 之缺件佔位，
        不得留空、不得填 NA）
      `Remarks` = `[BLOCKED-SPEC] Owner: CFTS009 — behavior defined in an
        external specification; no coverage found in any delivered workbook.`
        （形態沿用 Comfort 之既有慣例，非自創）
(c) **開 `DR-PMH1`** 向上游詢問：該 leaf 之行為應由 CFTS009 之 SWE 需求
    涵蓋，抑或本報告應自行載明其行為。DR 登記於本 feature 之
    `DATA_REQUESTS.md`，每包上繳附未結 DR 清單。

**含 PENDING 之工作簿不得出貨**（§8.4.3）—— 交付前須 DR-PMH1 結案，
或由 Pei 裁定降轉。

**連帶修改（兩處）**：profile §0 與 §2 之「48 leaf」加註
「**其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**」。
48 之總數不變 —— 該 leaf 仍在 R-PMH1 之範圍內。

依據：跨 feature 擴查零命中（母體 15 個有內容交付件、3,023 資料列、
11 個欄位、166 個相異 Test Set 全數人工核對）—— 兩邊都沒有，
是全案缺口而非分工；其 037 `Requirement Title` 逐字為
`CFTS009 Behavior Reference`，上游自己即命名為「參照」。
```

```
R-PMH48（下放包不載 git 提交狀態）
下放包不得記載 git 之提交狀態（「尚未提交」「累積未提交」「已授權」）。

理由：提交狀態為撰包時點之外之事實，分析層無從得知其於執行時是否仍成立
—— 已三次過時（08 §5.1、10 §七、11 §五）。

改為：提交狀態一律由執行層於上繳回報（R-G6 之揭露表已涵蓋）；
下放包若需觸及提交，只寫**授權與否**（授權為分析層或 Pei 之行為，
其效力不隨時間變動），不寫**已否提交**。

採納執行層 11 包上繳 §6 第 5 項之建議。
```

```
R-PMH49（互斥狀態檢查之兩項擴充）
(a) **互斥對清單擴充**，於 R-PMH45 之四組外增列：
      `已授權`/`未授權`、`已接上`/`wired: false`、`已定案`/`待裁`、
      `FULL`/`BLANK`（workbook_state）
    並於程式中明載「本清單為列舉而非全集」——
    列舉式判準之形態一變即靜默脫落（A-PMH08／A-PMH13 之同族形態）。

(b) **`RULINGS.md`／`ANOMALIES.md` 之按條號切分實作**：
    以 `^#{1,3}\s*(A-PMH\d+|R-PMH\d+|Q\d+)` 切段，段內判互斥。
    切分失敗（某狀態陳述不落在任何段內）者須具名列出，不得靜默歸入前段。

    實作後 11 包 §3.2 之具名排除即解除；若實作證明不可行，
    **維持具名排除並記其嘗試與失敗之處**，不得放寬判準後宣稱通過。

採納執行層 11 包上繳 §6 第 1、2 項之自陳。
```

```
R-PMH50（每批產出 JSON 之 source_clause）
Phase 4 之每批產出 JSON，其每一 leaf **必附 `source_clause`** ——
該 leaf 所對應章節之**規格原文子句**。

**取自 PDF**（判讀基準，通則 3），**不得取自 SYS1 匯出**
（追溯用）—— A-PMH03 已實測 SYS1 匯出相對 PDF 有 4 則偏離，
其中 outline 7.1 之偏離正是動畫／splash 之**時序子句重排**。

- 不得節錄至失去語意；過長者以 `...` 標明截斷處並另附全文檔。
- **該 TC 之 `expected_result` 所斷言之每一項行為，其規格依據必須完整
  出現於 `source_clause` 中**（比照 Power R-P109）。
- **機械檢查**：逐 leaf 檢查該欄存在且非空。
  **「是否忠於規格」本身不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  該檢查只保證覆核所需之材料存在，不保證覆核已做。

依據：Power Management 之 `006` 時序誤讀（A-PW68）歷經兩輪修正與多次
lint 全綠而未被察覺，最後由 `source_clause` 查出（R-P103／R-P104）。
本 feature 之 A-PMH03 為同一形狀且已知落在 7.1。
```

---

## 四、作業步驟

1. **抄錄** —— §三之 R-PMH46 ~ R-PMH50 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **profile 落檔（R-PMH46）** —— 寫入
   `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md`，
   含 R-PMH47 之兩處連帶加註。附逐字比對證明、行數、SHA256。
   **`PROFILE_INTEGRATION.md` 不得動**（待裁）。

3. **A-PMH13 之落實（R-PMH47）** ——
   - `ANOMALIES.md` 之 A-PMH13 改為 **RESOLVED（處置已定）**，
     內文載 (a)(b)(c) 三項與其依據；
   - `DATA_REQUESTS.md` 新增 **DR-PMH1**（本 feature 首筆），
     含詢問對象、問題全文、開立日期、狀態 `OPEN`；
   - `DECISIONS.md` 記其為**交付前阻斷項**（含 PENDING 之工作簿不得出貨）。

4. **R-PMH49 之實作** —— (a) 互斥對擴充至八組；(b) 按條號切分。
   二者各附故意失敗與範圍向之實跑輸出。
   (b) 若不可行，依條文維持具名排除並記其嘗試。

5. **Phase 4 首批（batch 1）之產出** —— **首批為 `Disclaimer Screen`（7 leaf）**。

   選批理由（三項，皆可查）：
   - 該組即交付夾名 `Disclaimer screen` 所指之能力，先做者最先可交；
   - **其 5 個 leaf 落在 outline 7.1／7.2／7.3／7.4，正是 A-PMH03 之
     指名複核章節** —— 首批即踩上已知最大風險，不留到最後；
   - `SWE1-HMI-PM-028`（R-PMH47 之揭露列）**不在本組**，
     故首批不受其牽動。

   產出要求：
   - 每 leaf 必附 `source_clause`，**取自 PDF**（R-PMH50）；
   - **outline 7.1 之三個 leaf（`001-03`／`-04`／`-05`）須另附
     PDF 原文與 SYS1 匯出之逐句對照**，具名其偏離處
     —— A-PMH03 之複核於本批完成；
   - 依 profile §3.1 之硬規則：`test_item` 之下半括號逐條檢查；
   - 依 profile §4 之 split policy：`Maserati` 變體、lower comfort screen
     配備與否各自成條；
   - `tc_id` 依 R-PMH16 之 `NR1L-DisclaimerScreen-{NNN}`，
     **本批為臨時編號**，最終編號待全 48 leaf 完成後單次指派
     （批次檔頭載 `"tc_id_status": "provisional"`）；
   - **零寫回工作簿** —— 本批只產出 JSON，不寫回。

6. **lint 首跑** —— 對 batch 1 之 JSON 跑現有檢查（含 `check_granularity.py`
   之 leaf 分布不受影響、`check_state_consistency.py`），
   並回報 profile §3 各欄規則之逐條符合狀況。

---

## 五、停止條件

canon §0 六條，另加本包三條：

7. profile 落檔後之逐字比對不符（R-PMH46 之驗證義務）
8. batch 1 之任一 leaf 缺 `source_clause`，或其 `source_clause` 取自
   SYS1 匯出而非 PDF
9. outline 7.1 之逐句對照發現**新的**偏離（A-PMH03 現記 4 則缺口）

**本包零寫回工作簿。** 11／12 兩包之提交**未授權**。
**不得改動 `scripts/new_feature.py`、`docs/runtime/` 下除 R-PMH46 所指之
單一檔案外之任何檔案、任何他 feature 之檔案**（含
`features/power/docs/internal_var_observability.md`）。

---

## 六、上繳包要求（`docs/upstream/12_phase4_batch1.md`）

1. §三五條之抄錄核對表（含命中數）
2. profile 落檔之逐字比對證明、行數、SHA256
3. A-PMH13 三處落實（`ANOMALIES.md`／`DATA_REQUESTS.md`／`DECISIONS.md`）
4. R-PMH49 (a)(b) 之實跑輸出
5. **batch 1 之 7 條 TC 全文** ＋ 每 leaf 之 `source_clause`
   ＋ outline 7.1 之 PDF/SYS1 逐句對照
6. lint 首跑結果 ＋ profile §3 逐欄符合狀況
7. **未結 DR 清單**（現應含 `DR-PMH1`）
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
9. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 七、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| **11／12 之 commit 授權** | 11 之 pathspec 見其上繳 §8（8 路徑，含 08 上繳之勘誤追加）；12 之待上繳後產生 | 否 |
| `PROFILE_INTEGRATION.md` | 是否登錄本 profile（R-PMH46 明文不授權） | 否 |
| Q10 | `Product Document 記錄封面頁`（profile §3.10 已預留） | 否，Phase 7 前 |
| — | A-PMH06 canon 層（`new_feature.py` 樣板） | 否，PENDING-CANON |

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-PMH46 | profile 落檔一次性授權（含明文不授權清單） | ✅ |
| R-PMH47 | A-PMH13 定案 (ii)＋(iii)：out of scope ＋ 揭露列 ＋ DR-PMH1 | ✅ |
| R-PMH48 | 下放包不載 git 提交狀態 | ✅ |
| R-PMH49 | 互斥對擴充至八組 ＋ 按條號切分實作 | ✅ |
| R-PMH50 | 每批 JSON 之 `source_clause` 須取自 PDF | ✅ |

五條各管一事。R-PMH47 為**定案型**，其連帶修改之範圍（profile 兩處加註、
48 總數不變）已於條內明載。
