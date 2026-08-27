# FW036 R1L — Driver Distraction Profile

Feature slug：`driver_distraction`　Test Group：`Driver Distraction`（R-DD1）
狀態：**ACTIVE**（Pei 2026-08-27 裁准，來源下放包 04 §二）
runtime 讀法：本檔之 `[OVERRIDE §x]` 勝出於 IN 之同節；無 override 者依 IN。
落檔註記：首次寫入於 MCP 逾時中失敗（get_file_info 驗 ENOENT），本檔為重寫，同稿。

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

---

## §3 訊號與參數寫法（IN §8.7.5；LID 對應自上繳包 01 T6）

| 037 之 `$…$` | 施加路徑 | 寫法 |
|---|---|---|
| `$Speedometer$` | LID r1738 → `GW_C1.VEH_SPEED`（CAN-B） | `Send the signal $GW_C1.VEH_SPEED$ = <raw> (<label>)` |
| `$VC_Trans_Equipped$` | LID r421 → `VehCfg7.VC_Trans_Equipped` | 同式 |
| `$PresentGear$` | LID r1397 → `GW_C1.Gr` | 同式 |
| `$PARK_BRK_EGD$` | **DR-DD2 未結** | 依 §8.7.5(d) 保留來源名：`Drive PARK_BRK_EGD from <值> to <值>`；**不得代以 `PARK_BRK_EDG`**（R-DD5、R-13）。定名後改 CAN 式 |
| `$Country_Code$` | LID r43 → `Car_Configuration_16.Country_Code` | `PROXI Country_Code = <值>`，不加 `$`（§8.7.5(c)） |

- `<raw>`／`<label>` 逐字取 DBC `VAL_` 列舉（T9a 實測後填入本表）
- 5／3 MPH 為 spec 具名門檻（§8.7.1）；**raw 編碼一律查得，
  不得由 MPH 自行換算臆填**（§8.4.1）。換算須 factor/offset 有據且經分析層覆核
- T9 結果到位前，相關欄位寫 `PENDING: DR-{n} <缺件名>`（§8.4.3），不留空

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

閉合 8 + 20 = 28 ✅（025／026／027／028 凍結中，priority 為草案值，
DR-DD1 裁後若改市場歸屬，priority 不因此變 —— 規則以方向判，非以市場判）

---

## §5 凍結與未結

| 項 | 範圍 | 狀態 |
|---|---|---|
| A-DD1／DR-DD1 | leaf 025–028 | **凍結**，不入任何批次 |
| A-DD2／DR-DD2 | leaf 021–024 | 不阻斷；訊號名保留 `$PARK_BRK_EGD$` |
| framework 組 6 | `Market Speed Gating` | 佔位名，**不寫入工作簿任何列** |

---

## §6 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-27 | 初版 ACTIVE：§1–§5 定案 | Pei 裁准；下放包 04 §二 |
