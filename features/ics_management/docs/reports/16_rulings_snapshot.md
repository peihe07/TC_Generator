# RULINGS.md 快照 — b16 完工時（2026-08-30）**＝ 回凍之新基準**

> 快照法（R-ICS38(a)）第六次落地。b16 完工即回凍（R-ICS48(a)）；
> 下次解凍之圍籬 diff 以本檔為基準，**不動用 git**。逐字複本，一字未改。

- 來源 sha256：`caae34462e6ea16684c11d450609bda2ebbda09066c2752324c70942f4a33452`
- 錨點 55 個

- 快照時間：2026-08-30 16:44:51

---

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

## R-ICS19 v1

```
R-ICS19（R-G13 指紋與 R-ICS17(d) 改題之交互）

⚠ **(b) 之機械判準有缺，已由 R-ICS19 v2 補正（2026-08-29）**。

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

## R-ICS23 v1

```
R-ICS23（按壓事件定義之覆蓋缺口、B1／B2 之等待值、Menu Navigation 之存續）

⚠ **(a) 之事實描述有誤，已由 R-ICS23 v2 更正（2026-08-29）**；
結論（本 feature 不驗短長按）不變。(b)(c)(d) 仍為現行。
依 R-TM13 不刪不改字；指紋變動依 R-ICS19 處理。

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

## R-ICS25 v1

```
R-ICS25（005／009 解鎖，及市場軸之跨 feature 承接）

⚠ **(b) 之解鎖依據有誤，已由 R-ICS25 v2 更正（2026-08-29）**；
(a)(c)(d) 仍為現行。

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

---

## R-ICS23 v2

```
R-ICS23 v2（更正 v1(a) 之事實描述）

取代 v1(a) 之事實描述；**結論不變**（本 feature 不驗短／長按之區別，
N1 只驗 `[pressed]` 之後果，A-ICS33 成立）。v1(b)(c)(d) 不變。

v1(a) 書「23 物件**皆為** `[ECU:FPDM]`」，實測（upstream-05 §9）為：
  · `ECU` 含 `FPDM`：**16**
  · `ECU` 僅 `CCDMF`：**2**（4819602、4819606）
  · **`ECU` 軸缺，因 `Radio`／`EE` 實值落空**：**5**
    （4819594、4819596、4819600、4819607、4819613）

即那 5 個之排除是 **R-ICS2 v2(b)(i)** 之 Radio／EE 落空，
**非** v2(b)(ii) 之 ECU 判定。v1(a) 以單一成因概括三種成因，
使「若 DR-ICS9 收窄 ECU 邊界則須重審」之影響面被估錯 ——
實際只有那 16 個繫於 ECU 軸，另 7 個不受其影響。

**拿法**：條文中之「皆為 X」、「全數 X」類描述，須有逐物件之
成因分類輸出為據；只有判定結果相同不足以寫「皆因 X」。
（分析層即裁，2026-08-29；upstream-05 §9、§11-2）
```

---

## R-ICS26

```
R-ICS26（上繳包之台帳快照，及執行期間之寫入）

成因：upstream-05 §7-1。`ledger_guard` 二次輸出不逐字相同 ——
`ANOMALIES.md` 於執行期間由權杖持有者（analysis-A）新增 A-ICS34。
寫入**合法**（R-ICS17 治的是二個分析層同寫），但上繳包所依之前提
於其產出期間發生變動，為 R-ICS17 未治之另一面。

(a) **上繳包一律以「開工時快照」為準**：其 §1 指紋、前提驗證、
    預期數字皆以開工時之台帳狀態判定；完工時之差異**不判為不符**，
    而是以「執行期間台帳變動」具名回報，並附 `ledger_guard` 之 diff。
(b) **分析層之自拘**：下放後至上繳前之期間，分析層避免寫入
    `scope` 五類檔；必須寫入時（如本件之 A-ICS34，其發現不得拖），
    須於下一份下放包 §0 具名該次寫入及其對前一包的影響。
(c) **`ledger_guard` 之逐字比對不得降為只比 exit code**：
    本件二次 exit 皆 0，只比 exit 完全看不見。
    逐字比對之失效本身即該檢查有效性之證明。
(d) 本件之 upstream-05 預期 #10 改判 **相符（依 (a) 重判）**，
    不計入不符項；執行層之回報方式合式。
（分析層即裁，2026-08-29；upstream-05 §7-1、§11-3）
```

---

## R-ICS27

```
R-ICS27（符號值之錨定與回填；R-ICS24(e) 之完成）

R-ICS24(e) 令 b06 定出適用之定義塊物件；upstream-05 §8-2 已先定出，
且三路徑（分析層 A-ICS34、主實例複驗、作業 D 並行實例）收於一點。

(a) **錨定 `CFTS020-4819541`**（§1.8.1 之定義塊；`Artifact Type` =
    Subsystem Functional Requirement、ECU 軸缺、Radio 含 R1L／R1L-R、
    EE 含 Atlantis High → R-ICS2 v2 判適用）。
    **其余三份（§1.5.1／§1.11.1／§1.14.1）不得引用** ——
    §1.8.1 之 `<Tpress> = 500 msec` 與其餘三份不同，引錯即取錯值。
(b) 回填得於 b07 為之：DR-ICS10 2 處 → `120 seconds`；
    DR-ICS12 4 處 → `50 msec`（detent 計數窗）／`20 msec`（no-change 重送）。
    錯行增 `CFTS020-4819541`（與原錨並列、升序）。
(c) **`initial value` 之保留字**：`50 msec` 帶 `parameter tuning process`
    之註，回填後其值仍為暫定。處置：值入 TC，reasoning 須載
    「initial value、可於整合測試後變更」，且 **DR-ICS12 不結案**，
    改為「請上游確認調校後之定值」之追蹤件。
    **DR-ICS10 得結**（120 sec 無暫定註，且與 CFTS022-4914956 互證）。
(d) 回填前之 6 處佔位屬「值已在手而未用」（upstream-05 §12-2-1），
    其外觀與真缺值之佔位無異 —— b07 後佔位清單須區分
    「缺值」與「待回填」二態，不得混列。
(e) **節前定義塊之全面掃查**（upstream-05 §12-2-2）：b07 須對 CFTS020
    全文掃同類「節前定義塊」（不限時間符號：門檻、限値、列舉、
    預設值等），出清單。同一文件用了五包而 4819541 至第五包方被讀到，
    不得假定只有這一塊。
（分析層即裁，2026-08-29；upstream-05 §8、§11-1、§12-2-1／2）
```

---

## R-ICS28

```
R-ICS28（未錯定斷言之出貨閘；「無佔位」不等於「可出貨」）

成因：upstream-05 §12-1。V1／V2 **無任何佔位**、機檢全綠、
逐字命中，而其 ER 各有 2 行斷言 `"VOLUME POP_UP"` 顯示，
該顯示條件五包追索仍查無。佔位擋得住「知道自己不知道」，
擋不住「不知道自己不知道」。

(a) 立**未錯定斷言**之概念：ER 中之斷言，若其成立條件於
    **任一已納源文件皆無載**，即為未錯定斷言。
    其危害不在「寫錯」而在「無法判對錯」（IN §7 之 FF）。
(b) **出貨閘新增一項**：每條 TC 之每一行 ER 須能指回一個已錨之
    來源句，或已登為 A-（如 A-ICS16）。**二者皆無者不得出貨**。
    本項為人工判（無機檢形式），須逐條記於交付前體檢。
(c) V1／V2／V3 之 popup 行已登 A-ICS16，故**得出貨但須於
    交付時標明該 6 行為未錯定斷言**；未標明即不得出貨。
(d) 執行層 upstream-05 §12-1 將 V1／V2 列為「不可出貨」——
    其判斷採認為**預設態**；(c) 之標明為解除該預設之唯一途徑。
（分析層即裁，2026-08-29；upstream-05 §12-1）
```

---

## R-ICS29

```
R-ICS29（台帳之登記表結構與 ledger_guard 之掃法）

成因：A-ICS45。b06 之 E1 觸發（`ledger_guard` exit 1，報 DUPLICATE），
實測為**掃描定義有缺而非台帳有錯**：主登記表 17 列、相異 17、
號段無缺口；重號全數來自分析層新增之同形過渡表。

(a) **一檔一登記表**：`DATA_REQUESTS.md`／`ANOMALIES.md` 各只得有
    一個登記表；狀態寫於其 `狀態` 欄，**不得另立同形之過渡表**。
(b) **過渡區塊之標記**：確實需要保留之非登記區塊（沜革、重排、
    例示）須以 `<!-- LEDGER-IGNORE-BEGIN -->` 與
    `<!-- LEDGER-IGNORE-END -->` 包覆。
(c) **`ledger_guard.py` 之掃法改為**：先剔除所有 IGNORE 區塊，
    再於剩餘文本中取登記列。此一改動**由執行層依本條為之**，
    屬裁定後之實作，非「闘紅著改闘」。
(d) **正則須同時支援嚴格與寬鬆二式**：掃描須能辨識
    `| DR-ICS2、3、4 |` 這類**合併列**（其首格以編號開頭但非單一編號），
    且不得將其計入登記列。執行層報 11 筆而分析層實測 10 筆，
    差額正是該合併列（A-ICS45）—— 二數皆非錯，量的不是同一件。
(e) **執行層未自改工具而上報，合式且記於此**：
    在閘紅著時改閘使其變綠，是需避免之形態；
    工具之判準屬台帳結構，由分析層裁。
(f) **分析層寫台帳後須自跑 `ledger_guard.py`**（補 R-ICS17(f) 之缺，
    現行只規定執行層跑）。A-ICS44 已預告此事，本件即其後果。
（分析層即裁，2026-08-29；b06 E1 回報）
```

---

## R-ICS30

```
R-ICS30（VC 覆蓋之補齊，及 SWRA Verification Method 之對應）

(a) **SWE-ICS-004 之 `scroll`／`tune` 須補 TC**（A-ICS41）。
    其 VC 逐字載 `browse, scroll and tune operations`，而現只涵蓋 browse。
    **此為覆蓋面之缺，非資料之缺** —— 不得以 DR-ICS6 未回為由不生成。
    三操作各至少一條，錯同為 `CFTS020-4819586`（其原句同時載
    Browse／Scroll／Tune 三者）；畫面對應仍以
    `PENDING: DR-ICS6 <…>` 承載。
    理由：佔位是缺件之正當表達，不是不生成之理由；
    不生成則該 VC 於台帳上零覆蓋，而覆蓋率統計看不出來。
(b) **N1 之目標畫面未具名（A-ICS42）維持現狀**：4819555 原句自帶
    `if any`，即規格自認可能無對應畫面；具名須待 DR-ICS6。
    不得自行指定畫面名（IN §8.4.1）。
(c) **SWRA `Verification Method` 與 TC `design_method` 不同軸**：
    前者為 SWE.1 側之驗證方法建議（Functional／Integration／Robustness），
    後者為 IN §12 之設計手法，**不強制對應、不得以前者推後者**。
    但 VM 含 `Integration Test`（006）或 `Robustness Test`（010）者，
    其 TC 之 reasoning 須註明該面是否已由本批涵蓋；
    未涵蓋者入覆蓋缺口清單，不得靜默。
（分析層即裁，2026-08-29；upstream-05 §5-2、§11-4／6）
```

---

## R-ICS19 v2

```
R-ICS19 v2（補正 v1(b) 之機械判準）

成因：upstream-07 §1.1。R-ICS23 v1 之作廢註記寫在**圍籬內**，
使 v1(b) 之「diff 非 0 行→停下」與 v1(d) 之「適用於作廢註記」相衝。

(a) **作廢註記一律寫於圍籬外**（`## R-ICSn vN` 標題下、
    開圍籬前）。既存之圍籬內註記不搬（R-TM13），以 (b) 處理。
(b) 圍籬 diff 非 0 行時，若**差異行全數為作廢註記**（以 `⚠` 開頭
    或明載「已由 … v\d 取代／更正」），**不停**，於上繳包具名；
    含任一非註記之差異行 → 依 R-G13 停下。
(c) 執行層於 upstream-07 依 v1(d) 之實質判斷不停並具名缺口，**合式**。
（分析層即裁，2026-08-29；upstream-07 §1.1、§12-4）
```

---

## R-ICS25 v2

```
R-ICS25 v2（更正 v1(b)：009 之阻斷面不在市場軸）

成因：upstream-07 §5-1。實測：`CFTS020-4819554` 之
`Radio = [VP4R84, VP384, VP484]`、`EE = [PowerNet]` —— **二軸皆實值落空**，
依 R-ICS2 v2(b)(i) 即已出局；Market 於該判準中**不是判準軸**。
v1(b) 以 Market 軸解鎖 009，**前提從一開始就不成立**。

(a) **009 乍未解鎖**。v1(b) 之解鎖撤回；R-ICS15(b) 之凍結回復，
    但其理由改為「無適用之母條」而非「市場軸未定」。
(b) 執行層依「判不適用即停下、不得改錯他物件」停下，**合式**。
    其已盡之查證（含 `Back_Button` 之物件 7 個、判適用 2 個且皆非
    HU／ICS 側行為母條）採認。
(c) **DR-ICS13 不得以「市場軸已定」結案**；其内容改為
    「請提供 ICS／HU 側之 Back_Button 行為母條，或確認 009 出案外」。
    R-DD25(a) 之市場軸承接（v1(a)）不受影響，仍為現行。
(d) 005 之解鎖（v1(c)）**不受影響**：`4914993` 三軸實測全命中，
    其未生成之因為 E4，見 R-ICS31。
（分析層即裁，2026-08-29；upstream-07 §5-1、§12-3）
```

---

## R-ICS31

```
R-ICS31（多值屬性之比對判準；E4 之補充）

成因：upstream-07 §5-2。CFTS022 新舊版覆驗：四句 verbatim 4/4
**位元級相同**，七物件三軸**值集合 7/7 相同**、v2 判定 7/7 未變，
而逐字比對 0/7 —— **不符全數出在列舉順序**，內容零變動。

(a) **屬性三軸（ECU／Radio／EE）之比對以「值集合」為準**，
    列舉順序不計；順序不同而集合相同者判為**相符**。
    理由：三軸於本案之用途為適用性判定（集合運算），順序無語意。
(b) **本條不及 test_item 上半之 verbatim**—— 那是逐字，任何字元差異皆算。
(c) 依 (a)：**E4 於本件未真正觸發**，**005 得於 b08 生成**（R-ICS25 v1(c)）。
(d) 執行層依 E4 字面停下並從三個角度（逐字／集合／判定）分別量測後
    交由分析層釋判準，**合式且為本條之成立基礎**。
(e) `4914993` 之 `Model Year` 由 `2025, 2023, 2024` 改為 `Default`
    —— **真的改了值**，登 A-ICS48。新版 28 物件本文變動亦登入，
    本輪四句七錯皆不在其中，故改綁後既有 TC 無需回收。
（分析層即裁，2026-08-29；upstream-07 §5-2、§12-2／7）
```

---

## R-ICS32

```
R-ICS32（未錯定斷言七行之處置；常設項之確立）

(a) **(i) 不作為之可觀察化（B3、I1、I2 共 3 行）：保留，標弱驗證**。
    來源句言「忽略」而 TC 以「狀態不變」承載，是可行之最佳近似；
    但須於 reasoning 載明「來源未承諾該不作為必有可觀察之無變化」，
    且於交付時標為弱驗證（R-ICS28(c) 同型）。
(b) **(ii) `if any` 之逾越（B6、Scroll、Tune、N1 共 4 行）：須改寫**。
    原句自帶 `if any`，而 TC 斷言必有可觀察差異 —— 潛在 FF（IN §7）。
    b08 改為條件式：以 Pre-Condition 限定於「已定義該動作之畫面」，
    ER 再斷言差異；畫面名仍以 `PENDING: DR-ICS6` 承載，
    **不得自行指定畫面名**（R-ICS30(b) 不變）。
    R-ICS30(b) 治的是「不得自取畫面名」，**未治本行之斷言逾越」** ——
    執行層指出二者非同一件，正確。
(c) **未錯定斷言檢查確立為常設項**，採執行層 §13-3 之二層式：
    候選篩（ER 實詞對所錯來源句之涵蓋度）**每包必跑**；
    判斷本身**每包人工複核**，不交給腳本。
    理由：本輪七行全數通過 19 項機檢與逐字比對 ——
    機檢抓不到的正是這一類。
（分析層即裁，2026-08-29；upstream-07 §7-1、§13-3）
```

---

## R-ICS33 v1

```
R-ICS33（§1.18「ICS Management」之處置；不改錯，先比對）

成因：upstream-07 §13-2。CFTS020 §1.18（`AtlMi & AtlHi & AtlLo`）下之
§1.18.1 章名逐字為 **`ICS Management`** —— 與本 feature 同名；
37 物件、判適用 29。前七包全錯於 §1.8（`PNet & AtlHi & AtlMi`），
二者同樣涵蓋 Atlantis High。且 §1.18 更具體：`4821688` 逐字點名
**`CLIMATIC_PANEL message`**，`4821694／96／97` 之旋鈕值與 DBC `VAL_` 字面一致。

(a) **現階段一律不改錯**。既有 25 條之 `specification_reference` 維持不動。
(b) b08 須出 **§1.8 vs §1.18 之逐物件對比**：二節各自之適用物件清單、
    行為面之重疊與差異、並指出現有 25 條之每一個錯於 §1.18 是否有
    更具體之對應物件。**只列不裁**。
(c) **權威之取捨屬 Pei**（範圍問題，且涉及已交付面之回收規模）。
    三種可能結果須於 b08 報告中分別估其影響：
    ① §1.8 為正、§1.18 不適用；② §1.18 為正，25 條須重錯；
    ③ 二節並存且各有其涵蓋面。
(d) **本件不降低 b02～b04 之結論效力**：其 LID→DBC 推得之
    `CLIMATIC_PANEL` 與 §1.18 逐字所載一致 —— **二路徑獨立收於一點**，
    反而是其正確性之強佐證。惟繞遠路之事實須登 A-ICS50。
(e) §1.18 之存在亦可能解 DR-ICS16（`$TGW_DISP_STAT$`）與
    DR-ICS13（Back_Button 母條）：b08 之對比須特別查該二項。
（分析層即裁，2026-08-29；upstream-07 §13-2、§12-5）
```

---

## R-ICS33 v2

```
R-ICS33 v2（更正 v1 之成因段；增泛用母條一項）

v1 之成因段引 upstream-07 §13-2 之「§1.18 比 §1.8 講得更具體」，
該句已由 upstream-08 §2-3 以逐物件實測更正：**「更具體」是分項而非全面**。
  · 旋鈕／訊息名上確實更具體（`4821694／96／97` 新增引號值與上下界；
    `4821688` 點名 `CLIMATIC_PANEL message`）。
  · **POWER／SCREEN OFF 上反而更抽象**：少了數值與方括號值，
    多為 `See TLM CFTS and TLM HMI for details` 之外指，且主詞為 TLM 非 HU。
v1 之 (a)~(e) 拘束不變，惟其成因段不得再以「全面更具體」作為採 §1.18 之理由。

(f) **泛用母條與逐鍵母條之關係未釐清**（A-ICS55）：
    `4821683`~`4821689` 七個判適用之 `for all buttons` 泛用母條
    涵蓋所有 ICS 按鍵，而現有 TC 全數逐鍵錯定。
    **本項不得單獨裁** —— 其取捨繫於 §1.18 之權威歸屬（(c)）。
(g) **DR-ICS16 之第二條路確認不通**（A-ICS53）：§1.18 全 37 物件中
    含 `DISP_STAT`／`DISP_INTS` 者 **0 個**，且全節無任何匯流排叙述。
    即 §1.18 之權威歸屬無論如何裁，都不解 `$TGW_DISP_STAT$` 之 12 處佔位。
（分析層即裁，2026-08-29；upstream-08 §2-3、§2-5、§10-4）
```

---

## R-ICS34

```
R-ICS34（候選篩之門檻與其報告形式）

成因：A-ICS54。候選篩首版對 126 行 ER 命中 122 行（96%）——
執行層自判「一支命中率如此之篩等於沒有篩」並自行改法，判斷正確。

(a) **分層法採認**：對未涵蓋實詞計其跨 TC 出現數，**≥ 5 條 TC 者**
    列為衍生載具詞、自候選中扣除。門檻值可調，調後須量其效果。
(b) **二數必並報**：原始命中數與殘餘候選數（本輪 122／67），
    **不得以分層掩蓋原始噪音**。衍生載具詞須逐個印出可覆核。
(c) **53% 殘餘率採認為現階段基線**，不再調至 b09 後；
    但每包須報其殘餘率，連續三包 > 60% 即須重議門檻。
(d) **篩不取代判斷**（R-ICS32(c) 不變）：篩只產候選，
    未錯定之認定仍為人工。篩的命中率不得作為品質指標報出。
（分析層即裁，2026-08-29；upstream-08 §6-1、§10-6）
```

---

## R-ICS35 v1

```
R-ICS35（§1.8 與 §1.18 之權威歸屬；二節並存之過渡姿態）

Pei 裁定 ③（2026-08-29）：二節並存，非新舊版取代關係。
判定依據：二節之獨有面互不重疊（upstream-08 §2-2 實測）——
§1.18 獨有 Back_Button、CLIMATIC_PANEL 點名、Logistic Mode；
§1.8 獨有 DISP_STAT 家族、stuck button、short／long press、時間變數之定值。
此形態為「各有涵蓋範圍」而非「新版取代舊版」。

(a) §1.8 與 §1.18 對本 DUT **同時具母條效力**。
    二節獨有之行為面，各自為該面之唯一母條。

(b) 【**暫緩生效**，待 b09 作業 A 之量測】同一行為二節皆有判適用之母條時，
    取**主詞為 HU／ICS 者**為錨。
    本款暫不生效，理由見 A-ICS56：其成立繫於「TLM 非本 DUT」，
    而該前提未經量測。量測結果到達前，**13 條之錨一律不動**。

(c) 經 (b) 判定後仍二節皆合者，取敘述較具體者（含具名元件、具名訊息、
    具體定值）。仍不可分者，登 DR，不得逕選。
    (b) 暫緩期間本款一併暫緩。

(d) 本條為**過渡姿態**，非規格權威歸屬之終局認定。
    DR-ICS18 之上游答覆到達時，本條自動進入重議，不需另行提請。

(e) 依本條所立之錨，reasoning 須註明所據為 §1.8 或 §1.18，
    不得只寫「規格」。

(f) **生效即發生之效果（不待 (b)）**：
    · 25 條既有錨**全部維持有效** —— §1.8 未被推翻，故 b03 之 8 條、
      `4819541` 所支撐之 6 條、b07 回填之 6 處佔位皆不動。
    · R-ICS33 v1(a)「現階段一律不改錨」之全面禁令，
      改為「**(b) 生效前不改錨**」。
    · A-ICS55（泛用母條與逐鍵母條之關係）之處置一併繫於 (b)，不另裁。

(g) **DR-ICS13 不因本裁定結案**。§1.18 之 Back_Button 母條中，
    ICS 側 `4821681` 為 LID 清單非行為母條；行為母條 `4821704` 主詞為 TLM
    —— 其可用與否正是 (b) 待量之事。**009 於 (b) 定案前不生成。**

（Pei 裁定 ③，2026-08-29；分析層草擬條文同批准（含 (b) 暫緩）；
  upstream-08 §2-6、§10-1；報告 docs/reports/08_s118_vs_s18.md §5）
```

> ⚠ **成因段已由 R-ICS35 v2 更正**（拘束不變）；
> (b)(c) 之處置已移交 R-ICS36(b)（由暫緩改為廢止）。

---

## R-ICS35 v2

```
R-ICS35 v2（更正 v1 之成因段；(b)(c) 之處置移交 R-ICS36）

v1 之成因段以「二節之獨有面互不重疊 → 各有涵蓋範圍」為 Pei 裁 ③ 之依據。
upstream-09 §2-5 逐字實測後，該推論**另有一個更簡單且更可能之解釋**：
`CFTS020-4819134` 逐字界定 —— Associated 變體為觸控螢幕整合於 HU 模組，
Disassociated（'Silver Box'）變體為外接 DCSD；而 §1.8 標題含 `Silver Box HU`、
§1.18 標題為 `ICS and Associated HU`，且 §1.18 提及 `DCSD` 者 **0 次**。
即：二節係同一顆 HU 之**兩種硬體變體**，而一顆 DUT 只會是其中一種。
若如此，則非「二節並存」而是「**只有一節適用**」。

(h) v1 之 (a)(d)(e)(f)(g) **拘束不變** —— 其效果全為「不動」
    （25 條錨維持、009 不生成、DR-ICS13 不結案），
    維持之成本為零，撤回之成本則是回到無裁狀態。
    故於變體量測回覆前，v1 繼續作為過渡姿態。

(i) **但 v1 之成因段不得再以「互不重疊」作為「二節並存」之證據。**
    互不重疊同樣（且更簡單地）由「二變體」解釋。

(j) v1(b)(c) 之處置移交 **R-ICS36(b)**：由「暫緩」改為「廢止」。

(k) v1(d) 之重議觸發條件擴充：除 DR-ICS18 之上游答覆外，
    **b10 作業 A 之變體量測結論到達時，本條亦自動進入重議**。

(l) **本項須向 Pei 具名**：③ 之依據已動搖。
    是否維持過渡姿態至變體量測回覆，或即刻撤回 ③ ——
    分析層建議維持（理由見 (h)），並已具名上呈。

（分析層即裁，2026-08-29；upstream-09 §2-5；R-ICS33 v1→v2 同型）
```

---

## R-ICS36

```
R-ICS36（變體歸屬為前置量測；R-ICS35(b)(c) 廢止；E6 四件押後）

成因：upstream-09 §2-5、§3-3、§3-5、§9-2。

(a) **本 DUT 之變體歸屬（Associated／Disassociated）為現階段最高優先之量測**，
    交 b10 作業 A。其結論一旦成立，「取哪一節」自動有解，
    且「同一行為二節皆有母條」之情形根本不會發生。

(b) **R-ICS35(b)(c) 由「暫緩」改為「廢止」**（採 upstream-09 §9-2 建議一）。
    理由：(b) 之可操作性全來自「TLM 是他者，故主詞為 TLM 者可排除」；
    量得 `TLM = DUT` 後，二節之主詞同指一物，該判準**無從區辨**
    —— 不是變嚴或變鬆，是**篩子沒有網目了**。不改寫其文字，直接廢止。

(c) **E6 之四件（G2／G3／G5／G9）一律押後，不生成**。
    理由與 (a) 同源：若本 DUT 為 Disassociated，§1.18 之 29 個適用物件
    整批不適用，現在生成即為白做。待變體量測回覆後另裁。

(d) **§3-5 之範圍重疊處理（納入令優先）予以追認**。其三理由成立，
    尤以 (c)「若不在此清點則無其他作業會清點」為要。

(e) **禁區條文補強**：自 b10 起，「git 全數不執行」須逐字寫為
    「git 全數不執行，**唯讀指令亦不可**；如需自證未改檔，
    用 `ls`／`shasum`／`get_file_info`」。b09 之違規歸因於本補強之缺漏
    （A-ICS58），**不追究執行層**。

(f) G3 之 `Tbutton`：值取 A-ICS34 實測之 §1.8 定義塊 `<Tbutton> = 100 msec`，
    **不另立 DR**；惟 reasoning 須註明其來源為 §1.8 而非 §1.18，
    並繫於 (a) 之變體歸屬。（§1.18 全節無定值已於 upstream-08 §2-2 實測在案。）

(g) `{VF601}`（G5 之觸發側）**暫不納源**：其需要性繫於 (a)，
    變體判為 Disassociated 時該物件整批退出，納源即無意義。
（分析層即裁，2026-08-29；upstream-09 §2-5、§3-3、§3-4、§3-5、§9-2）
```

---

## R-ICS37

```
R-ICS37（變體歸屬採認 Disassociated；錨層懸置解除；覆蓋層不逕退出）

成因：upstream-10 §2-1。作業 A 量得本 DUT 為 **Disassociated**
（'Silver Box'，外接 DCSD）。支持證據十項**全部脫離 §1.8／§1.18**
（循環不計入者 0），反證七項逐項處置。三份互相獨立之文件收於同一點：
  · SYSAD 之 `DCSD Domain` 定義（`External display module containing LCD,
    touch controller, MCU, and backlight control.`）與 `DCSD MCU` 背光執行；
  · SYS2 之 `NRL-52863`（HU 與 DCSD 失通訊之**在案** HW 需求）
    及四列 `This DTC is for DCSD module not LTM` 式之排除語；
  · LID 之 `RQ_DISP_INTS` = `HU calculated display intensity for use by DCSD.`
分支配對檢定：Associated 分支適用需求物件 **0**，
Disassociated／Silver Box 分支 **46** —— **46 : 0**。

(a) **採認 `Disassociated`**。為**過渡採認**，繫於 DR-ICS18 之上游答覆。

(b) **錨層之效果：27 條之錨 0 變動，且此為終局而非暫時**（除非上游推翻）。
    15 個 CFTS020 錨 15/15 在 §1.8 子樹且判適用。
    **自 b08 起之三包錨層懸置，至此解除。**

(c) **覆蓋層不逕行退出**：§1.18 之 29 個適用物件與 upstream-09 之
    9 個缺口**維持登記，不消滅**。理由：A-ICS63 之衝突未解 ——
    本 DUT 自身之 SYS2 收 §1.18 之 29 列為在案需求（其中 8 列為
    Functional Requirement）。**「量得變體」與「§1.18 對本 DUT 之地位」
    是兩件事，不得默認為同一件。**

(d) **R-ICS35 v1(a)（二節並存）之拘束維持，其依據更替**：
    不再以「獨有面互不重疊」（v2(i) 已禁），
    **亦不得以本條之變體結論反推**。
    現行依據為 A-ICS63 之未解衝突：SYS2 同時收二節，
    而其收錄是否具獨立意義未明。二候選並列，交 DR-ICS18。

(e) **009 維持不生成、DR-ICS13 維持 OPEN 不得結案**。
    於 Disassociated 下 009 之母條為零（CFTS020 含 `Back_Button` 之 7 物件：
    §1.5／§1.8／§1.14 之 5 個判不適用、§1.18 之 2 個隨節退出），
    **但「出案外」屬範圍縮減，須待 A-ICS63 解後由 Pei 裁，分析層不逕定。**

(f) R-ICS36(c) 押後之四件（G2／G3／G5／G9）**維持押後，不轉取消**，理由同 (c)。

(g) A-ICS55（泛用母條）**維持 OPEN，不消滅**，理由同 (c)。

(h) 作業 B 之二欄代價對照採認入檔（Disassociated 改寫 0 條／
    Associated 改寫 20 條、退佔位 6 處、b03 退 7 救 1）；
    惟**不得以代價較小作為採認 (a) 之理由** ——
    作業 A 之十項證據皆脫離二節，且交辦之三條主路徑全部落空（A-ICS64）。
（分析層即裁，2026-08-29；upstream-10 §2-1、§2-3、§3-2、§3-4）
```

---

## R-ICS38

```
R-ICS38（快照法取代 git；NBSP 正規化；probe 變體層；三項工具處置）

(a) **採 upstream-10 §0 建議 (b)：快照法。**
    執行層於每包**完工時**將當輪 `RULINGS.md` 存一份快照至
    `docs/reports/{nn}_rulings_snapshot.md`；下一包之圍籬 diff **比對該快照，不碰 git**。
    自 b11 起實施。b11 無前快照，該輪之圍籬 diff 標「無基準，不判」，
    **非停工事由**。R-ICS36(e) 之禁 git 條文**不開例外**，維持「唯讀亦不可」。
    順帶解決「執行期間分析層改台帳」之溯源問題（b05 §7-1 已發生過一次）。

(b) **A-ICS62 之違規不追究執行層**：條文互斥為分析層下派所致
    （禁 git 與 C-5 同包並列，而圍籬舊版只存於 git）。
    主實例自承具名，合式；其「**該選擇不該由執行層逕定**」之自我判斷正確，本條採之：
    **此後遇條文互斥，應停下回報，不得自行擇一**（E9）。

(c) **NBSP 正規化納入 R-ICS31(a) 之比對前處理**：
    凡自 docx 取出之文字，比對前一律將 `U+00A0` 正規化為半形空格。
    `s118_compare_08.py` 之缺陷（A-ICS66）依此修；
    **08 之報告與腳本不回改**（R-TM13），b11 重跑 09 之覆蓋清點並二數並報。
    **本款不及 test_item 上半之 verbatim**（R-ICS31(b) 不變，那是逐字）。

(d) **`cfts020_probe` 之適用性判定加一道「變體層」**（A-ICS67）：
    變體層之退出與軸層之不適用**不同源**，須分列輸出，
    不得合併為單一「適用」旗標。b11 實作並回溯報 §1.18 之 29 物件於二層下之判定。

(e) **CFTS022 之變體軸未量**（A-ICS68）：7 條純 CFTS022 之 TC 現以「不受影響」計，
    其前提未經量測。b11 作業量之。

(f) `4819541` 之時間變數為**七個**非六個（下放包 10 §3 之誤，A-ICS65）；
    第七個 `<TPeriodToSendNoChange> = 20 msec` 為 b04-01／02 之回填來源。
（分析層即裁，2026-08-29；upstream-10 §0、§3-5）
```

---

## R-ICS39

```
R-ICS39（Pei 裁定：§1.18 之 29 物件算數；並列雙錨；009 解鎖）

**Pei 裁定（2026-08-29）：§1.18 之 29 個物件對本 DUT 算數。**
A-ICS63 之二候選依（ii）定案：SYS2 之收錄為實質範圍決定，非軸層過濾之副產物。
本裁定屬範圍決定（Tier 3），於 b11 之量測之前作出，取代該量測作為判斷依據。

(a) **二節真並存**。R-ICS35 v1(a) 之拘束自此以**本裁定本身**為依據，
    不再繫於 A-ICS63 之未解衝突；R-ICS35 v2(l) 之上呈事項結案。
    v2(i)「不得以互不重疊作為證據」仍存（那是推論之禁，非結論之禁）。

(b) **變體歸屬不因本裁定變更**。R-ICS37(a) 之 `Disassociated` 維持。
    理由：**變體是硬體事實，§1.18 之算數是範圍決定，二者不同層**。
    §1.8 仍為變體正解，其支撐之 27 條錨**全部有效，一條不撤**。

(c) **同一行為二節皆有母條時：並列雙錨，不擇一。**
    據 IN §10.7（`lists every spec section the TC directly verifies`）。
    已廢止之 R-ICS35(b)(c) **不復活** —— 不需取捨判準，因為不取捨。
    排列依 IN §10.7：同為 CFTS 家族，一 ObjectID 一行，ID 升序。

(d) **加錨作業押後至 b12，b11 仍一條不改錨。**
    前置：b11 之 NBSP 重跑（R-ICS38(c)）。理由：現行「13 條有對應」
    之集合由含 NBSP 缺陷之 `s118_compare_08.py` 產出（A-ICS66），
    正規化後錨層由 11／4 變 13／2 —— **對應集合本身須重測後方得加錨**。
    不先重測即加錨，是 A-ICS64 同一錯誤族之再犯。

(e) **009 解鎖**。其母條為 `4821704`（行為、主詞 TLM＝本 DUT）
    與 `4821681`（LID 清單）。**於 b11 生成**；
    DR-ICS13 於 009 生成且通過自檢後結案，**不得提前結**。

(f) **R-ICS36(c) 押後之四件：G2、G3、G9 解除押後，G5 維持押後**。
    G3 之 `Tbutton` 依 R-ICS36(f) 取 §1.8 定義塊 `100 msec` ——
    §1.8 於 Disassociated 下有效，來源成立（upstream-10 §3-3 之「G3 反而惡化」
    係 Associated 情境下之估，不適用於本裁定）。
    G5 之阻因為 A-ICS60（DBC 查無 ＋ `{VF601}` 不在件內），**與本裁定無關**。

(g) A-ICS55（泛用母條 `4821683`~`4821689` 與逐鍵母條之關係）
    自「繫於待裁」轉為**須答之實題**，b12 處理。

(h) **DR-ICS18 降為告知性／追認件**，不再阻斷。
    向上游告知本裁定並求追認；**若上游否認（即表示 §1.18 之 29 列
    應自 SYS2 剔除），本條自動進入重議**，屆時 009 與加錨皆須退回。
    此風險已具名，不以其存在而停工。

(i) 本裁定使 b11 原作業 A（SYS2 收錄面判讀）**失去決策用途，撤除**。
    其量測內容若日後因 (h) 之重議而需要，再行交辦。
（Pei 裁定，2026-08-29；upstream-10 §2-4；A-ICS63；IN §10.7）
```

---

> ⚠ **以下為作廢之重複草案**（A-ICS70：分析層違 R-G23，未取現場號即落條，
> 與既存之 `R-ICS40` 正本撞號）。依 R-TM13 不刪除，加註保留。
> **正本見下方之 `## R-ICS40`**；本草案未被正本吸收之唯一一款
> （Market 限 NAFTA 之廢止）已移入 `R-ICS41(c)`。**本區塊無拘束力。**

```text
【作廢草案】原題：並列雙錨之適用限縮；加錨粒度；跨家族排列

(a) **並列雙錨限於二側皆判適用者**（採 upstream-11 §9-2 建議）。
    一側判**不適用**時單錨，且其 reasoning 須載明另一側之存在與其不適用之理由。
    理由：IN §10.7 令 `specification_reference` 列「該 TC 直接驗證之每一 spec section」，
    而一個判不適用之物件，本 TC 並未驗證它。
    R-ICS39(c) 之「二節皆有母條」自此讀為「二節皆有**判適用**之母條」。
    009 依本款單錨 §1.18 之 `4821681`＋`4821704`；
    其現行 reasoning 已載 §1.5／§1.8／§1.14 五物件之不適用，**合式，不修**。

(b) **加錨粒度採「行為等值覆蓋」（15 條／24 錨行），不採節層標籤（18／86）**。
    理由：後者含明顯假性對應（如 b02-01 stuck button 對 `4821709` Mute），
    屬 IN §8.4.2 之範圍造假。錨是驗證關係之聲明，不是詞彙重疊之記錄。

(c) **跨 CFTS 文件之錨行排列**：依文件分組、組內 ObjectID 升序、
    文件依 CFTS 編號升序（`CFTS020-…` 全數在 `CFTS022-…` 之前）。
    此為 IN §10.7「同文件內 ID 升冪」之**明文化，非新制**。
    b06-01／02 依此排；跨家族混排無先例一事不構成障礙。

(d) 加錨於 **b12** 執行，依 upstream-11 作業 B 報告 §4-2 之逐條表**照抄**；
    其 §4-3 所列不加錨之 12 條，**一條不动**。

(e) **R-ICS25 v1(b) 之「009 必載 Market 限 NAFTA」廢止**。
    該限制繫於舊候選錨 `4819554`（現判不適用）；
    實際二錨實測皆為 `Market = All`。執行層之不照抄正確，
    **若照抄即為與實測不符之陳述**。
（分析層即裁，2026-08-29；upstream-11 §3-4、§2-3(a)、§8-5、§9-2）
```

---

> ⚠ **以下為作廢之重複草案**（同 A-ICS70）。其 (a)(c)(d) 已由正本
> `R-ICS40(d)(e)` 吸收；(b) 之論證已改落於新之 `R-ICS41(a)`。
> 依 R-TM13 不刪除，加註保留。**本區塊無拘束力。**

```text
【作廢草案】原題：母條粒度高於 SWRA RD 時之 trace 通則；不逐鍵展開

成因：upstream-11 §2-3(b)、§9-1-3。`4821688`（多鍵並存）與
`4821689`（事件變化→幀更新）之主詞為**任一按鍵**，屬跨鍵之傳輸層行為；
而 SWRA 之 RD 為逐訊號切分（001~010），無與之對應者。

(a) **通則**：CFTS 母條之行為為跨物件之**全稱**，而 SWRA 無對應 RD 者，
    TC 之 `requirement_id` 取**該行為所具現之代表 RD**，
    並於 reasoning 具名三事：① 母條為全稱、② 本 TC 為單稱具現、
    ③ 代表之選擇理由。
    **不得為求對應而改寫母條、不得自創 RD**（IN §8.2）。

(b) **不逐鍵展開**。理由：IN §8.3 之 sibling axis 適用於「行為隨輸入而異」者；
    此處行為對所有按鍵同一，逐鍵展開為冗餘，且不满足 IN §7 之拆分判準
    （不同輸入不產生不同判定）。G2／G3 取 Display Control 二鍵具現，**合式**。

(c) 惟須登 DR 向上游詢問是否應有一條跨鍵之 RD（**DR-ICS20**）。
    **若上游答覆指出逐鍵有差異，本條進入重議**，G2／G3 須重審。

(d) 本條之適用須**逐案於 reasoning 具名**，不得默默套用 ——
    否則「全稱母條以單稱具現」會成為覆蓋缺口之隱形入口。
（分析層即裁，2026-08-29；upstream-11 §2-3(b)、§8-1、§9-1-3）
```

---

## R-ICS40

```
R-ICS40（並列雙錨之適用限、加錨粒度、跨家族排序、全稱母條之具現）

成因：upstream-11 §8 之待裁八項、§9-2 之建議。

(a) **並列雙錨限於二側皆判適用者**（採 upstream-11 §9-2 建議）。
    一側判**不適用**時單錨，且其 reasoning 須載明
    另一側之**存在**與其**不適用之理由**。
    理由：IN §10.7 令 `specification_reference` 列「該 TC 直接驗證之每一 spec section」，
    而一個判不適用之物件，本 TC 並未驗證它。
    R-ICS39(c) 之「二節皆有母條」自此讀為「二節皆有**判適用之**母條」。
    **009 不併列 §1.8**（其 5 個含 `Back_Button` 之物件皆判不適用），
    其現有 reasoning 已載該 5 個之不適用，**合式，不修**。

(b) **加錨粒度：採行為等值覆蓋（15 條／24 錨行），不採節層標籤（18／86）。**
    理由：節層標籤法產生「b02-01（stuck button）加 `4821709`（Mute）」
    這類**明顯假性對應**，直接違 IN §10.7 之 `directly verifies`。
    b12 依 upstream-11 報告 §4-2 之逐條表**照抄**，不重新推導。

(c) **跨 CFTS 家族之錨行混排：允許**。排序為
    **① 文件號升序（CFTS020 先於 CFTS022）② 同文件內 ObjectID 升序**。
    本款補 IN §10.7 之空缺（該節只定 CFTS 家族先於 HMI 家族，
    未定 CFTS 家族內部之跨文件排序）。
    b06-01／02 為全案首例，**不因無先例而阻**。

(d) **全稱母條之具現（G2／G3 形）**：
    母條主詞為「任一按鍵」等全稱、而 SWRA 無對應 RD 時：
    ① 以**代表元素具現**，trace 至該母條 ObjectID；
    ② reasoning **須逐項載**：母條為全稱之事實、所選代表元素及其選擇理由、
      **未具現之元素清單**、以及「為何不需各生一條」之論證；
    ③ ② 之論證**寫不出來者，登 DR，不得以「測試實作選擇」帶過**。
    G2／G3 現行之 reasoning 已满 ①② 之前三項，**缺第四項（未具現清單與論證）**
    —— b12 補之（作業 D）。本款不使 G2／G3 退回。

(e) **SWRA 之 RD 粒度缺口登 DR-ICS20**：跨鍵／跨訊號之傳輸層行為
    於 SWRA 無對應 RD，屬上游分解之缺口（IN §8.2：RD 之分解屬上游），
    **不得由 TC 作者自行再分解**。

(f) **87 個「軸層適用、變體不合、範圍隨變體層」之物件：不逕裁、不類推。**
    R-ICS39 之依據為 **SYS2 之收錄**，而該 87 個是否亦為 SYS2 所收**未測**。
    未測即類推，是 A-ICS64 同一錯誤族。b12 作業 B 量之，量完再定。

(g) **CFTS022 之外引反噬（A-ICS73）：b12 作業 C 量之**。
    本輪七錨本文無 `{CFTS020}` 外引，判定不改；
    惟**全文族層之外引關係未逐一追**，存疑不得以「本文無外引」陣滅。

(h) **A-ICS66 之因果陳述依執行層之自我更正修正**：
    NBSP 缺陷真實存在，但其後果**只落於錨層對應集合，不落於 09 之覆蓋清點**
    —— 09 走 `tokens()`／`hits()`，其 token 不含空白且 `norm()` 已剥非英數字元，
    結構性免疫。**分析層於審 upstream-10 時所寫「使 09 §1 之三條覆蓋判
    可能有誤」為誤推**（A-ICS71）。

(i) **DR-ICS13 標「可結」**：R-ICS39(e) 之條件已達成
    （009 已生成、機檢 19 項 FAIL 0、逐字 31／31）。
    依 DR 台帳值域之定義，**佔位實際回收後方改 CLOSED**。
（分析層即裁，2026-08-29；upstream-11 §2-3、§3-2、§3-4、§4-3、§5-2、§8、§9-2）
```

---

## R-ICS41

```
R-ICS41（G2／G3 不逐鍵展開之論證；Market 限 NAFTA 之廢止）

(a) **補 R-ICS40(d)② 之第四項（「為何不需各生一條」之論證），就 G2／G3 一案逕裁**：
    **不逐鍵展開。** 理由：IN §8.3 之 sibling axis 適用於「行為隨輸入而異」者；
    `4821688`（多鍵並存）與 `4821689`（事件變化→幀更新）之行為
    **對所有按鍵同一**，逐鍵展開不滿足 IN §7 之拆分判準
    （不同輸入不產生不同判定），為冗餘。
    故 G2／G3 取 Display Control 二鍵具現為**合式**，**不退回**。
    惟 b12 仍須依 R-ICS40(d)② 於 reasoning **補列未具現之按鍵清單**，
    並引本款作為該論證。

(b) 本款之效力繫於 **DR-ICS20**：若上游答覆指出逐鍵有差異，
    本款進入重議，G2／G3 須重審。

(c) **`R-ICS25 v1(b)` 之「009 必載 Market 限 NAFTA」廢止**（正本 R-ICS40 未及）。
    該限制繫於舊候選錨 `4819554`（現判不適用）；
    009 實際二錨 `4821681`／`4821704` 實測皆為 `Market = All`
    （另 `Model Year = Default`）。
    執行層之不照抄正確 —— **若照抄即為與實測不符之陳述**。

(d) 本條之立，係分析層於審 upstream-11 時違 R-G23（未取現場號即落條）
    而與既存 `R-ICS40` 撞號後之重整結果；撞號經過見 **A-ICS70**。
（分析層即裁，2026-08-29；upstream-11 §2-3(b)、§9-1-3；R-ICS40(d)）
```

---

## R-ICS42

```
R-ICS42（「87 個」之重界定；probe 三值化；掃描起點盲區；五項附帶處置）

成因：upstream-12 §3-2、§3-3、§3-4、§3-5、§4-2、§4-3、§4-4、§1.2。

(a) **「87 個」之題目重界定**。實測其為 **§1.4（Diagnosis and Recovery Common
    Between Architectures）× 86 ＋ §1.5 × 1**，非 Associated 分支。
    A-ICS74 之描述依此改述（A-ICS77）。
    **分析層於審 upstream-11 時未複驗即登入 A-ICS74，並據以下放作業，
    且一度擬以此錯誤前提併問上游（A-ICS83）。**

(b) **probe 之 `variant_fits_dut` 三值化**：`Disassociated`／`Associated`／`Unclassified`
    分列，**不得以布林值將「未分類」與「Associated」合桶**。b13 實作，
    並回溯報全域三層交叉表（upstream-11 §4-3 之 138／29／87 須重算）。

(c) **「87 併問 DR-ICS18」之計畫撤銷**。該計畫建於「Associated 分支」之錯誤前提，
    **幸因 MCP 逾時未寫入**。DR-ICS18 之追認文維持現狀。
    反向查核（§3-4）顯示 SYS2 於 Associated 分支 262 物件中**只收 §1.18 之 29 個**
    —— **強化 R-ICS39**，採為其旁證入檔。

(d) **§1.4 之 86 物件之處置**：依本 DUT 自身 SYS2 之分類 ——
    標 `Out of Scope` 或 Feedback 為 `Marking the statement as information` 者，
    **不入驗證範圍**（此為遵從上游自身之分類，非分析層之範圍決定）。
    唯一 FR `4819353`（→ `NRL-52850`）**須查現有 31 條之覆蓋**，b13 量之；
    未覆蓋者登覆蓋缺口，不逕生成。

(e) **掃描起點盲區（A-ICS78）**：SYS2 有 23 列在案 FR 無 CFTS020 來源，
    以 CFTS020 為起點之掃描結構性掃不到。
    b13 **以 SYS2 為起點反向掃一次**：23 列逐一列其 Category／子分類／Feedback／
    是否屬 HW 供應商範圍（I2C／觸控時序等），以及其中是否有任一列為
    HMI 軟體側可驗證之行為。**只列不裁**；若有 HMI 側可驗證者，停下回報（範圍屬 Pei）。

(f) **第三種變體表達採為 R-ICS37(a) 之旁證（非決定性）**：
    `NRL-52847` 逐字 `The 10.1 inch DCSDX which will be paired with the VP4R84, R1H, R1L radio HUs`
    指向 Disassociated，與 R-ICS37(a) 一致。
    **局限具名**：`$Head_Unit_Screen_Size$` 本 DUT 實值查無；`R1L` 與 `R1L-R` 之差未調和。
    A-ICS76 之描述三處不符（`ICS_R/CCDMR`；`= [10]` 為枚舉非吋數；判別軸為 CCDM 在否＋螢幕規格，
    非變體軸），為**分析層之誤**，改述（A-ICS81）。

(g) **b06 二條加 §1.18 錨（`4821709`）合式**。A-ICS73 所慮之「波及 CFTS022 側」
    經加錨成為事實，但這不是反噔而是追溯 —— 該 TC 直接驗證 §1.18 之 Mute 行為，
    IN §10.7 令列之。其退回風險已由 R-ICS39(h) 吸收，不另處置（A-ICS79 登記後結案）。

(h) **`forms/PDT27_E2A_R1_BHCAN2.dbc` 登記，不逕綁定**（A-ICS82）。
    其 `BO_ 1445 DIS_CENTERSTACK` 由 SGW 轉發、`DCSD_DISP_STAT` 收方明列 `ETM,LTM`，
    **可能部分回答 DR-ICS16**。b13 以唯讀方式量其對 DR-ICS16 之填補程度，
    綁定與否待 A-DM14（R4）之跨 feature 裁定，**不在本線逕裁**。

(i) **A-ICS70 之時序更正**：正本 `R-ICS40` 不存於 b11 完工快照，寫於 08-29 21:22 之後；
    「既存」之說不成立。來源仍未明，**已直接問 Pei**（A-ICS80）。
    快照法首次使用即收窄一件來源不明之事，其價值已實證。

(j) **`$Touchscreen_ICS$` 第四條路徑**：登記，不走。變體已三路交叉一致，
    第四路之邊際價值低於其成本。
（分析層即裁，2026-08-30；upstream-12 §1.2、§3、§4、§10）
```

---

## R-ICS43

```
R-ICS43（ICS 線凍結；凍結基準；解凍第一批；五項收尾處置）

成因：upstream-13 全文。17 項全數相符；E19 觸發。

(a) **ICS 線自本條起凍結**。凍結基準：`docs/reports/13_rulings_snapshot.md`（49 錨點）、
    `docs/reports/13_freeze_record.md`。TC 31／佔位 18 處 14 條／DR 20／
    A-ICS 至本輪所登。**凍結期間五簿不寫、錨不動、TC 不生**，
    唯上游 DR 回覆之登記例外。解凍須 Pei 一字。

(b) **凍結記錄之三缺（upstream-13 §11-2）不另開包補，列為解凍第一件**：
    ① 以 SYS2 333 列為主鍵之對照表（標各列是否已有 TC 覆蓋）—— 結構性，最重；
    ② 254 → 31 之收斂軌跡；③ 失敗史附錄（至少含：節前定義塊須搜、
    布林旗標會合桶、未量即斷五例）。三件皆不依上游。
    理由不另開包：① 正是接手者開工時最該自己做的事，現在做只是多一包。

(c) **E19（`NRL-180522`，觸控去重／CarPlay 認證）上呈 Pei**。
    分析層建議：**非 ICS 範圍，轉 `display` feature 為覆蓋候選**——
    其行為面為觸控事件處理，與 PDT27 dbc（`FORMS.md` 登 `display`）同域；
    ICS Management 之範圍為旋鈕／按鍵面板。**分析層不逕定**。
    另 `NRL-180512`（不可判）隨同。

(d) **SYS2 自帶三欄（`Verifiability`／`Verification Criteria`／`Verification Method`）
    為全案工具知識，提請升 R-G**：本線十三包自行推導可驗證性，而 SYS2 早已逐列標定。
    建議 Phase 1 recon 新增一道：讀 037 SWRA／SYS2 之驗證性欄，以之為覆蓋分母之一。
    本線之用法：解凍時將 31 條 ER 與 SYS2 `Verification Criteria` 逐列對照（b(1) 之對照表同作）。
    **與 (e) 同為 ICS 線最值得帶去 PM／SU／DD 之二件**；正式提案待 Pei 指示後落於 `docs/fw036/`。

(e) **掃描起點盲區 73 列（21.9%）登記**：42 列節標題錨（FR 0）、
    31 列來源空白（FR 23）。其真實出處 `DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf`
    全 repo 查無 → **DR-ICS21**。

(f) **已綁 FDCAN8 載 `BO_TX_BU_ 1427 : ETM,LTM;`，與 A-ICS47／upstream-07 E3
    「二 DBC 皆無 DUT 發送側」相對 —— 登記，不調和**（A-ICS87）。
    若 LTM 為 `TELEMATIC_FD_4` 之追加發送方，則本 DUT 是 `$TGW_DISP_STAT$` 之**發源**而非觀察者，
    b03 八條「觀察 TGW_DISP_STAT」之前提可能反向。**這是解凍後第一批量測，非凍結期間之事**。
    併同：`DCSD_DISP_STAT` 與 `TGW_DISP_STAT` 是否同一訊號之不同側命名（§11-1-1）；
    佔位字面與 dbc 實名（`TGW_DISP_STATSts`／`PowerSts_Telematic`）及值名之不符（A-ICS88）。
    **DR-ICS16 維持 OPEN，判「部分」不採認**；PDT27 綁定待 A-DM14。

(g) `4819353`（§1.4 唯一 FR，implausible value 5／6 → last plausible／Sleep 後預設 ON）
    **登記為覆蓋缺口**，不生成。解凍後依 SYS2 分類與 (f) 之訊號命名結果再定。

(h) 作業 C 對「12 處佔位」之質疑**不成立**（漏計 `test_procedure` 欄；將訊號字面次數與佔位數混同），
    主實例已獨立複驗。**不登 anomaly**。主實例之複驗合式且必要。

(i) 下放包 13 §3 作業 B「列其來源文件為何」之前提不成立（SYS2 來源欄從不含文件名），
    為**分析層之誤**（A-ICS89）；執行層以 7 位 ID 解析作等價量測並具名代換，合式。

(j) **A-ICS80（R-ICS40 正本來源）維持 OPEN 待 Pei 答**，凍結不影響其狀態。
（分析層即裁，2026-08-30；upstream-13 §2-4、§3、§4、§10、§11）
```

---

## R-ICS44

```
R-ICS44（窗口式解凍：僅 b14；三件量測；不回填、不改寫）

成因：Pei 於 2026-08-30 連下二裁：
  ① 「BHCAN2」—— DR-ICS16 之匯流排取捨軸結，台架觀察點定為 BH-CAN2；
  ② 「需求只是一個大概，實際上要以 DBC 為主」—— 落為 **R-17**（全案）。
二裁合起使 b03 之 12 處佔位首次有回填之路，但三件前提未量。

(a) **R-ICS43(a) 之凍結開一窗口，範圍限於下放包 14**。
    b14 完工即自動回到凍結，**不需另一道裁定**；
    若要繼續（b15），須 Pei 另一字。

(b) **b14 為純量測包：零 TC 新生、零錨變動、零佔位回填、零步驟改寫。**
    理由：三件之一（發收方向）若成立，b03 八條之因果結構須反向，
    屆時回填之佔位全數白做 —— 同於 b08 若採 ② 之「無錨可重」。

(c) **三件之量測順序不得顓倒**：先 (c-1) 同一物、再 (c-2) 方向、後 (c-3) 綁定。
    理由：R-17(e) 明定「須先以 (c) 確認同一物，再談方向」——
    未確認同一物而談方向，等於拿另一個訊號之方向來判本訊號。

(d) **`FORMS.md` 與 `feature.yaml` 本包一字不改**。
    BHCAN2 之綁定繫於 A-DM14（跨 feature，`display` 線），
    b14 只量「綁定需要什麼、會動到誰」，**不綁**。
    Pei 裁「BHCAN2」是定台架觀察點，不等於已裁跨 feature 之檔案歸屬。

(e) **R-17 於本包只用於判定，不用於寫入**。
    即依 R-17(c) 三項出判定表，但不依 R-17(a) 改任何 TC 之實名實值。
    R-17(f) 之「既有 TC 回改逐 feature 裁」，於 ICS 之裁定待 b14 量完再作。

(f) 本條不解除 R-ICS43 之其餘拘束：五簿仍只寫本輪所列；
    G5 維持押後；A-ICS84（NRL-180522）、A-ICS80 維持待 Pei。
（分析層即裁，2026-08-30；Pei 裁「BHCAN2」「以 DBC 為主」「開」；R-17；A-ICS87／88／82）
```

---

## R-ICS45

```
R-ICS45（b14 之採認與上呈；回凍；世代錯配為下一優先）

成因：upstream-14。16 項相符、1 項不符（圓籬 diff 預期一條實為二條，
分析層之誤，A-ICS99）。E25 觸發；E22／E23／E24 未觸發，
惟 E22 字面涵蓋不到之一件範圍事項已具名呈報。

(a) **二訊號之同一物判定採認**：
    `$TGW_DISP_STAT$` ≡ `TGW_DISP_STATSts` ＠ `BO_ 1500 TELEMATIC_DISPLAY2`；
    `$Telematic_Power$` ≡ `PowerSts_Telematic` ＠ `BO_ 1470 STATUS_TELEMATIC`。
    **惟須逐案具名：本判定僅繫於 R-17(c) 項③一項**（項①② 不可比，A-ICS94）；
    日後取得載訊息名或位元佈局之規格件時，**須重驗**。

(b) **回凍**：b14 已完工，依 R-ICS44(a) 自動回到 R-ICS43 之凍結。
    回凍基準：`docs/reports/14_rulings_snapshot.md`（51 錨點）。
    **12 處佔位仍未回填** —— 回填須開 b15，屬 Pei。

(c) **回填之建議（上呈，不逕定）**：採執行層 §10-2 之分割 ——
    12 處佔位中，**不涉 TC 2／TC 4 者先填**；TC 2／TC 4 連同其前提問題押後。
    回填時 **值名須與訊號名同批改為 DBC 實值**（R-17(a)）——
    `DISP_OFF` → `Display_off`、`DISP_NORMAL` → `Normal_mode` 等；
    **不得出現「訊號名用 DBC、值名用規格」之混用**。
    同批複審 `(supporting observation)` 標記（A-ICS98）。

(d) **TC 2／TC 4 之前提可建立性：上呈 Pei，分析層不逕定**（A-ICS91）。
    **且不得推定其為「不可建立」** —— 規格 `4819144`／`4820117` 之主詞為 **ICS**
    （面板）而非本 DUT；而 TC 2／4 之前提是否以 CAN 輸入建立、
    或以 DUT 自身之電源模式建立，**本包未量**。
    b15 若開，須先量該二條現行步驟究以何法建立該前提，再談可否。

(e) **世代錯配為解凍後最高優先**（A-ICS93）：本 DUT 為 **R1L**，
    而已綁之二支 dbc 為 **R4／R5**、未綁之二支為 **R1**。
    前十四包之訊號解析皆建立於 R4／R5 上，**而該前提從未量過**。
    其優先序在 12 處回填之前 —— 若 R1 與 R4／R5 於本線已用訊號上有差，
    回填之值本身即可能錯。

(f) **A-DM14 無承載流程：上呈 Pei**（A-ICS92）。
    分析層建議二選一：① Pei 直接裁 BHCAN2 之檔案歸屬；
    ② 立一條跨 feature 争點之承載規則（登於全案台帳並向對造 feature 告知）。
    **分析層不逕裁**；惟具名：等待 A-DM14 不是等待一個進行中之程序。

(g) **只量不綁之實測採認**：本 feature 之六支讀 dbc 之腳本皆硬寫路徑，
    工具鏈層未阻。**唯一限制在條文面：未綁定之 dbc 不得採認入 TC**。
    回填屬「採認入 TC」，故 (c) 之執行仍繫於 (f) 之結果或 Pei 之單獨授權。

(h) `BHCAN2` 於 CFTS020 查無、規格只載 `BH-CAN`（A-ICS95）：**登記，不調和**。
    二者是否同一條匯流排，規格內無可判依據；併入 DR-ICS16 之後續。

(i) `FORMS.md` 二支已綁 dbc 無自身登錄（A-ICS96）、
    本 feature 之 10 個 sha 無程式比對（A-ICS97）：**工具面，登記**，
    不在本線修（跨 feature 且本線已凍）。

(j) `gate_all` 由四支紅變五支，新紅者 `lint_docs036` 之二項皆在
    `features/power/DATA_REQUESTS.md`（DR-PW23 缺結尾 `|`、序號跳號）。
    **非 ICS 所致。列為轉 PM 線之首件（一行可修）。**
（分析層即裁，2026-08-30；upstream-14 §2、§3、§4、§9、§10）
```

---

## R-ICS46

```
R-ICS46（Pei 裁：BHCAN2 歸屬確立；第二次窗口式解凍（b15））

Pei 於 2026-08-30 下二字：**「開」**、**「裁 BHCAN2」**。

(a) **BHCAN2 歸屬確立**（採 A-ICS92 之選項①）：
    `forms/PDT27_E2A_R1_BHCAN2.dbc` 確立為本 feature 可用之參考件，
    得**綁定入 `ics_management/feature.yaml`** 並**採認入 TC**。
    R-ICS44(d)「不逕裁」之拘束至此解除 —— 裁者為 Pei。

(b) **本裁定之射程限於 `ics_management`。**
    其**不裁** display 線之 A-DM14（R4 與 BHCAN2 之取捨），
    亦**不令** `display`／`vehicle_setting` 改用任何檔。
    理由：本線只問過「本 feature 可否用」，未問過「他線應否改」；
    以一個答案覆蓋一個未問之問，是 A-ICS83 同族之錯。

(c) **A-ICS92（承載流程）不因本裁定而結案**。
    本裁解了 ICS 之阻塞，但「跨 feature 争點無人承載」之結構問題仍在：
    `vehicle_setting`（R4 持有者）對 A-DM14 命中仍為 0，**從未被告知**。
    建議 Pei 順手向 display／vehicle_setting 二線告知本裁定之存在及其射程限制；
    **分析層不代為告知**（跨 feature 寫入非本線之權）。

(d) **綁定須有讀者（R-G40 之精神）**：本 feature 之 10 個 sha 現無程式比對
    （A-ICS97）。**綁入 BHCAN2 之同一包內須建立讀者**，
    否則只是把第 11 個無人讀之 sha 加進去。

(e) **第二次窗口式解凍，範圍限於下放包 15**（同 R-ICS44(a) 之形式）。
    b15 完工自動回凍；繼續須 Pei 另一字。

(f) **b15 之順序不得顓倒**：先世代錯配（A-ICS93）、再綁定（含讀者）、
    後回填。理由：若 R1 與 R4／R5 於本線已用訊號上有差，
    **回填之值本身即可能錯** —— 先填再發現，等於把錯值寫進交付簿。

(g) **回填範圍限於不涉 TC 2／TC 4 者**（R-ICS45(c)）。
    A-ICS91（TC 2／4 之前提可建立性）**Pei 未裁，維持上呈中**；
    b15 只量該二條現行步驟以何法建立該前提，**不改、不回填、不推定**。

(h) 回填時 **值名與訊號名同批改為 DBC 實值**（R-17(a)）；
    同批複審 `(supporting observation)` 標記（A-ICS98）。
    R-17(f) 之「既有 TC 回改逐 feature 裁」，於 ICS **限於本次回填所觸之列**，
    不擴及其他 TC。
（Pei 裁「開」「裁 BHCAN2」，2026-08-30；A-ICS91／92／93／97／98；R-17；R-G40）
```

---

## R-ICS47

```
R-ICS47（E26 之放行；A-ICS91 之論據崩解；Pre-Condition 未寫建立法非缺陷）

成因：upstream-15。E26 觸發，執行層依令停下、未自行判斷是否足以放行 —— **合式且正確**。

(a) **E26 放行。** 其立法理由為「綁定與回填皆以**訊號解析正確**為前提」，
    而實測已證該前提成立：17 個已用訊號之**起始位元、長度、字節序、
    factor／offset、值域、單位、`VAL_` 列舉於四支 dbc 中 17／17 全數相同**；
    交付欄受影響 **0 條**。實際觸發者為 `reasoning` 中一行引述過時（A-ICS100），
    性質不同且較輕。**b15 之量測不需重做；作業 B／C 得於下一包直接執行。**

(b) **E26 之措辭為分析層之瑕疵（A-ICS101）**：其判定面寫作
    「任何一條既有 TC 受影響」，而其立法理由只涉**交付欄**。
    二者不對齊，致一條較輕之瑕疵停了整包。
    **拿法：今後 E 條件之判定面須與其立法理由逐字對齊**；
    若理由只涉交付欄，判定面不得寫「任何一條 TC」。
    **惟不追究執行層** —— 其依字面停下且不自行放行，正是 E9 所要求之行為。

(c) **A-ICS91 之論據崩解（A-ICS102，分析層之誤）**：
    其所據之 `4819144`／`4820117`（主詞 ICS 面板、內容為 Diagnostics 之啟閉）
    **於 31 條之 `specification_reference` 中命中 0**，未被任何 TC 引為錨；
    而 TC 2／TC 4 之錨實為 `4819561`／`4819564`，**主詞為 HU（本 DUT）**。
    分析層於審 upstream-14 時接受其 §3-3 之舉證而**未複驗該二物件是否為該二條之錨**。
    **A-ICS91 之論據須重新指認**；其核心觀察（於 BHCAN2，`ICS` 不在 `BU_` 內、
    本 DUT 為 `PowerSts_Telematic` 之發送側）**仍成立**，惟其對 TC 2／4 之漢意已失。

(d) **「Pre-Condition 未寫建立法」非缺陷**（答執行層 §10-1-2 之未驗項）：
    IN §4.4 定 Pre-Condition 為**起始狀態／環境**，且**明禁寫入動作**；
    其所舉合式例（`Bluetooth is enabled.`）同樣不附建立法。
    故 TC 2／4 之 `Telematic Power is in the "Full_Operation" state` 合乎體例，
    **不是缺陷，不需回改**。
    A-ICS91 之關切因此自「TC 缺陷」轉為「**台架可行性**」—— 後者仍屬 Pei，
    惟**不阻斷其餘 TC 之回填**。

(e) **A-ICS93 改述**：「世代錯配」之命名誤導。實測：
    差異不在世代而在**匯流排族**（BHCAN vs FDCAN）；15 個訊號同時存於
    A(R1)與 B(R4) 二支 BHCAN，只是不在二支 FDCAN。
    **數值面風險（位元佈局、值域、`VAL_`）經量測不成立**；
    剩下之實質差異只有發收方，而那是閘道轉發之必然（同一鍵之上下游二段）。

(f) **`reasoning` 三條之過時引述須更正**（A-ICS100）：
    b03 三條逐字引 B 檔（R4_BHCAN）之 `SG_ RQ_DISP_INTS ... DCSD` 並斷
    「發送節點為 SGW 而非 ICS」；而於 Pei 所裁之 A 檔，其為 `ETM`→`SGW`。
    **更正限於 `reasoning` 三條，不及交付欄**（交付欄受影響 0）。
    更正時須同時註明所據之 dbc 檔名，以免再次發生同型過時。

(g) **DR-ICS8 維持 OPEN，不標可結**（採執行層 §10-2）：
    其缺件（訊號實體）知識面已完備，但 12 處佔位一處未回填。
    標可結而佔位仍在，會使 `pending_census` 與 DR 台帳互相矛盾。

(h) 本條**不自行開第三次窗口**。R-ICS46(e) 明定 b15 完工自動回凍、
    繼續須 Pei 另一字。本條只確立「一旦開，作業 B／C 直接執行，
    不需重做 b15 之量測」。**現狀：已回凍，基準 `15_rulings_snapshot.md`（53 錨點）。**
（分析層即裁，2026-08-30；upstream-15 §2、§4、§9、§10；IN §4.4）
```

---

## R-ICS48

```
R-ICS48（第三次窗口式解凍：b16；回填範圍擴至 TC 2／4）

Pei 於 2026-08-30 下「開」。

(a) **第三次窗口式解凍，範圍限於下放包 16**（同 R-ICS44(a)／R-ICS46(e) 之形式）。
    b16 完工自動回凍；繼續須 Pei 另一字。

(b) **作業 B／C（b15 未執行者）直接執行，不需重做 b15 之量測**（R-ICS47(a)）。

(c) **回填範圍擴至 TC 2／TC 4**，變更 R-ICS46(g) 之限制。
    理由：R-ICS47(d) 已判「Pre-Condition 未寫建立法」非缺陷（IN §4.4）；
    A-ICS91 之論據已崩解（A-ICS102）。二條之佔位與其他十處同質，
    皆為 `$TGW_DISP_STAT$` 之訊號實體缺件。
    **惟二條之台架可行性（A-ICS91 殘餘面）維持 OPEN**，不因回填而結案。

(d) **綁定與讀者須同包**（R-ICS46(d)／R-G40）：
    無讀者之綁定不得交付 —— 實作未完則綁定不算數。

(e) **`reasoning` 過時引述之更正限於三條**（A-ICS100），不及交付欄；
    更正時須註明所據之 dbc 檔名。

(f) **其餘 29 條之 Pre-Condition 體例抽查為「只量不改」**。
    依 R-ICS47(d)，「未寫建立法」本身非缺陷；
    本項只為量其是否為全批體例（執行層 §10-1-1），**不得因量測結果而改任何 TC**。

(g) A-ICS105（`Radio_btn0` 收方僅 `LTM`）、A-ICS104（R5 只貢獻 2 個）
    **本包不排入**，維持登記。
（Pei 裁「開」，2026-08-30；R-ICS47(a)(d)；A-ICS100／102／103；R-G40）
```
