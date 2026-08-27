# 下放包 02 —— Q1–Q6 裁定落條（R-DD1~R-DD5）、DR-DD1 文稿、Phase 0/1 任務啟動

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`01_feature_open.md`
- 裁定狀態：Q1–Q6 —— **Pei 2026-08-27 全案照提案裁定**；本包落條文
- DR-DD1 文稿於 §三，待 Pei 發送

---

## 一、裁決條文（R-DD1~R-DD5；執行層 T-抄 逐字 append 入 `RULINGS.md`，程式回讀逐字元核對）

```
R-DD1（feature 身分）

Feature slug = `driver_distraction`；Test Group = `Driver Distraction`
（取 037 Project Name 欄實值；CFTS 章名 `Driver Distraction Lockout`、
HMI spec 題名 `Driver Lockout` 均不採 —— 037 為生成主驅動，Layer 1 從其命名）。
裁決／異常／資料請求前綴 = R-DD／A-DD／DR-DD。
（Pei 2026-08-27 裁定，下放包 02）
```

```
R-DD2（TC ID 格式）

tc_id_format = `newR1L-DD-{n:03d}`（IN §10.3）。
project 前綴之權威為工作簿 D2 儲存格；執行層開副本時實測確認為
`newR1L`，不符即停並回報，不得逕改格式字串。
（Pei 2026-08-27 裁定，下放包 02）
```

```
R-DD3（ER 之斷言錨層級）

037 之 Verification Criteria 以軟體層事件表述
（「The subscribed Listener receives a RESTRICTED callback」等）。
SWQT 之可觀察面為 HMI 現象與可讀之 log。裁定：

(a) ER 之主錨為 **HMI 現象**（鎖定 feature 之 UI 態、Fullscreen
    Lockout 畫面、Standard Lockout Popup、feature 之可及性）。
(b) VC 中之 callback／Listener 事件類敘述，依 reaction presence
    降階處理（R-BLM13 同族）：ER 得斷言「系統對條件變化有可觀察
    之反應」（如鎖定生效／解除於 HMI 呈現），**不得**斷言
    callback 本身之送達、時序或參數 —— 該層非 SWQT 觀察面。
(c) 細則（各 leaf 之 HMI 錨對照、log 錨之採認條件）入 feature
    profile，於 pilot 前定稿。
（Pei 2026-08-27 裁定，下放包 02）
```

```
R-DD4（SYSAD 之地位）

SYS3 SYSAD（FM-WI-FSM-015-A01）入 `inputs/` 並入 feature.yaml
`reference` 節綁 sha256；地位為**人讀參考**，不入批次語料、
不入 prompt 指紋 fingerprint.prompt_sources。
TC 之任何內容不得以 SYSAD 為來源（其為 SWE.2 側架構文件，
非 SWE.1 需求 —— 引之即層級錯置）。
（Pei 2026-08-27 裁定，下放包 02）
```

```
R-DD5（四庫綁定）

$Speedometer$／$VC_Trans_Equipped$／$PresentGear$／$PARK_BRK_EGD$／
$Country_Code$ 之 DBC/LID/PROXI 對應，沿 R-BLM11 乙案：
綁 `features/vehicle_setting/inputs/` 之四原件
（LID v1_76、PDT27_E2A_R4_BHCAN.dbc、PDT27_E2A_R5_FDCAN8.dbc、
PROXI_HDCC27_R3_20250424.xlsx），不複製入本 feature inputs/。
sha256 由執行層自實體檔重算，不抄他 feature 之宣告值。
逐訊號查對照；查無者依 IN §8.7.5(d)(g) 保留來源名稱並逐項登 DR，
不得代以語意相近之他訊號（R-13）。
（Pei 2026-08-27 裁定，下放包 02）
```

---

## 二、A-DD1 之暫行處置（分析層提案，隨包生效，Pei 可推翻）

**leaf 025–028（4 列）凍結**至 DR-DD1 回覆，不入任何批次。
理由：市場條件（HK vs LATAM）為該 4 列 Pre-Condition 之核心值
（`PROXI Country_Code` 之設定值），裁錯即整列重寫；先例為
SXM C-class rows 凍結待 DR-SXM10 之同型處置。
framework 組 6 `Market Speed Gating` 維持中立佔位名，
組名不寫入工作簿任何列（包 01 §三既定）。
其餘 24 leaf 之生成**不受阻**。

---

## 三、DR-DD1 文稿（待 Pei 發送；發送後執行層登入 `DATA_REQUESTS.md`）

> **DR-DD1 — Market condition conflict for SWE1-RA-Driver_Distraction-025 ~ -028**
>
> In FM-WI-FSM-037-A03 (DD_SWE1, 2026-08-07), rows
> SWE1-RA-Driver_Distraction-025 through -028 cite source requirements
> `SYS-RA-Driver_Distraction-125` (section gate: "The requirements in the
> section shall be implemented if $Country_Code$ = [Hong Kong]") together
> with `SYS-RA-Driver_Distraction-132` / `-133` (5 MPH lock / 3 MPH unlock
> thresholds). Their Requirement Descriptions and Verification Criteria
> also state "When Country_Code is Hong Kong".
>
> However, in CFTS022 SYSRA (FM-WI-FSM-035-A02), `-132` and `-133` are
> located under the **LATAM Market Regulations** heading (`-130`), whose
> applicability note (`-131`) states the section applies to the LATAM
> market only. The two sources are mutually exclusive on the market
> condition.
>
> Question: for SWE1 rows -025 ~ -028, should the market condition be
> (a) Hong Kong, (b) LATAM, or (c) both markets? If (c), please confirm
> whether separate SWE1 rows for the LATAM side will be added, since the
> current four rows carry Hong Kong wording only.
>
> Until clarified, the four rows are on hold in SWQT test case generation.

---

## 四、任務（本輪）

| # | 任務 |
|---|---|
| T-抄 | R-DD1~R-DD5 逐字 append 入 `RULINGS.md`（T1 骨架建立後）；程式回讀逐字元核對；依 R-SU8 同型建檔首現行版索引表（本 feature 自始即建，5 條現行、0 留存） |
| T1–T5 | 包 01 §五 原文照跑（T1 骨架 → T2 inputs 驗型+sha → T3 intake/recon → T4 leaf_inventory → T5 上繳） |
| T6 | R-DD5 之逐訊號對照初查：五個 `$…$` 參數對四庫逐一查 MESSAGE 全名／VAL_ 列舉／PROXI 參數名，輸出查得/查無清單（查無者之 DR 由分析層擬稿） |
| T7 | `DATA_REQUESTS.md` 建檔，DR-DD1 登記（狀態：DRAFTED，待 Pei 發送） |

**不在本輪**：framework 定稿（待 DR-DD1 與 T6 結果）、profile、任何 TC、寫回、git。

---

## 五、上繳包要求（`docs/upstream/01_scaffold_recon.md`）

1. T-抄 核對結果 + 索引表全文
2. T2 驗型結果（逐檔 `file`/magic 實測）+ sha256 清單
3. T3 recon assertion 輸出（`functional_requirement_count: 28`）
4. T4 之 28 列 leaf 清單（`_x000D_` 正規化前後對照留原文欄）
5. T6 五訊號查對結果（原始輸出）
6. 未結 DR 清單（DR-DD1）
7. 獨立自評
8. 量測條件揭露（R-G8）
