# 上繳包 03 —— T9a–c：訊號編碼實測

- 日期：2026-08-27
- 對應下放：`docs/handoff/04_priority_profile.md`
  （SHA256 `8bfba3f89db2e84de6261e81e8d67291d016d3a808f100c6c929f428125be3f0`，122 行）
- profile 已落 `docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`
  （SHA256 `a5441cff3d35b223…`，138 行）
- **結論：T9a–c 全數執行。⚠ 三項實測與 profile §3 之訊號表不符，見 §0。**
- 未產任何 TC、未改 profile、未寫回、未進行任何 git 操作。

---

## 0. ⚠ profile §3 之五列，三列對不上

| profile §3 之路徑 | 實測 |
|---|---|
| `$Speedometer$` → LID **r1738** → `GW_C1.VEH_SPEED` | LID 列**正確**；**但 `GW_C1` 不在綁定之二個 DBC 內** |
| `$VC_Trans_Equipped$` → LID **r421** → `VehCfg7.VC_Trans_Equipped` | **LID r421 是 `DCSD_Enter`，不是它**；真正位置為**另一分頁** `Proxi & Configuration` **r420**；`VehCfg7` 亦不在二 DBC 內 |
| `$PresentGear$` → LID **r1397** → `GW_C1.Gr` | LID 列**正確**；**`GW_C1` 同樣不在二 DBC 內** |
| `$PARK_BRK_EGD$` → 保留來源名 | ✅ 照辦，未代換 |
| `$Country_Code$` → LID **r43** → `Car_Configuration_16.Country_Code` | **`CAN Mapping` r43 是 `ACV_FailType`**；真正位置為 `Proxi & Configuration` **r43**（同號、**不同分頁**），對應**正確** |

### 0.1 根因一：LID 有二個分頁，profile 未標分頁

- `Speedometer`（r1738）、`PresentGear`（r1397） → 分頁 **`CAN Mapping`**
- `Country_Code`（r43）、`VC_Trans_Equipped`（**r420**） → 分頁 **`Proxi & Configuration`**

`Country_Code` 之 r43 在二分頁**各有一列且內容不同** ——
**只寫「LID r43」會指到錯的那一列。**

### 0.2 ⚠ 根因二：架構不匹配（**本項較嚴重**）

`GW_C1`／`VehCfg7` **不存在於綁定之任一 DBC**：

```
PDT27_E2A_R4_BHCAN.dbc   BO_ 訊息 155 個   含 GW_C1？ 否   含 VehCfg7？ 否
PDT27_E2A_R5_FDCAN8.dbc  BO_ 訊息 323 個   含 GW_C1？ 否   含 VehCfg7？ 否
```

**LID r1738 之欄位顯示其為多架構對照表**：

| LID 欄 | 架構 | CAN 名 |
|---|---|---|
| c5 | **Powernet** | `GW_C1.VEH_SPEED` ← **profile 取的是這欄** |
| c15／c25 | **ATLANTIS** | `STATUS_CCAN3.VehicleSpeedVSOSig` |

而**綁定之 DBC 用的是 ATLANTIS 側之名**：

| DBC | BO_ . SG_ | 長度 | factor | offset | 範圍 | 單位 |
|---|---|---|---|---|---|---|
| `R4_BHCAN` | `STATUS_CCAN3.VehicleSpeedVSOSig` | 13 bit | **0.0625** | 0 | [0\|511.9375] | **`Km/h`** |
| `R5_FDCAN8` | `BRAKE_FD_2.VehicleSpeedVSOSig` | 13 bit | **0.0625** | 0 | [0\|511.875] | **`Km/h`** |
| `R4_BHCAN` | `GW_B_3.GearEngagedForDisplay` | 5 bit | 1 | 0 | [0\|30] | `-` |
| `R5_FDCAN8` | `TRANSM_FD_2.GearEngagedForDisplay` | 5 bit | 1 | 0 | [0\|30] | `-` |

**即：profile §3 之三條 CAN 路徑取自 Powernet 欄，而 R-DD5 所綁之
DBC 為 ATLANTIS／PDT27 —— 照 profile 寫的步驟，在這二份 DBC 上施加不了。**

**我沒有自行改用 ATLANTIS 名**：架構之選定屬裁定（哪一個是 R1L 之目標平台），
非執行層可定。**證據在此，裁定在分析層。**

---

## 1. T9a —— DBC 逐訊號

### 1.1 查無清單

```
GW_C1.VEH_SPEED            —— 二 DBC 皆查無
VehCfg7.VC_Trans_Equipped  —— 二 DBC 皆查無
GW_C1.Gr                   —— 二 DBC 皆查無
```

### 1.2 A-DD2 之候選對應 —— **查得，但僅查證不採用**

下放包 T9a 明文「僅查證不採用」。二者皆在：

| DBC | BO_ | id | SG_ | 長度 | factor／offset | `VAL_` |
|---|---|---|---|---|---|---|
| `R4_BHCAN` | `STATUS_BH_BCM1` | 854 | `ParkBrakeSts` | 1 bit | 1／0 | **`0 "OFF" 1 "ON"`** |
| `R5_FDCAN8` | `BCM_FD_9` | 1066 | `ParkBrakeSts` | 1 bit | 1／0 | **`0 "OFF" 1 "ON"`** |

**其 `VAL_` 之 `OFF`／`ON` 與 CFTS022 `-128`／`-129` 之
`$PARK_BRK_EGD$ = [ON]`／`[OFF]` 逐字相合。**

**這使 A-DD2 之「同一訊號、拼法倒置」更為可能** —— 但**仍未採用**：
DR-DD2 未結，R-DD5／R-13 之拘束不因證據變強而解除。
**證據記於此，供分析層裁。**

---

## 2. T9b —— `Country_Code` 值域：**Hong Kong 查無**

PROXI `Format` **r468** 之值表逐字：

```
Car_Configuration_16 | 107–107 | bit 0–7 | Country_Code | Table
  0 = World            2 = United States of America   4 = Canada
 14 = Mexico          16 = China Mainland            18 = Bahrain
 97 = Iraq           104 = Jordan                   108 = Kuwait
112 = Lebanon        149 = Oman                     160 = Qatar
165 = Saudi Arabia   204 = United Arab Emirates     215 = Yemen
```

**無 Hong Kong。** 且該列 c18 自書 **`See Country Code Table`**
—— 它自己說這是**部分列舉**。

### 2.1 權威來源已被指名，而它不在我方素材

LID `Proxi & Configuration` r43 c7 逐字：

> `See latest version of 'CIP Market Configuration Table v*.xlsx',
>  worksheet 'Marke…'`

**即：`Country_Code` 之完整值域在 `CIP Market Configuration Table v*.xlsx`，
該檔不在 `inputs/`、不在 `forms/`、不在任何已綁之 reference。**

**DR-DD3 之標的因此是具名的**（非「請提供值域」而是「請提供該檔」）。
下放包 T9b 稱「查無 → 列 DR 候選，分析層擬 DR-DD3」——**候選已列，含檔名。**

> **連帶**：A-DD1（HK vs LATAM）之四凍結 leaf，其 Pre-Condition 需要
> `Country_Code` 之 HK 值。**即使 DR-DD1 裁 HK，沒有該表仍寫不出值。**
> 二者為**不同的阻斷**，不可互相取代。

---

## 3. T9c —— 5／3 MPH 之 raw：**只列原值，未換算**

**profile §3 所指之 `GW_C1.VEH_SPEED` 不在二 DBC 內，故其 factor／offset
無從列出。** 綁定 DBC 之對應訊號（ATLANTIS 側）之原值已列於 §0.2 之表。

**⚠ 單位問題（本項之要害）**：

```
spec 之門檻 = 5 MPH ／ 3 MPH
DBC 之單位 = "Km/h"（二 DBC 皆然，逐字）
```

**換算涉及 MPH→km/h，其係數不在 DBC 內，亦不在 LID 內。**

依下放包 T9c「執行層不逕填 TC 值」與 §8.4.1，**我未做任何換算**。
**且此處不只是「不逕填」的問題** ——
換算係數是一個**來源未載之值**，填了就是造值，不論由誰填。

**建議**：分析層覆核時一併裁「MPH 門檻如何落到 km/h 訊號」——
是取換算值、或改以 spec 之 MPH 表述而由測試員之工具轉換、
或另有一個 MPH 單位之訊號未被找到。

---

## 4. 未結 DR

| DR | 狀態 | 阻斷 |
|---|---|---|
| DR-DD1 | DRAFTED（待發送）| `-025`~`-028` 凍結 |
| DR-DD2 | DRAFTED（待發送）| 不阻斷；訊號名待定 |
| **DR-DD3**（候選）| **未擬**（分析層擬）| `-017`~`-028` 之 `Country_Code` 值；**標的具名**：`CIP Market Configuration Table v*.xlsx` |

---

## 5. 獨立自評

1. **§0 之三列不符，我是先照 profile 查、查不到才回頭驗 profile 的。**
   若我一開始就「找得到就好」地去 DBC 裡找速度訊號，
   會直接找到 `VehicleSpeedVSOSig` 並填進去 —— **然後 profile 之錯永遠不會浮出來**。
   **照著錯的指示查、查不到、回報**，比自己找到對的答案有用。
2. **`Country_Code` 之 r43 在二分頁各有一列，這件事差點被我當成 profile 寫錯。**
   `CAN Mapping` r43 是 `ACV_FailType`，我原本要寫「profile 引錯列」——
   **查了另一分頁才發現 r43 在那裡是對的**。
   **「引錯」與「沒標分頁」是兩種錯，其修法不同。**
3. **A-DD2 之候選在 DBC 裡查得，且 `VAL_` 之 ON/OFF 與 CFTS 逐字相合。**
   證據又強了一層，而我仍然沒有採用它 —— **理由與上一包相同，未因證據變強而改變**。
4. **T9c 我原本只打算寫「不逕填」。** 寫到一半發現真正的問題不是誰填，
   是**那個係數在所有已綁素材裡都不存在** —— 那不是權限問題，是缺件問題。

---

## 6. 量測條件揭露（R-G8）

- **DBC 之解析以正則逐行**：`BO_` 行起訊息、`SG_` 行取
  start／len／order／sign／factor／offset／範圍／單位、`VAL_` 行取列舉。
  **未匹配樣式之 `SG_` 行以逐字原文輸出**，不靜默丟棄。
- **「二 DBC 皆查無」為否定性判斷**，其母體為 155 + 323 個 `BO_` 訊息；
  **以 `BO_` 名 ＋ `SG_` 名雙鍵比對**，另以單獨訊號名複查（亦零命中）。
- **LID 之分頁**：本輪讀 `CAN Mapping` 與 `Proxi & Configuration` 二分頁；
  **其餘分頁未掃** —— 若某訊號另載於他分頁，本輪看不到。
- **PROXI 之 `Country_Code` 掃描涵蓋全部分頁**（含 `Revision Notes`），
  命中 10 列，其中值表僅 `Format` r468 一列。
- **未做**：任何換算、任何 TC、profile 之修改。
