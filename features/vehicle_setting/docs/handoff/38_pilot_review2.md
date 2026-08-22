# 38 下放包 — pilot review 第二輪：內容層之三項缺陷、放行建議

分析層寫入，2026-08-20。對象：`generated/batch01_v2.json`（**逐條讀過 10/10**）。

**形式面：通過。** 27 個訊號行對 2,044 個 DBC signal 值表逐字核對 0 不符；
殘留三件組 0（同一支反查腳本兩本各跑，v1 得 34、v2 得 0）；
四欄未預期變動 0。**這是本 feature 迄今最強的一次自證。**

**內容面：三項缺陷、一項待對照。** 皆為 metadata 層驗證所看不見者 ——
**pilot 之存在意義即此。**

---

## 1. 缺陷（defect，須改）

### D-1 `SwitchLHD/RHDConfiguration-009` —— **TC 未驗證其需求所主張之事**

test_item 逐字：

> If there is no Driver or Passenger label …, the `$DriverSide$` signal value
> **shall have no impact on** the Heated and Vented seat switch behavior.

該需求主張的是**一個比較**：`$DriverSide$` 改變時，行為不變。

而 TC 之 procedure 為：於 `PROXI Driver_Side = 1 (Right Side)` 之下
讀 `FL_HS_Tlm` 為 0 → 按下 → 讀為 1。
**它證明的是「右駕下按鍵會送出請求」，不是「左右駕之間沒有差別」。**

即使 `$DriverSide$` 對行為**有**影響，本 TC 仍會通過 —— **§7 之 false pass。**

**修法**（§5.6 baseline comparison）：
```
1. Set PROXI Driver_Side = 0 (Left Side) and power cycle the HU
2. Press the left front heated seat switch and record the value of
   $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$
3. Set PROXI Driver_Side = 1 (Right Side) and power cycle the HU
4. Press the left front heated seat switch and check that
   $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ is the same as recorded in step 2
```
ER 之末行採 §5.6 之比較式（`the same as recorded in step 2`）。

> **`-011` 之寫法正確且可為範本** —— 其 step 1 記錄、step 4 比較，
> 正是 `-009` 所缺者。同一 Layer 3 內兩條，一條做對一條沒做。

### D-2 `Stop-StartSystem-004` —— **末步驟無 action**（§5.5）

其 procedure 步驟 4 為 `Check that all heat and vent switches remain active
and selectable` —— 只有 check，無 action。
成因為其 action（設定 `$EngRun_Stat$`）落在步驟 3 之 `PENDING: DR-19`。

**DR-19 未覆期間之修法**：將驗證併入最後一個**可執行**步驟，
或於 PENDING 行後補一個可執行之 action 步驟。**不得讓末步驟只剩 check。**

### D-3 `Stop-StartSystem-006` —— **可執行步驟僅 1**（§10.5）

其 procedure 為兩個 numbered item，但**第 1 項是 `PENDING: DR-19` 佔位**，
實際可執行者僅第 2 項。§10.5 要求至少 2 步（Setup → Verification）。

```
分析層裁定 2026-08-20（記於 profile，非新編號條文）
`PENDING: DR-{n}` 佔位行**不計入 §10.5 之最低步數**。
一條 TC 若扣除 PENDING 行後不足 2 個可執行步驟，
該 TC 標 `split_flag = false` 但於 `split_reason` 記
`BLOCKED-BY-DR-{n}: executable steps < 2`，
**並自本批移出，待該 DR 覆後再入批**。
```
→ `-006` **自 batch01_v2 移出**，`-004`／`-005` 依 D-2 修正後保留
（二者扣除 PENDING 行後各餘 3 與 2 個可執行步驟）。

---

## 2. 待對照（style-divergence，不阻放行）

### S-1 ER 之 `is registered without a bus error`（8 處）

該措辭為送出型步驟之 ER。分析層**未能自既有交付本枚舉其house style** ——
`features/comfort/inputs/` 之 036 為近空白樣板（59 列、TC 內容全空），
無可枚舉之樣本；SWC 0708 不在本 feature 之 `inputs/`。

**依「格式裁決須先枚舉既有交付本之實際書寫樣式」之原則，
分析層不自訂此處之措辭。** 記為 **A-VS62**，兩條路徑擇一：

(a) Pei 提供 SWC 0708 或任一已交付本之 CAN 送出步驟樣本 → 據以對齊
(b) 逕以 pilot review 認可現行措辭 → 記為本 feature 之既定寫法

**不阻擋放行** —— 若日後對齊，為單欄字串替換。

---

## 3. 正確而值得記明者

| 項 | 評述 |
|---|---|
| `ThirdRowHeadrestDump-025` 無訊號行 | **正確**。其驗證對象為軟鍵與頭枕實體位置，無 CAN 觀察點。**不是遺漏**，執行層之自陳成立 |
| 同條刪除「再按一次」 | **正確**。條文僅述 `only to lower … not to raise`，未定義再按之行為 |
| `PROXI Driver_Side = 1 (Right Side)` | **正確**。canon §8.7.5(c) 明定 `$` 為訊號之標記而非 PROXI 之標記（v2 之指派相反，v3 已更正） |
| `-011` 之 baseline 比較 | **正確**，且為 D-1 之修法範本 |
| `-004`／`-005` 之 `distinguishing_axis` | **正確**，軸為 `trigger_state`，delta 具名兩者之 `ESS_ENG_ST` 差異 |
| `reasoning` 之 `未涵蓋` 段 | **正確**，逐條具名 PENDING 與刪步驟之依據 |

---

## 4. 放行建議（**pilot 之裁決屬 Pei**）

| leaf | 狀態 | 處置 |
|---|---|---|
| `Stop-StartSystem-002`／`-003`／`-007` | 通過 | **放行** |
| `SwitchLHD/RHD-011` | 通過 | **放行** |
| `ThirdRowHeadrestDump-025` | 通過 | **放行** |
| `SwitchLHD/RHD-009` | **D-1 缺陷** | 依 §5.6 改寫後放行 |
| `Stop-StartSystem-004`／`-005` | **D-2 缺陷** | 修末步驟後放行（PENDING 保留） |
| `Stop-StartSystem-006` | **D-3** | **移出批次**，待 DR-19 |
| `SwitchLHD/RHD-010` | DR-20 | **移出批次**，待 DR-20 |

**建議：5 條逕予放行、3 條改寫後放行、2 條移出待覆。**
**pilot 通過與否由 Pei 裁定**（canon §1.2）。

---

## 5. 未執行之下放包（**執行層未讀 36／37**）

執行層自陳未讀 `36_framework_signoff.md`／`37_rd1_dispatch.md`。
**成因為分析層在 18 輪指令發出後才寫該二包**，非執行層之疏漏。

→ 其文書項（D-5～D-10）順延至 19 輪。

---

## 6. §4.1.4 之疑慮 —— **canon 已自帶答案**

執行層記：「profile 合法化了 Layer 2 粗粒度，但 §4.1.4『以 Test Set 為
覆蓋分析單位』在本 feature 仍不可行（46 leaf 橫跨 7 個 Layer 3）」。

**canon §4.1.4 第 3 點逐字**：

> **Coverage analysis** — Layer 3 is the unit of completeness check.
> 「Have we covered every RD under PT1?」is answerable；
> 「Have we covered every RD under Playing Tab?」mixes too many spec chapters.

**覆蓋分析之單位本來就是 Layer 3，不是 Test Set。**
canon 早已預期 Layer 2 會混章節，此即其設 Layer 3 之理由。
**該疑慮不成立，不需新條文，亦不需 profile override。**

---

## 7. 19 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/36_framework_signoff.md   ← 未讀
  features/vehicle_setting/docs/handoff/37_rd1_dispatch.md        ← 未讀
  features/vehicle_setting/docs/handoff/38_pilot_review2.md       ← 本輪依據

## 文書（36／37 之順延項）

D-5   依 36 包 §1 鎖定 framework.md（簽核區塊 ＋ 重開條件逐字；
      原草案標題與阻塞項表保留加註）
D-6   Layer 3 表增「正規化名」欄；阻塞項 8／10／底部第 5 標「已解」
D-7   PLAYBOOK.md §6 狀態板更新
D-8   DATA_REQUESTS.md 依 Pei 回報之實際送出項次標「送出／待覆」，
      **未送者維持待送，不得推定**
D-9   PLAYBOOK.md §6 之未結 DR 分「待送／待覆」兩態
D-10  於 37 包記明實際送出項次（由 Pei 回報）
D-11  ANOMALIES.md 新開 **A-VS62**（38 包 §2）；
      profile 增列 38 包 §1 之 D-3 裁定（PENDING 行不計入 §10.5）

## 作業（**兩項**）

W-56  batch01_v2 之缺陷修正 → `generated/batch01_v3.json`（v2 保留）
      (1) `-009` 依 38 包 §1 之 D-1 改為 baseline 比較（§5.6）
      (2) `-004`／`-005` 依 D-2 修末步驟，使其含 action ＋ check
      (3) `-006`／`SwitchLHD/RHD-010` **移出批次**，
          於 `split_reason` 記 `BLOCKED-BY-DR-19`／`-20`，
          另存 `generated/blocked_pending_dr.json`
      (4) 重跑 §9 自檢與 DBC 值表核對，逐項列出
      **批次規模由 10 降為 8**

W-57  第二批生成 → `generated/batch02.json`，**10 條**
      自 Common Features 之可用 leaf（42 − 本批 10）中，
      依 reqid 升冪取 10，排除 DR-19／DR-20 所涉者。
      **須注入 `## Sibling Rows`**（§4.6）—— 18 輪僅補 35 包點名之一對，
      其餘八條未經比對，本批起不得再省。
      套 profile 全部五項 ＋ canon §8.7.5 v3。

## 禁區

git 不執行。不寫回工作簿。不執行 backlog（R-VS40）。不代擬條文。
v1／v2 保留不刪。

## 升級條件

W-56 修正後出現新的 §9 不通過項；
W-57 之 sibling 比對發現 batch01 已放行者與新批重複（§10.6）；
可用 leaf 不足 10。
```

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| D-3 之裁定 | `PENDING` 行不計入 §10.5 最低步數；不足者移出批次 | 分析層（記入 profile，不另編號） |
| A-VS62 | ER 之送出型措辭未能自交付本枚舉 | 分析層登記 |

**未立新編號條文**，符合 R-VS40。
