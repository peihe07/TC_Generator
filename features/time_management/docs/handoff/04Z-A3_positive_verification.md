# 04Z-A3 — 引用截斷之訂正、G-TM2 項 3 收緊、A-TM22 正向驗證缺口

分析層 → 執行層。覆核對象：`docs/upstream/04Z-A2_corrections.md`。**受理。**

**兩件比條文更要緊的，兩件都成立，第一件是我的錯。**

`scripts/` 仍凍結（A-TM20 第四次呈報未獲答覆），本包全部動作為條文與
`backend/` 唯讀。

---

## 1. canon §10.3 之引用截斷 —— 我引到一半，而被切掉的那半是規範性的

`04Z` §4 我引 canon §10.3 止於
`monotonically increasing within the same {project}-{abbr} group.`，
原文其後尚有分號與一句：

> **; the generator handles assignment, the LLM does not emit `tc_id`.**

分析層已對 canon 原文複驗，**執行層所指屬實**。該句不是補充說明，
是規範性要求，且它是三項判定中唯一會改變**實作方式**的一項 ——
前三項只約束 tc_id 長什麼樣，這句約束**誰產生它**。

**我用 canon 當權威，卻把句子在分號處切斷，切掉的正好是操作性的那半。**
這與我一路在指摘的形態同構：docstring 承諾／實作缺失是寫的人切斷，
「找到保護所在」當「保護有效」是讀的人切斷，本次是**引用的人切斷**。

```
R-TM38（分析層自裁，2026-08-21）—— 引用條文須引至規範性句末

引用 canon、FORMS.md、feature profile 或任何規範文件作為裁決依據時，
須引至該句之句末（`.` / `。`），不得於分號、逗號、破折號處截斷。

理由：規範文件常以分號銜接「形式要求」與「操作要求」，前半描述成品
長什麼樣，後半描述由誰、以何方式產生。截斷於分號會保留形式而丟失
操作，而丟失的那半通常才是實作時真正需要的。

引用時一併標明來源檔與行號區間，使截斷可被對造發現。

依據：04Z §4 引 canon §10.3 止於 `... group.`，切掉
`; the generator handles assignment, the LLM does not emit tc_id.`
—— 該句為三項判定中唯一影響實作方式者。
（原文位置：docs/runtime/ASPICE_SWE6_AI_Instruction.md:521-525）
```

### 1.1 G-TM2 項 3 收緊 —— 執行層之提請成立

執行層指出：R-TM34 已把 `tc_id` 補進 `columns`，而現存 `write_back.py`
之 `write_rows()` 走 `tc.get(key)` 迴圈，**修法若照最直覺的方式做
（讓 TC JSON 帶 tc_id），會直接違反 canon**。

```
G-TM2 項 3 訂正（2026-08-21，依 04Z-A2 上繳 §1）

原文：「A-TM21 (c)+(d) —— tc_id 自 feature.yaml 讀取並實際寫入 F 欄」

訂正為：

  3. A-TM21 (c)+(d) —— tc_id 由**寫回端依列位置賦號**，格式取自
     feature.yaml 之 write_back.tc_id_format（R-TM32），寫入 F 欄。

     **TC JSON 不得攜帶 tc_id** —— canon §10.3 末句：
     `the generator handles assignment, the LLM does not emit tc_id`
     （ASPICE_SWE6_AI_Instruction.md:521-525）。

     故 write_rows() 之 tc.get(key) 迴圈**不得**用於 tc_id：
     - tc_id 須在迴圈外由序號計算，不從 tc 取
     - lint 層須增一項：TC JSON 若含 tc_id 鍵即報錯
       （生成端違反 canon §10.3 之偵測點）

     序號依 R-TM32 跨批連續不重設，故賦號需要一個跨批次之起點來源
     （既有列數或明文起點），該來源須為單一且可查 —— 實作時明示之。
```

**A-TM21(d) 之嚴重性隨之提高**：原記為「F 欄不會被寫入」，實則還多一層
—— 修法若走最直覺路徑會引入一個**違反 canon 的新缺陷**。已於 T2 註記。

R-TM32 三項判定全部支持，`feature.yaml:50` 不改。

## 2. `patch_sheet_xml` 之 inline string —— 我所慮之事已被設計規避

`_cell_xml` 之 docstring：

> the source `sharedStrings.xml` is copied verbatim, so appending to it
> would mean rewriting it — the one member the surgical path most wants
> to leave alone.

新字串以 `t="inlineStr"` 內嵌於 cell，`sharedStrings.xml` 完全不動。
**我 T3(2) 第 3 項所問之「新增字串是否使第三層誤報」，答案是相反 ——
該路徑根本不會產生新增字串。**

執行層之評語準確：這是用「每個字串多佔一點空間」換「最不想動的 member
完全不動」。**該取捨值得記入 Part VII，因為它解釋了為何 `surgical_save`
是唯一授權寫回路徑而非只是慣例。**

### 2.1 `_dv_counts` —— 三項回報皆受理，一句話值得立為判準

母本實測 `sheet6.xml (classic=3, x14=1)`、其餘七分頁全 `(0,0)`，
與 FORMS.md 所載四組 DV 逐項對應 —— 交叉驗證成立。

「可由讀碼判定」之理由（只依賴 regex 文字計數與節點消失即文字消失，
無隱藏狀態）**充分**，且有 FORMS.md 之獨立實測（1→0、legacy 3 存活、
48→47 members）同向支持。退化情形之判讀（`bad` 只遍歷 `before` 之 key，
但第一層之 `added` 已先攔，兩層互補非漏洞）正確。

最要緊的是這句：

> x14 存活不是靠保護邏輯，是靠根本沒去碰它（全檔 grep `extLst` 只命中
> 註解）—— 這比主動保護可靠，因為沒有可失效的邏輯。

```
R-TM39（分析層自裁，2026-08-21）—— 不觸碰優於主動保護

評估一項保護時，須區分「有邏輯在保護它」與「根本沒有程式碼會動到它」。
後者強度較高：主動保護有可失效之邏輯，不觸碰沒有。

故評估報告中，對「未被任何程式碼觸及」之結論，其舉證方式為
**全檔搜尋該識別字並確認零命中（或僅命中註解）**，而非追蹤保護邏輯
之正確性。

依據：04Z-A2 上繳對 x14 extLst 之判讀。母本 R 欄 x14 下拉之存活，
其依據為 backend/ 全檔 grep `extLst` 僅命中註解，非某個保護分支。
```

## 3. **A-TM22 —— 三層全是反向驗證，無一驗正向**

執行層新識別之風險，**成立且重要，本包列為 B1 前必決**：

> `verify_structure` 三層全部是「不該變的沒變」，沒有一層驗「該變的
> 變對了地方」。若 `sheet_members()` 之「sheet 名 → zip member」對映錯誤，
> patch 會寫進另一個 sheet 之 member，而該 member 恰在 `patched` 內
> → 三層全綠。

**與 A-TM21(a) 同構，只是發生在 member 層而非 column 層。** 兩者合看
即一個完整的盲區：

| 層 | 對映 | 錯了會怎樣 | 現有檢查 |
|---|---|---|---|
| column | `feature.yaml` 字母 → 實際欄 | 寫進錯欄，仍在目標分頁內 | 全綠（A-TM21(a)）|
| member | `sheet_members()` sheet 名 → zip member | 寫進錯分頁，該 member 在 patched 內 | 全綠（A-TM22）|

**兩者皆非「保護失效」，而是「該方向根本沒有檢查」。**

```
A-TM22（PENDING，Tier 2 —— B1 生成前必決）

backend/xlsx_surgical.py 之 verify_structure 三層全為反向驗證
（不該變的沒變）：
  第一層 zip member 名稱集合未增減
  第二層 DV 計數（classic / x14）未變
  第三層 逐 member 位元組比對，僅 patched 者得異

**無一層驗證正向**（該變的變對了地方）。若 sheet_members() 之
sheet 名 → zip member 對映錯誤，寫入會落在另一分頁之 member，
而該 member 恰在 patched 之列，三層全綠。

與 A-TM21(a) 同構（欄位對映錯 → 結構檢查全綠），發生層級不同：
前者 column 層，本條 member 層。

sheet_members() 與 diff_cells() 尚未讀（04Z-A3 T3 指派）。
本條之嚴重性須待該二函式讀畢方能定級 —— 若 sheet_members() 之對映
有自身之正確性保證，本條降為理論風險；若無，則為實質盲區。
```

```
G-TM3（閘門，2026-08-21）—— 寫回後須有正向驗證

B1 生成後之首次寫回前，寫回路徑須具備至少一項正向驗證：
寫回完成後，**重新開啟輸出檔，讀取目標分頁之指定 cell，
確認其值等於預期值**。

理由：現有三層全為反向驗證（A-TM22）。反向驗證再嚴格也無法發現
「寫對了內容但寫錯了地方」—— 而錯地方之後果是交付件靜默損壞。

最小實作：寫回後取 N 列（首列、末列、任一中間列）之
tc_id / test_item / design_method 三欄，與寫入前之預期逐項比對。
比對失敗即 raise，不得僅警告。

本條與 G-TM1 / G-TM2 並列為 B1 前之閘門。
```

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM38 / R-TM39 / G-TM3，訂正 G-TM2 項 3

標題行：

```
## R-TM38 — 引用條文須引至規範性句末
## R-TM39 — 不觸碰優於主動保護
## G-TM3 — 寫回後須有正向驗證
```

內文為 §1 / §2.1 / §3 之區塊全文。

G-TM2 項 3 依 §1.1 之區塊訂正 —— **原文加刪除線保留，訂正文置於其下
並註明依據包**（R-TM13）。

追加後 `## R-TM` 條數應為 **42**；`## G-TM` 應為 **3**。

### T2 — `ANOMALIES.md`：新增 A-TM22，A-TM21(d) 加註

A-TM22 內容為 §3 之區塊全文。索引追加：

```markdown
| A-TM22 | verify_structure 三層全為反向驗證，member 層對映錯誤不可偵測 | PENDING | Tier 2（B1 前必決）|
```

索引條數 21 → **22**。

A-TM21 條文末尾追加：

```markdown
**(d) 嚴重性提高（2026-08-21，依 04Z-A2 上繳 §1）**

原記為「F 欄不會被寫入」。經 canon §10.3 末句
（`the generator handles assignment, the LLM does not emit tc_id`，
ASPICE_SWE6_AI_Instruction.md:521-525）確認，本項尚多一層：
修法若照最直覺路徑做（讓 TC JSON 攜帶 tc_id 並由 tc.get(key) 取），
會引入一個**違反 canon 的新缺陷**。處置見 G-TM2 項 3 訂正。
```

### T3 — `backend/` 續讀（唯讀，兩項，A-TM22 定級所需）

**只讀，不改，不執行。** 依 R-TM31 附位置與片段。

**(1) `sheet_members()`** —— 回報：

- 其如何由 sheet 名解析出 zip member（讀 `workbook.xml` 之 `r:id` →
  `workbook.xml.rels`，或憑索引推算、或憑檔名慣例）
- **該對映是否有自身之正確性保證**：若憑 rels 解析，錯誤會 raise 還是
  靜默取到別的？若憑索引推算，索引來源為何
- 母本之 `Test Case Specification 測試用例規範` 分頁實際解析到哪一個
  member（母本 `sheet6.xml` 之 DV 計數為 `(3,1)`，可作交叉驗證：
  **若該分頁解析結果不是 sheet6.xml，兩者必有一錯**）

**(2) `diff_cells()`** —— 回報：

- 其產出之「要改的 cell」清單如何界定（座標從何而來）
- 是否有任何一處以**分頁名或 member 名**為 key，若有，其與
  `sheet_members()` 之來源是否同一

### T4 — 驗證（依 R-TM31，列明細）

```bash
grep -n '^## R-TM3[89]' features/time_management/RULINGS.md
grep -n '^## G-TM3'     features/time_management/RULINGS.md
grep -n '項 3 訂正'      features/time_management/RULINGS.md
grep -n '^| A-TM22'     features/time_management/ANOMALIES.md
grep -n '嚴重性提高'     features/time_management/ANOMALIES.md
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 42
grep -c '^## G-TM' features/time_management/RULINGS.md      # 期望 3
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 22
stat -f '%Sm %N' -t '%H:%M:%S' features/time_management/scripts/*.py
```

末項期望仍為 **09:13:36 / 09:14:32 / 09:15:18**。

### T5 — 上繳

`docs/upstream/04Z-A3_corrections.md`。須含 T4 全部輸出、T3 兩項逐項回報
（附位置與片段）、**A-TM22 之定級建議**（實質盲區 / 理論風險，附依據）、
**本包是否仍有該驗而未驗者之獨立判斷**（明列全集）。

### 不得執行者

- **不動 git**（除非 Pei 直接指示 —— R-TM36）
- **不寫入、不覆蓋、不修改 `features/time_management/scripts/` 任一行**
- 不修 A-TM21 / A-TM22 之任何一項（凍結中）
- **不改 `backend/` 任何檔**（T3 唯讀）
- 不執行任何腳本
- 不生成任何 TC
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 5. 呈報 Pei

**`features/time_management/` 之歸屬 —— 第五次。** 一句話：本 session
繼續，或交給另一邊。`05`（B1 生成）在此之前不下放。
另：分支 ahead 14 未 push。

## 6. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM38 | 分析層自裁，引用不得截斷 | §1 | ✅ T1 |
| R-TM39 | 分析層自裁，不觸碰優於主動保護 | §2.1 | ✅ T1 |
| G-TM3 | 閘門，寫回後正向驗證 | §3 | ✅ T1 |
| G-TM2 項 3 訂正 | 依 R-TM13 加註保留 | §1.1 | ✅ T1 |
| A-TM22 | anomaly，PENDING，B1 前必決 | §3 | ✅ T2 |
| A-TM21(d) 嚴重性提高 | anomaly 註記，條數不變 | §1.1 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未觸 `scripts/`、未改 `backend/`。
