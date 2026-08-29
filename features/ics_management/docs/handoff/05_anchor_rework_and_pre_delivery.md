# 下放包 05 — 佔位補齊、Display ER 主錨改寫、Volume 收尾（2026-08-29）

## §0 背景與量測時點

upstream-04 已審結，b04 七條收下。分析層即裁 **R-ICS22／R-ICS23**，
登 **A-ICS28～A-ICS33**，新開 **DR-ICS16／DR-ICS17**。

**前提量測時點 2026-08-29 15:3x。** 執行前依 R-DD26 v2(f) 先驗。

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：相異 ruling_id **23**、錨點總數 **24**（`R-ICS2` v1／v2） | `ledger_guard.py` |
| P2 | `ANOMALIES.md` 至 **A-ICS33**；`DATA_REQUESTS.md` 至 **DR-ICS17**，17 條全開 | `ledger_guard.py` |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | `ledger_guard.py` |

開工第一件事：重測本檔 sha256 入 upstream-05 §0；第二件事：跑 `ledger_guard.py`（E1）。

**本包不新增 TC 面**——全為既有 23 條之補正與收尾。

## §1 禁區

沿下放包 04 §1 全部八項。特別重申：
`$TGW_DISP_STAT$` 之 12 處佔位**維持**，不得自選匯流排（R-ICS22(a)）；
009／005 之 TC 仍為 0；`<Tpress>`／`<TPeriodToSendNoChange>`／`SIS-5161` 不臆值；
**不得以「ICS 收得到此訊號」書寫任何 ER**（R-ICS22(c)）。

## §2 裁決引用（sha8 執行層實測；不符時依 R-ICS19(b) 先取圍籬 diff）

R-ICS22（作業 A／B）、R-ICS23（作業 C／D）、R-ICS18（引號例外之範圍）、
R-ICS8(d)／R-ICS13（訊號值書寫）、R-DD3 同族（ER 錨層級）。

## §3 作業清單

### 作業 A — b03 八條之 ER 主錨改寫（R-ICS22(b)）

1. 八條之 ER：**HMI 可觀察現象為主錨**（螢幕亮／滅、背光態、
   `TOUCH SCREEN TO TURN ON` 之顯示），訊號面降為輔助觀察行。
   主錨行須能單獨判定通過與否；訊號行為佐證，缺之不影響判定。
2. 每條之 `reasoning` 增一句：明載訊號面為輔且 `$TGW_DISP_STAT$` 現為佔位
   （**不得以外觀上之完整掩蓋驗證強度**）。
3. 已解之 `$RADIO_B3.RQ_DISP_INTS$` 三處：觀察位置改書為
   匯流排追蹤（CAN trace），**不得書為「HU／ICS 收到」**（R-ICS22(c)）。
4. 12 處 `$TGW_DISP_STAT$` 佔位**維持不動**。

### 作業 B — 佔位補齊（R-ICS23(b)）

`b04` 之 B1／B2：`pre_conditions` 各增
`PENDING: DR-ICS12 <no-change resend period>`。
其餘欄位不動；`b04_tcs.json` 就地修訂，`manifest.json` 重算。

### 作業 C — 佔位數之口徑統一（A-ICS31）

1. 全批（b01～b04，23 條）之佔位以腳本重新計數，逐 DR 分列。
2. 四份 `manifest.json` 之 `counts.pending_placeholders` 一律改為腳本值；
   `b03/manifest.json` 之 `counts_correction` 欄**保留**（不刪，回溯用）。
3. 上繳包列出「每個 DR 各阻幾處佔位、涉幾條 TC」之對照表。

### 作業 D — 短長按缺口之記錄（R-ICS23(a)）

不改 N1 之內容。於 `docs/reports/05_coverage_gaps.md` 新建覆蓋缺口清單，
首筆為 A-ICS33（短按／長按定義缺口），格式含：
缺口描述、所缺母條之位置與其排除原因（`[ECU:FPDM]`）、
受影響之 TC、對應 DR。**不得以 FPDM 條文充當**。

### 作業 E — 全批 lint 與交付前體檢（不改內容，只出報告）

23 條跑一次完整體檢並出 `docs/reports/05_pre_delivery_check.md`：
Test Set 分佈、priority 分佈、trace 覆蓋（哪些 RD 已有 TC、哪些沒有）、
佔位分佈、`specification_reference` 之錨分佈（CFTS020／CFTS022 各幾條）、
以及**每條 TC 之驗證強度自評**（強：主錨可獨立判定；弱：主錨依賴未解之佔位或
以「不變」承載）。弱者逐條具名——B3（「VAL 被忽略」以畫面不變承載）
與 V1／V2／V3（popup 顯示條件未載，A-ICS16）已知，其餘由實測補。

## §4 掃描條件

沿 upstream-04 §0 全部條件。另：
佔位計數一律 `re.findall(r'PENDING: (DR-ICS\d+) <([^>]+)>')` 對六欄，禁人工列舉；
PDF 偵察若再發生，須同時做去連字號重掃與**壓平重掃**（A-ICS32）；
DBC 一律 `latin-1` 開檔、邊界由下一個 `BO_` 判定（A-ICS25）。

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；錨點 24（相異 23）、A-ICS 33、DR-ICS 17 |
| 2 | TC 總數 | **23，不變**（本包不新增） |
| 3 | b03 八條之 ER | 主錨皆為 HMI 現象；訊號行皆標為輔 |
| 4 | `$TGW_DISP_STAT$` 佔位 | **12，不變** |
| 5 | 新增佔位 | 2 處（B1／B2 之 DR-ICS12） |
| 6 | 全批佔位總數 | 21（19 ＋ 2）；以腳本計數為準，不符即以腳本值為真並具名 |
| 7 | manifest 修訂 | 4 份；`b03` 之 `counts_correction` 保留 |
| 8 | 覆蓋缺口清單 | ≥ 1 筆（A-ICS33） |
| 9 | 驗證強度自評 | 23 條逐條有評；弱者逐條具名 |
| 10 | `ledger_guard` 完工後 | exit 0，與開工前逐字相同 |
| 11 | 四支 gate | 差皆 0；`lint_paths` 基線外 2（皆 `driver_distraction`） |

## §6 升級條件

- **E1**：`ledger_guard` 開工前報 DUPLICATE／INCONSISTENT → 停。
- **E2**：作業 A 改寫後，某條之 HMI 主錨無法獨立判定（即該條之驗證完全依賴訊號面）
  → 該條具名回報，**不得以佔位充主錨**。
- **E3**：作業 C 之腳本計數與各 manifest 之差異 > 2 處 → 停下逐份核對後再改。
- **E4**：作業 E 之強度自評顯示有 TC 之主錨依賴未解 DR → 具名列出，不自行降階或刪除。
- **E5**：任一作業須改動禁區所列之檔。

## §7 上繳要求

1. 沿 upstream-01～04 體例；§0 含本檔重測 sha256。
2. §1 列 R-ICS1～R-ICS23 全部 sha8（`R-ICS2` v1／v2 並列）。
3. 附 `ledger_guard` 前後二次實跑。
4. §預期數字逐項對 §5 之 11 項，相符者亦列。
5. §獨立判斷須回答：**23 條之中，若上游 17 條 DR 全部無回覆，哪幾條可以現狀出貨、
   哪幾條不能**——逐條給判與理由。這是交付面的問題，不是技術面的。
