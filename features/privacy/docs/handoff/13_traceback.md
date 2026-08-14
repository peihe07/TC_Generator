# 下放包 13 — 回溯產物之裁定、語意覆核之機制化、P6 前置收尾

分析層 → 執行層。2026-08-13。承接上繳包 12。

**權限標示**：§1 全部為分析層自裁。其中 R35-3（`the HU has determined`
之處置）採保守方向並附 RD-1 提問，**可逆** —— Pei 若不同意，一句話即改。

---

## 1. 裁決條文

```text
[RULING] R35 — 回溯產物與覆核機制化（分析層自裁，2026-08-13）

R35-1  placeholder 旗標 —— 追認，且界線正確
  事實：BLOCKED 列會使既有四個 gate 同時誤報（design_method 空、
      priority 空、步驟 < 2、步驟/ER 不對等）。執行層未放寬既有 gate，
      改以 `placeholder: true` 導向一組專屬 gate
      （placeholder-body / placeholder-blank / placeholder-remarks）。
  裁：追認。**為一列而鈍化其餘十列之檢查，是以標準遷就實作**；
      改變實作而保留標準，方向正確。旗標名沿用既有 placeholder 慣例
      亦正確（不創新詞彙）。
  §5a：**當新增之合法列型使既有 gate 誤報時，正確處置是為該列型另立
      gate，不是放寬既有 gate。** 判準：修改後，原本會被抓到的違規
      是否仍會被抓到。

R35-2  [Off] 跨條文借用 —— 非違規，但產生引用義務
  事實：-006／-007 之 PC 2 使用 `[Off]`，其值域定義於 4915170
      （-005 之條文），不在 -006／-007 自身條文內。
  裁：**不構成 §8.4.2 之範圍杜撰** —— §8.4.2 之標的是「外部 spec」，
      而 4915170 與 4915171／4915172 同屬 CFTS022，同一 spec 內之
      跨條文引用為正常。
      但依 **§10.7「List every spec section the TC directly verifies
      or relies on as setup」**，產生引用義務：
      **-006／-007 之 `specification_reference` 加列 `CFTS022-4915170`**，
      排序由最具體到一般（本葉條文在前，被借用之值域定義在後）。
      `reasoning` 須註明該筆為 setup 依賴而非驗證標的。
  §5a：**同一 spec 內之跨條文借用不是範圍問題，是引用完整性問題**；
      兩者處置不同 —— 前者加引用，後者刪內容。

R35-3  `the HU has determined that…` —— 以客觀組態為觸發（保守方向）
  事實：4915174／4915175 之觸發含「HU 已判定 amplifier 不存在／存在」
      這個中間狀態；執行層之 PC 只設定客觀組態（PROXI 側）。
  裁：**PC 維持只設定客觀組態，不得斷言 HU 之內部判定狀態。**
      理由（方向性，非等同性）：
      「HU 已判定」是 HU 自客觀組態導出之內部狀態，測試者無法直接
      設定，亦無規格指定之可觀察指標。以客觀組態為觸發時，
      **判定環節被納入受測範圍** —— 若 HU 未能正確判定，TC 即 fail，
      而那正是應被偵測的失效。故此處置是**保守方向**（多測而非少測），
      符合不對稱錯誤代價原則。
      **禁止**：PC 不得寫「The HU has determined that the amplifier is
      not present」一類措辭 —— 那是對不可觀察內部狀態之斷言。
  `reasoning` 須載明：條文之觸發含 HU 之判定環節，本 TC 以客觀組態
      為起點，判定環節一併納入受測範圍。
  RD-1 新增 **#13**：請上游確認 HU 對 amplifier presence 之判定是否
      有規格指定之可觀察指標；若有，該指標應成為獨立之中間驗證點。
  **本裁決可逆** —— 若 Pei 或上游裁定判定環節應獨立驗證，
      -009／-010 須增加中間步驟，現行 TC 不需重寫，只需擴充。

R35-4  -006 ER 收斂 —— 追認，並記其切法
  事實：收斂前為「The HU has adjusted the output volume according to
      the speed controlled level」，同時斷言「有調整」與「依該 level
      調整」；收斂後只留「The output volume has changed」。
  裁：追認。切點正確 —— **前半是本條之標的（歸屬），後半是 CFTS019
      之標的（行為曲線）**，一句 ER 同時承載兩個 spec 之主張是本次
      最典型之越界形態。
      -007 未改動亦正確（其 ER 本即止於「level 未被 HU 改變」）。

R35-5  負向對照之鑑別力 —— baseline 型可接受，但須補邊界例
  事實：16 個 gate 缺對照 0；其中三個（test-group / step-er-parity /
      step-count）以 baseline 自身為負向對照，程式內標
      `PASS (baseline)` 而非隱去。
  裁：**標示法追認** —— 明標 baseline 型使讀者知悉其性質，優於隱去。
      但補一條原則：
      **負向對照之鑑別力，隨其與違規之距離遞減。** 乾淨之 baseline
      距違規最遠，只能證明 gate 不對「明顯合規」誤報，不能證明它不對
      **邊界合規**誤報。
      作業：該三項於 P6 前各補一個**邊界例**負向對照 ——
        step-count → 恰為 2 步之 TC（下界，須 PASS）
        step-er-parity → 單一步驟對應多行 ER 之合法形態（須 PASS）
        test-group → 與正確值僅差大小寫或尾隨空白之近似值（須 FAIL，
                     屬陽性對照之補強；另備一合法但不同 Test Set 之
                     值須 PASS）
      **非阻塞**，但 P6 前完成。

R35-6  -008 之語意對應正常 —— 此區分必須保留
  裁：追認執行層之註記。-008 之 artifact 與 leaf **語意完全對應**
      （037 標題 `Restore on AMP Wake-Up` 對條文 `the AMP shall
      recall`）；其問題是 **ECU 歸屬**，不是**對映錯誤**。
      兩者必須分開記載，否則日後會被讀成「-008 之
      specification_reference 也有問題」。
  §5a：**同一列上可能同時存在「正確的引用」與「錯誤的歸屬」**；
      覆核結論須逐面向分別陳述，不得以單一「有問題／無問題」概括。

R35-7  語意對應覆核之機制化 —— 一次性人工作業改為 ratchet
  事實：執行層指出 §6 之語意對應表為一次性人工作業，**無任何機制會在
      下次生成時重跑**；若 P6 之後某葉之 `specification_reference` 被
      改動，沒有東西會要求重做。
  裁：**建立 `features/privacy/data/spec_ref_reviewed.json`（進版控）**，
      逐葉記錄：leaf id / artifact id / 覆核日期 / 覆核依據
      （條文要旨 vs 葉子驗證目標之對應說明摘要）。
      lint 新增 gate：**各葉之 `specification_reference` 須與該檔記載
      相符；不符即 FAIL**，訊息指明「該葉之 spec_reference 已變動，
      語意對應覆核須重做」。
      該檔為**只增不改**：覆核重做時新增一筆並保留舊筆（同 DELIVERY
      台帳之 append-only 語意）。
      同 R20-2 之 ratchet 形態 —— 人工判斷之結果被固定下來，
      機制負責偵測它何時失效，而非重做判斷。
  §5a：**一次性人工覆核之結論，必須被固定為可比對之紀錄**；
      否則該覆核只在做完的當下有效。

R35-8  profile §3.2 之 PC 詞彙表未回溯 —— P6 前必辦
  事實：本輪回溯之標的為 **TC 之 PC**，非 **profile §3.2 之詞彙表**；
      而 `An external amplifier is present on the vehicle` 正出自
      分析層於下放包 04 起草、當時即自陳未回溯之該表。
  裁：執行層之區分正確（兩者是不同的東西，前者已辦後者未辦）。
      profile §3.2 詞彙表為 B3+ 與日後 regen 之來源，**P6 前必辦**：
      逐條回溯 CFTS022 原文，措辭不符者以原文為準修訂，
      無原文對應者標明其為測試設定用語而非 spec 措辭。
```

---

## 2. 執行層作業

1. 貼入 §1（R35）至 `RULINGS.md`
2. **-006／-007 `specification_reference` 加列 `CFTS022-4915170`**
   （R35-2），`reasoning` 註明為 setup 依賴
3. **-009／-010 `reasoning`** 依 R35-3 加入判定環節之說明；
   **PC 不動**（現行只設客觀組態，已符合裁定）
4. RD-1 新增 **#13**（R35-3）
5. **建立 `data/spec_ref_reviewed.json`**（R35-7），以本輪 §6 之十葉
   覆核結果為首筆；新增對應 lint gate，含陽性＋負向對照
6. **profile §3.2 詞彙表逐條回溯**（R35-8），差異逐條回報
7. **三項 baseline 型 gate 各補邊界例負向對照**（R35-5）
8. lint 全批回跑，findings 應為 0；非 0 停手回報

**不做**：不改 -009／-010 之 PC、不動 -008 之 spec_reference、
不放寬任何既有 gate、不執行任何 git 操作。

---

## 3. 停手條件

1. 第 2 項加列後，該兩葉之 `specification_reference` 未通過既有格式
   gate → 停止該項，續行其餘，回報 gate 訊息
2. 第 5 項之新 gate 在現況下即 FAIL → 停止該 gate 入庫，續行其餘，
   回報差異（不得為使其通過而改動任一葉之 spec_reference）
3. 第 6 項回溯發現 profile §3.2 有**三條以上**詞彙無 CFTS022 原文對應
   → 停止修訂，續行回報全表盤點結果。理由：多數詞彙為自創時，
   該表之性質須重新裁定，非逐條修補可解
4. 台帳任一條指令 FAILED → 停止全部，回報

---

## 4. 上繳包要求

寫入 `features/privacy/docs/upstream/13_traceback.md`：

1. §2 八項完成狀態
2. `spec_ref_reviewed.json` 全文與新 gate 之雙對照輸出
3. profile §3.2 回溯之逐條結果（原文相符／已修訂／測試設定用語）
4. 三項 baseline gate 之邊界例對照輸出
5. lint 全批回跑結果
6. 台帳兩條指令輸出
7. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 5. 下一階段預告（本包不執行）

P6／P7 之下放包將涵蓋：

- 依 **R20-5** 建立 Privacy 之寫回路徑，**自始建於
  `backend/xlsx_surgical.py`**，不得複製任一既有 feature 之
  write_back 腳本（四支皆已封存，R20-3）
- 受 **R18-3** 之 ABORT 級 invariant 拘束（zip 成員集合、DV 計數）
- **BLOCKED 列之寫回驗證**（placeholder 旗標、空白欄位、
  Remarks marker 皆尚未走過 write_back —— 執行層已正確指出）
- 欄 S 與車型欄之兩個 gate 由 NOT MEASURED 重標為可實測（R34-6）
- 寫回後更新 `DELIVERY.sha256`（新增 ENTRY，不覆蓋）

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R35-1 新列型使既有 gate 誤報時另立 gate（§5a）—— §1
- [x] R35-2 同 spec 內跨條文借用為引用完整性問題（§5a）—— §1
- [x] R35-3 客觀組態為觸發，判定環節納入受測範圍（可逆）—— §1
- [x] R35-4 -006 ER 收斂追認 + 一句 ER 不得承載兩 spec 之主張 —— §1
- [x] R35-5 負向對照之鑑別力隨距離遞減 + 三項邊界例 —— §1
- [x] R35-6 引用正確與歸屬錯誤須分面向陳述（§5a）—— §1
- [x] R35-7 語意覆核 ratchet 化 + spec_ref_reviewed.json —— §1
- [x] R35-8 profile §3.2 詞彙表 P6 前必辦 —— §1
- [x] 停手條件四項（已依 R17-1 明列標的與續行標的）—— §3

<!-- HANDOFF-LINK: 13 -> upstream:13 -->
