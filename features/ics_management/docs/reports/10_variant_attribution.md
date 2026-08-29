# 下放包 10 作業 A —— 本 DUT 之變體歸屬量測（Associated / Disassociated）

- **問題**：本 DUT（`newR1L`／`R1L-R`，Atlantis High）是 **Associated**（觸控螢幕整合於 HU）
  還是 **Disassociated**（'Silver Box'，外接 DCSD）？
- **腳本**：`features/ics_management/scripts/variant_probe_10.py`（新建；`--m1`～`--m6`／`--all`）
- **依令**：`cfts020_probe.py` 以 `importlib` 唯讀載入，未改一字；本輪未執行任何 git 指令
  （含唯讀指令）；未改任何 TC JSON、未動任何 `specification_reference`、未生成任何 TC。
- **禁循環令**：**§1.8 與 §1.18 之內容不得作為判定變體之證據**。本報告逐項標記
  「脫離／循環」。禁區二節之數字僅作**對照陳列**，一律標 `【循環·不計入】`。

---

## §0 掃描條件

### §0-1 各檔抽取法

| 素材 | 抽取法 |
|---|---|
| CFTS020（物件面） | `importlib` 唯讀載入 `features/ics_management/scripts/cfts020_probe.py` 之 `parse()`。抽取法與判準見該檔 docstring（`word/document.xml` → `</w:p>` 換行、`</w:tc>` tab、去標籤、`html.unescape`；物件屬性頭 `^(\d{7}): \[`；本文取次一行；軸缺記 `None`）。**判定一律 R-ICS2 v2(b)**。實測物件母數 **2180** |
| CFTS020（行面） | 重用同檔 `doc_lines()`；章節行以 `SEC_RE` 命中且不含 `PAGEREF`（目次行帶 `PAGEREF`） |
| 其他 `.docx`（SYSAD） | 與上同一抽取法，另寫於 `variant_probe_10.docx_lines()` |
| `.xlsx`（SYS2／SWRA／LID／HMI） | `openpyxl`，`read_only=True`、`data_only=True`；逐分頁逐列以 `\t` 併為一行 |
| `.dbc` | **一律 `latin-1` 開檔**；`BO_ <id> <name>: <dlc> <sender>` 起訊息，**邊界由下一個 `BO_` 判定**；`SG_` 行末空白後之逗號串為接收節點 |

### §0-2 詞界與大小寫

- `DCSD`／`LTM`／`TLM`／`ICS`／`_ADspl`／`_DDspl`：**區分大小寫之子字串比對**
  （`_ADspl`／`_DDspl` 本身即帶底線，無需 `\b`）。
- `Associated`／`Disassociated`：`\bAssociated\b`／`\bDisassociated\b`（區分大小寫）；
  另附不分大小寫之 `\b(dis)?associated\b` 對照數。
- `Silver Box`：區分大小寫之字面；另附 `silver\s*box`（`re.I`）以捕獲 `SilverBox` 之無空白寫法。
- **軸值比對**：區分大小寫之精確字串集合交集（沿用 `cfts020_probe` 之規則，不作正規化、不作前綴比對）。

### §0-3 「出現」之計數單位

物件面 = **物件數**（同物件內多次記 1，另附次數 `n`）；行面 = **行數**，另附總次數。

### §0-4 LID 表頭自驗結果

檔：`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，分頁 `CAN Mapping`。

- 分頁清單（實測 14 個）：`Rev History`, `Notes`, **`CAN Mapping`**, `Proxi & Configuration`,
  `Atlantis Low Specific Signals`, `M240 …`, `BSEGMENT …`, `332BEV …`, `M182BEV …`,
  `250MCA …`, `965 …`, `ALFAMCA …`, `637MCA …`, `356MCA …`
- 列數（含表頭）：**2627**
- **表頭自驗**（取前 5 列中非空欄數最多者）：命中 **第 2 列（0-based）**，欄名逐字：
  `Logical Identifier`, `Function`, `Object Text`, `Arch Basis`,
  `Transfer Function (from other CANs to CAN basis)…`,
  然後為 5 組重複之 `Signal Name / CAN / Format / SNA / VFs`，
  末尾 `Usage Comment`, `Primary CFTS Usage`, `Revision Flag`, `Revision Comments`, `Sort Tool`。
- 資料列數：**2624**

### §0-5 DBC 開檔編碼

`latin-1`，二檔皆是。BHCAN 節點宣告 `BU_:` 實測 17 個；FDCAN8 實測 4 個（見 §3）。

---

## §1 量測項 1 —— 變體定義之完整逐字與 `_ADspl`／`_DDspl` 之綁定力

**脫離 §1.8／§1.18：是**（全部證據取自 §1.2 Introduction）。

### §1-1 `CFTS020-4819134` 全文（逐字，非節錄）

物件屬性（實測）：
`§1.2 Introduction {4819128}`；`Artifact Type = Description`；`State = Approved`；
`ECU = ['ALL']`；
`Radio = ['VP1.5','VP365','R1L','High','VP484','R1H','VP2R84','VP4','VP4R7','VP5R120','VP2','VP384','VP1','VP4R84','R1L-R','VP2.5','VP465','VP2R5','VP2R7','R1M','VP3']`（21 值，**含 `R1L` 與 `R1L-R`**）；
`EE Architecture = ['All']`；R-ICS2 v2(b) 判定 **不適用**（`ECU ['ALL'] ∩ {ICS,LTM} = ∅`）。

> `Note: There are essentially 2 variants of the LTM and ETM Radio HUs; those with the touch screen integrated into the HU module are known as Associated variants while those HUs that interface to an external touch screen module (DCSD) are known as Disassociated variants (and are also referenced as a 'Silver Box' variants).  In order to distinguish between these two types of HUs we are using a '_ADspl' suffix on the Associated variants and '_DDspl' suffix on the Disassociated variants.`

**全文即上引一段，無其他文字**（前一輪之節錄與全文一致，無遺漏後半）。

### §1-2 前後鄰接物件（各 3 個，逐字）

| 位移 | ObjectID | 節 | Radio 軸 | 逐字（要點） |
|---|---|---|---|---|
| −3 | `4819129` | 1.2 | `['allSys']` | `This CFTS chapter discusses requirements for variants of the ICS and the DCSD modules that interact with the various LTM_ADspl, ETM_ADspl, LTM_DDspl andETM_DDspl Radio HUs and optional CVPM, CVPAM, DTV, VRM and TMM components when present.` |
| −2 | `4819130` | 1.2 | `['allSys']` | `In the case of conflict between this document and the HMI requirements, the HMI requirements shall have precedence.` |
| −1 | `4819133` | 1.2 | 21 值含 `R1L`,`R1L-R` | `Notation Convention: The list of Component Acronyms referenced in this chapter are: LTM_ADspl, LTM_DDspl, ETM_ADspl, ETM_DDspl, ICS_OldwithBack, ICS_Maserati, ICS_NewWithPower, DCSD84_NoMTouch, DCSD121_NoMTouch, DCSDX, DCSD120_wICS_Port, DCSD70_wICS_NonCAN, DCSD120_wICS, CVPM, CVPAM, VRM, DTV, FPDM, and TMM. …` |
| **+0** | **`4819134`** | 1.2 | 21 值含 `R1L`,`R1L-R` | 見 §1-1 |
| +1 | `4819135` | 1.2 | 21 值含 `R1L`,`R1L-R` | `Note: There are many DCSD variants that pair with the disassociated variants of the HUs. …` **（含 DCSD 與 Radio 型號之配對清單，見 §1-5）** |
| +2 | `4819136` | 1.2 | `['allSys']` | `All DTCs shall self-heal at 40 key cycles, based on harmonized specification CS.00099.` |
| +3 | `4819137` | 1.2 | `['allSys']` | `All DTCs shall self-heal at 100 key cycles, based on harmonized specification CS-11736.` |

### §1-3 `_ADspl`／`_DDspl` 於 CFTS020 全文之出現位置（實測）

| 掃描面 | `_ADspl` | `_DDspl` |
|---|---|---|
| 物件面（命中物件數） | **3** | **3** |
| 行面（命中行數／總次數） | **3 行／5 次** | **3 行／5 次** |

命中之三個物件**完全相同**：`4819129`、`4819133`、`4819134`，**全部位於 §1.2 Introduction**，
`ECU` 軸分別為 `['ALL']`（三者皆是）。

行層級位置：`L402`（= `4819129`）、`L406`（= `4819133`）、`L408`（= `4819134`）。
**CFTS020 全文再無第四處。**

前綴組合實測（行層級，區分大小寫）：

```
LTM_ADspl: 2    LTM_DDspl: 2    ETM_ADspl: 2    ETM_DDspl: 2
RRM_ADspl: 0    RRM_DDspl: 0
```

即：`LTM` 與 `ETM` **各自都同時擁有 `_ADspl` 與 `_DDspl` 兩型**，且二後綴總是**成對並列**出現。

### §1-4 `R1L-R` 與後綴之綁定檢定（**本項為交辦所指之「決定性證據」候選**）

| 檢定 | 實數 |
|---|---|
| `_ADspl` × Radio 軸含 `R1L-R` 之物件 | **2** |
| `_DDspl` × Radio 軸含 `R1L-R` 之物件 | **2** |
| `_ADspl` × 本文字面含 `R1L-R` 之物件 | **0** |
| `_DDspl` × 本文字面含 `R1L-R` 之物件 | **0** |
| `_ADspl` × Radio 軸含 `R1L` 之物件 | **2** |
| `_DDspl` × Radio 軸含 `R1L` 之物件 | **2** |

**答（量測項 1）：`_ADspl`／`_DDspl` 無法與 `R1L-R` 綁定 —— 綁定力為零。**

理由（實測，非推測）：

1. 二後綴只出現於**同一組 3 個物件**，且每次都**成對並列**（`LTM_ADspl, ETM_ADspl, LTM_DDspl, ETM_DDspl`）。
   沒有任何一個物件只提 `_ADspl` 而不提 `_DDspl`（或反之）。
2. 這 3 個物件的 `Radio` 軸**同時含 `R1L` 與 `R1L-R`**（`4819133`／`4819134`）或為 `allSys`（`4819129`），
   即二後綴對 `R1L-R` 之屬性面命中**完全對稱**（2 : 2）。
3. 後綴是加在 **Component Acronym（`LTM`／`ETM`）** 上，不是加在 **Radio 軸值（`R1L`／`R1L-R`）** 上。
   CFTS020 全文查無 `R1L_ADspl`／`R1L-R_DDspl` 之類寫法（掃法：`_ADspl`／`_DDspl` 之 3 行逐字全覽）。

**故本項為「查無」，非決定性證據。交辦所預期之「把 `R1L-R` 與某一後綴綁定」在本文件內不可能達成。**

### §1-5 附帶實測（`4819135` 之 DCSD 配對清單）—— 與本題有關之逐字

`4819135`（§1.2，Radio 軸含 `R1L`、`R1L-R`）逐字節錄：

> `b) The 10.1 inch DCSDX which will be paired with the VP4R84, R1H, R1L radio HUs.`
> `b) DCSD70_wICS_NonCAN which will be paired with the R1 radio HU.`

即 **`R1L` 被明列為與 DCSD（10.1 吋 DCSDX）配對之 radio HU**。
`R1L-R` 本身未於該清單中被點名（該清單只列 `VP4R84, R1H, R1L, R1, VP5R120, VP384, VP484, VP3`）。
**處置**：此為 `R1L` 存在 Disassociated 配對之正面證據，但**不足以單獨定 `R1L-R`**
（`R1L` 與 `R1L-R` 於 CFTS020 是兩個獨立軸值）。列為**弱正向**（指向 Disassociated），不作主證。

---

## §2 量測項 2 —— 四個 `Configuration parameters` 節之適用性

**脫離 §1.8／§1.18：是**（四節皆非該二節）。

行層級掃描 `Configuration parameters` 之章節標題（區分大小寫），實測全部命中：

```
§1.7.1    Configuration parameters {4819530}
§1.7.1.1  Configuration parameters description {4819531}
§1.10.1   Configuration parameters {4820161}
§1.10.1.1 Configuration parameters description {4820162}
§1.13.1   Configuration parameters {4820375}
§1.13.1.1 Configuration parameters description {4820376}
§1.17.1   Configuration parameters {4821670}
§1.17.1.1 Configuration parameters description {4821671}
```

**恰為交辦所列之四節，無第五節。**

### §2-1 四節之逐物件判定（R-ICS2 v2(b)）

| 節 | 標題逐字 | 所屬分支 | 物件數 | **判適用** |
|---|---|---|---|---|
| §1.7 | `Function properties - PNet - ICS and Associated HU {4819529}` | Associated | 5 | **0** |
| §1.10 | `Function properties - PNet & AtlHi - ICS, Silver Box HU and DCSD {4820160}` | Disassociated | 5 | **0** |
| §1.13 | `Function properties - PNet & AtlHi - VP5R120 Silver Box HU and DCSD120_wICS_Port {4820374}` | Disassociated（VP5R120 專用） | 2 | **0** |
| §1.17 | `Function properties - CUSW - ICS and Associated HU {4821669}` | Associated | 1 | **0** |

**逐物件之不適用理由（實測）**：

- §1.7 之 5 物件：`4819532`(Radio `noSys` + EE `PowerNet`)、`4819533`／`4819534`／`4819535`(EE `PowerNet`)、
  `4819536`(Radio `noSys`)。**全落在 EE 軸或 Radio 軸**。
- §1.10 之 5 物件：`4820163`(Radio `noSys` + EE `PowerNet`)、
  `4820164`／`4820165`／`4820166`（Radio `['VP5R120','VP4R84','VP484','R1M','R1H','VP384']`，
  **不含 `R1L` 亦不含 `R1L-R`**）、`4820167`(Radio `noSys`)。
- §1.13 之 2 物件：Radio `['VP5R120','R1M','R1H']`。
- §1.17 之 1 物件：`4821672`，Radio `allSys` 但 EE `['CUSW']`。

### §2-2 答（量測項 2）

**四節一律判不適用（0／0／0／0）—— 本項為「查無」，不指出任何分支。**

交辦假設「四節分屬不同架構分支，何者判適用即指出本 DUT 落在哪一分支」，
**該假設在實測上落空**：四節全部不適用，故無分流訊號。

**附帶之弱反證（須誠實列出）**：§1.10.1.1 之三個 `DSP_SK_PRSNT` 需求（`4820164`～`4820166`）
是 **Silver Box 分支之 Configuration parameter**，其 `Radio` 軸列了 6 個型號而
**`R1L-R` 與 `R1L` 皆不在其中**。此為指向「`R1L-R` 不屬 Silver Box」之**弱反證**。
處置見 §7-2(反-1)。

---

## §3 量測項 3 —— DCSD 之存在與否（結構證據）

**脫離 §1.8／§1.18：是**（LID 表與 DBC 皆為 CFTS020 外部素材）。

### §3-1 LID 全表中與 DCSD 相關之項

表頭自驗結果見 §0-4。資料列 **2624**。

| 掃描 | 實數 |
|---|---|
| 含 `DCSD`（區分大小寫，全欄）之資料列 | **56** |
| `Logical Identifier` 欄以 `DCSD` 起首之列 | **25** |
| 該 25 列之 `Arch Basis` 分佈 | `None` 16、**`AtlHi` 7**、`PNet` 2 |
| 含詞界 `LTM` 之資料列 | **9** |
| 含詞界 `TLM` 之資料列 | **0** |
| 含詞界 `ICS` 之資料列 | **12**（對照用） |

> 附註：`LTM` 之 9 列全部與本題無關（`BatPwrUsageDisp`／`EngPwrUsageDisp`／`Est_Range_Disp`／
> `HVBatSOC_HCP` 等 HEV 顯示訊號），其寫法一律為 `HCP_DISP.<訊號>  (ETM) / … (LTM)`
> —— 即 `LTM` 在該表中是**顯示側之接收者**。與 DCSD 無交集（`LTM` 與 `DCSD` 同列者：**0**）。

`Arch Basis = AtlHi` 之 7 個 DCSD LID（逐字，`Logical Identifier` 欄）：
`DCSD_Enter`、`DCSD_Power`、`DCSD_Screen_Off`、`DCSD_TUNEKNOB_DIR`、`DCSD_TUNEKNOB_VAL`、
`DCSD_VOLKNOB_DIR`、`DCSD_VOLKNOB_VAL`。

> **即：DCSD 於 Atlantis High 架構（= 本 DUT 之 EE）上有 7 個 LID 在案，非僅 PowerNet 遺留。**

**焦點三 LID 之逐字（本項為本報告最強之非循環證據之一）**：

| LID | `Function` 逐字 | `Arch Basis` | `Signal Name` | `CAN` | `VFs` |
|---|---|---|---|---|---|
| `DCSD_DISP_STAT` | `DCSD display status` | `PNet` | `DCSD_CTRL.DCSD_DISP_STAT` | `CAN-B` | `650` |
| **`RQ_DISP_INTS`** | **`HU calculated display intensity for use by DCSD.`** | `PNet` | `TGW_3I.RQ_DISP_INTS` | `CAN-B` | `650` |
| `TGW_DISP_STAT` | `HU display status` | `pnet` | `TGW_A1.TGW_DISP_STAT` | — | `688 / 659 / 650` |

`RQ_DISP_INTS` 之定義逐字為 **「HU 算出、供 DCSD 使用之顯示亮度」**。
本 DUT 之 SYSAD 逐字指明本 DUT 產生 `RQ_DISP_INTS`（見 §4-2），二者接合成一條完整鏈路。

### §3-2 二綁定 DBC 中之 DCSD 收發關係

開檔編碼 `latin-1`；訊息邊界由下一個 `BO_` 判定。

#### `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`

- `BU_:` 節點 **17** 個，逐字：
  `AMP ANC BCM DALM DCSD DDM DSM ECC ICS PDM PFTM PSM PSSM PTGM SGW SMMD SMMP`
  → **含 `DCSD`（是）**、含 `ICS`（是）、**含 `LTM`（否）**、含 `TLM`（否）
- `BO_` 訊息數 **340**
- **DCSD 為發方**之訊息 **4**：
  `CFG_DATA_CODE_RSP_DCSD`(11 訊號)、`DIAGNOSTIC_RESPONSE_DCSD`(1)、
  **`DIS_CENTERSTACK`**(25)、`NWM_DCSD`(7)
- 訊號名含 `DCSD` 者 **42**（含 `DIS_CENTERSTACK.DCSD_DISP_STAT`／`DCSD_Mute`／`DCSD_Power`／
  `DCSD_Screen_Off`／`DCSD_VOLKNOB_*`／`DCSD_TUNEKNOB_*` 等 25 個）
- `DIS_CENTERSTACK`（sender = `DCSD`）之接收方逐字：全部為 `ECC`／`SGW`／`BCM` 之組合，
  **無一則以 `LTM` 或 `TLM` 為接收方**
- 節點 `LTM`：發送 **0**、接收 **0**（該節點不存在於本 DBC）
- 節點 `TLM`：發送 **0**、接收 **0**
- 節點 `ICS`：發送 **7**（`CENTERSTACK1/2/4`、`CFG_DATA_CODE_RSP_CENTERSTACK`、
  **`CLIMATIC_PANEL`**、`DIAGNOSTIC_RESPONSE_CENTERSTACK`、`NWM_CENTERSTACK`）、接收 **23**
- **DCSD 與 `LTM`／`TLM` 同現於同一訊息之收發方：0**

#### `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc`

- `BU_:` 節點 **4** 個，逐字：`ETM LTM SGW TBM` → **含 `LTM`（是）**、**含 `DCSD`（否）**
- `BO_` 訊息數 **323**
- DCSD 為發方之訊息 **0**；訊號名含 `DCSD` **0**；`SG_` 行末接收節點含 `DCSD` **0**
- 訊息名含 `DCSD` 者 **2**，逐字：
  `BO_ 2564451057 DIAGNOSTIC_REQUEST_DCSD: 8 TBM`（發方 `TBM`，收方 `SGW`）
  `BO_ 2564485482 DIAGNOSTIC_RESPONSE_DCSD: 8 SGW`（發方 `SGW`，收方 `TBM`）
  → **二則皆與 `LTM` 無關**（`LTM` 既非發方亦非收方）
- 節點 `LTM`：發送 **0**、接收 **120**
- **DCSD 與 `LTM`／`TLM` 同現於同一訊息之收發方：0**

#### §3-3 補測：`LTM` 在 FDCAN8 上是否收到任何 ICS／DCSD 按鍵訊號

掃法：`FDCAN8` 全部 323 則訊息之 `SG_`，正則
`ICS|CENTERSTACK|CLIMATIC|Knob|KNOB|Screen_Off|ScreenOff|Mute|Front_Panel`（`re.I`）
或訊息名含 `CENTERSTACK|CLIMATIC`。命中 **5** 條，逐字：

```
DIAGNOSTIC_REQUEST_CENTERSTACK(sender=TBM).N_PDU  -> SGW
DIAGNOSTIC_RESPONSE_CENTERSTACK(sender=SGW).N_PDU -> TBM
EPS_FD_1(sender=SGW).ElectricSteeringFailSts      -> ETM,LTM,TBM
IPC_VEHICLE_SETUP(sender=SGW).TelematicSetupACK   -> ETM,LTM
TBM_SCHEDULE_FD_2(sender=TBM).TelematicSetupAck_TBM -> ETM,LTM
```

**`LTM` 收到之 ICS 相關訊號：0。`LTM` 收到之 DCSD 相關訊號：0。**

### §3-4 答（量測項 3）

**本 DUT 之 ECU（`LTM`，A-ICS47）於二綁定 DBC 中與 DCSD 無任何訊號關係 —— 但本項不得判為
「指向 Associated」，因為同一檢定同時測出 `LTM` 與 `ICS` 亦無任何訊號關係（0 條）。**

理由：本 DUT 之全部 27 條 TC 皆以 ICS→HU 之按鍵訊號為前提（規格明載），
若「無訊號關係 ⇒ 不存在」成立，則同一推論會導出「本 DUT 與 ICS 亦不相干」之荒謬結論。
二綁定 DBC 之涵蓋面本身有缺口（與 A-ICS47 之 `$TGW_DISP_STAT$` 空缺、
報告 09 §4-4 之 `Volume_Knob_*`／`Mute.Req`／`Front_Panel_OnOff.Info` 全數查無同型）：
**ICS／DCSD 位於 BHCAN（`LTM` 不在其上），`LTM` 位於 FDCAN8（`DCSD`／`ICS` 皆不在其上），
二網之間的閘道對映（`SGW`）未涵蓋於這二個 DBC 檔。**

**故本項判為「查無，且已證實掃描面有盲區」，對本題之證據值 = 0（雙向皆不成立）。**
交辦所設之「若無訊號關係 → 指向 Associated；反之 → Disassociated」二分法，
在本素材上**前提不成立**（掃描面缺口使雙向皆不可推）。

**惟有一項正向事實成立且不受盲區影響**：
**DCSD 於 `Arch Basis = AtlHi` 有 7 個 LID 在案（§3-1）** —— 即 DCSD 在本 DUT 之 EE 架構上存在，
非 PowerNet 遺留。此為**正向**證據（指向 Disassociated），且脫離 §1.8／§1.18。

---

## §4 量測項 4 —— DUT 自身文件之逐字

**脫離 §1.8／§1.18：是**（SYSAD／SYS2／SWRA／HMI 皆為 CFTS020 之外或其下游 SRA）。

### §4-1 掃描面（實測目錄清單）

`features/ics_management/inputs/`（5 件）：
- `ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
- `R1LR_Atl-H_…_CFTS_020 ICS and DCSD _20260310-1533.docx`
- `R1LR_Atl-H_…_CFTS_022 Functional Specification_20260608-1205.docx`
- `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`
- `SYS3_CFTS020_ICS_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`

`spec-index/sources/`（1 件）：
- `Steering Wheel Controls HMI Logic and Flow SR24 DCR21423 (august 3 2022).xlsx`

> **HMI Logic and Flow 之查無說明**：`spec-index/sources/` 內僅有 **Steering Wheel Controls** 之
> HMI Logic and Flow 一件，**repo 內查無 ICS／HU 之 HMI Logic and Flow**（掃法：上列二目錄
> `rglob("*")` 之 `.docx`／`.xlsx` 全覽）。CFTS020 多處外引之 `TLM HMI`／`HMI Logic and Flow`
> 於 repo 內**不存在**。

### §4-2 逐檔實測（命中行數／總次數）

| 檔 | 行數 | `DCSD` | `Silver Box` | `SilverBox`(i) | `Associated` | `Disassociated` | `_ADspl` | `_DDspl` |
|---|---|---|---|---|---|---|---|---|
| SWRA `.xlsx` | 275 | **0／0** | 0 | 0 | **0** | **0** | 0 | 0 |
| CFTS020 `.docx`（對照） | 5204 | 1484／3303 | 25／25 | 50／50 | 17／18 | 25／26 | 3／5 | 3／5 |
| **SYS2 `.xlsx`** | 794 | **191／730** | 1／1 | 1／1 | 1／2 | **3／4** | 3／5 | 3／5 |
| **SYSAD `.docx`** | 1410 | **5／5** | **0／0** | **0／0** | **0／0** | **1／1** | 0 | 0 |
| HMI（Steering Wheel）`.xlsx` | 1022 | **0／0** | 0 | 0 | 0 | 0 | 0 | 0 |

### §4-3 SYSAD —— 本 DUT 自身之系統架構文件（**本項為本報告之主證**）

`DCSD` 於 SYSAD 命中 **5 行**，逐字全列（一行不漏）：

```
L146: DCSD
L147: Disassociated Central Stack Display
L239: Brightness control using RQ_DISP_INTS executed by display hardware (DCSD MCU control).
L242: DCSD Domain
L1384: R1LR_Atl-H_25PI3.4_Cabin_CFTS_020 ICS and DCSD _SR26_20250813-1632.doc
L1385: SYS1_CFTS_020 ICS and DCSD _SR26_20250813-1632.xlsx
```

（`L146`／`L147` 為 `Table 1 – Abbreviations Table` 之相鄰二行；`L1384`／`L1385` 為參考文件清單。）

**`定義 Definitions` 表（`Table 1` 之後）之逐字，欄位為 `Name` / `Description`**：

```
L238: Backlight Control
L239: Brightness control using RQ_DISP_INTS executed by display hardware (DCSD MCU control).
L242: DCSD Domain
L243: External display module containing LCD, touch controller, MCU, and backlight control.
L244: Display HOT State
L245: Thermal protection state causing brightness reduction or display shutdown (safety behavior).
L246: HU Domain
L247: Domain running AAOS14, ICSClientService, AudioManagerService, HAL, and display logic.
L258: Vehicle Domain
```

**判讀（僅陳述文件所言，不作調和）**：

1. 本 DUT 之 SYSAD **自行定義了一個 `DCSD Domain`**，其定義逐字為
   **`External display module containing LCD, touch controller, MCU, and backlight control.`**
   —— 即「含 LCD、**觸控控制器**、MCU 與背光控制之**外接**顯示模組」。
2. 本 DUT 之 SYSAD 把 `HU Domain` 與 `DCSD Domain` 列為**兩個並列的 Domain**。
3. 本 DUT 之 SYSAD 逐字指明背光控制為
   **`Brightness control using RQ_DISP_INTS executed by display hardware (DCSD MCU control).`**
   —— 亮度由 `RQ_DISP_INTS` 控制，而**執行者是 DCSD 的 MCU**。
4. 本 DUT 之 SYSAD 於多處（`L273`／`L281`／`L389`～`L392`／`L462`／`L480`／`L957`／`L1173`／`L1210`）
   逐字指明 `SYSAD-ICSCLIENTSERVICE` **產生** `TGW_DISP_STAT` 與 `RQ_DISP_INTS`。
5. LID 表（§3-1，外部素材）對 `RQ_DISP_INTS` 之定義逐字為
   **`HU calculated display intensity for use by DCSD.`**

> **(4) + (5) 接合**：本 DUT 產生 `RQ_DISP_INTS`；`RQ_DISP_INTS` 的定義是「HU 算出、**供 DCSD 使用**」；
> 而本 DUT 自己的 SYSAD 說這個值是「由 DCSD MCU 執行」。
> **三份互相獨立之文件（DUT 之 SYSAD、專案 LID 表、CFTS020 §1.2 之變體定義）收於同一點：
> 本 DUT 的顯示面是一個外接的 DCSD。** 依 `4819134` 之逐字定義，此即 **Disassociated**。

**交辦所問之「SYSAD 分解表是否含 DCSD 元件」—— 實測答案：否。**
`Table 6 — System Decomposition Table` 之列為
`SYSAD-TLM`／`SYSAD-HMI`／`SYSAD-ICSAPP`／`SYSAD-ICSCLIENTSERVICE`／`SYSAD-AUDIOMANAGERSERVICE`／
`SYSAD-CPM`／`SYSAD-CARSERVICE`／`SYSAD-VHAL`／`SYSAD-VCPU`（報告 09 §3-3 已實測；本輪複驗
`DCSD` 於 SYSAD 僅 5 行且無一行位於該表 → **無 `SYSAD-DCSD` 列**）。

**此「否」不構成反證，反而與 Disassociated 一致**：System Decomposition Table 列的是
**本 DUT 內部之元件分解**；DCSD 依定義是**外接模組**（`External display module`，另一供應商），
本就不會出現在 DUT 自身的分解表中 —— 它出現在 `Definitions` 表的 **Domain 層**，
正是外部介面該在的位置。若 DUT 為 Associated（螢幕整合於 HU 模組內），
其 SYSAD 沒有任何理由定義一個外接的 `DCSD Domain`，更沒有理由把背光交給 `DCSD MCU`。

### §4-4 SYS2 —— 本 DUT 自身之系統需求分析（`All_HW_System_Accepted & Released`）

表頭自驗：欄0 `ID`、欄3 `Description`、欄7 `SYS2 來源需求項目ID  Source Requirement items`、
欄10 `SYS2 分類 Category`。資料列 **333**。

| 掃描 | 實數 |
|---|---|
| `Description` 含 `DCSD` 之列 | **131** |
| 其 `Category` 分佈 | `Out of Scope` 70、**`Functional Requirement` 23**、`Information` 21、`Heading` 14、`Out of scope` 3 |
| `Description` 含 `ICS` 之列（對照） | 85（`Out of Scope` 50、`Functional Requirement` 17、`Information` 14、`Heading` 4） |

**在案（非 Out of Scope）之 DCSD 需求逐字舉證**（`SYS2 子分類` 欄多為 `ICS / DCSD (CFTS020)`）：

| SYS2 ID | 來源 ObjectID | Category | 逐字（節錄） |
|---|---|---|---|
| `NRL-52853` | `4819622` | Information | `The DCSD and HU are connected via an LVDS interface with the ability to send screens rendered by the HU to the DCSD's display (HU_Video.Data) and with the ability for the DCSD to communicate status and Touch Screen information to the HU (using the LVDS 'Backchannel', DCSD_LVDSBCH.TCH_MSG). …` |
| `NRL-52854` | `4819623` | **Functional Requirement**（SW） | `The DCSD supplier and the HU supplier shall work together to develop a [DCSD_and_HU_LVDS_Backchannel_Protocol] … equivalent document …` |
| `NRL-52855` | `4819624` | **Functional Requirement**（SW） | `The DCSD supplier and the HU supplier shall work together to develop a [DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts] document …` |
| `NRL-52850` | `4819353` | **Functional Requirement**（System） | `If the $DCSD_DISP_STAT$ signal is received with an implausible value (values 5 or 6), the HU shall continue to behave using the last plausible value received. …` |
| **`NRL-52863`** | **`4820127`** | **Functional Requirement**（HW） | `SYS2 System-HW` 欄逐字：`HW supplier shall set the DTC for HU lost communication with DCSD with considering, $DCSD_DISP_STAT$== ON  Please refer to CAN mapping for Atl-Hi and Atl-Mid architecture in the Logical Identifiers and …` |
| `NRL-52868`～`NRL-52871` | `4820950`／`4820952`／`4820954`／`4820957` | **Functional Requirement**（System）×4 | `Multi-stage' DCSD Display Hot Algorithm` 一組，主詞為 `the HU`，客體為 `$DCSD_DISP_STAT$` |

**對照組（本 DUT 明文排除之項，逐字）**：`SYS2 MD Feedback` 欄含 `not LTM` 者共 **4 列**：

```
NRL-52860  src=4820123  Out of scope | [11/27/2025]: This DTC is for ICS module not LTM. Noted. This DTC is for ICS. Marking this as Out of scope
NRL-52861  src=4820124  Out of scope | [11/27/2025]: This DTC is for DCSD module not LTM. Noted. This DTC is for DCSD. Marking this as Out of scope
NRL-52862  src=4820126  Out of scope | [11/27/2025]: This DTC is for ICS module not LTM. Noted. This DTC is for ICS. Marking this as Out of scope
NRL-52864  src=4820128  Out of scope | [12/8/2025] … [11/27/2025]: This DTC is for DCSD module not LTM. Noted. This DTC is for DCSD. Marking this as Out of scope
```

**判讀（本項為主證之二）**：本 DUT 之專案團隊在 SYS2 中作了一組**極清楚的邊界劃分**：

- 「**DCSD 模組自己**的 DTC」→ **Out of scope**，理由逐字 `This DTC is for DCSD module not LTM`。
- 「**HU 與 DCSD 失去通訊**的 DTC」（`4820127`）→ **在案，Functional Requirement，HW**。

> 亦即：本 DUT 團隊承認「**本 DUT 是那個會與 DCSD 失去通訊的 HU**」，
> 同時明確表示「**DCSD 是另一個模組，不是本 DUT**」。
> 這兩件事同時成立的唯一解釋是：**本 DUT 是一台外接 DCSD 的 HU = Disassociated 變體。**
> 若本 DUT 為 Associated（螢幕整合於 HU 模組內、無外接 DCSD），
> 「HU 與 DCSD 失去通訊」之 DTC 對本 DUT 根本無從成立，不可能被列為在案之 HW 需求。

### §4-5 SWRA 之查無

`ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`（275 行）：
`DCSD`／`Silver Box`／`Associated`／`Disassociated`／`_ADspl`／`_DDspl` **全部 0 命中**。
**查無**，不作推定（SWRA 為軟體需求層，本就不描述硬體變體）。

---

## §5 量測項 5 —— 章節樹之旁證

**脫離 §1.8／§1.18：是**（本節僅用**標題語意**與**§1.8／§1.18 以外**各節之適用數；
禁區二節之數字只作對照陳列並標明不計入）。

### §5-1 CFTS020 頂層章節標題全表（逐字，實測 20 節）

```
§1     ICS and DCSD {4819125}
§1.1   Revision Notes {4819126}
§1.2   Introduction {4819128}
§1.3   Functional Requirements Common Between Architectures - DCSD HU {4819138}
§1.4   Diagnosis and Recovery Common Between Architectures - ICS, HU, DCSD, FPDM, CCDMF and CCDMR {4819140}
§1.5   Functional Requirements - PNet - ICS and Associated HU {4819356}
§1.6   Diagnosis and recovery - PNet - ICS and Associated HU {4819506}
§1.7   Function properties - PNet - ICS and Associated HU {4819529}
§1.8   Functional Requirements - PNet & AtlHi & AtlMi- ICS, Silver Box HU, DCSD, FPDM, CCDMF, and CCDMR {4819537}
§1.9   Diagnosis and recovery - PNet & AtlHi & AtlMi - ICS, Silver Box HU and DCSD {4820114}
§1.10  Function properties - PNet & AtlHi - ICS, Silver Box HU and DCSD {4820160}
§1.11  Functional Requirements - PNet & AtlHi - VP5R120 Silver Box HU and DCSD120_wICS_Port {4820168}
§1.12  Diagnosis and recovery - PNet & AtlHi - VP5R120 Silver Box HU and DCSD120_wICS_Port {4820340}
§1.13  Function properties - PNet & AtlHi - VP5R120 Silver Box HU and DCSD120_wICS_Port {4820374}
§1.14  Functional Requirements - CUSW - ICS and Associated HU {4820379}
§1.15  Functional Requirements - CUSW and Disassociated HU {4820454}
§1.16  Diagnosis and recovery - CUSW - ICS and Associated HU {4821650}
§1.17  Function properties - CUSW - ICS and Associated HU {4821669}
§1.18  Functional Requirements - AtlMi & AtlHi & AtlLo - ICS and Associated HU {4821673}
§1.19  Functional Requirements - AtlMi - DCSD {4821728}
```

**標題語意之結構**：全書以「(功能面) - (EE 架構) - (變體)」三段命名，
變體段只有兩個值：`ICS and Associated HU`／`Silver Box HU (and DCSD)`（= Disassociated），
外加 `CUSW and Disassociated HU`（§1.15）之直白寫法與 `DCSD HU`（§1.3）、`- DCSD`（§1.19）。
**`Silver Box` 與 `Disassociated` 為同義**（`4819134` 逐字：`… are also referenced as a 'Silver Box' variants`）。

### §5-2 分支配對檢定（**排除 §1.8／§1.18** —— 本檢定完全脫離禁區）

以標題所宣告之變體分支分組，逐節列 R-ICS2 v2(b) 之適用數：

| 分組 | 節 | 物件數 | **判適用** |
|---|---|---|---|
| **Associated** | §1.5 | 132 | **1** |
| | §1.6 | 13 | 0 |
| | §1.7 | 5 | 0 |
| | §1.14 | 64 | 0 |
| | §1.16 | 10 | 0 |
| | §1.17 | 1 | 0 |
| | **小計** | **225** | **1** |
| **Disassociated / Silver Box** | §1.3 | 1 | 0 |
| | **§1.9** | 32 | **17** |
| | §1.10 | 5 | 0 |
| | §1.11 | 144 | 0 |
| | §1.12 | 22 | 0 |
| | §1.13 | 2 | 0 |
| | **§1.15** | 1039 | **29** |
| | §1.19 | 1 | 0 |
| | **小計** | **1246** | **46** |
| 中性（Common／Intro） | §1.1／§1.2／§1.4 | 182 | 86 |
| **【循環·不計入】** | §1.8 | 490 | *92* |
| **【循環·不計入】** | §1.18 | 37 | *29* |

**Associated 分支之唯一適用物件（`4819365`，§1.5.1）之逐字與屬性**：

```
4819365  §1.5.1  Artifact Type = Description  ECU=None  Radio=['R1L-R','R1L']  EE=['All']
The Integrated Center Stack module (ICS) provides HMI information such as hard button presses and
hard knob rotations/presses to the HU, HVAC and to other Vehicle Components (the Body Controller
gateways the information to other Vehicle Components). This section discusses general hard button
and knob behavior …
```

依 **R-ICS2 v2(c)** 之明文（`1.5 之 132 物件中 130 為 PowerNet、餘二皆 Description 型章節引言
—— 故 1.5 之需求物件 100% 不適用`），此物件為 **`Description` 型章節引言，非需求物件**。

> **故 Associated 分支（排除 §1.18 後）之適用需求物件數 = 0；
> Disassociated 分支（排除 §1.8 後）之適用需求物件數 = 46。**

**§1.9 之 17 個適用物件（Disassociated 分支之診斷節）之逐字舉證**（4 例）：

```
4820152 §1.9.3.1  Radio=['R1L-R','R1H','R1M','R1L']  EE=['Atlantis Mid','PowerNet','Atlantis High']
  If the DCSD has received a plausible data value since exiting Sleep Mode and then the
  $RQ_DISP_INTS$ signal is received with an Implausible-Invalid value …

4820153 §1.9.3.1  Radio 含 R1L-R  EE 含 Atlantis High
  If the DCSD has received a plausible data value since exiting Sleep Mode and then the
  $TGW_DISP_STAT$ signal is received with an implausible value …

4820157 §1.9.3.2  Radio 含 R1L-R  EE 含 Atlantis High
  If the $DCSD_DISP_STAT$ signal is received with an implausible value (values 5 or 6),
  the HU shall continue to behave using the last plausible value received. …

4820147 §1.9.2.1  Radio 含 R1L-R  EE 含 Atlantis High
  The ICS module shall switch to standby mode upon loss of communication with the HU. …
```

**§1.15 之 29 個適用物件（`CUSW and Disassociated HU`）**：
EE 軸實測全部為 `('Atlantis High','Atlantis Mid','PowerNet')`（29／29，**不含 `CUSW`**），
Radio 軸全部含 `R1L-R`。逐字舉證：

```
4820950 §1.15.2.5.2  When the HU sees the transition from $DCSD_DISP_STAT$ <> [DISP_HOT] to
        $DCSD_DISP_STAT$ = [DISP_HOT] the HU shall display the 'Display Hot State' warning screen …
4821013 §1.15.3      The DCSD shall send the $DCSD_DISP_STAT$ signal to indicate the periodic and
        on-change status of the display. …
```

> **注意（誠實揭露）**：§1.15 之標題冠 `CUSW`，但其 29 個適用物件之 `EE Architecture` 軸
> **不含 `CUSW`**，而是 `Atlantis High/Mid + PowerNet`。此為**標題與逐物件屬性不符**之情形。
> 依 **R-ICS2 v2(c)**「章節分支為輔證，不得取代逐物件實測」，本報告以**逐物件實測**為準。
> 此不符本身另記於 §7-4（未預料之事）。

### §5-3 §1.15／§1.19 之標題語意與 §1.18 之關係

- **§1.15 `Functional Requirements - CUSW and Disassociated HU`**：全書唯一在標題直書
  `Disassociated HU` 之節。其 29 個適用物件全部與 `DCSD_DISP_STAT`／`RQ_DISP_INTS`／
  `TGW_DISP_STAT` 之 Display Hot 演算法有關，主詞為 `the HU` 與 `the DCSD`。
- **§1.19 `Functional Requirements - AtlMi - DCSD`**：僅 1 物件 `4821729`，
  `Radio=['noSys']`、`EE=['Atlantis Mid']`，判**不適用**。逐字：
  `The communication and wake-up strategy for non-CAN DCSD is defined and updated in the following
  documents: SD-HAD4.1.9.3 LVDS Output (1) – DCSD Support / PF-R15.14.20 LVDS Output (1) – DCSD Support`
  → 其 EE 為 `Atlantis Mid`，**不涵蓋本 DUT 之 `Atlantis High`**。
- **§1.18 之架構軸 `AtlMi & AtlHi & AtlLo`**：其標題所涵蓋之三個 EE 中，
  `AtlLo` 與 `AtlMi` 均非本 DUT。與之對稱的 Disassociated 側是
  §1.8 之 `PNet & AtlHi & AtlMi`。**本項不計入**（涉及 §1.18 之內容）。

### §5-4 答（量測項 5）

**分支配對檢定（脫離禁區）之結論：Associated 分支 0 個適用需求物件、
Disassociated／Silver Box 分支 46 個適用需求物件。指向 Disassociated，比數 46:0。**

---

## §6 量測項 6 —— A-ICS61 之併案判讀

A-ICS61 之二項實測事實（複驗成立）：
- §1.18 之 29 個適用物件，Radio 軸**全數經 `allSys` 命中**（明列 `R1L-R` 僅 1、`R1L` 僅 1）。
- §1.8.1 明列 `R1L-R` 者 **58** 個。

### §6-1 本項對本題是否構成證據：**否，且不計入**

**兩個獨立理由：**

**理由一（形式）：本項之二個數字全部取自 §1.8 與 §1.18 之內部。**
依交辦之禁循環令，二節之內容不得作為判定變體之證據。
本項**整項標為「循環，不計入」**。

**理由二（實質）：即便解除禁令，本項在 R-ICS2 v2 下亦無區辨力。**
R-ICS2 v2(b)(i) 明定 `Radio ∈ {R1L, R1L-R, allSys}` —— **`allSys` 與點名 `R1L-R` 判定完全等價**，
二者皆為「適用」，判準對二者不作強弱之分。
「概括 vs 點名」之差異原本要供 R-ICS35(c)「敘述較具體者」使用，
而 **R-ICS35(c) 已依 R-ICS36(b) 廢止**。故該差異在現行條文下**沒有任何條文可以承接**。

**理由三（反向檢驗，用以確認本項確實中性）**：
若「點名 `R1L-R` 集中於一側 ⇒ 該側為本 DUT 之變體」之推論成立，
則以同一推論套用於**脫離禁區**之各節，應得同向結果。實測：
§1.9 之 17 個適用物件中，Radio 軸明列 `R1L-R` 者 **17／17**（全數點名，無一經 `allSys`）；
§1.15 之 29 個適用物件中，Radio 軸明列 `R1L-R` 者 **29／29**。
即：**Disassociated 側之非禁區各節同樣是「全數點名」**。
這說明「點名 vs `allSys`」之差異是 **§1.18 一節獨有的書寫習慣**，
而非變體歸屬之標記 —— 用它推變體會把 §1.9／§1.15 一併判進 Disassociated 側，
與 §1.18 之判定方向相反卻由同一規則導出，**規則本身不自洽**。

### §6-2 A-ICS61 之處置建議（不作裁決，僅陳述）

A-ICS61 原文已自記「**本項為中性事實，不得單獨用以推定變體歸屬**」。
本輪量測**複驗該自記為正確**：它既不支持 Associated 亦不支持 Disassociated。
本報告不對 A-ICS61 作結案（依禁區令，不得對 A-／DR- 作結案）。

---

## §7 結論

# 【量測結論：`Disassociated`（'Silver Box'，外接 DCSD）】

**E7 未觸發**（未量得 `Associated`）。
**E8 未觸發**（未量得 `不可判`）。

一句話理由：**本 DUT 自己的系統架構文件（SYSAD）定義了一個外接的 `DCSD Domain`
並把背光交由 `DCSD MCU` 執行，本 DUT 自己的系統需求分析（SYS2）把「HU 與 DCSD 失去通訊」
列為在案之 HW 需求、同時把「DCSD 模組自己的 DTC」明文標為 `not LTM` 而排除
—— 這只有在本 DUT 是一台外接 DCSD 的 HU 時才能同時成立。**

### §7-1 支持證據逐項（含脫離標記）

| # | 證據 | 來源 | **脫離 §1.8／§1.18** | 強度 |
|---|---|---|---|---|
| S1 | SYSAD `定義 Definitions` 表：`DCSD Domain` = `External display module containing LCD, touch controller, MCU, and backlight control.`；並與 `HU Domain` 並列 | DUT 自身 SYSAD `L242`-`L243`、`L246`-`L247` | **脫離** | **主證** |
| S2 | SYSAD `定義` 表：`Backlight Control` = `Brightness control using RQ_DISP_INTS executed by display hardware (DCSD MCU control).` | DUT 自身 SYSAD `L238`-`L239` | **脫離** | **主證** |
| S3 | SYSAD 縮寫表：`DCSD` = `Disassociated Central Stack Display`（本 DUT 之文件收錄此縮寫） | DUT 自身 SYSAD `L146`-`L147` | **脫離** | 中 |
| S4 | LID 表 `RQ_DISP_INTS` 之 `Function` 逐字 = `HU calculated display intensity for use by DCSD.`，與 SYSAD 之「本 DUT 產生 `RQ_DISP_INTS`」接合 | `forms/…v1_78.xlsx` + SYSAD | **脫離** | **主證** |
| S5 | SYS2 `NRL-52863`（src `4820127`）為在案 `Functional Requirement`(HW)：`HW supplier shall set the DTC for HU lost communication with DCSD …` | DUT 自身 SYS2 | **脫離** | **主證** |
| S6 | SYS2 明文排除「DCSD 模組自己的 DTC」，逐字 `This DTC is for DCSD module not LTM`（2 列）；同批亦排除 ICS 模組之 DTC（2 列） | DUT 自身 SYS2 | **脫離** | **主證** |
| S7 | SYS2 在案之 DCSD 需求：`Description` 含 `DCSD` 之 131 列中 **23 列為 `Functional Requirement`**（子分類 `ICS / DCSD (CFTS020)`），含 LVDS Backchannel 協定、Display Hot 演算法四條 | DUT 自身 SYS2 | **脫離** | 強 |
| S8 | 分支配對檢定：Associated 分支（§1.5／1.6／1.7／1.14／1.16／1.17）適用需求物件 **0**；Disassociated 分支（§1.3／1.9／1.10／1.11／1.12／1.13／1.15／1.19）適用需求物件 **46** | CFTS020，**已排除 §1.8／§1.18** | **脫離** | 強 |
| S9 | LID 表中 `Arch Basis = AtlHi`（本 DUT 之 EE）之 DCSD LID **7 個**：`DCSD_Enter`／`DCSD_Power`／`DCSD_Screen_Off`／`DCSD_TUNEKNOB_DIR`／`DCSD_TUNEKNOB_VAL`／`DCSD_VOLKNOB_DIR`／`DCSD_VOLKNOB_VAL` | `forms/…v1_78.xlsx` | **脫離** | 中 |
| S10 | CFTS020 `4819135`（§1.2）逐字：`The 10.1 inch DCSDX which will be paired with the VP4R84, R1H, R1L radio HUs.` —— `R1L` 明列為與 DCSD 配對之 radio HU | CFTS020 §1.2 | **脫離** | 弱（未點名 `R1L-R`） |

**脫離統計：支持證據 10 項，10 項全部脫離 §1.8／§1.18，循環不計入者 0 項。**

### §7-2 反證之逐項處置（不略過任何不利證據）

**反-1：§1.10.1.1 之 Silver Box Configuration parameter 之 Radio 軸不含 `R1L-R`。**
實測：`4820164`／`4820165`／`4820166` 之 `Radio = ['VP5R120','VP4R84','VP484','R1M','R1H','VP384']`。
**處置**：此三物件是 `$DSP_SK_PRSNT$`（Screen Off softkey 有無）之**單一配置參數**行為，
其 Radio 軸列的是「會用到該配置參數的型號」，不是「Silver Box 變體的完整型號名冊」。
同節之 §1.10.1.1 首物件 `4820163` 為 `Radio=['noSys']`（已下架行為），
可見該節本身即是零星殘留。**不足以推翻 S1／S2／S5／S6，降為弱反證保留在案。**
（同型觀察：§1.11／§1.12／§1.13 皆為 `VP5R120` 專用之 Silver Box 節，本 DUT 亦全不適用 —— 這說明
「某個 Silver Box 節不適用」不等於「本 DUT 非 Silver Box」，只等於「本 DUT 非該型號」。）

**反-2：§1.18 標題為 `ICS and Associated HU`，且其 29 個物件依 R-ICS2 v2(b) 判適用。**
**處置**：本項為**禁區內容，依令不得計入判定**（`【循環·不計入】`）。
但其存在必須記錄：本結論（Disassociated）**若被外推為「§1.18 整批退出」，將與 §7-4(未預料-1) 之
實測相衝突**。本報告**不作該外推**，亦不對任何錨作處置（依禁區令）。

**反-3：DBC 中本 DUT（`LTM`）與 DCSD 無任何訊號關係（0 條）。**
**處置**：詳見 §3-4。同一檢定同時測出 `LTM` 與 `ICS` 亦為 0 條，
而本 DUT 與 ICS 有訊號關係是規格明載之事實 → **掃描面有已證實之盲區**
（ICS／DCSD 在 BHCAN、`LTM` 在 FDCAN8，二網之 `SGW` 閘道對映不在這二個 DBC 檔內）。
**本項證據值歸零（雙向皆不可推），不作為反證亦不作為正證。**

**反-4：SYSAD 之 `Table 6 System Decomposition Table` 不含 `SYSAD-DCSD` 列。**
**處置**：詳見 §4-3 末段。分解表列的是 DUT **內部**元件；DCSD 依定義為 `External display module`
（他供應商件），本就不在內部分解表中，而應在 `Definitions` 之 Domain 層 —— 實測正是如此。
**此「否」與 Disassociated 相容，不構成反證。**

**反-5：`_ADspl`／`_DDspl` 無法與 `R1L-R` 綁定（交辦預期之決定性證據落空）。**
**處置**：此為**查無**，不是反證。二後綴在 CFTS020 全文只出現於 §1.2 之 3 個 Introduction 物件、
且永遠成對並列（§1-3、§1-4）。**中性，不計入任一方。**

**反-6：SWRA、HMI Logic and Flow 全數 0 命中。**
**處置**：SWRA 為軟體需求層、`spec-index/sources/` 內之 HMI 件是 **Steering Wheel Controls**
（非 ICS／HU），二者本就不描述硬體變體。**查無，中性。**
ICS／HU 之 HMI Logic and Flow **不在 repo 內**（見 §4-1），此為素材缺口，另記於 §7-4。

**反-7：CFTS020 §1.2 之 `4819135` 未點名 `R1L-R` 與 DCSD 配對（只點名 `R1L`）。**
**處置**：S10 已自標為弱。`R1L` 與 `R1L-R` 是兩個獨立軸值，不得互推。
**降級為弱正向，不作主證。**

### §7-3 本結論之推翻條件（記於此以備複核）

本結論將被推翻，若出現以下任一項：
1. 本 DUT 之 SYSAD 或 SYS2 有**更新版**，其中 `DCSD Domain` 之定義被移除或改為內部整合螢幕；
2. 出現本 DUT 之硬體 BOM／PROXI 配置，證明本 DUT 之螢幕為模組內建（無外接 DCSD 件號）；
3. DR-ICS18 之上游答覆明文指本 DUT 為 Associated 變體。

### §7-4 未預料之事（必須向上呈報，本報告不作調和、不代擬條文）

**未預料-1（最重）：本 DUT 之 SYS2 同時把 §1.8 與 §1.18 之物件列為在案需求。**
SYS2 之 333 列以「來源 ObjectID」對映回 CFTS020，交叉表（實測）：

| 來源節 | SYS2 列數 | Category 分佈 |
|---|---|---|
| §1.8 | 89 | `Out of Scope` 43、**`Functional Requirement` 29+1**、`Information` 15、`Heading` 1 |
| §1.4 | 86 | `Information` 44、`Out of Scope` 41、`Functional Requirement` 1 |
| §1.15 | 29 | **`Functional Requirement` 16**、`Out of Scope` 13 |
| **§1.18** | **29** | `Out of Scope` 14、**`Functional Requirement` 8**、`Information` 7 |
| §1.9 | 20 | `Information` 8、`Out of Scope` 9、`Functional Requirement` 2、`Heading` 1 |
| §1.2 | 6 | `Information` 6 |
| §1.1 | 1 | `Information` 1 |
| （無法對映 CFTS020） | 73 | — |

§1.18 側之 8 個在案 `Functional Requirement` 逐字對應之 ObjectID：
`4821701`／`4821702`／`4821703`／`4821704`／`4821705`／`4821706`／`4821709`／`4821710`
（即報告 09 §3-1／§3-2 所列之 TLM 主詞物件），子分類皆為 `ICS / DCSD (CFTS020)`。

> **意涵**：本 DUT 之專案團隊在 SYS2 中**沒有**把 §1.18 整批排除；它把 §1.18 的 8 條
> 當作本 DUT 之在案功能需求接受了。
> 因此 **「量得 Disassociated ⇒ §1.18 之 29 個適用物件整批不適用」之外推，
> 與本 DUT 自身 SRA 之實測不符。**
> 本報告**不調和此不符**，亦**不對任何錨作處置**（R-ICS36(c)、禁區令）。
> 依 R-ICS35 v2(k)、R-ICS36(a)，本結論到達後 R-ICS35 自動進入重議 —— 此不符須於重議時一併處理。
> 本項**建議登為新異常**（編號待分析層給定，此處寫 `A-ICS?`）。
> 附註：SYS2 之各節列數與 R-ICS2 v2(b) 之適用數高度吻合（§1.15 = 29/29、§1.18 = 29/29、
> §1.4 = 86/86、§1.9 = 20 vs 17、§1.8 = 89 vs 92），
> 即 **SYS2 之「收錄哪些列」本身就是同一套適用性過濾之下游**，不具區辨力；
> 具區辨力的是**每列之 `Category`（人工範圍決定）**，而該欄的判讀正是上述不符之來源。

**未預料-2：§1.15 之標題冠 `CUSW`，其 29 個適用物件之 EE 軸卻不含 `CUSW`。**
實測：29／29 之 `EE Architecture = ('Atlantis High','Atlantis Mid','PowerNet')`。
依 R-ICS2 v2(c) 以逐物件實測為準，故判適用；但**標題與屬性之不符**本身是一個新事實
（與 R-ICS2 v2(c) 所舉之 §1.5 反例同型，但方向相反：那裡是標題正確、屬性落空；
這裡是標題誤導、屬性成立）。**建議登為新異常（`A-ICS?`）。**
本項對本結論之影響：§1.15 之 29 條是 S8 的一半來源，
即便將其全數剔除，S8 仍為 Associated 0 : Disassociated 17（§1.9），方向不變。

**未預料-3：交辦所設之二個「決定性／強證據」路徑均落空。**
- 「`_ADspl`／`_DDspl` 綁定 `R1L-R`」→ 綁定力為零（§1-4）。
- 「四個 Configuration parameters 節何者判適用」→ 四節全不適用（§2-2）。
- 「DBC 中 DCSD 與 DUT 之收發關係」→ 掃描面有盲區，雙向皆不可推（§3-4）。
- 「SYSAD 分解表是否含 DCSD 元件」→ 不含，但此「不含」與結論相容（§4-3、反-4）。
**本結論實際上是由交辦未特別指定之三項撐起的**：
SYSAD 之 `Definitions` 表（S1／S2）、SYS2 之 Category 邊界劃分（S5／S6）、
以及分支配對檢定（S8）。

**未預料-4：素材缺口 —— ICS／HU 之 `HMI Logic and Flow` 不在 repo 內。**
`spec-index/sources/` 僅有 Steering Wheel Controls 一件。
CFTS020 §1.18 多處外引之 `TLM HMI`／`HMI Logic and Flow`（報告 09 §3-1／§3-2 逐字）無從查證。
**此缺口不影響本結論**（本結論不依賴 HMI 件），但若日後需以 HMI 件複核，該件需另行索取。

**未預料-5：LID 表無法以 `VFs` 欄交叉驗證本 DUT。**
`DCSD_DISP_STAT`／`RQ_DISP_INTS` 之 `VFs = 650`、`TGW_DISP_STAT` 之 `VFs = 688/659/650`，
但 **repo 內查無本 DUT 之 Vehicle Family 編號**
（掃法：`features/ics_management/{framework.md,feature.yaml}`、
`docs/runtime/PROJECT_INSTRUCTION.md` 之 `VF\d{3}`／`Vehicle Family`／`HDCC27`／`DT27` 全文查無）。
故「本 DUT 之 VF 是否在 DCSD LID 之 `VFs` 清單中」**無法量測**。此為**查無**，不作推定。
若日後需以此路徑複核，需先取得本 DUT 之 VF 編號 —— **該資料不在 repo 內**。

### §7-5 本輪之已知局限（如實揭露）

1. **未使用 §1.8／§1.18 之任何內容作為判定依據**（依令）。此使本結論之樣本面縮小，
   但反過來說，本結論**不受該二節之歸屬爭議影響**，這正是禁循環令要達成的效果。
2. DBC 面之量測有已證實之盲區（§3-4），該面之結果一律歸零處理。
3. 本報告**未對任何錨、任何 TC JSON、任何 `specification_reference` 作任何更動**，
   亦未生成任何 TC、未對 DR-ICS13／DR-ICS18 作結案、未自取 `A-`／`DR-` 編號。
