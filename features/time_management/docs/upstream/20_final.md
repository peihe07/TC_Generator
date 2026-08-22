# 20 上繳 —— 收尾包：架構更正落實、四批重生成、寫回就緒

執行層，2026-08-22。對應下放包 `docs/handoff/20_final.md`
（合併 `18` 架構更正與 `19` HMI 標籤之未執行指令）。

---

## 0. 逐 T 項對照表（R-TM74）

| T 項 | 內容 | 狀態 | 備註 |
|---|---|---|---|
| **T0** | `cd` 專案根 | **完成** | — |
| **T1** | `18` T1–T3 + `19` T1–T3 之條文落檔 | **完成** | 見 §1 |
| **T2** | 工具連動（`18` T3 五項） | **完成** | 見 §2；自驗 57 → 53（見 §2.4） |
| **T3** | B1–B3 重生成 | **完成** | 見 §3；**B4 一併，見 §3.4** |
| **T4** | DR-12b 記號 | **完成** | 23 條 |
| **T5** | DR-12 之值寫入 | **完成** | 1 處 |
| **T6** | B4 生成 | **不適用 —— 已於 `17` 完成** | 8 條；本包依新架構規則一併轉換（§3.4） |
| **T7** | 全批驗證 | **完成** | 見 §5 |
| **T8** | 上繳 + dry-run 就緒檢查 | **完成** | 本檔；**dry-run 抓到一項會毀掉交付件的錯，見 §6** |

**未做者：無。不適用者：T6（前包已完成）。**

**增量（R-TM46）**：`## R-TM` 標題 **74 → 78**；**但實際條文為 80** ——
R-TM62 / R-TM63 依 R-TM13 改為刪除線標題（`## ~~R-TM62 …~~`），
不再匹配 `^## R-TM`。**增量檢查須知此差異**，否則會誤判為 +4 而非 +3。
`## A-TM` **27 → 28**；`## G-TM` **0**（3）。

---

## 1. T1 —— 條文落檔

### 1.1 `18`：R-TM75 / 76 / 77 與四項撤回

R-TM62 / R-TM63 之標題改為 `## ~~…~~ **已撤回**` 並於其下加引述框指向
R-TM75，原文全部保留（R-TM13）。A-TM27 之結論作廢段、A-TM26 之訂正段
皆已追加，**事實記載一律保留**。

DR-11 標 **CANCELLED**，理由逐字為 R-TM75(2)，**該列未刪**。

### 1.2 `19`：新版 HMI Settings List 與 A-TM28

新版已落 `inputs/`，SHA256 與來源一致。舊版標 **SUPERSEDED**（未刪）。
DR-12 → **RESOLVED**；DR-12b 與 A-TM28 已登記。

### 1.3 **素材來源有兩份同名檔案，內容不同**

```
26PI1.5/HMI/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026) .xlsx   294,199 B
26PI2.5/HMI/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx    295,635 B
                                            ↑ 前者檔名多一個尾隨空格
SHA256 相異。
```

**執行層取 `26PI2.5`**（PI 版本較新），並實測**兩份之 §7 Clock 節逐列
完全相同** —— 故本次全部結論不受選擇影響。此事已記入 `DATA_REQUESTS.md`
之 DR-21，因日後若引用該檔他節，兩份之差異須先釐清。

### 1.4 `19` T5 之逐字複驗 —— 六項全符，停止條件未觸發

五個標籤逐字相符、三組值域相符、7-5 與兩個 CFTS022 項相符、
§7 標題附註全文相符、三種區域排序與子項序相符。

**§4(4) 之截斷註記全文取得**（原文有 typo `Set Dateis`）：

```
"(DD/MM/YY)" is dynamic and should update to current date
[NOTE:  Set Dateis only shown for vehicles in which the cluster does not
have data needed to reference date]
```

**其為 015 之顯示前提**，與 4814000（`If the HU has No GPS, the HU shall
provide a manual method…`）同向。B4 之 015 現行 TC 未含此前提 ——
**列入未驗清單 A 區**（本包指令未指派其寫入）。

---

## 2. T2 —— 工具連動

### 2.1 架構模型：二值 → 三值

`is_atl_hi`（True/False）改為 `arch`（`Atlantis High` / `Atlantis Mid` /
`Both`），由 `arch_of_tag()` 依標籤逐字判定。tsv 之原欄保留為
`is_atl_hi_legacy`（軌跡），**不再由其判定適用與否**。

`lid_columns_for(arch)` **一併回傳欄號與記錄字樣** —— 使兩者不可能分離
（記了 26-30 卻取 16-20 之類）。

### 2.2 **LID 表重建為兩架構，且三態須分辨**

`data/lid_by_arch.tsv`：19 LID × 2 架構 = 38 列。舊檔保留為軌跡。

**實測三態分佈**：

```
有訊號有網段  19
有訊號無網段  11   ← 全部在 Atlantis Mid 側
無訊號         8
```

**`18` §5 T4 稱「`$DateTmHour$` 在 Atl-Mid 為 `TIME_DATE.Hour1` on CAN-B」
—— 訊號名正確，`on CAN-B` 無來源。** 實測該 LID 之 Atl-Mid 側
SignalName 有值（`TIME_DATE.Hour1 / TIME_DATE.Hour2`）而 **CAN 欄為空**。

Atl-Mid 側僅 6 個 LID 有網段（`GPSDateTmSecond` 與五個 `TLM_MANAGED_*`，
皆為 `CAN-B`），其餘 11 個**有訊號而網段未載**。

**故 DR-6（CAN 網段依據）對 Atlantis Mid 未解除。** 三態分開處置：
無訊號 → 不寫任何斷言；有訊號無網段 → 訊號可寫、segment 寫 DR-6 佔位；
有值 → 照用。**合併二者會使處置錯誤**（前者不該寫，後者該寫而標缺件）。

### 2.3 `Both` 之處置

跨架構之片取 Atl-Hi 欄為基準值，並在每個訊號帶
`cross_arch_note`：「本片跨兩架構；此為 Atlantis High 之值。
Atlantis Mid 之 MESSAGE 與 segment 不同 —— 若該 TC 之斷言涉此訊號，
須加架構限定或拆分為兩條。」

**不逕自合併兩架構之值** —— 同一 LID 在兩架構之 MESSAGE 與 segment 不同，
合併會產出一個兩邊都不對的值。

**017 為此情形之實例**：其 4 個物件中 3 個為 Atl-Mid，target 判為 `Both`，
故 TLM LID 取 Atl-Hi 欄而該欄無訊號 → 標 `excluded` 並附跨架構註記。
**該片之 Atl-Mid 部分若需 TLM 斷言，須拆為架構限定之 TC** ——
列入未驗清單。

### 2.4 lint：三處改動，**自驗 57 → 53**

| 閘 | 改動 |
|---|---|
| `lint_arch`（DR-11 判準） | **整個移除**（R-TM75(1)） |
| `lint_arch_column` | 由「有無記錄架構欄」改為「**記錄之架構欄須與 Pre-Condition 之架構限定行一致**」 |
| `lint_placeholder_completeness` | 應有集合移除 Atl-Mid 項；**殘留之 DR-11 佔位改為須報** |

**自驗數下降是移除過時案例所致，非能力下降**：
`lint_arch` 之 4 項、`lint_arch_column` 舊判準之 4 項、R-TM69(2) 逐 TC 之
3 項共 11 項移除，新增 5 + 2 = 7 項。

**一律移除而非改期望值** —— 留一個永遠不報之案例會在每次自驗顯示 PASS，
使人以為該面向仍受檢（`17` §2.3 同一理由，本包第二次適用）。

### 2.5 `lint_arch_column` 之新判準與 R-TM75 之成因直接相關

舊判準只驗「reasoning 有記錄架構欄」。而 `11`–`17` 九輪中**每條 TC 都記了
`Atlantis High (col 26-30)`** —— **記錄完備，而記錄的內容整整九輪都是錯的。**

該判準之射程限制（只驗記錄存在、不驗記錄正確）先前已寫入 docstring
（`14` §1.2），本次即為其實例化。**新判準改驗「記錄與該 TC 之架構限定
是否一致」**，紅綠五項全通過。

---

## 3. T3 —— 四批之轉換

### 3.1 方式：**依新規則轉換既有 TC，非從零重寫**

下放包 §3 稱「重生成」。**執行層採「依新規則轉換」**，理由：

1. §3(4) 要求 `14` 之四項修正在重生成後仍成立 —— **從零重寫無法保證**，
   那四項是人工判斷之結果（`greyed out` 之收斂尤其）
2. §3(3) 要求 `test_item` 上半逐字不變 —— 轉換可保證，重寫只能事後比對
3. 受影響者為架構相關之四類欄位，**其餘欄位之改動皆為回退風險**

**實質等同重生成**：受影響欄位全部依新規則重出（佔位→真值、
Pre-Condition 架構行、訊號 MESSAGE/segment、reasoning 架構欄記錄）。

`.pre-arch.json` 四份已保留，**未覆蓋、未刪除**。

### 3.2 §3(3) 之五項回報

| 項 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|
| 條數 | 19→19 | 16→16 | 14→14 | 8→8 |
| **`test_item` 上半改變** | **0** | **0** | **0** | **0** |
| 佔位轉真值 | 5 | 10 | 6 | 5 |
| 新增架構限定行 | 10 | 6 | 5 | 2 |
| 步驟/ER 改寫 | 1 | 1 | 0 | 0 |

**條數全同 4/4 批；上半 verbatim 改變 0 條（期望 0）。**

轉換統計（跨四批）：佔位改真值 **46 處**、BARE 佔位改真值 **4 條**、
加架構限定行 **23 條**、reasoning 架構欄改寫 33 條、
訊號 MESSAGE 改寫 1 處、segment 改寫 1 處。

### 3.3 §3(4) 之四項複驗 —— **全部仍成立**

```
PASS TC#3 之 greyed out 收斂未回退（未改回 unavailable）
PASS 六條 input_test_data = NA
PASS S1 之 The HU main screen is displayed 已刪
PASS S3 之步驟措辭
```

### 3.4 B4 之處置

**B4 已於 `17` 生成（8 條），本包 T6 標「不適用」。** 但其同受架構更正
影響（5 處佔位轉真值、2 條加架構限定行），故**與 B1–B3 同批轉換**，
並同樣保留 `.pre-arch.json`。

### 3.5 目標架構之分佈（22 片）

```
Both           12 片   （不加限定行）
Atlantis High   8 片   （006 007 010 012 005 016 011 013）
Atlantis Mid    2 片   （020 021）
```

020 / 021 之 `spec_reference` 由 R-TM64 之零真值佔位改為**真值**
（其 Atl-Mid 物件即本專案之引用），且加 Atl-Mid 限定行、
訊號改取欄 16–20。

---

## 4. T4 / T5

**T4 —— DR-12b 記號 23 條**（凡含 `Open the "Clock" settings` 者）。
值照留 `Clock` 不改；Remarks 依 R-TM68 升冪（DR-5 → DR-8/9/10 → DR-12b
→ DR-20）。

**T5 —— DR-12 之值寫入 1 處**（B1 之 007）。該佔位實際落在
`input_test_data` 而非 pre_conditions，故一併依 canon §4.5 改為 `NA`，
UI 操作寫入 Procedure：

```
2. Set "Show Time in Status Bar" to OFF
```

reasoning 註明來源（§7-5，Technical Reference `CFTS015`）
**並明寫不採 §7-7 之兩項**（Technical Reference 為 CFTS022，屬他 feature
範圍，§8.4.2）。

---

## 5. T7 —— 全批驗證

```
lint_tcs --self-test                 53 / 53
build_batch_context --self-test      13 / 13
lint（四檔，不含 .pre-arch 備份）      檔 4；發現 0 項

B1 19 條 / 7 片      B3 14 條 / 5 片
B2 16 條 / 7 片      B4  8 條 / 3 片
                     ─────────────────
                     **57 條 / 22 片**

22 片無遺漏無重複: True（差集為空）
```

### 5.1 佔位總數 **78 → 49**（實測，非估計）

```
PENDING: DR-12b   23      設定頁名（本包新增之記號）
PENDING: DR-10    10      GPS 位置與訊號可用性
PENDING: DR-20     9      注入無效訊號
PENDING: DR-5      4      CFTS015 缺件物件（A-TM13）
PENDING: DR-8      1      ECU 軟體重置
PENDING: DR-9      1      CAN sleep 之終止條件
PENDING: DR-6      1      CAN 網段依據（**Atl-Mid 側未解除**，§2.2）
                  ──
                  49
```

**`PENDING: DR-11` 殘留 0**（期望 0）。

**扣除本包新增之 DR-12b 23 處，實際降幅為 78 → 26**。
其中設備類（DR-8/9/10/20）21 處為問測試團隊當天可解者，
真正卡在上游文件者僅 **DR-5 四處 + DR-6 一處**。

---

## 6. T8 —— 寫回就緒檢查（dry-run）

### 6.1 **dry-run 抓到一項會直接毀掉交付件的錯**

首次 dry-run 顯示 `rows : 114 TCs at rows 10-123` —— **應為 57。**

成因：`load_tcs()` 之 glob 讀入了 `.pre-arch.json` 四份備份，
**每條 TC 寫入兩次**。備份是本包依 §3 之指令刻意建立的，
而該指令未提示其會進入寫回路徑。

**同一形態在 lint 亦發生**（39 項發現全來自備份檔），先修 lint 才發現
write_back 亦然 —— **兩處各自 glob，無共用之「待交付物」定義**。

已於兩處排除，並在 `load_tcs` 之 docstring 寫明：排除以**副檔名樣式**
為準而非白名單 —— 白名單須隨批次增減維護，而漏維護之後果是
「少寫一批」，那比多寫一批更難察覺。

`load_tcs` 另加一行輸出 `skipped : N 個軌跡備份 —— …`，
使排除成為可見狀態而非靜默行為。

### 6.2 修正後之 dry-run

```
source        : FM-WI-FSM-036-A01 …_20260817_ext.xlsx
  SHA256      : 6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2
sheet         : 'Test Case Specification 測試用例規範', header row 9
columns       : req_id=D, tc_id=F, test_group=G, test_set=H, test_item=I,
                pre_conditions=J, input_test_data=K, test_procedure=L,
                expected_result=M, spec_reference=N, tc_ref_id=O, priority=P,
                design_method=R, functional_safety=S, author=AA, remarks=AH
skipped       : 4 個軌跡備份 —— B1.pre-arch.json, B2.pre-arch.json,
                B3.pre-arch.json, B4.pre-arch.json
rows          : 57 TCs at rows 10-66
tc_id         : 起點序號 0；本批 NR1L-TimeAndDate-001 … NR1L-TimeAndDate-057
test_group    : 'Time and Date' (fill_test_group_set=True)
blank by decision: C (Polarion ID) — TODO(R-TM10-A1); E (TestRail ID) —
                assigned downstream; O — feature.yaml; Q — TODO(R-TM10-A1);
                T–Z (Vehicle Model) — **R-TM77**（交付件該七欄 189/189 全空）

內容常數        : 全部已決 —— unresolved 為空（R-TM57 / R-TM59）

DRY RUN —— 未寫出任何檔案。
```

**R-TM77 已落實**：T–Z 之理由由 `TODO(R-TM10-A1)` 改為本條之依據。

---

## 7. 未驗清單（R-TM54 三分）

### A. 可驗而未驗

| # | 項目 |
|---|---|
| A1 | **017 跨架構而其 TLM 斷言未寫**（§2.3）—— 該片之 Atl-Mid 部分若需 TLM 斷言，須拆為架構限定之兩組 TC |
| A2 | **015 之顯示前提未寫入**（§1.4 之截斷註記：`Set Date is only shown for vehicles in which the cluster does not have data needed to reference date`） |
| A3 | **DR-6 對 Atlantis Mid 未解除**（11 個 LID 有訊號無網段）—— 現僅 1 處佔位，因多數 Atl-Mid 片未涉該等訊號 |
| A4 | 57 條中 50 條未經獨立覆核；**且 B1 之 pilot 覆核已因架構更正而部分作廢**（其 spec_reference 與 Pre-Condition 已改） |
| A5 | `.pre-arch.json` 與新版之逐欄差異未全量列出（只列五項統計） |
| A6 | `10`–`17` 遺留：G1（讀 CAN 訊號）、G2、G4、PROXI 設定方式、89 筆 docx 無標籤物件、`section` 未交叉驗證 |
| A7 | 07/08/09 遺留六項 |

### B. 待 Pei

| # | 項目 |
|---|---|
| B1 | **寫回之放行** —— `surgical_save` 之寫入路徑至今從未執行 |
| B2 | **A-TM28**（設定頁名 `Clock` / `Clock & Date`）—— 影響 23 條，寫回後改動成本更高 |
| B3 | DR-5（4 處）與設備類（21 處）之上游查詢 |
| B4 | A1 之 017 拆分是否要做 |

### C. 已解決

| # | 項目 | 解決於 |
|---|---|---|
| C1 | 架構範圍誤判（R-TM75） | 本包 T1–T3；DR-11 零殘留 |
| C2 | DR-12（UI 標籤） | `19` + 本包 T5 |
| C3 | 五個 TLM LID 之適用性（R-TM62 撤回） | 本包 T2；改依架構取欄 |
| C4 | T–Z 車型欄（自 `04` 起未裁） | R-TM77 |
| C5 | 22 片之生成 | B1–B4 四批，57 條 |

---

## 8. 未執行者（下放包所禁，逐項確認）

- 未動 git；**未寫回工作簿**（止於 dry-run）
- **未刪除 `.pre-arch.json` 備份**（四份俱在）
- **未刪除 R-TM62 / R-TM63 / A-TM27 / DR-11 之原文**（皆加註保留）
- **未改 `Clock` 之頁名**（A-TM28 未裁）
- **未寫入 CFTS022 之兩項**（§4 已於 reasoning 明寫不採）
- 未建 `tm_constants.py`；未送 RD-1
- 未縮減任何 leaf 之覆蓋；未改寫 test_item 上半之 verbatim
- 未碰 `features/vehicle_setting/`

---

## 9. 提請裁定

1. **§6.1 —— 備份檔進入寫回路徑，由 dry-run 抓到。** 若本包未做 dry-run
   而直接寫回，交付件會有 114 列且每條重複。**建議把「dry-run 必跑」
   寫入寫回程序**，而非視為選用之檢查。
2. **§2.2 —— `18` §5 T4 之 `on CAN-B` 無來源**。Atl-Mid 側 11 個 LID
   有訊號而網段未載，DR-6 對該架構未解除。
3. **§0 —— R-TM 標題計數與實際條文數已分岔**（78 vs 80），
   因撤回條改為刪除線標題。R-TM46 之增量檢查須改為兼計兩種形態。
4. **A1 / A2** —— 017 之拆分與 015 之顯示前提，兩者皆為本包指令未涵蓋
   而實測發現者。
