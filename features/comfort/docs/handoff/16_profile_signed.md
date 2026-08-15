# 16 — Comfort HMI / profile 簽署 ＋ Phase 4 起跑條件

- 產出層：分析層｜2026-08-15｜對象：執行層
- 簽署：Pei，2026-08-15（「裁的都是是是是」—— 下放包 15 §9 三項全數照建議）
- 承接：`15_profile_draft.md`

---

## 1. 15 §9 三項之裁定

| # | 事項 | 裁定 |
|---|---|---|
| 1 | §3.1 Test Item 繼承（modal 允許於該欄） | **照建議** —— 繼承，**且其附帶條件一併生效**：簽署前須對 `home` done region 實測比對。條件併入裁定，不因核可而消失，故轉為 §2 之 gate |
| 2 | §3.4 `«Front»`／`«Rear»` 等 source token 照錄 | **照建議** —— 照錄。§11 profile-scoped 例外，前例 Home A-H10。含 `12.1` 之 `LEDs (.` |
| 3 | §0.1 Excel 實開確認由 Pei 執行 | **照建議** —— 同 Privacy R29-1 |

下放包 15 之其餘條款於本包簽署時一併生效。執行層據以寫
`docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。

---

## 2. G-1 gate —— §3.1 之實測前置

「繼承但須實測」不改寫成「先問一輪再繼承」，而是寫成 gate，使其在流程中
機械發生，不倚賴記得。

```
G-1  Test Item 形態實測

對象：features/home 之 done region（144 列）之 Test Item 欄。

量測條件須明載：讀哪一個檔、哪一張工作表、哪一欄、母體幾列、
以何判準判定「含 modal」（shall／will／should／would，case-insensitive，
詞界比對）。

輸出（PASS/FAIL + 實測值）：
  - 144 列中含 modal 者幾列、不含者幾列
  - Test Item 是否為需求陳述之濃縮（相對於 tc_title 型短語），
    以隨機 10 列全文並列呈現，供分析層判讀

判定：
  - 若 done region 之形態與 profile §3.1 一致 → §3.1 生效，Phase 4 續行
  - 若不一致 → §3.1 停止適用，回分析層重裁；**不得自行調整 §3.1 以
    遷就實測結果**（調整 profile 屬 Tier 2）

G-1 為 Phase 4 之前置，但**不阻塞 profile 落檔**：profile 先寫，§3.1 段
標註「pending G-1」，G-1 PASS 後移除該標註。
```

理由：15 §3.1 之風險具體 —— exemplar 是 `home` 而非 Privacy／SXM，若 home
之該欄形態不同，pilot review 會整批被判 style-divergence，而那時已寫了 14 條 TC。

---

## 3. 執行層作業指示

### 3.1 先做（本輪）

1. 依下放包 **14** 之 §5 全部六項（Part N 四節改置、R-C19、五處同步、
   `verify_partn.py` 七項重跑、`framework.md` 增記、`DECISIONS.md` §6 增記
   且 Sign-off 不重簽、`RUNBOOK.md` 記 SYNC 註記）。
2. 依下放包 **15** ＋ 本包 §1 寫
   `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。
   §3.1 段標註 `pending G-1`。
3. 執行 **G-1**（§2）。
4. `DECISIONS.md` §6 之 profile `[OVERRIDE]` 由 `[PEI — 維持未定]` 轉為
   **`[SIGNED 2026-08-15]`**，記本包為依據。**Sign-off 區塊增列第二筆
   簽署記錄，不覆寫首筆**（R-C10；首筆為 Part N，2026-08-14）。
5. A-CF07 依 profile §0.1 執行範本清列，並建
   `features/comfort/BASELINE.sha256` 與 `DELIVERY.sha256`（ENTRY 001）。
   **Excel 實開確認由 Pei 執行，執行層備妥檔案後停下等候**（裁定 3）。

### 3.2 不做

- **Phase 4 不開始** —— 起跑條件為：G-1 PASS ＋ profile 落檔 ＋ A-CF07
  清列經 Pei 於 Excel 確認。三者皆備方可產第一條 TC。
- 不重跑既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 不執行 git。

### 3.3 上繳

`docs/upstream/09_partN_amendment_and_profile.md`（14 與本包共用一次往返），
附「本包是否仍有該驗而未驗者」之獨立判斷，更新 `docs/INDEX.md`。

---

## 4. Phase 4 起跑後之首批（預告，本包不執行）

- pilot = `Seat Control Tab`（13.2 ~ 13.6，**14 leaves**），DECISIONS.md 已簽
- pilot review 依 canon §1.2：分層取樣；發現先分類為 defect /
  style-divergence / note，再決定是否阻塞
- **R-C19 違反者列 defect，非 style-divergence**（14 §3）
- 首筆 TC 落於 workbook **row 10**（profile §0.1）

---

## 5. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| G-1 Test Item 形態實測 gate | ✅ §2 | 已簽 2026-08-15 |

G-1 為 gate 非 R-Cnn 條文，寫入 `features/comfort/RUNBOOK.md` 之 Phase 4
前置段，不入 `RULINGS.md`。下放包 15 之 profile 條款隨 profile 檔落地。
