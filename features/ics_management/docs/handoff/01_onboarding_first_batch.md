# 下放包 01 — ICS Management 建檔與首批 TC（2026-08-29）

Pei 已准：①命名（R-ICS1）②DR-ICS1~9 即發 ③首波動工面 ④骨架落檔。
分析層已落：`framework.md`、`DATA_REQUESTS.md`、`ANOMALIES.md`、`RULINGS.md`（R-ICS1~4）。

## 一、執行層任務

1. **骨架補齊**：比照 `features/bed_lowering/` 增 `feature.yaml`、`batches/`、
   `output/`、`workbook/`、`docs/upstream/`。`inputs/` 已建，三份來源檔
   （SWRA xlsx、SYSAD、CFTS022，皆偽 docx／UTF-8 文字）由 Pei 置入或自
   專案掛載複製。
2. **首批 TC 起草**（見二），輸出至 `batches/b01/`，依 IN §10 十鍵 JSON。
3. **上繳包**：`docs/upstream/` 例行格式，**必附未結 DR 清單（DR-ICS1~9 全開）**。

## 二、首批 TC 計畫（6 條，僅限已解鎖面）

TC ID：`NR1L-ICS-{NNN}`，生成器編號。Test Group = `ICS`。English only（IN §1，新 feature 不援引雙語例外）。

### Stuck Button（RD: SWE-ICS-010）— 3 條
| # | 驗證點 | 錨 | Design Method |
|---|---|---|---|
| S1 | 按鍵連續按壓 >120 s → DTC set + not-pressed 值送出 | CFTS022-4914956 | Fault Injection |
| S2 | 故障維持：not-pressed 週期送出，至 stuck 條件清除（de-bounced not pressed）後 DTC 清除 | CFTS022-4914957 | Fault Injection |
| S3 | 邊界負向：按壓未逾 120 s 釋放 → 無 DTC、按鍵功能正常 | CFTS022-4914956 | Boundary Value Analysis |

S1/S2 為同一 sub-id 下獨立 partial failure，分列（IN §8.2.2），皆 trace SWE-ICS-010。
代表按鍵取 ICS "Mute"（測試實作選擇，reasoning 註明）。120 s 依 R-ICS3。

### Volume Control（RD: SWE-ICS-001, 002）— 3 條
| # | 驗證點 | 上半來源 | Design Method |
|---|---|---|---|
| V1 | Knob 1 順時針每格 → 音量 +1 | CFTS022-4914975（R-ICS4） | Functional Based |
| V2 | Knob 1 逆時針每格 → 音量 −1 | CFTS022-4914976（R-ICS4） | Functional Based |
| V3 | KNOB1_VAL 值對應：連轉 n 格 → 音量變化 n 階（HMI 觀察 Volume popup） | SWRA SWE-ICS-002 Description verbatim | Functional Based |

- V1/V2 trace SWE-ICS-001（方向軸 sibling）；V3 trace SWE-ICS-002。
- Pre-Condition 引 4914972 之啟用條件（HU Audio Mode ON）。
- Volume popup 觀察面錨 4914974。CFTS019 細節一律 `PENDING: DR-ICS4 <item>`。
- 適用域依 R-ICS2（{ICS, LTM} 暫定）；DR-ICS9 收窄時 V 組回收。

### 通用格式規制
- 訊號欄無 DBC：`PENDING: DR-ICS8 <signal>`，不得留空／NA、不得造 MESSAGE 名（IN §8.4.1、R-13 精神）。
- 無尾句號；UI 標籤 `"..."`；ER 無情態動詞；test_item 括號下半必有且 sibling 不重複。
- Priority 依 `TEST_CASE_PRIORITY.md` 自判 P0–P3，不抄 SWRA High/Medium（A-ICS6）。

## 三、Pilot TC（S1 範式，格式基準）

```
tc_title: Stuck button held over 120 s

test_item:
If the button is continuously in the pressed state for longer than 120 seconds, the HU shall set the stuck button DTC and send the "not pressed" value for the stuck button.
(Stuck button held over 120 s: DTC set and not-pressed substitution)

pre_conditions:
1. The A&T System has exited SLEEP MODE
2. A diagnostic tool is connected to the vehicle

input_test_data:
NA

test_procedure:
1. Press and hold the ICS "Mute" button
2. Keep the button pressed for more than 120 seconds
3. Read the DTC list on the diagnostic tool and check that the stuck button DTC is set
4. Read the stuck button signal on the CAN trace and check that the "not pressed" value is sent (signal name PENDING: DR-ICS8 <ICSMuteButton CAN signal>)

expected_result:
1. The "Mute" button enters and remains in the pressed state
2. The button remains in the pressed state for more than 120 seconds
3. The stuck button DTC is set
4. The "not pressed" value is periodically sent for the stuck button

specification_reference:
CFTS022-4914956

design_method: Fault Injection
priority: P1
split_flag: false
split_reason: ""
```

reasoning（範式）：驗證目標為 stuck button 逾時保護（DTC 置位與 not-pressed
代送）。關鍵條件為 A&T 離開 SLEEP MODE 後之持續按壓逾 120 s（R-ICS3）。
同一觸發之二後果（DTC、not-pressed）併一 TC 多行 ER（IN §5.7）；故障維持
與清除屬獨立 partial failure，另列 S2（IN §8.2.2）。代表按鍵取 "Mute" 為
測試實作選擇，非規格限定。

## 四、回報

批次完成後回報：TC JSON 路徑、自檢（IN §9）逐項結果、PENDING 佔位清單。
分析層審後出下放包 02。
