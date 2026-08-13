# FW036 SXM HMI — TC Generation Runbook

> **2026-08-11: directory moved `SXMHMI` → `features/sxm`.** Repo-wide reorganisation —
> all features now live under `features/`, lowercase and without the HMI
> suffix. Path strings in the body below are NOT rewritten: they are dated
> records, and they record what was true when they were written (same
> convention as the 2026-08-10 `AMFMHMI` → `AMFM` rename). Read any
> `SXMHMI/…` path in this file as `features/sxm/…`. `feature.yaml` paths are
> relative to the feature directory and were not affected.

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to SXM.

## Phase 0 — Intake
- [ ] Source files placed in `inputs/` (workbook, 037, spec, popup list)
- [ ] spec_mode classified: ___  (FEATURE_ONBOARDING §3)
- [ ] `feature.yaml` filled from `docs/fw036/templates/feature.yaml`

## Phase 1 — Recon (Tier 1, fully delegable)
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [ ] workbook_state: ___
- [ ] Coverage: ___ leaves total / ___ done / ___ regen targets

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_SXM_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [x] Batches generated → lint green → write-back invariants pass
      B1–B14, 202/202 leaves, 215 TCs, lint 0 findings, 952 tests

## Phase 7 — Delivery (Tier 3)
- [x] Release tag (xlsx SHA256 ↔ commit)
- [x] Submission drafted — `docs/fw036/RD1_sxm_submission.md`
- [ ] **RD-1 sent** — off-repo, Pei to send. Two documents go together: the
      SXM submission above and the AMFM one (`RD1_amfm_submission.md`), which
      gained an F5 FYI line about the TC ID prefix change and cannot be sent
      as previously reviewed.

## Close-out (2026-08-12)

**Tag `fw036-sxm-v1` on `3d6adb0`**, annotation from
`features/sxm/docs/tag-annotation-sxm-v1.txt`.

| | |
|---|---|
| output | `FM-WI-FSM-036-A01 …_SWQT_SXM_20260810.xlsx` |
| SHA256 | `7b6e760d524fb79e3e4f7cafb43be4b2c945d64b9063abb3974a5e9737538a02` |
| rows | 0 preserved / 215 new / 0 placeholder; rows 10–224 |
| coverage | 202/202 leaves, exact set equality |
| priority | P0=22 · P1=181 · P2=12 |
| form | revision C, ChangeHistory revision D |
| repo state | lint 0 findings · 952 tests |

> **The command below is a dated record, not the current one.** It produced
> the original delivery through openpyxl's save path; that path was
> quarantined under R20-3 (2026-08-13) and the quarantine was **lifted the
> same day** once the writer moved to `backend/xlsx_surgical.py`. The command
> string is unchanged, but what it now does is not what it did here — the
> current output is the **v2** described in the addendum below, not the
> `7b6e760d…` file this block records. See A-SX28 / A-SX29 / A-SX30.

**Re-running the delivery requires `--date 2026-08-12`.** Without it the writer
falls back to `date.today()`, the ChangeHistory date moves and the output hash
drifts daily — the reproducibility claim is void unless the flag is given.
This precondition is specific to SXM; the AMFM annotation carries no equivalent.

```
python features/sxm/scripts/write_back.py --feature-dir features/sxm \
  --date 2026-08-12 --write
```

The annotation records `produced at: da8b38e` while the tag sits on `3d6adb0`.
Both are correct and neither needs changing: `da8b38e` is the commit the
delivered file was actually written from, and it is a **docs-only** descendant
of `3d6adb0` — `git diff 3d6adb0 da8b38e -- features/sxm/generated
features/sxm/feature.yaml features/sxm/scripts` is empty, so the tagged commit
re-derives the same bytes. This mirrors the AMFM annotation, which records a
producing commit (`bf514e2`) and a second verification at a later one.

## Addendum (2026-08-13) — 交付件滅失與重產

原交付件（148,734 B，SHA256 `7b6e760d…`）於清理作業中連同
`inputs/`、`output/` 一併誤刪。三者皆為 `.gitignore` 排除項，**未進入
任何 git 物件庫**，本機與 remote 均無副本，亦無 APFS snapshot 或
Time Machine。**原件永久滅失。**

`git restore features/` 救回全部受追蹤內容：202 個 `generated/*.json`、
所有 `.md`、`scripts/`。來源檔自 repo 外復原並驗證雜湊（空白範本
`cd876c20…`、CFTS024 reqifz `325dba60…`、docx `e5c12e9e…`，皆與
`feature.yaml` 記載相符），`build_stla_map.py` 重建 `data/` 四檔。

| | 原交付件 | 重產件 |
|---|---|---|
| SHA256 | `7b6e760d…`（已無對應實體） | `206a8dd2…` |
| bytes | 148,734 | 148,714 |
| rows / coverage / priority | 215 · 202/202 · 22/181/12 | 相同 |
| ChangeHistory | revision D | revision D |
| lint | 0 findings | `PASS — no findings` |
| 結構缺損 | lost 11 / added 10 · x14 DV 2 → 0 | 逐項相同 |

內容層不變量全數相符，結構缺損未加重亦未修復。**雜湊差異 20 bytes
未能歸因**（已排除 `stla_to_cfts.json`、來源 workbook、`--date`、
程式碼；兩次執行結果一致，具確定性）。

重產過程違反 R20-3 隔離令與 R18-1 不重產令，**已裁定保留此檔**
（Pei, 2026-08-13）。完整登記見 **A-SX29**。

### v2（2026-08-13）—— Test Item 修正與結構修復

同日再次重產，起因為 Test Item 缺 scenario tag（**A-SX30**）：
`tc_title` 215 筆全數生成卻從未寫入任何欄位，I 欄僅 6/215 帶 tag。
依 R18-1 判準 1（內容正確性受影響者必須重產）裁定重產，
格式定為條文 + 空行 + `(自己產出的 tag)`。

writer 同時遷至 `backend/xlsx_surgical.py`（R18-3 rule 1），
**A-SX28 的結構缺損因此一併修復**——正是該條 DEFERRED 所等待的時機。

| | 原交付件 | 重產件 v1 | **v2（現行）** |
|---|---|---|---|
| SHA256 | `7b6e760d…`（已滅失） | `206a8dd2…` | **`a332a700…`** |
| bytes | 148,734 | 148,714 | 115,222 |
| zip members | 47 | 47 | **48**（= 客戶原件） |
| x14 DV | 0 | 0 | **2**（R 欄下拉復原） |
| LOST / ADDED | 11 / 10 | 11 / 10 | **0 / 0** |
| I 欄帶 tag | 6 / 215 | 6 / 215 | **215 / 215** |
| lint | 0 findings | PASS | PASS |
| 測試 | 952 | — | 944 passed / 15 skipped |

現行重跑指令（writer 已非 openpyxl save 路徑）：

```
python features/sxm/scripts/write_back.py --feature-dir features/sxm \
  --date 2026-08-12 --write
```

tag `fw036-sxm-v1` 之處置仍**未裁**——該 tag 記載的 `7b6e760d…`
已無對應實體，而 v2 為第三個雜湊且內容已變。在裁定前
v2 不得視為 `fw036-sxm-v1` 之交付物。見 A-SX29 PENDING 標的。

Still owed after this: RD-1 sending (above), and the two post-delivery canon
items — A-SX27 (framework Part IV `Source Availability` Set name vs its
content) and the `<Feature>HMI` scaffold convention in
`docs/fw036/templates/PLAYBOOK.md`, whose stale pointers already materialised
in `features/projection/PLAYBOOK.md`.
