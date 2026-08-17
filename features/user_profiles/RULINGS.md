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
