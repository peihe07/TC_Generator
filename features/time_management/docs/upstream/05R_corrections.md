# 上繳 05R — 階段 B 八項完成（self-test 17/17），R-TM40 依據改指新 §10.7(a)

執行層 → 分析層。對應 `docs/handoff/05R_stage_b.md`。2026-08-21。

**T1–T6 完成。階段 B 八項 + 階段 C 之 C1/C2 已實作，self-test 17/17 全數
實跑通過。依 T5 明令，階段 C 之 C3 以外未逕行完成之部分停下回報。**

**三項須先講**：

1. **T1 指示引用之 canon §10.7 Rules 第 2 條已不存在** —— 該節被他方整節
   改寫。執行層未照字面執行，改指新 §10.7(a)，該依據更強。見 §2
2. **新 §10.7 之排列規則與既有候選表格式不符** —— 已於 B7 依新規實作，
   並回頭發現 `04Z-A4` T4 之候選表需重排。見 §2.2
3. **T3 實測：S 欄無 DV，A-TM24 來源 1 不成立** —— 轉來源 2/3，須 Pei。見 §3

---

## 1. T6 驗證（R-TM31 列明細；R-TM46 增量 + 前後實測值）

```
R-TM45  RULINGS.md:1632      R-TM46  RULINGS.md:1659      R-TM47  RULINGS.md:1679
R-TM40 依據再訂正             RULINGS.md:1442
A-TM24 索引                   ANOMALIES.md:36
A-TM23 修正註記                ANOMALIES.md:1342
Q-TM4 SourceID 措辭           RD1_questions_time_management.md:79
lint_tcs.py 來源標記           lint_tcs.py:4

條數（前 → 後，增量）
  ## R-TM   47 → 50   +3   期望 +3   OK
  ## G-TM    3 →  3   +0   期望 +0   OK
  ## A-TM   23 → 24   +1   期望 +1   OK
```

## 2. **T1 之偏離：R-TM40 依據改指新 §10.7(a)**

### 2.1 指示所引之規則已不存在

`05R` T1 要求將 R-TM40 之依據改為 canon §10.7 **Rules 第 2 條**
（`Use the SourceID format from SYS1 / Polarion when available`）。

**實測**：`grep -c 'Use the SourceID format' docs/runtime/ASPICE_SWE6_AI_Instruction.md`
→ **0**。canon §10.7 已由他方**整節改寫**（工作樹變更，尚未 commit）：
舊節之 `Format per entry` 與六條 `Rules` 全數刪除。

**執行層未照字面執行**，改指新 §10.7(a)：

```
(a) CFTS 母文件 → `CFTS{nnn}-{ObjectID}`，ObjectID 為該物件之
    Polarion 7 位號碼。短號需求 ID（如 CFTS015-824）不得作為錨，
    僅得於 reasoning 引用。
```

**新依據強於指示所引者**：前者是「明文允許使用 SourceID 格式」，
後者是「**明文規定** CFTS 母文件即用此格式」，且**明文禁止短號作為錨**
—— 其舉例 `CFTS015-824` 恰為本 feature 短號家族之成員。

**連帶**：A-TM23 之「本專案新定之形式」一語，其修正不再是「canon 明文
允許」而是「**canon 明文規定**」。已於該條之修正註記載明。

### 2.2 **新 §10.7 之排列規則與 `04Z-A4` 候選表格式不符**

新節之排列段（舊節無此規定）：

```
排列：一來源文件一行（換行分隔）；同一文件內多個 ObjectID／章節號
以 `, ` 續列且文件前綴僅敘明一次；禁用 `;`。TC 直接驗證之主要來源
列於首行，同文件內 ID／章節號升冪。
```

`04Z-A4` T4 所產之候選表為 `CFTS015-4813919, CFTS015-4813920, …`
（**前綴逐條重複**），依新規應為
`CFTS015-4813919, 4813920, 4813984, 4814069`（**前綴僅一次**）。

**處置**：B7 已依新規實作（前綴重複即報 spec-reference），
**候選表檔案本身保留為軌跡未改**（`data/spec_reference_candidates.txt`）。
**提請**：該表是否需重新產出為新格式 —— 執行層未逕行，因其為
`04Z-A4` 之產物且已上繳。

## 3. T3 — 母本 S 欄 DV 實測：**來源 1 不成立**

`xl/worksheets/sheet6.xml` 唯讀解析，四組 DV：

| DV | sqref | 涵蓋欄 | formula1 |
|---|---|---|---|
| classic | `P10:Q1411` | **P–Q** | `"P0,P1,P2,P3"` |
| classic | `T10:Z1411` | T–Z | `"0,1"` |
| classic | `AF10:AF1411` | AF | `"Pass, Fail, Pending,Block,NA"` |
| x14 | `R10:R1411` | R | `下拉選單!$A$1:$A$9` |

**S 欄（第 19 欄）不落在任何 sqref 範圍內** → **A-TM24 來源 1 不成立**，
轉來源 2（036 填寫規範／SWQT 慣例，Tier 3）或來源 3（範圍界定，Tier 2）
—— **兩者皆須 Pei**。

**附帶發現**：P 欄之 DV 範圍為 `P10:Q1411`，**涵蓋至 Q 欄**（Estimated
Test Time）。對本 feature 無實質影響（Q 欄留空，空值不觸發 list 驗證），
但若日後有人填 Q 欄，將被迫填 P0–P3 之一。屬母本既存形態，
已記入 A-TM24 條末，不另立條。

## 4. T5 — 階段 B 八項（＋ C1 / C2）

**修改前備份**：`/tmp/lint_tcs.py.pre-05R`。修改後 **636 行**（原 301 行）。

### 4.1 逐項實作

| # | 閘門 | 函式 | 依據 |
|---|---|---|---|
| B1 | D5 Scope 守衛 | `lint_d5_scope()` | G-TM1 項 1 / R-TM9-A2 |
| B2 | leaf 文字來源隔離 | `lint_leaf_source()` ＋ `read_leaves()` | G-TM1 項 2 / R-TM24 |
| B3 | spec gap | `lint_spec_gap()` | G-TM1 項 3 / A-TM13 |
| B4 | 界線（五條） | `lint_boundary()` ＋ `BOUNDARY_SIGNALS` | G-TM1 項 4 / R-TM23 + R-TM25 |
| B5 | 必填及於空值 | `lint_required_fields()` | G-TM2 項 4 / A-TM21(f) |
| B6 | 詞彙數量驗證 | `read_design_methods()` ＋ `DESIGN_METHOD_COUNT=9` | G-TM2 項 5 |
| B7 | spec_reference 三重 | `lint_spec_reference()` ＋ `read_sys2_items()` | R-TM40 / R-TM41 / canon §10.7(a) |
| B8 | TC JSON 不得帶 tc_id | `lint_no_tc_id()` | G-TM2 項 3 訂正 / canon §10.3 |
| C1 | Test Set 值域 | `lint_test_set()` ＋ `TEST_SETS` | G-TM2 項 11 / R-TM17 |
| C2 | priority **值域** | `lint_priority_domain()` ＋ `read_priority_domain()` | G-TM2 項 12 |

**B1 之語意已明示**（`05` §3 之要求）：D5 現階段**本應為空**，故綠向為
「D5 為空 → 報 `spec-scope-pending`」，**報的是待決狀態而非缺陷** ——
它使「D5 空著」每次 lint 都現形，不致因久未處理而被當成正常。
D5 若已有值則報 `d5-scope`（要求先更新 A-TM02a / A-TM11 再填）。

**C2 之拆分已落實**：值域自母本 P 欄 DV **讀取**（`read_priority_domain()`，
不寫死字面）；**分佈**改標 `TODO(內容裁決)` 並於註解明示其與
`TODO(R-TM10-A1)` 之區別 —— 後者管跨 feature 樣式，前者管本 feature
自身之內容決定，**不會隨 R-TM10-A1 解除而解決**（與 A-TM24 同一形態）。

### 4.2 red-green self-test —— **17 / 17 全部實跑通過**

```
PASS 綠向：合規之 TC 未轉紅
PASS 紅向 required-fields  (B5 空值，只留一欄空): 欄位 `pre_conditions` 為空
PASS 紅向 leaf-source      (B2 不在 22 筆內): req_id `SWE-RA-TIME&DATE-099` 不在 …22 筆 leaf 全集內
PASS 紅向 test-set         (C1 非七組之一): test_set `Time` 不是 framework Part VII 之七組（R-TM17 已簽）
PASS 紅向 priority-domain  (C2 值域外): priority `P9` 不在母本 P 欄 DV 之值域 ['P0','P1','P2','P3'] 內
PASS 紅向 spec-gap         (B3): SWE-RA-TIME&DATE-002 為 A-TM13 之受影響 leaf，其 Remarks 為空…
PASS 紅向 boundary         (B4): SWE-RA-TIME&DATE-011 之內文命中 `$DateTmHour$`，該訊號屬鄰片…
PASS 紅向 no-tc-id         (B8): TC JSON 含 `tc_id` 鍵。canon §10.3 明訂 generator 賦號…
PASS 紅向 test-group       (R-TM8): test_group `Time Management` ≠ `Time and Date`
PASS 紅向 design-method    : design_method `不存在之方法 (Nope)` 不在母本下拉選單詞彙內
PASS 紅向 spec-reference i (B7 形式): 首 token `4813905` 不符 `CFTS015-<7 位>`（canon §10.7(a)）
PASS 紅向 spec-reference ii(B7 SYS2 全集): 物件 `9999999` 不在 SYS2 `Source Requirement items` 之全集內
PASS 紅向 spec-reference iii(B7 R-TM41): 物件 `6151328` 不存在於 CFTS015 docx。格式湊得出來不等於來源有此內容
PASS 紅向 spec-reference   (B7 禁用 ;): 含 `;` —— canon §10.7 排列段明文禁用…
PASS 紅向 spec-reference   (B7 前綴重複): `CFTS015-4813898` 重複帶前綴 —— canon §10.7 排列段「文件前綴僅敘明一次」
PASS 紅向 step-er-count    : 步驟 2 條 vs ER 1 條
PASS B1 D5 守衛: D5（範圍 Scope）為空 —— R-TM9-A2…

自驗：17 / 17
```

**B7(iii) 之紅綠兩向皆實跑**（`05` 明令必測）：綠向以
`CFTS015-{sorted(spec_objects ∩ sys2_items)[0]}` 通過；
紅向以 `CFTS015-6151328` 報錯。

### 4.3 **綠向抓到一個真問題 —— `remarks` 被誤列為必填**

首次執行 self-test 為 **16/17**，唯一失敗者為**綠向**：

```
**FAIL** 綠向：合規之 TC 轉紅 → [('required-fields', 'GREEN: 欄位 `remarks` 為空')]
```

**成因**：B5 之必填清單未排除 `remarks`。但 `remarks` 之必要性是
**條件式**的 —— 僅 A-TM13 兩片與 BLOCKED 列需填，其餘 20 片本應為空
（`BLANK_BY_DECISION`），而該條件正由 B3（`lint_spec_gap`）在管。

**若無綠向，此誤報不會被發現**，且其後果是 20 片正常 leaf 全部誤報 ——
一個把真發現淹沒在雜訊裡的閘門。已修正（B5 skip 清單加 `remarks`，
並於註解說明其條件式性質由 B3 管）。

**此即 R-TM45 所稱「綠向證明不誤報」之實例** —— 紅向全過不代表閘門正確。

### 4.4 R-TM45 之同層版本已預先套用

`05R` §1 之 R-TM45 管跨層互斥。**階段 B 八項皆於 TC 層同層**，無跨層問題，
但有**順序依賴**：全空 TC 會同時觸發多閘。故 B5 之紅向以
「僅 `pre_conditions` 一欄為空」構造，**不用全空 TC** —— 後者看不出是
哪一閘抓到的。已記入 R-TM45 之回報段。

## 5. T7(4) — 該驗而未驗者（五全集）

### 5.1 依全集 1

T1–T6 完成。**階段 C 之 C3（兩支檔頭來源標記）**：`lint_tcs.py` 已加
（`:4`），`write_back.py` 於階段 A 已加（`:4`），
`build_batch_context.py` **未加** —— 該支未在本包修改範圍內。

### 5.2 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **完整 lint 路徑（非 self-test）** | `generated/` 無 TC JSON，`main()` 印「尚未生成 TC」後 return 0。**B1 之 D5 守衛在該路徑下不會執行**（其在 `for p in gen` 之後）—— 若 `generated/` 為空即提前 return，D5 守衛被跳過。**此為執行層新識別之缺口，見 §5.3** |
| 2 | `build_batch_context.py` 之來源標記 | 未加（不在本包範圍） |
| 3 | A-TM24（functional_safety 值） | 來源 1 已否定，待 Pei |
| 4 | 候選表是否需依新 §10.7 重排 | §2.2 之提請 |
| 5 | R-TM47 之寫入動作 | 落點為 `docs/fw036/framework.md`（全域檔，他方併行修改中），本包指令段未指派 |
| 6 | canon 新增之三節對本 feature 之影響 | §5.4 |

### 5.3 **執行層新識別：`generated/` 為空時 B1 被跳過**

`main()` 之流程為：

```python
gen = sorted((fd / "generated").glob("*.json"))
if not gen:
    print("generated/ 無 json —— 尚未生成 TC")
    return 0                      # ← 提前 return
for p in gen:
    findings += lint_file(p, auth)
findings += lint_d5_scope(auth)   # ← B1 在此，永遠到不了
```

**B1（D5 守衛）為工作簿層檢查，與是否已生成 TC 無關**，卻被放在 TC 迴圈
之後。`generated/` 為空時提前 return，B1 不執行。

**現況無實害**（尚未生成 TC，且 self-test 已涵蓋 B1），但 B1 之設計意圖
是「使 D5 空著這件事每次 lint 都現形」—— 而現在只有在有 TC 時才現形。

**執行層未逕改**（B1 之位置為 `05R` T5 所未指定，且改動 `main()` 之控制流
超出「逐項實作」之範圍）。**提請於階段 C 或下一包指派移至 `if not gen`
之前。**

### 5.4 canon 新增三節對本 feature 之影響（未評估）

`docs/runtime/ASPICE_SWE6_AI_Instruction.md` 除 §10.7 改寫外，另新增：

| 新節 | 對本 feature 之潛在影響 |
|---|---|
| **§4.3.1 test_item 兩段式（R-S4）** | 上半 verbatim **上限 50 token**、超限須摘句；下半 `(...)` 測試目的，**缺括號 = FAIL**。與 R-TM24 之來源隔離相容，但多了長度約束與格式約束 |
| **§8.4.3 缺件佔位（S6）** | 欄位無法填寫時寫 `PENDING: DR-{n}`，**不得留空、不得填 NA**。直接關係 A-TM13 兩片之 Remarks 寫法與 D5 |
| **§8.7.5 訊號記法（R-1）** | CAN 訊號斷言須三件組 `<Signal> in <MESSAGE> on <segment>`；**網段須有 DBC 或架構文件依據，查無者標 PENDING 不得杜撰** |

**§8.7.5 對 B4 之衝擊最大**：本包所實作之 `BOUNDARY_SIGNALS` 用
`$DateTmFormat$` / `$DateTmHour$` 等單 token。依新規，若該等為 CAN 訊號
則須寫為三件組，而**本 feature 無 DBC 或架構文件** → 依 §8.4.3 得標
`PENDING`。

**執行層未依新 canon 調整 B4**，理由：三節皆為他方於工作樹之未提交變更，
其生效時點與適用範圍未經本 feature 之往返確認。**提請分析層評估。**

### 5.5 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| 十七項 self-test 全過 | 首次執行為 16/17，綠向失敗 → 該測試非一律全綠 | 有 |
| S 欄無 DV | 同一解析對 P/R/T–Z/AF 四欄皆命中 → 掃描有效 | 有 |
| `Use the SourceID format` 不存在 | 同一 grep 對 `CFTS{nnn}-{ObjectID}` 命中 → canon 檔可讀 | 有 |
| B7(iii) 擋掉 6151328 | 同閘對 `CFTS015-{合法 id}` 綠向通過 → 非一律報錯 | 有 |

## 6. 本包未動之事項

未動 git。**未執行階段 C 之 C3 對 `build_batch_context.py` 之部分**。
未生成任何 TC。未改 `backend/`。**未對母本或任何工作簿存回**（T3 唯讀）。
未刪除 `data/scripts_snapshot_20260821/`。未修改任何既有下放包或上繳包。
**未將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位**（B7(iii) 反而
主動擋之）。**未填 `functional_safety` 之值**（A-TM24 未決）。
未碰 `features/vehicle_setting/`。未填 `D5`、未組 Scope 值。未送出 RD-1。
**未依新 canon 三節調整任何實作**（§5.4 之提請）。
