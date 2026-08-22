# 41 下放包 — 21 輪覆核：DR-15 之近失、B1 依既有政策降為 3、22 輪指令

分析層寫入，2026-08-22。對象：`docs/upstream/19_writability_refined.md`。

**覆核結論：接受。** 本包之最重要處不在任何一個數字，在 §2.2。

---

## 1. §2.2 —— **本 feature 迄今最接近實質損害的一次**

初版 R-VS43 實作判出 20 組 derivable，其中包含：

```
FL_HS_RQ 之 High / Low / Medium  →  值域 {Not_Pressed, Pressed}
```

**那正是 DR-15 所問之事本身** —— 請求訊號為 1 bit 或承載階數，影響 160 leaf，
**且該 DR 已於 2026-08-22 送出、待覆。**

把它判為「可演繹」，等於**我方以一條內部判準，逕自解掉一個已送出、
正在等上游回覆的問題** —— 而上游之答覆若為 (b)（請求訊號承載階數），
我方已依 (a) 寫出之 160 leaf 全數錯誤，且**沒有任何痕跡顯示我方曾決定過這件事**。

執行層自行發現並修正兩處判準（(1) 加共享實詞之唯一性測、
(3) 無對偶詞可測時預設不成立），20 → 1。

```
R-VS44（分析層裁定 2026-08-22；本輪唯一新條文）
**任何判準、演繹、對映或正規化，不得使一個已開立且未結之 DR 所問之事項
獲得解答。**

實作要求：凡自動化判定（值域演繹、別名聚合、錨點解析、正規化合併等）
產出之結論，須先與 `DATA_REQUESTS.md` 之未結 DR 清單交叉：
  該結論若落在某未結 DR 之提問範圍內 → **一律標 `DR-CONFLICT`，
  不採用該結論**，並於上繳具名該 DR 編號。

**待覆之 DR 尤然**：其已送出，上游正在作答；我方自行作答會使
兩個答案並存而無人知曉何者生效。

理由：R-VS43 之初版實作將 `FL_HS_RQ` 之 High／Low／Medium 判為可演繹，
而該值正是 DR-15 之提問標的（已送出待覆，影響 160 leaf）。
若採之，我方將以內部判準解掉一個外部問題，且無痕跡。

**本條之檢查應併入所有判定腳本之輸出階段，非事後人工核對。**
```

---

## 2. A-VS72 —— **既有政策已有答案：B1 應為 3**

執行層問：5 條 `TLM has to show an informative popup relative to the failure`
是否足以撰寫可觀察之 ER？並正確地不自行改判。

**該問題已由 R-VS17 裁定（35 包之前，17 包 §2 開立、34 包確認）：**

```
R-VS17（現行，逐字）
DR-5-B 未到位期間：受影響之 17 leaf（16 引 TLM HMI Document ＋
1 引 PDO graphics）仍產出 TC，其 ER 寫至**訊號層**為止，
畫面層之斷言以 Remarks 標 BLOCKED 並註明其待補來源，
不寫入 expected_result。
不得以「畫面文字未知」為由不產 TC。
```

`4859386`／`4859387`／`4859448`／`4859449`／`4859498` 之條文形態為
`IF (…_STATFailSts == "Fail_Present") THEN TLM has to show an informative
popup …` —— **其觸發條件在訊號層完全可寫**（`Fail_Present` 之值已由
LID 與 DBC 雙來源給出），**正是 R-VS17 所指之情形。**

```
分析層裁定 2026-08-22（適用既有政策，不另立條文）
B1 之 8 條中，5 條「informative popup」型**依 R-VS17 為可寫**：
  TC 之觸發與訊號層 ER 照寫，畫面層（popup 內容）標 BLOCKED 於 Remarks。
**B1 由 8 降為 3**（`4858560`／`4859509`／`4859032`）。
`writability.tsv` 之該 5 leaf 改為 `writable = yes`，
並增欄 `blocked_layer = screen`／`blocked_ref = DR-5-B`。

A-VS72 依此關閉；動詞表**不需補 `has to show`** ——
其判定結果由 R-VS17 決定，非由動詞表決定。
```

**此為 canon §5a 條 17 之形態：立新規則前先查既有政策。**
執行層未自行改判是對的；分析層之職責即在此處指出該政策。

---

## 3. 三個數字仍為界 —— 但已可分出「穩定核心」

| 量 | 現值 | 方向 |
|---|---:|---|
| `writable = yes` | 165 | §6-1 之 4 個 PROXI token 回查 LID 後**可能降**（79 leaf 帶 `quoted_form_risk`） |
| B1 | 8 → **3** | 本包 §2 已降，**5 leaf 轉為可寫** |
| `generatable` | 141 | 承接上二者 |

**但兩個修正方向相反且範圍已知**，故存在一個**不受任一修正影響的子集**：

```
穩定核心 ⟺ generatable = yes ∧ quoted_form_risk = no
```

該子集之 leaf 無論 §6-1 之回查結果如何，皆為可生成。
**batch03 應自此子集出，不必等 §6-1。**

→ **W-64 之選 leaf 判準即此。** 其規模由執行層實測（141 − 79 之交集部分）。

---

## 4. 其餘未驗之處置

| 項 | 處置 |
|---|---|
| §6-1 4 個 PROXI token 未回查 LID | → **W-62(1)** |
| §6-2 值之第三種比對形態未量 | → **W-62(2)**，**採 W-22 之餘數驗證法**（該法已於 08 輪證明有效） |
| §6-3 141 為上界 | 由 W-62 收斂；本輪以穩定核心規避 |
| §6-4 極性對照表 5 對之召回率 | → **W-62(3)**，小項；**derivable 僅 1 組，其漏詞之影響有界** |

---

## 5. 22 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/41_review_round21.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/20_stable_core.md，六節先留空。
D-2  逐字轉錄 41 包 §1 之 **R-VS44** 入 RULINGS.md。
D-3  依 41 包 §2 更新 `writability.tsv`：5 條 informative popup 型改
     `writable = yes`，增 `blocked_layer = screen`／`blocked_ref = DR-5-B`；
     B1 由 8 記為 3。**A-VS72 關閉。**
D-4  ANOMALIES.md 依 R-VS35 列兩數（含分析層側：41 包開立 0 筆）。

## 作業（三項，R-VS25）

W-62  可寫性之最後收斂
      (1) `== "值"` 之 14 個未解 token 中，4 個 PROXI 參數
          （`Cooled_Seats`／`Heated_Seats`／`Heated_Seat_Levels`／
            `Heated_Steering_Wheel`）**逐一回查 LID 之 Format 欄**
          （含 `See Proxi Table` 之標記，其為未解而非不存在）。
          解得者自阻塞移除；未解者維持並標其來源為 LID 轉指。
      (2) **值之比對形態以餘數驗證窮舉**（採 W-22 之法）：
          取全部 (token, 條文) 對，減去 `= [值]` 與 `== "值"` 兩式已命中者，
          逐筆檢視餘數之上下文，分類為
            (a) 不承載值域　(b) 承載值域但形態為第三式　(c) 無法判定
          **通過條件：(b) 為 0，或 (b) 全數化為新式並重跑。**
          已知候選形態：`= '值'`、`is set to`、`shall be`、表格式同列並置。
      (3) R-VS43(3) 之極性對照表以反向抽樣驗召回率：
          自本 feature 之 30 個 token 之全部值中，抽出含極性詞者，
          確認其對偶詞是否在表內。**抽法與抽樣數具名。**
      **必列**：修正後之 `writable = no`／`generatable` 兩數，
      及其與 21 輪之 72／141 之對照。

W-63  R-VS44 之實作
      將「結論與未結 DR 交叉」併入 `writability_w58.py`／
      `attribution.py` 等判定腳本之輸出階段。
      **驗收錨點**：以 `FL_HS_RQ` 之 `High`／`Low`／`Medium` 為測試輸入，
      腳本須輸出 `DR-CONFLICT: DR-15` 而非 `derivable`。
      **該錨點須可失敗** —— 移除交叉檢查後應判為 derivable。

W-64  batch03 生成 —— **10 條**
      選 leaf：`generatable = yes` ∧ `quoted_form_risk = no`（**穩定核心**），
      依 reqid 升冪取 10。**先列出穩定核心之總數**；不足 10 則取全部並回報。
      套 profile 全部 ＋ canon §8.7.5 v3 ＋ R-VS43（若有演繹須記三條件）
      ＋ `## Sibling Rows` 注入。
      §9 十七項逐項自檢 ＋ DBC 值表逐字核對。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。v1／v2／v3 保留不刪。
**不得以任何判準解掉未結 DR 所問之事項**（R-VS44）。

## 升級條件

W-62(2) 之 (b) 類非 0 且無法化為新式；
W-62(1) 回查後 `writable = no` 較 72 增加；
W-63 之驗收錨點不可失敗；
W-64 之穩定核心不足 10。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| — | **DR-18／DR-21／DR-22／DR-23／DR-8／DR-11 送出** —— DR-21 之實例清單俟 W-62 定案（A-VS71 之 14 token 尚有 4 個未回查）；**DR-22／DR-23 之清單已定**（B3 = 2 leaf；B1 = **3** leaf，本包 §2 已降），**可先送** |

**條文面無待裁項。**

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS44 | 判準不得解掉未結 DR 所問之事項；輸出階段須交叉檢查 | 分析層（本輪額度用畢） |
| A-VS72 之裁定 | B1 5 條 informative popup 依 R-VS17 可寫，B1 8 → 3 | 分析層（適用既有政策，不另立條文） |
