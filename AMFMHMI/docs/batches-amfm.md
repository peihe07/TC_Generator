# batches-amfm.md — 102 leaf 批次分組表(11 批)

Single source of truth for batch membership, the same role
`docs/batches-home.md` plays for Home. The Test Set names and their CFTS
section allocation are the Phase 3 ruled table (framework Part III, R7-Q2);
what is new here is that the allocation is **checked**, not asserted —
`build_stla_map.py --check-batches` brackets every leaf's STLA id into a CFTS
section and fails if a leaf lands outside the sections its batch declares.

Leaf ids are the numeric tails of `SWE-RA-RAD-nnn`; `a-b` is an inclusive
range. The `n` column is cross-checked against the expanded id list.

| Batch / Test Set | CFTS sections | n | Leaf ids | Context 注入來源 |
|---|---|---|---|---|
| Tuner Availability | 1.3 | 2 | 001-002 | CFTS024 §1.3 HU Analog Tuner (AM presence gate); SYSAD AMFM_RADIO_APP |
| Seek | 1.3.1, 1.3.2 | 11 | 003-013 | CFTS024 §1.3.1 Seek Up / §1.3.2 Seek Down; `[[table:seek_cancel_stop]]` 為 006/007/008/011/012/013 的 cancel-vs-stop 判準來源;`[[table:pi_seek_ordering]]` 為 004 吸收 4872385 的排序規則來源; band split axis (§8.3) |
| Browse | 1.3.3, 1.3.3.1, 1.3.3.2 | 11 | 014-024 | CFTS024 §1.3.3 + Presets/Genre subsections; 014 的 clause 4872420 引用 `{See CFTS019-718}` (rejection tone) — R11 引用式:多引 `CFTS024-4872420; CFTS019-718`,ER 以 `as defined by CFTS019-718` 錨定,不測 CFTS019 規則面 |
| Tune | 1.3.4, 1.3.5, 1.3.6 | 6 | 025-030 | CFTS024 §1.3.4-1.3.6; A-AM08 適用 028/029 (共用 4872451) |
| Presets | 1.3.7, 1.3.8 | 9 | 031-039 | CFTS024 §1.3.7 Select/Recall + §1.3.8 Save; short vs long press; `[[table:radio_tuner_configuration]]` 為 039 preset label 的 AF 市場適用性來源 |
| List Navigation | 1.3.10, 1.3.11, 1.3.12 | 12 | 040-051 | CFTS024 §1.3.10-1.3.12 Scroll / Page / Enter |
| RDS Features | 1.3.13, 1.3.13.1, 1.3.13.2 | 12 | 052-063 | CFTS024 §1.3.13 + TA/PTY31 + AF subsections; `[[table:ta_pty31_cancel]]` 為 4872538 所指的 TA/PTY31 取消動作來源（062 吸收）;057 引用 `CFTS024-707`（R11 引用式) |
| Station List | 1.3.14 | 17 | 064-080 | CFTS024 §1.3.14; largest set, single section |
| Market Configuration | 1.12.1.3.1.5, 1.12.2.2.1 | 5 | 081-085 | CFTS024 §1.12 Country_Code / HU Radio Configuration |
| Engineering Mode | CFTS011 (external) | 9 | 087, 089-096 | A-AM06 檔案未到;037 title 自帶需求原文 (blocked-parent proportion test) |
| Diagnostics | CFTS004 (external) | 8 | 097-104 | A-AM07 attribution 為假設;每條 TC reasoning 標 `[ASSUMPTION A-AM07]` |

總計 102 條(= 037-A03 全部 leaves)。編號缺口 086 / 088 存在於 037 本身
(A-AM08),不是本表的遺漏。

## Pilot 批次提議

**Tuner Availability (2) + Tune (6) = 8 leaves.**

理由:

- Tuner Availability 是 §4.2 的合法離群(2 條),它的 AM-presence 設定閘門與任
  何兄弟集合都不共用 setup —— 先跑它,可以在最小成本下驗證「設定型前置條件」
  這條路徑
- Tune 帶 A-AM08 的 028/029 重複對(共用 STLA id `4872451`),讓 R7-Q4 的標注
  機制(`duplicate_of` / `distinguishing_axis`)在 pilot 就被實地檢驗,而不是
  等到第 5 批才發現標注格式不對
- 兩批合計 8 條、跨 4 個 CFTS 節(1.3 / 1.3.4 / 1.3.5 / 1.3.6),足以檢查
  spec_reference `{doc}-{stla_id}` 與節文字注入,又不會大到讓 review 失焦

替代方案 Seek 前段(003-008,§1.3.1 六條)覆蓋單一節、無 anomaly,樣本較同質
—— 作為 pilot 能驗證的東西比較少。最終切法在 pilot gate 前由 Pei 定。

## 各批附帶指示

- 每批 context = 037 該批原文列(title 含 STLA id 尾標 + description)
  + CFTS 對應節全文 + framework Part III 該 Test Set 節 + Wilson 同類
  exemplar 2-3 列(**style only**,R4:借風格不借追溯)+ sibling rows
- Test Group 一律寫 `AMFM`(R7-Q1);Test Set 寫本表的能力名稱(R7-Q2),
  **不用** legacy 的 band 方案(`FM`/`AM`/`USB`)
- spec_reference 用 `{doc}-{stla_id}`,`{doc}` 取自 `data/stla_to_cfts.tsv`
  的 doc 欄,不手填
- 001-080 多數同時適用 AM 與 FM;band 是 TC family 內的 split axis(§8.3),
  不是 Test Set 邊界 —— 不要為了 band 拆 Test Set
- Wilson 的 158 列是 frozen legacy region(R4 選項 i):可讀、可借風格,
  不得改動,不計入覆蓋率與追溯不變量
