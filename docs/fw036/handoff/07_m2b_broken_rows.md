# 下放包 07：批 3 —— M2b 殘缺列重建（BT／HFP／Projection，38 列）

PM 告一段落，轉其他 feature。本包為跨三本之機械修，
**三本各自獨立作業、各自產出工作副本**，不合併。新規 0 條。
前置：先執行 06 包 §三之 lint C 範圍調整（R-6b），再開始本包。

## 一、範圍（分析層實測，逐列可核）

**BT 0729 —— 8 列**：rows 159、160、171、172、179、180、183、184
空欄：`test_set`(8)、`author`(8)。其餘欄完整。
既有 Test Set 詞彙（9 種）：`Phone(HFP)`、`Adapter & Device`、
`Connection`、`IVI Integration`、`Media(A2DP)`、`Pairing`、
`Phonebook(PBAP)`、`Data Control`、`Telephone(TEL)`

**HFP 0316 —— 29 列**：rows 74–78、99、101–106、113–115、117、119、
123、124、126、130、131、134、135、144、146、148、151、153
空欄：`author`(23)、`spec`(23)、`pre`(15)、`er`(1)
既有詞彙（11 種可用）：`Call Log`、`Bluetooth`、`Device Manager`、
`AddressBook`、`Contact`、`Voice recognition`、`Message`、
`Service Control`、`Status Information`、`System State`、`Phone Call`
⚠ 第 12 種為 `12-01需求重點不是只是看電話號碼格式` —— **非 Test Set，
係工作備註誤入欄位**。登記 **A-HF01**，本包一併清除該格並依內容歸類。

**Projection 0623 —— 1 列**：row 571
空欄：`test_set`、`author`、`pre`、`proc`、`er`、`spec` —— **六欄全空**。
既有詞彙（12 種）：`iPod / Apple Device`、`HMI Display`、
`Projection Launch`、`Connection`、`Device Manager`、
`Projection Detection`、`Disconnection`、`Knob`、`Projection Audio`、
`Voice Recognition`、`Vehicle Signal Forwarding`、`Day/Night Mode`

## 二、作業規則

**Test Set 補值**：一律自該本既有詞彙表選值（closed vocabulary），
**不得新造詞彙**。歸類依據為該列之 `test_item`／`proc` 實際內容與
同 Requirement ID 之鄰列既有值。歸類無把握者標記待覆核，不臆測。

**author 補值**：取該本同區段（前後鄰列）之作者值。全本單一作者者
逕取之；跨作者交界處無法判定者標記待覆核，**不得預設為 Pei**。

**pre／spec／er／proc 補值**：**不得自行撰寫內容**。依 §8.4.3 判別三態：
- 該列確實不需要 → `NA`
- 來源文件缺失 → `PENDING: DR-{n} <缺件名>` 並登記 DR
- 應有而遺漏 → 標記待覆核，交由分析層判定，**本包不填**

**Projection row 571 六欄全空**：先判定該列是否為誤留之空列
（檢查其 Requirement ID／TC ID 是否有值、是否落在連續編號中）。
若為誤留空列 → 回報，**不得自行刪列**（刪列屬 Pei）。
若為應有而未寫之 TC → 全列標記待覆核，本包僅補 `test_set`。

## 三、驗收

- lint036 三本：**G = 0**（BT 8→0、HFP 29→0、Proj 1→0）
- **M（空欄三態）不得增加**；本包可能使 M 減少（填 NA／PENDING）
- 其餘檢查項逐本**不得變動**（以 06 包 §三調整後之報告為基線，
  非舊報告）
- 逐格 diff：三本各自變動格數 ≤ 該本目標欄數；非目標欄零變動
- x14 下拉讀回驗證（三本各驗）

## 四、上繳

`docs/fw036/upstream/07_m2b_broken_rows.md`：三本各自之改動列清單、
Test Set 歸類依據（逐列列出所據之 test_item／鄰列值）、
待覆核列清單、新增 DR 清單、lint 前後對照、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

**三本皆止於工作副本**，不寫回交付路徑（屬 Pei）。

## 五、附帶任務：7 本報告補跑

`docs/fw036/lint_reports/` 之 AMFM、BT、DealerMode、HFP、Home、
MediaHMI、Projection 七本報告係加入 P 欄前之版本，已過期。
連同 R-6b 之 C 範圍調整，**七本一併重跑覆蓋**，作為後續各批之基線。
