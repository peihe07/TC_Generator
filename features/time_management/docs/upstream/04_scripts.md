# 上繳 04 — T1–T4 / T6 完成，**T5 遭併行覆蓋，部分未竟**

執行層 → 分析層。對應 `docs/handoff/04_scripts.md`。2026-08-21。

**T5 未如實完成，須先講**：執行層所建之 `write_back.py` 與 `lint_tcs.py`
在寫入後**被另一 session 覆蓋**。現存版本非執行層產出，且缺四項本輪往返
才建立之閘門。詳見 §5。**執行層未覆蓋回去**，提請裁定。

其餘：T1（四條裁決）、T2（A-TM19）、T3（錨點複驗，**九項全中**）、
T4（`privacy` 已清空還原）、T6（六項全符）皆完成。

---

## 1. T6 六項驗證（實際輸出）

```
1. R-TM 條數                        : 33   期望 33   OK
2. A-TM 條數                        : 19   期望 19   OK
3. features/privacy/DECISIONS.new.md : 不存在 → privacy 已清   OK
4. regression_evidence/              : README.md + 2 檔        OK
5. scripts/                          : 3 支（歸屬見 §5）        OK（數量）
6. TODO(R-TM10-A1) 命中               : 13                      OK
```

判準 6 之 13 處分佈於三支腳本，位置清單見 §5.4。

## 2. T3 — R-TM23 錨點對原始 docx 複驗：**九項全中，六項章節全符**

執行層兩度提請之未驗項，本包關閉。

**九個 token 之 count（原始 docx，非沙箱副本）**

```
4813974          count=  1     $DateTmFormat$   count= 10
GPSDateTmHour    count=  8     GPSDateTmYear    count=  8
4813937          count=  1     4813999          count=  1
4814098          count=  1     4813953          count=  2
4813960          count=  1
```

**物件 → 章節歸屬，與 `04` §5 之表逐項對差**

| 物件 | 期望 | 實測 | |
|---|---|---|---|
| `4813974` | 1.3.1.1.5.1 | 1.3.1.1.5.1 | 相符 |
| `4813937` | 1.3.1.1.3 | 1.3.1.1.3 | 相符 |
| `4813953` | 1.3.1.1.4 | 1.3.1.1.4 | 相符 |
| `4813960` | 1.3.1.1.4 | 1.3.1.1.4 | 相符 |
| `4814098` | 1.5.2.5 | 1.5.2.5 | 相符 |
| `4813999` | 1.3.1.1.6.1 | 1.3.1.1.6.1 | 相符 |

**R-TM23 兩條界線之錨點成立。** B1 之 008/011/014 可依其撰寫。

## 3. T4 — `privacy` 遺留物移出（R-TM30）

兩檔已 **mv**（非 rm）至
`features/time_management/data/regression_evidence/`，並更名加來源前綴：

```
privacy_DECISIONS.new.md              2372 B
privacy_recon_leaf_to_section.tsv       48 B
README.md                             1626 B（來源、緣由、還原狀態、相關條文）
```

**`git status --short features/privacy` → 無輸出**（無殘留）。
該目錄與本 feature 動它之前完全一致。

## 4. T1 / T2 寫入確認

| T | 內容 | 結果 |
|---|---|---|
| T1 | R-TM27 / R-TM28 / R-TM29 / R-TM30 逐字追加 | 29 → **33** |
| T2 | A-TM19 新增 + 索引列 | 18 → **19** |

四條裁決均附執行層回報段。R-TM27 之一般化規則（改回傳語意前須讀遍消費點）
已納為作業慣例 —— 本次即因先讀 `recon.py:1135` 而發現字面指令之缺陷。

## 5. **T5 —— 併行覆蓋，未如實完成**

### 5.1 事實

執行層依 T5 建立三支腳本，逐支 `py_compile` 通過。其後複查 T6 判準 6
（`TODO(R-TM10-A1)` 位置清單）時發現**兩支之內容已非執行層所寫**。

| 腳本 | 執行層所寫 | 現存 | 歸屬 |
|---|---|---|---|
| `write_back.py` | 351 行，英文 | **214 行，中文** | **非執行層** |
| `lint_tcs.py` | 312 行，英文 | **301 行，中文** | **非執行層** |
| `build_batch_context.py` | 222 行，英文 | 222 行，英文 | 執行層（特徵字串在） |

判定依據：執行層版本之特徵字串 `Structure ported from` 於前二者
`grep -c` 皆為 **0**，於後者為 **1**。mtime 顯示覆蓋發生於 09:13–09:14。

**執行層之兩份內容已不存於磁碟，無備份。**

### 5.2 A-TM17 之認知須更新 —— 併行者現亦寫入本 feature

A-TM17 已於 `03Z-A1` 經 Pei 確認結案（併行者為 Pei 自己開啟之另一
session）。**但當時之三項登記事實，其作業範圍皆在
`features/vehicle_setting/`。**

本次為**首次觀察到併行者寫入 `features/time_management/`** ——
即本 feature 之目錄。此為新事實，A-TM17 之「保留限制」段落
（不對 `vehicle_setting/` 寫入或實跑）所依據之範圍認知已不完整。

**執行層不重開 A-TM17**（已 RESOLVED，且成因已解釋）。**提請**：
是否另立一條記錄「併行者之作業範圍已含本 feature」，以及本 feature
之寫入是否需要協調機制。

### 5.3 現存兩支之評估 —— 安全項無虞，但缺四項閘門

執行層對現存版本做唯讀評估（未修改、未執行）：

**安全項（無虞）**

| 項 | `write_back.py` 現存版 |
|---|---|
| `surgical_save` 匯入與使用 | 5 處命中 |
| `wb.save(` | **0**（未走 openpyxl 存回路徑，母本 x14 下拉安全）|
| header 不變檢查 | 7 處命中 |
| `TODO` 標記 | 8 處 |

`py_compile` 三支皆通過。

**缺口（四項，皆為本輪往返才建立之條文）**

| 缺口 | 條文依據 | 現存版 grep |
|---|---|---|
| `write_back.py` 無 `D5` 守衛 | **R-TM9-A2** —— Scope 須維持空白，且空白須可驗證 | `D5` = 0 |
| `lint_tcs.py` 未讀 `data/leaf_descriptions.txt` | **R-TM24** —— 該檔為 leaf 文字之唯一許可來源 | `leaf_descriptions` = 0 |
| `lint_tcs.py` 無 A-TM13 spec gap 閘門 | **A-TM13** —— 005/002 之 Remarks 須宣告缺口 | `A-TM13` = 0 |
| `lint_tcs.py` 無五條界線閘門 | **R-TM23 + R-TM25** —— §8.2.1 拘束條款 | `R-TM23`/`R-TM25` = 0 |

**四項皆非風格差異，而是條文未被編碼。** 其中 R-TM9-A2 之 D5 守衛尤要 ——
D5 為交付欄位，且 A-TM02a 明訂其「無值可填」而非「暫緩填」。

### 5.4 執行層版本之設計（供比對，內容已失）

四項缺口在執行層版本中之實作方式，記錄於此供分析層判斷是否值得補回：

- **`check_scope_still_empty(out, sheet)`** —— 於 `surgical_save` 之後、
  與 `check_header_untouched` 並列。理由：header 檢查雖會捕捉到 D5 變動，
  但只作為眾多 drift 之一列；D5 有其專屬條文與 anomaly，應有專屬之
  具名失敗。
- **`load_authorities` 讀 `leaf_descriptions.txt`** 取 22 筆 leaf 全集，
  數量不符即 `LintError`。理由：R-TM24 之風險是「整理式簡寫被當原文複製」，
  對策為來源隔離而非人工記得。
- **`lint_remarks`** —— `SPEC_GAP_LEAVES = {005, 002}`，其 Remarks 為空
  即報 `spec-gap`。
- **`lint_boundary`** —— `BOUNDARY_SIGNALS` 表列 011/008/014 各自
  `owns` 與 `not_ours` 之訊號名（`$DateTmFormat$` / `$DateTmHour$` 等，
  **全部取自 T3 已複驗之錨點**），TC 全文命中 `not_ours` 即報 `boundary`。
- **`self_test`** —— 八個案例，每閘各造一紅一綠。理由為 R-TM21 套用於
  linter 自身：不能失敗的閘門不是閘門。

**現存之 `build_batch_context.py`（執行層版）已含 A-TM13 與五條界線之
指示**（`SPEC_GAP` 與 `BOUNDARIES` 兩表），故該二條文在 context 層有
編碼，僅 lint 層缺。

### 5.5 執行層未採取之動作與理由

**未覆蓋回去。** 理由：
1. 併行寫入同一目錄已證實會互相覆蓋，再寫一次只會重演，且可能覆蓋掉
   對方正在進行之工作
2. 現存版本之安全項無虞（不走 `wb.save`），**不構成須立即介入之風險**
3. 兩份版本孰優非執行層可單方認定 —— 對方版本可能有執行層未見之考量

**未執行任何腳本**（`04` 明令）。**未修改現存兩支之任何一行。**

### 5.6 提請

1. **四項缺口是否補**、由誰補、以何形式（整檔取代 / patch 特定函式）
2. 本 feature 之併行寫入是否需協調機制（見 §5.2）
3. `TODO(R-TM10-A1)` 現為 13 處，其中 `lint_tcs.py` 之 4 處為中文版所寫，
   `write_back.py` 之 8 處同 —— **執行層未複核該 11 處之標記是否恰當**，
   因未讀完對方全文。若採信其標記，須有人複核

## 6. T7(5) — 該驗而未驗者（五全集）

### 6.1 依全集 1（指令逐項）

| T | 狀態 |
|---|---|
| T1 | 完成 |
| T2 | 完成 |
| T3 | 完成，九項全中 |
| T4 | 完成，`privacy` 無殘留 |
| T5 | **部分** —— 三支存在但兩支非執行層產出（§5）|
| T6 | 完成，六項全符 |

### 6.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 | 33 |
| `ANOMALIES.md` | 條數 + 索引 | 19 / 19 |
| `regression_evidence/` | `ls` + README 內容 | 3 檔 |
| `scripts/` 三支 | `py_compile` + **歸屬比對** | 語法通過；**歸屬比對即本次發現覆蓋之途徑** |

**T6 判準 6（`TODO` 位置清單）是本次發現覆蓋之唯一途徑。** 若該判準只
數數量而不列位置，覆蓋不會被發現 —— 位置清單顯示了中文行號，數量不會。
此點值得記入判準設計之經驗。

### 6.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **現存兩支腳本之全文** | **未讀完** —— 僅做關鍵項 grep。其 8+4 處 TODO 標記是否恰當未複核（§5.6(3)）|
| 2 | 三支腳本之實際執行 | `04` 明令不執行。`lint_tcs.py --self-test` 亦未跑，故「閘門能否真的 fire」未驗 |
| 3 | `write_back.py` 之 `feature.yaml` 依賴 | 執行層版本會因缺 `write_back.tc_id_format` 而 raise；**現存版是否有同等檢查未驗** |
| 4 | A-TM05 / A-TM10 之實跑 | 需 drop folder 素材，續掛 |
| 5 | PU 陽性對照 | 待 Pei 裁 |
| 6 | A-TM12 / A-TM19 | 明令併後續批次 |

**第 3 項須特別說明**：本 feature 之 `feature.yaml` **無
`write_back.tc_id_format` 鍵**（privacy 有 `NR1L-Privacy-{n:03d}`，由
R-PV02 裁定）。tc_id 體系為 R-TM10(b) 明列之**不得援引**項，故本 feature
須自行裁定。**在其裁定前，write-back 不可執行。** 執行層版本以顯式
`raise` 攔截；現存版是否如此未驗。

### 6.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| 九個錨點 token 皆命中 | 同一解析對 `615\d{4}` 仍為零命中（A-TM13）| 有 |
| `privacy` 無殘留 | 同一 `git status` 對 `features/time_management/` 有輸出 | 有 |
| 兩支腳本非執行層所寫 | 第三支之特徵字串命中 1，證明比對方法有效 | 有 |

### 6.5 依全集 5（設計說明之可驗性）

`04` §5 之四項錨點主張 —— **本包已全部複驗**（§2），四項全中。
此為分析層主張經執行層獨立確認之第三例（前二為三個 037 檔名、A-TM13）。

## 7. 本包未動之事項

未動 git。**未執行 T5 所建之任何腳本**（含 `--self-test`）。
**未修改現存之 `write_back.py` / `lint_tcs.py` 任何一行。**
未修 A-TM12 / A-TM19。未碰 `features/vehicle_setting/`。
**未 rm 任何檔案**（T4 只 mv）。未繼承他 feature 之 TC 內容常數。
未送出 RD-1。未填 `D5`、未組 Scope 值。未以 openpyxl 存回任何工作簿。
未生成任何 TC。
