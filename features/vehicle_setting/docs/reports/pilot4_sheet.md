# pilot #3＋#4 合併 review sheet

執行層產出（W-118，42 輪）。依 67 包之抽樣裁定。

## 1. 母體與抽樣

母體 **43 條**（batch14 10／15 13／16 10／17 10）——
**batch18 之 10 條於本輪產出，不在本次抽樣之母體內。**

### 抽樣之交叉格矩陣（使抽法可複現）

| batch \ `dr_dependent` | 有 | 無 | 小計 |
|---|---:|---:|---:|
| `batch14` | 10 | 0 | 10 |
| `batch15` | 13 | 0 | 13 |
| `batch16` | 10 | 0 | 10 |
| `batch17` | 10 | 0 | 10 |

必檢 **8**（batch16／17 之 `Fail_Present` 各 4，reqid 升冪）；分層 **7**（各交叉格取 reqid 最小者；不足時自最大格補足）；**合計 15**。

## 2. pilot #3 之 13 條（只列清單，全文見 `pilot3_sheet.md`）

| # | batch | leaf_id |
|---:|---|---|
| 1 | `batch13_v2` | `SWE1-VC-TwoStagesHeatedSeat-058` |
| 2 | `batch13_v2` | `SWE1-VC-TwoStagesVentedSeatsManagement-040` |
| 3 | `batch13_v2` | `SWE1-VC-TwoStagesHeatedSeat-059` |
| 4 | `batch13_v2` | `SWE1-VC-TwoStagesVentedSeatsManagement-041` |
| 5 | `batch13_v2` | `SWE1-VC-TwoStagesHeatedSeat-060` |
| 6 | `batch13_v2` | `SWE1-VC-TwoStagesVentedSeatsManagement-042` |
| 7 | `batch13_v2` | `SWE1-VC-TwoStagesHeatedSeat-067` |
| 8 | `batch13_v2` | `SWE1-VC-TwoStagesVentedSeatsManagement-049` |
| 9 | `batch13_v2` | `SWE1-VC-TwoStagesHeatedSeat-068` |
| 10 | `batch13_v2` | `SWE1-VC-TwoStagesVentedSeatsManagement-050` |
| 11 | （W-101 之 Priority 變動） | `SWE1-VC-ThirdRowHeadrestDump-025` |
| 12 | （W-101 之 Priority 變動） | `SWE1-VC-TwoStagesHeatedSeat-057` |
| 13 | （W-101 之 Priority 變動） | `SWE1-VC-ThirdRowHeadrestDump-030` |

## 3. pilot #4 之 15 條 —— 十欄全文

### 1. `SWE1-VC-OneStageHeatedSeat-051`

| 項 | 值 |
|---|---|
| 來源批次 | `batch16` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 R-VS59(2) 取自 Comfort 素材，而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | （未標） |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.1.1 |

**來源條文逐字**

`CFTS044-4859372`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present changes the left front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

(Failure present, icon change regardless of level)
```

**pre_conditions**

```
1. The vehicle is configured for one heated seat state
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present)
3. Read the left front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859372
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 2. `SWE1-VC-OneStageHeatedSeat-052`

| 項 | 值 |
|---|---|
| 來源批次 | `batch16` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 R-VS59(2) 取自 Comfort 素材，而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | （未標） |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.1.1 |

**來源條文逐字**

`CFTS044-4859373`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.
> 1.3.3.3.2 Two Stages Heated Seats Management {4859374}
> 1.3.3.3.2.1 TLM Algorithm requirements {4859375}

**十欄全文**

**tc_title**：Failure present changes the right front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.
1.3.3.3.2 Two Stages Heated Seats Management {4859374}
1.3.3.3.2.1 TLM Algorithm requirements {4859375}

(Failure present, icon change regardless of level)
```

**pre_conditions**

```
1. The vehicle is configured for one heated seat state
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present)
3. Read the right front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859373
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 3. `SWE1-VC-TwoStagesHeatedSeat-064`

| 項 | 值 |
|---|---|
| 來源批次 | `batch16` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 R-VS59(2) 取自 Comfort 素材，而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | （未標） |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859386`（`EE Architecture: Atlantis Mid`）：

> IF (DrvSeatHeating.Req passes to "Requested" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Present")THENTLM has to show an informative popup relative to the failure. Refer to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present blocks the left front heated seat request with a popup
**test_item**

```
IF (DrvSeatHeating.Req passes to "Requested" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Present")THENTLM has to show an informative popup relative to the failure. Refer to TLM HMI Document.

(Failure present at request, informative popup)
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
2. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present)
3. Press the left front heated seat icon and check that an informative popup relative to the failure is shown
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859386
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 4. `SWE1-VC-TwoStagesHeatedSeat-065`

| 項 | 值 |
|---|---|
| 來源批次 | `batch16` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 R-VS59(2) 取自 Comfort 素材，而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | （未標） |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859387`（`EE Architecture: Atlantis Mid`）：

> IF (PsngrSeatHeating.Req == "Requested" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Present")THENTLM has to show an informative popup relative to the failure. Refer to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present blocks the right front heated seat request with a popup
**test_item**

```
IF (PsngrSeatHeating.Req == "Requested" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Present")THENTLM has to show an informative popup relative to the failure. Refer to TLM HMI Document.

(Failure present at request, informative popup)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present)
3. Press the right front heated seat icon and check that an informative popup relative to the failure is shown
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859387
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 5. `SWE1-VC-TwoStagesHeatedSeat-074`

| 項 | 值 |
|---|---|
| 來源批次 | `batch17` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 W-115(2) 之逐 leaf 行為層對照，本 leaf 判「PENDING」，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | PENDING |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859396`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.
> 1.3.3.3.3 Three Stages Heated Seats Management {4859397}
> 1.3.3.3.3.1 TLM Algorithm requirements {4859398}

**十欄全文**

**tc_title**：Failure present changes the right front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.
1.3.3.3.3 Three Stages Heated Seats Management {4859397}
1.3.3.3.3.1 TLM Algorithm requirements {4859398}

(Failure present, icon change regardless of level)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present)
3. Read the right front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859396
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 6. `SWE1-VC-ThreeStagesHeatedSeat-098`

| 項 | 值 |
|---|---|
| 來源批次 | `batch17` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 W-115(2) 之逐 leaf 行為層對照，本 leaf 判「PENDING」，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | PENDING |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.3.1 |

**來源條文逐字**

`CFTS044-4859422`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present changes the left front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

(Failure present, icon change regardless of level)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present)
3. Read the left front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859422
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 7. `SWE1-VC-ThreeStagesHeatedSeat-099`

| 項 | 值 |
|---|---|
| 來源批次 | `batch17` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 W-115(2) 之逐 leaf 行為層對照，本 leaf 判「PENDING」，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | PENDING |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.3.1 |

**來源條文逐字**

`CFTS044-4859423`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present changes the right front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFR$, IF STATUS_CSWM.FR_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

(Failure present, icon change regardless of level)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present)
3. Read the right front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859423
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 8. `SWE1-VC-ThreeStagesVentedSeatsManagement-080`

| 項 | 值 |
|---|---|
| 來源批次 | `batch17` |
| 納入理由 | 必檢（新形態，不抽樣） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：通風座椅之失效狀態處置（非熱源，不入 P0(b)）；畫面層依 W-115(2) 之逐 leaf 行為層對照，本 leaf 判「PENDING」，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | PENDING |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.5.1 |

**來源條文逐字**

`CFTS044-4859486`（`EE Architecture: Atlantis Mid`）：

> regardless of the value of $VentedSeatFL$, IF STATUS_CSWM.FL_VS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

`CFTS044-4859487`（`EE Architecture: Atlantis Mid`）：

> regardless of the value of $VentedSeatFL$, IF STATUS_CSWM.FL_VS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present changes the left front vented seat icon
**test_item**

```
regardless of the value of $VentedSeatFL$, IF STATUS_CSWM.FL_VS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

(Failure present, icon change regardless of level)
```

**pre_conditions**

```
1. The vehicle is configured for three vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 1 (Fail_Present)
3. Read the left front vented seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**

```
CFTS044-4859486
CFTS044-4859487
```

**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 9. `SWE1-VC-TwoStagesHeatedSeat-061`

| 項 | 值 |
|---|---|
| 來源批次 | `batch14` |
| 納入理由 | 分層（batch14 × `dr_dependent` 有） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱座椅之按壓啟用；觸發表述依 `CFTS044-4859365`，其與駕駛側 `4859364` 逐字對稱，駕駛側之觸發表述由 `4859508` 之 `or` 並列確立（61 包 §2） |
| `dr_dependent` | DR-25 |
| `screen_source` | （未標） |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859383`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFR$ == "Heated_seat_off" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_high".

**十欄全文**

**tc_title**：Right front heated seat at off plus request commands high
**test_item**

```
IF ($HeatedSeatFR$ == "Heated_seat_off" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_high".

(Two stage configuration, off plus press request)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off)
3. Press the right front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 3 (Heated_seat_high) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 3 (Heated_seat_high) is sent
```

**specification_reference**：CFTS044-4859383
**design_method**：決策表 (Decision Table Testing)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 10. `SWE1-VC-TwoStagesHeatedSeat-070`

| 項 | 值 |
|---|---|
| 來源批次 | `batch15` |
| 納入理由 | 分層（batch15 × `dr_dependent` 有） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `screen_source` | （未標） |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859392`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFR$ passes to "Heated_seat_off" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_off";

**十欄全文**

**tc_title**：Right front heated seat status change mirrors off to the command
**test_item**

```
IF ($HeatedSeatFR$ passes to "Heated_seat_off" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_off";

(Two stage configuration, status transition, no press)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium)
3. Send CAN: STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 0 (Heated_seat_off) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 0 (Heated_seat_off) is sent
```

**specification_reference**：CFTS044-4859392
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 11. `SWE1-VC-TwoStagesHeatedSeat-073`

| 項 | 值 |
|---|---|
| 來源批次 | `batch16` |
| 納入理由 | 分層（batch16 × `dr_dependent` 有） |
| `priority` | **P0** |
| Priority 所依類別（R-VS56） | P0(b)：加熱元件之失效狀態處置；畫面層依 R-VS59(2) 取自 Comfort 素材，而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | （未標） |
| `design_method` | 基礎故障注入 (Fault Injection Lite) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859395`（`EE Architecture: Atlantis Mid`）：

> Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

**十欄全文**

**tc_title**：Failure present changes the left front heated seat icon
**test_item**

```
Regardless of the value of $HeatedSeatFL$, IF STATUS_CSWM.FL_HS_STATFailSts passes to "Fail_Present" value, the relative icon on TLM_Display.GUI shall change according to TLM HMI Document.

(Failure present, icon change regardless of level)
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
2. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present)
3. Read the left front heated seat icon on the Heated / Vented Seats screen and check that it changes from the state shown before the failure
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATFailSts = 1 (Fail_Present) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859395
**design_method**：基礎故障注入 (Fault Injection Lite)
**priority**：P0
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 12. `SWE1-VC-OneStageHeatedSeat-047`

| 項 | 值 |
|---|---|
| 來源批次 | `batch17` |
| 納入理由 | 分層（batch17 × `dr_dependent` 有） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯；畫面層依 W-115(2) 之逐 leaf 行為層對照，本 leaf 判「PENDING」，故依 R-VS59(4) 標 `PENDING: DR-5-B` |
| `dr_dependent` | DR-5-B |
| `screen_source` | PENDING |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.1.1 |

**來源條文逐字**

`CFTS044-4859368`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ passes to "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall change the stored status of the driver heated seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.

**十欄全文**

**tc_title**：Left front heated seat display follows the status change to off
**test_item**

```
IF ($HeatedSeatFL$ passes to "Heated_seat_off" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall change the stored status of the driver heated seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.

(One heated seat state, status transition, no press)
```

**pre_conditions**

```
1. The vehicle is configured for one heated seat state
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
4. The vehicle architecture is Atlantis Mid
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off)
3. Read the displayed state of the left front heated seat and check that it changes to off
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off) is sent
3. PENDING: DR-5-B
```

**specification_reference**：CFTS044-4859368
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 13. `SWE1-VC-TwoStagesHeatedSeat-071`

| 項 | 值 |
|---|---|
| 來源批次 | `batch15` |
| 納入理由 | 分層（batch15 × `dr_dependent` 有） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `screen_source` | （未標） |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859393`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFR$ passes to "Heated_seat_low" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_low"

**十欄全文**

**tc_title**：Right front heated seat status change mirrors low to the command
**test_item**

```
IF ($HeatedSeatFR$ passes to "Heated_seat_low" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_low"

(Two stage configuration, status transition, no press)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium)
3. Send CAN: STATUS_CSWM.FR_HS_STATSts = 1 (Heated_seat_low) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 1 (Heated_seat_low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 1 (Heated_seat_low) is sent
```

**specification_reference**：CFTS044-4859393
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 14. `SWE1-VC-TwoStagesHeatedSeat-072`

| 項 | 值 |
|---|---|
| 來源批次 | `batch15` |
| 納入理由 | 分層（batch15 × `dr_dependent` 有） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯 |
| `dr_dependent` | DR-25 |
| `screen_source` | （未標） |
| `design_method` | 狀態轉換 (State Transition Testing) |
| 章節 | 1.3.3.3.2.1 |

**來源條文逐字**

`CFTS044-4859394`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFR$ passes to "Heated_seat_high" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_high".

**十欄全文**

**tc_title**：Right front heated seat status change mirrors high to the command
**test_item**

```
IF ($HeatedSeatFR$ passes to "Heated_seat_high" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_high".

(Two stage configuration, status transition, no press)
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
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium)
3. Send CAN: STATUS_CSWM.FR_HS_STATSts = 3 (Heated_seat_high) without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 3 (Heated_seat_high) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 2 (Heated_seat_medium) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 3 (Heated_seat_high) is sent
```

**specification_reference**：CFTS044-4859394
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---

### 15. `SWE1-VC-ThreeStagesHeatedSeat-084`

| 項 | 值 |
|---|---|
| 來源批次 | `batch15` |
| 納入理由 | 分層（batch15 × `dr_dependent` 有） |
| `priority` | **P1** |
| Priority 所依類別（R-VS56） | P1：主要功能邏輯；觸發表述依 `CFTS044-4859508` 之 `or` 並列（60 包 §1） |
| `dr_dependent` | DR-25 |
| `screen_source` | （未標） |
| `design_method` | 決策表 (Decision Table Testing) |
| 章節 | 1.3.3.3.3.1 |

**來源條文逐字**

`CFTS044-4859406`（`EE Architecture: Atlantis Mid`）：

> IF ($HeatedSeatFL$ == "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off".

**十欄全文**

**tc_title**：Left front heated seat at low plus request commands off
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_low" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_off".

(Three stage configuration, low plus press request)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
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

**specification_reference**：CFTS044-4859406
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| Priority 判定 | | |
| 畫面層 `PENDING` 之處置 | | |

---
