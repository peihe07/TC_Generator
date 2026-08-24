# PM 詳細修改清單（Pei 三項覆核意見之逐列處置，2026-08-21）

基底：現行交付版（283 列，四欄已改寫）。四區。

## 區一、TLM／LTM 判定與行文統一 [DEFAULT]

**判定（CFTS009 實查）**：
- `LTM` = 具體 ECU（Atlantis 之 radio 模組；Glossary 元件表
  `RRM, LTM, ETM, ICS, AMP…`；「LTM High Radio」）
- `TLM` = 規格行文之行為主體（telematic 系統泛稱 = 被測 HU）；
  Glossary 無 TLM
- `LTM_OperationalModeSts.Info` 之 `LTM_` 為 DOORS 元件前綴
  （「需求適用於特定元件時 pre-pend 元件縮寫」），非訊號名一部分；
  訊號本體 `OperationalModeSts`。A-PM10 之 RRM／LTM 疑義據此結案：
  同一訊號，不同元件段落各自冠名

**修改 [DEFAULT-1]**：行文主詞統一為 **HU**（SWC 語料 286 列全用 HU）。
- `The TLM is in <X> state` → `The HU is in <X> state`
- `TLM screen`→`HU screen`；`TLM display`→`HU display`；
  `TLM audio output`→`HU audio output`；`TLM menu`→`HU menu`；
  `the TLM Power button`→`the HU Power button`
- **不改**：verbatim 上半；規格訊號／變數名（`TLM_Display.GUI`）；
  `PowerSts_Telematic` 一類 DBC 名
- 影響：proc／er／pre 約 448 行

**LTM 之 13 行全數用法正確**（bench 配置之 radio 型號），不動：
rows 53、54、91、121、157、158、159、160、163、164、167、168、169

## 區二、A 型拆分（多 trigger，§8.3）—— 7 列 → 19 TC，淨增 12 列

判準：每個驅動步驟後**各自有驗證步驟** = 獨立 trigger。
（同一訊號 from→to 連發後單一驗證 = transition，不拆：rows 47、55、
57、59、72、157–159、187–196 之雙訊號組合條件亦不拆）

| 列 | 現況 | 拆為 | 拆分軸 |
|---|---|---|---|
| 11 | 4 個 ignition 條件逐一送、逐一驗 Full_Operation | **4 TC**（=5／6／7／8 各一） | trigger_state |
| 12 | SDCARD／BT streaming／phone call 三源逐一切換驗證 | **3 TC** | input_data（source） |
| 23 | 同 12（Timed 狀態） | **3 TC** | 同上 |
| 16 | user setting 拒絕／其他 HMI 拒絕／Power button 接受 | **3 TC** | 操作類別＋正反 |
| 19 | 不改變狀態之互動拒絕／改變狀態之互動接受 | **2 TC** | 正反配對（§7） |
| 46 | 同 19（Partial_Operation） | **2 TC** | 同上 |
| 34 | audio＋video 並存請求 | **不拆** —— 35／36 已各驗單獨 case，34 即「並存」組合情境本身 | — |

拆分後 TC ID 依序遞補、B 欄 Requirement ID 沿用母列（§8.2.2 多 TC
同 sub-id）。**拆列屬 Pei —— 本區為方案，經核可後出下放包。**

## 區三、步驟不明確之根治 —— 內部變數觀察途徑（~130 行）

已明確：135 行 `Read the signal $…$`；102 行螢幕類（可目視）。
**不明確者為內部變數，分三類處置**：

**(a) HMI 設定類 → 從 HU menu 讀（語料先例 row 165）[DEFAULT-2]**
- `SwitchOff_Timeout_Setting.Req`（16 行）→
  `Open the timeout setting entry in the HU menu and read the SwitchOff Timeout value`
- `Auto_SwitchOn_Setting.Req`（34 行中屬讀取者）→ 同式（Auto Switch-On entry）

**(b) 已有 CAN 對應之狀態 → 前批已改，無殘留**

**(c) 純內部旗標／記憶體值 → 無已知觀察途徑，開 DR**
- `VPLastStatus`（17）、`RemStartFail`（11）、
  `Antitheft_Activation.Req`（24）、`Antitheft_Result.Info`、
  `Timeout1` 讀值（19）、`AMP/ICS/DTV functionality` 判定法（26）
- **開 DR-PW23**（High）：請上游／測試環境提供上述變數之觀察途徑
  （Eng Mode 畫面？診斷服務？log？）。**取得前維持現行寫法**，
  於 Remarks 標 `observation path pending DR-PW23`（不入 proc，
  避免 PENDING 阻斷）

## 區四、B 型 30 列（單 trigger 多面向）—— 待 Pei 勾選

canon §5.7 現行寫法合規（同一 trigger 之多後果屬一 TC）。
若改採「每面向一 TC」，此 30 列將增至約 170 TC：
rows 10、17、21、24、26、28、29、30、32、39、45、97、102、109、
124–127、157–159、162、170、188、189、190、194、197、204、285
**[待 Pei] 拆／不拆一句話**；不拆則此區結案。

## 執行順序

1. 區一（448 行機械替換）＋ 區三(a)（50 行）＝ 下放包 23，可即出
2. 區二經你核可 → 下放包 24（拆列）
3. 區三(c) DR-PW23 登記隨包 23
4. 區四待你一句話
