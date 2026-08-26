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
