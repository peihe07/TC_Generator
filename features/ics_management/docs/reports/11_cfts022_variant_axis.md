# 下放包 11 作業 D —— CFTS022 之變體軸量測

- **問題 1**：CFTS022 是否亦分 Associated／Disassociated 軸？
- **問題 2**：7 條純 CFTS022 錨之 TC 是否受影響？
- **腳本**：`features/ics_management/scripts/cfts022_variant_11.py`（新建）
- **依令**：本輪未執行任何 git 指令（含唯讀之 `status`／`diff`／`log`／`show`）；
  未改任何 TC JSON、未動任何 `specification_reference`；未生成任何 TC；
  未寫入 `RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`／
  `ANALYSIS_LOCK.md`／`docs/handoff/**`／`feature.yaml`；
  未改 `scripts/` 下任何既有檔（本輪僅新開 `cfts022_variant_11.py`）。
- **只列不裁**：本報告不裁決、不代擬條文、不自取 `A-`／`DR-` 編號（需要時寫 `A-ICS?`）。

**自證未改檔（`shasum -a 256`，本輪結束時實測）**

```
7acfa462533d143c8099933e5b9e707f1c36aa3be95f5d8d0875b42a1f917fef  inputs/…CFTS_022…20260608-1205.docx
682e2d24f89e4ae74a8efbc0733a77af0b1e679d1c3f9c67dc596aefef200f7f  generated/b01/b01_tcs.json
a0a416e9a6583b2f16eff6f666c48714195a1d104bde2f91b31e88938fcd3988  generated/b06/b06_tcs.json
249241453595cc2cb433a8d2d518ac1ad2df8efffca8aec4cbfc90247baedc5b  RULINGS.md
eeaa403508bfd5c0710b50ec05b6319e8f8e6e4fa9df7426802950b4e6aeb0fd  ANOMALIES.md
ea6ed546d8a8aa19c5fa12469e30b7311bf5e31ca7c98c626a64ad7da210556a  feature.yaml
```

---

## §0 掃描條件

### §0-1 素材與抽取法

| 項 | 值 |
|---|---|
| 素材 | `features/ics_management/inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 Functional Specification_20260608-1205.docx` |
| 抽取法 | 讀 `word/document.xml`；`</w:p>` → 換行、`</w:tc>` → tab；`re.sub(r"<[^>]+>","")` 去標籤；`html.unescape` |
| 實測行數 | **1669** |
| 物件屬性頭 | `^(\d{7}): \[`（對 `line.strip()` 比對） |
| 屬性擷取 | `\[([^\[\]:]+):([^\[\]]*)\]`，同 key 取首見 |
| 物件本文 | 屬性頭之**次一行** |
| 實測物件數 | **336** |

### §0-2 NBSP 與空白正規化

去標籤後、切行前，將以下字元一律換為一般空白（`U+0020`）：
`U+00A0`(NBSP)、`U+2007`、`U+202F`、`U+2009`、`U+2002`、`U+2003`；
`U+200B`(ZWSP) 直接刪除。**不合併連續空白**（保留欄位切分）。
此步驟先於一切比對執行，故本報告之所有命中數皆為 NBSP-正規化後之數。

### §0-3 詞界與大小寫

- **主掃**：`re.escape(term)` 之**子字串**比對，**不分大小寫**（`re.I`）。
  子字串法為**寬鬆側**，故「查無」在此法下之效力最強
  （子字串查無 ⟹ 詞界查無必然亦查無）。
- **詞界對照掃**：`\bTERM\b`，不分大小寫，施於 `Associated`／`Disassociated`／`DCSD`。
  兩法之命中數在本文件**完全相同**（見 §2），故詞界處理不影響任何結論。
- `Silver Box`：另掃無空白之 `SilverBox`。
- `_ADspl`／`_DDspl`：另掃去底線之 `ADspl`／`DDspl`（更寬鬆側）。

### §0-4 計數單位

行面 = **命中行數**。物件面另於 §3 逐物件列示。

---

## §1 屬性軸值域全列

CFTS022 全 336 物件之屬性 key **僅七個**，無第八個：

| key | 出現物件數 | 相異值數 |
|---|---|---|
| `Artifact Type` | 336 / 336 | 2 |
| `State` | 336 / 336 | 1 |
| `Model Year` | 336 / 336 | 1 |
| `ECU` | 334 / 336 | 48 |
| `Market` | 334 / 336 | 22 |
| `Radio` | 334 / 336 | 206 |
| `EE Architecture` | 332 / 336 | 42 |

> 註：`ECU`／`Market`／`Radio` 缺 2 個、`EE Architecture` 缺 4 個 —— 皆為表格內之
> `Artifact Type:Description` 物件（如 `4914987` Mute Conditions 表頭、`4914997`）。

### §1-1 `Artifact Type`（相異 2）

`Subsystem Functional Requirement` ×253、`Description` ×83。

### §1-2 `State`（相異 1）

`Approved` ×336。**無 `Draft`／`Rejected`／`Obsolete`。**

### §1-3 `Model Year`（相異 1）

`Default` ×336。**此軸在本文件完全不具區辨力。**

### §1-4 `ECU`（相異 48，值為逗號串，順序不定）

出現於 ECU 串中之**相異 ECU 名（原子值）全列**（實測，去序）：

```
ALL, AMP, CCDMF, CCDMR, CDM, DVD, ETM, FPDM, ICS, LTM, RRM, SCCM,
TBM, TBM2, VES2, VES3, VRM
```

**17 個原子值，無一帶變體資訊**（無 `DCSD`、無 `_ADspl`／`_DDspl`、
無 `LTM_ADspl`／`LTM_DDspl`／`ETM_ADspl`／`ETM_DDspl` 之任何形式）。

高頻串（前 12）：`LTM, ETM` ×63、`ETM` ×59、`ETM, LTM` ×49、`LTM` ×27、
`LTM, RRM, ETM` ×16、`ETM, LTM, RRM` ×14、`ETM, RRM, LTM` ×13、
`RRM, LTM, ETM` ×13、`LTM, ETM, RRM` ×13、`FPDM, ETM` ×10、
`RRM, ETM, LTM` ×9、`ETM, FPDM` ×4。其餘 36 串各 1～3 次。

> **關鍵**：CFTS020 之變體詞彙是掛在 **ECU／元件名**上的（`LTM_ADspl` 等，
> 見報告 10 §1-3）。CFTS022 之 ECU 軸**一律使用未加後綴之裸名**
> （`LTM`／`ETM`／`RRM`／`ICS`），**故此軸不承載變體資訊**。

### §1-5 `Market`（相異 22）

`All` ×291 佔絕對多數；其餘為 NAFTA／EMEA／APAC／LATAM 之區域列舉
（多為同一集合之不同排列）。**無變體相關值。**

### §1-6 `Radio`（相異 206 串）

出現於 Radio 串中之**相異原子值全列**（實測，去序）：

```
CTS1_2, High, R1H, R1L, R1L-R, R1M, VP1, VP1.5, VP2, VP2.5, VP2R5,
VP2R7, VP2R84, VP3, VP365, VP384, VP4, VP465, VP484, VP4R7, VP4R84,
VP5R120, allSys, noSys
```

**24 個原子值，無一帶變體資訊。** 本 DUT 相關者為 `R1L-R`（另有 `R1L`）。
高頻串：`R1H` ×48、`allSys` ×25、`R1L-R, R1L` ×14、`R1H, R1M` ×8、
`R1M, R1H` ×7、`R1L, R1M, R1L-R, R1H` ×7、`R1L, R1L-R` ×6、`noSys` ×2……
其餘 198 串多為長列舉之不同排列，各 1～3 次。

> **關鍵**：`R1L` 與 `R1L-R` **並列為兩個平行值**，二者皆無 `_ADspl`／`_DDspl`
> 之對應項。報告 10 §1-4 已實測「`_ADspl`／`_DDspl` 與 `R1L-R` 之綁定力為零」；
> 本輪在 CFTS022 側得到同向之結果 —— **Radio 軸亦不承載變體資訊**。

### §1-7 `EE Architecture`（相異 42 串）

出現於 EE 串中之**相異原子值全列**（實測，去序）：

```
All, Atlantis High, Atlantis Mid, CUSW, PowerNet, Small/Compact
```

**6 個原子值，無一帶變體資訊。**
高頻：`All` ×159、`Atlantis High` ×42、`PowerNet, Atlantis High` ×14、
`PowerNet` ×12、`Atlantis Mid` ×9、`Atlantis High, PowerNet` ×8、`CUSW` ×5……

### §1-8 §1 之結論

**CFTS022 之七個屬性軸中，無任何一軸帶變體資訊。**
逐軸複核 `_ADspl`／`_DDspl`／`Associated`／`Disassociated`／`Silver Box`／`DCSD`
於**軸值集合**中之出現：全部 **0**（`ECU` 17 原子值、`Radio` 24 原子值、
`EE Architecture` 6 原子值、`Market` 22 串、`Artifact Type` 2 值、
`State` 1 值、`Model Year` 1 值，逐一比對，無一命中）。

---

## §2 變體相關詞之全文出現與逐字

### §2-1 命中數總表（行面，NBSP-正規化後）

| 詞 | 子字串 `re.I` | 詞界 `\b…\b` `re.I` |
|---|---|---|
| `Associated` | **2** | **2** |
| `Disassociated` | **0** | **0** |
| `Silver Box` | **0** | —（含空白，不適用 `\b`） |
| `SilverBox` | **0** | — |
| `DCSD` | **2** | **2** |
| `_ADspl` | **0** | — |
| `_DDspl` | **0** | — |
| `ADspl`（去底線，更寬鬆） | **0** | — |
| `DDspl`（去底線，更寬鬆） | **0** | — |

**補掃（皆為子字串 `re.I`）**：

| 詞 | 命中行數 |
|---|---|
| `variant` | **0** |
| `touch screen`（含空白） | **0** |
| `Silver` | **0** |
| `suffix` | **0** |
| `integrated` | **0** |
| `LTM_`（後綴前綴形） | **0** |
| `ETM_`（後綴前綴形） | **0** |
| `touchscreen`（無空白） | 18 |
| `external` | 14 |
| `ICS` | 26 |

> **`variant` 一詞在 CFTS022 全文出現 0 次**（子字串、不分大小寫、NBSP 正規化後）。
> CFTS020 之變體定義段（`4819134`）以 `variants` 一詞出現 4 次；CFTS022 無對應段落。

### §2-2 `Associated` 之 2 處逐字（**均非變體義**）

**命中 1 —— L1423，物件 `4915210`**
（§3.2.6 Clear Personal Data；`ECU:ETM, LTM`；`Radio:R1H, R1L, R1L-R, R1M`；
`EE Architecture:PowerNet, CUSW, Atlantis Mid, Atlantis High`）

> `The new active profile shall be associated with the current memory seat position.`

判讀：小寫 `associated`，**動詞義「與……關聯」**，主詞為 profile／seat position，
與 HU 變體無關。

**命中 2 —— L1509，物件 `4915256`**
（§3.2.10 Selectable Theme；`ECU:ETM, LTM`；`Radio:R1L, R1M, R1L-R, R1H`；
`EE Architecture:All`）

> `When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. Note:  See the $VC_SpecialPKG$ column of the {PDO Theme Configuration} reference document for the value to send in $Radio_Theme$.Note:  This requirement does not apply to R1L for SR21.`

判讀：小寫 `associated`，**動詞義**，修飾 `special package value`／`theme`，
與 HU 變體無關。

**大寫首字之 `Associated`（變體名詞義）於 CFTS022 全文出現 0 次。**

### §2-3 `Disassociated` —— **查無（0）**

掃法：子字串、不分大小寫、NBSP 正規化後、1669 行全掃。**命中 0 行。**
詞界法同為 0。**此為有效之查無結果。**

### §2-4 `Silver Box`／`SilverBox` —— **查無（0）**

掃法同上，另單掃 `Silver`（不分大小寫、子字串）亦為 **0 行**。
**CFTS022 全文無 `Silver` 這五個字母之任何組合。**

### §2-5 `DCSD` 之 2 處逐字（**均非變體軸，且均非本輪 7 錨**）

**命中 1 —— L1171，物件 `4915151`**
（§3 Personalization Features 首個物件；`Artifact Type:Subsystem Functional Requirement`；
`ECU:ETM, LTM`；`Radio:VP2R84, VP1.5, High, VP2R7, VP3, R1L-R, CTS1_2, VP2.5, VP2, VP4R7, VP4R84, VP365, R1L, VP484, VP2R5, R1M, VP384, VP4, VP465, R1H`；
`EE Architecture:All`）

> `The HU shall send the touch coordinates as specified in Chapter {CFTS020} 'ICS and DCSD'.`

判讀：**外引 CFTS020 之章名**，`DCSD` 出現於被引文件之標題內，
**不是 CFTS022 自身之變體宣告**。此物件不在 7 錨之列。

**命中 2 —— L1490，物件 `4915246`**
（§3.2.9 Manual Display Intensity for CCDM both Front and Rear；
`ECU:CCDMR, ETM, CCDMF`；`Radio:R1H`；`EE Architecture:Atlantis High`）

> `The HU shall send the desired display intensity to the front and rear CCDM and to DCSD modules using the $CCDMF_RQ_DISP_INTS$ signal when (CAN node 94 (CCDMF) OR CAN node 119 (ICS_R) are present) OR ($Head_Unit_Screen_Size$ = [10]). See {VF668} for other requirements.`

判讀：`DCSD` 作為**收訊模組名**出現於本文，其適用條件是
**CAN 節點在否（node 94 / node 119）與螢幕尺寸**，
**不是 Associated／Disassociated 之變體分支**。
且此物件 `Radio:R1H` **不含 `R1L`／`R1L-R`**，
依 R-ICS2 v2(a) 對本 DUT **不適用**。此物件亦不在 7 錨之列。

### §2-6 §2 之結論

CFTS022 **從未定義、從未使用**「Associated／Disassociated 變體」這組概念。
其 2 處 `associated` 為普通動詞、2 處 `DCSD` 為外引章名與收訊模組名。
`Disassociated`／`Silver Box`／`_ADspl`／`_DDspl`／`variant` **五者全數查無**。

---

## §3 7 個錨物件逐一之變體面判定

### §3-0 錨之自行複驗（唯讀）

自 `generated/b01/b01_tcs.json`（6 條）與 `generated/b06/b06_tcs.json`（2 條）
逐條讀出 `specification_reference`，實測：

| # | batch | `req_id` | `tc_title` | `specification_reference` | 純 CFTS022？ |
|---|---|---|---|---|---|
| 1 | b01 | `SWE-ICS-010` | Stuck button held over 120 s | `CFTS022-4914956` | ✅ |
| 2 | b01 | `SWE-ICS-010` | Stuck fault held until de-bounced not-pressed | `CFTS022-4914957` + `CFTS022-4914958` | ✅ |
| 3 | b01 | `SWE-ICS-010` | Button held exactly 120 s | `CFTS022-4914956` | ✅ |
| 4 | b01 | `SWE-ICS-001` | VOLUME knob rotated clock-wise | `CFTS022-4914974` + `CFTS022-4914975` | ✅ |
| 5 | b01 | `SWE-ICS-001` | VOLUME knob rotated counter clock-wise | `CFTS022-4914974` + `CFTS022-4914976` | ✅ |
| — | b01 | `SWE-ICS-002` | Three detents rotated clock-wise | `CFTS020-4819541` + `CFTS022-4914975` | ❌（混錨） |
| 6 | b06 | `SWE-ICS-005` | Mute hardkey pressed while audio unmuted | `CFTS022-4914993` | ✅ |
| 7 | b06 | `SWE-ICS-005` | Mute hardkey pressed while audio muted | `CFTS022-4914993` | ✅ |

**複驗結果：7 條純 CFTS022 錨之 TC 確認無誤**（b01 5 條＋b06 2 條），
其**相異 ObjectID 集合大小 = 7**：
`4914956`、`4914957`、`4914958`、`4914974`、`4914975`、`4914976`、`4914993`。

> **與下放包之一項不符（如實記錄，不調和）**：下放包 11 作業 D 文中寫
> 「該 7 條所錨之 **6 個**相異物件」，隨後卻列出 **7 個** ObjectID。
> 實測相異物件數為 **7**，與所列 ID 個數一致，與「6」不一致。
> 本報告依實測採 **7**。此為文書筆誤之嫌，**不作裁決**。

### §3-1 逐物件之屬性三軸與變體面判定

七物件全部通過 **R-ICS2 v2(a)** 三軸交集
（`ECU ∈ {ICS, LTM}` ∧ `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE ∈ {Atlantis High, All}`），
逐一列示如下。

---

#### (1) `4914956` —— 行 L180，§1.5 Stuck Button Behavior `{4914953}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `ICS, ETM, DVD, LTM, RRM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `allSys` |
| `EE Architecture` | `CUSW, Small/Compact, Atlantis High, Atlantis Mid, PowerNet` |

本文（逐字）：
> `If the button is continuously in the pressed state for longer than 120 seconds, the HU shall set the stuck button DTC and send the “not pressed” value for the stuck button.`

- R-ICS2 v2(a)：`ECU ∋ ICS,LTM` ✅ ／ `Radio ∋ allSys` ✅ ／ `EE ∋ Atlantis High` ✅ ⟹ **適用**
- 本文是否涉變體元件（DCSD／外接螢幕／整合螢幕）：**否**。主詞為 `the HU`，
  客體為 `button`／`DTC`，無任何螢幕或 DCSD 之提及。
- **變體面判定：變體中立（variant-agnostic）。**
  `Radio = allSys`、`EE = 全五值`、`ECU` 涵蓋 `ICS`＋`LTM`＋`ETM`＋`DVD`＋`RRM`
  —— 此為文件中**最寬**之適用面，不可能是任一變體分支之專屬條文。

---

#### (2) `4914957` —— 行 L182，§1.5 Stuck Button Behavior `{4914953}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `RRM, LTM, ICS, DVD, ETM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `allSys` |
| `EE Architecture` | `Small/Compact, PowerNet, CUSW, Atlantis High, Atlantis Mid` |

本文（逐字）：
> `The fault shall remain active and the “not pressed” value periodically sent until the stuck button condition is cleared.`

- R-ICS2 v2(a)：**適用**（同上三軸全過）
- 涉變體元件：**否**
- **變體面判定：變體中立。** 軸值集合與 (1) 完全相同（僅列舉順序不同）。

---

#### (3) `4914958` —— 行 L184，§1.5 Stuck Button Behavior `{4914953}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | **`Description`** |
| `State` | `Approved` |
| `ECU` | `LTM, RRM, ICS, ETM, DVD` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `allSys` |
| `EE Architecture` | `PowerNet, Atlantis Mid, Atlantis High, Small/Compact, CUSW` |

本文（逐字）：
> `The Stuck Button DTC is cleared when a de-bounced "not pressed" signal is received. As such, the active DTC and "not pressed" states may persist across an ignition cycle.`

- R-ICS2 v2(a)：**適用**
- 涉變體元件：**否**
- **變體面判定：變體中立。** 軸值集合同 (1)(2)。

---

#### (4) `4914974` —— 行 L213，§2.2 Volume `{4914970}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `ETM, LTM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `VP484, VP365, R1L, VP4R84, VP4R7, R1L-R, R1H, VP384, R1M, VP465, VP4, VP3`（12 值，**含 `R1L` 與 `R1L-R`**） |
| `EE Architecture` | `PowerNet, Atlantis High, CUSW, Atlantis Mid` |

本文（逐字）：
> `The HU shall show the 'VOLUME POP_UP' to indicate the current volume level.`

- R-ICS2 v2(a)：`ECU ∋ LTM` ✅ ／ `Radio ∋ R1L, R1L-R` ✅ ／ `EE ∋ Atlantis High` ✅ ⟹ **適用**
- 涉變體元件：**否**。`show the 'VOLUME POP_UP'` 之主詞為 `the HU`，
  **未指定顯示於哪一塊螢幕**（既未寫 integrated screen，亦未寫 DCSD／external screen）。
- **變體面判定：變體中立。** 其 `Radio` 同時含 `R1L` 與 `R1L-R`，
  即本條**不區分**這兩個 Radio 型號，更不區分變體。

---

#### (5) `4914975` —— 行 L215，§2.2 Volume `{4914970}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `RRM, LTM, ETM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `High, VP384, VP365, R1H, CTS1_2, VP4R7, R1L, VP2.5, VP4R84, VP2, VP3, VP484, VP2R84, VP2R5, VP2R7, R1M, VP465, VP1, VP4, R1L-R, VP1.5`（21 值，含 `R1L`、`R1L-R`） |
| `EE Architecture` | **`All`** |

本文（逐字）：
> `When the VOLUME knob is active and the knob is rotated clock-wise, the HU shall increment the current audio level up by one for each detent position.`

- R-ICS2 v2(a)：**適用**
- 涉變體元件：**否**。`VOLUME knob` 為旋鈕（實體件），非螢幕件。
- **變體面判定：變體中立。** `EE = All`、`Radio` 21 值涵蓋全譜。

---

#### (6) `4914976` —— 行 L217，§2.2 Volume `{4914970}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `LTM, ETM, RRM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `VP4R7, VP3, High, VP465, VP2, VP1.5, R1H, VP4, VP4R84, VP384, VP2R7, VP365, VP2R84, CTS1_2, VP1, R1M, R1L, VP2R5, VP2.5, VP484, R1L-R`（21 值，含 `R1L`、`R1L-R`） |
| `EE Architecture` | **`All`** |

本文（逐字）：
> `When the VOLUME knob is active and the knob is rotated counter clock-wise, the HU shall decrement the current audio level down by one for each detent position.`

- R-ICS2 v2(a)：**適用**
- 涉變體元件：**否**
- **變體面判定：變體中立。** 與 (5) 成 CW／CCW 對，軸值集合等價。

---

#### (7) `4914993` —— 行 L256，§2.2.2 Entertainment Audio Mute/Unmute `{4914991}`

| 軸 | 實測值 |
|---|---|
| `Artifact Type` | `Subsystem Functional Requirement` |
| `State` | `Approved` |
| `ECU` | `LTM, ETM` |
| `Market` | `All` |
| `Model Year` | `Default` |
| `Radio` | `R1L, R1M, R1L-R, R1H`（4 值，含 `R1L`、`R1L-R`） |
| `EE Architecture` | **`All`** |

本文（逐字）：
> `When the HU detects that the Mute hardkey or softkey* has been pressed the HU shall toggle the mute/unmute state of the Entertainment Audio Source.* Note:  The Mute softkey applies only if the HMI calls for such a softkey.`

- R-ICS2 v2(a)：**適用**
- 涉變體元件：**否**。本文提及 `softkey`（軟鍵，需螢幕）與 `hardkey`（實體鍵），
  但**未指定該 softkey 位於哪一塊螢幕**，其條件寫作
  `applies only if the HMI calls for such a softkey` —— 掛在 **HMI 文件**上，
  **不掛在 Associated／Disassociated 變體上**。
- **變體面判定：變體中立。** `EE = All`、`Radio` 四值同列 `R1L` 與 `R1L-R`。
- **對照**：其 FPDM 對應條 `4915000`（§2.2.4）之 `ECU:FPDM, ETM`／`Radio:R1H`／
  `EE:Atlantis High` —— 該條與 `4914993` 構成一組**分支對**，
  但其分支軸為 **ECU（HU vs 前排乘客顯示器 FPDM）**，**不是變體**。

### §3-2 §3 之小結

| ObjectID | 節 | `Artifact Type` | R-ICS2 v2(a) 判定 | 本文涉變體元件 | 變體面判定 |
|---|---|---|---|---|---|
| `4914956` | §1.5 | SFR | 適用 | 否 | 變體中立 |
| `4914957` | §1.5 | SFR | 適用 | 否 | 變體中立 |
| `4914958` | §1.5 | Description | 適用 | 否 | 變體中立 |
| `4914974` | §2.2 | SFR | 適用 | 否 | 變體中立 |
| `4914975` | §2.2 | SFR | 適用 | 否 | 變體中立 |
| `4914976` | §2.2 | SFR | 適用 | 否 | 變體中立 |
| `4914993` | §2.2.2 | SFR | 適用 | 否 | 變體中立 |

**7 / 7 皆為變體中立**：無一物件之任何軸值、任何本文字面涉及
`Associated`／`Disassociated`／`Silver Box`／`DCSD`／`_ADspl`／`_DDspl`／
外接螢幕／整合螢幕。

---

## §4 章節結構

### §4-1 頂層章節樹（到二層，實測；行號取正文而非目次）

```
1  Functional Specification [CFTSMV022_CIP_R1] {4914924}          L90
   1.1  Revision Notes {4914925}                                   L91
   1.2  Introduction {4914927}                                     L126
   1.3  Returning to the Last Used Radio Group Source {4914936}     L143
   1.4  Function Change Arbitration {4914941}                       L152
   1.5  Stuck Button Behavior {4914953}                             L175   ← 錨 (1)(2)(3)
2  HU General Functions {4914959}                                   L186
   2.1  Delaying Cabin Output Channel Mode changes due to
        CD Disc Eject transitions {4914965}                         L197
   2.2  Volume {4914970}                                            L206   ← 錨 (4)(5)(6)，(7) 在其 2.2.2
   2.3  Cabin Output Channel Source Select HMI Events {4915004}     L279
   2.4  Climate Control Mode Select {4915053}                       L366
   2.5  Climate Control Mode Select {4915055}                       L369
   2.6  Controls Mode Select {4915057}                              L372
   2.7  Nav Mode Select {4915059}                                   L375
   2.8  Nav Mode Select {4915061}                                   L378
   2.9  Phone Mode Select {4915063}                                 L381
   2.10 More {4915065}                                              L384
   2.11 Screen On/Off {4915096}                                     L434
   2.12 Front Passenger Display Screen On/Off {4915098}             L437
   2.13 Driver Distraction Lockout (SR23+) {4915100}                L440
3  Personalization Features {4915150}                               L1169
   3.1  Personalization Configuration {4915155}                     L1178
   3.2  Personalization Features {4915163}                          L1241
```

**頂層章 3 個、二層節 21 個。無第 4 章。**
（目次面另有同一份章節樹，帶 `PAGEREF`，已於掃描中與正文區分。）

### §4-2 是否有類似 CFTS020 §1.8／§1.18 之分支章節？

**有分支章節結構，但其分支軸不是變體。** 實測到三種分支形制：

**形制 A —— 同名節成對（§2.4／§2.5、§2.7／§2.8）**

| 節 | ObjectID | `ECU` | `EE Architecture` | 本文 |
|---|---|---|---|---|
| §2.4 Climate Control Mode Select | `4915054` | `LTM, ETM` | **`Atlantis High, PowerNet`** | `When the Climate Controls mode is invoked the HU shall enter the Climate Controls mode and display the corresponding screen.  Note:  See {VF664} …` |
| §2.5 Climate Control Mode Select | `4915056` | `LTM, ETM` | **`CUSW, Atlantis Mid`** | **逐字相同** |

> §2.4 與 §2.5 **標題完全相同、本文逐字相同**，唯一差別在 `EE Architecture`
> （`Atlantis High + PowerNet` vs `CUSW + Atlantis Mid`）與 `Radio` 集合。
> **這正是「同一行為在不同架構分支各寫一次」的形制** —— 但其軸為
> **EE Architecture**，非 Associated／Disassociated。

| 節 | ObjectID | `ECU` | `EE Architecture` | 本文差異 |
|---|---|---|---|---|
| §2.7 Nav Mode Select | `4915060` | **`ETM, FPDM`** | `PowerNet, Atlantis High` | `When the NAV mode is invoked **on the HU or Front Passenger Display**, the modules shall enter Navigation mode…` |
| §2.8 Nav Mode Select | `4915062` | **`ETM, LTM`** | `Atlantis Mid, CUSW` | `When the NAV mode is invoked the HU shall enter Navigation mode…` |

> §2.7／§2.8 之分支軸為 **ECU（FPDM 在否）＋ EE Architecture**。

**形制 B —— HU 面／FPDM 面成對（§2.2 vs §2.2.3、§2.2.2 vs §2.2.4、§2.11 vs §2.12）**

| HU 面 | FPDM 面 | 分支軸 |
|---|---|---|
| §2.2 Volume（`4914970`） | §2.2.3 Front Passenger Display Volume（`4914994`） | `ECU` = `FPDM, ETM`、`Radio` = `R1H`、`EE` = `Atlantis High` |
| §2.2.2 Entertainment Audio Mute/Unmute（**含錨 `4914993`**） | §2.2.4 Front Passenger Display Entertainment Audio Mute/Unmute（`4915000`） | 同上 |
| §2.11 Screen On/Off（`4915097`） | §2.12 Front Passenger Display Screen On/Off（`4915099`） | 同上 |

> §2.11／§2.12 之本文亦逐字近同，僅主詞由 `the HU Screen` 換為
> `the Front Passenger Display Screen`。**分支軸為 ECU（FPDM），非變體。**
> 附註：§2.11 之本文明文寫 `Note:  See {CFTS020} for Screen On/Off behavior.`
> —— 即**螢幕開關之實質行為被外包給 CFTS020**；CFTS022 只留一句指向句。

**形制 C —— 節內同義物件並列（§2 章引言、§2.2 Volume Indicator 條）**

| 位置 | ObjectID | `ECU` | `EE Architecture` | 本文 |
|---|---|---|---|---|
| §2 引言 | `4914960` | `LTM, RRM` | `All` | `…activated by hardkey press and knob rotate events monitored by the HU.` |
| §2 引言 | `4914961` | `VES2, CDM, VRM, DVD, ETM, ICS, VES3` | `PowerNet, Atlantis High` | `…activated by hardkey/softkey press and knob rotate events monitored by the HU and ICS as defined in {VF650} or {VF169}…` |
| §2 引言 | `4914962` | `ICS, CDM, ETM` | `Atlantis Mid, CUSW` | 同上，去 video 面 |

| §2.2 | `4914983` | `ETM, LTM, RRM` | `PowerNet, Atlantis High` | `The HU shall not update the Volume Indicator or change the $VolumeENT$ signal when volume adjustment is disabled.` |
| §2.2 | `4914984` | `LTM, ETM, RRM` | `Atlantis…（另一集合）` | **逐字相同** |

> 同一句話寫兩次、以 `EE Architecture`／`Radio`（`noSys` vs 全譜）區分。
> **仍非變體軸。**

### §4-3 §4 之結論

CFTS022 **確有**「同一行為在不同分支各寫一次」之章節形制，
但其分支軸經實測為 **`EE Architecture`（Atlantis High／Atlantis Mid／PowerNet／CUSW／
Small/Compact）** 與 **`ECU`（HU 側 LTM/ETM vs 前排乘客顯示器 FPDM vs ICS）**，
**不存在任何 Associated／Disassociated 之分支**。
**七個錨物件無一位於任何分支對之一側**：
§1.5 為單節無對；§2.2 之三錨（`4914974/75/76`）為 §2.2 主體、其 FPDM 對應節
§2.2.3 不含旋鈕條；`4914993` 之對應側 `4915000` 為 FPDM 分支（`Radio:R1H`，
對本 DUT 不適用）。

---

## §5 結論與 E10 判定

### §5-1 問題 1：CFTS022 是否亦分 Associated／Disassociated 軸？

## **答：無。CFTS022 不存在 Associated／Disassociated 變體軸。**

三重獨立證據：

1. **屬性面（§1）**：336 物件之七個屬性軸（`Artifact Type`／`State`／`ECU`／
   `Market`／`Model Year`／`Radio`／`EE Architecture`）之**全部值域**逐一列盡，
   `ECU` 17 原子值、`Radio` 24 原子值、`EE Architecture` 6 原子值，
   **無一帶變體資訊**。CFTS020 之變體標記形式（`LTM_ADspl`／`ETM_DDspl` 之
   ECU 後綴，報告 10 §1-3）在 CFTS022 之 ECU 軸 **0 次出現**（`LTM_`／`ETM_` 皆 0 行）。
2. **詞彙面（§2）**：`Disassociated` 0、`Silver Box` 0、`Silver` 0、
   `_ADspl` 0、`_DDspl` 0、`ADspl`／`DDspl` 0、`variant` 0。
   `Associated` 之 2 次命中經逐字複核**皆為普通動詞義**（profile 與座椅記憶位置關聯／
   theme 與 special package value 關聯），**非變體名詞**。
   `DCSD` 之 2 次命中為**外引 CFTS020 章名**與**CCDM 亮度訊號之收訊模組名**，
   **非變體宣告**，且後者 `Radio:R1H` 對本 DUT 不適用。
3. **結構面（§4）**：CFTS022 有分支章節形制（§2.4/2.5、§2.7/2.8、
   §2.2 vs §2.2.3、§2.2.2 vs §2.2.4、§2.11 vs §2.12、§2 引言三並列、
   `4914983` vs `4914984`），但其分支軸經逐物件實測**一律為
   `EE Architecture` 與 `ECU`**，**無一為變體**。

**形式上之補述**：CFTS022 之變體處理方式是**外包** ——
§2.11 明文 `See {CFTS020} for Screen On/Off behavior.`、
§3 首條明文 `as specified in Chapter {CFTS020} 'ICS and DCSD'`。
即：**凡涉螢幕架構之行為，CFTS022 一律指向 CFTS020**，
自身只保留與螢幕架構無關之 HU 側行為。這與「CFTS022 無變體軸」互相印證。

### §5-2 問題 2：7 條純 CFTS022 錨之 TC 是否受影響？

## **答：7 條全部不受影響。逐條判如下。**

| # | TC | `req_id` | 錨 | 錨之變體面 | 判 |
|---|---|---|---|---|---|
| 1 | b01-01 Stuck button held over 120 s | `SWE-ICS-010` | `4914956` | 變體中立（`Radio:allSys`／`EE` 全五值／`ECU ∋ ICS,LTM`） | **不受影響** |
| 2 | b01-02 Stuck fault held until de-bounced not-pressed | `SWE-ICS-010` | `4914957` + `4914958` | 二者皆變體中立 | **不受影響** |
| 3 | b01-03 Button held exactly 120 s | `SWE-ICS-010` | `4914956` | 同 #1 | **不受影響** |
| 4 | b01-04 VOLUME knob rotated clock-wise | `SWE-ICS-001` | `4914974` + `4914975` | 二者皆變體中立（`4914975` `EE:All`） | **不受影響** |
| 5 | b01-05 VOLUME knob rotated counter clock-wise | `SWE-ICS-001` | `4914974` + `4914976` | 二者皆變體中立（`4914976` `EE:All`） | **不受影響** |
| 6 | b06-01 Mute hardkey pressed while audio unmuted | `SWE-ICS-005` | `4914993` | 變體中立（`EE:All`、`Radio` 含 `R1L`＋`R1L-R`） | **不受影響** |
| 7 | b06-02 Mute hardkey pressed while audio muted | `SWE-ICS-005` | `4914993` | 同 #6 | **不受影響** |

**判準之邏輯**：一條 TC 因變體而受影響，必須其錨物件落在某個變體分支之一側；
若該側非本 DUT 之變體（Disassociated），則該錨失據。
本輪實測 CFTS022 **不存在變體分支**，故七個錨無一落在任何變體側，
**無論本 DUT 是 Associated 或 Disassociated，此七個錨之適用性皆不變**。

**強化檢定（實測，非推論）**：即令把「本 DUT = Disassociated」代入，
七個錨之 R-ICS2 v2(a) 三軸判定**逐一重算，結果完全不變**
（七軸中無一軸之值域含變體項，代入無處可代）——
此即「不受影響」之量測證據，而非假設。

### §5-3 **E10 判定：未觸發**

E10 之觸發條件為「判 7 條**受影響**」。本輪實測判 **7 條全部不受影響**，
**故 E10 未觸發**。本報告未改任何錨、未改任何 TC JSON、未動任何
`specification_reference`（見報告首之 `shasum` 自證）。

### §5-4 **E9 判定：未觸發**

本輪未遇條文互斥。CFTS022 內部無互斥；CFTS022 與 CFTS020 之關係為
**外引（CFTS022 指向 CFTS020）**，非互斥。

### §5-5 對報告 10 §3-6 保留條之回填

報告 `10_variant_impact.md` §3-6 保留 1 載：

> 「**CFTS022 之變體軸未量**：7 條純 CFTS022 之 TC 於本欄計為『不受影響』，
> 其前提是『CFTS022 之物件不分 Associated／Disassociated 變體』。
> **此前提本輪未量**。若 CFTS022 亦分變體，b01-01~05、b06-01/02 亦可能受影響。」

**本輪已量。該前提成立。** 報告 10 之「7 條不受影響」由**未經量測之假設**
轉為**經量測之結論**。報告 10 §4 總表之「└ 不受影響（純 CFTS022）＝ 7」
與 §3-1 之「7 條不進入重錨」二項**不需修正**。

> 本報告不改動 `10_variant_impact.md`（禁區外但非本輪授權寫入之檔）。
> 此回填之登錄方式由分析層決定。

---

## §6 未預料之事（如實呈報，不作調和、不代擬條文）

**未預料-1：下放包所述「6 個相異物件」與所列 7 個 ObjectID 不符。**
實測 7 條純 CFTS022 之 TC 所錨之相異 ObjectID 為 **7 個**
（`4914956`／`4914957`／`4914958`／`4914974`／`4914975`／`4914976`／`4914993`），
與所列 ID 個數一致，與文中之「6」不一致。本報告依實測採 7，
**不裁定此為筆誤或實質不符**。

**未預料-2：CFTS022 對變體之處理是「全數外包給 CFTS020」，而非「不分變體」。**
§2.11 `Screen On/Off` 之本文只有一句
`The Screen On/Off hardkey or softkey shall be used to request the HU to turn the HU Screen image On and Off. Note:  See {CFTS020} for Screen On/Off behavior.`
—— 實質行為**不在 CFTS022**。
§3 首條 `4915151` 亦然（touch coordinates → `{CFTS020}`）。
**意涵**：CFTS022 之「無變體軸」不等於「CFTS022 之需求對兩種變體行為相同」；
正確的讀法是「**凡變體敏感之行為，CFTS022 都不寫，改指 CFTS020**」。
本輪之七個錨經逐條複核**皆無此類外引**（本文中無 `{CFTS020}`），
故此觀察**不改變 §5-2 之判定**，但它是一個**新事實**，
且直接關係到「CFTS020 §1.8／§1.18 之取捨會不會透過外引反噬 CFTS022 側之 TC」。
**建議登為新異常（編號待分析層給定，此處寫 `A-ICS?`）。**

**未預料-3：CFTS022 有大量「同名節成對」與「同文物件並列」，其分支軸為 EE Architecture。**
§2.4／§2.5 標題與本文**逐字全同**，僅 `EE Architecture` 與 `Radio` 不同
（`Atlantis High, PowerNet` vs `CUSW, Atlantis Mid`）；
`4914983` 與 `4914984` 之本文亦逐字全同。
**形制與 CFTS020 §1.8／§1.18 同型，軸不同型。**
此對 `R-ICS2 v2(c)`（章節分支為輔證）有實例意義：
CFTS022 側之分支輔證軸是 `EE Architecture`，而非 `ECU`。
**建議登為新異常或供 R-ICS2 v2(c) 補實例（`A-ICS?`）。**

**未預料-4：`Model Year` 軸在 CFTS022 完全無區辨力（336/336 皆 `Default`）。**
`State` 亦然（336/336 皆 `Approved`）。
即 R-ICS2 v2(a) 之三軸選擇（`ECU`／`Radio`／`EE`）**在實測上是完備的**
—— 其餘四軸中，二軸單值、`Market` 291/334 為 `All`、
`Artifact Type` 只分需求／描述。此為對現行判準之**正面佐證**，非問題。

**未預料-5：`4915246`（§3.2.9）是 CFTS022 唯一把 `DCSD` 當作實體收訊模組的條文，
但其適用條件寫成 CAN 節點與螢幕尺寸，不是變體。**
逐字：`… when (CAN node 94 (CCDMF) OR CAN node 119 (ICS_R) are present) OR ($Head_Unit_Screen_Size$ = [10]).`
**意涵**：本文件族內存在**第三種**表達「是否有外接螢幕件」的方式
（CAN 節點在否 ＋ `$Head_Unit_Screen_Size$`），
既非 `_ADspl`／`_DDspl` 後綴，亦非 §1.8／§1.18 分支章節。
若日後需以「本 DUT 是否 Disassociated」再作交叉複驗，
**`$Head_Unit_Screen_Size$` 與 CAN node 119 (ICS_R) 是一條本輪未走過的量測路徑**。
本輪**未走此路徑**（該物件 `Radio:R1H` 對本 DUT 不適用，不構成本 DUT 之證據），
**此處僅記錄該路徑之存在，不作任何推定。**

---

## §7 本輪之已知局限（如實揭露）

1. 本報告只量 CFTS022 **自身**是否有變體軸，**未量**「CFTS022 經 `{CFTS020}` 外引
   而間接繫於變體」之傳遞面（未預料-2）。七個錨經複核本文無外引，
   故此局限**不影響 §5-2 之判定**，但對 CFTS022 之其他物件未作此檢定。
2. 本報告未使用 CFTS020 之任何內容作為 CFTS022 判定之依據；
   §5-1 引報告 10 之數字僅作**對照**，判定本身完全由 CFTS022 自身之實測撐起。
3. 屬性擷取以 `[key:value]` 為形制。若某物件之屬性值本身含 `[` 或 `]`，
   該屬性會被漏抓。實測 336 物件中，`Artifact Type`／`State`／`Model Year`
   之覆蓋率為 336/336，`ECU`／`Market`／`Radio` 為 334/336、
   `EE Architecture` 為 332/336，缺者經逐一目視確認**皆為表格內之
   `Description` 型物件（本就無該些軸）**，非擷取失敗。
4. 本報告未對任何錨、任何 TC JSON、任何 `specification_reference` 作任何更動，
   亦未生成任何 TC、未自取 `A-`／`DR-` 編號。
