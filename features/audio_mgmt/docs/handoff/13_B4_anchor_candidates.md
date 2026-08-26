# Audio Management — 下放包 13：Batch B4 候選錨表（R-AM15 第一路，綠色通道首批）

- 日期：2026-08-26
- 批次：B4 = Volume Control 後 13（含自 B3 遞延之 SWE1_AMM_194）＋ Audio Sources 37 = 50 葉
- 通道：R-AM20 綠色通道生效。**池內葉**：兩路一致即寫入，不再逐批裁定；
  **池外葉**（本批已知 5：266、306、307、308、311，C 級若查得池外者併入）：
  照常雙路對帳＋裁定，不入免審範圍。
- **葉集差集核對（12 包 §七 防線，首跑）**：已交付∪B4 = 199 唯一 SWE ID；
  差集 118 = Audio Processing 34 ＋ Tones and Alerts 32 ＋ Power and
  Persistence 25 ＋ Surround and Fade 24 ＋ Logistic Mode 3，恰為 B5–B7
  三站之集，**無葉靜默消失；SWE1_AMM_194 已在 B4 列**。

---

## 一、A 級（30 葉）：已定向查證、附原文佐證

### Volume Control 後 13（A 級 8）

| 葉 | 錨 | 池 | 佐證 |
|---|---|---|---|
| SWE1_AMM_194 | CFTS019-4866722 | ✓ | TBM Unmute 序列：`Send $VolumeENT$ = [Recalled level]` |
| SWE1_AMM_196 | CFTS019-4866724 | ✓ | 同序列：`Send $VolumeINFO1$ = [Recalled level]` |
| SWE1_AMM_197 | CFTS019-4866725 | ✓ | 同序列：`Send $VolumeINFO2$ = [Recalled level]` |
| SWE1_AMM_220 | CFTS019-4866891 | ✓ | NAV 作用中調音量 → 顯示 Volume Level Adjustment 畫面並示 NAV 音量 |
| SWE1_AMM_262 | CFTS019-4867582 | ✓ | 接受之 Cabin EQ 對應二喇叭系統 → 之後續處置（Fade 停用） |
| SWE1_AMM_272 | CFTS019-4867751 | ✓ | `<ENT Key Vol> = step 15`（變數定義錨，同 B1 275–278 型；行為物件由第二路續查，見 §四.1） |
| SWE1_AMM_273 | CFTS019-4867752 | ✓ | `<HFP Vol Th max> = 38 step`（同上） |
| SWE1_AMM_274 | CFTS019-4867753 | ✓ | `<HFP Vol Th min> = 15 step`（同上；LATAM 變體 4867754=19 屬 B6/B7 之 299，勿混） |

### Audio Sources（A 級 22）

| 葉 | 錨 | 池 | 佐證 |
|---|---|---|---|
| SWE1_AMM_001 | CFTS019-4865912 | ✓ | Entertainment 來源以立體聲處理 |
| SWE1_AMM_005 | CFTS019-4865917 | ✓ | Entertainment 來源分類清單 |
| SWE1_AMM_006 | CFTS019-4865918 | ✓ | TA/PTY31 視為 entertainment 來源 |
| SWE1_AMM_007 | CFTS019-4865928 | ✓ | Information 來源以 mono 處理並依來源指派 INFO1／INFO2 路徑 |
| SWE1_AMM_010 | CFTS019-4865936 | ✓ | INFO2 路徑指派清單（R-Call/E-Call、HFP Audio…） |
| SWE1_AMM_108 | CFTS019-4866289 | ✓ | 音訊通道指派於個別來源振幅調整後執行 |
| SWE1_AMM_148 | CFTS019-4866501 | ✓ | Info1 啟用分支：`$INFO1Active$ = [active]` |
| SWE1_AMM_149 | CFTS019-4866502 | ✓ | 同分支：`$INFO1Type$ = [依 Information Source Handling Table「Audio Type」欄]` |
| SWE1_AMM_151 | CFTS019-4866506 | ✓ | Info2 啟用分支：`$INFO2Active$ = [active]` |
| SWE1_AMM_152 | CFTS019-4866507 | ✓ | 同分支：`$INFO2Type$ = [依表]` |
| SWE1_AMM_162 | CFTS019-4866532 | ✓ | Info1 停用分支：`$INFO1Active$ = [inactive]` |
| SWE1_AMM_163 | CFTS019-4866533 | ✓ | 同分支：`$INFO1Type$ = [NONE]` |
| SWE1_AMM_164 | CFTS019-4866535 | ✓ | Info2 停用分支：`$INFO2Active$ = [inactive]` |
| SWE1_AMM_165 | CFTS019-4866536 | ✓ | 同分支：`$INFO2Type$ = [NONE]` |
| SWE1_AMM_175 | CFTS019-4866659 | ✓ | 前/後喇叭啟用前儲存現行音訊模式設定（volume、tone、Fade/Balance） |
| SWE1_AMM_176 | CFTS019-4866662 | ✓ | 之後 recall last audio settings |
| SWE1_AMM_210 | CFTS019-4866872 | ✓ | 無來源播放 → `$HUModeStatus$`="HU_Off"、INFO1/2 Active="Inactive"、Type="None" |
| SWE1_AMM_214 | CFTS019-4866876 | ✓ | HFP 啟用：`$INFO2Active$`="Active"、`$INFO2Type$`="Phone_Aud"、recall 音量經 `$VolumeINFO2$` |
| SWE1_AMM_217 | CFTS019-4866881 | ✓ | HFP 停用：儲存 `$VolumeINFO2$`、`$INFO2Active$`="Not_Active" |
| SWE1_AMM_256 | CFTS019-4867564 | ✓ | `$DriverSide$`=[LHD] → **HU** 將駕駛側音訊導向左側 |
| SWE1_AMM_257 | CFTS019-4867566 | ✓ | `$DriverSide$`=[RHD] → **HU** 導向右側（候選演算法原給 4867567 為 **AMP** 側，已排除） |
| SWE1_AMM_311 | CFTS019-4866914 | ✗ | Phone 作用中偵得 NAV 事件 → NAV 於駕駛側啟用 |

## 二、B 級（15 葉）：候選明確，待第二路佐證

| 葉 | 候選錨 | 池 | 備註 |
|---|---|---|---|
| SWE1_AMM_264 | 4867598 | ✓ | Surround HMI 啟用 |
| SWE1_AMM_266 | 4867604 | ✗ | Surround 停用 |
| SWE1_AMM_306 | 4866207 | ✗ | Cabin audio 作用中之預設 alert 音量 |
| SWE1_AMM_307 | 4866208 | ✗ | Cabin audio 非作用之預設 alert 音量 |
| SWE1_AMM_308 | 4866242 | ✗ | SCV 停用處置 |
| SWE1_AMM_002 | 4867570 | ✓ | Entertainment 通道路由 |
| SWE1_AMM_003 | 4865915 | ✓ | Entertainment 播放狀態處理 |
| SWE1_AMM_009 | 4865932 | ✓ | INFO1 路徑指派 |
| SWE1_AMM_013 | 4865967 | ✓ | Confirmation tone 前通道路由 |
| SWE1_AMM_122 | 4865895 | ✓ | Audio Routing Table 遵循 |
| SWE1_AMM_202 | 4866843 | ✓ | 啟用後來源狀態更新 |
| SWE1_AMM_204 | 4866845 | ✓ | 停用後來源狀態更新 |
| SWE1_AMM_207 | 4866854 | ✓ | ENT 轉換後 `$HUModeStatus$` 更新 |
| SWE1_AMM_228 | 4866904 | ✓ | NAV 提示期間之 HFP 路由 |
| SWE1_AMM_263 | 4867584 | ✓ | 二喇叭系統之後喇叭靜音 |

## 三、C 級（5 葉）：未決，第二路查證

| 葉 | 問題 |
|---|---|
| SWE1_AMM_020 | Alert Front Channel Routing——候選演算法給 4866916（Signal 混流），語意不符，**不採**。請於 1.3.1.5／1.3.2.6 Alert 區段續查 |
| SWE1_AMM_024 | External Amplifier Audio Output Mapping——疑與 108 共錨 4866289（R-AM16 型），或另有外部擴大機專屬物件；請判別 |
| SWE1_AMM_145 | Applied Channel Ramp-Down——候選 4866497 未經佐證；**警示：4866494 已為 B1 之 144 錨**，取之須依 R-AM16 論證，不得默默重用 |
| SWE1_AMM_146 | Remaining Channel Volume Adjustment——同上警示；疑落 HALF／SDW 通道子集區（4866620–4866662） |
| SWE1_AMM_155 | Information Channel Ramp-Up——候選 4866512 已為 B1 之 154 錨；154 為音量斜坡、155 為通道面向，是否共錨或另有通道句（4866512 尾段「applied to the channels indicated」之獨立物件）請判別 |

## 四、撰寫與對帳注意

1. **272/273/274 之錨為變數定義物件**（B1 275–278 先例）。第二路請續查
   sleep-resume 章是否另有行為物件（4867742–4867749 實測為 VirtualConcertHall
   ／ANC，非此題）；查得則升為行為錨＋變數錨併列，查無則維持現案。
2. **啟停分支四組**（148/149、151/152、162/163、164/165）為序列子句錨，
   同分支之兩葉 TC 宜合併觀察於同一序列 TC 或以括號下半嚴格區分
   （Active 訊號 vs Type 訊號），依 §8.2.2 判準決定拆併。
3. **214/217 與 B2/B3 之 HFP 相關列**（309、273/274）情境相鄰：
   214/217 是啟停訊號序列、309 是暫停行為、273/274 是音量門檻，
   tc_title 括號下半勿互相撞題。
4. **256/257 為 §7 列舉配對**（LHD／RHD 成對）；另有 4867568（無效值→
   {CIP Default Settings} 預設）**無對應 SWE 葉**，屬負向缺口，
   於 reasoning 揭露，不擅自擴編。
5. **210 的三訊號複合 ER**：`$HUModeStatus$`＋INFO1/2 四訊號同一觸發，
   依 §5.7 一 TC 多 ER 行，勿拆。
6. 訊號、`[$xx]` 記法、大小寫不敏感複查——同 12 包 §四.6–8，不重抄。

## 五、池外與裁定路徑

已知池外 5（311、266、306、307、308）＋ C 級查得之池外者。
依 R-AM20 除外條款：此等葉之定案仍須 Pei 裁；其餘池內葉兩路一致即寫入。
第二路對帳報告請分列「池內一致（逕寫）／池內不一致（對帳）／池外（待裁）」三段。

## 六、未結 DR

八件同 12 包 §八，無新增。
