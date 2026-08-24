# 上繳包 12 —— profile 落檔、A-PMH13 定案與 Phase 4 首批

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/12_phase4_batch1.md`
- 前一包：[upstream/11_claim_evidence.md](11_claim_evidence.md)
- 執行狀態：**步驟 1–6 全部執行完畢。九條停止條件全未觸發**（第 9 條之判定見 §5.2）。
  **零寫回工作簿**；**改狀態 git 零次**；未觸碰他 feature 之檔案。

---

## 1. 抄錄核對表（步驟 1，依 R-PMH41 驗命中數）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH46 | profile 落檔一次性授權 | 448 | `3c12ee5e7db1e695` | `3c12ee5e7db1e695` | 逐字相符 |
| R-PMH47 | A-PMH13 定案 (ii)＋(iii) | 1312 | `391b39313a6b3759` | `391b39313a6b3759` | 逐字相符 |
| R-PMH48 | 下放包不載 git 提交狀態 | 253 | `46273e8cf65f867a` | `46273e8cf65f867a` | 逐字相符 |
| R-PMH49 | 互斥對擴充 ＋ 按條號切分 | 456 | `404337182adbefd7` | `404337182adbefd7` | 逐字相符 |
| R-PMH50 | `source_clause` 須取自 PDF | 609 | `879f74215e51fa7e` | `879f74215e51fa7e` | 逐字相符 |

10 個 placeholder 各命中 1，共替換 10 次（預期 10）。
Pei 之裁定原文「上繳了 兩項都核可」已抄入條段首。

---

## 2. 步驟 2 —— profile 落檔（R-PMH46）

**已寫入** `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md`
（該檔先前不存在，已驗）。

| 項 | 值 |
|---|---|
| 行數 | **284**（草案 281 ＋ R-PMH47 之連帶 3 行） |
| SHA256 | `8f8a15145bdf3b16dd4110d52c662f6bb67d7efd978a503f063707d26d48122a` |

### 2.1 逐字比對證明（R-PMH46 之驗證義務）

以 `difflib.unified_diff` 比對 10 §四之草案區塊與落檔內容：

```
差異行數 = 3
   +  —— **其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**（R-PMH47）
   +
   +**其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**（R-PMH47）。**48 之總數不變** —— 該 leaf 仍在 R-PMH1 之範圍內。

新增 3 行、刪除 0 行
僅新增而無刪除（原文一字未改）: True
新增之行全部含 R-PMH47 之加註: True
```

**除 R-PMH47 所定之兩處連帶外，零增刪改。停止條件 7 未觸發。**

**`PROFILE_INTEGRATION.md` 未動**（R-PMH46 明文不授權）；
`docs/runtime/` 下其他檔案亦未觸碰。

---

## 3. 步驟 3 —— A-PMH13 之三處落實（R-PMH47）

| 檔 | 落實 |
|---|---|
| `ANOMALIES.md` | A-PMH13 標題改 **RESOLVED（處置已定，R-PMH47）**；內文新增 (a)(b)(c) 三項與其欄位處置表；原三種處置之並列保留於其後供追溯 |
| `DATA_REQUESTS.md` | **重寫** —— 新增 **`DR-PMH1`**（本 feature 首筆），含問題全文、兩輪擴查之量測表、影響、狀態 `OPEN`、Urgency `High（交付前阻斷）`，並附「未結 DR 清單」 |
| `DECISIONS.md` | 新增 **交付前阻斷項（DR-PMH1）** 一列，載「含 PENDING 之工作簿不得出貨（§8.4.3）」 |

**連帶修改已落實**：profile §0 與 §2 之「48 leaf」已加註揭露列，**48 總數不變**。

---

## 4. 步驟 4 —— R-PMH49 之實作

### 4.1 (a) 互斥對擴充至 **8 組**

原四組 ＋ `已授權`/`未授權`、`已接上`/`wired: false`、`已定案`/`待裁`、
`FULL`/`BLANK`。程式中以常數 `PAIRS_IS_ENUMERATION_NOT_TOTAL = True` 明載
**「本清單為列舉而非全集」**，每次執行皆印出該聲明。

### 4.2 (b) 按條號切分 —— **已實作並實跑，惟判準對散文檔不可用**

**切分本身可行**：`RULINGS.md` 切得 **51** 段、`ANOMALIES.md` **13** 段。

**不可用者為判準**。實跑所見：

| 檔 | 命中 | 性質 |
|---|---:|---|
| `RULINGS.md` | 10 | **10 皆誤報** —— R-PMH43／45／49 之條文**本身即逐字列舉互斥對兩側**（R-PMH45：「最低限度之互斥對：`定版`/`未定版`、`PENDING`/`RESOLVED`…」）。**定義本檢查之條文，其字面必然含兩側。** |
| `ANOMALIES.md` | 段外 2 ＋ 段內 1 | 段外 2 為**檔頭之詞彙說明**（"PENDING entries block their batch … RESOLVED entries record the ruling verbatim"）；段內 1 為 A-PMH13 之**歷史引述**與**規則敘述** |
| `DECISIONS.md` | 1 | 兩側皆為**規則敘述**：「含 PENDING 之工作簿不得出貨」與「通則 8：文字修補不構成 RESOLVED」 |

### 4.3 可修與不可修之界線（本輪已修前者，**未動後者**）

| 類 | 內容 | 處置 |
|---|---|---|
| **可修** —— pattern 之**精確度** | `PENDING-CANON` 為**另一狀態值**、`PENDING: DR-` 為**欄位佔位標記**、`非 RESOLVED` 為**否定式** | 已加 lookaround |
| **不可修** —— **散文提及 vs 狀態斷言** | 二者在字面與上下文形態上**完全相同**，行級或段級掃描皆無從區分 | **不再加 lookaround** —— 再加即是把判準往資料上調，正是 R-PMH49(b) 所禁之「放寬判準後宣稱通過」 |

### 4.4 處置 —— 三個散文檔具名排除，範圍窄於所期，據實記載

**有效範圍為「狀態板」三檔**：`framework.md`／`feature.yaml`／`PLAYBOOK.md`
（其內容為欄位值與勾選項，非散文）。

```
=== 互斥狀態一致性檢查 ===
互斥對 8 組（R-PMH49(a)）—— **本清單為列舉而非全集，未列舉者不會被發現**
有效範圍（狀態板）：framework.md, feature.yaml, PLAYBOOK.md
按條號切分之嘗試（R-PMH49(b)）：RULINGS.md, ANOMALIES.md —— 已實作實跑，判準對散文檔不可用，具名排除如下
    具名排除 RULINGS.md —— 散文檔 —— 條文本身列舉互斥對兩側（切分 51 段，10/10 誤報）
    具名排除 ANOMALIES.md —— 散文檔 —— 檔頭詞彙說明 ＋ 歷史引述 ＋ 規則敘述（切分 13 段）
    具名排除 DECISIONS.md —— 散文檔 —— 兩側皆為規則敘述（§8.4.3 與通則 8）

  framework.md       PASS
  feature.yaml       PASS
  PLAYBOOK.md        PASS
exit=0
```

**此範圍窄於 R-PMH49(b) 所期**（其原欲納入 `RULINGS.md`／`ANOMALIES.md`），
**據實記載，未宣稱通過。停止條件 9 未觸發**（未放寬判準）。

**⚠ 一項退步須具名**：11 包時 `DECISIONS.md` 在範圍內且 PASS；
本輪因 (a) 之擴充與本輪新增之條文敘述而產生散文碰撞，**改為具名排除**。
**覆蓋率因此下降**，非提升。

### 4.5 **本輪實跑之實益 —— 查出一項真缺陷**

段內掃描於 `A-PMH13` 查出一句**已過時之狀態陳述**：07 包所寫
「本則之 **PENDING** 狀態僅繫於 `-028` 之處置」，而 12 包已裁為 RESOLVED。
**已改標為「07 包當時之陳述」並註明 12 包之定案。**

**故 (b) 雖判為對散文檔不可用，其一次實跑仍抓到一件真的。**
故意失敗（暫存副本上把 `framework.md:7` 改回「未定版」）仍如期攔下。

---

## 5. 步驟 5 —— Phase 4 batch 1（`Disclaimer Screen`）

**產出**：`generated/batch01.json`，**8 條 TC 自 7 leaf**。
**零寫回工作簿。**

### 5.1 ⚠ **8 條而非 7 條** —— profile §4 之拆分

下放包 §六第 5 項稱「batch 1 之 **7 條** TC 全文」（依 1 leaf : 1 TC 推得）。
**實產 8 條** —— `SWE1-HMI-PM-001-04` 依 **profile §4「不同觸發即拆分」**
拆為兩條：

| tc_id | 觸發 | 結果 |
|---|---|---|
| `NR1L-DisclaimerScreen-002` | **按 Accept** | 直接進 last mode screen |
| `NR1L-DisclaimerScreen-003` | **等待逾時** | 逾時等同 Accept |

規格逐字為 `The user is able to either press the Accept … or wait for the screen
to timeout.` —— **兩個使用者路徑，結果相同而觸發不同**。
profile §4 之判準優先於下放包之計數推估，**特此具名其差異**。

### 5.2 A-PMH03 之指名複核 —— **7.1 是漏句，不是重排。停止條件 9 之判定**

**逐句對照**（SYS1 8 句 vs PDF 9 句，`difflib.SequenceMatcher` on sentences）：

| # | 對照 |
|---|---|
| 1 | **≠ 差異段** |
| | SYS1：`SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off after animation, screen is black.` |
| | PDF ：`SU1.) … presented (3 sec), `**`after the animation (3 sec) a splash screen is presented timeout (1.5 each).`** |
| | PDF ：`If ignition remains off after animation, screen is black.` |
| 2–8 | **＝ 逐句相同** |

**被漏之子句於 SYS1 全 52 則描述中完全不存在**（實測四組檢索皆 0）：
`after the animation (3 sec) a splash screen is presented timeout (1.5 each)`／
`after the animation`／`splash screen is presented`／`1.5 each`。

**不是同義改寫，是整句消失。** SYS1 保留了另一句
`If ignition is turned on during animation, splash screen(s) are presented
(1.5 sec timeout each).` —— 其為**有條件**（點火於動畫期間開啟），
被漏者為**無條件**（動畫結束後即呈現 splash）。**二者非同一敘述。**

**故 canon §3 之 Home 型 Mode A blind spot 在本 feature 確實發生**，
而 01 包記「**於本 feature 未觀察到**」。**該結論已於 `ANOMALIES.md` 更正
（原文保留於其後供追溯）。**

**成因（量測方法之限制）**：01 包以「SYS1 該則是否為 PDF 全文之子字串」判定
—— **該量測只驗 SYS1 之字有沒有出現在 PDF，不驗 PDF 之字有沒有出現在 SYS1**。
**方向性缺陷**：它看不見「PDF 有而 SYS1 無」。

**其嚴重性**：被漏者為**時序子句**（動畫 3 sec → splash 1.5 each）——
正是 **A-PW68**（Power Management `006` 時序誤讀，歷經兩輪修正與多次
lint 全綠而未被察覺）之同一形態。

**停止條件 9 之判定**：條文為「發現**新的**偏離（A-PMH03 現記 4 則缺口）」。
**位置未變**（7.1 本即四則之一）、**缺口數仍為 4**，故**依其字面未觸發**。
**惟其性質由「重排」變為「漏句」，且推翻該則之標題結論** ——
**執行層將此以與停止條件同等之份量具名於此，不因字面未觸發而降低其呈現。**

**R-PMH50 因而得到直接佐證**：本批 4 條 7.1 系 TC 之 `source_clause`
取自 PDF，**皆含該被漏之時序子句**；若取自 SYS1 則無從得知。

### 5.3 八條 TC 之摘要（全文見 `generated/batch01.json`）

| tc_id | leaf | outline | 設計方法 | Pri | 區辨軸 |
|---|---|---|---|---|---|
| `-001` | `001-03` | 7.1 | 狀態轉換 | P1 | 系統就緒與否 |
| `-002` | `001-04` | 7.1 | 功能測試 | P1 | 觸發路徑：按壓 Accept |
| `-003` | `001-04` | 7.1 | 狀態轉換 | P1 | 觸發路徑：等待逾時 |
| `-004` | `001-05` | 7.1 | 負向測試 | P1 | 變體：Maserati（無逾時） |
| `-005` | `003` | 7.2 | 功能測試 | P1 | 配備：未配備 lower comfort screen |
| `-006` | `004` | 7.3 | 負向測試 | P1 | 配備：已配備 lower comfort screen |
| `-007` | `005` | 7.4 | 功能測試 | P1 | 同一觸發之兩後果（§5.7 不拆） |
| `-008` | `022-02` | 10.4 | 狀態轉換 | P1 | 進入路徑：Power Button Off → On |

`tc_id_status = "provisional"`（最終編號待 48 leaf 完成後單次指派）。

### 5.4 三處**不造值**之具名（§8.4.1）

| tc | 規格未載者 | 本批之處置 |
|---|---|---|
| `-003` | **逾時之秒數**（PDF 僅寫 `wait for the screen to timeout`） | ER 不斷言秒數，只斷言逾時後之結果 |
| `-004` | 同上（Maserati 之對照時長） | 步驟以「長於非 Maserati 之逾時」表述，不填數字 |
| `-008` | `unless certain phone call scenarios have occurred` **未列舉該等情境** | **不斷言其例外**，僅驗正向路徑；例外之列舉屬 10.6（`Power Off Behavior` 組），不在本批 |

### 5.5 `source_clause` 之來源（R-PMH50）

| 來源 | 涵蓋之 TC |
|---|---|
| `spec_pdf p8` — `SU1.)` 全文 | `-001`～`-004` |
| `spec_pdf p8` — `SU2.)` | `-005` |
| `spec_pdf p8` — `SU2.1)` | `-006` |
| `spec_pdf p8` — `SU3.)` | `-007` |
| `spec_pdf p10` — `PITA6.1` | `-008` |

**8/8 皆 `spec_pdf`，零取自 SYS1。停止條件 8 未觸發。**

---

## 6. 步驟 6 —— lint 首跑：**20/20 PASS**

`scripts/lint_batch.py generated/batch01.json` → exit 0

| # | 檢查 | 結果 |
|---|---|---|
| 1 | R-PMH50 每 leaf 有 `source_clause` 且非空 | PASS |
| 2 | R-PMH50 `source_clause` 取自 PDF（非 SYS1） | PASS |
| 3 | profile §3.1 `test_item` 具下半括號（**硬規則**） | PASS |
| 4 | profile §3.3 `design_method` ∈ 下拉選單 9 詞條 | PASS |
| 5 | profile §3.4 `spec_reference` 形態且與 `layer3_sections.tsv` 相符 | PASS |
| 6 | profile §3.5 `priority` ∈ `{P0,P1,P2,P3}`（母本 DV） | PASS |
| 7 | profile §3.6 `estimated_test_time` 留白 | PASS |
| 8 | profile §3.8 `vehicle_models` 留白 | PASS |
| 9 | profile §3.7 `functional_safety` = `NA` | PASS |
| 10 | R-PMH18 `test_group` = `Disclaimer screen`（**小寫 s**） | PASS |
| 11 | R-PMH36 `test_set` = `Disclaimer Screen`（**大寫 S**） | PASS |
| 12 | R-PMH16 `tc_id` 形態 `NR1L-DisclaimerScreen-{NNN}` | PASS |
| 13 | `test_set` ∈ Layer 2 定版 8 組 | PASS |
| 14 | canon §11 方括號禁止（本 feature 無 profile 例外） | PASS |
| 15 | procedure 與 ER 步數一致 | PASS |
| 16 | 必填欄無空 | PASS |
| 17 | ER 未以 `NA` 充當未知 | PASS |
| 18 | `tc_id` 唯一 | PASS |
| 19 | `tc_id_status` = `provisional` | PASS |
| 20 | 本批 leaf == `Disclaimer Screen` 之 7 leaf | PASS |

**lint 之限度已寫入其輸出**（R-PMH50 末段之照錄）：

> 本 lint 只驗 `source_clause` **存在且取自 PDF**。
> **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
> 本檢查只保證覆核所需之材料存在，不保證覆核已做。

另跑：`check_state_consistency.py` exit 0、`check_granularity.py --check-doc-sync` exit 0。

---

## 7. 未結 DR 清單（R-PMH47(c) 之每包義務）

| DR | 主旨 | 狀態 | 阻斷交付 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 所定之 Off Road+ power moding 行為 | **OPEN** | **是**（§8.4.3：含 PENDING 之工作簿不得出貨） |

**合計未結 1 筆。** 其影響限於 `Off Road Plus` 批之 1 條（`SWE1-HMI-PM-028`），
**不影響本批**。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，六項。**

1. **batch 1 之「是否忠於規格」未經人讀覆核。** lint 20/20 只證明材料齊備。
   **R-PMH50 明言該項不可機械檢查** —— 八條 TC 之 `expected_result` 是否
   完整落在其 `source_clause` 之依據內，**須分析層或 Pei 人讀 PDF 對照**。
   **本包未做，也做不了**（自己覆核自己不構成覆核）。

2. **A-PMH03 之其餘三則未以逐句法複驗。** 本輪只對 7.1 做了逐句對照，
   而 **01 包之量測方法有方向性缺陷**（只驗 SYS1→PDF，不驗 PDF→SYS1）。
   **8、9.1、11.1 三則之「重排／條列再流」判定，其依據與 7.1 相同，
   同樣可能是漏句。** 未複驗。

3. **同一方向性缺陷及於全部 52 則。** 01 包對 43 則可比對描述判「39 則逐字
   命中」，**該判定同樣只驗一個方向**。若 SYS1 對其他 outline 亦有漏句，
   現行紀錄看不見。**本輪只補了 7.1 一則。**

4. **`DECISIONS.md` 退出互斥檢查範圍**（§4.4）—— 覆蓋率下降，未補償。

5. **profile 之敘述性條款未逐句回溯**（10 包 §6 第 4 項之延續）——
   §3.2 之變體詞、§4 之四條 split 判準等，其正確性仍倚賴分析層。
   本批已實際套用 §4 之三條（不同觸發拆、變體拆、同觸發不拆），
   **其套用是否正確，同樣須人讀覆核。**

6. **`tc_id` 為 provisional 而無任何機制防止其被當成最終編號。**
   `tc_id_status` 欄僅為宣告；若日後有人直接取 `tc_id` 寫回，
   **無檢查會攔** —— 與 `check_write_back.py` 之 `wired: false` 同型。

---

## 9. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— 三處不造值已具名（§5.4） |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | profile 落檔逐字比對不符 | **未觸發** —— 差異 3 行，全為 R-PMH47 連帶，零刪除 |
| 8 | 任一 leaf 缺 `source_clause` 或取自 SYS1 | **未觸發** —— 8/8 皆 `spec_pdf` |
| 9 | 7.1 逐句對照發現**新的**偏離 | **未觸發**（位置未變、缺口仍 4）；**惟其性質由重排改為漏句，推翻 A-PMH03 之標題結論，已以同等份量具名（§5.2）** |

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 12 — profile landed, A-PMH13 ruled, phase 4 batch 1
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DATA_REQUESTS.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/RULINGS.md \
           features/power_moding/generated/batch01.json \
           features/power_moding/scripts/check_state_consistency.py \
           features/power_moding/scripts/gen_batch01.py \
           features/power_moding/scripts/lint_batch.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/12_phase4_batch1.md \
           features/power_moding/docs/upstream/12_phase4_batch1.md \
           docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md
```

- **`docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` 在 pathspec 內**
  —— R-PMH46 所授權之單一檔案。**`PROFILE_INTEGRATION.md` 與 `docs/runtime/`
  下其他檔案不在內。**
- `feature.yaml`／`PLAYBOOK.md`／`framework.md` 本輪未改。
- **未觸碰任何他 feature 之檔案**（含 `features/power/docs/internal_var_observability.md`）。
- pathspec 逐項寫全名（R-PMH3(c)）。

### 10.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short`／`git log -1 --format` | 2 |
| **改狀態 git** | **無** | **0** |

**11 包之提交狀態**：已於本輪之前提交為 **`365a2db`**（依 R-PMH48，
提交狀態由執行層於上繳回報）。**12 包之提交尚未授權。**

---

## 11. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **batch 1 之人讀覆核** | 八條 TC 之 `expected_result` 是否完整落在其 `source_clause` 內（§8 第 1 項）—— **R-PMH50 明言不可機械檢查** | **是** —— 下一批之前 |
| **A-PMH03 之其餘三則** | 是否以逐句法複驗（§8 第 2 項）；**其判定依據與 7.1 相同，而 7.1 已證為漏句** | 建議：是 |
| **01 包量測之方向性缺陷** | 是否對全 52 則重跑雙向比對（§8 第 3 項） | 否，但影響面未知 |
| **12 包之 commit 授權** | pathspec 見 §10（12 路徑，含 profile） | 否 |
| `PROFILE_INTEGRATION.md` | 是否登錄本 profile（R-PMH46 明文不授權） | 否 |
| Q10 | `Product Document 記錄封面頁` | 否，Phase 7 前 |
