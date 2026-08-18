# G114 —— G103 全量掃描（R-P162）

> 對**全部 115 leaf** 執行 G103：自 037 之 `Source Requirement ID` 獨立重算
> token → SYS2 → item id，與 `layer3_full.tsv` 之 `item_ids` 比對。
> **未讀 layer3 之任何中間產物**（R-P144(a)）。**未自行補齊 layer3**（R-P162）。

## (a) 不相等之 leaf —— **2 / 115**

| leaf | 037 token 數 | 重算 item 數 | layer3 item 數 | **layer3 缺** | layer3 多 |
|---|---|---|---|---|---|
| `SWE-PM-008` | 13 | 17 | 14 | **4941425、4941430、4941433** | — |
| `SWE-PM-010` | 8 | 8 | 7 | **4941984** | — |

其餘 **113 leaf 全數相等**；全量之 unresolved token 為 **0**。

## (b) 被丟棄之 item 於兩份 CFTS 文字層之存在情形

| item id | 所屬 leaf | CFTS009 / CFTS010 文字層之內文段落 | 判讀 |
|---|---|---|---|
| `4941425` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941430` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941433` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941984` | `SWE-PM-010` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |

**四個被丟棄之 item 全部於文字層不存在** —— 非「有內文而章節解析失敗」，
而是 **037 → SYS2 所指之 item id 在 CFTS 文件裡根本沒有對應之需求錨點**。
`build_layer3` 以「item → 章節」為索引建表，該等 item 因無章節而**靜默丟棄**，
`layer3_full.tsv` 遂少載，`source_anchor` 隨之少列，而 **G94 與 G99 皆會全綠**。

## (c) 與既有 anomaly / DR 之關聯

| 既有項 | 關係 |
|---|---|
| **A-PW02 / DR-PW3**（`4942087` 無法解析至任一 CFTS 章節）| **同型之最早一例** —— 當時判為「錨點鏈之缺口」，未查其內文是否存在。本次四例證明該形態會**靜默改變 `source_anchor`**，其後果較當時所評估者嚴重 |
| **DR-PW11**（`4941984`，22 包開）| 本次擴大為 **4 個 item / 2 個 leaf**，已併入該 DR |
| **DR-PW6**（`SWE-PM-001`–`009` 之懸空 `WrapperResource`）| `SWE-PM-008` 同時受此二者影響 —— 其 TC 於 DR-PW6 與 DR-PW11 皆解之前無法產出 |

**執行層未自行補齊 layer3**（R-P162 明令）。
