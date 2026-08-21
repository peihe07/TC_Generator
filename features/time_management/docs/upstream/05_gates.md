# 上繳 05（第一部分）— 解凍、階段 A 六項完成，依 T4 停下回報

執行層 → 分析層。對應 `docs/handoff/05_gates.md`。2026-08-21。

**T1–T4、T7 完成。依 T4 明令「階段 A 完成後停下回報，不逕入階段 B」，
階段 B（八項）與階段 C（三項）未執行。**

**兩項須先講**：

1. **05 T4 所建議之 A5 紅向構造不可行** —— A1 之表頭複驗會先 raise，
   執行到不了 G-TM3。已改以函式層構造，紅綠皆實測通過。見 §4.5
2. **R-TM 條數為 47，非本包期望之 45** —— 條數差異連鎖自 `04Z-A4`
   之補做。見 §1

---

## 1. 條數與執行順序

`05` 依 R-TM20 聲明「`04Z-A5` 尚未上繳」，並要求先跑 `04Z-A5` T1–T5。
**執行層另發現 `04Z-A4` 亦未執行**（其 R-TM40/41 為 `04Z-A5` T1(d) 所依賴），
故實際順序為：**`04Z-A4` → `04Z-A5` → `05`**。

| 階段 | `## R-TM` |
|---|---|
| `04Z-A4` 執行前 | 42 |
| ＋ R-TM40 / R-TM41 | 44 |
| ＋ R-TM42（`04Z-A5`） | 45 |
| ＋ R-TM43 / R-TM44（本包） | **47** |

本包 T1 期望 45（＝`04Z-A5` 之 43 + 2），該 43 假設 `04Z-A4` 未執行。
**實際 47。** `## A-TM` 23 與期望相符。

## 2. T1 / T2 / T3 寫入確認

| T | 內容 | 位置 |
|---|---|---|
| T1 | R-TM43、R-TM44 逐字 | `RULINGS.md`；45 → **47** |
| T2 | A-TM20 → **RESOLVED**（R-TM44） | 索引 `:32`；條末加結案段 |
| T2 | A-TM23 → **AWAITING_UPSTREAM**（R-TM43） | 索引 `:35`；條末加處置段 |
| T3 | 快照 README「歸屬未定」加刪除線 + R-TM44 註記 | `data/scripts_snapshot_20260821/README.md` |

**A-TM20 之事實記載未因結案而變**（R-TM13）：09:13–09:14 之覆蓋確曾發生，
執行層原產出之兩份確已失落。**結案的是歸屬，不是事件。**

## 3. T7 — RD-1 增列 Q-TM4

`docs/fw036/RD1_questions_time_management.md` 現有 Q-TM1（`:5`）、
Q-TM2（`:26`）、Q-TM3（`:46`）、**Q-TM4（`:65`）**。狀態 DRAFT，未送出。

## 4. T4 — 階段 A 六項

**修改前備份**：`/tmp/write_back.py.pre-05`。修改後 356 行（原 214 行）。

### 4.1 A6 — 來源標記（R-TM33）

`write_back.py:4`：

```
modified by TC_Generator analysis round 05 under G-TM1/G-TM2/G-TM3
```

**此標記自此為歸屬判定之依據**，取代已解除之 mtime 凍結期望值
（R-TM44 第 4 點）。

### 4.2 A1 — `resolve_columns()` 表頭複驗（G-TM2 項 1 / A-TM21(a)）

**取分析層建議之前者**（實作複驗），非改 docstring。**理由**：
A-TM21(a) 為本 feature 現存唯一「錯了會被執行而非被攔」之盲區
（`verify_structure` 保護檔案結構，不驗欄位對映；寫進錯欄時錯欄仍在
目標分頁內、屬 `patched`，三層全綠）。改 docstring 只是讓文件誠實，
不消除該盲區。

實作（`:113-150`）：新增 `HEADER_NEEDLE` 判準表（十六欄，取自母本 rev C
實測表頭）與 `_norm()`；`resolve_columns()` 以 `ws` 與 `header_row` 實際
讀出表頭，逐欄比對字母宣告，不符即彙整全部 drift 後 raise。

**原實作之 `ws` / `header_row` 兩參數完全未使用，本次接上。**

**red-green（已實測）**

```
綠向：現行 feature.yaml 字母 vs 母本表頭
  PASS 未 raise，解析 16 欄
       tc_id=F  design_method=R  functional_safety=S  author=AA  remarks=AH

紅向 1：tc_id 由 F 暫改 G（記憶體內 deepcopy，不動檔案）
  PASS 已叫：tc_id: feature.yaml 宣告 G，該欄表頭為 'Test Group\n測試組'；
             表頭文字指向 F

紅向 2：整體位移一格（design_method R→S）
  PASS 已叫：design_method: feature.yaml 宣告 S，該欄表頭為
             'Functional Safety\n功能安全'；表頭文字指向 R
```

紅向 2 為 rev A/B → rev C 漂移之實際形態（`design_method` Q→R），
故該構造比單欄改動更貼近真實風險。

### 4.3 A2 — 移除 `check_other_sheets()`（G-TM2 項 2 訂正 / A-TM21(b)）

`def check_other_sheets` 計數 **0**。`:235` 留註解指向
`backend/xlsx_surgical.py:268-275`，並說明其功能被 `verify_structure`
第三層完全涵蓋且後者更嚴格。呼叫處（`run()`）改為註解。

**連帶**：`zipfile` 隨之成為未使用之 import，一併移除；
`re` 因 A1 之 `_norm()` 而新增。**兩者皆已驗證**（`py_compile` 通過，
且 A1 測試實跑）。

### 4.4 A3 — tc_id 依列位置賦號（G-TM2 項 3 訂正 / A-TM21(c)(d)）

**canon §10.3 末句之遵守**：`tc.get(key)` 迴圈**排除 `tc_id`**（`:198-203`
之 skip 清單），序號在迴圈外由 `start_seq + i + 1` 計算，
格式取 `feature.yaml` 之 `write_back.tc_id_format`。

**跨批連續之起點來源 —— 明示為「既有資料列數」，且只取此一來源**：

新增 `existing_data_rows(ws, cols, header_row)`（`:161-178`），
判準為 `req_id`（D 欄）非空之列數。

**理由（G-TM2 項 3 訂正要求「單一且可查」）**：候選有二 —— 讀工作簿既有
列數、或讀 `generated/` 之累計 TC 數。**兩者在正常情形一致，但某批若曾
撤回或重生成即分歧**，而工作簿是交付件、是唯一真相。故取前者，
且**不並存**。

判準取 `req_id` 而非 B 欄：B 欄為公式（`=IF(ISBLANK($D{r}),"",ROW()-9)`）
恆存在；其餘欄可能因 BLOCKED 列而留空。

**red-green（綠向已實測；紅向見 §4.7）**

```
綠向：existing_data_rows 對 BLANK 母本
  PASS 既有資料列數 = 0（BLANK per R-TM5，期望 0）
```

### 4.5 A5 — G-TM3 正向驗證（含訂正）

新增 `check_written_back(out, sheet, cols, expected)`（`:244-281`），
於 `verify_structure` 之後呼叫。取樣：首列、中間列、末列之
`tc_id`（首選）與 `test_item`，比對失敗即 **raise**（非警告）。

docstring 明載其**主要防護對象為 column 層（A-TM21(a)），非 member 層**
（G-TM3 訂正），並說明不取 `design_method` / `priority` 之理由（R-TM42）。

#### **05 T4 所建議之紅向構造不可行 —— 已改構造**

T4 建議「暫時把 `columns.tc_id` 由 `F` 改為 `G` 跑一次，G-TM3 須報錯」。

**該構造在本次修法後不可行**：A1 之表頭複驗會在 `resolve_columns()`
先 raise（G 欄表頭為 `Test Group`，與 `test case id` 不符），
**執行根本到不了 G-TM3**。

**此非缺陷，是兩閘門之正確層序** —— A1 在前攔下設定錯誤，A5 在後攔下
寫入結果錯誤。但它使 T4 之建議構造失效，故改以**函式層構造**：

**red-green（已實測）**

```
綠向：於 /tmp 之測試副本寫入兩列後，以正確 cols 比對
  PASS 值在預期位置，未 raise

紅向 1：預期值改為 NR1L-TimeAndDate-999
  PASS 已叫：列 10 欄 F（tc_id）：預期 'NR1L-TimeAndDate-999'，
             實得 'NR1L-TimeAndDate-001'

紅向 2：cols["tc_id"] 位移一格（此即 A5 之主要防護對象）
  PASS 已叫：列 10 欄 G（tc_id）：預期 'NR1L-TimeAndDate-001'，實得 None
```

**紅向 2 即 column 層位移之直接模擬** —— 它證明 A5 能發現「寫對了內容
但讀錯了地方」，而該情形正是 `verify_structure` 三層全綠者。

**測試副本產於 `tempfile.mkdtemp()` 並於測後刪除，未觸及 `inputs/`
或 `output/`。`feature.yaml` 全程未被改動** —— 三次紅向皆以
`copy.deepcopy(cfg)` 或直接改 `cols` dict 為之，**未寫入檔案**。
SHA256 複驗：`6a309731d20cfadfe4978a59432337c7f7c5852edd3e138b38742129dbc53786`
與 `04Z-A4` T2 所記之改後值**逐字元相同**。

### 4.6 A4 — `CONST_FUNCTIONAL_SAFETY` 二擇一

**取「接上 `write_rows()` 使其實際寫入 S 欄」**，非移除。

**理由**：S 欄為交付欄位，其值應由**條文**決定而非由 TC 資料決定。
若移除該常數而讓 `tc.get("functional_safety")` 決定，等於把欄位值之
決定權下放給生成端 —— 與 canon §10.3 對 tc_id 之處理精神相反
（該條明訂 generator 賦值、LLM 不得產出）。

實作：`write_rows()` 之 skip 清單加入 `functional_safety`（不從 tc 讀），
於 `:213-215` 寫入常數。值未裁定前由 `run()` 之 `unresolved` 檢查
**攔在寫入之前**（`--write` 路徑 raise，dry-run 僅提示）。

**現況**：`CONST_FUNCTIONAL_SAFETY` 出現於三處 —— 定義（`:57`）、
**實際寫入（`:215`，本次新增）**、`unresolved` 檢查（`:316`）。
**不再是死碼。** 其值仍為 `None`（`TODO(R-TM10-A1)`，待本 feature 條文）。

### 4.7 階段 A 之未實測項

| 項 | 狀態 |
|---|---|
| A3 紅向 | **未實測** —— 需既有資料列之工作簿方能測「跨批續號」，而本 feature 為 BLANK 且無 TC。**標未實測，不標 PASS** |
| A4 之實際寫入 | **未實測** —— `CONST_FUNCTIONAL_SAFETY` 為 `None`，`unresolved` 檢查會攔在 `--write` 之前。值裁定後方能測 |
| 完整 `run()` 路徑 | **未實測** —— `generated/` 無任何 TC JSON，`load_tcs()` 會 raise。**`surgical_save` 之寫入路徑在本 feature 仍從未執行過**（`04Z-A3` §4.3 項 1 之延續）|

**三項皆為「需要 B1 之產物方能測」**，非本階段可補。

## 5. T8 驗證（可跑之項，依 R-TM31 列明細）

```
R-TM43 / R-TM44   RULINGS.md（T1 追加）
A-TM20            ANOMALIES.md:32   **RESOLVED**（R-TM44）
A-TM23            ANOMALIES.md:35   **AWAITING_UPSTREAM**（R-TM43）
R-TM 條數 47（見 §1）    A-TM 條數 23（期望 23）OK
來源標記          write_back.py:4   modified by TC_Generator analysis round 05
Q-TM4             RD1_questions_time_management.md:65
feature.yaml SHA  6a309731…dbc53786（與 04Z-A4 T2 改後值相同，未被測試改動）
```

`grep -rn 'TODO('` 與 `lint_tcs.py` 之來源標記待階段 B/C 完成後一併驗。

## 6. 該驗而未驗者（五全集）

### 6.1 依全集 1

T1–T4、T7 完成。**T5（階段 B）、T6（階段 C）依 T4 明令未執行。**
T8 部分執行（階段 B/C 相關判準待其完成）。

### 6.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 | 47 |
| `ANOMALIES.md` | 條數 + 兩列狀態 | 23；RESOLVED / AWAITING_UPSTREAM |
| 快照 README | 刪除線 + 新註記 | 已加 |
| `write_back.py` | `py_compile` + 六項落點 grep + red-green 實跑 | 通過 |
| `RD1_...md` | Q-TM 四節位置 | :5 / :26 / :46 / :65 |
| `feature.yaml` | SHA256 | 未變 |

七處 `str.replace` 全部前置 `assert` + `count==1`。

### 6.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | 階段 A 之三項（A3 紅向、A4 寫入、完整 `run()`） | §4.7，需 B1 產物 |
| 2 | **階段 B 八項、階段 C 三項** | 依 T4 停下，未執行 |
| 3 | R-TM43(a) 之「交付說明」落點 | **未指定** —— 候選：工作簿 Remarks / `docs/fw036/` 交付文件 / Part VII。影響 B1 之 Remarks 設計（每列帶或僅首列帶）。**已於 R-TM43 回報段提請** |
| 4 | R-TM40 之依據應改為 canon §10.7 Rules 第 2 條 | `04Z-A5` 上繳 §3.4 之提請，未獲回覆 |
| 5 | 其餘 106 處條文「提及」之逐一比對 | `04Z-A5` §5.2 項 1 |
| 6 | PU 陽性對照、A-TM12 / A-TM19 | 續掛 |

### 6.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| A1 綠向不誤報 | 同一函式對兩種紅向構造皆 raise → 非一律通過 | 有 |
| A5 綠向不誤報 | 同一函式對兩種紅向構造皆 raise | 有 |
| `existing_data_rows` = 0 | 該函式對非空工作簿之行為未測（§4.7），故 0 之意義限於「BLANK 下正確」 | **部分** |
| `check_other_sheets` 已移除 | `def` 計數 0，而 `verify_structure` 仍在 `run()` 中被呼叫 | 有 |

### 6.5 依全集 5（設計說明之可驗性）

`05` §2 之三項形式要求（red-green、來源標記、附位置片段）**全部套用**。
其中 red-green 之「紅向須以刻意構造之壞輸入觸發，不得以理論上會 raise
代替」—— 本階段之四個紅向皆為實跑，無以讀碼代替者。

**但 §4.7 之三項確實無法構造壞輸入**（缺 B1 產物），故依同一要求
**標未實測而非 PASS**。

## 7. 本包未動之事項

未動 git。**未執行階段 B / C**（依 T4）。未改 `backend/`。
未刪除 `data/scripts_snapshot_20260821/`。未修改任何既有下放包或上繳包。
**未將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位。**
未碰 `features/vehicle_setting/`。未動 `TODO(R-TM10-A1)` 之步驟措辭常數
與 ER 樣板。未填 `D5`、未組 Scope 值。未送出 RD-1。
未以 openpyxl 存回任何工作簿 —— **§4.5 之測試副本產於 `tempfile.mkdtemp()`
並於測後刪除，非交付路徑，且未觸及 `inputs/` 或 `output/`。**
未生成任何 TC。
