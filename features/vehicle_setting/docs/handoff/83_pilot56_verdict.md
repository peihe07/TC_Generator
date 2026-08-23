# 83 下放包 — pilot #5＋#6 之建議分類、55 輪

分析層寫入，2026-08-23。**18 條逐條讀畢。建議：不通過，五項 defect。**

母本已寫入 243 列（`d5d2d3af…`），完整性檢查 237 ＝ 219 ＋ 7 ＋ 11。

---

## 1. 覆核前之三項確認

| 項 | 確認 |
|---|---|
| **§2.1「232」為重複計數** | **成因在我**。上繳 46 §2.3 之 225 已含 probe 7，§2.4 又報其「不在來源集內」——**兩節各自為真而併讀致誤**，我未回頭量母體即據以定 232。**交付基準 225 不變**（實測 225／219 leaf） |
| **§2.2「七項全數持平」之誤導** | **自陳正確**。x14 之持平值為 **0** —— 一個已失去者持平在失去之狀態。**「無下降」不等於「無損」**，該表述三輪未改，於此更正 |
| **§2.3 併列子形態是判準遷就數字** | **自陳正確且重要**。G6 之 `PowerMode` 與 `DriverSide` 觸發訊號不同、標的不同，**無理由併為一個子形態** —— 其併列係為對齊「八」。G 型實為**九子形態**（含 G1） |

---

## 2. pilot #5＋#6 之逐條分類

| # | leaf | 判 |
|---:|---|---|
| 1 | `HeatedSteeringWheel-004` | **defect D-1** |
| 2 | `HeatedSteeringWheel-008` | **defect D-2** |
| 3 | `LeftFrontHeatedSeat-010` | **defect D-3** |
| 4 | `HeatedSteeringWheel-013`（G5） | pass |
| 5 | `SwitchLHD/RHD-010` | **defect D-3, D-4** |
| 6 | `ThirdRowHeadrestDump-029` | pass |
| 7 | `ScreenOFF-048` | pass |
| 8 | `Stop-StartSystem-006` | **defect D-2** |
| 9 | `HeatedSteeringWheel-013`（D 型） | pass |
| 10 | `HeatedSteeringWheel-014` | pass |
| 11 | `ThirdRowHeadrestDump-027` | **defect D-5** |
| 12 | `SwitchLHD/RHD-013` | **defect D-3, D-4** |
| 13 | `RightFrontHeatedSeat-024` | **defect D-1** |
| 14 | `RightFrontHeatedSeat-033` | pass |
| 15 | `HeatedSteeringWheel-012` | pass |
| 16 | `HeatedSteeringWheel-019` | pass |
| 17 | `RightFrontVentedSeat-028` | pass |
| 18 | `RightFrontVentedSeat-033` | pass |

**pass 11／defect 7（涉 5 項）。** Priority 判定 18/18 pass。

### D-1 —— procedure 含不可執行之步驟（#1／#13，母體 G2 共 9 條）

```
2. Send CAN: STATUS_CSWM.HSW_STATSts = a value outside the declared valid set
```

**測試員無從執行** —— 其非值而為描述。ER 已標 `PENDING: DR-18`，
**而 procedure 未標**，致步驟不可執行且與 ER 不一致（§5.1／§6）。

**修法**：procedure 該步驟亦標 `PENDING: DR-18`，其前後步驟照寫。

### D-2 —— pre_condition 與 procedure 重複設定配置（#2／#8，母體 G3／G4／G8 共 10 條）

```
Pre-Condition 1. The vehicle is an electrified vehicle
Procedure     1. Set PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle)
```

**同一配置兩處各述一次**，違 §4.5 之欄位歸屬。
**80 包 §1 已對 `-021` 判此 defect 並令刪 pre_condition，該修正未推廣至 batch23。**

**修法**：刪 pre_condition 之該條，餘項重編號。

### D-3 —— ER 為 `PENDING` 而 procedure 已寫 check target（#3／#5／#12）

```
Procedure 3. … and check that the left front heated seat switch is greyed out
ER        3. PENDING: DR-19
```

**§6 之 1:1 不成立**，且該 TC 執行時無通過條件。

**且不確定之處不在步驟 3**：步驟 3 之觀察（灰階與否）可觀察；
不確定者為「所送之 `EngineSts = 0` 是否滿足條文之 `$EngRun_Stat$ <> [四值]`」——
**其為前提之不確定，非結果之不可觀察**。

**修法**：ER 3 寫可觀察斷言（`The … switch is greyed out`），
**AH 增註**「條文之條件為 `$EngRun_Stat$` 之四值，其與所送 `EngineSts` 之對應待 DR-19」。

### D-4 —— 最弱斷言未套用（#5／#12，母體 `screen_pending = yes` 16 條）

```
Procedure 3. … check that the seat control layout differs from Layout_LHD
ER        3. PENDING: DR-5-B
```

**「有無變更」本身可驗** —— 72 包 §1 之最弱斷言裁定（R-VS59(4) 之細化）
**未套用至 batch23**。

**修法**：ER 3 ＝ `The seat control layout differs from Layout_LHD`；
具體版面待補仍以 AH 承載。

### D-5 —— `test_item` 上半段非逐字（#11）

| | |
|---|---|
| 來源 `4858988` | `The Third Row Headrest Dump Softkey button **will also be** accessible from the Rear View Camera screen, **if applicable**.` |
| test_item | `The Third Row Headrest Dump softkey **shall also be** accessible from the Rear View Camera screen, **when supported**.` |

**`will` → `shall`、`if applicable` → `when supported`、`Softkey button` → `softkey`** ——
**三處改寫，違 R-VS6**（上半段須為 037／條文之**逐字**）。

**該條為 50 輪 W-143 之拆分產出**（`batch02_v5`），
**拆分時改寫了上半段** —— 拆分只應窄化其實體，不得改其文字。

**修法**：上半段回復條文逐字；拆分之窄化改記於括號內之下半段。
**並全母體掃同型**：`split_flag = true` 之 7 條，其上半段是否皆為逐字。

### note —— #5 與 #12 內容完全相同而未標 `duplicate_of`

`SwitchLHD/RHD-010`（`4858560`）與 `-013`（`4859509`）之
tc_title／pre_conditions／procedure／ER **逐字相同**，其來源條文亦逐字相同。

**其為 A-VS119 型冗餘之新實例。** 依 §8.2.2 不得合併（兩個 leaf），
**惟應標 `duplicate_of`**（§10.6）以使覆核者可辨。

---

## 3. 55 輪指令

```text
你是 FW036 管線之執行層。repo: /Users/peihe/Work_Projects/TC_Generator
第 55 輪。**pilot defect 之修正 → 重寫回。**

讀：docs/handoff/83_pilot56_verdict.md（本輪依據）＋ RULINGS.md
    ＋ docs/handoff/66_writeback_procedure.md

## 文書
D-1  建 docs/upstream/48_pilot_fix2.md，六節先留空。
D-2  依 R-VS35 分線列兩數。D-6 骨架對照。
D-3  ANOMALIES.md 新開 **A-VS161**（拆分時改寫 test_item 上半段，違 R-VS6）。

## 作業（三項）

W-157  **五項 defect 之全母體修正**
       D-1 procedure 之不可執行步驟標 `PENDING`（G2 型，母體 9 條）
       D-2 刪 pre_condition 之重複配置（G3／G4／G8，母體 10 條）
       D-3 ER 之 `PENDING` 改可觀察斷言 ＋ AH 增註前提之不確定
       D-4 `screen_pending = yes` 者套最弱斷言（母體 16 條）
       D-5 `split_flag = true` 之 7 條，其 test_item 上半段**逐字比對條文**，
           不符者回復；窄化改記於括號內
       note `-010`／`-013` 標 `duplicate_of`
       **錨點（R-VS54，須可失敗）**：修正前之版本須各報出其違規數
       §9 十七項自檢 ＋ 固定錨點 20 項

W-158  **R-VS76 完整性檢查**（修正後重跑）
       三類之和須為 237

W-159  **重寫回**（依 R-VS70／R-VS72）
       寫前另備份 `REF/036_pre_fullwrite3_<YYYYMMDD>.xlsx`；
       XML 外科式；寫前後 raw XML 七項比對；重讀逐列比對十六欄；
       **必列**：總列數、x14 之值（現為 0，**其為已失非本輪所致**）、
       實寫後 sha256、**x14 修復所需之範圍**（依實際資料列）

## 禁區
git 不執行。不補素材、不代擬條文。各版保留不刪。
不得以 openpyxl 存檔 xlsx。**不得改寫 test_item 之上半段**（R-VS6）。

## 升級條件
W-157 之任一錨點未報出違規；
W-157 之 D-5 掃描發現逐字不符者 > 2（則拆分之改寫為系統性）；
W-158 之三類和 ≠ 237；
W-159 之七項任一下降／重讀比對不符。
```

---

## 4. 其後

| 輪 | 內容 |
|---|---|
| 55 | defect 修正 → 重寫回 |
| **56** | **交付**（工作簿 ＋ `DELIVERY.md`） |

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| pilot #5＋#6 之分類 | **不通過**；pass 11／defect 7（五項）；Priority 18/18 pass | 分析層 → **待 Pei 覆核** |
| D-3 之處置 | 不確定在前提者，ER 寫可觀察斷言，前提之不確定以 AH 承載 | 分析層 |
