# G164 —— `priority` 全面重判提案（R-P237）

> **本檔只出提案，不改任何 `priority` 值。**
> 受檢範圍：全部 **P0 193 條** ＋ Branding and Theme 全 **34** 條，去重後 **201** 條 / 264。
> 謂詞取自 §10.2 之字面 P0 類別，非自語料回推；命中字串逐條列出為證。
> 代理判準不得凌駕實質判準（§5a）—— 最終判定屬人工。

## 一、彙總

| 判定 | 條數 |
|---|---|
| P0 成立 | **108** |
| **無 P0 類別命中，亦非裝飾性** | **53** |
| **無 P0 類別命中；命中裝飾性／個人化** | **40** |

## 二、逐條

| tc_id | test set | 現值 | 命中之 §10.2 P0 類別（證據） | 判定 | 提案 |
|---|---|---|---|---|---|
| `005` | 1_power_down | P0 | boot / recovery（開機與復原） → `boot` | P0 成立 | P0 |
| `007` | 1_power_down | P0 | audio output（音訊輸出） → `volume`；eCall → `Ecall`；vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `STATUS_LIN.` | P0 成立 | P0 |
| `009` | 1_power_down | P0 | boot / recovery（開機與復原） → `BODY ON`；audio output（音訊輸出） → `volume`；eCall → `Ecall`；vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `STATUS_LIN.` | P0 成立 | P0 |
| `033` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `034` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby`；connection（連線） → `bluetooth` | P0 成立 | P0 |
| `035` | 2_timeout_settings | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `036` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `037` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `038` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `039` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `040` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `ignition off` | P0 成立 | P0 |
| `041` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `042` | 2_timeout_settings | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `043` | 2_timeout_settings | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `044` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `045` | 3_power_state_a | P0 | connection（連線） → `CarPlay`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `046` | 3_power_state_a | P0 | connection（連線） → `CarPlay`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `047` | 3_power_state_a | P0 | connection（連線） → `CarPlay`；audio output（音訊輸出） → `mute` | P0 成立 | P0 |
| `048` | 3_power_state_a | P0 | connection（連線） → `CarPlay`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `049` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `050` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `051` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `052` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `053` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `054` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `055` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `056` | 3_power_state_a | P0 | audio output（音訊輸出） → `chime` | P0 成立 | P0 |
| `058` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `ignition off` | P0 成立 | P0 |
| `059` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `060` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `061` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `062` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `063` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `064` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `065` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `066` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `067` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `068` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `071` | 3_power_state_a | P0 | safety（安全） → `rear view camera` | P0 成立 | P0 |
| `072` | 3_power_state_a | P0 | safety（安全） → `rear view camera`；audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `073` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition off` | P0 成立 | P0 |
| `074` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `075` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `076` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `077` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `078` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `079` | 3_power_state_a | P0 | connection（連線） → `CarPlay` | P0 成立 | P0 |
| `080` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `081` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `082` | 3_power_state_a | P0 | safety（安全） → `rear view camera` | P0 成立 | P0 |
| `083` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `084` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition Off` | P0 成立 | P0 |
| `085` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition Off` | P0 成立 | P0 |
| `086` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `087` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `088` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `089` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `090` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `091` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `092` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `093` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `094` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `095` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `098` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `099` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `100` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `101` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `102` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `103` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `104` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `105` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `106` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `107` | 3_power_state_a | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `108` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `109` | 3_power_state_a | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `110` | 3_power_state_a | P0 | safety（安全） → `Rear view camera`；boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `111` | 3_power_state_a | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `112` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `113` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Ignition Off` | P0 成立 | P0 |
| `114` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `115` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `116` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `117` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `118` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `119` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `120` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `122` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `123` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `125` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `power down` | P0 成立 | P0 |
| `126` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Ignition Off` | P0 成立 | P0 |
| `127` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `128` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Ignition Off` | P0 成立 | P0 |
| `129` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `130` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `132` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `133` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `134` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `135` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `136` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `137` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `138` | 4_power_state_b | P0 | safety（安全） → `Rear view camera`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `139` | 4_power_state_b | P0 | safety（安全） → `Rear view camera`；audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `142` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `143` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `144` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `145` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `147` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `149` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `150` | 4_power_state_b | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `151` | 4_power_state_b | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `152` | 4_power_state_b | P0 | audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `153` | 4_power_state_b | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `154` | 4_power_state_b | P0 | audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `155` | 4_power_state_b | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `160` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `161` | 4_power_state_b | P0 | boot / recovery（開機與復原） → `boot` | P0 成立 | P0 |
| `162` | 5_startup_display | P0 | eCall → `SOS` | P0 成立 | P0 |
| `163` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `164` | 5_startup_display | P0 | connection（連線） → `paired` | P0 成立 | P0 |
| `165` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `166` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `167` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `168` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `169` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Body OFF` | P0 成立 | P0 |
| `170` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Body OFF` | P0 成立 | P0 |
| `171` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Body OFF` | P0 成立 | P0 |
| `172` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `173` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `174` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `175` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `176` | 5_startup_display | P0 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P0 |
| `178` | 5_startup_display | P0 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `Door_Ajar_Status` | P0 成立 | P0 |
| `179` | 5_startup_display | P0 | boot / recovery（開機與復原） → `STANDBY`；vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `Door_Ajar_Status` | P0 成立 | P0 |
| `180` | 5_startup_display | P0 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `Door_Ajar_Status` | P0 成立 | P0 |
| `181` | 5_startup_display | P0 | boot / recovery（開機與復原） → `STANDBY` | P0 成立 | P0 |
| `182` | 5_startup_display | P0 | boot / recovery（開機與復原） → `BODY ON` | P0 成立 | P0 |
| `183` | 5_startup_display | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `184` | 5_startup_display | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `185` | 5_startup_display | P0 | boot / recovery（開機與復原） → `BODY ON`；vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `Door_Ajar_Status` | P0 成立 | P0 |
| `188` | 5_startup_display | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `190` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup`；audio output（音訊輸出） → `sound` | P0 成立 | P0 |
| `191` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup`；audio output（音訊輸出） → `sound` | P0 成立 | P0 |
| `195` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup`；audio output（音訊輸出） → `sound` | P0 成立 | P0 |
| `196` | 5_startup_display | P0 | audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `197` | 5_startup_display | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `198` | 5_startup_display | P0 | audio output（音訊輸出） → `audio` | P0 成立 | P0 |
| `199` | 5_startup_display | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `202` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Ignition On`；audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `203` | 5_startup_display | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `204` | 5_startup_display | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `205` | 5_startup_display | P0 | audio output（音訊輸出） → `Audio` | P0 成立 | P0 |
| `207` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `208` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `209` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `210` | 5_startup_display | P0 | boot / recovery（開機與復原） → `Standby` | P0 成立 | P0 |
| `211` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `212` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `219` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `220` | 5_startup_display | P0 | eCall → `SOS` | P0 成立 | P0 |
| `221` | 5_startup_display | P0 | eCall → `SOS` | P0 成立 | P0 |
| `222` | 5_startup_display | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `223` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup`；eCall → `SOS` | P0 成立 | P0 |
| `224` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `225` | 5_startup_display | P0 | boot / recovery（開機與復原） → `startup`；eCall → `SOS` | P0 成立 | P0 |
| `228` | 5_startup_display | P0 | eCall → `SOS` | P0 成立 | P0 |
| `229` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `230` | 5_startup_display | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `231` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `232` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `233` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `234` | 6_branding_theme | P0 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P0 |
| `235` | 6_branding_theme | P0 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P0 |
| `236` | 6_branding_theme | P1 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P1（維持） |
| `237` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `238` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `239` | 6_branding_theme | P1 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `240` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `241` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `242` | 6_branding_theme | P1 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `243` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `244` | 6_branding_theme | P1 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `245` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `246` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `247` | 6_branding_theme | P2 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `248` | 6_branding_theme | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `249` | 6_branding_theme | P2 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `250` | 6_branding_theme | P1 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P1（維持） |
| `251` | 6_branding_theme | P1 | vehicle-critical CAN signal（車輛關鍵 CAN 訊號） → `CAN` | P0 成立 | P1（維持） |
| `252` | 6_branding_theme | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `253` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `254` | 6_branding_theme | P0 | （無） | **無 P0 類別命中，亦非裝飾性** | **提案人工裁決** |
| `255` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `256` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `257` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `258` | 6_branding_theme | P0 | （無） | **無 P0 類別命中；命中裝飾性／個人化** | **提案 P3** |
| `259` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `260` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `261` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `262` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `Ignition On` | P0 成立 | P0 |
| `263` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
| `264` | 6_branding_theme | P0 | boot / recovery（開機與復原） → `startup` | P0 成立 | P0 |
