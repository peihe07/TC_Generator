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
