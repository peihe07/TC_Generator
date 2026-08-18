# B5 —— 殘差詞「措詞差異」抽樣覆核（R-P138）

> 母體：第二批之「措詞差異」桶，共 **120** 個（候選 125 － 依 R-P42 委由他節者 5）。
> 抽樣：`random.seed(19)` ＋ `random.sample(母體, 20)`；**種子值 19（＝本包編號）載明於本檔與 `build_residual_sample.py`**，可重現。
> 抽樣率 **16.7%**。**由分析層覆核。**
> 註：18 包所報之唯一真缺口（`pre`）已由 `043` 補測，故不再出現於本母體。

| leaf | 行為項 | 殘差詞 | 最佳對應 | overlap | 判為措詞差異之理由 |
|---|---|---|---|---|---|
| `SWE-PM-038` | #1 | `like` | `033` | 0.61 | `like` —— 舉例連接詞 |
| `SWE-PM-038` | #8 | `minutesand` | `033` | 0.69 | CFTS 原文之排版黏連（`minutes AND`），非語義單位 |
| `SWE-PM-038` | #11 | `thi` | `034` | 0.60 | `this` 之詞幹，指示代名詞 |
| `SWE-PM-057` | #4 | `respectively` | `018` | 0.60 | 英文連接副詞，無獨立可觀察標的 |
| `SWE-PM-057` | #7 | `user` | `018` | 0.67 | 規格以 `the user can select` 述主體，TC 之 procedure 以祈使句 `Select …` 述同一動作；主體詞於 TC 中不出現屬體例差異 |
| `SWE-PM-057` | #8 | `equal` | `018` | 0.47 | 規格用 `is equal to`，TC 用 `reads` —— 同一斷言之不同措詞 |
| `SWE-PM-057` | #9 | `equal` | `018` | 0.75 | 規格用 `is equal to`，TC 用 `reads` —— 同一斷言之不同措詞 |
| `SWE-PM-057` | #13 | `respectively` | `018` | 0.60 | 英文連接副詞，無獨立可觀察標的 |
| `SWE-PM-060` | #2 | `set` | `022` | 0.67 | `is set to` —— TC 之 pre_condition 以 `is at …` 述同一狀態 |
| `SWE-PM-060` | #2 | `signal` | `022` | 0.67 | `Phone_Call.Info signal` —— TC 以訊號名本身指稱 |
| `SWE-PM-061` | #1 | `only` | `023` | 0.50 | 限定副詞 —— 其語義由否定分支之獨立 TC（`024`）承載，非措詞遺漏 |
| `SWE-PM-063` | #1 | `accord` | `028` | 0.32 | `according to` 之介系詞 |
| `SWE-PM-063` | #1 | `follow` | `028` | 0.32 | `the following` 之文件內指涉，非行為 |
| `SWE-PM-063` | #1 | `parameter` | `028` | 0.32 | `parameters` 之上位詞 |
| `SWE-PM-063` | #1 | `time` | `028` | 0.32 | `time parameters` 之上位詞 |
| `SWE-PM-065` | #1 | `like` | `031` | 0.46 | `like` —— 舉例連接詞 |
| `SWE-PM-065` | #1 | `minutesand` | `031` | 0.46 | CFTS 原文之排版黏連（`minutes AND`），非語義單位 |
| `SWE-PM-065` | #1 | `pass` | `031` | 0.46 | 同 `pas` —— TC 以 `is in … state` 述同一轉換結果 |
| `SWE-PM-065` | #2 | `case` | `032` | 0.36 | `Case 1:` / `In this case` 之文件編號與指涉語 |
| `SWE-PM-065` | #2 | `manage` | `032` | 0.36 | `manage` —— 該行為由 `032` / `034` 覆蓋 |

## 抽中之行為項原文（供對照）

- `SWE-PM-038` #1（最佳對應 `033`，overlap 0.61）：Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN IF RemStartFail = ”True” TLM has to stop its active functi
- `SWE-PM-038` #8（最佳對應 `033`，overlap 0.69）：Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeout1 expiration THENTLM has to set TLM_Status.Info to “Standby” value and to pass to Standby
- `SWE-PM-038` #11（最佳對應 `034`，overlap 0.60）：In this case, TLM has to manage the phone call(s) and to stay in Timed state
- `SWE-PM-057` #4（最佳對應 `018`，overlap 0.60）：so Timeout1 is equal to "00 min" OR "60 minutes" respectively
- `SWE-PM-057` #7（最佳對應 `018`，overlap 0.67）：For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI paramet
- `SWE-PM-057` #8（最佳對應 `018`，overlap 0.47）：For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Se
- `SWE-PM-057` #9（最佳對應 `018`，overlap 0.75）：So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes"
- `SWE-PM-057` #13（最佳對應 `018`，overlap 0.60）：so Timeout1 is equal to "00 min" OR "60 minutes" respectively
- `SWE-PM-060` #2（最佳對應 `022`，overlap 0.67）：For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu
- `SWE-PM-061` #1（最佳對應 `023`，overlap 0.50）：These settings could be only done in TLM Full-Operation Status
- `SWE-PM-063` #1（最佳對應 `028`，overlap 0.32）：In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout
- `SWE-PM-065` #1（最佳對應 `031`，overlap 0.46）：Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before
- `SWE-PM-065` #2（最佳對應 `032`，overlap 0.36）：In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration
