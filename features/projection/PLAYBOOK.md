# PLAYBOOK — Projection (FW036 TC Generation)

Copied into every feature directory by `new_feature.py`. This is the
OPERATIONAL view: who does what, in which tool, with which handoff
artifacts, and the core TC-production loop. Rule authority stays with
`docs/fw036/FEATURE_ONBOARDING.md` (phases, tiers, workbook_state,
spec_mode) and the generic instruction + feature profile — on any conflict,
those win. Check off and annotate this file as the feature progresses; it
doubles as the feature's status board.

---

## 0. The working model

**Analysis happens in the Claude Project (chat). Execution happens in
Claude Code.** The two never blur:

- Chat is where evidence is weighed, options are surfaced, and Pei rules.
  Nothing in chat writes the workbook.
- Claude Code is where scripts run, files change, and gates enforce.
  Nothing in Claude Code rules on scope, style authority, or anomaly
  dispositions — it registers and proposes, then continues unaffected work.
- Every handoff is a FILE, not a memory: chat's output is signed
  documents (DECISIONS, RULINGS, profile, digests recorded into
  ANOMALIES/RUNBOOK); Claude Code's output is generated artifacts plus
  reports (RECON, lint_report, dry-run summary) that come BACK to chat for
  the next ruling. If it wasn't written down, it didn't happen.

## 1. Flow at a glance

```
 CHAT (analysis)                      CLAUDE CODE (execution)
 ──────────────────                   ──────────────────────
 P0  dump files, read INTAKE.md   →   intake.py [--scaffold]
 P1                                   recon.py → RECON + DECISIONS(pre-filled)
 P2  rule on [PROPOSED]/[PEI],    →
     sign DECISIONS
 P3  draft framework Part N +     →   (commit docs)
     profile with Claude, approve
 P4                                   adapt scripts per feature.yaml,
                                      build data artifacts
 P5  review pilot digest in chat, →   generate PILOT batch only, report
     rule corrections
 P6                                   remaining batches → lint green
 P7  review dry-run summary,      →   commit → --write → tag
     approve --write;
     draft RD-1 with Claude;
     submit (Pei only)
```

Chat touchpoints are exactly five: DECISIONS sign-off, framework/profile
approval, pilot review, dry-run approval, delivery. Everything else runs in
Claude Code without asking — bounded by the six stop conditions (canon §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_projection_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (canon §6) — a summary missing a field is returned, not approved

## 3. The TC production loop (P5/P6 core, one parent per turn)

For each requirement parent, in 037 document order within its batch:

1. **Read** the parent's literal text + its batch context (spec sections,
   sibling rows including the done region, exemplars, popup/table rows)
2. **Scope** — before writing anything: check sibling reqs (do not absorb
   what a sibling owns, §8.2.1); check external references (do not absorb
   other specs' rules, §8.4.2); check the RD sub-id structure (one sub-id
   may need several TCs, §8.2.2 — never the inverse)
3. **Split** along genuine axes only (trigger / input / boundary / mode /
   environment, §8.3); one verification objective per TC (§5.7): one
   trigger's consequential outcomes = one TC with multi-line ER
4. **Write** fields per the generic instruction + profile overrides;
   reuse standard snippets verbatim; every literal (label, number, popup
   text, state name) traces to THIS feature's spec — cross-feature
   exemplars lend shape, never facts
5. **Reason** (繁中, 2–5 sentences): objective, key conditions, why this
   split, what was deliberately delegated and to whom
6. **Self-check** against the §9 list; emit; the generator assigns TC ids
7. On anything the sources don't state: `[ASSUMPTION A-PRnn]` marker +
   ANOMALIES entry, or BLOCKED placeholder — never a fabricated value

Placeholders keep the leaf's row (completeness invariant, both
directions): requirement sentence as Test Item, `BLOCKED - see Remarks`,
Remarks = reason + anomaly id.

## 4. The rules that never change per feature

- Three-layer quality: lint (mechanical) → human pilot gate (judgment) →
  done region arbitrates disputes with evidence. Lint-green ≠ done; a
  reviewer finding isn't a defect until it survives the done-region check.
- Done region is style authority, never factual authority; frozen
  byte-for-byte under the state-appropriate hash invariant.
- Write-back invariants abort, never warn; weakening one is a chat ruling.
- Sequence at delivery: dry-run reviewed → clean-tree commit → `--write`
  (touches no tracked file) → annotated tag `fw036-{feature}-regen-vN`
  carrying xlsx SHA256 + done-region hash + row summary + lint result.
- The workbook Scope field is the workbook's identity claim — verify it
  matches the ruled requirement source at intake AND before submission
  (two independent features had it wrong in one week).
- RD-1 at delivery: systemic classes first with class-level remedies;
  every item = anomaly id + evidence + local disposition + requested
  action; the feature never waits on answers.
- What VARIES lives only in `feature.yaml` (paths, columns, done-region
  rule, spec_mode, reference template, lint vocab) and the profile
  ([OVERRIDE]/[ADD] clauses citing what they displace). Scripts are
  copy+yaml, no shared library (canon §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `projectionHMI/PLAYBOOK.md`、`projectionHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`projectionHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Projection

`workbook_state = FULL_REFINE` (profile §1). This feature does not follow the
generic P4→P7 regeneration arc: there is nothing to regenerate. P4 onward is a
**refinement** pass over 559 existing rows plus a small append.

- [x] **P0 intake complete** (2026-08-11)
- [x] **P1 recon complete** (2026-08-11) — 12 項預驗不符全數上報，未自行調和
- [x] **P2 rulings landed** (2026-08-12，含補裁)
  - R-P8′ + R-P11 … R-P20 逐字入 `DECISIONS.md` §0.1；R-P6 / R-P8 標
    `SUPERSEDED`，原文保留供審計軌跡
  - 素材補入 7 件（R-P16 / R-P17 / §6.4），hash 無衝突，異 hash 分支未觸發
  - lint gate 修正 4 條：L-PJ2（值域改對 PROXI）、L-PJ4（窄口）、
    L-PJ6（詞界）、L-PJ7（證據綁定）
  - PCTS 實機取證完成：2 confirmed / 3 partial / 1 not_found
  - 補裁六項落檔（`DECISIONS.md` §0.2）：RD-1 列號定為實體列 434/435/520、
    A-PJ20 不指定 V59/V8、A-PJ21 不指定 V45、MT1/D5/WP43 併入首次實跑回填、
    SYS1 匯出追認留用（A-PJ23）、A-PJ06 抽出為獨立分析輪
  - R-P21 / R-P22 落檔（§0.3）：DR#4 重開並更名「HUIG 4.5 規格本文」，
    `HUIG 4.5.pdf` + `SYS1_HUIG4.5.xlsx` 補入（hash 全同，未觸發停下分支）
  - A-PJ22（規則設計缺陷，歸屬分析層）、A-PJ24（HUIG 缺件曾被 SYSRA 誤代）落檔
  - Anomaly 收斂：**17 CLOSED、1 RETRACTED、6 PENDING**（登記 24 條）
  - DR 收斂：**5 CLOSED、2 撤銷、4 OPEN**（#4 曾重開又關閉）
  - **仍未動任何一列 TC**
- [x] **P3 framework Part V 落檔**（2026-08-12）—— 分析層起草可簽版，執行層
      照抄至 `docs/fw036/framework.md`（第 553 行起），並追加 §N.7 記錄 HUIG
      推導結果與一項數字修正
- [x] **P3 framework Part V 定案**（2026-08-12）—— Layer 2 收斂為
      **16 乾淨 + 1 橫切（Performance）+ 1 綑綁（HMI Display）**；A-PJ06 關閉。
      Layer 3 雙閘門結構（結構 R-P29 機械 / 語意 R-P23·R-P32 人工）寫入 §N.3
- [ ] **P3 profile approved** ← **當前關卡**（profile §3d 須同步 Part V 定案）
  - **A-PJ06 三層框架：分析完成，待 chat 出可簽版**。R-P23（Layer 3 五碼 +
    version-track）、R-P24（相鄰性判準）已裁准並寫入 profile §3d。
    Layer 2 判定：**15 乾淨 + 1 橫切（Performance）+ 1 待拆（HMI Display）**；
    `Device Manager` 經切法驗證判定不綑綁（共享 UI 入口 96%）
  - profile 已依 §5 全數修正 + 補裁回寫，待核
  - **framework 的正題 A-PJ06 已抽出為下一輪獨立分析**（補裁 #6）：
    10 個 Test Group × 18 個 Test Set 攤開，比對 spec 目錄與 037 分組，
    出三層框架提案。理由是 Test Group 一旦要動就牽動 559 列的既有執行紀錄
    （Pass 67 / Fail 34 / Block 3 / NA 90，跨五個 build），越晚處理成本越高
- [ ] P4 data artifacts built
  - `data/signal_map.json` ✅（未解析僅剩 1 個 token）
  - `data/pcts_evidence.json` ✅（14/23 列解鎖）
  - 尚缺 spec 條款索引 —— CFTS085 473 列、CarPlay Addendum R10 82 列、
    Projection Device HMI (May 3 2023) 116 列
- [x] **P4/P5 pilot 產出**（2026-08-12，R-P34）—— `Vehicle Signal Forwarding`
      22 列：**修訂 13、依規則不得動 8、手冊核實無誤 1**。lint 全跑：L-PJ1 /
      L-PJ2 / L-PJ3 / L-PJ4 / L-PJ6 / L-PJ7 全通過；**L-PJ5 殘留 1**（r230，
      查無 spec 依據，A-PJ34）。**本專案第一次修改 TC 內容**
- [x] **P5 pilot reviewed**（2026-08-12）—— verdict: **條件 PASS**；
      D-1（r167/168 步數破壞 1:1 對齊 + 前向引用）已修，複驗 22/22 通過。
      新增 **L-PJ8**（步數對齊）；R-P36 ~ R-P38 落檔
- [ ] **P6 批次（B2–B14，536 列）** —— 計畫已定（風險遞增排序）
  - [x] **B2 Day/Night Mode 22 列**（2026-08-12）：22 列全改，lint L-PJ1~L-PJ8
        全通過；`$Day_Night_Mode$` → `BCM_FD_27.DAY_LGT_MD_DISP`（24 處 L-PJ1
        解析成功）。修正 **L-PJ5 詞界缺陷**（A-PJ38）。r177/r188 之回頭指涉
        依 **R-P39 已還原** —— 交叉指涉不構成缺陷。**verdict: PASS**
  - [x] **B3 Apps+Coex+USB+Performance 30 列**（2026-08-12）：改對了 1／
        核實無誤 22／正確地不動 7。lint L-PJ1~L-PJ8 **0 命中**。
        ⚠️ **gate 充分性評估發現 12 列「gate 未命中但不可執行」，超過 §6 之
        3 列門檻 → 升級 chat 覆核，B4 暫停**（A-PJ39 / A-PJ40 / A-PJ41）
  - [x] **B4 Voice Recognition + Pairing 34 列**（2026-08-12）：改對了 1／
        核實無誤 28／正確地不動 5。ABORT 級 gate 全通過；**新 gate L-PJ9/
        L-PJ10 零命中對照成立**（原樣式 0 誤報）。27 列 PJHMI 引用全為
        `(May 3 2023)`，與 R-P17 一致。新開 A-PJ42/43/44
  - [⛔] **B5 Knob 42 列（2026-08-12）：BLOCKED**。三項檢驗中 token/CAN 全對、
        L-PJ11 人工檢核完成（14/14 一致 → 慣例，L-PJ11 不成立），但
        **L-PJ2 值域檢驗全數不合格** —— 7 個 PROXI 值皆為測試矩陣車型代號，
        無一在列舉內（**A-PJ45 停下條件 / DR#14**）。42 列維持不動待裁
  - [x] **B6 Projection Detection 49 列**（2026-08-12）：**核實無誤 49／
        改對了 0／正確地不動 0**。lint 全綠（L-PJ9/L-PJ10 亦 0）。
        profile §4 之 `Projection_Mode_Selection = 0` 陷阱註記**首次實地檢驗，
        本簿 4 列用法全部正確**
  - [x] **B7 Disconnection 49 列**（2026-08-12）：核實無誤 48／正確地不動 1
        （r36，A-PJ40 佔位符）。**R-P39 首次大量遭遇：11 列回頭指涉全部未動** ✅
  - [x] **B8 Device Manager 54 列**（2026-08-12）：**改對了 2**（r89/r98
        `Check whether` → 依該列自身 `Read the …` 慣例改寫，判準留在 ER）／
        核實無誤 52。**A-PJ48：執行端掃描漏 `re.I`，被下放包預期值攔下**
  - [x] **B9 Connection 61 列**（2026-08-12）：改對了 3（r270/271/272 token
        名稱層級更正）／正確地不動 1（r267 WP43 partial）／核實無誤 57。
        **L-PJ7 首次雙分支檢驗：放行與攔阻各一，皆正確** ✅。
        R-P49 之 `lint_defs.py` 單一實作啟用，八項基線重現
  - [x] **B10′ 機制批 48 列**（2026-08-12，R-P50 合批）：改對了 21／
        正確地不動 17／核實無誤 10。含 L-PJ4 窄口 6 列、PROXI 品牌 12 列、
        VF176 5 列（R-P51 後解析成功）
  - [x] **B11′ 清查批 147 列**（2026-08-12）：**核實無誤 147、變更 0**。
        §3.4 防呆：機制洩漏 **0** 列 ✅
  - **Phase 5 修訂完成**（B5 42 列除外）

### 進度（每輪自總量重算，A-PJ51 / canon §5a 第十條）

```
總資料列                     559
r562 殘樁（R-P19 刪除）       −1  → 558
已修訂完成                    516   （B1–B4, B6–B10′, B11′）
B5 阻塞（DR#14 (b)）           42
                           ─────
校驗                516 + 42 = 558 ✅

累計變更                       63 列（佔已完成 516 之 12%）
```

- [x] **Phase 6 dry-run 首次執行**（2026-08-12，R-P53）：**FAIL**。
      D-3／D-5 PASS；D-4 FAIL（r562 刪除使 `SWE1-PROJ-227` 失去追溯）；
      D-1／D-2 條件與 R-P12 窄口衝突；§3 兩項不符。報告見
      `docs/dryrun_report.md`，六項待處置

**剩餘阻塞：DR#14 (b) + dry-run 六項待處置** —— Atl-Mid 車型是否在 SWQT 範圍內。—— **B6/B7 之 PROXI 經查為不同型
        （`Projection_Mode` / `Wi-Fi_Cfg` / `USB_Presence`），全部可在 HDCC27
        檔內解析，不受 A-PJ45 牽連，可照常開批**
- [ ] P6 all batches refined; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____

### PCTS 取證結果（R-P11）

| 測項 | status | 服務列 | 解鎖 |
|---|---|---|---|
| `C2 - Confirm HU Vehicle Information` | **confirmed** | 13 | ✅ 全解 |
| `NavigationStatusTests`（N1, N3, N5–N17） | **confirmed** | 5 | ✅ 僅 row 371（餘 4 列環境阻塞） |
| `MT1 - Microphone Sensitivity` | partial | 2 | ❌ |
| `D5 - Confirm HU Displays 24-Bit Color` | partial | 1 | ❌ |
| `WP43 - Verify MD can start wireless projection` | partial | 1 | ❌ |
| （無編號）video / display configuration | **not_found** | 1 | ❌ |

**23 列中解鎖 14 列。** workbook 所稱的 N 編號範圍（N1 / N3 / N5–N17）與 app
內實際清單**逐項相符**。三項 partial 缺的都是測項頁內才看得到的操作細節，
需人工確認補足（DR#11）。

### Open PENDING rulings

| # | 待裁 | Anomaly | 影響 |
|---|---|---|---|
| 1 | **pilot review** —— 13 列 diff 待 Pei 逐字看，特別是 r151/152/167/168 | — | Phase 5 放行 |
| 2 | **A-PJ34** —— r230 是否改以整車配置文件為核對對象 | A-PJ34 | 1 列 + L-PJ5 殘留 |
| 3 | **A-PJ44** —— L-PJ9 樣式清單是否改為可增補清單 | A-PJ44 | 3 列 + 方法論 |
| 4 | **⛔ A-PJ45 / DR#14** —— B5 之 PROXI 車型代號對照表；**42 列阻塞** | A-PJ45 | **B5 停下** |
| 5 | **DR#14 (b) 是否先問** —— Atl-Mid 是否在 SWQT 範圍；若否，阻塞 42→12 列 | A-PJ45 | 建議先問 |
| 2 | **spec_mode 重評**（R-P22 要求）—— 現行 `[A,B,D]` 無法表達 CarPlay Addendum(82) + HUIG(79) 這類 SYS.1 外部規格 | — | 已在 `feature.yaml → spec_sources` 記錄實際分層，字面未擅改 |

不阻塞、僅記錄：A-PJ01 / A-PJ03 / A-PJ07（入 RD-1）、A-PJ16（R-P18 明示不阻塞）。

Phase 2 補裁已關閉 A-PJ19 / A-PJ20 / A-PJ21，並追認 A-PJ23。原先列在此處的
六項待裁只剩 A-PJ06 一項。

### PCTS 未解鎖列的最終處置（補裁後）

| 列 | 狀態 | 何時解 |
|---|---|---|
| 376–379 | 環境阻塞（`Not in ASW-R1 Release Scope`） | 無條件不動，不解 |
| 267 / 521 / 522 | partial（WP43 / MT1） | **首次實跑時回填 `pcts_evidence.json`，status 轉 confirmed 即自動解鎖** |
| 441 / 443 | 已定案維持不動並入 RD-1 | 不解（A-PJ20 / A-PJ21） |

L-PJ7 讀的是 `data/pcts_evidence.json` 的 status，不是靜態清單 —— 首次實跑回填
後解鎖不需修改任何 gate。

### A-PJ06 分析底稿（已產出，供 chat 定稿三層框架）

| 檔案 | 內容 |
|---|---|
| `data/testgroup_matrix.json` | 559 列逐列：TG / TS / 037 Sub Categorization / 五 build 執行紀錄；10×18 交叉表 |
| `data/cfts085_sections.json` | CFTS085 clause→章節對映（486 clause / 0 未對映）+ 章節→服務列 |
| `data/sub_x_testset.json` | 037 Sub Categorization × Test Set 13×18 交叉表 |
| `data/protocol_axis.json` | 559 列的協定／傳輸軸抽取（來源＝Test Item + Test Group，**未取 Test Set** 以免循環） |
| `data/layer2_x_layer3.json` | Test Set × CFTS085 章節的雙向矩陣 |
| `data/layer2_isomorphism.json` | 排除 version-track 後的同構度；`_meta` 帶 R-P23 補充條款警語 |
| `data/huig_sections.json` | HUIG R-ID → 章節對映（1,028 個，章號一致性 100%）+ Test Set × 章節 |
| `data/sysad_sections.json` | SYSAD NRL → 章節對映（254 個）。**NRL 是章節 id 非需求 id，2 章經 R-P29 閘門排除** |
| `data/carplay_addendum_sections.json` | CarPlay Addendum 章節 → 列（自 PDF outline，310 章節，解出 72 列） |
| `data/layer3_gate.json` | **R-P29 鑑別力閘門**：五份來源逐 id 跨 Set 數與排除清單 |

**⚠️ version-track 警語**：CFTS085 `1.3.2.14`~`.18` 共 115 列排除於同構檢驗，
**但排除只在框架推導階段生效** —— 這批列在 Phase 4 的 spec 核對對象仍是那些
版本章節（R-P23 補充條款）。詳見 profile §3d。

### P6 批次規劃（[PROPOSED]，未定案）

自然的批次單位是 **Test Set**（18 值）。建議 pilot 取 **Vehicle Signal
Forwarding**（22 列）—— 它同時踩到 CAN 送值、PROXI 前置與訊號對照三條新機制，
是最早能證偽整套 gate 的一批。其餘依 HMI Display 76 / Projection Launch 65 /
Connection 61 … 順序推進。9 列 PCTS 未解鎖列從所有批次排除。

### 本 feature 的執行守則（與其他 feature 不同之處）

1. **可寫欄位為 3 欄**：`Pre-Conditions`(I)、`Test procedure`(K)，以及
   R-P19 授權的 `Test Case Author`(Z) 之 41 個空格。其餘全部凍結。
2. **列數與列序僅有一個例外**：R-P19 授權刪除第 562 列殘樁（559 → 558 列）。
   其餘任何移動或增刪即中止。
3. **`Estimated Test Time` 維持全空** —— R-P19 定為慣例，填它是違規。
4. **模糊語落在 Expected Result 時**，只有 R-P12 窄口的純刪除可放行
   （row 424–429 六列）；RD-1 三列為 **434 / 435 / 520**（實體列號，補裁 #1）。
   row 520 的 Procedure 那一處不受 L-PJ4 拘束，仍須依 L-PJ6 清除。
8. **候選不唯一即不選** —— R-P9 → R-P18 → 補裁 #2 → 補裁 #3 四次同判準：
   來源之外需要指認對象時一律不指認，該列維持不動並入 RD-1。同型情形可直接
   援用，不必逐次上呈。
5. **訊號一律走 mapping 表取名、PROXI／DBC 取值**（R-P20）。直接拿 token 查
   DBC 會全數落空；拿 mapping 查值域會誤判合法值。
6. **PCTS 列看證據不看清單** —— `data/pcts_evidence.json` 的 status 決定該列
   能否修訂（R-P11）。
7. **spec 核對基準是 May 3 2023 版**，不是 `inputs/` 裡較新的 2026 版（R-P17）。
