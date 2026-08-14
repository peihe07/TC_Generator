# 下放包 16 — P7 完成、close-out 作業、Tier 3 交接

分析層 → 執行層。2026-08-13。Pei 於本日完成 Excel 實開確認（七點全過），
**P7 完成**。

---

## 1. 裁決條文

```text
[RULING] R38 — Privacy P7 完成（Pei 確認 2026-08-13）

R38-1  P7 完成
  裁：Pei 於 2026-08-13 開啟
      features/privacy/output/FM-WI-FSM-036-A01 …_Privacy_20260813_
      regen-v1.xlsx，下放包 15 §2 之七項檢查點全過：
        1. 無「檔案已損毀，Excel 已修復」提示
        2. R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
        3. D5 範圍 Scope = SWE1_CFTS_022-Privacy_Features
        4. 第 10–20 列共 11 列 TC，其餘列為空
        5. B 欄序號顯示 1…11
        6. 第 18 列 Remarks 288 字元完整顯示，無截斷無亂碼
        7. 第 18 列字型／填色／框線與第 17 列一致
      **PLAYBOOK §6 之 P7 可勾。**
      產出：11 TC / 10 葉，SHA256 ad595ed0cad24375…，
      zip 成員 48（零增零減），classic 3+1 / x14 2 前後相同，
      差異成員僅 sheet6.xml。

R38-2  R17-9 / R37-6 —— B 欄 cached value 問題於外科手術路徑上解除
  事實：檢查點 5 通過 —— B 欄 11 格皆為公式且無 cached <v>，
      Excel 開啟時正確重算並顯示 1…11。
  裁：**此為該問題之首次現場實測**（此前皆為推論）。結論：
      **zip 層外科手術寫入之顯式公式，缺 cached <v> 不影響 Excel
        之正確重算。**
      連動：AMFM v2 之同型疑慮（R17-9）於機制層面消解 ——
      同一寫回路徑、同一形態。但 **AMFM v2 本身仍未經 Excel 實開**，
      本裁決不得被讀為「AMFM v2 已驗證」；
      它證明的是機制無此缺陷，不是那份檔案已被檢查。
  §5a：**機制之驗證與實例之驗證是兩件事**；證明機制不產生某類缺陷，
      不等於證明某個實例沒有該缺陷 —— 實例可能另有他因。

R38-3  BLOCKED 列全鏈路驗證完成
  裁：NR1L-Privacy-009（第 18 列，CFTS022-4915173）之
      [BLOCKED-ECU] marker 已通過**生成 → lint → 寫回 → 顯示層**
      全鏈路驗證（R34-3 立、R37-4 寫回層驗、R38-1 檢查點 6/7 顯示層驗）。
      本 feature 第一個 marker 之機制自此為實測有效。
```

---

## 2. 執行層作業

### 2.1 補陽性對照（R37-5(a)，下放包 15 §3.1）

寫回腳本兩層自加 invariant 各補一次：
- 刻意改動輸出**副本**之表頭區某格 → 須 ABORT
- 刻意改動輸出**副本**之某非目標分頁某格 → 須 ABORT

副本產於暫存目錄，**不得觸及 `output/`**，測畢即刪。

### 2.2 `DELIVERY.sha256` 加註

ENTRY 002 追加一行（**追加不改寫**既有欄位，R27-2）：

```
Excel 開啟確認：Pei, 2026-08-13, 七點全過（R38-1 / 下放包 15 §2）
```

### 2.3 `PLAYBOOK.md` §6

- 勾 **P7**，記入 R38-1 之全部數值（SHA256 全長、zip 成員、DV 計數、
  11 TC / 10 葉、列範圍 10–20）
- 依 **R15-3** 標明量測條件：本次結構驗證以成員集合與 DV 計數為據，
  **非以位元組數**（R37-2）
- 依 **R15-4** 記載雜湊**全長**，不截斷

### 2.4 anomaly 狀態收束

- **A-PV02**（ANC 兩變體）→ **RESOLVED**：十葉皆已完成且未觸及 ANC
  配置，Not requested 未觸發
- **A-PV15**（車型欄世代）/ **A-PV16**（CAN trace 能力）/
  **A-PV17**（037 額外主張）/ **A-PV18**（-008 分配）
  → 依 **R15-2** 標 `DEFERRED — 待 RD-1 回覆（<裁決編號>）`，
  移出 Open PENDING
- **A-PV03**（ETM V3_R3）→ 維持 DEFERRED
- **A-PV13**（feature.yaml 欄位字母）→ 確認狀態；寫回腳本已改由表頭
  文字解析（R37-3(a)），該落差不再影響產出，但 `feature.yaml` 之
  記載仍為舊值 —— 若未修，狀態改為
  `DEFERRED — 記載與實作不一致，實作以表頭為準（R37-3(a)）`

### 2.5 close-out 清單（非交付阻塞）

依 **R15-2** 逐項標 DEFERRED 或辦結，移出 Open PENDING：
- profile 其餘六節之來源類別標註（R37-5(c)）
- `spec-ref-source-version` gate 之真實換版驗證（R37-5(b)）

### 2.6 為 Pei 備妥 commit message（英文，conventional commits，**不執行**）

須涵蓋：feature scaffold、framework Part VI、profile、rulings R22–R38、
11 TC 生成、lint 腳本（19 gate 全具雙對照）、寫回路徑
（`xlsx_surgical` 首次正向適用）、兩份 sha256 台帳、
`spec_ref_reviewed.json`。

### 2.7 tag 建議（**不執行**）

- 名稱建議 `fw036-privacy-v1`
- annotation 須載：產出檔名、**全長** SHA256、bytes、
  zip 成員數、classic／x14 DV 計數、11 TC / 10 葉、
  lint 結果、輸入基準之 SHA256、Excel 確認日期
- **不得截斷任何雜湊**（R15-4）

---

## 3. 停手條件

1. §2.1 之陽性對照**未觸發 ABORT** → **停止 §2.2 之 ENTRY 002 加註**，
   續行其餘各項，回報。
   理由：invariant 不會失敗時，先前之「三層全過」不具意義
2. §2.4 發現任一 anomaly 之現行狀態與本包所述不符 → 停止該條之更新，
   續行其餘，回報實際狀態
3. 台帳任一條指令 FAILED → 停止全部，回報

---

## 4. Tier 3 序列（僅 Pei，本包不執行、不催辦）

1. commit（執行層備妥 message）
2. tag（`--date` 旗標為可重現性所需）
3. 交付時點與位置 —— `10_Reviewing/00_TestCase/` 下之路徑由 Pei 決定
4. RD-1 送出 —— 現有 **#6–#13 八項**，時點由 Pei 決定

---

## 5. 上繳包要求

寫入 `features/privacy/docs/upstream/16_p7_done.md`：

1. §2.1 兩項陽性對照之輸出
2. §2.2 加註後之 `DELIVERY.sha256` 全文
3. §2.3 更新後之 PLAYBOOK §6 全文
4. §2.4／§2.5 逐項現況
5. commit message 與 tag annotation 草案全文
6. 台帳兩條指令輸出
7. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R38-1 P7 完成（七項檢查點逐項）—— §1，區塊形式
- [x] R38-2 cached value 問題於機制層解除 + 機制驗證 ≠ 實例驗證（§5a）—— §1
- [x] R38-3 BLOCKED 列全鏈路驗證完成 —— §1，區塊形式
- [x] close-out 作業七項 —— §2
- [x] Tier 3 序列四項 —— §4
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §3

<!-- HANDOFF-LINK: 16 -> upstream:16 -->
