# B2 —— R-P135 三對成對錨點之屬性逐欄原值（R-P143）

> **不摘要、不歸納**。屬性取自 CFTS 本文錨點標頭（R-P17 文字層）。
> **執行層未裁定合併或排除**（20 §I）。

## 1. 逐欄原值

| 屬性 | `4941727` | `4941728` | `4941729` | `4941730` | `4941735` | `4941736` |
|---|---|---|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | LTM, ETM, RRM | RRM, ETM, LTM | LTM, ETM, RRM | RRM, LTM, ETM |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High |
| Market | All | All | All | All | All | All |
| Model Year | （無此欄） | 2017 | （無此欄） | 2017 | （無此欄） | 2017 |
| Radio | allSys | allSys | allSys, noSys | allSys | allSys, noSys | allSys |
| **State** | **Under Review** | **Under Review** | **New** | **Under Review** | **New** | **Under Review** |

## 2. `State` 值（本條特別要求）

| 錨點 | `State` | 對 |
|---|---|---|
| `4941727` | **Under Review** | 第 1 對 |
| `4941728` | **Under Review** | 第 1 對 |
| `4941729` | **New** | 第 2 對 |
| `4941730` | **Under Review** | 第 2 對 |
| `4941735` | **New** | 第 3 對 |
| `4941736` | **Under Review** | 第 3 對 |

## 2.1 SYS2 匯出之 `All_Accepted` 是否即 `State` 過濾（R-P143 之附帶回報）

> **否 —— 二者不是同一件事。**

| 項目 | 實測 |
|---|---|
| SYS2 匯出檔名 | `SYS2_CFTS_009_…_Polarion_uploaded_**All_Accepted**_04_13_2026.xlsx` |
| 匯出中之狀態欄 | **無 `State` 欄** —— 有 `SYS2 HARMAN Status`（第 15 欄）與 `SYS2 MD Status`（第 17 欄）|
| CFTS009 之 `HARMAN Status` 值分布 | `Accepted` **168**、**`Need rework` 4**（其餘列該欄為空）|
| CFTS009 之 `MD Status` 值分布 | `Accepted` 168 |
| CFTS010 | `HARMAN Status` / `MD Status` 皆 `Accepted` 4，無非 Accepted 者 |
| `Need rework` 之四列 | `Sys-RA-PM-0021`、`Sys-RA-PM-0291`、`Sys-RA-PM-0292`、`Sys-RA-PM-0293` |

**兩項結論**：

1. **`All_Accepted` 指的是 SYS2 之審查狀態（HARMAN / MD Status），
   與 CFTS 錨點標頭之 `[State:…]`（Polarion 工作流狀態，值為 `New` / `Under Review`）
   是兩個不同層級的欄位。** 匯出中不含 `[State:…]` 之對應欄。
2. **檔名之 `All_Accepted` 於 CFTS009 並非字面為真** ——
   `HARMAN Status` 有 **4 列為 `Need rework`**。
   **該四 token 之範圍已順帶查證**（成本極低）：全 115 leaf 中，
   僅 **`SWE-PM-112`** 引用其一（`Sys-RA-PM-0293`）；
   **不落在已產出 TC 之 11 leaf 內**，故不影響現有 43 條。
   `Sys-RA-PM-0021` / `0291` / `0292` **無任何 leaf 引用**。

**執行層不就 `State` 相異是否影響範圍作任何裁定**（R-P143 明訂裁定於 21 包）。

## 3. 標頭原字串（逐字，供覆核屬性抽取是否完整）

### `4941727`

```
4941727: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
```

### `4941728`

```
4941728: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
```

### `4941729`

```
4941729: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:LTM, ETM, RRM] [Market:All] [Radio:allSys, noSys] [EE Architecture:Atlantis High, Atlantis Mid]
```

### `4941730`

```
4941730: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
```

### `4941735`

```
4941735: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:LTM, ETM, RRM] [Market:All] [Radio:allSys, noSys] [EE Architecture:Atlantis High, Atlantis Mid]
```

### `4941736`

```
4941736: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
```

