# 上繳材料 21a —— 037 四個說明欄之抽樣全文（R-SU28(b)）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/22_coverage_split.md` §五 T35b
- 依據：**R-SU28(b)**（四個說明欄待抽樣後裁）
- 母包：`docs/upstream/21_coverage_split.md`

> ⚠ **欄 12（`Description/Action for Risk Factor`）之 unique 為 1**
> —— 全 311 列同一句，實為**常數欄**，依 R-SU28(a) 可逕裁「不用」，
> 不必待抽樣（母包 §3.1）。本冊仍列其抽樣以資佐證。
>
> **執行層不裁「已用／不用」**（R-SU26(b) 為分析層之事）。

---

取樣：自 311 母體以 `random.Random(35).sample(rows, 8)` 各抽 8 列。


---

### 欄 8 — `Description/Action for Feasibility`

- 非空 **311／311**｜unique **138**

**unique 值前 5 名**：

| 次數 | 值（前 90 字元） |
|---:|---|
| 171 | Recquirement is feasible to implement for functional recquirement. |
| 2 | The requirement is feasible as update services can provide version metadata and the Arbite |
| 2 | The requirement is feasible because the update services can provide package version metada |
| 2 | Achievable using existing TBM signal listeners and ignition state monitoring. |
| 1 | The requirement is feasible because the WiFi Update Service can monitor download activity, |

**抽樣 8 列之全文**：

- `SWE1-FOTA-352` — Software Inventory Request Handling
  > Recquirement is feasible to implement for functional recquirement.

- `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigg
  > Recquirement is feasible to implement for functional recquirement.

- `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced
  > Achievable using existing HMI event handling and signal transmission APIs.

- `SWE1-FOTA-231` — Display What’s New Popup on User Selection
  > Recquirement is feasible to implement for functional recquirement.

- `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is
  > Achievable using existing vehicle property access and conditional execution logic.

- `SWE1-FOTA-199` — Transmit Tester Present During External ECU 
  > Recquirement is feasible to implement for functional recquirement.

- `SWE1-FOTA-286` — OTA Flow Status Reporting
  > Recquirement is feasible to implement for functional recquirement.

- `SWE1-FOTA-173` — Integrate with Signature Verification Module
  > The requirement is feasible as the system can integrate with external or internal security modules through defined interfaces.


---

### 欄 10 — `Description/Action for Impact`

- 非空 **311／311**｜unique **191**

**unique 值前 5 名**：

| 次數 | 值（前 90 字元） |
|---:|---|
| 118 | Requires event source integration, trigger filtering, debounce logic, and validation for m |
| 2 | This requirement impacts multi-source update handling by introducing version-based arbitra |
| 2 | This requirement impacts multi-source update handling and arbitration logic by introducing |
| 2 | This requirement improves user visibility by showing real-time installation progress and r |
| 1 | This requirement adds timeout-based termination and ignition-based retry control to the Wi |

**抽樣 8 列之全文**：

- `SWE1-FOTA-352` — Software Inventory Request Handling
  > Requires event source integration, trigger filtering, debounce logic, and validation for multiple configuration change scenarios.

- `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigg
  > Requires reliable signal decoding, status transition mapping, and synchronization between vehicle message updates and HMI states.

- `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced
  > Impacts update triggering flow and backend signaling.

- `SWE1-FOTA-231` — Display What’s New Popup on User Selection
  > Requires synchronization between message parsing and UI rendering.

- `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is
  > Only impacts feature gating, no runtime complexity.

- `SWE1-FOTA-199` — Transmit Tester Present During External ECU 
  > Requires periodic scheduler handling, message routing, timeout supervision, and coordination with ECU reflash state machine.

- `SWE1-FOTA-286` — OTA Flow Status Reporting
  > Requires event source integration, trigger filtering, debounce logic, and validation for multiple configuration change scenarios.

- `SWE1-FOTA-173` — Integrate with Signature Verification Module
  > This requirement impacts system architecture by introducing dependency on a signature verification module for secure update processing.


---

### 欄 12 — `Description/Action for Risk Factor`

- 非空 **311／311**｜unique **1**

**unique 值前 5 名**：

| 次數 | 值（前 90 字元） |
|---:|---|
| 311 | The requirement is able to reuse upto 50% |

**抽樣 8 列之全文**：

- `SWE1-FOTA-352` — Software Inventory Request Handling
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigg
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-231` — Display What’s New Popup on User Selection
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-199` — Transmit Tester Present During External ECU 
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-286` — OTA Flow Status Reporting
  > The requirement is able to reuse upto 50%

- `SWE1-FOTA-173` — Integrate with Signature Verification Module
  > The requirement is able to reuse upto 50%


---

### 欄 14 — `Description/Action for Reusable`

- 非空 **311／311**｜unique **115**

**unique 值前 5 名**：

| 次數 | 值（前 90 字元） |
|---:|---|
| 191 | The requirement can reuse above 50% of previous requirement, but not fully reuseable. |
| 2 | Existing version handling and Arbiter decision logic can be reused with additional compari |
| 2 | Existing update availability handling and Arbiter-based priority control can be reused wit |
| 2 | Existing status handling and pop-up framework can be reused. |
| 2 | Existing HMI callback handling and signal transmission logic can be reused. |

**抽樣 8 列之全文**：

- `SWE1-FOTA-352` — Software Inventory Request Handling
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigg
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced
  > Reuses HMI interaction and signal write mechanisms.

- `SWE1-FOTA-231` — Display What’s New Popup on User Selection
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is
  > Same logic reused across all TBM FOTA flows.

- `SWE1-FOTA-199` — Transmit Tester Present During External ECU 
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-286` — OTA Flow Status Reporting
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-173` — Integrate with Signature Verification Module
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

