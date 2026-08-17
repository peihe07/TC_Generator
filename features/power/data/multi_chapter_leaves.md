# B1 — 跨多章節 leaf 清單（R-P15(b) 之裁定素材）

> 依 R-P15(b)：本檔**不含任何建議歸屬**。指派為 Pei 之裁決。
> 產生指令：`python features/power/scripts/build_b1.py`
> 錨點鏈採 §C 字面讀法（rule 3 之 item id 僅比對需求錨點）。
> 已驗：改採含章節錨點 id 之延伸讀法，11 個 leaf 之名單不變。

---

## 1. `SWE-PM-001`

**Requirement Title**：Full-Operation

**Source Requirement ID 欄之完整 token 清單**（4 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0016
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0016` | CFTS009 | `4941357` | §1.6.2.1.1 — Full-Operation |
| `Sys-RA-PM-0016` | CFTS009 | `4941358` | §1.6.2.1.1 — Full-Operation |
| `Sys-RA-PM-0016` | CFTS009 | `4941360` | §1.6.2.1.1 — Full-Operation |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.1（出現 3 次）
- CFTS009 §1.6.2.1.14（出現 1 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.1

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Full-Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to full operation to enable all features. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and service
```

---

## 2. `SWE-PM-002`

**Requirement Title**：Idle

**Source Requirement ID 欄之完整 token 清單**（9 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0018
Sys-RA-PM-0019
Sys-RA-PM-0020
Sys-RA-PM-0022
Sys-RA-PM-0023
Sys-RA-PM-0024
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0018` | CFTS009 | `4941364` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0018` | CFTS009 | `4941365` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0019` | CFTS009 | `4941366` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0020` | CFTS009 | `4941369` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0022` | CFTS009 | `4941371` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0023` | CFTS009 | `4941372` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0024` | CFTS009 | `4941373` | §1.6.2.1.2 — Idle |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.2（出現 7 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.2

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Idle' power state through custom power interface
* MD power service shall apply power policy corresponding to Idle. Ensure
 - Display is off
 - audio is muted except for ADAS related chimes
 - Bluetooth is on
 - Tuner is on
 - USB is off
 - AUX is off
* All applications a
```

---

## 3. `SWE-PM-003`

**Requirement Title**：Partial Operation

**Source Requirement ID 欄之完整 token 清單**（6 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0029
Sys-RA-PM-0030
Sys-RA-PM-0031
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0029` | CFTS009 | `4941391` | §1.6.2.1.3 — Partial Operation |
| `Sys-RA-PM-0029` | CFTS009 | `4941392` | §1.6.2.1.3 — Partial Operation |
| `Sys-RA-PM-0029` | CFTS009 | `4941393` | §1.6.2.1.3 — Partial Operation |
| `Sys-RA-PM-0029` | CFTS009 | `4941394` | §1.6.2.1.3 — Partial Operation |
| `Sys-RA-PM-0030` | CFTS009 | `4941396` | §1.6.2.1.3 — Partial Operation |
| `Sys-RA-PM-0031` | CFTS009 | `4941400` | §1.6.2.1.4 — Stolen Vehicle Mode |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（4 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.3（出現 5 次）
- CFTS009 §1.6.2.1.4（出現 1 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.3

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Partial Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to Partial Operation. Ensure
 - Display is off except to show Antitheft screen
 - audio shall be muted except for ADAS related chimes
 - Bluetooth is of
```

---

## 4. `SWE-PM-004`

**Requirement Title**：Timed

**Source Requirement ID 欄之完整 token 清單**（5 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0033
Sys-RA-PM-0056
Sys-RA-PM-0131
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0033` | CFTS009 | `4941402` | §1.6.2.1.5 — Timed |
| `Sys-RA-PM-0033` | CFTS009 | `4941403` | §1.6.2.1.5 — Timed |
| `Sys-RA-PM-0033` | CFTS009 | `4941404` | §1.6.2.1.5 — Timed |
| `Sys-RA-PM-0033` | CFTS009 | `4941406` | §1.6.2.1.5 — Timed |
| `Sys-RA-PM-0033` | CFTS009 | `4941407` | §1.6.2.1.5 — Timed |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |
| `Sys-RA-PM-0131` | CFTS009 | `4941663` | §1.6.2.1.15.1 — ICS Wakeup Reasons by POWER Button Pressed |

**相異章節集合**（4 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.15.1（出現 1 次）
- CFTS009 §1.6.2.1.5（出現 5 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.5

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Timed' power state through custom power interface
* MD power service shall apply power policy corresponding to Timed power state. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power st
```

---

## 5. `SWE-PM-005`

**Requirement Title**：Standby

**Source Requirement ID 欄之完整 token 清單**（4 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0035
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0035` | CFTS009 | `4941410` | §1.6.2.1.6 — Standby |
| `Sys-RA-PM-0035` | CFTS009 | `4941411` | §1.6.2.1.6 — Standby |
| `Sys-RA-PM-0035` | CFTS009 | `4941412` | §1.6.2.1.6 — Standby |
| `Sys-RA-PM-0035` | CFTS009 | `4941413` | §1.6.2.1.6 — Standby |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.6（出現 4 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.6

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Standby' power state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* All applications and service
```

---

## 6. `SWE-PM-006`

**Requirement Title**：Sleep

**Source Requirement ID 欄之完整 token 清單**（4 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0037
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0037` | CFTS009 | `4941416` | §1.6.2.1.7 — Sleep |
| `Sys-RA-PM-0037` | CFTS009 | `4941417` | §1.6.2.1.7 — Sleep |
| `Sys-RA-PM-0037` | CFTS009 | `4941418` | §1.6.2.1.7 — Sleep |
| `Sys-RA-PM-0037` | CFTS009 | `4941419` | §1.6.2.1.7 — Sleep |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.7（出現 4 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.7

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Sleep' power  state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* Transiting to sleep state, al
```

---

## 7. `SWE-PM-007`

**Requirement Title**：Bench

**Source Requirement ID 欄之完整 token 清單**（4 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0039
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0039` | CFTS009 | `4941422` | §1.6.2.1.8 — Bench |
| `Sys-RA-PM-0039` | CFTS009 | `4941423` | §1.6.2.1.8 — Bench |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.8（出現 2 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.8

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify 'Bench' state through custom power interface
* subcomponents shall ensure all features are available for development / testing
```

---

## 8. `SWE-PM-008`

**Requirement Title**：Logistic Mode

**Source Requirement ID 欄之完整 token 清單**（13 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0040
Sys-RA-PM-0041
Sys-RA-PM-0042
Sys-RA-PM-0043
Sys-RA-PM-0044
Sys-RA-PM-0045
Sys-RA-PM-0056
Sys-RA-PM-0184
Sys-RA-PM-0185
Sys-RA-PM-0186
Sys-RA-PM-0187
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0040` | CFTS009 | `4941425` | **未解析** |
| `Sys-RA-PM-0041` | CFTS009 | `4941426` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0041` | CFTS009 | `4941427` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0041` | CFTS009 | `4941428` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0042` | CFTS009 | `4941430` | **未解析** |
| `Sys-RA-PM-0043` | CFTS009 | `4941431` | §1.6.2.1.10 — Logistic Standby |
| `Sys-RA-PM-0043` | CFTS009 | `4941432` | §1.6.2.1.10 — Logistic Standby |
| `Sys-RA-PM-0044` | CFTS009 | `4941433` | **未解析** |
| `Sys-RA-PM-0045` | CFTS009 | `4941434` | §1.6.2.1.11 — Logistic Sleep |
| `Sys-RA-PM-0045` | CFTS009 | `4941435` | §1.6.2.1.11 — Logistic Sleep |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |
| `Sys-RA-PM-0184` | CFTS009 | `4941755` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0185` | CFTS009 | `4941756` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0186` | CFTS009 | `4941757` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0187` | CFTS009 | `4941758` | §1.6.7.1 — TLM algorithm requirements |

**相異章節集合**（6 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.10（出現 2 次）
- CFTS009 §1.6.2.1.11（出現 2 次）
- CFTS009 §1.6.2.1.14（出現 1 次）
- CFTS009 §1.6.2.1.9（出現 3 次）
- CFTS009 §1.6.7.1（出現 4 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.7.1

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

---

## 9. `SWE-PM-009`

**Requirement Title**：Init state

**Source Requirement ID 欄之完整 token 清單**（8 個）：

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0049
Sys-RA-PM-0050
Sys-RA-PM-0051
Sys-RA-PM-0052
Sys-RA-PM-0053
Sys-RA-PM-0056
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0013` | CFTS009 | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | CFTS009 | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0049` | CFTS009 | `4941441` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0049` | CFTS009 | `4941442` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0050` | CFTS009 | `4941443` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0050` | CFTS009 | `4941445` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0051` | CFTS009 | `4941446` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0052` | CFTS009 | `4941447` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0053` | CFTS009 | `4941449` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0053` | CFTS009 | `4941450` | §1.6.2.1.13 — TLM initialization: Init state |
| `Sys-RA-PM-0056` | CFTS009 | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1（出現 2 次）
- CFTS009 §1.6.2.1.13（出現 8 次）
- CFTS009 §1.6.2.1.14（出現 1 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.13

**Requirement Description 前 300 字元**：

```
* HW supplier shall notify Init power state though custom power state interface
* subcomponents shall stop activities upon receiving Init power state, until exiting this state
* Settings service shall restore settings to before init state values after exiting init state
```

---

## 10. `SWE-PM-057`

**Requirement Title**：Proxi Parameter management

**Source Requirement ID 欄之完整 token 清單**（7 個）：

```
Sys-RA-PM-0146
Sys-RA-PM-0147
Sys-RA-PM-0148
Sys-RA-PM-0216
Sys-RA-PM-0217
Sys-RA-PM-0218
Sys-RA-PM-0158
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0146` | CFTS009 | `4941692` | §1.6.2.1.17 — Proxi Parameters management |
| `Sys-RA-PM-0147` | CFTS009 | `4941693` | §1.6.2.1.17 — Proxi Parameters management |
| `Sys-RA-PM-0148` | CFTS009 | `4941695` | §1.6.2.1.17 — Proxi Parameters management |
| `Sys-RA-PM-0216` | CFTS009 | `4941814` | §1.8.1.1.1 — ID 1 Description |
| `Sys-RA-PM-0217` | CFTS009 | `4941815` | §1.8.1.1.1 — ID 1 Description |
| `Sys-RA-PM-0218` | CFTS009 | `4941817` | §1.8.1.1.1 — ID 1 Description |
| `Sys-RA-PM-0158` | CFTS009 | `4941706` | §1.6.3.1.1 — SwitchOff_Timeout_Setting.Req management |
| `Sys-RA-PM-0158` | CFTS009 | `4941707` | §1.6.3.1.1 — SwitchOff_Timeout_Setting.Req management |
| `Sys-RA-PM-0158` | CFTS009 | `4941708` | §1.6.3.1.1 — SwitchOff_Timeout_Setting.Req management |

**相異章節集合**（3 個）：

- CFTS009 §1.6.2.1.17（出現 3 次）
- CFTS009 §1.6.3.1.1（出現 3 次）
- CFTS009 §1.8.1.1.1（出現 3 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.6.2.1.17

**Requirement Description 前 300 字元**：

```
The System UI shall read the PROXI parameter Switch_Off_Time using the interface provided by the hardware supplier and shall use the hardware supplier’s interface to set the user-selected value to SwitchOff_Timeout_Setting.Req.

TheSystem UI shall also provide an option for the user to select:

"Cas
```

---

## 11. `SWE-PM-093`

**Requirement Title**：Start-Up Animation Playback and Skip Logic - Suspend-Resume

**Source Requirement ID 欄之完整 token 清單**（2 個）：

```
Sys-RA-PM-0007, Sys-RA-PM-0274
```

**每個 token 之解析結果**：

| token | 域 | Polarion item id | 解析到之 (章節號, 章節標題) |
|---|---|---|---|
| `Sys-RA-PM-0007` | CFTS009 | `4941301` | §1.3.5 — Start-Up and Shut Down Animations |
| `Sys-RA-PM-0274` | CFTS009 | `4941941` | §1.9.8 — Startup Animation |

**相異章節集合**（2 個）：

- CFTS009 §1.3.5（出現 1 次）
- CFTS009 §1.9.8（出現 1 次）

**02 包所採規則（次數最多、同數取最深）指派之結果**：CFTS009 §1.3.5

**Requirement Description 前 300 字元**：

```
Cold boot animation is HW supplier responsibility.

For suspend-resume (warm boot) case, System UI (Status Bar HMI) shall manage start-up animation upon receiving power state change notifications as follows:

Play conditions:
1. HW Supplier VPS shall notify System UI via the custom power state notif
```
