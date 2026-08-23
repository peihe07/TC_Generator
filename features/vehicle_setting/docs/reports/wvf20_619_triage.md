# W-VF20 —— 以 619 為母體之陳述之逐句判別（R-VF18）

**V07 §6.4 之工單。只判不改。**

## 0. 錨點（R-VF11）

| 錨點 | 位置 | 判別 |
|---|---|---|
| 必為「不改」（逐行覆寫之標的） | `feature.yaml:119`（含 `388/619`） | 不改 |
| 必為「不改」（已上繳之歷史紀錄） | `docs/upstream/vf230/00_intake.md:21` | 不改 |

**錨點皆符。**

> **R-VF22 施行後，「須改」應為 0** —— 原判出之 2 處已改為 627。
> 首版之必為「須改」錨點指向 `feature.yaml:29`，於 R-VF22 施行後
> 即因該行不再含 `619` 而停 —— **R-VF21 第 1 項之正面作用**。

## 1. 判別規則（明列，逐行套用）

| 條件 | 判別 | 依 R-VF18 之理由 |
|---|---|---|
| 位於 `docs/handoff/` | 不改 | 下放包，作成當時之指示與量測 |
| 位於 `docs/upstream/` | 不改 | 上繳包，已提交之歷史紀錄 |
| 文字為對照式（`619 → 627`／`619 版`／`619 或 627`／`619 ＋ 8`） | 不改 | 其為變更之紀錄本身，改之即抹除變更 |
| 位於 `feature.yaml`／`PLAYBOOK.md`／`RUNBOOK.md`／`framework.md` | **須改** | 現行有效之設定／作業文件 |
| 位於 `docs/reports/` | 不改 | 已結案之報告 |
| `RULINGS.md` | 不改 | 條文中引為理由之當時實測值 |
| `ANOMALIES.md`／`DATA_REQUESTS.md` | 不改 | 登記簿，記錄開立當時之事實 |
| `scripts/` 且該行為可執行之常數／斷言 | **須改** | 現行行為據以判定 |
| `scripts/` 之 docstring 或輸出字串 | 不改 | 敘述當時之量測 |

**逐行覆寫**（R-VF18：同一檔內可能兼有兩類，判斷須逐句為之）：

| 檔:行 | 覆寫為 | 理由 |
|---|---|---|
| `feature.yaml` 含 `388/619` 之行 | 不改 | 此行為 **當時之 Sub Categorization 實測**（388/619），非後續作業據以行動之設定值 —— 其所支持之判定（Test Group）已由 R-VF9 裁定，本行僅存為裁定當時之證據。雖位於現行有效之 `feature.yaml`，依 R-VF18「逐句為之」判為歷史紀錄。 |

## 2. 結果：128 處 ／ 27 檔

- **須改 0**
- **不改 128**
- **待人工 0**

### 2.3 不改（逐檔計數）

| 檔 | 處 |
|---|---:|
| `RULINGS.md` | 15 |
| `docs/upstream/vf230/00_intake.md` | 15 |
| `docs/handoff/62_vf230_recon_review.md` | 13 |
| `docs/upstream/V07_review_v06.md` | 8 |
| `docs/upstream/V06_scope_close.md` | 7 |
| `docs/upstream/vf230/01_recon.md` | 7 |
| `docs/upstream/V08_review_v07.md` | 6 |
| `ANOMALIES.md` | 6 |
| `docs/handoff/V06_scope_close.md` | 5 |
| `docs/handoff/V07_review_v06.md` | 5 |
| `docs/reports/vf230_crosscheck.md` | 5 |
| `docs/reports/wvf20_619_triage.md` | 5 |
| `docs/handoff/V08_review_v07.md` | 4 |
| `scripts/vf230_crosscheck.py` | 4 |
| `docs/handoff/V05_scope_and_vcrit.md` | 3 |
| `docs/handoff/V04_numbering_separation.md` | 3 |
| `DATA_REQUESTS.md` | 3 |
| `docs/handoff/63_test_group_ruling.md` | 2 |
| `docs/handoff/V10_four_rulings.md` | 2 |
| `docs/reports/w120_verification_criteria.md` | 2 |
| `scripts/vf230_leaves.py` | 2 |
| `feature.yaml` | 1 |
| `docs/handoff/ZZ_vf230_numbering_collision.md` | 1 |
| `docs/reports/wvf28_disclosure_draft.md` | 1 |
| `docs/reports/vf230_layer2_candidates.md` | 1 |
| `scripts/vf230_layer2.py` | 1 |
| `scripts/vf230_w120_vcrit.py` | 1 |

## 3. 留痕（R-VF18 末段：改與不改皆須留痕）

本表即為留痕。**128 處判「不改」者，其理由逐條見 §1 之規則**；
**0 處判「須改」者逐處列於 §2.1，本輪未改。**

