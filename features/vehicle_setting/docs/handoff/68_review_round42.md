# 68 下放包 — R-VS64（門檻不得寫死）、兩個標記之分離、43 輪

分析層寫入，2026-08-23。**交付 139／池 6。dry-run 乾淨，四錨點皆可失敗。**

---

## 1. R-VS64 —— 升級門檻不得以常數表示（本輪唯一新條文）

本輪三項不符中，**三項皆為下放包自身之數隨交付而變**：

| 門檻 | 寫死之數 | 本輪實況 |
|---|---|---|
| dry-run 之列數對照 | **129** | 139（batch18 產出後） |
| AH 欄非空 | **21** | 26（batch18 新增 5） |
| 「池不足 10（預期命中）」 | 池 16 | 未命中；括號內之預期誤把「取後之池」當「取前之池」 |

**三者皆非執行層之偏差，是我把當下之量寫成了恆定之門檻。**

```
R-VS64（分析層裁定 2026-08-23）
升級門檻與驗收條件**不得以常數表示**，須以**關係式**表示，
其兩端皆為當輪可實測之量。

  ✗ 「AH 欄非空應為 21」
  ✓ 「AH 欄非空數 ＝ delivery_disclosure.md 所載之條數」
  ✗ 「將寫入之列數與 129 之對照」
  ✓ 「將寫入之列數 ＝ generated/batch*.json 最新版之 leaf 聯集數」
  ✗ 「池不足 10」
  ✓ 「**選池前**之池 < 該輪之批次規模」（並具名其量測時點）

常數僅得用於**不隨交付而變**之量（如母體 237、Test Set 四值）。

**回溯**：現行各包之門檻須於次輪逐條檢視，凡以交付量為常數者改寫為關係式。
執行層本輪之處置（將「應為 21」讀為「＝ disclosure 所載之數」）**追認**。
```

---

## 2. 兩個標記須分離（§6-4）

`dr_dependent` 現為 **139/139**，已無區分力；
而 `delivery_disclosure.md` 之 26 條係以「畫面層 PENDING」篩出。
**兩個標記名義不同而範圍差 113 條，交付時混用即誤導。**

```
分析層裁定 2026-08-23
二標記分離，各有其義：

  dr_dependent    —— 該 TC 之**可寫性**繫於某 DR 之答覆
                     （R-VS57 之 WARN 類、R-VS61 之逐字值類）
                     其覆後須逐條複檢**訊號名與值**
  screen_pending  —— 該 TC 之**畫面層**待補（新欄）
                     （R-VS59(4)、R-VS17 之 BLOCKED）
                     其覆後須逐條補**畫面層 ER**，訊號層不動

delivery_disclosure.md 之母體改以 screen_pending = yes 篩出。
交付時二者分列，**不得以「有 N 條依賴 DR」一句涵蓋**。
```

---

## 3. A-VS141 —— 逐式列舉已第六次脫落，改判準

W-87 之適用性前言式：四式（初）→ 五式（A-VS109）→ 本輪第六式
（`Also the requirements are valid only if …`）。

**每次脫落都使 `generatable` 虛增，而修法一直是「再加一式」。**

```
分析層裁定：判準由列舉式改為結構判準（W-121）
適用性前言之判準改為：
  該條文**無可測動詞**（shall show／shall send／shall set／shall display／
  shall change／shall maintain／shall activate … —— 以已交付 139 條之
  procedure 所實際驗證之動詞為全集）
  **且** 其含條件性措辭（valid only if／applicable／applies／defines／
  covers）之任一。

驗收（R-VS54）：以已知六式之全部實例為必命中錨點；
以含可測動詞之條文（如 4858325）為必不命中錨點。
**兩側皆須有標的**，無標的者依 R-VS54(2) 不得記為通過。
```

---

## 4. pilot #4 之分層維度（A-VS142）

`dr_dependent` 43/43 皆為「有」，八格只有四格。**執行層照抽法執行並具名，正確。**

```
分析層裁定
pilot #4 之分層維度改為 batch × priority（P0／P1）——
本母體之 P0 24／P1 109 於各 batch 皆非單值。
**不重抽**：本輪已出之 15 條（必檢 8 ＋ 分層 7）維持；
其分層 7 條之代表性限制記入 pilot 之結論。
```

---

## 5. 43 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/68_review_round42.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/38_threshold_and_preamble.md，六節先留空。
D-2  逐字轉錄 68 包 §1 之 R-VS64 入 RULINGS.md。
D-3  各現行下放包之門檻逐條檢視（R-VS64 之回溯）：
     凡以交付量為常數者，列出其所在包號與條文，改寫為關係式。
     產 docs/reports/threshold_audit.md。
D-4  generated/ 各批次增 screen_pending 欄（68 包 §2）；
     delivery_disclosure.md 之母體改以 screen_pending = yes 篩出，
     列其數與 dr_dependent 之數並列對照。
D-5  ANOMALIES.md：A-VS142 依 68 包 §4 標處置；依 R-VS35 分線列兩數。D-6 照做。

## 作業（三項，R-VS25）

W-121  適用性前言之判準結構化（68 包 §3）
       (1) 自已交付 139 條之 test_procedure 抽出其實際驗證之動詞，成全集
       (2) 判準改為「無可測動詞 ∧ 含條件性措辭」
       (3) 錨點（R-VS54，兩側皆須有標的）：
             必命中 —— 已知六式之全部實例
             必不命中 —— 含可測動詞之條文（如 4858325）
       (4) 全量重跑分級，列 W0／W1／W2 與 138/2/97 之對照；
           並列因本判準而新判 B4 者之條數

W-122  A-VS141 之 leaf 處置 ＋ batch19
       (1) A-VS141 具名之 leaf 依 W-121 之新判準重判，其若判 B4
           則自 held_out 移入 W2
       (2) batch19 —— 自 W-121 後之池選取，池不足該批規模時取全部並回報
           （依 R-VS64，不寫死條數）
       套 profile ＋ 各現行條文 ＋ Sibling Rows；
       §9 十七項自檢 ＋ 值表核對 ＋ 錨點

W-123  母本備份（G3）之準備
       **不執行 cp／不動母本** —— 僅產出其指令與預期雜湊之核對表：
       (1) 母本現行之 sha256
       (2) 備份路徑之建議（REF/036_pre_writeback_YYYYMMDD.xlsx）
       (3) 備份後之核對指令
       實際備份屬 Pei（66 包 §4 步驟 0）。

## 禁區

git 不執行。**不實寫 036 母本**（三道 gate 只過一道）。
不補素材、不代擬條文、不自行調和數字。各版保留不刪。
**不得以常數表示新增之門檻**（R-VS64）。

## 升級條件

W-121(3) 之任一側無標的；
W-121(4) 之新判 B4 條數 ＞ 現行 B4 之條數；
W-122(2) 之選池前池數 < 該批規模。
```

---

## 6. 待 Pei —— **三道 gate 之二仍未過**

| gate | 現況 | 誰 |
|---|---|---|
| dry-run 通過 | ✅ 本輪過，四錨點可失敗 | — |
| **pilot #3＋#4 之 28 條覆核** | ❌ **分析層次包出建議分類** | 分析層 → Pei |
| **母本備份 ＋ sha256** | ❌ W-123 備指令，**執行屬你** | Pei |

另：**AA 欄之作者姓名**（實寫前須指定）；
**DR-25′（23）／DR-19（7）／DR-15′ 補送** —— 池 6，**下輪見底**。

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS64 | 升級門檻須以關係式表示，不得寫死交付量 | 分析層（本輪額度用畢） |
| `screen_pending` 之分離 | 與 `dr_dependent` 分列，交付揭露改以前者篩 | 分析層 |
| 前言判準結構化 | 由列舉式改「無可測動詞 ∧ 含條件性措辭」 | 分析層 |
