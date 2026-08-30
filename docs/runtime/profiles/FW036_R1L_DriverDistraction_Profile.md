# FW036 R1L — Driver Distraction Profile

Feature slug：`driver_distraction`　Test Group：`Driver Distraction`（R-DD1）
狀態：**ACTIVE**（Pei 2026-08-27 裁准，來源下放包 04 §二）
runtime 讀法：本檔之 `[OVERRIDE §x]` 勝出於 IN 之同節；無 override 者依 IN。
落檔註記（2026-08-27 更正）：本檔首次寫入即成功，僅 MCP 回應遺失；
前一版註記所述之「ENOENT 後重寫」對本檔不成立（該情形發生於下放包 04，非本檔）。
該行非分析層所寫，成因未量測，依 A-DD4 處理。

---

## §1 spec_reference —— IN §10.7(a)，**無 override**

形制 `CFTS022-{ObjectID}`，ObjectID 為 CFTS022 SYSRA `Basic Report`
之 7 位 Polarion 號，逐字查得（spec_mode D）。

- **一行一 ObjectID**，前綴逐行重述，禁 `,`／`、`／`;` 串接（IN §10.7）
- 同一 TC 內升冪
- 雙引 leaf（`-017`~`-028`）：HK 章閘 `CFTS022-4915120` 一行，
  ＋ 條文 ObjectID 一行

ObjectID 對照（15 列，逐字自 `Basic Report`）：

| SYS-RA | ObjectID | | SYS-RA | ObjectID |
|---|---|---|---|---|
| -113 | 4915104 | | -125 | 4915120 |
| -114 | 4915105 | | -126 | 4915121 |
| -115 | 4915106 | | -127 | 4915122 |
| -116 | 4915107 | | -128 | 4915123 |
| -117 | 4915108 | | -129 | 4915124 |
| -118 | 4915109 | | -132 | 4915128 |
| -120 | 4915112 | | -133 | 4915129 |
| -121 | 4915115 | | | |

本 feature **無 HMI Logic and Flow 家族之 spec_reference 行** ——
HMI spec 為 ER 錨之素材（§2），非追溯錨；不得寫入 N 欄。

---

## §2 ER 之斷言錨（R-DD3(c) 之細則）

### 2.1 觀察面 A（主錨）—— 存取阻擋

對 Lockout Table 標 `L/O` 之 feature 發起存取，ER 斷言該 feature
未被開啟／存取被阻。

- 取樣 feature **於 TC 內具名**（例：`Destination Entry`、
  `Pairing (1st time)`、`Reconfigurable menu bar`）；
  **禁寫** `some restricted feature`／`a locked-out feature` 等泛稱
- 取樣以 HMI spec p7 `Driver Lockout Tables` 為準，並受其註記拘束：
  黃標項不適用 R1L；Embedded NAV 僅 LATAM；VR/TTS 僅隨 Embedded NAV
  存在。**黃標項不得取為樣本**

### 2.2 觀察面 B —— lockout 通知

`Standard Lockout Popup`，字串逐字取 HMI spec p4：

```
Feature not available while the vehicle is in motion.
```

ER 引用時以 `"..."` 雙引號包覆（IN §11）。

### 2.3 降階規則（R-DD3(b) 落地）

- 軟體層敘述（`notifies the subscribed Listener`、
  `DD Service outputs RESTRICTED`、callback 之送達／時序／參數）
  **一律不入 ER** —— 非 SWQT 觀察面
- `RESTRICTED`／`NOT_RESTRICTED`／`Locked`／`Unlocked` 四詞
  **不得出現於 ER**（A-DD3 已結）
- `test_item` 上半 verbatim 照 037 原文，**含上述詞彙者不改字**
  （上半為需求原句，非斷言）

### 2.4 §8.4.2 界線（硬）

下列皆為 HMI spec 自有需求，**非本 28 leaf 所有**：

- PC1–PC4（駕駛/乘客安全帶、乘客座佔位偵測、Level 3 ADAS 狀態）
- 乘客確認 popup 流程（`Are you the passenger?` 之 No/Yes 分支）
- UF1／UF2（解鎖之 per-key-cycle 限制、前提不再滿足即復鎖）
- Fullscreen Lockout 之 ADAS 有無兩版決策分支（spec p5／p6）

**TC 不得引入其邏輯、不得以其為 Pre-Condition、不得斷言其分支結果。**
Fullscreen Lockout 畫面僅得作 reaction presence 錨
（「lockout 畫面顯示」），不得斷言其分支決策之正確性。

### 2.5 IN §11 方括號例外之啟用（R-DD12）

依 IN §11 之 Exception（profile-scoped），本 feature **啟用**之：

- `test_item` **上半**（需求原句 verbatim）中源自 037 之方括號記法
  （`Case [Normal]`、`Case [Exception]`、`$VC_Trans_Equipped$ = [Manual]` 等）
  **保留原樣** —— 改寫即違 R-S4 之逐字
- 例外**僅及於上半**。括號下半（作者所書之測試目的）與四欄
  （`pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`）
  一律用 `"..."`，不得出現方括號；唯一例外為裁決所命之
  `[ASSUMPTION A-DDn]` marker（標記，非 UI 標籤）
- lint／自檢對 `test_item` 之方括號，以「該 token 是否為所引來源列之逐字」
  為判準（比對 037 原文），非一律禁

### 2.6 引號內字串之終端標點（R-DD11）

IN §11 之「無行尾句號」規制作者所書句末之標點；逐字引用之 UI 字串，
其自身之終端標點屬該字串之一部，**保留**。
判準：移除引號後，該 item 是否以作者之句點結尾。是即違規。
合規例：`... showing "Feature not available while the vehicle is in motion."`

---

## §3 訊號與參數寫法（IN §8.7.5）

> **解除記錄（2026-08-28，下放包 08 §六）**：前版 SUSPENDED 標記針對
> `$Speedometer$`／`$VC_Trans_Equipped$`／`$PresentGear$` 三列，成因為分析層
> 取 Powernet 欄名而未回驗其存在於綁定 DBC，及引 LID 漏標分頁而指錯列。
> 現 `$Speedometer$`／`$PresentGear$`／`$Country_Code$` 三列已依實測回填而解除；
> **`$VC_Trans_Equipped$` 現為 CONDITIONAL**（R-DD19 乙案；下放包 15），非 SUSPENDED。
> 本節寫法依 R-DD6 v2、R-DD7、R-DD9、R-DD10。

| 037 之 `$…$` | 施加路徑（逐字） | 寫法 | 狀態 |
|---|---|---|---|
| `$Speedometer$` | `LID CAN Mapping r1738 [Atlantis High 欄]` → `STATUS_CCAN3.VehicleSpeedVSOSig`（`PDT27_E2A_R4_BHCAN.dbc`、msg 994、13 bit、factor `0.0625`、offset `0`、`Km/h`） | `Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = <raw> (<km/h>)`（R-DD9(b)）；失效值 `= 8191 (SNA)`（R-DD9(c)） | **解除** |
| `$PresentGear$` | `LID CAN Mapping r1397 [Atlantis High 欄]` → `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT`（`PDT27_E2A_R5_FDCAN8.dbc`、msg 263、5 bit、factor `1`、offset `0`） | `= <raw> (<VAL_ 逐字>)`（R-DD9(a)）；Park = `12 (Park)` | **解除** |
| `$Country_Code$` | `LID Proxi & Configuration r43 [Atlantis & Atlantis High 欄]` → `Car_Configuration_16.Country_Code`（PROXI `Format` r468、byte 107、bit 0–7） | `PROXI Country_Code = 91`，**不加 `$`**（§8.7.5(c)）；確定值，A-DD5 已撤（DR-DD3 RESOLVED，下放包 13 §二） | **解除** |
| `$VC_Trans_Equipped$` | **CONDITIONAL（R-DD19，乙案）** —— 依 LID `Proxi & Configuration` r421 [Atlantis 欄] 採 PROXI `Gear_Box_Type`（`Powertrain_Configuration_4`、byte 101、bit 0–2）；DR-DD5／DD6 必發不變 | `PROXI Gear_Box_Type = 1 (MTX)`（[Manual]）／`= 4 (ATX)`（[Automatic]），不加 `$`；用及者標 `[ASSUMPTION A-DD8]` 與 `[ASSUMPTION A-DD9]`；**MTA（2）／DDCT（3）不得入任何 TC**（R-DD19(c)） | **CONDITIONAL** |
| `$PARK_BRK_EGD$` | **R-DD18 已採勘誤** → 施加名 `PARK_BRK_EDG`（`LID CAN Mapping r1310`，A 欄全分頁唯一）。二架構欄不同字，依 R-DD6 v2(b) 取 `[Atlantis High 欄]` → `BCM_FD_9.ParkBrakeSts`（`PDT27_E2A_R5_FDCAN8.dbc`、BO_ 1066、1 bit、`180\|1@0+`、CAN-FD） | `Send the signal $BCM_FD_9.ParkBrakeSts$ = <raw> (<VAL_ 逐字>)`（R-DD9(a)）；`0 (OFF)`／`1 (ON)`。test_item 上半 verbatim 仍照原文 `$PARK_BRK_EGD$` 不改字（R-DD18(b)）；用及施加路徑者標 `[ASSUMPTION A-DD2]` | **解除** |

> **備援路徑（R-DD13(d)）**：`STATUS_BH_BCM1.ParkBrakeSts`
> （`[Atlantis 欄]`、CAN-B、`PDT27_E2A_R4_BHCAN.dbc` BO_ 854、1 bit、`VAL_` 逐字相同）。
> 二名**皆在綁定庫中**，R-DD13(a) 之篩在此篩不掉任一個，
> 取捨**完全**由 R-DD6 v2(b) 承擔。台架若無 CAN-FD，**須先報再換**，不得逐自替代。

### §3.1 速度門檻之 raw（R-DD7）

| spec 門檻 | km/h | raw（未取整）| **採用 raw** | 實值 |
|---|---|---|---|---|
| ≥ 5 MPH 上鎖 | 8.04672 | 128.74752 | **129** | 8.0625 km/h = 5.0097 MPH |
| ≤ 3 MPH 解鎖 | 4.828032 | 77.248512 | **77** | 4.8125 km/h = 2.9903 MPH |

BVA（IN §12）：上鎖側 `128`（不應鎖）／`129`（應鎖）；解鎖側 `77`（應解）／`78`（不應解）。
**凡用及本表之 TC 須標 `[ASSUMPTION A-DD6]`**（R-DD7(f)）。

### §3.2 fail-safe 之形態

`VehicleSpeedVSOSigFailSts` 於綁定之二 DBC **皆不在**（上繳包 04 T10c）。
故 AC2 之「訊號失效」以 **SNA（`= 8191 (SNA)`）** 或 **匯流排逾時** 表現；
**何者適用逐 leaf 依 037 AC2 原文定**，本 profile 不統一指定（統一即造值）。

---

## §4 priority（Pei 2026-08-27 裁准）

規則：

```
PR-a  進鎖方向之常態路徑（RESTRICTED 之施加或其 HMI 強制，常態輸入）→ P0
PR-b  fail-safe 例外路徑（輸入失效 → RESTRICTED）→ P1
PR-c  解鎖方向常態、初始化、監看能力 → P1
本 feature 無 P2/P3。
```

P0（8）：007, 009, 011, 013, 015, 019, 023, 025
P1（20）：001, 002, 003, 004, 005, 006, 008, 010, 012, 014, 016,
017, 018, 020, 021, 022, 024, 026, 027, 028

閉合 8 + 20 = 28 ✅。025／026／027／028 已依 **R-DD25(b)** 判為**範圍外**，
其 priority 保留於本表僅為 28 之閉合計數之用，**不導致任何 TC 之生成**。
實際指派之 P0 為 7（007, 009, 011, 013, 015, 019, 023）、P1 為 17，合 24。

---

## §5 凍結與未結

| 項 | 範圍 | 狀態 |
|---|---|---|
| A-DD1／DR-DD1 | leaf 025–028 | **範圍外（R-DD25(b)）**，不生成 TC。依據三：`-132`／`-133` 屬 CFTS022 LATAM 章；SYSAD 載速度遲滯為 `JudgmentProcessorType4to6 … for LATAM`；Pei 2026-08-28 裁定本案只做 NAFTA、不做 LATAM。A-DD1 改 **`CLOSED-BY-SCOPE`**（**非以 DR 回覆結案**）；登 [CG-DD2]。DR-DD1 改為確認件，必發但不阻斷 |
| A-DD8／A-DD9（R-DD19） | leaf 017–024 | **解凍生成**，雙 marker；DR-DD5／DD6 回覆後撤或換值 |
| A-DD2／DR-DD2 | leaf 021–024 | 不阻斷。施加名依 **R-DD18** 已採勘誤為 `PARK_BRK_EDG`（→ `BCM_FD_9.ParkBrakeSts`，見 §3）；`test_item` 上半 verbatim 仍保留 `$PARK_BRK_EGD$` 不改字；用及施加路徑者標 `[ASSUMPTION A-DD2]`，上游正式更正後撤 |
| framework 組 6 | `Market Speed Gating` | **OUT OF SCOPE（R-DD25(b)）**。組名保留（其為 037 分組之事實，刪之則 28 之閉合無從交代），**不寫入工作簿任何列** |

---

## §6 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-27 | 初版 ACTIVE：§1–§5 定案 | Pei 裁准；下放包 04 §二 |
| 2026-08-28 | **範圍裁定（R-DD25）**：Pei 裁定本案只做 NAFTA、不做 LATAM；Hong Kong 在案內之依據為**右駕（RHD）**而非區域 —— `Market Config - R1` c14（`Right-Hand Drive vs. Left-Hand Drive`）載 HONG KONG r97 = RHD，與 UNITED KINGDOM r216 同；其 Region（c16）為 APAC。故 `-025`~`-028` 轉**範圍外**（§5），`-017`~`-024` 維持在案。同輪依 §2.4 拘束全帳 grep 過期陳述，更正 §3 首註之 SUSPENDED、§4 之凍結註、§5 之組 6 列 | Pei 2026-08-28；下放包 20 |
| 2026-08-28 | §3 之 `$PARK_BRK_EGD$` 列（含備援路徑段）**非分析層所寫** —— 分析層最後一次編輯將該列設為「待 T19c」，回讀時已為回填態；執行層上繳包 10 §8.3 載 profile「未開」。內容經分析層覆核與 T19c 實測相符而**保留**，來歷未量測，依 **A-DD4** 處理。Pei 2026-08-28 重申分工不變：**profile 由分析層回填**。同日發現 §5 未隨之同步（仍書「訊號名保留 EGD」），已由分析層更正 | A-DD4；Pei 2026-08-28 |
