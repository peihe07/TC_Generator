# 036 現況重測（W-3）

母本：`inputs/FM-WI-FSM-036-A01 …_SWQT_CFTS044_Vehicle Controls_20260819.xlsx`
SHA256 `ebe5a65f30a0d4bcf9e46b51a43145ce222027ac49ad523fe5c2d2b6566a5089`

## 掃描條件（canon §5a 條 1／2／4／5）

- 分頁 `Test Case Specification 測試用例規範`；表頭**列 9**；資料**列 10–246**（實體列號）
- **逐列**計數，非逐引用
- 空判定：`None` 或 `strip()` 後為空字串
- 037 對照：比對前 `\s+` → 單一空格，**區分大小寫**，**全字串相等**（非子字串）

## 逐欄填充率（非空列數 / 237）

| 欄 | 名稱 | 非空 |
|---|---|---|
| B | No.# 序號 | 237 |
| D | Requirement or Design ID | 237 |
| H | Test Set | 237 |
| I | Test Item | 237 |
| L | Test procedure | 191 |
| M | Expected Result | 191 |
| N | Specification Reference | 237 |

**填充為 0 者**：`A, C, E, F, G, J, K, O, P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC, AD, AE, AF, AG, AH`

> 下放包 §5.2 之零填充清單為 `C/E/F/G/J/K/O/P/Q/R/S/T–Z/AA/AH`，
> **少列 `A` 與 `AB`–`AG`**（實測亦為 0）。數字無不符，清單不完整。

## R-VS1 之依據是否成立 —— **成立**

| 對照 | 結果 |
|---|---|
| I 欄 == 037 `Requirement Description` | **237 / 237** |
| H 欄 == 037 `Requirement Title` | **237 / 237** |
| N 欄 == 037 `Source Requirement ID` | **237 / 237** |
| D 欄值全部落在 leaf 全集內 | **237 / 237**（0 未匹配、0 重複） |

## qualifying done row

canon §2 之判準所需之 `F`（Test Case ID）欄非空數 = **0**
→ **qualifying done row = 0**，`workbook_state = BLANK`（recon 獨立判定亦為 BLANK）。

## L / M 之相異值

- L 相異 **17**；M 相異 **44**
- L 為 `Requirement is not clear…` 系列者 **12** 列，措辭 **3** 種，分布 **10 / 1 / 1**

## 覆蓋差（W-6）

leaf 全集 271 − 036 之 D 欄相異值 237 = **未覆蓋 34**
（Common Features 10／HeatedSeat 11／VentedSeat 9／Heated Steering Wheel 4）
逐條見 `data/uncovered_leaves.tsv`。
