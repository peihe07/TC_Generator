# 上繳包 02 —— Vehicle Category 裁定落地（T10–T18）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層 / Pei
- 對應下放：`docs/handoff/02_rulings.md`
  （SHA256 `210b6e913d008370531e25edcf6f5c833d971a3a88efd19072043689976f361f`，16,499 B）
- 前一包上繳：`docs/upstream/01_intake_recon.md`（含 §9 後記）
- **結論：T10–T18 九項全數完成，無停點。T12 為 30/30 `=`，Phase 1 收斂。**
- 未產出任何 TC、未寫回工作簿、未進入 Phase 2、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T10 | 抄錄 R-VC6~R-VC10 | ✅ 五條逐字；連同 R-VC1~R-VC5 共**十條全部 byte-level diff 通過** |
| T11 | ANOMALIES 異動 | ✅ A-VC1 撤銷；A-VC5/6/7 RESOLVED；A-VC8 新立；A-VC2/4 依 §四補裁定 |
| T12 | T4 重新收斂 | ✅ **30 項全 `=`，≠ 0 項** |
| T13 | R-VC8 修 `recon.py` | ✅ comfort 四件產出**逐字不變**；本 feature 不再崩潰 |
| T14 | 重跑 recon | ✅ 三件全產出；assertion **3/3 PASS**；TSV 錨點欄 **145/145 逐字相符** |
| T15 | `recon_assertions` | ✅ 刪二鍵，留二鍵，補三判準並存之註解與揭露義務 |
| T16 | `paths` / `reference` | ✅ 二檔複製入 `inputs/`（雜湊前後相同）；`reference:` **六項**；排除四項已註 |
| T17 | 18 節逐節重驗 | ⚠️ **相符 13 / 部分不符 2 / 無法判讀 3** —— 詳見 §7，有實質發現 |
| T18 | 四欄可用性盤點 | ✅ 四欄皆 **117/117 覆蓋、117 個相異值**，非樣板 |

**一項須你先看**：T17 查出 §15 之 11 個 EPB PU id 與 §10.1／10.2 之
「Type / Power Source / Last State 四種組合」**在 repo 之權威素材中並不存在**
—— 它們只在圖裡。下放包 01 §4.2(b) 與 §五 T6 之措辭皆預設它們是文字。
見 §7.3。

---

## 1. T10 —— 抄錄與逐條核對

抄入位置：`features/vehicle_category/RULINGS.md`。

R-VC6 之抄錄有一次**更正**：上繳包 01 §9 曾依對話中之條文先行落條，
其文字與下放包 02 §二之正式條文不同（正式版為四項拘束 (a)–(d)，
且明文「在該裁定落地前，priority 欄不得產出」）。
本輪以下放包 02 之正式條文**整段取代**，不留混合版本。

**核對方法**：以 `sed -n '<a>,<b>p'` 自下放包抽出原段 → 正則自
`RULINGS.md` 取回同名 code fence → `diff -q` 逐位元組比對。非目視。

| 條 | RULINGS.md 行 | 來源 | bytes | lines | sha256(前16) | 逐字一致 |
|---|---|---|---|---|---|---|
| R-VC1 | 14 | 包01 35–58 | 1,311 | 24 | `2344769c6998db1e` | **是** |
| R-VC2 | 43 | 包01 62–86 | 1,262 | 25 | `12c10f107cbe85ca` | **是** |
| R-VC3 | 73 | 包01 90–113 | 1,145 | 24 | `8dd3cbfa7fb69053` | **是** |
| R-VC4 | 102 | 包01 117–143 | 1,361 | 27 | `b7aeb14a67bf05d8` | **是** |
| R-VC5 | 134 | 包01 147–164 | 1,026 | 18 | `de1debf16da7e164` | **是** |
| R-VC6 | 157 | 包02 84–109 | 1,617 | 26 | `28119d9877a36cf3` | **是** |
| R-VC7 | 188 | 包02 113–129 | 957 | 17 | `2d74bfedacce38ee` | **是** |
| R-VC8 | 210 | 包02 133–159 | 1,612 | 27 | `39087f49494aa651` | **是** |
| R-VC9 | 242 | 包02 163–193 | 1,619 | 31 | `71ef7e57c6fd6308` | **是** |
| R-VC10 | 278 | 包02 197–227 | 1,749 | 31 | `bd8b65d4acc0c457` | **是** |

**十條全部逐字一致。**

---

## 2. T11 —— ANOMALIES 異動

| A | 現況 | 依據 | 檔內位置 |
|---|---|---|---|
| A-VC1 | **撤銷** | R-VC6 | `## A-VC1`（行 21）—— 原文與重測表保留為軌跡，標明不再具效力 |
| A-VC2 | PENDING（附於 DR-VC2）| 包02 §四 | 行 85；裁定「不單獨發 DR」已逐字記入 |
| A-VC3 | PENDING（併入 DR-VC3）| 不變 | 行 103 |
| A-VC4 | PENDING（全域排程）| 包02 §四 | 行 114；「繞開不是壓制」之理由逐字記入 |
| A-VC5 | **RESOLVED** | 包02 §一 | 行 150 |
| A-VC6 | **RESOLVED** | R-VC8 | 行 216 |
| A-VC7 | **RESOLVED** | R-VC7 | 行 271 |
| A-VC8 | **PENDING（新立）** | 包02 §三 | 行 313，條文逐字抄錄 |

A-VC5 之成因已依下放包 02 §一改寫 —— 原記為「未量測斷言」，
正解為**分析層之全稱斷言未經全表掃描**：量測程式只取索引
`0, 1, 3, 5, 6, 7, 8` 七欄，索引 `9`–`17` 未被讀取過一次。
「不是量錯，是根本沒量」已記入。

> **一處自我更正**：本輪首次寫入時，A-VC7 之裁定段因字串替換錯置
> 落到 A-VC2 段內。已於同輪修回 —— A-VC2 現載其自身之裁定（不單獨發 DR），
> A-VC7 現載 R-VC7 之裁定。已逐段複查確認無其他錯置。

---

## 3. T12 —— T4 重新收斂（30 項全表）

第 23 項之基準已由 R-VC6 取代下放包 01 §3.3。`t4_remeasure.py` 之該項
改測 R-VC6 所裁之形態：**117 leaf 皆有實質內容 ∧ 28 個有子之父為 `\xa0`
∧ 欄 16／17 之該 28 列中恰有 3 列為 None（VC-034／052／063）**。
其餘 29 項之判準未動。

```
$ python features/vehicle_category/scripts/t4_remeasure.py
```

| # | 項目 | 基準 | 實測 | 判 |
|---|---|---|---|---|
| 1 | Analysis Report 資料列數 | 145 | 145 | = |
| 2 | 資料列起始列號 | 8 | 8 | = |
| 3 | 資料列結束列號 | 152 | 152 | = |
| 4 | 父需求 `SWE1-HMI-VC-NNN` | 66 | 66 | = |
| 5 | 子需求 `SWE1-HMI-VC-NNN-MM` | 79 | 79 | = |
| 6 | 形態外之 id | 0 | 0 | = |
| 7 | 父需求無重號（相異數）| 66 | 66 | = |
| 8 | 父需求連號（min, max）| (1, 66) | (1, 66) | = |
| 9 | 父需求跳號數 | 0 | 0 | = |
| 10 | 有子之父（不入 leaf）| 28 | 28 | = |
| 11 | 無子之父（本身即 leaf）| 38 | 38 | = |
| 12 | leaf 全集 | 117 | 117 | = |
| 13 | Categorization = Functional Requirement | 145 | 145 | = |
| 14 | Release Version = 1.00.00 | 145 | 145 | = |
| 15 | FROP = Vehicle Settings | 128 | 128 | = |
| 16 | FROP = Power Management | 16 | 16 | = |
| 17 | FROP = Audio Management | 1 | 1 | = |
| 18 | Sub Categorization = HMI | 103 | 103 | = |
| 19 | Sub Categorization = Service | 42 | 42 | = |
| 20 | Source Requirement ID 相異值 | 61 | 61 | = |
| 21 | HMI Source ID 相異值 | 66 | 66 | = |
| 22 | Verification Method 起首一致（117 leaf）| 117 | 117 | = |
| 23 | **第 10–18 欄符合 R-VC6 所裁之形態（欄數）** | **9** | **9**（九欄全符）| **=** |
| 24 | SYS1 Basic Report 資料列（列 2–110）| 109 | 109 | = |
| 25 | 有效 Outline Number | 108 | 108 | = |
| 26 | 037 HMI Source ID → SYS1 命中 | 66 | 66 | = |
| 27 | 命中但不在 SYS1 者 | 0 | 0 | = |
| 28 | `SYS-HMI-RA` 於 SYS1 全簿出現次數 | 0 | 0（三分頁逐頁 0/0/0）| = |
| 29 | 引用章節數 | 66 | 66 | = |
| 30 | 未引用章節數 | 42 | 42 | = |

```
30 項；≠ 0 項
```

**30/30 `=`。** 第 30 項之 42 節清單亦逐項核對，與下放包 01 §4.2(a) 24 節 +
(b) 18 節之組成完全相符（清單見上繳包 01 §3）。

---

## 4. T13 —— `recon.py` 之 R-VC8 修法與回歸

### 修法（`scripts/recon.py`，+23 −1）

依 R-VC8(a)，於 `survey_a03()` 新增 `citations: dict[str, str]`，
在解析 citation 之處**同時保留 `first` 之原值**，並隨回傳值送出：

```python
citations: dict[str, str] = {}
...
first = raw.split("\n")[0].strip()
if first:
    citations[rid] = first          # R-VC8(a)
m = re.match(r"^(?P<stem>.+)_(?P<sec>\d+(?:\.\d+)*)$", first)
```

**未**以 `stem + "_" + sec` 還原 —— R-VC8(a) 明文禁止，且理由在本 feature
即成立：其 stem 以 `..._Post_2A_(December_27_2023)` 結尾，
`.+_\d+(\.\d+)*$` 之貪婪切點在該形態下會取錯。

於 `emit()` 之 TSV 產生處：

```python
tpl = cfg.get("spec_reference_template", "{outline}")
citations = a03res.get("citations", {})
for rid in sorted(a03res["sections"]):
    ...
    ref = citations.get(rid, "") if tpl is None else tpl.replace("{outline}", sec)
```

依 R-VC8(b)，**未宣告該鍵之 feature 走原本之 `dict.get` 預設值路徑，
行為不變**。`recon.py` 之其他行為一律未動。

### 回歸證據一 —— 既有 feature 逐字不變（R-VC8(c)）

取 `comfort`（其宣告 `spec_reference_template` 為非 null 字串，
正好走「不得改變」之那條路徑；且其 `DECISIONS.md` 已簽署，
可一併確認 R-C9 之拒寫行為不受影響）。

修法前後各跑一次 `python scripts/recon.py --feature features/comfort --root .`：

| 產出 | 修法前 sha256(前16) | 修法後 | 判 |
|---|---|---|---|
| `RECON.md` | `e6ced08f22013b63` | `e6ced08f22013b63` | **逐字不變** |
| `data/recon.json` | `ff6fc7565f29f365` | `ff6fc7565f29f365` | **逐字不變** |
| `data/recon_leaf_to_section.tsv` | `a0eb8a51f9f712c6` | `a0eb8a51f9f712c6` | **逐字不變** |
| `DECISIONS.new.md` | `9a156b615939a60b` | `9a156b615939a60b` | **逐字不變** |

兩次皆正確觸發 `REFUSED (R-C9)`（comfort 之 `DECISIONS.md` 已簽署，未被覆寫）。
**回歸後 comfort 之工作區已還原**（`git status --porcelain features/comfort`
輸出為空；`DECISIONS.new.md` 已刪、三份既有檔以修法前之快照覆回）。

### 回歸證據二 —— 本 feature 不再崩潰

見 §5。

---

## 5. T14 —— 重跑 recon（本 feature）

```
$ python scripts/recon.py --feature features/vehicle_category --root .
assertions:
- PASS — leaf count == Functional Requirement rows: expected 145, measured 145 — categorization distribution: {'Functional Requirement': 145}; the banned id-suffix criterion would have selected 79 (66 parent-shaped requirements dropped)
- PASS — distinct spec sections after citation parse: expected 66, measured 66 — 0 citation cells carry extra lines below the section (Polarion item ids), not parsed
- PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0 — 66 cited / 108 outline entries in the export
recon complete: state=BLANK, leaves=145, sections=66, targets=145
NOTE (A-TM15): .../DECISIONS.md already exists and was NOT overwritten. The fresh survey is at .../DECISIONS.new.md — diff and merge by hand.
decisions written to: .../features/vehicle_category/DECISIONS.new.md
EXIT=0
```

### assertion 逐項

| assertion | expected | measured | 判 |
|---|---|---|---|
| `functional_requirement_count` | 145 | 145 | **PASS** |
| `distinct_spec_sections` | 66 | 66 | **PASS** |
| cited sections not in ruled outline | 0 | 0 | **PASS** |

**3 checked / 0 failed。** `distinct_spec_sections: 66` 依 R-VC9 之授權
（「由執行層於重跑後確認其 PASS 再定去留」）**保留** —— 該鍵有實作、
本輪 PASS，是本 feature 目前唯一機器護住的錨點數字，刪之無益。

### 三件產出

| 檔 | 大小 |
|---|---|
| `data/recon.json` | 19,140 B |
| `data/recon_leaf_to_section.tsv` | 29,000 B（145 資料列）|
| `DECISIONS.new.md` | 2,607 B（`DECISIONS.md` 已存在，依 A-TM15 之守則改寫此檔）|

### R-VC8 之產出驗證

TSV 第 4 欄（`spec_reference`）與 037 `HMI Source ID` 欄原值逐列比對：

```
TSV 資料列: 145
第 4 欄 ≠ 037 原值者: 0
第 4 欄為空者: 0
樣本: SWE1-HMI-VC-001 | SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_(December_27_2023)_2.2
```

**145/145 逐字相符，零空值。** 錨點為全名而非光禿章節號 —— R-VC8 所要之結果。

> `DECISIONS.md` 仍為 scaffold 樣板，未被覆寫（A-TM15 之既有守則，非缺陷）。
> `DECISIONS.new.md` 之採納屬 Phase 2 之 Tier 2 事項，執行層不自行合併。

---

## 6. T15 / T16 —— `feature.yaml`

### T15（R-VC9）

```yaml
recon_assertions:
  functional_requirement_count: 145
  distinct_spec_sections: 66      # 保留：該鍵有實作，T14 重跑 PASS
```

`leaf_count: 117` 與 `uncovered_content_sections: 18` **已刪除**。
註解中逐字記入 R-VC9 之依據（「宣告一個不被讀取的鍵，比不宣告更糟」）、
揭露義務（117 與 18 僅靠 T4／T12 重測與上繳交叉檢查守護，非機器保證），
以及 leaf 判準三者並存之事實（145 / 117 / 79，並註明 display 未暴露此分歧
因其 037 三值恰皆為 8）。

### T16（R-VC10）

二檔複製入 `inputs/`，來源 `forms/` 未變：

| 檔 | 大小 | mtime | SHA256（複製前＝複製後＝來源複測） |
|---|---|---|---|
| `Pop Up List HMI R1 (26PI).xlsx` | 2,951,835 B | 2026-08-25T13:51:21 | `ff47b7be63e5824cafe35deda9f9ddd0a63f6ea458169ef73689a1c559ea13ea` |
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | 295,635 B | 2026-08-25T09:15:30 | `41daac0048d2afe15fe9aeee52a6197a28efdd2a71da44d2b836b4da3e9d4cf9` |

```yaml
paths:
  popup_list:    "inputs/Pop Up List HMI R1 (26PI).xlsx"
  settings_list: "inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx"
```

`reference:` 經 YAML 載入實測為 **六項**：
`a03_report` / `sys1_export` / `spec_pdf` / `workbook_master` /
`popup_list` / `settings_list`。三份 forms 類綁**原件**而非 `inputs/` 複本
（R-VC10 之「擇一並註明」已於註解記明；理由：原件變動才是要偵測的事件）。

「明文排除四項」（`dbc_b` / `dbc_fd` / `lid` / `proxi`）之註解已寫入，
含其依據與「少綁是裁定，不是遺漏」之落款。「本無第七項」亦已記明。

---

## 7. T17 —— 18 節逐節重驗（R-VC7）

### 7.1 權威素材之選擇與其限制

R-VC7 指定以 repo `inputs/` 之 PDF 重驗。實測該 PDF 之文字層**不足以承擔
此任務**：28 頁中 10 頁（p9–p18）與 4 頁（p24–p27）之文字層僅存投影片
標題與頁碼（25–55 字元），需求句本身在圖內。目標 18 節之章節號在文字層之
出現次數幾乎全為 0。

故改以**二重來源**：

1. **SYS1 Polarion export 之 `Description` 欄**（repo `inputs/`，
   SHA256 `1fcc8711…b091d6`）—— 逐 outline 帶完整需求文字，
   且其 `SYSRE_HMI_Source ID` 已於 T4 驗明對 037 命中 66/66。**主要依據。**
2. **repo PDF 之文字層**（`3a6752c8…776a76`）—— 佐證，並用以標定
   哪些內容確實只存在於圖。

> 揭露：SYS1 export 為規格之**結構化匯出**，非規格本身。二者若有落差
> （FO §3 之 Mode A 盲點：匯出可能靜默漏句），本法看不見。
> 但在本案它嚴格優於 PDF 文字層 —— 後者連句子都沒有。

### 7.2 逐節結果

| 節 | 下放包 01 §4.2(b) 之摘要 | 權威素材所載 | 判 |
|---|---|---|---|
| 8.1 | A1/A2 長按開闔全程、3D 動畫 | 「push and hold (for entire operation) button A1／A2」「graphic popup (3D render animation)」 | **相符** |
| 8.2 | 放開即停 | 「If user release the button … the rooftop stops」 | **相符** |
| 8.3 | （摘要未涵蓋）| 「A graphic representation of the vehicle status will be present on pop up」 | **摘要漏列**（非錯，是不完整）|
| 8.4 | 車速 < 50 km/h、最長 15 s、VF507 | 「Car speed below 50 kmlh (see VF507)」「up to 15s (see VF507)」 | **相符** |
| 8.5 | 故障時控制灰化 | 「The roof controls are greyed if the system detect a fail」 | **相符** |
| 9.1 | B1/B2 長按升降 | 「push and hold button B1／B2」 | **相符** |
| 9.2 | 放開即停於任意位置 | 「the window will stop to the user desiderate position」 | **相符** |
| 10.1 | 進入路徑 Controls | 「The flow of pressing the Aux settings from Controls」 | **相符** |
| 10.2 | 進入路徑 Apps | 「The flow of pressing the Aux settings from Apps」 | **相符** |
| 10.1／10.2 | **「Type / Power Source / Last State 之四種組合、Last State 之可用條件（Latching + Ignition）」** | **不存在** —— SYS1 該二節僅存 `(image: image9–12.png)` 與「Refer to the HMI Settings list」「All four Aux switches … simultaneously」 | **無法判讀**（內容在圖）|
| 11.9 | （通則標題）| 「General logic for setting with options」 | **相符** |
| 11.9.1 | 多選項列之按壓語意 | 「pressing on option currently not selected … move the selection」「already selected … do not perform action」 | **相符** |
| 11.9.2 | 單選項列、駕駛分心之整列行為 | 「on/off setting … select/deselect」「For driver distraction the same behavior … entire row area」 | **相符** |
| 11.9.3 | +/- 之增減與端值灰化 | 「increment or decrement …」「At max values + greys out, at min values - greys out」 | **相符** |
| 14.2 | 彈窗優先序 E-Call → 來電／簡訊 → System Errors → EPB Service Mode → System Feedback | 「E-Call  Incoming Call /Text Message System Errors EPB Service Mode  System Feedback (e.g. Mute Pop-up)」 | **相符**（順序逐字一致）|
| 15 | **「PU0132 / 0133 / 0134 / 0136 / 0139 / 0141 / 0143 / 0144 / 0145 / 0202 / 0275 之訊息文字與逾時」** | **不存在** —— SYS1 該節僅存標題 + `(image: image20–22.png)`；PDF p25–p27 文字層僅存投影片標題 | **無法判讀**（內容在圖）|
| 16.1 | Widget 內之車頂／擋風板操作 | 「Refer to the Vehicle Category - Cabrio Rooftop and Cabrio Wind Draught Deflector HMI sections for complete logic.」 | **部分不符** —— 其為**交叉引用**，非該節自身之實質需求內容 |
| 16.2.1 | Widget 內之車頂開闔 | 「Open／Close rooftop operation … button A1／A2 … graphic popup on cluster」 | **相符** |
| 16.2.2 | Widget 內之擋風板 | 「push and hold button B1／B2」 | **相符** |

**計：相符 13 節／部分不符 2 節（10.1+10.2 之細節、16.1）／
無法判讀 3 節（10.1、10.2、15 之關鍵內容）／另 8.3 為摘要漏列。**

（10.1／10.2 同時列於「相符」與「無法判讀」—— 其**節之標的**相符，
其**摘要所述之細節**不可得。二者為同節之兩個層次，故分列。）

### 7.3 實質發現 —— 有兩處摘要描述了 repo 素材中不存在的文字

1. **§15 之 11 個 EPB PU id**。下放包 01 §4.2(b) 記其為「訊息文字與逾時」，
   §五 T6 亦以「規格 §15 之 11 個 EPB PU id」為前提指派查詢。
   實測：該 11 個 id **不在 SYS1 之 `Description`，亦不在 repo PDF 之文字層**。
   01 包 T6 之 11/11 命中係查 `forms/Pop Up List HMI R1 (26PI).xlsx` 所得
   —— 那是**由 id 反查彈窗表**，不是**從規格取得 id**。
   即：那 11 個 id 的出處，在 repo 內無法追溯。
2. **§10.1／10.2 之「Type / Power Source / Last State 四種組合」與
   「Last State 之可用條件（Latching + Ignition）」**。同樣不在權威素材中。

二者之共同形態：**分析層讀了圖**（其附件為衍生 PDF，可能帶 OCR 或以視覺
判讀），而 repo 內之權威素材把那些內容留在 `(image: imageNN.png)` 佔位後面。

**這不是 A-VC7 之重複** —— A-VC7 是「附件與 repo 為不同檔」，已 RESOLVED；
本項是其**後果**：依 R-VC7，衍生物之判讀不得作為判準來源，
而這兩處摘要正是那樣的判讀。故：

- DR-VC3 對 §15 與 §10.1／10.2 之提問，已改為「該節內容僅存於圖，
  SYS1 匯出未帶文字」，**不引述任何摘要文字**（已寫入 `DATA_REQUESTS.md`）。
- 表 B 之該三節同樣不得寫入摘要文字。
- **若 Phase 4 需要 §15 之彈窗細節或 §10 之 Aux 組合表，
  現有素材不足**，須另取 —— 這是一個新的素材缺口，不是既有 DR 之子項。
  是否立 DR-VC6 請你裁（本輪未立）。

### 7.4 §4.2(a)／(b) 之分類本身

16.1 之內容為交叉引用而非實質需求，嚴格說其歸入 (b)「有實質規格內容」
可議。**未自行改分類** —— 42 節之總數與 24／18 之切分為 R-VC3 表 B 之
母體，變更屬 Tier 2。僅回報。

---

## 8. T18 —— 欄 11／13／15／17 可用性盤點

母體：117 個 leaf。

| 欄 | 表頭 | 覆蓋 | 相異值 | 中位字數 | 最短 | 最長 | 固定起首 |
|---|---|---|---|---|---|---|---|
| 11 | Description/Action for Feasibility | **117/117** | **117** | 325 | 259 | 508 | `Achievable for this rule —`（117/117）|
| 13 | Description/Action for Impact | **117/117** | **117** | 360 | 295 | 554 | `For this rule —`（117/117）|
| 15 | Description/Action for Risk Factor | **117/117** | **117** | 250 | 168 | 460 | `Risk is {Low\|Medium} for '…'` |
| 17 | Description/Action for Reusable | **117/117** | **117** | 328 | 262 | 511 | `Reuse is {High\|…} (≥50%) for '…'` |

**四欄皆逐 leaf 有值，且 117 個值全部相異 —— 不是樣板複製。**

### 可直接引用之句

四欄之每一格皆內嵌該 leaf 之 `Requirement Title` 全文（單引號夾住）。
逐字包含檢查：

```
欄11: Requirement Title 逐字出現於該欄者 117/117
欄13: 117/117
欄15: 117/117
欄17: 117/117
```

> 更正：本項首次以正則 `'([^']{10,})'` 擷取引號內字串時得「相同 82／
> 相異 35」。該 35 筆為**正則假陽性** —— 標題內含 `user's` 之撇號與
> 巢狀引號（如 `the literal string 'Controls'`）會使擷取提早結束。
> 改以子字串包含檢查後為 **117/117**。以後者為準。

### 對 Phase 4 之可用性判讀（僅陳述，不裁）

- 欄 11／13 之後半為**理由句**（「as a configuration-level extension of
  the existing … pattern; no new platform integration is required」），
  形態穩定，適合作 `reasoning` 之素材。
- 欄 15／17 之後半為**逐條差異化之判斷**（風險為何 Low／Medium、
  重用度為何 High），117 筆各不相同，資訊密度最高。
- 四欄皆以 `Requirement Title` 為錨，故可與 leaf 一對一接合，
  不需另建對應表。
- **未實作任何抽取**（Phase 4 之資料建置不在本輪範圍）。

---

## 9. 未結清單

### DR（`DATA_REQUESTS.md`）

| DR | 狀態 | 本輪異動 |
|---|---|---|
| DR-VC1 | **未結** | 無 |
| DR-VC2 | **未結** | 併入 A-VC2 之封面一問（包02 §四）|
| DR-VC3 | **未結** | 措辭依據改為 T17 之重驗結果；§15／§10.1／10.2 之提問改寫 |
| DR-VC4 | **未結** | 無（條件性，待 DR-VC3）|
| DR-VC5 | **未結** | 無 |

五筆全未結。DR 由 Pei 發出（Tier 3），本輪未發送。

### A（`ANOMALIES.md`）

未結三筆：**A-VC2**（附於 DR-VC2）、**A-VC3**（併入 DR-VC3）、
**A-VC4**（全域排程）、**A-VC8**（工具修法，不得併入 R-VC8）—— 共四筆。
已結四筆：A-VC1（撤銷）、A-VC5 / A-VC6 / A-VC7（RESOLVED）。

### 待裁

1. **R-VC6(a) 之 priority 映射**（High/Medium/Low → P0–P3）。
   R-VC6(a) 明文「在該裁定落地前，priority 欄不得產出」——
   這是 Phase 4／6 之硬前置。
2. **§7.3 之素材缺口**：§15 之彈窗細節與 §10 之 Aux 組合表在 repo 內
   不可得。是否立 DR-VC6。
3. **16.1 之 (a)/(b) 分類**（交叉引用 vs 實質內容），影響表 B 之 18 節總數。
4. **A-VC8 之修法時程**（`leaf_count` assertion）。在其落地前，
   117 與 18 之守護仍非機器保證（R-VC9 之揭露義務，本節即為履行）。

---

## 10. 量測條件揭露（R-G8）

### 通則

同上繳包 01 §7 之通則（openpyxl `read_only=True, data_only=True`；
U+00A0 先轉半形再 strip；集合比對逐字；`shasum -a 256`）。

### T12

- 腳本 `features/vehicle_category/scripts/t4_remeasure.py`，只讀不寫，
  任一 `≠` 即 `exit(1)`；本次 `exit(0)`。
- 第 23 項之新判準為**三個條件之合取**（filled 集合恰等於 117 leaf 集合
  ∧ nbsp ∪ none 恰等於 28 個有子之父 ∧ none 恰為指定之 3 筆且僅於欄 16／17）。
  **偽陽性風險**：以集合相等而非計數相等判定，故「數目對但成員錯」會被抓到；
  但若 R-VC6 之條文本身抄錯了成員，本判準會忠實地跟著錯。
  條文之成員已於上繳包 01 §9.3 獨立驗過（列 70／118／142）。
- 其餘 29 項之判準與 T4 完全相同，未因收斂而放寬。

### T13

- 回歸對象為 `comfort` 之四個產出檔，比對為 `diff -q` 逐位元組。
  **偽陽性風險**：comfort 走的是 `tpl` 非 null 之路徑，
  **不覆蓋 `tpl` 為 null 之新路徑** —— 新路徑之正確性由本 feature 之
  145/145 逐字比對背書（§5），二者合起來才是完整證據。
- 未對其餘 11 個 feature 重跑。依 R-VC8(b)，未宣告該鍵者走原路徑，
  程式碼上該路徑未變（`cfg.get` 之預設值分支逐字未動）——
  這是**靜態論證**，不是實測。若你要實測覆蓋，須逐一重跑。

### T17

- 主要依據為 SYS1 export 之 `Description` 欄；佐證為 repo PDF 之
  `pymupdf` 文字層（28 頁逐頁字元數已量，總 18,750 字元）。
- **偽陽性風險（重要）**：SYS1 為結構化匯出而非規格本身。
  FO §3 明列 Mode A 之盲點 —— 匯出可能靜默漏句，且項目層級之 diff
  看不見。故「相符」之 13 節應讀作「**與 SYS1 所載相符**」，
  不是「與規格原件相符」。
- 「無法判讀」之判定依據為 `Description` 內出現 `(image: imageNN.png)`
  佔位且無對應文字。此為**保守判定** —— 寧可標無法判讀，
  不以圖檔名推測其內容。
- 未使用任何 OCR、未對圖作視覺判讀。若採用之，即重蹈 R-VC7 所禁之路徑。

### T18

- 覆蓋率以「該格 strip 後非空且非 `\xa0`」計；相異值以精確字串集合計。
- 逐字包含檢查為 `title in cell`，大小寫敏感、不正規化空白。
  **偽陽性風險**：若某 title 為另一 title 之子字串，包含檢查會對錯的
  那格也回報命中。已查 —— 117 個 title 兩兩互不為子字串。
- 「固定起首」之統計以 `—` 切分後取前 46 字元，僅供形態描述，
  非判準。

---

**T10–T18 全數完成，無停點。未自行進入 Phase 2。**
