# 35 下放包 — pilot review 第一輪：訊號書寫形式撤回、profile 建檔、DR-19／20

分析層寫入，2026-08-20。對象：`docs/upstream/15_pilot_batch.md` ＋ `generated/batch01.json`。

**pilot 第一輪之結論：批次不通過，全數改寫。**
但這正是 pilot 存在的理由 —— **在 10 條上發現，而不是在 237 條上。**

---

## 1. A-VS57 —— **R-VS9(3) 撤回，canon §8.7.5 勝**

分析層讀了 repo 之 `docs/runtime/ASPICE_SWE6_AI_Instruction.md`（現行版），
確認 §8.7.5 v3 存在且已歷 v1→v2→v3 之修訂，其 v3(a) 令訊號以
`$<MESSAGE>.<Signal>$` 全名書寫、值採 `= <raw> (<label>)`，
並明文「**v1 之三件組 `<Signal> in <MESSAGE> on <segment>` 已撤銷**」。

**執行層採 R-VS9(3) 之三個理由，分析層逐一回應：**

| 執行層之依據 | 分析層回應 |
|---|---|
| (1) R-VS9 為 Pei 裁定，§8.7.5 之撤銷署名為分析層下放包 | **不成立**。canon 之修訂經 Pei 於該 feature 之輪次裁定，其署名記為下放包號係記載慣例；且本 Project 之 Operating Charter 逐字載明「repo 版本為權威且於該處演進」 |
| (2) 下放包 §3 為最具體指令且明引 R-VS9(3) | **成立但不足**。最具體指令之效力止於其不與上位規則衝突者 |
| (3) 本 feature 無 profile，R-VS9 實質承擔該角色 | **不成立**。§0 之衝突條款要求 profile 之 **cited override**；未寫入 profile 者不生 override 之效力 |

**決定性理由不在上述三點，而在其來源**：

> Signal／field 之書寫慣例**專由 Pei 之 SWC 0708 交付本推導**；
> 格式裁決須先枚舉既有交付本之實際書寫樣式，**分析層自訂之慣例不予採用**。

**R-VS9(3) 之三件組是分析層自訂的**——其理由（兩份 DBC 之 141 個共有 signal
中 128 個起始位元不同）是推理，不是對既有交付本之枚舉。**該條違反上開原則。**

```
R-VS41（分析層裁定 2026-08-20；本輪唯一新條文，R-VS40 之額度用畢）

(1) **R-VS9(3) 撤回。** 訊號書寫依 canon §8.7.5 v3：
    `$<MESSAGE>.<Signal>$`，值採 `= <raw> (<label>)`。
    例：`$STATUS_CSWM.HSW_StatFailSts$ = 1 (Fail_Present)`
    R-VS9 之 (1)′(2)(4)(5) 不變 —— 拼寫取 DBC、對映取 LID、
    值域交叉核對、`$var$` 不入 procedure／ER。
    lint 判準 L-VS2 不變；**L-VS1（三件組檢查）一併撤回**。

(2) **網段資訊改由 Pre-Condition 承載。** 依 R-12a，工具型前置條件
    採 SWC 措辭並置於末位。本批既有之匯流排模擬器條目即為此用，
    **保留**（15 輪 §6-4 之疑慮由本項解消，非新裁）。

(3) **`specification_reference` 之排列改依 canon §10.7 現行版**：
    **一個 ObjectID 一行**，每行完整重述 `CFTS044-{7位數}`，
    **禁用 `,`／`、`／`;` 串接**，同文件內升冪。
    R-VS33′ 之「多值以分號分隔」與 R-VS14 之「逐一列出（未指明分行）」
    **就此更正**。本批 10 條皆單值，未違規；
    但 11 個多值 leaf 於後續批次必受此規制。

(4) **通則**：feature 級條文與 canon 衝突時，**canon 勝**，
    除非該例外已寫入 `docs/runtime/profiles/` 之本 feature profile
    並於條文中 cite 之。分析層自訂之書寫慣例一律不得凌駕 canon。
```

**batch01 之 10 條 procedure 與 ER 全數改寫。**

---

## 2. A-VS60／A-VS61 —— 建 profile，兩項一併關閉

canon §11 之方括號例外為 **profile-scoped**；§4.2 之 Test Set 反樣式
亦得由 profile override。**本 feature 至今無 profile 檔，是缺件不是缺條文。**

```
W-54（建 profile）
建 `docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md`，內容為
既有裁決之 profile 化，**不新增任何規則**：

[OVERRIDE §11] test_item 上半段為 037 Requirement Description 逐字
  （R-VS6），其內含之方括號 token（`[IDLE_STBL//UNLIMITED//LIMITED//RUN]`、
  `[SNA]`、`[Right Drive]` 等）**予以保留**。
  四個交付欄（pre_conditions／input_test_data／test_procedure／
  expected_result）仍禁方括號。
  lint 對 test_item 之保留 token 以「與所引來源列逐字相符」驗證，非禁用。
  先例：Home A-H10（pilot review 時修訂）。

[OVERRIDE §4.1.3／§4.2] Layer 2 = `Common Features`（R-VS4，Pei 裁定）。
  其為 037 之檔界，涵蓋 Stop-Start、LHD/RHD、Screen OFF、
  Third Row Headrest Dump、PHEV 等異質能力，
  **不滿足「共用 setup 與 UI 進入路徑」之期待**。
  理由：037 檔界即上游作者選定之能力叢集邊界（00 包 §3 R-VS4）。

[ADD] 訊號書寫依 canon §8.7.5 v3；網段以 Pre-Condition 承載（R-VS41(2)）。
[ADD] spec_reference 依 canon §10.7(a)，`CFTS044-{7位數}`，一行一個。
[ADD] input_test_data 一律 `NA`（R-VS5）。

A-VS60／A-VS61 於 profile 落檔後關閉。
```

---

## 3. DR-19／DR-20 —— 分析層擬（執行層已正確地不代擬）

```
DR-19（阻塞 3 leaf）
CFTS044 條文 4858551／4858553／4858555（`[EE Architecture:Atlantis High]`）
以 `$EngRun_Stat$ = [IDLE_STBL]`／`[UNLIMITED]`／`[LIMITED]`／`[RUN]`
為 Stop/Start 開關可用性之判定條件。

惟 `Logical Identifiers and CAN Mapping v1.76` 將 `EngRun_Stat` 對映至
`STATUS_CCAN3.EngineSts`（Atlantis High 欄組），
其 Format 與基線 DBC `PDT27_E2A_R4_BHCAN.dbc` 之 `VAL_` 皆為
`0 = Engine_Off`／`1 = Engine_Cranking`／`2 = Engine_On`／`3 = SNA`。
**四個規格值於 LID 與 DBC 中皆無對應。**

請提供 `IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` 之匯流排對應
（訊號名、message、值），或確認其應改用他訊號。
影響：SWE1-VC-Stop-StartSystem-004／-005／-006 三個 leaf 之 procedure
與 expected_result 無法在不編造值之下寫出。
```

```
DR-20（阻塞 1 leaf）
CFTS044 條文 4858560（`[EE Architecture:Atlantis High]`）逐字為
`… the HMI shall be modified as defined by HMI requirements.`
—— **未具名任何文件、章節或需求 ID**。

我方已查 26PI2.5/HMI 之全部 107 檔（含對無文字層 PDF 施以旋轉 OCR），
未能定位其所指之 HMI 需求。

請指明該 HMI 需求之文件與章節。
影響：SWE1-VC-SwitchLHD/RHDConfiguration-010 之末步驟無可寫之驗證目標；
寫具體修改項即為造值（§8.4.1），寫「HMI is modified」則不可觀察（§6）。
現以 `PENDING: DR-20` 佔位。
```

---

## 4. 其餘三項未驗之處置（皆依既有政策，不立新條文）

| 項 | 處置 |
|---|---|
| §6-2 未經 sibling 比對 | **下批必須注入 `## Sibling Rows`**。`Stop-Start-004`／`-005` 於改寫時一併補 `distinguishing_axis`（§4.6） |
| §6-3 `ThirdRowHeadrestDump-025` 之「再按一次不上升」 | **刪除該步驟**。條文僅述 `only to lower … not to raise`，**未定義再按之行為** —— 寫其結果即 §8.4.1 之造值。改為單向驗證（按下→下降；不驗反向） |
| §6-4 匯流排模擬器之 Pre-Condition | **保留**，依 R-VS41(2) 與 R-12a：工具型前置採 SWC 措辭、置末位。非 §8.5 所指之環境穩定前提 |

---

## 5. 18 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  docs/runtime/ASPICE_SWE6_AI_Instruction.md                **TC 內容規則（現行版）**
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/35_pilot_review1.md 本輪依據（本檔）

## 文書

D-1  依 R-VS18 建 docs/upstream/16_batch01_rework.md，六節先留空。
D-2  逐字轉錄 35 包 §1 之 **R-VS41** 入 RULINGS.md；
     R-VS9(3) 標「撤回，經 R-VS41(1) 取代」、L-VS1 標「撤回」；
     R-VS33′／R-VS14 之排列段標「經 R-VS41(3) 更正」（原文保留）。
D-3  DATA_REQUESTS.md 補入 DR-19／DR-20 之提問文（35 包 §3 全文）。
     **仍不送出。**
D-4  ANOMALIES.md：A-VS57 依 R-VS41 關閉；A-VS60／A-VS61 俟 W-54 落檔後關閉。
     依 R-VS35 列兩數。

## 作業（**兩項**）

W-54  建 `docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md`
      內容如 35 包 §2，**不新增任何規則**，逐條 cite 其來源條文。

W-55  batch01 改寫（10 條）
      (1) procedure／ER 之訊號書寫全數改為 canon §8.7.5 v3：
          `$<MESSAGE>.<Signal>$ = <raw> (<label>)`
          `<raw>` 取 DBC 之數值、`<label>` 取 DBC `VAL_` 逐字
      (2) 網段以 Pre-Condition 承載（R-12a：SWC 措辭、置末位）
      (3) `ThirdRowHeadrestDump-025` 刪除「再按一次」步驟，改單向驗證
      (4) `Stop-Start-004`／`-005` 補 `distinguishing_axis`（§4.6）
      (5) `Stop-Start-004`／`-005`／`-006` 之 `$EngRun_Stat$` 相關步驟
          維持 `PENDING: DR-19`；`SwitchLHD/RHD-010` 維持 `PENDING: DR-20`
      (6) 重跑 §9 十七項自檢，逐項列出；
          **檢查 15 對 test_item 之方括號改以 W-54 之 profile override 判定**
      (7) 輸出 `generated/batch01_v2.json`，**保留 v1 不刪**（R-TM13）

## 禁區

git 寫入性操作一律不執行。不寫回 036 工作簿。不鎖定 framework。
不執行任何 backlog 項（R-VS40）。不代擬條文。

## 升級條件

改寫後 §9 有新的不通過項；
canon §8.7.5 v3 之形式與某條 TC 之內容不相容（具名該 TC 與衝突點）；
實測與 35 包不符。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| — | **DR-15／17／18／19／20 一次送出** —— 現有 **5 份**待送，其中 4 份阻塞共 178 leaf |
| P19 | framework 簽核 |
| — | 追認 R-VS41（一句話；不追認亦依此執行） |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS41 | 撤回三件組改依 canon §8.7.5 v3；網段入 Pre-Condition；spec_ref 逐行；canon 優先於 feature 自訂 | 分析層（R-VS40 額度用畢） |

**本輪僅立一條，符合 R-VS40。** W-54／W-55 為作業，DR-19／20 為提問文。
