# RULINGS — User_Profiles (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 User_Profiles 之裁決權威；
跨 feature 條文承接時註明來源包。

來源包：`features/user_profiles/docs/handoff/01a_rulings.md`
（Pei 2026-08-17 裁定）。以下 R-G1、R-G2 為全域條文，於本 feature 首次適用；
R-U1～R-U7 為本 feature 條文。

---

## 全域條文（跨 feature，於本包首次落檔）

```text
R-G1  036 母本（全域，跨 feature）
      自 2026-08-17 起，所有新 feature 一律以
      forms/…_SWQT_20260817_ext.xlsx 為 036 母本，不再逐 feature 詢問。
      母本選擇自此為 Tier 0 AUTO；既有 feature 之已交付件不因本條改變。
      執行層須將本條寫入 FORMS.md 與 FEATURE_ONBOARDING.md。

R-G2  forms/ 舊檔處置（全域，Pei 2026-08-17 裁定：歸檔）
      forms/ 只保留 …_SWQT_20260817_ext.xlsx。其餘三份
      （…_SWQT_20260121.xlsx、…_SWQT_20260816_ext.xlsx、
      …_SWQT_Home_20260809.xlsx）以 mv 移入
      archive/forms_superseded/，**不得刪除**。
      移動前後各記錄 shasum -a 256，證明內容未變。
      理由（實測，2026-08-17）：features/home/ 已無 inputs/ 亦無
      output/，Home 之 225 列工作簿在 repo 內僅存 forms/ 這一份，
      它同時是 R-U6 所指定之 style authority（Arif 144 列 done
      region）唯一載體，以及 rev A/B 版面（A–AG）唯一結構參照
      （AMFM 寫回與 Home v2 補發 A-H26 皆跑在該幾何上）。
      前例：2026-08-13 amfm／home／media／projection 之 inputs/
      全數清空，git 無從還原（從未被追蹤），tag 仍在而產物已不存在。
      歸檔後 FORMS.md 之各條目須改指 archive/ 路徑，條目本身保留。
```

**執行層回報（Phase 0，2026-08-17）**

- R-G1：已寫入 `forms/FORMS.md`（§036 母本條文）與
  `docs/fw036/FEATURE_ONBOARDING.md`（§0 Tier 0 條列）。
- R-G2：三份舊檔已以 `mv` 移入 `archive/forms_superseded/`，移前移後
  SHA256 各記錄一次且完全一致，未使用 `rm`。`forms/` 僅餘
  `…_SWQT_20260817_ext.xlsx`。FORMS.md 各既有條目已改指 `archive/` 路徑，
  條目未刪。逐項數值見 `docs/upstream/01_intake.md`。

---

## 本 feature 條文

```text
R-U1  命名分離
      Test Group 欄 = "User Profiles"（依 037 FROP 欄 182 列實測值）。
      specification_reference 一律使用 spec 之 SYSRE_HMI_Source ID 字串
      Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_
      (October_03_2023)_{section}，不改寫為 User Profiles，
      亦不使用檔名之 R1L-R (February_10_2023) 形式。

R-U2  feature slug = user_profiles；目錄 features/user_profiles/
      tc_id = NR1L-UserProfiles-{NNN}

R-U3  spec 基線 = SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_
      (February_10_2023).xlsx；spec_mode = A
      證據：Source ID 欄 169 列全屬 CR24798 (October_03_2023) namespace；
      037 引用之 135 個唯一 section id 缺漏 0。

R-U4  SWE1-HMI-PROF-017、SWE1-HMI-PROF-035（Out of scope）不生成 TC，
      登記為 note，不計入覆蓋率分母。生成母體 = 180 個 Functional
      Requirement 葉節點。

R-U5  Priority（修訂版，取代 08-17 初版之「High→P1」預設帶）
      依據 docs/runtime/TEST_CASE_PRIORITY.md 本文，非 canon §10.2 摘要。
      該文明定：feature 之核心主流程預設即 P0，除非明確屬次要或進階
      操作，否則不得降為 P1。故：
        P0 — 本 feature 核心主流程：profile 建立、切換、偏好之儲存與
             回復、Valet Mode 進出，以及資料遺失風險項（5.13.x
             Clear Personal Data／刪除全部 profile／回復原廠）
        P1 — 主要功能之次要／進階操作、邊界與變化路徑、非主路徑分支
        P2 — 輔助功能，失敗對主功能影響有限
        P3 — UI 強化、罕用情境
      037 之 High/Medium/Low 僅為先驗，衝突時以 TEST_CASE_PRIORITY.md
      為準；任何偏離須於 reasoning 具名依據。

R-U6  workbook_state = BLANK
      style authority = Home 之 done region（Arif 之 144 列），
      標記 cross-feature: style only。
      不採 Comfort（其為本管線自身產出，違反 §5a「不以自身先前輸出
      為來源」）；不採 AMFM（Wilson 之 158 列已裁為 frozen prefix，
      非 done region）。借用之任何字面值（label、數字、popup 文字、
      狀態名）一律重新回溯本 feature spec，以 lint 規則強制。
      BLANK 綁定：Test Group／Test Set = FILL；Test Item = 標準 §4.3
      tc_title；spec_reference 依 spec_mode A 模板構造；
      write-back = 自首個資料列起 append。

R-U7  036 母本採用前置（承 R-G1）
      須完成：forms/ 內各 036 檔之 shasum -a 256、20260817_ext 之結構
      探測（sheet 名、header row、A–AH 欄位對映、B 欄公式範圍、
      P/R/T–Z/AF 之 DV 範圍、下拉選單詞彙 9 條）、FORMS.md 新增本版
      條目並修復 A-UP03。母本不得被覆寫；複本置於
      features/user_profiles/inputs/。
```

**執行層回報（Phase 0，2026-08-17）**

- R-U1／R-U2：目錄與 slug 已依條文建立（`features/user_profiles/`）。
  Test Group 之 182 列實測值本輪**無法複驗** —— 037 工作簿不在 repo 內
  （見 A-UP04）。條文照錄，數值待 037 到齊後實測。
- R-U3：spec 基線檔在 `spec-index/cache/` 內確認存在，`Basic Report`
  171 列（表頭 1 ＋ 資料 169 + 1 空列，見上繳包量測條件）。
  spec_mode = A 之 169 列 namespace 已複驗；037 側之 135 個 id 命中率
  待 037 到齊。
- R-U4：待 037 到齊後於 recon 實施；本輪未生成任何 TC。
- R-U5／R-U6：本輪未進入生成，僅登記。R-U6 之 style authority
  （Home 225 列工作簿）已依 R-G2 移入 `archive/forms_superseded/`，
  仍在 repo 內、內容 SHA 未變。
- R-U7：已完成 forms/ 四檔 SHA256、`20260817_ext` 結構探測、FORMS.md
  新增條目並修復 A-UP03、母本複本置於 `inputs/` 且母本未被覆寫
  （openpyxl save 全 repo 未執行）。

---

## 第二輪條文

來源包：`features/user_profiles/docs/handoff/02a_rulings.md`
（Pei 2026-08-17 裁定）。**R-G3 為全域條文**（跨 feature 缺陷，非本 feature 專屬）；
其餘為本 feature 條文。

> **supersede 註記**：**R-U8 取代 `01b_tasks.md` 作業項 3 之預期值。**
> 01 輪之下放包**不改寫**（已結輪次不回溯編輯），其原文留存；
> 讀 01b 作業項 3 者，其預期值以本條為準。

```text
R-U8  Recon 閘值與判準（取代 01b_tasks.md 作業項 3 之預期值）
      三個閘一律以 Categorization 欄之逐列計數為單位：
        functional_requirement_count == 180
        heading_count == 25（欄值等於 "Heading" 者，非 len(headings)=27）
        out_of_scope_count == 2
      葉節點 182 之 ID 前綴形態值降為對照輸出，不作閘。
      依據：Comfort R-C3 逐字禁止以 ID 形態判定 leaf，
      recon.py:568 已將其標為 "the heuristic that the ruling BANS"；
      canon §5a 第 17 條「既有政策優先」。
      生成母體維持 180，不變。
      **本條之成因為下放包之誤**：01b 同時寫入「leaf = Categorization
      以 Functional 起始」與「葉節點 182、扣 2 得 180」，兩者單位不同，
      在該判準下 182 不可能量得。A-UP07 判定成立，執行層停下為正確。

R-U9  Pop Up List 來源
      以 features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A
      (Dec 15, 2023).xlsx（SHA b0827f02…，見 Comfort BASELINE.sha256）
      為候選，先驗本 feature 引用之 20 個 PU id 之涵蓋率再採用。
      採用後比照 Comfort R-C11 移入 spec-index/ 作單一來源，
      不在各 feature inputs/ 各留一份。涵蓋不全才轉 DR 索取。
      A-UP06 之處置以本條為準：素材未必缺，先驗再說。

R-G3  framework.md §Workbook sync 之範例程式碼（全域）
      該節範例為 openpyxl + wb.save()，對 rev C 工作簿會摧毀 R 欄
      x14 dataValidation（A-UP09 實測：節點 1→0、zip members 48→47、
      而 P／T–Z／AF 三條 legacy DV 存活，表面像無害重封裝）。
      須於該節加禁用警示，並將範例改寫為 xlsx_surgical splice。
      屬跨 feature 缺陷，非 User Profiles 專屬。

R-U10 A-UP08 —— 採 (b)
      rev C 起 `Test Case Framework` 分頁不列為交付要求；
      framework.md §Workbook sync 之該項改標「rev A/B only」。
      理由：rev C 為現行官方表單且無該分頁，該分頁係 Media 時期
      工作流產物，非 STLA 表單要求。不因此產生新 DR。

R-U11 A-UP05 —— 結案為「歷史記載失效」
      20260816_ext 之 mtime 2026-08-17 09:45:54，15 秒後另存為
      20260817_ext；容量擴充（B 欄 601→1411）發生於 FORMS.md 記載之後，
      故原記載之量測對象已不存在。FORMS.md 維持雙欄並列，原記載留為歷史。
      **記載限制**：本條依 Pei 裁定結案，**非經成因查證確認**。
      兩者不同，不得日後被引為「成因已查明」。

R-U12 歸檔三檔之雜湊保護
      於 archive/forms_superseded/ 建 BASELINE.sha256，涵蓋三檔。
      理由：R-G2 保住了檔案，雜湊卻只記於 FORMS.md；
      而 R-U6 之 style authority（Home 225 列工作簿）正倚賴其中一份。
      保住檔案與保住雜湊是兩件事。
```

**執行層回報（第二輪，2026-08-17）**

- **R-U8**：`feature.yaml` 之 `recon_assertions` 三閘已由 `TBD` 改填
  180／25／2；182 之 ID 前綴形態值標為對照輸出。**recon 本身未跑** ——
  037 仍不在 repo（DR #1），作業項 6 之前置未成立。
- **R-U9**：涵蓋率實測 **18 / 20**，缺 `PU1087`、`PU1088`。
  依 02b 作業項 2 之明文「不足 → 具名列出缺哪幾個 id，轉 DR，
  **不以近似版本替代**」——**未移入 `spec-index/`、未更新 BASELINE、
  A-UP06 不結案**，已開 **DR #4**。量測條件見上繳包 §2。
- **R-G3**：`docs/fw036/framework.md` §Workbook sync 已加禁用警示
  （引 A-UP09 實測表）並將範例改寫為 `xlsx_surgical` splice。
- **R-U10**：同節之 `Test Case Framework` 分頁項已改標 **rev A/B only**。
  A-UP08 RESOLVED，未產生新 DR。
- **R-U11**：A-UP05 RESOLVED，**其「非經成因查證」之記載限制已照錄**
  於 ANOMALIES.md 該條內。
- **R-U12**：`archive/forms_superseded/BASELINE.sha256` 已建（3 檔），
  `shasum -a 256 -c` **3/3 OK**，輸出見上繳包 §4。

---

## 第三／四輪條文

來源包：`docs/handoff/04a_rulings.md`（R-U13～R-U17，02／03 輪聊天提出，本輪首次落檔）
與 `docs/handoff/04b_rulings.md`（R-U18～R-U20、R-G4～R-G6，03 輪覆核所生）。
**R-G4／R-G5／R-G6 為全域條文**，另依既有慣例登錄於全域規則處（見本檔 §全域條文）。

```text
R-U13 .gitignore 之 archive/forms_superseded/BASELINE.sha256 例外
      —— 追認（內容成立），程序補正。
      追認範圍僅限本次已作之單行例外與其註解改寫，不及其他。
      明訂：版控政策一律先裁後改；執行層不得以「某條裁決之必然結果」
      推導出對 .gitignore／入庫範圍／tag 之授權。
      成因兼含分析層起草不全（R-U12 未處理追蹤狀態），一併留檔。

R-U14 A-UP09 之解除條件
      文字修補不構成 RESOLVED。解除條件 = 機器檢查存在且實跑：
      對產出檔驗 x14:dataValidation 節點數與 zip member 集合，
      比對來源母本（可借 Comfort write_back §3.3 之同型 assertion）。
      **該 gate 立起並實跑前，本 feature 之寫回實作不得開工。**
      A-UP09 維持 PENDING。

R-U15 DR #4（PU1087／PU1088）之阻斷範圍
      非 Phase 1 阻斷，recon 與 framework 不受其擋。
      阻斷範圍限於 spec 4.1.1（Profile Setup）之 popup 引用：
      該章相關 TC 於 DR #4 到齊前不生成，不得以鄰近 PU id 推定內容
      （§8.4.1 禁止捏造）。
      索取標的：載有 PU1087／PU1088 之 Pop Up List 版本。
      現有 SR24 Post 2A (Dec 15, 2023) 已驗為正確文件家族、
      兩缺者落在編號區間內（PU0001–PU1578，空號 248）——
      即「不是版本不對，是這一版沒有這兩列」。

R-U16 037 採認
      inputs/ 之 037（SHA 9d176dde…）為本 feature 之權威需求來源。
      Phase 0 之全部 037 側數字係分析層於 Project 附件副本上量得，
      未與本檔比對雜湊，一律重測不沿用。
      BASELINE.sha256 依 R-C20 比照更新，涵蓋 inputs/ 全部檔案。
      （執行層 03 輪已完成，6/6 OK。）

R-U17 inputs/ 之 spec 副本處置
      兩份 R1L-R 已驗為逐位元組相同（SHA 368d5874…）。
      依 Comfort R-C11 單一來源原則：由 Pei 刪除 inputs/ 副本，
      spec 引用路徑維持 spec-index/。刪除屬不可逆，執行層不得代勞。
      **反對意見已記錄**：執行層於 03 包 §5 主張兩份各自受檢
      正是日後任一份被改動時會出聲的機制，合併會關掉該能力。
      該意見未被採納；若日後改採雙份併存，須以新條文取代本條，
      不得以「當時有人反對過」為由逕行回退。

R-U18 A-UP04 → RESOLVED
      037 已落 inputs/，SHA 9d176dde… 入 BASELINE，
      三閘 180／25／2 相符，表頭列實得 row 7。
      **記載限制（永久）**：Project 附件副本不在 repo，
      其與 inputs/ 這份之同源性永不可證。
      故 Phase 0 之 037 側數字非「被複驗」，是「被取代」；
      日後不得以「Phase 0 已驗過」為由跳過重測。

R-U19 135 / 133 分立
      data/expected_cited_sections.tsv 維持 135 列
      （記「037 引用了哪些」，該記載正確，不改）。
      另立生成集合 133（扣 4.7、5.11 —— 該二 outline 之唯一引用者
      為 R-U4 排除之 PROF-017／035），作為覆蓋率分母與 batch 排程依據。
      兩數不得互相取代；引用時一律具名是哪一個。
      R-U3 之證據行「135 個 section id 缺漏 0」仍為真，
      但它不是覆蓋率的分子。

R-U20 Layer 2 定案 —— 採 B 案，8 個 Test Set
      Preference Storage (ch4, 28)
      Profile List        (ch5, 40)
      Defaults            (ch6, 11)
      Welcome Flow        (ch7, 14)
      Setup Flow          (ch8, 25)
      Editing             (ch9+ch10, 25)
      Connected Account   (ch11, 6)
      Valet Mode          (ch12+ch13+ch14, 31)
      合計 180。
      **命名判準**（解執行層自陳之不一致）：§4.2 禁止的是重複
      Test Group 之「整體」—— 即不得出現 "User Profiles xxx"；
      單一詞 Profile 在承載能力語義時允許。
      故 Profile List 成立；ch6 取 Defaults、ch7 取 Welcome Flow
      （去 Screen／Popup 之 UI widget 名）。
```

### 全域條文（R-G4～R-G6，於本包首次落檔）

```text
R-G4  recon.py 之輸出檔名歸屬（全域）
      recon.py 之 leaf→section 產物一律寫
      data/recon_leaf_to_section.tsv；不得寫 spec_id_to_outline.tsv
      （後者歸 build_outline_map.py，內容為 spec 側索引，兩者不同物）。
      並加前置檢查：腳本不得無聲覆寫既存之 tracked 檔，
      偵測到即中止並報告，不自行備份、不自行還原。
      **改動 recon.py 前**須先查 features/home 之 lint_tcs.py 與
      make_batch_context.py 實際讀的是哪一種內容，確認後才動。
      成因：本 feature 先建 spec 側索引才跑 recon，順序與
      home／comfort 相反，後者遂無聲覆蓋前者，git status 僅顯示 M。

R-G5  git 禁令之正面條款（全域，重申並擴充）
      「全部 git 操作屬 Pei」包含還原、回退、checkout、restore、
      stash、clean。
      追認 03 輪已作之 git checkout（結果正確，被丟棄者已另存為
      data/recon_leaf_to_section.tsv）；追認範圍僅限本次單一檔案。
      **遇覆寫事故之正確作法**：兩版皆保留（改名並存）、上報、停手，
      不自行還原。理由：checkout 丟棄工作區變更且不可救回，
      執行層無從確知該檔是否另有未提交之他人變更。
      本條與 R-U13 為同一失效模式之第二次發生（前次為 .gitignore）：
      以「某條裁決之必然結果」自推授權。

R-G6  上繳包之記載一致性
      03 包 §7.1 記「git checkout 還原」而 §8 記「git 未執行」，
      同份文件互相矛盾。§8「本包所動之檔」須含 git 動作，據實更正。
      往後「未執行 git」一語須與全文動作清單逐項對得起來；
      摘要與內文不符者退回，不予核可。
```

**執行層回報（04 輪，2026-08-17）**

- **R-U13／R-U15／R-U16／R-U17**：追認與範圍已知悉。**R-U17 之刪除未執行**
  —— 屬 Pei，執行層不代勞（04c §不在授權範圍）。`inputs/` 之 spec 副本仍在，
  BASELINE 之該列亦未動。
- **R-U14**：A-UP09 維持 PENDING；**寫回實作本輪未開工**，x14 DV gate 未立。
- **R-U18**：A-UP04 已改 RESOLVED，其**永久記載限制已照錄**於該條內。
- **R-U19**：已另立 `data/generation_sections.tsv`（133 列），
  `expected_cited_sections.tsv` **未改**（仍 135 列）。
- **R-U20**：八個 Test Set 已落 `feature.yaml` 之 `layer2`；合計實測 180。
- **R-G4**：前置查證已完成（見上繳 04 §7），`scripts/recon.py` 已改名並加
  「不得無聲覆寫既存 tracked 檔」之前置檢查。
- **R-G5**：**本輪全程未執行任何 git 指令**，含 checkout／restore／stash／clean。
- **R-G6**：`docs/upstream/03_recon.md` §8 已據實更正，§7.1 未動。

---

## 第五輪條文

來源包：`docs/handoff/05a_rulings.md`（Pei 2026-08-17 裁定，04 輪覆核所生）。
**R-G7 為全域條文**。

```text
R-U21 Service 欄之地位
      Sub Categorization == "Service" 不作為阻斷判準。
      22 條全數納入生成母體。
      判讀依據：R-C38 之判準為「無任何介面可觀察端」，而 22 條全部
      有可觀察端（直接可觀察 9、需來回一趟 13），C 群為 0。
      Comfort 之唯一成員 044-02 為物理量而非介面量，本 feature 無同形者。
      B 群 13 條之測法採「設定 → key cycle／切換 → 讀回」結構，
      依 §5.6 建立 baseline 與比較步驟。
      **此為測法之形狀，非阻斷** —— 03 輪所擔心之「一整章返工」不成立。

R-U22 PROF-001-01（PLP 表）之處置 —— 先驗可讀性，不逕列阻斷
      該 leaf 本文即寫 "listed in PLP table"，即 Req 自身引用該表，
      故 spec 3.1–3.5 屬其 in-scope 依據（§8.6 原始 spec 優先），
      不受 A-UP02「037 未引用」所限 —— **037 沒引用不等於 spec 沒寫**。
      先查 spec 3.1–3.5 之文字可讀性：
        可讀   → 該 TC 正常生成，specification_reference 併列 4.1 與 3.x，
                 偏好清單以 spec 原文為據，不列舉未載之項（§8.4.1）
        不可讀 → 才進 DR
      並據此重估 A-UP02 之性質：若 3.1–3.5 可讀，
      其為「spec 有而 SWE 未涵蓋」，非「內容不存在」。兩者處置不同。

R-U23 spec 8.2 之處置 —— 先驗抽取能力，再決定 DR
      「完全依賴圖」之判讀依據為 outline_map 之文字欄僅含 (image: …)
      標記，而本層未嘗試自 xlsx 抽出內嵌圖片。
      Comfort A-CF23 之結論為「不是缺件，是缺讀取能力」。
      故先試抽 8.2 之內嵌圖：抽得出且可判讀則不開 DR，
      抽不出或判讀不能才開。同一作法適用於「部分依賴」5 節
      （4.6、6.2、9.1、10.2、11.4）。

R-U24 跨 feature 之 spec_id_to_outline.tsv 現況掃描
      授權對 comfort／sxm／amfm／projection 之該檔作**唯讀**掃描
      （欄名、列數、第一欄形態），判斷是否已被 recon 形狀污染。
      唯讀 —— 不得寫入他 feature 任何檔案。
      發現污染者逐一具名上報，處置另裁。
      home 之實跑驗證：以 **repo 外複本**進行（複製 features/home 至
      tempfile 目錄後跑 recon），不得對 repo 內之 home 執行。
```

### 全域條文（R-G7，於本包首次落檔）

```text
R-G7  反向驗證之對照組（全域慣例）
      任何注入式反向驗證須含一個「什麼都沒做」之對照向 ——
      即「複製並以同一工具重存但不改任何資料，檢查仍全綠」。
      缺此向者，其餘各向之紅燈無法區分係注入所致或工具所致，
      **該組驗證不予採認**。
      來源：執行層 04 包 §4 之自陳（該向原不在其設計內，
      寫到一半才意識到沒有它另外三向證明不了任何事）。
```

**執行層回報（05 輪，2026-08-17）**

- **R-U21**：已知悉，22 條納入生成母體；`generation_sections.tsv` 之分母不因此改變
  （該檔以 section 為單位，非以 leaf）。
- **R-U22**：**PLP 表可讀**（spec 3.1–3.5 之逐項清單於 PDF 文字層完整抽出）。
  故 `PROF-001-01` 正常生成，A-UP02 之性質重估為「spec 有而 SWE 未涵蓋」。
- **R-U23**：**抽取能力有，且 6 節中 5 節改判**。詳見上繳 05 §4，
  含 04 包 §6 分類之前後對照。
- **R-U24**：四個 feature 唯讀掃畢，**未寫入他 feature 任何檔**。
  **comfort 為 recon 形態但非污染**（其從未有 build_outline_map，
  且全部文件一致記載為 403 leaf 查表）。
  home 之 recon 實跑**做不到** —— 其 `inputs/` 不存在（R-G2 條文自身所記之事實）；
  改以「直接餵兩種形態給 home 三個讀者」觀察，危害已由推導變為觀察。
- **R-G7**：本輪之讀者實驗含兩個對照向（原檔逐字、原檔重寫），兩者一致。

---

## 第六輪條文

來源包：`docs/handoff/06a_rulings.md`（Pei 2026-08-17 裁定，05 輪覆核所生）。

```text
R-U25 spec 基線之修訂 —— xlsx 為結構、PDF 為內文
      R-U3 之證據（Source ID namespace 一致、135 id 缺漏 0）證明的是
      **結構完整**，非**內文完整**。兩者當時被合為一件，於此分開。
      spec 基線改為：xlsx 提供 outline 結構與 Source ID，
      PDF 提供條文內文與圖形內容；兩者為同一基線之兩面，
      皆已在 BASELINE.sha256 內。
      **前置作業（優先於 framework 定稿）**：對 169 條逐節比對
      xlsx Description 與 PDF 文字層，量出 export 之掉句率與形態。
      若為系統性掉句，outline_map.json 須以 PDF 重建，
      且 04／05 輪之全部判讀須標示其依據面。
      成因：05 輪 §7 第 2 項自陳——PDF 之條文比 xlsx export 完整，
      而本 feature 自 recon 至 framework 之全部判斷皆建於 xlsx 側。

R-U26 spec_popup_ids 之擴充
      由 20 擴為 32，加 `source` 欄標 `xlsx_text`／`pdf_only`。
      原 20 列之記載不刪 —— 它記的是「xlsx Description 欄掃得者」，
      該記載正確，只是涵蓋範圍小於其類別。
      12 個 pdf_only id（PU0575–0579、0586、0587、0609、0612、0614、
      1497、1511）須逐一定位其所屬 section；05 輪只比了集合差。

R-U27 R-U15 之阻斷範圍收窄
      spec PDF p6 已載 PU1087／PU1088 之觸發條件，
      DR #4 所缺者僅為 Pop Up List 中該二列之 popup **內文**。
      故 4.1.1 相關 TC **得以生成**：觸發條件、顯示與否、流程分支皆可驗；
      **僅 popup 內文之逐字 ER 不寫**，該處以 spec 原文之描述為據，
      不推定內容（§8.4.1）。
      PROF-002-03 據此解除阻斷。DR #4 降為 MEDIUM，不再擋章節。

R-U28 A-UP02 / DR #3 之性質重估
      3.1–3.5 有內容且可讀 → A-UP02 非「內容不存在」，
      而是「spec 有而 SWE 未涵蓋」，形態同 Comfort R-C16。
      處置分兩支：
        3.1–3.5      依 R-U22 得作為 PROF-001-01 之 in-scope 依據，
                     不另生成獨立 TC（我方不自造需求）
        10.1/11.1/11.2  變體覆寫條款且無任何 SWE 需求，不生成 TC，
                     列 RD-1 之上游覆蓋缺口
      DR #3 仍送出，性質改為「上游覆蓋缺口」而非「索取缺件」。

R-U29 PLP3（Memory Seat Module）再試一次
      p5 有 11 張點陣圖，PLP3 之列項可能在點陣圖內而非向量文字層。
      以 pdfimages 抽該頁圖後視覺判讀，再定可讀與否；
      仍不可讀才進 DR。
      理由：Memory Seat 連動屬 R-U21 之 B 群測法，
      該清單缺項會直接影響 PROF-001-01 之 ER 範圍。

R-U30 comfort 孤兒檔之處置 —— 延後，登記不動手
      R-G4 生效後 comfort 若重跑 recon，產物將落新名，
      而其 RUNBOOK／INDEX／RULINGS／DECISIONS 四處仍指舊名。
      comfort 已交付，實務上不會重跑，故不於本輪動它。
      登記為跨 feature note，待 Comfort 下次開輪次一併清。
      **本 feature 不得寫入 comfort 任何檔。**
```

### R-G4-1 —— R-G4 之修訂（**R-G4 原文不改，保留其漏數之痕跡**）

> **06b 作業項 1 明文**：不得逕行改寫 R-G4 原文 ——
> 其「兩個讀者」是當時的記載，**保留才看得出漏數發生過**。
> 故 R-G4 之區塊維持原樣（見本檔第三／四輪條文段），本條列於其後。

```text
R-G4-1 R-G4 之修訂 —— 讀者為三個
      `spec_id_to_outline.tsv` 之讀者除 `lint_tcs.py`、
      `make_batch_context.py` 外，尚有
      `features/home/scripts/extract_exemplars.py:97`，
      其用法同 make_batch_context（load_outline_to_chapter → chapter_of），
      受同一危害。原條文之「兩個讀者」為漏數，據實更正。
```

**執行層回報（06 輪，2026-08-17）**

- **R-U25**：169 條全掃完成，**判定為系統性 → 依 06b 作業 3 停手上報，
  未重建 `outline_map.json`**。逐節結果落 `data/xlsx_pdf_audit.tsv`。
- **R-U26**：`spec_popup_ids.tsv` 已擴為 **32 列**，加 `source` 欄；
  原 20 列之 `refs`／`sections` 記載未改。
- **R-U27**：`PROF-002-03` 之阻斷已解除；DR #4 降 MEDIUM 並改寫索取標的。
- **R-U28**：A-UP02 已改記，兩支處置分列；DR #3 性質改為上游覆蓋缺口。
- **R-U29**：**PLP3 可讀，且不需 `pdfimages`** —— 其列項一直在 PDF 文字層，
  05 輪未定位到是因版面順序使其落在 `3.5` 之段落內。
- **R-U30**：已登為本 feature `ANOMALIES.md` 之跨 feature note，
  **comfort 一個檔都沒動**。
- **R-G4-1**：已置於 R-G4 之後，R-G4 原文未改。

---

## 第七輪條文

來源包：`docs/handoff/07a_rulings.md`（Pei 2026-08-17 裁定，06 輪覆核所生）。
**R-G8 為全域條文。** 06 輪之停手判定成立，未重建為正確。

```text
R-U31 outline_map.json 之處置 —— 增欄，不取代
      **駁回整份以 PDF 重建。** 理由為執行層自身之證據：
      PDF 切段已證實會誤吃相鄰內容（3.1–3.5 並排表、11.5 之 Table CPA2、
      10.3.1 吃進 10.1 全文），且 PLP3 之列項排在其標籤**之前** ——
      文字層順序不等於 outline 順序。
      以一個已知會誤切之來源整份取代一個已知會少句之來源，
      是換一種錯法，不是修好。
      作法：
        1. outline_map.json 增 `pdf_text` 與 `divergence` 兩欄；
           原 `text` 欄（xlsx 側）保留不動
        2. 判讀基準依 R-U25 以 PDF 為準，xlsx 側供追溯與比對
        3. 另立 `data/xlsx_missing_clauses.tsv` 補句表，逐條登記真掉句
           （現為 9.8、9.3.2、9.1、11.4 四條），欄含 outline、掉句原文、
           查證方式（全 169 節語料查無）、影響之判讀
        4. **全量列出 PDF 中 10 條 `**` 起首之註記**，逐條標示 xlsx 側
           有無（現測 6 有 4 無），四條缺者一併入補句表
      第 4 項之必要性：9.3.2 所掉者為 "Stellantis Account" →
      "Connected Account" 之變體覆寫，屬 §8.7.3 直接管轄；
      掉了就會寫出錯的 label。故不得只補已發現之四條。

R-U32 Service 22 條之 PDF 複查
      R-U21 裁定「22 條全數納入生成母體」，其判讀全建於 xlsx
      Description，而 06 輪證明該側可能少句。
      22 條逐條以 PDF 文字層複查其可觀察端是否仍成立。
      任一條之分群因此改變者具名上報；
      R-U21 之結論視結果修訂或維持，**不預設維持**。

R-U33 29 個無標籤之節納入比對
      該 29 節不入分母，故自始未被檢查過。
      以章節位置（而非條款標籤）定位其 PDF 段落，
      量其有無內容、有無掉句。其中含章 3（PLP 表章）與各章標題。

R-U34 「條款不跨頁」之假設須反向驗證
      該假設之依據為 140 個標籤全數與 xlsx 起首相符 ——
      **那證明的是起首，不是結尾。**
      若有條款跨頁，其續頁部分會被當成下一節之殘留而不計入掉句，
      故 2.9% 現為**下界**而非量值。
      驗法：取每節 xlsx Description 之結尾句，
      查其是否出現於 PDF 之次頁頁首；有命中者即為跨頁條款，
      掉句率須重算並重報三個比率（含各自之分子定義，見 R-G8）。
```

### 全域條文（R-G8，於本包首次落檔）

```text
R-G8  比率之判準揭示（全域慣例）
      任何以比率呈現之量測，須同時載明「它把什麼算成分子」。
      06 輪同一份資料先後得 17.1%／9.3%／2.9%，三者皆非計算錯誤，
      而是三種分子定義（無頁界切段／加頁界／逐條查證後之真掉句）。
      **缺判準之比率不予採認，等同未量測。**
      來源：執行層 06 包 §7 之自陳。
```

**執行層回報（07 輪，2026-08-17）**

- **R-U34（最優先）**：跨頁反向驗證完成，**未發現任何跨頁條款**。
  唯一候選 `5.1` 經查為**重複標籤**所致之定位錯（`PRACC7.` 被 `4.7` 與
  `5.1` 共用），非跨頁。另補一道與 xlsx 無關之盲點檢查（頁末斷句 ＋ 次頁小寫續起），
  **0 / 20 個頁界命中**。故 2.9% **不再是下界**；訂正後之三個比率見上繳 07 §2。
- **R-U31**：`outline_map.json` 已增 `pdf_text`／`divergence` 兩欄，
  **原 `text` 欄逐字未動**（實測：`text` 鍵仍在，169 節齊）。
  補句表 `data/xlsx_missing_clauses.tsv`（7 列）與
  `**` 註記全量表 `data/pdf_starred_notes.tsv`（10 條，**6 有 4 無**，與下放包所測相符）已落檔。
- **R-U32**：22 條逐條以 PDF 複查，**18 相同、4 標點/空白差異、0 條落在掉句清單**。
  **R-U21 之結論維持** —— 而其依據面自此為 PDF 側，不再是未量之邊。
- **R-U33**：29 節全數比對完成，26 節於 PDF 命中、3 節查無（`2.1`／`10.1`／`11.2`）。
- **R-G8**：本輪之每個比率皆附其分子定義。

---

## 第八輪條文（Phase 1 收尾）

來源包：`docs/handoff/08a_rulings.md`（Pei 2026-08-17 裁定，07 輪覆核所生）。

```text
R-U35 補句表七條之回填
      (a) 生成階段之 spec 內文一律以 outline_map 之 `pdf_text` 為準
          （R-U25）；`text`（xlsx 側）僅供追溯，不作判讀依據。
      (b) 補句表七條登記為 **must-carry**：逐條指定其歸屬 outline、
          影響之欄位（ER 列舉／PU 清單／label 字面值），
          於該 outline 之 TC 生成時強制納入 prompt context。
      (c) 9.3.2 之變體覆寫（"Stellantis Account" → "Connected Account"，
          R1 High Only）進 feature profile 之 variant 清單，
          並立 lint 規則：R1 High 適用之 TC 字面值不得出現
          "Stellantis Account"。
          §8.7.3 管轄 —— 屬**字面值錯誤**，非風格分歧。
      (d) 11.4／11.5／p17 之 Table CPA2 列項、p14 之 Table EDPR1 列項
          為 ER 列舉之來源，登記其 PDF 出處頁次供生成時回查。

R-U36 字內斷字之全量掃描
      8.7 之 `spa ces` 形態於 07 輪僅在對照向撞見一例，
      其普遍程度未量。若 PDF 文字層普遍有此形態，
      逐字比對會有一批假陰性，C 組之 3.6% 仍偏低。
      全量掃 21 頁文字層，量此形態之出現節數與字元數，
      據此重報 C 組（附分子定義，R-G8）。

R-U37 相似度消歧之反向驗證
      兩處重複標籤之消歧結果經人讀過認為正確，
      惟未注入「故意選錯」之案例證明該機制會挑對。
      注入至少一組人工構造之近似段落，
      證明 difflib 消歧會選中正確者；
      選錯即為缺陷，**須改判準而非改案例**。
      R-G7 之精神及於定位機制本身。

R-U38 2.1 之處置 —— 不試抽，登記為 R-U25 之已知例外
      2.1（Reference Documentation 表）屬 spec 章 2，不入生成範圍，
      試抽之效益不足以償其成本。
      惟其為「xlsx 較 PDF 完整」之**唯一實測案例**，
      登記為 R-U25 分工原則之已知例外，
      使日後不得將該原則陳述為無例外之通則。
```

### R-G7-1 —— R-G7 之修訂（**R-G7 原文不改**）

> 08b 作業項 1 明文：置 R-G7 之後並標明修訂關係，R-G7 原文不改。
> 其原文見本檔第五輪條文段。

```text
R-G7-1 R-G7 之修訂 —— 對照向之第二用途
      對照向除區分「紅燈來自注入或來自工具」外，
      亦用於驗證**定位／抽取機制本身**之正確性。
      對照向未達全綠者（07 輪為 131/139），
      須逐項追因至具名成因，**不得以「多數命中」通過**。
      來源：07 輪之重複標籤缺陷（PRACC7. 為 4.7／5.1 共用）
      係對照向之副產品，非任何作業指示所求。
      R-G7 原文不改，本條置其後並標明修訂關係。
```

**執行層回報（08 輪，2026-08-17）**

- **R-U36**：**本條之前提有誤，據實更正** —— 字內斷字**全在 xlsx 側**（4 個形態：
  `aft er`／`know n`／`program med`／`spa ces`），**PDF 側 0 個**。
  07 輪本層寫「PDF 文字層有字內斷字」為誤，於本輪自查發現。
  其對 C 組之影響為 **0** —— 四者所在之 4 節皆已落「標點/空白差異（不算掉句）」。
  **C 組終值維持 3.6% 節數／2.1% 字元。**
- **R-U37**：**注入抓到判準之缺陷。** 第一版之相似度比對為「`want[:300]`
  對 `窗口[:300]`（窗口取 600 字元）」，兩候選之窗口長度不同 ——
  落在前面之候選其窗口吃進後一個候選之文字，ratio（2M/T）被 T 撐大而降低。
  兩個注入向（正確者在前／三候選在中）因此選錯。
  **依 R-U37 改判準（等長窗口），不改案例** —— 改後 8/8 PASS，
  且稽核表逐位元組未變（真實語料剛好不踩該缺陷，故非注入驗不出來）。
- **R-U35**：(a) `__meta__` 已標 `text` 為追溯用；(b) 補句表加 `must_carry`／
  `affected_field`；(c) variant 清單與 lint 規則已落地並**實跑，7/7 PASS**
  （含造假 TC 之三向與「R1 Low 不得誤報」之範圍向）；(d) PDF 出處頁次已登。
- **R-U38**：`2.1` 已登為 R-U25 之已知例外（`outline_map.json` 之 `__meta__`）。
- **R-G7-1**：本輪之三組反向驗證皆含對照向，且 8/8、7/7 全綠，無待追因項。
