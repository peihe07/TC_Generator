# W-VF24 —— 收斂為單一套之前置清單（V09 §2）

**只列不改。** R-VF23 第四項：全部檔案搬移與 git 操作屬 Pei，
兩層只備清單，不執行。**本輪未搬移、未改名、未 `git mv`、未刪目錄。**

## 1. 現況（本輪復測，不以 V07／V08 之目錄列表為來源）

- `docs/handoff/` 共 **99** 檔，其中屬 VF230 線 **14**
- `docs/upstream/` 一層共 **49** 檔，其中 `V*` **8**
- `docs/upstream/vf230/` **0** 檔：

**VF230 線之 handoff 逐檔**：

- `V00_numbering_collision.md`
- `V01_vf230_intake.md`
- `V02_vf230_recon_review.md`
- `V03_test_group_ruling.md`
- `V04_numbering_separation.md`
- `V05_scope_and_vcrit.md`
- `V06_scope_close.md`
- `V07_review_v06.md`
- `V08_review_v07.md`
- `V09_feature_identity.md`
- `V10_four_rulings.md`
- `V11_layer2_and_regression.md`
- `V12_layer2_final.md`
- `V13_move_verified.md`

**VF230 線之 upstream 逐檔**：

- `docs/upstream/V01_vf230_intake.md`
- `docs/upstream/V02_vf230_recon.md`
- `docs/upstream/V06_scope_close.md`
- `docs/upstream/V07_review_v06.md`
- `docs/upstream/V08_review_v07.md`
- `docs/upstream/V09_feature_identity.md`
- `docs/upstream/V10_four_rulings.md`
- `docs/upstream/V12_layer2_final.md`

## 2. 兩線同號之殘留（handoff 側）

無。

## 3. 搬移表（供 Pei 逐條核對；**本層未執行**）

| # | 舊路徑 | 新路徑 | 線 | 依據 | 現況 |
|---:|---|---|---|---|---|
| 1 | `docs/handoff/ZZ_vf230_numbering_collision.md` | `docs/handoff/V00_numbering_collision.md` | VF230 | V04 §3.2 | **新路徑已存在，須先確認** |
| 2 | `docs/handoff/61_vf230_intake.md` | `docs/handoff/V01_vf230_intake.md` | VF230 | V04 §3.2 | **新路徑已存在，須先確認** |
| 3 | `docs/handoff/62_vf230_recon_review.md` | `docs/handoff/V02_vf230_recon_review.md` | VF230 | V04 §3.2 | **新路徑已存在，須先確認** |
| 4 | `docs/handoff/63_test_group_ruling.md` | `docs/handoff/V03_test_group_ruling.md` | VF230 | V04 §3.2 | **新路徑已存在，須先確認** |
| 5 | `docs/upstream/vf230/00_intake.md` | `docs/upstream/V01_vf230_intake.md` | VF230 | V09 §1 第四項 | **新路徑已存在，須先確認** |
| 6 | `docs/upstream/vf230/01_recon.md` | `docs/upstream/V02_vf230_recon.md` | VF230 | V09 §1 第四項 | **新路徑已存在，須先確認** |

搬移後另須 **移除空目錄 `docs/upstream/vf230/`**（V09 §1 第四項）。

**Part 1 之 `00_`–`38_` 一律不列入**（V09 §2 第 2 項）。

## 4. 交叉引用（111 處 ／ 27 檔）

- **搬移後須同步更新 17 處**（現行有效之陳述）
- 其餘 **94** 處位於 `docs/handoff/`／
  `docs/upstream/`／`docs/reports/`，依 **R-VF18** 為歷史紀錄，**不追改**

### 4.1 須同步更新者（逐處）

| 檔:行 | 所指 |
|---|---|
| `RULINGS.md:1688` | `vf230/00_intake` |
| `RULINGS.md:2056` | `vf230/00_intake` |
| `RULINGS.md:2238` | `vf230/00_intake` |
| `RULINGS.md:2243` | `vf230/00_intake` |
| `RULINGS.md:2244` | `vf230/01_recon` |
| `RULINGS.md:2260` | `61_vf230_intake` |
| `RULINGS.md:2554` | `vf230/00_intake` |
| `docs/INDEX.md:86` | `61_vf230_intake` |
| `scripts/index_backfill.py:53` | `61_vf230_intake` |
| `scripts/vf230_wvf20_619.py:14` | `vf230/00_intake` |
| `scripts/vf230_wvf24_converge.py:25` | `61_vf230_intake` |
| `scripts/vf230_wvf24_converge.py:27` | `62_vf230_recon` |
| `scripts/vf230_wvf24_converge.py:31` | `vf230/00_intake` |
| `scripts/vf230_wvf24_converge.py:33` | `vf230/01_recon` |
| `scripts/vf230_wvf24_converge.py:36` | `vf230/00_intake` |
| `scripts/vf230_wvf24_converge.py:37` | `61_vf230_intake` |
| `scripts/vf230_wvf24_converge.py:56` | `61_vf230_intake` |

### 4.2 不追改者（逐檔計數）

| 檔 | 處 |
|---|---:|
| `docs/reports/wvf24_converge_plan.md` | 31 |
| `docs/handoff/V07_review_v06.md` | 8 |
| `docs/upstream/35_delegation_reopen.md` | 6 |
| `docs/handoff/V09_feature_identity.md` | 5 |
| `docs/upstream/V07_review_v06.md` | 5 |
| `docs/handoff/V13_move_verified.md` | 4 |
| `docs/handoff/V04_numbering_separation.md` | 4 |
| `docs/upstream/V06_scope_close.md` | 4 |
| `docs/reports/wvf20_619_triage.md` | 4 |
| `docs/handoff/64_review_round40.md` | 3 |
| `docs/upstream/34_redundancy_and_batch15.md` | 3 |
| `docs/upstream/V09_feature_identity.md` | 3 |
| `docs/handoff/V02_vf230_recon_review.md` | 2 |
| `docs/handoff/V00_numbering_collision.md` | 2 |
| `docs/upstream/36_domain_and_anchor.md` | 2 |
| `docs/upstream/V01_vf230_intake.md` | 2 |
| `docs/handoff/V08_review_v07.md` | 1 |
| `docs/handoff/63_rulings_round39.md` | 1 |
| `docs/handoff/V01_vf230_intake.md` | 1 |
| `docs/handoff/V10_four_rulings.md` | 1 |
| `docs/upstream/V08_review_v07.md` | 1 |
| `docs/upstream/V02_vf230_recon.md` | 1 |

## 5. 與併行線之協調點（V09 §2 第 4 項）

`docs/upstream/vf230/` 二檔係**併行線**於 `7a7747e`／`942f0d7` 所搬。
**搬回之衝突點如下，本層不逕行。**

**併行線之檔案已引用新路徑**，搬回將使其引用失效：

- `docs/handoff/64_review_round40.md`

→ **此為實質衝突**：該等檔為 Part 1 線之下放包，依 R-VF18 為歷史紀錄不追改，但搬移後其所指之路徑將不存在。

**兩種處置，本層不擇一**：

1. 搬回並接受 Part 1 下放包內留有失效路徑（與 R-VF18「歷史不追改」一致，代價是連結斷）
2. 不搬回，改令 R-VF23 第四項之收斂方向為 `vf230/`（與 R-VF23 第三項「R-VF10 維持原文」相牴觸）

**另**：本層未查併行線是否有未提交之作業正在動該二檔。
`git status` 於本輪執行時之結果須由 Pei 於實際搬移前復查 ——
**本清單之有效期止於下一次併行線提交。**

