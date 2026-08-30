# 下放包 12 作業 C —— CFTS022 外引反噬 ＋ 第三種變體表達

- **問題 C-1**：CFTS020 §1.8／§1.18 之取捨，會否透過 CFTS022 之 `{CFTS020}` 外引反噬回 CFTS022 側？七個現用錨是否間接受影響？
- **問題 C-2**：`CFTS022-4915246` 所示之第三種變體表達（CAN node 119 `ICS_R` 在否 ＋ `$Head_Unit_Screen_Size$`），代入本 DUT 後判為 Associated 抑或 Disassociated？與 R-ICS37(a) 一致或衝突？
- **腳本**：`features/ics_management/scripts/crossref_probe_12.py`（新建）
- **依令**：本輪**未執行任何 git 指令**（含唯讀之 `status`／`diff`／`log`／`show`）；
  未改任何 TC JSON、未動任何 `specification_reference`；未生成任何 TC；
  未寫入 `RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`／
  `ANALYSIS_LOCK.md`／`docs/handoff/**`／`feature.yaml`；
  未改 repo 根之 `scripts/`／`docs/runtime/`／`docs/fw036/`；
  未改 `features/ics_management/scripts/` 下任何既有檔（本輪僅新開 `crossref_probe_12.py`）。
- **只列不裁**：本報告不裁決、不代擬條文、不自取 `A-`／`DR-` 編號（需要時寫 `A-ICS?`）。

**自證未改檔（`shasum -a 256`，本輪結束時實測）**

```
7acfa462533d143c8099933e5b9e707f1c36aa3be95f5d8d0875b42a1f917fef  inputs/…CFTS_022…20260608-1205.docx
8696d1f596e3367754b092ff6d810cccff6258f46d6e90f8c0b30864314a30f3  inputs/…CFTS_020 ICS and DCSD …20260310-1533.docx
f18d66f7565239cae22f457fc6f67d66963931b4ce35b5d52bd61bd0f75c8494  RULINGS.md
9b9fc5b3e4b49d2419f91f66a7906e858c9aa467267aba1ecceea407955bc127  ANOMALIES.md
672a05d3cb0557b7663cf2af5fa4a4a5d5fbc8b136742c0cb49a1afe68b6d675  DATA_REQUESTS.md
ea6ed546d8a8aa19c5fa12469e30b7311bf5e31ca7c98c626a64ad7da210556a  feature.yaml
38de4ab913b1663e0a3819f23ef390ef4b1ca2c153057890f58733f6d19c1edf  framework.md
e6c820f5c31796d392551269ded99a256db4818dd40a3ea5c6645c594079ba12  ANALYSIS_LOCK.md
fa43557a5379cc38e754a11ff91490d2fdde511c1e2b1dd69a0380e103eae7bc  generated/b01/b01_tcs.json
090517f126d02beb6ecc68faa897427cea4e340118fe5302248570d334a1ff4f  generated/b06/b06_tcs.json
```

> 註：`RULINGS.md`／`ANOMALIES.md`／`generated/b01`／`generated/b06` 之 shasum 與報告 11
> 所載**不同**。本輪僅唯讀開檔，未寫入其中任一者（見 §4-1 之實質差異記錄）。

---

## §0 掃描條件

### §0-1 素材與抽取法

| 素材 | 抽取法 |
|---|---|
| CFTS022 `.docx` | 讀 `word/document.xml`；`</w:p>`→換行、`</w:tc>`→tab；`re.sub(r"<[^>]+>","")` 去標籤；`html.unescape`。實測 **1669 行／336 物件／82 章節行（去目次）** |
| CFTS020 `.docx` | 同上。實測 **5204 行／2180 物件／407 章節行（去目次）** |
| SYSAD `.docx` | 同上。實測 1410 行 |
| `.xlsx`（SYS2／LID／PROXI／SR26 Default Settings 等） | `openpyxl`，`read_only=True`、`data_only=True`；逐分頁逐列 |
| `.dbc` | **一律 `latin-1` 開檔**；訊息以 `^BO_ <id> <name>: <dlc> <sender>` 起，邊界由下一個 `BO_` 判定；`SG_` 行末空白後之逗號串為接收節點 |

- 章節行：`^(\d+(?:\.\d+)*) (.+?) \{(\d{7})\}$` 且該行不含 `PAGEREF`（目次行帶 `PAGEREF`）。
- 物件屬性頭：`^(\d{7}): \[`（對 `line.strip()`）；本文取**次一行**。
- 屬性：`\[([^:\]]+):([^\]]*)\]`，同 key 取首見。
- **行號慣例**：本報告之 `L<n>` 為 **1-based**，且指向**屬性頭那一行**。
  報告 11 之行號一律比本報告小 1（例：`4914956` 本報告 L181、報告 11 L180）。
  **此為慣例差，非素材差**（CFTS022 之 shasum 與報告 11 完全相同）。

### §0-2 NBSP 與雙空格之折疊（**本輪之關鍵前處理**）

去標籤後、切行前，下列字元一律換為一般空白（`U+0020`）：
`U+00A0`(NBSP)、`U+2002`、`U+2003`、`U+2005`、`U+2006`、`U+2007`、`U+2008`、
`U+2009`、`U+202F`、`U+205F`、`U+3000`；`U+200B`(ZWSP)、`U+FEFF` 直接刪除。

**另備一份「折疊連續空白」之比對面**：`re.sub(r"[ \t]+", " ", line)`。
**所有比對式一律施於折疊後之文字**，逐字引用則取未折疊之原行。
理由：二檔皆大量使用 NBSP，且上一輪實測存在**雙 NBSP**；不折疊會漏命中
（實例：`4915246` 之 `Note:  See …` 與 `4914993` 之 `softkey* has` 皆含雙空白）。

### §0-3 比對式與大小寫

**C-1 外引比對式**（五式，各自獨立計數後取聯集；全部 `re.I`）：

| 式名 | 正則 |
|---|---|
| `brace_plain` | `\{ ?CFTS ?0?20 ?\}` |
| `brace_id` | `\{ ?CFTS ?0?20 ?- ?\d{5,8} ?\}` |
| `bare` | `CFTS ?0?20`（裸寫，涵蓋前二式，為**最寬鬆側**） |
| `title_quoted` | `['‘’"“”] ?ICS and DCSD ?['‘’"“”]` |
| `title_bare` | `ICS and DCSD` |

式中之 ` ?` 即為對「NBSP／雙空白已折疊為單一空白」之容忍位。
`bare` 為最寬鬆側，故其命中數為外引之上界。

**C-2 比對式**（`re.I`）：`CAN ?node`、`ICS_R\b`、`ICS_R`（無詞界，更寬鬆）、
`Head_Unit_Screen_Size`、`Screen_Size`、`node ?119`、`node ?94`、`(?:is|are) present`。

### §0-4 計數單位

行面 = 命中行數；物件面 = 物件數。二者分列，不混用。

### §0-5 R-ICS2 v2 之判定實作

- CFTS022 用 **v2(a)**：`ECU ∩ {ICS, LTM} ≠ ∅` ∧ `Radio ∩ {R1L, R1L-R, allSys} ≠ ∅` ∧ `EE ∩ {Atlantis High, All} ≠ ∅`。
- CFTS020 用 **v2(b)**：`Radio ∩ {R1L, R1L-R, allSys} ≠ ∅` ∧ `EE ∩ {Atlantis High, All} ≠ ∅`；`ECU` 軸**存在時**須含 `{ICS, LTM}`，不存在時不視為不適用。
- 軸值比對：區分大小寫之精確字串集合交集，不作正規化、不作前綴比對。

---

## §1 C-1：CFTS022 之 `{CFTS020}` 外引反噬

### §1-1 逐式命中（行面，全文 1669 行）

| 式名 | 命中行數 |
|---|---|
| `brace_plain` | **3** |
| `brace_id` | **0** |
| `bare`（最寬鬆） | **4** |
| `title_quoted` | **1** |
| `title_bare` | **1** |
| **五式聯集** | **4** |

> **`{CFTS020-nnnnnnn}` 形式在 CFTS022 全文出現 0 次** ——
> 即 CFTS022 之外引**一律不指名 CFTS020 之 ObjectID，亦不指名章節號**。
> 此為本輪之首要實測事實，直接決定 §1-3 之判定形制。

**對照**：全文 `{…}` 引用 token（去 7 位數 ObjectID 後）之統計中，
`CFTS020` 出現 **3** 次（另 `CFTS019` 3、`CFTS024` 1、`CFTS026` 1、`CFTS22-1248` 2、
`VF230` 10、`VF665` 5、`VF169` 4、`VF668` 4、`VF650` 3、`VF664` 3…）。
`bare` 之第 4 個命中為 `4915278` 之無括號寫法 `according HMI and CFTS020`。

### §1-2 外引點全清單（物件面，**4 個**）

| # | ObjectID | 行 | 章節 | `Artifact Type` | v2(a) 對本 DUT |
|---|---|---|---|---|---|
| 1 | `4915097` | L436 | §2.11 Screen On/Off | SFR | **適用** |
| 2 | `4915099` | L439 | §2.12 Front Passenger Display Screen On/Off | SFR | **不適用** |
| 3 | `4915151` | L1171 | §3 Personalization Features | SFR | **適用** |
| 4 | `4915278` | L1550 | §3.2.13 Show Time in Screen Off | SFR | **不適用** |

**章節標題行本身之外引：0**。**未歸入任何物件本文之命中行（表格列／目次列）：0**。
即 4 個命中**全部**落在物件本文，無散行。

---

#### 外引點 1 —— `4915097`（§2.11 Screen On/Off）

- `ECU:ETM, LTM`／`Radio:VP2R7, CTS1_2, VP465, R1L-R, VP3, VP484, VP4R84, VP2.5, R1H, VP4R7, VP2R5, VP384, High, VP365, R1L, R1M, VP2, VP2R84, VP4`／`EE Architecture:Atlantis Mid, PowerNet, Atlantis High, CUSW`
- v2(a)：`ECU ∋ LTM` ✅／`Radio ∋ R1L, R1L-R` ✅／`EE ∋ Atlantis High` ✅ ⟹ **適用**

逐字：
> `The Screen On/Off hardkey or softkey shall be used to request the HU to turn the HU Screen image On and Off. Note:  See {CFTS020} for Screen On/Off behavior.`

- 所指之 CFTS020 章節：**未明示**（無章節號、無 ObjectID）。

#### 外引點 2 —— `4915099`（§2.12 Front Passenger Display Screen On/Off）

- `ECU:FPDM, ETM`／`Radio:R1H`／`EE Architecture:Atlantis High`
- v2(a)：`ECU ∩ {ICS, LTM} = ∅` ✗ 且 `Radio ∩ {R1L, R1L-R, allSys} = ∅` ✗ ⟹ **不適用**

逐字：
> `The Screen On/Off hardkey or softkey shall be used to request the Front Passenger Display to turn the Front Passenger Display Screen image On and Off. Note:  See {CFTS020} for Screen On/Off behavior.`

- 所指之 CFTS020 章節：**未明示**。

#### 外引點 3 —— `4915151`（§3 Personalization Features 首個物件）

- `ECU:ETM, LTM`／`Radio:`（20 值，含 `R1L`、`R1L-R`）／`EE Architecture:All`
- v2(a)：**適用**

逐字：
> `The HU shall send the touch coordinates as specified in Chapter {CFTS020} 'ICS and DCSD'.`

- 所指之 CFTS020 章節：**未明示**（僅指整章 `Chapter {CFTS020}`）。
- 註：此物件同時命中 `brace_plain`、`bare`、`title_quoted`、`title_bare` 四式。

#### 外引點 4 —— `4915278`（§3.2.13 Show Time in Screen Off）

- `ECU:LTM`／`Radio:R1L-R, R1L`／`EE Architecture:Atlantis Mid`
- v2(a)：`ECU ∋ LTM` ✅／`Radio ∋ R1L, R1L-R` ✅／`EE ∩ {Atlantis High, All} = ∅` ✗ ⟹ **不適用**

逐字：
> `If the setting is disable, in screen off mode the screen shall be off according HMI and CFTS020. See [*Default Settings and PNet ECU Configuration*] document for default values.`

- 所指之 CFTS020 章節：**未明示**（且為裸寫，無大括號）。

### §1-3 落在 CFTS020 §1.8 或 §1.18 者之數

**須先分辨兩種問法，其答案不同：**

#### (i) **明示落點**：**0 / 4**

四個外引**無一**寫出 CFTS020 之章節號或 ObjectID（§1-1 已測得 `brace_id` = 0）。
**依明示落點判，落在 §1.8 或 §1.18 者為 0。此為確定之查無。**

#### (ii) **依行為主題可對映之落點**：**3 / 4**（其中 2 個**同時**落 §1.8 與 §1.18）

對映法（逐項揭露）：取外引句所指之行為關鍵詞，於 CFTS020 全 2180 物件之本文
作 `re.I` 折疊後比對，再以節號歸屬與 v2(b) 判定分佈。

| 外引點 | 行為關鍵詞 | 落 §1.8 子樹（v2(b) 適用數） | 落 §1.18 子樹（v2(b) 適用數） | 判 |
|---|---|---|---|---|
| `4915097`（§2.11） | `screen (on\|off)` | **有**（23） | **有**（3：`4821705`／`4821706`／`4821707`，皆 §1.18.1.2） | **二節皆落** |
| `4915099`（§2.12） | 同上 | 有（23） | 有（3） | 二節皆落（惟物件本身不適用） |
| `4915151`（§3） | `touch ?coordinate` | **有**（7） | **無（0）** | **只落 §1.8** |
| `4915278`（§3.2.13） | `screen off`（未指行為細目） | 有 | 有 | 無法收斂（惟物件本身不適用） |

**§1.18.1.2 之三個 Screen On/Off 物件逐字**（皆 `Radio:allSys`／`EE:Atlantis High, Atlantis Mid`，v2(b) 判**適用**）：

> `4821705`：`IF TLM is in "Screen Off" modality AND it receives $ICSScreenOffButton$ passing from "Not_Pressed" to "Pressed", TLM has to set Screen On internal modality.`
> `4821706`：`IF TLM is in "Screen On" modality AND it receives $ICSScreenOffButton$ passing from "Not_Pressed" to "Pressed", TLM has to set Screen Off internal modality.`
> `4821707`：`See TLM HMI for details on Screen On and Screen Off modalities.`

**§1.8 側之對應（節錄 3 條，v2(b) 判適用）**：

> `4819571`（§1.8.1.1.3）：`When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority.`
> `4819576`（§1.8.1.1.3）：`When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS SCREEN OFF hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DIS…`
> `4819637`（§1.8.2.1.2）：`While the HU is in the 'HU Screen ON' state it shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]).`

**touch coordinates 之落點**（`4915151` 所指）：
§1.8 子樹 v2(b) 適用者 **7** 個（`4819657`、`4819659`、`4819679`、`4819879`、
`4819889`、`4819897`、`4819905`）；**§1.18 子樹 0 個**（全 37 物件中無一含 `touch coordinate`）。

> **本項之意涵（陳述，不裁）**：`4915151` 之外引若真要落地，
> 其唯一落點在 §1.8 —— §1.18 沒有可承接之物件。
> 而 `4915097` 之外引則二節皆有可承接之物件。
> **即：§1.8／§1.18 之取捨確實會改變「§2.11 之外引指向何處」，
> 但不會改變「§3 之外引指向何處」。**

### §1-4 七個現用錨之間接影響檢定

#### §1-4-0 錨之自行複驗（唯讀；**與下放包所述不符，如實記錄**）

自 `generated/b01`～`generated/b07` 全部七個 `*_tcs.json` 逐條讀出
`specification_reference`（該欄為換行分隔之字串，本輪以 `\n` 切分後比對），
**篩出全部 token 皆以 `CFTS022-` 起首者**：

| batch | `tc_title` | `specification_reference`（實測逐字） |
|---|---|---|
| b01 | Stuck button held over 120 s | `CFTS022-4914956` |
| b01 | Stuck fault held until de-bounced not-pressed | `CFTS022-4914957` ⏎ `CFTS022-4914958` |
| b01 | Button held exactly 120 s | `CFTS022-4914956` |
| b01 | VOLUME knob rotated clock-wise | `CFTS022-4914974` ⏎ `CFTS022-4914975` |
| b01 | VOLUME knob rotated counter clock-wise | `CFTS022-4914974` ⏎ `CFTS022-4914976` |

**實測：純 CFTS022 錨之 TC 現為 5 條，相異 ObjectID 6 個**
（`4914956`／`4914957`／`4914958`／`4914974`／`4914975`／`4914976`）。

**`4914993` 現已非純 CFTS022 錨。** b06 之二條 Mute TC 實測逐字為：

```
CFTS020-4821709
CFTS022-4914993
```

即 b06-01／b06-02 已加錨 `CFTS020-4821709`（**位於 §1.18.1.2**）。
報告 11 §3-0 所載之「b06 二條為純 CFTS022 錨」在本輪已**不再成立**。
本報告**不裁定**此變更之依據與正當性（形制上與 `R-ICS40(d)` 之加錨令相符），
僅如實記錄並據以重算。詳見 §4-1。

**下列檢定對「報告 11 之七個 ObjectID」全數執行**（含 `4914993`），
以維持與下放包交辦面之可比性。

#### §1-4-1 節層：七錨所在章節內之全部物件與其外引狀態

| 錨 | 所在節 | 該節（含子節）物件數 | 其中帶 `{CFTS020}` 外引者 |
|---|---|---|---|
| `4914956`／`4914957`／`4914958` | §1.5 Stuck Button Behavior `{4914953}` | **5** | **0** |
| `4914974`／`4914975`／`4914976` | §2.2 Volume `{4914970}`（含 §2.2.1～§2.2.5） | **28** | **0** |
| `4914993` | §2.2.2 Entertainment Audio Mute/Unmute `{4914991}` | **2** | **0** |

**§1.5 之 5 物件**（逐一，無一帶外引）：`4914954`、`4914955`、`4914956`*、`4914957`*、`4914958`*
**§2.2 子樹之 28 物件**（無一帶外引）：`4914971`～`4914987`（§2.2）、
`4914989`／`4914990`（§2.2.1）、`4914992`／`4914993`*（§2.2.2）、
`4914995`～`4914997`（§2.2.3）、`4914999`／`4915000`（§2.2.4）、`4915002`／`4915003`（§2.2.5）。

**七錨本文自身之外引複驗：7/7 皆無外引**（與報告 11 §7-1 之複核一致）。

#### §1-4-2 章層：外引之章分佈

| 章 | 帶外引之物件數 |
|---|---|
| 第 1 章 Functional Specification | **0** |
| 第 2 章 HU General Functions | **2**（`4915097` §2.11、`4915099` §2.12） |
| 第 3 章 Personalization Features | **2**（`4915151` §3、`4915278` §3.2.13） |

- `4914956`／`4914957`／`4914958` 位於**第 1 章**——該章外引數 **0**，
  **節層與章層皆無外引，二重查無。**
- `4914974`／`4914975`／`4914976`／`4914993` 位於**第 2 章**——
  節層（§2.2 子樹）外引 **0**，但**章層有 2 個外引**（§2.11／§2.12）。
  下列為對這一路徑之實測檢定。

#### §1-4-3 章層路徑之逐項檢定：§2.11 之外引會否改變四個 §2.2 錨之解讀？

**檢定 1 —— 行為主詞是否重疊**（實測，非推論）

| 錨 | 本文逐字（節錄） | 行為主詞／客體 |
|---|---|---|
| `4914974` | `The HU shall show the 'VOLUME POP_UP' to indicate the current volume level.` | HU／VOLUME POP_UP |
| `4914975` | `When the VOLUME knob is active and the knob is rotated clock-wise, the HU shall increment the current audio level up by one for each detent position.` | HU／audio level |
| `4914976` | `… rotated counter clock-wise, the HU shall decrement …` | HU／audio level |
| `4914993` | `When the HU detects that the Mute hardkey or softkey* has been pressed the HU shall toggle the mute/unmute state of the Entertainment Audio Source.* Note:  The Mute softkey applies only if the HMI calls for such a softkey.` | HU／mute state |
| `4915097`（外引點） | `The Screen On/Off hardkey or softkey shall be used to request the HU to turn the HU Screen image On and Off.` | Screen On/Off hardkey／**HU Screen image** |

外引所外包之行為 = **「Screen On/Off hardkey 對螢幕影像之開關」**。
四個錨之行為 = **音量增減／靜音切換／音量彈出視窗顯示**。
**客體不重疊**（螢幕影像開關 vs 音量／靜音狀態）。

**檢定 2 —— §1.5／§2.2 子樹之本文是否提及 screen／display／DCSD**（實測）

§1.5 子樹：**0 命中**。
§2.2 子樹：**9 命中**，逐一列示並判其是否為錨：

| ObjectID | 是否為錨 | 本文（節錄） |
|---|---|---|
| `4914982` | 否 | `If Volume Adjustments are allowed, the HU shall continue to display the Volume Level indicator.` |
| `4914989` | 否 | `… automatically exit the Volume Level screen and return to the mode the HU was at prior …` |
| `4914995`／`4914996`／`4914997` | 否 | Front Passenger Display 側（§2.2.3） |
| `4914999`／`4915000` | 否 | Front Passenger Display 側（§2.2.4） |
| `4915002`／`4915003` | 否 | `'Status Bar Volume Popup'`／`'Extended Volume Popup'`（§2.2.5，`Radio:R1H`／`EE:Atlantis High`，v2(a) 不適用） |

**七個錨無一在此 9 命中之列。** 錨 `4914974` 之 `'VOLUME POP_UP'` 未含
`screen`／`display`／`DCSD` 三詞之任一。

**檢定 3 —— `'VOLUME POP_UP'` 是否在 CFTS020 側被 §1.8／§1.18 之取捨牽動**（實測）

- CFTS020 全文 `VOLUME POP`（`re.I`、折疊後）：**0 命中**。
- CFTS020 全文 `pop_?up`（`re.I`）：**40 命中行**。其節分佈之 §1.8／§1.18 面：

| 節 | popup 物件數 | 其中 v2(b) 判**適用**者 |
|---|---|---|
| §1.8 子樹 | **10** | **0** |
| §1.18 子樹 | **0** | **0** |

§1.8 之 10 個 popup 物件（`4819686`～`4819693`、`4820035`、`4820084`、`4820087`、`4820101`）
逐一以 v2(b) 判定，**適用數 0**（其 `Radio`／`EE` 皆不含本 DUT 之組合）。
**故：無論 §1.8／§1.18 如何取捨，CFTS020 側都沒有任何對本 DUT 適用之 popup 物件
可用以改變 `4914974` 之解讀。**

#### §1-4-4 §1-4 之判定

> ## **七個錨（含已轉為混錨之 `4914993`）皆未受 `{CFTS020}` 外引之間接影響。**

判準與實測依據逐項：

1. **節層**：七錨所在之 §1.5（5 物件）、§2.2 子樹（28 物件）、§2.2.2（2 物件）
   **共 33 個物件中，帶 `{CFTS020}` 外引者 0 個**。
   交辦所設之路徑（「同節其他物件帶外引 → 該外引所指行為改變七錨解讀」）
   **前提即不成立**：同節根本無外引物件。
2. **章層**：第 1 章外引 0（三個 stuck button 錨二重查無）。
   第 2 章雖有 2 個外引（§2.11／§2.12），但其外包之行為（Screen On/Off hardkey
   對螢幕影像之開關）與四個 §2.2 錨之行為（音量／靜音）**客體不重疊**（檢定 1），
   且錨本文無 screen／display／DCSD 之任何字面（檢定 2），
   且 CFTS020 側之 popup 物件對本 DUT **v2(b) 適用數為 0**（檢定 3）。
3. **外引形制**：四個外引**全部未指名章節號或 ObjectID**（§1-1、§1-3(i)），
   故不存在「外引直接把某一節之取捨釘進 CFTS022」之機制。
4. **屬性面**：七錨之 v2(a) 三軸判定完全由 CFTS022 自身之屬性決定，
   `{CFTS020}` 不在任一軸之值域內；§1.8／§1.18 之取捨代入後**無處可代**。

**惟須明白登記兩項限縮（不調和、不自行擴張結論）：**

- **限縮 A**：§1-3(ii) 已測得 §2.11 之外引在 §1.8 與 §1.18 **二節皆有可承接之物件**，
  §3 之外引則**只有 §1.8 可承接**。**即「§1.8／§1.18 之取捨確會改變 CFTS022 側
  某些外引的落地位置」——只是被改變者是 `4915097`／`4915151`／`4915099`／`4915278`，
  **不是七個錨**。A-ICS73 所問之「反噬是否存在」，答案是**存在但不及於七錨**。
- **限縮 B**：`4914993` 之 b06 二條 TC 現已**直接**錨 `CFTS020-4821709`（§1.18.1.2），
  故其對 §1.18 之依存**不再是「間接經外引」而是「直接經錨」**。
  該依存不在 E16 之定義面（E16 限「外引影響」），但**在事實面已存在**。
  此為 §4-1 之呈報事項，**本報告不裁其效果**。

---

## §2 C-2：第三種變體表達

### §2-1 該表達於文件族中之全部出現

**掃描面**：CFTS022（1669 行／336 物件）＋ CFTS020（5204 行／2180 物件），
折疊後 `re.I`。

| 詞 | CFTS022 命中行數 | CFTS020 命中行數 |
|---|---|---|
| `CAN ?node` | **1** | **0** |
| `ICS_R\b`（詞界） | **1** | **0** |
| `ICS_R`（無詞界，更寬鬆） | **1** | **0** |
| `node ?119` | **1** | **0** |
| `node ?94` | **1** | **0** |
| `Head_Unit_Screen_Size` | **1** | **1** |
| `Screen_Size` | **1** | **1** |
| `(?:is\|are) present`（對照） | 7 | 37 |

**全文出現之 CAN node 編號**：CFTS022 = `{94: 1, 119: 1}`；CFTS020 = **無**。

**`$…$` token 中含 `Screen` 者（實測全列）**：

| CFTS022 | 次數 |
|---|---|
| `$Touchscreen_ICS$` | 3 |
| `$Rear_Screens_Present$` | 2 |
| `$Head_Unit_Screen_Size$` | **1** |

| CFTS020 | 次數 |
|---|---|
| `$DCSD_Screen_Off$` | 29 |
| `$ICSScreenOffButton$` | 26 |
| `$Screen_Open_Close$` | 3 |
| `$Head_Unit_Screen_Size$` | **1** |

#### §2-1-1 出現點逐字（**文件族中共 2 個物件，其中「CAN node + ICS_R」組合僅 1 個**）

**出現點 1 —— `CFTS022-4915246`**（L1490，§3.2.9 Manual Display Intensity for CCDM both Front and Rear）

- `Artifact Type:Subsystem Functional Requirement`／`State:Approved`／`Market:All`／`Model Year:Default`
- **`ECU:CCDMR, ETM, CCDMF`**／**`Radio:R1H`**／**`EE Architecture:Atlantis High`**

逐字：
> `The HU shall send the desired display intensity to the front and rear CCDM and to DCSD modules using the $CCDMF_RQ_DISP_INTS$ signal when (CAN node 94 (CCDMF) OR CAN node 119 (ICS_R) are present) OR ($Head_Unit_Screen_Size$ = [10]). See {VF668} for other requirements.`

- **v2(a) 判定**：`ECU ∩ {ICS, LTM} = ∅` ✗（`CCDMR`／`ETM`／`CCDMF` 皆非）
  且 `Radio ∩ {R1L, R1L-R, allSys} = ∅` ✗（僅 `R1H`）⟹ **對本 DUT 不適用**（二軸皆落空）。

**出現點 2 —— `CFTS020-4819139`**（L417，§1.3 Functional Requirements Common Between Architectures - **DCSD HU**）

- `ECU:` **軸不存在**／`Radio:R1M, R1H`／`EE Architecture:All`／`Market:All`

逐字：
> `The HU shall use the $Head_Unit_Screen_Size$ parameter to determine the size of the display.`

- **v2(b) 判定**：`Radio ∩ {R1L, R1L-R, allSys} = ∅` ✗（僅 `R1M`、`R1H`）⟹ **對本 DUT 不適用**。
- 註：其所在節之標題逐字為 `Functional Requirements Common Between Architectures - **DCSD HU**`
  —— 即 `$Head_Unit_Screen_Size$` 之使用主體被文件明載為 **DCSD HU**。

**除此二處外，`CAN node`／`ICS_R`／`Head_Unit_Screen_Size` 於二檔查無其他出現。**

### §2-2 表達方式之語意實測（外部素材；本項為 b10 未走過之路徑）

#### §2-2-1 `CAN node 119 (ICS_R)` 之實體所指

**`forms/PROXI_HDCC27_R3_20250424.xlsx` 分頁 `Format`（PROXI STANDARD FORMAT - 29 BIT）逐字**：

| 列 | `Parameter Name` | `Annotation` | `Table` | `Used by NODE(VFXXX)` | `Rule Reason` |
|---|---|---|---|---|---|
| R100 | `CAN node 94 (CCDMF)` | `CAN Node ID 143` | `0 = Absent` / `1 = Present` | `ECC (VF727_V6); VRM (VF727_V6); ETM (VF169_V3, VF664_V3, VF727_V6); TBM (VF684_V3);` | `0 = Set to` / `1 = Never` |
| R125 | **`CAN node 119 (ICS_R/CCDMR)`** | `CAN Node ID 119` | `0 = Absent` / `1 = Present` | `ECC (VF066_V1, VF727_V3, VF727_V6); ETM (VF664_V3, VF727_V3, VF727_V6); VRM (VF727_V3, VF727_V6); TBM (VF684_V3);` | **`0 = Set to`** / **`1 = Never`** |
| R253 | `EOL node 119 (ICS_R/CCDMR)` | `CAN Node ID 119` | `0 = Hasn't EOL` / `1 = Has EOL` | `BCM (VF603_V1);` | `0 = Set to` / `1 = Never` |

> **關鍵逐字**：`ICS_R` 在 PROXI 中之全名為 **`ICS_R/CCDMR`**
> —— 即「後排 ICS／後排 Cabin Climate Display Module」，
> 與 node 94 `CCDMF`（前排 CCDM）成前後排對。
> **`Used by NODE` 欄列 `ETM`，未列 `LTM`。**

**`forms/Logical Identifiers and CAN Mapping v1_78.xlsx` 分頁 `CAN Mapping`**：
含 `ICS_R` 之資料列 **17** 列。其中 `ICS_R_*` 型 LID（`ICS_R_L_BlowerDown`、
`ICS_R_L_BlowerUp`、`ICS_R_L_TempDown`、`ICS_R_L_TempUp`、`Rear_ICS_HVACPowerCntrl`）
之欄位逐字：

```
Function     : Rear Left Blower Down pressed  ／ Rear HVAC power control mode request
Arch Basis   : PNet
Transfer Fn  : Powernet = CUSW= NA(Atlantis)
Signal Name  : ICS_R1.ICS_R_L_BlowerDown   CAN: CAN-B   VFs: 727
Usage Comment: N/A for Atlantis High
```

> **關鍵逐字二處**：`Powernet = CUSW= NA(Atlantis)` 與 **`N/A for Atlantis High`**。
> 即 `ICS_R` 為**後排 HVAC 控制面板**，其 LID 於 **Atlantis High 架構明載 N/A**。

#### §2-2-2 `$Head_Unit_Screen_Size$` 之定義域

**LID 分頁 `Proxi & Configuration` R95 逐字**：

```
Logical Identifier : Head_Unit_Screen_Size
Object Text        : <Head Unit Screen Size >
Arch Basis         : Atlantis
Signal Name        : EcuCfg16.EC_AudTel3B.<Head Unit Screen Size >    CAN: CAN-B
Table              : 0 = Absent
                     1 = Reserved
                     2 = Reserved
                     3 = R1_12.3 1920x720
                     4 = R1_10.25 1920x720
                     5 = R1_8.4" 1024x768
                     6 = R1_10.1" 1920x1200
                     7 = R1_12" 1920x1200
                     8 = R1 12" 1200x1920
                     9 = R1 12" 800x1280
                     10 = R1 10.1" 1200x1920
                     11 = R1 14.4" 1024x1920
                     12 = R1 12.3" 1920x720
                     13/14/15 = Reserved
Sales Code         : Radio_Display_Type
```

（`forms/SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` 分頁
`PNET ECU Master Configurations` R73 載同一枚舉，`Parameter` = `EC_AudTel3B`，
`Primary CFTS Usage` = `CFTS033, CFTS020`。二源枚舉逐項一致。）

> **本輪最重要之語意更正**：`$Head_Unit_Screen_Size$ = [10]`
> **不是「10 吋」**，而是**枚舉值 10 = `R1 10.1" 1200x1920`**。
> 該參數是 **HU 螢幕之尺寸／解析度枚舉**（`0 = Absent`），
> **不是「有無外接螢幕件」之旗標**。

### §2-3 代入本 DUT 之判定

本 DUT：`newR1L`／`R1L-R`，`EE Architecture = Atlantis High`，`ECU = LTM`（A-ICS47）。

#### §2-3-1 逐運算元代入

| 運算元 | 代入結果 | 依據（實測） |
|---|---|---|
| 物件 `4915246` 本身之適用性 | **不適用** | `ECU:CCDMR, ETM, CCDMF` 無 ICS/LTM；`Radio:R1H` 無 R1L/R1L-R。R-ICS2 v2(a) 二軸皆落空 |
| `CAN node 119 (ICS_R)` 在否 | **不在**（Absent） | LID：`ICS_R_*` 之 `Usage Comment` 逐字 `N/A for Atlantis High`、`Transfer Fn` 逐字 `Powernet = CUSW= NA(Atlantis)`、`Arch Basis = PNet`。PROXI R125 之 `Rule Reason` 逐字 `0 = Set to / 1 = Never`（該表下恆為 Absent） |
| `CAN node 94 (CCDMF)` 在否 | **不在**（Absent） | PROXI R100 `Rule Reason` 逐字 `0 = Set to / 1 = Never` |
| `$Head_Unit_Screen_Size$` 之值 | **查無** | 無本 DUT 專屬之 PROXI 表。`forms/PROXI_HDCC27_R3_20250424.xlsx` 之 `Cover` 逐字為 `27MY HDCC SPECIFIC PROXI TABLE`，**非本 DUT 車型**；其中亦無 `Head_Unit_Screen_Size` 之列（僅 `Rev History` 提及）。SYSAD 全 1410 行掃 `screen ?size`／`Head_Unit_Screen`／`inch`／`CCDM`：**0 命中**。SYS2 掃同組詞：`Screen_Size` 0 命中 |
| DBC 佐證 | `ICS_R` 於四個 DBC 全部 **0 次**；`Screen_Size` 全部 **0 次** | `forms/PDT27_E2A_R1_BHCAN2.dbc`（`BU_:` = `ETM FPDM LTM SGW`）、`forms/PDT27_E2A_R1_FDCAN8.dbc`（`ETM LTM SGW TBM`）、`vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`（17 節點，含 `DCSD`／`ICS`）、`vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc`（`ETM LTM SGW TBM`）。**四檔之 `BU_:` 皆無 `ICS_R` 節點** |

**小結（機械代入）**：`(node 94 present OR node 119 present) OR (Head_Unit_Screen_Size = [10])`
之三個運算元，前二者**判為 Absent**，第三者**查無值**。
**故本表達式在本 DUT 上不成立或不可判 —— 其本身不產生「Associated」之任何指示。**

#### §2-3-2 語意鏈之續查（**本項為本 DUT 自身文件之正向證據**）

`$Head_Unit_Screen_Size$` 之枚舉 `10 = R1 10.1" 1200x1920` 引出一條可續查之鏈。
本 DUT 自身之 SYS2（`SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`，
分頁 `Basic Report` R10）之在案項 **`NRL-52847`**（`SYS-RA-DM-009`；
`col7` 之 trace 對象逐字為 CFTS020 物件 **`4819135`**；`col79` = `SYS2_System Requirements Analysis`）
本文逐字（節錄，`_x000D_` 為原檔之換行編碼）：

> `Note: There are many DCSD variants that pair with the **disassociated** variants of the HUs.  The key characteristics of the DCSDs that differentiate the variants are:`
> `1) Diagonal Screen Size in inches.  Between the associated HUs and the DCSDs we have screens of various diagonal sizes (currently 5.0, 6.5, 7.0, 8.4, 10.1, 12.0 and 12.1).  It is useful to reference specific variants of the HUs and DCSDs using the screen size and so we will include the screen diagonal dimension (without including the decimal point) as part of the Component acronym.  This will correlate to the System attribute where we have included the screen size as a suffix on some System attribute values.  For the DCSDs we currently have screen sizes of 7.0, 8.4, 10.1, 12.0 and 12.1 inches.`
> `…`
> `b) The **10.1 inch DCSDX which will be paired with the VP4R84, R1H, R1L radio HUs.**`
> `…`
> `2) ICS Knobs and buttons integrated into the DCSD or not integrated. …`
> `a) DCSD120_wICS_Port which will be paired with the VP5R120 and R1H radio HU.`
> `b) DCSD70_wICS_NonCAN which will be paired with the R1 radio HU.`
> `4) … a) DCSD84_NoMTouch which will be paired with the VP384, VP484 and VP4R84 radio HUs.`

**鏈之三節（逐一標明實測來源）**：

1. `$Head_Unit_Screen_Size$` 枚舉值 `[10]` = `R1 10.1" 1200x1920`（LID `Proxi & Configuration` R95）。
2. 10.1 吋之螢幕件，SYS2 `NRL-52847` 逐字載為 **`The 10.1 inch DCSDX which will be paired with the VP4R84, R1H, R1L radio HUs`** —— 即 10.1 吋螢幕於本文件族中是**一個 DCSD（DCSDX）**，且其配對之 radio HU **明列 `R1L`**。
3. 同一段之首句逐字：**`There are many DCSD variants that pair with the disassociated variants of the HUs`** —— 即 **DCSD 配對之 HU 側為 disassociated 變體**。

> **故：若 `$Head_Unit_Screen_Size$ = [10]` 成立，其語意鏈指向之螢幕件是 DCSDX，
> 而 DCSD 之配對側依本 DUT 自身 SYS2 之逐字為 disassociated。
> 此路徑指向 Disassociated，不指向 Associated。**

#### §2-3-3 **判定**

> ## **代入本 DUT 之判定：Disassociated（且不指向 Associated）。**

分兩層陳述，二層皆為實測，**不合併、不互相補強**：

- **層一（表達式本體，機械代入）**：三運算元「Absent／Absent／查無」，
  **表達式不成立或不可判**。此層之結論是 **「本路徑對本 DUT 不產生變體指示」**，
  **不是** 「指向 Associated」。
  且其載體物件 `4915246` 依 R-ICS2 v2(a) 對本 DUT **不適用**（二軸落空），
  依 R-ICS9(b) 之逐物件實測原則，一個判不適用之物件本不構成本 DUT 之證據。
- **層二（語意鏈續查，本 DUT 自身文件）**：`$Head_Unit_Screen_Size$` 之
  10.1 吋枚舉值經 SYS2 `NRL-52847` 之逐字，接到 **DCSDX ↔ R1L radio HU ↔
  disassociated HU 變體** 這條鏈上。**此層指向 Disassociated。**

**兩層合觀：本路徑無一處指向 Associated；可判之部分指向 Disassociated。**

#### §2-3-4 本判定之已知弱點（如實揭露，不掩飾）

1. **`$Head_Unit_Screen_Size$` 之本 DUT 實值未取得**（無專屬 PROXI）。
   層二之鏈以「若 = [10]」為條件句成立；**本報告不斷言該值為 [10]**。
2. `NRL-52847` 之 `10.1 inch DCSDX` 段明列 `R1L`，**未明列 `R1L-R`**。
   本 DUT 之 Radio 為 `R1L-R`（另有 `R1L`）。**此差本報告不調和**。
   同段 `2)b)` 另有 `DCSD70_wICS_NonCAN which will be paired with the R1 radio HU`
   之更寬寫法（`R1` 而非 `R1L`），二者之關係未明。
3. PROXI `HDCC27` 非本 DUT 車型，其 `Rule Reason` 只證「該車型下 node 119 恆 Absent」，
   **不直接等同本 DUT**。惟 LID 之 `N/A for Atlantis High` 是**架構層**之陳述，
   不繫於車型，此項對本 DUT 成立。
4. 下放包將此表達述為「表達『有無外接螢幕件』的方式」。
   **本輪實測不支持該描述**：`node 119` 之全名為 `ICS_R/CCDMR`（後排 HVAC 面板／後排 CCDM），
   `$Head_Unit_Screen_Size$` 為 HU 螢幕尺寸解析度枚舉，
   而 `DCSD` 在該句中僅為 `$CCDMF_RQ_DISP_INTS$` 之**收訊方之一**。
   **此句之判別軸是「前／後排 CCDM 在否」＋「HU 螢幕規格」，不是變體軸。**
   此與報告 11 §2-5 之判讀（「不是 Associated／Disassociated 之變體分支」）一致。

### §2-4 與 R-ICS37(a) 之一致性

**R-ICS37(a) 逐字**：

> `(a) **採認 `Disassociated`**。為**過渡採認**，繫於 DR-ICS18 之上游答覆。`

**R-ICS37 成因段之逐字（節錄）**：

> `成因：upstream-10 §2-1。作業 A 量得本 DUT 為 **Disassociated**（'Silver Box'，外接 DCSD）。支持證據十項**全部脫離 §1.8／§1.18**（循環不計入者 0），反證七項逐項處置。`
> `分支配對檢定：Associated 分支適用需求物件 **0**，Disassociated／Silver Box 分支 **46** —— **46 : 0**。`

**本輪 C-2 之判定與 R-ICS37(a) 之比對**：

| 面向 | R-ICS37(a) | 本輪 C-2 | 判 |
|---|---|---|---|
| 變體結論 | `Disassociated` | Disassociated（層二）／無指示（層一） | **一致** |
| 是否指向 Associated | 否 | **否**（無任一運算元或語意鏈指向 Associated） | **一致** |
| 是否脫離 §1.8／§1.18 | 十項證據全數脫離 | **本路徑亦全數脫離**（素材為 CFTS022 §3.2.9、CFTS020 §1.3、LID、PROXI、SYS2、DBC，無一取自 §1.8／§1.18） | **一致** |

> ## **C-2 之判定與 R-ICS37(a) 之結論一致。無衝突。**

**逐字回報（依交辦要求）**：本輪走通 b10 未走過之第三條路徑後，
所得為 **`Disassociated`**，與 `R-ICS37(a)` 之 **`採認 Disassociated`** **一致**。
本路徑構成 R-ICS37 之**第十一項獨立證據候選**（脫離 §1.8／§1.18），
**惟其是否採認為證據，屬分析層之範圍，本報告不裁。**

---

## §3 E16 判定

### §3-1 E16 之二個觸發條件逐一比對

E16 逐字（下放包 12）：
「若 C-1 確認**七錨受外引影響**、或 C-2 之判定**與 R-ICS37(a) 衝突**，立即停下回報。」

| 條件 | 本輪實測 | 觸發？ |
|---|---|---|
| C-1：七錨受外引影響 | 七錨所在節（§1.5／§2.2 子樹／§2.2.2）共 33 個物件中，帶 `{CFTS020}` 外引者 **0**；七錨本文自身外引 **0**；第 1 章外引 **0**；第 2 章之 2 個外引其行為客體與四個 §2.2 錨**不重疊**；CFTS020 側對本 DUT 適用之 popup 物件 **0**。⟹ **未受影響** | **否** |
| C-2：與 R-ICS37(a) 衝突 | C-2 判 **Disassociated**（層二）／**無指示**（層一），**無一處指向 Associated**。R-ICS37(a) 採認 **Disassociated**。⟹ **一致** | **否** |

### §3-2 **E16：未觸發**

本輪未改任何錨、未改任何 TC JSON、未動任何 `specification_reference`
（見報告首之 shasum 自證）。

### §3-3 **E9：未觸發**

本輪未遇條文互斥。
CFTS022 與 CFTS020 之關係經實測為**外引（單向指向）**，非互斥；
CFTS020 §1.8 與 §1.18 之關係本輪未新增互斥證據
（A-ICS63 之既有衝突不因本輪而變）。
`4915246` 與 `4819139` 二處之 `$Head_Unit_Screen_Size$` 用法不互斥
（前者為送訊條件、後者為顯示尺寸判定）。

---

## §4 未預料之事（如實呈報，不作調和、不代擬條文、不自取編號）

### §4-1 **未預料-1（最重要）：「七個純 CFTS022 錨」在本輪已不成立 —— 現為六個**

`generated/b06/b06_tcs.json` 之二條 Mute TC 之 `specification_reference` 實測逐字為：

```
CFTS020-4821709
CFTS022-4914993
```

而報告 11 §3-0（2026-08-29 實測）載其為 `CFTS022-4914993`（單錨）。
`generated/b06/b06_tcs.json` 之 shasum 亦由 `a0a416e9…`（報告 11）
變為 `090517f1…`（本輪）。`generated/b01/b01_tcs.json` 之 shasum 亦已變
（`682e2d24…` → `fa43557a…`），惟其五條 TC 之錨內容經逐條複驗**與報告 11 完全相同**。

**現況**：純 CFTS022 錨之 TC = **5 條**，相異 ObjectID = **6 個**
（`4914956`／`4914957`／`4914958`／`4914974`／`4914975`／`4914976`）。

**意涵（陳述，不裁）**：
1. 下放包 12 作業 C 之交辦面（「七個現用錨」）與 repo 現況已不一致。
   本報告對七個 ObjectID 全數執行檢定以維持可比性，並同時登記現況為六個。
2. **`4914993` 現已直接錨在 §1.18.1.2 之 `4821709`**
   （逐字：`TLM shall adjust the volume of the audio output according to signal $ICSMuteButton$.In particular, TLM shall set Mute.Req signal to the same value as…`，
   v2(b) 判**適用**）。即 A-ICS73 所擔心之「§1.18 取捨波及 CFTS022 側 TC」
   **已在 `4914993` 上以「直接加錨」而非「外引反噬」的形式成為事實**。
   E16 之定義面限於「外引影響」，故本項**不觸發 E16**；
   但其風險面（§1.18 若退出，b06 之二錨行如何處置）**與 A-ICS73 同源**。
   **此為 Pei 之範圍決定，本報告不裁。建議登為 `A-ICS?` 或併入 A-ICS73。**
3. 本輪未讀取任何 handoff，無從得知加錨之執行批次與依據；
   形制上與 `R-ICS40(d)`（「加錨於 b12 執行」）相符，**惟本報告不作此認定**。

### §4-2 未預料-2：下放包對「第三種表達」之描述與實測不符

下放包述為「**CAN node 119（`ICS_R`）在否 ＋ `$Head_Unit_Screen_Size$`**」
表達「有無外接螢幕件」。實測：

- `ICS_R` 之 PROXI 全名為 **`ICS_R/CCDMR`**（後排 ICS／後排 CCDM），
  其 LID 為**後排 HVAC 按鍵**（`ICS_R1.ICS_R_L_BlowerDown` 等），
  `Arch Basis = PNet`、`Usage Comment` 逐字 **`N/A for Atlantis High`**。
- `$Head_Unit_Screen_Size$` 為 **HU 螢幕尺寸／解析度枚舉**（`EcuCfg16.EC_AudTel3B`，
  `0 = Absent` … `10 = R1 10.1" 1200x1920`），**`[10]` 不是 10 吋**。
- `4915246` 之句意為：**前排或後排 CCDM 在場、或 HU 螢幕為 10.1" 1200x1920 時，
  HU 送顯示亮度給前後排 CCDM 與 DCSD 模組**。
  `DCSD` 在此僅為**收訊方之一**，不是判別項。

**故該句之判別軸為「CCDM 前／後排在否」＋「HU 螢幕規格」，非變體軸。**
此與報告 11 §2-5 之判讀方向一致，但**語意細節（`ICS_R` = 後排 CCDM、
`[10]` = 枚舉值而非吋數）為本輪新測**。
**建議據此修正 A-ICS76 之描述（`A-ICS?`／併 A-ICS76）。**

### §4-3 未預料-3：`forms/PDT27_E2A_R1_BHCAN2.dbc` 之 `DIS_CENTERSTACK` **收方含 `LTM`** —— 填補 b10 §3-4 自承之盲區

報告 10 §3-4 自承：「**ICS／DCSD 位於 BHCAN（`LTM` 不在其上），`LTM` 位於 FDCAN8
（`DCSD`／`ICS` 皆不在其上），二網之間的閘道對映（`SGW`）未涵蓋於這二個 DBC 檔。**」

本輪為查 `ICS_R` 而掃了**四個** DBC（含 b10 未掃之 `forms/` 二檔），實測：

**`forms/PDT27_E2A_R1_BHCAN2.dbc`**（`latin-1`；`BU_:` = `ETM FPDM LTM SGW`，4 節點；`BO_` 63 則）

```
BO_ 1445 DIS_CENTERSTACK: 8 SGW
  SG_ DCSD_DISP_STAT   : 7|3@0+ (1,0) [0|6] ""  ETM,LTM
  SG_ DCSD_Enter       : 11|1@0+ …            ETM
  SG_ DCSD_Screen_Off  : 12|1@0+ …            ETM
  SG_ DCSD_VOLKNOB_DIR : 9|2@0+ …             ETM
  SG_ DCSD_VOLKNOB_VAL : 21|6@0+ …            ETM
  …（共 21 個 `DCSD_*` 訊號）
```

**對照 `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`**（b10 所用）：

```
BO_ 1445 DIS_CENTERSTACK: 8 DCSD
  SG_ DCSD_DISP_STAT : 7|3@0+ …  SGW
  …（共 25 個訊號，收方為 ECC／SGW／BCM）
```

**即：同一則 `BO_ 1445 DIS_CENTERSTACK`，在 R4_BHCAN 上由 `DCSD` 發出、收方到 `SGW` 為止；
在 R1_BHCAN2 上則由 **`SGW`** 轉發，且 `DCSD_DISP_STAT` 之收方明列 **`ETM,LTM`**。**
`LTM` 於 R1_BHCAN2 收到之含 `DCSD` 字樣訊號 = **1**（`DCSD_DISP_STAT`）；
於 R4_BHCAN = **0**。

**意涵（陳述，不裁）**：
1. `$DCSD_DISP_STAT$` 正是 CFTS020 §1.8 判定 `'DCSD Screen ON' state` 所用之訊號
   （如 `4819638` 逐字：`While the DCSD is in the 'DCSD Screen ON' state it shall send $DCSD_DISP_STAT$ = [ON].`）。
   **本 DUT 之 ECU `LTM` 在此 DBC 上是該訊號之收方** —— 這是**正向**之
   Disassociated 結構證據，且**脫離 §1.8／§1.18**（素材為 DBC）。
2. **但本報告不得逕用之為證據**：`forms/FORMS.md` 對該檔之登錄逐字載
   「**(e) 取代關係**：與 `PDT27_E2A_R4_BHCAN.dbc`（`features/vehicle_setting/inputs/`）
   **並非版次關係**。訊號名集合三分實測：兩者皆有 310、僅 R4 有 **573**、
   僅 BHCAN2 有 **32**。**何者適用於本專案未裁定（A-DM14）**」，
   且其「使用中之 feature」欄為 **`display`（R-DM19）**，**不含 `ics_management`**；
   `features/ics_management/feature.yaml` 之 `reference:` 節所綁定者為
   `PDT27_E2A_R4_BHCAN.dbc` 與 `PDT27_E2A_R5_FDCAN8.dbc`（本輪唯讀確認）。
3. **故本項為「盲區已可被填補」之事實登記，非證據採認。**
   是否將 `PDT27_E2A_R1_BHCAN2.dbc` 綁入本 feature，是綁定層之決定
   （繫於 A-DM14），**分析層與執行層皆不得逕定**。
   **建議登為 `A-ICS?`，並與 A-ICS24（`R5_FDCAN8` 零貢獻）、A-ICS47 併看。**

### §4-4 未預料-4：CFTS022 另有二個未量之螢幕組態參數

§2-1 之 `$…$` token 全掃另測出 CFTS022 有：

- **`$Touchscreen_ICS$`（3 次）**：`4915184`／`4915185`／`4915186`，§3.2.2 Audible Touchscreen Feedback，
  `ECU:ETM`／`Radio:R1H, R1M`／`EE:Atlantis High` —— 三者 v2(a) 皆**不適用**本 DUT（`ECU` 無 LTM、`Radio` 無 R1L/R1L-R）。
  逐字例：`When the customer has selected to enable the audible touchscreen feedback setting, the HU shall send $Touchscreen_ICS$ = [enabled] signal within <Tsend>.`
- **`$Rear_Screens_Present$`（2 次）**：`4915296`／`4915303`，§3.2.16 Video Button Readback，
  `ECU:ETM`／`Radio:R1H`／`EE:Atlantis High` —— 二者 v2(a) 皆**不適用**本 DUT。

**意涵**：`$Touchscreen_ICS$` 之命名暗示「ICS 帶觸控螢幕」之組態面，
是**第四條**可能之變體表達路徑；但其三個載體物件對本 DUT 全部不適用，
**本輪不走此路徑，僅記錄其存在，不作任何推定**（處理方式同報告 11 對 A-ICS76 之作法）。

### §4-5 未預料-5：`4915278`（§3.2.13）為 CFTS022 唯一之**無括號**外引

`according HMI and CFTS020` —— 不帶 `{}`、不帶引號。
若比對式只寫 `\{CFTS020\}`（如報告 11 §7-1 之複核所用形制），
**此點會被漏掉**。本輪以 `bare` 式（`CFTS ?0?20`）捕獲。
**意涵**：外引之寫法不統一，`{}` 不是可靠之錨定符。
其 `EE Architecture:Atlantis Mid`（不含 Atlantis High／All）令其對本 DUT 不適用，
故本輪之結論不因它而變；**但若日後有 Atlantis Mid 面之量測，須沿用 `bare` 式。**

### §4-6 未預料-6：報告 11 之行號與本報告一律差 1

CFTS022 之 shasum 二輪完全相同（`7acfa462…`），故非素材差。
差因在行號慣例（本報告 1-based 且指屬性頭行）。
**登記於此以免日後被誤讀為素材更動。**

---

## §5 本輪之已知局限（如實揭露）

1. **`$Head_Unit_Screen_Size$` 之本 DUT 實值未取得**（§2-3-4-1）。
   C-2 層二之判定為條件句，非斷言。
2. **未讀 `docs/handoff/**`**（禁區），故無從交叉核對 §4-1 之加錨執行依據。
3. 外引之「所指章節」判定（§1-3(ii)）為**行為主題對映**，非文件明示。
   對映之關鍵詞由本報告選定（`screen (on|off)`／`touch coordinate`），
   **該選擇本身未經上游確認**。§1-3(i) 之「明示落點 0」則為確定之事實。
4. 本輪只掃 CFTS022 與 CFTS020 二檔之外引關係，
   **未掃 CFTS022 對 `{CFTS019}`／`{CFTS024}`／`{CFTS026}`／`{VF***}` 等
   其他 22 種外引 token 之落點**（§1-1 已列其計數）。
   若 §1.8／§1.18 之取捨經由 CFTS019 等第三份文件迂迴影響 CFTS022，
   **本輪未量**。
5. 屬性擷取以 `[key:value]` 為形制；值本身含 `[` 或 `]` 者會被漏抓
   （CFTS022 之 336 物件中，`ECU`／`Market`／`Radio` 覆蓋 334、
   `EE Architecture` 覆蓋 332，缺者為表格內 `Description` 型物件，
   與報告 11 §7-3 之實測一致）。
6. PROXI 僅有 `HDCC27` 一份且非本 DUT 車型（§2-3-4-3）。
7. 本報告未對任何錨、任何 TC JSON、任何 `specification_reference` 作任何更動，
   未生成任何 TC，未自取 `A-`／`DR-` 編號，未執行任何 git 指令。
