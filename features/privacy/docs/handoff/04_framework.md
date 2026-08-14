# 下放包 04 — framework Part VI 草案、DECISIONS 簽核、BASELINE 入版控

分析層 → 執行層。2026-08-13。Pei 本日裁示：
**「1. 可以（framework 三層）  2. 簽（DECISIONS §8）  3. 要（BASELINE 入版控）」**

三項全數簽署。P-1 / P-2 / P-3 由 PENDING 轉 RESOLVED。

---

## 1. 裁決條文

```text
[RULING] R25 — Phase 3 三項簽署（Pei 簽署 2026-08-13）

R25-1  framework 三層核可
  裁：Layer 1 Test Group = `Privacy`
      Layer 2 三個 Test Set：Input Monitoring / Personalization Display
              / Speed-Controlled Volume
      Layer 3 CFTS022 artifact id 區塊
      全文寫入 docs/fw036/framework.md 之 **Part VI**（草案見 §2）。
      P3 之 framework 部分據此可勾。

R25-2  DECISIONS.md §8 整份簽核
  裁：Pei 簽核整份 DECISIONS.md（2026-08-13）。
      Sign-off 區塊填入簽核人與日期後，PLAYBOOK §6 之 **P2 可勾**。
      「個別裁決已簽」與「整份已簽核」之區分（執行層 01 包判斷）
      正確且已被採納，記為體例：**Sign-off 區塊為獨立動作，
      不因個別裁決簽署而自動成立。**

R25-3  BASELINE.sha256 入版控
  裁：建立 `features/privacy/inputs/BASELINE.sha256` 並納入版控
      （屬版控政策，Pei 裁定事項，已簽）。
      內容逐檔記錄：檔名 + SHA256 + 命中之客戶樹路徑 + 稽核日期。
      **本項為 Privacy 專屬，不推及其他 feature。**
  用途已由「防護」升為「復原能力」：8 檔中 7 檔之同名候選不只一種
      內容（V6_R2 為 7 候選 / 6 內容，且其中混有 DT 平台版）。
      無此清單時，重新取用素材有極高機率取錯且無任何機制告知。
```

---

## 2. framework.md **Part VI** 草案（逐字，供 append）

> 落點：`docs/fw036/framework.md` 檔末，Part V 之後。
> 檔首「Covers Test Groups …」一句須同步加列 **Privacy（Part VI）**。

```markdown
---

## Part VI — Privacy (CFTS022)

Ruled by Pei 2026-08-13（「可以」）：Test Group `Privacy`；下列三 Set 表；
批次計畫 B1（pilot）/ B2。

Deliverable workbook: FM-WI-FSM-036-A01 空白範本 rev C
`SWQT_20260121`（SHA256 `cd876c202c71e74b…`，A-PV01 / R23-1 裁定以通用
範本產生 Privacy 交付件即為最終形態）; RD source 037-A03
`SWE1_CFTS_022-Privacy_Features.xlsx`（**10 leaf FRs**,
`SWE1-HMI-PRIVACY_FEATURES-001…010`, 版本 C 核准 2026-02-09）;
spec_mode **D** —— clause 權威為 CFTS022 docx
（R1LR Atl-H 25PI3.5, 20250910_1708）。
SYS3 SYSAD 為 **context-only**，不得列入 `specification_reference`
（R23-3，§10.7）。外部參照 VF651（見 Part VI 注 3）。
執行計畫 `features/privacy/RUNBOOK.md`；profile
`docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`（待建）；
rulings `features/privacy/RULINGS.md`（R22–R25）。

**Workbook state**: BLANK —— 無 legacy region。範本殘留樣本列（第 10–11 列）
依 R23-4 以 zip 層外科手術清除五格（D10/F10/G10/S10/D11），B 欄序號公式
`=IF(ISBLANK($D10),"",ROW()-9)` 保留。首筆 TC 落第 10 列，
tc_id `NR1L-Privacy-001` 起算（R-PV02）。
Style authority = fallback chain；跨 feature 樣本僅供形式，
每一 literal 回溯本 feature 之 spec 行。

### Layer 2 derivation note — §4.1.2 的第三種退化

AMFM 與 SXM 的退化是「RD 側分群無資訊」（Categorization 全同值），
Privacy 的退化在另一側：**spec 側沒有章節結構**。

CFTS022 匯出實測 336 個 artifact，型別僅 `Description` 83 +
`Subsystem Functional Requirement` 253，**Heading 型 0 個** —— 這是平鋪
匯出，沒有 TOC 可與 037 分群取交集。故 Layer 3 改用 spec 自身之
**artifact id 區塊**（canon §4.1.1 要求用 spec 自己的 id，非自創標籤）。

RD 側之 Sub Categorization **有兩值**（`Service` 4 筆：001/004/005/010；
`HMI` 6 筆），但它切的是「訊號側 vs 顯示側」，橫跨 Speed-Controlled
Volume，且 `Service` / `HMI` 本身是分類標籤而非能力名稱（§4.2 禁）。
故不作為 Layer 2，改記為軸（見注 2）。

### PROF → CFTS022 artifact 對映（實測，offset = −1）

037 之 Source Requirement ID 為 `SYS-RA-PROF-nnn`，CFTS022 之 artifact
為 `4915xxx`。實測連續 8 筆全中，**offset 恆為 −1**：

| leaf | SYS-RA-PROF | CFTS022 artifact | 條文要旨 |
|---|---|---|---|
| -003 | PROF-169 | 4915168 | HU wakes up on Interior CAN → recall SCV state |
| -004 | PROF-170 | 4915169 | HU wakes up → send `$VolumeSCV$` within `<Tsend>` |
| -005 | PROF-171 | 4915170 | valid signals for `$VolumeSCV$`；其餘視為 invalid |
| -006 | PROF-172 | 4915171 | amp **not** present → HU adjusts output volume |
| -007 | PROF-173 | 4915172 | AMP present → HU shall **not** change level |
| -008 | PROF-174 | 4915173 | AMP wakes up on Interior CAN → AMP recalls SCV state |
| -009 | PROF-175 | 4915174 | no amp + user changes level → HU … |
| -010 | PROF-176 | 4915175 | amp present + user changes level → HU … |

`specification_reference` 據此構成。**-001（PROF-023 → 4915022）與
-002（PROF-160 → 4915159）之對映未逐條驗證**，P2 進場時比照補驗。

### 未分配 clause —— 觀察，非覆蓋缺口

三條 HU/AMP 側 clause 在本 037 內無對應 leaf：

- `4915167`（PROF-168）—— HU 顯示 personalization entry 供使用者調整 SCV 音量
- `4915176` / `4915177` —— AMP 接收 `$VolumeSCV$` 後之比對與儲存

CFTS022 共 253 條功能需求而本 037 僅分得 10 片葉子，**「無 leaf」極可能
只代表分配給了其他 feature 之 037**。P2 須查證後方可判定，
**現階段不得記為覆蓋缺口**（canon §8.4.2 / 不對稱錯誤代價）。

### Layer 1 — Test Group

- `Privacy`（workbook Test Group 欄值：`Privacy` —— BLANK workbook，
  FILL 適用；= spec 文件標題、= 037 之 `PRIVACY_FEATURES`）

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS022 artifact id；framework-internal only —— NEVER 寫入 workbook。

| Test Set | Layer 3（CFTS022 artifact） | Leaves | n | Status |
|---|---|---|---|---|
| Input Monitoring | 4915022（PROF-023） | -001 | 1 | remaining |
| Personalization Display | 4915159（PROF-160） | -002 | 1 | remaining |
| Speed-Controlled Volume | 4915168–4915175（PROF-169–176，連續） | -003…-010 | 8 | remaining |

合計 10 = 全 leaf set。

### Granularity check（§4.1.3）

- 三個 Set 皆通過 filter test。
- **兩個單葉 Set 為 §4.2 之 genuine outlier**：-001（睡眠退出後恢復輸入
  監測）與 -002（Interior CAN 喚醒後恢復個人化顯示）是整個 feature 中
  僅有的兩條非 SCV 需求，與 SCV 不共享 setup 或 UI 入口。
  先例：AMFM `Tuner Availability`(2)、SXM `Source Availability`(1)。
- **Speed-Controlled Volume (8) 刻意不再細分**。若依 restore / signal /
  adjustment 拆為三組，全 feature 將成 5 Set 配 10 leaf、平均 2 片 ——
  正是 §4.1.3「Test Set 欄變成 TC ID 欄之近似複本」的過granular 反模式。
  先例：SXM `Instant Replay`(30) / `Browse`(39) 之不拆理由同源。

### Batch plan（生成批次 ≠ Test Set）

| Batch | Leaves | n | 內容 | 依賴 |
|---|---|---|---|---|
| **B1（pilot）** | -001, -002, -003, -004, -005 | 5 | 三個 Test Set 各至少一片；SCV 之 restore 與 signal 側 | **無** |
| B2 | -006, -007, -008, -009, -010 | 5 | AMP present / not present 之四條件分支 + AMP 側 recall | **A-PV14 平台版本須先定** |

**pilot 刻意避開 AMP-present 分支**：那五片需引用 V6_R2，而 A-PV14
（`inputs/` 之 V6_R2 來自 DT28 平台樹而非 HDCC28）尚未結案。
如此 pilot 不被任何未決項阻塞，且仍覆蓋全部三個 Test Set。

### Privacy notes

1. **AMP present / not present 是成對的正負分支，不是重複**：
   -006/-007（自動調整側）與 -009/-010（使用者調整側）各構成一對
   present / not-present。依 §7「列舉之支援項必配至少一負向 TC」，
   兩對皆須各自成 TC，不得合併。

2. **Service / HMI 為軸，非 Set**（§8.3）：037 Sub Categorization 將
   -001/-004/-005/-010 標 `Service`（訊號側）、其餘六片標 `HMI`
   （顯示側）。該軸橫跨 Speed-Controlled Volume，可作為同一 Set 內
   sibling 之區辨提示，但不得升為 Test Set 邊界。
   先例：AMFM 注 2（band 是切分軸非 Set 邊界）、Projection §N.4（傳輸軸）。

3. **外部參照 VF651 —— 平台一致性（R24-2）**：`specification_reference`
   之 VF651 來源檔一律取 **HDCC28** 平台版本。
   - `VF651_V2_R2`（LTM Non-Amplified）：`inputs/` 現存 `d5813bb7…`
     已確認為 HDCC28 基線（R23-2）
   - `VF651_V6_R2`（LTM/ETM Amplified）：`inputs/` 現存 `49dd3c31…`
     實測來自 **DT28** 平台樹；HDCC28 副本為 `e20ba7a4…`。
     **A-PV14 未結案前不得於 B2 引用**（R24-2 之先量後換）
   - `VF651_V3_R3`（ETM Non-Amplified）：在庫、**不引用**；
     不得因未列而視為已排除（A-PV03 / R-PV01(a)，DEFERRED 至 P2 重驗）
   - ANC 兩變體（V9_R3 / V11_R3）：Not requested（A-PV02）。
     若 P2 發現任一 leaf 觸及 ANC 配置，**停手回報**，不自行擴充

4. **範本層缺陷不修，隨 RD-1 回報上游**：下拉選單 R10 指向 `$A$1:$A$9`
   而 R11:R59 指向 `$A$1:$A$11`（含 2 空選項）（A-PV10 / R23-6）；
   `Reference!C9` 與 `下拉選單!A6` 第 6 條字串不符（A-PV11 / R23-7）。
   lint 之 design_method 權威為 `下拉選單!A1:A9` 九詞條。

5. **舊分頁保留**：`Cover_old` / `ChangeHistory_old` 原樣保留，
   不進 lint、不進 trace、不寫回（A-PV12 / R23-8）。
   佐證：AMFM 已交付件同樣保留該兩頁。

### Workbook sync

BLANK workbook、FILL 適用：Test Group `Privacy` 與 Part VI 之 Test Set
值寫入每一生成列之 G / H 欄。
範本 rev C 是否帶 `Test Case Framework` 分頁，於 feature.yaml 接線時
查證（Tier 1）；若有，填入三個 Set 名稱，否則逐列欄位即足（AMFM 先例）。
```

---

## 3. 執行層作業（依序）

1. 貼入 §1（R25）至 `features/privacy/RULINGS.md`
2. **append §2 之 Part VI 全文**至 `docs/fw036/framework.md` 檔末；
   同步更新該檔首句「Covers Test Groups …」加列 Privacy（Part VI）
3. `DECISIONS.md` §8 Sign-off 區塊填入：簽核人 Pei、日期 2026-08-13、
   依據 R25-2。**逐字記錄，不得改寫既有裁決內容**
4. 建立 `features/privacy/inputs/BASELINE.sha256`（R25-3），
   欄位：檔名 / SHA256 / 命中之客戶樹路徑 / 稽核日期。
   確認未被 `.gitignore` 排除；**若被排除，停手回報，不自行修改 `.gitignore`**
5. `PLAYBOOK.md` §6：勾 **P2**（R25-2）；P3 之 framework 部分標為已核可、
   profile 待建
6. 起草 `docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`：
   比照 SXM profile 體例（同為 BLANK + rev C 範本），
   `[OVERRIDE]` / `[ADD]` 條款須逐條標明其取代之通則條號。
   **草案完成即回報，不自行定案**（profile 核可為 chat 觸點）

**不做**：不執行 B1 生成（待 profile 核可）、不引用 V6_R2、
不動 `backend/api_server.py`、不追查素材消失機制、
不處理其他 feature 之任何事、不執行任何 git 操作。

---

## 4. 停手條件

1. `docs/fw036/framework.md` 已存在 Part VI（與前提不符）→ 停止 append，
   續行第 3–6 項，回報既有內容
2. `BASELINE.sha256` 之路徑被 `.gitignore` 排除 → 停止該項，
   續行第 5–6 項，回報 `.gitignore` 相關行號
3. 第 3 項發現 `DECISIONS.md` §8 已有簽核紀錄 → 停止填入，
   續行其餘，回報既有內容
4. 第 6 項起草 profile 時，發現 SXM profile 之任一 `[OVERRIDE]` 條款
   在 Privacy 情境下**無對應通則可取代** → 停止該條，續行其餘條款，
   逐條回報

---

## 5. 上繳包要求

寫入 `features/privacy/docs/upstream/04_framework.md`，須含：

1. §3 六項完成狀態
2. Part VI append 後之 framework.md 行數與 Part VI 起訖行號
3. `BASELINE.sha256` 全文
4. profile 草案全文（供 chat 核可）
5. `PLAYBOOK.md` §6 更新後全文
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R25-1 framework 三層核可 —— §1，區塊形式
- [x] R25-2 DECISIONS 整份簽核 + Sign-off 為獨立動作之體例 —— §1，區塊形式
- [x] R25-3 BASELINE.sha256 入版控 —— §1，區塊形式
- [x] framework Part VI 全文草案 —— §2，可直接 append 之區塊
- [x] 停手條件四項（已依 R17-1 明列標的與續行標的）—— §4

<!-- HANDOFF-LINK: 04 -> upstream:04 -->
