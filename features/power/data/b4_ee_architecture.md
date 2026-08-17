# B4 — 被引用 item 之 EE Architecture 分布（R-P40）

> 母體：**238 個被引用 item**（經 `layer3_full.tsv` 之 `item_ids` 欄）。
> 車型（`Radio`）軸已於 04 包驗畢無虞（全為 `allSys` 或含 `R1L`，零例外）。
> 產生指令：`python features/power/scripts/build_b4_b5.py`

## 1. 值域與計數

| EE Architecture 值組 | item 數 |
|---|---|
| `Atlantis High, Atlantis Mid` | **162** |
| `All` | **61** |
| `Atlantis Mid` | **13** |
| `Atlantis High, Atlantis Mid, CUSW, PowerNet` | **1** |
| `Atlantis High` | **1** |
| **合計** | **238** |

相異值：`All`、`Atlantis High`、`Atlantis Mid`、`CUSW`、`PowerNet`

**無 `EE Architecture` 欄者：0 個。**

## 2. 與 FW036 c21–c27 七個車型欄之對照

| 欄 | 標頭（實測） | 世代 |
|---|---|---|
| c21 | `HDCC27 Atl-Hi` | Atlantis High |
| c22 | `DT27 Atl-Hi` | Atlantis High |
| c23 | `VF(ProMaster)637 Atl-Mi` | Atlantis Mid |
| c24 | `Commander (598) Atl-Mi` | Atlantis Mid |
| c25 | `Regengade (5210) Atl-Mi` | Atlantis Mid |
| c26 | `Toro(2261) Atl-Mi` | Atlantis Mid |
| c27 | `Fastack (376) Atl-Mi` | Atlantis Mid |

七欄之世代分布：**Atl-Hi 2 欄**、**Atl-Mi 5 欄**。

## 3. 明確回答：是否存在被引用 item 其 EE Architecture 不含本專案適用之值

本專案為 R1L（R-P2），FW036 七個車型欄橫跨 Atlantis High（2 欄）與 Atlantis Mid（5 欄）。

**答：不存在「兩世代皆不含」者。**

- 兩世代通用（`All` 或同時含 High 與 Mid）：**224** 個
- **`Atlantis Mid` 單值：13 個** —— 僅適用 Atl-Mi，不適用 Atl-Hi 兩欄
- **`Atlantis High` 單值：1 個** —— 僅適用 Atl-Hi，不適用 Atl-Mi 五欄

即 224 / 238 兩世代通用，14 個為單世代專屬。

### 3.1 單世代專屬 item 清單

**`Atlantis Mid` 專屬（13）**：`4941453`, `4941587`, `4941692`, `4941693`, `4941695`, `4941706`, `4941707`, `4941708`, `4941768`, `4941784`, `4941814`, `4941815`, `4941817`

**`Atlantis High` 專屬（1）**：`4941588`

**含非本案世代值者（1）**：`4941301`

### 3.2 逐 leaf 之 EE Architecture 聯集僅含單一世代者

114 個 leaf 中：**2** 個

| leaf | EE Architecture 聯集 |
|---|---|
| `SWE-PM-057` | `Atlantis Mid` |
| `SWE-PM-095` | `Atlantis Mid` |

> **登記**：01 包 §F 已載 FW036 c21 標頭 `HDCC27 Atl-Hi` 沿用 A-PV15（世代落差、入 RD-1、不自行對應）與 R30-3 / R30-4（車型欄留白）。本檔僅提供實測分布，**不改變該政策，也不建議如何填欄**。
