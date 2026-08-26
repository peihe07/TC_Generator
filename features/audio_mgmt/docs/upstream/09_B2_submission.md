# Audio Management — 上繳包 09：Batch B2 交付

- 日期：2026-08-26（rev 3 —— `<Vent off>` 出處更正為 CFTS019-4867782）
- 對應下放包：`docs/handoff/08_B2_final_anchors.md`（定案錨表，雙路必經）
- 執行層：Claude Code
- 依據裁定：R-AM1–R-AM16，特別是 R-AM15（雙路必經）、R-AM16（共錨允許）

---

## 一、交付摘要

| 項目 | 值 |
|---|---|
| 批次 | B2 |
| 葉數 | 50／50（Audio Arbitration 13 ＋ Focus and Ducking 18 ＋ Mute Requests 19） |
| TC 數 | 66 |
| Test Set 分佈 | Audio Arbitration 19，Focus and Ducking 22，Mute Requests 25 |
| Priority 分佈 | P0 24，P1 42 |
| 設計方法分佈 | 決策表 21，功能測試 17，狀態轉換 16，負向測試 9，情境 / 用例 2，邊界值分析 1 |
| 帶 PENDING 之 TC | 22 項次（DR-AM4 20、DR-AM6 1、DR-AM8 1） |
| 池外錨（R-AM2′） | 10 |
| 併列雙錨 | 1（SWE1_AMM_032，見 §四） |
| TC JSON | `generated/B2.json` |
| 交付簿（累積） | `generated/SWQT_AudioMgmt_B1-B2.xlsx` |
| 交付簿 SHA256 | `445b944d141c4d69b60676a285f93943b8b6a87fff9e4032c4d128154b492bd4` |
| 交付簿內容 | **136 列**＝B1 70 ＋ B2 66；tc_id `NR1L-AMM-001`–`136`，無重複、無缺號 |

**產出量：** 66 條／50 葉（1.32 條/葉），與 B1 之 70／50（1.40）同量級。
未刻意對齊 B1 之條數 —— B2 之葉以單一 shall 陳述居多，強拆會產生逐字相同之
括號下半而違 R-S4。拆為 2 條者限於條款本身帶分支者（見 §六）。

## 二、§9 自檢通過聲明

`scripts/selfcheck_b1.py --batch B2`，66 條全數通過。

**自檢於本批攔下執行層之錯誤，記錄留痕：** 初次生成時四條 TC（068／069／
078／079）之步驟 1 寫作 `Verify no …`，違 canon §5.1 步驟禁用動詞。
該四步之意圖為建立起始狀態，正確寫法為 `Confirm`（禁詞表所禁者為
`confirm whether`，裸 `confirm` 合法）。**於寫回前攔下並改正**，未進交付簿。
此檢查係上一輪（B1 交付後）方才補實作，本批即發揮作用。

## 三、Lint 報告

`scripts/lint_tcs.py --batch B2 --profile audio_mgmt` → **green**（十六項全實作）。

首輪跑出 **11 項違規**，全數為真，已全部修正：

| 違規 | 條數 | 處置 |
|---|---|---|
| 檢查 L：verbatim 上半逾 R-3 之 50 token 上限 | 11 項次（030／287／061／068／069／070／071 七葉） | 依 R-S4 摘句，全文以 specification_reference 指回 |

另修正一項 lint 未攔但為真之問題（見 §五.2）：Cabin EQ 值之 `$` 與訊號標記衝突。

Lint 之 note 全為 v3 (g) 與 PENDING 項，無其他。

## 四、逐案處置之落實（對應 08 包 §二）

| 葉 | 08 包裁定 | 交付落實 |
|---|---|---|
| 030 | 部分覆蓋，不寫動作集 | TC 僅驗「依既定優先權與使用者請求選擇來源」。duck／mute／reject／pause 未寫；reasoning 註明全文 0 命中、併入 DR-AM1 |
| 031／032 | 共錨 4866055（R-AM16），括號下半須各異 | 031 括號＝優先權取得與 interrupted 狀態；032 括號＝暫停至 INFO2 全部非作用。逐字不同 |
| 032 | 併列雙錨 | spec_reference 兩行：`CFTS019-4866054` ⏎ `CFTS019-4866055`（同文件內升冪，IN §10.7） |
| 061 | 掛 DR-AM6，嚴禁推測 CFTS020 | TC 僅驗 `$ICSPowerButton$` 抵達與進入靜音路徑；靜音邏輯掛 PENDING。**CFTS020 內容一字未寫** |
| 233 | 部分覆蓋，不寫 ducking level | TC 僅驗 signal source 混入全部輸出通道 |
| 309 | C→A，錨 4866484（池外） | 已採。TC 驗 CD 於 HFP 期間暫停並於通話結束後回復 |
| 076 | 維持 4866155，部分覆蓋 | TC 僅驗「靜音行為依設定之啟用」；Routing_Table 具體對應未寫，併入 DR-AM1。本列為 076b（SYS-RA-AMM-246），交付欄依 R-AM6 照抄 `SWE1_AMM_076` |
| 086 | 改錨 4866442 | 已採。TC 涵蓋 Entertainment／Information／Signal 三者 |

## 五、本批之技術判斷（供分析層複核）

### 五.1 三個參數，三種處置 —— 證據不同，非標準不一

| 參數 | 全文證據 | 處置 |
|---|---|---|
| `<Tdisp>` | `Max = 100 ms` | 實值入 TC（VSIM 四葉之回應時間） |
| `<Vent Nav Off>` | `= 9 steps`（4867783） | 實值入 TC（314／316） |
| `<vent off>` | **出現 1 次（即錨本身），無定義列** | **rev 2：−16 dB 入 TC（R-AM17）** |

`<vent off>` 未以 `<Vent Nav Off>` 之 9 steps 代入 —— 08 包 §三.5 明訂二者為
不同參數。與 A-AM04（`<Temp Ramp Down>`）之差異：後者出現 10 次且有
`<Tent Ramp Down>` 可資對照而具拼寫錯誤之判讀空間，本件僅出現一次，無此空間。

**rev 2（R-AM17）：** Pei 定 `<vent off>` = **−16 dB**，已回填 287、撤 DR-AM8。
287 之 ER 改為量測式（以起始位準為基準，Main Audio 較之低 16 dB），
自檢與 lint 重跑全綠，交付簿重寫並複驗計數。

**更正（rev 3）：上段之「該值不在 CFTS019 內」為執行層之誤，予以撤銷。**
錯因為大小寫敏感檢索 —— 只比對小寫 `<vent off>`（1 筆），未比對 `<Vent off>`
（8 筆）。定義列為 **CFTS019-4867782**：`<Vent off> = -16 dB`。
故該值 **spec-sourced**，R-AM17 降為採認紀錄，287 之 reasoning 已改引 4867782。
交付欄未變（前後摘要一致），工作簿未重寫。詳見 A-AM08 之更正段。

### 五.2 Cabin EQ 值之記法（259／260）

CFTS019 原文寫 `[$00]` / `[$FF]` / `[$DF]`。該寫法在本 feature 同時觸犯兩條：
方括號禁令（§11 檢查 F），且 `$` 為 §8.7.5 v3 之**訊號標記**，`"$00"` 會被
訊號解析誤讀為訊號 token。

交付採 **SWE.1 葉本身之寫法 `S00` / `SFF` / `SDF`**，加雙引號。此非改寫規格值，
而是在兩種記法皆存在於上游時取不與本案記法系統衝突者；且與 verbatim 上半
（葉原文即寫 `S00 / SFF`）一致。

### 五.3 訊號：本批全數不在 DBC

B2 涉及之 `$VSIMMuteReq$`、`$ENTMuted$`、`$VolumeINFO1$`、`$VolumeINFO2$`、
`$VolumeENT$`、`$ICSMuteButton$`、`$ICSPowerButton$`、`$ICSPresent$`
**全部查無**（兩本 DBC 共 2,260 個訊號；唯一查得者 `SOSCallType` 本批未用）。
一律依 R-13 (g) 保留 CFTS019 原文名，未以近似訊號代換，各條掛 DR-AM4。

`TLM_Status.Info` / `TLM_Mute_Setup.Req` / `TLM_Mute_Status.Info` 為內部訊號，
依 v3 (d) 保留來源名稱、不加 `$`。

**建議 DR-AM4 擴大範圍**：原記載為缺 `$HUModeStatus$` 與 `$VolumeENT$`，
實測缺漏為系統性 —— HU 側 CAN 定義整體不在供應之 DBC 內。

## 六、拆為 2 條者及其理由（分支覆蓋）

| 葉 | 分支 |
|---|---|
| 229／232／236／239 | 忽略 TA ／ 客戶已選則播放（`unless selected by the customer` 例外） |
| 259 | `S00` ／ `SFF`（同一 OR 之兩個列舉值，範圍檢查可能只擋其一） |
| 310 | HFP ／ 緊急通話（錨為 R1L-R 變體，含 E-Call/R-Call） |
| 004 | Information ／ Signal 兩類皆高於 Entertainment |
| 014 | ENT ／ INFO1 兩條通道 |
| 060 | 靜音 ／ 解除靜音（toggle 兩向；只驗一向則閂鎖式實作可通過） |
| 068／069 | 有 ENT 作用中則切換 ／ 無則忽略（if/else 兩支） |
| 070 | 儲存並靜音 ／ 解除後回復（回復才證明儲存值未被預設值取代） |
| 071 | 一般靜音可由音量變更解除 ／ **內部靜音不可**（例外分支） |
| 184 | 解除 ／ **另有靜音原因時不解除**（`if no other reasons` 之守衛） |
| 315 | 降至 step 0 則靜音 ／ **來源仍為播放中而非暫停**（`without PAUSE`，08 包 §三.1 指明之關鍵區別） |
| 317 | 增加 ／ 減少（`same adjustment` 涵蓋兩向） |

九條為負向測試 —— 上表中標粗者皆屬「正向通過亦不能證明」之分支。

## 七、寫回驗證

| 驗證項 | 結果 |
|---|---|
| zip 成員集 | 48／48 不變 |
| 受改成員 | 僅 `xl/worksheets/sheet6.xml` |
| `<dataValidation>` classic ／ x14 | 3 ／ 1，不變 |
| `<conditionalFormatting>` | 不變（**本母本計數為 0，該檢查仍為 vacuously true**） |
| 追溯性 | 66 列 req_id 逐列回讀比對，全符 |
| 完整性 | 葉集合前後一致 |
| 累積正確性 | 136 列 ＝ 70 ＋ 66；tc_id 001–136 無重複、無缺號 |

## 八、本批暴露之寫回缺陷（A-AM09，已修）

B2 為**首個非首批**，因而暴露兩個在單批交付下不可見之缺陷：

1. **`tc_id` 逐批重新起算。** `write_rows` 以批次內 offset 計序，B2 首次寫回
   得 `NR1L-AMM-001`–`066`，與 B1 已用之 001–070 全面碰撞。
   修正：新增 `next_tc_seq()`，自**簿內既有列**讀最大序號後續接
   —— 序號之權威為簿內資料，非批次之內部偏移。
2. **來源預設為母本。** `write_back.py` 原一律以 `paths.workbook` 為來源，
   B2 照跑會自第 10 列重寫並**靜默覆蓋 B1 之 70 列**。
   修正：新增 `--source`，交付簿改累積式。

兩者皆非 B1 交付之瑕疵（B1 為首批，兩條路徑當時均正確），但**若 B2 未經
逐列回讀驗證即出貨，B1 之 70 列將已遺失**。已登記 A-AM09。

## 九、未結 DR（七件未結，一件撤回）

| DR | 內容 | 狀態 | 卡批？ |
|---|---|---|---|
| DR-AM1 | SWE1↔CFTS 正式對照表缺失；另收 030 動作集、076 Routing_Table 之無錨部分 | 待送出 | 否 |
| DR-AM2 | SWE1_AMM_076 編號碰撞 | 待送出 | 否（076b 已交付，076a 落 B3） |
| DR-AM3 | Basic Report 遺漏圖表型物件（範圍已補 1.3.3.11 與導航 Fade-Out 段） | **已裁發** | 否 |
| DR-AM4 | DBC 缺 HU 側 CAN 定義（**建議擴大範圍，見 §五.3**） | 待送出 | 否 |
| DR-AM5 | `<Temp Ramp Down>` / `<Temt Ramp Down>` 未定義 | 待送出 | 否 |
| DR-AM6 | `{CFTS020}` 不在 `inputs/` | **Pei 裁發** | 否 |
| DR-AM7 | 24 個錨標 Atlantis Mid 之適用性 | **Pei 裁發** | 否 |
| ~~DR-AM8~~ | ~~`<vent off>` 未定義~~ **撤回（R-AM17 定 −16 dB）** | **撤回，未送出** | 否 |

## 十、待分析層裁定

0. **B2 收工條件已達成**（R-AM17 回填、DR-AM8 撤、自檢與 lint 重跑全綠、
   交付簿重寫並複驗計數：136 列、tc_id 001–136 無重複無缺號、
   dataValidation classic 3 ／ x14 1 不變）。
1. DR-AM4 之範圍是否依 §五.3 擴大為「HU 側 CAN 定義整體缺件」。
2. §五.2 之 `S00/SFF/SDF` 記法是否認可（涉及後續批次凡引用規格內
   `[$xx]` 型值者）。
3. B3 之下放。已知兩項須帶入：`SWE1_AMM_076` 之另一列（076a ＝
   SYS-RA-AMM-242）落於該批，依 R-AM6 交付欄同樣照抄；
   篩選上界依 R-AM12 為 **4867784**，不得沿用包 01 之 4867749。
