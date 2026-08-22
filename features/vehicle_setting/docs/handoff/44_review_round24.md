# 44 下放包 — 24 輪覆核：四項裁定、停止搜尋、25 輪加速

分析層寫入，2026-08-22。**Pei 指示注意速度 —— 本包一次裁完，不留待決項。**

---

## 1. A-VS77 裁定：**不採用他車型 PROXI 表**

24 輪之新事實使天平倒向不採用：

> `VF664_V42_R3`（Toro226）**完全未提及該四參數**，而 `V2_R1`／`V2_R2` 提及。
> **即 VF664 之內容隨版本而異，而 R1LR 目錄下無 VF664。**

**兩份轉錄一致，只證明 DT27 與 HDCC28 用同一版；不證明 R1LR 用該版。**
且 VF664 本文只列參數名、不定義值域 —— **轉錄之上游本身不是值域來源**，
其值域另有出處，我方對該出處一無所知。

```
分析層裁定 2026-08-22（Pei 得推翻）
不採用他車型 PROXI 表之值域寫入 TC。
四個 PROXI 參數維持未解，79 個 leaf 維持阻塞。
`evidence_note` 之 `VF664-inferred` 標記保留，供答覆到達時比對。

**DR-22′ 即刻送出**，並依 23 輪 §2.1 改為是非題：

  「我方 LID v1.76 之 `Proxi & Configuration` 分頁，下列四參數之
   `Format` 欄為 `See Proxi Table`，`VFs` 欄為 `664`：
     Cooled_Seats／Heated_Seats／Heated_Seat_Levels／Heated_Steering_Wheel
   請確認 R1LR 之該四參數值域，是否即 VF664_V2／V3 所對應之 PROXI 表定義
   （我方於他車型之 PROXI 表見：Cooled_Seats／Heated_Seats =
    `0 Absent／1 Front Seats／2 Front And Rear Seats`；
    Heated_Steering_Wheel = `0 Absent／1 Present`；
    Heated_Seat_Levels = `0 = 1 Level／1 = 2 Levels／2 = 3 Levels`）？
   若否，請提供 R1LR 所適用之 PROXI 表。」

是非題 ＋ 附我方推定值，其回覆成本最低。
```

---

## 2. 停止型 B 之搜尋 —— **邊際價值已低於其成本**

`TLM HMI Document` 之搜尋已證其不存在（檔名 0、內容 15 處引用 0 份本體、
Comfort L&F 與 26PI2.5/HMI 之 89 份 PDF 皆 0）。

**而 R-VS17 早已裁定該 17 個 leaf 之處置**：TC 照寫，ER 寫至訊號層，
畫面層標 BLOCKED。**取得該文件只影響畫面層之補寫，不影響 TC 之產出。**

```
分析層裁定
型 B 之唯讀搜尋**就此停止**。§6-1／§6-2 之殘餘
（`Core HMI` 18 頁未 OCR、5 份 pdf 未 OCR、三個頂層目錄未掃內容）
**列入 BACKLOG，不再排入輪次**（R-VS40）。

理由：R-VS17 使 17 leaf 不因該文件缺席而停產；
搜尋之唯一收益為畫面層之補寫，而該補寫在 DR-20／23 覆後亦可為之。
**再掃 3,678 檔之成本，換不到一條 TC。**

DR-20／DR-23 **即刻送出**（型 B，訴求為取得文件）。
```

---

## 3. A-VS83 裁定：**不撤回，但須全量掃曝險**

```
分析層裁定
(1) batch03 之 `LeftFrontHeatedSeat-014`、batch04_v2 之
    `RightFrontHeatedSeat-031` **不撤回** ——
    其於 R-VS44′ 生效前產出，且其斷言之 `0/1` 有 CFTS044 自載之
    `1h: pressed`／`0h: not pressed` 錨點支持。
(2) **但須標記**：`generated/` 之各批次增 `dr15_exposed` 欄，
    凡斷言該五個 token 之值者標 `yes`。
(3) DR-15 覆後，`dr15_exposed = yes` 者**逐條複檢**；
    若答覆為「承載階數」，該等 TC 之 procedure 與 ER 須改寫。

**§6-3 之全量掃即 W-71。** 已知 2 條，總數未量 ——
**該數決定 DR-15 覆後之回溯工作量**，須現在就知道。
```

**`TwoStagesHeatedSeat-057` 之處置正確**：其驗證目標為畫面狀態循環
（`off → high → low → off`），請求訊號為實作手段。
**驗畫面即驗其需求，不觸 DR-15。** 惟依 (2) 仍應標 `dr15_exposed = no` 並記其理由。

---

## 4. W-70(1) 複檢：**逐字命中、實質未命中，採實質讀**

執行層之判斷正確。43 包 §3.2 明訂替代路徑即「配置相依無效值」，
故 `LeftFrontHeatedSeat-008`／`RightFrontHeatedSeat-026`／
`LeftFrontVentedSeat-006` 之 `2 (medium)` **非誤用，不改**。

`HeatedSteeringWheel-006` 改注入 `4`（未定義編碼）正確；
**其不寫 `(<label>)` 亦正確** —— 為未定義編碼編造標籤即違 §8.4.1。

```
分析層裁定（記入 profile）
無效值注入之優先序：
  (1) DBC 中**未定義之編碼** → 寫作 `= <raw>`，**不加 `(<label>)`**
  (2) 無未定義編碼時，取**配置相依之無效值**（他條文之有效值列舉所排除者），
      寫作 `= <raw> (<label>)` 並於 reasoning 記其依據條文
  (3) 二者皆無 → `PENDING: DR-{n}`
```

---

## 5. DR-8 改寫（實測使其前提失效）

實測：`VC_VEH_LINE` 於 R1LR 之 CFTS 命中 103，其值為
`[332]`／`[M182]`／`[M189]`／`[VEH_M182 OR VEH_M189]` ——
**與 DR-8 原文所列之 `DT`／`WS`／`HDCC`／`M240` 不同**。

```
DR-8′（型 B，取代原 DR-8）
`Logical Identifiers and CAN Mapping v1.76` 之 `VC_VEH_LINE` 值域列舉
為數字車型碼且截斷於 `101 = WL (65 Hex)`。

而 R1LR 之 CFTS 文件實際使用之值為 `332`／`M182`／`M189`
（`VEH_M182 OR VEH_M189` 等形態），**與該列舉無交集**。

請提供 R1LR 所適用之完整車型碼對照（含 `332`／`M182`／`M189` 之編碼）。
```

---

## 6. 25 輪指令 —— **加速：兩批生成 ＋ 一項掃描**

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/44_review_round24.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/23_dr15_exposure.md，六節先留空。
D-2  `DATA_REQUESTS.md`：DR-22′ 依 44 包 §1 改為是非題全文；
     **DR-8 改寫為 DR-8′**（44 包 §5），原文保留加註。
     全部型 B 標「搜尋已停止（44 包 §2）」。
D-3  profile 增列 44 包 §4 之無效值注入優先序三項。
D-4  BACKLOG.md 增列型 B 搜尋之三項殘餘（44 包 §2）。
D-5  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-71  **DR-15 曝險之全量掃描**
      對 `generated/` 之全部批次（batch01_v3／02／03／04_v2／05，**42 條**）
      逐條掃其 procedure 與 expected_result，凡斷言下列五個 token 之值者
      標 `dr15_exposed = yes`：
        `FL_HS_RQ`／`FR_HS_RQ`／`FL_VS_RQ_TGW`／`FR_VS_RQ_TGW`／`HSW_RQ_TGW`
      （其 DBC 名為 `FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`HSW_Tlm` 等）
      **必列**：曝險條數、逐條 leaf_id、及其斷言之值。
      已知 2 條（`LeftFrontHeatedSeat-014`／`RightFrontHeatedSeat-031`）。
      **該數即 DR-15 覆後之回溯工作量。**

W-72  batch06 生成 —— **10 條**
W-73  batch07 生成 —— **10 條**
      二批皆依逐 Layer 2 輪流選 leaf（配額以當時餘量重算），
      套 profile ＋ canon §8.7.5 v3 ＋ R-VS43 ＋ Sibling Rows ＋
      44 包 §4 之無效值優先序；
      選入後逐條過 `guard()`，`DR-CONFLICT` 者移出並記 `held_out`；
      §9 十七項逐項自檢 ＋ DBC 值表逐字核對。
      **W-72 完成後不等覆核，逕行 W-73。**

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得再執行型 B 之唯讀搜尋**（44 包 §2）。
**不得採用他車型 PROXI 表之值**（44 包 §1）。

## 升級條件

W-71 之曝險條數 > 10；
W-72／W-73 之某 Layer 2 餘量為 0；
§9 出現新型違規。
**本輪無其他必停項 —— 兩批連續生成，不中斷。**
```

---

## 7. 待 Pei —— **五份即刻可送，無待裁項**

| DR | 型 | 影響 leaf | 狀態 |
|---|---|---:|---|
| **DR-22′** | B | **79** | 本包改為是非題，**即刻送** |
| **DR-20／DR-23** | B | 17 ／ 3 | 搜尋已證不存在，**即刻送** |
| **DR-8′** | B | 8 引用 | 本包改寫，**即刻送** |
| **DR-24′** | A | 43 | 已定稿，**即刻送** |
| DR-21／DR-18／DR-11 | A | 65／160／1 | 已定稿，可併同 |

**條文面無待裁項。** 本包所有裁定皆已下，Pei 得隨時推翻。

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| A-VS77 之裁定 | 不採用他車型 PROXI 表；DR-22′ 改是非題 | 分析層 |
| 型 B 搜尋停止 | 邊際價值低於成本；殘餘入 BACKLOG | 分析層 |
| A-VS83 之裁定 | 不撤回，標 `dr15_exposed`，全量掃（W-71） | 分析層 |
| 無效值注入優先序 | 未定義編碼 → 配置相依 → PENDING | 分析層（記入 profile） |
| DR-8′ | 前提失效之改寫 | 分析層擬 |

**未立新編號 R- 條文** —— 符合 R-VS40。
