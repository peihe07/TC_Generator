# 01b 下放包 — User Profiles 作業指示（執行層）

裁決依據見 `01a_rulings.md`；量測基準見 `01_intake.md`。

## 作業順序

1. **Scaffold** — `scripts/new_feature.py` 建 `features/user_profiles/`。
   `docs/handoff/` 已存在且已有本輪三份檔案；若腳本拒絕既存目錄，
   補齊其餘檔案即可，**不得刪除或覆寫本輪三份下放包**。
   由 `01a_rulings.md` 播種 `RULINGS.md`（R-U1～R-U7 逐字），
   由 `01_intake.md` 播種 `ANOMALIES.md`（A-UP01～A-UP03）。

2. **R-G1／R-G2／R-U7 之 form 處置** — 先對 `forms/` 內四份 036 檔
   算 `shasum -a 256` 並記錄；依 R-G2 建 `archive/forms_superseded/`，
   以 `mv` 移入 20260121、20260816_ext、Home_20260809 三份
   （**不得使用 rm**），移後重算 SHA 確認一致；`forms/` 應僅餘
   20260817_ext 一份。FORMS.md 各既有條目改指 archive/ 路徑，
   條目不刪。另：
   對 `20260817_ext` 做結構探測；`FORMS.md` 新增本版條目、修復
   `20260816_ext` 之脫鉤條目（A-UP03）、寫入 R-G1。
   母本複本置於 `features/user_profiles/inputs/`，建立 `BASELINE.sha256`
   （涵蓋 inputs/ 全部檔案＋ spec-index 之 Personal Account 三件，
   比照 Comfort R-C20：涵蓋以來源為準，「還沒用到」不是不保護的理由）。

3. **Recon** — `scripts/recon.py`。判準：header row = 含
   `Requirement Description` 之列（本件為第 7 列）；leaf = Categorization
   以 `Functional` 起始者。**預期值：葉節點 182、扣除 Out of scope 2 後
   母體 180、Heading 25**。與預期不符即停並回報，不得自行調整判準。

4. **Outline map** — 由 spec `Basic Report` 之 `SYSRE_HMI_Source ID` 欄
   建 section id → 正文對映（169 條）。037 引用之 135 個 id 須全數命中，
   fail-loud on miss。

5. **Framework Part N** — Layer 1 = `User Profiles`；Layer 3 骨架 = spec
   章節 4–14（章 1–3 不入生成範圍，見 A-UP02）。Layer 2 取
   spec 目錄與 037 分群之交集，草案回上繳包，**不自裁**（Tier 2）。

6. **上繳** — `features/user_profiles/docs/upstream/01_intake.md`，
   同時更新 `docs/INDEX.md`（分析層不寫該檔）。

## 上繳包必附

- 「本包是否仍有該驗而未驗者」之獨立判斷（不得省略）
- 每一數字之量測條件（量什麼、單位、掃描哪些欄位、是否區分大小寫）
- 凡本包預期值與實測不符者，逐項具名，不得以「已修正」帶過

## 未決（不在本包授權範圍）

- A-UP02 之 8 條無覆蓋 spec 條文 → RD-1，Tier 3 由 Pei 送出
- Layer 2 Test Set 邊界 → Tier 2
- （已裁定，移至作業項 2）forms/ 舊檔 → R-G2：歸檔，不刪除
