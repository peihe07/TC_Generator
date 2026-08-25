# DATA REQUESTS — Display (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/display/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

**R-G14（2026-08-24，全域）**：凡屬「某訊號／參數查無」之 DR，開立前須先
滿足 R-G13 三要件並登入 `forms/LOOKUP_MISSES.md`。台帳防重複發現、
本表綁上游提問、`ANOMALIES.md` 綁批次 —— 三處各有其職，不互相取代。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-DM1 | CFTS_009（條號 `{CFTS009-722}`，定義 `Start Up Sequence - Splash/Disclaimer Screen` 之時段）— 檔名待查（pattern：`…CFTS_009…docx`） | OPEN | SWE-DM-003 | splash/sleep 時長之預期結果無法寫 | — | HIGH |
| DR-DM2 | Popup 優先序仲裁規則與 timeout 之來源（CFTS 本文僅有 RVC「high priority」語句，無仲裁順序表或 timeout 值） | OPEN | SWE-DM-006 | popup 仲裁之預期結果無法寫 | — | HIGH |
| DR-DM3 | `SYS-RA-DISP-*` ↔ SYS2 之對應表，或含 `DISP` id 之 SYS2 版本 | OPEN | 全 8 leaf 之追溯欄 | 追溯鏈斷；spec_reference 無 id 路徑 | A-DM2 / A-DM10 | MEDIUM |
| DR-DM4 | CFTS_013（條號 `CFTS013-629` Standard/`-633` Standard/`-952` Multi-stage，載 DCSD Display Hot 演算法本體與其分級溫度門檻）— 檔名待查（pattern：`…CFTS_013…docx`） | OPEN | SWE-DM-005（004 部分） | multi-stage 之分級判準無法寫；單級 85 °C 行為可寫 | A-DM13 | HIGH |
| DR-DM7 | 本專案（R1LR Atl-H）之 VF 代碼，或其 PROXI 實例檔（已填值之 PROXI，非 `_R3` 空白格式檔） | OPEN | 全 8 leaf 之前置條件 | `Used by NODE(VFXXX)` 無法用於篩選；PROXI 446 列母體無法收斂 | A-DM20 | MEDIUM |
| DR-DM6 | `Display_OFF_SoftKey_Prsnt` 之 PROXI 定義；或確認其與 `PROXI_HDCC27_R3` `Format` r692 之 `Display_OFF_SoftKey` 為同一參數（LID r63 `DSP_SK_PRSNT`） | OPEN | SWE-DM-001（Screen Off 行為之配備前提） | 該 leaf 之前置條件是否需帶軟鍵存在旗標，無法判定 | A-DM17／`forms/LOOKUP_MISSES.md` M-3 | MEDIUM |
| DR-DM5 | `RADIO_B4.CCDMF_RQ_DISP_INTS` 之 DBC 定義（訊息 `RADIO_B4` 存在於 `PDT27_E2A_R1_BHCAN2.dbc`，該 `SG_` 不存在）；一併確認 `GW_B_5.Mute_Button` | OPEN | 用到 `$CCDMF_RQ_DISP_INTS$` 之 SYS2 FR 列 | 該訊號之值域與位元定義無法寫 | A-DM10a／`forms/LOOKUP_MISSES.md` M-1、M-2 | MEDIUM |

## R-DM8 之查證結果（先查 CFTS 與 SYS3，查得者記章節）

R-DM8 列四處缺值。實測（`scripts/probe_missing_values.py`）：

| SWE-DM | 缺值 | CFTS_020 | SYS3 SYSAD | 處置 |
|---|---|---|---|---|
| 003 | Splash / sleep 之時長門檻 | 命中 9 段「splash」，惟時段定義一律轉指外部條號 `{CFTS009-722}`；`sleep` + 數值+單位 0 段 | 命中 10 段，含數值+單位 0 段 | **DR-DM1** |
| 004 | thermal warning threshold 之門檻值與單位 | **查得**：`1.11.2.2 DCSD Display Hot Behavior {4820281}`，另 `1.15.1.5 {4820659}` / `1.15.2.5 {4820937}` / `1.15.4.x` 為各架構之對應節 | 含數值+單位 0 段 | 記章節，不開 DR |
| 005 | thermal protection 之 critical 判準與回復條件 | **部分查得**：回復條件在 `{4820290}`／`{4820287}`／`{4820288}`；**分級（multi-stage）之 critical 判準轉指 `{CFTS013-952}`，不在手上** | 含數值+單位 0 段 | 回復條件記章節；分級判準 → **DR-DM4** |
| 006 | popup priority arbitration 之優先序規則與 timeout | 命中 70 段，惟皆為「high priority Rear View Camera screen」之個別語句；無仲裁順序表、無 timeout 值 | 命中 6 段，含數值+單位 0 段 | **DR-DM2** |

> 004/005 之章節為**位置登記**，非值之確認。門檻值之讀出與採用屬 Phase 2，
> 依 R-DM8 不得由本輪回填（canon §8.4.1）。

## R-DM8 之再判定（2026-08-24，下放包 03 §4.1 / 步驟 9）

上繳包 02 §14b 之查證只回 CFTS 與 SYS3，**未查 SYS2** —— 而 SYS2
r31–r34 正是該行為之狀態機定義。本輪已補查並將兩側併讀
（`scripts/hot_behaviour_join.py`，全文見上繳包 03 §6）：

| SWE-DM | 缺值 | 再判定 | 證據位置 |
|---|---|---|---|
| 004 | thermal warning threshold 之門檻值與單位 | **不缺**（就單級門檻而言） | CFTS `{4820289}`／`{4820290}`（同段落載 `> 85 degrees C` 與 `<= 85 deg C`；該兩段之 `[Radio:R1H] [EE Architecture:Atlantis High]` 與本專案 R1LR Atl-H 相符）。SYS2 r30–r34 **不含**任何溫度數值 |
| 005 | critical 判準 | **仍缺** | CFTS `1.15.1.5 {4820660}`／`1.15.4.5 {4821298}` 明載 multi-stage 版本「有較低之溫度門檻」並轉指 `{CFTS013-952}`；`{4820282}` 亦轉指 `{CFTS013-629}` → **DR-DM4** |
| 005 | 回復條件 | **不缺** | CFTS `{4820287}`（DCSD 送 `DISP_ON`）／`{4820288}`（HU 恢復正常顯示）／`{4820290}`（背光與觸控恢復、DTC de-mature）；SYS2 r34 為 `{4820288}` 之逐字同語句 |

**溫度門檻在全文之出現位置：CFTS 僅 2 段，皆在 `1.11.2.2 {4820281}` 之下
（`{4820289}`、`{4820290}`）。SYS2 r30–r34 為 0 段。**

訊號／值 token 之兩側逐字對照（非相似度）：`$DCSD_DISP_STAT$`、
`$TGW_DISP_STAT$`、`$RQ_DISP_INTS$` 三者兩側皆有、無單側；值
`[DISP_HOT]`／`[DISP_OFF]`／`[DISP_ON]`／`[0% Intensity]` 亦兩側皆有。
即 **SYS2 之 hot 四列為 CFTS `1.11.2.2` 之 HU 側子集**，非另一組需求。

> 本節仍未回填任何值。上表之 `> 85 degrees C` 係為指出「該值存在於何處」
> 而引其位置，Phase 2 方得讀出採用（R-DM8、canon §8.4.1）。
