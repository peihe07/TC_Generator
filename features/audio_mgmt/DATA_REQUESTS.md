# DATA REQUESTS — Audio Management (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/audio_mgmt/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

## 一、置檔清單（03 包 §一；執行層開工前置）

實測 2026-08-26：五件中第 5 件（R-G1 母本）已複入，**其餘四件仍未在位**。
03 包 §一 明訂「缺件即停，回報分析層」，故 B1 現為 BLOCKED。

| # | 檔案 — 全名 | Status | Batch impact | Urgency |
|---|---|---|---|---|
| 1 | `SWE_1_Audio_Management_Pending_For_Review.xlsx` | MISSING | 需求主源；缺則無 test_item 上半 verbatim 來源（R-S4） | 阻塞 B1 |
| 2 | `CFTS019AudioManagementPart1_released_20260415.xlsx` | MISSING | 錨源 Part 1（R-AM2） | 阻塞 B1 |
| 3 | `CFTS_019_Part2_All_AcceptedExceptDTCrework.xlsx` | MISSING | 錨源 Part 2（R-AM2）；B1 全 50 葉之錨落在此本 | 阻塞 B1 |
| 4 | `R1LR_Atl-H_25PI3_5_Multimedia_-_Radio_and_Audio_CFTS_019_Audio_Management_20250910_1235.pdf`（實為純文字，非 PDF） | MISSING | 章節上下文查閱 | 阻塞 B1 |
| 5 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | **IN PLACE**（2026-08-26 自 `forms/` 複入，sha256 `6372fb6b…6fb825b2` 與母本相同；原為 03 包 §一漏列） | R-G1 母本複本 = 新簿基底（R-AM3）；缺則無簿可寫回。母本在 repo `forms/` 下，但 `resolve_path` 之 glob 基準為本 feature 目錄，故須複製一份進 `inputs/` | 阻塞寫回 |

## 二、上游資料請求（DR；01 包 §五、03 包 §七）

DR 送出屬 Pei；分析層僅代擬。

| DR | 內容 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-AM1 | SYS-RA-AMM-082..1111 ↔ CFTS019 ObjectID 正式對照表缺失（SYS2 CFTS019 主體分析報告未在案；Basic Report 橋接欄全空）。請上游提供對照或補件 | 待 Pei 送出 | 全 318 葉 | **不卡批** —— 過渡採 R-AM2 內容對位＋`PENDING: DR-AM1` 並行，回件後末站統一回填校正 | — | 中（回件前每批累積回填債） |
| DR-AM2 | SWE1_AMM_076 編號碰撞（SYS-RA-AMM-242 與 -246 同號）。請上游改號 | 待 Pei 送出 | 2 葉（076 兩條） | **不卡 B1** —— 076 不在 B1；B3 遇之依 R-AM6 照抄 `SWE1_AMM_076` | — | 低（B3 前送出即可） |
| DR-AM3 | 兩本 CFTS019 Basic Report 系統性遺漏圖表型需求物件（實測在池率 7.7% vs 非圖表 39.0%；池外 12 個）。請上游依 FEATURE_ONBOARDING §3 之 chapter-level 慣例重匯 1.3.3 章，含圖表物件 | 待 Pei 送出 | 至少 7 葉（B1）＋ 全簿其餘圖表葉 | **阻塞 B1 之 7 葉**（43/50 可行） | A-AM03 | **高（B1 當下）** |
| DR-AM4 | 供應之兩本 DBC（PDT27_E2A_R1_FDCAN8／BHCAN2）缺 `$HUModeStatus$` 與 `$VolumeENT$`，且無任何命名變體或 volume 類訊號。請補 HU 側 CAN 定義或指明正確 DBC | 待 Pei 送出 | B1 之 6 條 TC；全簿凡引 HU 模式／音量訊號者 | **不卡批** —— 依 R-13 (g) 保留 CFTS 原文名交付，DBC 到位後回填全名與 label | A-AM05 | 中 |
| DR-AM5 | CFTS019 以 `<Temp Ramp Down>` / `<Temt Ramp Down>` 指涉一個全文未定義之參數（出現 10 次），疑為 `<Tent Ramp Down>`（4867767）之拼寫錯誤。請上游確認或更正 | 待 Pei 送出 | B1 之 3 條 TC（SWE1_AMM_203／206／208） | **不卡批** —— 行為面已驗證，僅時序界值待補 | A-AM04 | 中 |
| DR-AM6 | `{CFTS020}` 不在 `inputs/`。CFTS019-4866123（$ICSPowerButton$ 靜音邏輯）將行為本體外包至該文件，SWE1_AMM_061 之音量/靜音狀態、螢幕 On/Off、螢幕優先權判斷於 CFTS019 全文皆無對應。請補件或指明替代來源 | 待 Pei 送出 | B2 之 SWE1_AMM_061 | 不卡批（錨可定，行為細節掛 PENDING） | A-AM07 | 中 |
| ~~DR-AM8~~ | ~~`<vent off>` 全文僅出現一次且無定義列~~ **撤回（R-AM17，Pei 定 −16 dB）**。註：值由裁定供給，非文件補入；文件之缺口未消滅 | **撤回，未送出** | B2 之 SWE1_AMM_287 | 不卡批（行為面已驗，僅衰減量待補） | A-AM08 | 中 |

