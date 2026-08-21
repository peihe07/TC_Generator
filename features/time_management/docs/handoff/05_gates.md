# 下放包 05 — scripts/ 解凍，十七項閘門修法

分析層 → 執行層。往返編號 `05`。對應上繳 `docs/upstream/05_gates.md`。

**依 R-TM20 聲明**：`04Z-A5` 尚未上繳。追發理由：Pei 之兩項裁定改變凍結
狀態，`scripts/` 解凍後之修法為全案最大阻塞項，不宜再等一輪。
**執行順序：先跑 `04Z-A5` 之 T1–T5，再跑本包。** 兩者互不相依
（前者為條文與回溯自查，後者為腳本修法）。上繳可合併為一份，分節回報。

---

## 1. 兩項裁定

```
R-TM43（Pei, 2026-08-21）—— A-TM23 之處置

採 (a) + (c)：
(a) 維持 R-TM40 之 7 位家族（SYS2 `Source Requirement items` 欄之值），
    不阻塞 B1。並於交付說明註明本工作簿之 spec_reference 採 7 位物件 id
    家族，與 CFTS015 修訂註記所用之短號家族（CFTS015-732 … -1639）
    不互通。
(c) 於 RD-1 併問上游該參照體系之期望寫法（新增 Q-TM4）。

(b)（改用短號家族）確定不採 —— SYS2 不提供短號，且短號僅 26 個相異值，
涵蓋不到全部 270 個物件。

A-TM23 由 PENDING 轉 **AWAITING_UPSTREAM**（處置已定，答案待 RD-1）。
```

```
R-TM44（Pei, 2026-08-21）—— features/time_management/ 由本 session 續持

A-TM20 之歸屬問題結案：`features/time_management/` 由本 session
（分析層 + 其執行層）繼續持有。

直接後果：
1. **`scripts/` 解凍。** A-TM20 轉 RESOLVED。
2. 現存三支腳本自此為本 session 之工作基底，得修改。其中
   `write_back.py`、`lint_tcs.py` 源自另一 session（2026-08-21 09:13–09:14），
   本裁定使其歸屬確定，**不因來源而降低其地位** —— A-TM21 之六項缺陷
   依 G-TM2 修正，非因其非我方所寫而重寫。
3. `data/scripts_snapshot_20260821/` 之快照**保留不刪**（R-TM35），
   其 README 之「歸屬未定」一句依 R-TM13 加註更新，不刪除原文。
4. 併行寫入之風險由 Pei 於另一端停止該 feature 之作業消除；
   本 session 不再對 `scripts/` 之 mtime 設凍結期望值。
```

## 2. 修法之形式要求（十七項共通）

分析層**未讀** `write_back.py` / `lint_tcs.py` 全文，故本包**不寫逐字
程式碼補丁** —— 依 R-TM7 之同一理由（不得憑印象寫未經實測之內容）。
本包給的是**行為規格 + 驗收測試**，實作由執行層為之。

每一項修法須同時滿足：

1. **red-green self-test** —— 綠向證明不誤報，紅向證明抓得到。
   紅向須以**刻意構造之壞輸入**觸發，不得以「理論上會 raise」代替
   （charter：不可能失敗之檢查項標未實測，不標 PASS）
2. **來源標記**（R-TM33）—— 修改後之檔案 docstring 首段須含
   `modified by TC_Generator analysis round 05 under G-TM1/G-TM2/G-TM3`
3. **回報形式**（R-TM31）—— 附程式碼位置與片段，不只「已完成」

---

## 3. 三階段

### 階段 A — `write_back.py`（六項）

| # | 依據 | 行為規格 |
|---|---|---|
| A1 | G-TM2 項 1 / A-TM21(a) | `resolve_columns()` 須以 `ws` 與 `header_row` 實際讀出表頭文字，與 `feature.yaml` 之字母宣告比對，不符即 raise。**或**改寫 docstring 使其誠實描述現行行為。**二擇一，不得留下承諾與實作不符之狀態。**<br>**分析層建議取前者** —— 該複驗正是 rev A/B → rev C 漂移之防線（design_method Q→R、author Z→AA），且 A-TM21(a) 為現存唯一「錯了會被執行」之盲區 |
| A2 | G-TM2 項 2 / A-TM21(b) | **移除 `check_other_sheets()`**，於 `run()` 該處加註解指向 `backend/xlsx_surgical.py:268-275` 之 `verify_structure` 第三層 |
| A3 | G-TM2 項 3 訂正 / A-TM21(c)(d) | tc_id 由寫回端**依列位置賦號**，格式取 `feature.yaml` 之 `write_back.tc_id_format`（`NR1L-TimeAndDate-{n:03d}`，R-TM32），寫入 F 欄（`columns.tc_id`，R-TM34）。<br>**TC JSON 不得攜帶 tc_id**（canon §10.3 末句）—— `tc.get(key)` 迴圈不得用於 tc_id；序號在迴圈外計算。<br>**跨批連續之起點來源須為單一且可查**，實作時明示（既有列數或明文起點擇一，不得二者並存） |
| A4 | A-TM21(e) | `CONST_FUNCTIONAL_SAFETY` 現為死碼。**二擇一**：接上 `write_rows()` 使其實際寫入 S 欄，或移除該常數。**不得留下宣告了卻不寫入之狀態** |
| A5 | G-TM3（含訂正） | 寫回後**重新開啟輸出檔**，讀目標分頁之指定 cell，確認值等於預期。取樣：首列、末列、任一中間列之 `tc_id` 三處（首選，逐列必異）+ `test_item` 三處。**比對失敗即 raise，不得僅警告。**<br>**主要防護對象為 column 層（A-TM21(a)），非 member 層** |
| A6 | R-TM33 | 檔頭來源標記 |

**A5 之紅向 self-test 構造建議**：暫時把 `columns.tc_id` 由 `F` 改為 `G`
（相鄰欄）跑一次，G-TM3 須報錯。此即 column 層位移之最小可觸發案例。
**測完務必還原**，並於回報中附還原後之 `feature.yaml` SHA256。

### 階段 B — `lint_tcs.py`（八項）

| # | 依據 | 行為規格 |
|---|---|---|
| B1 | G-TM1 項 1 | **D5 Scope 守衛**：寫回後 D5 仍為空即具名失敗（訊息含 `D5` 與 `R-TM9-A2`），**不與 header drift 混列**。<br>註：D5 現階段本應為空（A-TM02a 未決），故本閘門之綠向即「D5 為空 → 報 spec-scope-pending」，非「D5 有值才過」。實作時明示其語意 |
| B2 | G-TM1 項 2 | **leaf 文字來源隔離**：`test_item` 上半之文字只認 `data/leaf_descriptions.txt`；該檔之 leaf 筆數不等於 **22** 即報錯（R-TM24 之對策為來源隔離，非人工記得）|
| B3 | G-TM1 項 3 | **spec gap 閘門**：`SWE-RA-TIME&DATE-005` / `-002` 之 TC，其 Remarks 為空即報 spec-gap（A-TM13）|
| B4 | G-TM1 項 4 | **界線閘門**：五條界線（R-TM17 三條 + R-TM25 兩條）之 owns / not_ours 訊號名表，TC 全文命中 not_ours 即報 boundary。訊號名取自已複驗之錨點（`$DateTmFormat$`、`$GPSDateTm*$`、`$DateTmHour/Minute/Second$`、物件 `4813974`/`4813937`/`4813953`/`4813960`/`4814098`）|
| B5 | G-TM2 項 4 / A-TM21(f) | 必填欄位檢查**須及於空值**，非只檢查鍵存在。紅向以「所有欄位皆空之 TC」觸發 |
| B6 | G-TM2 項 5 | `read_design_methods()` 加**數量驗證**：期望 **9**（母本 `下拉選單` `$A$1:$A$9`，FORMS.md 實測）。不等於 9 即 raise |
| B7 | R-TM40 / R-TM41 | **spec_reference 三重閘門**，逐條目：<br>(i) 形式符合 `CFTS015-\d{7}`<br>(ii) 其 7 位部分存在於 SYS2 第 5 欄之全集<br>(iii) 其 7 位部分存在於 CFTS015 docx —— **此項擋掉 `CFTS015-6151328` / `-6151331`**（R-TM41）。<br>此為現存 `lint_spec_reference` 之強化，非取代；G-TM2 項 6「不得回退」適用 |
| B8 | G-TM2 項 3 訂正 | **TC JSON 若含 `tc_id` 鍵即報錯** —— 生成端違反 canon §10.3 之偵測點 |

**B7(iii) 之綠向 self-test**：以 `CFTS015-4813974` 應通過；
**紅向**：以 `CFTS015-6151328` 應報錯。**兩者皆須實跑，不得只讀碼。**

### 階段 C — TODO 訂正（三項）

| # | 依據 | 動作 |
|---|---|---|
| C1 | G-TM2 項 9–11 | 撤除三處 TODO：`TC_ID_FORMAT`（R-TM32 已裁）、C 欄 Polarion ID（非未定，Part VII 已明載 SYS2 之角色為錨鏈中介）、Test Set 值域（Part VII 七組已由 R-TM17 簽核，可立即實作為值域閘門）|
| C2 | G-TM2 項 12 | priority 閘門**拆分**：**值域** P0–P3 自母本 P 欄 DV 讀取（非 TC 內容裁決，可立即實作）；**分佈**為內容裁決，維持 TODO 並改標 `TODO(內容裁決)` 以與 `TODO(R-TM10-A1)` 區分 |
| C3 | R-TM33 | 兩支檔頭來源標記 |

**其餘 `TODO(R-TM10-A1)` 標記**（步驟措辭常數、ER 樣板）**維持不動** ——
R-TM10-A1 仍 SUSPENDED，該類常數須待本 feature 依條文決定。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM43 / R-TM44

標題行 `## R-TM43 — A-TM23 之處置`、
`## R-TM44 — features/time_management/ 由本 session 續持`，
內文為 §1 之區塊全文。追加後 `## R-TM` 條數應為 **45**（`04Z-A5` 之 43 + 2）。

### T2 — `ANOMALIES.md`

- **A-TM20** 轉 RESOLVED，條文末尾追加 R-TM44 之處置摘要與依據包
- **A-TM23** 由 PENDING 轉 **AWAITING_UPSTREAM**，條文末尾追加 R-TM43
- 索引兩列狀態同步更新。**A-TM 條數不變（23）**

### T3 — 快照 README 更新（R-TM35 + R-TM13）

`data/scripts_snapshot_20260821/README.md` 之「歸屬未定（A-TM20，待 Pei 裁）」
一句**加刪除線保留**，其下加：

```markdown
> **歸屬已定（2026-08-21，R-TM44）**：features/time_management/ 由本
> session 續持。本快照保留為 A-TM20 事件與階段 A/B/C 修法前狀態之證據，
> 不刪除。
```

### T4 — 階段 A（六項）

依 §3 階段 A 之表逐項實作。**每項附 red-green self-test。**
A5 之紅向須以 `columns.tc_id` 暫改 `G` 觸發，**測後還原並附 SHA256**。

**階段 A 完成後停下回報，不逕入階段 B。**

### T5 — 階段 B（八項）

同上，逐項附 red-green。B7(iii) 之紅綠兩向須實跑。

### T6 — 階段 C（三項）

### T7 — RD-1 增列 Q-TM4（R-TM43(c)）

於 `docs/fw036/RD1_questions_time_management.md` 追加：

```markdown
## Q-TM4 — spec_reference 之參照體系寫法

CFTS015 內存在兩套並存且可互相對應之物件編號：

  短號家族：CFTS015-732 … CFTS015-1639（26 個相異值，僅見於修訂註記）
  7 位家族：4813898 … 4814253（270 個相異值，全篇正文與章節標題）

對應實例：物件 4814185 之內文含 `CFTSMV015_CIP_R1_O922_118_inline.rtf`，
其次一物件 4814186 稱 `CFTS015-922` —— 短號 922 即 7 位 4814185。

本工作簿之 specification_reference 採 `CFTS015-{7 位物件 id}`，
id 取自 SYS2 匯出之 `Source Requirement items` 欄。
`CFTS015-<7 位>` 之寫法於 CFTS015 全文出現 0 次，為本專案新定之形式。

**問**：該欄之期望寫法為何？是否應改採短號家族，或另有既定之參照體系？

**影響**：兩套編號字面不互通 —— 審閱者見工作簿之 `CFTS015-4814185`
而於文件搜尋同字串將零命中，須改搜 `4814185`。
```

**狀態 DRAFT，不送出**（送出屬 Pei）。

### T8 — 驗證（依 R-TM31，列明細）

```bash
grep -n '^## R-TM4[34]' features/time_management/RULINGS.md
grep -n '^| A-TM20' features/time_management/ANOMALIES.md   # 應 RESOLVED
grep -n '^| A-TM23' features/time_management/ANOMALIES.md   # 應 AWAITING_UPSTREAM
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 45
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 23
grep -n 'modified by TC_Generator analysis round 05' features/time_management/scripts/*.py
grep -n 'Q-TM4' docs/fw036/RD1_questions_time_management.md
grep -rn 'TODO(' features/time_management/scripts/          # 逐處列出，判定各自依據
shasum -a 256 features/time_management/feature.yaml         # A5 紅向測後之還原確認
```

### T9 — 上繳

`docs/upstream/05_gates.md`（可與 `04Z-A5` 合併，分節）。須含：

1. T8 全部輸出
2. 十七項逐項之 red-green self-test **實際輸出**（綠向與紅向各一段），
   標「已實測」或「未實測」，**不得對未實測者標 PASS**
3. A1 之二擇一決定與理由
4. A3 之跨批起點來源之明示
5. A4 之二擇一決定與理由
6. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**（B1 為 `06`）
- 不改 `backend/`（本包全部修法在 `features/time_management/scripts/`）
- 不刪除 `data/scripts_snapshot_20260821/`
- 不修改任何既有下放包或上繳包
- 不將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位
- 不碰 `features/vehicle_setting/`
- 不動 `TODO(R-TM10-A1)` 之步驟措辭常數與 ER 樣板（R-TM10-A1 仍 SUSPENDED）
- 不填 `D5`、不組 Scope 值
- 不送出 RD-1
- 不以 openpyxl 存回任何工作簿

---

## 5. 呈報 Pei

1. **另一 session 對本 feature 之作業請停止**（R-TM44 之前提）。
   本包起本 session 將寫入 `scripts/`，兩端並寫會重演 09:13 之覆蓋。
2. **R-TM10-A1 替代樣式來源** —— 仍無候選，維持 SUSPENDED。
   其後果現具體化：階段 C 之 `TODO(R-TM10-A1)`（步驟措辭常數、ER 樣板）
   在 B1 生成前仍須有值，屆時只能依條文逐項決定，無先例可循。
   **此為 B1 之下一個實質阻塞項**，請預為考慮。
3. RD-1 Q-TM1–4 已備齊，送出屬你。
4. 分支 ahead 14 未 push。

## 6. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM43 | 裁決（Pei），A-TM23 處置 | §1 | ✅ T1 + T2 + T7 |
| R-TM44 | 裁決（Pei），歸屬與解凍 | §1 | ✅ T1 + T2 + T3 |
| A-TM20 → RESOLVED | anomaly 結案 | §1 | ✅ T2 |
| A-TM23 → AWAITING_UPSTREAM | anomaly 狀態變更 | §1 | ✅ T2 |
| Q-TM4 | RD-1 草案增列 | §4 T7 | ✅ T7 |

分析層本包未動 git、未改任何腳本（本包為行為規格，實作屬執行層）、
未改 `backend/`。
