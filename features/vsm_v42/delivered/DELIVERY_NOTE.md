# 交付說明 — Vehicle Setup Management R1 Low（VF665 V42）b1

交付日：2026-09-02　授權：Pei「出貨」（R-VL25(b) 預授權 ＋ 本次明示）

| 項 | 值 |
|---|---|
| 交付檔 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleSetupManagementR1Low_20260902.xlsx` |
| sha256 | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6` |
| 來源 | `features/vsm_v42/sandbox/b1/candidate_vsm42_b1.xlsx`（`copy2`，sha256 相等） |
| Test Group | `Vehicle Setup Management R1 Low`（R-VL3） |
| Test Set | `EPB Maintenance Mode` |
| 列 | 10–26（**17 列**） |
| TC ID | `NR1L-VSM42-001` … `NR1L-VSM42-017`（R-VL3） |
| 檔名依據 | R-VL3（`{FeatureName}` ＝ Test Group 去空白，無尾綴） |

---

## 一、交付範圍與**未涵蓋之範圍**

**本件只含母體之一個 Test Set。**

| 項 | 數 |
|---|---|
| 本線母體（R-VL4：兩份 037 之 Functional leaf） | **128** |
| **本件所含** | **17**（`EPB Maintenance Mode`） |
| **尚未交付** | **111**（其餘九個 Test Set） |

Layer 2 之十組與其 leaf 數見 `features/vsm_v42/framework.md`（R-VL17 鎖定）。
`Park Sense`（18 條）已生成於 `generated/b2_park_sense/`，**尚未寫回、未交付**。

**另外，SYSRA 之 Functional 318 列中 191 列無 037 覆蓋，依 R-VL4 不入本線範圍**
（覆蓋揭露見 DR-VL1）。

## 二、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| **DR-VL1** | V42 SYSRA Functional 318 列中 **191** 列無 037 覆蓋（覆蓋揭露） | no | 已登記，**未送出**（Pei 裁先不送） |
| **DR-VL2** | 037／SYSRA 標註完整性三面：037 1 列 `Categorization` 空；SYSRA Functional 112 列 `EE Architecture` 與 `Document ID` 同時為空；037 leaf `-063` 之 Source ID 於 SYSRA 為 `Heading` | no | 已登記，**未送出** |
| **DR-VL3** | ATL-Mi（P637／CAN-B／CAN-C）之 DBC | — | **結案**（2026-09-02 到件，R-VL14） |
| **DR-VL4** | 三個內部訊號之驅動與觀察方法（見第三節） | 影響 3 條 TC 之 2 欄 | 已登記，**未送出** |

## 三、本件之未驗證性質（**逐項揭露**）

### 3.1 PENDING —— 6 格，3 條 TC

| TC ID | req_id | 內部訊號 | 欄 |
|---|---|---|---|
| `NR1L-VSM42-015` | `SWE1-VC-EPBMaintenanceMode-058` | `EPB_MaintenanceMode_Active.Info` | Procedure ＋ ER |
| `NR1L-VSM42-016` | `SWE1-VC-EPBMaintenanceMode-059` | `ServiceMode_Popup_Trigger.Info` | Procedure ＋ ER |
| `NR1L-VSM42-017` | `SWE1-VC-EPBMaintenanceMode-060` | `TLM_Vehicle_Setup_Menu.Info` | Procedure ＋ ER |

三者於 `data/signal_chain_v42_v3.tsv` 皆為 **未解得（止於段 1）** ——
LID／HMI Settings List／PROXI 三處之段 1 皆無依據。
依 **R-P355(c)** 不得以 `Set X.Info` 假裝可執行，故該步寫 `PENDING: DR-VL4 <訊號名>`。
**三條 TC 之其餘步驟仍可執行**（上游 CAN 訊號與具名 UI 元件皆可觀察）。

### 3.2 訊號值無 `VAL_` label —— 9 條 TC、11 個賦值

主 DBC（`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`）之
`VAL_ 1486 EPB_Maintenance_Fdbk` **只定義 `0 "Initialization"` 與 `31 "SNA"`**；
規格所用之 **2／3／4／5／6／8／9／10／11 九個值無 label**。
`STATUS_CCAN3.VehicleSpeedVSOSig` 為物理量（13 bit、factor 0.0625、`Km/h`），
其 `VAL_` 只有 `8191 "SNA"`，本件所用之 raw **64／65** 亦無 label。

依 **IN §8.7.5(a)**（label 逐字取 DBC `VAL_`）與 **§8.4.1**（不造值），
該 11 個賦值寫 `$MESSAGE.Signal$ = <raw>`，**不附 `(<label>)`**，逐條於 Remarks 揭露。
對照表：`features/vsm_v42/data/lint_p_waivers_b1.tsv`。

### 3.3 未涵蓋之分支 —— 1 條

`NR1L-VSM42-016`（`-059`）只覆蓋**車速跨越 `V_Car_Moving` 門檻**之分支。
規格同句之 **ignition Off→On 或分支未涵蓋** ——
037 寫 `(Ignition_{S}tatus)`（佔位符殘留）、規格段 1111 拼作 `Inigtion`，
**皆非合法訊號名**，依 §8.4.1 不臆造。已於該條 Remarks 與 reasoning 揭露。

### 3.4 規格語意不明處（不補洞，逐項留檔）

| # | 內容 |
|---|---|
| K-1 | 見 3.2（`Fdbk` 2–11 無 `VAL_`） |
| K-2 | `Fdbk` **4 與 5 之規格文字逐字相同**（皆 `the EPB switch is currently engaged`），兩碼語意差異規格未述。依 §8.2.2 各出一條，未合併、未臆測 |
| K-3 | 見 3.3（ignition 分支無合法訊號名） |
| K-4 | 規格節內拼字瑕疵（`EPB Maintance Mode`、`THEN TLM sall:`、`Inigtion`）。`test_item` 上半 verbatim 取 037 `Requirement Description`（RD 權威單位，R-VL21(c)），規格段以 `specification_reference` 指回 |
| K-5 | **退出側之請求路徑規格未載** —— 規格只載進入側（段 1054），故退出側四條之發起步 ER 只斷言 UI 設定狀態，**不斷言 `EPB_MaintenanceMode_Req = 0 (Off)` 之送出** |
| K-6 | `-054`（`Fdbk = 8`）之進出側歸屬無詞證，經量測（段 1092–1096 掃 `entering`／`exiting`／`request` 命中 0）判為 **in-mode 狀態回報型**（R-VL22(c)） |

## 四、品質證據

| 項 | 結果 |
|---|---|
| `lint036.py --profile vsm_v42` | **淨紅 0** —— `C`=0／`P` 之 23 列**全數對銷**於 `lint_p_waivers_b1.tsv`（11 賦值，23／23，無未對銷）／`U`=6 為 PENDING 計數（非 FAIL）／`I-cross`=17 全屬「窗未宣告」基線型（R-VL26(d)，警示器非判準）／其餘 20 項全 0 |
| 工作簿完整性 | `x14:dataValidation` 節點**逐字存活**（含 `xr:uid` GUID 與 `sqref R10:R1411`）；zip members **48**（無增減）；逐位元差異**僅目標分頁 `sheet6.xml`**；B 欄編號公式未被值取代 |
| 出件工法 | openpyxl 僅為計算層，出件走 `backend.xlsx_surgical.surgical_save`（R-VL24(a)；R-G3 禁 `openpyxl.save()`） |
| 回讀驗證 | 自出件讀回 17 列，**269 格逐欄比對 `generated/b1_epb/*.json`，不符 0** |
| 生成端自檢 | E38–E45／E53–E56 全過（覆蓋 17／17；`test_item` 上半對 037 `Requirement Description` **逐字全等 17／17**） |

## 五、一項與 lint 判準之衝突（**未解，交裁**）

`scripts/lint_delivery_spec.py` 之 `TC_ID_RE = ^NR1L-([A-Za-z]+)-(\d{3})$` ——
**`{ABBR}` 只收字母**，而本線之 TC ID 依 **R-VL3（Pei 2026-09-01 裁定）** 為
`NR1L-**VSM42**-{nnn}`，**含數字**。故該檢查判「17 列不合形制」。

**本執行層未改 TC ID**（其為 Pei 裁定且已寫入交付簿與 `writeback_map_b1.tsv`），
**亦未改 lint 腳本**（共用檔）。
**待裁**：(a) 放寬 `TC_ID_RE` 為 `[A-Za-z0-9]+`；或 (b) 改 R-VL3 之 ABBR 為純字母。

---

## 六、追溯

| 項 | 檔 |
|---|---|
| 生成產物（文字形，凍結） | `features/vsm_v42/generated/b1_epb/`（35 檔，`INDEX.md` 載逐檔 sha8） |
| 工作簿列 ↔ 產物對應 | `features/vsm_v42/data/writeback_map_b1.tsv` |
| 訊號鏈事實表 | `features/vsm_v42/data/signal_chain_v42_v3.tsv`（R-VL15(d) 現行版） |
| `VAL_` 表 | `features/vsm_v42/data/val_tables_v42.tsv` |
| 母體 | `features/vsm_v42/data/leaves.tsv`（152 列＝128 leaf ＋23 Heading ＋1 UNCATEGORIZED） |
| 條文 | `features/vsm_v42/RULINGS.md`（R-VL1–R-VL26） |
| 往返紀錄 | `features/vsm_v42/docs/INDEX.md`（下放包／上繳包 00–12） |
