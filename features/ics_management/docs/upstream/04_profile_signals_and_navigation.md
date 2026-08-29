# 上繳包 04 — profile 落檔、四訊號解佔位、Browse／Navigation 面（2026-08-29）

對應下放包：`docs/handoff/04_profile_signals_and_navigation.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `1beddf56bdf5026a52d2145c6636da0e49071a35967ef988d6ffd8ea35f767d4`**
—— 與執行層自身記錄相符，未停。

**引用體例**：依 A-ICS27③，本包引上繳包一律寫 `upstream-NN §x`。

**禁區遵守**：git 全數未執行；分析層四簿與 `ANALYSIS_LOCK.md`、`docs/handoff/**` 一字未寫
（`ledger_guard.py` 開工前／完工後**逐字相同**，見 §7-1）；009／005 之 TC 各 **0** 條；
`<Tstuck_button>`／`<TPeriodToCountKnobDetents>`／`SIS-5161` 一律未臆值；
**第 8 項新禁區遵守**：profile 內容逐字取 R-ICS18(a)(b)(c)，程式比對 `True`（§2-1）。

**並行執行**：作業 B（四訊號）與作業 D（二本偵察）以並行執行層實例進行，
可寫檔集合互斥；作業 A／C 由主實例執行。

---

## §0 量測基礎

沿 upstream-03 §0 全部條件（含第五項正規化：句首大小寫）。本包新增／自驗：

| 項 | 條件 |
|---|---|
| **profile 體例之取樣** | 落檔前所讀之現存 profile 為 **`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`**（R-DD12 之所在，R-ICS18(e) 明指之先例）。其檔頭形制為「Feature slug／Test Group／狀態／runtime 讀法／落檔註記」五行，後接 `## §n ... —— cited [OVERRIDE ...]` 之節 |
| DBC 讀取 | **`latin-1` 開檔**；訊息邊界由下一個 `BO_` 判定（A-ICS25）。以 UTF-8 讀得之「查無」不算數 |
| LID 表頭 | **本包自驗**：群組列 2（`Atlantis High` 起 c26）、欄名列 3、資料自列 4（`max_row` 2627、`max_col` 35）；五欄 c26 `Signal Name`／c27 `CAN`／c28 `Format`／c29 `SNA`／c30 `VFs`；c1 `Logical Identifier`、c31 `Usage Comment`。逐格斷言通過 |
| PDF | `pdftotext` ＋ `pdfplumber` 雙工具逐頁 ＋ 去連字號重掃。**另加壓平換行重掃**（見 §6-2 之意外）|
| 佔位計數 | 以腳本對六欄逐一 `re.findall(r'PENDING: (DR-ICS\d+) <([^>]+)>')` 計數，**非人工列舉** |

---

## §1 裁決指紋（R-ICS1 ~ R-ICS21，`R-ICS2` v1／v2 並列）

`rulings_hash.py --target features/ics_management/RULINGS.md` —— **22 錨點**（相異 ruling_id 21）。

| 條 | sha8 | 行 | 條 | sha8 | 行 |
|---|---|---|---|---|---|
| R-ICS1 | `3e48552b` | 12 | R-ICS12 | `558acc83` | 215 |
| **R-ICS2 v1** | `4a8819f0` | 25 | R-ICS13 | `273e1dbb` | 233 |
| R-ICS3 | `b10318e0` | 47 | **R-ICS2 v2** | `b6ddfe90` | 255 |
| R-ICS4 | `85de9871` | 61 | R-ICS14 | `6f9e4686` | 289 |
| R-ICS5 | `e6a4790d` | 76 | R-ICS15 | `545928c0` | 307 |
| R-ICS6 | `77478a91` | 92 | R-ICS16 | `4d0eb301` | 335 |
| R-ICS7 | `2c51cc80` | 107 | R-ICS17 | `ed8d8f0c` | 361 |
| R-ICS8 | `bf473e9c` | 125 | **R-ICS18** | `ab6dc8ea` | 393 |
| R-ICS9 | `7e7aa921` | 152 | **R-ICS19** | `1c841773` | 424 |
| R-ICS10 | `a2cda337` | 180 | **R-ICS20** | `b0e7170f` | 446 |
| R-ICS11 | `e16c88e3` | 199 | **R-ICS21** | `bf7ae107` | 469 |

**R-ICS1 ~ R-ICS17 之 sha8 與 upstream-03 §1 逐項相同** ——
**R-ICS19(b) 之圍籬 diff 程序本包無須動用**（無一不符）。
R-ICS18～21 為本輪新條，首次落其指紋。

### 1.1 前提驗證（R-DD26 v2(f)）—— **P1～P4 全部相符**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | 相異 ruling_id **21**、錨點總數 **22** | 相異 21、總數 22 | **相符** |
| P2 | A-ICS 至 **27**；DR-ICS 至 **15**，15 條全開 | A-ICS 登記列 27／相異 27／號段無缺口；DR-ICS 登記列 15／相異 15／無缺口 | **相符** |
| P3 | `holder: analysis-A`、`released: null` | 同，一致性 OK | **相符** |
| P4 | b03 八條之出貨資格已由 R-ICS18 解鎖 | R-ICS18 末句「b03 八條之出貨資格自本條解鎖」 | **相符** |

（對比 upstream-03：該輪 P1 之「17」與實測「18」不符；本輪四項全中。）

---

## §2 作業 A — profile 落檔

### 2-1 `docs/runtime/profiles/FW036_R1L_ICS_Profile.md`（新建，sha256 `2bedb33d…`）

**內容逐字性以程式驗證**：自 `RULINGS.md` 之 `## R-ICS18` 圍籬取
`(a)` 起至 `(d)` 前之片段，與 profile 圍籬內容作字串相等比較，
結果 **`True`**（非目視）。除檔頭五行與二個節標題外，**無一字為執行層所書**
（下放包 §1 禁區第 8 項）。

檔頭之「落檔註記」明載：本檔由執行層落檔，**執行層不是條文之作者**。

### 2-2 落檔前後之 `lint_paths`（E2 檢查）

| 時點 | 基線外數 |
|---|---|
| 落 profile 前 | **2** |
| 落 profile 後 | **2** |

**不增 → E2 未觸發**，未動 `PATH_POLICY_BASELINE.tsv`。
（二筆皆為 `driver_distraction` 之 `workbook/*.xlsx`，非本 feature。）
`lint_docs036 --gate` 亦仍 PASS。

### 2-3 自檢改判（R-ICS18(d)）

方括號與單引號之「上半 verbatim 列示」二項由 `MANUAL` 改判 **PASS**，
作者欄位維持硬 FAIL（實測 0）。**機檢項數 17 → 19（+2）**，與預期一致。

改判之條件寫在程式註解裡：**不是「有 profile 就 PASS」，而是「逐字對得上
cited source row」**（R-ICS18(c)）——該比對由 `verify_verbatim_b01.py` 承擔，
本項只確認保留之記法確實落在上半而非作者所書之處。

### 2-4 `feature.yaml` 增 `profile` 節

`file` 指向該檔，`sha256` 自實體檔算（`2bedb33d…`）。

---

## §3 作業 B — 四訊號 LID→CAN（DR-ICS15）

產出 `generated/b04/lid_dbc_map.json`（**累計表**：本輪 4 筆標 `b04 實測`，
b03 八筆自 `generated/b03/lid_dbc_map.json` 原樣併入並標
`沿用 b03 實測（未重新量測）` 與 `source_file`）與 `scripts/lid_dbc_probe_b04.py`。

| 訊號 | LID 列 | Atlantis High 候選 | 主路徑 | 節點 | `VAL_` |
|---|---|---|---|---|---|
| `TGW_DISP_STAT` | 2084 | `TELEMATIC_DISPLAY2.TGW_DISP_STATSts` ／ `TELEMATIC_FD_4.TGW_DISP_STATSts` | **E1，不自選** | SGW(R4 id 1500) ／ ETM(R5 id 1427) | 有（二路內容一致）|
| `RQ_DISP_INTS` | 1626 | `RADIO_B3.RQ_DISP_INTS`（**單名**）| `RADIO_B3.RQ_DISP_INTS` @R4 id **1283** | **SGW** | 有（僅 255 "SNA"）|
| `DCSD_DISP_STAT` | 420 | `DIS_CENTERSTACK.DCSD_DISP_STAT`（單名）| 同左 @R4 id **1445** | **DCSD** | 有 |
| `Telematic_Power` | 2069 | `TELEMATIC_FD_4.PowerSts_Telematic` ／ `STATUS_TELEMATIC.PowerSts_Telematic` | **E1，不自選** | ETM(R5 id 1427) ／ SGW(R4 id 1470) | 有（二路一致）|

**E5：0 筆**（四筆皆在 LID 查有且各唯一命中一列，候選在二 DBC 合計皆有命中）。
**E1：2 筆**。

### 3-1 R-ICS13 之適用性判定（逐筆，不套公式）

R-ICS13 之觸發前件為「LID 一格**多名**且綁定 DBC **皆查有**」。本包將「前件是否成立」
與「結論條款能否落地」分開判：

- **`RQ_DISP_INTS`、`DCSD_DISP_STAT` —— R-ICS13 不適用**：Atlantis High 欄為**單名**，
  前件不成立，取捨無從發生。**不套「取 ICS」**，如實記其節點為 SGW／DCSD 並判 RESOLVED。
  JSON 以 `primary_node_is_ics: false` 明標。
- **`TGW_DISP_STAT`、`Telematic_Power` —— 前件成立，結論條款落不了地**：候選皆在庫，
  卻**無一發送節點為 ICS**。R-ICS13 只規定「取 ICS 者」，未規定「無 ICS 候選時取何者」，
  且其末句明寫「非 ICS 發送而無他選者仍依 E1 停下回報」。故標 **E1、維持佔位、不自選**，
  二候選全數記入 `fallbacks`。

### 3-2 【重】二筆 E1 之性質**與 b03 那筆不同族**

b03／R-ICS13 之 E1 是「同一匯流排上 ICS 面板 vs DCSD 面板」之 **ECU 變體**取捨；
本輪二筆是**同一訊號之匯流排變體** —— `TGW_DISP_STATSts` 與 `PowerSts_Telematic`
各自在 B-CAN 與 CAN-FD 上以不同 message 承載
（LID `CAN` 欄逐字為 `CAN-B\nCAN-FD` 與 `CAN_FD\nCAN-BH`，正是兩條匯流排）。
**R-ICS13 之「取 ICS 面板」語意在此結構上沒有對應物** ——
恐非補一句「無 ICS 時取誰」即可收，請分析層留意此為新情境（§9-2）。

### 3-3 【重】ICS 在這四筆全是接收方，且三筆之接收清單不含 ICS

`STATUS_TELEMATIC.PowerSts_Telematic` 之接收節點為 `AMP,ANC,DCSD,ICS`（含 ICS）；
但 `TELEMATIC_DISPLAY2.TGW_DISP_STATSts` 收方為 `DCSD`、
`RADIO_B3.RQ_DISP_INTS` 收方為 `DCSD`、
`DIS_CENTERSTACK.DCSD_DISP_STAT` 收方為 `SGW` —— **均不含 ICS**。
若下游要以「DUT = ICS 收得到此訊號」立 TC 預期，**這三筆在 DBC 上沒有支撐**。
本包不自行判斷是否構成異常，具名回報（§9-3）。

### 3-4 LID `Format` 與 DBC `VAL_` 之字面不符（照錄，不調和）

`TGW_DISP_STAT` 之 LID Format 寫 `1= Diplay_closed`（拼字缺 `s`），DBC 為 `"Display_closed"`；
LID 列 `F= SNA`（15），而 `SG_` 宣告範圍為 `[0|14]`，`VAL_` 卻有 15="SNA"。
`DCSD_DISP_STAT` 之 `SG_` 範圍 `[0|6]` 而 SNA=7 亦超界。二邊逐字皆已存入 JSON。

### 3-5 b03 佔位之回改

**b03 之佔位實測為 15 處，不是 14**（見 §5-5）。本輪解 **3 處**（`$RQ_DISP_INTS$`），
**餘 12 處維持**（`$TGW_DISP_STAT$`，E1）。

改寫形式（P1／P2／S3 各一處）：
`Read the display intensity signal and check that it is the "0% Intensity" value (signal name PENDING: …)`
→ `Read the signal $RADIO_B3.RQ_DISP_INTS$ and check that it is 0 (0 %)`

值之書寫依 R-ICS8(d)：`VAL_ 1283 RQ_DISP_INTS 255 "SNA";` **只列舉 255**，
0–100% 為連續量（`SG_ … 55|8@0+ (0.5,0) [0|100] "%"`），
故**不為 0 自造 label**，改沿 `bed_lowering` 之連續量既例書 `= <raw> (<物理值>)`。

---

## §4 作業 C — Browse／Navigation（b04，7 條）

落點 `generated/b04/b04_tcs.json`（sha256 `b0ef699c…`）、`generated/b04/manifest.json`。
**E3 未觸發**（`4819555` 判適用）、**E4 未觸發**（`1.8.1.2` 群 **9/9 適用**）。

| # | tc_title | req_id | Test Set | 錨 | priority |
|---|---|---|---|---|---|
| B1 | Knob 2 rotated clock-wise | SWE-ICS-003 | Browse Control | CFTS020-4819583 | P0 |
| B2 | Knob 2 rotated counter clock-wise | SWE-ICS-003 | Browse Control | CFTS020-4819583 | P0 |
| B3 | Knob 2 held stationary | SWE-ICS-003 | Browse Control | CFTS020-4819582 | P1 |
| B4 | Knob 2 no change sent periodically | SWE-ICS-003 | Browse Control | CFTS020-4819584 | P1 |
| B5 | Three detents counted in one rotation | SWE-ICS-004 | Browse Control | CFTS020-4819583 | P1 |
| B6 | Knob 2 signals acted on by the HU | SWE-ICS-004 | Browse Control | CFTS020-4819586 | P0 |
| N1 | Enter button pressed | SWE-ICS-008 | Menu Navigation | CFTS020-4819555 | P0 |

### 4-1 9 個適用物件中 **4 個不生 TC**，逐一具名

| ObjectID | 理由 |
|---|---|
| 4819578／4819579 | `Description` 型章節引言（「ICS will send signals on the BH-CAN…」），無可驗行為 |
| 4819581 | 「見 LID 檔取 CAN 訊號」之指向，非行為需求 |
| 4819585 | KNOB**1** 之音量面（`ICS_Volume_Adjustment.Info`），屬 001／002 而非本批 |

### 4-2 verbatim 摘取 —— **本批全數未動用 R-ICS20**

實測各物件 token 數：`4819555` 19、`4819582` 38、`4819584` 38、`4819586` 33、
`4819580` 45 —— **皆未逾 R-3 之 50，逐字全取**。
`4819583` 為 65 token（二句 20＋45），**取整句**：
B1／B2 取**第二句**（45 token，DIR／VAL 之送出形制）、
B5 取**第一句**（20 token，detent 計數）。
**此為 IN §4.3.1 之正規摘句（整句），非 R-ICS20 之片段摘取**，
故 R-ICS20(c) 之三項限制於本批無適用之對象。

### 4-3 訊號

- `$CLIMATIC_PANEL.Radio_Knob2_DIR$`（`BO_ 1050`，節點 ICS）
  `VAL_ 1050 Radio_Knob2_DIR 0 "Knob_no_change" 1 "Knob_increment" 2 "Knob_decrement" 3 "Knob_enter";`
- `$CLIMATIC_PANEL.Radio_Knob2_VAL$`（同訊息）**無 `VAL_`**
  （`SG_ Radio_Knob2_VAL : 29|6@0+ (1,0) [0|63]`）→ 依 R-ICS8(d) **不加標籤**，書 `= 1`／`= 3`／`= 0`
- `$CLIMATIC_PANEL.Radio_btn1$`（同訊息）`VAL_ … 0 "Not_Pressed" 1 "Pressed";`

### 4-4 **E6 觸發 —— 按壓事件之定義為覆蓋缺口，未自他處補**

`1.8.1.3 Button Press Events` 之 24 物件中 23 判**不適用**，
本包逐一查其成因：**皆為 `[ECU:FPDM]`**（Front Passenger Display Module），
ECU 軸**存在**且 ∩ `{ICS, LTM}` = ∅ → v2(b)(ii) 排除。
**這是實質判定，不是軸缺** ——與 upstream-03 §3-1(f) 一致。

後果：`Short Press`（4819593 起）、`Long Press`（4819599 起，含 `<Tpress>`）之定義
本 feature **無母條可依**。N1 因此只驗 `[pressed]` 訊號值之後果，
**不涉短按／長按之區別**，亦不自他處補（下放包 §三 C-4）。

### 4-5 三處新佔位

| TC | 欄位 | DR | 缺件 |
|---|---|---|---|
| B5 | pre_conditions | DR-ICS12 | `detent counting time window` |
| B6 | test_procedure | DR-ICS6 | `HMI Logic and Flow browse, scroll and tune mapping for ICS_KNOB2` |
| N1 | test_procedure | DR-ICS6 | `HMI Logic and Flow screen mapping for Enter_Button` |

B6／N1 之錨句皆帶 `if any`（`the corresponding HMI screen to 'flow' to, if any`）
—— 明示「可能無對應畫面」。故二者之 Pre-Condition 皆限定於
「已定義該動作之畫面」，否則末步之斷言即為潛在 FF（IN §7）。

---

## §5 預期數字對照（下放包 §5，12 項，相符者亦列）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；錨點 22（相異 21）、A-ICS 27、DR-ICS 15 | exit **0**；**22（相異 21）**、**27**、**15** | 相符 |
| 2 | profile 檔 | 1 個；`lint_paths` 基線外不增 | 1 個；**2 → 2** | 相符 |
| 3 | b03 自檢 | 二項改 PASS；機檢項數 +2 | 二項 **PASS**；**17 → 19** | 相符 |
| 4 | 四訊號 | 4 個全有判，無「未查」 | **2 RESOLVED ＋ 2 E1**，E5 為 0，無「未查」 | 相符 |
| 5 | b03 之佔位 | **14** 處，依作業 B 減少 | **實測原為 15**；解 3、餘 12 | **不符 —— 見下** |
| 6 | 008 之 TC | ≥ 1 | **1** | 相符 |
| 7 | 003／004 之 TC | 依適用數，不預設 | **6**（003×4、004×2）| 相符（具名）|
| 8 | 009／005 之 TC | 0 | **0／0** | 相符 |
| 9 | Test Set 相異值 | 3 → 4 或 5 | **5**（Browse Control、Display Control、Menu Navigation、Stuck Button、Volume Control）| 相符 |
| 10 | 作業 D | 二本各一節；TC 新增 0 | 二本各一節；TC 新增 **0** | 相符 |
| 11 | `ledger_guard` 完工後 | exit 0，與開工前逐字相同 | exit **0**，`diff` **0 行** | 相符 |
| 12 | `canon_refs` | 475 → 475 | **475 → 475** | 相符 |

### 5-5 不符 1 項：**b03 之佔位實測為 15，不是 14**

以腳本對六欄逐一 `re.findall` 計數：`$TGW_DISP_STAT$` **12** 處 ＋
`$RQ_DISP_INTS$` **3** 處 = **15**。

**成因是執行層自身之誤**：`upstream-03 §13` 之 DR-ICS8 列寫「b03 有 14 處佔位」，
該數為人工估算而非腳本計數，經下放包 04 §5-5 引用而傳播。
`b03/manifest.json` 之 `counts.pending_placeholders` 亦誤記 14。
本包已於該 manifest 增 `counts_correction` 欄具名此誤，**未靜默改數**。
現值 **12** 為解 3 後之數。

---

## §6 作業 D — 二本新納偵察（R-ICS21(c)，TC 新增 0）

產出 `docs/reports/04_source_recon_2.md` 與唯讀腳本 `scripts/src_recon_04.py`。

| | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf` |
|---|---|---|
| 檔名 | 與下放包**完全一致** | 與下放包**完全一致** |
| 頁數 | **10**（`pdfinfo`／`pdftotext`／`pdfplumber` 三者一致）| **276**（三者一致）|
| 文字層 | **有**，10/10 頁 | **有**，276/276 頁 |
| sha256 前 16 | `dc078763c67b5238` | `69884c963c08cac5` |

### 6-1 【本包最重要之單一結果】`VOLUME POP_UP` 之顯示條件 —— **強查無**

`Pop Up List Priority Matrix` 10 頁全有文字層、已 100% 抽出並逐頁通讀：
**全篇不含 `VOLUME POP_UP`，連 `volume` 一字都完全不出現**
（`mute`／`duration`／`audio` 亦 0 命中）。
獨立以 `pdftotext -layout | grep -inE "volume|mute|duration|audio|vol"` 複驗，
**grep exit code = 1**。寬鬆樣式 `volume[\s_\-]*pop[\s_\-]*up`（IGNORECASE、
掃去連字號後之壓平文本）亦 0 命中。

**結構性原因**：該本是**通則文件**，全篇以類別（Cat. RVC／SL／1P／1T／2／3／X／VR）
為粒度，**不含任何個別 pop-up 之逐項清單**。

**線索（只列不判）**：p.3 逐字把逐項 timeout 外指到另一份文件 ——
> "Popups with X button which do not have a timeout defined in the **Pop-up List Notification** will have a 5 sec timeout."

**`Pop-up List Notification` 不在 `spec-index/sources/` 之 33 件內**（已對 `ls` 全表比對，
無同名近名檔）。b01 那 6 行 ER 之顯示條件若存在，最可能在這份**未入庫**文件。
另：p.8 之 Cat. X 定義與 p.10 矩陣之 "Type X remains visible in its small area till timeout"
**未點名 volume**，本包**未推定** `VOLUME POP_UP` 屬 Cat. X。

### 6-2 `HeadUnitCameraSystems` 與 (012)

前置事實：`grep -rln "SWE1-ICS-012"` 全 repo **0 命中**；
只有 `DATA_REQUESTS.md` DR-ICS2 記其「SYS2 有列、需求分頁缺列」。
**故 012 目前無需求本文可比對**，以下僅依標題字面相干性列，未判採用、未充錨：

RVC 主幹 p.22–30、**Rear View Camera 專章 p.39–49**、Tailgate Down p.60–61、
Swing Doors（含 Camera Delay OFF/ON）p.62–68；
檔位相干 p.91（FFCTL）、p.105–119（Surround View）、p.120–136（Park Sense）、
p.155–156、p.160–172／179、p.225–226；Camera Delay 彙整 p.24／25／54／64–67／111。

**三項意外**：
1. `camera transition` 複合詞 **0 命中**；`transition` 全 276 頁只有 3 頁（p.21／27／91），
   以動詞形出現（p.91 逐字：`Shifting from REVERSE to PARK, NUETRAL or DRIVE will
   transition to FFCTL`，原文 `NUETRAL` 拼字如此）。
2. **坑不是連字號而是純換行斷詞**：p.14／92／93／269 之 `rear view`
   **只在壓平文本命中、raw 不命中**（原文斷成 `Rear` / `View`）。
   下放包之警告方向正確，但實際成因不同；本包二者皆處理。
   **後續同類偵察須沿用壓平重掃。**
3. 該本 TOC 頁碼與 PDF 實際頁次**系統性不符**（TOC 在 p.16，標的為投影片原始編號）；
   報告 §3.1 併列 TOC 逐字與實抽起始頁。另其 `ModDate` 為 **2025-11-05**，
   晚於檔名之 2023-02-10 —— 只記錄不判斷。

---

## §7 自檢與閘

### 7-1 `ledger_guard.py` 開工前／完工後 —— **`diff` 0 行**，exit 皆 0

錨點總數 22（相異 21）、`R-ICS2 ['v1','v2']` 並存合法、
A-ICS 27 列／DR-ICS 15 列、號段皆無缺口、無 DUPLICATE／INCONSISTENT。
**「逐字相同」即「執行層未寫台帳」之機器證據。**

### 7-2 `selfcheck_b01.py`（b01~b04 合檢，**23 條**）

```
受檢批次：b01（6 條）、b02（2 條）、b03（8 條）、b04（7 條）
§9-1 Test Set   PASS  ['Browse Control','Display Control','Menu Navigation','Stuck Button','Volume Control']
§9-2 tc_title   PASS  23 條字數 [6,6,5,4,5,4,5,4,7,8,7,7,8,8,8,8,4,5,4,6,6,8,3]
§10.2 priority  PASS  {'P0': 11, 'P1': 12}
§11 方括號於 test_item 上半（R-ICS18(a) 例外）  PASS  13 條；作者欄位 0
§11 單引號於 test_item 上半（R-ICS18(a) 例外）  PASS  9 處；作者欄位 0
§8.4.3 PENDING 佔位  PASS  佔位 19 處，涉 14 條
（其餘機檢項全 PASS）
總判：PASS —— 機檢 19 項，FAIL 0；人工 6 項
```

### 7-3 `verify_verbatim_b01.py` —— **23 條逐字命中 23**

b04 之 7 條全數命中 CFTS020，**無一動用 R-ICS20 之片段摘取**。

### 7-4 四支 gate

| 閘 | 開工前 | 完工後 | 差 |
|---|---|---|---|
| `lint_docs036` | PASS | PASS | **0** |
| `canon_refs` | FAIL：475 | FAIL：**475** | **0** |
| `rulings_hash` | FAIL | FAIL | **0** |
| `gates_tsv` | FAIL | FAIL | **0** |
| `lint_paths` | FAIL：基線外 **2** | FAIL：基線外 **2** | **0** |

`lint_paths` 二筆逐筆具名：`features/driver_distraction/workbook/driver_distraction_00.xlsx`
與 `…_00_bak.xlsx` —— **皆屬 `driver_distraction`，`ics_management` 之落點違規為 0**。
本包新落之 `docs/runtime/profiles/FW036_R1L_ICS_Profile.md` 未使該數增加。

---

## §8 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | profile 落檔（逐字性程式驗證 True）；自檢二項改判＋機檢 +2；`feature.yaml` 增 `profile` 節；四訊號對照＋累計表；b03 三處佔位解為 `$RADIO_B3.RQ_DISP_INTS$`；b04 七條；二本偵察報告；`lid_dbc_probe_b04.py`／`src_recon_04.py` 二支新腳本 |
| **核實無誤** | R-ICS1~17 之 sha8 與 upstream-03 逐項相同（R-ICS19(b) 無須動用）；LID 表頭自驗與前包相符；`4819555` 與 `1.8.1.2` 群 v2 判適用；`1.8.1.3` 之 23 不適用成因為 `[ECU:FPDM]` 實質判定（非軸缺）；b04 七條之上半皆未逾 R-3，**未動用 R-ICS20** |
| **正確地不動** | `$TGW_DISP_STAT$` 12 處佔位維持（E1，不自選）；009／005 各 0 條；`_VAL` 無 `VAL_` 故不加標籤；`RQ_DISP_INTS` 之 0 不自造 label；`<TPeriodToSendNoChange>` 未臆值（B1／B2 之 2 秒明記為測試實作選擇）；按壓事件定義不自他處補（E6）；`Pop-up List Notification` 未推定其內容；Cat. X 未推定含 volume；分析層五簿一字未寫；未代擬任何條文 |

---

## §9 待分析層裁定

1. **【最重】`$TGW_DISP_STAT$` 之 E1（§3-2）**：其為**匯流排變體**（B-CAN vs CAN-FD）
   而非 ECU 變體，R-ICS13 之「取 ICS 面板」語意無對應物。
   **b03 之 12 處佔位、Display 面八條之訊號面驗證強度，全繫於此。**
2. **三筆訊號之 DBC 接收清單不含 ICS（§3-3）**：若 TC 預期為「ICS 收得到」，DBC 無支撐。
   此問題是否構成異常、是否影響 b03 之 ER 立論。
3. **`Pop-up List Notification` 不在 repo（§6-1）**：建議新開 DR 向上游索取
   —— 這是 `VOLUME POP_UP` 顯示條件連續四包追索後**唯一剩下的線索**。
4. `Telematic_Power` 之 E1（同 §3-2 之結構）。
5. LID `Format` 與 DBC `VAL_` 之字面不符與範圍越界（§3-4）是否登異常。
6. b03 佔位數之誤（14 vs 15，§5-5）之登錄方式。
7. `1.8.1.3` 之按壓事件定義缺口（§4-4）：是否向上游要 ICS 側之等價條文，或裁定
   本 feature 不驗短按／長按之區別。

---

## §10 獨立判斷

### 10-1 【下放包 §7-7 指定】Browse／Navigation 二組是否應合併

IN §4.1.3 之判準：filter 該 Test Set 須得 **meaningful cluster** ——
「**不只一條**，也不是整本」；健康徵候為「共用之 setup pattern 與共用之 UI entry path」。

現況：**Browse Control 6 條**、**Menu Navigation 1 條**。

**建議：不合併，但 Menu Navigation 現況不合格，其解在 DR-ICS13 而非合併。**

- **不合併之理由**：二者 entry path 不同（旋鈕 vs 按鍵），
  setup pattern 亦異（B 組須先進入有 browse 行為之列表畫面；N 組只需有 Enter 動作之畫面）。
  依 §4.1.3 之健康徵候，合併會製造一個「共用不了 setup 也共用不了 entry path」的組。
- **但 Menu Navigation 現為 1 條，字面上正踩 §4.1.3 之 "not just one TC"**。
  其成因**不是分組太細，而是 009 被 R-ICS15(b) 凍結**（DR-ICS13 未回）。
  009 解凍後該組會有 Back 鍵之 TC，屆時即成 cluster。
  **在 DR-ICS13 未回前合併，是拿分組手段去補一個資料缺口** —— 治錯了病。
- 若 DR-ICS13 回覆確認 009 出案外（Market 限 NAFTA 而本專案非 NAFTA），
  屆時 Menu Navigation 將永久只有 008 一條，**那時才是合併的時機**；
  可併入 Browse Control 並更名為涵蓋二者之名（如 `Knob and Button Navigation`）。

### 10-2 本包是否仍有該驗而未驗者 —— **有，六項**

1. **`$TGW_DISP_STAT$` 未解 → Display 面八條之訊號面仍是佔位**（§9-1）。
   b03 八條目前**只有按鍵側訊號（`Radio_btn0`／`btn2`）是實名的**，
   顯示狀態側全是佔位 —— 該八條之驗證強度低於其外觀。
2. **B1／B2 之「轉動後 2 秒」是測試實作選擇，非規格值**。
   `<TPeriodToSendNoChange>` 於 CFTS020 為符號無值；
   **若上游回覆之 T2 大於 2 秒，該二條之步驟 4／5 必須改**。
   本包未為此落佔位（該值不影響「送什麼」，只影響「何時觀察」），但風險已具名。
3. **B3 之「VAL 被忽略」以「畫面不變」承載，是弱驗證**。
   條文之 `ignored by the receiving components` 是「不做事」，無直接訊號面可觀察。
4. **`Pop-up List Notification` 未取得 → b01 之 6 行 ER 仍懸**（§6-1）。
   本包已把 CFTS 系列（022／020／019）與 HMI L&F 六本掃遍，
   **線索首次收斂到一份具名而未入庫之文件** —— 這是四包以來最實質的進展，
   但它同時意味著**再掃 repo 內任何文件都不會有答案**。
5. **012（Camera Transition）之需求本文仍缺**（`SWE1-ICS-012` 全 repo 0 命中）。
   `HeadUnitCameraSystems` 有 276 頁材料，卻**沒有需求可比對** ——
   upstream-03 §12-1-3 建議該組自 Layer 2 移出，本包實測支持該建議。
6. **`ICS_KNOB1_VAL`／`ICS_KNOB2_VAL` 無 `VAL_` 一事之下游效應未驗**：
   b01 之 V3 與 b04 之 B5 皆斷言 `= 3`，其正確性繫於 detent 計數窗（DR-ICS12），
   而該窗未回。**二條 TC 之數值面目前無法在台架上判定對錯。**

---

## §11 未結 DR 清單

**DR-ICS1 ~ DR-ICS15，15 條全開。** 本包之新事實：

| DR | 新事實 |
|---|---|
| DR-ICS1 | 阻斷面續縮：008 已由 R-ICS15(a)／本包解鎖，**現僅阻 005** |
| DR-ICS2 | 012 之需求本文全 repo 0 命中；`HeadUnitCameraSystems` 276 頁材料已定位但無需求可對 |
| DR-ICS4 | b01 之 6 行 ER 線索收斂至 `Pop-up List Notification`（不在 repo）|
| DR-ICS6 | b04 新增二處佔位（B6／N1）待其回覆 |
| DR-ICS8 | **9/9 個 ICS LID 已解**；四訊號中 2 解 2 為 E1，**不宜逕結** |
| DR-ICS12 | b04 之 B5 新增一處佔位（連同 b01 之 V3 共二處）|
| DR-ICS13 | Menu Navigation 之組別存續繫於此（§10-1）|
| DR-ICS15 | **本包之標的**：2 解（`RQ_DISP_INTS`／`DCSD_DISP_STAT`）、**2 維持佔位**（E1）|
| DR-ICS3／5／7／9／10／11／14 | 無新事實 |

**建議新開 1 條**（編號由分析層取）：`Pop-up List Notification`（§6-1、§9-3）。

---

## §12 本包引用之編號清單

R-ICS1 `3e48552b`、R-ICS2 v1 `4a8819f0`、R-ICS3 `b10318e0`、R-ICS4 `85de9871`、
R-ICS5 `e6a4790d`、R-ICS6 `77478a91`、R-ICS7 `2c51cc80`、R-ICS8 `bf473e9c`、
R-ICS9 `7e7aa921`、R-ICS10 `a2cda337`、R-ICS11 `e16c88e3`、R-ICS12 `558acc83`、
R-ICS13 `273e1dbb`、R-ICS2 v2 `b6ddfe90`、R-ICS14 `6f9e4686`、R-ICS15 `545928c0`、
R-ICS16 `4d0eb301`、R-ICS17 `ed8d8f0c`、R-ICS18 `ab6dc8ea`、R-ICS19 `1c841773`、
R-ICS20 `b0e7170f`、R-ICS21 `bf7ae107`；
A-ICS1、A-ICS5、A-ICS21、A-ICS22、A-ICS25、A-ICS27；DR-ICS1 ~ DR-ICS15；
R-G13、R-G18、R-G23、R-G25；R-DD12、R-DD26 v2；R-TM13；
FO §8.2、FO §8.4、FO §8.5、FO §8.8；
IN §4.1.3、IN §4.3、IN §4.3.1、IN §4.4、IN §5.7、IN §7、IN §8.2.2、IN §8.3、
IN §8.4.1、IN §8.4.3、IN §9、IN §10.7、IN §11、IN §12。

**本包未產生任何新裁決條文。**
建議登錄之 anomaly 五則（編號由分析層取）：
§3-2（E1 之匯流排變體，R-ICS13 語意無對應物）、
§3-3（三筆訊號之 DBC 接收清單不含 ICS）、
§3-4（LID Format 與 DBC VAL_ 之字面不符與範圍越界）、
§5-5（執行層自身之佔位計數誤 14／15 之傳播）、
§6-2（PDF 換行斷詞之漏命中，非連字號）。
