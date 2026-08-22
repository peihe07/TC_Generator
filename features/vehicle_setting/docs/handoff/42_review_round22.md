# 42 下放包 — 22 輪覆核：79 個 leaf 卡在一份文件上、DR 之二型、23 輪指令

分析層寫入，2026-08-22。對象：`docs/upstream/20_stable_core.md`。

**覆核結論：接受。** `generatable` 由 141 降為 **72**，且降得有依據 ——
21 輪已標記之風險本輪落地，不是新發現。

**但本包最有價值的是 §6-1：DR-22 問錯了問題。**

---

## 1. 79 個 leaf 卡在**一份既有文件**上

四個 PROXI 參數之 LID `Format` 皆為 **`See Proxi Table`** ——
**LID 有記載，只是把值域轉指出去；而該表不在 `inputs/`。**

| 現況 | 實情 |
|---|---|
| DR-22 問「token 於三處無記載」 | **錯**。LID 有記載 |
| 其解法為「請上游定義該參數」 | **錯**。定義存在，我方沒有那份表 |

**兩者之收件人與前置時間完全不同**：
前者須上游撰寫並經審查；後者只是**把一份已存在的檔案給我們**。

```
R-VS45（DR 之二型，分析層裁定 2026-08-22；本輪唯一新條文）
DATA_REQUEST 於開立時須標明其型別：

  **型 A — 規格缺陷**：來源文件本身未定義、自相矛盾、或引用不存在之物。
    解法：上游修訂規格或補寫定義。前置時間以週計。
    例：DR-15（請求訊號 1 bit vs 階數）、DR-19（EngRun_Stat 四值無對應）

  **型 B — 素材缺件**：定義存在且被來源明確指名，我方未持有該文件。
    解法：**取得該文件**。前置時間以日計，且**往往不需上游動作** ——
    先於客戶需求目錄唯讀搜尋，找到即解。
    例：`See Proxi Table` 所指之 PROXI 表、`TLM HMI Document`

**型 B 之處置順序**：
  (1) 先於客戶目錄唯讀搜尋（唯讀，不複製 —— 素材補入仍屬 Pei）
  (2) 搜尋無果，方以「請提供該文件」為訴求開 DR，
      **提問文不得寫成「請定義該參數」** —— 那是型 A 之訴求

理由：DR-22 以型 A 之措辭承載型 B 之訴求，
其影響為 **79 個 leaf**（`writable` 由 170 降至 91 之主因）。
若上游依其字面作答，會回覆一份「參數定義」，而我方要的是一份既有的表。
```

**DR-22 依本條改寫為型 B**，其提問文見 §2。

---

## 2. DR-22′（改寫，型 B）

```
DR-22′（型 B — 素材缺件）
`Logical Identifiers and CAN Mapping v1.76` 之下列四個 PROXI 參數，
其 `Format` 欄逐字為 **`See Proxi Table`**：

    Cooled_Seats／Heated_Seats／Heated_Seat_Levels／Heated_Steering_Wheel

即其值域已定義，惟定義於該表所轉指之 **PROXI Table**，
而該文件不在我方持有之素材中。

**請提供該 PROXI Table**（檔名＋版本＋發行日）。

我方待解之值：`Front Seats`（Cooled_Seats／Heated_Seats）、
`One Level`（Heated_Seat_Levels）、`Present`（Heated_Steering_Wheel）。

影響：**79 個 SWE leaf** 之 Pre-Condition 與 Procedure 無法在不編造值之下寫出
（`writable` 由 170 降為 91）。

註：同表之 `Heated_Steering_Levels` 有實 Format
（`0 = 1 Level`／`1 = 2 Levels`／`2 = 3 Levels`），
故該轉指非全表性質，而是逐參數之選擇。
```

**且在送出前先做 §4 之 W-65（唯讀搜尋）** —— 若該表在客戶目錄內，
本 DR 不必送出。**79 個 leaf 可能一日內解除。**

---

## 3. 三項裁定（皆適用既有政策，不另立條文）

### 3.1 A-VS75 —— 補極性表，R-VS44 已提供安全網

執行層以「補表會撞 DR-15 之爭點」為由未補，**謹慎正確**。
但 **R-VS44 已於本輪實作為輸出閘**（W-63 之錨點通過且可失敗）：
補表後新增之 derivable 若落在 DR-15 範圍，**閘會攔下並標 `DR-CONFLICT`**。

```
分析層裁定：補表，並依 R-VS44 過閘。
極性對照表補入 9 個漏詞之對偶（`pressed↔not pressed`／`high↔low`／
`start↔stop`／`disabled↔enabled`／`lock↔unlock`／`true↔false`／
`valid↔invalid` 等），**其新增之 derivable 逐筆列出並標其是否過閘**。
`pressed` 相關者預期全數 `DR-CONFLICT`（DR-15）——
**該預期若不成立，即閘有漏，須回報。**
```

此舉之意義不在增加 derivable，在**驗證閘確實在擋** ——
以一個已知會撞的輸入去測它。

### 3.2 §6-3 `<Tsend>` —— canon §8.7.1 已定其處置

canon §8.7.1 逐字：

> Every trigger / release threshold MUST come from the spec and appear as a
> **concrete value** in the Pre-Condition, **never vague language**.

`<Tsend>` 無具體值，故**不得作為 ER 之通過條件**。
§8.4.1 允許 `<configured limit>` 形態者為**佔位之書寫**，非**可判定之斷言**。

```
分析層裁定：
(1) `<Tsend>` 於 procedure 保留原樣（來源逐字）
(2) **ER 不得以 `within <Tsend>` 為通過條件** ——
    改寫為可觀察之終態（訊號值已變更為 X）
(3) 時間量測另開 **DR-24（型 A）**：索取 `<Tsend>` 之具體值
    影響：`4858320` 及同型引用 `<Tsend>` 之 leaf（數量待 W-66 掃出）
```

### 3.3 §6-4 覆蓋均勻性 —— 選 leaf 判準改為輪流

以 reqid 升冪取，會先耗盡 `Common Features`（穩定核心 30 / 72），
使四個 Layer 2 之進度失衡。

```
分析層裁定（作業判準，不另編號）
batch04 起，選 leaf 改為**逐 Layer 2 輪流**：
每批 10 條，自四個 Layer 2 之穩定核心各取，
比例依其穩定核心之規模加權，**每個 Layer 2 至少 1 條**。
批內順序仍依 reqid 升冪。
理由：canon §4.1.3 之覆蓋均勻性；且早期即觸及四類 leaf，
可使各 Layer 2 特有之問題提早暴露，而非集中於後期。
```

---

## 4. 23 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/42_review_round22.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/21_proxi_hunt.md，六節先留空。
D-2  逐字轉錄 42 包 §1 之 **R-VS45** 入 RULINGS.md。
D-3  `DATA_REQUESTS.md`：
     - **全部未結 DR 逐筆標型別（A／B）**（R-VS45）
     - **DR-22 改寫為 DR-22′**（42 包 §2 全文，型 B），原文保留加註
     - 新開 **DR-24**（型 A，`<Tsend>` 之具體值），提問文分析層已定（42 包 §3.2）
D-4  ANOMALIES.md 依 R-VS35 列兩數（含分析層側：42 包開立 0 anomaly／1 DR）

## 作業（三項，R-VS25）

W-65  **PROXI Table 之唯讀搜尋**（最高優先 —— 79 leaf）
      於 `/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/` 之下
      **全目錄唯讀搜尋**（不限 26PI2.5/HMI），關鍵詞：
        `PROXI`／`Proxi Table`／`Cooled_Seats`／`Heated_Seat_Levels`
        ／`Heated_Steering_Wheel`
      檔型含 xlsx／xls／pdf／docx／csv。
      PDF 須先驗文字層產出量；抽不到者標「未解析」不猜（§5a 條 12）。
      **唯讀，不複製任何檔案入 `inputs/`**（素材補入屬 Pei）。
      找到者列其路徑、檔名、版本、並抽出四個參數之值域以佐證其為所指之表。
      **找不到亦須列出已掃之目錄與檔數**（餘數驗證，R-G10）。

W-66  兩個掃描盲區
      (1) **B4 之偵測**（A-VS76）：以措辭 `invalid`／`all other states`／
          `any other value`／`unsupported`／`not defined` 掃 237 leaf 所引條文，
          逐條判其可寫性是否依賴「他條文之有效值列舉」。
          `4858310`／`4858340` 為已知實例（其解由 `4858307` 提供）。
          **列出同型之總數**
      (2) `<Tsend>` 及同型時間符號（`<T...>`）之全量掃描，
          列出引用之 leaf 數，供 DR-24 之影響範圍
      (3) 補極性對照表 9 詞（42 包 §3.1），**逐筆列出新增之 derivable
          及其是否過 R-VS44 之閘**；`pressed` 相關者預期全數 `DR-CONFLICT`，
          **不成立即回報**

W-67  batch04 生成 —— **10 條**
      選 leaf 依 42 包 §3.3 之**逐 Layer 2 輪流**判準，
      自穩定核心（扣除已用者）取，每個 Layer 2 至少 1 條。
      **先列出四個 Layer 2 之穩定核心餘量。**
      套 profile 全部 ＋ canon §8.7.5 v3 ＋ R-VS43 ＋ `## Sibling Rows`。
      §9 十七項逐項自檢 ＋ DBC 值表逐字核對。
      **ER 不得以 `within <Tsend>` 為通過條件**（42 包 §3.2）。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。v1／v2／v3 保留不刪。
**不得複製任何檔案入 `inputs/`**（W-65 為唯讀搜尋）。
**不得以任何判準解掉未結 DR 所問之事項**（R-VS44）。

## 升級條件

W-65 找到 PROXI Table（**正向升級** —— 79 leaf 可解，須立即回報）；
W-66(1) 之 B4 同型總數 > 20；
W-66(3) 之 `pressed` 相關 derivable 有未被閘攔下者；
W-67 之某 Layer 2 穩定核心餘量為 0。
```

---

## 5. 待 Pei

| # | 事項 |
|---|---|
| — | **DR-23（型 A，B1 = 3 leaf）可送** —— 清單已定 |
| — | **DR-22′ 暫緩送出**，俟 W-65 之搜尋結果；找到則不必送 |
| — | DR-18／DR-8／DR-11 可併同送 |
| — | DR-21 之實例清單本輪已定案（B2 65 leaf），可送 |

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS45 | DR 之二型（規格缺陷／素材缺件）；型 B 須先唯讀搜尋 | 分析層（本輪額度用畢） |
| DR-22′ | 改寫為型 B，訴求為取得 PROXI Table | 分析層擬 |
| DR-24 | `<Tsend>` 之具體值（型 A） | 分析層擬 |
