# 下放包 00 — Time Management：Phase 0 Intake + Scaffold

分析層 → 執行層。往返編號 `00`；對應上繳包
`features/time_management/docs/upstream/00_intake_scaffold.md`。

本包只做 Phase 0（intake 分類）與 scaffold，**不含 recon**。Phase 1 於
本包上繳並經 chat 覆核後，以下放包 01 另行下放。

> **rev B（2026-08-20）**：rev A 只給作業意圖、未給指令，且未查
> `new_feature.py` / `intake.py` 之實際 slug 推導與既存目錄行為。實查後發現
> 三項會直接使本包執行失敗或產出錯誤目錄名之事實，補為 §3 之指令序列
> 與 A-TM04 / A-TM05。**rev A 之 §3「作業指示」已被 rev B 取代，不得照 rev A 執行。**

---

## 1. 本包生效之裁決

以下為 Pei 於 2026-08-20 之裁定，逐字記錄。scaffold 完成後，執行層須將
本節整段複製進 `features/time_management/RULINGS.md`，並於
`DECISIONS.md` 以 `[PEI]` 條目引用。

```
R-TM1（Pei, 2026-08-20）—— feature 定名

feature 目錄 slug = `time_management`
feature.yaml `feature` = "Time Management"

素材四種名稱並存：
  - Pei 指定之 feature 名 = "Time Management"（本條採用）
  - spec 文件標題        = "CFTS_015 Time and Date"
  - SWRA 檔名            = "SWE1_Secure_DateTime"
  - 需求 ID family       = "TIME&DATE"（SYS-RA-TIME&DATE-* / SWE-RA-TIME&DATE-*）

「Time and Date」「Secure DateTime」「TIME&DATE」均為別名，不進目錄路徑。
ID family 之字面值當然照原樣使用於 req_id 欄與 traceability。

slug 一律小寫加底線，不得含空格 —— 依據 A-TM01 / A-TM04（見 §5）。
```

```
R-TM2（Pei, 2026-08-20）—— test_group 暫定值與其推翻條件

feature.yaml `test_group` 暫定 = "Time Management"。

本值為 [PROVISIONAL]，非最終。推翻條件（recon 時自動判定，Tier 0）：
  若 036 工作簿之 Test Group 欄（G 欄，實測為準）已存在非空值，
  則以工作簿實測值為準，直接覆寫本欄，不需再問。

理由：canon §4.1.1 之通則為 Test Group 等同 spec 文件標題（本例即
"Time and Date"），與 R-TM1 之 feature 名不同。工作簿既有值優先於兩者，
因為那是客戶已接受之欄位內容。三者若三不相同，於 Phase 2 升 Tier 2。
```

```
R-TM3（分析層自裁，2026-08-20）—— CLI 參數字面值與 anomaly 縮寫

1. `intake.py` / `new_feature.py` 之 feature 參數一律使用 `Time_Management`
   （底線，非空格）。理由見 A-TM04：兩支腳本之目錄名推導為
   `feature.lower()`，無 slugify，空格會原樣進路徑。
2. 因 (1)，scaffold 產生之 `feature.yaml` 之 `feature:` 值會是
   `"Time_Management"`，與 R-TM1 不符 —— 執行層須於 scaffold 後手動改為
   `"Time Management"`（見 §3 步驟 5）。
3. anomaly 縮寫固定為 **TM**，不用腳本推導之 `TI`
   （`abbr = feature[:2].upper()`）。理由：本包已以 A-TM01…A-TM05 落檔，
   縮寫換寫會使既有編號失效。同一形態之先例：`home` 用 `A-H`、
   `user_profiles` 用 `A-UP`，皆非腳本推導值。

本條屬「量測與作業之技術性選擇」，分析層自裁範圍；其判準與風險已於本節揭露。
```

---

## 2. 前置條件（未滿足則本包不可執行）

`_intake/Time_Management/` 尚不存在，素材由 Pei 投放。**目錄名須逐字為
`Time_Management`**（見 R-TM3）。目前已知素材三份（分析層僅見沙箱副本，
**未取得 repo 內原始 binary，故下列一切屬性均為待驗，不得引為基線**）：

| 檔名（沙箱副本所見） | 預期分類 |
|---|---|
| `R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and Date _SR26_20250909-1851.docx` | `cfts_doc` |
| `SYS2_CFTS_015_Time and Date _SR26_V1_Including_Delta_Released.xlsx` | `polarion_export`（`Basic Report` 分頁存在，應被 SHEET_SIGNATURES 命中；subtype 預期 SYS2）|
| `SWE1_Secure_DateTime.xlsx` | `swra_report`（`Analysis Report` 分頁存在）|

**尚缺、且 intake 無法自行產生者**：

1. **036 工作簿** —— 本 feature 之 FW036 客戶原件。缺此件之連鎖後果有二，
   非只是少一個檔：
   - `workbook_state` 判不出來（BLANK / PARTIAL_CLEAN / PARTIAL_INTERLEAVED / FULL）
   - `intake.py` 之 SWRA 仲裁靠 workbook 之 Scope 欄；無 workbook 時
     `pick = swras[0]`，即**以排序第一者為預設而非仲裁**。本 feature 目前
     只有一份 swra_report，故不致誤選，但 A-TM02 之身分問題因此無法由
     腳本回答，必須人工裁。
2. **037-A03 正式件** —— `SWE1_Secure_DateTime.xlsx` 之封面標 Project Name
   = `New R1L`、日期 `2020/09/05`，**與 FW036-037-A03 之標準命名不符**
   （對照 SXM：`SWE1_SXM_FM-WI-FSM-037-A03 …_20260406.xlsx`）。此件是否
   即為本 feature 之權威 037，或另有正式版，屬 §8.6 之來源權威問題 ——
   **執行層不得自行認定，登記為 A-TM02 並於上繳包回報。**
3. **Pop Up List** —— 是否被引用由 intake 之命中測試決定，不必預先索取。

036 母本不需選擇：R-G1（全域）已固定為
`forms/…_SWQT_20260817_ext.xlsx`。

---

## 3. 指令序列

**順序不可調換**，理由見 A-TM05：分析層已先建
`features/time_management/docs/handoff/` 以投放本包，而 `intake.py --scaffold`
遇既存目錄會**跳過** `new_feature.py`，隨即讀不存在的 `feature.yaml` 而
`FileNotFoundError`。步驟 3 之 `--adopt-existing` 即為此而設。

```bash
cd /Users/peihe/Work_Projects/TC_Generator

# 1) 確認素材已就位；若為空，停止並回報，不得以其他路徑之檔案代替
ls -la _intake/Time_Management/

# 2) 先分類，不 scaffold —— 看清楚再落地
python scripts/intake.py Time_Management
#    讀 _intake/Time_Management/INTAKE.md 與 intake.json，對照 §2 表列

# 3) 補建骨架（本目錄已存在，故必須帶 --adopt-existing；
#    該旗標永不覆寫既有檔案，docs/handoff/ 之本包安全）
python scripts/new_feature.py Time_Management --adopt-existing

# 4) 移檔入 inputs/ 並回填 feature.yaml 之 paths 與 spec_mode
python scripts/intake.py Time_Management --scaffold

# 5) 驗證目錄名逐字正確，且未生出含空格之孿生目錄
ls -d features/time_management
ls -d "features/time management" 2>/dev/null && echo "ABORT: 空格目錄已生成"
```

**步驟 4 之後必須手動修正三處**（腳本不會做，做完在上繳包逐項確認）：

| 檔案 | 現值（腳本產出） | 應改為 | 依據 |
|---|---|---|---|
| `feature.yaml` | `feature: "Time_Management"` | `feature: "Time Management"` | R-TM1 / R-TM3(2) |
| `feature.yaml` | `test_group: "Time_Management"` | `test_group: "Time Management"`，並加 `# [PROVISIONAL] 見 R-TM2` | R-TM2 |
| `ANOMALIES.md`、`PLAYBOOK.md` | 縮寫 `TI`（`A-TInn`） | 縮寫 `TM`（`A-TMnn`） | R-TM3(3) |

**步驟 4 之後不要跑 `recon.py`。** 本包止於 scaffold。

---

## 4. 其餘作業指示

1. 將 §1 之 R-TM1、R-TM2、R-TM3 寫入 `RULINGS.md`（逐字照錄，不改寫、
   不摘要），並於 `DECISIONS.md` 建 `[PEI]`／`[分析層自裁]` 條目引用之。
2. 將 §5 之 A-TM01…A-TM05 登記進 `ANOMALIES.md`（**登記，不裁定**）。
3. `DATA_REQUESTS.md` 之骨架由 scaffold 產出；把 §2 之「尚缺」兩項
   （036 工作簿、037 正式件）填為 Urgency = High，並註明各自阻塞哪個 Phase。
   骨架內含「每次 session opener 與 batch gate 按 Urgency 回報」之常設規則 ——
   本 feature 沿用，回報對象為本 feature 之表，不涉其他 feature。
4. intake 之回報須含：每檔之分類與判定依據（sheet 簽章／PU 欄偵測／
   text-layer 探測）、提議之 `spec_mode`、以及 **037 之 Source ID 欄能否
   推導 missing-document list**；若該欄為 component/Polarion id 而非文件名，
   明講「not derivable」，不要編一份清單。

---

## 5. 本包一併登記之 anomaly（執行層寫入 ANOMALIES.md，狀態 PENDING）

**A-TM01 — `features/` 下有孤兒 scaffold `vehicle setting`（含空格）**

實測（分析層，2026-08-20，對 repo 實際路徑）：`features/vehicle setting/`
與 `features/vehicle_setting/` 並存，兩者皆為完整 feature 目錄結構。
比對 `feature.yaml`：

| | `vehicle setting`（空格） | `vehicle_setting`（底線） |
|---|---|---|
| paths | 全為 `<FW036 xlsx>` 等佔位符 | 真實檔名 |
| spec_mode | `"A"`（模板預設） | `"D"`（00 包 W-12） |
| design_method 欄 | `Q`（模板值） | `R`（實測；Q 為 Estimated Test Time）|
| author 欄 | `Z`（模板值） | `AA`（實測；Z 為 Fastack (376) Atl-Mi）|
| `RECON.md` | 無 | 有 |

判讀：含空格者為未填之 scaffold，實跑者為底線版。**成因已由 A-TM04 查明，
非人為手滑而是工具行為。** 處置屬不可逆操作，Tier 3，執行層不得動；
建議 `mv` 入 `archive/`（比照 R-G2 不刪除慣例），待 Pei 裁。

**A-TM02 — 037 之身分未定**

`SWE1_Secure_DateTime.xlsx` 之命名與封面欄位（Project Name `New R1L`、
日期 `2020/09/05`）與 FW036-037-A03 之既有命名慣例不符。是否為本 feature
之權威 037 待確認。未確認前，**不得以其 leaf 集合作為覆蓋稽核之分母**。
本件因只有單一 swra_report，`intake.py` 不會觸發多報告仲裁，故腳本不會
自行提出本問題 —— 這是登記本條的理由。

**A-TM03 — SYS2 之 EE Architecture 欄大小寫漂移**

分析層對沙箱副本之唯讀探測（2026-08-20，量測條件：`Basic Report` 分頁，
第 2 列起共 227 資料列，取第 7 欄 `SYS2 EE Architecture (All,ATL-Hi,ATL-Mi)`
之值，區分大小寫，精確相等計數）：

```
ATL-Hi   101
All       61
ATL-Mid   55
Atl-Hi    10
```

`ATL-Hi` 與 `Atl-Hi` 為同義不同寫。**任何以字串等值篩 Atlantis High 之
腳本會靜默漏掉 10 列**，且不會報錯 —— canon §5a「詞彙型工具之缺陷不會
報錯，須以已知全集驗證」。凡涉本欄之篩選，判準須先對 227 列全集驗過再立。

同批探測另得（同一量測條件，取第 10 欄 `Category`）：
`Functional Requirement 126 / Heading 70 / Information 30 / Out of Scope 1`。
**以上兩組數字均取自沙箱副本，執行層須對 `_intake/` 之原始 binary 重測，
不得沿用。** 重測結果若與此不符，以重測為準並回報差異。

**A-TM04 — `new_feature.py` 之目錄名推導無 slugify（工具缺陷，A-TM01 之成因）**

`scripts/new_feature.py` `scaffold()`：

```python
feat_dir = root / "features" / feature.lower()
```

`.lower()` 不處理空格。`python scripts/new_feature.py "Vehicle Setting"` 即
產生 `features/vehicle setting/` —— **A-TM01 之孿生目錄由此而來，不是手滑。**
腳本不報錯、不警告，且該目錄之後續一切操作看起來都正常。

現行迴避方式已寫入 R-TM3(1)（參數帶底線）。**根本修法（改 slugify）會改變
既有 feature 之目錄名推導，屬跨 feature 影響，Tier 2，執行層不得逕改。**
提議之處置：加 slugify 並對既有目錄做一次性對照表，或至少在偵測到空格時
`sys.exit`。連帶副作用須評估：`abbr = feature[:2].upper()` 亦受參數字面值
影響（見 R-TM3(3)）。

**A-TM05 — `intake.py --scaffold` 與 `new_feature.py --adopt-existing` 之整合缺口**

`new_feature.py` 之註解明言 `--adopt-existing` 的用途是
「the analysis layer has already delivered docs/handoff/ into an otherwise-empty
feature dir」——**正是本包之形態**。但 `intake.py` `scaffold()` 為：

```python
feat_dir = root / "features" / feature.lower()
if not feat_dir.exists():
    subprocess.run([... "new_feature.py", feature ...], check=True)
...
text = yaml_path.read_text(encoding="utf-8")     # ← 目錄已存在時，此檔不存在
```

目錄已存在時直接跳過 scaffold，隨即在讀 `feature.yaml` 處
`FileNotFoundError`。亦即：**兩支腳本對「分析層先落檔」這件事的假設相反**，
一支專門設計了旗標去支援，另一支則會崩。

現行迴避方式已寫入 §3（先手動跑 `--adopt-existing` 再跑 `--scaffold`）。
提議之處置：`intake.py` 改為既存目錄時以 `--adopt-existing` 呼叫
`new_feature.py`，而非跳過。屬 Tier 2，執行層不得逕改。

---

## 6. 升級 chat 覆核之條件

以下任一發生，停止並升 Tier 2：

- `_intake/Time_Management/` 為空，或內含檔案與 §2 表列不符
- intake 分類結果與 §2「預期分類」不一致
- `spec_mode` 提議非 `D`（分析層之預期為 D：CFTS docx + SYS2 export，
  無 HMI L&F PDF；若 intake 提議 A 或其他，代表有分析層未見之素材）
- §3 步驟 5 之驗證出現含空格之目錄
- 036 工作簿缺件導致 `workbook_state` 無法判定
- §3 任一步驟之實際輸出與本包所述之腳本行為不符（代表分析層讀的是舊版腳本）

---

## 7. 上繳包須包含

1. `INTAKE.md` 與 `intake.json` 之全文或路徑
2. scaffold 後之目錄樹（一層即可）與 `feature.yaml` 全文
3. §3 之三處手動修正之逐項確認（改前／改後值）
4. §5 五條 anomaly 之寫入確認，A-TM03 之**重測數字**（對原始 binary）
5. `DATA_REQUESTS.md` 初版
6. **本包是否仍有該驗而未驗者之獨立判斷** —— 不得省略，不得寫「無」了事；
   若真無，說明是依什麼全集判定為無

---

## 8. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM1 | 裁決（Pei 已裁） | ✅ §1 |
| R-TM2 | 裁決（Pei 已裁，含 [PROVISIONAL] 推翻條件） | ✅ §1 |
| R-TM3 | 分析層自裁（CLI 字面值、feature.yaml 修正、abbr=TM） | ✅ §1 |
| A-TM01 | anomaly，PENDING，處置屬 Tier 3 | ✅ §5 |
| A-TM02 | anomaly，PENDING | ✅ §5 |
| A-TM03 | anomaly，PENDING | ✅ §5 |
| A-TM04 | anomaly，PENDING，修法屬 Tier 2 | ✅ §5 |
| A-TM05 | anomaly，PENDING，修法屬 Tier 2 | ✅ §5 |

分析層本包未動 git，未動 `_intake/`，未動任何既有 feature 目錄，未改任何腳本。
新建者僅 `features/time_management/docs/handoff/`（為投放本包所需，
其副作用即 A-TM05，已於 §3 給出迴避序列）。
