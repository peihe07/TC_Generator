# 01Z-A3 — 上繳 01Z 之覆核，並更正 R-TM9 之框架

分析層。覆核對象：`docs/upstream/01Z_corrections.md`。

**結論：受理。** 但 R-TM9 之整個框架須更正 —— **D5 不是 feature 標籤欄，
是 037 報告之文件識別欄**。此一更正由執行層 §3.2 之獨立第二樣本觸發，
分析層據以追查後證實，並連帶改變 A-H26 與 A-TM02a 之性質。

---

## 1. 已複驗且相符者

- **A-TM15 之工具行為** —— 分析層已於 01R 覆核時通讀 `recon.py`，
  `write_decisions()` 確為：`signoff["signed"]` 為真才轉寫
  `DECISIONS.new.md`，否則 `target.write_text(body)` **整份覆寫**。
  且 R-G4 之 `write_data_file()` 保護**只套用於 `data/*.tsv`**，
  `DECISIONS.md` 不在其射程內。執行層所述與工具實際行為一致。
- **T4 六項數字** 全數相符，且 §4.1 之「兩種獨立判準（`w:pStyle` vs
  字面）收斂到同一結果」為比單次量測更強之證據 —— 此作法採納，
  往後之量測若成本許可應比照。
- **§4.2 之 5 筆 split cells 皆落單一章節** —— `spec_reference` 取值
  無多章節裁決問題，此為有價值之附帶結論。
- **§2.1 之陰性對照設計**（35 筆 Home xlsx 陽性對照 + 150 筆 SHA 全域比對）
  正確且必要。特別是「不依賴檔名、改以 SHA256 全域比對」一著，
  排除了改名之可能性，使「確已不存」之結論成立。

## 2. §1.1 之 `git diff` 12 行 —— 執行層之釐清成立，但問題不在此

釐清正確：01 包之更正未 commit，故 diff 基準為 Phase 0 之 HEAD。

**但真正的問題是分析層寫錯了驗收條件。** 指令集 T1 寫「`git diff` 確認
只動這一行」，而在「全部 git 屬 Pei、執行層從不 commit」之工作形態下，
`git diff` 必然累積數個往返之全部更正，**該條件從一開始就不可能成立**。

```
R-TM11（分析層自裁，2026-08-20）—— 驗收條件不得預設 commit 節奏

下放包之驗收條件不得以 `git diff` 之範圍為判準。本專案全部 git 操作屬
Pei，執行層之工作樹持續累積跨往返之未提交更正，故 `git diff` 反映的是
「自上次 commit 以來」而非「本包」。

單行修改之正確驗收方式為：修改前 assert 目標字串存在且唯一、
以 count=1 取代、修改後複查該行。執行層本包所採之
`assert old in t` + `replace(o, n, 1)` 即正確形態。

依據：01Z-A2 T1 之驗收條件不可能成立（本包 §2）。
與 R-TM7 同族 —— 前者是指令未經實測，本條是驗收條件未經可行性檢查。
```

## 3. **R-TM9 之框架錯誤 —— D5 是 037 文件識別，不是 feature 標籤**

執行層 §3.2 取得之第二樣本
（`FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx`）
使分析層循交付路徑追查，實測如下（`/Users/peihe/Work/02_Project_R1LR/
10_Reviewing/00_TestCase/ASW-R2/`）：

| 目錄 | 036 工作簿 | **同目錄之 037 報告** |
|---|---|---|
| `Core HMI/HomeHMI/` | `…_SWQT_Home_20260809.xlsx` | `FM-WI-FSM-037-A03-N1L-SWE1-`**`Home-HMI-V0.1`**` STLA 報告.xlsx` |
| `Core HMI/Menu Bar and AppDrawer/` | `…_SWQT_AppDrawer_20260729.xlsx` | `FM-WI-FSM-037-A03-N1L-SWE1-`**`AppDrawer-HMI-V0.1`**` STLA 報告.xlsx` |
| `User Profiles/` | `…_SWQT_UserProfiles_20260820.xlsx` | `FM-WI-FSM-037-A03-N1L-SWE1-`**`PersonalAccount-HMI-V0.1`**` STLA 報告.xlsx` |
| `Time Management/` | **無** | **無** —— 只有 CFTS docx、SYS2、`SWE1_Secure_Date&Time.xlsx` |

三個 feature 之 037 檔名皆為
`FM-WI-FSM-037-A03-N1L-SWE1-<X>-HMI-V0.1 STLA 報告.xlsx`，而 Home 工作簿
之 D5 值為 `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1
STLA 報告` —— **D5 之值就是一份 037 報告的檔名去掉副檔名。**

### 3.1 三項連帶結論

**(a) R-TM9 之「feature 識別段」框架作廢。** D5 不是給 feature 取個名字，
是宣告「本工作簿依據哪一份 037」。`Time-and-Date-HMI-V0.1` 這個值除非
真有一份叫那個名字的 037，否則寫下去就是指向一份不存在的文件。

**(b) A-H26 之性質比既有記載更嚴重。** 既有記載稱其為「Scope 未修正」，
讀起來像標籤打錯字。實際上 Home 工作簿之 D5 指向的是
`AppDrawer-Projection-SWE1HMI-V0.1` —— **另一個 feature 的 037**。
那不是筆誤，是**追溯來源指錯文件**。`SWE1HMI` vs 三個實例一致之 `HMI`
亦佐證該字串非取自任何真實檔名。
執行層 §3.2 之第 2 點疑問（是否該複製 `SWE1HMI` 寫法）**答案為否**，
且理由比「形態不一致」更強：那個字串整體不對應任何文件。

**(c) A-TM02a 由「上游版本問題」升為「阻塞交付欄位」。** 本 feature 之
037 名為 `SWE1_Secure_Date&Time.xlsx`，**不符三個實例一致之
`FM-WI-FSM-037-A03-N1L-SWE1-<X>-HMI-V0.1 STLA 報告` 形態**，且交付目錄
`Time Management/` 下並無任何符合該形態之檔案。故 D5 之值在 A-TM02a
裁定前**無法取得**，不是「暫緩填」而是「無值可填」。

### 3.2 裁決

```
R-TM9-A2（分析層，2026-08-20）—— 撤回 R-TM9 之識別段裁定，改綁 A-TM02a

R-TM9 及 R-TM9-A1 關於 D5 值之全部內容撤回，包括
「feature 識別段 = Time-and-Date-HMI-V0.1」與前綴段之切分作業。
撤回理由見本包 §3：D5 之語意為「本工作簿所依據之 037 報告之文件識別」，
非 feature 標籤，故不可由 feature 名組成。

新規定：
1. D5 之值 = 本 feature 所依據之 037 報告之檔名（去副檔名），逐字照抄。
2. 該值在 A-TM02a（037 身分）裁定前無法取得。D5 維持空白。
3. 空白是可見狀態；指向不存在文件之值不是。任何情況下不得以
   feature 名、spec 標題或類推形態組出一個字串填入（§8.4.1）。
4. A-TM11 之解除條件改為：A-TM02a 裁定 + 037 檔名逐字實測。
   不再綁 Home 之前綴段切分。

R-TM8（test_group = "Time and Date"）不受本條影響 —— 該欄是 Test Group，
語意為功能模組名，與 D5 之文件識別語意不同，兩者本不必一致。
```

```
A-TM16（PENDING，Tier 2 / 跨 feature）—— A-H26 之既有定性可能低估

Home 之 A-H26 於既有文件中記為「Scope 欄未修正」。依本包 §3 之實測，
該欄之語意為 037 文件識別，而 Home 工作簿之值指向
AppDrawer-Projection 之 037（且其 `SWE1HMI` 形態不對應任何實存檔名）。

若此讀法成立，A-H26 不是標籤筆誤而是追溯來源指錯文件，其嚴重性與
既有記載不同。**本條不裁 Home 之事**，僅登記供 Home 之 owner 覆核；
本 feature 之處置已由 R-TM9-A2 涵蓋。

證據：交付路徑三個 feature 之 037 檔名形態一致
（Home-HMI-V0.1 / AppDrawer-HMI-V0.1 / PersonalAccount-HMI-V0.1）。
```

## 4. A-TM14 之加深 —— 兩份同名檔

執行層 §2.2 之發現（交付路徑與 archive 各有一份 `…_SWQT_Home_20260809.xlsx`，
SHA 相異、差 754 bytes、mtime 差 10 天）**成立且重要**：FORMS.md 之
provenance warning 其**受測物身分**已不可判定 —— 該 warning 測的是哪一份，
現無從得知。

此使 A-TM14 之損害範圍擴大：不只基準（v2）不可覆驗，連「被判定受污染者」
是哪一份也不確定。A-TM14 之條文須補入本項。

執行層未認定交付路徑該份可用、未複製、未援引 —— **正確**。
§7.3 第三列之推理（「檢查其是否乾淨」在實質上已是把它當候選來源評估）
**採納**，這是對 SUSPENDED 之正確理解，記錄為往後之標準讀法。

## 5. A-TM15 之覆核

**執行層之自我更正應予肯定**：01 包上繳 §5 之陳述字面無誤但整體誤導，
主動更正且指明失誤性質（未驗證**後果**，相對於 A-TM09／A-TM12 之未驗證
**前提**）—— 此分類正確。

**分析層之責任亦須記錄**：`00` §4(1)、`01` §1、`01Z-A2` T5(4) 三包都要求
在 `DECISIONS.md` 建裁決引用條目，而 `01` §5 同時要求跑 `recon.py`。
**這兩條指示在同一個下放包內互相抵銷，是分析層下放包之缺陷**，
不能只記為執行層未複查。

§6.4 之處置（重建 §0、標警告、列四項覆寫關係）Tier 1 範圍內，採納。
`recon.py` 修法屬 Tier 2，與 A-TM04 / A-TM05 / A-TM10 / A-TM12 併案。

**§7.2 之「寫入後複查」全集為本包新增，直接源自本次教訓 —— 此為
盤點全集之正確演化方式，採納為往後常態。**

## 6. §7.4 之 PU 陰性對照 —— 判斷正確，補一條可行路徑

「未證明該掃描方法對確實含 PU 之文件會命中」之自我標示正確，
不略過亦不誇大。

補充：陽性對照物**已在 repo 內** ——
`features/amfm/inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`
（AMFM DATA_REQUESTS #5b 載其已入 `inputs/`）。該檔本身即 PU 編號之集合，
可用以驗證正則是否捕獲。**但跨 feature 取用他 feature 之 `inputs/` 檔案
須 Pei 裁**（素材補入超出既定根目錄）。列為建議，不逕行。

## 7. 執行層下一步

1. R-TM9-A2、R-TM11 逐字寫入 `RULINGS.md`；A-TM16 登記
2. A-TM14 條文補入 §4 之「兩份同名檔使受測物身分不可判定」
3. A-TM11 之解除條件改綁 A-TM02a（R-TM9-A2(4)）
4. 索引表 → **16 條**
5. **T3 之切分作業全部作廢**，不必再做；已取得之 `repr()` 保留為 A-TM16 證據
6. 極短上繳

## 8. 呈報 Pei

| # | 事項 | 層級 | 建議 |
|---|---|---|---|
| 1 | **A-TM02a 037 身分** | Tier 3（RD-1） | **已升為阻塞項** —— D5 交付欄位無值可填。交付路徑 `Time Management/` 下無 `FM-WI-FSM-037-A03-N1L-SWE1-*` 形態檔案，須向上游確認是否另有正式 037，或 `SWE1_Secure_Date&Time.xlsx` 即是而命名未依慣例 |
| 2 | A-TM13 兩筆 CFTS 基線缺口 | Tier 3（RD-1） | 與 1 併問 |
| 3 | R-TM10-A1 解除 | Tier 2 | Home v2 內容經 150 筆 SHA 全域比對確認不存在；替代來源請裁。**交付路徑那份同名檔不建議** —— 其與 archive 版孰為 FORMS.md 之受測物已不可判定 |
| 4 | `recon.py` 五項修法（A-TM04/05/10/12/15） | Tier 2 | 併為一次修改一次回歸 |
| 5 | A-TM16 之 Home A-H26 重新定性 | Tier 2 | 屬 Home，非本 feature |

`02`（framework）不受上列阻塞 —— Test Set 之推導依 22 筆 leaf 與 21 個
可達章節即可起草，不依賴 D5 或 037 檔名。**分析層可即刻起草。**

## 9. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM9-A2 | 撤回 R-TM9／R-TM9-A1 之 D5 內容，改綁 A-TM02a | ✅ §3.2 |
| R-TM11 | 分析層自裁，驗收條件不得預設 commit 節奏 | ✅ §2 |
| A-TM16 | anomaly，PENDING，Tier 2，屬 Home | ✅ §3.2 |

本包 §3 之全部斷言為 2026-08-20 對交付路徑之實測（目錄列舉，非轉述）。
分析層未動 git、未改腳本、未開啟任何 xlsx、未複製任何檔案。
