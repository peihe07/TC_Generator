# 25 下放包 — W-32 覆核、09 輪指令

分析層寫入，2026-08-20。對象：W-32 之回報與 `data/leaf_to_reqid.tsv`。

---

## 1. 覆核：接受，並經分析層抽樣複驗

分析層自 `inputs/` 之 CFTS044 原始 docx **獨立重建**
（`word/styles.xml` 之 `styleId 1–7` → heading；需求段落以
`\b(\d{7})\b\s*:\s*\[Artifact Type` 錨定；以位置歸屬最近之前方章節），
得 **需求區塊 2,030、章節錨 270**，與執行層相同。

抽樣比對 `data/leaf_to_reqid.tsv` 前五列：

| reqid | tsv 之 section | 分析層獨立解出 |
|---|---|---|
| `CFTS044-4858549` | 1.3.2.1.3.12.1 | **1.3.2.1.3.12.1** |
| `CFTS044-4858550` | 1.3.2.1.3.12.1 | **1.3.2.1.3.12.1** |
| `CFTS044-4858551` | 1.3.2.1.3.12.1 | **1.3.2.1.3.12.1** |
| `CFTS044-4858553` | 1.3.2.1.3.12.1 | **1.3.2.1.3.12.1** |
| `CFTS044-4858555` | 1.3.2.1.3.12.1 | **1.3.2.1.3.12.1** |

另抽多值列之成員：`4858304`→`1.3.2.1.3.1`、`4858317`→`1.3.2.1.3.1`、
`4859492`→`1.3.3.3.6.1`、`4859377`→`1.3.3.3.2.1` —— 皆與 24 包 §2 之記載相符。

**5 / 5 相符。** 抽樣非全量，此點具名。

## 1.1 (d) 之獨立性成立

執行層之兩條路徑：
`reqid` 走 037 → SYS-RA → SYS2 錨鏈；
`章節` 走 docx 樣式階層。**唯一共同點為 7 位數 id 本身**，
「它屬於哪一章」由兩個互不相干之來源各自給出，236 筆全數一致。

**且其自陳之附帶收穫成立**：`outline_map.tsv` 之 section 係 00 輪以
**位置法**建立，本次以**樣式階層**重解並逐 reqid 比對 —— 兩者一致，
等同把 00C §2.2 當時只到 leaf 層級（245／25／1）之複驗，
推進到逐 reqid 層級。**位置法於此 236 筆上獲證。**

該未驗項可除役：登記為 **A-VS06′ 之關聯項已收**（不新開 anomaly）。

---

## 2. 現況盤點

| 項 | 狀態 |
|---|---|
| N 欄取值來源 | **已備**。236 / 237 可直接填，1 筆（`SWE1-VC-HeatedSteeringWheel-009`）依 R-VS17 標 BLOCKED（DR-11） |
| 母體 | 237 Functional leaf（R-VS15） |
| Test Set | 四個（R-VS4） |
| 訊號名寫法 | R-VS9(1)′ ＋ L-VS2 |
| 值域來源 | R-VS20 階梯 |
| 委派界線 | R-VS7；來源表 06 輪已出，**反向表未出（W-29）** |
| **framework 之外部阻塞** | **DR-15 一項** —— 請求訊號 1 bit vs 帶階，決定 Heated Seat 88 ＋ Vented Seat 72 共 160 leaf 之分支結構與設計方法 |

### 2.1 未結之作業（依序）

| 作業 | 狀態 |
|---|---|
| **W-22 續作** | 22 包裁定之三項（式八重跑／(c) 36 筆逐筆人讀／W-22(d) 極性標記）**尚未執行**；`docs/upstream/07_residual_verification.md` 六節**尚未填** |
| W-29 | 反向委派表（本 feature 側為列） |
| W-30 | BLOCKED 16 leaf 之具名與 R-VS7(a)/(b) 優先序檢查 |
| W-17／W-24／DR-14′ 追問／`unesc()` 併模組 | 小項 |
| 36 條「未分左右」複核 | 06 輪 §6-1 |

---

## 3. 09 輪指令

依 R-VS28：W-22 續作自 22 包起已延一輪，尚未達四輪門檻；
依 R-VS25 上限三項。**本輪三項。**

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/22_w22_adjudication.md  W-22 續作之裁定
  features/vehicle_setting/docs/handoff/24_reqid_source_correction.md
  features/vehicle_setting/docs/handoff/25_review_w32.md     本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  補完 docs/upstream/07_residual_verification.md 之六節
     （W-22 之三式→八式全程、R-VS27 之 27 筆證否結果、W-32 之四項驗收）。
     **判準跑過而無命中，與判準未跑過，必須可分辨**（22 包 §4）。
D-2  逐字轉錄入 RULINGS.md：R-VS30／R-VS31（21 包）、R-VS32（22 包）、
     R-VS33′／R-VS34（24 包）。
     並註記 R-VS33 之實作段經 R-VS33′ 取代，以 R-VS33′ 為準。
D-3  ANOMALIES.md：DR-16 標為**撤銷**（24 包 §0）；
     A-VS06′ 之關聯未驗項標為**已收**（25 包 §1.1）。

## 作業（三項，R-VS25）

W-22′ 續作（22 包 §1／§3／§5 之三項）
      (1) 立**式八：裸值** `<token>\s*[>）\]]?\s*(?:=|==|is)\s*([A-Za-z0-9_]+)`
          邊界以已知全集驗證：須抓到 `$RVC_SK_PRSNT$> = 1`；
          **不得**抓到 `$HeatedSeatFL$ = [0h: Off]`（該筆屬式一）。
          重跑八式，重算餘數與 (a)/(b)/(c)。(b) 非 0 則逐筆列出並停。
      (2) (c) 類 36 筆**逐筆人讀**，改判為 (a) 或 (b)，
          或維持 (c) 並**具名其無法判定之理由**（不得只寫「無法判定」），
          列出 token／位置／上下文節錄。
      (3) W-22(d)：式四（`!=` / `<>`）之 91 筆為**排除值**，
          於 `spec_variables.tsv` 標記極性欄（`include` / `exclude`），
          不得與正向值混列。
      **依 R-VS32**：本輪任何參數調整須測量前固定並具名；
      事後調整者該次結果作廢並重跑全量，列新舊兩組計數。

W-29  反向委派表 → docs/reports/delegation_lookup.tsv
      以本 feature 之 **237 個 Functional leaf 為列**：
        leaf_id / layer3 / delegate(yes|no|blocked) /
        comfort_leaf_ids / basis（具名依據）/ blocked_ref
      判定順序：
        1. 屬 R-VS7(b) 之 16 個 BLOCKED leaf → blocked
        2. Layer 3 於 06 輪表中有對應 → yes
        3. **自本 feature 側重掃 Comfort 037 之 498 leaf 全集**
           （不限 06 輪之 43 條）→ 有對應者 yes 並註「反向新增」
        4. 皆無 → no
      **須列出「反向新增」筆數**：為 0 才證明 06 輪之 43 條已窮盡；
      非 0 則單向表有漏，逐筆具名。

W-30  BLOCKED 16 leaf 之具名與交叉
      列出 R-VS7(b) 之 16 個 leaf id（16 引 TLM HMI Document ＋
      1 引 PDO graphics），與 06 輪對應表交叉：
        - 其中幾個同時出現在委派對應中？
        - 重疊者依 R-VS17 標 BLOCKED，或依 R-VS7(a) 委派？
      **此為條文衝突檢查**：R-VS7(b) 與 R-VS7(a) 對同一 leaf 皆適用時，
      現行條文未定優先序。**有重疊即回報，由 Pei 裁，不自行擇一。**

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
衍生檔之刪除屬 Pei；.gitignore 之修改屬 Pei。

## 升級條件

W-22′ 之 (b) 重跑後非 0 且無法化為新式；
W-29 之「反向新增」非 0；
W-30 發現 R-VS7(a)/(b) 重疊；
實測與 24／25 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
本輪無「必停」項。

## 完成後

W-17／W-24／DR-14′ 追問／`unesc()` 併 lid_parse.py 排 10 輪；
06 輪 §6-1 之 36 條「未分左右」複核排 11 輪。
DR-15 到位後即進 framework Part Vehicle Setting ＋ profile（Tier 2）。
```

---

## 4. 本包產生之新條文清單（自檢）

無新條文。W-22′／W-29／W-30 均為既有裁定之執行。
