# RULINGS — ICS Management (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。前綴 `R-ICS` / `A-ICS` / `DR-ICS`，
不與既有 feature 共用序號。取號依 R-G23：落檔當下 grep 本檔與
`docs/handoff/` 全目錄，不得自記憶推定。

來源：2026-08-29 chat 偵察報告＋分析層判斷四項，Pei 同日「准」
（①命名 ②DR-ICS1~9 即發 ③首波動工面 ④落檔骨架）。

---

## R-ICS1

```
R-ICS1（feature 命名）

slug = `ics_management`，Test Group = `ICS`。
依據：三份來源檔名／題名均為 ICS Management／ICS Buttons Management，
「Integration」於全部來源零命中；IN §4.1.1 Layer 1 取 spec 題名。
Pei 口頭之「ICS Intergration」判為代稱，不入檔。
```

---

## R-ICS2 v1

> **已被 R-ICS2 v2 取代（2026-08-29，分析層，A-ICS18）。**
> 依 R-TM13 不刪不改，下文僅供沿革查考，**其所載之判準不得引用**。
> 失效值：未分來源文件之屬性形制，將依 CFTS022（跨 ECU 文件）所設之
> 三軸交集施於 CFTS020（ICS 專屬文件，87% 物件無 ECU 軸），
> 致 2180 物件只放行 28。

```
R-ICS2（CFTS022 適用域，暫定）

CFTS022 物件適用判準：ECU ∋ {ICS, LTM} ∧ Radio ∋ {R1L, R1L-R, allSys}
∧ EE ∋ {Atlantis High, All}。

{ICS, LTM} 聯集為暫定：Stuck Button 物件 ECU 列 ICS，Volume 物件
（4914972–76）僅列 LTM/ETM/RRM，而 DUT 實為 HU 側軟體（SYSAD 通篇
AAOS14 HU 棧）。邊界由 DR-ICS9 上游確認；裁定收窄時，受影響 TC
以 A- 登冊回收，不靜默改判。
```

---

## R-ICS3

```
R-ICS3（Tstuck_button 首波取值，暫定）

<Tstuck_button> 首波採 120 秒，來源 CFTS022 物件 4914956（HU 側，
ECU 明列 ICS，Radio allSys，EE 含 Atlantis High）。
SCCM 側之 10 分鐘（4914954）不適用本 DUT。
SWRA 所稱「configured」之組態值由 DR-ICS7 上游確認；
確認值異於 120 s 時回收修正。非造值（IN §8.7.1 spec-sourced）。
```

---

## R-ICS4

```
R-ICS4（verbatim 來源分流：SWRA Description 錯置期間）

A-ICS1 五列（001/005/006/009/010）之 SWRA Description 不得作
test_item 上半之 verbatim 來源。依 IN §8.6（來源 spec 勝過索引輸出），
凡 CFTS022 有直載原句者（現況：010 之 4914955/56/57；001 之 4914975/76），上半 verbatim
取 CFTS022 原句，specification_reference 錨 CFTS022-{ObjectID}；
CFTS022 無載者（005/006/009）俟 DR-ICS1 回覆，不得動工。
未受錯置之列（002/003/004/007/008）仍以 SWRA Description 為上半來源。
```

---

## R-ICS5

```
R-ICS5（b01 落點之採認）

執行層依 R-G25 落 `sandbox/`（.xlsx）與 `generated/b01/`（.json），
採認為本 feature 之定制落點；下放包 01 §一-1 之 `workbook/`／`batches/`
字面作廢。依據：lint_paths.py 實跑（字面落點 → 基線外 4，全為本 feature
新件；改落後 → 基線外 1，該 1 筆為開工前即紅之他 feature 檔）；
PATH_POLICY_BASELINE.tsv 之列為既存違規之凍結，非新件之許可。
落點基線不改 —— 版控政策屬 Tier 3，Pei 未裁前不動。
（分析層即裁，2026-08-29；下放包 01 之落點指定誤已登 A-ICS10）
```

---

## R-ICS6

```
R-ICS6（b01 priority 之採認）

S1 = P0 採認：TEST_CASE_PRIORITY.md「CAN 測試案例分級 P0」第 5 項
（系統異常時 DTC 正確回報診斷工具）字面命中。下放包 01 §三範式之 P1
為示例值，§二「依 TEST_CASE_PRIORITY.md 自判」為現行指令；
二者衝突時後者勝，執行層之取捨與具名回報（上繳包 01 §四-4）合式。
V1/V2 = P0（audio output 主流程）、S2/S3/V3 = P1，一併採認。
（分析層即裁，2026-08-29）
```

---

## R-ICS7

```
R-ICS7（Description 型物件之充錨資格，暫定）

CFTS 物件 Artifact Type = Description 者，得充 specification_reference
之錨，限於「所驗行為之原句僅存於該 Description 型物件」時；
該 TC 之 reasoning 須註明所錨物件之型別。S2 之雙錨
（4914957 + 4914958）維持。
依據：IN §10.7 未限 Artifact Type；privacy 既有交付無 Description 錨，
實測其所驗原句皆在 SFR 型物件，屬無此需求，非禁例。
本條為分析層暫裁，Pei 若另裁「否」：S2 改單錨 4914957，
清除面之驗證轉 DR 向上游要 SFR 級條文。
（分析層即裁，2026-08-29；上繳包 01 §六-5）
```

---

## R-ICS8

```
R-ICS8（DR-ICS8 之解法路徑：LID→CAN，R-DD5／R-DD6 v2／R-DD13 同族）

(a) 對照權威 = `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`
    之 `CAN Mapping` 分頁。依據：CFTS020 物件 4819547 逐字令取
    latest version，v1_78 為 repo 內實測最新；driver_distraction
    所綁之 v1_76 不承接（其綁定繫於該 feature 之 R-DD5，非全域）。
(b) 架構欄取 Atlantis High（R-DD6 v2 同理由：可施加性）。
(c) 一格多名（如 ICSMuteButton 之 CLIMATIC_PANEL／GW_B_5／
    DIS_CENTERSTACK 並列）沿 R-DD13：綁 vehicle_setting/inputs 之
    PDT27_E2A_R4_BHCAN.dbc、PDT27_E2A_R5_FDCAN8.dbc 原件
    （sha256 自實體檔重算），先以綁定 DBC 篩，查有者取之；
    查無者依 IN §8.7.5(d)(g) 保留 LID 名、不加 $、記備援、
    DR-ICS8 續開追蹤。
(d) 訊號值書寫沿 R-DD9 同族：有列舉者逐字取之
    （如 = 1 (Pressed)、= 0 (Not_Pressed)）。
(e) 本條僅及觀察／記錄步驟之訊號名；刺激面維持實體按壓／旋轉步驟
    （CFTS020-479 所指之 physical button press signals 為 HU 之受信面）。
(f) b01 三處 PENDING 之改寫由執行層於 b02 依本條實測後為之，
    分析層不代填名。
（分析層即裁，2026-08-29；上繳包 01 §六-4）
```

---

## R-ICS9

```
R-ICS9（CFTS020 納為第二來源，及 SWE-ICS-010 範圍之擴充）

(a) `inputs/R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD_20260310-1533.docx`
    納為本 feature 之第二來源母文件，地位同 CFTS022：得作
    test_item 上半之 verbatim 來源，得作 specification_reference 之錨
    （式為 `CFTS020-{ObjectID}`，IN §10.7(a)）。
    區別於 SYSAD —— SYSAD 為 SWE.2 側架構文件，仍不得入 TC
    任何欄位（R-DD4 同理）。
(b) 適用判斷同 R-ICS2 之三軸（ECU／Radio／EE），逐物件實測，
    不得以章節標題之屬性代替子物件之屬性。
(c) SWE-ICS-010 之範圍擴充為二行為面：
    (i) DTC 面（CFTS022-4914956／57／58）—— b01 已涵蓋；
    (ii) ignore 面（CFTS020-4819617）—— 即 SWRA 010 之 Verification
         Criteria 本體，b02 補寫。
    二面同 trace SWE-ICS-010（IN §8.2.2：RD sub-id ≠ TC 數）。
(d) 二門檻不得互代：R-ICS3 之 120 s 僅治 DTC 面；ignore 面之
    `<Tstuck_button>` 無數值，一律 `PENDING: DR-ICS10 <…>` 佔位，
    不得挪用 120 s（造值，IN §8.4.1）。
(e) Display／Browse／Navigation 三面之解鎖：b02 只做偵察，
    不生 TC；framework Layer 2／3 之修訂待偵察結果出來再議。
（Pei 2026-08-29 裁定，「准」；上繳包 01 §六-2／六-3／八-1）
```

---

## R-ICS10

```
R-ICS10（外部素材之綁定形式，追認）

CFTS022 之實體維持綁
`features/privacy/inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional
Specification_20250910_1708.docx` 原件（sha256 自實體檔重算），
**不複製入本 feature inputs/**。同理適用於
`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`、
`forms/DTCs Matrix Core List Rev. 1.6.xlsx`、
及 R-ICS8(c) 所綁之二 DBC。
理由同 R-BLM11：原件變動才是要偵測之事件；複本只會點斷該偵測。
綁定登於 `feature.yaml` 之 `reference` 節，逐件帶 sha256。
（Pei 2026-08-29 追認，「准」；執行層已先行於上繳包 01 §六-1）
```

---

## R-ICS11

```
R-ICS11（CFTS019 納源）

CFTS019（volume 母文，SWE-ICS-001/002 之 Description 明引）納為本
feature 來源，綁 `features/audio_mgmt/inputs/` 原件（R-ICS10 式，
不複製；sha256 自實體檔重算）。何件為現行版俻 DR-ICS4 上游確認；
確認前得先偵察（音量階數域、VOLUME POP_UP 顯示條件之所在），
偵察所得只入報告不入 TC，俟版本確認後方得充 verbatim 來源與解
`PENDING: DR-ICS4` 佔位。
（Pei 2026-08-29 裁定，「裁」；A-ICS12）
```

---

## R-ICS12

```
R-ICS12（CFTS022 版本雙軌之收口）

(a) 26PI2.5_20260608-1205 之 CFTS022 真 docx 由 Pei 置入
    `features/ics_management/inputs/`（素材補入屬 Pei）。
(b) 落檔後，本 feature 之 CFTS022 綁定自 privacy 原件（25PI3.5）
    改綁本 feature inputs/ 之新版；privacy 自身之綁定不動（他轄）。
(c) 改綁同時，b01 所用之 4 句 verbatim（4914956/57/75/76）與
    所錨 6 物件（另含 4914958/74）之屬性三軸須於新版逐字覆驗；
    不符即停並報（A-ICS13 升級）。
(d) 落檔前，b01 之錨維持現狀（舊版實測命中，非缺陷）。
（Pei 2026-08-29 裁定，「裁」；A-ICS13）
```

---

## R-ICS13

```
R-ICS13（下放包 02 E1 之預解：多名皆在 DBC 時之取捨）

實測（2026-08-29，PDT27_E2A_R4_BHCAN.dbc）：
`BO_ 1050 CLIMATIC_PANEL: 8 ICS`（發送節點 ICS）含 Radio_btn0–4、
Radio_Knob1/2 之 DIR/VAL 全訊號及 VAL_ 列舉；
`BO_ 1445 DIS_CENTERSTACK: 8 DCSD`（發送節點 DCSD）亦在庫。

裁定：LID 一格多名且綁定 DBC 皆查有時，取**發送節點 = ICS**
之訊息（即 CLIMATIC_PANEL.*）為主路徑 —— 本 feature 之 DUT 受信面
為 ICS 實體面板，DIS_CENTERSTACK 為 DCSD 變體之對應，記備援
（R-DD13 之備援欄位），不入 TC。GW_B_5 訊息在庫但無
Mute_Button 訊號（grep 0 命中），不充候選。
下放包 02 之 E1 自本條生效起不再成立；執行層仍須逐訊號實測
發送節點，非 ICS 發送而無他選者仍依 E1 停下回報。
（分析層即裁，2026-08-29）
```

---

## R-ICS2 v2

```
R-ICS2 v2（適用域：依來源文件之屬性形制分流）

取代 v1。成因見 A-ICS18（上繳包 02 §四實測）。

(a) **CFTS022（跨 ECU 文件，全物件帶 ECU 軸）**：維持 v1 之三軸交集
    ECU ∈ {ICS, LTM} ∧ Radio ∈ {R1L, R1L-R, allSys}
    ∧ EE ∈ {Atlantis High, All}。ECU 邊界仍由 DR-ICS9 確認。

(b) **CFTS020（ICS 專屬文件，題名 ICS and DCSD）**：ECU 非區別軸。
    判準為：
      (i)  Radio ∈ {R1L, R1L-R, allSys} ∧ EE ∈ {Atlantis High, All}；
      (ii) ECU 軸**存在時**須含 {ICS, LTM}（如 4819364 之 [ECU:FPDM]
           即排除）；**不存在時不視為不適用**，亦不記 WARN
           —— 該軸於本文件本不作區別之用。
(c) 章節分支（如 1.5 = PNet-only、1.8 = PNet & AtlHi & AtlMi）為
    **輔證**：得用以解釋判定、得用以發現可疑之判定，
    **不得取代逐物件實測**（R-ICS9(b) 不變）。
    實例：1.5 之 132 物件中 130 為 PowerNet、餘二皆 Description 型
    章節引言 —— 故 1.5 之需求物件 100% 不適用，
    上繳包 01 §六-2 所列之 1.5.1.1.2 {4819389} 確不適用；
    其 Atlantis High 對應者為 1.8.1.1.3 {4819570}。
(d) 上繳包 02 §五之 82 物件判定、§十一-5 之「1.8.1.3 之 24 物件
    中 23 不適用」皆為 v1 判準下之結果，**一律作廢**，
    於 b03 依 v2 重判並重出偵察報告。
(e) b02 所錨之 4819617（ECU 軸缺、Radio 含 R1L、EE 含 Atlantis High）
    依 v2(b) 判**適用** —— 與 R-ICS9(c)(ii) 之授權一致，I1／I2 無需回收。
（分析層即裁，2026-08-29；上繳包 02 §四／§五-1）
```

---

## R-ICS14

```
R-ICS14（訊號取捨之明文追認）

追認執行層之取捨：`ICSMuteButton` 取 `CLIMATIC_PANEL.Radio_btn4`（DBC
發送節點 = ICS），`DIS_CENTERSTACK.DCSD_Mute` 記備援，
`GW_B_5.Mute_Button` 因 DBC 無該訊號而落。

註：同一判準已於同日落為 R-ICS13，但執行層所取之下放包 02
快照未含該條（A-ICS14）。執行層以 R-ICS2 之 ECU 軸 ＋ DBC
發送節點獨立推得同一結果，二路徑收於一點，無實害。
R-ICS13 為現行條文；本條僅作追認。
（分析層即裁，2026-08-29；上繳包 02 §二-1(c)、§十-2）
```

---

## R-ICS15

```
R-ICS15（以 CFTS020 繞過 SWRA 位移：R-ICS4 之適用）

實測（上繳包 02 §五-3）：CFTS020 直載之原句與 A-ICS1 之 +1 位移
判定**相符而非衝突**（006 之 Description 內容直載於 4819572，
屬 ScreenOff；009 之 Description 內容直載於 4819617，屬 Stuck Button）。
E5 未觸發。

裁定：
(a) 006（題 ICSPowerButton）與 007（題 ICSScreenOffButton）**解鎖**：
    上半 verbatim 改取 CFTS020 直載原句（006 → 1.8.1.1.1 {4819556} 群；
    007 → 1.8.1.1.3 {4819570} 群），不再等 DR-ICS1。
    依據：IN §8.6（來源 spec 勝過索引輸出）與 R-ICS4。
(b) 009（題 Back_Button）**不解鎖**：其唯一直載原句 4819554 之
    Market 限 NAFTA，而本專案之市場軸未經量測。登 DR-ICS13；
    未回前不得生成（R-DD25 同族：不得以「有原句」充「在案」）。
(c) 005（題 ICSMuteButton）**不解鎖**：CFTS020 無直載，
    CFTS022 2.2.2 {4914991} 適用性未驗，SWRA 原句為唯一候選
    且已判位移，繼續等 DR-ICS1。
(d) 解鎖者之 Test Set 歸屬依 framework 不變，不因來源改變而重分。
(e) 解鎖後之適用性判定一律依 **R-ICS2 v2(b)**，不得沌 v1。
（分析層即裁，2026-08-29；上繳包 02 §五-2、§五-3、§十-3）
```

---

## R-ICS16

```
R-ICS16（S1 等待步驟之處置與 DTC 具名，採認）

(a) **S1 不另增等待步驟，採認**。DTCs Matrix r57 之
    `Mature Criteria` = `Key is pressed and held.`、
    `Mature Time` = `120 seconds.` —— 與 CFTS022-4914956 之門檻
    量的是同一段時間（自按下起算）；另立等待步驟將使台架
    執行成 240 s，造出規格未載之門檻（IN §8.4.1）。
    以步驟 2 加註承載為正解。**下放包 02 §三 B.3 之字面
    （「S1／S2 各＋1 等待步驟」）於 S1 作廢** —— 分析層書該
    字面時未先量 mature 與 DTC 門檻是否同一時段（A-ICS19）。
(b) S2 增 `Wait for 8 ms after the button release` 採認
    （`De-Mature Time` = `8 ms.` 逐字）。
(c) DTC 具名 `B14DA-2A`（及 S1 ER 之 `"Head Unit Button-Stuck"`）
    **保留**。逐字取自 r57，非估算；台架讀 DTC 清單需號碼方
    判得出（IN §5.1 之「具體可觀察標的」）。執行層之超出字面
    已具名回報，合式。
(d) `SIS-5161` 之 Enable 條件未寫入 TC，採認（文件不在 repo，
    寫入即造值）。已登 DR-ICS11。
（分析層即裁，2026-08-29；上繳包 02 §三-3、§三-4、§十-4、§十-5）
```

---

## R-ICS17

```
R-ICS17（分析層台帳之單一寫者協定）

成因：A-ICS20 —— 2026-08-29 同日有二個分析層實例實際寫入
`RULINGS.md`。本次未撞號屬僥倖（v2 不佔新號），不得視為安全。

(a) **權杖**：`features/ics_management/ANALYSIS_LOCK.md` 為唯一權杖。
    其 `scope` 所列五類檔（RULINGS／ANOMALIES／DATA_REQUESTS／
    framework／docs/handoff/*.md）僅持有者得寫。
(b) **非持有者**一律改寫提案於 `docs/handoff/proposals/NN_<slug>.md`，
    條文全文＋量測依據，編號寫 `R-ICS?`，**不自取號**。
    持有者合併時取號、落檔、並於 ANOMALIES 記其來源。
(c) **落檔三步**（持有者亦須遵）：
    (i)   寫前 live grep `^## R-ICS` 取現行最大號（R-G23）；
    (ii)  寫入；
    (iii) **寫後回讀驗證**（read-after-write）—— 確認所寫存在且
          無重號。MCP timeout 後先 `get_file_info` 再重試（既例）。
(d) **附加制**：已落之條文不刪不改字（R-TM13）。需修訂者另立
    `R-ICSn vN+1` 並將舊條改題為 `R-ICSn vN`；改題本身須於
    ANOMALIES 具名。
(e) **下放包不得原地追寫**（A-ICS14 之拿法）：已下放之包若需補充，
    另發 NN+1。執行層開工前須重測 handoff 之 sha256 並入上繳包；
    與包內所載不符即停並報。
(f) **驗證工具**：`scripts/ledger_guard.py`（b03 作業 A）。
    每份上繳包須附其開工前／完工後二次實跑輸出。
（分析層即裁，2026-08-29；A-ICS20）
```

---

## R-ICS18

```
R-ICS18（IN §11 Exception 之啟用：本 feature profile）

成因：A-ICS22。IN §11 之方括號／引號 Exception 為 profile-scoped，
而本 feature 無 profile（執行層實測 `docs/runtime/profiles/` 無 ICS 檔），
致 b03 八條之出貨資格懸置。

(a) 本 feature 啟用 IN §11 Exception，範圍限定於：
    `test_item` **上半**之 verbatim 段落，及 ER 中以
    `... as defined by CFTS0xx-{ObjectID} ...` 式引註之引句段落。
    保留之記法包含來源自身之方括號（`[DISP_OFF]`、`[DISP_NORMAL]`、
    `[0% Intensity]`、`[current non-zero value]`、`[Idle]`）與單引號
    （`'HU Screen ON'`、`'HU Screen OFF'`）。
(b) **作者自書之文字不適用本例**：procedure 之按鍵標的、非引句之
    ER 行、pre_conditions、input_test_data 一律用 `"..."`（IN §11 本文）。
(c) **驗證方式**：保留之 token 須能於所錨之 cited source row 逐字對上
    （IN §11 Exception 本文之 lint 規定）。本 feature 之對比器為
    `scripts/verify_verbatim_b01.py`；對不上即為違規，不得以本條免責。
(d) 自檢之分流（作者欄位硬 FAIL／上半 verbatim 列示）**採認**；
    自本條生效起，上半之列示項改判 **PASS**，不再標 MANUAL。
(e) 下放包 04 令執行層落 `docs/runtime/profiles/FW036_R1L_ICS_Profile.md`，
    內容逐字取本條 (a)(b)(c)，並標 cited `[OVERRIDE IN §11]`。
    先例：driver_distraction R-DD12（同一件事，同一驗證方式）。
b03 八條之出貨資格自本條解鎖。
（分析層即裁，2026-08-29；上繳包 03 §四-4(b)(c)、§十-2）
```

---

## R-ICS19

```
R-ICS19（R-G13 指紋與 R-ICS17(d) 改題之交互）

成因：A-ICS21。依 R-ICS17(d) 正確改題之條文，其 sha8 必然改變
（`R-ICS2 v1`：`ad557b5d` → `4a8819f0`，而圍籬內容 diff 0 行），
而 R-G13 之設計為「sha 不符即停下」—— 二條直接衝突。

(a) **不改 `rulings_hash.py`**（全域工具，改之影響十餘本之基線）。
(b) 引用之 sha8 不符時，**先取圍籬內容 diff**：
    diff 為 0 行 → 條文未變，**不停**，於上繳包具名新舊 sha8；
    diff 非 0 行 → 條文已變，依 R-G13 停下並報。
(c) 改題之人須於 ANOMALIES 登新舊 sha8 對照（本件見 A-ICS21），
    使舊包之引用可回溯。
(d) 本條之適用限於「改題與作廢註記」所致之指紋變動；
    條文本體改字仍屬 R-TM13 禁區，不得援引本條。
（分析層即裁，2026-08-29；上繳包 03 §1.1、§十-1）
```

---

## R-ICS20

```
R-ICS20（R-3 上限與 CFTS020 單句長度之衝突：摘取法採認）

CFTS020 多條為單一長句（`4819560` 66 token、`4819561` 54、
`4819572` 66），無次句可摘，而 R-3 上限 50 token。

採認執行層之摘取法：
(a) 取後半**獨立子句之連續逐字片段**（`then the HU shall …` 起），
    句首依 R-4 轉大寫（排版正規化，允許）。
(b) 前提子句改由 Pre-Condition 與括號下半承載，
    全文以 `specification_reference` 指回（R-S4 本旨）。
(c) **限制**：只得取**連續**片段，不得跨句拼接、不得刪中間字。
    所取片段須自足地載明「何物在何條件下為何」之後二者；
    前提子句所載之條件**必須**出現於 Pre-Condition，不得不見。
(d) 逐字比對器新增之第五項正規化（句首大小寫）採認，
    依據為 IN §8.7.5 之 R-4。
（分析層即裁，2026-08-29；上繳包 03 §四-4(a)、§十-3）
```

---

## R-ICS21

```
R-ICS21（綁定 DBC 、強度分級、偵察範圍三件）

(a) **`PDT27_E2A_R5_FDCAN8.dbc` 維持綁定**，不解除。
    實測零貢獻（九個 LID 之候選全數訊息不存在）之事實註於
    `feature.yaml` 之 `reference`。理由：R-ICS8(c) 之「二 DBC 篩」
    是判定程序，解綁即使日後新訊號少查一庫；
    「已查而無」與「未查」在台帳上必須可區別。
(b) **v2 下之強度分級採認**（執行層實作）：
    `正面命中（三軸齊備且全命中）` ／
    `正面命中（ECU 軸缺，依 v2(b)(ii) 不記 WARN）` ／ `不適用`。
    二級命中須可區別 —— 後者之確信度低於前者，
    DR-ICS9 若收窄 ECU 邊界，只有後者需重審。
(c) **偵察範圍擴充**：`spec-index/sources/` 之
    `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` 與
    `HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7
    (February 10th, 2023).pdf` 納入偵察範圍（b04）。
    **偵察非納源** —— 得列章節與命中，不得充 verbatim 來源、
    不得充錨，納源另裁。
（分析層即裁，2026-08-29；上繳包 03 §六-2、§三-4、§七-3、§十-5／6／7）
```

---

## R-ICS22 v1

```
R-ICS22（匯流排變體之 E1，及 Display 面 ER 之主錨）

⚠ **(a) 已由 R-ICS22 v2 取代（2026-08-29）**；(b)(c)(d) 仍為現行。
依 R-TM13 不刪不改字；改題與本註記之指紋變動依 R-ICS19 處理。

成因：A-ICS28／A-ICS29。`TGW_DISP_STAT` 與 `Telematic_Power` 之二候選
為**同一訊號之匯流排變體**（B-CAN vs CAN-FD），非 ECU 變體；
R-ICS13 之「取發送節點 = ICS」在此結構上無對應物。

(a) **不自裁取哪一條匯流排**。二候選維持 `fallbacks`，
    b03 之 12 處 `$TGW_DISP_STAT$` 佔位**維持**；新開 DR-ICS16
    向上游問「本 DUT 於哪條匯流排上觀察該訊號」。
    理由：二者發送節點皆非 ICS，且接收清單亦不含 ICS（A-ICS29），
    台架上取哪一條無量測依據；自選即造值（IN §8.4.1）。
(b) **b03 八條之 ER 主錨定為 HMI 可觀察現象**（螢幕亮／滅、
    背光態、`TOUCH SCREEN TO TURN ON` 之顯示），**訊號面為輔**。
    依據：R-DD3 同族 —— SWQT 之可觀察面為 HMI 現象，
    `$TGW_DISP_STAT$` 屬匯流排層。
    **故 b03 八條不因 (a) 之佔位而阻出貨** —— 但其 reasoning 須明載
    訊號面為輔且現為佔位，不得以外觀上之完整掩蓋其驗證強度。
(c) **不得以「ICS 收得到此訊號」立任何 ER**：
    `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`、`RADIO_B3.RQ_DISP_INTS`、
    `DIS_CENTERSTACK.DCSD_DISP_STAT` 三者之 DBC 接收清單均不含 ICS
    （A-ICS29）。已解之 `$RADIO_B3.RQ_DISP_INTS$` 三處改寫採認，
    但其觀察位置須書為匯流排迷蹤（CAN trace），
    不得書為「HU／ICS 收到」。
(d) 單名者（`RQ_DISP_INTS`、`DCSD_DISP_STAT`）之處置採認：
    R-ICS13 前件不成立即不套其結論，如實記其節點為 SGW／DCSD
    並判 RESOLVED —— 執行層將「前件是否成立」與「結論能否落地」
    分開判，合式。
（分析層即裁，2026-08-29；upstream-04 §3-1／3-2／3-3、§9-1／2／4）
```

---

## R-ICS23

```
R-ICS23（按壓事件定義之覆蓋缺口、B1／B2 之等待值、Menu Navigation 之存續）

(a) **短按／長按之區別：本 feature 不驗**。
    `1.8.1.3 Button Press Events` 之 24 物件中 23 為 `[ECU:FPDM]`，
    依 R-ICS2 v2(b)(ii) 為**實質不適用**（非軸缺），
    `Short Press`／`Long Press`（含 `<Tpress>`）於 ICS 側無母條。
    N1 只驗 `[pressed]` 訊號值之後果、不涉短長按，**採認**；
    執行層不自他處補（E6 觸發之處置）合式。
    登為覆蓋缺口 A-ICS33，並於 DR-ICS6 附問上游是否有 ICS 側等價條文。
    **不得以 FPDM 之條文充當** —— 不同 ECU，不同適用域。
(b) **B1／B2 之「轉動後 2 秒」須落佔位**。該值為測試實作選擇，
    而 `<TPeriodToSendNoChange>` 於 CFTS020 為符號無值；
    若上游之值 > 2 s，二條之觀察步驟即錯。
    依 IN §8.4.3 於 `pre_conditions` 增
    `PENDING: DR-ICS12 <no-change resend period>`（b05 補）。
    執行層之「不影響送什麼、只影響何時觀察」之區分成立，
    但「何時觀察」錯了仍致該 TC 判錯，故仍須佔位。
(c) **Browse Control 與 Menu Navigation 不合併**，採執行層 §10-1 之判斷：
    二者 entry path（旋鈕 vs 按鍵）與 setup pattern 皆異；
    Menu Navigation 現為 1 條之成因是 009 遭 DR-ICS13 凍結，
    **不是分組太細** —— 以合併補資料缺口是治錯了病。
    DR-ICS13 若回覆 009 出案外，屆時方得合併並更名（候選
    `Knob and Button Navigation`）；在那之前 framework 不動。
(d) LID `Format` 與 DBC `VAL_` 之字面不符及範圍越界（A-ICS30）：
    值一律以 **DBC 為準**（R-6 既例），LID 之拼字誤與越界不得入 TC，
    二邊逐字存於 JSON 供回溯，並於 DR-ICS8 附問。
（分析層即裁，2026-08-29；upstream-04 §3-4、§4-4、§9-5／7、§10-1、§10-2-2）
```

---

## R-ICS22 v2

```
R-ICS22 v2（匯流排之取捨：取 DUT 發送側）

取代 v1(a)。v1(b)(c)(d) 不變，仍為現行。
成因：v1(a) 斷「台架取哪一條無量測依據」，該斷言已由新量測推翻（A-ICS35）。

新量測（2026-08-29，二綁定 DBC 之 `BU_:` 與 `BO_` 發送者）：
  · FDCAN8 之節點 = {ETM, LTM, SGW, TBM}；**LTM 發送 0 則訊息**；
    `BO_ 1427 TELEMATIC_FD_4` 之發送者 = **ETM**。
  · BHCAN 之 `BO_ 1500 TELEMATIC_DISPLAY2` 發送者 = **SGW**（閘道）。
  · SWRA 011 載 DUT **維持並送出** `$TGW_DISP_STAT$`。

裁定：
(a) 同一訊號跨匯流排承載時，**取 DUT 自身為發送者之那一條**為主路徑；
    閘道轉發侧（SGW）記備援。理由：所驗者為 DUT 所送之訊號，
    觀察點自然在 DUT 所發之匯流排；於閘道侧觀察則多一層轉發，
    失敗時無法區別 DUT 未送與閘道未轉（因果塔縮）。
(b) 依 (a)：`$TGW_DISP_STAT$` 取
    **`$TELEMATIC_FD_4.TGW_DISP_STATSts$`**（CAN-FD，發送者 ETM）；
    `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`（B-CAN，SGW）記備援。
    `$Telematic_Power$` 同理取 `TELEMATIC_FD_4` 側。
    b03 之 12 處佔位於 b06 回收改寫。
(c) **先決問題：ETM 是否即本 DUT**。本條之成立繫於「DUT 之 DBC 節點
    名為 ETM」。實測佐證：FDCAN8 之 LTM 發送 0 則，而 CFTS022 之
    ECU 軸以 `LTM/ETM` 並列指 HU；執行層於 b06 須**先驗此一前提**
    （取 SYSAD／SWRA／LID 三路交叉），不成立即停並報，
    佔位維持、本條不適用。
(d) DR-ICS16 不逐結：降為「請上游確認 DUT 之 DBC 節點名與觀察點」之
    確認件，不再阻斷生成。
（Pei 2026-08-29「准」；A-ICS35）
```

---

## R-ICS24

```
R-ICS24（符號參數值之採認，及符號類 DR 之發出前置義務）

實測（2026-08-29，CFTS020 全文，§1.8 前文之 time-variables 定義塊）：
  `<Tsend> = 150 msec`、`<Tbutton> = 100 msec`、
  `<TPeriodToCountKnobDetents> = initial value 50 msec`、
  `<Tpower> = 1.5 sec`、`<Tstuck_button> = 120 sec`、
  `<Tpress> = 500 msec`、`<TPeriodToSendNoChange> = 20 msec`。

(a) 上列值採為 spec-sourced（IN §8.7.1），得直入 TC，非造值。
(b) `<Tstuck_button> = 120 sec` 使 **ignore 面與 DTC 面同值得證**；
    b02 之 I1／I2 二處 `PENDING: DR-ICS10` 於 b06 回收改寫。
    R-ICS9(d) 之「二門檻不得互代」**不撤** —— 其為程序拘束
    （不得以此推彼），現在是二者各自有來源而值相同，不同事。
(c) `<TPeriodToCountKnobDetents> = initial value 50 msec` 帶
    `parameter tuning process` 之註：得入 TC，**但須於 reasoning
    註明其為 initial value、可於整合測試後變更**；
    b01 V3、b04 B1／B2／B5 之佔位於 b06 回收。
(d) `<Tpress> = 500 msec` 之存在**不解 A-ICS33**：
    該值為時間參數，而所缺者為 ICS 側之 Short／Long Press
    **行為條文**（`1.8.1.3` 之 23 物件皆 `[ECU:FPDM]`）。
    有門檻而無行為，不得自行組合成 TC。
(e) **適用屬性須逐物件驗**：該定義塊於文中出現多次，
    各次之屬性三軸不同（含 PowerNet-only 之版本）。
    b06 須依 R-ICS2 v2 定出**適用於本 DUT 之那一物件**，
    以其 ObjectID 充錨；多版本值不一致時停並報。
(f) **置義務**：符號類缺件之 DR 發出前，須先於已納源文件全文搜
    `<符號>` 與 `<符號> =`，並於 DR 內文載明該搜尋之範圍與結果。
    只查需求句不算已搜（A-ICS34）。
（Pei 2026-08-29「准」；A-ICS34）
```

---

## R-ICS25

```
R-ICS25（005／009 解鎖，及市場軸之跨 feature 承接）

(a) **市場軸承接 R-DD25(a)**（Pei 2026-08-28 裁定，
    driver_distraction 下放包 20 §二）：**NAFTA 在案、LATAM 不在案**；
    `Hong Kong` 在案之依據為右駕（RHD）非區域。
    該裁定為**專案級範圍**，非 driver_distraction 專有，
    依 FO 之跨 feature 承接例採用，並於本條註明來源包。
(b) 依 (a)：**009（Back_Button）解鎖**。其直載原句 CFTS020-4819554
    之 Market 限 NAFTA，而 NAFTA 在案 → 在案。
    R-ICS15(b) 之凍結解除；Test Set 仍為 `Menu Navigation`，
    該組自此成 cluster，R-ICS23(c) 之合併議題不再發生。
    **須於 TC 之 reasoning 載明其 Market 限 NAFTA 及其在案依據。**
(c) **005（ICSMuteButton）解鎖**，依 R-ICS15(a) 同型：
    CFTS022-4914993 實測 `[Artifact Type:Subsystem Functional Requirement]`
    `[ECU:LTM, ETM] [Market:All] [Radio:R1L, R1M, R1L-R, R1H]`
    `[EE Architecture:All]` —— 依 R-ICS2 v2(a) 三軸全命中；
    其逐字直載 Mute hardkey 按下→ HU toggle mute/unmute state。
    上半 verbatim 改取 4914993，錨 `CFTS022-4914993`，
    不再等 DR-ICS1。Test Set = `Volume Control`。
(d) DR-ICS1 降為**帳面修正件**：其阻斷面歸零，但 SWRA 之
    Description 欄位移（A-ICS1）仍須上游更正，不逐結。
（Pei 2026-08-29「准」）
```
