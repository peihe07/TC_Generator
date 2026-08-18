# G150 —— `design_method` 分布與 §12 first-match 走查（R-P223 / T24）

> **本閘不改任何值**（R-P223(c) / §I）—— 只量測與走查，裁定於 32 包。

## 1. 全批分布（264 條）

| design_method | 條 | 佔比 |
|---|---|---|
| 功能測試 (Functional based ; no specific technique) | **90** | 34.1% |
| 狀態轉換 (State Transition Testing) | **90** | 34.1% |
| 決策表 (Decision Table Testing) | **83** | 31.4% |
| 基礎故障注入 (Fault Injection Lite) | **1** | 0.4% |

## 2. 逐 Test Set 分布

| Test Set | 條 | 最大值 | 佔比 | ≥ 60% |
|---|---|---|---|---|
| Branding and Theme | 34 | 功能測試 (Functional based ; no specific technique) | **61.8%** | **是** |
| Power Down | 17 | 功能測試 (Functional based ; no specific technique) | **58.8%** | 否 |
| Power State | 128 | 狀態轉換 (State Transition Testing) | **41.4%** | 否 |
| Startup Display | 59 | 決策表 (Decision Table Testing) | **37.3%** | 否 |
| Timeout Settings | 26 | 狀態轉換 (State Transition Testing) | **42.3%** | 否 |

## 3. 抽樣（種子 `random.Random(31)`，率 ≥ 16.7%）

| Test Set | 母體 | 抽樣 | 率 |
|---|---|---|---|
| Branding and Theme | 21 | **4** | 19.0% |
| **合計** | 21 | **4** | 19.0% |

## 4. §12 逐列 first-match 走查

**相符 0 / 4；不符 2 / 4 = 50.0%**

| tc_id | Test Set | 現值 | §12 首個命中列 | 應為 | 相符 | 依據 |
|---|---|---|---|---|---|---|
| `231` | Branding and Theme | 功能測試 | 第 **9** 列 | Functional Based | **否** | 設定值 → 主題來源，無狀態變更 |
| `234` | Branding and Theme | 功能測試 | — | — | **未走查** | 母體因 38 包改值而變（R-P227） |
| `245` | Branding and Theme | 功能測試 | — | — | **未走查** | 母體因 38 包改值而變（R-P227） |
| `255` | Branding and Theme | 功能測試 | 第 **4** 列 | Decision Table | **否** | `Theme Mode == Auto` ＋ `$Day_Night_Mode$` 二條件 → 主題；無狀態變更 |
