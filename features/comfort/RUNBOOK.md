# FW036 Comfort HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Comfort.

Comfort 之裁決基線：**SR24 CR24879**（R-C1）。SR25 CR29359 為 out-of-scope
參考資料，**不得作為查得依據**。全部條文見 `RULINGS.md`；往返序見
`docs/INDEX.md`。

## Phase 0 — Intake  ✅ 2026-08-14
- [x] Source files placed in `inputs/`：037 + 036 空白範本（BLANK，取自
      `forms/`）。SR24 spec 三件**不搬移**，留在 `spec-index/`，
      `feature.yaml` 以 `../../spec-index/…` 回指。popup list 無（null）
- [x] spec_mode classified: **A**（SYS1 export 齊備）。intake 第一次跑提 `E`，
      因其只掃 drop folder —— 見 A-CF04
- [x] `feature.yaml` filled：含 `recon_assertions`（R-C3／R-C4 之機械期望值）
      與 `spec_reference_template`（SR24 全名 stem，R-C1）

## Phase 1 — Recon (Tier 1, fully delegable)  ✅ 2026-08-14
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: **BLANK**（done 0 列／draft 2 列，皆範本樣本，A-CF07）
- [x] Coverage: **403** leaves total / **0** done / **403** regen targets
- [x] Assertions（PASS/FAIL + 實測值，非僅印計數）：
      leaf 403 **PASS**；相異 section 129 **PASS**；citation stem 唯一且為
      SR24 **PASS**；129 節對 SR24 outline 查得 miss=0 **PASS**
- [x] outline map：`data/spec_id_to_outline.tsv`（403 列，追蹤入版控）

指令：
```
python3 scripts/new_feature.py Comfort --adopt-existing --root .
python3 scripts/intake.py  Comfort --root . --scaffold
python3 scripts/recon.py   --feature features/comfort --root .
```

## Phase 2 — Rulings (Tier 2)
- [x] 執行層覆核完成 2026-08-14 —— 9 個 `[PROPOSED]` 逐項意見見
      `docs/upstream/02_phase2_review.md` §7
- [ ] **DECISIONS.md signed by Pei** —— Sign-off 仍為空白範本，
      recon 每次跑都會發 R-C10 警告，屬正確狀態
- [x] 51 節分類（A-CF08）：`data/sr24_uncited_sections.tsv`，
      container 20／assumption 9／figure 5／**substantive 17**
- 已凍結、**不在簽署範圍內**者：`test_group` = `Comfort`（R-C6）、
  `tc_id` = `NR1L-ComfortHMI-{NNN}`（R-C7）、baseline = SR24（R-C1）、
  UI label 拼寫依 SR24（R-C2）、leaf 判準（R-C3）
- open PENDING：**無**
- **待裁 2 項**（上繳 02 §0）：甲 R-C5 與 SR24 基線之 16 節重疊；
  乙 04 §2 前提訂正

指令：
```
python3 features/comfort/scripts/classify_uncited_sections.py
python3 scripts/recon.py --feature features/comfort --root .
```

## Phase 3 — 進場前之未決事項（本包記入，勿留到當下決定）
**Phase 3 未開始。** 切分母體現況：403 leaves 確定 ＋ 10 節待 D-C10
＋ 7 節待缺料（DR #6／#7）。

- [x] 甲項已由 **R-C5-1** 處置 —— 16 節退出 R-C5，併入 A-CF08
- [x] 17 節適用性判讀完成 —— `data/sr24_substantive_applicability.tsv`，
      10 `in_scope`／7 `undetermined`／0 `out_of_scope`
- [ ] **D-C10 裁定** —— 10 節 `in_scope` 者之處置。**宜待 A-CF12 釐清**：
      該判定繫於「採 CFTS043 結構化欄位而非其散文 NOTE」之選擇，
      NOTE 若有效則 10 節全部翻面（DR #8，單一問句可解）
- [ ] **DR #6／#7 落位** —— 7 節 `undetermined` 之解除條件
- [ ] **exemplar source 具名** —— 提案寫「nearest sibling done region」，
      但時序最近的 privacy／sxm 皆 BLANK 無 done region；實有者為
      home（144 列）與 amfm（158 列，其需求族已被裁決取代，僅可借樣式）
- [ ] **A-CF07 之寫回處置須於 profile 明文**（下放包 03 §5）——
      BLANK 型 write-back 為「append from first data row」，範本殘留列
      會位移首資料列
- [ ] **batch plan 改寫** —— 現提案「依章分組，pilot 取最小」會選到
      第 6 章 1 個 leaf；且章 2（92）與章 16（99）佔 47%，其切分應由
      Part N 決定而非沿用依章

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
