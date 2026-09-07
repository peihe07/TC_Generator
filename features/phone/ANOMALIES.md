# ANOMALIES — FW036 Phone HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PHnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

登記日一律 2026-09-07（下放包 PH-01 Phase 0–1）。

---

## A-PH01 — SYS1 有兩份互不相容之匯出（PENDING，**升級**）

`_intake/Phone/` 與 `spec-index/cache/` 各有一份**同檔名**之
`SYS1_HMI_Phone_HMI_Logic_and_Flow_R1_SR24_Post 2A_(June_21_2022).xlsx`，
sha256 不等：

| 來源 | sha256 | docProps modified | Basic Report 列 |
|---|---|---|---|
| `_intake/Phone/` | `e6d58766cf6ddb19…` | 2026-05-19T03:00:52Z | 273 |
| `spec-index/cache/` | `61c3a6a022f8dd18…` | 2026-03-16T06:33:04Z | 273 |

**兩份列數相同（273）——故任何以列數為準之檢查對此一律沉默。**
逐列實測（`data/sys1_variant_diff.tsv`）：ID 不同 **125** 列、Outline Number 不同 **124** 列。

根因為**兩處單列增刪互相抵銷**：

- `_intake` 版多 `NRL-535272`（`PHCC8.)` 若干句，落 Outline `5.17`），
  致 `NRL-127983`～`NRL-128106` 之 Outline **整段後移一格**。
- `_intake` 版少 `NRL-128107`：其正文被**併入前一格 `NRL-128106`（17.5）之儲存格**
  （該格尾端可見 `…the select...NRL-128107 - TTS if TTS currently active)…`），
  故第 17 章在 `_intake` 版只到 `17.8`，`cache` 版到 `17.9`。

**其後果在追溯，不在字數** —— `spec_reference` 之 `{檔名}_{章節號}`（IN §10.7(b)）
在 `5.17`～`17.5` 區間之 124 列會指向不同需求。

**且兩份皆非 037 之來源**：037 引用 `_5.16.2`（`PHCC8.`）與 `_17.9`，
前者兩份皆無（`_intake` 置於 `5.17`），後者只有 `cache` 有。
即上游至少有**第三份**匯出，其 `PHCC8.` 為 `5.16` 之子項。

→ **`DRAFT-PH-a`（DR 草稿，未取號）**。裁定前 `feature.yaml` `paths.sys1_export = null`，
`sources.sys1_export` 不登錄，`recon.py` 之 outline 斷言為 FAIL（如實留著）。

## A-PH02 — 43.6 MB PDF 之文字層詞序錯亂（RESOLVED-WORKAROUND）

`Phone HMI Logic&Flow R1.pdf`（PDF24 產製，21 頁，1920×1108 pt）**有**文字層
（`pdftotext` 得 140 664 字元），惟字型為 **Type 3 ／ Custom 編碼**，
`pdftotext -layout` 之詞序錯亂，例：`Unauthori z ed`、`Pro j ection`、
`MPA 2 1`（實為 MPA12）、`follow N AFTA`。

**處置**：改以 `pdfplumber` 取 word 之 `(top, x0)` 重排，實測還原正確
（見 `docs/26pi_delta.md` 之抽取）。`sources/extracted/phone_hmi_lf_pdf_26pi/`
由 `extract_source.py` 產出（其內部亦用 pdfplumber），**該抽取物可用**；
但**任何以 `pdftotext` 讀本檔之後續步驟一律不可信**。

spec_mode 判定：**B 可用**（非 C）；不 OCR。

## A-PH03 — 26PI 之日期兩說（PENDING，僅揭露）

變更日誌 xlsx 記 `05/20/2026`；同一變更於 PDF p.1 之變更列記 `May 11 2026`。
相差 9 日。逐字照錄，不調和。不影響本輪（MPA11／MPA12 本輪不併入，R-PH2）。

## A-PH04 — 037 description 之機械改寫痕跡（PENDING）

037 之 `Requirement Description` 大量為「`The system shall ` ＋ SYS1 原句」之
機械前綴，且**原句首字母被降格**，致：

| 類 | 列數 | 例 |
|---|---:|---|
| L1 標籤殘留 | **80** | `The system shall pHCAT3.2)…`、`The system shall mP04.1)…`、`The system shall sMS12.1)…` |
| L2 首字母降格 | 12 | `The system shall dND…`、`The system shall rOAMING…`、`The system shall nAFTA`、`The system shall bUX…` |
| L3 非動詞連接 | 574 | `The system shall if…`（137）、`The system shall the…`（90）、`The system shall when…`（40） |
| L4 非字母開頭 | 38 | `The system shall (image:…`、`The system shall “Answer”…`、`The system shall 555-262-4312,…` |
| **合計** | **704** | 全列清單見 `data/mechanical_rewrite_candidates.tsv` |

下放包 §4 任務 3-3 所指定之字面 regex `^The system shall [a-z]` 實測命中 **716** 列
（754 leaf 中之 95%）—— 該式**不具鑑別力**，因合法句 `The system shall allow…`
亦以小寫起始。上表為分類後之結果，查詢條件見 TSV 首列與本節。

**候選而非裁定**：verbatim 上半改取 SYS1 原句（IN §8.6）之處置待 Phase 2；
且其可行性**繫於 `DRAFT-PH-a`**（要取哪一份 SYS1 的原句）。

## A-PH05 — 下放包 §4 任務 3-2 之前提與實測不符（僅揭露，已循 FO §8.2 不調和）

下放包載「037 只載文件名（`HMI Source ID` 欄 = 文件名），**無 NRL 號亦無章節號**」。

**實測不然**：037 `HMI Source ID`（C 欄）之值形如
`Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022)_10.14.1`，
**本身即帶章節號**，213 個 parent 對應 213 個相異值，恰為 IN §10.7(b) 之
`{檔名}_{章節號}` 形制。三處獨立佐證：本包之逐欄量測、`intake.py`
（「sources: document citations (need-list derivable)」）、`recon.py`
（「citation column: C；distinct sections cited by the leaves: 213」）。

故對映不必以 description 文字比對為唯一手段；本包兩法並陳（上繳包 §4-2）。
**惟無 NRL 號一節屬實**（037 無 Polarion ID 欄）。

## A-PH06 — Multiphone 關鍵字子集之數與下放包預期不符（僅揭露）

下放包 §5 預期 42 parent／120 child；本包以其所載查詢條件實測 **35 parent／108 child**
（child 以「parent 命中則其 child 全帶入」計；直接命中之 child 為 17）。
另試 6 種查詢變體（含前綴不帶數字、全欄關鍵字、標題＋描述），**無一還原 42／120**。
不自行調和。本項為**登記用、非範圍**（R-PH2），不阻擋任何步驟。

## A-PH07 — MPA11 與本 feature 之客戶側名稱方向相反（PENDING）

26PI 新增之 `MPA11) Multiphone not applicable for R1L-R` 與客戶側資料夾名
「Bluetooth, Multiple Phones Paired Simultaneously」在方向上相反。
037 V0.1 之基線為 SR24 Post 2A（2022-06-21），早於 26PI，故 037 內
Multiphone 條文（parent 35 列，含 child 143 列）之現行效力存疑。

→ **`DRAFT-PH-b`（DR 草稿，未取號）**。本輪仍依 R-PH2 走完整份 037，不預先剔除任何列。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PHnn]`.
