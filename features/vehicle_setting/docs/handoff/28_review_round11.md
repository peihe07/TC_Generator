# 28 下放包 — 11 輪覆核、判準之反向驗證、12 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/09_reverse_coverage.md`。

**覆核結論：接受。** (a) = 0 —— **R-VS15 之母體 237 完整**，
這是 framework 之最後一個內部前置。

---

## 1. A-VS39 是分析層的錯，記明

27 包之 in-scope 判準只看 `Artifact Type` 與 `EE Architecture`，
**未看 `ECU` 與 `Radio`** —— 致 39 筆「缺口」中 **33 筆為假缺口**。

執行層補入後之驗證方式正確且非事後湊合：
**在已知正確集合（130 個已覆蓋條文）上全量驗證，130 / 130 成立。**

**此為 R-VS34 之形態，犯者為分析層**：以自訂之 in-scope 形態掃描，
未先確認「本專案之適用範圍由哪些屬性界定」。
27 包 §2.3 曾自陳「(b) 之可能性不低」——**實測證實，且佔 33 / 39。**

---

## 2. `$Cooled_Seats$` —— R-VS34 形態第二次，補一條可執行的防線

`4858294` 一度誤判為 (a)：以 `$Cooled_Seats$` 掃 037 命中 0，
改查 `Cooled` 任意形態才找到兩個 leaf ——
037 之描述寫 `PROXI parameter Cooled_Seats`，**非 `$...$` 形態**。

R-VS34 已立「掃描前先確認識別碼定義」，但其為**原則**；
本次需要的是**可執行之預設**：

```
R-VS36（token 比對之最小試法，分析層裁定 2026-08-20）
凡以 token 查其在某來源中之出現（覆蓋查詢、引用查詢、值域查詢），
**最小須同時試三種形態**，取聯集：

  (1) `$X$`（美元包夾）
  (2) 裸名 `X`（前後加詞界）
  (3) 描述式：`(PROXI parameter|signal|LID|parameter)\s+X`

三者命中數須分別列出。**僅試 (1) 而得 0 者，不得結論為「未出現」。**

理由：本 feature 已兩次因只試 (1) 而誤判
（`$HSW_StatFailSts$` 之值域、`$Cooled_Seats$` 之覆蓋）。
兩次皆非資料問題，皆為查法問題。
```

---

## 3. §6-1 —— **本輪最重要的未驗項，排 12 輪首位**

新 in-scope 判準（＋`ECU`＋`Radio`）**只在已覆蓋側驗過**（130/130）。

**未驗**：新判準是否把某些**本應 in-scope** 者排除掉。
執行層已具名其驗法，分析層照採：

```
W-39（判準之反向驗證，12 輪首項）
(1) 以新判準（Artifact Type ＋ EE Architecture ＋ ECU ＋ Radio）
    重掃全部 2,030 條，得新之 in-scope 數 N。
(2) **確認 251 個已覆蓋 reqid 全數仍落在 N 之內**。
    落在其外者即為「新判準排除了已知 in-scope 者」——
    **任一筆落外即為升級條件**，判準須退回。
(3) 以 N 重算 27 包 §2.1 之「全文層級未覆蓋數」（原 998，以舊判準算得）。
    **該數已失效**，須以新判準重述；其結論（非缺口）預期不變，
    但數字須正確。
(4) 21 章節內之 169／39／76.9% 亦以新判準重算並列新舊兩組。

**(2) 為本項之核心**：它是判準之範圍向（R-G9）——
只驗「該排除者被排除」不足，須驗「不該排除者未被排除」。
```

---

## 4. 其餘三項未驗之處置

| 項 | 處置 |
|---|---|
| §6-2 10 筆負向候選無掛載點 | → **W-40(1)**。依 §7，負向 TC 須掛在某 leaf 上 |
| §6-4 階數維度未複核 | → **W-40(2)**。W-34(1) 之收斂失敗有側別與階數兩維，本輪只複核側別 |
| §6-3 純交叉參照無機器判準 | **登記 A-VS41，不排作業**。其風險為「已覆蓋側可能混有純參照條文」，而已覆蓋側之條文皆有 leaf 引用，**即使為純參照亦已在母體內，不影響覆蓋結論** |

```
W-40(1) 之判準（分析層裁定；Pei 得推翻）
負向測試候選之掛載規則：
  該 exclude 值之 token **若有其他 Functional leaf 引用** →
      掛在該等 leaf 上，於其 TC 之負向分支承載
  該 token **無任何 Functional leaf 引用** →
      **不寫負向 TC**，於 `negative_test_candidates.tsv` 標
      `no_mount_point`，並登記為「規格有排除值而 037 未涵蓋」之觀察

理由：§7 之負向 TC 依附於「列舉支援項」之 TC；無 leaf 即無該 TC，
負向分支無所依附。**強行為其造一個 TC 等同擴母體**，而母體由 037 定
（R-VS15）。
```

---

## 5. 12 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/28_review_round11.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/10_criterion_and_framework.md，六節先留空。
D-2  逐字轉錄 28 包 §2 之 R-VS36 入 RULINGS.md。
D-3  ANOMALIES.md 新開 A-VS41（純交叉參照條文無機器判準；
     已覆蓋側即使混有純參照亦已在母體內，不影響覆蓋結論）。
     並依 R-VS35 列「本輪新增 N／登記簿現有 M」兩數。

## 作業（三項，R-VS25）

W-39  in-scope 判準之反向驗證（28 包 §3 全文）
      (1) 以新判準重掃 2,030 條，得新 in-scope 數 N
      (2) **確認 251 個已覆蓋 reqid 全數仍在 N 內** ——
          任一落外即升級，判準退回
      (3) 以 N 重算 27 包 §2.1 之「全文未覆蓋數」（原 998 已失效）
      (4) 21 章節內之 169／39／76.9% 以新判準重算，列新舊兩組

W-40  兩個小項
      (1) 負向候選之掛載：依 28 包 §4 之判準，逐筆標
          `mount_leaf_ids` 或 `no_mount_point`
      (2) W-38 之階數維度複核：27 個相異 Comfort leaf 中明示階數者
          （06 輪記為 1）逐條複核，判準放寬為「全文任意處含
          `\b(one|two|three|single|multi)[\s-]?(stage|level)s?\b`」

W-41  framework 草案 Layer 3（**不需等 DR-15**）
      產出 `features/vehicle_setting/framework.md` 之**草案**：
        Layer 1 = `Vehicle Setting`（R-VS3）
        Layer 2 = `Common Features` / `Heated Seat` / `Vented Seat` /
                  `Heated Steering Wheel`（R-VS4）
        Layer 3 = 037 之 SWE ID 中段 token（如 `LeftFrontHeatedSeat`、
                  `ThreeStagesVentedSeatsManagement`），逐一列出並附：
                  leaf 數 / 對應 CFTS044 章節 / 委派狀態分布
                  （yes/no/blocked 各幾）
      **僅列 Layer 1–3 表，不列個別 RD**（canon §4.1.2 步驟 5）。
      **DR-15 影響者為 Heated Seat／Vented Seat 之分支數，屬 TC 撰寫階段，
      不影響 Layer 3 之界定** —— 故本項可先行。
      草案完成後**不鎖定**，待 Pei 簽核（Tier 2）。

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
**framework 不得鎖定**（Tier 2 屬 Pei）。

## 升級條件

W-39(2)：251 個已覆蓋 reqid 有任一落在新判準之外；
W-40(2)：階數之明示數與 06 輪之 1 不符；
實測與 28 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。

## 完成後

framework 草案 → Pei 簽核（Tier 2）→ profile → 首批生成 → pilot。
DR-15 於首批生成前須有答覆，否則 Heated Seat／Vented Seat 之
分支結構無法定案（160 leaf）。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| P18 | 裁 **R-VS7(a)′**（委派句之精度；27 包 §4，建議 (a)）—— **仍未裁** |
| P19 | 12 輪產出之 **framework 草案簽核**（Tier 2） |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS36 | token 比對之最小三形態試法 | 分析層 |
| W-40(1) 之掛載規則 | 無 leaf 引用者不寫負向 TC | 分析層（Pei 得推翻） |
| W-39／W-40／W-41 | 作業 | 分析層 |
