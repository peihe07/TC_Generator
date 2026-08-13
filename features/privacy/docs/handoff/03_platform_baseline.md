# 下放包 03 — 前提更正、A-PV14 平台一致性、Privacy 專注範圍

分析層 → 執行層。2026-08-13。承接上繳包 `docs/upstream/01_carryover.md`。

**Pei 裁示（2026-08-13）**：「現在只專心做 Privacy mode，請不要管其他的。」
本包據此設定範圍：**除 Privacy 外，一切不追、不查、不動**。
下放包 01 §4 之「不追查已消失之 feature 目錄」續行有效，但其理由由
「目錄不存在」改為「Pei 裁示專注 Privacy」。

---

## 1. 裁決條文

```text
[RULING] R24 — 前提更正與 Privacy 專注範圍（2026-08-13）

R24-1  下放包 01 之背景前提錯誤 —— 分析層過失
  事實：01 包寫「features/ 下現僅存 privacy/，其餘五個 feature 目錄
        已不在」。執行層實測六個 feature 目錄全部存在，追蹤檔數
        amfm 135 / home 68 / media 170 / projection 77 / sxm 230，
        ANOMALIES、RULINGS、PLAYBOOK、scripts 皆在。
        消失者為目錄內**未被 git 追蹤之素材**（各 inputs/ 內容），
        以及 repo 根 output/（此項 01 包所述正確）。
  分析層複核：本日再次以 list_directory 實測，六目錄確實全部存在。
        先前之單次列目錄結果只回傳 privacy，成因未判定（不追）。
  歸因：**錯不在量測失準，錯在以單次量測支撐一項範圍決定**。
        01 包據該次列目錄結果宣告「下放包 08 內容全部作廢」——
        作廢是不可逆之範圍決定，而依據只有一次未複驗的觀察。
  裁：01 包之「其餘一律不追」續行有效（依 Pei 本日裁示），
        但「08 包作廢」之**理由撤回**，改記為「因專注 Privacy 而
        不處理」。兩者結果相同、依據不同，須分辨。
  §5a 新增：**不可逆之範圍決定，其依據不得為單次量測。**
        欲據觀察結果縮減範圍者，須先複驗；複驗成本高於保留範圍時，
        保留範圍。（與既有「擴範圍證據自足即可、縮範圍須重驗」之
        不對稱原則同源，本條將其自 spec 範圍擴及 repo 狀態。）
  執行層之處置正確：依 §4 未做追查，但回報前提不成立 —— 此即
        R17-3 之正確適用。

R24-2  A-PV14 平台一致性 —— specification_reference 來源檔一律取 HDCC28
  事實（執行層稽核副產物）：`inputs/` 之兩份 VF651 分屬不同平台樹 ——
        `…VF651_V2_R2.docx` 命中 `HDCC28_Split`
        `…VF651_V6_R2.docx` 命中 `28DT_2A_LTM / DT28_split`
        V6_R2 之 HDCC28 副本（`e20ba7a4…`）與 `inputs/` 這份
        （`49dd3c31…`）不同內容。
  裁（**由 R23-2 直接導出，非新政策**）：R23-2 已裁定本專案為
        **HDCC28 平台**、`inputs/` 之 V2_R2（`d5813bb7…`）為 HDCC28
        基線。同一原則適用於全部 VF651 引用：
        **`specification_reference` 之來源檔一律取 HDCC28 平台版本。**
        若不如此，-007 / -008 / -010 三筆 AMP-present 之
        `specification_reference` 將指向 DT 平台文件。
  執行順序（先量後換，不得逕行換檔）：
    (1) 對 `e20ba7a4…`（HDCC28 版）與 `49dd3c31…`（inputs/ 現存）
        做全文 diff，範圍限 SCV / AMP 相關條款
        （`CTRL_AMP.*`、`$VolumeSCV$`、`Acustic_Configuration`、
        `Audio_System_Type`、AMP present/not present 敘述）
    (2) **兩版於上述條款零差異** → 換入 HDCC28 版，記為
        「平台標籤更正，實質內容無影響」，不回溯任何已簽裁決
    (3) **任一條款有差異** → **停手回報**，不得自行判定何者為正
        （R-PV01(c) 之簽署依據為「需求本身要求 AMP-present」，
        不涉平台版本，故該裁決不因本項而動搖；但引用來源須另裁）
  A-PV14 狀態：PENDING → 依上述執行結果更新。
  §5a：**「檔案在正確的交付夾裡」不蘊含「檔案來自正確的平台樹」**；
        交付夾可混入他平台副本，須逐檔以 hash 回溯來源樹。

R24-3  Privacy inputs/ 基準之版控保護
  事實：`features/privacy/inputs/` 8 檔本日全數 MATCH，但 `inputs/`
        本身為 gitignored，其完整性目前無任何機制保障。
        8 檔中 7 檔之同名候選不只一種內容（V6_R2 為 7 候選 / 6 內容）。
  裁：建立 `features/privacy/inputs/BASELINE.sha256`（**進版控**），
        逐檔記錄檔名 + SHA256 + 命中之客戶樹路徑 + 稽核日期。
        此後任何素材增刪改皆會在 `git diff` 現形。
        本項為 Privacy 專屬，不推及其他 feature（依 Pei 裁示）。
  註：R15-5 在本 feature 不是保守規定而是必要條件 —— 執行層此判斷
        成立，本裁決即其機制化。
```

---

## 2. 執行層作業（依序）

1. 貼入 §1 全文至 `features/privacy/RULINGS.md`（R24）
2. **先執行既有之下放包 `02_template_rulings.md`**（R23 八條，含五格清除
   與 D5 Scope 填入）—— 該包已在目錄內未執行，優先度高於本包第 3 項
3. 執行 R24-2 之 diff 與（條件性）換檔
4. 建立 `features/privacy/inputs/BASELINE.sha256` 並確認其未被
   `.gitignore` 排除（若被排除，**停手回報**，不自行修改 `.gitignore`）
5. `ANOMALIES.md`：A-PV14 依 R24-2 執行結果更新狀態
6. `PLAYBOOK.md` §6 之 `Open PENDING` 欄同步

**不做**：不追查素材消失機制、不處理其他 feature 之任何事、
不動 `backend/api_server.py`（R22-6 未簽）、不動
`03_Tools/037import036/template/` 之同名範本、不執行任何 git 操作。

---

## 3. 停手條件

1. 第 2 項（R23 執行）之任一停手條件觸發 → 依該包 §3 處置，
   **停止本包第 3–6 項**，續行回報
2. R24-2 之 diff 顯示 SCV / AMP 條款有差異 → 停止換檔，
   續行第 4–6 項，回報差異逐條
3. `BASELINE.sha256` 之路徑被 `.gitignore` 排除 → 停止該項，
   續行第 5–6 項，回報 `.gitignore` 之相關行號與樣式

---

## 4. 待 Pei（三項，皆為 Privacy 內部）

```text
[PENDING] P-1  framework 三層草案
  Layer 1  Test Group = Privacy
  Layer 2  Input Monitoring (1 leaf) / Personalization Display (1 leaf)
           / Speed-Controlled Volume (8 leaves)
  Layer 3  4915022 / 4915159 / 4915168–4915175
  待 Pei 核可後方可寫 framework.md Part N 與 profile 草案。

[PENDING] P-2  DECISIONS.md §8 Sign-off 區塊
  三條個別裁決已簽，但整份 Sign-off 區塊仍空白。
  「個別裁決已簽」與「整份已簽核」是兩件事（執行層判斷正確，
  故 P2 未勾）。需 Pei 簽署整份方可勾 P2。

[PENDING] P-3  R24-3 之 BASELINE.sha256 入版控
  屬版控政策（入庫範圍），依 charter 為 Pei 之裁定事項。
  本包已將作業寫入 §2.4，但**未經 Pei 明示前不得建立**。
```

---

## 5. 上繳包要求

寫入 `features/privacy/docs/upstream/03_platform_baseline.md`，須含：

1. 第 2 項（R23 八條）之完整執行結果，含四組清除前後比對與 D5 讀回值
2. R24-2 之 diff 輸出（條款層，逐條）與換檔與否之結論
3. `BASELINE.sha256` 建立結果（若 P-3 已簽）或未建立之說明
4. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R24-1 前提更正 + 不可逆範圍決定不得依單次量測（§5a）—— §1
- [x] R24-2 平台一致性 + 「正確交付夾」不蘊含「正確平台樹」（§5a）—— §1
- [x] R24-3 Privacy inputs BASELINE.sha256 —— §1（執行待 P-3 簽署）
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §3
- [ ] P-1 framework 三層 —— §4，**未核可**
- [ ] P-2 DECISIONS 整份簽核 —— §4，**未簽**
- [ ] P-3 BASELINE 入版控 —— §4，**未簽**
