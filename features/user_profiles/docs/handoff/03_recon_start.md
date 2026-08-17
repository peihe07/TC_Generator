# 03 下放包 — User Profiles 作業 6–8 開工（DR #1 已到齊）

承 `02b_tasks.md` 作業 6–8 之前置解除。裁決見 `01a/02a_rulings.md`。

## 素材現況（分析層實測，2026-08-17，`get_file_info` 對 repo 實際路徑）

| 檔 | bytes | mtime |
|---|---|---|
| `inputs/FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` | **143,645** | 2026-08-06 15:36:53 |
| `inputs/…_SWQT_20260817_ext.xlsx`（036 母本複本） | 200,650 | 2026-08-17 09:46:09 |
| `inputs/SYS1_HMI_Personal_Account…(February_10_2023).xlsx` | **60,091** | 2026-08-17 03:02:00 |
| `spec-index/cache/SYS1_HMI_Personal_Account…(February_10_2023).xlsx` | **60,091** | 2026-04-24 22:14:53 |

**未驗**：以上為 bytes 與 mtime，**非雜湊**。分析層無 hash 能力；
兩份 spec 之同一性尚未證明（大小相同不等於內容相同）。

## 作業

1. **037 採認前置** — `shasum -a 256`；表頭列以 `Requirement Description`
   定位並回報實得列號（下放包預期 7，未複驗）。
   Phase 0 之全部 037 側數字係分析層於 **Project 附件副本**上量得
   （該副本 143,645 bytes，與本檔大小相同但**未比對雜湊**）；
   本輪一律以 `inputs/` 這份重新實測，不沿用。

2. **作業 6 Recon** — 依 R-U8 三閘：`functional_requirement_count == 180`、
   `heading_count == 25`（欄值等於 `Heading`，非 `len(headings)`）、
   `out_of_scope_count == 2`。182 為對照輸出，不作閘。
   **不符即停，不得調整判準**（Comfort R-C3）。

3. **作業 7 037 側複驗** — header row、FROP 欄 182 列值、
   PROF-017／035 之 Out of scope 身分、引用 135 id 與
   `data/expected_cited_sections.tsv` 之**集合對集合**比對（非計數比對）、
   Sub Categorization 與 Priority 分布、被引 135 條之長度分布與圖片參照數。

4. **BASELINE.sha256 更新** — 依 R-C20 比照（涵蓋以來源為準），
   涵蓋 `inputs/` **全部**檔案（現為 3 檔）＋ spec-index 三件。
   更新後 `shasum -a 256 -c` 須全數 OK 並附輸出。

5. **兩份 spec 之同一性驗證（只驗，不處置）** —
   `inputs/` 與 `spec-index/cache/` 之 R1L-R 各算 SHA256 並比對。
   相同或不同**都不得自行刪除、移動或改引用路徑** —— 處置屬 Tier 2／3，
   見 R-U17 提案。R-U3 之 spec 基線引用路徑維持 `spec-index/`。

6. **作業 8 Layer 2 草案第二版** — 037 分群到齊後重出，
   須同時處理 §4.2：`All Profiles Tab` 為 UI widget 名、
   `Profile Overview`／`New Profile Setup` 與 Test Group `User Profiles`
   重複前綴。仍為 Tier 2，只出草案不自裁。

## 不在本包授權範圍

- 刪除或移動 `inputs/` 內任何檔（Tier 3）
- 動 `spec-index/`（R-U9 之移入須待 DR #4 到齊）
- spec 4.1.1（Profile Setup）相關之 TC 生成（R-U15 未裁前一律不動）
- 任何 git 操作

## 上繳

`docs/upstream/03_recon.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷，每個數字標明量測條件。

## 仍待 Pei 裁定（不擋本包）

R-U13（`.gitignore` 例外追認）、R-U14（A-UP09 解除條件＝機器檢查）、
R-U15（DR #4 之阻斷範圍）、R-U16、R-U17。
其中 **R-U14 管 Phase 6 能否開工**，本包不觸及該階段。
