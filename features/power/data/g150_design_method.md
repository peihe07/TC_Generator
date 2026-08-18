# G150 —— `design_method` 分布與 §12 first-match 走查（R-P223 / T24）

> **本閘不改任何值**（R-P223(c) / §I）—— 只量測與走查，裁定於 32 包。

## 1. 全批分布（264 條）

| design_method | 條 | 佔比 |
|---|---|---|
| 狀態轉換 (State Transition Testing) | **253** | 95.8% |
| 決策表 (Decision Table Testing) | **9** | 3.4% |
| 功能測試 (Functional based ; no specific technique) | **1** | 0.4% |
| 基礎故障注入 (Fault Injection Lite) | **1** | 0.4% |

## 2. 逐 Test Set 分布

| Test Set | 條 | 最大值 | 佔比 | ≥ 60% |
|---|---|---|---|---|
| Branding and Theme | 34 | 狀態轉換 (State Transition Testing) | **100.0%** | **是** |
| Power Down | 17 | 決策表 (Decision Table Testing) | **52.9%** | 否 |
| Power State | 128 | 狀態轉換 (State Transition Testing) | **100.0%** | **是** |
| Startup Display | 59 | 狀態轉換 (State Transition Testing) | **100.0%** | **是** |
| Timeout Settings | 26 | 狀態轉換 (State Transition Testing) | **100.0%** | **是** |

## 3. 抽樣（種子 `random.Random(31)`，率 ≥ 16.7%）

| Test Set | 母體 | 抽樣 | 率 |
|---|---|---|---|
| Branding and Theme | 34 | **6** | 17.6% |
| Power State | 128 | **22** | 17.2% |
| Startup Display | 59 | **10** | 16.9% |
| Timeout Settings | 26 | **5** | 19.2% |
| **合計** | 247 | **43** | 17.4% |

## 4. §12 逐列 first-match 走查

**相符 17 / 43；不符 26 / 43 = 60.5%**

| tc_id | Test Set | 現值 | §12 首個命中列 | 應為 | 相符 | 依據 |
|---|---|---|---|---|---|---|
| `024` | Timeout Settings | 狀態轉換 | 第 **1** 列 | Negative / Invalid | **否** | **第 1 列即命中** —— procedure 為 `Attempt to change` 而 ER 為「控制項停用／值未變」，即對不允許之操作之否定驗證；全條無任何 A → B |
| `025` | Timeout Settings | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 選單設值後讀回，**無狀態轉換**；tie-break 之 Functional（單一功能）較合，惟其為 3 步，與 tie-break 之「1–2 steps」不完全吻合 —— 仍不屬第 3 列 |
| `029` | Timeout Settings | 狀態轉換 | 第 **3** 列 | State Transition | 是 | ER 載 TLM **leaves Full-Operation state**，為 A → B |
| `030` | Timeout Settings | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 計時器到期觸發計數器啟動，**ER 未斷言任何狀態變更**；第 2 列之 `timeout` 指**注入之故障**，本條為正常行為，不命中 |
| `037` | Timeout Settings | 狀態轉換 | 第 **3** 列 | State Transition | 是 | ER 載 `TLM_Status.Info` 轉 `Standby` |
| `048` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | FULL OPERATION → IDLE |
| `051` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | INIT → Sleep |
| `055` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | 進入 Partial Operation 並以 `$Telematic_Power$` 回報 |
| `058` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | ER 僅 `RemStartFail reads "True"` —— 旗標設定，無狀態變更 |
| `061` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | → Timed |
| `062` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | → Standby（雖有多條件，第 3 列先於第 4 列命中） |
| `070` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | → Idle |
| `073` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | Idle → Standby |
| `096` | Power State | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | **ER 逐字為 `still reads "Timed"` 與 `stays in Timed state`** —— 明示不轉換；其為門開啟＋前狀態＋通話三條件之組合結果，命中第 4 列 |
| `101` | Power State | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | 條件（防盜成功 ＋ `SwitchOff_Timeout_Setting.Req == 00 min`）→ Timeout1 取值；無狀態變更 |
| `111` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | Standby → Partial Operation |
| `112` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | Partial Operation → Standby |
| `128` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 查 FPDM / AMP / ICS / DTV 之可用性，無狀態變更 |
| `135` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | ER 為旗標設為 `True` 與畫面顯示，**未斷言狀態變更** |
| `137` | Power State | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | **ER 明示 `stays in the original Sleep state`** —— 不轉換 |
| `138` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 提供影音，無狀態變更 |
| `140` | Power State | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | **ER 明示 `stays in the original Standby state`** —— 不轉換 |
| `152` | Startup Display | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | `SDARS_Presence` ＋ `Audio_Brand` 二條件 → logo 呈現；無狀態變更 |
| `156` | Startup Display | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | `$VC_SpecialPKG_IC$` ＋ `$VC_MODEL_YEAR$` ＋ `$VC_VEH_LINE$` → 畫面；無狀態變更 |
| `158` | Startup Display | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 單一 DID 值 → logo 取代，無狀態變更 |
| `173` | Startup Display | 狀態轉換 | 第 **3** 列 | State Transition | 是 | Timed → Standby |
| `174` | Startup Display | 狀態轉換 | 第 **3** 列 | State Transition | 是 | Timed → Standby |
| `177` | Power State | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | 條件（長按 ＋ 韌體安裝中）→ 不重置；**ER 為否定結果且無狀態變更** |
| `185` | Startup Display | 狀態轉換 | 第 **3** 列 | State Transition | 是 | power mode 變更確有發生（動畫略過為其伴隨結果） |
| `190` | Startup Display | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 設定值 → 是否伴隨開機音，無狀態變更 |
| `202` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 查音訊關閉與畫面限制，無狀態變更 |
| `203` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 同 `202` |
| `204` | Power State | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 同 `202` |
| `207` | Startup Display | 狀態轉換 | 第 **3** 列 | State Transition | 是 | → Timed mode 之首次轉換 |
| `219` | Startup Display | 狀態轉換 | 第 **3** 列 | State Transition | 是 | → Full Operation 之再次轉換 |
| `222` | Startup Display | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 跨多個點火循環查顯示頻率；**非第 6 列之邊界值**（30 為週期而非門檻±1） |
| `229` | Power State | 狀態轉換 | 第 **3** 列 | State Transition | 是 | IDLE → FULL OPERATION |
| `231` | Branding and Theme | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 設定值 → 主題來源，無狀態變更 |
| `235` | Branding and Theme | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 觀察匯流排送值，無狀態變更 |
| `238` | Branding and Theme | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 品牌值 → 字型映射，無狀態變更（其亦近第 5 列之值域切分，惟第 5 列在第 9 列之前，**若視為值域切分則應為 Equivalence Partitioning** —— 二者皆非現值） |
| `243` | Branding and Theme | 狀態轉換 | 第 **9** 列 | Functional Based | **否** | 同 `238`，映射至 avatar 清單 |
| `255` | Branding and Theme | 狀態轉換 | 第 **4** 列 | Decision Table | **否** | `Theme Mode == Auto` ＋ `$Day_Night_Mode$` 二條件 → 主題；無狀態變更 |
| `261` | Branding and Theme | 狀態轉換 | 第 **6** 列 | Boundary Value Analysis | **否** | **第 6 列即命中** —— `An Ignition On **after the date passes June, 21st**` 為日期界線之驗證，屬 limit / limit±1 |
