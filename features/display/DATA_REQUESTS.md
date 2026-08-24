# DATA REQUESTS — Display (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/display/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-DM1 | CFTS_009（條號 `{CFTS009-722}`，定義 `Start Up Sequence - Splash/Disclaimer Screen` 之時段）— 檔名待查（pattern：`…CFTS_009…docx`） | OPEN | SWE-DM-003 | splash/sleep 時長之預期結果無法寫 | — | HIGH |
| DR-DM2 | Popup 優先序仲裁規則與 timeout 之來源（CFTS 本文僅有 RVC「high priority」語句，無仲裁順序表或 timeout 值） | OPEN | SWE-DM-006 | popup 仲裁之預期結果無法寫 | — | HIGH |
| DR-DM3 | `SYS-RA-DISP-*` ↔ SYS2 之對應表，或含 `DISP` id 之 SYS2 版本 | OPEN | 全 8 leaf 之追溯欄 | 追溯鏈斷；spec_reference 無 id 路徑 | A-DM2 / A-DM10 | MEDIUM |

## R-DM8 之查證結果（先查 CFTS 與 SYS3，查得者記章節）

R-DM8 列四處缺值。實測（`scripts/probe_missing_values.py`）：

| SWE-DM | 缺值 | CFTS_020 | SYS3 SYSAD | 處置 |
|---|---|---|---|---|
| 003 | Splash / sleep 之時長門檻 | 命中 9 段「splash」，惟時段定義一律轉指外部條號 `{CFTS009-722}`；`sleep` + 數值+單位 0 段 | 命中 10 段，含數值+單位 0 段 | **DR-DM1** |
| 004 | thermal warning threshold 之門檻值與單位 | **查得**：`1.11.2.2 DCSD Display Hot Behavior {4820281}`，另 `1.15.1.5 {4820659}` / `1.15.2.5 {4820937}` / `1.15.4.x` 為各架構之對應節 | 含數值+單位 0 段 | 記章節，不開 DR |
| 005 | thermal protection 之 critical 判準與回復條件 | **查得（同上節）**：Hot → non-Hot 之回復敘述與 DTC 清除在同節 `{4820281}` | 含數值+單位 0 段 | 記章節，不開 DR |
| 006 | popup priority arbitration 之優先序規則與 timeout | 命中 70 段，惟皆為「high priority Rear View Camera screen」之個別語句；無仲裁順序表、無 timeout 值 | 命中 6 段，含數值+單位 0 段 | **DR-DM2** |

> 004/005 之章節為**位置登記**，非值之確認。門檻值之讀出與採用屬 Phase 2，
> 依 R-DM8 不得由本輪回填（canon §8.4.1）。
