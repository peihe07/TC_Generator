# batches-sxm.md — 202 leaf 批次分組表(B1–B14)

Single source of truth for batch membership. Test Set 名稱與章節分配為
framework Part IV 的簽核表(Pei 2026-08-10);此處把它變成**被檢查的宣告**——
`build_stla_map.py --check-batches` 會把每個 leaf 的 STLA id 解析到 CFTS024
章節,並在 leaf 落在批次宣告章節之外時失敗。

Leaf ids 是 `SWE-RA-SXM-nnn` 的數字尾;`a-b` 為含端點區間。`n` 欄與展開後的
id 清單交叉檢查。

**批次 ≠ Test Set**:Instant Replay(30)與 Browse(39)兩個 Set 依 §4.2 不拆,
但生成負載切在批次層 —— B1/B2 同屬 Instant Replay,B8/B9 同屬 Browse。

| Batch / Test Set | CFTS024 sections | n | Leaf ids | Context 注入來源 |
|---|---|---|---|---|
| B1 (pilot) — Instant Replay | 1.5.10, 1.5.10.1, 1.5.10.4, 1.5.16 | 20 | 063-075, 087-092, 154 | ReqIF 條文 + 印刷編號;§1.5.10/.1/.4 未配置條款隨批(R10-2 決策測試素材);§1.5.16 只因 154 而列(pilot 裁決把它移進本批;該節其餘 7 條在 B11),內容以 `4872962` 條文為準,reasoning 疊 `[A-SX03]`+`[A-SX07]` |
| B2 — Instant Replay | 1.5.10.2, 1.5.10.3 | 11 | 076-086 | 080 帶 R11 引用式(`CFTS024-193/195/197`);083 帶 `[A-SX03]` |
| B3 — Seek | 1.5.1, 1.5.2 | 16 | 006-021 | `[[table:seek_cancel_stop]]` 為 009/012/017 的 cancel/stop 判準來源;020 帶 twin mirror Remarks |
| B4 — Tune | 1.5.3, 1.5.4, 1.5.5 | 12 | 002, 003, 022-031 | 024 帶 twin mirror Remarks |
| B5 — Source Availability + Presets | 1.5, 1.5.6, 1.5.7 | 9 | 001, 004, 032-038 | 037 帶 twin mirror Remarks;§1.5 有 14 條未配置條款(全 corpus 最密) |
| B6 — Favorites | 1.5.9, 1.5.9.1 | 17 | 005, 039-054 | 005 帶 R11 引用式 |
| B7 — Activation | 1.5.9.2 | 8 | 055-062 | 訂閱/啟用狀態為 §3.2 合法前置 |
| B8 — Browse | 1.5.11, 1.5.12, 1.5.12.1, 1.5.12.1.1 | 20 | 093-112 | 107 帶 R11 引用式(`CFTS019-494/496`);108/110 帶 twin mirror Remarks |
| B9 — Browse | 1.5.12.1.2, 1.5.12.1.3, 1.5.12.1.4 | 19 | 113-131 | — |
| B10 — List Navigation | 1.5.13, 1.5.14, 1.5.15 | 19 | 132-150 | 132/140/142/143/148/149 帶 twin mirror Remarks(全 corpus 最密);137 帶 R11 引用式(`CFTS020-138`) |
| B11 — Traffic & Weather | 1.5.16 | 7 | 151-153, 155-158 | 154 已在 B1;本批 7 條中 4 條帶 `[A-SX03]`,合併閱讀 |
| B12 — Game Alert | 1.5.17 | 9 | 159-167 | — |
| B13 — Parental Skip + Error Displays | 1.5.19, 1.5.20 | 15 | 168-182 | 182 帶 `[A-SX03]` |
| B14 — Performance | 1.5.21.2, 1.5.21.2.2, 1.5.21.2.3, 1.5.21.2.4, 1.5.21.2.5, 1.5.21.2.6, 1.5.21.2.7 | 20 | 183-202 | §1.5.21.1 與 §1.5.21.2.1 為整節無 leaf 缺口,不得吸收,送 RD-1 Q-SX |

總計 202(= 037-A03 全部 leaves)。

## 各批附帶指示

- 每批 context = 037 該批原文列(title 含 STLA id 尾標 + description)
  + **ReqIF 條文**(HYBRID 來源)+ **docx 印刷章節號與 scope metadata**
  + framework Part IV 該 Test Set 節 + AMFM done region exemplar
  (**`cross-feature: style only`**,R4:借風格不借追溯)+ sibling rows
- Test Group 一律寫 `SXM`,Test Set 寫 Part IV 的能力名稱(BLANK workbook,
  FILL 已裁)
- spec_reference 用 `{doc}-{stla_id}`,取自 `data/stla_to_cfts.json`,不手填
- `Estimated Test Time`(Q 欄)**留白**,不是慣例留白而是待裁(A-SX05)
- 未配置條款隨批攜帶並帶 scope 標籤;R10-2 決策測試逐條跑,吸收即標
  `[A-SX08]` 並多引;整節缺口不得吸收
