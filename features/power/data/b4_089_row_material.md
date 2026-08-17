# B4 —— R-P116 之裁定素材（`SWE-PM-089` 佔不佔列）

> **本檔僅為裁定素材。R-P116 明訂屬交付形式，分析層不自裁；
> 執行層依 16 §I 不實作任何一種處置、不提出建議。**
> 三份工作簿皆 `read_only=True`，未呼叫 `save()`。

## 1. Comfort 已交付件中是否存在「僅填 `req_id` 而其餘欄留空」之列

依 **R-P80**，僅取其結構性事實。

| 量測項 | 值 |
|---|---|
| `D` 欄（Requirement or Design ID）非空之列 | **466** |
| 其中「僅 `D` 欄（＋`B` 序號）有值、其餘 33 欄全空」者 | **0** |

即：**Comfort 之已交付件無此形態之先例。**
（此為事實陳述，不蘊含任何一種處置為正確。）

## 2. 037 之 `SWE-PM-088` / `089` / `090` 三筆

取自 `Power_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
之 `SWE1 Requirements` 分頁（G0 台帳內之素材）。

| 欄 | SWE-PM-088 | **SWE-PM-089** | SWE-PM-090 |
|---|---|---|---|
| Source Requirement ID | `Sys-RA-PM-0331` | **`SWE1-PM-ANT-008`** | `Sys-RA-PM-0343` |
| Requirement Title | Vehicle Line-Based Performance Gauge Selection | **Seasonal Startup Animation Selection** | Auto Theme Mode Selection |
| Categorization | Functional Requirement | **Functional Requirement** | Functional Requirement |
| Sub Categorization | HMI Service | **HMI Service** | HMI Service |

**與 R-P1 / DR-PW1 直接相關之事實**：`089` 之 `Source Requirement ID` 為
`SWE1-PM-ANT-008` —— **非 `Sys-RA-*` 形態**，故 §C rule 1 之錨點鏈於此斷開，
此即該 leaf 依 R-P1 留空之原因。088 / 090 皆為正常之 `Sys-RA-PM-*`。

其 `Categorization` 與 `Sub Categorization` 與前後兩筆**完全相同**，
即：**從 037 之分類欄看不出 089 有任何特殊性**，其特殊性全在來源 ID 之形態。

## 3. 二種處置對列數與 B 欄序號之影響

前提：R-P113(e) —— 工作簿列序即 SWE-PM ID 序，故 `089` 之位置介於
`088` 之末條與 `090` 之首條之間。設全案 TC 總數為 `N`（尚未定，
首批 3 leaf 已產出 15 條）。

| | （甲）保留一列空白 | （乙）整列跳過 |
|---|---|---|
| 工作簿資料列數 | **N + 1** | **N** |
| `B` 欄序號最大值 | N + 1 | N |
| `089` 之後所有列之 `B` 值 | 較（乙）**各 +1** | —— |
| 最終 `tc_id` 之連號 | 若該空列**不配 tc_id**，則 tc_id 仍為 1..N 而**列號與 tc_id 自 089 之後全面錯開**；若配 tc_id，則有一個 tc_id 對應不到任何 TC | tc_id 與列號自始至終一致 |
| 客戶以 037 比對時 | 037 之 115 筆與工作簿逐筆對得上（含 089 之空列）| 工作簿無 089 之痕跡，需另行說明其缺席 |
| 涵蓋率之呈現 | 空列會被計入列數，若有人以「列數 / 037 筆數」計算覆蓋率將失真 | 不受影響 |

**114 / 115 之關係**：037 有 **115** 筆 SWE-PM ID（G1 實測，連續），
其中 `089` 依 R-P1 不產 TC，故可測者 **114**。
§E 之 `63 / 24 / 16 / 8 / 3 = 114` 為 **leaf 數**，非 TC 數 ——
TC 數因 §8.2.2 拆分而大於 114（首批 3 leaf 已產 15 條）。
**二種處置皆不影響 §E。**

---

**執行層未提出建議，未實作任何一種（16 §I）。**
