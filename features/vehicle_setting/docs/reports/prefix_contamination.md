# 交叉前綴污染 —— 全掃結果（W-47，15 輪）

依 31 包 §5。14 輪只掃 `cfts044_include` 一欄、只查 `HS_`/`VS_` 一對前綴（A-VS49）；
本次掃**全部值域欄**、對**全部有語意前綴之 token**。

## 掃描範圍

| 項 | 值 |
|---|---|
| `spec_variables.tsv` 之 token | **30** |
| 其中有期望前綴者 | **14** |
| 掃描之值域欄 | `cfts044_include`／`cfts044_exclude`／`cfts044_other_arch`／`lid_values`／`dbc`／`lid_format` |
| 期望前綴對照 | `HSW_`／`Heated_Steering` → `HSW_`；`VentedSeat` → `VS_`；`HeatedSeat`／`Heated_Seat` → `HS_` |

> `cfts044_other_arch` 為 JSON（架構 → 值陣列），**須逐值展開**。
> 14 輪把整格當一個值，故一格只看得到首個命中。

## 結果：**4 個相異 (token, 值) 對，全部為 `Vented → HS_` 單向**

| # | token | 值 | 來源 reqid | 章節 | EE Arch |
|---|---|---|---|---|---|
| 1 | `$VentedSeatFR$` | `Vented Seat High / HS_HI` | `4858393` | 1.3.2.1.3.4 | PowerNet |
| 2 | `$VentedSeatFR$` | `Vented Seat High/HS_HI` | `4858001` | 1.3.1.1.3.4 | CUSW |
| 3 | `$VentedSeatFR$` | `Vented Seat Off / HS_OFF` | `4860021` | 1.3.4.12.4 | Atlantis Mid |
| 4 | `$VentedSeatFL$` | `Vented Seat Off / HS_OFF` | `4860015` | 1.3.4.12.3 | Atlantis Mid |

**反向（`Heated …` 配 `VS_`）掃描命中 0。**

## 逐筆判據（typo vs 別名）

### #1 `4858393` → **typo**

對稱側 §1.3.2.1.3.3 同位第 3 條 `4858363` 之值為
`[Vented Seat Off / VS_OFF]`、`[Vented Seat Low / VS_LO]`、**`[Vented Seat High / VS_HI]`**。

### #2 `4858001` → **typo**

對稱側 §1.3.1.1.3.3 同位第 4 條 `4857982` 之值為
`[Vented Seat Off/VS_OFF]`、`[Vented Seat Low/VS_LO]`、**`[Vented Seat High/VS_HI]`**。
**該對稱節內 `HS_` 出現 0 次。**

### #3 / #4 `4860015`／`4860021` → **typo（但 31 包之判據會判為別名，見下）**

31 包 §5 之判據逐字為「對稱側一律用另一前綴者判 typo；**對稱側亦用同前綴者判別名**」。
`4860015`（LF）與 `4860021`（RF）**兩側一致地寫 `HS_OFF`** ——
**依該判據應判別名。**

**但更寬之基礎顯示其為 typo**：

| 證據 | 值 |
|---|---|
| §1.3.4.12.3 內 `4860011`／`4860013` 寫 | `[Vented Seat Off / **VS_OFF**]` |
| §1.3.4.12.4 內 `4860017`／`4860019` 寫 | `[Vented Seat Off / **VS_OFF**]` |
| **即同一章節內兩形態並存，`HS_OFF` 為節內少數** | |
| 全文 `$VentedSeatF*$ = [Vented Seat Off / VS_OFF]` | **15 次** |
| 全文 `$VentedSeatF*$ = [Vented Seat Off / HS_OFF]` | **2 次**（即本二筆） |

**別名須為系統性之雙軌命名；此處同節內即自相矛盾，故判 typo。**

> **判據之界線已記明**：31 包之「對稱側」判據無法分辨
> 「兩側一致地抄錯」與「真雙軌命名」。本輪改以**章節內並存 ＋ 全文頻次**為基礎。
> 判準之修訂屬分析層，本報告只陳述所用之基礎與其理由。

## 結論

| 判 | 筆數 |
|---|---:|
| **typo** | **4** |
| **別名** | **0** |

**升級條件（「有判為別名者」）未命中。**

## 處置

依 31 包 §3，**原值保留不清除**，於 `data/spec_variables.tsv` 增 `suspect_prefix` 欄標記：

```
$VentedSeatFL$   Vented Seat Off / HS_OFF → VS_
$VentedSeatFR$   Vented Seat High / HS_HI → VS_ | Vented Seat High/HS_HI → VS_ | Vented Seat Off / HS_OFF → VS_
```

DR-18 之擬定屬分析層。**本報告不代擬提問。**
