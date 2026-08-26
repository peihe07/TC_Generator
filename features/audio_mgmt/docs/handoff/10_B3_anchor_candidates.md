# Audio Management — 下放包 10：Batch B3 候選錨表（R-AM15 第一路）

- 日期：2026-08-26
- 批次：B3 = Mute Requests 後 13 ＋ Volume Control 前 37 = 50 葉（包 02 §三）
- **本包非定案。** 依 R-AM15 雙路必經，B/C 級須經執行層第二路獨立佐證。
- 第一路語料：**CFTS019 全文 PDF 之 1,730 個屬性物件**（非 Basic Report）。
  第二路請取不同語料或不同判讀路徑，以維持獨立性。

---

## 一、A 級（26 葉）：已定向查證、附原文佐證

執行層仍須複核，重點見 §四之區辨提示。

### Mute Requests 後 13

| 葉 | 錨 | 池 | 佐證 |
|---|---|---|---|
| SWE1_AMM_185 | CFTS019-4866696 | ✓ | `$VSIMMuteReq$` Mute→Unmute 且無其他靜音原因 → 解除 **Information 1**，`$VolumeINFO1$` = 靜音前回復值，於 `<Tdisp>` 內 |
| SWE1_AMM_186 | CFTS019-4866697 | ✓ | 同上，**Information 2**，`$VolumeINFO2$` |
| SWE1_AMM_187 | CFTS019-4866698 | ✓ | 同上，**免持麥克風**（if equipped）並更新 HMI |
| SWE1_AMM_191 | CFTS019-4866717 | ✓ | TBM 靜音序列中之 `Send $ENTMuted$ =` |
| SWE1_AMM_192 | CFTS019-4866718 | ✓ | 作用中 INFO1 優先權低於 TBM Mute → 送 `$VolumeINFO1$` |
| SWE1_AMM_193 | CFTS019-4866719 | ✓ | 同上，INFO2 → `$VolumeINFO2$` |
| SWE1_AMM_195 | CFTS019-4866727 | ✓ | TBM 解除分支「ELSE HU shall unmute …」 |
| SWE1_AMM_288 | CFTS019-4866823 | ✗ | `$ShiftLeverPosition$` = R → 儲存現行 ENT 音量、靜音 ENT |
| SWE1_AMM_289 | CFTS019-4866824 | ✗ | `$ShiftLeverPosition$` = R → 忽略任何 VR 請求之發起 |
| SWE1_AMM_290 | CFTS019-4866825 | ✗ | `$ShiftLeverPosition$` ≠ R → 解除靜音至回復音量 |
| SWE1_AMM_291 | CFTS019-4866826 | ✗ | 離開 R 後 VR 請求恢復受理（**須第二路確認 OID**，見 §三.1） |
| SWE1_AMM_295 | CFTS019-4867710 | ✗ | `$Reverse_Mute_Enable$` = Disable → 停用 Reverse Mute 全部行為 |
| SWE1_AMM_296 | CFTS019-4867712 | ✗ | `$Reverse_Mute_Enable$` 未存在或未燒錄 → 停用全部行為 |

### Volume Control 前 37（A 級部分）

| 葉 | 錨 | 池 | 佐證 |
|---|---|---|---|
| SWE1_AMM_044 | CFTS019-4866082 | ✓ | 使用者調整音調控制 → 於 `<Tdisp>` 內更新 Equalizer HMI |
| SWE1_AMM_051 | CFTS019-4866099 | ✓ | HU 應為 ENT／INFO1／INFO2 各提供客戶控制項 |
| SWE1_AMM_053 | CFTS019-4866107 | ✓ | 使用者音量調整套用於最高優先權之作用中來源 |
| SWE1_AMM_063 | CFTS019-4866126 | ✓ | `TLM_Status.Info` == Full-Operation OR Timed → ENT 音量旋鈕 |
| SWE1_AMM_064 | CFTS019-4866127 | ✓ | 亦可經 `TLM_Vol_UP/DOWN_Status.Info` 設定 ENT 音量 |
| SWE1_AMM_067 | CFTS019-4866130 | ✓ | 音量設至最小 → 不中斷現行媒體，送 `$VolumeENT$` = 最小值 |
| SWE1_AMM_075 | CFTS019-4866150 | ✓ | `TLM_Status.Info` == Full-Operation OR Timed OR Idle → Information 音量旋鈕 |
| SWE1_AMM_077 | CFTS019-4866156 | ✓ | Information 音量設至最小 → 送 `$VolumeINFO1/2$` = 最小值 |
| SWE1_AMM_081 | CFTS019-4866212 | ✓ | SCV 預設 = OFF（NAFTA 市場） |
| SWE1_AMM_082 | CFTS019-4866213 | ✓ | SCV 預設 = level 1（其他市場）。**與 081 為互補對** |
| SWE1_AMM_083 | CFTS019-4866214 | ✓ | SCV 於電話、VR 等期間不得停用 |
| SWE1_AMM_084 | CFTS019-4866215 | ✓ | 使用者經 HU HMI 自支援清單選取 SCV 設定 |
| SWE1_AMM_085 | CFTS019-4866216 | ✓ | 選取新 SCV 等級 → 送 `$VolumeSCV$` |
| SWE1_AMM_089 | CFTS019-4866232 | ✓ | `SVC_Setup.Req` == "Disable" → 停用並設 `$VolumeSCV$` |
| SWE1_AMM_090 | CFTS019-4866233 | ✓ | `SVC_Setup.Req` <> "Disable" → 啟用並送 `$VolumeSCV$` |
| SWE1_AMM_073 | CFTS019-4866148 | ✓ | HU 經 `$VolumeINFO1$` 於 CAN 傳送 INFO1 音量 |
| SWE1_AMM_074 | CFTS019-4866149 | ✓ | 同上，INFO2 → `$VolumeINFO2$` |
| SWE1_AMM_150 | CFTS019-4866114 | ✓ | INFO1 音量控制之使用者調整經 `$VolumeINFO1$` 傳達 |
| SWE1_AMM_153 | CFTS019-4866115 | ✓ | 同上，INFO2 → `$VolumeINFO2$` |
| SWE1_AMM_054 | CFTS019-4866113 | ✓ | ENT 音量控制之使用者調整經 `$VolumeENT$` 傳達 |
| SWE1_AMM_141 | CFTS019-4866490 | ✓ | HU 應儲存現行顯示設定。**與 4866467 同文異錨**，見 §四.2 |
| SWE1_AMM_158 | CFTS019-4866527 | ✓ | HU 應儲存現行音量等級 |
| SWE1_AMM_190 | CFTS019-4866716 | ✓ | TBM 靜音序列中之 `Send $VolumeENT$ =` |

---

## 二、B 級（14 葉）：候選明確但未經第二路佐證

| 葉 | 候選錨 | 池 | 備註 |
|---|---|---|---|
| SWE1_AMM_055 | CFTS019-4866503 | ✓ | INFO1 音量值列；與 4866148 之分工待第二路確認 |
| SWE1_AMM_056 | CFTS019-4866508 | ✓ | 同上，INFO2 |
| SWE1_AMM_065 | CFTS019-4866113 | ✓ | 與 054 疑共錨（R-AM16 型）；若共錨須括號下半各異 |
| SWE1_AMM_072 | CFTS019-4866152 ⏎ CFTS019-4866153 | ✓ | 併列雙錨候選（INFO1／INFO2 各一） |
| SWE1_AMM_088 | CFTS019-4866309 | ✓ | Full-Operation／Timed 下之 SCV 啟停 |
| SWE1_AMM_091 | CFTS019-4866215 | ✓ | 與 084 疑共錨 |
| SWE1_AMM_114 | CFTS019-4866299 | ✓ | Fade/Balance HMI 更新；**4866299 與 4866308 同文異錨**，見 §四.3 |
| SWE1_AMM_119 | CFTS019-4866308 | ✓ | 同上（分派待第二路） |
| SWE1_AMM_147 | CFTS019-4866526 | ✓ | Information 停用序列；音量回復之落點待確認 |
| SWE1_AMM_183 | CFTS019-4866693 | ✓ | `$VSIMMuteReq$` = Mute → 顯示 HMI 指示 |
| SWE1_AMM_050 | CFTS019-4866112 | ✓ | **前提／外部參照句**（指向 {Radio Performance Standard}），部分覆蓋，見 §三.2 |
| SWE1_AMM_087 | CFTS019-4866221 | ✓ | **前提／外部參照句**（HU HMI Spec ＋ Routing_Table），部分覆蓋，見 §三.3 |
| SWE1_AMM_026 | — | — | 見 §三.4，C 級 |
| SWE1_AMM_076 | — | — | 見 §三.5，C 級 |

（上表末二列為 C 級，列此僅為清單完整；正式歸屬見 §三。）

---

## 三、C 級與部分覆蓋（需裁定）

### 三.1 SWE1_AMM_291 — OID 待第二路確認
288/289/290 分別對上 4866823/4866824/4866825，連續且精確。291（離開 R 後
VR 請求恢復）依序列推應為 **4866826**，但第一路未直接讀到該物件本文。
**處置建議**：第二路確認 4866826 之本文；相符則 A 級，否則 C 級掛 PENDING。
**不得以序列推定逕行寫入**（R-AM15 禁單路定案）。

### 三.2 SWE1_AMM_050 — 部分覆蓋
4866112 為「獨立音量控制之細節參見 {Radio Performance Standard}」，
係外部參照句。葉之「維持並控制 ENT／INFO1／INFO2 之獨立音量等級」
本體不在 CFTS019。
**建議**：錨 4866112，標部分覆蓋；獨立音量控制之具體行為併入 DR-AM1。
TC 僅驗三來源音量可各自獨立設定且互不影響，不寫 RPS 之細節。
註：`inputs/` 內有 SYS2 PF R1L-R（Radio Performance Standard Part-1），
但依 R-AM5 該文件範圍外（無 SWE.1 覆蓋），**不得引為錨**。

### 三.3 SWE1_AMM_087 — 部分覆蓋
4866221 為「音量調節與靜音條件依 HU HMI Specification 與 Routing_Table
執行」之前提句。與 076b（4866155）同型。
**建議**：錨 4866221，標部分覆蓋；Routing_Table 具體對應併入 DR-AM1。
（4866223 為同文之另一物件且在池外，**第二路請一併判別何者為本案適用**。）

### 三.4 SWE1_AMM_026 — 未決
葉為「收到音量增加請求 → 決定目標音量」。全文檢索 `target volume` 僅命中
4866011／4866015（Ramp Up／Ramp Down 之「線性變化至目標音量」定義），
係斜坡函數定義，非音量請求處理。
**建議**：C 級，掛 `PENDING: DR-AM1`。第二路若尋得直接對應則升級。
**不得以 4866011 代入**——該物件之驗證對象為斜坡連續性，非目標音量決定。

### 三.5 SWE1_AMM_076（＝076a，SYS-RA-AMM-242）— 未決
葉為「經 `$StWhl_VolumeUp$` / `$StWhl_VolumeDown$` 之方向盤音量請求」。
全文檢索 `StWhl_Volume` 與 `steering wheel volume` **零命中**。
CFTS019 疑無方向盤音量控制之需求（該功能或屬 SWC/Steering Wheel Controls
之獨立 CFTS）。
**建議**：C 級，掛 `PENDING: DR-AM1`，並於 DR 中明列此一疑似跨文件缺口。
**交付欄依 R-AM6 照抄 `SWE1_AMM_076`**（本批為 076a；076b 已於 B2 交付，
兩列同號不同錨，reasoning 須註明本列來源為 SYS-RA-AMM-242）。

---

## 四、撰寫注意

1. **VSIM mute／unmute 兩組已定序**：mute = 4866689–4866694，
   unmute = 4866695–4866698。B2 已用 4866689–4866692、4866695；
   B3 用 4866693（183，HMI 指示）、4866696/97/98（185/186/187）。
   **跨批一致性**：183 與 B2 之 179–182 同屬 mute 組，撰寫時參照 B2 既有 TC。
2. **141 之同文異錨**：4866490 與 4866467 本文皆為「HU 應儲存現行顯示設定」，
   分屬不同序列（Information 停用序列 vs Entertainment 序列）。
   第二路請確認 141 歸屬何序列；若兩者皆需覆蓋，屬 §8.2.2 之一 RD 多 TC。
3. **114／119 之同文異錨**：4866299 與 4866308 本文相同（Fade/Balance HMI
   更新），分屬不同章節。兩葉分派須由第二路定；分派後 tc_title 之 sibling
   區分 token 須寫出章節情境差異。
4. **081／082 為互補對**：NAFTA = OFF、其他市場 = level 1。屬 §7 之列舉配對，
   兩條必須成對出現，不得只寫其一。
5. **`<Tdisp>` = Max 100 ms**（全文 18 處使用，定義列已確認），
   185/186/187 與 044、114、119 依 IN §8.7.1 以實值入 TC，不留 PENDING。
6. **訊號**：本批涉及 `$VolumeENT$`、`$VolumeINFO1/2$`、`$VolumeSCV$`、
   `$ENTMuted$`、`$VSIMMuteReq$`、`$ShiftLeverPosition$`、
   `$Reverse_Mute_Enable$`、`$StWhl_VolumeUp/Down$`。
   依 B2 §五.3 之實測，HU 側 CAN 定義整體不在供應之 DBC 內，
   一律依 R-13(g) 保留原文名並掛 DR-AM4，**不得代換近似訊號**。
   `TLM_Status.Info`、`TLM_Vol_UP/DOWN_Status.Info`、`SVC_Setup.Req`、
   `SVC_Level_Setting.Req` 為內部訊號，依 v3(d) 保留來源名、不加 `$`。
7. **`[$xx]` 型值依 R-AM17** 取 SWE.1 葉之等義寫法並加雙引號；
   葉無等義寫法者掛 DR，不自創。
8. **大小寫不敏感檢索**：B2 之 `<Vent off>` 一案（大小寫敏感檢索漏掉定義列，
   誤掛 DR-AM8）為前車之鑑。本批凡查「參數無定義」者，一律以
   大小寫不敏感檢索複查後方得掛 PENDING。

---

## 五、EE Architecture 統計（DR-AM7 證據補強）

B3 之 A＋B 級錨共 39 個（不含 C 級未定）：

| 標記 | 個數 |
|---|---|
| 含 `Atlantis High`（或 All） | 27 |
| **僅 `Atlantis Mid`，不含 High** | **12** |

比例 31%，低於 B2 之 51%（24/47），但仍屬顯著。集中於 TLM 音量段
（4866126／4866127／4866130／4866148–4866156）與 SCV 段（4866212–4866233）。
**併入 DR-AM7 之證據**：兩批累計 36 個錨標記為 Atlantis Mid 而不含 High，
橫跨仲裁、靜音、音量、SCV 四個功能域，非零星現象。
處置不變：**不阻塞**，照現行錨表出貨（IN §8.2.1 上游分解為權威）。

---

## 六、執行層下一步

1. A 級 26 葉：複核（重點 §四之區辨提示）。
2. B 級 12 葉：第二路獨立佐證，與本表對帳。
3. C 級 4 葉（026、076a、291、以及 087／050 之部分覆蓋判定）：
   第二路查證結果回報，未決者掛 PENDING。
4. 對帳結果回分析層 → 定案錨表下放 → 方得開工。

## 七、未結 DR（七件；DR-AM8 已撤）

DR-AM1（**擬再收**：026 目標音量、076a 方向盤音量、050 獨立音量控制、
087 Routing_Table）、AM2、AM3、AM4（範圍已擴大為 HU 側 CAN 定義整體缺件）、
AM5、AM6、AM7（證據已補強）。
