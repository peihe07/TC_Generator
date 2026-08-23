# pilot #3 review sheet —— 13 條

執行層產出（W-104，37 輪）。依 60 包 §5 之抽樣裁定。

| 母體 | 條數 | 理由 |
|---|---:|---|
| `batch13_v2` 全數 | 10 | 首批「標的訊號不在基線 DBC」之 TC，形態與前 76 條皆不同，pilot #1／#2 之結論不涵蓋 |
| W-101 之 Priority 變動 | 3 | P0(a) 1／P0(b) 1／由 P2 升 P1 1 —— 驗 R-VS56 之判定可覆核性 |

**分析層先讀並附建議分類，Pei 覆核分類（60 包 §5）。**

---

## 1. `SWE1-VC-TwoStagesHeatedSeat-058`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱座椅之按壓啟用 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859380`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ == "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_high".

### 十欄全文

**tc_title**：Heated seat at off plus request commands high
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_high".

(Off plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off)
3. Press the left front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 3 (Heated_seat_high) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 3 (Heated_seat_high) is sent
```

**specification_reference**：CFTS044-4859380
**design_method**：決策表 (Decision Table Testing)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 2. `SWE1-VC-TwoStagesVentedSeatsManagement-040`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.4.1 |

### 來源條文逐字

`CFTS044-4859442`（`EE Architecture: Atlantis Mid`）：

> IF ($VentedSeatFL$ == "Vented_seat_off" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_high".

### 十欄全文

**tc_title**：Vented seat at off plus request commands high
**test_item**

```
IF ($VentedSeatFL$ == "Vented_seat_off" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_high".

(Off plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 0 (Vented_seat_off)
3. Press the left front vented seat icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 3 (Vented_Seat_High) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 0 (Vented_seat_off) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 3 (Vented_Seat_High) is sent
```

**specification_reference**：CFTS044-4859442
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 3. `SWE1-VC-TwoStagesHeatedSeat-059`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859381`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ == "Heated_seat_high" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low".

### 十欄全文

**tc_title**：Heated seat at high plus request commands low
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_high" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low".

(High plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 3 (Heated_seat_high)
3. Press the left front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 3 (Heated_seat_high) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is sent
```

**specification_reference**：CFTS044-4859381
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 4. `SWE1-VC-TwoStagesVentedSeatsManagement-041`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.4.1 |

### 來源條文逐字

`CFTS044-4859443`（`EE Architecture: Atlantis Mid`）：

> IF ($VentedSeatFL$ == "Vented_seat_high" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low".

### 十欄全文

**tc_title**：Vented seat at high plus request commands low
**test_item**

```
IF ($VentedSeatFL$ == "Vented_seat_high" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low".

(High plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 3 (Vented_seat_high)
3. Press the left front vented seat icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 3 (Vented_seat_high) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is sent
```

**specification_reference**：CFTS044-4859443
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 5. `SWE1-VC-TwoStagesHeatedSeat-060`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859382`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ == "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off".

### 十欄全文

**tc_title**：Heated seat at low plus request commands off
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off".

(Low plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 1 (Heated_seat_low)
3. Press the left front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 0 (Heated_seat_off) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 1 (Heated_seat_low) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 0 (Heated_seat_off) is sent
```

**specification_reference**：CFTS044-4859382
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 6. `SWE1-VC-TwoStagesVentedSeatsManagement-042`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.4.1 |

### 來源條文逐字

`CFTS044-4859444`（`EE Architecture: Atlantis Mid`）：

> IF ($VentedSeatFL$ == "Vented_seat_low" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_off".

### 十欄全文

**tc_title**：Vented seat at low plus request commands off
**test_item**

```
IF ($VentedSeatFL$ == "Vented_seat_low" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_off".

(Low plus press request, no failure present)
```

**pre_conditions**

```
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 1 (Vented_seat_low)
3. Press the left front vented seat icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 1 (Vented_seat_low) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is sent
```

**specification_reference**：CFTS044-4859444
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 7. `SWE1-VC-TwoStagesHeatedSeat-067`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859389`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ passes to "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off";

### 十欄全文

**tc_title**：Heated seat status change mirrors off to the command
**test_item**

```
IF ($HeatedSeatFL$ passes to "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off";

(Status transition to off mirrored, no press)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 2 (Heated_seat_medium)
3. Send CAN: STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 0 (Heated_seat_off) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 2 (Heated_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 0 (Heated_seat_off) is sent
```

**specification_reference**：CFTS044-4859389
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 8. `SWE1-VC-TwoStagesVentedSeatsManagement-049`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.4.1 |

### 來源條文逐字

`CFTS044-4859451`（`EE Architecture: Atlantis Mid`）：

> IF ($VentedSeatFL$ passes to "Vented_seat_off" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_off";

### 十欄全文

**tc_title**：Vented seat status change mirrors off to the command
**test_item**

```
IF ($VentedSeatFL$ passes to "Vented_seat_off" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_off";

(Status transition to off mirrored, no press)
```

**pre_conditions**

```
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 2 (Vented_seat_medium)
3. Send CAN: STATUS_CSWM.FL_VS_STATSts = 0 (Vented_seat_off) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 2 (Vented_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is sent
```

**specification_reference**：CFTS044-4859451
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 9. `SWE1-VC-TwoStagesHeatedSeat-068`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859390`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ passes to "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low"

### 十欄全文

**tc_title**：Heated seat status change mirrors low to the command
**test_item**

```
IF ($HeatedSeatFL$ passes to "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low"

(Status transition to low mirrored, no press)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 2 (Heated_seat_medium)
3. Send CAN: STATUS_CSWM.FL_HS_STATSts = 1 (Heated_seat_low) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 2 (Heated_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is sent
```

**specification_reference**：CFTS044-4859390
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 10. `SWE1-VC-TwoStagesVentedSeatsManagement-050`

| 項 | 值 |
|---|---|
| 來源批次 | `batch13_v2` |
| 納入理由 | 新形態全數納入 —— 標的訊號不在基線 DBC |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.4.1 |

### 來源條文逐字

`CFTS044-4859452`（`EE Architecture: Atlantis Mid`）：

> IF ($VentedSeatFL$ passes to "Vented_seat_low" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low"

### 十欄全文

**tc_title**：Vented seat status change mirrors low to the command
**test_item**

```
IF ($VentedSeatFL$ passes to "Vented_seat_low" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low"

(Status transition to low mirrored, no press)
```

**pre_conditions**

```
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 2 (Vented_seat_medium)
3. Send CAN: STATUS_CSWM.FL_VS_STATSts = 1 (Vented_seat_low) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 2 (Vented_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is sent
```

**specification_reference**：CFTS044-4859452
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 11. `SWE1-VC-ThirdRowHeadrestDump-025`

| 項 | 值 |
|---|---|
| 來源批次 | `batch01_v6` |
| 納入理由 | P0(a) 之唯一一條 —— 實體致動；驗 R-VS56 之 P0(a) 是否可覆核 |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(a)：第三排頭枕之下放致動 |
| `dr_dependent` | （無） |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| 章節 | 1.3.2.1.18 |

### 來源條文逐字

`CFTS044-4858986`（`EE Architecture: Atlantis High, PowerNet`）：

> The Headrest Dump button shall activate both left and right head restraint dumps at the same time (they are not independent).  The soft button shall perform similar to the other buttons within the same touch screen (i.e. press time to actuation, size of button).  The switch is only to lower the head restraints, and not to raise them.

### 十欄全文

**tc_title**：Headrest Dump button lowers both third row head restraints together
**test_item**

```
When the Headrest Dump Softkey button is pressed, the HMI shall simultaneously activate both left and right third-row head restraint dump functions. The left and right head restraint dump functions shall operate together and shall not be independently controlled.

(Single press, both restraints lower together)
```

**pre_conditions**

```
1. Both third row head restraints are in the raised position
2. The Headrest Dump Softkey button is shown and selectable
```

**input_test_data**：NA
**test_procedure**

```
1. Read the position of the left and right third row head restraints and check that both are raised
2. Press the "Headrest Dump" softkey button and check that both the left and the right third row head restraints lower
```

**expected_result**

```
1. Both third row head restraints read raised
2. The left and the right third row head restraints lower at the same time
```

**specification_reference**：CFTS044-4858986
**design_method**：功能測試 (Functional based ; no specific technique)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 12. `SWE1-VC-TwoStagesHeatedSeat-057`

| 項 | 值 |
|---|---|
| 來源批次 | `batch05_v4` |
| 納入理由 | P0(b) 之代表 —— 加熱座椅之按壓啟用；驗「啟用」與「階數切換」之界線 |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱座椅之按壓啟用 |
| `dr_dependent` | （無） |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

### 來源條文逐字

`CFTS044-4859379`（`EE Architecture: Atlantis Mid`）：

> During the Ignition Working Condition- Ignition Off- Ignition On- Ignition On Engine On- Ignition Pre OffWHEN the user press the heated seats icons on TLM.Display.GUI, the relative icons status shall follow the logic descibed below (off -&gt; high -&gt; low -&gt; off):

### 十欄全文

**tc_title**：Heated seat icon cycles off to high to low to off
**test_item**

```
WHEN the user press the heated seats icons on TLM.Display.GUI, the relative icons status shall follow the logic descibed below (off -> high -> low -> off)

(Two-stage icon cycle on repeated press)
```

**pre_conditions**

```
1. The vehicle is configured for two heated seat states
2. The heated seat icon status is off
3. The ignition is in the Ignition On condition
```

**input_test_data**：NA
**test_procedure**

```
1. Press the heated seat icon and check that its status changes to high
2. Press the heated seat icon and check that its status changes to low
3. Press the heated seat icon and check that its status changes to off
```

**expected_result**

```
1. The heated seat icon status is high
2. The heated seat icon status is low
3. The heated seat icon status is off
```

**specification_reference**：CFTS044-4859379
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---

## 13. `SWE1-VC-ThirdRowHeadrestDump-030`

| 項 | 值 |
|---|---|
| 來源批次 | `batch02_v4` |
| 納入理由 | 由 P2 升 P1 者 —— 軟鍵之可選性；驗 R-VS56 之 P1 涵蓋範圍 |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | （無） |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.2.1.18 |

### 來源條文逐字

`CFTS044-4858993`（`EE Architecture: Atlantis High`）：

> The HU shall make the Third Row Headrest Dump Softkey button selectable when $PowerMode$ = [Ignition lock / IGN_LK].

### 十欄全文

**tc_title**：Headrest Dump softkey selectable at ignition lock
**test_item**

```
The HMI shall make the Third Row Headrest Dump softkey selectable when $PowerMode$ = [Ignition Lock / IGN_LK].

(PowerMode = IGN_LK)
```

**pre_conditions**

```
1. The vehicle is equipped with the third row head restraint dump feature
2. The Controls screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 0 (Initialization)
2. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK) and check that the "Headrest Dump" softkey button is selectable
```

**expected_result**

```
1. STATUS_BH_BCM2.CmdIgnSts = 0 (Initialization) is sent
2. The "Headrest Dump" softkey button is selectable
```

**specification_reference**：CFTS044-4858993
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| `dr_dependent` 標記 | | |

---
