# 上繳 V06 —— 627 落實、`not clear` 之停下、「已交付」三判準之實測

執行層寫入。依據：`docs/handoff/V06_scope_close.md` §5（3 項工單）。canon §8.2 六節。

**本輪未生成任何 TC，未寫回任何工作簿，未改任何既有分級，未改任何 AH 欄。**

> **編號**：本檔依 R-VF10 之新制（`V{NN}_`）落於 `docs/upstream/`。
> V04 §3.2 所令之既有檔改名（`61_`→`V01_`／`62_`→`V02_`）**本輪未執行** ——
> 該屬 W-VF13，且併行 session 正於 `docs/upstream/vf230/` 另行重整目錄，
> 兩者同時動會互相覆寫。**見 §6。**

---

## 1. 交付總表

| 工單 | 狀態 | 產物 |
|---|---|---|
| W-VF16「已交付」判準之證據（**先行**） | **完成（未擇一）** | 本檔 §2 |
| W-VF17 627 落實 ＋ Layer 2 重算 ＋ 619 清單 | **完成** | `data/vf230_leaves.tsv`（627）、`scripts/vf230_leaves.py`、本檔 §3–§4 |
| W-VF14 修訂為存查性 | **完成（未觸發變更）** | `docs/reports/wvf14_vcrit_registry.md`、`scripts/vf230_wvf14_registry.py` |
| 條文落檔 | **完成** | `RULINGS.md` +R-VF14／15／16（逐字） |
| DR-30 | **完成（未送出）** | `DATA_REQUESTS.md` |
| anomaly | **完成** | +A-VF2 |

---

## 2. W-VF16 —— 「已交付」之三判準（只列證據，未擇一）

**量測條件**：(a) 對交付路徑
`.../Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 ..._20260819.xlsx`，
分頁 `Test Case Specification 測試用例規範`，列 10–246 逐欄計非空；
(b) `generated/batch*.json`，各批取最高版次，取 `tcs[].leaf_id` 之聯集；
(c) `docs/reports/writability.tsv` 之 `layer3` 含 `HeatedSeat`／`VentedSeat`
且不含 `SteeringWheel` 者。

| 判準 | 定義 | leaf 數 | 範圍 |
|---|---|---:|---|
| **(a)** | 已寫回交付路徑並 tag | **0** | 見下之逐欄實測 |
| **(b)** | 已生成之批次 | **119** | batch01–08、10–16（15 批；batch09 無檔、batch12 之 TC 為 0） |
| **(c)** | 已於 RD-1 送出 | **158** | Heated Seat ＋ Vented Seat |

**(a) 之逐欄實測（獨立複驗，與 V06 §5.2 相符）**：

```
F 測試用例ID 0 ／ G Test Group 0 ／ J 先前條件 0 ／ K 輸入條件 0
O TC Ref ID 0 ／ P Priority 0 ／ R Design Method 0 ／ AA 作者 0 ／ AH 備註 0
（L 191 ／ M 191 為進場時即有之上游文字，非本 pipeline 產出）
```

→ **交付路徑之工作簿不含任何本 pipeline 產出之 TC。**

**(c) 之數為 158 而 RD-1 自述 160**，差 2 —— 該 2 未入 `writability.tsv`。
本層未追其身分（不在本包範圍）。

### 2.1 三判準對 R-VF14 第 3 項給出**同一答案**

R-VF14 第 3 項令 A-VS118 之 4 leaf「以其是否已交付為斷」。實測：

| leaf | (a) | (b) | (c) |
|---|---|---|---|
| `HeatedSteeringWheelManagement-029` | 否 | 否（TC 0 條） | 否 |
| `HeatedSteeringWheelManagement-030` | 否 | 否 | 否 |
| `HeatedSteeringWheelManagement-033` | 否 | 否 | 否 |
| `HeatedSteeringWheelManagement-034` | 否 | 否 | 否 |

(c) 判否之理由：RD-1 之標的為 `$FL_HS_RQ$`／`$FR_HS_RQ$`／`$FL_VS_RQ_TGW$`／
`$FR_VS_RQ_TGW$`（Heated／Vented **Seat**，160 leaf），
**`HeatedSteeringWheelManagement` 不在其內**。

→ **「已交付」之判準無論裁為 (a)(b)(c) 何者，該 4 leaf 皆為「未交付」。**
R-VF14 之排除效力於此 4 leaf 上不成立。

**惟本層未改其分級** —— R-VF14 第 4 項令「不作全面回溯重跑」，
且 W2→W0 之轉換為分級變更，非本層可自裁。**W2／`B6-value-absent` 維持。**

---

## 3. W-VF17 —— 627 落實

**依 R-VF11 先驗錨點，錨點相符方套用於全集**：

```
必命中錨點    A-VS132 之 8 個 swe_id                實測 8    ✅
必不命中錨點  037 判 Heading 且 035 亦判 Heading 之列  實測 118  ✅
兩集相交       0                                              ✅
提列後之集合   與必命中集逐一相等                              ✅
```

```
037 總列 745
  037 判 Functional              619
  ＋ R-VF16 提列（disagree=1）      8
  ────────────────────────────────────
  可測 leaf 母體                 627
  餘 heading                     118
```

`data/vf230_leaves.tsv` 新增 **`disagree` 欄**：該 8 列為 `1`，其餘 619 列為 `0`。
**未靜默併入**（R-VF16 之要求）。

**逐份分報告之 leaf 數變動**：僅 `6 Aux Switches, SWITCH 1 Power Mode and
E-Save features` 一份，**64 → 72**；其餘十份不變。

---

## 4. Layer 2 重算 —— **簇數與交集皆不變**

V06 §5.3(2) 之預期為「8 列集中於 SWITCH 族，非隨機散布，簇分布必變」。
**實測：分布變，簇數與交集不變。**

```
簇數        106 → 106      （新簇 0、消失 0）
交集        exact 104 ／ 無對應 2  →  exact 104 ／ 無對應 2
leaf 合計   619 → 627
```

**逐簇差異 —— 8 個既有簇各 +1，全為 SWITCH 族**：

| 簇 | 619 版 | 627 版 |
|---|---:|---:|
| SWITCH 3 Power Mode | 5 | 6 |
| SWITCH 3 Type | 5 | 6 |
| SWITCH 2 Hold Last State | 5 | 6 |
| SWITCH 3 Hold Last State | 5 | 6 |
| SWITCH 6 Power Mode | 2 | 3 |
| SWITCH 5 Type | 2 | 3 |
| SWITCH 6 Type | 2 | 3 |
| SWITCH 6 Hold Last State | 2 | 3 |

**粒度 D（037 之 11 份分報告族群）**：11 個候選不變，
僅 `6 Aux Switches…` 由 64 → **72**（21.2%→ 相對序位不變，仍為第 4）。

→ **Layer 2 起點之判斷不因 627 而變。** V06 §6 所稱「簇數須依 627 重算後
方有實數可據」之條件**已滿足**：實數為 106 簇／104 exact／11 族群。

---

## 5. W-VF17(3) —— 以 619 為母體之既有陳述（列出，**未改**）

全庫命中 **18 檔**，逐檔計數：

| 檔 | 次 | 類 |
|---|---:|---|
| `docs/upstream/vf230/00_intake.md` | 15 | 上繳（併行 session 所建） |
| `docs/upstream/vf230/01_recon.md` | 7 | 同上 |
| `docs/reports/vf230_crosscheck.md` | 5 | 本線產物 |
| `docs/handoff/V06_scope_close.md` | 5 | 下放包 |
| `ANOMALIES.md` | 5 | 條文簿 |
| `scripts/vf230_crosscheck.py` | 4 | 本線腳本 |
| `docs/handoff/V05_scope_and_vcrit.md` | 3 | 下放包 |
| `docs/handoff/V04_numbering_separation.md` | 3 | 下放包 |
| `DATA_REQUESTS.md` | 3 | 條文簿 |
| `scripts/vf230_leaves.py` | 2 | 本線腳本（已含 627 之說明） |
| `scripts/vf230_layer2.py` | 2 | 本線腳本 |
| `feature.yaml` | 2 | 設定 |
| `docs/reports/w120_verification_criteria.md` | 2 | 本線產物 |
| `docs/handoff/63_test_group_ruling.md` | 2 | 下放包 |
| `scripts/vf230_w120_vcrit.py` | 1 | 本線腳本 |
| `docs/reports/vf230_layer2_candidates.md` | 1 | 本線產物（已重生為 627） |
| `docs/reports/vf230_dr_impact.md` | 1 | 本線產物 |
| `RULINGS.md` | 1 | 條文簿 |

**一律未改**（V06 §5.3(3)）。其中多數之 `619` 為**當時之正確量測**，
非錯誤 —— 改之會使歷史紀錄失真。須改者僅為**現行有效之陳述**，
該判斷須逐句為之，不在本包範圍。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **R-VF15 所令之 AH 欄轉錄未施行，且其與 R-VF14 之關係未明。**
   R-VF15 令 104 個 `not clear` leaf 於 Remarks 逐字記之。VF230 尚無 TC；
   **Part 1 之該類 leaf 中已生成 TC 者，補記 AH 欄是否算「變更已交付之 TC」
   （R-VF14 第 1 項）？** 二條文對此無交集規定。**本層停下待示，未動任何 AH 欄。**

2. **V04 §3.2 之改名（W-VF13）未執行，且現有三套並存之路徑。**
   `docs/upstream/61_vf230_intake.md`（本線原檔）／
   `docs/upstream/vf230/00_intake.md`＋`01_recon.md`（併行 session 所建）／
   本檔 `docs/upstream/V06_scope_close.md`（V04 新制）。
   **三者同時存在，且前二者內容相近而不相同。**
   本輪未動 —— 改名與目錄重整同時進行會互相覆寫。**須先定何者為準。**

3. **RD-1 之 (c) 判準得 158 而其自述 160，差 2 未追。** 不在本包範圍。

4. **W-VF14 存查表之 14 列中，VF230 側 9 列之「現行分級」一律為 `—`** ——
   VF230 尚無 `writability` 產物，故該 9 列之存查價值目前只有「知其存在」，
   無法對照分級。VF230 之分級產出後須回填。

**另有一項為 R-VF11 立法後之首次驗證**：本輪 W-VF14 之判準 (c) 初版
命中 0（A-VF2），**若當時依 R-VF11 附錨點即可在落筆時發現**。
R-VF11 之必要性因此獲一次正面驗證 —— 但**本層自身在寫該判準時亦未附錨點**，
即該條文尚未進入本層之作業慣性。建議於 PLAYBOOK 明列為每次判準之必要步驟。
