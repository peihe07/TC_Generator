# G154 / G155 —— `design_method` 機械提案與「明示不轉換」閘門（R-P226）

> **本腳本不改任何值**（R-P226 / §I）—— 只產出提案與裁決清單，改值於 33 包。

## G155 —— 機械提案 vs 現值（264 條）

| 類 | 數 | 佔比 |
|---|---|---|
| 相符（不改）| **60** | 22.7% |
| **相異 → 人工裁決** | **8** | 3.0% |
| **機械無法判定 → 人工裁決** | **196** | 74.2% |
| **合計入人工裁決** | **204** | 77.3% |

## G154 —— 明示不轉換而標為狀態轉換：**26 條**

| tc_id | 命中字串 | ER 該行 |
|---|---|---|
| `024` | `no change` | 2. The parameter reads back its previous value and no change is stored |
| `028` | `remains in` | 3. Both calls were served and the TLM remains in Timed state |
| `030` | `still at` | 1. Phone_Call.Info is still at "Active" when Timeout1 expires |
| `031` | `remains in` | 2. The DAB Tuner source is active again and the TLM remains in Timed state |
| `032` | `remains in` | 2. The TLM remains in Timed state while the second call runs |
| `034` | `remains in` | 1. The DAB Tuner source is active again and the TLM remains in Timed state |
| `035` | `still at` | 1. Phone_Call.Info is still at "Active" when Timeout1 expires and the MaxCallTim |
| `056` | `stays in` | 1. The TLM stays in Partial Operation without further transition |
| `057` | `does not change` | 1. The interaction that does not change the status is not accepted |
| `071` | `stays in` | 1. The TLM stays in Full-Operation state on the camera activation |
| `075` | `still reads` | 2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown |
| `077` | `still reads` | 2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown |
| `081` | `still reads` | 2. TLM_Status.Info still reads "Full-Operation" and the TLM stays in Full-Operat |
| `088` | `still reads` | 2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state |
| `092` | `still reads` | 2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state |
| `095` | `still reads` | 2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state |
| `096` | `still reads` | 2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state |
| `097` | `does not pass` | 2. TLM_Status.Info does not pass to "Standby" through the transition of this cla |
| `099` | `stays in` | 2. The TLM stays in the original state Partial Operation and the Antitheft scree |
| `130` | `stays in` | 1. The HU stays in Standby mode |
| `136` | `stays in` | 2. The TLM stays in the original Standby state for at most Timeout1, with proper |
| `137` | `stays in` | 2. The TLM stays in the original Sleep state for at most Timeout1, with proper H |
| `140` | `stays in` | 2. The TLM stays in the original Standby state and proper HMI Antitheft screens  |
| `141` | `stays in` | 2. The TLM stays in the original Sleep state and proper HMI Antitheft screens ar |
| `150` | `stays in` | 2. The TLM stays in the original Partial Operation state and proper HMI Antithef |
| `177` | `does not reset` | 2. The HU does not reset due to a power button reset |

## 人工裁決（R-P226(c)(d)）—— 已裁 **32** 條

| tc_id | 現值 | 裁定列 | 裁定 | 依據 |
|---|---|---|---|---|
| `010` | 狀態轉換 | 3 | State Transition（維持現值） | **謂詞偽陽性** —— 命中之 `limit` 出自 `volume limit`（音量上限），非 §12 第 6 列之 limit / limit±1。ER2 載 `returns to its normal maximum`，確有恢復之變化 |
| `011` | 決策表 | 4 | Decision Table（維持現值） | 同 `010` 之偽陽性；現值決策表不動 |
| `024` | 狀態轉換 | 1 | Negative / Invalid | procedure 為 `Attempt to change`，ER 為控制項停用／值未變；全條無 A → B |
| `028` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `030` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `031` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `032` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `034` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `035` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `050` | 狀態轉換 | — | **待裁** | 命中之 `disconnect` 出自前提 `The battery is disconnected` —— §12 第 2 列逐字列 `disconnect` 為 simulated fault 之例，**惟本條之斷電為情境建構（重接後驗設定還原），非注入故障以觀察容錯**。二讀皆有據，**執行層不自行決定** |
| `056` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `071` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `075` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `077` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `081` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `088` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `092` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `095` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `096` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `097` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `099` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `130` | 狀態轉換 | 9 | Functional Based | ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列 |
| `136` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `137` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `140` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `141` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `150` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `177` | 狀態轉換 | 4 | Decision Table | ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列 |
| `259` | 狀態轉換 | 6 | Boundary Value Analysis | 季節起始日（12/21）為界線值 |
| `260` | 狀態轉換 | 6 | Boundary Value Analysis | 季節起始日（3/20）為界線值 |
| `261` | 狀態轉換 | 6 | Boundary Value Analysis | 季節起始日（6/21）為界線值 |
| `262` | 狀態轉換 | 6 | Boundary Value Analysis | 季節起始日（9/23）為界線值 |

**尚未裁決 174 條** —— 其成因為**謂詞過窄**：`ROW3_RE` 未涵蓋 `is in <X> state` 一類措詞，致大量確為狀態轉換者落入「機械無法判定」。

**放寬該謂詞會使更多條判為「相符現值」—— 方向對執行層有利，依 R-P187 不自行為之**；具體之放寬提案見上繳 §五。

## 入人工裁決之逐條（G155）

| tc_id | Test Set | 現值 | 提案列 | 提案 | 命中字串 | 狀態 |
|---|---|---|---|---|---|---|
| `001` | Power Down | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `002` | Power Down | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `003` | Power Down | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `004` | Power Down | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `005` | Power Down | 功能測試 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `006` | Power Down | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `007` | Power Down | 決策表 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `008` | Power Down | 基礎故障注入 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `009` | Power Down | 決策表 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `010` | Power Down | 狀態轉換 | 6 | Boundary Value Analysis | `limit` | **相異 → 人工裁決** |
| `011` | Power Down | 決策表 | 6 | Boundary Value Analysis | `limit` | **相異 → 人工裁決** |
| `012` | Power Down | 決策表 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `013` | Power Down | 決策表 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `014` | Power Down | 決策表 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `015` | Power Down | 決策表 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `016` | Power Down | 決策表 | — | （機械無法判定） | `unchanged` | **機械無法判定 → 人工裁決** |
| `017` | Power Down | 決策表 | — | （機械無法判定） | `unchanged` | **機械無法判定 → 人工裁決** |
| `018` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `019` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `020` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `021` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `022` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `023` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `024` | Timeout Settings | 狀態轉換 | 1 | Negative / Invalid | `Attempt to` | **相異 → 人工裁決** |
| `025` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `026` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `027` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `028` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `remains in` | **機械無法判定 → 人工裁決** |
| `029` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `030` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `still at` | **機械無法判定 → 人工裁決** |
| `031` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `remains in` | **機械無法判定 → 人工裁決** |
| `032` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `remains in` | **機械無法判定 → 人工裁決** |
| `033` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `035` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `still at` | **機械無法判定 → 人工裁決** |
| `036` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `037` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `038` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `039` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `040` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `041` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `042` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `043` | Timeout Settings | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `045` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `046` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `047` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `050` | Power State | 狀態轉換 | 2 | Fault Injection | `disconnect` | **相異 → 人工裁決** |
| `052` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `053` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `054` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `055` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `056` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `057` | Power State | 狀態轉換 | — | （機械無法判定） | `does not change` | **機械無法判定 → 人工裁決** |
| `058` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `059` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `060` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `061` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `063` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `064` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `065` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `066` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `072` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `075` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `077` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `081` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `082` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `086` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `088` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `090` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `092` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `095` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `096` | Power State | 狀態轉換 | — | （機械無法判定） | `still reads` | **機械無法判定 → 人工裁決** |
| `097` | Power State | 狀態轉換 | — | （機械無法判定） | `does not pass` | **機械無法判定 → 人工裁決** |
| `098` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `099` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `100` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `101` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `103` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `104` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `105` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `106` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `108` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `109` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `110` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `114` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `121` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `122` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `123` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `124` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `126` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `127` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `128` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `129` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `130` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `131` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `132` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `133` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `134` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `135` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `136` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `137` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `138` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `139` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `140` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `141` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `146` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `147` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `150` | Power State | 狀態轉換 | — | （機械無法判定） | `stays in` | **機械無法判定 → 人工裁決** |
| `151` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `152` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `153` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `154` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `155` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `156` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `157` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `158` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `159` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `161` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `162` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `163` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `164` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `175` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `176` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `177` | Power State | 狀態轉換 | — | （機械無法判定） | `does not reset` | **機械無法判定 → 人工裁決** |
| `178` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `179` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `180` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `181` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `186` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `187` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `188` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `189` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `190` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `191` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `192` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `193` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `194` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `195` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `196` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `197` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `198` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `199` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `200` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `201` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `202` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `203` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `204` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `205` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `206` | Power State | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `207` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `208` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `209` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `210` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `211` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `212` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `213` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `214` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `215` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `216` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `217` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `218` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `219` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `220` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `221` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `222` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `223` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `224` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `225` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `226` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `227` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `228` | Startup Display | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `231` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `232` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `233` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `234` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `235` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `236` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `237` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `238` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `239` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `240` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `241` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `242` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `243` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `244` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `245` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `246` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `247` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `248` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `249` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `250` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `251` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `252` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `253` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `254` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `255` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `256` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `257` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `258` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `259` | Branding and Theme | 狀態轉換 | 6 | Boundary Value Analysis | `boundary` | **相異 → 人工裁決** |
| `260` | Branding and Theme | 狀態轉換 | 6 | Boundary Value Analysis | `boundary` | **相異 → 人工裁決** |
| `261` | Branding and Theme | 狀態轉換 | 6 | Boundary Value Analysis | `boundary` | **相異 → 人工裁決** |
| `262` | Branding and Theme | 狀態轉換 | 6 | Boundary Value Analysis | `boundary` | **相異 → 人工裁決** |
| `263` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
| `264` | Branding and Theme | 狀態轉換 | — | （機械無法判定） | `` | **機械無法判定 → 人工裁決** |
