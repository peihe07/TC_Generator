# SYSAD — 診斷服務之 UDS 序列與 NRC 表（抽取，只抄不改）

來源：`sources/raw/sys3_cfts004_general_diag_sysad/SYS3_CFTS_004_General Diagnostics_System Architectural Design_SYSAD.docx`
sha16 `bc0bad3dbb0710a4`；242 段落、24 表格。抽取日 2026-09-17（CDD-01 任務 3-9）。

---

## 結論（先行）

**本 SYSAD 無 UDS 請求／回應位元組序列表，亦無 NRC 值表。**

全文量測：`UDS` 6 次、`NRC` 1 次（僅見於縮寫表）、`0x7F` 0 次、
`SID` 0 次、`sub-function`／`subfunction` 0 次、`RoutineControl`／`InputOutputControl` 0 次。
唯一之序列表（下 §2）為 **DTC 寫入流程**，而 037 之 DTC 提及列為 **0**。

故 **R-DIAG5(b) 之位元組步驟無法以本 SYSAD 為依據**；其可用者僅 §1 之三個 SID。
CFTS004 ↔ SYSAD 之 NRC 不一致清單因此為**空集**（SYSAD 側無值可比），
非「已比對且一致」—— 是「一方無表」。

---

## §1　SYSAD 所載之 UDS 服務（4.2.5 Assumptions，逐字）

> Diagnostic communication follows ISO 14229 (UDS) protocol.
> Transport layer (e.g., ISO 15765-2 (ISO-TP) over CAN or DoIP) is stable.
> ECU supports required services:
> 0x22 – ReadDataByIdentifier
> 0x2E – WriteDataByIdentifier
> 0x31 – Routine Control
> Tester and ECU are time-synchronized within acceptable latency bounds.

> MDTDiagService is always running before plugin invocation.
> Plugin handles framing/parsing of UDS payloads.
> Client services do not directly access lower diagnostic layer.
> Single ownership of diagnostic state.

**硬體相依**（4.2.6）：
> ECU hardware supporting UDS stack. CAN / Ethernet controller. Diagnostic connector (OBD-II)

**軟體相依**：
> Persistent storage for DTCs on IOC side. UDS stack implementation on IOC side. Security access algorithm library.

### 與 CFTS004 $XXXX 母節之對應（執行層推得，非 SYSAD 所載）

| SYSAD SID | 服務 | CFTS004 母節 | 被引用 L3 數 | 037 列數 |
|---|---|---|---:|---:|
| `0x22` | ReadDataByIdentifier | Read/Write DID Requirements（讀向）| 23 | 254 |
| `0x2E` | WriteDataByIdentifier | Read/Write DID Requirements（寫向）| 同上 | 同上 |
| `0x31` | Routine Control | Diagnostic Routine ID Requirements | 5 | 27 |
| **（SYSAD 無）** | **I-O Control（`0x2F` InputOutputControlByIdentifier）** | **I/O Control DID Requirements** | **14** | **114** |

**缺口（更正）**：I/O Control 母節之 114 列所需之 SID，**SYSAD 未載、CFTS004 亦未載**
（CFTS004 全文 `0x2F`／`$2F` 零命中，僅四處出現 `I/O Control` 字面）。
唯一載明者為 **037 自身之 24 列**，其寫法為
`0x2F (InputOutputControlByIdentifier)` 或 `InputOutputControlByIdentifier (0x2F)`
（母節分佈：I/O 23 列、Routine 1 列；逐列見 `row_kind.tsv` 與 `layer3_assign.tsv`）。

依 R-DIAG5(c)「SID／NRC／sub-function 值以 CFTS004 原文為準；原文未載者寫
`PENDING: DR-{n}`」之**字面**，037 所載之 `0x2F` 亦不得採用 —— 037 非 CFTS004 原文。
其結果為 I/O 母節 114 列之 SID 全數 PENDING，而該值實際上在 037 內明載且無歧義。
**此為條文之適用空白，非資料缺件**，已登 DR-DIAG-1 並列 DECISIONS §2 請 Pei 裁。

---

## §2　SYSAD 之唯一序列表（Table 10，Dynamic Behavior，逐字）

| Step | Interaction Content | SYS.3 Relevance (Dynamic Behavior & Interface) |
|---|---|---|
| 1 (Client Service → MDTDiagService) | `UpdateDTCStatus()` | Report a detected fault or fault status change to the Diagnostic Service |
| 2 (MDTDiagService → DiagServicePlugin) | `onDtcStatus()` | Set the DCT status |
| 2 (DiagServicePlugin → VHAL) | `SendProperty()` | Allows the Diagnostic Service to send validated diagnostic updates to the HAL using standardized vehicle properties. |
| 3 (Diag HAL → IOC) | `ipc_write()` | Used by Diagnostic HAL transmit a serialized DTC write command to the IOC across a protected IPC channel. |

**本表為 DTC 流程**（`UpdateDTCStatus` / `onDtcStatus`）。037 之 DTC 提及列 = 0，
且 R-DIAG8(b) 已裁「DTC（CS.00099）不另立工作簿」，故本表**不進步驟落地**。

---

## §3　元件與角色（Table 9，逐字）

| Component Name | Role Description |
|---|---|
| Client Service | Client Service is responsible for set and clear the DTC. |
| MDTDiagService | The MDTDiagService acts as the central control layer for all diagnostic operations. It provides a standardized interface between Client Service and the lower layer. |
| DiagServicePlugin | DiagSerivePlugin is the part of harman diagnostic service is responsible for set the DTC request received from MDT DiagService through AIDL interface. |
| VHAL | The abstraction layer that translates vehicle hardware signals from the IOC into standardized vehicle properties and vice versa. |
| IOC | IOC is responsible for storing the DTC and status. Eg: ipc_write(). |

**用途**：037 之 Description 混用 `The SW`／`DiagService`／`MDTDiagService` 三種主詞
（實測句型分佈見 `row_kind.tsv`）。本表為該三詞之同一元件鏈之證據，
供 pre_conditions 之元件命名統一參照；不改 test_item 上半之 verbatim。

---

## §4　介面（Table 22，SYSAD_Diagnostics_002，逐字）

| 欄 | 內容 |
|---|---|
| Interface Name | MDTDiagService |
| Interface connect Items | MDTDiagService ↔ DiagSericePlugin |
| Input Criteria | MDTDiagService provide as AIDL interface to DiagSericePlugin DID/RID and DTC request. and subscribe the interface for response |
| Output Criteria | MDTDiagService notify through the callback for DID/RID and DTC to DiagServicePlugin |
| Flow chart | MDTDiagService get the message request and through callback send response to DiagSericePlugin |
| Description | This AIDL interface is responsible for DID/RID and DTC request/response |

---

## §5　CFTS004 ↔ SYSAD 之 NRC 不一致清單

**空集**。理由見 §0 結論：SYSAD 無 NRC 值。

CFTS004 側之 NRC 載值實測（全 404 列）：
- 含 `negative response` 之列：**7**
- 其中帶值者 **5**：`$22, Conditions Not Correct` ×2（r32 SYS-RA-DIAG-031、r321 SYS-RA-DIAG-320）；
  `"Request Out of Range", code $31` ×3（r267 SYS-RA-DIAG-266、r271 SYS-RA-DIAG-270、r372 SYS-RA-DIAG-371）
- 無值者 2：r57 SYS-RA-DIAG-056「shall provide a negative response」（未指定）

037 側需要 NRC 之列 **230**（negative 135 ＋ unsupported 95）。
逐列覆蓋見 `nrc_coverage.tsv`：CFTS004 有值 5／僅 037 有值 20／**兩者皆無值 205**。
