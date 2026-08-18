# G162 —— P0 分布與 §10.2 七類對照（R-P235）

> **本閘不改任何 `priority` 值**（R-P235 / §I）—— 只量測與對照，裁定於 34 包。

## 1. 全批分布（264 條）

| priority | 條 | 佔比 |
|---|---|---|
| P0 | **193** | 73.1% |
| P1 | **63** | 23.9% |
| P2 | **8** | 3.0% |

## 2. 逐 Test Set 之 P0 佔比

| Test Set | 條 | P0 | 佔比 |
|---|---|---|---|
| Branding and Theme | 34 | **26** | 76.5% |
| Power Down | 17 | **3** | 17.6% |
| Power State | 128 | **113** | 88.3% |
| Startup Display | 59 | **40** | 67.8% |
| Timeout Settings | 26 | **11** | 42.3% |

## 3. 抽樣（種子 `random.Random(33)`，率 ≥ 16.7%）

| Test Set | 母體 | 抽樣 | 率 |
|---|---|---|---|
| Branding and Theme | 26 | **5** | 19.2% |
| Power Down | 3 | **1** | 33.3% |
| Power State | 113 | **19** | 16.8% |
| Startup Display | 40 | **7** | 17.5% |
| Timeout Settings | 11 | **2** | 18.2% |
| **合計** | 193 | **34** | 17.6% |

## 4. 逐條對照 §10.2 七類

**可歸類 21 / 34；無法歸類或依據薄弱 13 / 34 = 38.2%**

| tc_id | Test Set | 測項 | §10.2 類別 | 依據 |
|---|---|---|---|---|
| `007` | Power Down | Load Shed limits volume and mutes TLM | audio output | Load Shed 限制音量並靜音 —— 直接為音訊輸出 |
| `033` | Timeout Settings | Case 1 with RemStartFail true: TLM stops and | vehicle-critical CAN signal | `STATUS_BH_BCM2.RemStActvSts` 觸發之電源轉換 |
| `038` | Timeout Settings | Case 3: call already ended at Timeout1 expir | boot/recovery | Timeout1 到期後轉入 Standby —— 電源狀態之復歸 |
| `053` | Power State | Remote Start Active reports Partial_Operatio | vehicle-critical CAN signal | `STATUS_BH_BCM2.RemStActvSts` 之回報 |
| `068` | Power State | CLIMATIC_PANEL.Radio_Btn0 press with no acti | boot/recovery | 關機鍵觸發之 Idle 轉換 |
| `083` | Power State | Logistic mode on passes the TLM to Logistic  | boot/recovery | Logistic mode 之電源狀態轉換 |
| `085` | Power State | Remote Start not active on leaving Ignition  | vehicle-critical CAN signal | `RemStActvSts` 轉換所致之旗標清除 |
| `086` | Power State | Front_Panel_OnOff.Req press in Timed with an | connection | 通話中之轉接 popup —— 其標的為通話之保持 |
| `088` | Power State | Declining the Front_Panel_OnOff.Req popup ke | **—** | **依據薄弱** —— 所驗為「拒絕 popup 後**維持** Timed」，既非通話之建立或中斷，亦非電源轉換；較近 §10.2 之 P1「key operational logic flow」 |
| `101` | Power State | Antitheft success with a zero timeout takes  | **—** | **無法歸類** —— Timeout1 自 PROXI 取值，為參數設定，不屬七類任一 |
| `105` | Power State | Timeout1 follows Switch_Off_Time when the se | **—** | **無法歸類** —— 同 `101`，參數取值 |
| `110` | Power State | Rear view camera images follow the enable si | **—** | **依據薄弱** —— 後視影像之顯示；§10.2 之 `audio output` 不含 video，七類無「影像輸出」 |
| `113` | Power State | Ignition Off from Partial Operation passes t | boot/recovery | Ignition Off → Standby 之電源轉換 |
| `115` | Power State | Antitheft success with auto switch on active | boot/recovery | 防盜成功後之開機流程（→ Full-Operation） |
| `116` | Power State | Antitheft success with auto switch on not ac | boot/recovery | 防盜成功後之開機流程（→ Idle） |
| `117` | Power State | Antitheft success with recall last and last  | boot/recovery | 同上，Recall_Last 分支 |
| `129` | Power State | Entering the TLM off with network off status | boot/recovery | 進入 TLM off 狀態之關機流程 |
| `133` | Power State | Front panel press in Sleep arms the antithef | boot/recovery | Sleep 下之喚醒流程（防盜啟動 ＋ Splash） |
| `135` | Power State | Climatic panel press in Sleep arms the antit | boot/recovery | 同 `133`，另一觸發鍵 |
| `138` | Power State | Rear view camera is provided while the antit | **—** | **依據薄弱** —— 後視影像之提供；同 `110`，七類無影像輸出 |
| `139` | Power State | Rear view camera is provided after an unsucc | **—** | **依據薄弱** —— 同 `138` |
| `154` | Startup Display | SDARS present without audio brand adds the S | **—** | **無法歸類** —— Sirius logo 之呈現；屬 §10.2 之 P3「cosmetic detail / low-impact customization」 |
| `171` | Startup Display | A ROV FOTA update at Body OFF brings the HU  | boot/recovery | FOTA 更新致 HU 轉入 Timed —— 電源狀態轉換 |
| `182` | Startup Display | A mode change cancels a start-up animation i | boot/recovery | 模式變更取消開機動畫並切換電源模式 |
| `184` | Startup Display | A mode change to TIMED MODE cancels a start- | boot/recovery | 同 `182` |
| `191` | Startup Display | The once a day setting plays the startup sou | **—** | **依據薄弱** —— 開機音效之伴隨播放；其為裝飾性音效，非 §10.2 之 `audio output`（音訊輸出功能） |
| `208` | Startup Display | The splash and disclaimer screens appear on  | boot/recovery | 開機序列之 splash 與免責畫面呈現 |
| `212` | Startup Display | An ongoing call temporarily skips the discla | connection | 通話中之畫面略過 —— 其前提為通話進行中 |
| `230` | Power State | The disclaimer bypassed for a call is shown  | connection | 來電所致之畫面延後補顯 |
| `237` | Branding and Theme | The Chrysler brand selects the Chrysler font | **—** | **無法歸類** —— 品牌字型之選用；屬 P3 cosmetic |
| `240` | Branding and Theme | The Chrysler brand selects the Chrysler App  | **—** | **無法歸類** —— 品牌 App icon 之選用；屬 P3 cosmetic |
| `241` | Branding and Theme | The Jeep brand selects the Jeep App icon | **—** | **無法歸類** —— 同 `240` |
| `257` | Branding and Theme | The day theme mode uses the Day theme | **—** | **無法歸類** —— 日間主題之採用；屬 P3 cosmetic |
| `259` | Branding and Theme | The season changes to Summer at the December | **—** | **無法歸類** —— 季節判定；不屬七類任一 |

## 5. 無法歸類者之 Test Set 分布

| Test Set | 無法歸類 / 抽樣 |
|---|---|
| Branding and Theme | **5** / 5 |
| Power Down | **0** / 1 |
| Power State | **6** / 19 |
| Startup Display | **2** / 7 |
| Timeout Settings | **0** / 2 |
