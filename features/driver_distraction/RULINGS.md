# RULINGS — driver_distraction (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 driver_distraction 之裁決權威；
跨 feature 條文承接時註明來源包。

---

(no rulings recorded yet)

## 現行版索引（沿 R-SU8(b) 同型；本 feature 自始即建）

> 判準：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-DD1 | v1 | feature 身分：slug `driver_distraction`、Test Group `Driver Distraction`、前綴 R-DD／A-DD／DR-DD | 02 §一 |
| R-DD2 | v1 | tc_id_format `newR1L-DD-{n:03d}`；project 前綴權威為工作簿 D2 | 02 §一 |
| R-DD3 | v1 | ER 之斷言錨層級：HMI 現象為主錨；callback／Listener 依 reaction presence 降階 | 02 §一 |
| R-DD4 | v1 | SYSAD 為人讀參考，不入語料、不入 prompt 指紋 | 02 §一 |
| R-DD5 | v1 | 四庫綁 `vehicle_setting/inputs/` 原件；sha256 自實體檔重算；查無者逐項登 DR | 02 §一 |

**留存之被取代條文**：無（本 feature 自始無改版）。

---

```
R-DD1（feature 身分）

Feature slug = `driver_distraction`；Test Group = `Driver Distraction`
（取 037 Project Name 欄實值；CFTS 章名 `Driver Distraction Lockout`、
HMI spec 題名 `Driver Lockout` 均不採 —— 037 為生成主驅動，Layer 1 從其命名）。
裁決／異常／資料請求前綴 = R-DD／A-DD／DR-DD。
（Pei 2026-08-27 裁定，下放包 02）
```
---

```
R-DD2（TC ID 格式）

tc_id_format = `newR1L-DD-{n:03d}`（IN §10.3）。
project 前綴之權威為工作簿 D2 儲存格；執行層開副本時實測確認為
`newR1L`，不符即停並回報，不得逕改格式字串。
（Pei 2026-08-27 裁定，下放包 02）
```
---

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
---

```
R-DD4（SYSAD 之地位）

SYS3 SYSAD（FM-WI-FSM-015-A01）入 `inputs/` 並入 feature.yaml
`reference` 節綁 sha256；地位為**人讀參考**，不入批次語料、
不入 prompt 指紋 fingerprint.prompt_sources。
TC 之任何內容不得以 SYSAD 為來源（其為 SWE.2 側架構文件，
非 SWE.1 需求 —— 引之即層級錯置）。
（Pei 2026-08-27 裁定，下放包 02）
```
---

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
