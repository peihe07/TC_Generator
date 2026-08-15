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
- [x] **DECISIONS.md signed by Pei** ✅ 2026-08-14（PeiPYHsu）——
      受 **R-C9** 保護：recon 重跑拒絕覆寫、改寫 `DECISIONS.new.md`、非零離開
      （實測 sha256 前後不變、exit=1）。R-C10 空簽署警告已停止
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

## Phase 3 — Framework & profile（**Part N 完成**；profile 仍未定）

**Layer 3 map 已產；Layer 2 待分析層起草（Tier 2）。**

切分母體：**403 leaves 確定**。17 節 in-baseline substantive **不入母體** ——
4 節依 R-C16 為 RD-1 覆蓋缺口項、10 節 DEFERRED、3 節待 DR #6；但其所屬
章節須留為可插入之邊界（07 §5）。

### 已完成
- [x] 甲項已由 **R-C5-1** 處置 —— 16 節退出 R-C5，併入 A-CF08
- [x] 17 節適用性判讀 —— `data/sr24_substantive_applicability.tsv`（六欄）。
      **4 `in_scope`／13 `undetermined`／0 `out_of_scope`**
      - `in_scope`：16.1、18.2、18.3、18.4 —— 依 037 引用結構
        （ch16 引 18/19 得 99 leaves；ch18 引 18.1 得 3 leaves）
      - `undetermined`：20.1 ~ 20.4.3（DEFERRED）、19.1 ~ 19.3（DR #6）
- [x] **DR #8 轉 DEFERRED**（10 §2）—— Pei 直接向 RD 反應。依 R15-2 自
      open PENDING 與「阻塞 D-C10」清單移除。20.x verdict **不因此變動**
- [x] **四節處置已定**（R-C16）—— 16.1、18.2~18.4 為 **RD-1 覆蓋缺口項，
      非 TC 工作項**：不入分母、不列 BLOCKED、不指派 tc_id，待上游 037 補分析
- [x] **Layer 3 map** —— `data/layer3_map.tsv`，129 節 × 六欄，三個 assertion
      全 PASS（403／129／逐章分布）。結構事實：section ↔ parent 為 **1:1 雙射**

```
python3 features/comfort/scripts/build_layer3_map.py
python3 features/comfort/scripts/verify_partn.py
python3 features/comfort/scripts/build_section_fulltext.py
python3 features/comfort/scripts/gate_g1_test_item.py
python3 features/comfort/scripts/prepare_workbook.py --write
shasum -a 256 -c BASELINE.sha256                      # 自 features/comfort/
shasum -a 256 -c --ignore-missing DELIVERY.sha256
```

### 交付完整性台帳（profile §6）
- `BASELINE.sha256` —— **8 檔**：inputs/ 5 檔 ＋ spec-index/ 之 SR24 三件。
      涵蓋 spec-index 之理由：R-C11 把 spec 移出 inputs/，而
      `.gitignore:58` 使該處同樣不入版控 —— 若不列入，R-C11 之副作用即為
      「唯一 spec 來源脫離雜湊保護」。**此為執行層判斷，非裁決**，可駁回
- `DELIVERY.sha256` —— append-only，ENTRY 001 = 範本清列

### 待辦（Layer 2 屬 Tier 2，執行層不自裁）
- [x] **Layer 2 Test Set（Part N）** ✅ 已簽署 2026-08-14（下放包 12），
      **兩次修正 2026-08-15**（13 §2 更名、14 §1 四節改置）——
      Test Group `Comfort`、**15 個 Test Set**、leaf 區間 **14–59**（最大 14.6%）。
      落地 `framework.md`；`verify_partn.py` **七項** assertion 全 PASS。
      **Sign-off 未重簽**（結構未變，14 §5）
- [x] **6.3 落位確認**（12 §3）—— 讀全文後**維持 `Front Climate Anatomy`**。
      原疑慮「second row」係 60 字截斷把 `secondary` 腰斬所致；全文為
      `non-foldable secondary lower screen`，與後座無關。**未自行搬移**
- [x] 章 2／16 逐條覆核 —— **11 §1 裁定不做**：兩章不合併（進入路徑不同），
      該覆核不在 Part N 關鍵路徑上；鏡像即使個別條文對不齊也不失效
- [x] **邊界預留（07 §5）** —— 章 20 若日後 in_scope → **新增** Test Set
      `Rear Blower`（不併入 #6，進入路徑與市場變體不同）；章 19 → 併入 #15
      `Home Screen Widget`。**兩處皆不需重整既有切分**（framework.md §7）
- [x] **exemplar source 已具名** —— `home` 之 done region（144 列）；
      **`amfm` 具名排除**（DECISIONS §4，已簽）
- [x] **A-CF07 之寫回處置已於 profile §0.1 明文**（03 §5）——
      清 D10/F10/G10/S10/D11 五格、B 欄不動、不刪列。已執行，待 Pei 確認
- [x] **batch plan 已定** —— pilot = 第 13 章 `Seat Control Tab`（14 leaves）；
      其餘批次依 Part N 之 15 個 Test Set，不再「依章分組」（DECISIONS §7，已簽）
- [ ] **DR #6** —— 僅剩 7" 螢幕配置一題（擋 19.1 ~ 19.3）。09 §5 已改為
      **請 Pei 直接指認來源**；10 §3 之 Home Screen spec 亦不關閉本項
- [x] Part N 落地 —— 寫於 **`features/comfort/framework.md`**（feature 內）
- [x] **profile `[OVERRIDE]`** ✅ 已簽署 2026-08-15 ——
      `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`

### Phase 4 開始條件（16 §3.2）—— **三者皆備方可產第一條 TC**
- [x] **profile `[OVERRIDE]` 已簽署 2026-08-15**（15 ＋ 16 §1）——
      落地 `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。
      A-CF07 之寫回處置已於 §0.1 明文（03 §5 之要求已滿足）
- [x] **G-1 PASS 2026-08-15** —— `scripts/gate_g1_test_item.py`。
      home done region 144 列，**143 含 modal（99.3%）**，長度中位 273，
      形態 `The system shall …` ＋ 情境括號，與 profile §3.1 一致。
      **附 provenance 但書**：量測對象為 `forms/…_Home_20260809.xlsx`
      （`1895fb2a…`），非 home RECON 所測檔亦非 Home v2，兩者皆不在 repo
- [ ] **⏳ A-CF07 清列經 Pei 於 Excel 確認四項** —— **唯一未達成者**。
      prepared workbook 已備：`output/…_Comfort_20260815_prepared.xlsx`
      （`b68117a2…`）。待確認：無修復提示／R 欄下拉九項可用／D5 Scope 正確／
      第 10–11 列已清且無殘留列號。**程式層檢查不能代替 Excel 自身之判定**
- [x] **ch11／ch12 複核完成 2026-08-15 —— 合併維持** —— 分析層裁定：
      同一進入路徑，`opens popup` 為輸出回饋非入口。依據寫入
      `framework.md` §3.1.1。`Heated Vented Seats`（59）維持單一 Test Set。
      **Phase 4 注意**：該差異應以**預期結果**（是否出現 popup）表達，
      不得寫成不同的操作步驟或前置條件
- [x] **129 節全文已抽出** —— `data/section_fulltext.tsv`，四個 assertion 全 PASS

### Phase 4 前置（本包記入，勿留到當下決定）
- [ ] **Home Screen spec 通讀** —— R-C17 之判定測試（該規則定義於 Comfort
      或 Home Screen？）須逐條施行，只查過三處不足
- [ ] 引用 Home Screen spec 時比照 R-C11 **寫全名** ——
      `spec-index/cache/` 同時存有其 **SR25** 版（R-C17 指名 SR24 Post 2A）
- [ ] ch16 之 TC 以 **outline 節次**為 traceability 依據，不用條款標籤
      —— `C16.)` 被 2.15 與 16.17 共用（A-CF13）
- [ ] **一律讀 `section_fulltext.tsv` 之全文**（R-C18），不得以
      `layer3_map.tsv` 之 60 字 `section_title` 做任何判斷
- [ ] **R-C19 —— ch11／ch12 之差異以 `expected_result` 表達**（是否出現
      popup），**不得**寫成不同的 `test_procedure` 步驟或 `pre_conditions`。
      pilot review 時違反者列為 **defect**（非 style-divergence）
- [ ] **`2.6.1`／`2.11`（及 `16.6.1`／`16.11`）須一併閱讀對造節**（14 §2）——
      兩節內容重疊卻分屬 `Temperature and Fan` 與 `Climate Modes`，
      siblings 不相鄰。依 §4.6 作 sibling 判定，必要時輸出 `duplicate_of`。
      若顯示確不應分置，屬 Part N 變更，回分析層重簽
- [ ] `12.1` 之 `LEDs (.` 為 spec 原文之孤立左括號（A-CF13 第四項）——
      逐字引用時**照錄或明示節錄，不得靜默修正**（§8.4.2）
- [ ] `14.19` 之 8 leaves 對應條文之 8 個 bullet，逐項一一對應；
      `-02` 含 variant 分歧（`show for R1Low, do not show for R1H`），
      §8.7.3 variant label 可能適用（上繳 07 §5）
## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent

---

## 判準 vs 用詞禁令（22 §4，2026-08-15 記入）

> rev1 是 `is readable`，rev2 是 `is recorded`，兩者都把主詞放在觀察者身上。
> rev2 改的時候，以為問題是「readable 這個字」，實際問題是「ER 的主詞是誰」
> —— 換字沒有換主詞，所以錯誤原樣搬了家。
> **用詞禁令我可以繞過而不自知，判準不行。**

與 **R-C13**（零命中須換路徑而非下結論）、**R-C18**（截斷欄位不得用於判讀）
同源：**以表徵為判準者，其失敗形態是靜默的。**

實務上之兩條推論：

1. **寫 gate 時，先問它檢查的是表徵還是判準。** 檢查表徵者（禁某字、
   數某數）能擋住重複同一個字面錯誤，擋不住同一個判斷錯誤換個寫法。
2. **改動點不等於審視點。** rev2 親手改過的那幾行 ER 仍帶 `is recorded`；
   TC-014 之 PC 區塊因 rev2／rev3 皆未改動而三輪未被重讀。
   前者是「改過所以以為看過」，後者是「沒改過所以沒看」——
   兩者都不是「看過而判斷錯」。
