# 下放包 13 —— batch 1 人讀覆核（不通過）與 A-PMH03 之改判

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/13_batch1_rework.md`
- 前一包：[12_phase4_batch1.md](12_phase4_batch1.md)
  （上繳 [../upstream/12_phase4_batch1.md](../upstream/12_phase4_batch1.md)）

---

## 一、12 包之覆核結果 —— **程序面通過，產出面不通過**

| 面向 | 結果 |
|---|---|
| profile 落檔（R-PMH46） | **通過** —— diff 3 行全為 R-PMH47 連帶、零刪除 |
| A-PMH13 三處落實（R-PMH47） | **通過** —— 含 `DR-PMH1` 開立 |
| R-PMH49 之實作 | **通過**（其範圍窄於所期，據實記載，見 §三） |
| **A-PMH03 之 7.1 複核** | **通過，且為本輪最重要之發現**（§二） |
| **batch 1 之八條 TC** | **不通過** —— **六類違規，涉及全部八條**（§四） |

---

## 二、A-PMH03 之 7.1 —— 分析層獨立複驗，**漏句成立**

執行層指其為**漏句**而非重排。**我未採信其結論即改判，另行實測。**

**量測條件**：PDF 以 `pymupdf` 抽全文（11 頁、15,751 字元）；
SYS1 匯出以 `openpyxl` `read_only` 讀 `Basic Report` 分頁全部非空儲存格
（16,784 字元）。

| 探針 | PDF | SYS1 `Basic Report` |
|---|---|---|
| `after the animation` | **有**（p8, SU1.) 句中） | **0** |
| `splash screen is presented` | **有** | **0** |
| `1.5 each` | **有** | **0** |
| `1.5 sec timeout each` | 有 | **1** |

PDF 之 SU1.) 逐字（p8）：

> `SU1.) When the vehicle's driver door is closed a startup animation will be
> presented (3 sec), `**`after the animation (3 sec) a splash screen is presented
> timeout (1.5 each).`**` If ignition remains off after animation, screen is black.
> If ignition is turned on during animation, splash screen(s) are presented
> (1.5 sec timeout each). …`

**執行層之指認完全成立。** 被漏者為**無條件**之時序子句（動畫結束後即呈現
splash，1.5 each）；SYS1 保留者為**有條件**之另一句（點火於動畫期間開啟）。
**二者非同一敘述，不是同義改寫。**

### 2.1 01 包之量測有方向性缺陷 —— 且該缺陷及於全 52 則

01 包以「SYS1 該則是否為 PDF 全文之子字串」判定 ——
**只驗 SYS1→PDF，不驗 PDF→SYS1**。它看不見「PDF 有而 SYS1 無」。

**故 01 包「39/43 逐字命中、Home 型漏句於本 feature 未觀察到」之結論，
其涵蓋範圍不及於漏句。** 該結論已由執行層更正（原文保留）。

**A-PMH03 之標題結論須改判**（§五 R-PMH51）：其四則缺口中，
7.1 一則由「重排」改為「**漏句**」；**其餘三則（8、9.1、11.1）之判定
依據與 7.1 相同，同樣可能是漏句，未複驗。**

### 2.2 這一則為什麼要緊

被漏者是**時序子句**（動畫 3 sec → splash 1.5 each）—— 與 **A-PW68**
（Power Management `006` 之時序誤讀，歷經兩輪修正、多次 lint 全綠而未被
察覺）**同一形態**。

**R-PMH50 因此得到直接佐證**：本批四條 7.1 系 TC 之 `source_clause`
取自 PDF，**皆完整含該子句**；若依 SYS1 產出，該時序自始不存在於材料中，
覆核者連查都無從查起。

---

## 三、R-PMH49(b) 之處置 —— **接受其判定，並認其為正確之停手**

執行層實作了按條號切分（`RULINGS.md` 51 段、`ANOMALIES.md` 13 段），
實跑後發現**判準對散文檔不可用**：`RULINGS.md` 10/10 誤報，
**其成因是 R-PMH43／45／49 之條文本身即逐字列舉互斥對兩側** ——
**定義該檢查之條文，其字面必然含兩側。**

其 §4.3 之「可修 vs 不可修」界線劃得正確：pattern 之精確度可修
（`PENDING-CANON`／`PENDING: DR-` 之 lookaround），
而**「散文提及」與「狀態斷言」在字面與上下文形態上完全相同**，
再加 lookaround 即是把判準往資料上調 —— 正是 R-PMH49(b) 所禁者。

**其自行具名之退步亦予採認**：`DECISIONS.md` 由 11 包之在範圍內
改為具名排除，**覆蓋率下降而非提升**，據實記載。

**且該一次實跑抓到一件真的**：`A-PMH13` 內一句已過時之狀態陳述
（07 包所寫「本則之 PENDING 狀態僅繫於 `-028` 之處置」，而 12 包已裁 RESOLVED）。
**判準不可用，不等於該次執行無價值。**

---

## 四、batch 1 —— **不通過，六類違規**

以下為**人讀覆核**（12 包上繳 §8 第 1 項所指、執行層自陳做不了者）。
逐條比對 `source_clause`、canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11
與 profile §3／§4。

### 4.1 【嚴重】canon §10.5 —— 三條 TC 只有一個步驟

canon §10.5 逐字：「至少 2 numbered steps（Setup → Verification minimum）。
**Single-step TCs are rejected** —— even smoke tests need an explicit
verification step.」

| tc | `test_procedure` 步數 |
|---|---|
| `-002` | **1** |
| `-003` | **1** |
| `-006` | **1** |

**三條退回重寫。**

### 4.2 【嚴重】canon §5.1 —— 禁用動詞 `observe` 作主動詞，**8 處**

canon §5.1 明列 `observe` 為 forbidden main verb（其將判斷推給測試員）。
preferred verbs 為 `Check that`／`Confirm that`／`Read`／`Record`／`Compare`。

| tc | 位置 | 逐字 |
|---|---|---|
| `-001` | step 1 | `Observe the disclaimer screen while the system is still loading` |
| `-001` | step 2 | `… and observe the disclaimer screen again` |
| `-004` | step 1 | `… and observe the disclaimer screen for a period longer than …` |
| `-005` | step 1 | `Observe the disclaimer screen for the comfort controls` |
| `-006` | step 1 | `Observe the disclaimer screen for the comfort controls` |
| `-007` | step 1 | `… and observe the screen and the audio output` |
| `-008` | step 2 | `Observe the screen` |

**七條 TC 中八處命中**（`-002`、`-003` 未命中此項但另有 §10.5）。

### 4.3 【嚴重】canon §5.2B／§5.5 —— Final Step 未持有驗證意圖

Final Step 須含 ACTION ＋ check target（`check that …`／`to verify …`）。

| tc | Final Step 逐字 | 問題 |
|---|---|---|
| `-002` | `Press the Accept button on the disclaimer screen` | **無 check 子句**（且為唯一步驟） |
| `-005` | `Operate one of the comfort controls shown on the disclaimer screen` | **無 check 子句** |

### 4.4 【嚴重】§4.3.1 —— `test_item` 上半非規格原句 verbatim，四條

§4.3.1 定 `test_item` 上半 = **需求／規格原句 verbatim**。
本批**同一組內兩種寫法並存**：

| tc | 上半 | 判定 |
|---|---|---|
| `-005` | `SU2.) For Maserati vehicles, while on the disclaimer screen …` | ✅ verbatim |
| `-006` | `SU2.1) Do not display comfort controls …` | ✅ verbatim |
| `-007` | `SU3.) No pop-ups will appear …` | ✅ verbatim |
| `-001` | `During the Disclaimer screen (content per CFTS009/legal), if the system is not ready …` | ❌ **改寫** |
| `-002` | `The system allows the user to press Accept to go directly to the last mode screen.` | ❌ **改寫** |
| `-003` | `The system allows the user to wait for the screen to timeout, which automatically equals Accept.` | ❌ **改寫**，且 `automatically equals Accept` **為規格所無之推論** |
| `-004` | `Exception: For Maserati applications the system provides no timeout (per CFTS009); …` | ❌ **改寫** |
| `-008` | `Upon pressing the power button to On state …` | ⚠ 近 verbatim，`Upon pressing power button` 被加了 `the` |

`-003` 之 `which automatically equals Accept` **尤須注意** —— 規格逐字只有
`or wait for the screen to timeout`，**未言逾時等同 Accept**。
其 ER 亦寫 `the same outcome as pressing Accept`。**此為 §8.4.1 之造值**
（推論寫成斷言）。

### 4.5 【中】交付欄位含 markdown 粗體，三條

`pre_conditions` 為**寫入 Excel 儲存格之交付內容**，`**Maserati**` 會逐字
落入儲存格。

| tc | 逐字 |
|---|---|
| `-004` | `1. The vehicle is a **Maserati** application` |
| `-005` | `1. The vehicle is a **Maserati** application` / `2. The vehicle is **not** equipped …` |
| `-006` | `1. The vehicle is a **Maserati** application` / `2. The vehicle **is** equipped …` |

### 4.6 【中】§11 —— UI 標籤未用直雙引號

| 問題 | 例 |
|---|---|
| 彎引號 `“…”`（U+201C/201D） | `-001` ER：`“Loading…” is displayed` |
| UI 標籤未加引號 | `-002`／`-003`／`-004`：`the Accept button` → 應為 `the "Accept" button` |

### 4.7 【中】交叉引用錯誤，**四處** —— 拆分後編號位移未更新

`-002`／`-003` 之拆分使其後之 tc_id 全體 +1，而**交叉引用未跟著改**：

| tc | 逐字 | 應為 |
|---|---|---|
| `-005` test_item 括號 | `與 \`-004\` 之配備情形相對` | `-006` |
| `-005` reasoning | `與 \`-004\` 成對` | `-006` |
| `-006` test_item 括號 | `與 \`-003\` 之未配備情形相對` | `-005` |
| `-006` reasoning | `與 \`-003\` 為 profile §4 之變體對` | `-005` |

`-004` 是 Maserati 無逾時、`-003` 是逾時路徑，**皆與 lower comfort screen
之配備無關**。此為 §5.1 拆分後之連帶未更新。

### 4.8 【輕】§8.5 —— Pre-Condition 範圍溢出

| tc | 條目 | 問題 |
|---|---|---|
| `-001` | `The vehicle is a non-Maserati application` | 載入→Accept 之顯示切換**與 Maserati 與否無關**（Maserati 之差異僅在逾時），此條不必要地窄化 |
| `-002` | 同上 | Accept 按壓於 Maserati 亦成立，不必要 |
| `-001` | `with the ignition turned on during the start-up animation` | 取自規格之**條件分支**，為到達該畫面之環境前提，非本 TC 直接驗證之觸發條件 |

（`-003` 之 `non-Maserati` **是必要的** —— 逾時本身即 Maserati 之差異點。）

### 4.9 lint 20/20 全綠而以上六類全未被攔 —— **這才是本節之重點**

現行 `lint_batch.py` 之 20 項**全為 profile 欄位層與 id 層**
（`design_method` ∈ 九詞條、`priority` ∈ DV、大小寫、`tc_id` 形態…），
**零項檢查 canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11**。

**lint 全綠不構成 TC 可用之證據** —— 與 A-PW68（Power `006` 歷經多次
lint 全綠而時序誤讀未被察覺）為同一形狀。

---

## 五、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH51（A-PMH03 之改判與雙向比對義務）
A-PMH03 之 outline 7.1 一則，其性質由「重排」改判為「**漏句**」——
PDF 之 SU1.) 含 `after the animation (3 sec) a splash screen is presented
timeout (1.5 each).`，而 SYS1 匯出全 52 則描述中該子句之四組探針
（`after the animation`／`splash screen is presented`／`1.5 each`）
命中皆為 0（分析層 13 包 §二獨立複驗）。

**規格比對一律雙向**：既驗 SYS1→PDF（SYS1 之字是否出現於 PDF），
亦驗 PDF→SYS1（PDF 之字是否出現於 SYS1）。單向比對看不見漏句，
而漏句正是最危險之形態 —— 它不會在任何逐字比對中顯示為「不符」，
只顯示為「沒有這一則」。

A-PMH03 之其餘三則（8、9.1、11.1）之判定依據與 7.1 相同，
**須以雙向法複驗**；未複驗前，其「重排／拼字／條列再流」之標題結論
不得引用。
```

```
R-PMH52（lint 之涵蓋範圍須具名，且不得作為 TC 可用之證據）
任何 lint 之輸出須具名其**未涵蓋**之 canon 節號，不得只列已通過項。

現行 `lint_batch.py` 之 20 項全為 profile 欄位層與 id 層，
**零項檢查 canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11** ——
而 batch 1 於該七節共六類違規、涉及全部八條，lint 仍 20/20 全綠。

「lint 全綠」不得作為 TC 可用、可提交人讀覆核或可寫回之證據；
其僅證明所檢查之項通過。

依據：13 包 §四；A-PW68 之同一形狀（Power `006` 歷經多次 lint 全綠
而時序誤讀未被察覺）。
```

```
R-PMH53（拆分後之連帶更新）
一條 TC 拆為多條而使其後之 tc_id 位移時，須重掃該批全部交叉引用
（`test_item` 括號下半、`reasoning`、`distinguishing_axis`、
`split_reason`），並驗其所指之 tc_id 仍為所欲指者。

**機械檢查**：批內任一欄位所引之 `-\d{3}` 形態 tc_id，其被引用者之
`leaf_id` 或 `distinguishing_axis` 須與引用處之語意相容；
無法機械判定者，逐處列出供人讀。

依據：batch 1 因 `001-04` 拆為兩條而使 `-005` 之後全體 +1，
`-005`／`-006` 之四處交叉引用未更新，所指者變為無關之 TC（13 包 §4.7）。
```

---

## 六、作業步驟

1. **抄錄** —— §五之 R-PMH51 ~ R-PMH53 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **`ANOMALIES.md` 之 A-PMH03 改判（R-PMH51）** —— 標題結論改為
   「四則缺口：**1 則漏句（7.1，已證）**、3 則未以雙向法複驗」，
   **原文保留於其後**。

3. **A-PMH03 其餘三則之雙向複驗** —— 對 outline 8、9.1、11.1
   （及其餘全部 52 則，若成本允許）以**雙向**法比對 PDF 與 SYS1 匯出：
   - 方向一：SYS1 之每一句是否出現於 PDF；
   - **方向二：PDF 之每一句是否出現於 SYS1**（本輪之新增）；
   - 逐則回報二方向之結果，漏句者逐句列出其逐字內容與所在頁次。
   **此為本包最高優先** —— 其結果決定既有 48 leaf 之 `source_clause`
   是否有其他隱藏缺口。

4. **`lint_batch.py` 之擴充（R-PMH52）** —— 新增下列檢查，各附
   **must-hit 錨點**（以 batch 1 之現行違規為天然反例，依 R-PMH35）：

   | 新檢查 | canon | must-hit 錨點 |
   |---|---|---|
   | `test_procedure` ≥ 2 步 | §10.5 | `-002`／`-003`／`-006` 須 FAIL |
   | 禁用動詞（`observe`／`see if`／`check whether`／`verify` 作主動詞…） | §5.1 | 八處須 FAIL |
   | Final Step 含驗證意圖 | §5.2B／§5.5 | `-002`／`-005` 須 FAIL |
   | `test_item` 上半為 `source_clause` 之子字串（正規化空白後） | §4.3.1 | `-001`～`-004` 須 FAIL |
   | 交付欄位無 markdown 標記（`**`／`__`／`` ` ``） | — | `-004`／`-005`／`-006` 須 FAIL |
   | UI 標籤用直雙引號、無彎引號 | §11 | `-001`～`-004` 須 FAIL |
   | 批內交叉引用之 tc_id 存在且語意相容 | R-PMH53 | `-005`／`-006` 四處須 FAIL |

   **並依 R-PMH52 於輸出末尾具名其仍未涵蓋之 canon 節號。**

5. **batch 1 重寫** —— 依 §四逐項修正後重跑擴充後之 lint。
   **`-003` 之 `automatically equals Accept` 須刪除**（§8.4.1 造值）——
   規格只寫 `or wait for the screen to timeout`，其 ER 只得斷言
   「畫面移除並顯示 last mode screen」，**不得斷言其等同 Accept**。

6. **`tc_id` 之 provisional 防護（12 包上繳 §8 第 6 項）** ——
   於 `check_write_back.py` 增一項：若批次檔頭之 `tc_id_status` 為
   `provisional`，寫回即中止。附故意失敗。

---

## 七、停止條件

canon §0 六條，另加本包三條：

7. 步驟 3 之雙向複驗發現**任一新漏句**（除 7.1 外）
8. 步驟 4 之任一新檢查之 must-hit 錨點未 FAIL
9. 重寫後之 batch 1 於擴充後之 lint 仍有 FAIL

**本包零寫回工作簿。** 12／13 兩包之提交**未授權**。
**不得改動 `scripts/new_feature.py`、`docs/runtime/` 下任何檔案
（profile 已落檔，本輪不再動）、任何他 feature 之檔案。**

---

## 八、上繳包要求（`docs/upstream/13_batch1_rework.md`）

1. §五三條之抄錄核對表（含命中數）
2. A-PMH03 改判之落實（原文保留之證明）
3. **步驟 3 之雙向複驗全表** —— 逐則、逐方向、漏句逐字
4. 步驟 4 之新檢查清單 ＋ 各 must-hit 之實跑輸出 ＋ **未涵蓋節號之具名**
5. **重寫後之 batch 1 全文** ＋ 擴充後 lint 之輸出
6. 步驟 6 之故意失敗實跑
7. 未結 DR 清單
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
9. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 九、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| **12／13 之 commit 授權** | 12 之 pathspec 見其上繳 §10（12 路徑，含 profile） | 否 |
| `PROFILE_INTEGRATION.md` | 是否登錄本 profile | 否 |
| Q10 | `Product Document 記錄封面頁` | 否，Phase 7 前 |

**batch 1 之人讀覆核已由分析層完成（§四），不需 Pei 介入。**
下一批之開批以本批重寫通過為前提。

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §五 |
|---|---|---|
| R-PMH51 | A-PMH03 之 7.1 改判為漏句；規格比對一律雙向 | ✅ |
| R-PMH52 | lint 須具名未涵蓋節號；全綠不構成 TC 可用之證據 | ✅ |
| R-PMH53 | 拆分後之交叉引用連帶更新 | ✅ |

三條各管一事。
