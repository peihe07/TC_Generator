# 下放包 12 — R-TM62 之射程量測：45% 被引用物件為 Atl-Mid 專屬

分析層 → 執行層。往返編號 `12`。對應上繳 `docs/upstream/12_scope.md`。

Pei 於 2026-08-22 裁「`TLM_MANAGED_TIME_DATE_*` 視為不適用於 Atl-H」。
**分析層量測其射程後，發現該裁定之邏輯若一致適用，影響遠大於五個 LID。**

**本包不逕行擴張該裁定** —— 範圍界定屬 Pei。本包提供量測與選項。

---

## 1. 裁定（射程限於 Pei 明示者）

```
R-TM62（Pei, 2026-08-22）—— TLM_MANAGED_TIME_DATE_* 不適用於 Atl-H

LID 表 `CAN Mapping` 分頁中，五個 `TLM_MANAGED_TIME_DATE_*`
（Hour / Minute / Day / Month / Year）於 Atlantis High 欄（26–30）無值，
僅 Atlantis 欄（16–20）有值。

裁定：該五 LID **視為不適用於 Atl-H**，不寫入本 feature 之任何
訊號斷言，亦不列為 `PENDING`（其非缺件，而是本架構無此對映）。

DR-6b（原擬登記「無 Atl-H 對應者」之缺件）**取消** —— 依本條，
該類非缺件。

**本條之射程限於此五 LID。** 其邏輯是否延伸至 Atl-Mid 專屬之需求物件，
見 A-TM27，待 Pei 另裁。
```

## 2. **射程量測 —— 78 個被引用物件中 35 個為 Atl-Mid 專屬**

CFTS015 之每一物件皆帶 `[EE Architecture:...]` 標籤（269 個物件有標籤）。
分析層以之比對 037 引用之 78 個物件（量測條件：物件行之
`\*\*(\d{7}):.*?\[EE Architecture:([^\]]*)\]` 精確擷取，
逐 leaf 展開 SYS-RA → SYS2 第 5 欄來源物件）：

| EE Architecture 標籤 | 物件數 |
|---|---|
| **Atlantis Mid（專屬）** | **35** |
| Atlantis High（含與 PowerNet / CUSW 併列者） | 40 |
| All | 1 |
| CUSW, Atlantis Mid, Atlantis High | 1 |
| （不在 docx —— A-TM13 之兩筆） | 2 |

**35 / 78 = 45% 之被引用物件標為 Atlantis Mid 專屬。**

### 2.1 逐 leaf 之 Atl-Hi 錨點數（全 22 片，R-TM4：列全集）

| leaf | 總物件 | **Atl-Hi/All** | Atl-Mid 專屬 | 其他 |
|---|---|---|---|---|
| 001 | 4 | 3 | 1 | 0 |
| 002 | 6 | 2 | 3 | 1 |
| **003** | 6 | **1** | **5** | 0 |
| 004 | 6 | 2 | 4 | 0 |
| 005 | 2 | 1 | 0 | 1 |
| 006 | 3 | 3 | 0 | 0 |
| 007 | 4 | 4 | 0 | 0 |
| 008 | 7 | 5 | 2 | 0 |
| 009 | 9 | 9 | 0 | 0 |
| 010 | 2 | 2 | 0 | 0 |
| 011 | 3 | 3 | 0 | 0 |
| 012 | 2 | 2 | 0 | 0 |
| 013 | 1 | 1 | 0 | 0 |
| **014** | 5 | **1** | **4** | 0 |
| 015 | 9 | 5 | 4 | 0 |
| 016 | 2 | 2 | 0 | 0 |
| **017** | 4 | **1** | **3** | 0 |
| 018 | 3 | 1 | 2 | 0 |
| 019 | 3 | 2 | 1 | 0 |
| **020** | 4 | **0** | **4** | 0 |
| **021** | 1 | **0** | **1** | 0 |
| 022 | 2 | 1 | 1 | 0 |

### 2.2 **兩片之 Atl-Hi 錨點為零**

- **020 IPC Synchronization** —— 4 個物件全為 Atl-Mid
- **021 Sleep/Wakeup Handling** —— 唯一物件為 Atl-Mid

若 R-TM62 之邏輯延伸至需求物件，**此二片在 Atl-H 下無任何可引用之
spec 錨點**，其 `specification_reference` 將全部為佔位或空。

### 2.3 **影響 B1 —— 003 在 pilot 批次內**

批次計畫（Part VII）之 B1 為 `001, 003, 006, 007, 008, 010, 012`。
其中 **003 GPS Time Calculation 之 6 個物件有 5 個為 Atl-Mid 專屬**，
僅 1 個 Atl-Hi。

**B1 原設計為「零 A-TM13 曝險」以使 pilot 不被未決項阻塞**
（`03` §3）。**本問題是 A-TM13 之外的第二個未決項，且落在 B1 內。**

### 2.4 與既有兩項觀察之關聯

- **`1.5.3.*`（ETM）零命中**（Part VII 注 4，當時記「與 A-TM09 是否同源
  尚未查證，不主張」）—— 現有部分解釋：037 之引用集中於
  `1.5.2.*`（LTM / Atl-Mid），ETM 之 Atl-Mid 章節整支未被引用
- **A-TM09 之 48 筆缺口** —— 其與本問題**方向相反**：A-TM09 是 SYS2 有而
  037 未引；本問題是 037 引了但架構標籤不符。**兩者不可混為一談**

## 3. 三個選項（**Tier 3，Pei 裁，本包不採任一**）

| | 內容 | 後果 |
|---|---|---|
| **(a)** | R-TM62 射程**僅限五 LID**，Atl-Mid 專屬之需求物件仍可引用 | 現狀不變；但工作簿會引用標為 Atl-Mid 之物件，審閱者可能質疑 |
| **(b)** | 延伸至需求物件：Atl-Mid 專屬物件**不得引用**，其對應之驗證點亦不寫 TC | 020 / 021 兩片無錨點；003 / 014 / 017 之覆蓋大幅縮減；B1 須重排 |
| **(c)** | 延伸至引用但**不縮減 TC**：TC 照寫，Atl-Mid 物件之引用改為 `PENDING: DR-11 Atl-H 對應需求` | 缺口可見且可追；但若上游確認 Atl-H 本就無此需求，該 DR 永遠無解 |

**分析層建議 (c)，理由三點**：

1. (b) 之「無錨點即不寫 TC」等於由分析層認定該需求在 Atl-H 不存在 ——
   而 037 引用了它，即 SWE.1 認為它在範圍內。**推翻上游之範圍判斷
   不是本層之權限**（§8.2「TC 作者不得重新分解 RD 項目」之同一精神）。
2. (a) 之風險是靜默的：工作簿引用 Atl-Mid 物件而無任何標記，
   審閱者若發現，我方無法說明為何引用不適用之架構。
3. (c) 使問題**可見且歸屬明確** —— TC 覆蓋不縮減（不擅自砍範圍），
   而架構不符之處以 DR 標出，答案在上游。與 A-TM13 之處置同型
   （不寫偽值、不留空、寫佔位）。

**若採 (c)**，B1 之 003 可照原計畫生成，其 5 個 Atl-Mid 引用寫佔位 ——
**pilot 反而因此成為該處置形式之首個驗證樣本**。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM62

`## R-TM62 — TLM_MANAGED_TIME_DATE_* 不適用於 Atl-H`，內文為 §1 之區塊。
**增量**：`## R-TM` **+1**；`## A-TM` **+1**（A-TM27，見 T2）；`## G-TM` **0**。

### T2 — `ANOMALIES.md`：新增 A-TM27

```markdown
## A-TM27 — 45% 被引用物件標為 Atlantis Mid 專屬

**狀態：PENDING。Tier 3 —— 範圍界定，待 Pei（三選項見下放包 12 §3）。**

CFTS015 之 269 個物件帶 `[EE Architecture:...]` 標籤。037 引用之 78 個
物件中，**35 個（45%）標為 Atlantis Mid 專屬**，本 feature 為 Atl-H。

兩片之 Atl-Hi 錨點為零：
  020 IPC Synchronization —— 4 個物件全為 Atl-Mid
  021 Sleep/Wakeup Handling —— 唯一物件為 Atl-Mid

三片之 Atl-Hi 錨點 ≤ 1：003（1/6）、014（1/5）、017（1/4）。

**影響 B1**：003 在 pilot 批次內，其 6 個物件有 5 個為 Atl-Mid 專屬。

**與 A-TM09 方向相反，不可混為一談**：A-TM09 是 SYS2 有而 037 未引；
本條是 037 引了但架構標籤不符。

逐 leaf 全表見下放包 12 §2.1。
```

### T3 — 逐物件明細表（供 Pei 裁定用）

產出 `data/ee_architecture_by_leaf.tsv`，欄位：

```
leaf | sys_ra | object_id | ee_architecture | is_atl_hi | section
```

涵蓋全 78 個被引用物件（R-TM4：列全集）。
`is_atl_hi` 判準：標籤含 `Atlantis High` 或等於 `All` → True。

**須對 `inputs/` 之原始 docx 重測**，與 §2 之數字對差
（78 總數、35 Atl-Mid、40 Atl-Hi、1 All、1 三者併列、2 不在 docx）。
不符即回報並停。

### T4 — `11` 之 T3 依 R-TM62 調整

`11` 尚未上繳。**執行順序：先跑 `11`，再跑本包**（依 R-TM20 聲明：
`11` 未上繳，本包之 §2 量測不依賴 `11` 之產物，兩者互不相依）。

**惟 `11` 之 T3 須依 R-TM62 調整**：五個 `TLM_MANAGED_*` LID
不再列為「Atl-H 欄無值 → PENDING」，改列為 **`N/A (R-TM62)`**。

### T5 — 驗證

```bash
grep -n '^## R-TM62' features/time_management/RULINGS.md
grep -n '^| A-TM27' features/time_management/ANOMALIES.md
wc -l features/time_management/data/ee_architecture_by_leaf.tsv    # 期望 79（含表頭）
grep -c 'Atlantis Mid' features/time_management/data/ee_architecture_by_leaf.tsv
grep -n 'N/A (R-TM62)' features/time_management/data/lid_atlantis_high.tsv
```

### T6 — 上繳

`docs/upstream/12_scope.md`。依 R-TM54 三分列未驗清單。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**（B1 待 A-TM27 裁定）
- **不採 §3 之任一選項**（Tier 3）
- **不將 `TLM_MANAGED_*` 列為 PENDING**（R-TM62：非缺件）
- 不自 Powernet / CUSW / Atlantis / Compact 欄取值（A-TM26）
- 不改 `backend/`、canon、`docs/fw036/framework.md`
- 不碰 `features/vehicle_setting/`

---

## 5. 呈報 Pei —— 一個決定，影響 B1

**A-TM27：037 引用之 78 個物件中 35 個標為 Atlantis Mid 專屬（45%）。**

你裁 TLM LID 不適用於 Atl-H，該邏輯若一致適用於需求物件，
**020 與 021 兩片將無任何 spec 錨點**，003 / 014 / 017 之覆蓋大幅縮減，
而 **003 在 B1 pilot 批次內**。

三個選項見 §3。**我建議 (c)**：TC 照寫不縮減範圍，Atl-Mid 物件之引用
改為 `PENDING: DR-11 Atl-H 對應需求`。

理由是 (b) 等於由我方認定該需求在 Atl-H 不存在 —— **而 037 引用了它，
即上游認為它在範圍內。推翻上游的範圍判斷不是這一層的權限。**
(a) 的風險是靜默的：工作簿引用了不適用架構的物件而無任何標記。

**若採 (c)，B1 可照原計畫生成**，003 的 5 個 Atl-Mid 引用寫佔位，
pilot 順帶成為該處置形式的首個驗證樣本。

其餘待你：RD-1 送出、A-TM25（引號與 check whether）、常數表 v3 過目。

## 6. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM62 | 裁決（Pei），TLM LID 不適用 | §1 | ✅ T1 |
| A-TM27 | anomaly，PENDING，Tier 3 | §2 | ✅ T2 + T3 |
| DR-6b 取消 | 依 R-TM62，該類非缺件 | §1 | ✅ T1（隨 R-TM62 條文）|

分析層本包未動 git、未改任何腳本、未擴張 Pei 之裁定射程。
§2 之量測跑在沙箱複本，T3 為對 `inputs/` 之重測。
