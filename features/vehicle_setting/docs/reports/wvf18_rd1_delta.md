# W-VF18 —— RD-1 之 158 vs 160（A-VF3）

**V07 §6.2 之工單。只查不改。**

## 0. 錨點（R-VF11，先於結論）

| 錨點 | leaf | 實質判準 | 代理判準 |
|---|---|---|---|
| 必命中 | `SWE1-VC-LeftFrontHeatedSeat-003` | 命中 | 命中 |
| 必不命中 | `SWE1-VC-HeatedSteeringWheelManagement-031` | 未命中 | 未命中 |
| 鑑別 | `SWE1-VC-LeftFrontHeatedSeat-004` | 命中 | 未命中 |

**實質判準之錨點：皆符。**

**代理判準於必命中錨點上未命中** —— 此即 A-VF3 之差額所在，
亦為 R-VF11 之立法目的：判準之不足在落筆時不可見，唯錨點可使其可見。

## 1. 實質判準

RD-1 之標的逐字為「`Heated Seat`（88 leaf）與 `Vented Seat`（72 leaf）
之分支結構」。**二者為 Layer 2（Test Set）之名**，其成員以
`framework.md` 之 Layer 2 → Layer 3 對照表為準：

| Layer 2 | Layer 3 成員 |
|---|---|
| Heated Seat | `ThreeStagesHeatedSeat`、`TwoStagesHeatedSeat`、`LeftFrontHeatedSeat`、`RightFrontHeatedSeat`、`OneStageHeatedSeat`、`CrossZone Common` |
| Vented Seat | `ThreeStagesVentedSeatsManagement`、`TwoStagesVentedSeatsManagement`、`LeftFrontVentedSeat`、`RightFrontVentedSeat` |

自 `writability.tsv` 重算之各 Layer 2 leaf 數：

- **Heated Seat** — 88
- **Vented Seat** — 72
- **合計 — 160**

→ **與 RD-1 自述之 160 相符。**

## 2. 差額之身分（2 leaf）

| leaf | `layer3` | 為何代理判準漏之 |
|---|---|---|
| `SWE1-VC-LeftFrontHeatedSeat-004` | `CrossZone Common` | 其 `layer3` 不含字串 `HeatedSeat`／`VentedSeat` |
| `SWE1-VC-LeftFrontHeatedSeat-011` | `CrossZone Common` | 其 `layer3` 不含字串 `HeatedSeat`／`VentedSeat` |

## 3. 判別（V07 §6.2 第 3 項之三選一）

**(iii) 二者定義本不相同。**

- `writability.tsv` **無遺漏** —— 該 2 leaf 皆在其內，
  且 `layer3` 值正確（`CrossZone Common` 為 `framework.md` 明列之
  Heated Seat 之 Layer 3，見上表）。故**非 (i)**。
- RD-1 之 160 **無計數誤** —— 自 `writability.tsv` 依實質判準重算得 160，與其自述相符。故**非 (ii)**。
- 差額全數源於 **W-VF16 所用之代理判準**：其以 `layer3` 之**字串形態**
  篩選，而 `CrossZone Common` 之名不帶族名字串。
  **代理判準與實質判準之定義不同，非資料有誤。**

## 4. 後果

**A-VF3 所慮之「`writability.tsv` 非該範圍之全集」不成立** ——
其為全集，是取用方式錯了。canon §5a「代理判準不得凌駕實質判準」
於此獲一次正面驗證：實質判準（framework 之 Layer 2 成員）可得 160，
代理判準（字串比對）得 158。

**W-VF16 之判準 (c) 應以 158 或 160 為準？** ——
**160**。本輪之 2 leaf（`CrossZone Common`）確在 RD-1 之
標的內。惟**此更正不改變 W-VF16 之結論**：A-VS118 之 4 leaf 於
`HeatedSteeringWheelManagement`，於 158 與 160 兩版皆判「未交付」
（必不命中錨點 `SWE1-VC-HeatedSteeringWheelManagement-031` 於實質判準亦未命中）。

**本輪未改任何檔。**

