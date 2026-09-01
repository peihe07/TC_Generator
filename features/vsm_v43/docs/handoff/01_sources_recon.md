# 下放包 01 — vsm_v43：上繳 00 覆核、R-VT6–R-VT8 落地、W-2～W-6 續行

日期：2026-09-01
取號：落檔當下 `list_directory docs/handoff/` 實測有 00，取 01
對象：執行層。00 包之禁區、§三素材清冊、§六預期數字 E1–E9、§七、§八**繼續有效**，本包只載差異。
前提（**2026-09-01 實測修正**）：原檔未落 `_intake/`（實測 0 files），而落於 `features/vsm_v43/inputs/`（5 件）：
V43 規格 R4 docx、V43 SYSRA、SYSAD，**另含 V42 之兩份 037**。W-2 以此為來源落 `sources/raw/`（R-G27），落完後 `inputs/` 清空。
兩份 037 與 `features/vsm_v42/inputs/` 之同名檔 sha 比對，相同則**不另建 doc_id**（取 vsm_v42 之 `vf665_037_*`，MANIFEST features 欄加 `vsm_v43` 並 note「非本線母體，供 E7 與 DR-VT1 佐證」）；不同則停下回報。
SYSAD 同法：與 vsm_v42 之檔及 `features/vehicle_setting/inputs/` 之 `469162b8…` 三方比 sha。§三 W-2 之「#3 由 vsm_v42 落」改為：誰先跑誰落，後者只加 features 欄。
**A-VT3（recon.py 改碼）待 Pei 裁**：裁前 W-3 維持「不改腳本、人工 RECON.md」。

---

## 一、上繳 00 之覆核結果

| 項 | 判 |
|---|---|
| 停於 W-1；E1–E9 全填「未實測」不轉錄 §三數字 | **對**，讀法確認為通則 |
| A-VT1／A-VT2／A-VT3 皆不成對開 DR | **裁可**（皆非上游資料請求） |
| A-VT2 `tc_id_prefix` | 分析層之誤 → **R-VT7**；A-VT2 轉 RESOLVED |
| A-VT3 `recon.py` null guard | 共用腳本，**交 Pei**（§四）。裁前走人工 RECON |
| A-VT4 模板序列標記 | 執行層逕改，核實 |
| §九-6 R-P375 | 分析層之誤 → **R-VT6** |
| §八 台帳重生 | → **R-VT8(a)**：本線不重生，由 vsm_v42 01 包做 |
| §九-1 SYSAD 共引路徑 | 分析層之誤（A-VT5(c)），本包前提已改記路徑現況 |
| §九-5 workbook.columns 模板值 | → **R-VT8(b)** |

自誤登 A-VT5。

## 二、裁決引用（R-G13）

R-VT6／R-VT7／R-VT8 全文在 `RULINGS.md`。sha8 自 vsm_v42 01 包重生後之 `docs/fw036/RULINGS.sha.tsv` 讀取回報；R-VT1–R-VT5 須與上繳 00 §七逐字相同。
新引用 PM 條文：R-P375（`features/power/RULINGS.md:12640–12672`）、R-P369(b)。

## 三、作業清單

**W-1′ feature.yaml 修正**：刪 `tc_id_prefix`；`write_back.tc_id_format: "NR1L-VSM43-{n:03d}"`（R-VT7）；`spec_reference_template: null` 註「待 P3」（R-VT8(c)）；`paths.spec_docx`／`sysra`／`sysad` 自 `TBD` 改為 `../../sources/raw/<doc_id>/*` 相對 glob（同 vsm_v42 形制）。

**W-2 sources 落檔**：#1、#2 依 R-G27 落 `sources/raw/`、`extracted/`、MANIFEST 加列（features=`vsm_v43`）；#3 若 vsm_v42 已落則 MANIFEST `features` 欄加 `vsm_v43`，未落則記缺。
起手 R-VT8(b)：建 `sandbox/base/`，`cp` 母本，`cmp` 全等；`workbook.*` 自副本 r9 實測回填，每欄實測 vs 先驗上繳。
docx magic bytes 判讀；R-G28 對 #1 清點嵌入物件。

**W-3 人工 RECON.md**（A-VT3 裁前）：workbook_state BLANK、#1／#2 sha、SYSRA 計數（E1–E6、E9）、`a03_report = null (DR-VT1)`；標「人工，依 A-VT3」。

**W-4 SYSRA 分層預查**：依 00 包；`VF655` 247 列、DocID 空 82 列分別標記不入分母（DR-VT2）；`Out of scope`／`Out of Scope` 正規化計數後登 anomaly（live 取號）。

**W-5 訊號解析預查（R-VT6 取代 00 包 W-5 之段 1 條件）**：段 1 對 forms/ 七檔查；`data/signal_chain_v43.tsv` 欄位與結果值域同 vsm_v42 01 包 §三 W-5（`規格原名 | 類別 | 段1命中(多處;分隔) | 段2 | 段3 | 結果`，結果含 `UI路徑`／`PROXI路徑`／`B-1 衝突`）。V42↔V43 訊號名差集：V43 側自 #1 抽；V42 側**只讀** `features/vsm_v42/data/signal_chain_v42.tsv` 之規格原名欄（若該檔尚未產出，差集記「待 vsm_v42 W-5」，不自抽 V42 docx）。

**W-6**：A-VT 自當時末號 live 取；DR-VT1／VT2 沿用。

## 四、待 Pei 裁（A-VT3）

`recon.py` 於 `a03_report`／`workbook` 為 null 時 TypeError（`:430`、`:582`）。執行層建議加 None guard（`survey_workbook`／`survey_a03` 早退回空 dict，約十行，對既有 feature 零行為改變）。
分析層意見：**建議核可**，附條件 —— (i) `pytest` 通過；(ii) 對任一既有 feature（如 bed_lowering）改碼前後 `recon.py` 輸出逐位元相同並上繳 diff = 0；(iii) 改碼登全域線（`docs/fw036/` 之 A 或 R-G 加註），非本線條文。裁前本線走人工 RECON。

## 五、預期數字（本包新增；00 包 E1–E9 本包首測）

| # | 項 | 預期 | 掃描條件 |
|---|---|---|---|
| E10 | R-VT1–R-VT5 sha8 | 與上繳 00 §七逐字相同 | 字串比對 |
| E11 | sandbox/base 副本 sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | `shasum`；cmp 全等 |
| E12 | 副本 r9：design_method／author 欄 | R／AA（先驗） | 逐欄讀表頭 |
| E13 | #1 docx magic bytes | `50 4B 03 04` | 前 4 bytes |
| E14 | `Out of scope`＋`Out of Scope` 正規化後 | 99 | 小寫全等 |
| E15 | `signal_chain_v43.tsv` B-1 衝突列 | 0（≥1 即停交 §K） | 結果欄計數 |

## 六、上繳要求（`docs/upstream/01_sources_recon.md`）

00 包 §七全部，加：W-1′ 三鍵實值；E10–E15；人工 RECON.md 本體；W-5 七檔各命中數、結果分布、§K 表（空亦列）、差集或「待 vsm_v42」；R-VT6–R-VT8 sha8。

## 七、升級條件（00 包 §八續有效，加）

E10 任一不同；E11 不全等；E13 非 OOXML；E15 ≥ 1（停該部分）；原檔缺任一件停於 W-1′。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 已登記，建議送出 |
| DR-VT2 | SYSRA DocID `VF655` 疑誤植；R3 vs R4 | no | 已登記，未送出 |
