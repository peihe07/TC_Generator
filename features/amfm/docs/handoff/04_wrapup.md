# 下放包 04 — 收束：不重產，凍結解除，焦點回 Privacy

分析層 → 執行層。2026-08-13。Pei 裁示：**「做過的都不重產，只專心在現在」**。

本包目的是把 R16/R17 的未決項一次收乾淨，不留掛帳，讓 Privacy 無阻塞前進。

---

## 1. 裁決條文

```text
[RULING] R18 — 交付件結構缺損之收束（Pei 簽署 2026-08-13）

R18-1  已交付件一律不重產
  裁：SXM（fw036-sxm-v1）與 Home（fw036-home-regen-v2）維持現狀，
      不重產、不改 tag、不動任何一列。
      各自之結構缺損以 anomaly 形式登記，狀態 **DEFERRED —
      待下次內容變動時一併修復（R18-1）**，非 PENDING
      （依 R15-2：已裁而結果為延後者不得留在 Open PENDING）。
      登記內容須含實測數字：
        SXM   lost 11 / added 10，x14 DV 2 → 0（R 欄設計方法下拉）
        Home  lost 14 / added 10，含整組 SmartArt；x14 DV 0 → 0
              （該檔本無 DV，DV 判準看不見此缺損）
  R17-6 / R17-7 據此結案。whole-sheet splice 提案**不實作**，
      僅保留於 03 包內作為日後 interleaved 修復之已知路徑。

R18-2  AMFM v2 之處置
  裁：v2 已產出，保留於 output/，**不打 tag、不送出、不再加工**。
      v1 tag fw036-amfm-regen-v1 維持不動。
      v2 附掛未驗標籤：**尚未經 Excel 實開驗證（R17-9）**，
      交付前必須先由 Pei 完成該四點確認。時點由 Pei 決定。
      本包不觸發任何後續動作。

R18-3  凍結解除，代之以常設規則
  裁：R16-2 之全 repo 寫回凍結**即刻解除**。
      解除依據：探針對 AMFM 客戶原件與 FW036 空白範本兩次驗證
      皆 LOSSLESS（上繳包 02 §2 附原文），且不再有任何重產動作。
      代之以常設規則，即刻生效、適用全 feature：
        (1) backend/xlsx_surgical.py 為**唯一**寫回路徑；
            openpyxl 存檔路徑不得用於任何交付件產出
        (2) 寫回後強制比對輸出與輸入之 zip 成員集合、
            各 sheet 之 classic / x14 DV 計數，不等即 **ABORT**
            （非 warn）；允許差異者僅限被寫入之 sheet XML 本身
        (3) 該 invariant 之違反屬 canon §0 第三項，升 Tier 2，
            不得以放寬 invariant 解決
      五個 PLAYBOOK 之凍結橫幅一併移除，改記本規則。

R18-4  R17-5(b) 反向測試 —— 仍須執行，但不擋任何工作
  裁：invariant 之反向測試（以刻意破壞之輸出驗證確實 ABORT）
      仍須完成，因「不可能失敗之檢查項不得標 PASS」。
      但其完成與否**不作為任何 gate 之前提**，Privacy 照跑。

R18-5  AMFM 第 243–310 列無儲存格樣式
  裁：登記為 anomaly，**不修**。v1、v2 皆然，非結構缺損所致。
      狀態 DEFERRED — 待下次內容變動時一併處理。

R18-6  焦點
  裁：AMFM / Home / SXM / Projection 四 feature 之結構缺損議題
      至此**全部結案或 DEFERRED，無 Open PENDING**。
      分析層與執行層之工作焦點回到 Privacy。
```

---

## 2. 執行層作業（一次做完，不分批）

1. 貼入 §1 全文至 `features/amfm/RULINGS.md`（R18；占用則停手回報）
2. `features/{sxm,home}/ANOMALIES.md` 各登一條，含 R18-1 之實測數字，
   狀態 `DEFERRED — 待下次內容變動時一併修復（R18-1）`
3. `features/amfm/ANOMALIES.md`：A-AM18 改為 DEFERRED；
   另登 243–310 列樣式一條（R18-5），同為 DEFERRED
4. 移除五個 `PLAYBOOK.md` 之凍結橫幅，改記 R18-3 之常設規則
5. 依 R15-2 通則掃過五個 feature 之 Open PENDING，
   凡屬本輪 DEFERRED 者一律移出
6. 將 R18-3 之常設規則寫入 `docs/fw036/FEATURE_ONBOARDING.md` P7 交付段
   之**草案**（R16-4 之 canon 升格），供 Pei 簽，不直接改 canon
7. 執行 R18-4 之反向測試，回報兩次輸出原文

**不做**：不重產任何交付件、不打／改任何 tag、不動 AMFM v2、
不執行任何 git 操作、不實作 whole-sheet splice。

---

## 3. 停手條件

1. `RULINGS.md` R18 編號已占用 → 停止貼入，續行第 2–7 項
2. 第 4 項移除橫幅時發現某 feature 之橫幅內容與 R16 所述不符
   → 停止該 feature 之橫幅處理，續行其餘，回報差異
3. 第 7 項反向測試未能觸發 ABORT → 停止該項並回報，
   **續行其餘所有項**（invariant 缺陷不阻塞登記作業）

（依 R17-1：停手條件已明列停手標的與續行標的。）

---

## 4. 上繳包要求

寫入 `features/amfm/docs/upstream/04_wrapup.md`，須含：

1. §2 七項之完成狀態
2. 五個 feature 之 Open PENDING 清空後現況（逐 feature 列出剩餘項）
3. R18-4 反向測試之兩次輸出原文
4. canon 草案之路徑
5. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R18-1 已交付件不重產，缺損 DEFERRED —— §1，區塊形式
- [x] R18-2 AMFM v2 保留不送，附掛 R17-9 未驗標籤 —— §1，區塊形式
- [x] R18-3 凍結解除 + 三項常設規則 —— §1，區塊形式
- [x] R18-4 反向測試不作為 gate 前提 —— §1，區塊形式
- [x] R18-5 243–310 列樣式 DEFERRED —— §1，區塊形式
- [x] R18-6 焦點回 Privacy —— §1，區塊形式
- [x] 停手條件三項（已依 R17-1 明列標的）—— §3

以上均以可直接貼入之區塊形式出現，非夾敘於段落中。
