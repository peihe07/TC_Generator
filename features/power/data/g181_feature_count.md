# G181 —— 第 8 列之功能數謂詞（R-P259）

> §12 第 8 列之**條件欄**為 `End-to-end flow, ≥3 features`；
> 舊謂詞取其 tie-break 之「≥ 3 steps」，**只數步數不數功能**。
> 「功能」＝ `test_procedure` 所觸及之**相異子系統／訊號族**。
> **排除**：TLM / HU / ETM（受測件本身）、CAN / LIN / bus（施測手段）。

## 一、功能族（11 個）

| 族 | 詞彙 |
|---|---|
| 音訊輸出 | `\baudio\b|\bvolume\b|AUD_LVL|\bspeaker\b|\bmute[ds]?\b|\bchime` |
| 電話 | `\bcall\b|\bcalls\b|\bphone\b|\bbluetooth\b|\bhead ?set\b|Phone_Call\.` |
| 畫面顯示 | `\bdisplay\b|\bscreen\b|\bsplash\b|\bbacklight\b|\bimages?\b|\bvisuali[` |
| 品牌與主題 | `\btheme\b|\blogo\b|\bfont\b|\bicon\b|\bbrand` |
| 後視攝影機 | `\bcamera\b|Rear_View|Rear_Camera` |
| 防盜 | `\bantitheft\b|Antitheft_` |
| 電源狀態 | `\bBODY (?:ON|OFF)|\bStandby\b|\bSleep\b|\bTimed\b|\bIdle\b|\bFull-Oper` |
| 設定與選單 | `\bmenu\b|\bsetting\b|\bsettings\b|PROXI|Timeout\d*|_Setting\.|_Timeout` |
| 實體控制 | `\bfront panel\b|\bpanel\b|\bbutton\b|Front_Panel_|CLIMATIC_PANEL|\bHMI` |
| HVAC | `\bHVAC\b` |
| ICS 模組 | `\bICS\b` |

## 二、全批之功能數分布

| 功能數 | 條數 |
|---|---|
| 0 | 45 |
| 1 | 126 |
| 2 | 71 |
| 3 | 20 |
| 4 | 2 |

**≥ 3 者：22 條**

## 三、≥ 3 之逐條

| tc | leaf | 功能 |
|---|---|---|
| `…-007` | `SWE-PM-073` | ICS 模組、電源狀態、音訊輸出 |
| `…-009` | `SWE-PM-073` | HVAC、畫面顯示、電話、音訊輸出 |
| `…-014` | `SWE-PM-073` | HVAC、畫面顯示、電話、音訊輸出 |
| `…-031` | `SWE-PM-065` | 設定與選單、電話、音訊輸出 |
| `…-032` | `SWE-PM-065` | 設定與選單、電話、音訊輸出 |
| `…-033` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-035` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-036` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-037` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-038` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-039` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-040` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-041` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-042` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-043` | `SWE-PM-038` | 設定與選單、電源狀態、電話 |
| `…-056` | `SWE-PM-013` | ICS 模組、電源狀態、音訊輸出 |
| `…-075` | `SWE-PM-019` | 實體控制、畫面顯示、電源狀態 |
| `…-076` | `SWE-PM-019` | 實體控制、畫面顯示、電源狀態 |
| `…-077` | `SWE-PM-019` | 實體控制、畫面顯示、電源狀態 |
| `…-078` | `SWE-PM-019` | 實體控制、畫面顯示、電源狀態 |
| `…-138` | `SWE-PM-046` | 後視攝影機、畫面顯示、音訊輸出 |
| `…-139` | `SWE-PM-046` | 後視攝影機、畫面顯示、音訊輸出 |
