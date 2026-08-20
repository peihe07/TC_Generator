# User Profiles — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案）：scaffold／R-G1 R-G2 R-U7 form 處置／recon／outline map／framework 草案 | [handoff/01_intake.md](handoff/01_intake.md)＋[01a_rulings.md](handoff/01a_rulings.md)＋[01b_tasks.md](handoff/01b_tasks.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-G1、R-G2（全域，本包首次落檔）；R-U1 ~ R-U7（本 feature） | A-UP01 ~ A-UP03（下放包播種，A-UP03 本輪 RESOLVED）；**A-UP04 ~ A-UP09 新開** | **作業項 1／2／4(spec 側)／5(草案)／6 完成；作業項 3 停下 —— 037 不在 repo（A-UP04）＋ 預期值單位不一致（A-UP07）。相符 18／不符 4／未實測 12（4 項待裁）** |
| 02 | 2026-08-17 | 02a 裁決之落地：R-U8 三閘／R-U9 PU 涵蓋驗證／R-G3＋R-U10 canon 修補／R-U12 歸檔雜湊／異常狀態 | [handoff/02a_rulings.md](handoff/02a_rulings.md)＋[02b_tasks.md](handoff/02b_tasks.md) | [upstream/02_rulings_execution.md](upstream/02_rulings_execution.md) | R-U8、R-U9、**R-G3（全域）**、R-U10、R-U11、R-U12 | A-UP05／07／08 **RESOLVED**；A-UP09 修補完成待覆核；**A-UP06 不結案** | **作業 1–5 完成；6–8 未執行（DR #1）。R-U9 涵蓋率 18/20 → 不採用、開 DR #4** |
| 03 | 2026-08-17 | Recon 開工（DR #1 到齊）：037 採認前置／R-U8 三閘／037 側複驗／BASELINE／spec 同一性／Layer 2 草案二版 | [handoff/03_recon_start.md](handoff/03_recon_start.md) | [upstream/03_recon.md](upstream/03_recon.md) | （未產生新裁決；R-U13 ~ R-U17 仍待裁）| A-UP02 於 **037 側首次證實**；A-UP04 解除條件已滿足**待裁** | **作業 1–6 全部完成。三閘 180／25／2 相符；集合對集合 135＝135 差集皆空；BASELINE 6/6 OK；兩份 spec SHA 相同（未處置）** |
| 04 | 2026-08-17 | 記載更正、十一條入庫、四項實質查證（三閘反向驗證／Service 22 條／14 節帶圖／R-G4 前置） | [handoff/04a_rulings.md](handoff/04a_rulings.md)＋[04b_rulings.md](handoff/04b_rulings.md)＋[04c_tasks.md](handoff/04c_tasks.md) | [upstream/04_verification.md](upstream/04_verification.md) | R-U13 ~ R-U20；**R-G4／R-G5／R-G6（全域）** | A-UP04 **RESOLVED**；A-UP09 維持 PENDING（R-U14 定其解除條件）| **作業 1–7 全部完成。三閘反向驗證 6/6；`Service` 22 條無一符合 R-C38；14 節帶圖 = 不依賴 8／部分 5／完全 1；R-G4 已實作＋反向驗證 5/5。本輪未執行任何 git** |
| 05 | 2026-08-17 | 跨 feature 掃描（唯讀）／home 讀者實驗／抽圖能力／PLP 表／framework 草案 | [handoff/05a_rulings.md](handoff/05a_rulings.md)＋[05b_tasks.md](handoff/05b_tasks.md) | [upstream/05_framework_draft.md](upstream/05_framework_draft.md) | R-U21 ~ R-U24；**R-G7（全域）** | A-UP02 之性質重估待裁（spec 有而 SWE 未涵蓋）| **作業 1–6 完成。無污染；危害由推導變觀察（chapter 6 種→1 種 `SWE`）；**圖在 PDF 不在 xlsx**，6 節中 5 節改判、完全依賴歸零；PLP 表可讀；framework 草案落檔** |
| 06 | 2026-08-17 | 基線稽核：169 條逐節比對 xlsx vs PDF；PLP3；PU id 擴充；R-U27／R-U28 落地 | [handoff/06a_rulings.md](handoff/06a_rulings.md)＋[06b_tasks.md](handoff/06b_tasks.md) | [upstream/06_baseline_audit.md](upstream/06_baseline_audit.md) | R-U25 ~ R-U30；**R-G4-1**（R-G4 之修訂，原文保留）| A-UP02 性質重估落地；**N-XF01 跨 feature note 新開** | **判定系統性掉句 → 停手上報，未重建 outline_map.json。掉句率三個數：17.1%（上界）／9.3%（加頁界）／**2.9% 真掉句**。PLP3 可讀且不需抽圖。framework 未定稿** |
| 07 | 2026-08-17 | 基線稽核（二）：跨頁反向驗證／29 無標籤節／outline_map 增欄與補句表／Service 22 條 PDF 複查 | [handoff/07a_rulings.md](handoff/07a_rulings.md)＋[07b_tasks.md](handoff/07b_tasks.md) | [upstream/07_baseline_audit_2.md](upstream/07_baseline_audit_2.md) | R-U31 ~ R-U34；**R-G8（全域）** | —（無新開；補句表登記 7 條）| **0 個跨頁條款 → 2.9% 不再是下界。對照向揪出 06 輪之定位器缺陷（重複標籤 `PRACC7.` 被兩節共用）。三比率重報 17.1%／9.3%／**3.6%**。Service 22 條 0 條改變 → R-U21 維持。framework 仍未定稿** |
| 08 | 2026-08-17 | **Phase 1 收尾**：字內斷字全量掃／消歧反向驗證／R-U35 落地與 lint 實跑／framework 定稿 | [handoff/08a_rulings.md](handoff/08a_rulings.md)＋[08b_tasks.md](handoff/08b_tasks.md) | [upstream/08_phase1_close.md](upstream/08_phase1_close.md) | R-U35 ~ R-U38；**R-G7-1**（R-G7 之修訂，原文保留）| —（無新開）| **兩個作業都推翻了自己的前提**：R-U36 之「PDF 側有斷字」為 07 輪誤述（實在 xlsx 側，C 組終值維持 3.6%）；R-U37 之注入抓到判準缺陷，改判準後 8/8。lint 實跑 7/7。**framework 定稿待覆核**。Phase 1 收尾清單：已清 18／待清 8／永久 8 |
| 09 | 2026-08-17 | **條文收斂**（Phase 2 開工前）：A 類升 canon／C 類標 superseded／AUTO 範圍明列 | [handoff/09a_rulings.md](handoff/09a_rulings.md)＋[09b_tasks.md](handoff/09b_tasks.md) | [upstream/09_ruling_consolidation.md](upstream/09_ruling_consolidation.md) | R-U39 ~ R-U41；**R-G9（全域）** | —（無新開）| **canon 新增 §9（十一項通則＋R-G 集中）。異議兩項：C 類三條只有一部分被取代、A 類升格單位應為「原則」。**第四類有 1 條：R-U8**。未生成 TC** |
| 10 | 2026-08-17 | **Phase 2 開工前置**（上繳於 11 輪補落檔，R-U48）：標記修正／R-U45 落地／組裝自檢／pilot 取樣／PLP 前置掃描 | [handoff/10a_rulings.md](handoff/10a_rulings.md)＋[10b_tasks.md](handoff/10b_tasks.md) | [upstream/10_pilot.md](upstream/10_pilot.md) | R-U42 ~ R-U45；**R-G10（全域）** | —（無新開）| **前置 1–3 完成：六條標記改訖（`[SUPERSEDED]` 全稱用例 0）、`outline_map.json` 納入版控且 `shasum -c` 7/7、自檢 6/6（第 1 項判準改三版）。取樣 16 leaf 餘數 0（PROF-045 → 048）。PLP 掃描三讀法：甲 2／乙 4／聯集 4 → **停下待裁**，未生成 TC** |
| 11 | 2026-08-17 | **R-U46 落地 ＋ 10 輪補落檔**：PLP 聯集判準／位置指涉盲區 17 條人工判讀／must_carry 追蹤登記 | [handoff/11a_rulings.md](handoff/11a_rulings.md)＋[11b_tasks.md](handoff/11b_tasks.md) | [upstream/11_plp_and_pilot_prep.md](upstream/11_plp_and_pilot_prep.md)＋[upstream/10_pilot.md](upstream/10_pilot.md)（補落檔）| R-U46 ~ R-U48；**R-G11（全域）** | —（無新開）| **`PLP_ENABLED = True`；聯集 4 ＋ 人工 2 = 6。盲區掃描命中 17／未命中 163／餘數 0，其中 3 條指向 PLP 表。兩項具名回報：`001-02`／`001-03` 同節連坐、must_carry 實為「覆蓋 4／未覆蓋 3」（R-U47 前提為 3／4）。發現 `p17` 掛不回任何節之缺陷，未自行修改。自檢 6/6（第 6 項已加對照向）。未生成 TC** |
| 12 | 2026-08-17 | **p17 掛回（先紅後綠）／AUTO 集可重算性／`052f67d` 三案重述** | [handoff/12a_rulings.md](handoff/12a_rulings.md)＋[12b_tasks.md](handoff/12b_tasks.md) | [upstream/12_p17_and_commit.md](upstream/12_p17_and_commit.md) | R-U49 ~ R-U54 | —（無新開）| **R-U49 四步俱附輸出：第 7 項自檢先紅（`p17` 無歸宿，exit=1）→ 改 `PAGE_TO_SECTION` → 8/8 PASS。連帶 T-3 已解，待追蹤剩 T-1／T-2。R-U52 之對照向 drop／add 兩向皆紅。**`052f67d` 三案查無包號節次 —— 提於 power session 之聊天，從未落檔，故與 R-U41 相符、非分析層漏回應**；且該 commit **已推送**＋其後 4 個提交，案 2／3 之代價已變。未生成 TC** |
| 13 | 2026-08-18 | **Pilot 生成 16 條 ＋ p17 ＋ 052f67d（同輪）** | [handoff/13_pilot_run.md](handoff/13_pilot_run.md) | [upstream/13_pilot_generated.md](upstream/13_pilot_generated.md) | —（本包無裁決條文，屬分析層自裁）| —（無新開）| **首次生成：`generated/` 16 檔 / 16 條 TC，`NR1L-UserProfiles-001…016`。lint 全綠：`lint_tcs`（本輪新建）語料 0 違規、self-test **28/28**；`lint_variant_labels` 反向 7/7、語料 0（並證其對 TC-011 確實生效，非空過）；`--selfcheck` 8/8。判準歧義 **6 次依門檻續行**並具名。發現 3 項缺陷：**`feature.yaml` 之 PU 清單為 xlsx 側（PU0609 誤報）**、9.8 之 PU0609 無 037 leaf、`variant_of()` 不處理否定。lint 判準改三次（G6／G2／G14），皆改判準不改案例。`052f67d` 其後提交 4 → **5**，時效性成立** |
| 14＋15 | 2026-08-18 | **pilot 覆核之修正（D-1～D-5／S-1／N-1～N-3）＋ `052f67d` 處置** | [handoff/14_pilot_review.md](handoff/14_pilot_review.md)＋[15_commit_disposition.md](handoff/15_commit_disposition.md) | [upstream/14_pilot_fixes.md](upstream/14_pilot_fixes.md) | R-U55；**R-G12（全域，升 canon）** | **A-UP10 新開（ACCEPTED）** | **三項阻塞全清**：TC-002 priority P2→P0（連帶再改 2 條，分布 P0×6／P1×6／P2×4）、TC-004 指名 PLP 3.5 之記憶座椅項、TC-003／013 之 ER 展開為實際列項。D-4 補 G15 步驟長度閘：**紅 14 處**（非覆核所列之 3 處）→ 改寫 14 個步驟 → 綠；G9 隨 §6.1 子層改判準。D-5 popup_ids 20→21 並補 **G16 防再度分岔**。N-1 否定判讀已修（TC-013 不再誤判）、N-2 **PDF 複位揭出 `p17` 掛錯節** → 改掛 11.4＋11.5，「歸宿正確」納入自檢並以 `misplace` 證其會紅、N-3 取樣清單落 `data/pilot_sample.tsv`。lint 37/37、variant 9/9、selfcheck 8/8、語料 0 違規。**本輪未執行任何 git（連 status 都未跑）** |
| 16 | 2026-08-18 | **pilot 覆核（二）：F-1～F-4 ＋ 第一批取樣清單** | [handoff/16_pilot_review2.md](handoff/16_pilot_review2.md) | [upstream/16_pilot_review2.md](upstream/16_pilot_review2.md) | —（本包無裁決條文）| —（無新開）| **F-1** TC-013 移除 11.5（頁面共置≠章節歸屬），全批引用複核：`REF_EXTRA` 2 條皆逐字出現於 ER，PLP `3.x` 併列 2 條採「條文對象讀」未改但**具名待裁**。**F-2 判讀成功** —— 關鍵不是抽圖而是**向量版面重繪**：Table CPA2 為 **4 列非 5 列**（「Connected Profile App」是註解框不是表列）、欄別全部判定、**中國市場排除為列級非表級**。14 輪之「永久限制」判定**撤回**。**F-3** P0 tie-break 記 D-UP16-01 並於 R-U5 末加註（條文未改）；**F-4** 記 D-UP16-02。lint 37/37、variant 9/9、selfcheck 8/8（三向 tamper 皆紅）、語料 0 違規。**第一批取樣：ch9→10→11 共 27 leaf ＋ PROF-111 之 R1 High 反面（28–34 條 TC），批次邊界落在 Editing 與 Connected Account 兩個 Test Set 之完成點**。未生成。**本輪未執行任何 git** |
| 17 | 2026-08-18 | **ER 出處對照（55 句）＋ 第一批生成（28 條）＋ 版面判讀工具** | [handoff/17_batch01.md](handoff/17_batch01.md) | [upstream/17_er_provenance.md](upstream/17_er_provenance.md)＋[upstream/17_batch01.md](upstream/17_batch01.md) | —（本包無裁決條文）| —（無新開）| **B：55 句 ER 逐句對照** —— 逐字 9／改寫 20／推得 8／無出處 18（步驟回聲 14 ＋ **真缺口 4**）。四個真缺口集中兩形態：`ignition cycle`（其權威是 R-U21 非 spec）、**BVA 之界前基準線**（29 秒／第 9 次，spec 未述）。並挖出**反向引用問題**：TC-010 倚賴 5.1.1 卻未引用，已補。**A：J-1 代價句入 `DECISIONS` ＋ `framework` §4.1（覆蓋率不得以引用欄推定）；`render_spec_region.py` 落為工具，回歸 7/7，且發現欄別可由座標機器判定**（勾記為同一 PNG 置放 5 次）。**C：第一批 28 條（017–044），ch9→11 之 27 leaf ＋ PROF-111 負向配對。`lint_variant_labels` 擋下 2 條 —— 擋的是我自己的 `remarks` 寫了禁用字面值**，改案例後 44 條全綠。9.5.x 四條之 sibling 軸只差一個變數；ch10 三條先驗皆 Low 而判出 P2／P3 兩級。**本輪未執行任何 git** |
| 18 | 2026-08-18 | **來源標示、第一批 ER 對照（77 句）、J-6 雙向自檢、第二批取樣** | [handoff/18_provenance2.md](handoff/18_provenance2.md) | [upstream/18_provenance2.md](upstream/18_provenance2.md)＋[upstream/18_batch02_sample.md](upstream/18_batch02_sample.md) | —（本包無裁決條文）| —（無新開）| **J-4** pilot 五處於 reasoning 標示來源（方法／裁決），ER 文字未動；第一批之方法／裁決句數為 **0**。**J-5 揭出三條範圍層級錯**：p14 之 `****R1 High` 為**列級**（Table EDPR1 之該列），而 TC-011／023 把它當整條 TC 之條件（無故限縮到 R1 High 車）、TC-020 用了別節之變體 label —— 三條已修。**J-6 落為 G17（多引）／G18（少引）**；G18 首跑紅 5 條（`Edit Profile` 分頁名），改以自我查核之 `UI_LOCATORS` 登記表處置，不逐條灌引用欄。全批 44 條：60 個節次引用全部登記在案、字面值全部溯得到源。lint 44/0、self-test **44/44**。**第二批取樣：ch12–14 共 29 leaf，估 ≈34 條（未逾 40 故不分批）；must_carry 待追蹤實測為 0**。**本輪未執行任何 git** |
| 19 | 2026-08-18 | **J-7～J-12 落地 ＋ 第二批 29 條（語料 73）** | [handoff/19_batch02.md](handoff/19_batch02.md) | [upstream/19_batch02.md](upstream/19_batch02.md)＋[upstream/19_provenance3.md](upstream/19_provenance3.md) | —（本包無裁決條文）| **A-UP11 新開（PENDING）** | **J-10 兩次首跑各抓到一筆我自己的多引**（TC-022 之 provides 不符、TC-072 之 12.6 沒被用到）——G17 舊版「有登記就綠」擋不住。G18 擴及數值／PU／狀態值後另紅 5 條，皆判準未涵蓋（BVA 界前值、`steps 1 and 2` 互參、狀態值大小寫）。**J-11** variant 判定改只掃條件欄，禁用字串仍及 remarks。**J-12** 第四類「測試設置」落地。**`134` 之 R-U51 判讀首次受檢：結論成立、理由有誤** ——`above` 不可能指 ch14（14.1 即首條），實指 12.3.1，已補引用。**A-UP11：037 之 12.8／12.8.1 標題與描述整體錯位**，本批依 description 生成。第二批實得 **29 條**（估 34，差額為 §7 對照置於同一 TC）。語料 73 條違規 0、self-test 51/51、variant 11/11。**本輪未執行任何 git** |
| 20 | 2026-08-18 | **第一批覆核之修正（C-1～C-6）** | [handoff/20_batch01_review.md](handoff/20_batch01_review.md) | [upstream/20_batch01_review_fixes.md](upstream/20_batch01_review_fixes.md) | —（本包無裁決條文）| —（無新開）| **C-1** TC-039 之 ER 以 `render_spec_region.py` 讀出 **Table PIP1 之 15 列**逐列補入 ——工具在本案例上**紅了兩次，皆判準錯**（格線起點差 0.3pt 被整條排除；零寬矩形之 `Rect &` 恆為 empty），且**兩次都以「這張表沒有欄」之形狀失敗**。連帶發現 `****` 為列級，補 pre-condition 免 R1 High 假失敗。**C-2** TC-036 由 BVA 改功能測試（無 limit±1）；全批 BVA 自檢母體實為 **7 條非 6 條**（第二批之 TC-066 亦是），改判 1 後餘 6 條**皆有邊界對與界前基準線**。**C-3** TC-044 之 ER2 改為可觀察之缺席；**C-4** 偏好儲存之 P0／P2 分野寫入 D-UP16-01 附一；**C-5** TC-040 改述不改級。**19 包作業 1–6 已於上一輪完成，未重做**（順序差異之影響逐項查證）。語料 73 條違規 0。**本輪未執行任何 git** |
| 21 | 2026-08-18 | **R-U5 適用釐清、指代掃描、一致性抽查、40 條覆核包** | [handoff/21_consistency.md](handoff/21_consistency.md) | [upstream/21_consistency.md](upstream/21_consistency.md)＋[upstream/21_review_pack_40.md](upstream/21_review_pack_40.md) | —（本包無裁決條文）| —（無新開）| **K-1** R-U5 五類為例示非窮盡，加註入 R-U5（條文未改）＋ D-UP16-01 附二；另立「**防線成立本身 → P0／其回饋與呈現 → P2**」細則（TC-021 與 TC-022 同節相鄰而判級不同）。**改判 8 條**，P0 由 17→24（32.9%），依 J-9 未回調判準；**其中 5 條屬我自行推廣，具名待覆核**。**K-2** 採 (b) 逐列標適用條件；`Electric Vehicle` 一列 spec 未標 `(if applicable)`，**保留歧義、空白即記載**。**K-3** 指代掃描 0 處（首跑 2 處為行內逗號列舉之偽陽性）；**盲區補足先證其抓得到 C-1 原句**再掃，全批無第三例。**K-4a** 3 處中 2 處判準錯、**1 處真陽性**（TC-047「找不到一個東西不是非法操作」→ 改功能測試）；**K-4b 首跑 13 處全部不是缺陷** —— 判準測的是「用字在不在我的詞表裡」而非相斥，已改測相斥。作業 6 產出 40 條覆核全文（含 spec 原文）。**本輪未執行任何 git** |
| 22 | 2026-08-18 | **方括號閘、互指之委派、變體對造判準（語料 78）** | [handoff/22_review_fixes.md](handoff/22_review_fixes.md) | [upstream/22_review_fixes.md](upstream/22_review_fixes.md) | —（本包無裁決條文）| **A-UP12 新開並 RESOLVED** | **L-1 採 (a)** 立 §11 之 profile 例外，**與 G19 同生** —— 閘不是禁令是**對照**（方括號 token 須逐字溯得到被引之節）；5 案中最關鍵者為「**同一 token、換一個被引之節 → 須紅**」，守的是「對照來源而非 token 白名單」。**L-2 核出兩者非同一語意**（`connected profile feature` vs `connectivity`），**且連帶發現這是一組互指之委派** —— 9.2 稱由 11.3 承擔、11.3 稱由 9.2 承擔，**兩個缺口同時存在且兩份記載都看起來已交代**，補 `TC-077`／`TC-078`；順帶全量掃描「由…承擔」21 處，分**已存在／未取樣之承諾／假委派**三類。**L-3 立 V-1**：觸發要件為「spec 有明文覆寫註記」而非「另有一種配置」，母體取 `pdf_starred_notes.tsv` 之 4 條；**原本只配了 1 個 axis**，補 `074`／`075`／`076`。**「理由須不適用於已配者」做成述詞由閘實測，首跑即抓出兩處述詞錯**。語料 73→78，全閘綠。**本輪未執行任何 git** |
| 23 | 2026-08-18 | **profile 檔補建、委派可驗化、覆寫母體擴掃、35 條覆核包** | [handoff/23_delegation.md](handoff/23_delegation.md) | [upstream/23_delegation.md](upstream/23_delegation.md)＋[upstream/23_review_pack_35.md](upstream/23_review_pack_35.md) | —（本包無裁決條文）| **A-UP13 新開（PENDING）**；**A-UP11 結案** | **M-1** 補建 `FW036_R1L_UserProfiles_Profile.md`；**移入者只有 D-UP22-01**（canon §11 明指其載體），其餘八條**重述而不搬移** —— 搬走裁決條文會使裁決失去權威載體。**M-2** 委派改指名 leaf，落 D-1／D-2／D-3 三閘；**D-3 判準倒了兩次**（回看窗把 leaf id 切在窗外；單詞比對讓 23 包點名之案判綠 —— 差別在**詞的組合**不在詞）。**黃清單掃出另兩處假委派（A-UP13）—— 是「黃」抓到的不是「紅」**：`TC-005`／`TC-007` 把行為推給鄰節，而那些行為**寫在本節自己的條文裡**。**M-3** 擴掃 14 處全判；**真正的漏不在 `**` 而在 `kind` 欄** —— 兩條 R1 High 覆寫有 `**`、也在 TSV 裡，卻被歸為「圖／表內標籤」。母體 4→6 axis，新增 `pending` 絆線。**M-6** A-UP11 全 180 leaf 掃畢，偵測器**未被告知即重現已知四條**，新候選 3 條逐條複讀皆偽陽性 —— **範圍確認僅 12.8／12.8.1，承前四輪結案**。**M-5** 037 無 9.1.1 另一側之 leaf，而**同一份 037 在 8.8 卻切了兩側** → RD #7。語料 78 條未變（**A-UP13 之三個行為具名延後生成**）。**本輪未執行任何 git** |
| 24 | 2026-08-18 | **需求單位判準、判級對調、全稱 ER 收斂（A-UP11 降級）** | [handoff/24_review_close.md](handoff/24_review_close.md) | [upstream/24_review_close.md](upstream/24_review_close.md) | —（本包無裁決條文）| **A-UP11 降為記載瑕疵（不關閉）** | **P-4**（阻塞第三批之前置）以 180 leaf 全量實測定判準：**Description 為需求單位、Title 為索引標籤** —— Description 以條款編號起首者 105/180 而 **Title 為 0/180**；決定性論證是**只有 Description 能無重疊無缺漏地分割條文**，若以 Title 為單位則 PVAL8 之「狀態列互動受限」無 leaf、手套箱提示有兩個，且 `125-03` 之 Title 所指行為**與該 leaf 自己的 outline 相衝**。故 **`TC-057`～`062` 不重生成**。**P-1** 依建議對調：`062`（變灰）P0→**P2**、`063`（按下不生效）P1→**P0** —— §8.7.4 逐字「視覺狀態不蘊含不可操作」，**變灰是指示不是機制**；並更正「取中」之做法（判級取**核心斷言**非取各 ER 平均）。**P-2** ER3 收斂至 `PU0934`；**該改動使 K-4a 轉紅，而紅的是判準** —— 補「嘗試後無作用」之措辭且**刻意不放寬到純缺席斷言**（護欄案例守住溢出）。**P-3** 改 remarks 不補列 12.6（補列會被 G17 判多引）—— 其成因是 19 輪改對引用欄卻未同步改 remarks，**與 C-2 同形之再犯**。語料 78 條未變，全閘綠。**本輪未執行任何 git** |
| 25 | 2026-08-18 | **Q-1 反向掃描、G20、A-UP13 歸屬更正、第三批取樣清單** | [handoff/25_batch03_sample.md](handoff/25_batch03_sample.md) | [upstream/25_batch03_sample.md](upstream/25_batch03_sample.md) | —（本包無裁決條文）| —（無新開）| **覆核結清 78/78。A-1** `075` 加引號，並補 **Q-1 反向掃描**（G18 只查引號內字面值，查不到「該加而未加」）—— 7 處待判**皆非缺陷**（行為敘述與 spec 措辭相同，非顯示值）。**第八處 `TC-039` 之同一串字**逼出一條界線：**散文內嵌之顯示文字加引號／逐列轉錄之表格內容不加** —— 該界線**語料早已一致遵循**（`013` 之標題加、四列不加），本輪只是寫下來並落為判準；**其為歸納非 canon 明文，已具名待明示**。**A-2** 立 **G20**（`remarks` ↔ `specification_reference`）—— C-2 與 P-3 同形已兩次；**只取「宣稱有引用」之語境**，否則閘會逼人刪掉「某節為何不列」之正確說明（護欄案例守之）。**A-3 A-UP13 歸屬更正 —— 推翻我 23 輪的結論**：7.2.1 有三個 leaf，行為 2／3 **各有專屬 leaf**（`059-02`／`059-03`）只是未取樣，屬 (b) 類承諾**非覆蓋缺口**；成因是 23 輪查了條文卻**沒查該節有幾個 leaf**。**B** 第三批 = ch4 剩餘 **26 leaf**（實測相符）＋ 3 附掛，估 **30 條**（`079`–`108`），三項必含逐條具名（(b) 類兌現 2/5、`009` 之全稱須配負向、**變體 axis 為 0 且這是查過的**）。**本輪未執行任何 git** |
| 26 | 2026-08-18 | **R-U56 範圍界定入庫、DR 拆分、範圍語句連帶掃描** | [handoff/26_scope.md](handoff/26_scope.md) | [upstream/26_scope.md](upstream/26_scope.md)＋[upstream/26_rd_queries.md](upstream/26_rd_queries.md) | **R-U56（Pei 裁定，feature-level）** | **A-UP02 改 OUT-OF-SCOPE（記載不關閉）** | **R-U56 逐字入庫**：037 之 180 leaf 母體即範圍上界，**spec 有內容而 037 未切 leaf 者不生成 TC、不列缺口、不索取**。**DR #3／#7 改 CLOSED — OUT-OF-SCOPE，全部實測記載保留**（3.1–3.5 可讀之證據、與 Comfort R-C16 之形態比對、「8.8 切兩個而 9.1.1 切一個」之佐證），並明記**3.1–3.5 之使用不受影響**（仍為 `PROF-001-01` 之 in-scope 依據）——**關閉的是「向上游索取」，不是那些條文的可用性**。**#5／#6 改獨立送出**，並補一條可檢驗之送出門檻：**答案會改變已生成之內容**。**作業 4** 全批掃描命中 **3 處，改述 1 處**（`TC-012` 之 PU0609 句）；**`TC-005` 之「覆蓋缺口」判為 R-U56 不適用** —— 該行為寫在 `048` 自己的 description 裡（SWE 有切、已取樣），**是我方覆蓋不足非範圍問題；一併改掉等於用範圍裁決掩掉自己的缺口**。**作業 5** 出英文可寄版（含座標複位證據與「答案不同會導致什麼」），A-UP11 列附錄並標明 **for information only**。**本輪未執行任何 git** |
| 27 | 2026-08-18 | **RD 查詢單 v2（對外文件三處修正）＋ ch4 清單指路** | [handoff/27_rd_review.md](handoff/27_rd_review.md) | [upstream/27_rd_queries_v2.md](upstream/27_rd_queries_v2.md)＋[upstream/27_rd_review.md](upstream/27_rd_review.md) | —（本包無裁決條文）| —（無新開）| **X-1** 附錄之 `seven` 與表列 4 條不符 —— 採「列全七條」並**分兩表**（4 條錯置／3 條一致），比下放包所給之兩案多一步：**把沒問題的三條也列出來，對方才不必回頭查**；另更正 `125-01`／`125-02` 之「一致」實為「只涵蓋描述之一部分」。**X-2** 刪去未經證明之 `shifted by one position` —— 七條實查顯示**兩組互相取用，非單向 +1**；並**明寫我方不主張模式**（「證據無法顯示是否出自單一編輯操作」），比留白更不易被讀成疏漏。**X-3 採納**：檔名與 Source ID namespace 並列並附驗證（169 列全落 CR24798 namespace、135 個 section id 命中 100%）—— 兩識別差**八個月**，只給檔名會讓對方先要求更新文件再回答，**兩題各多耗一個往返**。v1 加 **WITHDRAWN** 標頭留檔。**ch4 取樣清單已出於 25 包 §B**（26 包 §6 只寫「已完成」未指路）——**不另出**，並自陳往後回報前輪項目須一併寫落點。語料 78 條未變、腳本未動。**本輪未執行任何 git；RD 查詢單未寄出（Tier 3 屬 Pei）** |
| 28 | 2026-08-18 | **第三批 30 條落地（語料 108／leaf 100）＋ 對外文件最小閘** | [handoff/28_batch03_go.md](handoff/28_batch03_go.md) | [upstream/28_batch03.md](upstream/28_batch03.md)＋[upstream/28_provenance4.md](upstream/28_provenance4.md) | —（本包無裁決條文）| —（無新開）| **第三批 ＝ ch4 剩餘 26 ＋ `009` 負向配對 1 ＋ A-UP13 附掛 3 ＝ 30 條**（`079`–`108`，**批界依 R-4 如此寫，不寫「＝ ch4」**）。**`005` 之順序斷言**：「切回還在」證不了「存在載入之前」——**能分開兩者的是 ER2**（B 顯示的是 B 自己的值，非 A 之變更），兩條 ER 併存才構成順序斷言。**生成時被閘擋下 7 處皆我方之錯**；其中 G18 之兩處**判定是對的**（條文確實沒給座椅編號），處置為登記測試設置＋於 TC 內具名，**不是放寬閘**。**R-1 對外文件最小閘**：v1 判準**對它所為之文件本身誤報兩處**，收兩道後 v2 綠而 v1 缺陷仍紅 —— 兩個誤報案例已納為**護欄**。**K-4a 紅 4 條逐條判**：三條補詞表（delete／customize／select driver profile），**`103` 改判功能測試**（按鈕 highlight 是條件式呈現非狀態機遷移），另補「只讀取不得算狀態轉換」之護欄。**出處對照抓到閘抓不到者**：G18 只掃 ER 不掃 pre_conditions，`100` 之 `“Driver 2”` 溯不到 4.5.4（該節寫 `Driver 1-2`），已改用本節寫法而**未另引 4.5.1**。**本輪未執行任何 git；RD v2 未寄出** |
| 29 | 2026-08-18 | **G18 擴及 pre_conditions、第三批覆核包、第四批取樣（含剩餘批次全數落位）** | [handoff/29_pack_and_sample.md](handoff/29_pack_and_sample.md) | [upstream/29_pack_and_sample.md](upstream/29_pack_and_sample.md)＋[upstream/29_review_pack_30.md](upstream/29_review_pack_30.md) | —（本包無裁決條文）| —（無新開）| **S-1** G18 擴及 `pre_conditions` 之**引號內**字面值（非引號之設置描述不掃）；**首跑紅 0，並先證其非空掃** —— 母體 10 個字面值逐一列出溯源，其中 `100` 之 `“Driver 1-2”` 正是 28 輪出處對照抓到而閘當時看不見者，**同型缺陷自此由閘承擔**。另**自我加窄一層**：未擴未加引號之數值（其登記機制為 ER 而設，貿然擴會產生只為轉綠而生的登記）。方向性 ＋4（**含護欄：非引號設置描述不得轉紅**），共 64/64。**作業 2** 出 `29_review_pack_30.md`（743 行 30 條，檔首另列生成時四項先具名處置之落點）。**作業 3** ch5 餘 38 leaf、估 **40 條逾 40**，**建議按 spec 自己的條款家族切分**（5.12 起由 `PRACC` 變 `ALLPR`）：第四批 25 leaf ≈26 條、第五批 13 leaf ≈14 條。**pending 兩 axis 與 (b) 類三處具名兌現批次**（`046`／`047` → 第六批；`065`／`073-02`／`073-03` → 第七批），並附**剩餘 80 leaf 全數落位之四批規劃**。另具名 `044`（5.15.1）依賴**基線外之 Core HMI 文件**。**本輪未執行任何 git；RD v2 未寄出** |
| 30 | 2026-08-18 | **T-1：`TC-101` 之基準線修正與「step N 引用」全批自檢** | [handoff/30_review_batch03.md](handoff/30_review_batch03.md) | [upstream/30_review_fixes.md](upstream/30_review_fixes.md) | —（本包無裁決條文）| —（無新開）| **T-1** `TC-101` 步驟 1 改為記錄圖示、ER1 改記錄式（ER1 之「按鈕存在」斷言保留 —— 兩者不可互換）。**連帶自檢命中 18 處紅 1**（即該條）。**最該記的是判準本身**：v1 寫成「該步驟有無 record／read 動詞」，而 `TC-101` 步驟 1 正好有 `Read` —— **v1 判它綠，而它正是本包點名要抓的那一條；照 v1 回報會寫成「紅 0」且通過所有閘**。v2 改抓**被比較之物**（具體物須見於該步驟／泛稱退回查動詞），首跑紅 4，其中 3 處為 `as`／`those` 之抽取誤判，補功能詞表後紅 1。**兩次都是判準錯，語料只有一處真缺陷。** 方向性 ＋4（含護欄「泛稱不得要求字面相符」與「引用之步驟不存在」），`audit_consistency` 29/29。**自陳**：本閘抓不到反向形態（步驟建立了基準線而 ER 從未用它），該形態本輪未查。**第四批未生成** —— 待取樣清單覆核且 17 條讀畢。**本輪未執行任何 git；RD v2 未寄出** |
| 31 | 2026-08-18 | **U-1 多觸發 popup 之分支綁定、U-2 反向形態掃描** | [handoff/31_review_batch03b.md](handoff/31_review_batch03b.md) | [upstream/31_review_fixes2.md](upstream/31_review_fixes2.md) | —（本包無裁決條文）| —（無新開）| **U-1** `TC-082` 之 ER3 併驗「該設定已回到預設」以綁定成功分支 —— 4.1.1 有**兩句**都指向 `PU1088`（成功／未確認），只驗 popup 顯示則兩分支皆過。全批自檢**命中 3 處，真缺陷 1**：`002` 綠（其綁定在**另一條 ER** ＋ procedure 之情境注入）、`031` 綠（兩句是**同一觸發被記載兩次**，非兩分支）。**本掃描列為「待判」是刻意的** —— 綁法不只一種，硬判會使 `002` 那種正確作法轉紅。**U-2**（T-1 之反向）**判準 v1 即錯**：以 `\brecord` 比對而把**回指**之 `recorded in step N` 當成記錄動作，得 14 處假紅 —— **方向剛好相反，而它要找的正是方向**；v2 排除 `recorded` 後得 1 處（`TC-104`），判為 **ER 漏斷言**而非多餘步驟（該記錄是 §5.6 基準線，刪了會使「永遠 highlight」之實作通過），補 ER1 記錄、ER3 比對。**全批 32 處記錄動作中多餘步驟為 0。** 方向性 ＋3（含護欄，為 v1 之 13 處假紅的固化）。**本輪未執行任何 git；第四批未生成** |
| 32 | 2026-08-18 | **V-1：4.4 覆寫之發生點與時序語自檢** | [handoff/32_review_batch03c.md](handoff/32_review_batch03c.md) | [upstream/32_review_fixes3.md](upstream/32_review_fixes3.md) | —（本包無裁決條文）| —（無新開）| **V-1** `TC-091` 之序列由「熄火→開機（**ER1 已斷言 B active**）→按座椅鍵」改為「熄火→按座椅鍵並開機」。**ER1 之改動是關鍵** —— 原 ER1 **把本 TC 要證明「不會發生」的那件事寫成已發生的事實**；現改為「B 是上次之 profile」。ER3 斷言 A 為**起始** profile 且 B 未被載入，序列自此與同節之 `TC-090`（key fob）同構。**原序列還與 `TC-086` 重複**（測到的是「按座椅鍵可切換 profile」，那是 4.3 已覆蓋者）。**實車限制依令入 remarks**：若座椅鍵僅能於 ignition on 後按，則「起始 profile」不可觀察，須回報而**不得以「先開機再按」充當覆寫之驗證**；本 TC **不假定**該鍵可於 key-on 前按，只要求不晚於。**時序語全批自檢命中 13 條，真缺陷 1** —— 逐條判出**同一個詞的三種身分**（真時序／位置／在 popup 文字內），故列「待判」而非紅（硬判會使 `035`／`003` 轉紅）。方向性 ＋2（含護欄：無時序語者不得列入，否則清單等於全語料）。**本輪未執行任何 git；第四批未生成** |
| 33 | 2026-08-18 | **W-1：pre-condition 之循環（第三批覆核結案 30/30）** | [handoff/33_review_close3.md](handoff/33_review_close3.md) | [upstream/33_review_close3.md](upstream/33_review_close3.md) | —（本包無裁決條文）| —（無新開）| **W-1** `TC-094` 之 pre `Every Profile has been deleted` **兩重問題**：4.5 逐字載全部刪除後車上**恆有**一個預設 profile，故該前提所述之穩態**系統不允許存在**；且其蘊含之結果（只剩 Driver 1）**正是本 TC 之 ER**。刪除移入 procedure（比照 `093`），pre 改述刪除**前**之狀態。修正後兩條 **procedure 相同、ER3 不同** —— `093` 驗**重建發生**（且為預設值非改名留下），`094` 驗**重建後只有一個**。**完成式 pre 全批自檢命中 4 處，循環 1**：`093`／`104`／`005` 皆為正當**佈署**描述而保留；**修正後之 `094` 其 pre 仍是完成式，而那是對的** —— 判準是「該狀態是不是 ER 要斷言的東西」，不是「有沒有用完成式」。方向性 ＋2（含護欄）。**四輪四種對應關係**（步驟↔ER、斷言↔分支、步驟↔條文時序、**前提↔ER**）全部由人工覆核先發現；四支掃描有三支只能「待判」—— **可測的是「有沒有」，不可測的是「指的是不是同一件事」**。**本輪未執行任何 git；第四批未開** |
| 34 | 2026-08-18 | **第四批 26 條落地（語料 134／leaf 125）** | [handoff/34_batch04_go.md](handoff/34_batch04_go.md) | [upstream/34_batch04.md](upstream/34_batch04.md)＋[upstream/34_provenance5.md](upstream/34_provenance5.md)＋[upstream/34_review_pack_26.md](upstream/34_review_pack_26.md) | —（本包無裁決條文）| —（無新開）| **條數更正**：下放包沿用我 29 輪之措辭錯誤 —— `041-04` 屬 5.13.2（**第五批**）且本身就是 leaf，不是額外造者；本批為 **25 leaf ＋ 1 額外造者 ＝ 26 條**。**生成時被閘擋下 6 處皆我方之錯**；其中 `TC-115` 之 G18 **判定正確**（5.2 以**指涉**帶入 PRACC7.2 字串），處置為 `REF_EXTRA` 併列 5.1.2（D-3／C-1 同型**第四例**）——**連帶發現 `_ref_allowlist` 只讀三支批次，第三、四批之登記讀不到**，若未擴則「補了引用反而更紅」。**五支對應關係掃描生成後即跑**：T-1／U-2／W-1 各 0；U-1 新增 3（PU0588 之兩句為**同一觸發記載兩次**）、V-1 新增 2（5.2 之 `before` 在 **popup 文字內**）皆判綠。**K-4a 3 處為判準漏詞**（`save`／`select … Driver Profile` 皆真狀態遷移），補詞並保留 `open`／`read` 之護欄。**`audit_delegation` 三處紅：兩處我用錯「承擔」一詞、一處是閘本身的 bug** —— `phrase_of` 把詞串中間 ≤3 字母之詞靜靜丟掉，**22 包那個要抓的案例一直是為錯的理由紅的**；v4 修正後該案例仍紅（這次為對的理由）。**另發現 `TC-003` 之 ER 越出其 leaf**（涵蓋 `021-02`／`021-03` 之內容），**本輪未改，具名待裁**。**本輪未執行任何 git；RD v2 未寄出** |
| 35 | 2026-08-18 | **X-1 跨節 popup、X-2 受檢畫面、review pack 拆檔** | [handoff/35_review_batch04.md](handoff/35_review_batch04.md) | [upstream/35_review_fixes4.md](upstream/35_review_fixes4.md)＋[upstream/35_review_pack_26a.md](upstream/35_review_pack_26a.md)＋[upstream/35_review_pack_26b.md](upstream/35_review_pack_26b.md) | —（本包無裁決條文）| —（無新開）| **X-1** `TC-128` 之步驟 2 正是 5.10.1 之觸發條件（**PU0588 會跳出來問**），原 procedure 未提它 —— **結果取決於測試者按了什麼**；加「選 No」並於 **ER2 併驗該 popup 出現**（否則「該詢問是否發生」未被斷言，而它正是 5.7 與 5.10.1 之接縫）。**全批自檢之 v1 得 60 處，等於沒有範圍** —— 多為主題重疊（`valet/mode/vehicle`）；v2 改**登記表式**（觸發動作 ＋ **成立條件**兩者皆命中），得 7 → 修正後 6，**逐條判無進一步缺陷**。**並立一條分類判準**：X-1 之真正判準不是「會不會跳 popup」，是「**跳出來之後測試者是否必須做一個會改變結果的決定**」—— PU0588 是決策型（必須處理），PU0580 是資訊型且 5 秒自行消失（不必）。**X-2** `TC-134` 步驟 2 之「outside」不是測試者能執行的位置，改為指名兩個受檢畫面並於 reasoning 具名其為**抽樣非窮舉**。**作業 3** review pack 拆為 `26a`（109–121）／`26b`（122–134）各 13 條。**本輪未執行任何 git** |
| 36 | 2026-08-18 | **Y-1 全稱限制之反向、配對宣稱自檢、孤兒下放包之來歷** | [handoff/36_review_batch04b.md](handoff/36_review_batch04b.md) | [upstream/36_review_fixes5.md](upstream/36_review_fixes5.md) | —（本包無裁決條文）| —（無新開）| **Y-1 採 (a)**：`TC-117` 之 ER3 加 `the “Edit Profile” tab is not opened` —— 選取另一 profile 之兩個必然結果（切換／不進入編輯）**同一觸發**，依 §5.7 併於同一條；若採 (b)，其 procedure 會與 `TC-117` 逐字相同而只有 ER 不同，**那是把同一次操作寫成兩條**。`TC-121` 之 remarks 改指**ER 行號**。**配對宣稱全批自檢命中 18 處，指錯 2 處** —— `TC-096` 指 `104`（實為 4.6.3 之 `016`）、`TC-127` 指 `133`（實為 5.10.1 之 `034-03`），**兩處都是我在 tc_id 尚未指派時寫下的號碼，且兩處都通得過現有的閘**（D-1 只認「由…承擔」句型，D-2 只驗被指者存在）——**A-UP12 之同型**。落 **Y-1 掃描**：配對兩條須屬同一 leaf 群（可測之必要條件），跨群者列待判。**自檢副產品**：`TC-073` 仍寫「rubric 無安全帶」，**21 輪 K-1 改了 `089`／`116` 而漏了它**，判級不變、依據補正為 §10.2 safety。**作業 2**：`20_batch03.md` 為**一份未被執行之 20 輪下放包**（mtime 早 `20_batch01_review.md` 兩分鐘、其上繳標的不存在）；**五項作業中四項已由後續包以不同編號重新提出並完成**，唯一遺漏為 **J-15 作業 3**（11 輪盲區掃描 17 條之「結論／理由」複核）。**未刪除、未加註**（下放包屬分析層之物），處置建議三項。**本輪未執行任何寫入性 git** |
| 37 | 2026-08-18 | **J-15 補做、號碼指派檢查、第四批收尾** | [handoff/37_j15_and_assignment.md](handoff/37_j15_and_assignment.md) | [upstream/37_j15_and_assignment.md](upstream/37_j15_and_assignment.md) | —（本包無裁決條文）| —（無新開）| **作業 1** J-15 作業 3 補做（36 輪查出之唯一遺漏）：11 輪盲區掃描 17 條之其餘 16 條逐條複核 —— **結論 16 條全部不變，理由更正五處**：`047`／`066` 指的是**圖**不是條文（`066` 同一句之 `not **pictured** here` 即證）、`090`／`091-01`／`091-02` 指的是 **9.3 自身之散文列舉**而非 Table EDPR1（那是 9.1 之選項順序表）、`108` 方向對但未複位（20 輪已精確化）。**並查證該錯誤理由未流入語料** —— `TC-022` 之 reasoning 寫的是「出自 9.3」，是對的；錯的只有 D-UP11-01 表裡三格。依 R-2 先例**加註不刪原表**。**作業 2** 立 `audit_assignment.py`：**號碼指派表自生成器重算，不讀 `generated/`**（A-1 為地基 —— 產物與生成器分岔則任何以產物為據之檢查都不可信），A-2 驗同句之 tc_id↔leaf、A-3 驗號碼存在。**首跑綠（0）**，並具名「0 之意義是修正生效，不是從來沒錯」；**盲區具名**：36 輪兩處正是「只寫號碼未附 leaf id」，A-2 擋不到，已納護欄。**作業 4** `TC-003` 維持現狀並於 remarks 具名核心斷言為「數目上限」；PU0580 四條 pre-condition 指定「已開啟」；**5.3.1 只有一個 leaf，其 `(if turned on)` 之關閉側依 R-U56 判 OUT-OF-SCOPE**。**本輪未執行任何 git** |
| 38＋39 | 2026-08-18 | **Z-1（`TC-110`）、R-U56 全批自檢、R-U57 入庫、label 曝險掃描** | [handoff/38_batch05_sample.md](handoff/38_batch05_sample.md)、[handoff/39_rd_disposition.md](handoff/39_rd_disposition.md) | [upstream/39_rd_disposition.md](upstream/39_rd_disposition.md)（兩輪合併，已具名） | **R-U57**（RD v2 之答覆不回頭改已生成之 TC；免除者為字面形式之返工，**不含判定翻轉**） | —（無新開） | **Z-1**：`TC-110` 採 (a) —— `per Profile` 就寫在該 leaf 自己的 037 description 內，**原記 OUT-OF-SCOPE 係誤用**，補 ER4（B profile 之分頁不受 A 之操作影響）。**R-U56 全批自檢**：立 `z1_ru56_scope` 掃描，四處 R-U56 判定中**三處為誤用** —— `TC-110`、`TC-082`（改為委派 `SWE1-HMI-PROF-002-03`），**以及我自己 37 輪對 5.3.1 之 `(if turned on)` 之判定**（改列我方覆蓋不足）。**label 曝險掃描**：餘 55 leaf 命中 2 處（5.16／`045`、8.2／`066`），兩者皆為名詞用法。**第五批取樣清單**：13 條、額外造者 0。**本輪未執行任何 git** |
| 40 | 2026-08-18 | **並行推進：第五批生成、DV gate、review pack 程式化** | [handoff/40_parallel.md](handoff/40_parallel.md) | [upstream/40_batch05_and_dvgate.md](upstream/40_batch05_and_dvgate.md)、[upstream/40_review_pack_24a.md](upstream/40_review_pack_24a.md)、[upstream/40_review_pack_24b.md](upstream/40_review_pack_24b.md) | —（本包無裁決條文） | **RD #8**（`5.13.2` 之 `PU0626` 與 `PU_0129` 是否同一個 —— 若為兩段確認則三條會假失敗，依 R-U57 不屬形式差異）| **第五批 22 條**（`135`–`156`，ch5 ALLPR 13 ＋ ch6 NOPR 9），leaf 覆蓋 **147 / 180**；額外造者 0（`041-04` 本身即 leaf，該措辭之誤已第二次出現）。**`046` 觸發 `audit_variant_pairs` 之 pending 絆線**（如設計），改判為具名不配，新增 `no-other-side-leaf` 述詞實測 base 側在 037 無 leaf。**系統性發現**：X-1 之觸發詞表只認 `select`，漏 `activate` —— 擴充後待判 6 → 22，**新增 16 處全在既有批次**，本批兩處已於生成時處理。**DV gate 立起並實跑**（`verify_dv_integrity.py`，6/6，三個注入向皆轉紅）——**A-UP09 之 R-U14 解除條件已成就**，惟不逕行改判（解除同時解除寫回封鎖）。新記兩事實：openpyxl 存回之 member 集合變動遠大於淨值 1（少 11 多 10）；`surgical_save` 之 `diff_cells` 對 TC 分頁逾 100 秒未完成。**review pack 改由 `build_review_pack.py` 產生**，不再手打轉錄。**本輪未執行任何 git** |
| 41 | 2026-08-18 | **X-1 十六條修正、動詞詞表、第六批（全覆蓋）、寫回設計草案** | [handoff/41_batch06.md](handoff/41_batch06.md) | [upstream/41_batch06_and_writeback_design.md](upstream/41_batch06_and_writeback_design.md)、[upstream/41_review_pack_33a.md](upstream/41_review_pack_33a.md)、[upstream/41_review_pack_33b.md](upstream/41_review_pack_33b.md) | —（本包無裁決條文；**A-UP09 落槌 RESOLVED**，D-UP41-01 記入） | —（無新開） | **X-1 修正 20 條**（下放包點名 16 ＋ 另四條 pre-condition 早已明定 popup 開啟者），集中於 `popup_guard.py` 一張表，X-1 待判 22 → **0**。**順帶抓出 PU0588 兩處誤報**（`004` 明寫不按存取鍵、`130` 只涉一個 profile）——補其成立條件為「跨 profile」，並發現原 `TC-128` 案例是簡化形而把成立條件簡化掉了。**動詞同義表**（`data/verb_synonyms.tsv` 41 列 ＋ `audit_verbs.py` 三項閘）：VB-2 把「詞表說 activate 會觸發 PU0580」拿去問掃描本身；**本輪立刻抓到第六批之 `Continue` 未登記**。**RD #8 依 §四逕行修正**：五條之確認步驟改為「於每一個確認 popup PU0626/PU_0129 按 Yes」，三種讀法下皆不假失敗，驗證目標未變。**第六批 33 條**（`157`–`189`，ch7 10 ＋ ch8 23）—— **leaf 覆蓋 180 / 180，全覆蓋達成**；ch8 沿用同節多 leaf 併寫，由此看出 8.4 與 8.8.1 是同一句話之兩處出現、`073-03` 之空格必須放在第十二個位置。**寫回設計草案**（未執行）：欄位對映 16 寫／不寫逐欄具名、edits 直給不經 `diff_cells`、DV 三段接點，**五項未決**（T:Z 車型欄為唯一無安全預設者）。**本輪未執行任何 git** |
| 42 | 2026-08-18 | **寫回程式、待判時效（G-A）、枚舉對照（G-B）、覆蓋率之讀法** | [handoff/42_writeback.md](handoff/42_writeback.md) | [upstream/42_writeback_impl.md](upstream/42_writeback_impl.md) | —（本包無裁決條文） | —（無新開；**未決 1 之提出屬 Pei**） | **未決 2–5 處置**：Q／AB 依 **Comfort 交付件實測**留空（非依其 yaml 宣告），輸出與台帳沿用 Comfort 形式（`output/` ＋ `DELIVERY.sha256`，**尚無 ENTRY**），換行 LF 並寫成 WB-6 之可測形式。**另發現 O／AA 兩欄同形**：`feature.yaml` 宣告 `NEW`／`PeiPYHsu` 而 Comfort 交付件實測為空，**兩 feature 皆然** —— 一併參數化預設不寫（署錯名不可補）。**`write_back.py`**：`build_edits` 直給 2646 格不經 `diff_cells`，六項寫回後檢查，**7/7 方向性案例**；`--write` 受未決 1 之閘拒絕且**無 `--force`**。**`row_order` 預設改為 `req_id`**（Comfort 96 §1 之 Pei 裁定），與我 41 輪草案不同，已具名待確認。**G-A**：43 條待判全數逐條判定並登記於 `data/pending_judgements.tsv`，判準之形改為「未結案之命中」，以 digest 守之（`audit_pending.py`，5/5）。**G-B**：`audit_enums.py`（7/7）＋ `data/enum_vocab.tsv` —— `STATE_VALUES` 對照取自 **spec 側**（候選 12 個），`UI_LOCATORS` 取自**語料側**（跨節 6 個）。**覆蓋率是分母的性質**寫入 profile §1 與 `framework.md` §4.2（含四處留白清單）。**本輪未生成、未改任何 TC；未產出任何交付件。本輪未執行任何 git** |
| 43 | 2026-08-18 | **宣告與生效之分離（G-C）、掃描存活之讀法（G-D／G-E）、T:Z 實測、寫回實跑探針** | [handoff/43_yaml_and_dryrun.md](handoff/43_yaml_and_dryrun.md) | [upstream/43_yaml_and_writeback_dryrun.md](upstream/43_yaml_and_writeback_dryrun.md) | —（本包無裁決條文） | **N-XF02 跨 feature note 新開**（comfort 之 yaml 宣告交付件不帶之兩值；comfort 一個檔都沒動） | **更正一處**：我 41／42 輪稱「T:Z 不填則 WB-5 會紅」**兩層皆錯** —— WB-5 只驗 R／P 欄，且母本該區 DV 自帶 `allowBlank="1"`；42 輪自我測試之第 ① 案本就是綠的，**結論與自己跑過的測試相矛盾而未對起來**。**作業 4 實測**：Comfort 交付件 T:Z **466 資料列逐列為空**，其 `write_back.py` 之 `NEVER_WRITE` 明列該七欄 —— **留空既有先例亦有表單許可，未決 1 不再擋交付**。**G-C**：`feature.yaml` 之 `write_back` 改為 `{value, applied, why}`，`write_back.py` 只讀 `applied: true` 者，並新增 **WB-0** 由程式驗其一致（兩條方向性案例）。**G-D／G-E** 寫入 profile §7.1／§7.2；§5 更新（封鎖已解除、不得呼叫 `diff_cells`、列序 `req_id`）。**作業 5 實跑探針**（`--probe`，產物落 scratchpad、受「不得落 `output/`」之閘）：三段接點 —— 寫回前二閘違規 0、封裝 2646 格、寫回後六項全綠。`write_back.py` 自我測試 **10/10**。**本輪未生成、未改任何 TC；未產出交付件；未執行任何 git** |
| 44 | 2026-08-18 | **AA-1：review pack 之時效；三項常規；T:Z 定為留空** | [handoff/44_pack_refresh.md](handoff/44_pack_refresh.md) | [upstream/44_pack_refresh.md](upstream/44_pack_refresh.md) ＋ [24a](upstream/44_review_pack_24a.md)／[24b](upstream/44_review_pack_24b.md)／[33a](upstream/44_review_pack_33a.md)／[33b](upstream/44_review_pack_33b.md) | —（本包無裁決條文） | **AA-1**（分析層於覆核時實測發現：pack 與語料不同步）| **pack 加語料指紋 ＋ `--verify` 過期檢查**（不符即拒絕採信；**無指紋者一律判過期**），4/4 方向性案例。**變動清單**：自原產生輪次以來僅 **5 條**有變動，全在 `24a`（`139`–`143`，來源唯一 —— 41 輪 RD #8 之處置）；`24b`／`33a`／`33b` 共 44 條**一字未動**。41 輪之 `popup_guard` 20 條不影響任何 pack（其動 `001`–`134`，pack 覆蓋 `135`–`189`）。**變動清單不用 git 取得** —— 舊值就在那份檔案裡，`--changes` 逐欄比對報到欄位層級。四份重出並帶指紋（`--verify` 皆 0 不符）；舊四份**加警語保留不刪**（記錄分析層當時讀到的是什麼）。**§二之 7 條逐條確認**：`144`／`145` 整條無變動，`140` 之依據欄（pre／reasoning）未變 → **三項觀察全部有效**；`139`–`143` 之 procedure／remarks 須以新 pack 重讀。**三項常規**寫入 profile §5.1（`why` 必填）／§7.3（「會轉紅」須指名案例）／§7.4（先查他 feature **交付件**）／§7.5（pack 時效）。**`vehicle_columns` 定為留空**，yaml 之 `why` 具名三項實測依據 —— **擋交付者現為 0**。**本輪未生成、未改任何 TC；未寫入他 feature；未執行任何 git** |
| 45 | 2026-08-18 | **AB-1 修正與全批自檢、靜態轉錄之指紋、上繳格式** | [handoff/45_fingerprints.md](handoff/45_fingerprints.md) | [upstream/45_fingerprints.md](upstream/45_fingerprints.md) ＋ [45_review_pack_24b](upstream/45_review_pack_24b.md)（重出） | —（本包無裁決條文） | **AB-1**（分析層覆核 `TC-154` 時發現：ER 未指明所讀者，其斷言恆真）| **`TC-154` 修正**：步驟 4／ER4 指名所讀者為**新建 profile**，ER 斷言其與步驟 1 所記者**相同**（carry-over），非「未改變」。**全批自檢命中 16 處**，逐條判定入登記表 —— 其中 **`TC-148` 為同型而未被點名者，一併修正**：同一句英文在 6.4 是**恆真**（該比兩個 profile）、在 6.1 是**歧義**（該比同一 profile 之兩時點）。**掃描只並排兩端不硬判** —— 16 條中 14 條之判別力在「中間那個事件」，那是句型看不見的。`audit_consistency` 方向性案例 48 → **52**；`audit_pending` 抑制 43 → **59**。**G-F**：新閘 `stamp_static_doc.py`（5/5），`27_rd_queries_v2`／`28_provenance4`／`34_provenance5` 加指紋（範圍取**全欄**，保守 —— 誤判過期只是重出一次，誤判新鮮是拿舊資料下判斷）；`26_rd_queries` **不標**（已 WITHDRAWN，標了反而像現行版）。**G-G 在建立當輪即抓到真陽性**：AB-1 之修正使 `44_review_pack_24b` 過期（`148`／`154`），**已於同輪重出**為 `45_review_pack_24b`。**G-H**：他 feature 先例須先確認**母本同一**（欄位字母與 DV 隨 revision 變動），寫入 profile §7.4。閘 16 → **17 支**，13 支自我測試全過；lint 189/0。**本輪未產出交付件；未寫入他 feature；未執行任何 git** |
| 46 | 2026-08-18 | **45 輪作業之完成回報；AB-1 修正之第二條；指紋現況** | [handoff/46_review_note.md](handoff/46_review_note.md) | [upstream/46_note.md](upstream/46_note.md)（**另立，不併入 45** —— 具名理由：不改已交出之靜態文件）| —（本包無裁決條文；**本包無新作業**）| —（無新開）| 45 輪四項作業**已於 45 輪完成**，本輪僅回報現況（語料 189／180-180、lint 0、17 支閘自我測試全過）。**指出 46 包只點名了一條**：AB-1 之修正實動 **2 條** —— `TC-154`（已點名）與 **`TC-148`（未點名，係自檢之產物）**；附其逐字差異（僅「指名所讀者」兩行，斷言方向未變），**不代覆核方認定免重讀**。**G-G 附件**：四份現行 pack `--verify` 皆 0 不符；**本輪起一併附三份靜態轉錄之 `--verify`**（補 45 輪自陳之缺口）。profile §7.5.1 收斂**重出（產出方之義務）vs 重讀（覆核方之判斷）**之分工。**獨立判斷**：覆核趨勢表所量者為「已知型之缺陷」—— 11 件中 8 件當場變成掃描，第五六批是在那些掃描存在下寫出的；表上另缺第二批，未擅自填。建議覆核表之「讀畢」欄改記**所讀之 pack 檔名**。**本輪未執行任何 git** |
| 47 | 2026-08-19 | **AC-1：欄內自相矛盾之修正與自檢** | [handoff/47_review_batch06b.md](handoff/47_review_batch06b.md) | [upstream/47_review_fixes6.md](upstream/47_review_fixes6.md) ＋ [47_review_pack_33b](upstream/47_review_pack_33b.md)（重出）| —（本包無裁決條文）| —（無新開）| **`TC-189` 之 `reasoning` 前半殘留已刪** —— 成因為 41 輪 K-4a 改判時**只替換後半句而未刪前半**（欄位與後半理由皆正確）。**新掃描 AC-1**：AC1-a（同欄 `design_method` ≥2 次）／AC1-b（「取 Y 而非 X」而 X 於同欄他處被肯定），掃 `reasoning`／`remarks` 兩欄，**全批命中 0**；四個方向性案例（含 `TC-189` 原形為紅向），`audit_consistency` 52 → **56**。**盲區具名**：同義改寫抓不到（本次靠殘留與現行句同詞）、只掃中文句式、`priority_basis` 未納（照包字面執行，未擅自擴大）。**連帶**：`TC-189` 之變動使 `44_review_pack_33b` 過期 → **同輪重出**為 `47_review_pack_33b`（第三次同型）。**INDEX 立「現行 pack 一覽」節**（§1.9）—— 六份被取代者已不易辨認。全閘重跑：**17 支自我測試全過**，語料 189／違規 0。**本輪未執行任何 git** |
| 48 | 2026-08-19 | **產出交付件（ENTRY 001，189 條）** | [handoff/48_delivery_build.md](handoff/48_delivery_build.md) | [upstream/48_delivery_build.md](upstream/48_delivery_build.md) ＋ [48_delivery_note.md](upstream/48_delivery_note.md) ＋ [48_review_pack_24b](upstream/48_review_pack_24b.md)／[33a](upstream/48_review_pack_33a.md)（重出）| —（本包無裁決條文）| —（無新開）| **產出 `output/…_UserProfiles_20260819_full.xlsx`**（189 條，row 10–198，列序依 Requirement ID，T:Z 留空），`DELIVERY.sha256` **ENTRY 001**，`shasum -c` **OK**（其 WARNING 已查明為空白分隔行，Comfort 同格式有 32 個）。**八項自檢逐項附實測輸出，全綠**：189 列無重無跳、列序遞增、必填 2457 格空值 0、多行 564 格含 CR 0、emoji 0、方括號僅 `[username]`×6（G19 通過）、行尾句點 0/1804 行、zip members 48=48 與 x14 節點 1=1、涵蓋檢查三欄皆含寫入列。**交付欄位淨化**：5670 格命中 **0**；修正三處（`148`／`167` 之 `pending`、`082` 之「未決」）。**自抓一個判準錯**：`\b` 對中文不成立，故語料側掃描漏掉 `082` —— 已 grep 全部 17 支閘確認無其他同型（0 命中）。**產出閘之判準改一次**（非拿掉）：由「值是不是 `None`」改為「`feature.yaml` 三項是否已決定且 `why` 非空」，`write_back` 自我測試 10 → **12**。**未刪 remarks 之六類內部指涉**（§節號 59、掃描代號 59 等），具名上報請裁示。**未送客戶目錄 —— 屬 Pei。本輪未執行任何 git** |
| 49 | 2026-08-19 | **G-I（`\b` 不適用於中文）、Comfort remarks 之先例查證、判例** | [handoff/49_remarks_scope.md](handoff/49_remarks_scope.md) | [upstream/49_remarks_scope.md](upstream/49_remarks_scope.md) | —（本包無裁決條文）| —（無新開）| **更正**：48 輪「已 grep 17 支確認無其他同型」之**證據當時無效** —— 該 grep 找「`\b` 緊鄰 CJK」，而出事形態是 `\b(…|待判|未決)\b`（`\b` 緊鄰 `(`）。以正確判準重查 17 支：**仍 0 命中，結論不變**。**G-I 落地為第 18 支閘** `audit_delivery_fields.py`（DF-1 交付 14 欄之內部字樣；**DF-2 對每個中文詞造「夾在中文裡」之探針實測**），7/7，其紅向案例即 48 輪之漏網形態（`TC-082` 之「上游未決事項」）。記入 profile §7.4.1。**作業 2（唯讀查 Comfort 交付件）**：466 列中 **remarks 非空僅 7 條（1.5%）**，六類內部指涉**皆 0**（一處 `N0` 誤報已具名 —— 那是 spec 之需求編號），且**全為英文**；其語料側亦僅 7/465 —— **非寫回時剝除，本來就幾乎不寫**。**且用途不同**：Comfort 只在「未涵蓋／不可判定」時寫，我方 143 條寫的是每條設計理由。→ **先例不成立**，備成本估計（110 條含指涉、393 句中 175 句、需譯 143 條）並列**甲維持／乙另出版／丙依 Comfort 收斂**三選項送 Pei，本層建議**丙**並具名其代價。**判例記入 profile §5.1：`why` 不是註解，它是狀態。****本輪未重生成、未重寫回**（G-J）；交付件 ENTRY 001 未動。18 支閘全綠。**本輪未執行任何 git** |
| 52 | 2026-08-19 | **上游素材、Table EDPR1 之比對、缺件清單收斂** | [handoff/52_upstream_materials.md](handoff/52_upstream_materials.md) | [upstream/52_upstream_materials.md](upstream/52_upstream_materials.md) | —（本包無裁決條文）| **A-UP14 新開**（`PU1089`／`1090`／`1091` 之角色在兩份上游文件間**整體錯開一位**）| **Pop Up List 入 `inputs/` 並列入 BASELINE**（`shasum -c` 8/8 OK）—— **它不是新到的檔**：repo 內原有兩份（comfort/inputs 之 SHA `b0827f02` 即 R-U9 之候選），身分以內容確認（原始字串 1341／正規化 1339、無 1087-1088、1089-1091 在，逐項重現 52 包之量測）。**Tutorials PDF 不在檔案系統**（全 repo 0 命中）→ **3.1 未做**，因其 `specification_reference` 之節次無法查證，寫了會同時違反 G11／R-U1／G18。**3.3 落在 52 包未列之第三分支**：p14 之 Table EDPR1 **含 `"Tutorials"`（第 9 列）而我方 ER 已列之** → 既非 defect 亦非 anomaly。**第 4 項已解**：Pop Up List 之 `Description` 欄確有逐步對映（`PU0585`／`0586`／`0587`／**`0612` 明寫 `Step 4`**）；本輪不改 TC，依 G-J 與餘 3 條之覆核一併落地。**RD #8 已由證據解答**（`PU0626` 為有 Profiles 之車輛、`PU0129` 為 Core 通用者 —— 五條寫法正確無須改）。`DATA_REQUESTS.md` 改為單一清單（§0 操作面四項→**三項**，歷史記載原文保留）。**51 包之 remarks 三分類量測至今未執行**，而它是 Pei 裁定之前置，具名等候指示。**本輪語料與交付件皆未動；未執行任何 git** |
| 53 | 2026-08-19 | **close-out：ENTRY 002 ＋ 全域同步（最後一個作業輪次）** | [handoff/53_closeout.md](handoff/53_closeout.md) | [upstream/53_closeout.md](upstream/53_closeout.md) ＋ [53_review_pack_33a](upstream/53_review_pack_33a.md)（重出）| —（本包無新裁決條文）| —（無新開）| **remarks 全刪**：`AH` 由必寫欄移入條件欄（`feature.yaml` 之 `remarks_column.applied`），交付件 189 列實測 0 非空，**語料一字未刪**，且 WB-0 守之 —— **裁定因此可檢驗亦可撤回**。51 包標 `[SUPERSEDED by 53]` 內容不改。**ENTRY 002 產出**：`TC-167` 之 ER4 由 `Tutorials begin` 改為 Video Bank 之標題與副標（可觀察形式）；A-UP14 依我方 spec 生成不改 TC（**判定在我方讀法下自洽**，無逕行修正之標的）；八項自檢全綠、兩個 ENTRY `shasum -c` 皆 OK。**一項未做具名**：`TC-167` 之引用欄未併列 Tutorials L&F —— 該 PDF 重查仍不在 repo，以 `INTR3` 充作節次等於造無法對照之引用；字串限制已寫入 `LITERAL_EXTRA_SOURCES`。**交付說明擴充**為 28 留白 ＋ `INTR2.)` ＋ 缺件 3 項 ＋ 覆蓋率讀法 ＋ A-UP14 ＋ AH 留空之說明。**canon 同步**：`FEATURE_ONBOARDING.md` 新增 §9 —— R-G1～R-G12 ＋ **G-A～G-M**（每項附其代價之實例）；新增 **G-L**（沒有路徑的「到齊」不算到齊）與 **G-M**（先查他 feature 之 `inputs/`）。**§4.3 選具名缺口而非加閘**：補句表是人工判讀之產物，重算式的閘只會是一支永遠綠的閘（G-D）。`PLAYBOOK.md` §6 狀態板全部更新（P0–P7 ＋ 覆核 ＋ open items ＋ 收尾數字）。**餘 3 條之覆核結果本輪未收到**，若有 defect 須另起 ENTRY 003。**本輪未執行任何 git（清單備於上繳 §7）** |
| 55 | 2026-08-19 | **Test Item 兩段：規格、TI 閘、ENTRY 003** | [handoff/55_test_item_two_parts.md](handoff/55_test_item_two_parts.md) | [upstream/55_test_item_two_parts.md](upstream/55_test_item_two_parts.md) ＋ 四份 pack 重出 | —（本包無裁決條文；規格由 Pei 確認）| —（無新開）| **TI-1／TI-2／TI-3 立閘，首跑對 ENTRY 002 之現況 189 列全紅**（輸出已貼），修正後 0；方向性案例 16/16（含「第二段僅一詞」「與首段逐字相同」之範圍向）。189 條之 `Test Item` 改為兩段，第二段落 `data/test_item_part2.tsv`（**以 `tc_id` 為鍵** —— 首版誤用 `req_id` 會把 §7 之配對造者併成一條）；`G3` 判準由 `test_item == tc_title` 改為**比首行**。**§三 唯讀量測**：Comfort 465/466、Home 180/201 **皆有第二段**，**本 feature 為唯一漏者**，而三份之形態各不相同（Comfort 第一段為 spec 條文、Home 為需求敘述、我方為 tc_title）。**Comfort 之第二段 459/465 可由「最末步 -> 最末 ER」逐字重算**，我方之來源（reasoning 驗證目標句）**不可重算** —— 具名此缺口。**事後查證**：該規格**不在 repo 任何文字內**，且 canon §4.3 反而把 Test Item 與 tc_title 視為同一物 —— **不是「規則在檔而未執行」，是規則只存在於產物**。**ENTRY 003 產出**，九項自檢全綠（**新增第 i 項：Test Item 兩段**），三個 ENTRY `shasum -c` 皆 OK。四份 pack 因原本只印 `tc_title` 而全部重出 —— **第二段之英文措辭是唯一沒有第二人讀過的交付內容**。**`TC-165` 之覆核未收到、`TC-167` 之 Tutorials 引用仍缺**（PDF 仍不在 `inputs/`）。**本輪未執行任何 git** |
| 56 | 2026-08-20 | **AD-1：Test Item 第二段之資訊量（本 feature 分析層之最後一項）** | [handoff/56_second_segment.md](handoff/56_second_segment.md) | [upstream/56_second_segment.md](upstream/56_second_segment.md) | —（本包無裁決條文）| —（無新開）| **代理判準立於 `scripts/audit_second_segment.py`（13/13）**，**門檻依據先寫後跑**（Q-1 之教訓）：去停用詞後「第二段帶進之新實詞數 < 2」列待判 —— 取計數而非比率（比率懲罰長句）、列待判而非轉紅（語意判斷，與 AB-1 同類）；純子集之選項**先寫下否決理由再跑**（`173`／`166` 各帶新詞卻仍是改寫）。**G-K：168／173／166 三條之原文命中（0／0／1 個新實詞）** —— 三條**以字面釘進自我測試**，**不讀語料**：若讀現況，改寫一落地證明就跟著消失（首版即如此，10/10 → 7/10）—— **判準抓不抓得到該病，與該病治好了沒有，是兩個獨立的問題**。首跑 **35 條待判**；人工判讀後 **31 條改寫**（來源為該條 ER 所斷言而首段未載者，措辭仍取自 `reasoning` 之驗證目標句，不另行構思）、**3 條殘餘具名**（`036`／`041`／`060` —— 其 ER 亦無首段未載之內容，改寫將構成自行構思，逾越授權）、**1 條偽陽**（`176`：判準之分詞吃掉數字，第二段實已帶 `12-character`）。重跑 35 → 5。**盲區四項具名**（同義改寫零重疊者抓不到、不判新詞之重要性、**數字不是實詞**、去尾 s 之粗略詞形還原）。**`TC-167` 之引用欄**：Tutorials L&F 之 PDF 仍未落 `inputs/` → 依 56 包 §三.2 **維持具名缺口，不再列為待辦**。**ENTRY 004 未產出** —— 57 包指示與 AE-1 合併為 ENTRY 005。**本輪未執行任何 git** |
| 57 | 2026-08-20 | **AE-1：Input Test Data 之孤兒值與 §4.5 欄位歸屬；ENTRY 005** | [handoff/57_input_data_orphans.md](handoff/57_input_data_orphans.md) | [upstream/57_input_data_orphans.md](upstream/57_input_data_orphans.md) ＋ 四份 pack 重出 | —（本包無裁決條文）| —（無新開）| **IT-1／IT-2 立於 `audit_consistency`（方向性案例 56 → 65）**。**方向從未被查過**：`G17`／`G18` 查「字面值有無 spec 出處」（往上游）、`T-1`／`U-2` 查 ER ↔ procedure，**而 `input_test_data` 這一組從未被納入**。IT-1 判準：具體值（含數字之詞、數字詞與序數正規化為阿拉伯數字、專有名詞但不取句首）須見於 `test_procedure` 或 `pre_conditions`；**綁定引用視同已使用**（`listed in Input Test Data`／`under test`）—— 11 條 PLP 資料集之逐值比對本就不該紅，**此放寬之代價已具名為盲區 3**。**G-K 三向先證後跑**：`TC-166` 現況紅、`TC-173` 綠、`NA` 者不轉紅。**首跑 IT-1 紅 6 處、IT-2 待判 3 處**（輸出已貼）。逐條處置：`163`／`166` 屬**互動資料**（何時按）→ 移入步驟、欄改 `NA`（§4.5 明文允許），`about` 之模糊語隨移入去除，且 `163` 之 remarks 原**明寫**「時點寫在 `input_test_data`」一併更正；`004`／`100` 屬**獨立資料集**未被引用 → 補綁定引用（`004` 補在**前提**而非步驟 —— 首次改法 13 詞觸發 `lint_tcs` G15）；`175`／`176` 屬**邊界值** → 補入步驟。重跑 IT-1 **0 處**。**IT-2 留 `049` 一處待判，人工判為保留** —— 其值為資料本身（一組 4 位 PIN），非互動；**若當初把 IT-2 設成紅燈，這條好 TC 現在已被清成 `NA`** —— 「列待判不轉紅」本輪救回一條。**`audit_pending` 之 PJ-2 兩次叫對**（`TC-004` 被改動 → AB-1 舊判定回列，重判結論不變，digest 由程式重取）。**ENTRY 005 產出**（AD-1 ＋ AE-1 同一次重出，G-J）：**十項**交付前自檢全綠（**新增第 j 項：IT**）、`verify_dv_integrity` 違規 0、全閘綠、**四份 pack 重出**、**四份靜態轉錄之指紋因第二段改寫全數過期，複核其轉錄內容未受影響後重新標記為 57 輪**。**ENTRY 004 於台帳留「未產出」區塊說明號次跳空** —— 台帳要能解釋自己的號次。**附帶發現未擅改**：`build_review_pack.py` 之產出日期寫死為 `2026-08-18`。**本輪未執行任何 git** |
| 58 | 2026-08-20 | **收尾：G-N、欄位接合矩陣入 canon、狀態板至 ENTRY 005** | [handoff/58_field_junction_matrix.md](handoff/58_field_junction_matrix.md) | [upstream/58_field_junction_matrix.md](upstream/58_field_junction_matrix.md) | —（本包無裁決條文）| —（無新開）| **G-N 立**（canon §9.2，與 G-D／G-K 並列 —— 三者皆為「證據本身之有效性」；profile §7.6 載其成因全文）：**自我測試不得以當前語料為案例**，缺陷原文須**以字面釘入測試**，另加「修正後不得再命中」之回歸。成因為 56 輪實測：31 條一改寫，`10/10` 立刻掉到 `7/10` —— **不是判準退化，是證明消失，而兩者在分數上長得一樣**；當時最省事的反應是回去調門檻，**那會為了讓測試變綠而弄壞判準**。會停下來只因三個 FAIL 全落在剛改寫過的那三條上 —— **抓到它有運氣成分，故立為條文**。**`build_review_pack.py` 之日期改為動態**（原寫死 `2026-08-18`，57 輪四份 pack 產於 8/20 卻印 8/18，**無任何閘會叫** —— G-C 之同型）；四份 pack 已重出，`--verify` 皆 0 不符。**欄位接合矩陣寫入 canon `FEATURE_ONBOARDING.md` §9.5**（**非僅 profile —— 它是流程資產，不是本 feature 之事實**）：**已查 14 組**附其閘與首次發現輪次、**未查 9 組**附「若壞了會怎樣」與可測性。**輪次分布才是重點**：14 組裡 3 組是最後三輪才發現的（`test_item` 兩段、`input_test_data` 兩組）——到 55 輪為止那三組上的缺陷**一直存在且一直全綠**，**不是因為難，是因為沒有人問過那兩欄之間有沒有接上**。**本 feature 不補做九組**（語料定稿、ENTRY 005 已出，九支閘之首跑紅各要付四份 pack 加一次重寫回）——**具名為「已知未查」，不是「已查為綠」**（G-D 之精神），且**把「在什麼條件下可以不做」寫進 canon 而非只寫上繳**：同樣九組在一個還在 P5 的 feature 身上答案相反。`PLAYBOOK.md` §6 更新至 **ENTRY 005**（覆核 **189／189 結清**、閘 19 支、自檢十項、新增「已知未查之欄位接合 9 組」一列）。**本輪未改任何 TC。分析層無未結項。本輪未執行任何 git** |

---

## 1.9 現行 review pack 一覽（隨每次重出更新）

**覆核一律以本表所列者為準**；其餘同名檔皆已被取代並帶警語。
讀前先跑 `python3 scripts/build_review_pack.py --verify <檔>`。

| 範圍 | 現行檔 | 產生輪次 |
|---|---|---|
| `135`–`145` | [`57_review_pack_24a.md`](upstream/57_review_pack_24a.md) | 57 |
| `146`–`156` | [`57_review_pack_24b.md`](upstream/57_review_pack_24b.md) | 57 |
| `157`–`173` | [`57_review_pack_33a.md`](upstream/57_review_pack_33a.md) | 57 |
| `174`–`189` | [`57_review_pack_33b.md`](upstream/57_review_pack_33b.md) | 57 |

**已被取代者**（不得作覆核依據）：`40_24a`／`40_24b`／`41_33a`／`41_33b`／
`44_24b`／`44_33b`／`45_24b`／`44_33a`／`48_33a`／**`44_24a`／`48_24b`／`53_33a`／`47_33b`**（55 輪：pack 原只印 `tc_title`，而 `test_item` 已成兩段）；
**`55_24a`／`55_24b`／`55_33a`／`55_33b`**（57 輪：AD-1 之第二段改寫 31 條 ＋ AE-1 之 `input_test_data`／步驟搬移 6 條）。

## 2. 現況

### 已完成

- **Scaffold**：`features/user_profiles/` 全套就位；下放包三檔未被覆寫。
  `RULINGS.md` 含 R-G1／R-G2／R-U1 ~ R-U7 **逐字**；
  `ANOMALIES.md` 含 A-UP01 ~ A-UP09。
- **036 母本處置（R-G1／R-G2／R-U7）**：三份舊檔以 `mv` 移入
  `archive/forms_superseded/`（**未刪除**），移前移後 SHA256 一致；
  `forms/` 僅餘 `…_SWQT_20260817_ext.xlsx`。母本結構探測六項全完成並寫入
  `forms/FORMS.md`；R-G1 亦寫入 `docs/fw036/FEATURE_ONBOARDING.md` §0。
  母本未被覆寫（**openpyxl save 全 repo 未執行**）。
- **BASELINE.sha256**：4 筆（inputs/ 1 ＋ spec-index Personal Account 3），
  `shasum -c` **4/4 OK**。
- **spec 側 outline map**：169 條，單一 stem、0 unparsed、0 重複、
  `Outline Number` 169/169 一致。候選被引集合 135 條已落檔。
  spec 全文唯一 PU id **20 個**（與下放包相符）。
- **workbook_state = BLANK**：獨立實測佐證 R-U6（A–AH 全欄非空格 0）。

### 第五十五輪已完成（2026-08-19）—— **Test Item 之兩段結構**

- **TI 閘首跑對 ENTRY 002 之現況 189 列全紅**（輸出見上繳 §2.1），修正後 0；16/16。
- 189 條之 `Test Item` 改為兩段；第二段來源為 `reasoning` 之驗證目標句，
  落 `data/test_item_part2.tsv`（**以 `tc_id` 為鍵**）。
- **唯讀量測**：Comfort 與 Home 之交付件**皆有第二段**，本 feature 為唯一漏者；
  **而該規格不在 repo 任何文字內** —— canon §4.3 反而把兩者視為同一物。
  **不是「規則在檔而未執行」，是規則只存在於產物。**
- **ENTRY 003**：九項自檢全綠（新增 Test Item 一項）；四份 pack 全部重出
  （原只印 `tc_title`）—— **第二段之英文措辭是唯一沒有第二人讀過的交付內容**。

### 第五十三輪已完成（2026-08-19）—— **close-out：本 feature 之最後一個作業輪次**

- **remarks 全刪**（Pei 裁）：`AH` 移入條件欄，交付件 189 列實測 0 非空，
  **語料一字未刪**，WB-0 守之 —— 要恢復只需改一個布林值。
- **ENTRY 002**：`TC-167` 之 ER4 補可觀察形式；A-UP14 依我方 spec 生成不改 TC；
  八項自檢全綠，兩個 ENTRY `shasum -c` 皆 OK。
- **canon 同步**：`FEATURE_ONBOARDING.md` **§9** —— R-G1～R-G12 ＋ G-A～G-M，
  每項附**其代價之實例**；新增 **G-L**（沒有路徑的「到齊」不算到齊）、
  **G-M**（先查他 feature 之 `inputs/`）。
- **§4.3 選具名缺口**：`data/*.tsv` 與 PDF 之一致性無法以重算式的閘涵蓋
  （補句表是人工判讀之產物），**加一支永遠綠的閘比留一個誠實的缺口更糟**。
- `PLAYBOOK.md` §6 狀態板結案；四份現行 pack 與三份靜態轉錄 `--verify` 全綠。
- **餘 Pei**：交付、git（清單備妥）、`R-U17`、RD v2＋#8＋A-UP14 之寄出。

### 第五十二輪已完成（2026-08-19）—— **上游素材與兩份文件之矛盾**

- **Pop Up List 入 `inputs/`**（BASELINE 8/8 OK）—— 它原就在 repo 裡三份之一；
  身分以**內容**確認（1341 raw／1339 normalised，逐項重現 52 包之量測）。
- **Tutorials PDF 不在檔案系統**（全 repo 0 命中）→ **3.1 未做**，
  因節次無法查證，硬寫會違反 G11／R-U1／G18。
- **3.3**：p14 之 Table EDPR1 **含 `Tutorials` 且我方 ER 已列** ——
  落在 52 包未列之第三分支（既非 defect 亦非 anomaly）。
- **第 4 項已解**：Pop Up List 確有逐步對映（`PU0612` 明寫 `Step 4`）。
  **卡了五十輪的東西，一直在 `features/comfort/inputs/` 裡。**
- **A-UP14 新開**：`PU1089`／`1090`／`1091` 之角色兩份文件**整體錯開一位**，
  `TC-142`／`143` 有假失敗風險 —— **登記不裁決**（52 包 §3.3 之原則）。
- **RD #8 已由證據解答**；`DATA_REQUESTS.md` 改為單一清單。

### 第四十九輪已完成（2026-08-19）—— **G-I 與 remarks 之先例查證**

- **更正 48 輪之證據**：那次 grep 的判準抓不到它自己要找的 bug；
  以正確判準重查 17 支閘，**仍 0 命中，結論不變**。
- **第 18 支閘 `audit_delivery_fields.py`**：DF-1（交付 14 欄之內部字樣）
  ＋ **DF-2（對每個中文詞實測「夾在中文裡」能否命中）**，7/7。
  **規則要有一條會叫的閘，否則它只是一句話。**
- **Comfort 交付件之 remarks 實測**：466 列僅 **7 條非空**、六類內部指涉皆 0、
  全英文，且**只在「未涵蓋／不可判定」時出現** ——
  **先例不成立，且爭點不是內部指涉，是 remarks 這個欄位的用法。**
  三選項（甲維持／乙另出版／**丙依 Comfort 收斂**）附成本估計送 Pei。
- **判例**：`why` 不是註解，**它是狀態**（profile §5.1）。
- 本輪未重生成、未重寫回（G-J）。

### 第四十八輪已完成（2026-08-19）—— **交付件產出（ENTRY 001）**

- **`output/…_UserProfiles_20260819_full.xlsx`**：189 條、row 10–198、
  列序依 Requirement ID、T:Z 七欄留空；`DELIVERY.sha256` **ENTRY 001**、
  `shasum -c` **OK**。**未送客戶目錄（屬 Pei）**。
- **八項交付前自檢逐項附實測輸出，全綠**；**交付欄位淨化 5670 格命中 0**
  （修正三處）。
- **自抓一個判準錯**：`\b` 對中文不成立 —— 語料側掃描因此漏掉 `TC-082`，
  在掃產出檔時才浮出。已確認 17 支閘無其他同型。
- **產出閘之判準改一次而非拿掉**：由「值是不是 `None`」改為
  「`feature.yaml` 三項是否已決定且 `why` 非空」——
  42 輪把一個「狀態」寫成了「值的形狀」，狀態改了閘沒跟著動。
- **remarks 之六類內部指涉未刪**，具名上報請裁示（§2.3）。

### 第四十七輪已完成（2026-08-19）—— **AC-1：欄內自相矛盾**

- **`TC-189` 之 `reasoning` 前半殘留已刪**（41 輪改判時只替換後半句）。
- **新掃描 AC-1**（欄內矛盾）：兩條判準、四個方向性案例，**全批命中 0**；
  `audit_consistency` 52 → **56**。**盲區三項具名**，其中
  「同義改寫抓不到」意謂**其召回率無法估計** —— 0 處不等於欄內矛盾已清。
- **連帶重出** `47_review_pack_33b.md`（第三次「修正 → pack 過期 → 同輪重出」）。
- **INDEX §1.9「現行 pack 一覽」**新立。

### 第四十六輪（2026-08-18）—— **無新作業；一項須分析層決定之事項**

- 45 輪四項作業**已於 45 輪完成**（46 包之行文為未來式）；本輪僅回報現況。
- **AB-1 之修正實動兩條**：`TC-154`（46 包已點名、讀畢不需重讀）與
  **`TC-148`（未點名 —— 它是自檢之產物）**。已附逐字差異，
  **是否重讀由分析層定**（產出方不代為認定「差異微小」）。
- **G-G 附件擴及三份靜態轉錄**（`27_rd_queries_v2`／`28_provenance4`／
  `34_provenance5`，皆 0 不符）—— 補 45 輪自陳之缺口。
- profile §7.5.1 收斂：**重出是產出方之義務，重讀是覆核方之判斷。**

### 第四十五輪已完成（2026-08-18）—— **AB-1 與靜態轉錄之指紋**

- **AB-1**：`TC-154` 之 ER4 未指明所讀者而恆真 —— 已改為指名新建 profile
  並斷言其與步驟 1 所記者**相同**（carry-over）。
- **全批自檢 16 處逐條判定**；其中 **`TC-148` 為同型而未被點名者，一併修正**
  （同一句英文在 6.4 是恆真、在 6.1 是歧義）。掃描**只並排兩端，不硬判**。
- **G-F**：新閘 `stamp_static_doc.py`；RD 查詢單與各批出處對照加指紋，
  範圍取**全欄**（保守）；已 WITHDRAWN 者不標。
- **G-G**：上繳附四份 pack 之 `--verify` —— **建立當輪即抓到真陽性**
  （AB-1 之修正使 `44_review_pack_24b` 過期），已於同輪重出。
- **G-H**：他 feature 之先例須先確認**母本同一**（profile §7.4）。
- 閘 16 → **17 支**。

### 第四十四輪已完成（2026-08-18）—— **AA-1：review pack 之時效**

- **`build_review_pack.py` 加語料指紋與 `--verify`**：指紋不符即
  「pack 已過期，**拒絕採信**」；**無指紋表者一律判過期**。4/4 方向性案例。
  與 `audit_pending` 之 digest **方向相反**（那個防「改了不重判」，
  這個防「判了舊的」）。
- **變動清單**：四份舊 pack 自其產生以來共 **5 條**有變動，全在 `24a`
  （`139`–`143`，來源唯一：41 輪 RD #8 之處置）；其餘 44 條一字未動。
  **不用 git —— 舊值就在那份檔案裡**（`--changes` 逐欄比對）。
- **四份重出**（`44_review_pack_24a/24b/33a/33b`，共 55 條，`--verify` 皆綠）；
  舊四份**加警語保留不刪**。
- **44 包 §二之 7 條覆核結果經確認全部有效**（`140` 之依據欄未變、
  `144`／`145` 整條未變）。
- **三項常規**寫入 profile §5.1／§7.3／§7.4，另加 §7.5（pack 時效）。
- **`vehicle_columns` 定為留空**（三項實測依據）—— **擋交付者現為 0**。

### 第四十三輪已完成（2026-08-18）—— **宣告與生效之分離、寫回實跑探針**

- **更正**：41／42 輪之「T:Z 不填則 WB-5 會紅」**兩層皆錯**（見上繳 §0.1）。
  實測：Comfort 交付件之 T:Z **466 列逐列為空**，母本該區 DV 自帶
  `allowBlank="1"`。**留空有先例亦有許可 —— 未決 1 不再擋交付。**
- **G-C**：`feature.yaml` 之 `write_back` 改為 `{value, applied, why}`；
  `write_back.py` 只讀 `applied: true` 者，並以 **WB-0** 驗其一致。
  comfort 之同形現象登記為 **N-XF02**（唯讀，comfort 一個檔都沒動）。
- **G-D／G-E** 寫入 profile §7.1／§7.2：待判抑制數為掃描存活之證據；
  可測範圍已到底，55 條人讀為品質判斷之主要承擔者。
- **寫回實跑探針**（`--probe`）：三段接點全綠，違規 0；
  產物落 scratchpad，**不落 `output/`**（另有一道閘守之）。
  `write_back.py` 自我測試 **10/10**。

### 第四十二輪已完成（2026-08-18）—— **寫回程式與兩項常規化**

- **`scripts/write_back.py`**：`build_edits` 直接產生 2646 格 edits
  （**不經 `diff_cells`**），`patch_sheet_xml` 封裝，六項寫回後檢查，
  **7 / 7 方向性案例**。`--write` 受**未決 1（T:Z）**之閘拒絕，**無 `--force`**。
  **未產出任何交付件**；`output/` 空，`DELIVERY.sha256` 尚無 ENTRY。
- **未決 2–5 處置**（依 Comfort **交付件實測**而非其 yaml 宣告）：
  Q／AB 留空、輸出與台帳沿用 Comfort、換行 LF（WB-6）。
  **另發現 O／AA 同形**（yaml 宣告而交付件為空，兩 feature 皆然）——
  一併參數化預設不寫。
- **G-A（待判時效）**：43 條全數逐條判定並登記；掃描清單語意改為
  「未結案之命中」，以 **digest** 守之（`audit_pending.py`，16 支閘之一）。
- **G-B（枚舉對照）**：`audit_enums.py` ＋ `data/enum_vocab.tsv` ——
  `STATE_VALUES` 之對照取自 **spec 側**（候選 12），
  `UI_LOCATORS` 取自**語料側**（跨節 6）。
- **「覆蓋率是分母的性質，不是分子的品質」** 寫入 profile §1 與
  `framework.md` §4.2，並列出第六批之四處留白。

### 第四十一輪已完成（2026-08-18）—— **第六批：leaf 全覆蓋**

- **第六批 33 條**（`NR1L-UserProfiles-157`–`189`）：ch7 `PRWEL` 10 leaf
  ＋ ch8 `NEWPR` 23 leaf。語料 **189 條**，**leaf 覆蓋 180 / 180 —— 全覆蓋**。
- **X-1 之 20 條修正落地**（`popup_guard.py` 一張表，15 條加 pre-condition、
  5 條具名該 popup 為標的），X-1 待判 **22 → 0**；
  順帶抓出 PU0588 之兩處誤報並補其成立條件。
- **`audit_verbs.py`**（第 14 支閘）＋ `data/verb_synonyms.tsv`：
  以動詞為觸發之掃描，其詞表須與掃描之正則對照。
  **VB-2 之注入向即 40 輪之缺陷本身**（正則退回只認 `select` → 轉紅）。
- **RD #8 依 41 包 §四逕行修正**，不待答覆；驗證目標未變。
- **A-UP09 → RESOLVED**（41 包落槌），Phase 6 寫回實作得開工；
  **交付仍屬 Pei**。D-UP41-01 記入 `DECISIONS.md`。
- **寫回實作之設計草案已出（未執行）**：五項未決見上繳 §5.5。

### 第四十輪已完成（2026-08-18）—— **第五批生成、DV gate、review pack 程式化**

- **第五批 22 條**（`NR1L-UserProfiles-135`–`156`）：ch5 `ALLPR`（5.12–5.16）13 leaf
  ＋ ch6 `NOPR`（6.1–6.6）9 leaf。**額外造者 0**。
  語料 **156 條**，leaf 覆蓋 **147 / 180**，餘 33（ch7 10 ＋ ch8 23）＝ 第六批。
- **`verify_dv_integrity.py` 立起並實跑**（R-U14 之解除條件）：
  DV-1 zip member 集合／DV-2 x14 節點數／DV-3 `xm:sqref` 範圍／DV-4 legacy 節點數，
  **6 / 6 方向性案例 PASS**，其中三個注入向皆轉紅。
  **A-UP09 之解除條件已成就，狀態改判待落槌**（解除同時解除寫回封鎖）。
- **系統性發現**：X-1 之觸發詞表只認 `select … Driver Profile`，
  **漏 `activate`** —— 擴充後待判 6 → 22，新增 16 處全在既有批次。
- **`build_review_pack.py`**：覆核用全文與 ER 出處對照改由程式產生，
  不再手打轉錄（21／23／29／34／35 輪皆為手打）。
- **RD #8 新開**：`5.13.2` 之 `PU0626` 與 `PU_0129` 是否同一個 popup。

### 第三十七輪已完成（2026-08-18）—— **J-15 補做與號碼指派檢查**

- **作業 1 J-15 作業 3**（36 輪查出之唯一真正遺漏）：複核 11 輪 PLP 位置指涉
  盲區掃描 17 條命中之其餘 16 條。
  **結論 16 條全部不變（皆為「非 PLP」），理由更正五處**：
  - `047`（6.2）／`066`（8.2）—— 指的是**圖**，不是條文。
    `047`：**ch6 之前沒有任何 Welcome Popup 條文**（6.1 是 R1 High 之 CPA 註記），
    而 ch7 之 `PRWEL` 在其**下方**，不可能是 `above` 所指；
    `066`：**同一句之 `not pictured here` 就是證據** —— 被指之 `flow above` 是圖。
  - `090`／`091-01`／`091-02`（9.3.x）—— 指的是 **9.3 自身之散文列舉**
    （`Deleting a Profile, editing username, …`），
    **而非 Table EDPR1（那是 9.1 之選項順序表，與行車限制無關）**。
  - `108`（10.3.1）—— 方向正確但未複位；20 輪 C-1 已精確化為 PDF p16 之 Table PIP1。
- **並查證該錯誤理由未流入語料**：`TC-022`（`090`）之 reasoning 逐字為
  「受限項目之清單**出自 9.3**，故併列該節」—— **寫的是對的**。
  `TC-011`／`TC-023` 之 remarks 雖提及 Table EDPR1，但那是指
  **9.3.2 之 R1 High 列級覆寫**，是另一件事且記載正確。
  **故錯的只有 D-UP11-01 那張表裡的三格，TC 本身沒有受影響。**
  依 36 輪 R-2 之先例**加註而不刪原表** —— 刪掉就看不出曾經給過錯的理由。
- **作業 2 立 `audit_assignment.py`**（6/6）：
  **A-1 之號碼指派表由六支生成器之取樣清單 ＋ `TC_START` 重算，不讀 `generated/`**
  —— 那是地基：**若產物與生成器分岔，任何以產物為據之檢查都不可信**。
  A-2 驗同句之 `tc_id`↔leaf id 相符、A-3 驗提及之號碼存在。
- **首跑綠（違規 0），並具名「0」之意義**：36 輪兩處指錯已於該輪修正，
  故本檔首跑本來就該綠 —— **它證明的是修正確實生效，不是「從來沒有這種錯」**。
- **盲區具名**：**A-2 只在同句同時出現號碼與 leaf id 時才驗**，
  而 **36 輪之兩處正是「只寫號碼、未附 leaf id」** —— 擋不到。
  已納為護欄案例（固化的是**界線**而非能力）。
  建議往後 remarks 提及他條時**號碼與 leaf id 併寫**；`TC-003` 之新 remarks 先行套用。
- **作業 4 兩項裁定落地**：`TC-003` 維持現狀，remarks 具名
  **核心斷言為「數目上限」**、ER3 其餘三項為情境確認並指出其各自之 leaf 與號碼；
  PU0580 四條（`117`／`119`／`120`／`108`）之 pre-condition 指定
  `The welcome popup is turned on for Driver Profile B`。
- **5.3.1 只有一個 leaf**（`023`），其 `(if turned on for that Profile)` 之
  **關閉側無對應 leaf** —— 依 **R-U56** 判 **OUT-OF-SCOPE**，具名不列缺口。
- **待判項數目本輪未增**：PU0580 之 pre-condition 屬 X-1 之處置，
  而 **X-1 之判準是「procedure 是否處理該 popup」，非「pre 是否指定其開關」** ——
  兩者是不同的事，未混為一談。
- 語料 **134 條**（改 5 條之 pre-condition／remarks，**ER 與 procedure 未動**）；
  全閘綠：lint 134/0、self-test 64/64、variant 11/11、batch_context 8/8、
  render 7/7、audit_consistency 43/43、audit_variant_pairs 7/7、
  audit_delegation 8/8、override `--check` 一致、lint_outbound_doc 8/8、
  **audit_assignment 6/6（語料違規 0）**。
  **本輪未執行任何 git；第五批未開。**

### 第三十六輪已完成（2026-08-18）—— **全稱限制之反向與配對宣稱**

- **Y-1 採 (a)**：`TC-117`（5.3）之 ER3 加 `and the “Edit Profile” tab is not
  opened`，步驟 3 相應改寫。**§5.7 之併入在此成立** ——
  「選取另一個 profile」是**一個觸發**，其必然結果有二（切換發生、不進入編輯）。
  **若採 (b)，其 procedure 會與 `TC-117` 逐字相同而只有 ER 不同 ——
  那是把同一次操作寫成兩條**；與 4.5.2／5.7 之配對不同（那兩處之正反兩條
  **操作本身就不同**）。
- `TC-121` 之 remarks 改指**ER 行號**（`ER3 後半`，逐字為
  `the “Edit Profile” tab is not opened`），並記明**在該句補上之前該 `only` 無人驗**。
- **配對宣稱全批自檢：命中 18 處，指錯 2 處。**
  `TC-096`（`009`）稱其反向為 `104` —— **而 `104` 是 4.6.3 之 `016`**，
  正確者為 `105`（`009-neg`）；
  `TC-127`（`030-01`）稱其反向為 `133` —— **而 `133` 是 5.10.1 之 `034-03`**，
  正確者為 `134`（`030-01-neg`）。
- **兩處都是我在 `tc_id` 尚未指派時寫下的號碼**：生成器之 remarks 先寫，
  而號碼由 `TC_START` ＋ 取樣序決定，**兩者之間沒有任何檢查**。
  **而且兩處都通得過現有的閘** —— `audit_delegation` 之 D-1 只認
  `由 … 承擔` 之句型（「**反向為** X」不在母體內），
  D-2 只驗被指名者**存在**，而 `104`／`133` 都存在。
  **這正是 A-UP12 之同型：委派指得到，但被指者不是那個東西。**
- **落為 Y-1 掃描**：「被指者之 ER 有沒有那句反向斷言」是語意，機械判不了；
  但 §7 之配對有一個**可測之必要條件** ——
  正反兩條驗的是同一條條文之兩面，故其 `req_id` 之**基號**應相同。
  該判準**抓得到本輪之兩處指錯**；跨 leaf 群者不一定是錯的
  （`121` → `022` 即正當之跨節委派），故列**待判**。方向性 ＋3（含護欄）。
- **自檢之副產品**：`TC-073`（14.2）之 reasoning 仍寫
  「R-U5 之 rubric 無安全帶，依 D-UP16-01 就近判 P0」——
  **該說法於 21 輪 K-1 已作廢，當時改了 `089`／`116` 而漏了本條**。
  判級不變（P0），依據補正為 **canon §10.2 之 safety 直接成立**。
- **作業 2 —— `20_batch03.md` 之來歷**：一份**未被執行之 20 輪下放包**。
  證據：mtime 比 `20_batch01_review.md` **早 2 分鐘**、
  兩者**同一個 commit 首次入版控**、
  **其指定之上繳標的 `20_batch03_sample.md` 不存在**。
  **寫入者無法由檔案判定** —— `docs/handoff/` 無作者欄位，
  git 首次提交者是我（我把當時未追蹤檔一併納入）；
  **故「非本層所出」與檔案證據不衝突，我也無法證明它是誰寫的**。
- **其五項作業逐條查證：四項已由後續下放包以不同編號重新提出並完成**
  （F-5 → 24 包 P-3 ＋ 25 包 G20；J-14 → 21 包 K-1；
  第二批出處對照 → 19 輪；第三批取樣 → 25 包 §B）。
  **唯一遺漏為 J-15 作業 3** —— 11 輪盲區掃描 17 條之「結論對／理由錯」逐條複核，
  查全部上繳檔**無執行記錄**。其形態**已被 34 輪之 `phrase_of` bug 證明非空談**。
- **未刪除、亦未加註標頭** —— 該檔為下放包（分析層之物），
  執行層不改下放包（19 輪起之慣例）。處置建議三項，請裁示。
- 語料 **134 條**（改 5 條之記載，**測試內容變動者僅 `117` 一條**）；全閘綠：
  lint 134/0、self-test 64/64、variant 11/11、batch_context 8/8、render 7/7、
  **audit_consistency 43/43**、audit_variant_pairs 7/7、audit_delegation 8/8、
  override `--check` 一致、lint_outbound_doc 8/8。
  **本輪未執行任何寫入性 git**（作業 2 之來歷查證用了唯讀之 `git log`，已具名）。
  **第五批未開** —— 待第四批餘 5 條覆核完成。

### 第三十五輪已完成（2026-08-18）—— **跨節 popup 之未處理**

- **X-1 `TC-128`**：其步驟 2「存座椅位置到**非現用 profile 所連**之座椅」
  正是 5.10.1 之觸發條件 —— **PU0588 會跳出來問**，而原 procedure 完全沒提它。
  **測試者會撞上未預期之 popup，結果取決於他按了什麼**：
  選 Yes 則該座椅就會連到 A，**與 ER3 相反**。
- **下放包「兩條條文並不衝突，衝突的是 TC 之寫法」之判定成立**：
  5.7 之 `not **automatically**` 是「不經詢問即發生」，
  5.10.1 是「問過且答 Yes 才發生」。
  修正為加一步 `Select No on PU0588`，**並於 ER2 併驗該 popup 出現** ——
  否則「該詢問是否真的發生」未被斷言，**而它正是兩節之接縫**。
- **全批自檢之 v1 得 60 處 —— 等於沒有範圍**：以「觸發句關鍵詞與 procedure
  重疊 ≥3」比對，絕大多數只是**主題重疊**（`valet`／`mode`／`vehicle`／`popup`）。
  **一份 60 筆的待判清單不是縮小範圍，是噪音**，而噪音清單會被略過（R-G9）。
- **v2 改為登記表式**：逐個 popup 登記其**觸發動作**與**成立條件**，
  **兩者皆命中**方列待判。成立條件是關鍵 ——
  v1 把靜止中按 Valet 鍵之 `TC-047` 判為可能觸發 PU0091（其觸發為**行車中**）。
  得 7 處，修正 `TC-128` 後 **6 處，逐條判無進一步缺陷**：
  `004` 之步驟 3 明寫 `Leave the … save controls **untouched**`（根本沒存）、
  `130` 之 pre-condition **刻意**使現用者即該座椅之連結者。
- **並立一條分類判準**：X-1 之真正判準不是「會不會跳 popup」，而是
  **「跳出來之後測試者是否必須做一個會改變結果的決定」** ——
  PU0588 是**決策型**（Yes／No，答案改變結果，必須處理）；
  PU0580 是**資訊型**且 5.3.1 載明 5 秒自行消失（不改變任何斷言，不必處理）。
  已寫入該掃描之 docstring。
- **X-2 `TC-134`**：步驟 2 原寫 `from outside the “Edit Profile” screen` ——
  **「outside」不是一個測試者能執行的位置**。改為指名兩個實際受檢畫面
  （All Profiles 分頁、車輛設定），比照 `TC-047`；
  reasoning 具名「該位置不可窮舉，此為**抽樣**，**未涵蓋之入口其結果不由本條保證**」。
- **作業 3**：review pack 拆為 `26a`（`109`–`121`）／`26b`（`122`–`134`）各 **13 條**、
  各 328 行，兩檔互相指路。
  **下放包之自陳照收** —— 其單輪讀取量之上限我方無從得知，
  故此後 review pack 一律拆至**每檔 ≤ 13 條**；若仍過長，請給一個具體條數。
- **本輪判準之觀察**：X-1 之 v1 與 30 輪 T-1、31 輪 U-2 之 v1 同型 ——
  **都是「找得到相關字就算命中」**；三次之修法也同型 ——
  **把「相關」換成「該動作／該物／該條件確實成立」**。
  差別在本輪用的是**登記表**而非更聰明的正則，因為觸發條件
  （「非現用 profile 所連之座椅」）**本來就不是字串比對得出來的**。
  **登記表之代價是要維護；好處是它的盲區可以被列出來。**
- 語料 **134 條**（修改其中 2 條）；全閘綠：lint 134/0、self-test 64/64、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 40/40**、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致、
  lint_outbound_doc 8/8。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）；第五批未取樣。**

### 第三十四輪已完成（2026-08-18）—— **第四批 26 條落地**

- **第四批 ＝ ch5 之 `PRACC` 群 25 leaf ＋ `030-01` 之反向配對 1 ＝ 26 條**
  （`tc_id` `109`–`134`）。語料 108 → **134**；leaf 覆蓋 100 → **125 / 180**。
- **條數更正 —— 下放包沿用了我 29 輪之措辭錯誤**：
  `041-04` 屬 `5.13.2`（**`ALLPR` 群，第五批**），且它本身就是一個 leaf，
  **不是額外造出來的一條**。我 29 輪把它與 `030-01` 之反向並列為「額外造者」，
  故該處之「38 ＋ 2 ＝ 40」多算了一條；ch5 全章實為 **39**。
  本批之 26 條與下放包所載之範圍與估數**一致**，只有那個標籤是錯的。
- **生成時被閘擋下 6 處，皆我方之錯**：G8 四處（`check` 未接 `that`）、
  G15 一處、G18 一處。
- **`TC-115` 之 G18 判定正確**：5.2 以**指涉**帶入 PRACC7.2 之字串
  （`the icon and the string **described in note PRACC7.2**`），未逐字重複。
  處置為 `REF_EXTRA` 併列 5.1.2 —— **D-3／C-1 之同型第四例**，處置與前三例一致。
  **連帶發現**：`_ref_allowlist()` 原只讀 pilot／batch01／batch02 三支之
  `REF_EXTRA`，**第三、四批之登記讀不到** —— 已擴至五支。
  **若未擴，本批之併列會被 G17 判為多引，即「補了引用反而更紅」。**
- **五支對應關係掃描於生成後即跑，待判項逐條判**：
  T-1／U-2／W-1 各 **0**；
  U-1 新增 3（`131`／`132`／`133` 之 PU0588）—— **綠**，
  其兩句觸發為 31 輪已判之「同一觸發記載兩次」，且三條各自另有綁定；
  V-1 新增 2（`115`／`116` 之 5.2 `before`）—— **綠**，
  該詞在 **PU0584 之 popup 文字內**，不約束測試順序（同 32 輪對 `TC-003` 之判定）。
- **K-4a 3 處紅為判準漏詞**：`117` 之 `Select the username of Driver Profile B`
  與 `132`／`133` 之 `save it to the memory seat …` **皆為真狀態遷移**
  （現用者改變、座椅連結歸屬改變），補 `save` 與 `select … Driver Profile`；
  **`open`／`read` 仍未收進來**，28 輪之護欄不變。
- **`audit_delegation` 三處紅 —— 兩處是我用錯詞，一處是閘本身的 bug**：
  `126`／`129` 我寫「由 ER3 前半**承擔**」，而 `承擔` 在本專案專指**跨 leaf 之委派**，
  已改為「斷言**落在** ER3 前半」。
- **那個 bug 值得單獨記**：`phrase_of` 只收 ≥4 字母之詞，
  而 1–3 字母者（`to`／`the`／`not`）**既不收進詞串、也不當斷點** ——
  **詞串中間的短詞被靜靜丟掉**（`switch system to that Profile`
  被抽成 `switch system that Profile`），再逐字比對節文自然對不上。
  **嚴重性不只是一次誤報**：22 包那個 D-3 要抓的案例
  （`does not support the connected profile feature`）**之所以轉紅，
  有一半是因為詞串被打斷**，不全是因為內容不符 ——
  **它一直在為對的結論給錯的理由**。
  v4 修正（短詞在詞串已開始時併入）後複驗：**該案例仍紅，這次是為對的理由**。
- **另發現一項既有問題，本輪未改**：`TC-003`（`021-01`，5.2）之 ER3
  涵蓋了 `021-02`（按鈕與圖示消失）與 `021-03`（PU0584 文字）之內容 ——
  而那兩個 leaf 正是本批之 `TC-115`／`TC-116`，**故三條 TC 斷言同一組事實**。
  依 D-UP24-01 與 §8.2.1，`TC-003` 之 ER 越出其 leaf。
  **未改之理由**：它屬已核可之 pilot 批；且其 ER 若收斂為「數目上限」，
  **其可觀察形式恰恰就是「按鈕不見了」**（即 `021-02` 之內容）——
  **這不是機械改寫，是要決定該 leaf 怎麼驗**。已具名待裁。
- **出處對照**（`34_provenance5.md`）：30 個引號字面值，**未溯得者 0**；
  **本批無任何 R1 High／China 變體條件**，與 25／29 輪之預告一致。
- **覆核用全文同輪交出**（`34_review_pack_26.md`，648 行 26 條）——
  依下放包，**使覆核不必再等一輪**。
- 全閘綠：lint **134/0**、self-test 64/64、variant 11/11、batch_context 8/8、
  render 7/7、**audit_consistency 37/37**、audit_variant_pairs 7/7、
  audit_delegation 8/8（紅 0 黃 13）、override `--check` 一致、lint_outbound_doc 8/8。
  **P0 = 37 / 134 = 27.6%**，未因批次擴大回頭調判準（J-9）。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第三十三輪已完成（2026-08-18）—— **前提之循環（第三批覆核結案）**

- **第三批 30 條之內容覆核結案**（分析層 30 / 30 讀畢），未經第二人讀過者 **0**。
- **W-1 `TC-094`**：pre-condition 原為 `Every Profile **has been deleted**`，
  **兩重問題疊在同一句上** ——
  1. 4.5 逐字載「全部刪除後車上**恆有**一個預設 profile」，
     故該前提所述之穩態**系統不允許存在**：測試員讀到它時，該狀態已經是假的；
  2. 其蘊含之結果（車上只剩 Driver 1）**正是本 TC 之 ER 要斷言者**（§4.4 所禁）。
- **修正**：刪除移入 procedure（比照 `TC-093`），pre 改述**刪除前**之狀態
  （曾客製之 Driver 1 存在）；ER 增為三條，ER1 為 `Every Profile is deleted`。
  **pre 2（座椅鍵少於 2）不動** —— 那是條文自帶之例外，非受測結果。
- **修正後兩條之分野更清楚**：`093` 與 `094` 現在 **procedure 相同、ER3 不同** ——
  `093` 驗**重建發生**（且重建出的是**預設**而非改名留下之客製 profile），
  `094` 驗**重建後只有一個**。同一操作、兩個斷言，037 切兩個 leaf 故不合併。
- **完成式 pre-condition 全批自檢：命中 4 處，循環 1。**
  `093`（客製化 → 使刪除後之重建有意義）、
  `104`（按鈕已移除 → 4.6.3 之適用條件本身，且該操作屬 Home feature）、
  `005`（起始狀態）**皆為正當之佈署描述，保留**。
- **修正後之 `094`，其 pre 仍是完成式 —— 而那是對的。**
  判準是「**該狀態是不是本 TC 的 ER 要斷言的東西**」，不是「有沒有用完成式」。
  客製化是**佈署**，重建後只剩一個才是**斷言**。
  **這正是本掃描只能「待判」的理由** —— 硬判會把四處中的三處正當者全部誤殺。
- 方向性案例 ＋2（`audit_consistency` **36 / 36**），含護欄
  「pre 為狀態描述者不得列入」—— 若它倒了，待判清單會等於全語料。
- **四輪連續之形態（自陳）**：
  30 輪 T-1（步驟↔ER）、31 輪 U-1／U-2（斷言↔分支、步驟↔ER 反向）、
  32 輪 V-1（步驟↔條文時序）、**33 輪 W-1（前提↔ER）** ——
  **四輪四種對應關係，四處都是人工覆核先發現。**
  本輪補上最後一組常見對應，**一條 TC 之四個欄位間的兩兩對應現在都有掃描在看**。
  **但四支掃描有三支只能是「待判」**（V-1／U-1／W-1），因為它們要判的是**語意關係** ——
  **這是本 feature 之閘所能到達的界線：可測的是「有沒有」，
  不可測的是「指的是不是同一件事」。**
- 語料 **108 條**（修改其中 1 條）；全閘綠：lint 108/0、self-test 64/64、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 36/36**、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致、
  lint_outbound_doc 8/8。
- **第四批未開** —— 其取樣清單自 29 輪提出，**已隔四輪未經覆核**，
  現為分析層唯一未讀項。**本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第三十二輪已完成（2026-08-18）—— **覆寫之發生點**

- **V-1 `TC-091`**：序列由「熄火 → 開機 → 按座椅鍵」改為
  「熄火 → **按座椅鍵並開機**」，比照同節之 `TC-090`（key fob）。
- **ER1 之改動才是關鍵**：原 ER1 為
  `The ignition is off and then on again **with Driver Profile B active**`
  —— **它把本 TC 要證明「不會發生」的那件事，寫成已經發生的事實**。
  覆寫在那一刻就沒有餘地了。現改為「B 是**上次之** profile」（key-on 前之狀態）。
  ER3 斷言 **A 為該 key cycle 之起始 profile 且 B 未被載入**。
- **原序列還有第二個問題**：步驟 2 之後所觀察者是「按座椅鍵 → profile 切為 A」，
  **而那是 `SWE1-HMI-PROF-004-03`（`TC-086`）已覆蓋之行為** ——
  原 `TC-091` 不只漏測 4.4 之覆寫，**它還與 `TC-086` 重複**。
  修正後兩者分野恢復：`086` 驗**切換途徑**，`091` 驗**起始載入之覆寫**。
- **實車限制依令寫入 remarks**：若該車之記憶座椅鍵僅能於 ignition on **之後**
  按下，則「A 為起始 profile」**在該車上不可觀察** —— 屆時須回報該不可觀察性，
  **不得以「先開機再按」充當覆寫之驗證**（那正是本次所修正之形態）。
  **本 TC 不假定該鍵可於 key-on 前按**，只要求其操作**不晚於** key-on ——
  現行寫法對「同時」與「先按後開」皆成立，未對車輛能力作 spec 未載之推定。
- **時序語全批自檢：命中 13 條，真缺陷 1。** 逐條判出**同一個詞的三種身分**：
  **真時序**（4.4 之 `at the start of`、12.8.2 之 `prior to activating`）／
  **位置而非時間**（9.7.2 之 `prior to the deleted one`）／
  **在 popup 文字內**（5.2 之 `before creating a new one`，不約束測試順序）。
  **機械判準分不出來**，硬判會使 `035`／`003` 那種正確的轉紅 ——
  故列「待判」，理由與 U-1 同型。
- 方向性案例 ＋2（`audit_consistency` **34 / 34**），其中一條是護欄：
  **無時序語者不得列入** —— 若它倒了，待判清單會等於全語料，
  那就不是縮小範圍而是沒有範圍。
- **三輪連續之形態（自陳）**：T-1（步驟↔ER）、U-1／U-2（斷言↔分支、步驟↔ER 反向）、
  V-1（步驟↔條文時序）—— **三者皆為「對應關係」之缺陷，不是單一欄位寫錯**。
  現行十支閘多為**欄位內**之檢查，**對應關係之檢查全是這三輪才長出來的，
  且全部由人工覆核先發現**。閘擋得住「寫錯」，
  擋不住「兩處各自正確而彼此不對應」—— A-UP12（互指之委派）同屬此類。
- 語料 **108 條**（修改其中 1 條）；全閘綠：lint 108/0、self-test 64/64、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 34/34**、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致、
  lint_outbound_doc 8/8。
- **第四批未生成** —— 其取樣清單自 29 輪提出，**已隔三輪未經覆核**；
  下放包載明「`TC-093`～`095` 與該清單讀畢後第四批方得開批」。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第三十一輪已完成（2026-08-18）—— **分支綁定與反向形態**

- **U-1 `TC-082`**：ER3 由 `PU1088 is displayed` 改為併驗
  **「該設定已回到預設值」** —— 4.1.1 有**兩句**都指向 `PU1088`
  （成功回復／HU 或 TBM 未確認），**同一個 popup 兩個分支**，
  只驗顯示則一個根本沒回復成功之實作照樣通過（§7）。
  **與 `TC-081` 之分野不變**：`081` 驗回復之**範圍**，`082` 驗**流程提示**，
  本次只加一個**綁定分支用**的觀察點。
- **全批自檢命中 3 處，真缺陷 1**：
  `002` **綠** —— 其綁定不在斷言 popup 那一句，而在**前一條 ER**
  （`The head unit does not receive the completion confirmation`）
  ＋ procedure 主動 `Withhold` 之情境注入；
  `031` **綠** —— PU0588 之兩句（5.10.1／9.6）**描述同一個情境**，
  是同一觸發被記載兩次，不是兩個分支。
- **U-1 列為「待判」而非「紅」是刻意的**：綁定分支之方式不只一種
  （`082` 靠同一句、`002` 靠另一條 ER ＋ 情境注入），
  **機械判準無法斷定哪一條 ER 綁住了哪一個分支** ——
  硬判會使 `002` 那種**綁得最紮實**的作法轉紅。掃描只負責縮小人工範圍。
- **U-2（T-1 之反向）—— 判準第一版即錯，且錯得很典型**：
  v1 以 `\brecord` 比對步驟得 **14 處**，逐條看才發現**其中 13 處是比較步驟**
  （`check that it matches the value **recorded** in step 1`）——
  **`recorded in step N` 是回指，不是記錄動作**；
  v1 把「引用基準線的那一步」當成「建立基準線的那一步」，
  **方向剛好相反，而它要找的正是方向**。v2 排除 `recorded` 後得 1 處。
- **`TC-104` 判為「ER 漏斷言」而非「多餘步驟」**：4.6.3 要驗
  「highlight 狀態**仍適用**」，**無開啟前之基準線則「永遠 highlight」之實作會通過** ——
  故該記錄步驟是必要的，缺的是 ER 沒去用它。
  補 ER1 之記錄與 ER3 之比對（作法同 `TC-103`）。
  **判為多餘步驟而刪掉它，等於把該條降級成「開啟後有 highlight」，正是 §5.6 所防者。**
  **全批 32 處記錄動作中，多餘步驟為 0 處。**
- 方向性案例 ＋3（`audit_consistency` **32 / 32**），其中一條是護欄 ——
  **它是 v1 那 13 處假紅的固化**：若日後有人把判準改回 `\brecord`，
  紅向兩條仍過，**只有這一條會倒**。
- **連續三輪之共同形狀（自陳）**：T-1、U-2 之判準第一版都寫成
  「有沒有那個詞」，而缺陷在**「那個詞指的是不是同一件事」** ——
  與 22 輪 D-3 之教訓（`does not support connectivity` 與
  `does not support the connected profile feature` 共用三個詞）同源。
- 語料 **108 條**（修改其中 2 條）；全閘綠：lint 108/0、self-test 64/64、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 32/32**、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致、
  lint_outbound_doc 8/8。
- **第四批未生成** —— 其取樣清單自 29 輪提出，**已隔兩輪未經覆核**。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第三十輪已完成（2026-08-18）—— **T-1：基準線之成對要求**

- **`TC-101` 修正**：步驟 1 由「查按鈕在不在」改為「**記錄** Profile 按鈕圖示」，
  ER1 相應改為記錄式。**ER1 之「按鈕存在」斷言保留** ——
  兩者不可互換：只寫「圖示已記錄」會失去「按鈕預設存在」這個斷言（4.6 之第一個要求）。
- **連帶自檢：命中 18 處，紅 1**（即該條）。修正後複跑 **T-1 0 處**。
- **本輪最該記住的是判準本身**：我第一版自檢寫成
  「該步驟有無 `record`／`read` 之動詞」——
  **而 `TC-101` 之步驟 1 正好有 `Read`**（`Read the status bar and check that…`），
  於是 **v1 判它綠，而它正是本包點名要抓的那一條**。
  **若照 v1 的結果回報，會寫成「命中 18 處、紅 0」，而且那份回報會通過所有閘。**
  > **動詞在，不代表讀的是同一個東西。**
- **v2 改抓「被比較之物」**：`the <X> recorded/read in step N` 之 X ——
  **具體物**（`icon`／`order`／`page`）須見於該步驟；
  **泛稱或功能詞**（`value`／`those`／`as`）退回查動詞。
  **泛稱之退回是必要的而非放水**：`the values recorded in step 1` 對應之步驟
  寫的是 `record the two **preferences**`，**泛稱與具名本就不會字面相同**。
- **v2 首跑仍紅 4，其中三處是抽取誤判**（`038` 之 `as`、`045` ×2 之 `those`
  被當成被比較之物），補功能詞表後為紅 1 ——
  **兩次都是判準錯，語料只有一處真缺陷。**
- 方向性案例 ＋4（`audit_consistency` **29 / 29**），其中兩條為護欄：
  「泛稱不得要求字面相符」守住那條退路沒被收掉；
  「引用之步驟根本不存在」補了下放包未提、但同屬「基準線不存在」之形態。
- **自陳之判準盲區**：本閘抓「ER 引用步驟而該步驟未建立基準線」，
  **抓不到反向**（步驟建立了基準線而 ER 從未用它）；
  另其具體物比對為**字面比對**，同一物換個詞（`button graphic` vs `icon`）會假紅 ——
  現行語料無此形態，**故未加同義詞表**（加了就要維護，而維護不動的詞表會過期）。
- 語料 **108 條**（修改其中 1 條）；全閘綠：lint 108/0、self-test 64/64、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 29/29**、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致、
  lint_outbound_doc 8/8。
- **第四批未生成** —— 待其取樣清單經覆核且 17 條讀畢。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第二十九輪已完成（2026-08-18）—— **G18 擴掃、第三批覆核包、第四批取樣**

- **S-1**：G18 擴及 `pre_conditions`，**僅限引號內字面值**；
  非引號之設置描述（`The vehicle is stationary`）**不掃** ——
  全掃會把每一句測試設置都判成「溯不到源」，**那是判準錯**。
- **另自我加窄一層（下放包未要求）**：本次**只擴引號內，未擴未加引號之數值／狀態值**。
  理由：pre-condition 之數字多為測試設置，而其登記機制（`TEST_SETUP_NUMERALS`）
  是為 ER 而設 —— **貿然擴會產生一批只為轉綠而生的登記，那比不設閘更糟**。
- **首跑紅 0 —— 並先證明它不是「沒掃到」**：本次擴掃之實際母體為
  **10 個字面值**（分布 10 條 TC），逐一列出其溯源（3 個逐字見於被引之節、
  7 個經 `UI_LOCATORS`）。**10 個全部溯得到，故 0 為實質結果。**
- **其中 `100` 之 `“Driver 1-2”` 值得記**：它正是 28 輪出處對照抓到、
  而 G18 當時**結構上看不見**的那一個。**同型缺陷自此由閘承擔，
  不再倚賴人工出處對照。**
- 方向性案例 ＋4（共 **64 / 64**），其中一條是**護欄** ——
  「pre 之非引號設置描述不得轉紅」；**若它倒了，代表擴掃溢出成
  「凡 pre-condition 皆須溯源」**，正是 S-1 明文禁止之情形。
- **作業 2**：`29_review_pack_30.md`（743 行、30 條），格式同 21／23 輪。
  檔首另列**生成時四項先具名處置之落點**，使覆核者不必回頭翻 28 包。
  **未經第二人讀過者仍為 30 條** —— 本輪只交格式。
- **作業 3 第四批取樣**：ch5 餘 **38 leaf**，一葉一 TC ＋ 兩條額外
  （`030-01` 之「**只能**自 Edit Profile 連」為全稱限制，須反向；
  `041-04` 之失敗路徑須注入情境）＝ **估 40 條**，**逾 40 之風險實質存在**，
  且會是迄今最大的一批（前四批 16／28／29／30）。
- **切分建議不按湊數目，按 spec 自己的條款家族界線**：
  5.12 起條款由 `PRACC` 變 `ALLPR` —— **那是 spec 換了家族，不是我方畫的線**。
  第四批 ＝ 5.1–5.10.1（25 leaf ≈ 26 條）、第五批 ＝ 5.12–5.16（13 leaf ≈ 14 條）。
  **若分析層仍要一批做完亦可執行** —— 分兩批之理由主要在**覆核節奏**
  （前三批之覆核各積欠 2–5 輪）。
- **pending 兩 axis 與 (b) 類三處，依令具名其兌現批次**（不再以「待後批」帶過）：
  `046`（6.1 axis）與 `047`（6.2，(b) 類）→ **第六批**；
  `065`（8.1 axis）與 `073-02`／`073-03`（8.7，(b) 類）→ **第七批**。
  其依據為**剩餘 80 leaf 全數落位之規劃**（第四 25 ＋ 第五 13 ＋ 第六 19 ＋ 第七 23 ＝ 80 ✓）。
  第六批合併 ch6 ＋ ch7，因兩者各不足一批且**在使用者旅程上相鄰**
  （進入車輛 → 預設 profile → welcome popup）。
  **本規劃不取代 `audit_variant_pairs` 之絆線，是給它一個期限。**
- **第四批之已知寫作限制先具名**：`044`（5.15.1）之條文為
  `follow the **Core HMI Logic and Flow** truncation rules` ——
  **該規則在另一份文件，不在本 feature 之 spec 基線內**：
  可驗「過長時發生截斷」，**不可寫截斷之具體規則**（§8.4.1）。
  形態同 `002-02` 之 R-U27，為第四批之唯一同型者。
- 語料 **108 條未變**（本輪未生成、未改任何 TC）；全閘綠：
  lint 108/0、**self-test 64/64**、variant 11/11、batch_context 8/8、render 7/7、
  audit_consistency 25/25、audit_variant_pairs 7/7、audit_delegation 8/8、
  override `--check` 一致、lint_outbound_doc 8/8。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第二十八輪已完成（2026-08-18）—— **第三批 30 條落地，語料 108 條**

- **第三批 ＝ ch4 剩餘 26 ＋ `009` 之負向配對 1 ＋ A-UP13 附掛 3 ＝ 30 條**
  （`tc_id` `079`–`108`）。leaf 覆蓋 **72 → 100 / 180**。
  **批界依 R-4 一律如此書寫，不寫「第三批 ＝ ch4」** ——
  附掛三項落在 ch6／ch7，**批界是被修訂，不是被稀釋**。
- **`005`（4.3.1）之順序斷言 —— 本批最值得單獨講的一條**：
  條文要求「切換前**先**存」，而「切走再切回，值還在」**證不了先後** ——
  它與「載入 B 之後才寫出」同樣相容。
  **能分開兩者的是 ER2**：若實作在 B 載入後才寫，**那筆變更會落到 B 上**；
  故 ER2 斷言 B 顯示的是**它自己的值**，不是步驟 1 所記之值。
  **兩條 ER 併存才構成順序之斷言**，任一單獨都不夠。
- **生成時被閘擋下 7 處，皆我方之錯**：G15 五處（步驟 14／20／14／13／13 詞）、
  **G18 兩處** —— 後者**判定是對的**：`091`／`105` 之座椅編號 `1`
  確實不在條文裡（4.4／4.5.2 只寫 memory seat buttons／position）。
  **處置不是放寬閘，是把它登記為測試設置（J-12）並在 TC 內說明它不是條文來的。**
- **R-1 對外文件最小閘**（`lint_outbound_doc.py`，8/8）：
  只查「敘述之筆數 vs 表列之列數」。
  **v1 判準對它所為之文件本身誤報兩處** ——
  一段同時寫總數與本表筆數（`seven … four of the seven`）、
  另一段之 `180 leaves` 根本不是在數那張量測表。
  **一支會把正確文件判紅的閘活不過三輪（R-G9）**，故收兩道
  （被數之物須見於表頭／首欄；段內任一數字命中即通過）。
  修正後 **v2 綠、v1 之原始缺陷仍紅**；**兩個誤報案例已納為護欄**。
- **K-4a 生成後紅 4 條，逐條判而非一律放寬**：`099`／`106`／`108` 為**判準漏詞**
  （刪除 profile／客製化／自 popup 選另一 profile 皆造成**持續狀態**改變），補詞表；
  **`103` 為案例錯 → 改判功能測試** —— 按鈕 highlight 隨區段開闔而變是
  **條件式呈現**，不是狀態機遷移（沿 P-1 之 §8.7.4 分野）。
  另補護欄案例「只有開啟／讀取之 procedure 標狀態轉換 → 仍須紅」，
  守住 `open`／`read` **未**被收進詞表。
- **出處對照抓到閘抓不到者**（`28_provenance4.md`）：
  **`G18` 只掃 `expected_result`，不掃 `pre_conditions`** ——
  `100` 之 `“Driver 2”` 溯不到 4.5.4（該節寫的是 `default **Driver 1-2**
  Profiles`，`Driver 2` 單獨出現在 4.5.1）。
  改用本節自己的寫法，**未另引 4.5.1**（引之即多引）。
  15 個引號字面值**未溯得者 0**；**本批無任何 R1 High／China 變體條件**，
  與 25 包取樣清單之預告一致。
- **R-2**：`ANOMALIES.md` 之「整體位移」**加註而不刪原文** ——
  刪掉就看不出「曾經主張過一個未經證明的模式」。
- **R-3**：Q-1 引號界線寫入 profile §3.3.1（散文內嵌加引號／逐列轉錄不加），
  **`039`／`013` 不改**；≥7 詞閾值之盲區一併寫入。
- **P0 比例 33 / 108 ＝ 30.6%**（前為 30.8%），**未因批次擴大回頭調判準**（J-9）。
- 全閘綠：lint **108/0**、self-test 60/60、variant 11/11、batch_context 8/8、
  render 7/7、**audit_consistency 25/25**、audit_variant_pairs 7/7、
  audit_delegation 8/8（紅 0 黃 13）、override `--check` 一致、
  **lint_outbound_doc 8/8**。
  **本輪未執行任何 git；RD v2 未寄出（Tier 3，屬 Pei）。**

### 第二十七輪已完成（2026-08-18）—— **對外 RD 查詢單 v2**

- **X-1（必改）**：v1 附錄寫 `seven leaves … displaced` 而其下只列 4 條。
  **採「列出全部七條」，並分兩表** —— 4 條「Title 指向他 leaf 之 Description」
  （逐條標明**那是誰的 description**）、3 條「與自身一致」。
  **比下放包所給之兩案多一步**：只寫「四條錯置」，收件者仍得自己去數另外三條；
  **把沒問題的三條也列出來並說明，對方才不必回頭查**。
- **並順帶更正一處措辭**：三條「一致」中，`125-01`／`125-02` 之 Title
  **只涵蓋其 Description 之一部分**（`125-01` 取的是**例外子句**，
  主句「只有 HVAC／Media 可用」未入標題）。那不是錯置，但也不是全然精準 ——
  **對外文件不宜把「不完全精準」寫成「一致」而不加說明**。
- **X-2（必改）**：刪去 `shifted by one position`。七條實查顯示
  **`125-03`／`125-04` 取自 12.8.1 組，而 `126-01`／`126-02` 取自 12.8 組 ——
  兩組互相取用，不是單向的 +1**，稱其為位移是未經證明之推測。
  改為中性敘述，**並另加一段明說我方不主張模式**
  （「證據無法顯示是否出自單一編輯操作」）——
  **收件者若自己看出「像是位移」會想知道我方為何不說，明寫比留白更不易被讀成疏漏**。
- **X-3（建議）採納**：新增「Source document」節，
  **檔名與 037 所引之 Source ID namespace 並列**並明記為同一 artifact，
  附驗證（169 列 `Source ID` 全落 `CR24798 (October 03 2023)` namespace、
  037 之 135 個唯一 section id 命中 100%）。
  **下放包之顧慮我認為低估了**：兩識別差**八個月**且後者帶 CR 號 ——
  只給 `R1L-R (Feb 2023)`，對方合理的第一反應是「這查詢基於過期文件」，
  **於是先要我方更新再回答，兩題各多耗一個往返而問題根本沒被回答**。
- **v1 加 `WITHDRAWN` 標頭留檔**（內容不刪），標明三處缺陷與**「本版從未寄出」**。
- **ch4 第三批取樣清單：已出，在 `25_batch03_sample.md` §B**（該檔第 149 行起，四小節）。
  **26 包 §6 只用一張表寫了「已完成」，沒指路** —— 分析層在 26 包找不到是合理的。
  **不另出 `27_batch03_sample.md`**；為便對照於上繳文重述其結論
  （26 leaf ＋ 3 附掛、估 30 條、`079`–`108`、批後覆蓋 100/180）。
  **自陳一項流程改進**：往後回報「前輪已完成」之項目，**一併寫出檔名＋節次**。
- **自陳（本輪最值得記者）**：v1 之三處缺陷都在我上一輪寫的同一份檔內。
  `seven` 與 4 條之不符尤其明顯 —— **附錄之表我是從 23 輪之掃描結果（4 條）抄的，
  而「七個 leaf」來自 A-UP11 之範圍句；兩個數字來自兩個地方，我沒對過**。
  **這與 C-2／P-3（同一條 TC 內兩處記載互相矛盾）是同一形狀，只是換到文件層** ——
  內部已為此立了 G20，**對外文件一支閘都沒有**，已列待驗項。
- 語料 **78 條未變**，**本輪未動任何腳本、任何 `generated/`**；
  依 27 包作業 4，全閘不重跑，沿用 26 輪結果（皆綠）。
  **本輪未執行任何 git；RD 查詢單未寄出（Tier 3，屬 Pei）。**

### 第二十六輪已完成（2026-08-18）—— **R-U56 範圍界定、DR 拆分、連帶掃描**

- **R-U56 逐字入庫**（`RULINGS.md` 第二十六輪條文），含其末段
  「**本條為 feature-level；升為全域須 Pei 另行一句**」——
  **未依其為他 feature 認定範圍**（R-U13 之界線）。
  profile §0 範圍段加註指向，§4 缺口表據此改列。
- **DR #3／DR #7 改 `CLOSED — OUT-OF-SCOPE (R-U56)`，全部實測記載保留**：
  `3.1`–`3.5` 之可讀性（05 輪自 PDF p5 抽出）、與 Comfort R-C16 之形態比對、
  R-U28 之性質重估推理、以及「037 在 8.8 對螢幕尺寸切兩個 leaf、
  在 9.1.1 只切一個」之佐證 —— **事實不因關閉而失效**。
- **並明記 `3.1`–`3.5` 之使用不受影響**：R-U22／R-U46 已裁其為
  `PROF-001-01`（SWE 有寫之 leaf）之 in-scope 依據，`3.x` 繼續併列。
  **關閉的是「向上游索取」這件事，不是那些條文的可用性 —— 兩者不同。**
- **A-UP02 改 OUT-OF-SCOPE（已裁），記載不關閉**：變的是**身分**（待辦 → 已裁之事實），
  不是事實。並記一個不逕行關閉的可推理由 ——
  **若日後 037 補上那些 leaf，這份實測就是現成的對照**。
- **#5／#6 改獨立送出**，「併 DR #3」字樣已移除。
  並補一條**可檢驗的送出門檻**：兩題續送之共同點不是「重要」，而是
  **leaf 存在、TC 已生成、答案會改變已生成之內容** —— 比主觀判斷穩固。
- **作業 4 連帶掃描：命中 3 處，改述 1 處。**
  `TC-012` 之 PU0609 句（037 無對應 leaf）改為 OUT-OF-SCOPE，
  刪去「已列覆蓋缺口／具名上報」之待辦語；
  **保留其「xlsx 側掉句、觸發不同、本 TC 不代測」** —— 那些與範圍判定無關。
- **最要緊的一條分辨：`TC-005` 之「覆蓋缺口」判為 R-U56 不適用。**
  R-U56 關的是「SWE 未切 leaf」者，而該行為寫在
  `SWE1-HMI-PROF-048` **自己的 description 裡**（SWE 有切、已取樣），
  只是本 TC 只驗了前半 —— **那是我方覆蓋不足，不是範圍問題**。
  **一併改成 OUT-OF-SCOPE 等於用一條範圍裁決掩掉一個自己的缺口**，
  正是下放包所禁者之對偶。已於該處加註，使日後讀者不必重推。
- **作業 5** `26_rd_queries.md`（英文可寄版，Tier 3 由 Pei 寄出）：
  #5 含座標複位證據（註記 y=275.9–286.7、該列 y=289.8、其餘列無 `****`）；
  #6 含兩種答覆各自之處置且**兩種都不刪 `TC-077`**；
  另**把「兩條件確為不同」之證明寫進查詢單** ——
  上游若不先接受該前提，第二問無從回答，
  **把前提留在我方文件而只送問題，是把最容易被駁的一環藏起來**。
  A-UP11 列附錄並標明 **for information only, not a request**。
- **自陳之判準風險**：§4.3 之分辨無閘 —— 「SWE 未切」與「SWE 切了而我方只驗一半」
  兩者措辭都可寫成「覆蓋缺口」，**下一次很可能又混**。
  建議：凡寫「缺口」者須併寫其 leaf id 與該 leaf 是否已取樣。
- 語料 **78 條未變**（本輪只改記載，未動任何測試內容）；全閘綠：
  lint 78/0、self-test 60/60、variant 11/11、batch_context 8/8、render 7/7、
  audit_consistency 23/23、audit_variant_pairs 7/7、audit_delegation 8/8、
  override `--check` 一致。**本輪未執行任何 git**。

### 第二十五輪已完成（2026-08-18）—— **Q-1 反向掃描、G20、第三批取樣清單**

- **覆核結清**：78 / 78 條全部經第二人讀畢，未經覆核者為 0。
- **A-1 Q-1**：`TC-075` 之逐字顯示文字加雙引號；並補**反向掃描** ——
  **G18 查的是「引號內之字面值溯不溯得到源」，查不到「該加而未加」**。
  全批命中 7 處，**逐條判皆非缺陷**：七處都是**行為敘述**與 spec 措辭相同，
  而非「螢幕上出現的那串字」。
- **第八處逼出一條界線**：`TC-039` 之第 m 列與 `075` 是**同一串字**，
  一處要加引號、一處沒加。差別在 ——
  **散文中內嵌之顯示文字加引號；逐列轉錄之表格內容不加**（列表形式本身即標示其為轉錄）。
  **這條界線語料早已一致遵循**（`013` 之畫面標題加、其 Table CPA2 四列不加），
  本輪只是把它寫下來並落為掃描判準（子層列舉行不計入）。
  **具名其為歸納所得而非 canon 明文** —— 若判為轉錄列亦須加，
  `039`（15 列）與 `013`（4 列）皆須改，**待明示，不自行擴張**。
- **A-2 立 G20**（`remarks` ↔ `specification_reference`）：C-2（20 包）與
  P-3（24 包）為同一形狀之兩次發生，**兩次都是改了一處而未掃同一條的其他記載**。
  判準**只取「宣稱有引用」之語境** —— remarks 常需說明某節**為何不列**，
  若把所有節號都算宣稱，**這條閘會逼人刪掉正確的說明，那比不設閘更糟**。
  四個方向性案例中，「說明為何不列 → 綠」是**護欄**。
- **A-3 A-UP13 歸屬 —— 推翻我自己 23 輪的結論**：查 037 母體後發現
  **7.2.1 有三個 leaf**，行為 2／3 **各有專屬 leaf**（`059-02`／`059-03`），
  只是尚未取樣 —— 屬 **(b) 類待兌現承諾，不是覆蓋缺口**。
  **成因**：23 輪我查了 7.2 與 7.2.1 之**條文**，**卻沒查該節有幾個 leaf**。
  真正的缺口只有第 1 項（6.2.1 之 `048`，其 description 後半無 TC）。
  並先寫下一個反面：**該項不可委派予 `007-02`（4.5）** ——
  「刪除全部後 Driver 1 重建」與「客製化後不再是預設」是兩件事，
  **兩者措辭極近，正是下一次假委派最可能的落點**。
- **B 第三批取樣清單（不生成）**：主體為 **ch4 剩餘 26 leaf**（實測與下放包所估相符），
  另 **3 項附掛**（A-UP13）。估 **30 條**（`079`–`108`），批後 leaf 覆蓋 72 → **100 / 180**。
- **三項必含逐條具名**：(b) 類委派本批兌現 **2 / 5**（`047`／`073-02`／`073-03` 留待後批）；
  §7 配對中 ch4 多數**037 已自行切成兩個 leaf**天然成對，
  **須額外造者僅 `009`** —— 其條文之「**永遠只有一個** Driver Profile per memory
  seat position」是全稱，只驗互換成功則一個允許兩個 profile 連同一座椅之實作會通過；
  **變體對造之新 axis 為 0，且具名其為「查過」而非「沒查」**
  （6 個 axis 全落在 6.1／8.1／9.1／10.3.1／11.4）。
- **附掛三項具名其不在 ch4**：若不具名，「第三批 = ch4」這句話往後會對不上實際內容。
- **`002-02` 之寫作限制先講**（R-U27）：DR #4 未到齊，該 TC 得生成但
  **popup 內文之逐字 ER 不寫** —— 本批唯一帶著上游未決事項生成的 leaf。
- 語料 **78 條未變**；全閘綠：lint 78/0、**self-test 60/60**（＋G20 4 案）、
  variant 11/11、batch_context 8/8、render 7/7、**audit_consistency 23/23**（＋Q-1 3 案）、
  audit_variant_pairs 7/7、audit_delegation 8/8、override `--check` 一致。
  **本輪未執行任何 git**。

### 第二十四輪已完成（2026-08-18）—— **需求單位判準、判級對調、全稱 ER 收斂**

- **P-4（阻塞第三批之前置）**：以 **180 leaf 全量實測**回答「title 與 description
  何者為需求單位」——
  **Description 以 spec 條款編號起首者 105 / 180，而 Title 為 0 / 180**；
  Description 前 60 字元逐字見於節文者 120 / 180；
  對節文之詞彙涵蓋率 Desc 0.859 vs Title 0.667（逐 leaf：Desc 較高 130、Title 較高 29）。
- **決定性論證不是統計，是分割**：12.8（PVAL8）有六個斷言，
  四個 leaf 之 **Description 恰好無重疊無缺漏地分割它**；
  **若以 Title 為單位，同一組 leaf 會同時缺漏與重複** ——
  PVAL8 之「狀態列互動受限」將無 leaf，手套箱提示會有兩個，
  且 `125-03` 之 Title（`Glove Box Lock Prompt`）所指行為**根本不在 12.8**，
  **與該 leaf 自己的 `outline` 相衝**。
  **一個需求單位不可能指向不屬於自己章節的行為。**
- **故 `TC-057`～`TC-062` 不重生成** —— 其驗證目標未錯置；
  TC 標題亦早由執行層依 Description 另擬，未沿用錯位標題。
  判準落 `DECISIONS.md` **D-UP24-01** 與 profile §1.1。
- **A-UP11 降為記載瑕疵，但不關閉**：錯位仍在 037 內未修，
  **任何以 Title 為索引找 leaf 的人在 12.8／12.8.1 仍會找錯**。
- **P-1 依建議對調**：`062`（手套箱鎖按鈕變灰）P0 → **P2**（同 `060`）；
  `063`（按下不生效、鎖定狀態未變）P1 → **P0**。
  21 輪之理由「變灰即防線之執行手段」**正是 canon §8.7.4 逐字所否定者**：
  `A visual state (greyed-out, dimmed) does NOT imply non-operability` ——
  **變灰是指示，不是機制**；一個變灰而按下仍解鎖之實作，`062` 會通過。
- **連帶更正一個做法**：21 輪對 `063` 寫「兩者各半，**取中**」——
  **「取中」本身就是錯的**。判級取其**核心斷言**，不取各 ER 之平均。已寫入 profile §3.1。
- **佐證更強於 24 包所述**：查證「手套箱真的鎖上」之唯一斷言在 `064` 之 ER2
  （`the glove box is locked`，屬 12.8.2）—— `062` 是該組四條中
  **唯一完全不觸及實體狀態者**。
- **P-2** `TC-070` 之 ER3 由全稱收斂為 spec 點名之 `PU0934`。
  **加一層 24 包未點出的理由**：13.2 逐字為 `must be blocked (PU0934, **etc**)`
  —— **`etc` 表示 spec 自己未列盡該集合；spec 沒列盡的東西，ER 不可能驗得完**。
- **該改動使 K-4a 立刻轉紅，而紅的是判準**：移除 `is blocked` 後詞表比對不到，
  但 `TC-070` 仍是負向測試（procedure 步驟 1 即對不該生效之操作的嘗試）。
  判準補「嘗試後無作用」（`does not open`），**刻意不放寬到 `no X is shown`** ——
  否則 21 輪剛判為功能測試之 `TC-047` 會被誤收。
  方向性案例 18 → **20**，其中一條是**護欄**（純缺席斷言仍須紅）。
- **P-3** `TC-072`：**改 remarks，不補列 12.6** —— 補列會立刻被 G17 判多引
  （19 輪首跑即以此擋下它）。**成因是 19 輪改對了引用欄卻沒同步改 remarks**，
  與 C-2 同形之再犯；已列待驗項（`remarks` ↔ `specification_reference` 現無閘）。
- **23 包之 M-1～M-5／M-7 照原指示，已於前一輪完成**；本輪 profile 再增
  §1.1（需求單位）與 §3.1（§8.7.4 交互）。
- **M-2 之閘在同一輪內攔下立閘者本人**：`062` 之新 reasoning 我寫
  「由 **126-03** 承擔」，D-1 判紅（非合格 leaf id），已改。
- 語料 **78 條未變**；全閘綠：lint 78/0、self-test 56/56、variant 11/11、
  batch_context 8/8、render 7/7、**audit_consistency 20/20**、
  audit_variant_pairs 7/7、audit_delegation 8/8（紅 0 黃 7）、override `--check` 一致。
  **本輪未執行任何 git**。

### 第二十三輪已完成（2026-08-18）—— **profile 檔補建、委派可驗化、覆寫母體擴掃**

- **M-1 profile 檔補建**：`docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md`
  （本 feature 原為九個中唯一無 profile 者）。
  **移入者只有一條** —— D-UP22-01（§11 方括號例外），因 canon §11 **明文指定**
  profile 為其載體；`DECISIONS.md` 該節改為權威載體變更聲明，條文留檔。
  **其餘八條為「重述」不是「搬移」**：`RULINGS.md` 是 Pei 裁決之逐字登記，
  **把裁決條文搬出裁決檔，會使裁決失去其權威載體**。歸位清單具於 profile §6，
  另具名四類**判定為非 profile 條款**者（素材處理判準、判讀口徑、盲區聲明、
  一次性流程裁決）。
- **M-2 委派指名 leaf**：8 處委派改寫，落 `audit_delegation.py` 三閘
  （D-1 指名／D-2 存在／D-3 節文含詞串），方向性案例 **8 / 8**。
- **D-3 之判準倒了兩次，兩次都是被自己的案例逼出來的**：
  v1 之回看窗取最短前綴，**把剛指名之 leaf id 切在窗外**；
  v2 之單詞比對讓 23 包點名要擋下的那一案判綠 ——
  `does not support connectivity` 與 `does not support the connected profile
  feature` **共用三個詞，差別在詞的組合不在詞**。v3 改比對最長連續詞串。
  另補方法學停用詞：`TC-028` 之唯一術語為 `pre-condition`，v2 判其假委派，
  複核 9.5.2 節文確認**委派成立** —— **紅的是判準，不是案例**。
- **黃清單掃出另兩處假委派 → A-UP13**。**這兩處是「黃」抓到的，不是「紅」**：
  兩者之委派句都無 ≥3 詞英文詞串，D-3 **不可能判它們紅**，
  是人工複讀條文才發現。**若當初把「黃」設計成「綠」，它們會原封不動地留著。**
  形狀與 A-UP12 不同 —— A-UP12 是**互指**，A-UP13 是**外推**：
  `TC-005`／`TC-007` 把行為推給鄰節，而 `6.2.1`／`7.2.1` 之條文裡**本來就寫著那些行為**。
  **三個行為現無任何 TC 覆蓋**；記載已更正，**覆蓋具名延後**
  （23 包已逐條列舉覆核包之 35 條組成，再加未覆核之 TC 是把同一個問題做大）。
- **M-3 覆寫母體擴掃**：六組語意形態掃 PDF 全 21 頁，命中 14 處**逐條判讀、未判 0**，
  落 `data/override_notes_m3.tsv` 並以 `--check` 防飄移。
  **真正的漏不在 `**`，在 `kind` 欄** —— `6.1`／`8.1` 之兩條 R1 High 覆寫
  **有 `**`、也在 TSV 裡**，卻被 07 輪歸為「圖／表內標籤」。
  **擴掃 pattern 救不到它們，重新判 kind 才救得到。** V-1 母體 4 → **6 axis**。
- **三分法再細一層**：新增「**狀態條件**」—— `5.2` 之
  `A text will be displayed instead` 確是替代，**但條件是「達 5 個 profile」，
  那是狀態不是變體**；收進 V-1 會與一般條件式行為混為一談。
- **兩個新 axis 之 leaf 尚未取樣**，故立 `pending` 狀態並在閘裡留**絆線**：
  該 leaf 一旦生成 TC，`pending` 即失效轉紅，須改判配對或具名不配 ——
  否則它們會像 `017`／`039`／`013` 當初那樣被寫成前提而無人測。
- **M-6 A-UP11 全量掃描（承前四輪，本輪結案）**：偵測器以「title 與**他 leaf**
  之 desc 顯著更合」為判準，**在未被告知的情況下重現已知之四條** —— 此即其有效性之證據。
  全 180 leaf 命中 7 條，**新候選 3 條逐條複讀皆偽陽性**（詞彙巧合／描述超集）；
  另以全集比對得 4 條遠距命中，**皆非位移 —— 位移之特徵是近鄰**。
  **範圍確認為 12.8／12.8.1 七條，不及於其他 173 個 leaf。**
- **M-5**：037 之 180 母體中 `9.1.1` **僅一個 leaf**，另一側（大螢幕版面）無 leaf。
  **關鍵佐證：同一份 037 在 8.8 對螢幕尺寸兩側切了兩個 leaf**
  （`076-02` / `076-03`）—— 故非慣例，是**該節之覆蓋缺漏** → **RD #7**。
- **M-4**：`TC-077` 之「區域有 app」前提具名為**推得**，送 **RD #6**，
  並預寫「若答覆為不存在」之處置。**TC 不刪** —— 條件 2 是條文寫的。
- **M-7**：`23_review_pack_35.md`（864 行，35 條）。
- 語料 **78 條未變**；全閘綠：lint 78/0、self-test 56/56、variant 11/11、
  batch_context 8/8、render 7/7、audit_consistency 18/18、
  **audit_variant_pairs 7/7**、**audit_delegation 8/8（紅 0 黃 7，七處人工複核皆成立）**。
  **本輪未執行任何 git**。
- **自陳之新風險**：profile 之八條「重述」是複本，**複本會分岔**，
  而現無閘驗其與原載體一致 —— 已列上繳 §8 第 8 項待裁。

### 第二十二輪已完成（2026-08-18）—— **方括號閘、互指之委派、變體對造判準**

- **L-1 採 (a)**：立 §11 之 profile-scoped 例外（`DECISIONS.md` **D-UP22-01**），
  **與閘同生** —— 22 包之警語（「立一個沒有邊界的例外等於沒有規則」）照收。
  取 (a) 而非 (b) 之理由：9.1.1 之 spec 原文即含 `[username]`，
  改寫會改掉逐字內容（§8.4.1）；**TC-018 要斷言的正是「那一行長什麼樣子」**。
- **G19 不是禁令，是對照**：方括號 token 須在**被引之節**之原文內逐字找得到。
  5 個方向性案例中最關鍵的一條是「**同一 token `[username]`、只換被引之節 → 須紅**」——
  若日後有人把閘簡化成「該 token 一律放行」，**只有這一條會倒**。
  **記載限制**：canon §11 之例外原文為「feature profile 明定」，
  而本 feature 無 profile 檔，本條遂落在 `DECISIONS.md`，**兩者不同**，已具名待裁。
- **L-2：兩者非同一語意** —— 9.2 條件 2 為 `does not support the connected
  profile feature`（功能支援），11.3 為 `connectivity`（硬體配置），
  且兩者所隱藏之**對象也不同**。不等價之證明不需外部資料：
  **9.2 自身把「區域無 app」與條件 2 並列，若兩者等價則「區域無 app」無處安放**。
- **連帶發現：這是一組互指之委派** —— 9.2 稱條件 2「由 11.3 承擔」、
  11.3 稱第二句「由 9.2 承擔」，**兩條各自把那一側推給對方**。
  **單向指錯至少有一份記載是空的；互指則兩份都看起來已交代**，
  且兩份都通得過 G17／G18 —— **缺口在文字裡，不在數字裡**。
  補 `TC-077`（9.2 條件 2）與 `TC-078`（11.3 第二句）——**兩個洞，非一個**。
  登記 **A-UP12**。
- **順帶做完全量掃描**：78 條之 reasoning ＋ remarks 之「由…承擔」命中 21 處，
  分三類 —— **(a) 指向語料內存在之 TC（可驗）／(b) 指向尚未取樣之 leaf
  （是承諾，不是覆蓋，4 處）／(c) 假委派（已修）**。
  (b) 之四處已逐條查證其 leaf 確實在 037 之 180 母體內，
  **但在該批生成前，那幾句話所描述的覆蓋並不存在**。
- **L-3 立判準 V-1**：**觸發要件為「spec 有明文之變體覆寫註記」，不是「另有一種配置」**——
  否則 `(if applicable)`、螢幕尺寸、有無連網全部要配，**判準會擴張到不可能執行然後被放棄**。
  母體取 `pdf_starred_notes.tsv` 之 `變體覆寫註記` **4 條**，新增時閘會紅。
- **依 V-1 掃全批：4 個 axis 原本只配了 1 個。** 22 包點名 `017` 一處，
  **另兩處為本輪掃出** —— `039`（10.3.1 之列級覆寫）與 `013`（China market 之列）
  **同樣以「排除該變體」為前提，於是覆寫本身無人測**。補 `074`／`075`／`076`。
  `074` 之方向另記一筆：`017` 把變體設為前提，**base variant（多數車輛）反而未被測**。
- **「不配之理由須不適用於已配者」做成述詞，由閘實測** ——
  `absence_only` 對不配者須為真、對同 axis 之已配者須為假。
  **該閘首跑即抓出兩處錯，皆為述詞錯**（以句為單位太粗，被 `only if not complete`
  誤讀成否定；`literal` 寫死單一字串而 axis 兩側本來就是不同字串）。
  **閘沒壞，是述詞壞了** —— 分得開只因它同時驗兩個方向。
- **語料 73 → 78 條**，五條**全部掛在既有 leaf 之下**（非新 leaf，**故不是第三批**）；
  生成器另起 `gen_pairs.py`，因往 batch01 尾端追加會**撞上 batch02 之起點 045**。
- **未經第二人讀過者：30 → 35 條**（新增之 5 條同樣未經覆核）。
- 全閘綠：語料 78 條違規 0、lint self-test **56/56**、variant 11/11、
  batch_context 8/8、render 7/7、audit_consistency 18/18、
  **audit_variant_pairs 5/5**。**本輪未執行任何 git**。

### 第二十一輪已完成（2026-08-18）—— **R-U5 適用釐清與兩組一致性掃描**

- **K-1**：R-U5 之核心五類判為**例示，非窮盡** —— 不排除 canon §10.2 之其他
  P0 條件。加註入 `RULINGS.md` R-U5（**條文本身未改**，同 F-3 之先例）
  與 `DECISIONS.md` D-UP16-01 **附二**。
  **`R-U5 無安全帶` 之待裁自此結案**（17→21 輪，掛了四輪）。
- **為使 73 條可一致套用，另立一層細則**：同屬防線之條文仍須再分，
  否則整個 ch12 都會變 P0 ——
  **防線成立本身 → P0；防線之回饋或呈現（提示音、訊息、變灰之外觀）→ P2**。
  最能說明它的一對是 `TC-021`（受限項目**不可選取**）與 `TC-022`（選取時播 bonk）：
  **同節相鄰、同一情境，判級不同** —— 前者壞了防線就沒了，後者壞了防線還在。
- **改判 8 條**，P0 由 17 → 24（23.3% → **32.9%**）。**未因比例回頭調判準**（J-9）。
  **其中 5 條（`057`／`058`／`059`／`062`／`063`）屬執行層自行推廣**
  —— 21 包明列者只有 `089`／`116`／`135` 三條，故推廣者**具名待覆核**。
  並具名列出**最容易被誤以為該改而未改之三條**（`022`／`023` 為回饋、
  `060` 為呈現、`051` 為 spec 明訂之逃生路徑非防線）。
- **K-2**：TC-039 之兩列採 **(b) 逐列標適用條件**（spec 自身即以 `(if applicable)`
  逐列標之；(a) 會把配備寫成前提而使該 TC 只能在特定車上跑）。
  **`Electric Vehicle` 一列 spec 未標 `(if applicable)`**，其在非電動車上之行為
  條文未述 —— 依 §8.4.1 **保留歧義**：ER 不標其條件、亦不推定其不顯示，
  remarks 具名。**空白本身就是記載**。
- **K-3 指代掃描**：首跑 2 處**皆為判準之偽陽性**（TC-017 用**行內逗號**列舉，
  已列舉而非指代）—— **改判準，不改案例**；修正後 0 處。
  盲區補足（`--plural`）**先證其抓得到 C-1 之原句**再掃全批，
  命中 2 處逐條判皆非缺陷。**D-3／C-1 之同型在現行語料中無第三例** ——
  惟此為兩個判準之聯集所得，非窮盡。
- **K-4a**：首跑 3 處，**2 處判準錯**（非法性常顯示在 **ER** 而非 procedure，
  判準只看了 procedure）、**1 處真陽性** —— `TC-047` 是「到兩個地方看，
  那裡沒有該控制」，**找不到一個東西不是非法操作**，改 design_method 為功能測試。
- **K-4b**：首跑 **13 處，全部不是缺陷** —— v1 驗的是「basis 之用字在不在我的詞表裡」，
  **詞表不全不等於記載矛盾**。C-5 要抓的是**相斥**，v2 改為只在 basis 出現
  **別級**之定性詞時轉紅；修正後 0 處。
- **`audit_consistency.py` 落為工具**，並補 `--self-test` **18 / 18** 方向性案例 ——
  三項掃描皆以「0 處」收尾，而**一個永遠 0 處的掃描與一個壞掉的掃描，輸出相同**。
  紅向取本 feature 真實出現過之形狀（C-1 原句、C-5 之 basis、TC-047），
  綠向取**曾被誤判為紅者**（TC-017 之行內列舉、TC-022 之 ER 側非法性、
  P0 之「防護本身」）—— 即兩次判準修正之回歸。
- **作業 6**：`upstream/21_review_pack_40.md`（980 行）交出 **40 條**之覆核用全文
  （`TC-017`～`027` ＋ `TC-045`～`073`），每條含 spec 原文與 037 description。
  **本輪不改變「未經第二人讀過者為 40 條」這個數** —— 只是把它變成可讀的。
- **第三批未開** —— 依 21 包，待該 40 條之內容覆核完成。
- 語料 73 條違規 0、self-test 51/51、variant 11/11、batch_context 8/8、
  render 7/7、audit 18/18。**本輪未執行任何 git**。

### 第二十輪已完成（2026-08-18）—— **第一批覆核之修正**

- **執行順序與 20 包所設不同，已具名**：19 包作業 1–6 於上一輪即全部完成
  （`378cce5`），故第二批之生成早於本包之 C-1／C-2。逐項查證其影響：
  C-1／C-3／C-4／C-5 無影響；**C-2 有影響且對本包有利** ——
  BVA 自檢母體因此由 6 條變 7 條（第二批之 `TC-066` 亦為 BVA）。**未重做。**
- **C-1**：`10.3.1` 之「chart above」複位為 PDF p16 之 **Table PIP1**，
  15 列以 `render_spec_region.py --table` 機器讀出並逐列補入 ER。
  **工具在本案例上紅了兩次，都是判準錯**：
  1. 格線判準要求線段起點落在框內 —— PIP1 之垂直線起於 y=59.7、框自 y=60 起，
     **差 0.3pt 整條被排除**，結果回報「垂直線 0 條」。
  2. 改用 `Rect &`／`.intersects()` 仍為 0 —— **零寬矩形在 PyMuPDF 一律是 empty**。
  **兩次都以「這張表沒有欄」之形狀失敗** —— 不報錯，只回報空結果，
  不去對照渲染圖就會被寫成「無法判讀」。
  另擴充工具以回報**格內文字**（PIP1 是文字表，原樣輸出會是一片 `False`）。
  連帶發現 `****Connected Account` 為**列級**變體，已加 pre-condition。
- **C-2**：TC-036（9.9）**無 limit±1 亦無界前基準線**，由 BVA 改功能測試 ——
  18 輪 §1 之文字與 design_method 欄互相矛盾，直到本包點名才發現。
  全批 BVA 自檢：母體 **7 條**（20 包載 6 條，未計第二批），改判 1 後餘 6 條
  **皆有邊界對且皆有界前基準線**。
- **C-3**：TC-044 之 ER2 後半改為「無通往該畫面之入口」——
  **沒有按鈕時能證的是按鈕不在，不是畫面開不起來**。
- **C-4**：「偏好之儲存與回復」之 P0／P2 分野寫入 `DECISIONS.md` D-UP16-01 附一，
  並聲明其灰帶（「某設定項之值在 key cycle 後遺失」兩邊都沾）。
- **C-5**：TC-040 之 reasoning 改述，判級 P1 不動。
- **C-6 照錄**：TC-017～TC-027 之全文仍未逐條讀；
  加上第二批 29 條，**未經第二人讀過者現為 40 條**。

### 第十九輪已完成（2026-08-18）—— **第二批落地，語料 73 條**

- **J-10 之收穫是抓到我自己**：G17 加 `provides` 驗證後，兩個批次各現形一筆多引 ——
  `TC-022` 登記 9.3 提供 `cannot be selected` 而 TC 寫的是 `The selection is not accepted`；
  `TC-072` 併列 12.6，但本 TC 走 welcome popup 之按鈕，**12.6 那條路徑沒被用到**。
  舊版 G17「有登記就綠」兩筆都擋不住。
  G18 擴及未加引號之字面值後另紅 5 條，逐條追因**皆為判準未涵蓋**：
  BVA 界前值（29／11）屬**方法**、`steps 1 and 2` 之互參未被移除、
  狀態值 `Small`／`Off` 為大小寫差異（spec 散文小寫、UI 首字大寫）。
- **J-11**：variant 判定改只掃 `pre_conditions`／`test_procedure`；
  禁用字串之檢查仍及於 `remarks`（14 輪判定不變）。兩案例俱附。
- **J-12**：第四類「測試設置」落地 —— 座椅編號、3 碼、profile 數皆登記；
  與「方法」（BVA 界前值，承載驗證但權威為 §5.6）**分開登記**。
- **`134`（14.1）之 R-U51 判讀首次受檢：結論成立，理由有誤。**
  11 輪記「`above` 指向 14.x 之流程」—— 但 **ch14 只有 14.1／14.2，14.1 即首條**，
  其上沒有 14.x。實際指涉為 **12.3.1**（同一 PIN 退出），已補列引用欄。
  **結論對而理由錯，在別的案例上不一定還會對。**
- **A-UP11 新開**：037 之 `12.8`／`12.8.1` 七個 leaf **標題與描述整體錯位**
  （`125-03` 之標題寫手套箱、描述寫狀態列，餘類推）。
  以 `pdf_text` 複核後**描述與條文對齊、標題不對齊**，故本批依 **description** 生成。
  **未全量掃描 037 之 title↔description 對齊** —— 他章是否亦有，未知。
- **第二批 29 條（045–073）**：實得 29 而非 18 輪估計之 34 ——
  §7 之三處對照組**置於同一 TC 之 ER**（同觸發同條件，分兩條會產生除斷言外全同之 TC）。
  **若要求分立，改寫成本為三條。**
- **18 輪六項風險逐項回報**：`119` 之 `key on` 為條文明述（**非**裁決來源）；
  `128-03` 依 J-8 照寫並註明 30 分鐘成本，鎖定生效切給 `128-02`；
  P0 實得 8/29（全語料 17/73），依 J-9 未調整 rubric；G5 未觸發。
- **R-U5 無安全帶之待裁第三次提出** —— 本批 `116`／`135` 兩條落在該缺口上。

### 第十八輪已完成（2026-08-18）—— **範圍層級三修，雙向自檢入閘**

- **J-4 來源標示**：pilot 五處於 `reasoning` 具名其權威（**ER 文字未動**）——
  `ignition cycle` 屬**裁決**（R-U21，spec 從未提及）、
  BVA 之界前基準線屬**方法**（§5.6）。
  第一批之同型句數為 **0**：無 ignition cycle；`030` 之界前有 spec 依據
  （`until … exceeds` 之嚴格大於已含相等時不可用），`036` 無界前基準線。
- **J-5 之範圍層級查核揭出三條真缺陷**：對 PDF p14 複位後可見
  `****R1 High Only` 之標記掛在 **Table EDPR1 之 `Stellantis Account` 那一列**（**列級**）——
  - `TC-011`／`TC-023` 把列級覆寫當成**整條 TC 之條件**，而兩者之 ER 根本不含帳號 label，
    等於**無故把 TC 限縮到 R1 High 車上** → 移除該 pre-condition
  - `TC-020` 之 ER 用了 `Connected Account`（別節之變體形式），
    而 9.2 自己的字是 `Stellantis Connected Account` → 改回逐字
  - **並列一項待裁**：該覆寫是否及於 9.2 之 label，版面無從判定；
    取逐字（較窄）之代價是 **TC-020 在 R1 High 車上會假失敗**
- **J-6 落為兩閘**：`G17` 多引（引用欄之節須為本節／PLP／`REF_EXTRA`）、
  `G18` 少引（ER 之引號字面值須溯得到被引之節）。
  G18 首跑紅 5 條 —— `“Edit Profile”` 是分頁名、來源在 5.1，
  **不逐條把 5.1 灌進引用欄**（那會使引用欄變成導覽紀錄），
  改為一次登記於 `UI_LOCATORS`，並由 G18 **自我查核該登記表沒說謊**。
  方向性案例七案（含「登記表說謊須紅」），全批 **44/44**。
- **全批 44 條之雙向結果**：60 個節次引用（本節 44／`REF_EXTRA` 6／PLP 10）**全部登記在案**；
  ER 字面值全部溯得到來源。
- **第二批取樣（未生成）**：**ch12–14 共 29 leaf**，Valet Mode 一次收乾淨；
  估 **≈34 條**（29 ＋ 拆分 2 ＋ §7 配對 3），**未逾 40 故不提分批**，
  惟已寫明何種情況下應切 ch12 / ch13＋14。
  **must_carry 待追蹤實測為 0**（七條全數已被某條 TC 真的帶過）。
- **兩項提請生成前處置**：`128-03` 之 30 分鐘鎖定解除**跑不動**；
  **R-U5 無安全帶之待裁在本批放大**（第一批只 `089` 一條，本批可能十條以上）。

### 第十七輪已完成（2026-08-18）—— **第一批落地，語料 44 條**

- **作業 B（主要產出）**：`17_er_provenance.md` —— pilot 16 條之 **55 句 ER 逐句對照**。
  逐字引用 9／改寫自 20／由該句推得 8／無直接出處 18。
  **無直接出處再分兩型**：步驟回聲 14（正常，不承載驗證）、**真缺口 4**。
  四個真缺口集中於兩個形態：
  1. **`ignition cycle`**（TC-004／TC-010）—— spec 從未提及；
     「已儲存」是狀態不是事件，觀察方式由 **R-U21 指定，spec 沒有**。
  2. **BVA 之界前基準線**（TC-008 之 29 秒、TC-015 之第 9 次）——
     spec 只說「30 秒後清除」「第 10 次取消」，**沒說前一刻仍成立**。
     這是判準問題不是單條 TC 之問題，已列兩案待裁。
  另挖出**與 F-1 相反方向之引用問題**：TC-010 之 ER5 以「列於 Profile List」
  為觀察點，該行為出自 **5.1.1 而該節未被引用** —— 已補列。
- **作業 A**：J-1 之代價句入 `DECISIONS.md` D-UP17-01 **並寫進 `framework.md` §4.1**
  （覆蓋率分子一律取實際被驗之節，不取引用欄）——
  放在「135 與 133 不得互換」同一節，因為是同一種病的第二個病例。
  `scripts/render_spec_region.py` 落為工具，**回歸 7/7**；
  落工具時發現**欄別可機器判定**（勾記為同一張 61×64 PNG 置放 5 次，
  中心座標落在哪一格即答案），16 輪之肉眼判讀逐格複驗相符。
  建工具踩到三個坑，皆為判準錯：格線重複、勾記疊放、**表頭刪除線被當成列界**。
- **作業 C**：第一批 **28 條 TC（017–044）**，ch9→10→11 之 27 leaf
  ＋ `PROF-111` 之 R1 High 負向配對。語料合計 **44 條，違規 0**。
  - **風險① 有擋下，而且擋的是我**：`lint_variant_labels` 對 TC-017／023 轉紅 ——
    我在 `remarks` 寫「label 為 Connected Account（**非 Stellantis Account**）」，
    而 `remarks` 是測試員看得到的 AH 欄。判真陽性，**改案例不改判準**。
  - 風險② 9.5.x 四條之 sibling 軸：028 與 029 **只差一個變數**（前置是否已連結），
    其餘設置刻意相同，使失敗可歸因。
  - 風險③ ch10 三條先驗皆 Low，判出 **P2／P3 兩級**（038 為第二入口 → P3）。
  - **T-1／T-2 於本批首次真正被注入**（`PROF-085` 之 9.1 ＋ p14 兩條 must_carry）。
- **獨立判斷新增一項待裁**：**R-U5 之 rubric 沒有安全帶** ——
  `PROF-089`（行車中限制）失效之後果既非「核心能力被繞過」也非「體驗降級」，
  D-UP16-01 之兩分法接不住，本輪判 P1 是就近歸類而非判準給的答案。

### 第十六輪已完成（2026-08-18）—— **F-2 讀圖成功，第一批清單待覆核**

- **F-1**：TC-013 之 `specification_reference` 移除 `11.5`（保留 `11.4`）——
  **頁面共置不是章節歸屬**（§10.7）；`p17 → ["11.4","11.5"]` 之 must_carry 掛回不動。
  全批 16 條之引用逐條複核：`REF_EXTRA` 兩條（5.1.2／9.3.1）**其字面值皆逐字出現於 ER**；
  PLP `3.x` 併列兩條採**條文對象讀**（4.1 之 "all…listed in PLP table"、
  5.9 之 "any"）未改，**與 F-1 字面有出入，具名待裁**。
- **F-2 判讀成功，「永久限制」判定撤回**。關鍵不是抽圖 ——
  p17 之內嵌圖（HMI 示意）表格區被畫面捲軸裁掉；
  **Table CPA2 根本不是圖，是 PDF 之向量表格**，文字層把它攤平而版面一直都在。
  改以 `get_pixmap` 整頁重繪 ＋ 裁切區 6 倍放大即判讀完成：
  - **四列非五列** ——「Connected Profile App」是指向截圖之**註解框**，不是表列（14 輪誤列）
  - 欄別：Personalization **兩欄皆有**；App Store Download／Marketplace／
    Connected Navigation **僅 Connected Account**
  - **中國市場之排除為「列級」（Connected Navigation 那一列），非表級** ——
    14 輪之整條 pre-condition 範圍過寬，已於 remarks 更正其真實範圍
  - 表頭 `FCA` 有刪除線改 `Connected Account`，與 §8.7.3 同向
- **F-3**：P0 tie-break 記 `DECISIONS.md` D-UP16-01，
  並於 `RULINGS.md` R-U5 **末加註**（**條文一字未改**）；並聲明其盲區（失效後果無可測形式）。
- **F-4**：TC-004 未驗 5.9 全稱，記 D-UP16-02 —— **全稱命題以單例驗證**，本輪不擴充。
- **第一批取樣清單（未生成）**：**ch9 → ch10 → ch11，27 leaf**，
  ＋ `PROF-111` 之 R1 High 反面 = **28–34 條 TC**。
  批次邊界之理由：**結束時剛好結清 Editing 與 Connected Account 兩個 Test Set**，
  不把任一 Test Set 切在半路；T-1／T-2 由 `PROF-085`（9.1）一條 leaf 同時覆蓋。

### 第十四＋十五輪已完成（2026-08-18）—— **pilot 三項阻塞全清**

- **D-1 priority**：TC-002 由 P2 改 **P0**（回復原廠＝資料遺失風險項；
  原理由以「037 先驗 Low」覆蓋 rubric，方向與 R-U5 相反）。
  全批複核連帶再改 2 條（TC-005／TC-006 → P1）。**分布 P0×6／P1×6／P2×4**。
  **自立之 tie-break 已具名待覆核**：同為邊界形態，Valet 兩條判 P0、
  profile 建立兩條判 P1 —— 依「失效後果是否為完整性被繞過」分。
- **D-2**：TC-004 指名受測偏好為 PLP 表 3.5 之
  `Memory Profiles (Seats, mirrors, steering wheel)`，逐字取自 spec。
- **D-3**：TC-003 展開 PRACC7.2 之實際字串（並發現須排除 7 吋車，
  否則該 TC 在 7 吋車上**假通過**）；TC-013 以 §6.1 子層列出 Table CPA2 五列。
  **欄別歸屬不宣稱** —— PDF 文字層已把表攤平，無從還原，具名為永久限制。
- **D-3 揭出更深的問題**：`p17` 只掛 11.5，而需要那些列項的 TC 是 **11.4**。
  **需要的拿不到，拿到的不需要。** 改為多節掛回（引用者＋實體所在者）。
- **D-4**：補 G15 步驟長度閘 → **紅 14 處**（覆核所列 3 處為抽樣）→
  改寫 14 個步驟（一步塞多動作者拆步、最終步對齊 test_item）→ 綠。
  中途一次自我修正：`check the …` 觸發 G8，canon 要的是 `check that …`。
- **D-5**：`feature.yaml` popup_ids 20 → **21**（量測條件改標 `pdf_text`），
  原記載保留於註記；**新增 G16 防兩個數再度悄悄分岔**，三個對照向皆證。
- **S-1**：`PU_0118` 與 `PU1087` **同出 4.1.1 之同一句**，寫法之差異在 spec 本身，
  非抽取造成 → **不統一**（統一即改寫 spec 字面值）。
- **N-1／N-2／N-3** 全數處置；N-2 之「歸宿正確」以 `--selfcheck-tamper misplace` 證其會紅。
- **15 包**：R-U55（案 1，不動歷史）、**R-G12 升 canon** §9.2（同時補列 R-G10／R-G11）；
  **A-UP10 記 ACCEPTED 而非 RESOLVED** —— 問題未消失，是被接受。
  待執行之 git 清單依 R-G12 全部帶 pathspec，**canon 與 feature 分兩次 commit**。

### 第十三輪已完成（2026-08-18）—— **Phase 2 首批 TC 落地**

- **16 條 TC 生成**：`generated/<req_id>.json` 16 檔，`NR1L-UserProfiles-001…016`；
  生成器 `scripts/gen_pilot.py` 為單一來源、可重跑。**未寫回工作簿**（R-U14）。
- **lint**：`scripts/lint_tcs.py`（**本輪新建**，14 閘）語料 **0 違規**、
  `--self-test` **28/28**；`lint_variant_labels` 反向 7/7、語料 0 違規；
  `build_batch_context --selfcheck` 8/8（含兩向 tamper 皆紅）。
- **停手門檻改用**（13 包自裁）：判準歧義 **6 次取最保守解讀續行並具名**，
  未再逐項停等 —— 含 `~12` 取 12、不加 §7 負向配對、不用 `[spec-derived]` 標記、
  PU0609 不入 TC-012 之 ER、13.2 兩半不拆、11.5 之 CPA2 列項不入 ER。
- **三項缺陷（生成過程中發現）**：
  1. **`feature.yaml` 之 `lint.popup_ids` 為 xlsx 側量得（20 個）**，
     以 `pdf_text` 現測為 21 個 —— 多的 `PU0609` 正落在 9.8 之掉句裡。
     **以 xlsx 側清單檢查以 PDF 側生成之 TC，必然誤報。** lint 改現測，yaml 未動，待裁。
  2. 9.8 之 PU0609 句在 037 **無對應 leaf** —— 上游覆蓋缺口（同 DR #3 形態）。
  3. `variant_of()` **不處理否定**：pre-condition 寫「not an R1 High variant」
     仍被判為 R1 High（本批無害，具名待裁）。
- **lint 判準本輪改三次**（G6 pre-condition 誤報、G2 驗錯對象、G14 基準面不一致），
  **皆改判準不改案例**；G2 之對照案例隨判準更換為「重複／跳號」，G6 之誤報案例留作回歸。
- **`052f67d`**：其後提交數 4 → **5**（power 又疊一個），案 2／3 之 rebase 成本遞增。
  三案查無包號節次（提於 power session 之聊天，從未落檔）。**未自行處置。**

### 第十二輪已完成（2026-08-17）—— **p17 修好，三案重述，仍未生成 TC**

- **R-U49 四步**（順序不可調換，輸出俱附）：補第 7 項自檢 → **證明其紅**
  （`無歸宿者 = ['p17']`，exit=1）→ 改 `PAGE_TO_SECTION` 顯式對照表 →
  **8/8 PASS**。`impact` 散文欄自此不再參與任何比對。
- **連帶效果**：`p17` 現隨 sec 11.5 注入，而 `PROF-112-01` 在 pilot 取樣內 ——
  **T-3 已解**，待追蹤由三條減為兩條（T-1 9.1／T-2 p14）。
- **R-U52**：`plp_scan_union()` 收進自檢第 8 項，重算所得與常數逐條相符；
  對照向 `--selfcheck-tamper drop｜add` **兩向皆紅**（漏一條、多一條都抓得到）。
- **R-U50／R-U51** 寫入 `DECISIONS.md`：同節連坐四條件（**盲區：第 4 項無可測形式**）、
  判讀口徑採「指涉所指之物」，`PROF-106`／`PROF-108` 定案為否並記其代價。
- **`052f67d` 重述（R-U54）**：污染內容為**歸屬不準**（`feat(power)` 夾帶
  user_profiles 8 檔，內容本身完整）；成因為裸 `git commit` 提交整個 index。
  **三案查無包號節次** —— 提於 power session 之聊天回覆，從未落檔，
  **故分析層覆核記錄無此項與 R-U41 相符，非漏回應**；
  11 輪「三案已於前輪提出」之措辭經自查更正。
  **現況：已推送，其後 4 個提交** → 案 2／3 已需 rebase ＋ force push。**未自行處置。**
- **據實記載**：11 輪上繳後依 Pei 明確指示執行過一次 `add`／`commit`（`f653cb0`），
  以 pathspec 限定且逐檔驗證無他 feature 混入；未 push。

### 第十一輪已完成（2026-08-17）—— **R-U46 落地，仍未生成 TC**

- **10 輪之上繳補落檔**（R-U48）：`docs/upstream/10_pilot.md`，
  全部內容**自實際產物重出**（`grep` 讀條文、重跑 `--selfcheck`、重跑 PLP 掃描），
  **未以聊天貼文為據**；完整未截斷之 git 指令清單見該檔 §2.4。
- **R-U46 落地**：`PLP_ENABLED = True`；
  `PLP_LEAVES_AUTO`（甲∪乙，4 條）與 `PLP_LEAVES_MANUAL`（人工，2 條）**分列**。
- **盲區掃描**（R-G11）：180 leaf 全掃位置指涉，**命中 17／未命中 163／餘數 0**；
  逐條人工判讀記 `DECISIONS.md` D-UP11-01 —— **3 條指向 PLP 表，14 條不是**。
- **兩項具名回報**：
  1. `PROF-001-02`／`001-03` 與 `001-01` 同屬 sec 4.1 同一句，
     自動判準只抓得到 `001-01`；併列理由三條相同 → 一併列入。
  2. must_carry 實測為**覆蓋 4（9.3.2／9.8／11.4／11.5）、未覆蓋 3**，
     與 R-U47 所載之「3／4」不符。
- **新發現之缺陷（未自行修改）**：`must_carry_for()` 對 `p17` 之掛回條件
  以 `impact` 含節次字樣為準，而 `p17` 之 `impact` 為「同上」——
  **現況生成任何節次皆不會注入 `p17`**。待裁。
- **自檢 6/6**，第 6 項改為「已啟用」並**加入對照向**（非 PLP 之 14 條不得含 `3.x`，實測為空）。

### 第九輪已完成（2026-08-17）—— **條文收斂**

- **canon 新增 §9**：十一項通則（逐項附來源條號）＋ R-G1～R-G9 集中
  ＋ §9.3「一條裁決只管一件事」。**升格之單位為「原則」不是「條文」** ——
  `R-U6`／`R-U25`／`R-U16`／`R-U14`／`R-U35` 同時含 feature 事實，只升前者。
- **Tier 0 之 AUTO 三項已明列，各配一個反例** —— 只寫「可以做什麼」的清單，
  讀起來永遠比它實際的範圍寬。共同界線：**AUTO 管「怎麼做」，
  不管「做什麼」與「做出來對不對」；一旦選擇會改變結論，它就不是技術選擇。**
- **異議兩項具名**：
  (1) **C 類三條只有一部分被取代** —— `R-U3` 之 `spec_mode = A`、
      `R-U15` 之三項判讀、`R-U22` 之「037 沒引用不等於 spec 沒寫」
      **現仍生效且被其取代者本身引用**。整條標 `[SUPERSEDED]` 與事實不符。
      依 09b 照辦並附「仍然生效者」對照表，**請裁是否改 `[PARTIALLY SUPERSEDED]`**。
      `R-G7` 尤其 —— 它是**增補**不是取代。
  (2) A 類之升格單位（已逕行調整為「原則」，理由與請指正併陳）。
- **第四類有 1 條：`R-U8`** —— 其值為 feature-specific（歸 B），
  其通則部分之權威在 Comfort `R-C3`（引用而非重複升格）。
  **它為什麼會漏**：草案 B 類逐號列舉，而 `R-U8` 之相鄰兩號都在清單裡。
- **第 11 項通則是從這兩項異議歸納出來的**，不在任何下放包內 ——
  **收斂之副產品比收斂本身值錢**。

### 第八輪已完成（2026-08-17）—— **Phase 1 收尾**

- **R-U36：本條之前提有誤，據實更正。** 字內斷字**全在 xlsx 側**（4 個形態），
  **PDF 側 0 個** —— 07 輪本層寫「PDF 文字層有」是誤述。
  四者所在之 4 節皆已落「標點/空白差異」，**對 C 組影響 0**；
  **C 組終值維持 3.6% 節數／2.1% 字元**，補句表七條不增不減。
  判準之偽陽性風險四項已列（含詞庫不完整之漏抓下界）。
- **R-U37：注入抓到判準之缺陷。** 相似度比對之窗口長度不等，
  落在前面之候選其窗口吃進後一個候選之文字，ratio 被稀釋 ——
  兩個注入向因此選錯。**依 R-U37 改判準（等長窗口）不改案例** → 8/8 PASS，
  且稽核表逐位元組未變（**真實語料剛好不踩，故非注入驗不出來**）。
- **R-U35 四項落地**；`variant_label_overrides` 進 `feature.yaml`，
  lint **實跑 7/7** —— 含造假 TC 之三向，**另加一組本層自訂之「範圍向」**
  （R1 Low 用同一字串不得轉紅）：**一條只證明「會 FAIL」的規則，
  可能是一條對所有東西都 FAIL 的規則。**
- **`framework.md` 定稿**（仍待覆核），新增 §0 判讀依據面與 §6 生成階段之
  七條強制事項。
- **Phase 1 收尾清單**：已清 18／待清 8／永久 8。**Phase 2 起不再回頭翻前七包。**

### 第七輪已完成（2026-08-17）

- **R-U34：0 個跨頁條款。** 兩種互不相關之方法皆為負 ——
  尾句探針（次頁命中 1 節，經查為定位錯非跨頁）＋ 與 xlsx 無關之盲點檢查
  （頁末斷句＋次頁小寫續起，**0 / 20 個頁界**）。
  **故 2.9% 不再是下界**；訂正後之 C 為 **3.6% 節數／2.1% 字元**。
- **對照向揪出 06 輪之定位器缺陷** —— `PRACC7.` 被 `4.7`（p6）與 `5.1`（p7）
  **共用**，06 輪取第一個命中，於是把 `5.1` 對到了另一條條文。
  140 個標籤中 3 個重複。已加兩道修正（行首比對＋相似度消歧）。
  **這不是任何一條指示要找的東西，是對照向的副產品。**
- **三比率重報，各附分子定義**（R-G8）：
  **A 無頁界 17.1%／16.3%**、**B 加頁界 9.3%／6.2%**、**C 真掉句 3.6%／2.1%**。
  C 由 06 輪之 4 節改為 5 節 —— **計數單位不同**（`11.4`／`11.5` 分計），非計算錯誤。
- **29 個無標籤節**：26 命中、3 查無。其中 **`2.1` 是唯一一節 xlsx 比 PDF 完整者**
  （其參考文件表於 PDF 為圖）—— R-U25 之「xlsx 結構／PDF 內文」分工於此有例外。
- **R-U31 落地**：`outline_map.json` 增 `pdf_text`／`divergence`，**`text` 逐字未動**；
  補句表 7 列；`**` 註記全量 **10 條、6 有 4 無**（與下放包相符，惟條數隨 pattern 而變，
  另一 pattern 得 12 —— 檔頭已載明 pattern）。
- **R-U32：Service 22 條 0 條分群改變 → R-U21 維持。**
  **惟其地位變了** —— 06 包列為「未量之邊」，本輪把那條邊量了。
  結論相同、依據面不同，記錄上須分開。
- **作業 6 只清點未改**：`expected_cited_sections.tsv` 與
  `generation_sections.tsv` 各有 **9 列**之 `chars` 欄受影響。

### 第六輪已完成（2026-08-17）

- **169 條全掃（不抽樣）**，分母為標籤可定位之 **140** 節；
  逐節結果落 `data/xlsx_pdf_audit.tsv`。R-G7 對照向 PASS。
- **掉句率三個數，差六倍，資料同一份**：
  **17.1%**（第一版切段，把下一頁之頁首／圖說／表格算進條文，**高估**）→
  **9.3% 節數比／6.3% 字元比**（加頁界）→ **2.9%（4 節）真掉句**
  （逐條讀完，把切段殘留剔除）。
- **判定為系統性 → 依 06b 作業 3 停手上報，未重建 `outline_map.json`。**
  理由不在百分比：掉的是**變體覆寫註記**（決定適用範圍）、**表格內容**
  （決定 ER 列舉）、**含 PU id 之整句行為條文**；且 `9.8` 掉的是**純段落句**，
  **指不出一個「不會掉」的節型**。`****` 註記 10 條中 6 進 4 不進 ——
  **同形態時有時無，比整類都掉更難防**。
- **04／05 輪判讀之依據面已逐列標示**；要緊者為 **`Service` 22 條全部讀 xlsx**，
  而本輪證明 xlsx 可能少句 —— R-U21 之裁定因而有一個未量之邊。
- **PLP3 可讀，且不需 `pdfimages`** —— 一直在文字層；05 輪未定位到是因
  五表並排使其排在標籤**之前**。死路已記錄：**不是抽圖能力問題，是切段方向問題**。
- **`spec_popup_ids.tsv` 20 → 32**，加 `source` 欄；原 20 列記載未改。
- **DR #4 降 MEDIUM 並收窄**（spec 已載觸發條件，缺的只是 popup 內文）；
  **DR #3 性質改為上游覆蓋缺口**；`PROF-002-03` 解除阻斷。
- **N-XF01**：comfort 孤兒檔登為跨 feature note，**comfort 一個檔都沒動**。

### 第五輪已完成（2026-08-17）

- **跨 feature 掃描（唯讀）：無污染。** comfort 為 recon 形態**而非被污染**
  —— 它從無 `build_outline_map.py`，四份文件一致記載為「403 leaf 查表」，
  且無任何讀者。sxm／amfm／projection **無此檔**。
  **惟 R-G4 給 comfort 留下一個孤兒檔之連帶，待裁。**
  另更正 04 輪之漏數：home 之讀者是 **三個**（`extract_exemplars.py` 亦讀）。
- **home 實跑做不到** —— 其 `inputs/` 不存在（R-G2 條文自身所記）。
  改以「直接餵兩形態給三個讀者」，**危害由推導變為觀察**：
  chapter 集合由 `{BSP HS HSD HSS SNS SW}` **退化為 `{SWE}`**。
  含 R-G7 之兩個對照向，兩者一致。**`lint_tcs` 那一半仍是推導**（§2.3）。
- **抽圖能力：圖不在 xlsx，在 PDF。** spec xlsx **0 張內嵌圖**；
  BASELINE 第四列之 PDF 有 21 頁／174 個 Image XObject／有文字層。
  **與 Comfort A-CF23 方向相反 —— 不是缺讀取能力，是找錯檔案。**
- **6 節中 5 節改判，完全依賴歸零**：`8.2` 由**完全依賴**改為**不依賴**
  （流程圖之步驟／PU id／按鈕／分支全可讀），`6.2`／`9.1`／`10.2` 由部分改為
  不依賴；`11.4`／`4.6` 維持部分依賴（`4.6` 之理由改為 **spec 自稱圖示為
  placeholder**）。**04 包 §6.1 之 DR 候選建議撤回。**
- **PLP 表可讀**（R-U22）→ `PROF-001-01` 正常生成；
  **A-UP02 重估為「spec 有而 SWE 未涵蓋」**，形態同 Comfort R-C16。
- **順帶查到**：`spec_popup_ids.tsv` 之 20 個少算，PDF 全文有 **32** 個
  （12 個只出現在圖裡）；且 **`PU1087`／`PU1088` 在 spec 裡有觸發條件**，
  缺的是 Pop Up List 之內文 —— **DR #4 之範圍可能應收窄，待裁**。
- **`framework.md` 草案落檔**，每個數字複驗相符（180 leaf／133 生成 section）。

### 第四輪已完成（2026-08-17）

- **十一條入庫**（R-U13～R-U20、R-G4～R-G6 逐字）；三條全域條文另列。
- **R-G6 記載更正**：03 包 §8 之「git 未執行」改為據實之「執行了一次
  `git checkout`（單一檔案）」；§7.1 未動。R-G5 已追認該次還原，
  並裁定**其作法為錯** —— 遇覆寫事故應兩版並存、上報、停手。
- **A-UP04 → RESOLVED**（R-U18），永久記載限制照錄：
  **Phase 0 之 037 側數字沒有被複驗，也永遠不會被複驗**。
- **三閘反向驗證 6/6** —— 三型注入各自轉紅並報出正確差額；037 原檔雜湊
  前後一致。**含一個「複製＋重存但不改資料」之對照組** ——
  沒有它，另外三向證明不了紅燈來自注入。兩項標「未實測」而非 PASS。
- **`Service` 22 條逐條讀完：無一條符合 `[BLOCKED-NON-HMI]`（R-C38）**。
  該欄標的是「誰執行」而非「看不看得見」；ch4 之 12 條全屬「來回一趟」
  可觀察。**03 輪擔心的一整章返工不會發生。** 另揪出兩條屬別的阻斷
  （`PROF-002-03` 落 R-U15、`PROF-001-01` 依賴 A-UP02 之 PLP 表）。
- **14 節帶圖：不依賴 8／部分依賴 5／完全依賴 1**。
  **`8.2` 全文即「See flow … above」，一個可驗步驟都沒有 → DR 候選。**
- **R-G4 實作＋反向驗證 5/5**。前置查證揪出：home 之檔是**第三種 schema**，
  且 `make_batch_context` 之 `^([A-Z]{2,4})` **會命中 `SWE`** ——
  recon 若落在該檔名上，**每個 outline 之 chapter 都會變成 `"SWE"`**，
  不是崩潰，是安靜的錯答案。
- **R-U19／R-U20 落地**：`data/generation_sections.tsv`（133 列）新建，
  `expected_cited_sections.tsv` 未改；`feature.yaml` 記八組 Layer 2，
  **逐組實測全部相符，合計 180**。

### 第三輪已完成（2026-08-17）

- **037 已到齊並落錨**：SHA `9d176dde…` 首次進 BASELINE。Phase 0 之 037 側
  數字係在 **Project 附件副本**上量得且未比雜湊，本輪全部重測 ——
  **不是複驗，是取代**（該副本不在 repo，無從對它算雜湊）。
- **R-U8 三閘全數相符**：`Functional Requirement` **180**／`Heading` **25**／
  `Out of scope` **2**，合計 207 = 資料列數。未調整任何判準。
- **對照輸出 182 = 180 ＋ 2 Out of scope** —— A-UP07 之診斷由資料證實。
  另記 `recon.py` 之第三個數（被禁判準會選 **72**）：三個數並列，
  使日後無人再把其中兩個相減。
- **集合對集合 135 = 135，兩側差集皆空**；並查明 `recon.py` 之 133 與 135
  之分野 —— `4.7`／`5.11` **只被兩個 Out of scope leaf 引用**。
- **表頭列實得 row 7**；FROP 欄 `User Profiles` **182** 列，R-U1 首次複驗成立。
- **A-UP02 之 8 條於 037 側首次證實**（未被引之 34 條中含 `10.1`／`11.1`／
  `11.2` 與 `3.1`–`3.5`）。
- **BASELINE 4 列 → 6 列，`shasum -c` 6/6 OK**。
- **兩份 spec SHA256 相同**（`368d5874…`）—— **只驗未處置**，
  未刪未搬未改引用路徑；兩份皆列入 BASELINE 各自受檢。
- **Layer 2 草案第二版**：037 之 25 個 Heading 與章別分布到齊，
  出 11／8／6 三案，§4.2 三項命名問題逐項提案（Tier 2，不自裁）。
- **本層在本輪犯了一個錯並已處置**：跑 `recon.py` 前未查它會寫哪些檔，
  其產物覆蓋了 01 輪之 `data/spec_id_to_outline.tsv`（**同名而不同物**）。
  已還原，recon 之產物改置 `data/recon_leaf_to_section.tsv`，兩者皆不遺失。
  檔名歸屬屬 Tier 2（`features/home` 亦有讀者）。

### 第二輪已完成（2026-08-17）

- **R-U8 三閘落地**：`recon_assertions` 由 `TBD` 改填 **180／25／2**，
  182 降為對照輸出。**閘未跑** —— 037 仍不在 repo。
- **R-G3＋R-U10 canon 修補**：`docs/fw036/framework.md` §Workbook sync
  加 openpyxl 禁用警示（引 A-UP09 實測表）、範例改 `xlsx_surgical` splice、
  `Test Case Framework` 分頁項標 **rev A/B only**。
- **R-U12**：`archive/forms_superseded/BASELINE.sha256`（3 檔），
  `shasum -c` **3/3 OK、0 警告**。該目錄在此之前**不受任何雜湊保護**。
- **A-UP05／A-UP07／A-UP08 RESOLVED**；A-UP09 修補完成但**狀態變更屬 Tier 2**，
  本層不自裁，標為待覆核。

### 停下待裁 / 待覆核

| 項 | 內容 | 阻擋什麼 |
|---|---|---|
| ~~A-UP04~~ | **已 RESOLVED（R-U18）** | — |
| ~~135 vs 133~~ | **已裁（R-U19，兩者分立）**；`data/generation_sections.tsv` 133 列已建 | — |
| ~~`spec_id_to_outline.tsv` 之檔名~~ | **已裁（R-G4）並實作**；recon 改寫 `recon_leaf_to_section.tsv`，另加不得無聲覆寫之前置檢查 | — |
| **A-UP09 之 x14 DV gate** | R-U14 定其為解除條件；**gate 未立前寫回不得開工** | **擋 Phase 6** |
| **其餘四個 feature 之 `spec_id_to_outline.tsv`** | 現況未掃；若已是 recon 形狀則帶著 §7.2 之錯答案 | 不阻擋，未查 |
| **A-UP06** | **R-U9 之涵蓋驗證結果為 18/20**，缺 `PU1087`／`PU1088`（皆出自 spec `4.1.1` Profile Setup）。依 02b 明文不以近似版本替代 | Phase 3 之 popup 詞彙表；**已開 DR #4** |
| A-UP09 | R-G3 之修補已完成，**惟現行防線只是一段散文，無機器檢查** | 不阻擋；建議下一包立 gate（見上繳 02 §6 第 1 項）|
| Layer 2 | Test Set 邊界三草案（7／11／6 個 Set），**037 分群不可得，草案為 spec 單邊**；§4.2 之三項命名問題待併 | Phase 3 framework Part N |

### 阻擋中（素材，Tier 3 由 Pei 送出／取得）

| DR | 檔 | Urgency |
|---|---|---|
| #1 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`（A-UP04）| **BLOCKING** —— recon 全停 |
| #2 | HMI Pop Up List（A-UP06）—— **部分到齊 18/20**，見 #4 | 高（Phase 3 前）|
| #4 | **載有 `PU1087`／`PU1088` 之 Pop Up List 版本**（本輪新開）| 高（Phase 3 前）|
| #3 | A-UP02 之 8 條無覆蓋條文 RD-1 | 中 |

### 實作約束（已實測，非待裁）

- **A-UP09**：openpyxl 存回摧毀母本 R 欄 x14 下拉
  （`<x14:dataValidation>` 1 → 0、zip members 48 → 47，三條 legacy DV 存活）。
  Phase 6 寫回**不得**以 openpyxl 存回。`feature.yaml`
  `write_back.forbid_openpyxl_save: true`。

### 下一包之前置

1. ~~先裁 A-UP07~~ **已裁（R-U8）**，期望值已填。**037 到齊即可跑 recon。**
2. 037 到齊後：跑 `scripts/recon.py`（三閘 180／25／2，182 為對照輸出）、
   更新 `BASELINE.sha256`（**須加入 037**）、以
   `data/expected_cited_sections.tsv` 做 135 條**集合對集合**命中驗證，
   並補 01 輪列為未實測之五項（header row 7、FROP 欄 182 列值、
   PROF-017／035 之 Out of scope 身分、Sub Categorization 與 Priority 分布）。
3. Layer 2 定版後方可附 `docs/fw036/framework.md` Part（仍未附）。
4. ~~**建議立一道 gate 保住 R-G3**~~ —— **40 輪已立並實跑**：
   `scripts/verify_dv_integrity.py`（四項比對、6/6 方向性案例，
   注入向確實轉紅）。**A-UP09 之 R-U14 解除條件已成就，待落槌。**

---

## 3. 資料產物

| 檔 | 列數 | 說明 |
|---|---|---|
| `data/spec_id_to_outline.tsv` | 169 | section id → outline／polarion id／實體列號／字元數（tracked）|
| `data/outline_map.json` | 169 | 含 Description 全文 |
| `data/expected_cited_sections.tsv` | 135 | 候選被引 section（037 到齊後之比對基準）|
| `data/spec_popup_ids.tsv` | 20 | PU id → 引用次數／section |

腳本：`scripts/build_outline_map.py`
