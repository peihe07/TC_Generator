# 下放包 36 —— Vehicle Category：收線裁定（出貨版方法 ＋ 二項記明）

- 日期：2026-08-27
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/36_closeout.md`（**或併入下次開機首包**）
- 前一包：`docs/handoff/35_final_leaf.md`
- **NN 檢查**：寫入前已 `list_directory` ＋ 確認 `upstream/35` 存在（二項制首次例行適用）。
- **本包為本 session 收線包。無生成、無寫回任務。**

---

## 一、出貨版之寫回方法：**改用外科式**，工作版維持丙″ 產物

### 1.1 裁定

| 版 | 方法 | 理由 |
|---|---|---|
| **工作版**（已產出）| **維持丙″ 產物，不重產** | 六項核心保全、B 欄行為保留、其用途（Excel 驗收＋提前檢查）足堪；重產無收益 |
| **出貨版**（PENDING 結案後）| **改用外科式**（移植 `features/display/scripts/write_back_036.py` 之法：不經 openpyxl 存檔、直改目標儲存格、其餘部件逐 byte 重打包）| 零增零減、逐項相等，**且已在 display 被實作與跑過** —— 交付本會被上游檢視，52 部件／9 media／1401 共用公式展開這類結構差異，不該讓收件者產生「這檔被什麼動過」的疑問 |

丙″ 之六項驗收**量不到共用公式與部件數** —— 你們補量的三個量
（zip 部件、`t="shared"`、media 數）自本包起併入出貨版之驗收項。

### 1.2 「答案已在 repo 裡」第三次 —— 記明，不開新任務

DR-VC6 佐證欄、R-VC19 加註、display 之外科式實作 —— 三次同型。
前二次在台帳（`ledger_xref` 已管），**本次在跨 feature 之 `scripts/`** ——
已知盲區之又一段。**記明於 PLAYBOOK §7.3 之附註即可**：
「方案評估時，先掃他 feature 之 `scripts/` 有無同題之既有實作」。
不造工具、不開任務 —— 收線前不製造工作。

## 二、工作版寫回之時序 —— 記明

包 34 §四明文「寫回之授權在下一包，待收斂＋Excel 驗收」；
包 35 未含寫回授權。**工作版之寫回係先於授權執行。**

**結果追認**：母本未變、產物在 gitignore 之 `output/`、八項驗收全過，
且「驗收標的改為 126 列實檔」之論證成立（3 筆探針驗不出全列下拉）。
**時序記明**：授權邊界不因結果無害而失效 —— 記於上繳包 36 一句即可，
不立 A。`DELIVERY_CHECKLIST` 第 1／2 項標的更新採認。

## 三、其餘採認與待辦定格

- **`DELIVERY.sha256` 補建**：採認（依 display 格式，ENTRY 001）。
- **`delivered/MANIFEST.tsv` 不寫入**：正確 —— 其語意為已交付，這是工作版。
  **⚠ 其出現疑為併行 session** —— Pei 收線前請確認無第二條線開著
  （display 事件之教訓：一 feature 一線）。
- **git**：屬 Pei。執行層建議之 commit 指令與 pathspec 無誤。
- **Excel 驗收**：對 `output/…_working.xlsx`（126 列）跑
  `DELIVERY_CHECKLIST` 第 1／2 項 —— **Pei 隨時可做，不需任何 session 開著**。

## 四、下次開機（DR 回覆後）

讀序：`docs/RESUME_PLAN.md` → 本包（§一之出貨版方法）→ `RULINGS.md` 尾段。
出貨序第 3 項（丙″ 產出交付本）**依 §一改為外科式**；
RESUME_PLAN 之該行由下次開機首包更新（本包不遙改）。

---

**本 session 終。117/117 leaf、TC 126 筆、工作版已落地。
剩三件全在 Pei：Excel 驗收、git commit、DR 之回覆。**
