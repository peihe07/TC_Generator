# 59 — Comfort HMI / 25 條之判定依據複核：**四份被委派文件已找到**

- 產出層：執行層｜2026-08-16｜對象：分析層
- 對應：`docs/handoff/81_missing_docs_recheck.md`（分析層撰寫中）
- **未生成任何 TC、未修改任何既有 TC、未寫回。**

---

## 0. 一句話

那 25 條裡，**有一整類的理由是「文件不在手上」——而其中四份文件，就在客戶目錄裡。**
本輪找到 `Core HMI L&F`、`HMI Settings List`、`Pop Up List`、`VF727 Climate Controls`，
CFTS044 亦在（惟其內容不含所需之條文）。**`HMI Notes` 確實不存在。**

---

## 1. 搜尋之涵蓋範圍（R-C30）

| 項 | 範圍 |
|---|---|
| 客戶目錄 | `/Users/peihe/Work/02_Project_R1LR/` **全樹、深度不限**，另及 `Work_Projects/` 之 `R1L_RTM_V3`／`NR1L_RTM`／`R1LR_DocsManagment`／`R1L_TCDB` |
| pattern | `find -iname` 之 `*core*hmi*logic*`／`*Logic and Flow*`／`*settings*list*`／`*CFTS*044*`／`*HMI*Notes*`／`*PDO*`／`*VF*HVAC*`／`*pop*up*list*`；另一次系統層 `mdfind` 交叉核對 `HMI Notes` |
| 本地素材 | `inputs/` 之 CFTS043 `.doc`（1.74 MB 文字）、CFTS043 R1L-R scope tree view（4,265 列）、Market Configuration Table（8 個工作表全掃）|
| **已知漏報** | 以**內容**而非檔名承載者不被 `-iname` 命中（例如某份 L&F 內夾帶之圖示表）。本輪只對已找到之四份做了內容掃描，**未對 107 份 HMI 文件逐份內容掃描** —— 這是未被證明不存在，不是被證明不存在（R-C13）|

---

## 2. 五份文件之搜尋結果

| 文件 | 結果 | 位置與 bytes |
|---|---|---|
| **Core HMI Logic and Flow** | **找到**（PDF ＋ SYS1 export xlsx）| `…/26PI2.5/HMI/Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf` 5,705,314；SYS1 xlsx 61,837 |
| **HMI Settings List** | **找到（含 SR24 版）** | `…/25PI3.5/HMI/HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx`；另有 SR25 Post R1L-R (Feb 13 2026) 295,635 |
| **CFTS044** | **找到** | `…/26PI1.5/SubSystem/Activation and Configuration/…CFTS_044_Vehicle Controls_20260310-1524.doc` 2,019,328 |
| **HMI Notes** | **不存在** | 全樹 ＋ `mdfind` 皆 0 命中。**近似者**：`HMI Read Me R1 SR24 Post 1A (September 27 2021).pdf`（同一 HMI 資料夾內）—— 是否即條文所指之「HMI Notes」**由分析層判**，本層不代判 |
| **PDO release** | 找到近似者 | `PDO Graphics Release - SR24_SR25_Post2A_CR27516_CR27517.pdf` 208,824；`PDO Theme Config V3.4.xlsx` 39,621 |

**額外找到（未在指示之清單內，但正是三條之委派對象）**：

- **`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`** —— `083`（14.1）之「pop-up list」
- **`Climate_Controls_2_Zone_VF727_V3_R3.docx`**（`1_Customer_Requirement/VF/…`）——
  `019-02`／`019-03` 之「VF HVAC document」。**CFTS044 自己證實了這個對應**：
  其第 1316 行寫 `Pressing the button shall pop-up the Climate screen and follow
  the behavior described in {VF727}`

---

## 3. 餘留分析（R-C24 第四項）—— 扣除委派後是否真的無餘留

| 單位／列 | 委派對象 | 文件狀態 | **餘留之實測** | 判定是否改變 |
|---|---|---|---|---|
| `NR1L-ComfortHMI-010`（13.4，已交付之 BLOCKED 列）| Core HMI L&F | **在手** | **有**：`PECD3.) Long Press: When long press behavior is applicable, pressing the button for more than 500ms, will increment/decrement 1 step every 200ms` —— 具體、可觀察、可寫成 procedure | **會改變** |
| `NR1L-ComfortHMI-382`／`-383`（11.5／12.6，已交付之 BLOCKED 列）| HMI Settings List／HMI Notes | **Settings List 在手（SR24 版）** | **有**：`Settings` 工作表 **30 Auto-On Driver**（30.1 Heated Seat／30.2 Heated Steering Wheel／30.3 Vented Seat）與 **31 Auto-On Passenger**（31.1／31.2）—— 即「Auto Comfort Settings 之選項」 | **會改變（382）**；`383` 之 HMI Notes 仍不存在，**不改變** |
| `SWE1-HVAC-083`（14.1）| pop-up list | **在手** | **有**：`Main` 工作表 r52 `HVAC`／`Pop-up when HVAC hard key for Passenger or Driver Temperature is selected`（且該列回指 `Comfort HMI Logic and Flow`）、r110 `Climate Comfort`／`When Climate is set Off using Hard Key and the radio is not in climate screen` | **會改變** |
| `SWE1-HVAC-019-02`／`-03`（2.13 MAX A/C）| VF HVAC document | **在手（VF727）** | **弱**：VF727 為訊號介面文件，僅見 `HVACMaxAC_Req`／`HVACMaxAC_Sts`（`Used to indicate the Max AC request status`）與 `1h:Max A/C`。**未見 HMI 側之 on/off 邏輯**。訊號層之存在不等於畫面可觀察量 | **可能不變** —— 須分析層判「VF727 是否即該條所指之 VF HVAC document」 |
| `NR1L-ComfortHMI-012`（13.5，已交付之 BLOCKED 列）| CFTS044 | **在手** | **無**：該 `.doc`（26PI1.5 版，781 KB 文字）搜尋 `rocker`／`4-way`／`four way` **0 命中** | **不改變**（惟所查者為 26PI 版，非 SR24 同期版）|
| `SWE1-HVAC-006-04`（2.5 recirc icon）／`122-02`（16.16 seat off icon）| 「the table」／「see Climate section」 | PDO 為候選 | **未見**：`PDO Theme Config V3.4` 全檔掃 `recirc`／`climate`／`seat`／`icon` 僅 1 命中且無關（`JL Rubicon`）；`PDO Graphics Release` PDF 之文字層掃上述字串 **全部 0 命中** | **不改變**（惟 PDF 為圖形釋出說明，其圖像內容非文字，**此為弱陰性**）|
| `SWE1-HVAC-099`（14.15 可用之 comfort controls）| 「depend on vehicle configuration」 | Settings List 在手 | **部分**：Settings List r536 `18. Seats & Comfort｜This section is not shown when vehicle is not equipped with comfort controls (heated / vented seats, heated steering wheel)` —— 給了**顯示規則**，仍未給**配置 → 控制項之對照** | **可能部分改變** |

---

## 4. 以 CFTS043 ＋ Market Configuration Table 重查兩題（**此二題從未對這兩份查過**）

### 4.1 「哪種車配哪一組氣流模式」（9 條：`016-01`…`-03`／`018-01`…`-06`）

**CFTS043 有配置條件，但其 scope 排除 R1L。** 實測（R1L-R scope tree view，4,265 列）：

| 條文 | Scope 欄 | Radio 欄 |
|---|---|---|
| `…if PROXI parameter $VC_VEH_LINE$ = [637MCA] OR $Country_Code$ = [LATAM related countries] then HU shall display the **5 airflow modes combination**…` ×4 列 | **None** | **R1M, R1H** |
| `…‘Alternate Tri-Mode Climate Softkeys’ shall be implemented if PROXI parameter is $TriMode_cfg$ = [Trimode_5 modes]` ／ `$Tri_Mode$ = [Present]` ×4 列 | **None** | R1M, R1L, R1H |

**四模組（C13）之正面陳述：全文 0 命中。** `.doc` 全文（1.74 MB）搜
`4 airflow`／`four airflow`／`modes combination` 亦無四模組之條文。

**判定不變 —— 但問題之形狀變了**：原本是「規格沒說」，
現在是「**有說，但那句話被標成不屬於 R1L-R 之範圍**」。
這使 RD-1 問句 2 可以問得更準：不再問「四模組適用於誰」，
而是問「`637MCA / LATAM → 5 modes` 這條為何標為 R1L-R 範圍外，
而 R1L 之氣流模式組由何者決定」。

### 4.2 「哪種配置產生哪一組 tab」（2 條：`001-01`／`001-02`）

- CFTS043 R1L-R tree view：`tab`／`Massage`／`heated wheel` **各 0 列**
- CFTS043 `.doc` 全文：`comfort tab`／`Front tab`／`Seats tab` 等 **0 命中**
- **Market Configuration Table**：8 個工作表全掃
  `HVAC|climate|airflow|defrost|recirc|heated|vented|seat|comfort|fan` ——
  **僅 3 命中且全在 ReadMe 之範圍說明句**，資料工作表 0 命中。
  該表之內容為**市場／國別／收音機／語言／地圖**，**與氣候配置無關**

**判定不變。** 惟須記一件事：CFTS043 之 5 模組條文寫
`*Refer to Market Configuration Table to determine LATAM related countries`
—— **MCT 之用途是查「哪些國家算 LATAM」，不是查氣候配置**。
本層原先以 HVAC 關鍵詞掃 MCT，若只看那次掃描會誤判 MCT 與本題全然無關；
**它與本題有關，只是關聯在國別欄而不在 HVAC 欄。**

---

## 5. 25 條之判定依據 —— 分類回報

**先講一件不好聽的**：25 條之中，能從紀錄裡逐條回溯出**當時查了哪裡、
用什麼 pattern** 者，**不是全部**。凡屬「條文未定義」一類者，其依據多為
「129 節通讀後未見」，而**通讀不是 pattern，其涵蓋範圍無法事後重算**（R-C30）。

| 類 | 單位 | 當時之依據 | 可回溯性 |
|---|---|---|---|
| **A. 文件不在手上** | `019-02`／`019-03`（VF HVAC）、`083`（pop-up list）| 「該文件不在素材內」—— **而素材之界定是 `inputs/`＋`spec-index/`，未搜過客戶目錄** | 可回溯，**且其前提今日被推翻** |
| **B. 對照表不在本 spec** | `006-04`（`as displayed in the table`）、`122-02`（`see Climate section`）、`099` | 上繳 35 §9：「未指名節次，**全 129 節無該對照**」 | 可回溯（範圍＝129 節），pattern 為逐節通讀 |
| **C. 條文未定義該條件** | `047`（AUTO 何時不可用）、`016`／`018` 九條（哪種車配哪組模式）、`001-01`／`-02`（tab 組）| 129 節內無該定義 | 範圍可述，**pattern 不可重算** |
| **D. 兩章逐字相同** | `129-01`…`-03`（18.1 對 17.1）| 逐字比對，可重算 | 可回溯 |
| **E. 條文自身無可觀察量** | `039`（9.1 引入變體）| 條文閱讀 | 可回溯 |
| **F. 裝備存在與否未定** | `015-04`／`015-05`／`116-03`／`116-04`（後座氣候是否存在）| 129 節內無「哪些車有後座氣候」 | 見 §6 —— **此類今日亦有新證** |

---

## 6. 一項未在指示之內、但同源之發現：`$Rear_HVAC_cfg$`

`015-04`／`015-05`／`116-03`／`116-04` 四條之停下理由是
「文件未說哪些車有後座氣候」。

**CFTS043 之 R1L-R scope tree view 有 48 列**其 `Description` 為
`The below requirements shall be implemented when the PROXI parameter
$Rear_HVAC_cfg$ = [Present].`，**`Scope` 欄為 `Yes`、`Radio` 欄含 `R1L, R1L-R`**。

即：**後座氣候之有無，有一個具名、可引、且在 R1L-R 範圍內之配置參數。**

且本 pipeline **已有引用 CFTS043 為 PC 之前例** —— `039` 之後續七條即以
`See CFTS043 for details` 為其前提條件。

**故此四條之判定亦可能改變**，其形式為：PC 引 `$Rear_HVAC_cfg$ = [Present]`
（依 R-C28 第一問之「引該條文之明文」）。

---

## 7. 會改變之清單（本層之判讀，非裁定）

| 判定 | 單位／列 | 所依 |
|---|---|---|
| **改變（證據明確）** | `NR1L-ComfortHMI-010`、`NR1L-ComfortHMI-382`、`SWE1-HVAC-083` | §3 之逐條餘留實測 |
| **很可能改變** | `015-04`／`015-05`／`116-03`／`116-04` | §6 之 `$Rear_HVAC_cfg$`（48 列，Scope=Yes）|
| **可能部分改變** | `099` | Settings List 之顯示規則（非完整對照）|
| **待分析層判文件身分後定** | `019-02`／`019-03`（VF727 是否即 VF HVAC document）、`383`（`HMI Read Me` 是否即 HMI Notes）| §2／§3 |
| **不改變** | `012`（CFTS044 無 rocker）、`006-04`／`122-02`（icon 表未見，**弱陰性**）、`016`×3／`018`×6（CFTS043 之條文標為 R1L-R 範圍外）、`001-01`／`-02`（CFTS043 與 MCT 皆無 tab）、`129-01`…`-03`、`039`、`047` | §3／§4 |

**若上列「改變」與「很可能改變」全部成立，25 條會降至約 18–19 條，
另有二列已交付之 BLOCKED row 需重判。**

---

## 8. 待分析層裁定（本層不自行決定）

1. **文件範圍**：Core HMI L&F／HMI Settings List／Pop Up List／VF727／CFTS043
   是否得作為本交付件之依據？**R-C1 只定了 spec 之基線版本，未定「可引用哪些文件」。**
   —— 這一問必須先答，其餘全部繫於它
2. `HMI Read Me R1 SR24 Post 1A` 是否即 `11.5`／`12.6` 所指之 **HMI Notes**
3. VF727 `Climate_Controls_2_Zone` 是否即 `2.13` 所指之 **VF HVAC document**
4. 版本對齊：找到之 Settings List 有 SR24（June 2023）與 SR25（Feb 2026）兩版；
   Core HMI L&F 為 SR24 Post 2A；CFTS044 為 26PI 版。**基線為 SR24 CR24879**，
   跨文件之版本相容性非本層可判
5. **RD-1 尚未發出，其問句 2／3／4／6 之措辭將因本輪而改寫** ——
   在裁定前不動該檔

**未做**：未生成 TC、未改既有 TC、未寫回、未複製或移除任何檔案、
未改 `docs/RD1_questions_comfort.md` 與交付說明。git 未執行。
