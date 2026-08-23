# 64 下放包 — R-VS59 下半未兌現之處置、編號分線、41 輪

分析層寫入，2026-08-23。**交付 119／池 25。**

---

## 1. R-VS59 下半 —— **Comfort 對失效層確實為空，該事實須入交付揭露**

§2.2 之實測：Comfort 037 之 403 條 Functional 中，含 heated／vented seat 者 **20**，
**其中含 fail／error／malfunction 者 0**。

**即 R-VS59(2) 之「畫面層取自 Comfort 素材」，對失效狀態一類無素材可取。**
batch16 之 10 條全數 `PENDING: DR-5-B`，**非執行層之偷懶，是素材確實為空。**

```
分析層裁定 2026-08-23
batch16 之形態**成立**：其訊號層可測（CAN 注入 ＋ 狀態訊號讀取），
畫面層標 `PENDING: DR-5-B` 為 R-VS59(4) 之正解。

**但須入交付揭露**：`docs/reports/` 建 `delivery_disclosure.md`，
逐條列出「畫面層為 PENDING 之 TC」及其待補來源，
並記明 Comfort 037 對失效層之條文數為 **0** 之實測。

**理由**：該類 TC 交付後，客戶執行時只會驗到訊號層。
若無揭露，會被讀為「畫面行為已驗」。**該落差須由我方主動說明，非待其發現。**
```

---

## 2. §6-3 之判斷成立 —— W-112 之判準無偵測力

「查無 > 查得」在 Layer 3 粒度下**永不命中**；
問題是 W-113 撞出來的，**不是判準查出來的**。

```
分析層裁定：W-112 之判準改為**逐 leaf 之行為層比對**（W-115(2)）
其錨點為：`Fail_Present` 類之 16 leaf 須全數判「查無」——
**該錨點若命中，證明判準對已知為空之類別確實回報空。**
現行 Layer 3 判準對該 16 條回報「查得」，即其失準之直接證據。
```

---

## 3. §2.3／§2.4 —— 兩處我方之失準

| 項 | 事實 |
|---|---|
| **錨點 2 無標的** | `M182`／`M189`／`M240` 於 237 leaf 之條文命中 **0**。我以 CFTS 全文之引用數設錨點，**未先確認其於本 feature 母體內是否存在** —— **R-VS50′ 之「可及性回查」我自己沒做** |
| **`generatable` 對照數 110** | 產物實為 **105**（37／38 兩輪之值）。我引 34 包之表而未回查產物。**執行層不調和、逐項列出，正確** |

**R-VS62 之四碼解鎖因而未經驗證。** 真錨點應取**實際引用 `$VC_VEH_LINE$` 之 leaf**
（00G 記其為 8 處引用），**其於 237 母體內之數本輪未量** → W-115(1)。

---

## 4. R-VS63 —— 編號分線（本輪唯一新條文）

三次衝突（兩份 NN=61 之下放包／R-VS59～62 兩批同號／A-VS129-130 撞號）
皆為兩條線共用同一組登記簿而無預留所致。

```
R-VS63（分析層裁定 2026-08-23）
`features/vehicle_setting/` 下之兩條作業線，其編號空間分段預留：

  **主線（CFTS044 Vehicle Setting）**
    anomaly   `A-VS001` ～ `A-VS199`
    ruling    `R-VS01`  ～ `R-VS99`
    下放／上繳 `00` ～ `99`

  **VF230 線**
    anomaly   `A-VS200` 起
    ruling    `R-VS100` 起
    下放／上繳 **另立目錄** `docs/handoff/vf230/` 與 `docs/upstream/vf230/`，
              其內自 `00` 起編

**既有之衝突不追改**（R-TM13：原文保留）：
  VF230 線現行之 `R-VS59`～`R-VS63` 五條，其標題加註
  「⚠ 本條屬 VF230 線，與主線同號者為不同條文」；
  其後續新條自 `R-VS100` 起。
  `upstream/61_vf230_intake.md` 移入 `docs/upstream/vf230/00_intake.md`
  —— **該移動為檔案搬移，屬 Pei**（不可逆之路徑變更）。

**引用之義務**：跨線引用時須標線名（如「VF230 線之 R-VS59」）。
```

---

## 5. 41 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/64_review_round40.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/36_domain_and_anchor.md，六節先留空。
D-2  逐字轉錄 64 包 §4 之 **R-VS63** 入 RULINGS.md；
     VF230 線之 R-VS59～R-VS63 五條加註「⚠ 本條屬 VF230 線」。
D-3  建 `docs/reports/delivery_disclosure.md`（64 包 §1）：
     逐條列畫面層為 `PENDING` 之 TC ＋ 其待補來源 ＋
     Comfort 037 對失效層條文數 **0** 之實測。
D-4  ANOMALIES.md：A-VS137／138／139 標處置；依 R-VS35 列兩數（**分線列**）。
     D-6 骨架對照照做。

## 作業（三項，R-VS25）

W-114 **A-VS137 之補收 ＋ 全量重錨定**（B-02 解凍條件已成立）
      (1) `HSW_StatFailSts` 之值域自基線 DBC `VAL_` 補收
          （`0 = Fail_Not_Present`／`1 = Fail_Present`）
      (2) **同時檢查同型遺漏**：以 DBC 全部 `VAL_` 為已知全集，
          逐一比對 `spec_variables.tsv` 與 LID 兩欄組，
          **列出「DBC 有而我方兩處皆空」之全部 token**
          —— A-VS102 補收四個、本次補一個，**其總數本輪須量得**
      (3) 全量重跑分級，列 W0／W1／W2 與 **137/2/98** 之對照；
          **該對照鏈自本輪重新錨定**（64 包 §6-5 之預告）

W-115 **兩個錨點之補正**
      (1) **R-VS62 之真錨點**：先量 `$VC_VEH_LINE$` 於 237 leaf 之引用數與其值；
          以**實際引用 `DT`／`332`／`WS`／`HDCC` 之 leaf** 為必命中錨點
          （須判已解）、以引用 `M182`／`M189`／`M240` 者為必不命中
          （**若後者於母體內為 0，則具名「該側無標的」，不得記為通過**）
      (2) **W-112 之判準改逐 leaf 行為層**：
          比對粒度由 Layer 3 群改為「該 leaf 之行為描述 ↔ Comfort 條文之行為描述」
          **錨點**：`Fail_Present` 類之 16 leaf 須全數判「查無」
          （現行判準對其回報「查得」，即失準之直接證據）
          重出 `screen_source.tsv`，列查得／查無兩數

W-116 **batch17 —— 10 條**
      自 W-114 重跑後之池，依 R-VS58 優先序選取。
      畫面層依 W-115(2) 之新對照表；查無者依 R-VS59(4) 標 `PENDING`。
      套 profile ＋ 各現行條文 ＋ Sibling Rows；
      §9 十七項自檢 ＋ 值表核對 ＋ 錨點。

## 禁區

git 不執行。**不搬移 `upstream/61_vf230_intake.md`**（路徑變更屬 Pei）。
不寫回工作簿。不代擬條文。各版保留不刪。
不得合併 A-VS119／123 之 leaf。

## 升級條件

W-114(2) 之「DBC 有而兩處皆空」之 token 數 > 5（則 A-VS102 之補收為系統性不足）；
W-115(1) 之必命中錨點未命中；
W-115(2) 之 16 leaf 未全數判「查無」（則新判準仍失準）；
W-116 之池不足 10。
```

---

## 6. 待 Pei

| 項 | 內容 |
|---|---|
| **DR-25′**（23）／**DR-19**（7，轉確認）／**DR-8′**（三碼）／DR-15′ 補送 | 待送 |
| **`upstream/61_vf230_intake.md` 之搬移** | 依 R-VS63，移入 `docs/upstream/vf230/00_intake.md` —— **路徑變更屬你** |
| pilot #3 之 13 條分類 | 分析層次包出 |
| batch14／15／16 共 33 條不在任何 pilot 範圍 | pilot #4 時機另定 |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS63 | 兩線編號空間分段預留；VF230 線另立目錄 | 分析層（本輪額度用畢） |
| batch16 形態之確認 ＋ 交付揭露 | 訊號層可測，畫面層 PENDING；須主動揭露 | 分析層 |
| W-112 判準改逐 leaf 行為層 | 其錨點為 16 個 `Fail_Present` leaf 須判查無 | 分析層 |
