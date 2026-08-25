# VF230 交付說明（**草稿，未送出** —— R-VF27）

**對象**：VF230 之 036 工作簿交付本
**日期**：2026-08-25　**狀態**：草擬（W-VF87.3）

---

## 一、交付之範圍與數

```
已寫入工作簿      438 列（B 欄 244–681 連號）
  量產            435 條（內部 seq 268–702）
  pilot #3          3 條（內部 seq 901–903）
選池（可書寫）    470
隔離               84（其解除各繫於 DR）
去重（可還原）     35（繫於 DR-44）
```

**B 欄 244 起之依據**：Pei 之裁定（跨本續號）。
**其非工作簿內部之機制** —— 見 §四。

---

## 二、隔離之 84 條（**未交付，逐類具名**）

| 類 | 條數 | 其待解者 |
|---|---:|---|
| 純 `propId` 式 | 22 | 條文無 `TELEMATIC_*` 訊號名，TC 之訊號來源未驗（R-VF74） |
| `<Name>.Info` 式 | 4 | DBC 查無同名，或為 service 層介面（DR-36） |
| R-VF81 三（未指名值且無語意對應） | 28 | 訊號送出型，其第一款適用而無語意對應（DR-39） |
| 事實不足以書寫（R-VF80 一） | 30 | 含 PROXI 無值 9（DR-41）、參數名不可執行 5（DR-47 甲）、新形態 4 等 |

**其未交付非遺漏，而是「其事實不足以書寫一條可執行之 TC」** ——
逐條之理由載於 `data/vf230_isolated.tsv`。

---

## 三、交付物中須知悉之三類標記

### 3.1 佔位式 85 條（`Input Test Data` 非 `NA`）

其形如 `IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off), 1 (On)]`。

**其條文未指名所收之值**，故依 canon §8.4.1 之佔位形式處理：
`Input Test Data` 逐字列 DBC 有效值域全集，`Test procedure` 取列舉之**書寫序首值**
為代表值。**該值非條文所指定，其為 DBC `VAL_` 之書寫序首項**
（`reasoning` 欄逐條載此句）。

### 3.2 具名退化之標題 23 條

其 `Test Item` 之標題不含條件子句（如 `X is not displayed`）。
**其成因為 canon §4.3 之 2–14 字限制與區辨要求相衝** ——
長設定名 ＋ 長值使任何帶值之式皆逾 14 字。
**其區辨由正負向承擔**（`is displayed` vs `is not displayed`），
**逐條具名於 `reasoning`**。

### 3.3 `Remarks`（AH 欄）65 條

```
上游 Verification Criteria/Method 自述 `not clear` 之逐字轉錄   63
條文自身不一致之具名（動作動詞與值極性相反）                     2
```

**前者為上游文件之逐字轉錄，非本方之判斷**（R-VF15）。

---

## 四、⚠ B 欄之自動編號機制已失效

**交付本之 B 欄原為公式** `=IF(ISBLANK($D10),"",ROW()-9)`（列 10–246，237 格）。

**本次寫入將該 237 格覆寫為硬值 244–681。**

**其後果**：**該本之自動編號機制自此失效** —— 日後於該本增刪列，
B 欄**不再自動重編**，須手動維護。

**其為裁定之結果**（B 欄須自 244 起，而公式只會算出 `ROW()-9` 即 1 起），
**非疏失**。**列 247–447 原本即無公式**，其為新增之列。

---

## 五、值域來源與其版本

```
DBC   forms/PDT27_E2A_R1_BHCAN2.dbc ＋ forms/PDT27_E2A_R1_FDCAN8.dbc
LID   forms/Logical Identifiers and CAN Mapping v1_78.xlsx
PROXI PROXI_HDCC27_R3_20250424.xlsx
```

**DBC 之換本（自 `R4_BHCAN` ＋ `R5_FDCAN8`）對本交付之 438 列零影響**
—— 其所用之 158 個訊號於新舊二組合皆有且值域一致，**惟其一併修正了一處既有污染**：
`LanguageSelection` 之舊快取為 23 值，係 `BHCAN` 之同名訊號（msg 1468）
合併時污染所致；**其正確值域為 22 值**（`IPC_VEHICLE_SETUP`，msg 1443）。

**LID 之換本（v1_76 → v1_78）對分級零差異**（627 列逐列比對）。

---

## 六、已知而未解者（**交付時仍在**）

| # | 事項 | 其影響 |
|---|---|---|
| 1 | `HeadlightsOffDelay` 之 DBC 標籤為 `90ec`（疑缺 `s`） | 該 leaf 之第四列（`90sec`）未生成（DR-47 乙） |
| 2 | 35 對上游需求其可執行四欄逐字相同 | 已去重，**可還原**（DR-44） |
| 3 | `Greeting_Light` 不在 PROXI 表內；表內有名近之 `Greeting_Lights_Menu` | 2 條標 `PENDING: DR-34`，**未以名近推定其對應** |
| 4 | x14 下拉驗證之 XML 已補回且合法，**其於 Excel 中是否可用未驗** | 須以 Excel 開啟確認 |

---

## 七、R-VF12／R-VF16 之揭露（**本輪已自來源複驗**）

### 7.1 R-VF12 —— 460 條不在交付範圍

> **035 有 1087 條 `Functional Requirement`，其中 460 條於上游尚無 SWE.1 分析，
> 不在本次交付範圍。**

**複驗（自 035／037 原檔）**：
```
035 Basic Report 之 Functional Requirement   **1087**
037 之 11 份分報告所收（619 ＋ 8）             **627**
未收                                          **460**（42.3%）
```

**「覆蓋率」之分母為 627（037 所涵蓋者），非 035 之 1087**（R-VF12）。

### 7.2 R-VF16 —— leaf 母體 627，其中 8 列為刻意之偏離

**複驗（自 035／037 原檔）**：
```
037 之 745 列   Heading 126 ／ Functional Requirement 619
其中 037 判 `Heading` 而 035 判 `Functional Requirement`：**8**
   SWITCH2HoldLastState-058／SWITCH3HoldLastState-063／SWITCH3PowerMode-014
   SWITCH3Type-039／SWITCH5Type-045／SWITCH6HoldLastState-076
   SWITCH6PowerMode-026／SWITCH6Type-051      （**八者集中於 SWITCH 族**）
619 ＋ 8 = **627**，與 `data/vf230_leaves.tsv` 之 627 列**逐一對上**
```

**該 8 列計入可測 leaf 為裁定之偏離，非錯配之修正** ——
其 037 條文逐字為需求形態，而 037 為權威來源，**故本方之分類於該 8 列與 037 相左，
此為刻意且已具名**（R-VF16）。
