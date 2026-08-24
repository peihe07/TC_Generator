# V24 — pilot #1 v2 覆核：**不通過**（三項，皆為機械可修）

下放包 **V24**。對應上繳：`docs/upstream/V24_*.md`。
本包新增 **R-VF69**（1 條）、**W-VF62**（1 項工單）。

**本包所據之最新上繳**：`docs/upstream/V23_unblock.md`，實測於 2026-08-24；
另實測 `generated/vf230_pilot1.json` 全文十條。

---

## 1. 覆核結論：**不通過**。**三項 defect，皆為逐條字串修正，不需重跑選池**

**改善確實發生**：選池序修正後 Absent／Present 成對進入（238↔244、239↔245、
240↔246、241↔247），`reasoning` 九句各異未套版，
`specification_reference` 10/10 全解且相異，A-VF18 之處置正確
（以結論句為準、Remarks 具名不調和）。**此四項皆較 V19 版為優。**

**惟仍有三項 defect。**

---

## 2. Defect A（blocking）—— Pre-Condition 之系統預設 **10/10 未移除**

V23 §4.2 令「Pre-Condition **移除系統預設**」。
上繳 §4 稱「移除系統預設與可達性前提」。**可達性前提確已移除**（menu 之開啟
已移入 procedure 步驟 2）。**系統預設未移除**：

```
十條之 pre_conditions 第 1 項逐字：
  1. The vehicle is powered and the HU has completed start-up
```

canon §4.4 Forbidden 首例逐字為 `system defaults (HU is powered on.)`。
**「車輛已上電且 HU 已完成啟動」即該例之改寫，非其例外。**

**且其與 procedure 自相矛盾**：Pre-Condition 稱 HU 已完成啟動，
而步驟 1 為 `Power cycle the HU`、ER 1 為 `The HU completes start-up`。
**移除該項可同時解決二者。**

**修法**：刪 pre_conditions 第 1 項，僅留 PROXI 設定一項。
ER 隨 procedure 不變（步驟 1 仍為 power cycle）。

---

## 3. Defect B（blocking）—— `check whether` 為 §5.1 明列之禁用主動詞，**10/10**

```
十條之 procedure 步驟 3 逐字：
  Read the Vehicle Settings menu and check whether the ... setting is listed
```

canon §5.1 之 Forbidden verbs 逐字列有 `check whether`
（與 `observe whether`／`see if`／`confirm whether` 並列），
其理由為**將判斷推給測試者**。Preferred 為 `Check that`。

**修法**：改為 `check that the ... customer setting is not listed`（負向四條）
／`check that the ... customer setting is listed`（正向三條）。
**ER 已為確定敘述，改後 procedure 與 ER 之語氣方一致。**

---

## 4. Defect C —— `tc_title` 逾 14 字，3 條

canon §4.3 令 2–14 字。實測（以空白切分，括號與引號內之詞計入）：

| seq | 字數 | tc_title |
|---:|---:|---|
| 244 | **16** | Power Tailgate Alert is displayed and can be modified when CAN node 82 (PTGM) is "Present" |
| 246 | **15** | Lane Sense Warning is displayed and can be modified when Lane_Assist is "Active Lane Management" |
| 247 | **17** | Suspension Service Mode is displayed and can be modified when CAN node 27 (ASM / ASCM) is "Present" |

其餘 7 條為 13–14 字，合規。

**修法建議**（不強制其逐字）：正向三條改用 §4.3(c) 之情境標籤式，
其手足區辨 token 為分割值本身 —— 如
`Power Tailgate Alert displayed: PTGM = "Present"`（7 字）。
**惟情境標籤式須與已交付之 Part 1 慣例一致**，若 Part 1 無此式，
改以縮短句式為之。

---

## 5. Note 2 項（不阻塞）

1. **JSON 檔頭之計數與內容不符**：`selection` 欄稱「P0(a) 3 ／ P0(c) 7」，
   而逐條 `priority_class` 實為 **P0(a) 4 ／ P0(c) 6**
   （238／241／244／247 為 P0(a)）。上繳 §4 之表所載為 4／6，正確。
   **檔頭須改**（canon §5a：跨處之同一量須自同一來源重算）。
2. **UI 標籤未用雙引號**：procedure 與 ER 中之
   `the Power Tailgate Alert customer setting` 未加引號，
   而 seq 247 之 `test_item` 內出現 `"Suspension Service Mode"`（源自條文）。
   canon §11 令 UI 標籤用雙引號。**列為 style-divergence 而非 defect** ——
   須先查 Part 1 已交付之慣例（R-1：格式須窮盡既有範例），見 W-VF62 第 4 項。

---

## 6. R-VF69 —— 自檢項須以逐字禁止串表述，不得以概念表述

```
R-VF69（自檢項之表述形式，分析層裁定 2026-08-24）

**成因**：V23 §4.3 之自檢第 7 項為「Pre-Condition 無系統預設、
無以受測 feature 之可達性為前提」。執行層據以自檢，**回報通過**，
而十條之第 1 項系統預設**原封未動**。

**「系統預設」為概念**；實作者須自行決定哪些字串屬之，
其決定不會被檢驗。**概念型自檢項之通過，只證明實作者之解讀與其自身一致。**

**故：凡自檢項涉及禁止之內容者，須以逐字串或逐 pattern 表述**，例如：

  ✗ 「Pre-Condition 無系統預設」
  ✓ 「Pre-Condition 不得含下列 pattern：`powered`／`power on`／
     `start-up`／`booted`／`ignition on`；命中即失敗」

  ✗ 「procedure 無禁用動詞」
  ✓ 「procedure 不得含 `observe`／`observe whether`／`see if`／
     `check whether`／`confirm whether`／`verify`（主動詞位）／
     `watch`／`monitor`／`inspect`」

**本條與 R-VF11／R-VF21（錨點）互補**：錨點驗判準之區辨力，
本條驗判準之**可執行性**。**一個無法被機械執行之自檢項，
其通過與未做不可分辨** —— 此為 A-VS106 形態之第五例，
而前四例已各自立過條文。

**分析層同受拘束**：本條之成因即本層所擬之自檢清單。
凡本層於下放包中列出之自檢項，**須自問「實作者能否不加解讀即執行之」**。
```

---

## 7. W-VF62 — pilot #1 v3（**逐條字串修正，不重跑選池**）

**不重跑選池、不改 leaf 集合、不改 `specification_reference`、
不改 `reasoning` 之 Priority 段。** 僅下列五項：

1. **刪 `pre_conditions` 第 1 項**（Defect A），十條皆然。
2. **`check whether` → `check that`**（Defect B），十條皆然；
   負向四條之受詞為 `is not listed`，正向三條為 `is listed`。
   （按：正向為 244／245／246／247 四條，負向為 238–243 六條 ——
   **此數請以實測為準，本層不預設。**）
3. **縮短 244／246／247 之 `tc_title` 至 ≤14 字**（Defect C）。
4. **查 Part 1 已交付 TC 中 UI 標籤之引號慣例**（Note 2），
   逐字回報二至三個實例；**依其慣例決定本批是否加引號，不自創**。
5. **改 JSON 檔頭之 `selection` 欄計數為 4／6**（Note 1）。

**自檢依 R-VF69 改寫**：第 7 項與新增之禁用動詞項，
**皆以逐字 pattern 表述**，並實測其可失敗性
（人為插入 `The HU is powered on` 與 `check whether` 各一，檢查須失敗）。

**逐條回報修正前後之差異行**，然後上繳。**不生成第 2 批。**

---

## 8. 給 Pei

**pilot #1 v2 之 verdict**：本層分類為 **defect 3（皆機械可修）／
style-divergence 1 ／ note 1**，建議 **不通過，v3 修正後重提**。

**三項 defect 皆為逐條字串取代，不涉重跑選池或重寫邏輯** ——
其修正成本遠低於 v1→v2。

**待你裁者僅一項**：DR-35（A-VF18，`LaneSenseWarning-014` 條文自相矛盾）
之送出，與 DR-34 併同處理（R-VF27，送出屬你）。

---

## 9. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF69（自檢項須以逐字禁止串表述；與錨點條文互補；分析層同受拘束） | 分析層裁定 | ✅ §6 |

**工單**：W-VF62（pilot #1 v3，五項字串修正 ＋ 自檢改寫）。

**分析層本輪之錯**：V23 §4.3 之自檢第 7 項以概念表述，
致執行層之自檢通過而 defect 仍在（§6）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
