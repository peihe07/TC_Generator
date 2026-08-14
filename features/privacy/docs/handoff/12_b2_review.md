# 下放包 12 — B2 覆核、-008 BLOCKED 列、P6 前置

分析層 → 執行層。2026-08-13。Pei 回覆「照你建議」，R34 全數簽署。

---

## 1. 裁決條文

```text
[RULING] R34 — B2 覆核與 ECU 歸屬判準（Pei 簽署 2026-08-13）

R34-1  ECU tag 與行為主詞不一致時之判準（本包主要產物）
  裁：ECU tag 表示「哪些 ECU 的規格文件會收錄此條」（分發範圍）；
      行為主詞表示「誰執行此行為」。**驗證歸屬由後者決定。**
      兩層判準，須同時成立：
        (1) 必要條件 —— ECU tag 含本 ECU
        (2) 充分條件 —— 行為之 trigger 或 outcome 主詞含本 ECU，
            或本 ECU 在該訊號鏈上有可觀察之一端
      (1) 成立而 (2) 不成立 → 排除，並於 reasoning 指名歸屬。
      **tag 含本 ECU 只是「這條與我們相關」，不是「這個行為由我們驗」。**
  先例對照（同一判準、不同結果，兩者皆須保留於 profile）：
      -005 留下 —— HU 為 $VolumeSCV$ 之發送端，訊號鏈上有可觀察之一端
      -008 排除 —— trigger 與 outcome 皆為 AMP，HU 側無任何可觀察行為

R34-2  -008 排除確認
  裁：`SWE1-HMI-PRIVACY_FEATURES-008`（CFTS022-4915173）
      **排除於本交付件之驗證範圍**，歸 AMP ECU。
  證據四項同向（分析層獨立複驗 ECU tag，執行層判定成立）：
      (a) trigger 主詞 = AMP
      (b) outcome 主詞 = AMP
      (c) 條文全文不提 HU
      (d) **ECU tag 含 `AMP` —— 十片葉子中唯一**
          4915171 `RRM, LTM, ETM` / 4915172 `ETM, LTM, RRM` /
          4915173 `ETM, AMP, RRM, LTM` / 4915174 `RRM, LTM, ETM` /
          4915175 `LTM, ETM, RRM`
      執行層照實回報之反向指標（tag 仍含 LTM）依 R34-1 不足以推翻。

R34-3  -008 於交付件之表示 —— 產出 BLOCKED 列
  裁：交付件**為 -008 產出一列**，非略去。
      - tc_id 照序配發（不跳號）
      - Test Group `Privacy`、Test Set `Speed-Controlled Volume`
      - specification_reference = `CFTS022-4915173`
      - 各驗證欄位依 BLOCKED 形式填寫
      - Remarks 帶 marker，內容：
        `[BLOCKED-ECU] Out of scope for this deliverable: both the
         trigger and the outcome of CFTS022-4915173 are performed by
         the AMP; the HU has no observable behaviour in this clause.
         Verification belongs to the AMP ECU. Pending upstream
         confirmation of the leaf allocation (A-PV18 / RD-1 #12).`
  理由：交付件若直接少一片葉子，追溯表會出現**沒有說明的缺口**；
      BLOCKED 列使缺口可見、可審。
  連動：本項為本 feature **第一個 marker**。profile §5 之
      「本 feature 目前無 marker」須改寫為 marker 表，登記
      `[BLOCKED-ECU]` 之定義、適用條件與唯一用例。
      lint 須加一項 gate：Remarks 非空時，其開頭 token 必須為
      profile §5 marker 表內已登記者。
  新登 A-PV18：037 將 outcome 主詞為 AMP 之條文分配予 HMI/HU 之
      SWE.1；狀態 PENDING，待上游確認。
  RD-1 新增 #12：請上游確認 -008 之葉子分配；若確為 HU 側需求，
      請指出 HU 在該行為中之角色與可觀察面。

R34-4  -006／-007 之速度激勵 —— ER 不得斷言音量與車速之關係
  事實：CFTS022-4915171 全文為「If the amp is not present, the HU shall
      adjust the output volume **according to the speed controlled
      level**」，其自帶 Note 明將 speed controlled audio behavior
      交予 CFTS019。
  裁：本條擁有之標的為**歸屬**（amp 不在時由 HU 執行調整），
      非**行為曲線**。故：
      (a) 速度激勵得用於觸發，但 ER 不得斷言任何「音量 vs 車速」之
          具體關係、比例、階數或門檻（屬 CFTS019，§8.4.2）
      (b) -006 之 ER 止於「輸出音量隨之改變」
      (c) -007 之 ER 止於「level 未被 HU 改變」
      (d) 兩者可驗證之差異是**誰在調整**，不是調得對不對
  執行層之疑慮（速度激勵未經規格確認）成立，本裁決即其處置。

R34-5  lint gate 之 Interior CAN 誤判修正 —— 追認
  裁：修 gate 不修標準，界線正確（停手條件 1 之界線）。
      修法（modal 命中若字面全大寫則判為縮寫／訊號名）不改 gate 意圖，
      shall 仍照抓且經陽性對照確認 —— 追認。
  §5a 新增：**對正確輸入誤報的 gate，跟永不觸發的 gate 一樣壞。**
      故每一 gate 須同時具備：
        陽性對照 —— 證明它會抓（違規輸入必 FAIL）
        負向對照 —— 證明它不亂抓（合規之相似輸入必 PASS）
      **缺任一者，該 gate 標「未實測」而非 PASS。**
      本例之負向對照即「Interior CAN 必須不觸發 er-modal」。

R34-6  欄 S 與車型欄標 NOT MEASURED —— 追認
  裁：生成階段不產出該兩區，此處無從失敗，標 NOT MEASURED 正確
      （R18-4 原則）。該兩 gate 於 P6 寫回後方為可實測，屆時須重標。

R34-7  VF651 不進 specification_reference —— 追認
  裁：三項理由皆成立 —— 需求來源為 CFTS022；VF651 於本批為背景理解
      且未給可用值；profile §3.5 明文「No cite-form mechanism」，
      SXM 之 cite-form 明列為不繼承。
      以 spec 自身 token {VF651} 出現於 reasoning 即可。
      **推及全批**（B1 + B2 十葉一致）。

R34-8  -009 與 -003 非 duplicate —— 追認，不標 duplicate_of
  裁：觸發不同（使用者改變 level vs Interior CAN 喚醒），§8.3 之切分
      判準為觸發。-009 借喚醒作為「已存入」之觀察手段，屬**觀察手段
      重用**，非驗證目標重複。
      reasoning 須註明此區分，避免 review 時被誤讀為漏標。
  §5a：**觀察手段之重疊不構成 duplicate**；duplicate 之判準是
      trigger + outcome + input + verification target 四者皆同。

R34-9  PROXI 參數值不可得 —— 追認
  裁：VF651_V6_R2 明文「The characteristics of the PROXI Parameters and
      their related values are defined in the PROXI requirements
      specific for the vehicle project」，該文件不在 inputs/。
      依 §8.4.1 不填任何參數值，Pre-Condition 以條文自身措辭表述
      —— 追認。DATA_REQUESTS #11 已立。

R34-10  兩項延宕事項 —— 停止再延，列為 P6 硬性前置
  (a) **Pre-Condition 措辭回溯 CFTS022 原文** —— 已連續三次列為未辦
      （下放包 10 N5 / 上繳包 04 §6.3 / 09 §6.4），且範圍已自六葉擴為
      十葉。**P6 寫回前必辦，不得再列入「未辦」。**
  (b) **全 10 葉之 spec-reference 語意對應人工覆核** —— lint 只驗
      「id 查得於 CFTS022」，不驗該條文是否真的對應該葉；
      B1-GATE-1 抓到之 -002 指向 splash screen 一類的錯，lint 抓不到。
      **P6 寫回前必辦，不得以 lint 綠燈代替。**
  §5a：**同一未辦項連續三次出現於「該驗未驗」清單者，即刻升為
      下一階段之硬性前置**，不得再以「列入清單」處置 ——
      清單之功能是記住，不是延期。
```

---

## 2. 執行層作業（依序）

1. 貼入 §1（R34）至 `RULINGS.md`
2. **-008 之 BLOCKED 列**：依 R34-3 產出，Remarks 逐字照抄
3. **profile §5 改寫**為 marker 表：登記 `[BLOCKED-ECU]` 之定義、
   適用條件（R34-1 之兩層判準）、唯一用例（-008）
4. **profile 新增 R34-1 之判準條文**，含 -005／-008 之對照先例
5. **-006／-007 之 ER 依 R34-4 收斂** —— 移除任何音量與車速關係之斷言
6. **-009 之 reasoning** 依 R34-8 加註觀察手段重用之區分
7. **lint 新增兩項 gate**：
   - Remarks 非空時，開頭 token 須為 profile §5 marker 表內已登記者
   - 依 R34-5，逐一檢視現有 12 個 gate 是否具備負向對照；
     **缺負向對照者一律改標「未實測」**，不得維持 PASS
8. 登 A-PV18；RD-1 新增 #12
9. **P6 前置兩項（R34-10）** —— 本輪即辦，不列入未辦清單：
   - 全 10 葉之 Pre-Condition 逐句回溯 CFTS022 原文，差異逐條回報
   - 全 10 葉之 spec-reference 語意對應人工覆核，逐葉列出
     「條文要旨 vs 葉子驗證目標」之對應說明

**不做**：不寫回 workbook（P6 另包）、不動 -001 之 P0、
不改 -005 之 priority、不執行任何 git 操作。

---

## 3. 停手條件

1. 第 7 項檢視發現**三個以上** gate 缺負向對照 → 停止 lint 之
   「全批 PASS」宣稱，續行改標與其餘各項，回報缺對照之 gate 清單。
   理由：多數 gate 未經負向驗證時，全批 PASS 之陳述不具意義
2. 第 9 項之 Pre-Condition 回溯發現任一葉之措辭與 CFTS022 原文
   **語意不符**（非僅措辭差異）→ 停止該葉之後續，續行其餘葉，回報
3. 第 9 項之語意對應覆核發現任一葉之 specification_reference 指向
   **不對應之條文** → **停止全部後續**，續行回報。
   理由：此即 B1-GATE-1 型錯誤，會使 framework Part VI 之對映表
   連同 profile §1 須一併修訂
4. 台帳任一條指令 FAILED → 停止全部，回報

---

## 4. 上繳包要求

寫入 `features/privacy/docs/upstream/12_b2_review.md`：

1. -008 BLOCKED 列之全文
2. profile §5 marker 表與 R34-1 判準條文之落點
3. -006／-007 ER 收斂前後之 diff
4. lint 兩項新 gate 之陽性＋負向對照輸出；現有 12 gate 之
   負向對照盤點結果（逐 gate：有／無／已改標）
5. R34-10(a) 全 10 葉 Pre-Condition 回溯結果（逐葉）
6. R34-10(b) 全 10 葉語意對應覆核結果（逐葉）
7. 台帳兩條指令輸出
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R34-1 ECU tag vs 行為主詞之兩層判準（含 -005／-008 對照）—— §1
- [x] R34-2 -008 排除確認（四項證據）—— §1，區塊形式
- [x] R34-3 -008 BLOCKED 列 + 第一個 marker + A-PV18 + RD-1 #12 —— §1
- [x] R34-4 速度激勵：ER 不得斷言音量與車速關係 —— §1，區塊形式
- [x] R34-5 gate 須具陽性＋負向雙對照（§5a）—— §1，區塊形式
- [x] R34-6 NOT MEASURED 追認，P6 後重標 —— §1，區塊形式
- [x] R34-7 VF651 不進 spec_reference，推及全批 —— §1，區塊形式
- [x] R34-8 觀察手段重疊不構成 duplicate（§5a）—— §1，區塊形式
- [x] R34-9 PROXI 值不可得，§8.4.1 處置追認 —— §1，區塊形式
- [x] R34-10 連續三次未辦即升為硬性前置（§5a）—— §1，區塊形式
- [x] 停手條件四項（已依 R17-1 明列標的與續行標的）—— §3

<!-- HANDOFF-LINK: 12 -> upstream:12 -->
