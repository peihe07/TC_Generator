# 下放包 06 — 佔位回收、005／009 解鎖、CFTS022 改綁、Notifications 偵察（2026-08-29）

## §0 背景與量測時點

分析層自解檢查後，Pei 2026-08-29「准」。新落 **R-ICS22 v2**（v1(a) 作廢、v1 改題）、
**R-ICS24**、**R-ICS25**；登 **A-ICS34／35／36**；`DATA_REQUESTS.md` 增「狀態重排」節。

**前提量測時點 2026-08-29 16:0x。** 執行前依 R-DD26 v2(f) 先驗。

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：相異 ruling_id **25**、錨點總數 **27**（`R-ICS2` v1／v2、`R-ICS22` v1／v2） | `ledger_guard.py` |
| P2 | `ANOMALIES.md` 至 **A-ICS36**；`DATA_REQUESTS.md` 至 **DR-ICS17** | `ledger_guard.py` |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | `inputs/` 含 CFTS022 **26PI2.5**（`…_20260608-1205.docx`）與 CFTS020 **26PI1.5 Mar Release-Cabin**（`…_20260310-1533.docx`） | `ls` ＋ sha256 |

**P4 之注意**：CFTS020 之檔名為 `Mar Release-Cabin`，而下放包 02～05 皆書
`26PI1.5 …`＋`Feb Release` 之近似名——**以實體檔名為準**，並於 upstream-06 §0 具名此差異。

開工第一件事：重測本檔 sha256；第二件事：`ledger_guard.py`（E1）。
**R-ICS22 之 v1／v2 二列須各自實測 sha8 並列**（體例沿 `R-ICS2`）。

## §1 禁區

沿下放包 05 §1 全部；另：
- **不得以 `<Tpress> = 500 msec` 組出短／長按 TC**（R-ICS24(d)：有門檻而無行為）。
- **R-ICS22 v2 之先決問題未驗前不得改寫 `$TGW_DISP_STAT$` 佔位**（v2(c)）。
- 009 之 TC 須於 reasoning 載明 Market 限 NAFTA 及其在案依據（R-ICS25(b)）；
  **不得省略該註**。

## §2 裁決引用

R-ICS22 **v2**（作業 B）、R-ICS24（作業 A）、R-ICS25（作業 C）、
R-ICS12(b)(c)（作業 D）、R-ICS21(c)（作業 E）、R-ICS2 v2（全部適用性判定）。
sha8 不符時依 R-ICS19(b) 先取圍籬 diff。

## §3 作業清單

### 作業 A — 符號值佔位回收（R-ICS24）

1. **先定錨物件**（R-ICS24(e)）：time-variables 定義塊於 CFTS020 出現多次，
   逐次取其 ObjectID 與屬性三軸，依 R-ICS2 v2 定出**適用於本 DUT 之那一物件**。
   **多版本之值不一致時停並報**（E2）。
2. 依該物件回收下列佔位：
   - b02 I1／I2 之 `PENDING: DR-ICS10` 2 處 → `120 seconds`
   - b01 V3 之 `PENDING: DR-ICS12` 1 處、b04 B5 1 處 → `50 msec`（initial value）
   - b04 B1／B2 之 2 處（若 b05 已補）→ `20 msec`
3. **reasoning 須註明 `50 msec` 為 initial value、可於整合測試後變更**（R-ICS24(c)）。
4. 錨行增該定義塊之 `CFTS020-{ObjectID}`（與原有錨並列，升冪）。

### 作業 B — `$TGW_DISP_STAT$` 12 處回收（R-ICS22 v2）

1. **先驗先決問題**：DUT 之 DBC 節點名是否為 `ETM`。
   取 SYSAD／SWRA／LID 三路交叉，逐路寫出所據。
   **不成立即停並報，佔位維持**（E3）。
2. 成立則改寫為 `$TELEMATIC_FD_4.TGW_DISP_STATSts$`，值依 `VAL_` 逐字；
   `TELEMATIC_DISPLAY2` 側記 `fallbacks`。
3. `$Telematic_Power$` 同理（若 b03 有其佔位）。
4. **v1(b)(c) 不變**：ER 主錨仍為 HMI 現象、訊號面為輔；
   不得書為「HU／ICS 收到」（v1(c)）。

### 作業 C — 005／009 生成（R-ICS25）

| RD | Test Set | 上半 verbatim 來源 | 錨 |
|---|---|---|---|
| 005 ICSMuteButton | `Volume Control` | CFTS022-4914993 逐字 | `CFTS022-4914993` |
| 009 Back_Button | `Menu Navigation` | CFTS020-4819554 逐字 | `CFTS020-4819554` |

- 訊號：`$CLIMATIC_PANEL.Radio_btn4$`（Mute）、`$CLIMATIC_PANEL.Radio_btn3$`（Back），
  值依 `VAL_` 逐字（二者皆有列舉，upstream-03 §6）。
- 009 之 reasoning **必須**載 Market 限 NAFTA 與 R-ICS25(a) 之在案依據。
- 4819554 之原句含 `$Enter_Button$` **或** `$Back_Button$` —— 依 IN §8.2.1，
  Enter 側已由 N1 承擔，本批只驗 Back 側，reasoning 須註明該分工。
- 條數不預設；依 partial failure 拆分（IN §8.2.2），差異具名。

### 作業 D — CFTS022 改綁與 b01 覆驗（R-ICS12(b)(c)）

1. `feature.yaml` 之 CFTS022 綁定自 `features/privacy/inputs/…25PI3.5…` 改為
   本 feature `inputs/…26PI2.5…`，sha256 自實體檔算。**privacy 之綁定不動**。
2. **覆驗**：b01／b02 所用之 4 句 verbatim（4914956／57／75／76）與所錨 6 物件
   （另含 4914958／74）之屬性三軸，於新版逐字比對。
   **不符即停並報**（E4，A-ICS13 升級）。
3. 併驗本輪新用之 **4914993**（005 之錨）於新版之逐字與屬性。

### 作業 E — Notifications 偵察（DR-ICS17）

`spec-index/sources/Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf`：

1. 頁數、文字層、sha256。
2. 是否即 `Pop Up List Priority Matrix` p.3 所外指之 `Pop-up List Notification`
   ——**只列證據不判同一**（檔名近似不足以認定；須有內文自稱或結構對應）。
3. `VOLUME POP_UP`／`volume` 之目次與命中頁（**去連字號重掃＋壓平重掃**，A-ICS32）。
4. 命中則列其逐字與所在頁；**不充 verbatim 來源、不充錨**（R-ICS21(c)，納源另裁）。

## §4 掃描條件

沿 upstream-04 §0 全部；另：
符號搜尋一律 `<符號>` 與 `<符號> =` 二式全文搜（R-ICS24(f)）；
DBC `latin-1`、邊界由下一個 `BO_`（A-ICS25）；
PDF 去連字號＋壓平二式（A-ICS32）；佔位以腳本計數（A-ICS31）。

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；錨點 27（相異 25）、A-ICS 36、DR-ICS 17 |
| 2 | 符號佔位回收 | DR-ICS10 2 處 → 0；DR-ICS12 依 b05 是否已補為 2 或 4 處 → 0 |
| 3 | `$TGW_DISP_STAT$` | 先決成立 → 12 → 0；不成立 → 12 不變並停報 |
| 4 | 005 之 TC | ≥ 1 |
| 5 | 009 之 TC | ≥ 1 |
| 6 | Test Set 相異值 | **5，不變**（005→Volume Control、009→Menu Navigation，皆既有組） |
| 7 | CFTS022 覆驗 | 4 句＋7 物件（含 4914993）全數逐字相符；不符即停 |
| 8 | 作業 E | 一節；TC 新增 0 |
| 9 | 全批佔位總數 | 由腳本計；預期大幅降低，具體值不預設 |
| 10 | `ledger_guard` 完工後 | exit 0，與開工前逐字相同 |
| 11 | 四支 gate | 差皆 0 |

## §6 升級條件

- **E1**：`ledger_guard` 開工前異常 → 停。
- **E2**：time-variables 定義塊之多物件值不一致，或無一適用於本 DUT → 停，佔位維持。
- **E3**：`ETM = DUT` 之先決問題三路交叉不成立或互相矛盾 → 停，12 處佔位維持。
- **E4**：CFTS022 新版覆驗有任一句／屬性不符 → 停並報（既有 TC 之回收屬 Tier 3）。
- **E5**：作業 E 發現該本即所指文件且載有 `VOLUME POP_UP` 顯示條件 → **不得逕用**，
  停下回報以待納源裁定（R-ICS21(c)）。
- **E6**：任一作業須改動禁區所列之檔。

## §7 上繳要求

1. 沿 upstream-01～05 體例；§0 含本檔重測 sha256 與 P4 之檔名差異具名。
2. §1 列 R-ICS1～R-ICS25 全部 sha8（`R-ICS2`、`R-ICS22` 各 v1／v2 並列）。
3. 附 `ledger_guard` 前後二次實跑。
4. §預期數字逐項對 §5 之 11 項，相符者亦列。
5. **§須含「DR 狀態實測表」**：對 `DATA_REQUESTS.md` 之「狀態重排」表逐條回報
   ——授權為「可結」者，本包是否確已回收其全部佔位；未回收者具名。
6. §獨立判斷：續答 upstream-05 §7-5 之問（若剩餘上游 DR 無回覆，哪幾條可現狀出貨），
   以本包後之實況更新。
