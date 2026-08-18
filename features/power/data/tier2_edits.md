# B2 —— 第二級改值紀錄（R-P261）

> 模式：**套用**；改動 **2** 處；**標籤缺漏而未改 11 條**。

## 一、`design_method` 分布（前 → 後）

| 值 | 前 | 後 |
|---|---|---|
| 功能測試 (Functional based ; no specific technique) | 88 | **90** |
| 基礎故障注入 (Fault Injection Lite) | 1 | **1** |
| 決策表 (Decision Table Testing) | 84 | **83** |
| 狀態轉換 (State Transition Testing) | 91 | **90** |

## 二、`priority` 分布（前 → 後）

| 值 | 前 | 後 |
|---|---|---|
| P0 | 157 | **157** |
| P1 | 60 | **60** |
| P2 | 7 | **7** |
| P3 | 40 | **40** |

## 三、標籤缺漏而未改 —— **11** 條

> §12 之完整標籤表不在本庫；執行層**不自行擬定 canon 值**
> （34 包 G167 / 36 包 §4.6 之先例）。待分析層提供。

| tc | 應為 | 現值 | 依據 |
|---|---|---|---|
| `…-007` | 第 8 列 | 決策表 (Decision Table Testing) | first-match：跨 3 個功能：ICS 模組、電源狀態、音訊輸出 |
| `…-015` | 第 5 列 | 決策表 (Decision Table Testing) | first-match：out of range |
| `…-024` | 第 1 列 | 狀態轉換 (State Transition Testing) | first-match：Attempt to |
| `…-034` | 第 -1 列 | 狀態轉換 (State Transition Testing) | first-match：transition to ／ remains in |
| `…-056` | 第 8 列 | 狀態轉換 (State Transition Testing) | first-match：跨 3 個功能：ICS 模組、電源狀態、音訊輸出 |
| `…-071` | 第 -1 列 | 狀態轉換 (State Transition Testing) | first-match：passes to ／ stays in |
| `…-222` | 第 5 列 | 狀態轉換 (State Transition Testing) | first-match：a value other than |
| `…-259` | 第 6 列 | 狀態轉換 (State Transition Testing) | first-match：boundary |
| `…-260` | 第 6 列 | 狀態轉換 (State Transition Testing) | first-match：boundary |
| `…-261` | 第 6 列 | 狀態轉換 (State Transition Testing) | first-match：boundary |
| `…-262` | 第 6 列 | 狀態轉換 (State Transition Testing) | first-match：boundary |

## 三之二、逾 G164 受檢範圍而亦命中裝飾性者 —— **5** 條

> 其不在 G164 之提案內（該提案之範圍為全部 P0 ＋ Branding and Theme），
> 故**本包不改**；列出供分析層裁定是否納入下一輪。

| tc | 現值 | `tc_title` |
|---|---|---|
| `…-156` | P1 | The special package drives the Klipsch Splash Screen on the 2025 model year |
| `…-157` | P1 | The splash screen type drives the Klipsch Splash Screen after the 2025 model year |
| `…-200` | P1 | The special package drives the Klipsch Splash Screen on the 2025 model year |
| `…-201` | P1 | The splash screen type drives the Klipsch Splash Screen after the 2025 model year |
| `…-226` | P1 | A missing TBM adds the ADAS text to the disclaimer |

## 四、逐條改動（2）

| 欄 | tc | 舊 | 新 | 依據 |
|---|---|---|---|---|
| `design_method` | `…-010` | 狀態轉換 (State Transition Testing) | **功能測試 (Functional based ; no specific technique)** | first-match：（第 1–8 列皆未命中） |
| `design_method` | `…-011` | 決策表 (Decision Table Testing) | **功能測試 (Functional based ; no specific technique)** | first-match：（第 1–8 列皆未命中） |
