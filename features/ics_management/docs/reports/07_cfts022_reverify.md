# 07 — CFTS022 改綁與覆驗（作業 F，R-ICS12(b)(c)）

執行層，2026-08-29。工具：`features/ics_management/scripts/cfts022_reverify_07.py`。
全部數據為實測，未憑記憶。

---

## §0 掃描條件

### 抽取法
讀 docx 之 `word/document.xml`；`</w:p>` → 換行、`</w:tc>` → tab、
以 `<[^>]+>` 去 XML 標籤、`html.unescape`。
物件屬性頭之判準 `^(\d{7}): \[`；屬性以 `[key:value]` 抓；
物件本文取屬性頭之**次一行**。

### 正規化（只此五項，除此不動一字）
1. 彎引號（`‘ ’ “ ”`）→ 直引號
2. NBSP（U+00A0）→ 空格
3. 非斷字連字號（U+2011／U+2010）→ `-`
4. 連續空白摺為單一空格，並去頭尾
5. 去句末**單一**句號

另允許句首字母大小寫差異（R-4）。
**屬性軸之比對不套第 5 項以外之語意調和；順序不在正規化之列。**

### 適用性判準
R-ICS2 v2(a)（CFTS022 走三軸交集）：
`ECU ∈ {ICS, LTM}` ∧ `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE Architecture ∈ {Atlantis High, All}`。

### 二版之實體檔

| 版本 | 路徑 | sha256 |
|---|---|---|
| 舊（25PI3.5） | `features/privacy/inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx` | `5eb0dd739f002fe04e4891ceb9fd7d233b4e128a8b35eadce8ad6a631854dd78` |
| 新（26PI2.5） | `features/ics_management/inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 Functional Specification_20260608-1205.docx` | `7acfa462533d143c8099933e5b9e707f1c36aa3be95f5d8d0875b42a1f917fef` |

sha256 皆以 `shasum -a 256` 自實體檔算。

---

## §1 二版之基本比較

| 量 | 舊版 | 新版 |
|---|---|---|
| 物件總數（相異 ObjectID） | 336 | 336 |

- 共同 ObjectID：**336**
- 僅舊版有：**0**；僅新版有：**0**
- 全域本文（body）逐字相異者：**28** 個物件（本次七錨**皆不在**其中）
- 全域三軸字串相異者：**271** 個物件；其中**軸值集合真的變動**者僅 **5**
  （`4914928`、`4914930`、`4914983`、`4914984`、`4915132`）——
  其餘 266 之相異純為**列舉順序**。本次七錨皆不在該 5 之中。

---

## §2 四句 verbatim 之逐句比對

| ObjectID | 舊版原句 | 新版原句 | 相符 |
|---|---|---|---|
| 4914956 | If the button is continuously in the pressed state for longer than 120 seconds, the HU shall set the stuck button DTC and send the “not pressed” value for the stuck button. | （逐字相同） | ✅ |
| 4914957 | The fault shall remain active and the “not pressed” value periodically sent until the stuck button condition is cleared. | （逐字相同） | ✅ |
| 4914975 | When the VOLUME knob is active and the knob is rotated clock-wise, the HU shall increment the current audio level up by one for each detent position. | （逐字相同） | ✅ |
| 4914976 | When the VOLUME knob is active and the knob is rotated counter clock-wise, the HU shall decrement the current audio level down by one for each detent position. | （逐字相同） | ✅ |

四句於二版之原始字串（含彎引號）**位元級相同**，非僅正規化後相同。
四句亦與下放包 07 所載之字面相符（下放包用直引號，屬正規化第 1 項）。

**四句：4/4 相符。**

---

## §3 七物件之三軸比對

`字串相符` = 逐字（含列舉順序）相同；`集合相符` = 以逗號切分後之值集合相同。

| ObjectID | 軸 | 舊版 | 新版 | 字串相符 | 集合相符 |
|---|---|---|---|---|---|
| 4914956 | ECU | `ETM, DVD, LTM, RRM, ICS` | `ICS, ETM, DVD, LTM, RRM` | ❌ | ✅ |
| 4914956 | Radio | `allSys` | `allSys` | ✅ | ✅ |
| 4914956 | EE Architecture | `Atlantis High, PowerNet, CUSW, Atlantis Mid, Small/Compact` | `CUSW, Small/Compact, Atlantis High, Atlantis Mid, PowerNet` | ❌ | ✅ |
| 4914957 | ECU | `RRM, ICS, ETM, LTM, DVD` | `RRM, LTM, ICS, DVD, ETM` | ❌ | ✅ |
| 4914957 | Radio | `allSys` | `allSys` | ✅ | ✅ |
| 4914957 | EE Architecture | `Atlantis High, Small/Compact, CUSW, PowerNet, Atlantis Mid` | `Small/Compact, PowerNet, CUSW, Atlantis High, Atlantis Mid` | ❌ | ✅ |
| 4914958 | ECU | `LTM, ETM, RRM, DVD, ICS` | `LTM, RRM, ICS, ETM, DVD` | ❌ | ✅ |
| 4914958 | Radio | `allSys` | `allSys` | ✅ | ✅ |
| 4914958 | EE Architecture | `PowerNet, Atlantis High, Atlantis Mid, Small/Compact, CUSW` | `PowerNet, Atlantis Mid, Atlantis High, Small/Compact, CUSW` | ❌ | ✅ |
| 4914974 | ECU | `LTM, ETM` | `ETM, LTM` | ❌ | ✅ |
| 4914974 | Radio | `VP365, R1L, R1H, VP4R84, VP4R7, VP484, VP3, R1L-R, VP465, VP384, VP4, R1M` | `VP484, VP365, R1L, VP4R84, VP4R7, R1L-R, R1H, VP384, R1M, VP465, VP4, VP3` | ❌ | ✅ |
| 4914974 | EE Architecture | `PowerNet, CUSW, Atlantis Mid, Atlantis High` | `PowerNet, Atlantis High, CUSW, Atlantis Mid` | ❌ | ✅ |
| 4914975 | ECU | `RRM, ETM, LTM` | `RRM, LTM, ETM` | ❌ | ✅ |
| 4914975 | Radio | 21 值（含 `R1L`、`R1L-R`、`R1M`、`R1H`、`High`、`CTS1_2`、VP 系列） | 同一 21 值，順序不同 | ❌ | ✅ |
| 4914975 | EE Architecture | `All` | `All` | ✅ | ✅ |
| 4914976 | ECU | `RRM, LTM, ETM` | `LTM, ETM, RRM` | ❌ | ✅ |
| 4914976 | Radio | 21 值（同 4914975 之集合） | 同一 21 值，順序不同 | ❌ | ✅ |
| 4914976 | EE Architecture | `All` | `All` | ✅ | ✅ |
| 4914993 | ECU | `ETM, LTM` | `LTM, ETM` | ❌ | ✅ |
| 4914993 | Radio | `R1L, R1L-R, R1H, R1M` | `R1L, R1M, R1L-R, R1H` | ❌ | ✅ |
| 4914993 | EE Architecture | `All` | `All` | ✅ | ✅ |

### v2(a) 判定

| ObjectID | 舊版 v2(a) | 新版 v2(a) | 判定有無改變 |
|---|---|---|---|
| 4914956 | 適用 | 適用 | **無** |
| 4914957 | 適用 | 適用 | **無** |
| 4914958 | 適用 | 適用 | **無** |
| 4914974 | 適用 | 適用 | **無** |
| 4914975 | 適用 | 適用 | **無** |
| 4914976 | 適用 | 適用 | **無** |
| 4914993 | 適用 | 適用 | **無** |

**七物件之三軸：逐字（含順序）0/7 相符；以集合計 7/7 相符；v2(a) 判定 7/7 無改變。**

### 三軸外之附帶觀察（不在覆驗範圍，具名以免遺漏）
- `4914993` 之 `Model Year` 自 `2025, 2023, 2024` 改為 `Default`。
  該軸非 R-ICS2 v2(a) 之判別軸，本報告不判其影響，具名交分析層。

---

## §4 `4914993` 之完整逐字原句與三軸（005 之錨）

### 新版（26PI2.5，改綁後之權威）

屬性頭（逐字）：

```
4914993: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:LTM, ETM] [Market:All] [Model Year:Default] [Radio:R1L, R1M, R1L-R, R1H] [EE Architecture:All]
```

本文（逐字，未經任何正規化）：

```
When the HU detects that the Mute hardkey or softkey* has been pressed the HU shall toggle the mute/unmute state of the Entertainment Audio Source.* Note:  The Mute softkey applies only if the HMI calls for such a softkey.
```

（註：`Source.` 與 `* Note:` 之間無空格、`Note:` 後為**二個空格**，皆為來源原樣。）

三軸：

| 軸 | 值 |
|---|---|
| ECU | `LTM, ETM` |
| Radio | `R1L, R1M, R1L-R, R1H` |
| EE Architecture | `All` |

v2(a) 判定：**適用**（`ECU ∩ {ICS,LTM} = {LTM}`；`Radio ∩ {R1L,R1L-R,allSys} = {R1L, R1L-R}`；`EE ∩ {Atlantis High,All} = {All}`）。

### 舊版（25PI3.5）對照

```
4914993: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ETM, LTM] [Market:All] [Model Year:2025, 2023, 2024] [Radio:R1L, R1L-R, R1H, R1M] [EE Architecture:All]
```

本文與新版**位元級相同**。三軸值集合相同、順序不同；v2(a) 亦判適用。

與 R-ICS25(c) 所載之實測（`[ECU:LTM, ETM] [Market:All] [Radio:R1L, R1M, R1L-R, R1H] [EE Architecture:All]`）**逐字相符**——
R-ICS25(c) 所引者即新版之序列。

---

## §5 E4 是否觸發

# E4 觸發

依下放包 07 之字面判準（「任一句或任一屬性不符 → 停下」），
**七個物件之三軸屬性字串皆與舊版不逐字相符**，故 E4 觸發，已停下：
未改任何 TC、未自行調和、未代擬裁決條文。

### 不符者逐項具名

| 項 | 不符內容 |
|---|---|
| `4914956` | `ECU`、`EE Architecture` 之列舉順序 |
| `4914957` | `ECU`、`EE Architecture` 之列舉順序 |
| `4914958` | `ECU`、`EE Architecture` 之列舉順序 |
| `4914974` | `ECU`、`Radio`、`EE Architecture` 之列舉順序 |
| `4914975` | `ECU`、`Radio` 之列舉順序 |
| `4914976` | `ECU`、`Radio` 之列舉順序 |
| `4914993` | `ECU`、`Radio` 之列舉順序（另 `Model Year` 改值，非三軸） |

### 不符之性質（實測陳述，非調和主張）
上列 7 項之不符**全部**為多值屬性之**列舉順序**差異：
每一軸之值集合在二版**完全相同**（`SET_MATCH=True`，7/7），
無任何軸有值之增、刪或改字；R-ICS2 v2(a) 之判定 7/7 無改變。
四句 verbatim 4/4 逐字相符。

順序是否構成 R-ICS12(c) 意義下之「不符」，屬判準之解釋，
**執行層不自裁**。本報告如實列出二種比對之結果，交分析層裁。
若分析層裁定「多值屬性以集合比對」，則覆驗全綠、無升級之實體必要；
若裁定「逐字含順序」，則 A-ICS13 升級之實體為排序而非內容變動。

**b01 六條之錨與其上半 verbatim 於新版全數存在且逐字未變**——
就內容面而言，改綁未動任何已生成之 TC 所依之字句。
既有 TC 之回收與否屬 Tier 3，不在本作業之權限。
