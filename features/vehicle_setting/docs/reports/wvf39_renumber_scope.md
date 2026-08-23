# W-VF39 —— `R-VS59`–`R-VS67` 改號範圍之分類（R-VF45；**只列不改**）

**本輪未執行任何取代。** 分類結果回報待核（V15 §7 第 3 項）。

## 0. 錨點（R-VF21 ／ R-VF28：以內容定錨，不以行號）

| 錨點 | 處 | 判 |
|---|---|---|
| 必為「現行」 | `RULINGS.md` 之 `> **【(a) 段之「故不寫」效果經 R-VS59（63 包 §1，Pei 2026-…` | 現行 ✅ |
| 必為「歷史」 | `docs/handoff/77_split_and_full.md` | 歷史 ✅ |
| **鑑別**（Part 1 檔名而引用 VF230 線） | `docs/handoff/64_review_round40.md` — `VF230 線現行之 `R-VS59`～`R-VS63` 五條，其標題加註…` | 歷史／Part 1 ⚠ **機械取代最易誤傷者** |

## 1. R-VS67 是否亦撞號（V15 §7 第 1 項）

**否。** `RULINGS.md` 內 `### R-VS67 ——` 僅 **1 個條文起始**（Part 1 之 71 包，「訊號名與值域一律取 LID `Atlantis High` 欄組」）。

**惟實測揭出一項更嚴重者**：`R-VF1`–`R-VF9` **九號於 `RULINGS.md` 全為 0**。
R-VF1–R-VF8 以 `R-VS59`–`R-VS66` 存在（即 A-VF10 之撞號），
而 **`R-VF9`（Test Group）自始未以任何編號落檔** ——
其原號 `R-VS67` 已為 Part 1 所用，而其正文從未進入條文簿，
**卻被 `RULINGS.md` 引用 3 處，且 `framework.md` 之 Layer 1 立於其上**。
**本輪已補落**（見 `RULINGS.md` 之「V03 包（補落，自始未落檔）」節），
並補施行其所令之 `profiles.vf230.test_group` 賦值。

## 2. 分類（704 處 ／ 62 檔）

- **現行有效（須改）164 處**
- **歷史紀錄（不追改）540 處**
- 待人工 0 處

### 2.1 現行有效者 —— 須改（逐處，以內容片段定位）

| 檔 | 內容片段 | 涉及編號 | 屬哪一線 |
|---|---|---|---|
| `ANOMALIES.md` | `| **A-VS124** | **61 包所開之 W-102–W-107 與 DR-27 與 Part 1 既有編號全面撞號** | 38` | R-VS60 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS132** **【VF230 線舊制編號，R-VF10 前所開，保留】** | **037 之 8 列判 `Heading`` | R-VS59 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS129** **【VF230 線舊制編號，R-VF10 前所開，保留】** | **5 個 `swe_id` 與其 `tit` | R-VS66 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS135** **【VF230 線舊制編號，R-VF10 前所開，保留】** | **W-116／W-119 之判準三度修正 ` | R-VS65／R-VS66 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS137** | **`HSW_StatFailSts` 之值域於 `spec_variables.tsv` 與 LID 兩欄` | R-VS59／R-VS62 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS139** | **W-112 之「查得 174／查無 0」為 Layer 3 群層級之命中，非逐 leaf 之畫面層對應*` | R-VS59 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS140** | **`$VC_VEH_LINE$` 於 237 leaf 僅 2 處引用，其值為 `WL` 與 `M4 OR` | R-VS62 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS142** | **pilot #4 之分層維度 `dr_dependent`（有／無）退化 —— 43/43 皆為「有」*` | R-VS59 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS148** | **R-VS67 之 (a)(c) 相衝：44 條已交付 TC 之四階斷言於 1 bit 訊號上無法成立，分` | R-VS66／R-VS67 | 共用簿 |
| `ANOMALIES.md` | `| **A-VS152** | **D-3 令補入之 PDT24 兩檔不在 `inputs/`，與本輪禁區「不補素材」相衝** | 47 輪` | R-VS61 | 共用簿 |
| `ANOMALIES.md` | `| **A-VF10** | **`R-VS59`–`R-VS66` 八條各有兩個定義 —— R-VF10 所欲防之撞號至今仍活在 `RUL` | R-VS59／R-VS60／R-VS62／R-VS66 | 共用簿 |
| `CROSSLINE.md` | `| **R-VF10** | `RULINGS.md`／`ANOMALIES.md` 之編號 | 同一編號不得有兩個定義 | `grade_` | R-VS59／R-VS66 | 共用簿 |
| `DATA_REQUESTS.md` | `> **40 輪 D-3（依 R-VS61，63 包 §3）**：**性質由阻塞轉確認，不阻塞。**` | R-VS61 | 共用簿 |
| `DATA_REQUESTS.md` | `> 依 R-VS61 **仍產 TC**，其值取來源逐字（`STATUS_CCAN3.EngineSts = IDLE_STBL`，**不附` | R-VS61 | 共用簿 |
| `DATA_REQUESTS.md` | `## DR-8′（**撤回，不送出** —— R-VS62′，65 包 §1；42 輪 D-3。原文保留 —— R-TM13）` | R-VS62 | 共用簿 |
| `DATA_REQUESTS.md` | `> **撤回理由（R-VS62′）**：本 DR 縮限後之三碼（`M182`／`M189`／`M240`）` | R-VS62 | 共用簿 |
| `DATA_REQUESTS.md` | `> **40 輪 D-3 之縮限（依 R-VS62，63 包 §4，Pei 2026-08-23）**：` | R-VS62 | 共用簿 |
| `DATA_REQUESTS.md` | `> **40 輪 D-3（依 R-VS59，63 包 §6）**：**性質由阻塞轉確認，不阻塞。**` | R-VS59 | 共用簿 |
| `DATA_REQUESTS.md` | `> 其 61 leaf 依 R-VS57／R-VS59 照寫，訊號名與值域取來源逐字並標 `dr_dependent`；` | R-VS59 | 共用簿 |
| `DATA_REQUESTS.md` | `**不得代用 CFTS044 之 SYS2** —— 其為該 CFTS 專屬（R-VS63 之末段明排除）。` | R-VS63 | 共用簿 |
| `DATA_REQUESTS.md` | `補入須依 **R-VS61**（由 Pei 執行；2026-08-23 之免除為單次個案）。` | R-VS61 | 共用簿 |
| `RULINGS.md` | `> **【(a) 段之「故不寫」效果經 R-VS59（63 包 §1，Pei 2026-08-23）撤回；原文保留不刪】**` | R-VS59 | 共用簿 |
| `RULINGS.md` | `> 廢止理由：該判準之前提為「值未解即不可寫」，而 **R-VS61 已否定該前提**。` | R-VS61 | 共用簿 |
| `RULINGS.md` | `> **【(2) 經 R-VS67 推翻，2026-08-23（Pei）；原文保留不刪】**` | R-VS67 | 共用簿 |
| `RULINGS.md` | `第五條（R-VS63）為 Pei 於同日就 61 包 §6 第 3–5 項另行之裁定。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `### R-VS59 —— VF230 之 B 欄序號自 238 起（61 包 §3，**Pei 裁定 2026-08-23**）` | R-VS59 | 共用簿 |
| `RULINGS.md` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS59（VF230 序號基準，Pei 裁定 2026-08-23）` | R-VS59 | 共用簿 |
| `RULINGS.md` | `4. F 欄「Test Case ID」兩本 workbook 皆為 0 filled；R-VS59 **不**新增` | R-VS59 | 共用簿 |
| `RULINGS.md` | `### R-VS60 —— VF230 併入 `vehicle_setting`，不另開 feature（61 包 §3，**Pei 裁定 ` | R-VS60 | 共用簿 |
| `RULINGS.md` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS60（VF230 之 feature 歸屬，Pei 裁定 2026-08-23）` | R-VS60 | 共用簿 |
| `RULINGS.md` | `### R-VS61 —— 素材補入由 Pei 執行（61 包 §3，**Pei 裁定 2026-08-23**）` | R-VS61 | 共用簿 |
| `RULINGS.md` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS61（VF230 素材補入，Pei 裁定 2026-08-23）` | R-VS61 | 共用簿 |
| `RULINGS.md` | `### R-VS62 —— `output/` 之證據位階（61 包 §3，**Pei 裁定 2026-08-23**）` | R-VS62 | 共用簿 |
| `RULINGS.md` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS62（Pei 先前彙整之證據位階，Pei 裁定 2026-08-23）` | R-VS62 | 共用簿 |
| `RULINGS.md` | `- 其所含之任何列序，**不**構成 R-VS59 之續號依據` | R-VS59 | 共用簿 |
| `RULINGS.md` | `### R-VS63 —— 專案級 REF 素材得由 CFTS044 代用（**Pei 裁定 2026-08-23**）` | R-VS63 | 共用簿 |
| `RULINGS.md` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS63（VF230 之 REF 素材代用，Pei 裁定 2026-08-23）` | R-VS63 | 共用簿 |
| `RULINGS.md` | `> **編號說明（Pei 裁定 2026-08-23）**：下列四條為 **CFTS044 本線**之 R-VS59～R-VS62，` | R-VS59／R-VS62 | 共用簿 |
| `RULINGS.md` | `### R-VS59 —— 委派不等於不寫（63 包 §1，**Pei 裁定 2026-08-23**；取代 R-VS7(a) 之效果）` | R-VS59 | 共用簿 |
| `RULINGS.md` | `R-VS59（Pei 2026-08-23）` | R-VS59 | 共用簿 |
| `RULINGS.md` | `### R-VS60 —— A-VS103 之跨列引入，准（63 包 §2，**Pei 裁定 2026-08-23**）` | R-VS60 | 共用簿 |
| `RULINGS.md` | `R-VS60（Pei 2026-08-23）` | R-VS60 | 共用簿 |
| `RULINGS.md` | `### R-VS61 —— DR-19：無匯流排對應者，寫分析所載之名（63 包 §3，**Pei 裁定 2026-08-23**）` | R-VS61 | 共用簿 |
| `RULINGS.md` | `R-VS61（Pei 2026-08-23）` | R-VS61 | 共用簿 |
| `RULINGS.md` | `### R-VS62 —— DR-8′：車型碼取自 PROXI 表（63 包 §4，**Pei 裁定 2026-08-23**）` | R-VS62 | 共用簿 |
| `RULINGS.md` | `> **【經 R-VS62′ 取代，2026-08-23；原文保留不刪，見 R-TM13】**` | R-VS62 | 共用簿 |
| `RULINGS.md` | `R-VS62（Pei 2026-08-23）` | R-VS62 | 共用簿 |
| `RULINGS.md` | `### R-VS64 —— W 號改編追認（62 包 §3，分析層裁定 2026-08-23）` | R-VS64 | 共用簿 |
| `RULINGS.md` | `R-VS64（VF230 進場之 W 號改編，分析層裁定 2026-08-23）` | R-VS64 | 共用簿 |
| `RULINGS.md` | `### R-VS65 —— W-115（DR 波及判定）之輸入改以 token 掃描（62 包 §3，分析層裁定 2026-08-23）` | R-VS65 | 共用簿 |
| `RULINGS.md` | `R-VS65（DR 波及判定之輸入，分析層裁定 2026-08-23）` | R-VS65 | 共用簿 |
| `RULINGS.md` | `### R-VS66 —— Layer 2 決定前之前置複驗（62 包 §3，分析層裁定 2026-08-23）` | R-VS66 | 共用簿 |
| `RULINGS.md` | `R-VS66（Layer 2 交集之正規化複驗，分析層裁定 2026-08-23）` | R-VS66 | 共用簿 |
| `RULINGS.md` | `### R-VS63 —— 編號分線（64 包 §4，分析層裁定 2026-08-23）` | R-VS63 | 共用簿 |
| `RULINGS.md` | `R-VS63（分析層裁定 2026-08-23）` | R-VS63 | 共用簿 |
| `RULINGS.md` | `VF230 線現行之 `R-VS59`～`R-VS63` 五條，其標題加註` | R-VS59／R-VS63 | 共用簿 |
| `RULINGS.md` | `**引用之義務**：跨線引用時須標線名（如「VF230 線之 R-VS59」）。` | R-VS59 | 共用簿 |
| `RULINGS.md` | `### R-VS62′ —— `$VC_VEH_LINE$` 之值域取 PROXI 表列 466；DR-8′ 撤回（65 包 §1，分析層裁` | R-VS62 | 共用簿 |
| `RULINGS.md` | `R-VS62′（分析層裁定 2026-08-23，取代 R-VS62）` | R-VS62 | 共用簿 |
| `RULINGS.md` | `R-VS62 原文所列之四碼（`332`／`WS`／`DT`／`HDCC`）**於母體命中 0**，` | R-VS62 | 共用簿 |
| `RULINGS.md` | `R-VS60 之跨列引入只實作於驅動側，致 batch17 首次自檢報 4 項 R-VS39 違規）。` | R-VS60 | 共用簿 |
| `RULINGS.md` | `### R-VS64 —— 升級門檻不得以常數表示（68 包 §1，分析層裁定 2026-08-23）` | R-VS64 | 共用簿 |
| `RULINGS.md` | `R-VS64（分析層裁定 2026-08-23）` | R-VS64 | 共用簿 |
| `RULINGS.md` | `成因：R-VF2（原 R-VS60）令 VF230 併入 `vehicle_setting`，兩條分析線` | R-VS60 | 共用簿 |
| `RULINGS.md` | `理由：R-VF8（原 R-VS66）之逐字正規化不足以達成其自身目的 ——` | R-VS66 | 共用簿 |
| `RULINGS.md` | `### R-VS65 —— （69 包 §1，44 輪之條文；46 輪 D-2 補轉錄）` | R-VS65 | 共用簿 |
| `RULINGS.md` | `R-VS65（分析層裁定 2026-08-23）` | R-VS65 | 共用簿 |
| `RULINGS.md` | `### R-VS66 —— 規格明確而實作未見之處置（71 包 §2）` | R-VS66 | 共用簿 |
| `RULINGS.md` | `R-VS66（分析層裁定 2026-08-23）` | R-VS66 | 共用簿 |
| `RULINGS.md` | `**本例（`*_Cmd_Tlm`）依 R-VS67 改由 LID 取名，已無實作缺口，(a) 不適用。**` | R-VS67 | 共用簿 |
| `RULINGS.md` | `### R-VS67 —— 訊號名與值域一律取 LID 之 `Atlantis High` 欄組（71 包 §1，**Pei 裁定 2026` | R-VS67 | 共用簿 |
| `RULINGS.md` | `> **【經 R-VS67′ 限縮，2026-08-23（Pei 追認）；原文保留不刪】**` | R-VS67 | 共用簿 |
| `RULINGS.md` | `> 並依 R-VS66(a) 標 `impl_gap`。**(推翻 R-VS51(2) 之部分不變。)**` | R-VS66 | 共用簿 |
| `RULINGS.md` | `R-VS67（Pei 2026-08-23）` | R-VS67 | 共用簿 |
| `RULINGS.md` | `### R-VS67′ —— 欄組之選取依「能承載」，不能承載者標 `impl_gap`（73 包 §1，**Pei 追認 2026-08-` | R-VS67 | 共用簿 |
| `RULINGS.md` | `R-VS67′（**Pei 追認 2026-08-23**，限縮 R-VS67）` | R-VS67 | 共用簿 |
| `RULINGS.md` | `並依 **R-VS66(a)** 標 `impl_gap = <訊號名>`` | R-VS66 | 共用簿 |
| `RULINGS.md` | `該訊號不在基線 DBC → **標 `impl_gap`，依 R-VS66(a) 照寫、開 issue 予 RD**` | R-VS66 | 共用簿 |
| `RULINGS.md` | `(d) **DR-25′ 維持撤回** —— 其標的（訊號不在 DBC）依 R-VS66 已非 DR 之事由，` | R-VS66 | 共用簿 |
| `RULINGS.md` | `**⚠ 檢查二之「必不命中」錨點於現行全檔即失敗** —— 非錨點有誤，是**真違反**：`R-VS59`–`R-VS66` **各有兩個條` | R-VS59／R-VS66 | 共用簿 |
| `RULINGS.md` | `值無對應而來源有逐字   → `= <來源逐字值>`，**不附 raw**（R-VS61），` | R-VS61 | 共用簿 |
| `RULINGS.md` | `而 R-VS61 已否定該前提。R-VS47 之 W1／W2 分界依本條重定。` | R-VS61 | 共用簿 |
| `RULINGS.md` | `**W-VF39 實測發現**：`R-VF9`（Test Group）**自始未以任何編號落檔於 `RULINGS.md`** —— 其原編` | R-VS67 | 共用簿 |
| `RULINGS.md` | `> **原文之編號為 `R-VS67`，逐字保留於區塊內**（R-VF45 三之精神：使歷史引用可解）。` | R-VS67 | 共用簿 |
| `RULINGS.md` | `R-VS67（VF230 之 Test Group，Pei 裁定 2026-08-23）` | R-VS67 | 共用簿 |
| `RULINGS.md` | `（R-VS60），單一 feature 內之 Test Group 保持單值，優先於 spec 模組名之` | R-VS60 | 共用簿 |
| `RULINGS.md` | `R-VF45（R-VS59–R-VS66 撞號之處置，分析層裁定 2026-08-23）` | R-VS59／R-VS66 | 共用簿 |
| `RULINGS.md` | `A-VF10 實測：`R-VS59`–`R-VS66` 八號各有兩個定義，兩線皆為 Pei 裁定、` | R-VS59／R-VS66 | 共用簿 |
| `RULINGS.md` | ``R-VS59→R-VF1 … R-VS66→R-VF8`，並註明` | R-VS59／R-VS66 | 共用簿 |
| `RULINGS.md` | `「歷史文件中之 `R-VS59`–`R-VS66` 可能指兩義之任一，` | R-VS59／R-VS66 | 共用簿 |
| `RULINGS.md` | `**R-VF9 原為 R-VS67，亦在 V04 §3.1 之對照表內**；本條所列為 59–66 八號，` | R-VS67 | 共用簿 |
| `RULINGS.md` | `**第 1 項之實測揭出一項更嚴重者**：`R-VS67` **不撞號**（僅 1 個起始），而 **`R-VF1`–`R-VF9` 九號於` | R-VS67 | 共用簿 |
| `docs/INDEX.md` | `| 34 | — | 母體層冗餘掃描、R-VS57(4) 重跑、產能終局盤點 | [61](handoff/61_review_round3` | R-VS59／R-VS61／R-VS63 | 共用簿 |
| `feature.yaml` | `# 本 feature 含兩份交付（R-VS60）：` | R-VS60 | 共用簿 |
| `feature.yaml` | `# 尋得，惟未補入（R-VS61）且缺 6 個 E-Save leaf。` | R-VS61 | 共用簿 |
| `feature.yaml` | `# R-VS59 —— B 欄「No.#/序號」自 238 起連續遞增。` | R-VS59 | 共用簿 |
| `scripts/batch15_w108.py` | `"**以 pre_conditions 之階數配置分辨**（R-VS59 前之既有慣例）。",` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `（A-VS116 之標的，本輪因 R-VS59 首次入池）。同序內逐 Layer 2 輪流 ＋ reqid 升冪。` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `故本批之畫面層斷言一律標 `PENDING: DR-5-B`（R-VS59(4)）。見上繳 35 §2.2。` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `"reasoning": (why + "；畫面層依 R-VS59(2) 取自 Comfort 素材，"` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `"故依 R-VS59(4) 標 `PENDING: DR-5-B`"),` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `"selection": "W-111 後之池 **35**（R-VS59 解除 delegate 之扣除）。"` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `"screen_layer": "R-VS59(2) 之來源不足 —— 全 10 條之畫面層斷言標 `PENDING: DR-5-B`（R-` | R-VS59 | 共用簿 |
| `scripts/batch16_w113.py` | `"自 R-VS59 撤回 `delegate = blocked` 之扣除後首次入池）。"` | R-VS59 | 共用簿 |
| `scripts/batch17_w116.py` | `查無者依 R-VS59(4) 標 `PENDING`。` | R-VS59 | 共用簿 |
| `scripts/batch17_w116.py` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | R-VS59 | 共用簿 |
| `scripts/batch17_w116.py` | `+ ("故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | R-VS59 | 共用簿 |
| `scripts/batch17_w116.py` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-5-B`（R-VS5` | R-VS59 | 共用簿 |
| `scripts/batch17_w116.py` | `"`FR_VS_Cmd_Tlm` 之二條為 R-VS60 跨列引入後首次可寫。",` | R-VS60 | 共用簿 |
| `scripts/batch18_w119.py` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | R-VS59 | 共用簿 |
| `scripts/batch18_w119.py` | `+ ("，故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | R-VS59 | 共用簿 |
| `scripts/batch18_w119.py` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-5-B`（R-VS5` | R-VS59 | 共用簿 |
| `scripts/batch19_w122.py` | `**依 R-VS64，本批不寫死條數** —— 池扣除 held_out 後有幾條即取幾條。` | R-VS64 | 共用簿 |
| `scripts/batch19_w122.py` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | R-VS59 | 共用簿 |
| `scripts/batch19_w122.py` | `+ ("，故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | R-VS59 | 共用簿 |
| `scripts/batch19_w122.py` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-5-B`（R-VS5` | R-VS59 | 共用簿 |
| `scripts/carry_test_w133.py` | `"""W-133（73 包 §5）—— R-VS67′ 之「能承載」判準與欄組選取。` | R-VS67 | 共用簿 |
| `scripts/carry_test_w133.py` | `R-VS67′：欄組之選取依下列次序 ——` | R-VS67 | 共用簿 |
| `scripts/carry_test_w133.py` | `(2) 不能承載者 → 取**能承載之欄組**（`Atlantis`），並依 R-VS66(a) 標 `impl_gap`` | R-VS66 | 共用簿 |
| `scripts/carry_test_w133.py` | `"""R-VS67′ 之次序選取。"""` | R-VS67 | 共用簿 |
| `scripts/dr_conflict.py` | `# **R-VS61（63 包 §3，Pei 2026-08-23）**：無匯流排對應者仍產 TC，` | R-VS61 | 共用簿 |
| `scripts/dr_conflict.py` | `"DR-19": ("value", set(), r"(?!x)x", "待覆（性質轉確認，R-VS61；不阻塞）"),` | R-VS61 | 共用簿 |
| `scripts/dr_conflict.py` | `# **R-VS62（63 包 §4，Pei 2026-08-23）**：`VC_VEH_LINE` 之車型碼取自` | R-VS62 | 共用簿 |
| `scripts/dr_conflict.py` | `"DR-8": ("value", {"VC_VEH_LINE"}, r"M182|M189|M240", "待送（縮為三碼，R-VS62）` | R-VS62 | 共用簿 |
| `scripts/impl_gap_w133.py` | `"""W-133(4)（73 包 §5）—— 依 R-VS67′ 回復 44 條之斷言並標 `impl_gap`。` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `46 輪 W-131 依 R-VS67 將訊號名改取 `Atlantis High` 欄組之 `*_Tlm`（1 bit），` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `致四階斷言無法成立（44 條）。R-VS67′ 令**不能承載者取能承載之欄組**` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `（`Atlantis` → `*_Cmd_Tlm`，四階）並依 **R-VS66(a)** 標 `impl_gap`。` | R-VS66 | 共用簿 |
| `scripts/impl_gap_w133.py` | ``dr15_exposed` 之標記**保留**（R-VS67′(a)）—— DR-15′ 之答覆仍可能改其形態。` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `BACK = {  # `Atlantis High`（1 bit）→ `Atlantis`（四階），R-VS67′(2)` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `tc["signal_source"] = ("LID `Atlantis` 欄組（R-VS67′(2)：`Atlantis High` "` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `+ (f"IMPL_GAP: {tc['impl_gap']} —— 依 R-VS66(a) 照寫，"` | R-VS66 | 共用簿 |
| `scripts/impl_gap_w133.py` | `d["revision"] = ("W-133(4)（47 輪）：依 R-VS67′ 取能承載之 `Atlantis` 欄組，"` | R-VS67 | 共用簿 |
| `scripts/impl_gap_w133.py` | `"標 `impl_gap`（R-VS66(a)）；`dr15_exposed` 保留")` | R-VS66 | 共用簿 |
| `scripts/screen_layer_w132.py` | `**D-2 圖示變更類**（72 包 §1 之 R-VS59(4) 細化）：` | R-VS59 | 共用簿 |
| `scripts/screen_source_w112.py` | `"""W-112（63 包 §7）—— Comfort 素材之畫面層對照表（R-VS59(2) 之前置）。` | R-VS59 | 共用簿 |
| `scripts/screen_source_w112.py` | `**必列**：查得／查無兩數。**查無者即 R-VS59(4) 之 PENDING 標的。**` | R-VS59 | 共用簿 |
| `scripts/screen_source_w115.py` | `# R-VS59 已廢除 `blocked` 之值；`delegation_lookup.tsv` 尚未同步，` | R-VS59 | 共用簿 |
| `scripts/selfcheck_w53.py` | `# **R-VS60（63 包 §2，Pei 2026-08-23）**：`FR_VS_Cmd_Tlm` 之值域准自` | R-VS60 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `"""W-131（72 包 §6；承 71 包 §5 之 W-127＋W-128）—— R-VS67 之訊號名改寫。` | R-VS67 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `R-VS67：訊號名、message、值域**一律取 LID `Atlantis High` 欄組**，` | R-VS67 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `其為 **DR-15′ 之標的**，依 R-VS67(d) 逐條標 `dr15_exposed = yes`。` | R-VS67 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `+ ("BLOCKED: DR-15′ —— 改依 R-VS67 取 `*_Tlm`（1 bit，"` | R-VS67 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `tc["signal_source"] = "LID `Atlantis High` 欄組（R-VS67）"` | R-VS67 | 共用簿 |
| `scripts/signal_rewrite_w131.py` | `d["revision"] = ("W-131（46 輪）：依 R-VS67 將訊號名改取 LID "` | R-VS67 | 共用簿 |
| `scripts/vehline_anchor_w115.py` | `"""W-115(1)（64 包 §5）—— R-VS62 之真錨點。` | R-VS62 | 共用簿 |
| `scripts/vf230_crosscheck.py` | `"**本輪採 035**，其已在 `inputs/` 內（R-VS61 之補入由 Pei 執行）。", "",` | R-VS61 | 共用簿 |
| `scripts/vf230_layer2.py` | `"""比對用鍵 —— R-VS66 之正規化（W-116）。` | R-VS66 | 共用簿 |
| `scripts/vf230_w119_dr_impact.py` | `依 **R-VS65** 之掃描定義（逐字）：` | R-VS65 | 共用簿 |
| `scripts/vf230_w119_dr_impact.py` | `# 掃描面：title ＋ desc（R-VS65）` | R-VS65 | 共用簿 |
| `scripts/vf230_w119_dr_impact.py` | `"**依 R-VS65 之掃描定義（62 包 §3）。**", "",` | R-VS65 | 共用簿 |
| `scripts/writability_driver.py` | `"""**R-VS67（71 包 §1，Pei 2026-08-23）**：一律取 `Atlantis High` 欄組。` | R-VS67 | 共用簿 |
| `scripts/writability_driver.py` | `# **R-VS67′（73 包 §1，Pei 追認 2026-08-23）**：欄組依「能承載」擇之 ——` | R-VS67 | 共用簿 |
| `scripts/writability_driver.py` | `# **R-VS60（63 包 §2，Pei 2026-08-23）**：`FR_VS_Cmd_Tlm` 之值域` | R-VS60 | 共用簿 |
| `scripts/writability_driver.py` | `# **R-VS67′**：欄組之選取依「能承載」，**不依條文之架構標籤** ——` | R-VS67 | 共用簿 |
| `scripts/writability_driver.py` | `# 故不再以 `col == "Atlantis"` 為閘（R-VS51(2) 已由 R-VS67 推翻，` | R-VS67 | 共用簿 |
| `scripts/writability_driver.py` | `# 而 R-VS67 之「一律 High」又由 R-VS67′ 限縮）。` | R-VS67 | 共用簿 |
| `scripts/writability_driver.py` | `**R-VS59（63 包 §1，Pei 2026-08-23）**：委派不免除產出 TC 之義務 ——` | R-VS59 | 共用簿 |
| `scripts/writability_driver.py` | `# R-VS59：`blocked` 之值廢除` | R-VS59 | 共用簿 |

**⚠ 上表含兩線之引用。** 依 R-VF45 一，**僅 VF230 線之八號改為 `R-VF1`–`R-VF8`，Part 1 之八號不動** —— 故本表之每一處尚須判其
**所指為兩義之何者**，該判斷不可由編號決定，須讀其上下文。
**本層未判、未改。**

### 2.2 歷史紀錄者（逐檔計數，不追改）

| 檔 | 處 |
|---|---:|
| `docs/reports/wvf39_renumber_scope.md` | 175 |
| `docs/handoff/63_rulings_round39.md` | 27 |
| `docs/upstream/35_delegation_reopen.md` | 24 |
| `docs/handoff/71_lid_primary.md` | 22 |
| `docs/handoff/V00_numbering_collision.md` | 20 |
| `docs/handoff/V01_vf230_intake.md` | 17 |
| `docs/handoff/V02_vf230_recon_review.md` | 16 |
| `docs/handoff/73_rvs67_narrowing.md` | 16 |
| `docs/handoff/64_review_round40.md` | 16 |
| `docs/upstream/36_domain_and_anchor.md` | 16 |
| `docs/upstream/40_narrowing.md` | 14 |
| `docs/upstream/39_pilot_fix.md` | 14 |
| …（其餘 26 檔）| |

## 3. 對照表（供 R-VF45 三置入 `RULINGS.md`）

| 舊（VF230 線） | 新 |
|---|---|
| `R-VS59` | `R-VF1` |
| `R-VS60` | `R-VF2` |
| `R-VS61` | `R-VF3` |
| `R-VS62` | `R-VF4` |
| `R-VS63` | `R-VF5` |
| `R-VS64` | `R-VF6` |
| `R-VS65` | `R-VF7` |
| `R-VS66` | `R-VF8` |
| `R-VS67` | `R-VF9` |

> 歷史文件中之 `R-VS59`–`R-VS67` 可能指兩義之任一，**以該文件之線別判之**。使歷史引用**可解，而非可靠**。

