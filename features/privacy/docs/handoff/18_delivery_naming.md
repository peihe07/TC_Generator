# 下放包 18 — P-8 裁定（交付檔名）

分析層 → 執行層。2026-08-13。Pei 回覆「A」，P-8 選項 A 簽署。

**本包為短包**，僅記 P-8 之裁定與其連動；下放包 17 §3 各項不受影響，
兩包可併行執行（17 §3.6 之「P-8 未裁前不得改名」限制自本包起解除，
但交付動作仍屬 Tier 3）。

---

## 1. 裁決條文

```text
[RULING] R40 — Privacy 交付檔名與 ENTRY 003（Pei 簽署 2026-08-13）

R40-1  交付檔名
  裁：採選項 A ——
  (a) `features/privacy/output/` 內之產出檔**維持現名**
      `FM-WI-FSM-036-A01 …_SWQT_Privacy_20260813_regen-v1.xlsx`
      理由：`output/` 內已有 `…_SWQT_Privacy_20260813.xlsx`
      （ENTRY 001 之準備工作簿），改名會撞名；且 DELIVERY 台帳
      之路徑記載須與實體一致。
  (b) 交付至 `10_Reviewing/` 時**另存**為
      `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
       Specification & Result_SWQT_Privacy_20260813.xlsx`
      —— 與 AMFM（`…_AMFM_20260810.xlsx`）／
      SXM（`…_SXM_20260813.xlsx`）之命名一致
      （分析層對該兩份交付檔實測確認其不帶後綴）。
  (c) 交付後追加 **ENTRY 003**，欄位：
      交付路徑 / 交付檔名 / SHA256 / bytes / 交付日期 /
      「內容同 ENTRY 002，僅檔名與位置不同」之註記 /
      末行 `STATUS:`（依 R39-5）
      **SHA256 應與 ENTRY 002 相同**。
  (d) 交付後對**交付副本**重算 SHA256 與 ENTRY 002 比對；
      **不符即停手**，不得以「複製應該不會變」為由略過。

R40-2  ENTRY 003 之新增時點
  裁：ENTRY 003 於**交付動作完成後**新增，不得預先寫入。
      理由：台帳記錄之單位為已發生之事實（R27-2、R39-5）；
      預寫之條目在交付未執行時即為不實記載。
      交付屬 Tier 3（僅 Pei），故 ENTRY 003 之新增為交付後之
      執行層作業，須由 Pei 告知交付已完成後方得辦理。

R40-3  交付位置
  裁：`10_Reviewing/00_TestCase/` 之下，**實際路徑由 Pei 於交付時決定**。
      分析層不指定 —— 依 charter，交付形式、交付位置、送達執行
      均屬 Pei 之裁定範圍。
      既有同類路徑供參（分析層實測）：
        `ASW-R2/AMFM/`、`ASW-R2/SiriusXM/`、
        `ASW-R2/Privacy Mode/`（本 feature 素材來源目錄）
```

---

## 2. 執行層作業

**交付前**（可即刻辦）：無 —— 本包各項均待交付動作完成。

**交付後**（Pei 告知已交付後）：

1. 貼入 §1（R40）至 `RULINGS.md`
2. 對交付副本重算 `shasum -a 256`，與 ENTRY 002 之值逐字元比對
3. 比對相符後，追加 **ENTRY 003**（R40-1(c)），末行含 `STATUS:`
4. `PLAYBOOK.md` §6 記入交付路徑與交付日期
5. 台帳兩條指令回跑，須全綠

---

## 3. 停手條件

1. 第 2 項之交付副本 SHA256 **與 ENTRY 002 不符** → **停止第 3–4 項**，
   續行回報兩值與交付路徑。
   理由：內容不同表示複製過程改動了檔案，
   在成因判定前不得以台帳認可該副本為交付件
2. `RULINGS.md` R40 編號已占用 → 停止貼入，續行第 2–5 項
3. Pei 未告知交付完成 → **不執行本包任何一項**

---

## 4. 上繳包要求

併入 `features/privacy/docs/upstream/17_predelivery.md`（不另開，
並於 handoff／upstream NN 對應表註記 `18 → merged into 17`）：

1. 交付副本之 SHA256 與 ENTRY 002 之比對結果
2. ENTRY 003 全文
3. 更新後之 `PLAYBOOK.md` §6 交付段
4. 台帳兩條指令輸出

---

## 5. Tier 3 序列（僅 Pei，本包不執行、不催辦）

1. 依下放包 17 §3.5 之獨立複驗數據，與 tag annotation 草案逐項比對
2. commit（執行層備妥 message）
3. tag `fw036-privacy-v1`（annotation 載**全長**雜湊，帶 `--date`）
4. 交付 —— 另存新檔名至 `10_Reviewing/00_TestCase/` 下之選定路徑
5. 告知執行層交付完成 → 本包 §2 各項啟動
6. RD-1 送出（#6–#13 八項），時點由 Pei 決定

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R40-1 交付檔名（output 維持／交付另存／ENTRY 003／重算比對）—— §1
- [x] R40-2 ENTRY 003 不得預寫 —— §1，區塊形式
- [x] R40-3 交付位置屬 Pei，分析層不指定 —— §1，區塊形式
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §3

<!-- HANDOFF-LINK: 18 -> merged into 17 -->
