# 表 A —— FROP 跨域揭露（Vehicle Category）

> **出貨門檻二表之一**（R-VC3）。缺之不得出貨。

- 編製：`scripts/build_table_a.py`，下放包 27 T142
- 來源：`FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx` 第 8 欄 `FROP (Feature Rollout Plan)`，**逐列讀，非抽樣**
- **本表不引用任何既有敘述之數字** —— 承 REV-14，全部重測


---

## 0. 母體標註（R-VC15）

本表涉及**二個母體**，其數字**不得互援**：

| 母體 | 定義 | 大小 |
|---|---|---|
| **145 列** | 037 `Analysis Report` 之全部資料列（含 parent）| 145 |
| **117 leaf** | 其中之 leaf（R-VC3 全取）| 117 |

### 0.1 FROP 分布 —— 二母體並列

| FROP | 145 列母體 | 117 leaf 母體 |
|---|---|---|
| `Audio Management` **（跨域）** | 1 | 1 |
| `Power Management` **（跨域）** | 16 | 12 |
| `Vehicle Settings` | 128 | 104 |
| **合計** | **145** | **117** |

**歸屬域**：`Vehicle Settings`（117 leaf 中 104 筆，
145 列中 128 筆）—— 本表之「跨域」即指 FROP ≠ 此值。

**FROP 欄無空值** —— 145 列全部有值，故跨域之判定不涉缺值處置。

### 0.2 ⚠ 兩個 17，落在不同母體（R-VC15／R-VC17）

| 量 | 母體 | 值 |
|---|---|---|
| 跨域**列**數 | 145 列 | **17** |
| 跨域 leaf 所產出之 **TC** 數 | 120 TC（六批合計）| **17** |
| 跨域 **leaf** 數 | 117 leaf | 13 |

**前二者皆為 17，而它們不是同一件事** —— 一個是 037 的列、
一個是本專案產出的測試案例。**其相等為巧合，不得互援、不得據以主張對應。**

`DECISIONS.md` 簽署時所載之「145 列中之 17 列」即上表第一列，**該標註正確**。
本節之設立是因為第二個 17 是本輪新算出來的 —— **REV-11／REV-14 兩次教訓
都始於兩個相同的數字**，故在它們出現時即標明。


---

## 1. 跨域 leaf 逐筆（117 leaf 母體）

**13 leaf → 17 TC。**

| req_id | section | FROP | Test Set | 批次 | P | TC 數 | TC 標題 |
|---|---|---|---|---|---|---|---|
| `VC-048-02` | 12.3.2 | **Audio Management** | Settings List | `batch2_settings_list` | P2 | 2 | 1. Confirmation tone plays on a settings change<br>2. Exception settings play no confirmation tone |
| `VC-057` | 13.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Settings tab unavailable in three ignition states |
| `VC-058-01` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Pop-up on a blocked Settings tab attempt |
| `VC-058-02` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P2 | 1 | 1. Blocked-tab pop-up does not time out |
| `VC-058-03` | 13.1.1 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P2 | 2 | 1. Closing the blocked-tab pop-up with X<br>2. Closing the blocked-tab pop-up with OK |
| `VC-059-01` | 13.2 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Phone settings reached through the Phone screens |
| `VC-059-02` | 13.2 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Phone settings available in Key Off and ACC |
| `VC-060-01` | 13.3 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Audio settings reached through the Media |
| `VC-060-02` | 13.3 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Audio settings available in Key Off and ACC |
| `VC-061` | 13.4 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Software Updates available in Key Off and ACC |
| `VC-064-01` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 2 | 1. Transition to Key Off with the Settings tab open<br>2. Transition to ACC with a Settings category open |
| `VC-064-02` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 1 | 1. Transition pop-up neither times out nor closes |
| `VC-064-03` | 13.5 | **Power Management** | Ignition Availability | `batch5_ignition_availability` | P1 | 2 | 1. Returning to Run clears the transition pop-up<br>2. Returning to Key On clears the transition pop-up |

---

## 2. 對照 —— 章 13 之 FROP 組成（REV-14 之標的）

下放包 24 §3.1 曾稱「章 13 之 FROP = Power Management **全批**」，
**實測不成立**。REV-11／REV-14 已記其成因（母體混用）。本節為表 A 之佐證欄。

| 母體 | 章 13 之組成 |
|---|---|
| 145 列 | 22 列 —— {'Power Management': 16, 'Vehicle Settings': 6} |
| **117 leaf** | **16 leaf —— {'Power Management': 12, 'Vehicle Settings': 4}** |

**章 13 之 `Vehicle Settings` 四筆逐筆具名**（即使其非跨域，仍列此以杜絕再次反推）：

- `VC-062-01`（§13.4.1） —— When the user presses 'Software Downloads Over Wi-Fi' while the …
- `VC-062-02`（§13.4.1） —— When the user presses OK or X on the in-motion popup launched fr…
- `VC-063-01`（§13.4.2） —— When the vehicle starts moving while the user is mid-flow in FOT…
- `VC-063-02`（§13.4.2） —— When the user presses OK or X on the in-motion popup launched fr…

**R-VC16(e) 之正確讀法**：`Power Management` 之 16 **列**全部落在章 13
（該命題在列母體上成立）；**其逆命題「章 13 全為 PM」在 leaf 母體上不成立**。


---

## 3. 已知限制（R-G8）

- **FROP 值取自 037 第 8 欄，未與任何 FROP 主檔核對** ——
  本表只能證明「037 這樣寫」，不能證明「FROP 計畫確實如此分派」。
  **DR-VC5（FROP 跨域 17 列之承接單位）仍未結**，其回覆可能改變本表之解讀。
- **`Test Set` 取自 `data/test_set_map.tsv`**（framework §2 之 8 組）——
  若 DR-VC3 回覆為「應補」，章 8／9 另立 `Cabrio Rooftop` 將使組數變 9，
  **本表之 `Test Set` 欄須重編**（R-VC16(c)）。
- **TC 數為本輪之實測**（六批 JSON 之 `tcs`）。尾段 6 leaf 未生成者標
  `(未生成)`，其 TC 數為 0 —— **非「該 leaf 不需 TC」**。
- 本表**未涵蓋 `Vehicle Settings` 之 104 筆** —— 依定義它們非跨域。

