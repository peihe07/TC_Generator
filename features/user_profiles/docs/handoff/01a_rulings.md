# 01a 下放包 — User Profiles 裁決條文（Pei 2026-08-17 裁定，逐字）

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

## 本包產生之新條文清單（自檢）

- R-G1 ✓ 以區塊形式出現
- R-G2 ✓ 以區塊形式出現
- R-U1 ✓　R-U2 ✓　R-U3 ✓　R-U4 ✓　R-U5（修訂版）✓　R-U6 ✓　R-U7 ✓
