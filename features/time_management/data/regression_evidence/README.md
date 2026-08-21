# 回歸測試遺留物

依 **R-TM30**（2026-08-20）自 `features/privacy/` 移入，**mv 非 rm**。

## 來源與緣由

兩檔為 **A-TM15 修法之回歸測試產物**，產生於 2026-08-20 執行
`docs/handoff/03Z-A1_amendment.md` T4 時。

受測物選定 `features/privacy/`，依據 R-TM22 條件 2（後經 R-TM28 收緊）：
`signed=False`、宣告路徑齊全、相隔 14 分 10 秒之兩次 mtime 快照無變動。

| 檔案 | 原路徑 | 大小 | 性質 |
|---|---|---|---|
| `privacy_DECISIONS.new.md` | `features/privacy/DECISIONS.new.md` | 2372 B | **A-TM15 修法正確運作之現場證據** —— 修法後 recon 對既存且未簽核之 `DECISIONS.md` 不再覆寫，改寫入此檔 |
| `privacy_recon_leaf_to_section.tsv` | `features/privacy/data/recon_leaf_to_section.tsv` | 48 B | recon 之副產物（僅表頭列）|

## 為何移入而非刪除

1. 刪除不可逆；mv 可逆
2. 證據價值屬本 feature（A-TM15 之驗證），不屬 Privacy
3. 鄰居目錄不留來歷不明之檔案

## `features/privacy/` 之還原狀態

- `RECON.md`：已還原，SHA `2f3dc3dc726c297fe4535facef78927fcb0b0b27cae97da1b562ba59b3d4aa3a`
- `DECISIONS.md`：未被最終改動，SHA `a1a685a120f6e9c2ecff46d3aa82903e5f8c94d65f21aa354f02600b625b3569`
  （取真基線時曾被沖為 `622bdc44…`，已還原並經 SHA 驗證 —— 見
  `docs/upstream/03Z_corrections.md` 第二節 §3.2）
- 本次移出後，該目錄與動它之前完全一致

## 相關條文

R-TM30（處置）、A-TM15（被驗證之修法）、R-TM22 / R-TM28（受測物判準）、
R-C9（未被削弱之既有保護）。
