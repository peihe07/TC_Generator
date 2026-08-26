# RULINGS — Audio Management (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Audio Management 之裁決權威；
跨 feature 條文承接時註明來源包。

來源包：`docs/handoff/01_intake_recon.md` §三（Q1–Q6，Pei 2026-08-26 裁）、
`docs/handoff/03_batch_B1_handoff.md`、`framework.md`。

---

## R-AM1（Q6）：Phase 0 人工分類

> sniffer 輸出作廢，§一分類表為正式 Phase 0 產出。slug = `audio_mgmt` 併准。

（R-AM4 = slug 併准，併入本條；01 包 §首行「Feature slug：`audio_mgmt`（R-AM4 併准）」。）

執行層回報：`scripts/intake.py` 未執行、亦不執行；01 包 §一之九件分類表
為本 feature Phase 0 之唯一正式產出。

## R-AM2（Q2）：錨源 = 兩本 CFTS Basic Report

> specification_reference 之錨定物件池 = 檔 3、檔 4 兩本 Basic Report 之
> Source Requirement ID 欄（Polarion 7 位 ObjectID），格式依 IN §10.7(a)
> `CFTS019-{ObjectID}`。因正式橋接欄全空（F1），對位方法為：
> SWE.1 需求內容（Title + Description）↔ Basic Report Description 內容對位，
> **能唯一對位者**取該列 ObjectID 為錨；**對位不到或一對多者**填
> `PENDING: DR-AM1 SWE1-to-CFTS ObjectID mapping unresolved for this leaf`
> 並逐條登記，不硬配、不取語意相近他列代入（IN §8.4.1 / R-13 同理）。
> 內容對位屬 Pei 本裁定明文授權之例外，僅限本 feature、僅限此橋；
> DR-AM1 之上游正式對照表到位後，全簿回填校正。

### R-AM2′（修訂，2026-08-26，Pei 裁：「2採 R-AM2′准 DR-AM3發」）

> 錨源池 = (a) 兩本 CFTS Basic Report（主池，優先）；
> (b) 全文 PDF 中 State:Approved 之需求物件（**僅限該物件不在 (a) 時啟用**）。
> 凡取自 (b) 者：reasoning 逐條註明「池外錨，全文佐證」，並列入該批上繳包
> 之池外錨登記表；DR-AM3 重匯回件後逐條覆驗併回主池。
> 本修訂不改變「looked up, never constructed」判準（R-AM8 不動）。

適用緣由（A-AM03）：執行層實測兩本 Basic Report 系統性遺漏圖表型需求
物件（圖表型在池率 1/13＝7.7%、非圖表型 670/1717＝39.0%），B1 七葉
（138、156、157、200、205、240、241）因而不在主池。EE Architecture
過濾假設已由實測推翻。七錨經雙路獨立核驗（分析層語意對位、
執行層全文逐一佐證 State:Approved）。

內容提醒（不設新關卡）：七葉屬「Refer to figure」型需求，TC 行為序列
以圖說附文及 SWE.1 Description 為據；時序值仍循 IN §8.4.1 不造值。

執行層回報：`feature.yaml` 之 `spec_reference_template` 設為
`CFTS019-{object_id}`；兩本錨源分別掛 `paths.sys1_export`（Part 1）與
`paths.sys1_export_part2`（Part 2），因 `feature_config.resolve_path`
要求每鍵恰好 glob 到 1 檔，不得以單鍵表達。

## R-AM3（Q1）：工作簿基底 = BLANK + R-G1 模板

> 新 TC 簿自 R-G1 模板空白起建。既存 `SWQT_AudioAACP` 簿之 50 條舊 TC
> 原封不動、不續寫、不回修，僅作參考。理由：舊 TC 錨定 SWE1-PROJ-203
> （Projection 需求命名空間），與本案 SWE1_AMM 命名空間無交集，混簿將
> 污染追溯；且舊內容為中文 AC 式 test_item，非 canon 格式，續寫將迫使
> 單簿雙制。

執行層回報：`done_region.detection` 設 `none`（BLANK 下無 done region，
留 author_value 會使 content_hash 在 0 列上恆真）；`fill_test_group_set`
設 `true`（canon §2 之 BLANK 綁定）。

## R-AM5（Q3）：驗證範圍 = SWE.1 之 318 葉

> 範圍 = SWE.1 報告全部 318 列（317 唯一 SWE ID，含 F2 碰撞之兩列均入範圍）。
> PF / EQ / DSPPP 之 177 條需求範圍外，不擅自擴編，以 §六 揭露表列為
> coverage gap，交付時隨簿揭露。

## R-AM6（Q4）：SWE1_AMM_076 碰撞之交付欄處置

> 兩條 076 各自出 TC。交付簿 `Requirement or Design ID` 欄**均照抄
> `SWE1_AMM_076`**（上游僅存在此字串；自造 `076a/b` 寫入交付欄 = 造 ID，
> 追溯反斷）。兩組 TC 之區分由各自 test_item 內容與 specification_reference
> （錨至不同 CFTS 物件）承載。「076a（=SYS-RA-AMM-242）／076b（=SYS-RA-AMM-246）」
> 代號僅限分析層文件內部追蹤使用，禁入交付欄。DR-AM2 上呈請上游改號，
> 改號後交付欄隨改。（Pei 於 Q4 提問後說明，無異議即照此辦。）

## R-AM7（Q5）：req_id 欄格式

> `Requirement or Design ID` 欄照抄 SWE.1 原文底線式 `SWE1_AMM_{NNN}`，
> 不改寫為連字號、不增删前綴。

---

## Framework 鎖定（Pei 2026-08-26 裁：「1採 2採 B1准」）

`framework.md` 狀態 LOCKED。Layer 1 = `Audio Management`；Layer 2 共 11 集，
合計 318 列（317 唯一 SWE ID）。新 RD 進場：先歸位該表；無適集者先修
`framework.md` 再寫 TC（IN §4.1）。

同一裁定併准 Batch B1 之下放（03 包）：Source Transition 全 34 葉 ＋
Audio Arbitration 前 16 葉，共 50 葉。

---

## 執行層自裁（待 Pei 過目；FEATURE_ONBOARDING §4 —— 簽核時未動即成定案）

以下三項為 scaffold 落檔時 `feature.yaml` 必填、而 01/03 包未明文裁定者，
依 canon 與 repo 既有慣例提案，標 `[PROPOSED]`：

1. **spec_mode = D**。錨定「looked up, never constructed」（FO §3 之 D 定義），
   錨值逐葉取自 03 包 §四表且執行層不得自行改錨。來源形態雖為 Polarion
   xlsx export（近 A），但無 outline 可構造、無橋接欄可走（F1），
   行為與 time_management（CFTS015）／sxm（CFTS024）之 D 同型。
2. **tc_id_format = `NR1L-AMM-{n:03d}`**。03 包 §二 只給
   `{project}-AMM-{NNN}`（IN §10.3）並註明「project token 循 repo 既有慣例」。
   既有慣例之 project token 為 `NR1L`（舊 AudioAACP 簿之 `NR1L_AudioMgnt_*`、
   time_management 之 `NR1L-TimeManagement-*`）。分隔符取連字號以從
   time_management／canon，不從舊簿之底線式。
3. ~~**workbook 版面 = rev C**（原標 [PENDING]）~~ **已結案，非提案。**
   2026-08-26 母本複入 `inputs/`（sha256 `6372fb6b…6fb825b2`，與 `forms/` 母本
   及 time_management 所記逐字相同）後直讀第 9 列表頭實測，16 個宣告欄位
   全數對上，`feature.yaml` 已改註「實測」。無須等 recon，亦非鏡射 TM。
   scaffold 預設之 rev A/B 值在三處為誤，已更正：`design_method` 應為 R
   （Q 實為 Estimated Test Time (mins)）、`author` 應為 AA（Z 實為
   Fastack (376) Atl-Mi）、且預設無 `tc_id` 鍵（實為 F）。
   另註兩組易混欄位：C 為 `Requirement or Design ID (Polarion)`、D 才是
   R-AM7 所指之 `Requirement or Design ID`；E 為 `Test Case ID (TestRail)`、
   F 才是 `Test Case ID`。

---

## Pei 裁定（2026-08-26，原文：「1准 2准 3照辦 4代行准」）

1. **R-AM8（定案）**：`spec_mode = D`。上述提案第 1 項全文照採，
   [PROPOSED] 撤銘。
2. **R-AM9（定案）**：`tc_id_format = NR1L-AMM-{n:03d}`。上述提案第 2 項
   全文照採，[PROPOSED] 撤銘。舊 AudioAACP 簿之底線式不遵循（R-AM3：
   新簿與舊簿無延續義務）。
3. **第 3 項（欄位字母）**：Pei 裁「照辦」＝不猜待實測之行為準則成立；
   實測已於同日完成並結案（見上段），實測值為準。scaffold 預設 rev A/B
   之三處誤值更正納入本裁定效力。
4. **R-AM10（定案）**：R-G1 母本複本自 `forms/` 複入 `inputs/` 之一次性
   代行授權成立（純 repo 內檔案搬移，非客戶來源置檔亦非 git 操作，
   不在「檔案放置屬 Pei」範圍）。sha256 與 `forms/` 母本逐字相同已驗。
   本授權僅及此一次搬移，不擴張為通案。

備註：包 03 §一 已補遺第 5 項（R-G1 母本複本）並改「五件在位」；
四件客戶來源之置檔仍屬 Pei，不在 R-AM10 授權內。

---

## 分析層自訂正（2026-08-26，因 recon 回報 A-AM01 / A-AM02）

**R-AM11：來源指涉以 `inputs/` 實名為準。**
包 01／03 所載四件來源檔名取自 Claude Project 掛載副本，介面對空白、
點號做了正規化而失真，照抄之路徑四鍵全數 glob 到 0 檔。執行層改取
檔案系統實名正確。今後包內來源指涉一律以 `inputs/` 實名為準，
掛載名僅作內容識別。

**R-AM12：包 01 §一 檔 2 之形態判定更正。**
包 01 記「實為純文字、234 個 ObjectID、上界 4867749」。實測對象主體不同：
分析層讀的是掛載副本（介面抽取後的產物，確為純文字），234 是大括號
包裹之章節級標題 ID；執行層讀的是 `inputs/` 原件，為**真 PDF、
文字層完好、1,964 個 ObjectID、上界 4867784**。
**作為對來源工件之判定，包 01 寫錯**（量失真副本卻寫成原件屬性），
以執行層實測為準：B3 之篩選以全 ID 集、上界 4867784。
不影響 R-AM8（D 之判準為錨值 looked up 而非 constructed）。
本件與 R-AM11 同根：掛載副本不可代表原件。

---

## Pei 裁定（2026-08-26，原文「准」）

**R-AM14：1.3.3.11 Carplay Alternate Audio 在 audio_mgmt 範圍內。**

> SWE1_AMM_286（→4866817）、SWE1_AMM_287（→4866818）留在 audio_mgmt，
> Test Set = Focus and Ducking，Layer 3 增列 1.3.3.11。
> 依據：SWE.1 上游已為這兩條行為產出 SWE1_AMM 命名空間之葉；
> IN §8.1／§8.2.1：上游分解為「什麼算一個需求單元」之權威，
> TC 作者不得改判。章節標題掛 CarPlay 僅說明觸發來源型別，
> 需求本體為混音與衰減之音訊行為，非投影 UI。
> 連帶撤銷：包 02 §一 第 2 項中「1.3.3.11 零葉、歸 Projection」之判定。
> 仍屬 coverage gap：4866819（細節指向 Apple AIS）、
> 1.3.3.14 Android Auto Certification。

誤判根因留痕（分析層之誤，非上游問題）：包 02 之判定係以
`carplay` / `android auto` / `projection` 三詞全表掃描得 0 葉，
而需求原文寫 `Alternate Audio`，不提 CarPlay。關鍵詞過窄。

**R-AM15：錨定改採雙路必經（自 B2 起）。**

> 每葉之錨須經兩路獨立產出並一致，方得寫入交付欄：
> (1) 分析層定向查證（候選＋原文佐證）；(2) 執行層全文獨立比對。
> 兩路一致 → 寫入。不一致 → 列出對帳，未決者掛
> `PENDING: DR-AM1 <leaf>`，不硬配、不取單路結果逕用。
> 單路演算法輸出（DP 或逐葉最佳匹配）一律不得作為定案依據。

立法證據（二路獨立得出同一結論）：
- 執行層以 B1 已裁定之 43 個池內錨回測其候選演算法：top-1 49%、
  top-3 67%、top-10 84%、正解排名中位數 2；並主動撤除 strong／weak
  信心標籤（該標籤傳達的把握它沒掙得）。
- 分析層以同一 DP 方法跑 B2，逐條讀後實測 50 條中至少 13 條語意
  明顯錯配（如 310 被配至 4867764「<Tdelay>=250ms 開機畫面」、
  312–317 導航衰減六條全被配至尾段時序變數定義）。
  根因：SWE.1 以 SYS-RA 號升冪排列，尾段葉（SYS-RA 895–1111）對應之
  CFTS 章節位於文件前段，單調假設崩潰。B1 落在文件中段未暴露。
- **B1 之正確，原因不是演算法可靠，而是執行層事後以全文逐條
  佐證了 50 條。本條將該事後複驗提為前置必要條件。**

代價揭露：B2 進度將慢於 B1。但 B1 之速度建立於一個未經檢驗之
假設（DP 可靠），該假設已遭推翻。

---

## Pei 裁定（2026-08-26，原文「1准 2准 3准 4照裁 5送 DR-AM7開」）

對應上繳包 07（B2 第二路對帳）之四項待裁。完整錨表見
`docs/handoff/08_B2_final_anchors.md`。

**R-AM16：共錨允許。**

> 兩個不同 SWE ID 指向同一 CFTS 物件，係上游將一條 CFTS 需求分解為
> 兩個 SWE 葉之結果，屬正常形態，非造 ID，R-AM6 不適用。
> 實例：SWE1_AMM_031／032 共錨 CFTS019-4866055（來源 ID 178／179 連號）。
> **硬性條件**：共錨之兩條 TC，test_item 括號下半必須寫出各自側重，
> 不得逐字相同（IN §4.3.1 R-S4 sibling 區分 token）。

**第 1–4 項之逐案裁定**（全文見 08 包 §二，本處紀要）：
1. SWE1_AMM_309 → CFTS019-4866484（C→A，池外）。第二路證據充分，
   無推論一跳，R-13 疑慮不存在。取 4866484 不取 4866485：變體清單
   含 `R1L-R`，且本文僅言 HFP（與葉相符）。
2. SWE1_AMM_030 → CFTS019-4866054，標**部分覆蓋**。duck／mute／reject／
   pause 動作集無 CFTS019 正文對應，併入 DR-AM1；TC 範圍限縮至錨文
   字面，不寫動作集（IN §8.2.1 存疑從窄）。
3. SWE1_AMM_031／032 共錨 4866055（見 R-AM16）；032 之 spec_reference
   併列 4866054 ⮏ 4866055（首句「INFO2 優先於 ENT 與 INFO1」屬 4866054 範圍）。
4. 五條但書照裁：086 改錨 4866442（判準為涵蓋面，非相似度）；076 維持
   4866155 標部分覆蓋；061 維持 4866123 掛 `PENDING: DR-AM6`，
   **嚴禁推測 CFTS020 內容**；233 維持 4866916 標部分覆蓋；
   032 併列雙錨。
5. DR-AM6 送出。

**A-AM07 ／ DR-AM7（分析層提出，Pei 裁發）**

> B2 之 47 個錨中 24 個標記 `EE Architecture: Atlantis Mid` 而不含
> `Atlantis High`，本案為 R1LR Atlantis-H。集中於 TA/VR 仲裁段
> （4866926–4866933）、TLM 靜音段（4866129–4866134）、VSIM 段
> （4866689–4866695）。請上游確認該標記之需求是否適用於 Atlantis-H；
> 若不適用，SWE.1 對應葉需重新界定範圍。
> **不阻塞 B2**：依 IN §8.2.1 上游分解為權威，TC 作者不得改判範圍；
> 照現行錨表出貨，回件後統一處置。

與先前假設之關係（不衝突）：執行層曾測試「EE Architecture 過濾」作為
**池籍**（匯出缺漏）之解釋並推翻之（純 Mid 之 491 個中有 229 個在池內）；
本件問的是**適用性**，非匯出，兩者為不同命題。
