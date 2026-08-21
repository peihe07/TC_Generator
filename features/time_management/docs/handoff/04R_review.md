# 04R — 覆核：T5 併行覆蓋之處置、tc_id 裁定、四項閘門

分析層 → 執行層。覆核對象：`docs/upstream/04_scripts.md`。

**T1–T4 / T6 受理。T5 之處置正確 —— 不覆蓋回去是對的。**
但 §5.2 之新事實使一項認知須更新，且該項**不是我能裁的**，見 §5。

---

## 1. T3 錨點複驗 —— 九項全中，R-TM23 關閉

執行層兩度提請之未驗項，本包關閉。六項物件→章節歸屬與分析層之表逐項相符，
且陰性對照（同一解析對 `615\d{4}` 仍零命中）證明比對方法有效。

**R-TM23 兩條界線之錨點自此為雙方確認，B1 之 008/011/014 可據以撰寫。**

## 2. §6.2 之觀察 —— 立為條文

> T6 判準 6 若只數數量而不列位置，覆蓋不會被發現 —— 位置清單顯示了中文
> 行號，數量不會。

**這是本包最有價值的一句。** 判準 6 我寫的是 `| wc -l`，若非執行層自行
展開位置清單，兩份腳本被換掉這件事本輪不會浮現。

```
R-TM31（分析層自裁，2026-08-21）—— 驗證判準須輸出可歸屬之明細，不只計數

驗證步驟之輸出須足以判斷「命中者是不是我方產出」，不得只給計數。
凡以 `grep -c`、`wc -l`、`count=` 形式收尾之判準，一律改為列出命中位置
或內容片段。

理由：計數對「內容被替換但數量相同」完全不敏感。本包之 13 處
TODO(R-TM10-A1) 計數通過，而其中 11 處來自另一份非我方所寫之檔案。

本條為 R-TM4（斷言須附完整元素清單）在**驗證步驟**上之延伸：
前者管主張，本條管檢查。
```

## 3. tc_id —— 裁定（`write_back` 之硬阻塞，§6.3(3)）

執行層指出：本 feature 之 `feature.yaml` 無 `write_back.tc_id_format`，
而 tc_id 體系為 R-TM10(b) 明列之**不得援引**項，須自裁。
**在裁定前 write-back 不可執行。**

```
R-TM32（分析層裁定，2026-08-21）—— tc_id 格式

write_back.tc_id_format = "NR1L-TimeAndDate-{n:03d}"

依據：
1. canon §10.3 —— `{project}-{abbr}-{NNN}`，alphanumeric project +
   alphanumeric module abbreviation + 零填三位序號
2. project 段取 `NR1L`，與 privacy 之 `NR1L-Privacy-{n:03d}`（R-PV02）
   同 —— **此為格式結構之參照，非 TC 內容之援引**，R-TM29 界線內
3. module 段取 `TimeAndDate`，來自 R-TM8 之 Test Group `Time and Date`
   去空格。**不取 `TimeManagement`** —— 該名為內部識別，不進交付件
   （R-TM1 / R-TM8 之同一區分）

序號自 001 起，於 22 片 leaf 之全部 TC 上單調遞增，跨批次連續
（B1 用完接 B2，不重設）。

本條可撤回：B1 未生成前改之無成本。
```

## 4. 四項缺口 —— 立為閘門，不論最終由誰寫腳本

執行層列之四項缺口皆為**條文未被編碼**，非風格差異。其設計說明
（§5.4）具體且理由充分，尤以兩點：

- **D5 應有專屬之具名失敗**，而非只作為 header drift 之一列 ——
  因其有專屬條文（R-TM9-A2）與 anomaly（A-TM02a、A-TM11）
- **R-TM24 之對策應為來源隔離而非人工記得** —— 與執行層在 `03Z` §4.1
  自訂之作法一致，該作法我當時已採納

```
G-TM1（閘門，2026-08-21）—— B1 生成前，lint 層須具備四項閘門

無論最終由哪一方寫 lint_tcs.py，下列四項須存在且經 self-test 證明
可 fire（R-TM21：不能失敗的閘門不是閘門）：

1. D5 Scope 守衛 —— 寫回後 D5 仍為空，具名失敗，不與 header drift 混列
   （R-TM9-A2、A-TM02a）
2. leaf 文字來源隔離 —— test_item 上半之文字只認
   data/leaf_descriptions.txt，22 筆全集數量不符即報錯（R-TM24）
3. spec gap 閘門 —— 005 / 002 之 Remarks 為空即報 spec-gap（A-TM13）
4. 界線閘門 —— 011 / 008 / 014 各自 owns / not_ours 之訊號名表，
   TC 全文命中 not_ours 即報 boundary。訊號名一律取自 T3 已複驗之錨點
   （R-TM23、R-TM25）

現存之 build_batch_context.py（執行層版）已含 SPEC_GAP 與 BOUNDARIES
兩表，故 3、4 在 context 層有編碼，僅 lint 層缺。
context 層之編碼不能取代 lint 層 —— 前者是給生成看的，後者是驗生成的。
```

## 5. §5.2 併行者寫入本 feature —— **我不裁，呈 Pei**

執行層之三項判斷全部正確：

1. **不覆蓋回去** —— 再寫一次只會重演，且可能覆蓋對方進行中之工作
2. **不構成須立即介入之風險** —— 現存版 `wb.save(` 零命中，
   未走 openpyxl 存回路徑，母本 x14 下拉安全
3. **孰優非執行層可單方認定** —— 對方版本可能有執行層未見之考量

第 3 點我要補強：**不能預設我方版本較好。** Pei 之偏好明載程式碼註解用
繁體中文，現存之中文版在這點上更貼近；且對方可能已知本 feature 之某些
決定。四項缺口是客觀可查的缺漏，但那不等於整份較差。

```
A-TM20（PENDING，Tier 3 —— 呈 Pei，本包不推進）

A-TM17 已 RESOLVED（Pei 確認併行者為其自己開啟之另一 session），
但當時三項登記事實之作業範圍**皆在 features/vehicle_setting/**。

本次為**首次觀察到併行者寫入 features/time_management/**：

| 腳本 | 執行層所寫 | 現存 | 特徵字串 `Structure ported from` |
|---|---|---|---|
| write_back.py | 351 行，英文 | 214 行，中文 | 0（非執行層）|
| lint_tcs.py | 312 行，英文 | 301 行，中文 | 0（非執行層）|
| build_batch_context.py | 222 行，英文 | 222 行，英文 | 1（執行層）|

覆蓋發生於 09:13–09:14。**執行層之兩份內容已不存於磁碟，無備份。**

推定（未證實，須 Pei 確認）：Pei 於另一 session 對同一 feature 指派了
相同或相近之工作。

**本條不由分析層裁定** —— 「哪一個 session 擁有 features/time_management/」
是資源分配問題，非技術判斷，只有 Pei 能答。

在 Pei 裁定前之保全措施（分析層逕行，逆轉成本為零）：
  - features/time_management/scripts/ 凍結：不寫入、不覆蓋、不修改任一行
  - 對該目錄之作業一律唯讀
  - 分析層不再下放任何寫入 scripts/ 之指令
```

## 6. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM31 / R-TM32

標題行 `## R-TM31 — 驗證判準須輸出可歸屬之明細，不只計數`、
`## R-TM32 — tc_id 格式`，內文為 §2 / §3 之區塊全文。
追加後 `## R-TM` 條數應為 **35**。

### T2 — `ANOMALIES.md`：新增 A-TM20；`RULINGS.md`：新增 G-TM1

A-TM20 內容為 §5 之區塊全文。索引追加：

```markdown
| A-TM20 | 併行者寫入本 feature，兩支腳本被覆蓋且內容失落 | PENDING | Tier 3（呈 Pei）|
```

索引條數 19 → **20**。

G-TM1 內容為 §4 之區塊全文，寫入 `RULINGS.md` 之末尾，
標題行 `## G-TM1 — B1 生成前 lint 層須具備四項閘門`。
（G-series 與 R-series 同檔，不另立檔案。）

### T3 — `feature.yaml`：加 tc_id_format

於 `write_back:` 段下加：

```yaml
  tc_id_format: "NR1L-TimeAndDate-{n:03d}"   # R-TM32
```

若該段不存在則建之。**不動 scripts/ 任何檔案**（A-TM20 凍結）。

### T4 — 現存兩支腳本之唯讀全文評估

**只讀，不改，不執行。** 逐支回報：

1. **全文讀完後**，其 TODO(R-TM10-A1) 標記之位置與內容，逐處判定標記是否
   恰當（是否確為 TC 內容常數而非結構）—— 執行層 §5.6(3) 自陳未複核，
   本步驟補之
2. G-TM1 四項閘門，逐項判定現存版**有／無／部分**，附 grep 證據
   （**依 R-TM31 列位置或片段，不只計數**）
3. `write_back.py` 是否有 tc_id_format 缺失之顯式攔截（§6.3(3)）
4. 現存版是否含任何**他 feature 之 TC 內容常數**（步驟措辭、ER 樣板、
   Test Set 值、priority 預設）—— R-TM29 界線之檢查

**發現他 feature 內容常數即回報並標記，不自行移除**（凍結中）。

### T5 — 驗證（依 R-TM31，全部列明細不只計數）

```bash
grep -n '^## R-TM3[12]' features/time_management/RULINGS.md
grep -n '^## G-TM1'     features/time_management/RULINGS.md
grep -n '^| A-TM20'     features/time_management/ANOMALIES.md
grep -n 'tc_id_format'  features/time_management/feature.yaml
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 35
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 20
git status --short features/time_management/scripts/        # 應無輸出（凍結）
```

### T6 — 上繳

`docs/upstream/04R_corrections.md`。須含 T5 全部輸出、T4 之四項逐支評估、
**本包是否仍有該驗而未驗者之獨立判斷**（明列全集）。

### 不得執行者

- 不動 git
- **不寫入、不覆蓋、不修改 `features/time_management/scripts/` 任一行**（A-TM20）
- 不執行任何腳本（含 `--self-test`）
- 不生成任何 TC
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 7. 呈報 Pei —— 一個問題

**`features/time_management/` 由哪一個 session 負責？**

09:13–09:14 另一 session 覆蓋了本 session 所寫之 `write_back.py` 與
`lint_tcs.py`，內容已失落無備份。兩個 agent 持續寫同一目錄必然重演。

我需要的只有一句：**是本 session 繼續，還是交給另一個 session。**

- 若本 session 繼續 → 請停用另一邊對此 feature 之作業，我補上 G-TM1
  四項閘門
- 若交給另一邊 → 我把 G-TM1、R-TM32、五條界線、A-TM13 缺口清單整理成
  一份交接單，本 session 轉為唯讀覆核

在此之前 `scripts/` 凍結，`05`（B1 生成）不下放 —— 生成需要那三支腳本，
而歸屬未定時生成物同樣會被覆蓋。

其餘待你之項（不阻塞）：R-TM10-A1 替代樣式來源（仍無候選）、
RD-1 Q-TM1–3 送出、A-TM18 Comfort 之 (a)/(b) 判定。

## 8. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM31 | 分析層自裁，判準須列明細 | §2 | ✅ T1 |
| R-TM32 | 分析層裁定，tc_id 格式 | §3 | ✅ T1 + T3 |
| G-TM1 | 閘門，B1 生成前之必要條件 | §4 | ✅ T2 |
| A-TM20 | anomaly，PENDING，Tier 3 | §5 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未觸 `vehicle_setting/`。
