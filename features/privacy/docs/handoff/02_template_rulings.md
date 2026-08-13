# 下放包 02 — 範本相關八條裁決（R23）

分析層 → 執行層。2026-08-13。Pei 於本日回覆「照建議」，A-PV01 / 04 / 05 /
07 / 08 / 10 / 11 / 12 全數簽署。

**注意**：`features/privacy/RULINGS.md` **尚不存在**，本包為該檔之首次建立。

---

## 1. 裁決條文（可直接貼入新建之 `RULINGS.md`）

```text
[RULING] R23 — Privacy 範本相關八條（Pei 簽署 2026-08-13，回覆「照建議」）

R23-1  A-PV01 交付形態 —— 以通用範本產生 Privacy 交付件即為最終形態
  裁：不另索 Privacy 專屬 workbook。
  依據：範本第 10 列原廠樣本為 NR1L-AntiTheft-001，該範本本即供各
        feature 各自開工之用。
  A-PV01 由 PENDING 轉 RESOLVED。

R23-2  A-PV04 VF651_V2_R2 基線追認
  裁：`inputs/` 現有之 SHA256 `d5813bb7…`（146,929 bytes）為
        **HDCC28 平台基線**，與 `VF/VF_Split document/HDCC28_Split/`
        同源（hash 相同，非僅 size 相同）。
        `28HDCC_2A_LTM/…` 之 `7b5fc875…` 確為不同內容，不得假設為重存。
        DT 系列（DT27 / DT28）另三種內容不列入本專案。
  A-PV04 由 PENDING 轉 RESOLVED。

R23-3  A-PV05 SYSAD 分類
  裁：`SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx`
        於 `feature.yaml` 標為 **context-only**。
        **不得**作為 `specification_reference`（§10.7 禁引分析類文件；
        SYSAD 屬設計非規格）。其角色限於背景理解。
  A-PV05 由 PENDING 轉 RESOLVED。

R23-4  A-PV07 殘留樣本列清除計畫 —— 核可修訂版
  裁：核可 2026-08-13 修訂版計畫，即：
        (1) 僅清 **D10 / F10 / G10 / S10 / D11** 五格之值
        (2) 方式為 zip 層就地改寫：
            `<c r="D10" s="81" t="s"><v>44</v></c>` → `<c r="D10" s="81"/>`
            —— 值清除、`s=` 樣式屬性原地保留
        (3) **B 欄不清** —— B10 為公式 `=IF(ISBLANK($D10),"",ROW()-9)`，
            序號自 D 欄推算，清 D10 後自動空白；手動清 B 欄會刪掉
            範本之序號機制
        (4) **不採整列刪除** —— 會使 DV sqref 與 R10 之 x14 DV 移位
        清除後首筆 TC 落第 10 列，`NR1L-Privacy-001` 起算（R-PV02）。
        探針已實測通過（五格讀回全 None、B10 公式完好）。
  A-PV07 由 PENDING 轉 RESOLVED。

R23-5  A-PV08 表頭六格 —— **依 AMFM 已交付件實測修正建議**
  分析層更正：原建議「D3 Reviewer 與 Cover 封面 Reviewer 由 Pei 給值、
        交付件不該帶範本預設人名」**有誤**。實測 AMFM 之客戶端已交付件
        （`10_Reviewing/00_TestCase/Radio/…CFTS024_Radio_20260129.xlsx`）
        後修正如下：

  | cell | 欄位 | AMFM 已交付件實測 | Privacy 裁定 |
  |---|---|---|---|
  | D2 | 專案名稱 | `newR1L` | 維持 `newR1L` |
  | D3 | 審查者 Reviewer | **空** | **留空** |
  | D4 | 目的 Purpose | **空** | **留空** |
  | D5 | 範圍 Scope | `FM-WI-SW-RAD-SWRA-A02` | `SWE1_CFTS_022-Privacy_Features` |
  | J5 | 日期 Date | `2026/1/29`（交付日）| 交付日填，現在不預填 |

  Cover 封面之三格（核准者 / 審查者 / 作者）**一律不動**：
        實測 AMFM 交付件之 Cover 為版本 A、核准者 劉安哲 AllenACLiu、
        審查者 陳禹伸 YuShenChen、作者 張愷霏 ErinKFChang ——
        此為 **FM-WI-FSM-036-A01 表單本身之文件管制區**，記錄的是
        「誰核准了這份表單」，非「誰審查了本次交付內容」。
        Privacy 範本為版本 C，其對應人員即為該版之管制紀錄，
        不得更動。
  §5a：**表單自身之文件管制欄位與交付內容之責任欄位是兩件事**；
        判定某欄屬何者，須以同表單之已交付實例為據，不得由欄位
        名稱推斷。
  D5 Scope 之特別要求：依 PLAYBOOK §4，Scope 欄是 workbook 之身分
        宣告，**intake 與送件前各驗一次**（一週內兩個 feature 在此格
        出錯）。Privacy 之 037 檔內未給文件編號（cell AI2 僅標
        `FM-WI-FSM-037-A03`），故無法比照 AMFM 填
        `FM-WI-SW-xxx-SWRA-Axx` 形式，改填檔案識別碼。
  A-PV08 由 PENDING 轉 RESOLVED（intake 誤讀 Scope 之 bug 另計，
        見 §2.5）。

R23-6  A-PV10 下拉選單範圍不一致
  裁：範本瑕疵屬上游，**登記即可，不修**。
        lint 以 `下拉選單!A1:A9` 之 9 詞條為準
        （`feature.yaml` 之 `lint.design_method_source: dropdown_sheet`）。
        R10 指向 `$A$1:$A$9`、R11:R59 指向 `$A$1:$A$11`（含 2 空項）
        之落差不修，隨 RD-1 回報上游。
  A-PV10 由 PENDING 轉 RESOLVED（處置已定，缺陷續存於上游）。

R23-7  A-PV11 Reference 與 下拉選單 字串不符
  裁：以 **`下拉選單` 為 lint 權威**（DV 實際引用者）；
        `Reference` 分頁視為說明性附表，**不入 lint**。
        第 6 條之落差（`Pair-wise / N-wise` 對 `Pairwise / t-wise`）
        隨 RD-1 回報上游。
  A-PV11 由 PENDING 轉 RESOLVED。

R23-8  A-PV12 Cover_old / ChangeHistory_old
  裁：採**案 1 原樣保留**。兩頁不進 lint、不進 trace、不寫回。
        理由：刪除屬對公司管制表單之結構性修改，且交付件分頁數與
        原範本不符時，稽核反而須解釋「為何少兩頁」。
        佐證：AMFM 之已交付件同樣保留 `Cover_old` /
        `ChangeHistory_old` 兩頁（實測 10 分頁清單）。
  A-PV12 由 PENDING 轉 RESOLVED。
```

---

## 2. 執行層作業

1. **新建** `features/privacy/RULINGS.md`，體例比照既有 feature，
   貼入 §1 全文
2. `ANOMALIES.md`：A-PV01 / 04 / 05 / 07 / 08 / 10 / 11 / 12 八條之狀態
   依 §1 各條末行更新，裁決逐字記入（依 R19-1：更新既有條目，不另開新條）
3. `feature.yaml`：SYSAD 標 context-only（R23-3）
4. **執行 R23-4 之清除**：五格就地改寫，走 `backend/xlsx_surgical.py`
   （R18-3 規則 1 之首次正向適用）。清除後回報：
   - 五格讀回值（應全為 `None`）
   - B10 公式原文（應為 `=IF(ISBLANK($D10),"",ROW()-9)`）
   - zip 成員集合與清除前比對（應零增零減）
   - classic / x14 DV 計數與清除前比對（應完全相同）
5. **D5 Scope 填入** `SWE1_CFTS_022-Privacy_Features`（R23-5）；
   D2 / D3 / D4 / J5 與 Cover 封面**一律不動**
6. `PLAYBOOK.md` §6 狀態板之 `Open PENDING` 欄更新為剩餘項

**不做**：不動 Cover 封面任一格、不動 D2 / D3 / D4 / J5、
不刪 `Cover_old` / `ChangeHistory_old`、不修下拉選單範圍、
不改 `Reference` 分頁、不執行任何 git 操作。

---

## 3. 停手條件

1. `RULINGS.md` 已存在（與本包前提不符）→ **停止新建**，改為附加 R23，
   續行第 2–6 項，回報既有內容
2. 第 4 項之清除後比對出現任一不符（zip 成員增減、DV 計數變動、
   B10 公式改變）→ **停止第 5 項 Scope 填入**，續行回報。
   理由：寫入路徑未證實無損時，不得再寫第二次
3. 第 5 項填入後 D5 之讀回值與指定字串不符 → 停止該項並回報，
   不得重試覆寫

---

## 4. 尚未處置之 Privacy 項目（本包不動，供狀態板用）

- `A-PV02` ANC 部分：V9_R3 / V11_R3 維持不索取。若 P2 解析發現任一
  leaf 觸及 ANC 配置，停手回報，不自行擴充
- `A-PV03` ETM V3_R3：`DEFERRED — 待 P2 證據重驗（R-PV01(a)）`
- `A-PV13` `feature.yaml` 欄位字母：RESOLVED（執行層已處置）
- `R22-6` `backend/api_server.py:2410`：**未簽署**，不得修改該檔

---

## 5. 上繳包要求

寫入 `features/privacy/docs/upstream/02_template_rulings.md`，須含：

1. §2 六項完成狀態
2. 第 4 項之四組比對數據（清除前後）
3. 第 5 項 D5 之讀回值
4. `RULINGS.md` 建立結果
5. `intake.py` 之 `_workbook_profile` Scope 誤讀 bug（A-PV08 所載）
   於 D5 填入後是否自然消失 —— 實測回報，不修程式碼
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R23-1 交付形態 —— §1，區塊形式
- [x] R23-2 V2_R2 基線追認 —— §1，區塊形式
- [x] R23-3 SYSAD context-only —— §1，區塊形式
- [x] R23-4 殘留樣本列清除計畫核可 —— §1，區塊形式
- [x] R23-5 表頭六格 + 表單管制欄位 vs 交付責任欄位之區分（§5a）—— §1
- [x] R23-6 下拉選單範圍不修，lint 取 A1:A9 —— §1，區塊形式
- [x] R23-7 下拉選單為 lint 權威 —— §1，區塊形式
- [x] R23-8 舊分頁原樣保留 —— §1，區塊形式
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §3
