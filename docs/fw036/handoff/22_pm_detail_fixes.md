# PM 詳細檢查：需修改項總清單（2026-08-21，Pei 三問之答）

檢查對象：交付路徑現行版（sha 611fab59…，即 pm_19 寫回後之重序列化版）。

## 修改一：行文主詞統一為 HU（448 行）——依 SWC 權威自裁

**TLM／LTM 判定（CFTS009 查證）**：
- **LTM = 具體 ECU**（Atlantis 之 radio 模組；Glossary 元件表
  `RRM, LTM, ETM, ICS, AMP…` 有 LTM 無 TLM；「LTM High Radio」）
- **TLM = 規格行文之行為主體**（telematic 系統泛稱 = 被測 HU）
- DOORS 規則：需求適用於特定元件時 pre-pend 元件縮寫 →
  `LTM_OperationalModeSts.Info` 之 `LTM_` 為**元件前綴**，
  非訊號名一部分；訊號本體 `OperationalModeSts`（A-PM10 就此結案）

036 現況 TLM 448 行／HU 321 行混用；**SWC 全書僅用 HU**。
依 Pei 既有裁定「都照 SWC」：

```
R-16 行文主詞
作者欄位之被測物主詞一律 HU：`The TLM is in…`→`The HU is in…`、
`TLM screen`→`HU screen`、`TLM audio output`→`HU audio output`。
例外：verbatim 上半不動；規格訊號／變數名（TLM_Display.GUI 等）不動；
LTM 之 13 行為 radio 型號用法，正確，不動。
```

## 修改二：拆 TC —— 真 A 型僅 3 列（初篩 25 列，複核清除 22 列誤判）

逐列複核後之誤判類型（**不拆**）：
- 同一訊號兩值連發 = 一個 transition（47／55／57／59／66／67／72／
  79／82／98／106／132／133）
- 兩訊號同送 = 一個組合條件（Load Shed 之 187／191／192／196）
- 建立＋解除 = 一個情境流程（179／180／181／293）
- 兩 request 併發 = 該列情境本身（34；35／36 已是單項分支）

**真 A 型（不同 trigger 各一 TC，§8.3）**：

| 列 | 現況 | 拆為 |
|---|---|---|
| 11 | 4 個 ignition 值逐一送、逐一驗 | **4 TC**（= 5／6／7／8 各一） |
| 12 | SDCARD→BT→phone call 三源切換 | **3 TC** |
| 23 | 同 12（Timed 狀態） | **3 TC** |

3 列 → 10 列，淨增 7 列。拆後每 TC 單一 trigger、2 步、ER 2 點。
**拆列屬 Pei**；核可後分析層出逐列內容，執行層寫入。
B 型 30 列（單 trigger 多面向，如 row 24 Standby 七面向）依
§5.7 維持一 TC，**不拆**。

## 修改三：內部變數之觀察途徑（130 行）—— 分類處置

「執行步驟不明確」之根因：`Read <變數> and check…` 未指明**在哪讀**。

**(a) 設定類 → 改寫為 HMI 設定選單讀取（有依據，約 35 行）**
`SwitchOff_Timeout_Setting.Req`（16）／`Auto_SwitchOn_Setting.Req`
（源自 Customer setting screens，CFTS009 引用 VF665）：
```
前：2. Read SwitchOff_Timeout_Setting.Req and check that it is 00 min
後：2. Open the switch-off timeout entry in the HU settings menu and
    check that it is set to 00 min
```

**(b) 狀態類 → 開 DR-PW23，途徑到位後補寫（約 95 行）**
`Antitheft_Activation.Req`(24)／`Timeout1`(19)／`VPLastStatus`(17)／
`RemStartFail`(11)／`Phone_Call.Info` 等：規格未載讀取途徑
（Eng Mode 畫面？診斷？log？）。**不推定**（路線 c）。
現行寫法（保留變數名＋應觀察值）維持；DR-PW23 開列六變數
問上游觀察途徑，回覆後統一補 `via <途徑>` 前綴。
**不阻塞交付** —— 變數名與判準已明確，缺者僅為讀取管道。

**(c) 螢幕類（102 行）不改** —— `Read the HU screen and check that
the splash screen is shown` 已可執行（目視）。

## 執行順序

1. 修改一（448 行，機械替換）＋ 修改三(a)（35 行）→ 一包下放
2. 修改二待 Pei 核可拆分方案 → 分析層出 10 列內容 → 併入同包或次包
3. DR-PW23 登記即刻做；(b) 之補寫俟上游回覆
