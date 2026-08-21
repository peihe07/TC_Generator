# 裁決台帳（FW036 全案）
欄位：編號｜日期｜標題｜狀態｜出處包｜適用範圍
狀態：ACTIVE / [DEFAULT] / SUPERSEDED / WITHDRAWN
規則：條文全文僅於本台帳落檔一次，各包引用編號不重抄。
撤銷之裁決以刪除線保留並附區塊引註，不得刪除（R-TM13）。

| 編號 | 日期 | 標題 | 狀態 | 出處 | 範圍 |
|---|---|---|---|---|---|
| ~~R-1 v1~~ | 2026-08-21 | ~~訊號記法三層（CAN 採三件組）~~ | **SUPERSEDED** | 01a | 全案 |
| R-1 v2 | 2026-08-21 | 訊號與參數寫法（基準 SWC 0708） | ACTIVE | 09 | 全案 |
| R-2 | 2026-08-21 | spec_reference 家族分流 | ACTIVE | 01a | 全案 |
| R-3 | 2026-08-21 | test_item 上半 50 token | ACTIVE | 01a | 全案 |
| R-4 | 2026-08-21 | verbatim 首字轉大寫 | ACTIVE | 01a | 全案 |
| R-5 | 2026-08-21 | 雙語制合法化不回修 | [DEFAULT] | 01a | BT/Projection |
| S1 | 2026-08-21 | 舊規 superseded | ACTIVE | 01b | 09_ 目錄 |
| S2 | 2026-08-21 | §11 收斂 | ACTIVE | 01a | 全案 |
| S3 | 2026-08-21 | lint 出貨 gate | ACTIVE | 01b | pipeline |
| S4 | 2026-08-21 | test_item 括號下半 | ACTIVE | 01a | 全案 |
| S5 | 2026-08-21 | 裁決台帳制 | ACTIVE | 01b | 流程 |
| S6 | 2026-08-21 | 缺件 PENDING 佔位 | ACTIVE | 01a | 全案 |
| N-1 | 2026-08-21 | N 規制單位為 item，子步驟與續行同受規制 | ACTIVE | 00c/00d | lint |
| R-6 | 2026-08-21 | verbatim 上半豁免 P（訊號記法） | ACTIVE | 03 | lint／全案 |
| R-6b | 2026-08-21 | verbatim 上半豁免 C（hedge）；作者用語品質類檢查僅施於括號下半 | ACTIVE | 06 | lint／全案 |
| R-7 | 2026-08-21 | 值之語意標籤取自 DBC `VAL_` 列舉 | ACTIVE | 09 | 全案 |
| R-8 | 2026-08-21 | spec_reference 一值一行、前綴逐行重述、禁串接；CFTS 列不附檔名章節 | ACTIVE | Pei 直接裁定 | 全案 |

## 條文落檔位置

| 編號 | 條文全文所在 |
|---|---|
| ~~R-1 v1~~ | 已撤銷，見下方撤銷紀錄 |
| R-1 v2 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5 |
| R-6 | 同上 §8.7.5 末段＋`scripts/lint036.py` 檢查 P 之範圍 |
| R-6b | `scripts/lint036.py` 檢查 C 之範圍 |
| R-7 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5(a) |
| R-8 | 同上 §10.7 之「排列」段 |
| R-2 | 同上 §10.7 |
| R-3 | 同上 §4.3.1 |
| R-4 | 同上 §4.3.1 |
| R-5 | 同上 §1（`[OVERRIDE-R5][DEFAULT]`） |
| S1 | 本檔（標記行為見 `docs/fw036/upstream/01b_mechanism_setup.md`） |
| S2 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |
| S3 | `scripts/lint036.py` module docstring |
| S4 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §4.3.1 |
| S5 | `docs/fw036/FEATURE_ONBOARDING.md` §8.9 ＋ 本檔 |
| S6 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.4.3 |
| N-1 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |

## 撤銷紀錄（R-TM13：不刪除，加註保留）

~~**R-1 v1**：CAN 訊號斷言採三件組 `<Signal> in <MESSAGE> on <segment>`，
例 `RemStActvSts in STATUS_BH_BCM2 on BH-CAN`。~~

> **撤銷（2026-08-21，Pei 裁定「都是照我 SWC 怎麼樣寫就這樣寫」）**：
> v1 係分析層自「同一 signal 於 BH-CAN 與 FD-CAN8 皆存在且 message 不同」
> 推導網段必要性而立，**未先查證 Pei 既有交付之實際寫法**。
> 執行層複驗：三件組於 SWC 0708 之 286 列中出現 **0 次**；
> `Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)` 式出現 **546 次／273 列**。
> message 名本身即可判別網段（`BCM_FD_14` → FD-CAN），無須另書。
> 依 v1 已改動之 PM 42 格須回改（下放包 10a §A1）。
>
> **程序原則（09 §五）**：格式類裁決應先窮舉 Pei 既有交付之實際寫法，
> 以語料為權威，分析層僅負責歸納與一致化。
