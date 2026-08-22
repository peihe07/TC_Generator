# 47 下放包 — A-VS90 裁定（`ENS_DSBL` 成立）、R-VS43(1) 之實作缺陷、28 輪

分析層寫入，2026-08-22。**產能為 0，本包目標是把它變回非 0。**

---

## 1. A-VS90 裁定：**`ENS_DSBL → 7 (ENS disabled)` 成立**

分析層自 `inputs/` 原始 docx 實測 `$ESS_ENG_ST$` 之全部值形態：

| 值 | 次數 |
|---|---:|
| `[SNA]` | 13 |
| `[1h or 2h or 3h or 4h or 5h or 6h or 8h or 9h]` | 10 |
| **`[ENS_DSBL]`** | **9** |
| `[Fh: SNA]` | 6 |
| **`[7h: ENS disabled]`** | **5** |
| **`[ENS Disabled]`** | **4** |

| 形態 | 全文命中 |
|---|---:|
| `ENS_DSBL` | 11 |
| `ENS disabled` | 4 |
| **`ENS_ENBL`** | **0** |
| **`ENS enabled`** | **0** |

**R-VS43 三條件逐項成立**：

| 條件 | 判定 |
|---|---|
| **(1)** 二值域 **或目標在值域內唯一可判** | **後半成立** —— 11 值中僅 `ENS disabled` 之縮寫為 `DSBL`；其餘（`ENS Stopped`／`Running`／`Stop Pending`／`Start protection`／`Start inhibit`／`Starting`／`SNA`）皆不可能縮為 `DSBL`。**目標唯一** |
| **(2)** 值域已由來源自載之 `Nh:` 錨點定位 | **成立** —— `[7h: ENS disabled]` 全文 5 處 |
| **(3)** 無平行對偶 | **成立** —— `ENS_ENBL`／`ENS enabled` 全文各 **0** |

**且來源自身以三種措辭書寫同一值**：`ENS_DSBL` 9／`ENS Disabled` 4／
`7h: ENS disabled` 5 —— **三者並存於同一文件，即其為同一值之三種寫法。**

```
分析層裁定 2026-08-22（A-VS90 結案）
`$ESS_ENG_ST$` 之 `[ENS_DSBL]` → `7 (ENS disabled)` **成立**，依 R-VS43 三條件。

推論：
(a) `batch01_v3` 之 `Stop-StartSystem-005` 之寫法**獲追認**，不改
(b) **25 輪移出之 `StopStartSystemBehavior-054`／`-055` 過嚴，應入批**
(c) `ENS_DSBL` 加入 R-VS43 之已裁演繹對表（與 `DriverSide/right drive` 並列）
```

---

## 2. R-VS43(1) 之實作只做了前半 —— **這是產能為 0 的主因之一**

W-77 之 `resolved()` 四路中，R-VS43 之演繹對表**僅含 `DriverSide/right drive` 一項**，
且 §1.2 記其判 W2 之理由為「**`R-VS43(1)` 之『二值域』不成立**」。

**R-VS43(1) 之原文為「二值域，**或目標在值域內唯一可判**」——
實作只實現了前半，後半從未被實現。**

**該缺陷屬分析層**：R-VS43 立條時未給「唯一可判」之操作型定義，
致實作者只能實現可測的那一半。

```
R-VS48（R-VS43(1) 後半之操作型定義，分析層裁定 2026-08-22；本輪唯一新條文）
R-VS43(1) 之「目標在值域內唯一可判」，其操作型定義為：

  待對映之措辭 v 與值域 D 之成員逐一比對，
  若**恰有一個** d ∈ D 滿足下列任一，則目標唯一：

  (a) **縮寫關係** —— v 去除分隔符（`_`／空白／`-`）後之字元序列，
      為 d 去除分隔符後之**子序列**，且 v 之每個字元段皆為 d 對應詞之前綴
      例：`ENS_DSBL` → `ENSDSBL`；`ENS disabled` → `ENSDISABLED`；
          `DSBL` 為 `DISABLED` 之子序列且各段為前綴 → 成立
  (b) **共享實詞** —— v 與 d 共享至少一個實詞（去停用詞後），
      且與 D 之其他成員皆不共享
      例：`Right Drive` 與 `Right Side` 共享 `right`，與 `Left Side` 不共享
  (c) **來源自載之別名對** —— v 與 d 於來源中曾同格並列（`d / v` 形態）

滿足者仍須通過 R-VS43(2)(3) 方得對映。

**實作要求**：`resolved()` 之 R-VS43 路須實現 (a)(b)(c) 三者，
**不得只實現值域大小為 2 之情形**。
**驗收錨點（須可失敗）**：
  `ENS_DSBL` × `$ESS_ENG_ST$`（11 值）→ 須判**可對映**
  `IGN_START` × `$PowerMode$`（6 值）→ 須判**不可對映**
    （`IGN_START` 之 `START` 亦為 `START` 之子序列，
      **但 `Initialization` 之 `INIT`… 不衝突；其不可對映之理由為
      R-VS43(3)：`IGN_STOP`／`IGN_END` 之對偶未測 —— 見下）
```

**`IGN_START` 之重測**：依 (a)，`IGN_START` → `IGNSTART`，
`START` 為 `START` 之子序列 → **目標唯一（`START`）**。
(2) 錨點：`$PowerMode$` 有 `4h: ignition run` 之錨點，
**但 `START` 是否有 `Nh:` 錨點未測**。
(3) 對偶：`IGN_STOP` 是否存在未測。

→ **W-80 須重測 `IGN_START`／`IGN_OFF_ACC`，其結果可能改變 DR-21 之範圍。**

---

## 3. 產能為 0 之三個成因，逐一有解

| 成因 | 規模 | 解 |
|---|---:|---|
| R-VS43(1) 只實現一半 | 未知，**至少 2 條**（`-054`／`-055`） | **W-80**（R-VS48） |
| `OneStageHeatedSeat-047`~`-050` 卡 `delegate = pending` | 4 | **DR-17 送出**（待 Pei） |
| 79 leaf 卡 PROXI 值域 | 79 | **DR-22′ 送出**（待 Pei） |

**W-80 是唯一不需外部動作者。**

---

## 4. 28 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/47_review_round27.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/26_uniqueness.md，六節先留空。
D-2  逐字轉錄 47 包 §2 之 **R-VS48** 入 RULINGS.md。
D-3  A-VS90 依 47 包 §1 **關閉**；`ENS_DSBL → 7 (ENS disabled)` 加入
     R-VS43 之已裁演繹對表。
D-4  `blocked_pending_dr.json` 之 `StopStartSystemBehavior-054`／`-055`
     **移回可生成池**（25 輪之移出過嚴）。
D-5  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-80  **R-VS48 之實作與全量重跑**（最高優先）
      (1) `resolved()` 之 R-VS43 路實現 (a) 縮寫／(b) 共享實詞／
          (c) 來源自載別名對 三者
      (2) **驗收錨點（須可失敗）**：
            `ENS_DSBL` × `$ESS_ENG_ST$` → 可對映
            移除 (a) 後 → 不可對映
      (3) **重測 `IGN_START`／`IGN_OFF_ACC`**：逐項列 R-VS43 三條件之成立與否，
          **特別是 (2) 之 `Nh:` 錨點與 (3) 之對偶**
          （`IGN_STOP`／`IGN_END`／`IGN_ON_ACC` 等全文命中數）
      (4) 全量重跑 W-77 之分級，列 W0／W1／W2 三數與 27 輪之
          91／3／143 對照；**新增可對映之 (token, 值) 對逐筆列出**
      (5) 新對逐筆過 `guard()`（R-VS44′）—— 落在未結 DR 範圍者不採用

W-81  **`<w:drawing>` 內嵌圖片之清點**（27 輪 §6-1）
      (1) 列 `word/media/` 之圖檔數、格式、尺寸
      (2) 以文件順序定位各圖所屬之條文 id
      (3) **`4859495` 所屬之圖**若存在，以 00D 之法 OCR（含旋轉），
          抽出其內容並判其是否即 `described below` 之序列
      (4) **不逐張 OCR全部** —— 僅 OCR 落在 237 leaf 所引條文內者，
          並列其張數

W-82  batch10 —— **10 條**（W-80 之後）
      自重跑後之池選 leaf，依逐 Layer 2 輪流。
      **池不足 10 時取全部並回報其數。**
      套 profile ＋ canon §8.7.5 v3 ＋ R-VS43／R-VS48 ＋ Sibling Rows ＋
      無效值優先序；逐條過 `guard()`；§9 十七項自檢 ＋ DBC 值表核對。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
不得再執行型 B 之唯讀搜尋。不得採用他車型 PROXI 表之值。
**R-VS48 之 (a)(b)(c) 皆須通過 R-VS43(2)(3) 方得對映** ——
不得僅以唯一性成立即對映。

## 升級條件

W-80(2) 之錨點不可失敗；
W-80(4) 之池仍為 0；
W-80(3) 判 `IGN_START` 可對映（則 DR-21 之範圍須縮，且已生成之
  `PENDING: DR-19` 三條須複檢）；
W-81(3) 抽出之圖內容與 `described below` 無關。
```

---

## 5. pilot #2 —— 分析層本輪未出清單，理由具名

46 包 §2 承諾於 27 輪產物到齊後出 15 條清單。
**27 輪產出 0 條 TC**，母體仍為 65 條（8 已 PASS ＋ 57 未 review）。

**分析層之處置**：pilot #2 之抽樣**不等 batch10** —— 母體 57 條已足夠分層。
**下一包（48）出清單與建議分類**，與 28 輪之產出並行，不互相等待。

---

## 6. 待 Pei

| 項 | 解鎖 | 狀態 |
|---|---:|---|
| **DR-22′** | **79 leaf** | 待送 —— 單一最大 |
| **DR-17** | **4 leaf**（`OneStageHeatedSeat-047`~`-050`，已可寫） | 待送 |
| DR-21／DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11 | — | 待送 |

**W-80 是唯一不需外部動作即可恢復產能者，故排本輪首位。**

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS48 | R-VS43(1) 「目標唯一」之操作型定義：縮寫／共享實詞／來源別名對 | 分析層（本輪額度用畢） |
| A-VS90 之裁定 | `ENS_DSBL → 7` 成立；`-005` 追認；`-054`／`-055` 移回池 | 分析層 |
