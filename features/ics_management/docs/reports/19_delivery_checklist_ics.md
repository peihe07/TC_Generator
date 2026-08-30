# 作業 D-1 — `DELIVERY_CHECKLIST.md` 之 ICS 條目逐項對照｜2026-08-30

**本表為交付前之現況對照，非出貨授權。** IN §8.4.3 不變（R-ICS54(a)）。

## §1 逐項對照

| 項 | 現況 | 判 |
|---|---|---|
| TC 總數 | **31** | — |
| Test Set 相異值 | **5**（Volume Control／Browse Control／Display Control／Menu Navigation／Stuck Button）| — |
| 錨行 | **65**（相異 ObjectID 38：CFTS020 31 ＋ CFTS022 7）| — |
| `verify_verbatim` | **31／31** | PASS |
| `selfcheck`（機檢 19 項）| FAIL **0** | PASS |
| `verify_reference_binding` | **11／11 MATCH** | PASS |
| `pending_census` | **6 處／6 條** | **未清空** |
| 母本 sha256 | `6372fb6b…fb825b2`，與 `feature.yaml` 宣告相符 | PASS |
| x14 DV（R10:R1411）| `xlsx_surgical` 實測保留（E43 未觸發）| PASS |
| **TC ID** | **json 中不存在**（E42 觸發）| **阻斷** |
| 工作簿 GUI 驗證 | **未做 —— 屬 Pei 之手動項** | 待 |
| `delivered/` ＋ MANIFEST.tsv | **未產出** —— 屬 `--write` 之後、tag 之前 | 待 |
| `lint_docs036` | 既有紅，成因在 `features/power/DATA_REQUESTS.md` | 具名不修 |

## §2 PENDING 6 處及所繫 DR

| # | tc_title | 欄位 | DR | 缺件 |
|---|---|---|---|---|
| 1 | Three detents rotated clock-wise | `pre_conditions` | **DR-ICS4** | `CFTS019 volume level range` |
| 2 | Knob 2 signals acted on by the HU | `pre_conditions` | **DR-ICS6** | `HMI Logic and Flow browse mapping for ICS_KNOB2` |
| 3 | Enter button pressed | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow screen mapping for Enter_Button` |
| 4 | Knob 2 rotated on a scrollable screen | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow scroll mapping for ICS_KNOB2` |
| 5 | Knob 2 rotated on a tuner source | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow tune mapping for ICS_KNOB2` |
| 6 | Back button pressed | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow screen mapping for Back_Button` |

**6 處全部在 `pre_conditions` 欄**；繫於二個 DR：**DR-ICS6（5 處）** 與 **DR-ICS4（1 處）**。
依 R-ICS54(a) **原樣寫入，不降轉、不留白、不臆填**。

## §3 不可出貨之 4 條及所繫 DR

| 標號 | tc_title | 所繫 |
|---|---|---|
| V1 | VOLUME knob rotated clock-wise | **DR-ICS9** |
| V2 | VOLUME knob rotated counter clock-wise | DR-ICS9 |
| V3 | Three detents rotated clock-wise | DR-ICS9 |
| B5 | Three detents counted in one rotation | **DR-ICS2** |

**其中 V1／V2 無任何佔位**（V3 之 1 處佔位繫 DR-ICS4，非其阻因；B5 亦無佔位）——
故 `pending_census` 不報、`selfcheck` 全綠。**只有本表與凍結記錄 §2／§3 會提醒。**

**四條依令仍寫入工作簿**（依現狀寫回），**工作簿內不加任何註記**。

## §4 Excel GUI 驗證（**手動項，屬 Pei**）

執行層**未做**，具名如下。已知須以 GUI 確認之項（來自母本結構之實測）：

- R 欄（`Test Case Design Methods`）之 **x14 下拉**於 GUI 中是否仍可展開
  —— `xlsx_surgical` 之 DV 計數檢查只驗數量與 sqref，**不驗 GUI 可用性**；
- P／Q 欄（`P10:Q1411`）、T～Z 欄、AF 欄之 classic 下拉；
- 換行字元於儲存格內之呈現（本 feature 之 `test_procedure`／`expected_result` 皆為多行）；
- 中文表頭與英文內容混排之欄寬與截斷。

## §5 並行寫入對 sha 可信度之影響（R-ICS54(f)）

**本 session 期間 repo 有持續之並行寫入**，實證三項：

1. `canon_refs` 之計數於本 session 內由 **445 → 446 → 459 → 460 → 473 → 478**，
   而**執行層每輪之新檔於其 unresolved／ambiguous 報表中皆 0 命中**（b16／b17／b18 各驗一次）；
2. 掃描檔數由 **2523 → 2574**；
3. 分析層五簿之數輪變更於 `git status` 中已不顯示為未提交，
   表示**由並行 session 先行提交**（b17／b18 之 commit 均具名此事）。

**含意**：作業 C 產出之工作簿 sha256，**只在產出當下對其自身有效**；
它不保證「產出時 repo 之其他部分」與 tag 時相同。
**`verify_reference_binding` 之 11／11 是對 11 個參考件之保證，不是對 repo 全域之保證。**

**建議**（不裁）：`--write` 與 tag 之間若相隔任何時間，**tag 前應重跑一次 `verify_reference_binding`**。
