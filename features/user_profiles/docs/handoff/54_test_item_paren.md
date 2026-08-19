# 54 下放包 — Test Item 括號內容之缺漏（交付後發現）

**本包無裁決條文。** Pei 於 ENTRY 002 產出後指出：
**Test Item 欄下方應自動產生之括號內容未填入**，且以「又」字指其為**再次發生**。

## 一、分析層之自陳

**18 支閘與 8 項交付前自檢，無一項檢查 Test Item 欄之括號內容。**
成因不是漏跑，是**該規格從未被寫下來** ——
`framework.md`、profile、`feature.yaml`、canon §4.3（tc_title 三種形狀）
皆未提及括號內容。

**「又」字表示其跨 feature 重複發生** —— 若前一個 feature 已犯過同一件事，
那不是本 feature 之疏漏，是**規格從未落檔**（同 G-C：
沒有被任何程式讀取的設定值，會一直看起來像是決定過的）。

## 二、作業（**先找規則，再量形態**）

### 0. **先找 Pei 所寫之規則**（最優先）

Pei 指出：**該規則應已寫過** ——
「產測項之內容應該也要有一個自己的 title，又是簡短說明這條測項在測試什麼」。

即 `Test Item` 欄之內容為 **標題 ＋ 一段簡短說明「本條在測什麼」**，
而非僅 `tc_title` 一句。

**作業**：全 repo 搜尋該規則之落點，**逐一列出命中之檔與其原文**：

```
搜尋範圍：docs/**、features/*/（含 PLAYBOOK.md、profile、framework.md、
          RULINGS.md、DECISIONS.md、RUNBOOK.md、scripts/**）
關鍵詞：test_item / Test Item / 測項 / 標題 / title / 簡短說明 / 括號 /
        自己的 title
```

**三種結果，處置各不相同**：

| 結果 | 意義 | 處置 |
|---|---|---|
| **repo 內有** | 規則存在而我方未讀到 —— **連續兩個 feature 未套用** | 屬**執行與覆核之失效**，非規格缺漏；須查為何 prompt 與閘皆未涵蓋它 |
| **僅在他 feature 之交付件中體現，repo 無文字** | 規則只存在於產物，未成文 | 由產物反推並補寫成文 |
| **皆無** | 規則從未落檔 | 依 Pei 本輪之陳述立為規格 |

**不得以「找不到」直接跳到第三種** —— 搜尋判準須具名，
且依 G-I：詞表含中文者不得用 `\b`。

### 1. 量 Comfort 與 Home 之交付件 Test Item 欄（唯讀）

`features/comfort` 之**交付件**，逐列讀 Test Item 欄：

- 含括號內容之列數 / 總列數
- **括號內容之形態**逐類列出（前 20 個相異值）
- 其與同列他欄之關係：是否等於 Requirement ID、spec 節次、
  Test Set、design_method、或其他欄之衍生
- 括號在欄內之**位置**（同一儲存格內換行？行尾？獨立一行？）

**同時量 Home 之交付件**（`forms/…_SWQT_Home_20260809.xlsx`，rev A/B，
Arif 之 done region 144 列）—— **那是人手寫的，其形態即原始意圖**。

### 2. 量本 feature 之現況

ENTRY 002 之 Test Item 欄：含括號者 0 或 n？若 n > 0，其來源為何？

### 3. 由量測結果反推規格，寫成可測之判準

**不由分析層或執行層自擬** —— 依 §7.4／G-M：
**先查他 feature 之交付件與素材，再論裁示。**

若兩份交付件之形態一致 → 該形態即規格，寫入 profile 並立閘；
若不一致或皆為空 → 具名回報，屬交付形式（Tier 3），送 Pei。

### 4. 立閘（形態確定後）

`audit_delivery_fields` 增一項：Test Item 欄之括號內容依規格存在且正確。
**含方向性案例**：缺括號者轉紅、括號內容與其來源欄不符者轉紅。
**首跑須對 ENTRY 002 之現況轉紅**（G-K：報 0 命中前先證明它對已知案例會叫）。

## 三、ENTRY 003 之範圍（一次落地，G-J）

本輪之修正與下列一併重出：

1. Test Item 括號內容（本包）
2. **`TC-165` 之覆核** —— 分析層 189 條中唯一未讀者（`SWE1-HMI-PROF-063`，
   7.4.1，`The 30 seconds should not include when the vehicle is in remote start`）；
   本層於本輪讀畢，有 defect 則併入
3. `TC-167` 之 `specification_reference` 併列 Tutorials L&F ——
   **若該 PDF 已落 `inputs/`**（G-L：沒有路徑的「到齊」不算到齊）；
   未落則維持具名缺口

## 四、跨 feature（承 R-U44 之觸發點）

若 §二之量測顯示 Comfort／Home 之交付件亦缺該內容，
**登記為跨 feature note**，於各該 feature 下次開輪次時處理。
**本輪不寫入他 feature 任何檔。**

## 五、不在本包授權範圍

- 自擬括號內容之規格（§二第 3 項）
- 交付、git、RD 寄出 —— 屬 Pei
- 寫入他 feature 之檔（§二為唯讀）

## 六、上繳

`docs/upstream/54_test_item_paren.md`，更新 `docs/INDEX.md`，附獨立判斷。
**§二之量測結果為本包之主要產出** —— 規格由它反推，不由記憶反推。
