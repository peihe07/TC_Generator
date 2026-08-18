# G188 —— `source_clause` 逐字相同之反向全批掃（R-P269）

> **本檔只掃與呈，不改值**（R-P269(d)）。
> 正規化僅空白與 NBSP（比照 R-P125(a)）。
> **與 G178 互補**：G178 由 TC 側出發（TC 相同 → 問 leaf）；本檔由規格側出發（clause 相同 → 問 TC）。

## 一、彙總

| 項 | 數 |
|---|---|
| `source_clause` 逐字相同之 leaf 群 | **6** |
| 　其 TC 集合**亦相同** | **5** |
| 　其 TC 集合**不同 —— 新形態** | **1** |
| 　　其中**錨點亦相同**者 | 1 |
| 　　其中**錨點相異**者 | 0 |

## 二、逐群

| leaf 群 | 錨點 | TC 數 | TC 集合 | 共同 TC 數 |
|---|---|---|---|---|
| `SWE-PM-054`、`SWE-PM-101` | **相同** | 4／4 | 相同 | 4 |
| `SWE-PM-055`、`SWE-PM-102` | **相同** | 2／2 | 相同 | 2 |
| `SWE-PM-056`、`SWE-PM-097` | **相同** | 1／1 | **不同** | 0 |
| `SWE-PM-068`、`SWE-PM-114` | **相同** | 1／1 | 相同 | 1 |
| `SWE-PM-070`、`SWE-PM-115` | **相同** | 1／1 | 相同 | 1 |
| `SWE-PM-080`、`SWE-PM-086` | 相異 | 2／2 | 相同 | 2 |

## 三、新形態逐群 —— clause 相同而 TC 不同（**1** 群）

> 意義：**同一規格文字產出不同之驗證** ——
> 或為刻意（不同錨點側重不同面向），或為不一致。**裁定於 40 包。**

### `SWE-PM-056`、`SWE-PM-097`

- 錨點：**相同**（1 組）
- TC 數：1／1；**共同 TC 0 條**
- `SWE-PM-056` 之 TC：`…-158`
- `SWE-PM-097` 之 TC：`…-189`
- `source_clause`（前 200 字元）：
```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```
