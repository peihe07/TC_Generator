# 下放包 06 —— Market Configuration Table 到位、Country_Code 值查得、Q9 識別待確認

- 日期：2026-08-27
- 方向：分析層 → Pei（Q9 待確認）＋ 執行層（T11、T-登）
- 前一包：`05_arch_suspend.md`
- 觸發：Pei 置入 `forms/SR24 R1 Market Configuration Table v1.6.xlsx`
- **Q7／Q8 仍待裁；pilot 仍不開**

---

## 一、分析層實測（本包全部數字自該檔以 openpyxl `read_only/data_only` 讀得）

分頁八個；相關者為 `Market Config - R1`（表頭列 6，資料自列 7，
223 列具數值 Country_Code）。

### 1.1 Hong Kong 之列（r97）逐欄

| 欄 | 表頭（逐字，換行以空白代）| 值 |
|---|---|---|
| c8 | `Destination Country` | `HONG KONG` |
| c16 | `Region (Ref-only for FGA Default Regional Set…)` | `APAC` |
| c17 | `Value in <Dest> Signal - Hex` | `5B` |
| c18 | `Value in <Dest> Signal - Decimal` | `91` |
| **c19** | **`PROXI3  <Country_Code>Signal - Decimal`** | **`91`** |
| c58 | `Navigation Driver Distraction Lockout Disable…` | `N` |

**`$Country_Code$` 之 Hong Kong 值 = `91`（十進位；Hex `5B`）。**

一致性側證（非結論）：PROXI 檔之 `Country_Code` 位於
`Car_Configuration_16` byte 107 bit 0–7（上繳包 01 T6 實測），
值域 0–255，`91` 落於域內。

### 1.2 附帶事實 —— `c58` 之分布（**記錄，不入 TC**）

`Navigation Driver Distraction Lockout Disable`：`Y` 165 列／`N` 58 列。
Hong Kong = `N`；LATAM 諸國（Argentina 211、Brazil 15、Chile 45、
Colombia 47、Peru 154）皆 `Y`。

**§8.4.2 界線**：該欄對應 CFTS022 `-136`（**Out of scope**，
Embedded NAV 之 DD lockout「if requested by the destination」），
**不在本 feature 28 leaf 內**。本節僅為事實登記，
**TC 不得引用該欄、不得以其為 Pre-Condition**。

亦**不得**以「HK=N 而 LATAM=Y」推論 A-DD1 之歸屬 ——
該欄限 Navigation 範圍，與 `-132`／`-133` 之整車速度門檻非同一層；
以其推論即為跨範圍援引。A-DD1 仍待 DR-DD1。

---

## 二、Q9（待 Pei 確認）—— 文件識別

LID `Proxi & Configuration` r43 c7 指名之標的為
`CIP Market Configuration Table v*.xlsx`；
Pei 置入者為 `SR24 R1 Market Configuration Table v1.6.xlsx`。**檔名不同。**

支持二者為同一份之證據：
- 該檔 `ReadMe(Instruction)` 自陳為 **Market Configuration Table (MCT)**，
  釋出對象為 radio/navigation/RSE/cluster 供應商
- 其 c19 表頭逐字為 `PROXI3  <Country_Code>Signal - Decimal`
  —— 正是 LID 所指之資料項
- `Revision Log` v1.0 註 `New Release for SR24 1A`，與本專案 SR24 線相符

未能確認者：`CIP` 前綴之來歷（可能為同一份文件之另一命名，
亦可能為另一份）。**分析層不逕定二者同一** —— 文件識別屬裁定
（Home A-H03(c) 同型先例）。

**請 Pei 確認**：本檔是否即 LID 所指之 `CIP Market Configuration Table`？
- **是** → DR-DD3 結案（RESOLVED），Country_Code = 91 入 profile §3
- **否／不確定** → 值仍取 91 但標 `[ASSUMPTION A-DD5]`，DR-DD3 續開

---

## 三、任務

| # | 任務 |
|---|---|
| T11a | 該檔入 `feature.yaml` `reference` 節：`market_config`，file 記 `forms/SR24 R1 Market Configuration Table v1.6.xlsx`，**sha256 自實體檔重算**（R-G15；綁 `forms/` 原件，不複製入 feature inputs/，同 R-DD5 之理） |
| T11b | 複核 §1.1 之六欄值（獨立重讀，不抄本包）；不符即回報 |
| T11c | `Market Config - R1` 全表掃 `Destination Country` 含 `MACAU`／`TAIWAN`／`CHINA` 者之 c19 值，逐列輸出 —— **僅備查**，本輪不用於任何 TC |
| T-登 | DR-DD3 條目更新：標的已到位，狀態改 **ANSWERED-PENDING-CONFIRM**（值查得、識別待 Q9）；A-DD1／DR-DD1 不受影響，不互抵之註記維持 |

**不在本輪**：改 profile §3（待 Q7＋Q9）、任何 TC、pilot、寫回、git。

## 四、上繳包要求（併入 `docs/upstream/04_arch_binding.md`）

T10a–d（下放包 05）＋ T11a–c ＋ T-登；未結 DR 清單；獨立自評；R-G8 揭露。
