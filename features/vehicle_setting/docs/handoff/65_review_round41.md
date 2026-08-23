# 65 下放包 — R-VS62′（DR-8′ 撤回）、pilot #4、42 輪

分析層寫入，2026-08-23。**交付 129／池 16。**

---

## 1. R-VS62′ —— 母體實際用的兩個值，PROXI 表都有；**DR-8′ 撤回**

W-115(1) 先量而後錨，得母體實際引用僅 **2 leaf／2 值**：`WL`、`M4 OR MP`。

分析層查 `PROXI_HDCC27_R3` 之 `Format` 列 466 逐字：

```
… 93 = 552/MP (5D Hex) … 98 = 553/M4 (62 Hex) … 101 = WL (65 Hex) …
```

**兩個值皆已解**：

| 母體所用之值 | raw | 來源 |
|---|---|---|
| `WL` | **101** | PROXI 表列 466（LID v1.76 亦有，其截斷點即此） |
| `M4 OR MP` | **98 OR 93** | PROXI 表列 466 |

```
R-VS62′（分析層裁定 2026-08-23，取代 R-VS62）
`$VC_VEH_LINE$` 之值域取 `PROXI_HDCC27_R3_20250424.xlsx` 之
`Format` 分頁列 466（`Car_Configuration_15`／`Vehicle_Line_Configuration`）。

本 feature 母體實際引用者為二值，皆已解：
    `WL`        → 101 (65 Hex)
    `M4 OR MP`  → 98 (62 Hex) OR 93 (5D Hex)

R-VS62 原文所列之四碼（`332`／`WS`／`DT`／`HDCC`）**於母體命中 0**，
其為以 CFTS 全文之引用所裁 —— **該部分作廢**（R-VS50′ 之可及性回查）。

**DR-8′ 撤回，不送出。** 其縮限後之三碼（`M182`／`M189`／`M240`）
於母體命中亦為 0，覆之不解本 feature 任何一條。

A-VS140 依本條關閉。
```

**這是 R-VS50′ 立條以來第一次真正發揮作用** —— 若不先量而後錨，
我方會送出一份**覆了也解不開任何一條**的 DR。

---

## 2. 兩處確認

| 項 | 確認 |
|---|---|
| **§2.2 三數而非兩數** | **處置正確**。將 117 條「行為抽不出」計入「查無」，會把我方抽取式之不足記成 Comfort 素材之不足 —— 該區分是 R-VS34 之形態（掃不到 ≠ 資料缺）。**新判準目前只覆蓋 39%，該數須列入交付論述** |
| **§2.3 lint 未同步 R-VS60** | **與 R-VS55 同源而方向相反**（R-VS55 防 lint 較嚴、本項為 lint 較舊）。**併入 R-VS55 為其 (2)**：凡裁定同時影響分級與 lint 者，**兩處須同輪更新**，並以「新寫之 TC 被自身 lint 打掉」為其必失敗錨點 |

---

## 3. pilot #4 —— **43 條未入任何 pilot，且形態為新**

batch14／15／16／17 皆在 pilot #3 抽樣裁定之後產生；
其中 batch16／17 之形態（**畫面層全 `PENDING`**）為 pilot #1–#3 所未涵蓋。

```
pilot #4 之抽樣（分析層裁定）
母體 **43** 條（batch14 10／15 13／16 10／17 10）。

**必檢 8 條**（新形態，不抽樣）：
  batch16／17 之 `Fail_Present` 類各取 4 —— 其畫面層全為 `PENDING`，
  且其 Priority 為 R-VS56 之 P0(b)，**二者皆為首次交付之形態**

**分層抽樣 7 條**：
  維度 = batch（14／15／16／17）× `dr_dependent`（有／無）
  交叉格內各取 reqid 最小者；不足 7 時自條數最多之格補足

**合計 15 條。**
分析層先讀並附建議分類，Pei 覆核分類。
```

**pilot #3 之 13 條分類本包一併順延** —— 其 sheet 已在
`docs/reports/pilot3_sheet.md`，**與 pilot #4 合併為一次覆核**，
避免同一形態分兩次審。**分析層於次包出 28 條之合併分類。**

---

## 4. 42 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/65_review_round41.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/37_behavior_and_pilot4.md，六節先留空。
D-2  逐字轉錄 65 包 §1 之 **R-VS62′** 與 §2 之 **R-VS55(2)** 入 RULINGS.md；
     R-VS62 標「經 R-VS62′ 取代」（原文保留）。
D-3  `DATA_REQUESTS.md`：**DR-8′ 標「撤回，R-VS62′」**（原文保留）。
     A-VS140 關閉。
D-4  `delegation_lookup.tsv` 同步 R-VS59：廢除 `blocked` 之值
     （36 輪 §4 記其尚未同步）。
D-5  ANOMALIES.md 依 R-VS35 分線列兩數。D-6 骨架對照照做。

## 作業（三項，R-VS25）

W-117 **行為抽取式之補完**（§2.2 之 117 條）
      現行「對象 ∧ 行為」雙軸判準，其行為軸只抽出 74/191。
      (1) 對 117 條「行為未能抽出」者，**逐條讀其條文並歸類**：
            V1 行為存在而樣式未涵蓋（**可自解**，補樣式）
            V2 條文本無行為描述（純狀態賦值／適用性宣告）
            V3 行為描述於他條文（跨 reqid）
      (2) V1 補入樣式後重跑，列**補完前後之覆蓋率**（74/191 → ?）
      (3) 重出 `screen_source.tsv`，列查得／查無／未抽出 **三數**
      **錨點（R-VS54）**：16 個 `Fail_Present` leaf 須維持全數判「查無」

W-118 **pilot #3＋#4 之合併 review sheet**
      依 65 包 §3 之抽法產 `docs/reports/pilot4_sheet.md`，
      **pilot #4 之 15 條**（必檢 8 ＋ 分層 7），
      並附 `pilot3_sheet.md` 之 13 條清單（不重出全文，列 leaf_id 與其批次）。
      **列抽樣之交叉格矩陣**使抽法可複現。

W-119 **batch18 —— 10 條**
      自現行池（16）選取，依 R-VS58 優先序。**池不足 10 時取全部並回報。**
      套 profile ＋ 各現行條文 ＋ Sibling Rows；
      §9 十七項自檢 ＋ 值表核對 ＋ 錨點。
      **A-VS138 之 4 條已交付未更正者**：本輪一併更正
      （通風／方向盤節內誤引 `*_HS_STATFailSts`），產 `_v{n+1}`。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得將「行為未抽出」計入「查無」**（§2.2）。
不得合併 A-VS119／123 之 leaf。

## 升級條件

W-117(2) 之補完後覆蓋率 < 60%（則 Comfort 對照之結論仍不可用）；
W-117 之錨點未維持；
W-119 之池不足 10（**預期命中** —— 池 16，取 10 後餘 6）。
```

---

## 5. 待 Pei

| 項 | 內容 |
|---|---|
| **DR-25′**（解 23）／**DR-19**（7）／**DR-15′ 補送** | 待送 —— **DR-8′ 已撤回，待送剩十一份** |
| **pilot #3＋#4 合併覆核** | 28 條；分析層次包出建議分類 |
| **交付揭露** | `docs/reports/delivery_disclosure.md` 已列 **21 條畫面層 PENDING**；交付時須連同此檔 |

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS62′ | `VC_VEH_LINE` 取 PROXI 列 466；母體二值皆已解；**DR-8′ 撤回** | 分析層（本輪額度用畢） |
| R-VS55(2) | 裁定同時影響分級與 lint 者，兩處須同輪更新 | 分析層（R-VS55 之補充） |
| pilot #4 抽法 | 必檢 8 ＋ 分層 7；與 pilot #3 之 13 條合併覆核 | 分析層 |
