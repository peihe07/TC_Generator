# 57 下放包 — W-91 交付 0 之根因、R-VS55、36 輪

分析層寫入，2026-08-22。**W-91 交付 0 是判定結果，不是未執行 —— 該區分正確。**

---

## 1. 根因：分級說可寫，lint 說不可寫，兩者從未對過

池 36 條中 **33 條之斷言目標訊號不在基線 DBC**
（`TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm` 等三者，`SG_` 命中各 0），
而其分級為 **W0／generatable = yes**。

**三項同時成立而互不相容**：

| 條文 | 判 |
|---|---|
| R-VS19″ | 該 33 條在母體內（Radio／ECU 符） |
| R-VS51(2) | 其值域取 LID `Atlantis` 欄組，**確有值域** |
| R-VS9(1)′ ＋ L-VS2 | 訊號拼寫以 DBC 為權威，**而 DBC 沒有它** |

**有值域，沒訊號。** 分級只看前二者，lint 看第三者 —— **一寫出來就被打掉。**

```
R-VS55（分級與 lint 須同義，分析層裁定 2026-08-22；本輪唯一新條文）
可寫性分級之判準，**須涵蓋 lint 之全部否決條件**。
凡 lint 會否決之情形，分級須先判其為 W2，不得判 W0／W1。

現行須併入分級之 lint 條件（逐條具名）：
  **L-VS2** —— TC 內出現之 signal 名須於基線 DBC 中區分大小寫逐字存在
  §11 之尾句號、方括號、引號規則
  §10.5 之最低步數（扣除 `PENDING` 行，見 22 包）

二者若對「可寫」有不同定義，**以較嚴者為分級之判準**；
其不一致本身即為缺陷，須登記而非以任一方遷就。

**驗收（R-VS54）**：以 A-VS110 之 33 條為必命中錨點 ——
併入後其分級須由 W0 轉為 W2；未轉即併入未生效。
```

**併入後之預期**：`generatable = 108` 將下修至少 33 → **約 75**，
而已交付 76 條中有 4 條已判 W2 —— **即現行池實質為 0，本輪之 0 不是偶發。**

---

## 2. A-VS110 —— DR-25 之提問須同時涵蓋兩種讀法

33 條之 `EE Architecture` 皆為 `Atlantis Mid`，其訊號位於
`TELEMATIC_VEHICLE_SETUP`／`SETUP2`（**非** `SETUP3`），
而基線兩檔僅有 `SETUP3`。

**兩種讀法皆與現有證據相容**：

| 讀法 | 意涵 |
|---|---|
| (a) **素材缺件** | 承載 Mid 網段之 DBC 我方未持有 |
| (b) **R-VS19″ 判錯** | 該等條文屬 Atlantis Mid 專屬，其訊號不在本專案之匯流排上 —— 即不適用 R1LR |

**(b) 若成立，R-VS19″ 之 `Radio`／`ECU` 判準即不足** ——
`Radio` 含 R1L 只表示該條文之文字涵蓋該車型，不表示其訊號在本專案佈線上存在。

```
DR-25（分析層擬，Urgency High，型 A/B 兼具）
CFTS044 之 33 個 SWE leaf（`EE Architecture: Atlantis Mid`）其行為賦值於
    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm ／ .FR_HS_Cmd_Tlm
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm
三者於本專案之基線 CAN 資料庫
（`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`，
 VersionYear 25／VersionWeek 50）中**皆不存在**（`SG_` 命中各 0）；
基線僅有 `TELEMATIC_VEHICLE_SETUP3`。

而 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis` 欄組
確載其值域（列 763：`0 = Heated_seat_off` … `3 = Heated_seat_high`）。

請確認：
(a) 承載該三訊號之 CAN 資料庫為何？（請提供）；或
(b) 該等訊號不適用於 R1LR，其對應之 CFTS044 條文於本專案不需驗證？

影響：33 個 SWE leaf 之 TC 無法寫出可執行之訊號斷言。
若為 (b)，我方之適用性判準（`Radio` ＋ `ECU`）須修訂。
```

**與 DR-21 之關係**：DR-21 之 `*_Cmd_Tlm` 大宗即此。
**DR-25 取代其中該部分之提問**，DR-21 保留其餘 token。

---

## 3. 三項裁定

### 3.1 A-VS111 —— 閘之呼叫範圍不足，我的條文寫漏

`guard_new_conclusion()` 僅於「值需演繹」之路徑被呼叫，
**條文自帶值者完全不過閘**。R-VS44 令其「併入判定腳本之輸出階段」，
**未言明其須涵蓋所有進入 TC 之 (token, 值)**。

```
R-VS44″（範圍之更正，分析層裁定；不另編號，記為 R-VS44 之(4)）
`guard_new_conclusion()` 須於**每一個進入 TC 之 (token, 值)** 上呼叫，
不限「需演繹」者。條文自帶值、DBC 直接命中、LID 直接命中者**一律過閘**。
**驗收（R-VS54）**：以池中該 1 條（條文自帶值而 token 為 DR-15 標的）
為必命中錨點 —— 併入後須被攔下。
```

### 3.2 A-VS109 —— W-87 之式補一項

`This section defines` 未在四式內。**補為第五式**，並依 R-VS46 於下次
宣稱窮盡時逐式列出涵蓋清單。

### 3.3 §2.4 之 `ThirdRowHeadrestDump-038` —— **判為造值，退回**

執行層自陳其 `not selectable` 係自 tc_title 與條文推得，**非轉錄**。

**依 §8.4.1，推論即造值。** 退回原形態：維持記錄步驟並命名，
其 ER 為 `<變數名> is recorded`；**該 TC 之比較步驟若因此無值可比，
標 `PENDING: DR-{n}` 並登記。**

**執行層列此供覆核而未自行決定，正確。**

---

## 4. `design_method`／`priority` 兩欄 —— 待 Pei

| 欄 | 交付本 | 本 feature | 對映 |
|---|---|---|---|
| `design_method` | 受控下拉，**9 值**，形態 `中文 (English)` | 純英文 **5 值** | **一對一無歧義**（執行層已列對照表） |
| `priority` | P0 27／P1 190／P2 68 | P1 64／P2 12，**無 P0** | 待判 |

**分析層建議**：
- `design_method` **對齊交付本之受控值**（一對一對映已具名，無歧義，且該欄為下拉選單所控，不對齊即無法填入工作簿）
- `priority` **先查判準**：本 feature 之 P0 缺項，須確認是「確無 P0 級項」或「分級判準與交付本不同」——
  canon §10.2 之 P0 定義含 `vehicle-critical CAN signal`，而本 feature 全為 CAN 訊號驅動之 HMI 行為，**P0 為 0 值得複查**

**二者皆屬交付形式，待 Pei 裁。**

---

## 5. 36 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/57_review_round35.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/32_alignment_and_gate.md，六節先留空。
D-2  逐字轉錄 57 包 §1 之 **R-VS55** 與 §3.1 之 **R-VS44(4)** 入 RULINGS.md。
D-3  `DATA_REQUESTS.md` 新開 **DR-25**（57 包 §2 全文，Urgency High）；
     DR-21 註明「`*_Cmd_Tlm` 之部分由 DR-25 承載」。
D-4  ANOMALIES.md：A-VS109／110／111 標其處置；依 R-VS35 列兩數。D-6 照做。

## 作業（三項，R-VS25）

W-98  **判準之三項補完**（依 R-VS55／R-VS44(4)／§3.2）
      (1) 驅動併入 **L-VS2 之存在性**：TC 所需斷言之 signal 須於基線 DBC
          區分大小寫逐字存在；不存在者判 **W2**
          **錨點**：A-VS110 之 33 條須由 W0 轉 W2
      (2) `guard_new_conclusion()` 改為於**每一個進入 TC 之 (token, 值)**
          呼叫；**錨點**：池中該 1 條（條文自帶值而 token 為 DR-15 標的）須被攔下
      (3) W-87 補第五式 `This section defines`；
          依 R-VS46 列本輪之涵蓋清單與**未測者**
      (4) 全量重跑，列 W0／W1／W2 與 **129/2/106** 之對照，
          及 `generatable` 與 **108** 之對照

W-99  **`ThirdRowHeadrestDump-038` 之退回**（§3.3）
      退回記錄形態並命名；比較步驟無值可比者標 `PENDING` 並登記。
      重跑 §9 自檢 ＋ 錨點。

W-100 **batch13 —— 10 條**（自 32 輪順延四輪）
      自 W-98 重跑後之池選 leaf。**池不足 10 時取全部並回報其數；
      池為 0 時逐 leaf 列其阻塞類別與所屬 DR**（同 35 輪 §2.2 之作法）。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得自行對齊 `design_method`／`priority`**（待 Pei）。
不得跨列引入訊號名；不得放寬 L-VS2。

## 升級條件

W-98 之任一錨點未命中（則該項併入未生效）；
W-98(4) 之 `generatable` 下修後 < 40；
W-100 之池為 0（則本 feature 之產能全繫於 DR-25／DR-15／DR-21 之答覆）。
```

---

## 6. 待 Pei

| 項 | 內容 |
|---|---|
| **DR-25**（33 leaf，High） | **本包新擬，最急** —— 其答覆決定 R-VS19″ 是否須修訂 |
| DR-21／DR-17／DR-24′／DR-18／DR-11／DR-20／DR-23／DR-8′ | 待送 |
| DR-15 | 待覆；覆後須回溯已交付 5 條 |
| **`design_method`／`priority`** | §4 之二欄，屬交付形式，待裁 |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS55 | 分級判準須涵蓋 lint 之全部否決條件；不一致以較嚴者為準 | 分析層（本輪額度用畢） |
| R-VS44(4) | 閘須於每一個進入 TC 之 (token, 值) 呼叫 | 分析層（R-VS44 之範圍更正） |
| DR-25 | Mid 網段訊號不在基線 DBC（33 leaf） | 分析層擬 |
