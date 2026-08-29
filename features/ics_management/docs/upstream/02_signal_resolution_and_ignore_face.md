# 上繳包 02 — 訊號解佔位、Stuck Button ignore 面、CFTS020 偵察（2026-08-29）

對應下放包：`docs/handoff/02_signal_resolution_and_ignore_face.md`
（sha256 `1672032c0945c94376e5e74b22e497dc98b64f22c7ab47774cdf49d63c7ac907`，本包實測；亦記於 `generated/b02/manifest.json` 之 `context_sha256.handoff_02`）

> ⚠ **涵蓋範圍**：本上繳包所對之下放包版本為 sha256 `1672032c…`（§1～§7）。
> 下放包其後增補之 **§8 追補（R-ICS11／12／13、HMI L&F 四本、CFTS019 七件）**
> **本包未執行**；現行下放包 sha256 為 `02a81148…`。§8 之四項待另一輪。

**禁區遵守**：git 全數未執行（`add`／`commit`／`push`／`checkout`／`stash` 皆無）；
`framework.md`／`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md` 一字未改；
canon、`GATES.tsv`、`RULINGS.sha.tsv`、`PATH_POLICY_BASELINE.tsv` 未動；
未搬任何素材；Display／Browse／Navigation 三面 **TC 新增 0**。

---

## §0 量測基礎

沿上繳包 01 §0 之全部條件（docx 抽取法、逐字比對之四項正規化、`str.split()` 字數、
六欄掃描範圍、1-based 列號），另加本包新用者：

| 項 | 條件 |
|---|---|
| LID 掃描 | `forms/Logical Identifiers and CAN Mapping v1_78.xlsx` 之 `CAN Mapping` 分頁。**本包自驗表頭**：群組列 = **第 2 列**（`LID Information`／`Powernet`／`CUSW`／`Atlantis`／`Compact`／**`Atlantis High`(c26)**／`Comments`），欄名列 = **第 3 列**，資料自 **第 4 列** 起。`Atlantis High` 群組之五欄依序為 c26 `Signal Name`、c27 `CAN`、c28 `Format`、c29 `SNA`、c30 `VFs` —— **與上繳包 01 所用之 26／28 相符，但為本包重測所得** |
| DBC 掃描 | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`（sha256 `9ef1ec98…`）與 `PDT27_E2A_R5_FDCAN8.dbc`（`51c8fd60…`）。訊息以 `^BO_ <id> <name>:` 抓、訊號以 `^\s*SG_ <name>` 抓、列舉以 `^VAL_ <id> <sig>` 抓 |
| DTCs Matrix 掃描 | `forms/DTCs Matrix Core List Rev. 1.6.xlsx`（sha256 `06612fb4…`），分頁 **`DTC's in CFTS's`**；群組列 = 第 3 列（`ECU Columns`），欄名列 = **第 4 列**，資料自第 5 列起。所取欄名：`DTC (J2012 Format)`、`DTC Description`、`Lead CFTS / VF`、`ICS`、`R1L`、`Enable Conditions`、`Mature Criteria`、`Mature Time`、`De-Mature Criteria`、`De-Mature Time`（**以欄名引用，非 `c{n}`**，R-DD10） |
| CFTS020 物件辨識 | `scripts/cfts020_probe.py` 檔頭逐項載明：章節行 `^(\d+(\.\d+)*) (.+?) \{(\d{7})\}$` 且不含 `PAGEREF`；物件屬性頭 `^(\d{7}): \[`；三軸取 `ECU`／`Radio`／`EE Architecture`，逗號切分去頭尾空白；**軸不存在記 `None`，不以章節屬性代替**（R-ICS9(b)） |

---

## §1 裁決指紋（下放包 §2 之「待實測」由此填實）

`python3 scripts/rulings_hash.py --target features/ics_management/RULINGS.md`
（10 錨點，來源 1 檔）：

| 條 | sha8 | 落檔行 | 本文行數 |
|---|---|---|---|
| R-ICS1 | `3e48552b` | 12 | 8 |
| R-ICS2 | `ad557b5d` | 25 | 11 |
| R-ICS3 | `b10318e0` | 41 | 9 |
| R-ICS4 | `85de9871` | 55 | 10 |
| R-ICS5 | **`e6a4790d`** | 70 | 11 |
| R-ICS6 | **`77478a91`** | 86 | 10 |
| R-ICS7 | **`2c51cc80`** | 101 | 13 |
| R-ICS8 | **`bf473e9c`** | 119 | 22 |
| R-ICS9 | **`7e7aa921`** | 146 | 23 |
| R-ICS10 | **`a2cda337`** | 174 | 14 |

R-ICS1～4 之 sha8 **與上繳包 01 逐字相同** —— 分析層之增補未動既有四條。

## §1.1 前提驗證（R-DD26 v2(f)，執行前先驗）

| # | 前提 | 驗法 | 結果 |
|---|---|---|---|
| P1 | LID v1_78 存在且 9 個 ICS LID 全命中 | `ls` + `CAN Mapping` 第 1–1045 列全欄字串包含比對 | **成立**（9/9，列號 131／666／1024／1025／1026／1027／1038／1039／1044）|
| P2 | DTCs Matrix Rev. 1.6 存在 | `ls`，sha256 `06612fb4…` | **成立** |
| P3 | CFTS020 存在且 407 個相異 ObjectID | 本包重測：**物件 2180，相異 ObjectID 2180** | **不符 —— 見 §四-11** |

**P3 不自行調和**：上繳包 01 所報之 407 為「章節標題之 `{ObjectID}`」之相異數
（`\{(\d{7})\}` 全文比對）；本包所報之 2180 為「**物件屬性頭** `^\d{7}: \[`」之數。
二者量的不是同一件事，**兩數皆非錯**，但下放包 §0 P3 將前者寫為「物件數」。
以後者為 TC 生成之母數（章節標題不是可錨之物件）。

---

## §2 作業 A — DR-ICS8 佔位之解（R-ICS8）

### 2-1 逐步實測

**(a) LID 取值**（R-ICS8(a)(b)）：`CAN Mapping` r1038 `ICSMuteButton`，
`Atlantis High` 之 `Signal Name`(c26) 原值為**三名並列**（原檔以換行分隔）：

```
CLIMATIC_PANEL.Radio_btn4
GW_B_5.Mute_Button
DIS_CENTERSTACK.DCSD_Mute
```

同列 `CAN`(c27) = `CAN-B`、`Format`(c28) = `1 bit signal / 0 = Not_Pressed / 1 = Pressed`、
`Usage Comment`(c31) = `For Atlantis High, 14.4" and 12" DCSD on DT24 Truck uses the
DIS_CENTERSTACK signal which is equivalent to the CLIMATIC_PANEL signal`。

**(b) 綁定 DBC 篩**（R-ICS8(c)）：

| 候選 | `PDT27_E2A_R4_BHCAN.dbc` | `PDT27_E2A_R5_FDCAN8.dbc` |
|---|---|---|
| `CLIMATIC_PANEL.Radio_btn4` | `BO_ 1050 CLIMATIC_PANEL: 8 ` **`ICS`**，`SG_ Radio_btn4 40\|1@0+` — **有** | 訊息不存在 |
| `GW_B_5.Mute_Button` | `BO_ 1449 GW_B_5: 8 BCM` 存在，但 `SG_ Mute_Button` **不存在** — **落** | 訊息不存在 |
| `DIS_CENTERSTACK.DCSD_Mute` | `BO_ 1445 DIS_CENTERSTACK: 8 ` **`DCSD`**，`SG_ DCSD_Mute 0\|1@0+` — **有** | 訊息不存在 |

FDCAN8 三者皆無 → **E1 之字面條件（「綁定二 DBC 皆查有而名不同」）不成立**，
未觸發升級。但 DBC 篩後仍餘二名，**first-match 本身不決斷**。

**(c) 二名之取捨 —— 本包所用之判準與其依據**：取 `CLIMATIC_PANEL.Radio_btn4`。

依據為**已裁之 R-ICS2 ECU 軸**，非新判準：DBC 之發送節點實測
`CLIMATIC_PANEL` = **`ICS`**、`DIS_CENTERSTACK` = `DCSD`。
本 feature 之適用域為 `ECU ∋ {ICS, LTM}`，`DCSD` 不在其內；
且 LID 之 `Usage Comment` 自載 DIS_CENTERSTACK 僅適用於
「14.4" 與 12" DCSD on DT24 Truck」，並稱其與 CLIMATIC_PANEL **等效**。
`DIS_CENTERSTACK.DCSD_Mute` 依 R-ICS8(c) 之「記備援」登於
`generated/b02/manifest.json` 之 `signal_resolution.fallback`。

**此為執行層之取捨，非條文所明定。** 若分析層認為 R-ICS8(c) 於此應停下升級，
改回一名即可（三份 JSON 之 `$CLIMATIC_PANEL.Radio_btn4$` 全文替換）。

**(d) 值之列舉**（R-ICS8(d)）：`VAL_ 1050 Radio_btn4: 0 "Not_Pressed" 1 "Pressed";`
—— TC 中之 `0 (Not_Pressed)`／`1 (Pressed)` 為此列逐字，非自 LID `Format` 欄轉寫。

### 2-2 b01 三處佔位之改寫（IN §8.7.5(a)(b)）

| TC | 原 | 現 |
|---|---|---|
| S1 步驟 4 | `Read the stuck button signal on the CAN trace and check that the "not pressed" value is sent (signal name PENDING: DR-ICS8 <ICSMuteButton CAN signal>)`（25 token）| `Read the signal $CLIMATIC_PANEL.Radio_btn4$ and check that it is 0 (Not_Pressed)`（11 token）|
| S2 步驟 3 | `Keep the button pressed and read the stuck button signal on the CAN trace (signal name PENDING: …)` | `Keep the button pressed and check that $CLIMATIC_PANEL.Radio_btn4$ is 0 (Not_Pressed)` |
| S3 步驟 5 | `… and check that the button status changes on the CAN trace (signal name PENDING: …)` | `… and check that $CLIMATIC_PANEL.Radio_btn4$ toggles 1 (Pressed) then 0 (Not_Pressed)` |

**副效**：改寫後三步皆落回 §5.2 之字數帶（上繳包 01 曾具名之「PENDING 佔位使步驟
逾 18 token」隨之消失）。ER 對應行同步改為 IN §8.7.5 之觀察式。

---

## §3 作業 B — DTC 成熟條件

### 3-1 CFTS020-4819296 之逐字（`1.4.1.3.1 Integrated Center Stack (ICS) - Audio and Telematics Button Stuck`）

| ObjectID | 逐字 |
|---|---|
| 4819297 | `The ICS shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.` |
| 4819298 | `For monitor type, the ICS shall consider Continuous.` |
| 4819299 | `For monitor rate, the ICS shall consider 4 ms.` |
| 4819300 | `For limp-in action, refer to CFTS022-679.` |
| 4819301 | `The ICS shall heal the DTC after 40 ignition cycles with DTC in stored status.` |

### 3-2 DTCs Matrix 之對應條目（`DTC's in CFTS's` 第 57 列）

| 欄名 | 實值（逐字） |
|---|---|
| `DTC (J2012 Format)` | `B14DA-2A` |
| `DTC Description` | `Head Unit Button-Stuck` |
| `Lead CFTS / VF` | `CFTS020` |
| `ICS` | `X` |
| `R1L` | `X` |
| `Enable Conditions` | `CFTS020-851 description:` ⏎ `EC1: DTC Setting Enabled.` ⏎ `EC3: Local Battery Voltage within operating range (see {SIS-5161}).` |
| `Mature Criteria` | `Key is pressed and held.` |
| `Mature Time` | `120 seconds.` |
| `De-Mature Criteria` | `Key is released.` |
| `De-Mature Time` | `8 ms.` |

掃描條件：`DTC Description` 含 `tuck` 且該列任一欄含 `ICS`／`Button`／`button` 者，
全 998 列命中 4 列（r57／r60／r61／r82），其中 `Lead CFTS = CFTS020` 且 `ICS` 欄為 `X`
者**唯一**：r57。

### 3-3 S1／S2 之修訂與**一處不照下放包字面**

- **S2 增一等待步驟（照辦）**：新步驟 5 `Wait for 8 ms after the button release, which
  is the DTC de-mature time`，ER 對應一行。`8 ms` 逐字取自 `De-Mature Time`。
- **S1 未增等待步驟（不照辦，具名回報）**：`Mature Time` = `120 seconds.`、
  `Mature Criteria` = `Key is pressed and held.` —— **與 CFTS022-4914956 之門檻同為
  120 s，且量的是同一段時間**（自按下起算）。若依字面另加一等待步驟，台架會執行成
  「按住 >120 s，再等 120 s」= 240 s，**造出一個規格沒有的門檻**。
  改以步驟 2 加註承載：`Keep the button pressed for more than 120 seconds, which is
  the DTC mature time`。若分析層認為仍應另立步驟，回覆即改。
- **另增（超出下放包字面，具名）**：S1／S2／S3 之 DTC 由「the stuck button DTC」
  改為具名 `B14DA-2A`（S1 之 ER 另帶 `"Head Unit Button-Stuck"`）。
  理由：台架讀 DTC 清單時需要號碼才判得出；該號為 r57 逐字，非估算。
  下放包 §三 B.4 令「不動 S1／S2 之其餘欄位」，本改動落在 procedure／ER 之內，
  非其餘欄位；但仍超出 B.3 所述之「增一等待步驟」，故具名。

### 3-4 E3 之部分觸發

`Enable Conditions` 之 EC3 轉引 **`{SIS-5161}`**（Local Battery Voltage operating range），
**該文件不在 repo**（全 repo `.md`／`.tsv`／`.json` 掃描 0 命中，`forms/` 無同名檔）。

- 觸發部分：Enable 條件轉引第三份未在 repo 之文件（E3 之後半）。
- 未觸發部分：`Mature`／`De-Mature` 之準則與時間**自足**，作業 B 之核心可完成。
- **處置**：未將任何 Enable 條件寫入 TC（電壓範圍未知，寫入即造值），
  亦**未**落 `PENDING: DR-ICS11` —— 下放包 B.3 之佔位條件為「查無或條件不以時間表述」，
  而本案查得且以時間表述。**建議另開 DR 向上游要 `SIS-5161` 之電壓範圍**（§九）。

---

## §4 作業 C — ignore 面（b02，2 條）

落點 `generated/b02/b02_tcs.json`（sha256 `f5db81a9…`）、`generated/b02/manifest.json`。

| # | tc_title | req_id | Test Set | 錨 | design_method | priority |
|---|---|---|---|---|---|---|
| I1 | Press ignored during stuck condition | SWE-ICS-010 | Stuck Button | CFTS020-4819617 | Fault Injection | P1 |
| I2 | Button responsive after release | SWE-ICS-010 | Stuck Button | CFTS020-4819617 | Fault Injection | P1 |

- 上半 verbatim 取 4819617 **首句**（`When the HU receives … has been released`）；
  末句 `Refer to {CFTS020-479} …` 未取（§4.3.1：摘句以與測試目的直接相關者為限）。
  **`CFTS020-479` 於交付六欄之出現次數實測 0**，僅出現於 I1 之 `reasoning`（1 次）。
- 門檻二處皆 `PENDING: DR-ICS10 <Tstuck_button value>`；
  **全 8 條 TC 之交付欄中 `120` 只出現於 b01 之 S1／S2／S3（DTC 面）**，b02 為 0 —— 未挪用。
- **HU 動作以前後基線比較表述**（I1 步驟 2 記錄、步驟 5 比較；I2 步驟 4 記錄、步驟 5 比較），
  不指名具體回應：`ICSMuteButton` 之回應定義於 CFTS019（4819553 逐字：
  `When the HU receives $ICSMuteButton$ = [pressed] it shall determine the corresponding
  Volume adjustment behavior as defined in {CFTS019} …`），該文件未到（DR-ICS4），
  指名即造值（IN §8.4.1）。前後比較不需該資料（IN §5.6）。

### E4 之檢驗結果 —— **未觸發，但揭出一個更大的問題**

4819617 之三軸實測：
`ECU` = **軸不存在**、
`Radio` = `VP4R84, VP484, R1M, R1H, R1L, VP384, R1L-R`（**含 R1L**）、
`EE Architecture` = `Atlantis High, PowerNet`（**含 Atlantis High**）。

E4 之條件為「三軸實測**不含**本 DUT」—— Radio 與 EE 皆含，故**不成立**，
依 R-ICS9(c)(ii) 之明令生成。

但 `ECU` 軸不存在，而 R-ICS2 之判準以三軸交集為之。
**這不是個案**：全 CFTS020 2180 個物件中，`ECU` 軸不存在者 **1916 個（87%）**
（`Radio` 軸不存在 10、`EE Architecture` 軸不存在 11）。
依現行 R-ICS2 逐字套用，判定分佈為
**適用 28、不適用 1916、WARN-軸缺 236** —— 即 **CFTS020 中只有 28 個物件通得過三軸判準**，
而 b02 所錨之 4819617 不在其中。

**R-ICS2 之三軸判準在 CFTS020 上幾近不可用**（其為 CFTS022 之屬性形制所設）。
本包依 R-ICS9(c)(ii) 之具名授權生成 I1／I2，
**但「軸不存在時如何判適用」需要一條裁決**（§十-1）。

---

## §5 作業 D — 三面偵察（不生 TC）

報告：**`docs/reports/02_cfts020_face_recon.md`**（由 `scripts/gen_face_recon.py` 產生，
表格非人工謄寫；82 個物件列，逐物件帶 ObjectID／Artifact Type／三軸實值／判定／未命中判準）。

### 5-1 分支歸屬（下放包 §三 D.4）—— 已明測

| 節 | 物件數 | EE 實值分佈 | 判定 |
|---|---|---|---|
| `1.5`（`Functional Requirements - PNet - ICS and Associated HU`）| 132 | `PowerNet` **130**、`PowerNet, Atlantis High` 1、`All` 1 | **不適用本 DUT** |
| `1.8.1`（`ICS HMI Communication`，母節 `1.8` = `PNet & AtlHi & AtlMi`）| 71 | 皆含 `Atlantis High` 或 `PowerNet` 組合 | **適用面在此** |

`1.5` 之二個例外經逐一查證，**皆為 `Description` 型之章節引言**
（4819364 `[ECU:FPDM]`、4819365 `[EE:All][Radio:R1L, R1L-R]`），
**無一為 Subsystem Functional Requirement** → `1.5` 之需求物件 100% PowerNet-only。

**故：上繳包 01 §六-2 所列之 `1.5.1.1.2 {4819389}` 確不適用本 DUT**（下放包 §三 D.4 之待驗點）。
其 Atlantis High 對應者為 **`1.8.1.1.3 HU behavior in response to ICS SCREEN OFF
hardkey press events {4819570}`** —— 該節號**上繳包 01 未列**，為本包新測。

### 5-2 三面之材料與對應建議（**只建議不裁**）

| SWRA RD | 建議對應之 CFTS020 物件 | 何以 |
|---|---|---|
| 003（`ICS_KNOB2_DIR`）| 4819580、4819582、4819583、4819584、**4819586** | 4819586 逐字：`When the HU receives $ICS_KNOB2_DIR$ and $ICS_KNOB2_VAL$ signals it shall determine the corresponding HMI screen to 'flow' to (Browse), if any, HMI screen to update (Scroll) or change in Entertainment Audio state ('Tune')` |
| 004（`ICS_KNOB2_VAL`）| **4819583**、4819586 | 4819583 逐字載 detent 計數語意：`the ICS shall count the relative number of detents rotated through in <TPeriodToCountKnobDetents> seconds … $ICS_KNOB<n>_VAL$ = [1 to 63]` |
| 006（題 `ICSPowerButton`）| `1.8.1.1.1 {4819556}` 之 8 物件 | POWER hardkey 之 HU 回應面 |
| 007（題 `ICSScreenOffButton`）| `1.8.1.1.3 {4819570}` 之 6 物件（4819571–76）| SCREEN OFF hardkey、3 秒 `TOUCH SCREEN TO TURN ON` 計時、`$TGW_DISP_STAT$`／`$RQ_DISP_INTS$` 之送出 |
| 008（`Enter_Button`）| **4819555**（`When the HU receives $Enter_Button$ = [pressed] it shall determine the corresponding HMI screen to 'flow' to, if any`）| 全案唯一直載 Enter 行為者 |
| 009（題 `Back_Button`）| **4819554**（NAFTA 限定，`$Enter_Button$` 或 `$Back_Button$` = [pressed]）| Back 行為僅此一處直載，且其 Market 限 NAFTA |
| (011)（`HU Screen ON`）| 4819572、4819574、4819576 | 三者逐字載 `$TGW_DISP_STAT$ = [DISP_NORMAL]`／`[DISP_OFF]` 與 `$RQ_DISP_INTS$` 之送出條件 |

### 5-3 E5 之檢驗 —— **未觸發**

下放包 §三 D.5：CFTS020 是否直載 006／009 之原句，且與 SWRA 位移之判定衝突。

- **006 之 SWRA Description**（`$ICSScreenOffButton$ … Screen ON/OFF modality transition,
  3-second timeout sequence, and TOUCH SCREEN TO TURN ON operational flow`）
  之內容，直載於 **4819572**（`… until the 3 second "TOUCH SCREEN TO TURN ON" timer
  expires …`）。該內容屬 **ScreenOff**（= 007 之題），**與 A-ICS1 所判之 +1 位移相符**。
- **009 之 SWRA Description**（`… ignore corresponding actions when continuous button
  pressed status exceeds configured <Tstuck_button> timeout duration`）
  直載於 **4819617**，屬 **Stuck Button**（= 010 之題），**同樣與 A-ICS1 相符**。

即：CFTS020 **佐證**了 A-ICS1 之位移判定，**不與之衝突** → E5 之觸發條件不成立。
材料已列，是否據此依 R-ICS4 繞過 SWRA 位移，判由分析層（§十-3）。

---

## §6 預期數字對照（下放包 §5，10 項，相符者亦列）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | b01 之 DR-ICS8 佔位 | 3 → 0 | **3 → 0** | 相符 |
| 2 | b01 之 DR-ICS4 佔位 | 1 → 1 | **1 → 1**（V3 之 pre_conditions）| 相符 |
| 3 | b02 新增 TC | 2 條 | **2 條**（I1／I2）| 相符 |
| 4 | b02 之 trace | 皆 `SWE-ICS-010` | `{'SWE-ICS-010'}` | 相符 |
| 5 | b02 之錨 | 皆 `CFTS020-4819617`，不得出現 `CFTS020-479` | `{'CFTS020-4819617'}`；六欄中 `CFTS020-479` **0 次** | 相符 |
| 6 | 門檻佔位 | ≥ 1 處 `PENDING: DR-ICS10` | **2 處** | 相符 |
| 7 | S1／S2 修訂 | 各 +1 等待步驟，或各 +1 `PENDING: DR-ICS11` | **S2 +1 步驟；S1 +0 步驟（改為步驟 2 加註）** | **不符 —— §三-3** |
| 8 | 偵察面 | 3 面，逐物件三軸齊備，TC 新增 0 | 3 面、82 物件列、**TC 新增 0** | 相符 |
| 9 | Test Set 相異值 | 仍為 2（`Stuck Button`／`Volume Control`）| `['Stuck Button', 'Volume Control']` | 相符 |
| 10 | 語言 | 交付六欄與 test_item 無非 ASCII | 逐字元掃 8 條 × 6 欄，命中 **0** | 相符 |
| 11 | （下放包 §0 P3）| CFTS020 407 個相異 ObjectID | **物件 2180**（章節標題之 ObjectID 相異數為 407）| **不符 —— §1.1** |

**不符 2 項，不自行調和，理由分見 §三-3、§1.1。**

---

## §7 自檢與閘之實跑

### 7-1 `scripts/selfcheck_b01.py`（b01 + b02 合檢，8 條）

```
受檢批次：b01（6 條）、b02（2 條）
§9-1 Test Set              PASS      相異 Test Set = ['Stuck Button', 'Volume Control']
§9-2 tc_title              PASS      8 條字數 [6, 6, 5, 4, 5, 4, 5, 4]；違規 0
§4.3.1 test_item 兩段式    PASS      8 條皆有下半、皆英文；違規 0
§10.1 十鍵齊備             PASS      缺鍵 0
§10.2 priority             PASS      分佈 {'P0': 3, 'P1': 5}；越界 0
§10.5 procedure ≥2 步      PASS      步數 [4, 6, 5, 4, 4, 4, 5, 5]；違規 0
§9-10 Procedure↔ER 1:1     PASS      違規 0
§6 ER 無情態動詞           PASS      命中 0
§5.1 禁用動詞（主動詞）    PASS      命中 0
§11 無尾句號               PASS      違規 0
§11 無行首行尾空白         PASS      違規 0
§11 無方括號               PASS      違規 0
§11 UI 標籤雙引號          PASS      單引號 token 0
§10.7 spec_reference       PASS      違規 0
§12 design_method          PASS      ['Boundary Value Analysis','Fault Injection','Functional Based']
§8.4.3 PENDING 佔位        PASS      佔位 3 處，涉 3 條
§1 交付欄無非 ASCII        PASS      命中 0
§11 角括號之出現（列示）   MANUAL    5 處（見下）
§9-3／9-5／9-11／9-12／9-17            MANUAL

總判：PASS —— 機檢 17 項，FAIL 0；人工 6 項
```

**角括號 5 處，逐處具名**（新增之列示項，非 FAIL）：
`<Tstuck_button>` 於 I1／I2 之 `test_item`（4819617 逐字，R-S4 不得改字）；
`<Tstuck_button value>` 於 I1／I2 之 `test_procedure`、
`<CFTS019 volume level range>` 於 V3 之 `pre_conditions`（皆為 IN §8.4.3 之佔位語法）。
IN §11 之角括號禁例（`Press <Apps> button`）所規制者為 **UI 標籤**，
此五處非 UI 標籤 —— **列示供覆核，本包未自行認定其合規**。

### 7-2 `scripts/verify_verbatim_b01.py`（8 條逐字比對，來源三份）

```
Stuck button held over 120 s                   SWE-ICS-010   CFTS022  CFTS022-4914956
Stuck fault held until de-bounced not-pressed  SWE-ICS-010   CFTS022  CFTS022-4914957
Button held exactly 120 s                      SWE-ICS-010   CFTS022  CFTS022-4914956
VOLUME knob rotated clock-wise                 SWE-ICS-001   CFTS022  CFTS022-4914974
VOLUME knob rotated counter clock-wise         SWE-ICS-001   CFTS022  CFTS022-4914974
Three detents rotated clock-wise               SWE-ICS-002   SWRA     CFTS022-4914975
Press ignored during stuck condition           SWE-ICS-010   CFTS020  CFTS020-4819617
Button responsive after release                SWE-ICS-010   CFTS020  CFTS020-4819617

總判：PASS —— 8 條，逐字命中 8，未命中 0
```

### 7-3 四支 gate（`scripts/gate_all.py`）

| 閘 | 開工前 | 完工後 | 差 |
|---|---|---|---|
| `lint_docs036` | PASS exit 0 | PASS exit 0 | **0** |
| `canon_refs` | FAIL：474 | FAIL：**474** | **0** |
| `rulings_hash` | FAIL | FAIL | **0** |
| `gates_tsv` | FAIL | FAIL | **0** |
| `lint_paths` | FAIL：基線外 **1** | FAIL：基線外 **2** | **+1** |

**`lint_paths` 之 +1 不是本包所產**，逐筆具名：
完工後之二筆為
`features/driver_distraction/workbook/driver_distraction_00.xlsx`（開工前即紅）與
`features/driver_distraction/workbook/driver_distraction_00_bak.xlsx`（**本包執行期間出現**）。
二者皆屬 `driver_distraction`，為他 feature 之併行作業所產；
**`features/ics_management/` 之落點違規為 0**（b02 之 `.json` 落 `generated/`，
無新 `.xlsx`）。開工前之 `1` 為上繳包 01 完工時之實測值（本包開工時未另測，
此點如實揭露）。

升級說明同上繳包 01：四支之母體本包一律未觸及（禁區 4）。

---

## §8 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | b01 三處佔位改為實名訊號；S2 增 de-mature 等待步驟；S1 步驟 2 加註 mature time；三條 DTC 具名 B14DA-2A；b02 兩條 ignore 面 TC；`cfts020_probe.py`／`gen_face_recon.py` 二支新腳本；偵察報告；二份 manifest 重算 |
| **核實無誤** | LID 表頭之 c26／c28 重測與上繳包 01 相符；R-ICS1～4 之 sha8 未變；b01 之 V 組六欄未受本包影響（僅 S 組改動）；`CFTS020-479` 未入交付欄；DTCs Matrix r57 之 `ICS`／`R1L` 欄皆 `X`（本 DUT 在該 DTC 之適用範圍內） |
| **正確地不動** | V3 之 `PENDING: DR-ICS4` 未動（下放包 §三 A.4 明令）；Display／Browse／Navigation 三面 TC 新增 0（R-ICS9(e)）；ignore 面門檻未挪用 120 s（R-ICS9(d)）；`SIS-5161` 之 Enable 條件未寫入 TC（文件不在 repo，寫入即造值）；分析層四簿一字未動；`framework.md` 之 Layer 2／3 未改（R-ICS9(e)：待偵察結果再議）；未代擬任何條文 |

---

## §9 未結 DR 清單

**DR-ICS1 ~ DR-ICS10，10 條全開。** 本包之新事實：

| DR | 本包新事實 |
|---|---|
| DR-ICS4 | 仍阻 V3 一處佔位；另阻 b02 之 HU 回應指名（已以前後比較繞過，非結案）|
| DR-ICS5 | §五-1 確認 `1.5` 為 PowerNet-only、適用面在 `1.8.1`；DR 之「未提供」前提仍應更正（上繳包 01 §六-2）|
| DR-ICS6 | 003／004／008／009 之 CFTS020 對應物件已列（§五-2）；仍缺者為 HMI Logic and Flow 之畫面流本體 |
| DR-ICS7 | §三-2 佐證 DTC 面之 120 s（Mature Time 亦 120 s，二者同值互證）|
| DR-ICS8 | **佔位已解**（b01 三處），但 DR 本身**不宜逕結**：解法只覆蓋 `ICSMuteButton` 一個 LID，其餘 8 個 LID 尚未逐一驗證入 DBC |
| DR-ICS10 | b02 二處佔位待其回覆 |
| DR-ICS1／2／3／9 | 無新事實 |

**建議新開 1 條**（編號由分析層確認）：
`SIS-5161`（Local Battery Voltage operating range）—— DTC `B14DA-2A` 之 EC3 轉引，
文件不在 repo（§三-4）。阻斷面：S1／S2／S3 之 Enable 條件無法寫入 Pre-Condition。

---

## §10 待分析層裁定

1. **【最重】`ECU` 軸不存在時如何判適用**（§四）。CFTS020 2180 物件中 1916 個無 `ECU` 軸，
   R-ICS2 之三軸判準在該文件上只放行 28 個物件，而 b02 所錨之 4819617 不在其中。
   現行條文不修，`framework.md` 三面之解鎖將無法逐物件判定。
2. **R-ICS8(c) 於「同一 DBC 內多名皆查有」時之決斷**（§二-1(c)）。本包以 R-ICS2 之 ECU 軸
   ＋ DBC 發送節點取 `CLIMATIC_PANEL`，備援 `DIS_CENTERSTACK`；是否追認。
3. 是否依 R-ICS4 以 CFTS020 之直載原句繞過 SWRA 006／009 之位移（§五-3，材料已列）。
4. S1 未增等待步驟之處置（§三-3）；DTC 具名 `B14DA-2A` 是否保留。
5. `SIS-5161` 之 DR 是否開（§九）。
6. 下放包 §0 P3 之「407」與本包之「2180」，何者為 CFTS020 之物件母數（§1.1）。

---

## §11 獨立判斷：本包是否仍有該驗而未驗者

**有，五項。**

1. **`VOLUME POP_UP` 之顯示條件仍未驗**（上繳包 01 §八-3，本包未列作業，下放包 §7-7
   要求具名回報）。**本包判斷：應先於任何新 V 組 TC 處置。**
   4914974 只說 HU shall show 'VOLUME POP_UP'，未載出現時機；
   V1／V2／V3 之 ER 第 1／3 行各斷言其顯示，**三條共 6 行**皆為潛在 FF（IN §7）。
   本包實測 CFTS020 全文 `VOLUME POP_UP` 命中 **0** —— 第二來源亦解不了，
   仍繫於 CFTS019（DR-ICS4）。
2. **DR-ICS8 只解了 1/9 個 LID**（§九）。其餘 8 個 LID 之 DBC 存在性未逐一驗證，
   Display／Browse／Navigation 面一旦解鎖即需要它們。
3. **I1／I2 之 HU 動作面未真正驗到**。以前後基線比較迴避了造值，
   但「HU 狀態不變」在 stuck 情形下也可能因其他原因成立 —— 弱驗證。
   Display 面若解鎖，`$TGW_DISP_STAT$`／`$RQ_DISP_INTS$`（4819572／74／76 逐字定義）
   可給 ignore 面一個**完全可觀察**的載體，屆時 I1／I2 宜重寫。本包不越 R-ICS9(e)。
4. **`<TPeriodToCountKnobDetents>`／`<TPeriodToSendNoChange>` 未查**（4819583 逐字）。
   b01 之 V3「一次轉三格」隱含這兩個時間窗；二者於 CFTS020 皆為符號無值，
   V3 目前無佔位涵蓋此點 —— **b01 之 V3 可能少一個 PENDING**。
5. **`1.8.1.3 Button Press Events` 之 24 物件中 23 判不適用**（§五之報告），
   其中含 Short／Long Press 之定義。若 Navigation 面解鎖而該節不適用，
   008／009 將無「按壓事件」之母條可依 —— 該空缺本包只測到，未追。

---

## §12 本包引用之編號清單

R-ICS1 `3e48552b`、R-ICS2 `ad557b5d`、R-ICS3 `b10318e0`、R-ICS4 `85de9871`、
R-ICS5 `e6a4790d`、R-ICS6 `77478a91`、R-ICS7 `2c51cc80`、R-ICS8 `bf473e9c`、
R-ICS9 `7e7aa921`、R-ICS10 `a2cda337`；
A-ICS1、A-ICS6、A-ICS10；DR-ICS4、DR-ICS5、DR-ICS6、DR-ICS7、DR-ICS8、DR-ICS10；
R-G13、R-G23、R-G25；R-DD5、R-DD6 v2、R-DD9、R-DD10、R-DD13、R-DD22、R-DD23、
R-DD24、R-DD26 v2；R-BLM11；
FO §2、FO §3、FO §8.1、FO §8.2、FO §8.4、FO §8.5、FO §8.8；
IN §4.3、IN §4.3.1、IN §5.2、IN §5.5、IN §5.6、IN §7、IN §8.2.2、IN §8.4.1、
IN §8.4.3、IN §8.7.5、IN §9、IN §10.7、IN §11、IN §12。

**本包未產生任何新裁決條文。** 建議登錄之 anomaly 三則（編號由分析層取）：
§1.1（下放包 P3 之物件母數口徑）、§四（CFTS020 之 `ECU` 軸 87% 不存在，
使 R-ICS2 三軸判準在該文件上幾近不可用）、§三-4（`SIS-5161` 不在 repo）。
