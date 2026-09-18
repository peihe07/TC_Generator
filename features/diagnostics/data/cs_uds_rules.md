# CS 系列之 UDS 規則逐字抽出（R-DIAG29／R-DIAG30 之來源）

來源（皆已在 `sources/MANIFEST.tsv`，CDD-01 T0 已登 sha，本包首次開讀）：

| doc_id | 檔 | sha16 | Analysis Report 列數 |
|---|---|---|--:|
| `sys2_cs00099_sysra` | `SYS2_CS.00099_…_Released.xlsx` | `caffcd100c3d8657` | 808 |
| `sys2_cs00100_sysra` | `SYS2_CS.00100_…_146_150_RAR.xlsx` | `b2dc81d7f92ab278` | 807 |

**只抽下放包 §1 表所列條號之逐字文字；圖片處標 `(image)` 不補述。**

---

## 一　CS.00100 —— UDS 服務之 STELLANTIS 實作

### 1.1　Table 51 —— Input Output Control Parameter（`RQMT 5.6.1.2.1.2-1`，r272）

```text
RQMT 5.6.1.2.1.2-1 Following are reported the request IOCP in STELLANTIS applications
Table 51 - Input Output Control Parameter definitions(NOTE)
Hex     | Description               | Cvt | Mnemonic
00      | Return Control to ECU     | M   | RCTECU
01      | Reset to Default          | M   | RTD
02      | Freeze Current State      | U   | FCS
03      | Short Term Adjustment     | M   | STA
04 - FF | Reserved By Document
          This value is reserved by this document for future definition. | M | RBD

NOTE: Control Option Record parameter is only used when Input/Output Control Type [03 Hex]
(Short Term Adjustment) is used. Example: 2F AA AA 03 XX, where XX is mandatory when 03 hex is used.
```

**此即 R-DIAG29(a) 之來源。** `Cvt` 欄：`M` = mandatory、`U` = unsupported by default。
**注意 `02 Freeze Current State` 為 `U`** —— 非強制支援，不得逕自產其 sibling。

### 1.2　Control Enable Mask（`RQMT 5.6.1.2.1.3-1`，r274）

```text
RQMT 5.6.1.2.1.3-1 Control Enable Mask Record parameter is only used when Input/Output Control Type
equals [03 Hex] AND the Data Identifier contains more than 1 (one) parameter (packeted data identifier).
```

**此即 R-DIAG29(d) 之來源** —— 單參數 DID 之 TC 不得帶 mask。

### 1.3　I/O 期間 session 中斷（`RQMT 5.1.5-4`，r28）

```text
RQMT 5.1.5-4 If during the activation of an ECU component (Input/Output Control By Identifier) the
diagnosis session or the communication is stopped, the ECU must automatically have the total control
of the component in order to avoid any possible damages.
```

（原文含 OCR 雜訊 `hy6thy6t`，逐字為 `the activation hy6thy6tof an ECU component`；此處按語意讀為 `activation of`，**不改原檔**。）

### 1.4　Table 53 —— RoutineControl 子功能（`RQMT 5.7.1.2.1-2`，r286）

```text
Table 53 - Request message sub function definition
Hex (bit 6-0) | Description             | Cvt | Mnemonic
00            | Reserved By Document    | M   | RBD
01            | Start Routine           | M   | STR
02            | Stop Routine            | U   | STPR
03            | Request Routine Results | M   | RRR
04 - 7F       | Reserved By Document …
```

**印證 R-DIAG20**（start `31 01`／stop `31 02`／results `31 03`）。
**`02 Stop Routine` 為 `U`** —— 本 feature 之 `$0307`／`$0309`／`$030A` 之 stop TC 係依 CFTS004 明文
（`When commanded to stop this routine, the HU shall not interrupt…`）而產，不因 `U` 而撤。

### 1.5　Table 2 —— 服務適用矩陣（`RQMT 5.2-1`，r33，節錄）

| 服務 | Hex | Cvt |
|---|---|---|
| Diagnostic Session Control | `$10` | **M** |
| ECU Reset | `$11` | **M** |
| Security Access | `$27` | **C1** |
| Communication Control | `$28` | **M** |
| Tester Present | `$3E` | **M** |
| Control DTC Setting | `$85` | **M** |
| **Link Control** | `$87` | **U** |
| **Read Data By Identifier** | `$22` | **M** |
| **Read Memory By Address** | `$23` | **U** |
| **Read Data By Periodic Identifier** | `$2A` | **U** |
| **Dynamically Define Data Identifier** | `$2C` | **U** |
| **Write Data By Identifier** | `$2E` | **M** |
| **Write Memory By Address** | `$3D` | **U** |
| Clear Diagnostic Information | `$14` | M |

`U` 之六個服務（`$23`／`$2A`／`$2C`／`$3D`／`$87`）為 `DR-DIAG-6`「不支援之 SID」之**候選**，
但 Table 2 之 `U` 意為「**預設不支援**（unsupported by default）」，不等於「本 ECU 不支援」——
**仍待 RD 確認**，佔位 `<unsupported SID>` 不撤。

### 1.6　NRC 處理（r40）

```text
Parameters Definition Response Code parameter values are detailed in ISO 14229-1:2020 in section
"7.5 Server response implementation rules" that contains rules for NRC handling with prioritizations.
In Annex A there is a flowchart that explicitly implements the NRC behavior. ECUs shall adopt NRC $78
for routines/activations that shall not be interrupted and …
```

各服務之 NRC 表一律 `Supported negative response codes (NRC_) Refer to Annex A.`（r63／r72 等 **22 處**）——
**Annex A 為圖（匯出本未帶）→ `DR-DIAG-9`。** 此即 `R-DIAG5(amend3)` 之來源鏈第三級。

---

## 二　CS.00099 —— STLA 診斷總則

### 2.1　S3ECU = 5000 ms（`5.5.6.2` ＋ Table 8，r39）

```text
Table 8 - Session Management Timing
Timing Parameter | Description                                                    | Value
S3 ECU           | S3ECU is defined as the time for the ECU to keep a diagnostic
                   session other than the default Session active while not
                   receiving any diagnostic request message.
                   NOTE: This parameter is referred to as S3server in ISO 14229-2 | 5000ms

RQMT 5.5.6.2-1 If after 5000ms no diagnostic requests have been received, each ECU shall timeout and
return to a Default Session. …
RQMT 5.5.6.2-2 The S3ECU timer shall be restarted upon receiving any diagnostic command which keeps
the ECU in any non-default diagnostic session. …
```

**此即 R-DIAG30(b) 之來源。**

### 2.2　I/O 控制權回收之條件（`RQMT 5.10.2.3-2`，r67）

```text
RQMT 5.10.2.3-2: Each ECU shall re-assume control over the outputs previously under control of the
external test tool (I/O Control Service) if one of the following conditions is met:
 • A request to Return Control to ECU is received
 • A diagnostic session transition occurs
 • An ECU Reset occurs
 • Internal disable conditions (e.g. to prevent damage to the ECU or for security reasons)
   ECU recognizes the condition of "vehicle moving" and/or the condition of "engine not idling"
   (ex.: engine revolutions 1500 rpm);
 • Time-out of Diagnostic communication (S3ECU)
 • Internal disable conditions (e.g. to prevent damage to the ECU or for security reasons)
```

> **逐字轉錄之實測**：下放包 §1 書「6 條件」，原文之項目符號亦為 6 個，
> 惟**第 4 項與第 6 項逐字相同**（`Internal disable conditions (e.g. to prevent damage to the ECU or for security reasons)`），
> 故**相異條件實為 5 個**。此為原文重複，**不改寫**（`[A-DIAG63]`）。

### 2.3　未配置之 I/O（`RQMT 5.10.2.3-5`／`-6`，r67）

```text
RQMT 5.10.2.3-5: If ECU I/O-devices are not configured to be present, the ECU shall negatively respond
to a request from an external test tool as defined by the diagnostic protocol definition.
NOTE: Outputs are configured via Vehicle Configuration (VC) or PROXI based on vehicle architecture.
RQMT 5.10.2.3-6: If ECU I/O-devices are not configured to be present; the ECU shall not allow the
device to be controlled via a request from an external test tool.
```

`as defined by the diagnostic protocol definition` 指向 CS.00100 Annex A（圖）→ NRC 值仍缺。

### 2.4　輸出之預設逾時（`RQMT 5.10.2.3-7`，r67）

```text
RQMT 5.10.2.3-7: The ECU shall support a default timeout value to return to normal operating mode if
no request to halt actuation is received; that is, the ECU shall not continuously cycle an actuator
test indefinitely even if the extended diagnos…（原文於匯出本截斷）
```

**逾時「值」未載** —— 不得據此產具體秒數之 TC。

### 2.5　安全存取（`9.3.3`，r140／r141）

```text
9.3.3 Security Access Process (Seed and Key) … Figure 13 shows a high-level overview …(image)
9.3.3.1 Security Access Service … Figure 15 illustrates and defines this transition …(image)
```

**序列圖與鎖定時間皆為圖** —— R-DIAG30(a) 之「序列 `10 → 27 → 2E/31`」於匯出本**無逐字文字可引**，
只能引節號。是否含 `0x2F` **仍不定**，維持 R-DIAG13 保守（`DR-DIAG-10`）。

---

## 三　CFTS004 對 CS 之引用（T1）

| 本 | 命中 | 內容 |
|---|--:|---|
| CFTS004 索引匯出（404 列） | **5** | `SYS-RA-DIAG-344` `Refer to [CS.00099].`；`SYS-RA-DIAG-403`（objid 6151764）`Please refer [CS.00102], [CS.00021], [CS.00099], [CS.00156], [CS.00103], [CS.00052], [CS.00051] and all the other references described by CFTSs and Reference Mapping.`；另 `[CS-11736]`／`[TFO 09009]`／`[CS.00052]` |
| CFTS004 原始 docx | **18** | 同上之重複出現 |
| SYSAD | **6** | 同上（`CS.00099`／`CS.00052`／`CS-11736`／`TFO 09009`） |

**結論**：
- **`CS.00099` 為 CFTS004 明引** → 其條文作為值來源，位階無疑義。
- **`CS.00102` 為 CFTS004 明引**（`SYS-RA-DIAG-403`）。
- **`CS.00100` 三本皆未明引**（零命中）。其位階依下放包 §1 末段之判斷（STLA 全 ECU 之 UDS 實作規範，同 SYSAD 之 R-DIAG3 先例）採用。
  惟 `SYS-RA-DIAG-403` 之 `and all the other references described by CFTSs and Reference Mapping` 為概括引用，
  且該列 **037 未引用**（Category `Information`）。**此點請分析層覆核**（`[A-DIAG64]`）。
