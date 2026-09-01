# RULINGS — Vehicle Setup Management R1L TBM（VF665 V43）

Feature slug：`vsm_v43`。條號系列 **`R-VT`**（本線單一來源，R-G23 live 取號）。
姊妹線 `vsm_v42`（`R-VL` 系列）為獨立 feature；兩線互不引用對方條號作為依據，
共用者一律引 canon（IN／FO／`RULINGS_LEDGER.md`）或 PM 之 `R-P` 條文。

裁決者標示：**Pei** = Tier 3 裁定；**分析層** = Tier 2 於 Pei 授權範圍內之裁定。
歷史條文不刪，修訂加註（R-TM13）。

---

### R-VT1 —— 獨立 slug；工作簿自 BLANK 起建

```
R-VT1（Pei 裁定 2026-09-01，00 包待裁題 1：「1 准」）
VF665 V43（Vehicle Setup Management by VP - LTM (R1L) with TBM）立為獨立 feature，
slug = vsm_v43，自有 RULINGS／ANOMALIES／DATA_REQUESTS／feature.yaml／
framework.md／docs/{handoff,upstream}/。
不併入 features/vehicle_setting/，不與 vsm_v42 共用任何工具、資料檔或條號。
工作簿自 BLANK ＋ R-G1 模板起建，不沿用任何既有 036 本。
```

依據：R-BLM1／R-VC1 先例；`vehicle_setting/CROSSLINE.md`（A-VF8／A-VF9／A-VF30）所載
兩線共目錄之代價。V43 ↔ V42 之 Functional 描述逐字重疊實測僅 30／398（V43 側）。

### R-VT2 —— 訊號書寫依 canon §8.7.5 v3 ＋ PM 現行條文；不承襲 R-VS52

```
R-VT2（Pei 裁定 2026-09-01，00 包待裁題 2：「2 准」）
(a) 本線 profile 不承襲 FW036_R1L_VehicleSetting_Profile.md 之
    [OVERRIDE §8.7.5]（R-VS52，SWC 0708 交付本式 `Send CAN:` 前綴）。
    訊號書寫依 canon IN §8.7.5 v3 (a)–(g)：
      `$<MESSAGE>.<Signal>$ = <raw> (<label>)`，<label> 逐字取 DBC VAL_；
      PROXI 參數 `PROXI <Param> = <值>`，不加 `$`；
      內部訊號（X.Req／X.Info／X.GUI）優先依對照表轉為可觀察 CAN 訊號，
      DBC 查無者保留來源名不加 `$`（(d)），規格訊號名與 DBC 不符者保留原文（(g)，R-13）；
      Hold 獨立成步（(e)）；baseline 採 <Name>_initial／<Name>_after（(f)）。
(b) 併採 PM 之三條（引用制 R-G13，執行層自 features/power/RULINGS.md 讀原文）：
      R-P353  Procedure／ER 之觀察對象限四類白名單
      R-P355  內部訊號不得直接 Set；尚無 DBC 對照者 `PENDING: DR-{n} <訊號名>`
      R-P368  訊號實名依 forms/ 三段鏈（LID v1_78 → MESSAGE.Signal →
              forms/PDT27_E2A_R1_BHCAN2.dbc／R1_FDCAN8.dbc）；R4／R5 DBC 降旁證
(c) lint 檢查 P 對本線以 `--profile vsm_v43` 走 v3 判準。
(d) input_test_data 一律 NA，資料內聯至 pre_conditions／test_procedure（IN §4.5）。
```

依據：Pei 原話「訊號寫法要遵照 power management 最新的部分」；分析層之讀法即 (a)(b)，
已於 00 包報 Pei，未點名出入即為採認。
**待 recon 查證**：本線 SYSRA EE Architecture 全為 ATL-Mi（1280/1280），R-P368(a) 段 1 之
LID 欄組適用性與 `vsm_v42` 同題，recon 實測後另裁。

> **註記（R-TM13，2026-09-01，R-VT6）**：(b) 所引 R-P368 連帶承接 **R-P375**，欄組二擇一問題消滅，
> 處置見 R-VT6。分析層引用未讀至 R-P375，記 A-VT5。

### R-VT3 —— Test Group／TC ID／交付檔名

```
R-VT3（Pei 裁定 2026-09-01，00 包待裁題 3：「3 准」）
Test Group（Layer 1）= `Vehicle Setup Management R1L TBM`
TC ID = `NR1L-VSM43-{nnn}`（R-G42 二之 Pei 裁一次；037 token `VC` 已為 vehicle_category 所佔）
交付檔名 = `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
           Specification & Result_SWQT_VehicleSetupManagementR1LTBM_{YYYYMMDD}.xlsx`
```

依據同 `vsm_v42` R-VL3 之理由（兩線同名則 `delivered/` 撞名，R-G42 五禁尾綴）。

### R-VT4 —— 037 = 0：本線止於 P0–P3，TC 生成待 037

```
R-VT4（Pei 確認 2026-09-01，00 包待裁題 4：「4 無其他」）
現有 037 兩份之 Source Requirement ID 全為 V42（152/152），本線 037 = 0；
Pei 確認無其他 037 檔。
依 IN §8.2（037 為需求單位之權威）與 R-VS15／R-BLM2 先例（母體自 037 取），
本線無母體，TC 生成不得以 SYSRA 或規格直接代之。
本線之作業止於 P0 intake／P1 recon／P2 DECISIONS／P3 framework 與 profile，
P4 以後待 037 到齊。DR-VT1 登記並建議送出（阻塞型）。
```

### R-VT5 —— 素材落點；spec_mode D 需 OOXML 原檔

```
R-VT5（Pei 裁定 2026-09-01，00 包待裁題 5：「5 准」）
投遞區 _intake/Vehicle_Setup_VF665/（與 vsm_v42 共用投遞區，落點分開；R-G24 已建妥實測）。
原檔落點 sources/raw/<doc_id>/，feature.yaml 以 doc_id 引用（R-G27）。
SYSAD 一份兩線共引；LID／DBC／PROXI 取 forms/。
Project 內 docx 為文字抽取本；spec_mode D 之抽取須自原檔，Pei 須投遞原始 .docx。
```

### R-VT6 —— R-VT2(b) 加註：段 1 入口依 R-P375 擴為 forms/ 全部參考檔；多命中之處置

```
R-VT6（分析層裁定 2026-09-01，上繳 00 §九-6；訂正分析層對 Pei「PM 最新」之窄讀）
(a) R-VT2(b) 所引 R-P368 連帶承接 R-P375(a)–(e)：段 1 入口為 forms/ 全部參考檔
    （LID 全分頁含 `637MCA Specific Signals`、HMI Settings List R1 SR25、PROXI_HDCC27_R3 `Format`、
    SR26 Default Settings、SR24 Market Configuration Table），每檔以 forms/FORMS.md 之 SHA 入台帳。
(b) `X.Req` 類設定值依 R-P375(b)走 UI／PROXI 路徑；`X.Info` 類致能狀態依 R-P375(c)。
(c) 同一規格原名多處命中而解至同一標的者為同物，附表記全部命中處；解至不同標的者記 B-1 型衝突
    交 Pei（R-P369(b) 型）。命中即候選非認定（R-P375(d)）。
(d) R-VT2 原文不改，加註指向本條。
```

### R-VT7 —— TC ID 鍵名採全庫慣例 `write_back.tc_id_format`

```
R-VT7（分析層裁定 2026-09-01，A-VT2）
feature.yaml 落 `write_back.tc_id_format: "NR1L-VSM43-{n:03d}"`；`tc_id_prefix` 鍵刪除，不保留（R-VC9）。
R-VT3 之值不變。A-VT2 依本條 RESOLVED，其根因為分析層之誤（A-VT5）。
```

### R-VT8 —— `docs/fw036/RULINGS.sha.tsv` 本線不重生；sandbox 與欄位從 R-VL8 同法

```
R-VT8（分析層裁定 2026-09-01，上繳 00 §八／§九-5）
(a) 台帳重生由 vsm_v42 之 01 包執行一次（其 R-VL9），本線包不重生；本線 sha8 自重生後之台帳讀取回報。
(b) 工作簿：W-2 起始建 `features/vsm_v43/sandbox/base/`，自 forms/ R-G1 母本（sha256 6372fb6b…825b2）
    檔案複製，不經 openpyxl 存回；`workbook.*` 自副本 r9 實測回填，模板值不得沿用。
    先驗（同 sha 母本實測）：priority P、estimated_test_time Q、design_method R、functional_safety S、
    author AA、test_version AB。
(c) `spec_reference_template` 落 null，待 P3 裁（VF 類母件之 IN §10.7 型態未定）。
```

---

## 取號紀錄

| 條號 | 落檔日 | 取號依據 |
|---|---|---|
| R-VT1–R-VT5 | 2026-09-01 | 本檔新建，全庫 `R-VT` 系列實測未佔 |
| R-VT6–R-VT8 | 2026-09-01 | 落檔當下讀本檔實測至 R-VT5；上繳 00 §七 sha 表亦止於 R-VT5 |
