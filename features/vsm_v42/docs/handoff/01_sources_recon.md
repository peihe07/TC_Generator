# 下放包 01 — vsm_v42：上繳 00 覆核、R-VL6–R-VL9 落地、W-2～W-6 續行

日期：2026-09-01
取號：落檔當下 `list_directory docs/handoff/` 實測有 00，取 01
對象：執行層。00 包之禁區、§三素材清冊、§六預期數字、§七上繳要求、§八升級條件**繼續有效**，本包只載差異。
前提（**2026-09-01 實測修正**）：原檔未落 `_intake/`（實測 0 files），而落於 `features/vsm_v42/inputs/`（5 件，16.46 MB）：
V42 規格 R6 docx、V42 SYSRA、兩份 037、SYSAD。W-2 以此為來源落 `sources/raw/`（R-G27），落完後 `inputs/` 清空（該目錄 gitignored），不得保留副本。
檔名與 00 包 §三所載有空白／括號差異，以實檔為準，MANIFEST 記實檔名。

---

## 一、上繳 00 之覆核結果

| 項 | 判 |
|---|---|
| 停於 W-1、不以抽取本代原檔、E1–E13／E16 填「未實測」而非轉錄 §三數字 | **對**。§三之數為分析層於 Project 內所測，預期與實測同源即無對照，執行層之讀法確認為本專案通則 |
| E14 = 65／E15 = 22 相符，來源在 forms/ 不在缺件內 | 核實 |
| A-VL1 不成對開 DR | **裁可**（投遞屬 Pei 動作，非上游請求） |
| 三項候選 anomaly 未先登 | 對；惟「A-VL2 起保留」不承認，見 A-VL2 附註（R-G23 live 取號） |
| 未預期發現 (1) `tc_id_prefix` | 分析層之誤 → **R-VL7**：改 `write_back.tc_id_format: "NR1L-VSM42-{n:03d}"`，刪 `tc_id_prefix` |
| 未預期發現 (2)(3) 欄組／R-P375 | 分析層之誤 → **R-VL6**：段 1 入口為 forms/ 全部參考檔，二欄組皆入口，多命中依 R-VL6(c) |
| §10-3 sandbox／母本時點 | → **R-VL8** |
| §11 丁 RULINGS.sha.tsv | → **R-VL9**：本包重生一次，夾帶 R-VT 五列為結構性 |
| §11 甲乙丙三支存量紅 | 與本線無關，核實其歸因；本線不觸 |

自誤登 A-VL2（三項，分析層之誤）。

## 二、裁決引用（R-G13）

R-VL6／R-VL7／R-VL8／R-VL9 全文在 `RULINGS.md`（本包同時落檔）。sha8 於本包 W-0 重生台帳後自 `docs/fw036/RULINGS.sha.tsv` 讀取回報；R-VL1–R-VL5 之 sha8 須與上繳 00 §9 逐字相同（不同即停）。
新引用之 PM 條文：**R-P375**（`features/power/RULINGS.md:12640–12672`）、R-P369(b)（同檔 :12473–12484）。

## 三、作業清單

**W-0 台帳重生（R-VL9）** —— 本包首步、只做一次
`python3 scripts/rulings_hash.py`（寫入 `docs/fw036/RULINGS.sha.tsv`）。先 `git status --short docs/fw036/RULINGS.sha.tsv` 確認為乾淨（Pei 已入庫）；若仍 `M`，停下回報，不覆寫。重生後 diff 須**恰為新增列**：R-VL1–R-VL9（9）＋ R-VT1–R-VT5（5）＝ 14 列，其餘逐位元相同；不符即停。

**W-1′ feature.yaml 修正（R-VL7／R-VL8(c)）**
刪 `tc_id_prefix`；`write_back` 下加 `tc_id_format: "NR1L-VSM42-{n:03d}"`；`done_region.author_value: null`。`spec_reference_template` 現值為執行層自填之 `{outline}` 構造式，**尚無裁決** —— 改為 `null` 並註「待 P3 裁（VF 類母件之 §10.7 型態未定）」，不得帶著構造式進 recon。

**W-2 sources 落檔** —— 依 00 包 W-2，加：
- 起手先 R-VL8(a)：建 `sandbox/base/`，自 forms/ 母本 `cp` 副本，`cmp` 全等回報；`paths.workbook` 指該副本實名。
- `workbook.sheet`／`header_row`／`columns` 自副本 r9 實測回填（R-VL8(b)），先驗值列於該條；每欄實測 vs 先驗逐項上繳。
- 每檔 sha256 自原檔實算；#5 SYSAD 與 `features/vehicle_setting/inputs/` 同名檔（sha `469162b8…`）比對結果上繳，相同則 MANIFEST `features` 欄記 `vsm_v42,vsm_v43`。
- R-G28：對 #1 docx 之 `word/embeddings/`、`word/media/` 清點。

**W-3 recon**、**W-4 leaf 母體**、**W-6 anomaly／DR** —— 依 00 包，DR-VL1 之「約 190」以 W-4 命中數回填實數。

**W-5 訊號解析預查（R-VL6 取代 00 包 W-5 之段 1 條件）**
段 1 對 forms/ **七檔**查（LID 全 14 分頁、HMI Settings List R1 SR25、PROXI `Format`、SR26 Default Settings、SR24 Market Configuration Table），`data/signal_chain_v42.tsv` 欄位改為：
`規格原名 | 類別(CAN/Req/Info/PROXI) | 段1命中(檔/分頁/欄/列，多處以;分隔) | 段2 MESSAGE.Signal 或 UI/PROXI 路徑 | 段3 DBC 檔 | 結果`
結果 ∈ {解得, 未解得(止於段1), 未解得(止於段2), 查無, B-1 衝突, UI路徑(R-P375b), PROXI路徑(R-P375b/c)}。
多命中而解至同一標的 → 一列記全部命中處；解至不同標的 → `B-1 衝突`，另列 §K 表交 Pei。**不自選、不合併**。
`forms/LOOKUP_MISSES.md` 只登段 3 實查後之「查無」（R-G14）。

## 四、預期數字（本包新增；00 包 E1–E16 續有效，本包首測）

| # | 項 | 預期 | 掃描條件 |
|---|---|---|---|
| E17 | W-0 台帳 diff 新增列 | 14（R-VL 9 ＋ R-VT 5），修改 0，刪除 0 | 逐行 diff |
| E18 | R-VL1–R-VL5 sha8 | 與上繳 00 §9 逐字相同 | 字串比對 |
| E19 | sandbox/base 副本 sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | `shasum -a 256`；cmp 全等 |
| E20 | 副本 r9 表頭：design_method／author 欄 | R／AA（先驗，非免測） | 逐欄讀表頭文字 |
| E21 | #5 SYSAD 原檔 sha256 ＝ `469162b8…`（vehicle_setting 既有檔） | 相同（預期） | 兩檔 `shasum` |
| E22 | #1 docx magic bytes | `50 4B 03 04` | `xxd \| head -1` 或 python 讀前 4 bytes |
| E23 | `signal_chain_v42.tsv` 之 B-1 衝突列 | 0（預期；≥1 即停交 §K） | 結果欄計數 |

## 五、上繳要求（`docs/upstream/01_sources_recon.md`）

00 包 §七 1–11 全部，加：W-0 之 diff 摘要與 E17／E18；W-1′ 後之 feature.yaml 三鍵實值；E19–E23；W-5 之七檔各命中數、結果分布、§K 衝突表（空亦列）；R-VL6–R-VL9 sha8。

## 六、升級條件（00 包 §八續有效，加）

- W-0 前 `RULINGS.sha.tsv` 非乾淨；重生 diff 非恰 14 新增列
- E18 任一不同；E19 cmp 不全等；E22 非 OOXML
- E23 ≥ 1（B-1 衝突）—— 停 W-5 該部分，其餘續行，衝突表隨上繳
- 原檔仍缺任一件 —— 停於 W-1′，回報缺件

## 七、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中約 190 列無 037 覆蓋（W-4 後回填實數） | no | 已登記，未送出 |
