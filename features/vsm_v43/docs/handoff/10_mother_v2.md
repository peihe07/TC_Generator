# 下放包 10 — vsm_v43：暫代母體 v2 建檔（R-VT22 甲案）＋ K-10 回掃

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–09，取 10
台帳不重生；DR 不代發；不寫工作簿；**已凍 b1 一位元不動**。

## 一、W 清單

**W-1 母體 v2 建檔**（R-VT22(a)）：依 (i)–(iv) 合成 `data/leaves_interim_v2.tsv`——欄同 v1 加 `batch_source`、`spec_section`、`spec_section_source`（`direct`＝VF655 批偏移 0／`segment_map`＝295 批依 `data/section_map_v43.tsv` 分段換算／`none`＝無法換算者列數回報）。superseded 3 列另檔 `data/superseded_by_r4.tsv`（舊列全欄＋取代列 ID＋R4 修訂說明逐字）。**v1 不覆寫**。確實列數上繳（E73）。近似對之「實質獨有 5 列」以 09 包 `k6_vf655_vs_interim.tsv` 之對號實取，不重判。

**W-2 Layer 2 v2 列數實測**（R-VT22(b)）：依 (b) 之歸組規則逐列指派 `test_set`（v2 帶欄），輸出各組列數表——含三新組與十六舊組之增量；任何無處可放之列列出不硬配（E74）。

**W-3 K-10 回掃**（R-VT22(d)）：R4 修訂說明整節逐字取出（逐項編號）；每一「Replacement of X by Y」「Deleted Z」型項，以詞界式掃 v2 全批 `Description` 之 X／Z 命中；輸出 `data/k10_stale_hits.tsv`（項號｜修訂說明逐字｜命中列 ID｜命中片段）。只報不修。非 Replacement/Deleted 型之修訂項照列並標「不可機掃」。

**W-4 framework／DECISIONS 加註**：framework Layer 2 節加「v2 依 R-VT22 重組中，鎖定待 Pei」註（R-VT19 表不刪只標）；DECISIONS 母體列加 3″ 列（v2，列數實測值）。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E73 | v2 列數 | 實測值；= 295 − 3 ＋ (38＋5) ＋ 1 之算式逐項對帳 |
| E74 | Layer 2 v2 | 各組列數合計 = E73；無處可放 = 0（有則列出升級） |
| E75 | spec_section 覆蓋 | `direct`／`segment_map`／`none` 三類計數；`none` 逐列列出 |
| E76 | K-10 | 修訂項總數；可機掃項數；命中列數 |
| E77 | b1／v1 | b1 一位元不動（cmp）；v1 未覆寫 |

## 三、上繳（`docs/upstream/10_mother_v2.md`）

E73–E77；Layer 2 v2 列數表（供分析層定表→Pei 准）；K-10 命中清單；superseded 3 列；獨立判斷；gate_all 歸因。

## 四、升級條件

E74 無處可放 > 0 而被硬配；spec_section 之 `segment_map` 換算出現 section_map 未載之偏移值；對已凍 b1 或 v1 之任何寫入。
