# 下放包 18 —— 五列定案、二項更正、Layer 2 全定稿、Phase 4 pilot 啟動

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`17_islands.md`；對應上繳：`docs/upstream/17_pilot_material.md`
- 裁定狀態：五個 `PROVISIONAL-ROW` 全部定案、R-SU21 v2、R-SU22.3 結案 —— 分析層即裁
- **Layer 2 自本包起無 provisional 列，R-SU20(f) 之寫回前要求已滿足**

---

## 一、上繳包 16 審查判定

**收。四個主結果中，二個是對分析層條文之否證。**

### 1.1 R-SU21(b) 之「8 群」實為 9 —— **分析層之誤，且其形狀最值得記**

漏列 `SWE1-FOTA-085`（`FOTA ROV Reflash Requirements`）。

> **一條專為 0 列群而設的條文，自己漏掉一個 0 列群。**

此為 PLAYBOOK §7(13)（0 列物件是閉合檢查之系統性盲區）**在條文層之再現** ——
寫條文時我逐一列舉，而列舉本身就是「以量為準」之作業，
**對零同樣無感**。§三 v2 更正。

### 1.2 R-SU22.3 之實測翻轉一個「缺項」—— 採認

驗證母體 311 列之 `Priority` 空白為 **0**（271 High + 34 Medium + 6 Low = 311）。
上繳包 15 §4.2 所列之「空白 72 列處置未裁」為**硬缺**，
實測後不成立 —— 那 72 列全部落在 311 之外。

**該缺項撤銷。** R-SU22.3 之要求已滿足，本項結案。

### 1.3 §6.1 關鍵詞測之自我限定 —— 採認，且其結論正確

「組名實詞出現於該列標題」可機器測，本輪 5/7 命中；
**但它測得的是循環之風險，非循環之事實** —— `339`／`358` 皆被標記，
而下放包 17 §四裁定二者維持。

**裁定**：該量為 **flag，非判準**。命中者須有記名依據方得維持
（此即 R-SU20(d) 之操作化）；命中不等於錯，未命中不等於對。

### 1.4 §5.2 之未要求探針 —— 採認並嘉許

空寫回 48 部件逐 byte 全同雖為必要，但**不能證明「有寫入時仍保全」** ——
執行層自行加了實寫 1 列之探針，證實 `<row>` 屬性、34 個儲存格與
全部 `s=` 樣式索引皆保全。**空測通過與實測通過是兩件事，自己補上了。**

---

## 二、五個 `PROVISIONAL-ROW` 之定案

依 T30a 之九列全文裁定。**每列之依據皆取自 Description 之內容，
非其標題關鍵詞**（R-SU20(d)）。

| 037 列 | 定案 | 記名依據 |
|---|---|---|
| `338` | **維持 `Integrity Verification`** | 其述「verify the **authenticity of the deployment package**」，與 `312`「perform the **integrity verification of the deployment package**」為**同一驗證對象**之一對（完整性／真確性）。前鄰 `337` 之述為「使部署包可用、啟動部署工作流」——**流程步驟**，其對象為工作流而非驗證。故 `338` 從對象走，不從流程走 |
| `357` | **維持 `Interruption Handling`** | 其首句「save the installation state when an interruption occurs … resume when the interruption condition is cleared」與 `360`（detect→save→resume）、`325`（suspend→record→wait until resumed）為**同一三段結構**。⚠ 其次句「report the installation status … to the SWMC」屬回報，**該列為雙職** —— 撰寫 TC 時依 IN §8.2.2 得拆為 2 TC，二者皆 trace 本列 |
| `359` | **改置 `Interruption Handling`**（原 `Session Management`） | 其述「**ignore any request to start a new OTA update flow when a session is already active** and ensure the current session is not interrupted」，與 `323`「**queue an incoming NIA received during an active OTA update session** without interrupting the current session」為**同一觸發面**（作用中 session 期間之外來請求）與**同一保護目標**（不中斷現行 session），差別僅在處置動作（ignore vs queue）。`323` 之 GT 正解為 `4907677`（章 `4.12`），本列從之 |
| `360` | **維持 `Interruption Handling`** | 其述「detect interruptions … save the current download state … resume when the interruption condition is cleared」與 `325`／`321` 同族，對象同為下載階段之中斷。**依據為三段結構與對象，非標題之 `Interruption` 一詞** |
| `361` | **維持 `Session Management`** | 其約束對象為「**server-initiated OTA update flows**」，與 `351`／`368`／`369` 同一流程族；「背景執行不阻斷前景」為該流程之**執行約束**，非獨立能力。⚠ 併記其族緣：`284`（Low Priority Execution，GT 正解 `4907440`、章 `4.7.1`）述同型之背景執行約束 —— **Layer 3 對本列須並列 `4.7.1` 之可能** |

### 2.1 列數之更動

`Session Management` 14 → **13**；`Interruption Handling` 18 → **19**。
其餘 19 組不變。合計仍 **311**。三重閉合須重跑（T31a）。

### 2.2 `PROVISIONAL-ROW` 全數解除

Layer 2 自本包起**無 provisional 列**，R-SU20(f)（不得帶入寫回）之要求已滿足。

---

## 三、R-SU21 v2（抄入 RULINGS.md，逐字，append 於 v1 之後）

```
R-SU21 v2（切分原則之射程與 0 列群之效力 —— 0 列群清單之更正）

v1(a)(c) 維持。(b) 更正。

(b) v2 —— **0 列 Heading 群為 9 群**（v1 誤載為 8 群並漏列
    `SWE1-FOTA-085`）：
    `016`, `017`, `020`, `022`, `072`, `073`, `074`, `076`, **`085`**

    v1 之漏列，其成因為**條文之列舉本身即「以量為準」之作業，
    對零同樣無感** —— PLAYBOOK §7(13) 在條文層之再現。
    記明：**寫「關於零之條文」時，其列舉須以程式產生，不得人手列**。

    其歸屬維持（供導航與群數閉合），**不具交付效力**（v1(b)(c) 不變）。
```

---

## 四、Phase 4 —— pilot 啟動

### 4.1 pilot 標的：`Silent Update`（9 列）

選定依據：
- **Layer 3 有 GT 支持**（`4.7.3.2 Silent Updates`；GT 列 `176`／`179`／`180`）
- 規模適中（9 列），含 HMI 列 1（`177`）與 Service 列 8，可同時試 UI 型與 Service 型
- 其中 `175`／`176`／`177` 來自 `170` 群、`179`–`184` 來自 `178` 群 ——
  **可一併驗證跨 Heading 群之 Test Set 在撰寫面是否成立**

### 4.2 本輪不寫 TC

pilot TC 由分析層起草（vehicle_category 之 `08_pilot`／`10_pilot_tc` 同制），
起草所需之材料尚缺。**T31 只備料，不產出任何 TC。**

---

## 五、任務（T31）

| # | 任務 |
|---|---|
| T31a | **三重閉合重跑**（§2.1 之更動後）：列數 311／群數 45／列 id 聯集 311 且不相交。**併跑孤島列檢查**（R-SU20）—— `359` 改組後之孤島清單與各組連續段數須重出，**新產生之孤島列須列出**（改組可能製造新孤島） |
| T31b | **pilot 材料傾印**：`Silent Update` 9 列（`175`,`176`,`177`,`179`,`180`,`181`,`182`,`183`,`184`）之：id、`Requirement Title`、**`Requirement Description` 全文**、`Sub Categorization`、`Priority`、`Source Requirement ID`、**路徑 A 前 5 候選**（ObjectID、母章、分數、**候選物件全文**）。**併**：標示各列是否落入機制 3（低分偵測器，門檻 0.267）或為自證錨／區塊成員 |
| T31c | **`framework.md` 更新**：五列定案（含 §二之記名依據逐列寫入）；`Session Management` 13／`Interruption Handling` 19；`PROVISIONAL-ROW` 標記全部移除；0 列群改 9 群並依 R-SU21 v2(b) 加註；`361` 之 Layer 3 併列 `4.7.1` 之可能 |
| T31d | **0 列群清單之程式化**（R-SU21 v2(b) 之要求）：`scripts/layer2_close.py` 增一項 —— 0 列 Heading 群之清單由程式產生並與 `framework.md` 所載比對，不符即停 |
| T31e | **T-抄**：R-SU21 v2 逐字 append；索引表同步（22 條現行、R-SU21→v2；留存 13 條）。PLAYBOOK 追加二則：(1)「寫『關於零之條文』時，其列舉須以程式產生 —— 人手列舉對零同樣無感」（出處：上繳包 16 §主結果 2）；(2)「空測通過與實測通過是兩件事」（出處：上繳包 16 §5.2 之自加探針） |

**T27 併行線之人裁（80 筆）仍待分析層**，優先序不變。

**不在本輪**：TC、實際寫回、git。

---

## 六、上繳包要求（`docs/upstream/17_pilot_material.md`）

1. T31e 核對結果 + 索引表
2. T31b 之 pilot 材料 —— **本輪核心，分析層據以起草 pilot TC**
3. T31a 之三重閉合與孤島列重跑結果（**新孤島列須明列**）
4. T31c／T31d 之結果
5. 未結 DR
6. 獨立自評 —— 特別回答：**`359` 改組後，`Session Management` 與
   `Interruption Handling` 二組之連續段數如何變化，該變化是否使切分更碎**
