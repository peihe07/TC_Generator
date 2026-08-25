# W-VF70 §2 —— C 類「條文之值對不上 DBC 值域」逐條成因

**C 類現為 8 條**（W-VF69 首報 15 條，其中 7 條經 W-VF70 修正抽取式後回收 ——
其非資料缺陷，而是值之終點由散文界定所致，見上繳 V30 §3）。

**只判不改**（V30 §5.2）。(a)／(b) → DR-40；(c) → 本層已修正。

| leaf | 訊號 | 條文之值 | DBC 值域 | 成因 | 依據 |
|---|---|---|---|---|---|
| `SWE1-VC-PowerTailgate-025` | `Power_Tailgate_Enable_Req` | `Disable` | ['Disabled', 'Enabled'] | **(b) 條文誤植** | 條文 `Disable`／DBC `Disabled` —— 差一字尾 `d`，二側指同一值之機率高，惟本層不代為補字 |
| `SWE1-VC-PowerTailgate-026` | `Power_Tailgate_Enable_Req` | `Enable` | ['Disabled', 'Enabled'] | **(b) 條文誤植** | 條文 `Enable`／DBC `Enabled` —— 同上 |
| `SWE1-VC-DaytimeRunningLights-005` | `DRLEnable_Req` | `Early` | ['False', 'True'] | **(b) 條文誤植** | 條文之值 `Early` 屬時序／靈敏度類語彙，而 `DRLEnable_Req` 之 DBC 值域為 `False`／`True`（開關）。**條文之動作句亦自相矛盾**：「chooses to **disable** … setting **to Early**」 |
| `SWE1-VC-EngineOffPowerDelay-047` | `Eng_Off_Pwr_Delay_Req` | `Forty_Five_Sec` | ['Five_Min', 'Fourty_Five_Sec', 'Ten_Min'] … | **(a) DBC 值域拼字** | 條文 `Forty_Five_Sec`／DBC `Fourty_Five_Sec` —— **DBC 側為英文拼字錯誤**（`Fourty` 非英文正詞）。條文側正確 |
| `SWE1-VC-TrailerBrakeType032` | `Trail_Brk_Type_Req` | `One` | ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric'] … | **(b) 條文誤植** | 條文 `Trail_Brk_Type_Req signal value as One`，而該訊號值域為 `Heavy_Electric` 等制動型別；`One` 屬同條文後句所引之 `Trail_Num_Req`（值域 One/Two/…）。**本層曾自動改取後者，已撤回** —— 值屬條文所指名之訊號，換訊號即以推測消解不符 |
| `SWE1-VC-TrailerBrakeType033` | `Trail_Brk_Type_Req` | `Two` | ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric'] … | **(b) 條文誤植** | 同 `-032`，其值為 `Two` |
| `SWE1-VC-TrailerBrakeType034` | `Trail_Brk_Type_Req` | `Three` | ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric'] … | **(b) 條文誤植** | 同 `-032`，其值為 `Three` |
| `SWE1-VC-TrailerBrakeType035` | `Trail_Brk_Type_Req` | `Four` | ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric'] … | **(b) 條文誤植** | 同 `-032`，其值為 `Four` |

## 分類彙總

| 成因 | 條數 | 處置 |
|---|---|---|
| (a) DBC 值域拼字 | 1 | **DR-40** |
| (b) 條文誤植 | 7 | **DR-40** |
| (c) 本層抽到錯的訊號／值 | 7（已修正，不計入現行 C 類） | 值之終點改由 DBC 值域界定；撤回自動換訊號 |

