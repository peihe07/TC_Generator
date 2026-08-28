# PLAYBOOK — SW Update (FW036 TC Generation)

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
Claude Code without asking — bounded by the six stop conditions (FO §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_SWUpdate_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (FO §6) — a summary missing a field is returned, not approved

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
7. On anything the sources don't state: `[ASSUMPTION A-SUnn]` marker +
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
  copy+yaml, no shared library (FO §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `SW UpdateHMI/PLAYBOOK.md`、`SW UpdateHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`SW UpdateHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — SW Update

- [x] P0 intake complete; INTAKE.md reviewed; missing files: **無**（六份素材 + 036 母本 + Pop Up List 全在場）
- [x] P1 recon complete; workbook_state: **BLANK**; leaves: **307**; targets: **307**
- [ ] P2 DECISIONS signed (date: ____)
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING rulings: **無**（A-SU1／A-SU2／A-SU3 皆 RESOLVED）
- 驗證母體（R-SU3）: **311** = FR 307 + NFR 4；錨點池（R-SU7 v2）: **574**

## 7. 操作慣例（建議，非條文）

> 本節為實際發生過之錯所留下的教訓，逐則記其出處。
> **違反不構成停止條件**，但照做可省一輪。

**(1) 分類型產出，每一類都要有一路獨立計數 —— 不能只驗最好驗的那類。**

出處：上繳包 02 §六（自評 #1），T10／T12 案例。

T10 對 CFTS_57 之 7 位 id 做四分類（章節／需求／Description／不可歸類），
交付時只做了一路交叉驗證：「章節物件 87 = TOC PAGEREF 87」。
該路只守章節物件 —— 對「需求物件」與「不可歸類」之邊界完全無獨立覆核。

缺陷因此存活：分類採「首見為準」，而 11 個帶 `[Artifact Type:…]` 宣告之
id 在文件中**先以內文 `Requirement ID {id}` 形態出現**，宣告排在後方，
遂被誤歸「不可歸類」。錨點池因而少了 9 個（565 而非 574）。

錯數之所以被抓到，是因為下一包（T12）從 **Description 側**重數一次而對不上
（137 ≠ 135）—— 屬僥倖，不屬設計。若 R-SU7 未恰好要求 Description 對照，
565 會一路帶進 Phase 2/3 之錨定。

**作法**：分類產出交付前，對每一類各找一路與分類邏輯**不同源**的計數
（如：宣告數 vs 文序走訪數、正向分類 vs 反向對照），並令各類之和
閉合到母體總數。本例修正後之閉合式為 `87 + 487 + 137 + 10 = 721`
= 裸命中 unique 總數。

**(2) 閉合檢查閉合的是它量的那個東西 —— 檢查通過不代表量對了東西。**

出處：上繳包 06 §3.1（T20a 之 487 空字串案）；本輪 A-SU4 為同族之再現。

T20a 抽取 487 個 CFTS 需求物件之全文，閉合檢查為 `487 = 487` ——
**通過了**。但該式閉合的是 **id 數**，不是**文字**：初版之切法取錯段落，
487 個全文**皆為空字串**，閉合照樣通過。若當時續跑，每列得分 0，
而 0 分不會讓任何檢查 FAIL —— 一份全零的錨表會看起來像一份錨表。

同族之再現（A-SU4）：修好空字串後，`487 = 487` 仍通過，
而 14 個物件之文字吞併了 43 個不屬於它們的 Description（佔全部文字 19.5%）。
**兩次都是閉合檢查通過、量錯了東西**；兩次都由**分布**（長度中位數、極值）
而非由閉合式察覺。

**作法**：對「抽出內容」之產出，閉合檢查至少要有一式**針對內容本身**
—— 長度分布（中位數／極值／零值計數）、抽樣目視、或內容之結構不變量
（如「不得含下一個物件之宣告」）。只數個數的閉合式必須明白寫出
「本式閉合的是個數，不是內容」。

**(3) 發現更強之探針時，增設而不取代 —— 探針之效力由裁定者定。**

出處：上繳包 06 §3、§2.3。

R-SU13 之自我檢定指定了三個「已知標的探針」，全部 FAIL。執行層另找到
證據更強之探針（037 自己寫出的對應，2/2 PASS）。換掉指定探針即可全過、
跑完全母體、交出一份漂亮的完成品 —— **而指定探針的 0/3 仍然是真的，
只是不會出現在報告裡**。

執行層增設而未取代，並自陳「沒發生是因為下放包指定了探針，不是因為我謹慎」。

**作法**：自我檢定之探針由裁定者指定；執行層發現更強者一律**增設並回報**，
不得替換。當強弱探針結論相反時，**停下來讓裁定者裁**，不由執行層決定
哪個探針算數 —— 那正是這條規則要防的事。

**(4) 候選產生器與裁決器是兩件事 —— 召回 100% 與首選正確 82% 可以同時為真。**

出處：下放包 09 §3.1（17 列人裁地面真值）；上繳包 08 §4（四規則回測）。

同一個 TF-IDF 管線，在 17 列地面真值上：**正解落於前 5 候選 17/17（100%）**，
但**首選即完整正解僅 12/17（71%）**、首選之章正確 14/17（82%）。
**它是個近乎無漏的候選產生器，同時是個會錯兩成的裁決器。**

若只看首選正確率，會結論「這條路不通」而換工具；若只看召回，
會結論「這條路很好」而直接取首選定錨。**兩個結論都錯。**
正確的用法是兩階段：管線產候選（用其高召回），裁決另設（不用其低精度）。

**作法**：評估一條檢索／比對管線時，**召回與精度必須分開報**，
且要明說它將被當成產生器還是裁決器。只報一個數字的評估，
無論那個數字多好看，都不足以決定該管線怎麼用。

**(5) 閉合式必須拆到被裁定的那個維度上。**

出處：上繳包 08 §2.1（A-SU5）。

T12 產出 137 個 Description 之**歸屬**（誰屬於誰），其閉合檢查為
`137 = 137`。**該式對「歸屬給了誰」完全不敏感** —— 把兩個 Description
歸錯宿主，總數仍然是 137，檢查照樣通過。錯誤存活了兩包，
直到 T22a 把「歸需求 43 / 歸章節 94」拆開單列才顯形。

這是 §7(2) 的第三次再現，而三次量錯的東西各不相同：
**文字**（487 個空字串）→ **邊界**（吞併 43 個 Description）→ **歸屬**（誤歸 2 個）。
每次的閉合式都通過了，每次通過的都是別的維度。

**作法**：問「這份產出被裁定的是哪個維度？」——是分類就拆到每一類，
是歸屬就拆到每個宿主群，是文字就驗長度分布。**總數閉合永遠是最弱的一式**，
它只能證明沒漏沒重，不能證明分對了。

**(6) 指標之選擇本身即可掩蓋問題。**

出處：上繳包 08 §9.3（`313` 之召回 vs 涵蓋率）。

同一列 `SWE1-FOTA-313`（正解 6 個物件）：
- 以**召回**（至少一個正解在候選內）衡量 → **PASS**（命中 1/6）
- 以**涵蓋率**（全部正解都在候選內）衡量 → **FAIL**

若報告只列召回 17/17（100%），那個「6 個正解只找到 1 個」的結構性盲區
**不會出現在報告裡** —— 不是被隱瞞，是被指標本身濾掉了。

**作法**：選指標前先問「這個指標對哪種失敗不敏感？」。
一對多的任務至少要同時報**召回**與**涵蓋率**；有層級的任務要同時報
細粒度與粗粒度的準確率。**只報一個指標時，須明寫它看不見什麼。**

**(7) 證明「零是真的零」與報「零」是兩件事。**

出處：上繳包 09 §2.4（統攝語形之式B／式C／式D 皆 0 命中）。

六式語形掃描中三式得 0。報「0 命中」是誠實的，但**讀者無從分辨那是
「語料真的沒有」還是「regex 寫得太嚴」** —— 而這兩件事對後續的意義完全相反：
前者是有效的否定結果，後者是掃描失效。

作法是**反向探測**：用更寬鬆的裸字串再掃一次（`listed`、`as follows`、
`section`、`table`、`refer to`、`see`），全部 0 —— 於是那三式的零被證明是真的零。
同一次探測也揭出了六式**確實會漏**的兩條路徑（語序倒置、計數門檻），
那才是該報的缺陷。

**關鍵是探測時不改原式** —— 改式即為看著結果轉旋鈕；漏網另列，
讓裁定者決定要不要補式。

**作法**：任何「未發現」「無命中」「無異常」之結論，都要附一路
**比原方法更寬鬆**的探測，證明該否定不是方法失效造成的。
只報零，等於把「沒有」與「沒看見」混為一談。

**(8) 偵測器須先對種子案例回測 —— 「找到新案例」不代表「找得到原案例」。**

出處：上繳包 10 §5.1（T24d 之缺陷掃描）。

為找 037 描述缺陷而寫的六式語形掃描，找到了一筆新案例（D-2 `248`），
台帳因此有兩筆。看起來掃描是有效的。

**實際上 D-1（`319`）是下放包給的，掃描抓不到它** —— 其
`the handling of condition during…` 因缺字後接 `during`，
不合式1 的「介詞 + 抽象名詞 + 句尾」條件。**種子案例自己不在結果裡。**

若不回頭驗這一步，讀者會合理推論「掃描找到兩筆」＝「掃描有效」，
而台帳會被當成全集而非下界。

**作法**：任何偵測器交付前，先拿**已知該被抓到的案例**餵進去。
抓不到就是偵測器不完整，不論它另外找到了多少新案例。
這一步是 R-SU13 v2「自我檢定」在偵測器上的同型要求 ——
**新發現不能替代原案例的回測**（同 §7(3) 之「增設而不取代」）。

**(9) 引用他文之敘述時，須對本文新算的數字重驗它仍成立。**

出處：上繳包 11 §7.3（自陳之擴寫錯誤）。

下放包 12 §4.2 寫「`292` 之首選分 0.257 高於第 10 百分位 0.229，故機制 3 攔不下它」
—— 在**只有第 10 百分位這一個門檻**的脈絡下，該句無誤。
上繳包把它擴寫成「高於全部四個門檻」時，**與同一頁自己新算的表格矛盾**
（第 20 百分位 0.267 > 0.257，攔得下）。

錯誤的形狀不是算錯，是**把上游的結論當成常數搬運**：
上游的敘述綁在上游的前提上，而本文新增了門檻、新增了語料版本、
新增了樣本 —— 前提一動，那句話就不再是同一句話。

**作法**：凡引用他包之判斷性敘述（「高於」「攔不下」「涵蓋」「唯一」），
一律在本文用本文的數字**重算一次**，不得沿用文字。
沿用文字而不重算，等於把別人的前提偷渡成自己的結論。

**(10) A 型之實例不能充當 B 型之種子 —— 先確認二者的結構特徵同源。**

出處：上繳包 11 §3（T25b 種子回測未過）。

下放包 12 令以區塊 #8 為 (a2)「無編號平行式」偵測器之種子，
理由是 #8「有編號，骨架亦平行」。實測 #8 六項之句首骨架 6/6 兩兩皆不同。

成因是把兩種結構**當成同一現象的兩個樣子**：(a1) 靠編號成塊，
(a2) 靠骨架成塊 —— 二者的**可觀測特徵不同源**，
所以「(a1) 的確定實例」不構成「(a2) 的確定實例」。
#8 是列舉區塊沒錯，但它是靠編號才是的。

這一條是 §7(8)（偵測器須先對種子回測）的前置：
**§7(8) 問「種子抓得到嗎」，本條問「這東西真的是種子嗎」。**
種子選錯時，§7(8) 會照實報未過 —— 那時該修的是前提，不是偵測器。

**作法**：指定種子時，須寫明該種子**滿足偵測器所依據的那一個特徵**，
並實測之；只寫「它是同一類現象」不足。
執行層發現種子不合前提時**回報，不自換** ——
自換一個「恰好通過」的種子，回測就必然通過而失去意義。

**(11) 改變指標之定義以產生召回，是最容易且最難察覺的一種造假。**

出處：上繳包 12 §1（機制 4 之回測）與下放包 14 §1.1 之採認。

機制 4 在 GT-A1 上召回為 0 —— 它為「正解排 6–20 而首選分不低」而設，
而 GT-A1 裡沒有這一型。**把「缺口」的定義由「正解不在前 5」改成
「正解非 top1」，`260` 立刻變成缺口，機制 4 立刻有召回。**
一行改動，表格從「增益為零」變成「有效」，而且**改的是定義，不是數字**
—— 沒有任何一個數字算錯，沒有任何一句話說謊。

這比捏造數字難察覺，因為讀者查得到的東西全都對得上。
唯一能發現它的方式是**看定義有沒有在中途變過**，而定義通常不在表格裡。

**作法**：指標之定義（缺口、命中、涵蓋、誤報）一經裁定即**凍結並寫進條文**，
其後任何一輪都不得為了讓某個機制有輸出而調整它。
確有必要更動時，**必須另立條號、重算全部歷史比率、且不得新舊並陳**
（同 R-SU17 v1(b) 對分組判準之拘束）。

**判準**：若一個定義之更動剛好使「本輪要證明的東西」成立，
那它就不是澄清，是轉旋鈕 —— 與 §7(7) 之「不改原式」、
§7(8) 之「先對種子回測」是同一條紀律的三個面向。

**(12) 導航面之推定與交付面之依據須分層 —— 前者可 provisional，後者不可。**

出處：R-SU18(c)（下放包 15 §二，Pei 2026-08-28 裁丙）。

framework 之 Layer 3（spec 章節分群）與工作簿之 `specification_reference`
用的是同一批錨定證據，所以很容易被當成同一件事而共用同一個把握度。
**但它們的失敗後果不同**：Layer 3 錯了，撰寫該列 TC 時會發現並就地修正 ——
代價是導航繞路；`specification_reference` 錯了，是**交付出去的缺陷**，
而且沒有下一關會撞到它。

於是可以（也應該）給它們不同的效力：Layer 3 標 provisional 並放行，
`specification_reference` 一律走逐列裁定，**不得以 Layer 3 之章推定其錨**。

**這條之所以值得記，是因為它解開了一個看似兩難的僵局**：
「錨定不夠嚴謹所以 framework 不能定稿」在此不成立 ——
不夠嚴謹的只是 Layer 3，而 Layer 3 本就不進工作簿。
把二者綁在一起，會讓交付面的嚴謹要求無限期地擋住導航面的產出。

**作法**：任何一份推定，先問**它錯了會被誰撞到**。
有下一關會撞到的，可以 provisional 並標明；
沒有下一關的，一律走完整裁定。
**危險的是把有下一關的東西也當成沒有下一關來要求**（進度停滯），
**以及把沒有下一關的東西當成有下一關來放行**（交付缺陷）。

**(13) 0 列物件是閉合檢查的系統性盲區 —— 以量為準的檢查對零無感，要抓只能改查種類。**

出處：上繳包 14 §1、§7.3（`SWE1-FOTA-022` 案），下放包 16 §1.1 立為通則。

framework Layer 2 之 12 組漏了一個 Heading 群（`022`，`Communication Security`）。
列數閉合 234 + 77 = **311/311 完全通過** —— 因為該群所轄 in-scope 列為 **0**，
漏掉它不會使任何列數短少。只有另算**群數**（42 + 2 = 44 ≠ 45）才撞到它。

錯誤的形狀是：**檢查式與被檢物的度量單位不同。**
以「列」為單位的閉合，對「群」這一層的遺漏是全盲的；
而零列的群剛好是二者唯一會分岔的地方。

**這種漏在當下無害，日後才發作** ——`022` 現在 0 列，不影響任何交付數字；
但它是一個真實存在的 Heading 群，日後 037 改版若該群長出列，
它會以「framework 從未涵蓋過的群」之形態出現，而那時沒有人會記得它是舊漏。

**作法**：任何歸屬類的閉合，**至少查兩個單位** ——
被歸屬物的「量」（列數）與「種類」（群數、id 集合）。
更嚴者再加第三項：**id 集合之聯集與兩兩不相交**
（前二者對「同一列被歸進兩組」同樣無感）。
R-SU10 v2 之三重閉合即此三項之條文化。

**判準**：若某一類物件之計量為零，它就不會出現在任何以量為準的檢查裡 ——
問一次「有沒有零值的那一類」，通常就是這一條的觸發點。

**(14) 已知某資訊不足以判斷，仍用該資訊下判斷 —— 比單純判錯嚴重。**

出處：上繳包 15 §6.1(甲)，下放包 17 §1.3 確認為分析層之方法錯誤。

上繳包 14 §7.1 已白紙黑字記明：`321 Interruption Recovery Handling`／
`325 Download Interruption Handling`／`360 Download Interruption Recovery`
**三個近義標題無法由標題判其為同一能力之三面或三個不同能力**。
下一包切 Layer 2 時，仍以標題之關鍵詞（`Interruption`／`Reporting`）
把 `357`／`358`／`360` 指去對應之組。

**為什麼比單純判錯嚴重**：判錯是資訊不夠而猜錯，補資訊即可修正；
**用已知不足的資訊下判斷，是把一個「已登記的未知」當成了已知** ——
登記過的那句話從此變成擺設，而讀者會合理假設「既然登記了，後續就有處理」。
**它同時毀掉判斷與登記制度本身。**

更隱蔽的是它的形狀：那不是新錯，是**舊警告失效**。
查錯的人會去看新產出對不對，不會回頭查「上一包警告過的事這一包有沒有犯」。

**作法**：凡上一包（或任何條文、台帳）明文登記「X 不足以判斷 Y」者，
本包若須判 Y，**須先在文內指名該登記並說明本次憑什麼可以判** ——
補了什麼新資訊、或為何該登記在此不適用。
不能只是不提它。**沉默地繞過一條自己寫下的警告，等同撤銷它。**

**判準**：交付前掃一次自己上一包的「不足／未知／待確認」清單，
逐項問「本包有沒有在沒補資訊的情況下用到它」。
R-SU20(d)「依據不得為其標題之關鍵詞與組名相符」即此條之條文化 ——
**關鍵詞相符是循環，不是依據**。

**(15) 寫「關於零之條文」時，其列舉須以程式產生 —— 人手列舉對零同樣無感。**

出處：上繳包 16 §主結果 2（R-SU21(b) 漏列 `SWE1-FOTA-085`），
下放包 18 §1.1 立為通則並寫入 R-SU21 v2(b)。

§7(13) 說「0 列物件是閉合檢查的系統性盲區」。R-SU21 是**專為 0 列群而設的條文**，
它逐一列舉了 8 個 0 列 Heading 群 —— **而實測是 9 個**，漏了 `085`。

這一條之所以值得與 (13) 分開記，是因為它指出盲區的**第二個位置**：
(13) 講的是**檢查式**對零無感；本條講的是**條文之列舉**也對零無感。
理由相同 —— **列舉是一種以量為準的清點**，人在清點時靠「看到東西」來推進，
而零列的群在任何按量排序、按內容瀏覽的視圖裡都不顯眼。
**寫條文的人與寫檢查的人犯的是同一個錯，只是載體不同。**

**作法**：條文若對某一類物件立規，而該類之判準是「某個計數為零」，
其**成員清單一律由程式產生**，並在檔內留下一個
**清單 vs 條文之比對步驟**（不符即停）。
本案之 `scripts/layer2_close.py 31d` 即此步。

**判準**：看到條文裡有手寫的 id 清單，就問「這份清單是誰數出來的」。
人數的就補一支程式重數一次 —— 尤其當該清單的成員資格取決於一個零值。

**(16) 空測通過與實測通過是兩件事。**

出處：上繳包 16 §5.2（外科式寫回之空寫回 vs 實寫探針），
下放包 18 §1.4 採認。

外科式寫回之空寫回（寫 0 列）產出「48 個部件逐 byte 全同、0 個相異」——
數字漂亮，而它**證明不了寫入時仍保全**：寫 0 列時
`_set_row()`（唯一會動 XML 的那段）**一次都沒被呼叫**。
那張全綠表真正證明的是「把一份 zip 解開再打包回去，內容不變」。

**形狀**：一個驗收的路徑**繞過了它要驗的機制**，而其結果仍然全綠。
比 §7(8)（偵測器未對種子回測）更難察覺，因為 §7(8) 是「跑了但沒抓到」，
本條是**「根本沒跑到」**，而輸出看起來完全正常。

**作法**：驗收設計完成後，問一句
**「這條路徑有沒有真的呼叫到我要驗的那段程式碼」**。
沒有就補一個**最小的實測**（本案為實寫 1 列之探針，量同一組指標
並比對 `<row>` 屬性、儲存格數、`s=` 樣式索引）。
零筆／空集／no-op 之驗收一律視為未驗，除非另有實測相佐。

**(17) 種子必須是獨立觀測 —— 由待驗規則推算出之預期值不得充當種子。**

出處：上繳包 17 §7.2（孤島檢查之「5/5 通過」），下放包 19 §1.1 立為通則。

孤島檢查之首次種子回測用的是 **7 個實際觀測到的**孤島 —— 那是真的回測。
下一輪切分改動後，我把種子換成 **5 個依改組推算出來的預期值**，
再報「5/5 通過」。**那一格驗的是「程式算出的結果等於我用同一套規則手算的結果」
—— 它驗的是我沒算錯，不是偵測器沒壞。**

**與 §7(10) 同族，但更隱蔽**：(10) 是「A 型之實例不能充當 B 型之種子」，
二者至少是**兩個不同的東西**，錯配看得出來；
本條之種子與被驗者**出自同一套規則**，形狀完全吻合，
所以它永遠會通過，且通過得毫無雜訊。**必然通過的檢查不是檢查。**

**作法**：種子之來源須與被驗者**互相獨立**。
規則改動後若無新的獨立觀測可用，就**不要報種子回測** ——
改報真正有鑑別力的那一格。本例中那一格是
**「種子外之新發現 0 個」**（改動有沒有製造非預期之產出），
以及**改動前後之對照表**（解除幾個／新產生幾個）。

**判準**：問「若偵測器壞了，這個回測會不會失敗？」
若種子是用被驗規則算出來的，答案是**不會** —— 二者會一起錯，並且一致。

**(18) 判準取「含界值之向」—— 以母體實測分位為門檻者，界上恆有一列。**

出處：上繳包 17 §5.2，條文化於 R-SU23。

門檻若定義為 `sorted(scores)[int(n * p / 100)]`，它**取自母體之一個實測值**，
於是那個位次上的列**必然**與門檻相等，其去留全看判準寫 `<` 還是 `≤`。

**這一條之價值不在選 `≤`，在於認出它不是巧合。**
本 feature 前後遇過三次邊界事件（差 0.001／差 0.00000／完全相等），
前兩次都被當成「個案之脆弱」處理 —— 直到第三次才看出
**三者是同一個結構的相鄰表現**。

**作法**：
- 門檻取自實測分位者，判準一律取**含界值之向**，並使「含」落在**代價較小**的那側
  （本案：多送一列人裁 vs 漏一個缺口，故 `≤` 為攔下）。
- 陳述此類門檻之效果時，**須同時載明「界上恆有一列」** ——
  不得把它寫成巧合或個案。
- 改判準時，**逐項列出已載數字之更正對照**（本案 62 → 63），
  並說明歷史腳本是否保留舊判準以維持既有包之可重現性。

**(19) lint 全綠不等於 TC 對 —— 機械層查得到「形」，查不到「驗錯了東西」與「台架上跑不起來」。**

出處：上繳包 18 §3.2 之記明與 §7.1 之實證，下放包 20 §1.3 採認。

pilot v1 之 5 個 TC 跑 lint036 得 **21 項中 18 項全 0**，
唯三處違規全落在同一列（已知有 DR 而刻意掛起的那列）。
**而那 5 個 TC 全部有在台架上跑不起來的步驟** ——
「Read the update type received by the WiFi Update Service」讀的是內部服務狀態，
本 feature 無任何已綁定之觀測通道。

**二者之落點恰好相反，這才是該記的**：
lint 抓到的是**已知**的那一列；lint 沒抓到的散在**全部 5 個 TC**，
包含看起來最乾淨的那一個。
**只看 lint 報告會得到「只有一列有問題」之印象，而實際上是每一列都有。**

**lint 能查什麼**：禁用動詞、情態詞、hedge、編號對齊、行尾句號、
不可見字元、佔位語言 —— **全是「這一行寫得合不合格式」**。

**lint 查不到什麼**：
- **驗錯了東西**（ER 檢查的不是該需求所述之行為）
- **跑不起來**（步驟之操作目標或 ER 之判定對象不可觀測）
- **錨錯了**（`specification_reference` 指向語意相反之物件 —— 本 feature
  之 `177` 即首選與正解語意相反之實例）

**作法**：lint 綠了之後，逐 TC 問三句 ——
**「這一步，台架上的人要看哪裡？」**（R-SU25(e)）、
「ER 驗的是不是該需求所述之那件事？」、「錨指的那段話是不是真的在說這件事？」
三者皆非機械可判，**故 lint 之全綠只能作為交付之必要條件，永遠不是充分條件**。

**(20) 掃描寫得再全，掃的範圍是自己選的 —— 先列全覽，再掃。**

出處：上繳包 19 §7.3（037 之二欄從未被讀過），條文化於 R-SU26。

037 有 18 欄。本 feature 自 T2 建 `feature.yaml` 起只用了 6 欄，
其中 **`Verification Criteria`（310 列非空）與 `Verification Method`
（311 列全非空）從未被讀過** —— 而那兩欄正是上游作者對每一列
「該用什麼方法驗」之既有判斷，恰是後來整整兩包在問的東西。

**它不是漏掉一個檢查，是漏掉一片素材。** T33c 之通道掃描寫得很全
（三個來源 × 九個語形），**而它掃的欄是我自己選的那六欄**。
掃描之完備性只在其範圍內成立，**而範圍本身從不出現在報告裡**。

**這是「答案已在 repo 裡」之第四次，且第一次發生在自己的主素材內** ——
前三次是沒去看別人的目錄，這次是沒去看自己手上這份檔的全部欄位。

**作法**：任一來源檔首次使用前，先產出**欄位全覽** ——
欄序、標頭原文、非空列數、值型態摘要，**且逐欄標記
`已用`／`不用（理由）`／`未定`**。
`未定` 不得跨輪留存：下一輪必須裁為前二者之一。

**判準**：報告裡出現「掃了全部 X」時，問一句
**「X 的全集是誰定義的」** —— 若答案是「我上次用的那些」，那就不是全集。
**「掃了但沒命中」與「根本沒掃到那一欄」須可分辨**，全覽表即其分辨之依據。

**(21) 判準測的是「文字裡有沒有提到」，不是「這件事有沒有」。**

出處：上繳包 19 §7.1(乙2)，下放包 21 §1.2 據以裁定 126 之讀法。

我用語形判準普查「主體全為內部服務且無外部可觀測面」之列，得 **126／311**。
那個數字看起來像「126 列寫不出可執行之 TC」。**它不是。**

**反例是同一包裡的 pilot v2**：它把「更新在背景執行」之驗證面
改成**版本號之前後變化**，而 **`version` 一詞在該需求之 Description 裡
一個字都沒有**。即：**一個需求可以毫無外部面之字眼，而其行為仍有可觀測之後果。**

**語形判準測得到的是「文字提及」，測不到「事實存在」** ——
後者需要對該行為之因果後果作推論，而推論不可由 regex 為之。

**故該類數字之正確地位是「上界」**：
126 列**需要逐列被問一次**「它的可觀測後果是什麼」，
**不是 126 列沒有可觀測後果**。二者在後續處置上完全不同 ——
前者是 126 筆待辦，後者是 126 筆缺件。

**作法**：語形普查之結論一律寫成
「**未提及 X 之列數**」，不得寫成「**無 X 之列數**」。
若讀者需要後者，須另以逐列人裁取得，且普查之數只作其上界與工作清單。

**判準**：問「有沒有一個反例 —— 某列不含該詞，而該事實仍成立？」
找得到一個，這個普查就只能當上界。

**(22) 欄之「不用」得因值型態成立，不得因其母欄之值型態成立。**

出處：R-SU28(c)（下放包 22 §三），其所處置者為 037 之 9 個未定欄。

037 之 `Feasibility` 全為 `Yes`、`Impact` 全為 `Yes`、`Risk Factor` 全為 `Medium`
—— **單值欄之資訊量為零**，故裁「不用」**不需讀其內容**即可成立：
一個在全母體上不變的欄，於任何用途皆不可分辨。

**危險的是下一步**：這三欄各有一個配對之說明欄
（`Description/Action for Feasibility` 等），
而**「母欄是常數」看起來像是「說明欄也沒東西可說」**。
實測相反 —— `Description/Action for Impact` 之 unique 為 **191／311**，
其內容載有該需求之影響面，而影響面與可觀測後果相關。

**即：一個欄之資訊量，只能由它自己的值決定。**
`Yes` 欄之常數性不會傳染給它的說明欄；
反過來，說明欄之豐富也不使 `Yes` 欄變得有用。

**作法**：
- 裁「不用」時，其理由**必須引用該欄自己的值型態實測**
  （單值／二值且差為寫法／unique 數與長度分佈）。
- **不得**以「其母欄為常數」「其為同一組欄位」「該組看起來是流程管理欄」
  之類的鄰接理由裁之 —— 那是把一個沒讀過的欄，用它旁邊那欄的性質判掉。
- 自由文字且 unique 數高者，**一律先抽樣讀再裁**。

**判準**：問「我是讀了這一欄才這樣說的，還是讀了它旁邊那一欄？」

**(23) 否證之方向本身是資訊 —— 「前提不成立」與「前提反向成立」，處置不同。**

出處：上繳包 21 §2.1（丙路之否證），下放包 23 §1.1 採認。

分析層提出丙路：**若 105 列多數標 `Integration Test`，則其歸 SWE.5 整合測試，
SWE.6 不予產出**。實測 **15%** —— 前提不成立。

**若只報「不成立」，該輪之產出就是一個 `False`，議題退回原點。**
但對照組是 **35%**（非內部列）—— **105 列不只沒有更集中於整合測試，
反而比其他列更少**。

**方向一出來，結論就換了一個**：
不是「這條路走不通」，而是
**「上游把 85% 之 105 列標為含 `System Test`，而它們正是給不出觀測面的那些」**
—— 即上游在「該在哪一層測」與「怎麼看得到」兩件事上**沒有一致的判斷**。

**這個轉換有實際後果**：DR 之立論從
「我們找不到通道」（我方之困難，上游可以不理）
變成「**你的文件說要做系統測，卻沒說系統測時要看哪裡**」
（上游文件之內在不一致，是正當且明確之 DR 標的）。

**作法**：否證一個前提時，**一律同時報對照組之值** ——
「不成立」只給一個布林，「反向成立」給的是一個**新的事實**。
若無對照組可算，就明說該否證只到布林為止。

**判準**：問「這個否證，讓我知道了什麼**新的東西**，
還是只讓我不知道原本以為知道的東西？」

**(24) 滾動清單須分「已確認」與「未確認母群」二段 —— 只寫母群數會使未確認被讀成已確認。**

出處：上繳包 22 §7.1（DR-SU2 之清單），條文化於 R-SU30。

DR-SU2 之清單為滾動式：初始 5 列（已逐列試過且取不到觀測面），
隨批次增列。而符合同一語形條件之列有 **105** 列 ——
**其餘 100 列尚未逐列判定**。

**兩個誤讀方向，其中一個遠比另一個危險**：

| 讀者之推論 | 成立？ |
|---|:--:|
| 在清單上 = 已試過且取不到 | ✅ 可由定義保證 |
| **不在清單上 = 已試過且取得到** | ❌ **完全不成立** |
| **DR 之規模 = 現有列數** | ❌ 其上界為母群 |

**真正的風險是進度感**：滾動清單會隨批次成長，
而**成長本身看起來像「新發現的問題」，其實是「原本就在那裡、現在才輪到它」**。
於是一個上界 105 列（母體 34%）之問題，會被讀成一個 5 列的小問題。

**而警語擋不住它** —— 一段警語與一個會成長的數字並排時，**數字比較大聲**。

**作法**：台帳之條目分二段，且**把上界寫進表頭本身**，不藏在註解裡：

```
DR-SU2：確認進度 5 / 105
  (a) 已確認段   5 列 —— 已逐列判定且取不到
  (b) 未確認母群 105 列 —— 尚未逐列判定
```

**判準**：一個清單若會成長，就問「**它最多會長到多少**」。
答不出上界，讀者只能用當前值估規模，而那必然低估。
**進度為 0 或極低之滾動清單，不得被陳述為「已盤點完成」。**

**(25) 一批樣本「全部通過」之意義，取決於它涵蓋了哪些類 —— 未涵蓋之類，其通過率是未知，不是高。**

出處：上繳包 23 §7.1（pilot 之選樣避開兩個難類），條文化於 R-SU31(d)。

pilot 之 5 個 TC 全部寫得出可執行之步驟、lint 20/21 全 0。
**而其 4 個來源列，無一屬 126 內部列，亦無一屬 105 列** ——
那兩類合佔母體 41% 與 34%。

於是「pilot 通過」之正確讀法只有一句：
**非內部列寫得出來。** 126 列與 105 列之寫法，**至今無一例經驗證**。

**這與取樣偏誤不同，且更難察覺**：取樣偏誤是「抽到的樣本不像母體」，
還看得出分佈歪了；本條是**「某一整類完全沒被抽到」** ——
於是那一類的通過率不是「偏高」，而是**沒有數字**。
**一張全綠的表對它完全沉默，而沉默看起來像沒問題。**

**成因通常不是疏忽，是時序**：pilot 選樣時（下放包 18），
可觀測性尚未被指認為問題（R-SU25 到下放包 20 才立）。
**問題被發現得比選樣晚 —— 但後果一樣。**

**作法**：
- 選樣之依據**須明列它涵蓋了哪些已知難類及其列數**，
  而非只列「形態多樣」「有 GT 支持」之類的正面理由。
- 每產出一份「全部通過」之結果，**同時列出該批之難類涵蓋表**
  （各類之列數／佔比 vs 母體），使沉默的那一類可見。
- 新難類被指認時，**回頭重算既有樣本之涵蓋**，
  並明寫既有結論之適用範圍縮到哪裡。

**判準**：問「這批**沒有**包含什麼？」——
而不是只問「這批包含了什麼？」。

**(26) 查一條路走得通，與查所有路都走不通，是兩件事 —— 後者需要窮舉，而它通常不在任務清單裡。**

出處：上繳包 24 §7.3（`C` 欄替代鍵之反向實測）。

T38a 只令追查 `vehicle_category` 之 `C` 欄**來源**。查完得一條 126/126
全對之鏈路 —— **而那條鏈路對本 feature 無用**：其第一環 `HMI Source ID`
在本 feature 之 037（18 欄舊版面）不存在。

任務到此已完成，且結論看起來是正面的（「鏈路查明」）。
**真正待答之問題卻是另一個**：本 feature 有沒有**別的**鍵可接上 SYS1？
該問題**不在任務清單裡** —— 因為任務是照著已知的那條路寫的。

反向實測（三欄交集皆 0、形態不同族）之後，`C` 欄才裁得下「留空」，
而該裁定**是結論不是遺漏**。若只交前半，讀者會以為「還沒查」。

**判準**：任務問「這條路通不通」時，先問**「這是不是唯一的路」**。
- 「通」只需一個成功案例；「不通」需要窮舉，二者之舉證成本不對稱。
- **留空／不用／無解**這類否定式裁定，其依據一律是窮舉，
  故凡要裁否定式，先確認窮舉做過了 —— 沒做過就只能寫「未查」。

**(27) 一個台帳若二段來源不同，其比值就不是進度。**

出處：上繳包 24 §7.1（DR-SU2 二段之成員資格用了兩套判準），
條文化於 R-SU30 v2(e)(f)。

DR-SU2 記「5 / 105」，讀來像 5%。實則 (a) 段之 5 列由**人裁**入列、
(b) 段之 105 列由**語形 regex** 圈定 —— `SWE1-FOTA-365` 在 (a) 而不在 (b)，
**(a) 不是 (b) 之子集**。分子不在分母裡，該比值遂不是任何東西的進度。

**其發現途徑值得記**：不是由 lint、不是由 review，
而是執行層在做別的任務（難類盤點）時撞到的。
**二段判準不一致，在台帳上完全看不出來** —— 二欄都是數字，
數字都對，只有把二段的**入列條件**並排寫出來才顯形。

**作法**：
- 凡分子／分母並陳之台帳，**二段之入列判準須逐字寫在台帳裡**，
  不是寫在產生它的腳本裡。
- 判準不同時**以人裁為準**，語形判準降為上界之估計工具。
- 母群數之變動**須逐次記明成因**，不得只改數字。

**判準**：看到 `M / N`，先問**「M 是不是 N 的子集」**。
