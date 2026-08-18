# G121 —— 全量對帳表（R-P178）

> 逐 leaf 一列，見 `data/leaf_batch_reconciliation.tsv`。
> 本表為往後全部批次之範圍依據（R-P177(b)）——**批次範圍取自 Test Set 成員資格，不得以 ID 區間表述。**

## 1. 各 Test Set 合計對 §E 定版

| Test Set | §E 定版 | 實測 | 相符 |
|---|---|---|---|
| Power State | 63 | **63** | 是 |
| Startup Display | 24 | **24** | 是 |
| Branding and Theme | 16 | **16** | 是 |
| Timeout Settings | 8 | **8** | 是 |
| Power Down | 3 | **3** | 是 |
| **合計（不含留空）** | **114** | **114** | 是 |
| ＋ `SWE-PM-089`（R-P141 留空）| 1 | 1 | 是 |
| **總計** | **115** | **115** | 是 |

**G121：PASS。**

## 2. 產出狀態

| Test Set | leaf | 已產出 | 未產出 | 其中受阻斷 | 未產出且未阻斷 |
|---|---|---|---|---|---|
| Power State | 63 | 53 | 10 | 10 | **0** |
| Startup Display | 24 | 23 | 1 | 0 | **1** |
| Branding and Theme | 16 | 0 | 16 | 0 | **16** |
| Timeout Settings | 8 | 8 | 0 | 0 | **0** |
| Power Down | 3 | 3 | 0 | 0 | **0** |

## 3. 未產出且未受阻斷之 leaf —— 逐一列出（R-P181(e)）

| leaf | Test Set | 諮詢性 DR |
|---|---|---|
| `SWE-PM-077` | Branding and Theme | — |
| `SWE-PM-078` | Branding and Theme | — |
| `SWE-PM-079` | Branding and Theme | — |
| `SWE-PM-080` | Branding and Theme | — |
| `SWE-PM-081` | Branding and Theme | — |
| `SWE-PM-082` | Branding and Theme | — |
| `SWE-PM-083` | Branding and Theme | — |
| `SWE-PM-084` | Branding and Theme | — |
| `SWE-PM-085` | Branding and Theme | — |
| `SWE-PM-086` | Branding and Theme | — |
| `SWE-PM-087` | Branding and Theme | — |
| `SWE-PM-088` | Branding and Theme | — |
| `SWE-PM-090` | Branding and Theme | — |
| `SWE-PM-091` | Branding and Theme | — |
| `SWE-PM-092` | Branding and Theme | — |
| `SWE-PM-096` | Branding and Theme | — |
| `SWE-PM-112` | Startup Display | DR-PW9 |

**合計 17 leaf。**

## 4. 未產出且受阻斷之 leaf

| leaf | Test Set | 阻斷之 DR |
|---|---|---|
| `SWE-PM-001` | Power State | **DR-PW6** |
| `SWE-PM-002` | Power State | **DR-PW6** |
| `SWE-PM-003` | Power State | **DR-PW6** |
| `SWE-PM-004` | Power State | **DR-PW6** |
| `SWE-PM-005` | Power State | **DR-PW6** |
| `SWE-PM-006` | Power State | **DR-PW6** |
| `SWE-PM-007` | Power State | **DR-PW6** |
| `SWE-PM-008` | Power State | **DR-PW6,DR-PW11** |
| `SWE-PM-009` | Power State | **DR-PW6** |
| `SWE-PM-010` | Power State | **DR-PW11** |
| `SWE-PM-089` | （留空 —— R-P141） | **DR-PW1** |
