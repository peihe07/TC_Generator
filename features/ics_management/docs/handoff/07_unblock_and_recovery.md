# 下放包 07 — 取代 06：解封、佔位回收、005／009／scroll／tune 生成（2026-08-29）

## §0 本包取代下放包 06

**下放包 06 作廢**（`docs/handoff/06_placeholder_recovery_and_unlock.md` 保留不刪，
標題不改；其作業內容併入本包並刷新）。理由：其 §0 前提、§2 裁決引用、§5 預期數字
於 b06 停工期間全部偏移。**執行層不得再依 06 執行任何作業。**

**b06 之 E1 停工判為正確**：一項作業未動、一個檔未寫、未自改工具而上報 —— 合式，
已記於 R-ICS29(e)。成因為分析層之誤（A-ICS45），非執行層。

### 本輪分析層之寫入（R-ICS26(b) 之具名義務）

自 upstream-05 審結至本包落檔，分析層寫入 `scope` 檔如下：
- `RULINGS.md`：R-ICS23 改題為 `v1` ＋ 新增 `R-ICS23 v2`、`R-ICS26`、`R-ICS27`、`R-ICS28`、`R-ICS29`、`R-ICS30`
- `ANOMALIES.md`：A-ICS37～A-ICS45
- `DATA_REQUESTS.md`：加檔頭 R-ICS29 說明、催件排序重排、過渡表以 `LEDGER-IGNORE` 包覆

### 前提（量測時點 2026-08-29 17:0x）

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：相異 ruling_id **30**、錨點總數 **33**（`R-ICS2`／`R-ICS22`／`R-ICS23` 三者各 v1／v2） | `ledger_guard.py` |
| P2 | `ANOMALIES.md` 至 **A-ICS45**；`DATA_REQUESTS.md` 主登記表 **17 列、相異 17、無缺口** | 同上 |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | `inputs/` 含 CFTS022 `…26PI2.5 Jun Release-Privacy…20260608-1205.docx` 與 CFTS020 `…26PI1.5 Mar Release-Cabin…20260310-1533.docx` | `ls` ＋ sha256 |

**P1 之數字為分析層自算，未經工具驗**（作業 A 完成前 `ledger_guard` 之掃法仍有缺）。
與實測不符時**以實測為準並具名**，不視為停工事由。

開工序：① 重測本檔 sha256；② **先做作業 A**（修掃法）；③ 再跑 `ledger_guard`（E1）。
**這是本包唯一允許「閘紅著動工」的情形，且僅限作業 A 本身**——依 R-ICS29(c)，
掃法之改動為裁定後之實作。

## §1 禁區

沿下放包 05 §1，並補：
- **不得以 `<Tpress> = 500 msec` 組出短／長按 TC**（R-ICS24(d)）。
- **R-ICS22 v2 之先決問題（ETM = DUT）未驗前，不得改寫 `$TGW_DISP_STAT$` 佔位**。
- **不得引用 §1.5.1／§1.11.1／§1.14.1 之定義塊**，只得用 `4819541`（R-ICS27(a)）。
- 009 之 TC 須載 Market 限 NAFTA 及在案依據（R-ICS25(b)）。
- **改 `ledger_guard.py` 僅限作業 A 所令之掃法**；不得順手改其他判準。

## §2 裁決引用

R-ICS29（作業 A）、R-ICS27（作業 B）、R-ICS22 v2（作業 C）、R-ICS25（作業 D）、
R-ICS30(a)（作業 E）、R-ICS28（作業 G）、R-ICS12(b)(c)（作業 F）、R-ICS21(c)（作業 H）、
R-ICS2 v2（全部適用性判定）、R-ICS23 v2（短長按之成因分類）。
sha8 不符時依 R-ICS19(b) 先取圍籬 diff。

## §3 作業清單

### 作業 A — `ledger_guard.py` 掃法修正（解封，最先做）

依 R-ICS29(c)(d)：先剔除 `<!-- LEDGER-IGNORE-BEGIN -->`～`<!-- LEDGER-IGNORE-END -->`
之區塊，再取登記列；正則須能辨識合併列（`| DR-ICS2、3、4 |`）並**不計入**。
改後對 `DATA_REQUESTS.md`／`ANOMALIES.md` 各跑一次，預期 exit 0。
**檔頭 docstring 同步更新**（現行 docstring 自稱「只掃登記表首格」而實作為全檔，
該不一致本身即本次事故之根）。

### 作業 B — 符號值佔位回收（R-ICS27）

錨 `CFTS020-4819541`。DR-ICS10 2 處 → `120 seconds`；
DR-ICS12 4 處 → `50 msec`／`20 msec`。reasoning 須載「initial value、
可於整合測試後變更」（僅 `50 msec`）。錨行增 `CFTS020-4819541`（並列、升序）。
**另**：依 R-ICS27(e) 對 CFTS020 全文掃同類「節前定義塊」（不限時間符號），出清單。

### 作業 C — `$TGW_DISP_STAT$` 12 處（R-ICS22 v2）

先驗 `ETM = DUT`（SYSAD／SWRA／LID 三路交叉，逐路寫出所據）。
不成立即停並報，佔位維持（E3）。成立則改
`$TELEMATIC_FD_4.TGW_DISP_STATSts$`，B-CAN 側記 `fallbacks`。
v1(b)(c) 不變：ER 主錨仍為 HMI 現象、不得書為「HU／ICS 收到」。

### 作業 D — 005／009 生成（R-ICS25）

005 → `Volume Control`，上半取 `CFTS022-4914993`；訊號 `$CLIMATIC_PANEL.Radio_btn4$`。
009 → `Menu Navigation`，上半取 `CFTS020-4819554`；訊號 `$CLIMATIC_PANEL.Radio_btn3$`。
009 之 reasoning 必載 Market 限 NAFTA 與在案依據；4819554 之 Enter 側已由 N1 承擔，
本批只驗 Back 側並註明分工（IN §8.2.1）。

### 作業 E — scroll／tune 補生成（R-ICS30(a)）

錨 `CFTS020-4819586`，Test Set `Browse Control`，trace `SWE-ICS-004`。
三操作各至少一條（browse 已有 B6，本批補 scroll／tune）；
畫面對應以 `PENDING: DR-ICS6 <…>` 承載。**不得以 DR 未回為由不生成。**

### 作業 F — CFTS022 改綁與覆驗（R-ICS12(b)(c)）

綁定改指本 feature `inputs/…26PI2.5…`，sha256 自算；privacy 之綁定不動。
覆驗 b01／b02 之 4 句 verbatim（4914956／57／75／76）與 7 物件屬性
（含 4914958／74、4914993）於新版之逐字。不符即停並報（E4）。

### 作業 G — 出貨閘之未錨定斷言檢查（R-ICS28(b)）

對全批每條 TC 之每一行 ER，判其能否指回已錨來源句或已登之 A-。
二者皆無者列為**未錨定斷言**並具名。此為人工判，逐條記於
`docs/reports/07_pre_delivery_check.md`（取代 05 之體檢報告，舊檔保留）。
V1／V2／V3 之 popup 6 行已登 A-ICS16，須明列於該報告之「已標明」節。

### 作業 H — Notifications 偵察（DR-ICS17）

`spec-index/sources/Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf`：
頁數、文字層、sha256；是否即 `Pop-up List Notification`（**只列證據不判同一**）；
`VOLUME POP_UP`／`volume` 之命中（去連字號＋壓平二式，A-ICS32）。
命中亦**不充 verbatim 來源、不充錨**（R-ICS21(c)）；觸 E5 則停下待納源裁定。

## §4 掃描條件

沿 upstream-05 §0 全部。另：符號一律搜 `<符號>` 與 `<符號>\s*=` 二式（R-ICS24(f)）；
DBC `latin-1`、邊界由下一個 `BO_`（A-ICS25）；PDF 去連字號＋壓平（A-ICS32）；
佔位以 `pending_census.py` 計數（A-ICS31）；台帳掃描依作業 A 之新掃法。

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | 作業 A 後 `ledger_guard` | exit 0；DR 登記 17／相異 17、A-ICS 45／相異 45 |
| 2 | 錨點 | 相異 30、總數 33（分析層自算，以實測為準） |
| 3 | DR-ICS10 佔位 | 2 → 0 |
| 4 | DR-ICS12 佔位 | 4 → 0 |
| 5 | `$TGW_DISP_STAT$` | 先決成立 → 12 → 0；不成立 → 12 不變並停報 |
| 6 | 005 之 TC | ≥ 1 |
| 7 | 009 之 TC | ≥ 1 |
| 8 | scroll／tune 之 TC | ≥ 2 |
| 9 | Test Set 相異值 | **5，不變** |
| 10 | CFTS022 覆驗 | 4 句 ＋ 7 物件全數相符；不符即停 |
| 11 | 未錨定斷言 | 逐條有判；已標明者與未標明者分列 |
| 12 | 作業 H | 一節；TC 新增 0 |
| 13 | 節前定義塊掃查 | 出清單；筆數不預設 |
| 14 | `ledger_guard` 完工後 | exit 0；與作業 A 後之基線比對，差異依 R-ICS26(a) 處理 |
| 15 | 四支 gate | 差皆 0 |

## §6 升級條件

- **E1**：作業 A 完成後 `ledger_guard` 仍 exit 1 → 停，回報其內容。
- **E2**：定義塊多物件值不一致或無一適用 → 停，佔位維持。
- **E3**：`ETM = DUT` 三路交叉不成立或互相矛盾 → 停，12 處佔位維持。
- **E4**：CFTS022 新版覆驗任一不符 → 停並報（既有 TC 回收屬 Tier 3）。
- **E5**：作業 H 發現該本即所指文件且載有 popup 顯示條件 → **不得逕用**，停下待納源裁定。
- **E6**：作業 G 發現 A-ICS16 以外之未錨定斷言 → 具名列出，**不自行刪改該 ER 行**。
- **E7**：任一作業須改動禁區所列之檔。

## §7 上繳要求

1. 沿 upstream-01～05 體例；§0 含本檔重測 sha256，並具名 06 已作廢。
2. §1 列 R-ICS1～R-ICS30 全部 sha8（`R-ICS2`／`R-ICS22`／`R-ICS23` 各 v1／v2 並列）。
3. 附 `ledger_guard` 作業 A 後與完工後二次實跑輸出（**開工前那次因 E1 已知紅，照列**）。
4. §預期數字逐項對 §5 之 15 項，相符者亦列。
5. §DR 狀態實測表：對主登記表 17 列逐條回報，標「可結」者是否確已回收其全部佔位。
6. §獨立判斷：續答「若剩餘上游 DR 無回覆，哪幾條可現狀出貨」，以本包後之實況更新；
   並回答——**作業 G 之未錨定斷言檢查，是否應成為每包必跑之常設項**。
