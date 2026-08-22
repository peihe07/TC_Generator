# 40 下放包 — 20 輪覆核：可寫性之三個上界、A-VS69 裁定、21 輪指令

分析層寫入，2026-08-22。對象：`docs/upstream/18_writability.md`。

**覆核結論：接受。升級條件命中（88 / 37.1% > 40）。**
但本包之核心不是 88，是**它自陳 88 是上界，並給出把它降下來的驗法**。

---

## 1. A-VS69 —— **裁定：演繹成立**，`-009`／`-011` 不改

執行層問：`[Right Drive]` → `1 (Right Side)` 是演繹還是造值？

分析層自 `inputs/` 原始 docx 實測 `$DriverSide$` 之全部值形態：

| 值 | 次數 | 帶 `Nh:` 錨點 |
|---|---:|---|
| `[Right Side]` | 10 | — |
| `[Left Side]` | 7 | — |
| `[Right Drive]` | 4 | 無 |
| `[1h: Right Side]` | 4 | **有** |
| `[Right hand drive]` | 2 | 無 |
| `[0h: Left Side, 1h: Right Side]` | 2 | **有** |
| `[1h: Right hand]` | 1 | **有** |

**決定性實測**：

| 形態 | 命中 |
|---|---:|
| `Right Drive` | 4 |
| `Right hand drive` | 4 |
| **`Left Drive`** | **0** |
| **`Left hand drive`** | **0** |

**不存在 `Left Drive`／`Left hand drive`。**
即 `Right Drive`／`Right hand drive`／`Right hand` 三者**不是另一組平行命名**，
而是同一個值 `Right Side` 之三種措辭 —— 若其為平行體系，必有其左側對偶。

且 `4858559` 之上下文逐字：
`when $DriverSide$ = [Right Drive] and the customer selects … the LF(Passenger)
heated seat` —— **`LF` 被稱為 `Passenger`，只有右駕成立。** 語意自證。

```
R-VS43（值域演繹之界線，分析層裁定 2026-08-22；本輪唯一新條文）
規格所用之值不在匯流排值域內時，得以演繹對映之，**須同時滿足三條件**：

(1) **該 token 之匯流排值域為二值**，或目標在值域內唯一可判
(2) 該值域**已由來源自載之 `Nh:` 錨點定位**
(3) 待對映之措辭**無平行對偶**（如 `Right Drive` 存在而 `Left Drive` 不存在），
    或有其他來源內證（如上下文之語意自證）

三者缺一即**不得對映**，改標 `PENDING: DR-{n}`。

**成立例**：`$DriverSide$` 之 `[Right Drive]` → `1 (Right Side)` ——
二值域、`1h: Right Side` 錨定、`Left Drive` 全文 0 命中、
且 `4858559` 稱 LF 為 Passenger（右駕自證）。
`SwitchLHD/RHD-009`／`-011` **維持已放行，不改**。

**不成立例**：`$PowerMode$` 之 `IGN_START` → `START` ——
`CmdIgnSts` 之值域為六值（條件 (1) 不成立），目標非唯一。
**維持 PENDING**（19 輪之處置正確）。

於 TC 之 `reasoning` 須記明其為演繹並附三條件之逐項成立依據。
```

**A-VS69 依本條關閉。**

---

## 2. 88 是上界 —— 三項未驗各自往哪個方向

執行層之四項未驗，分析層評估其對「88」與「149」之影響方向：

| 未驗項 | 影響 | 方向 |
|---|---|---|
| §6-1 B2 不做跨條文錨點聚合 | `-032`／`-038` 已證假陽性 | **88 會降、149 會升** |
| §6-2 未與委派狀態交叉 | `OneStageHeatedSeat` 14 條可寫但 12 條 `pending` | **149 會降** |
| §6-3 原 30 token 中 4 個未命中 | 若其實際承載值域 | **88 可能升** |
| §6-4 結果動詞表未驗召回率 | 漏詞則尾綴修飾被誤判為外推 | **B1 之 8 可能降** |

**四項全部未驗之下，88 與 149 皆不可引用為決策依據。**
→ 21 輪三項作業即為此，**不生成 TC**。

**惟本層須記明一件事**：19 輪之判斷「先量洞再生成」是對的，
**但量出來的第一個數就是上界而非實數** —— 這與 W-58 之設計有關，
其判準為單條文比對，而 CFTS044 之錨點跨條文散佈。
**該設計缺陷屬分析層**（W-58 之規格由 39 包 §2 所定，未要求跨條文聚合）。
→ **A-VS70**。

---

## 3. A-VS67 —— 65 → 8，與 A-VS39 同型，記明其防護

初測 65 個相異條文，逐條讀後只有 8 條真阻塞；
57 條為**尾綴修飾**（參照之前已有具體結果動詞）。

**若止於初測，本包會報 `writable = no` 117 條（49.4%），
並把 57 個實際可寫之 leaf 誤列為阻塞。**

執行層逐條讀而非採信初測，且自行指出其與 A-VS39 同型。
**該處置即 R-VS29 之精神**（更嚴格／更寬鬆之判準改變計數時須逐筆判定）。

---

## 4. 21 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/40_review_round20.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/19_writability_refined.md，六節先留空。
     **編號續前**（18 輪已用 18；20 輪回報之編號更正記載正確，不追改）。
D-2  逐字轉錄 40 包 §1 之 **R-VS43** 入 RULINGS.md。
D-3  ANOMALIES.md：**A-VS69 關閉**（依 R-VS43）；新開 **A-VS70**
     （W-58 之單條文比對設計致 B2 為上界，成因在分析層之 39 包 §2 規格）。
     依 R-VS35 列兩數（含分析層側：40 包開立 anomaly 1 筆）。

## 作業（三項，R-VS25）

W-59  B2 之跨條文錨點聚合 → 修正 `writability.tsv`
      對每個被 B2 標記之 (token, 值) 對，**全文回查該 token 是否有任一
      `Nh:` 錨點可解該值**（即 18 輪 §6-1 自陳之驗法）。
      解得者由 B2 移除。
      **必列**：修正前後之 `writable = no` 兩數、逐筆移除清單。
      並依 **R-VS43** 逐筆判定其可否演繹對映（三條件逐項）——
      成立者標 `derivable`，其 TC 得寫但 `reasoning` 須記三條件。

W-60  可生成量 = writable ∩ delegate
      交叉 `writability.tsv` 與 `delegation_lookup.tsv`，產出
      `docs/reports/generatable.tsv`：
        leaf_id / writable / delegate / generatable(yes|no) / blocker
      `generatable = yes` ⟺ `writable = yes` ∧ `delegate ∉ {pending, blocked}`
      **必列**：generatable 之總數，及其逐 Layer 3、逐 Layer 2 之分布。
      **該數為本 feature 之實際可交付量**，19 輪之 149 為上界。

W-61  兩個判準之召回率
      (1) 原 30 token 中本次未命中之 4 個
          （`HSW_StatFailSts`／`Heated_Seats_Levels`／`Heated_Steats_Levels`／
            `TGW_DISP_STAT`）逐一追因：其於 237 leaf 所引條文中以何形態出現？
          若承載值域而未被抽出，**B2 之計數偏低，須補**
      (2) B1 之結果動詞表（15 詞）以**反向抽樣**驗其召回率：
          自 57 條「尾綴修飾」中隨機抽 10 條，逐條確認其確有具體結果動詞；
          自 8 條「整個結果外推」中逐條確認其確無。
          **抽樣數與抽法須具名**（canon §5a）

**本輪不生成 TC。** batch03 俟 W-60 之 `generatable.tsv` 產出後排。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。v1／v2／v3 保留不刪。

## 升級條件

W-59 修正後 `writable = no` 仍 > 60；
W-60 之 generatable < 100；
W-61(1) 之四 token 有任一承載值域而未被抽出；
W-61(2) 之抽樣有反例。
```

---

## 5. 待 Pei

| # | 事項 | 狀態 |
|---|---|---|
| — | **DR-18／DR-21／DR-22／DR-23 送出** | DR-21／22／23 之實例清單**待 W-59 修正後才定案** —— 建議**俟 21 輪產出再一次送**，否則 DR-21 之 82 leaf 清單會含假陽性 |
| — | DR-8／DR-11 送出 | 不阻塞，可併入同一封 |

**條文面無待裁項。**

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS43 | 值域演繹之三條件；`Right Drive` 成立、`IGN_START` 不成立 | 分析層（本輪額度用畢） |
| A-VS70 | W-58 單條文比對之設計缺陷，成因在分析層 | 分析層登記 |
