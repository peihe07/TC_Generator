# W-VF45 —— VF230 之 Priority 預判與批次規劃（**不生成 TC**）

## 0. 錨點（R-VF21 ／ R-VF28）

| 錨點 | 簇 | 期望 | 實測 |
|---|---|---|---|
| 必命中 | `Power Tailgate` | P0 | P0 ✅ |
| 必不命中 | `Speed Unit` | 非 P0 | P2 ✅ |
| **鑑別** | `Suspension Display Messages` | **非 P0** —— 其為訊息顯示而非車身致動 | P1 ✅ |

> **鑑別錨點之作用**：一條以 `Suspension` 為鍵之規則會把訊息顯示
> 誤判為 P0。本方案逐簇具名，故不誤判。

## 1. ⚠ R-VS56 之 P0 二類係以 Part 1 之內容界定，VF230 二者皆無

R-VS56 之 P0(a) 為第三排頭枕下放、P0(b) 為加熱元件 ——**VF230 無頭枕下放、無加熱功能**。
故本層依其**原則**（實體致動且具傷害可能／熱源）對映 VF230 之內容。
**此對映為本層之預判，非 R-VS56 之逐字，逐簇列出待覆核。**

### P0(a) 之簇（逐簇具名）

| 簇 | leaf | 其驅動何機構、乘員何以可能在其行程內 |
|---|---:|---|
| `Suspension Auto Entry or Exit` | 6 | 上下車時車身自動升降 —— 實體升降且人正在其側 |
| `Power Liftgate/Tailgate Alert` | 6 | 電動尾門之警示 —— 同上，且警示失效即傷害可能 |
| `Power Tailgate` | 6 | 電動尾門之開閉 —— 其行程內可能有人，夾傷可能 |
| `Suspension Default Ride Height` | 6 | 車身高度之致動 —— 同上 |
| `Suspension Flash Lights With Lower` | 5 | 車身降低之致動（其附隨閃燈）—— 同上 |
| `Suspension Sound Horn With Lower` | 5 | 車身降低之致動（其附隨鳴笛）—— 同上 |
| `Suspension Service Mode` | 5 | 維修模式之車身升降 —— 作業者可能在車下 |
| `Driver Easy Exit Seat` | 5 | 駕駛座椅之自動退移 —— 實體致動且人在座 |
| `Power Side Step` | 5 | 電動側踏板之伸縮 —— 其行程貼近上下車者之足部 |

**P0(b)（熱源）：0** —— VF230 無熱源功能。

## 2. 分布：P0 **49** ／ P1 **288** ／ P2 **290**（合計 627）

| Test Set | P0 | P1 | P2 | 合計 |
|---|---:|---:|---:|---:|
| Trailer and Signage | 5 | 46 | 88 | 139 |
| Auxiliary Switches | 0 | 28 | 87 | 115 |
| Driver Convenience | 0 | 36 | 63 | 99 |
| Suspension and Comfort | 32 | 42 | 0 | 74 |
| Units and Cameras | 0 | 21 | 52 | 73 |
| Lane and Lighting | 0 | 49 | 0 | 49 |
| Approach and Tailgate | 12 | 37 | 0 | 49 |
| Measurement Units | 0 | 17 | 0 | 17 |
| Daytime Lighting | 0 | 12 | 0 | 12 |

## 3. 選池順序（R-VS58）

優先序 **P0 → P1 → P2**；同序內**逐 Test Set 輪流 ＋ reqid 升冪**。
可生成之池（`writable ∈ {W0, W1}`）= **621**（627 − W2 6 = 621）。

**前 20 條之順序**：

| # | leaf | Pri | Test Set | writable |
|---:|---|---|---|---|
| 1 | `SWE1-VC-PowerLiftgate/TailgateAlert-016` | P0 | Approach and Tailgate | W0 |
| 2 | `SWE1-VC-SuspensionServiceMode-002` | P0 | Suspension and Comfort | W0 |
| 3 | `SWE1-VC-PowerSideStep-051` | P0 | Trailer and Signage | W0 |
| 4 | `SWE1-VC-IlluminatedApproach-002` | P1 | Approach and Tailgate | W0 |
| 5 | `SWE1-VC-4AUXSwitches-027` | P1 | Auxiliary Switches | W0 |
| 6 | `SWE1-VC-DaytimeRunningLights-002` | P1 | Daytime Lighting | W0 |
| 7 | `SWE1-VC-BlindSpotAlert-002` | P1 | Driver Convenience | W0 |
| 8 | `SWE1-VC-CorneringLights-002` | P1 | Lane and Lighting | W0 |
| 9 | `SWE1-VC-PressureUnit-002` | P1 | Measurement Units | W0 |
| 10 | `SWE1-VC-SuspensionDisplayMessages-008` | P1 | Suspension and Comfort | W0 |
| 11 | `SWE1-VC-WarningsforLowFuelInverterShutdown - VisualWarning-115` | P1 | Trailer and Signage | W1 |
| 12 | `SWE1-VC-TimeandDateSettings-004` | P1 | Units and Cameras | W0 |
| 13 | `SWE1-VC-SWITCH1Type-002` | P2 | Auxiliary Switches | W0 |
| 14 | `SWE1-VC-Language-059` | P2 | Driver Convenience | W0 |
| 15 | `SWE1-VC-WarningsforLowFuelInverterShutdown - VisualWarning-117` | P2 | Trailer and Signage | W0 |
| 16 | `SWE1-VC-TimeandDateSettings-002` | P2 | Units and Cameras | W0 |
| 17 | `SWE1-VC-PowerLiftgate/TailgateAlert-017` | P0 | Approach and Tailgate | W0 |
| 18 | `SWE1-VC-SuspensionServiceMode-003` | P0 | Suspension and Comfort | W0 |
| 19 | `SWE1-VC-PowerSideStep-052` | P0 | Trailer and Signage | W0 |
| 20 | `SWE1-VC-IlluminatedApproach-003` | P1 | Approach and Tailgate | W0 |

## 4. 批次規劃（**待分析層核可，不得逕行生成**）

- 每批 **10** 條（沿用 Part 1 之批量）
- 批數 **63**（621 條）
- **pilot 批建議為第 1 批**：其含 P0 之前 10 條，涵蓋實體致動類 —— 風險最高者先驗其書寫形式

**pilot 批之範圍與時點須待核可**（V16 §5 第 3 項）。**本輪未生成任何 TC。**

## 5. 預判與定稿後判定之一致性

**本表為選池時之預判**（R-VS58：以來源條文預判，非待 TC 寫成後）。
**預判與 TC 定稿後之判定不一致者，須於其所屬批次之上繳具名**（W-VF45 第 1 項）。本輪無 TC，故無不一致可報。

