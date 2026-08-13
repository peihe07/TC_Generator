# Projection — 往返索引

> 依 R-P96。每次往返一列。由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-13（下放包 20 §5 第 3 步）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-11 | Phase 0 onboarding | 未落檔 | 未落檔 | R-P1 ~ R-P11 † | — ‡ | — ‡ |
| 02 | 2026-08-12 | Phase 2 裁決 | 未落檔 | 未落檔 | R-P12 ~ R-P20 † | — ‡ | — ‡ |
| 03 | 2026-08-12 | Phase 4 pilot | 未落檔 | 未落檔 | R-P36 ~ R-P38 † | — ‡ | — ‡ |
| 04 | 2026-08-12 | Phase 5 批次 | 未落檔 | 未落檔 | — ‡ | — ‡ | — ‡ |
| 05 | 2026-08-12 | B3 | 未落檔 | 未落檔 | R-P42 ~ R-P44 † | — ‡ | — ‡ |
| 06 | 2026-08-12 | B10′ / B11′ | 未落檔 | 未落檔 | — ‡ | — ‡ | — ‡ |
| 07 | 2026-08-12 | VF176 / B11′ | 未落檔 | 未落檔 | — ‡ | — ‡ | — ‡ |
| 08 | 2026-08-12 | Handoff contract | 未落檔 | 未落檔 | — ‡ | — ‡ | — ‡ |
| 09 | 2026-08-12 | Phase 6 dry-run | 未落檔 | 未落檔 | R-P53 † | — ‡ | — ‡ |
| 10 | 2026-08-12 | Phase 7 寫回包 | [handoff/10_phase7_writeback.md](handoff/10_phase7_writeback.md) | 未落檔 | R-P67 ~ R-P74 | A-PJ61、A-PJ62 | — ‡ |
| 11 | 2026-08-12 | DR#14 處置 | [handoff/11_dr14_disposition.md](handoff/11_dr14_disposition.md) | 未落檔 | R-P75、R-P76 | A-PJ61 CLOSED；A-PJ45 部分結案 | — ‡ |
| 12 | 2026-08-12 | 第 6 步執行條件 | [handoff/12_phase7_step6_conditions.md](handoff/12_phase7_step6_conditions.md) | 未落檔 | R-P77 ~ R-P80 | A-PJ63 ~ A-PJ65 | — ‡ |
| 13 | 2026-08-12 | 第 F 步執行條件 | [handoff/13_phase7_stepF_conditions.md](handoff/13_phase7_stepF_conditions.md) | 未落檔 | R-P81 ~ R-P85 | A-PJ66、A-PJ67 | — ‡ |
| 14 | 2026-08-12 | A-PJ69 重跑 | [handoff/14_apj69_rerun.md](handoff/14_apj69_rerun.md) | 未落檔 | R-P86、R-P87 | A-PJ70、A-PJ71 | — ‡ |
| 15 | 2026-08-12 | Phase 7 close-out | [handoff/15_phase7_closeout.md](handoff/15_phase7_closeout.md) | 未落檔 | — | A-PJ72；A-PJ68 CLOSED | — ‡ |
| 16 | 2026-08-12 | Close-out 處置 | [handoff/16_closeout_disposition.md](handoff/16_closeout_disposition.md) | 未落檔 | R-P88 ~ R-P90 | A-PJ73 | — ‡ |
| 17 | 2026-08-12 | 交付前檢 | [handoff/17_delivery_precheck.md](handoff/17_delivery_precheck.md) | 未落檔 | R-P91 | A-PJ74 | — ‡ |
| 18 | 2026-08-12 | 交付執行 | [handoff/18_delivery_execute.md](handoff/18_delivery_execute.md) | 未落檔 | R-P92、R-P93 | — | — ‡ |
| 19 | 2026-08-12 | 旁檔政策 | [handoff/19_sidecar_policy.md](handoff/19_sidecar_policy.md) | 未落檔 | R-P94 | A-PJ75 | — ‡ |
| 20 | 2026-08-13 | 封存規範 + Operating Charter | [handoff/20_archive_and_charter.md](handoff/20_archive_and_charter.md) | [upstream/20_archive_and_charter.md](upstream/20_archive_and_charter.md) | R-P95 ~ R-P97 | A-PJ76、A-PJ77 | PASS |
| 21 | 2026-08-12 | canon §8 補寫 + Charter 收斂 + 自檢表修正 | [handoff/21_canon_s8_and_charter.md](handoff/21_canon_s8_and_charter.md) | [upstream/21_canon_s8_and_charter.md](upstream/21_canon_s8_and_charter.md) | R-P98、R-P99 | A-PJ78；A-PJ76 / A-PJ77 CLOSED | PASS |

---

## 2. 註記

### ‡ 未落檔之欄位

`—` 標於 01–19 之「產生之異常」與「結果」欄，係因該資訊**無法自 repo 還原**，非因該次往返無異常或無結果：

- **01–09 之下放包**未落檔（A-PJ62 之更正自第 10 號起才生效）
- **01–19 之上繳包全部未落檔**（R-P95 之缺陷，自第 20 號起補正）

該次往返之結果與異常，其**實質內容**已落於 `DECISIONS.md` / `ANOMALIES.md` /
`DATA_REQUESTS.md` / `profile`，該四處為權威。缺的是**逐包歸屬**，不是內容。

**不重建**——重建即為以記憶產出文件，違反 canon §5a 第十五條。

### † 推得之裁決範圍（01–09）

01–09 之下放包不存在，其產生之裁決編號**無直接紀錄**。表中所填係以
`DECISIONS.md` 之節標題主題與 §2 之下放包 slug **逐字比對**推得：

| NN | slug | 比對之 DECISIONS 節 | 節標題中之主題字樣 |
|---|---|---|---|
| 01 | `phase0_onboarding` | §0（2026-08-11） | 唯一之 08-11 節，Phase 0 |
| 02 | `phase2_rulings` | §0.1 | `Phase 2` |
| 03 | `phase4_pilot` | §0.9 | `pilot review` |
| 05 | `b3` | §0.11 | `B3 review` |
| 09 | `phase6_dryrun` | §0.17 | `dry-run 檢查表` |

**04 / 06 / 07 / 08 無可比對之節標題，故填 `—`。** 未比對到不代表該包未產生
裁決——`R-P21` ~ `R-P35`、`R-P39` ~ `R-P41`、`R-P45` ~ `R-P52`、`R-P54` ~ `R-P66`
均落於 §0.2 ~ §0.19 而無從歸屬至特定包。

**量測條件**：比對範圍為 `DECISIONS.md` 之 `^## 0` 節標題共 27 列，區分大小寫，
以主題字串（非編號）比對；`features/projection/docs/HANDOFF_archive_and_charter.md`
§2 之 20 列 slug 為另一側。此推導**不具權威性**，僅為索引用途；
任何以此為據之後續陳述須回到 `DECISIONS.md` 原文查證。

**可還原之邊界**：`R-P67` 起之逐包歸屬有直接紀錄（各下放包 §「本包產生之新條文
清單」），故 10–20 之裁決欄為實錄而非推得。`R-P1` ~ `R-P66` 全數落於
§0 ~ §0.19，其逐包歸屬僅部分可還原。

---

## 3. 目錄

```
features/projection/docs/
├── INDEX.md          ← 本檔
├── handoff/          10–21，共 12 檔（01–09 未落檔）
├── upstream/         20–21，共 2 檔（01–19 未落檔）
└── reports/          8 檔
```

`reports/` 內容：`dryrun_report.md`、`dryrun_v2_report.md`、`dryrun_v3_report.md`、
`phase7_step1_5_report.md`、`phase7_step_a_e_report.md`、`phase7_delivery_report.md`、
`git_inventory_closeout.md`、`closeout_pending_items.md`。

報告與往返編號之對應**未記錄**，同屬 ‡ 之缺口。自 NN=20 起，上繳包須於
`INDEX.md` 之「上繳」欄指向其報告。
