# 73 下放包 — R-VS67′（限縮）、錨點固定樣本、D-3 改採最弱斷言、47 輪

分析層寫入，2026-08-23。**R-VS67 之淨效果為負，本包限縮之。**

---

## 1. R-VS67′ —— 限縮（本輪唯一新條文；**Pei 得推翻**）

實測之代價：**48 leaf W0 → W2、44 條已交付 TC 之斷言失效、69 項自檢違規、池 6 → 2。**

**成因**：R-VS67(a) 令取 `Atlantis High` 欄組之 `*_Tlm`（1 bit），
而該欄組**承載不了條文之語義**（四階 `Heated_seat_off/low/medium/high`）。
**以一個 1 bit 訊號斷言四階狀態，其斷言本身不成立。**

**而 R-VS66 正是為此而立**，我於 71 包 §2 誤判「本例依 R-VS67 已無實作缺口」。
**Pei 兩輪前之原話即其正解**：「我寫成測項之後測不到，我就會開 issue 給 RD 去新增」。

```
R-VS67′（**Pei 追認 2026-08-23**，限縮 R-VS67）

訊號名、message、值域取 LID 之欄組，**依下列次序**：

(1) **`Atlantis High` 欄組**能承載該條文之語義者 → 取之
(2) **不能承載者**（其值域之基數或語義不足以表達條文所述之狀態）
    → 取**能承載之欄組**（`Atlantis`／`Atlantis & Atlantis High`），
      並依 **R-VS66(a)** 標 `impl_gap = <訊號名>`
(3) 二者皆不能承載 → `PENDING: DR-{n}`

**「能承載」之判準（可機器判定）**：
    條文所述之相異狀態數 ≤ 該欄組訊號之值域基數
    **且** 條文所用之狀態名於該值域中可對映（R-VS43／R-VS48′）

**實例**：`$FL_HS_RQ$` 等五者
    條文（`4859383` 等）述四階 `Heated_seat_off/low/medium/high`
    `Atlantis High` → `SETUP3.FL_HS_Tlm`，**1 bit 二值 → 不能承載**
    `Atlantis`      → `SETUP.FL_HS_Cmd_Tlm`，**2 bit 四階 → 取之**
    該訊號不在基線 DBC → **標 `impl_gap`，依 R-VS66(a) 照寫、開 issue 予 RD**

**連帶**：
(a) 44 條已交付 TC 之斷言**回復成立**，其 `dr15_exposed` 標記**保留**
    （DR-15′ 之答覆仍可能改變其形態）
(b) 48 leaf 由 W2 回復 W0；`generatable` 由 96 回升
(c) 該類 TC 標 `impl_gap`，**交付揭露列為「預期發現實作缺口」**
(d) **DR-25′ 維持撤回** —— 其標的（訊號不在 DBC）依 R-VS66 已非 DR 之事由，
    而是 issue-to-RD 之事由
(e) L-VS2 對 `impl_gap` 類判 **WARN**（其名有 LID 之逐字來源），不判 FAIL
```

**這是我的錯**：71 包 §2 我寫「本例依 R-VS67 已無實作缺口，(a) 不適用」——
**當時未量 `Atlantis High` 欄組能否承載四階**，即宣告其適用。
R-VS50′ 之「可及性回查」我第三次未做。

---

## 2. A-VS149 —— 錨點改用固定違規樣本（適用既有政策）

錨點以「各批之前一版」為之，其假設為「舊版較差」。
本輪 W-131 使新版變差，**9 批之錨點回報 0 而被判為「檢查已失效」**。

```
分析層裁定
`selfcheck_anchored.py` 之錨點改為**固定之刻意違規樣本**
（`tests/anchor_samples/` 之一組 JSON，逐項對應 §9 之十七檢查
 ＋ L-VS2 ＋ R-VS39 ＋ R-VS52），**不再以前一版為錨**。

理由：以前一版為錨者，其語意在「本輪使其變差」時反轉，
**而「檢查失效」與「輸入變差」在計數上不可分辨**（同 R-VS54 之立條理由）。
固定樣本之預期恆為「必命中」，不隨被檢輸入而變。

執行層本輪不改判準而具名此反轉，**正確**。
```

---

## 3. A-VS150 —— D-3 改採最弱斷言（我的指令二擇一給錯了）

72 包 §2 之 D-3 給二選項，執行層取 `check whether` 者，
**與 canon §5.5（末步驟須有驗證意圖）相衝**。

```
分析層裁定
D-3 改採**選項二**（72 包 §1 之最弱斷言）：
    procedure `3. Press … and check that an informative popup is shown`
    ER        `3. An informative popup is shown`
    AH        `BLOCKED: DR-5-B —— 彈窗之內容與樣式待 TLM HMI Document`

**彈窗之「存在」為來源逐字所載**（`shall show an informative popup`），
其可觀察性不依賴 TLM HMI Document；待補者為其**內容與樣式**。
故最弱斷言成立，`whether` 不必要，§5.5 之衝突消解。

**72 包 §2 之 D-3 給二選項本身即缺陷** —— 其一與 canon 相衝而我未察。
```

---

## 4. 三項確認

| 項 | 確認 |
|---|---|
| §2.3 D-4／D-5 之樣本 vs 母體不符 | **正常**。樣本 15 條之計數本不等於母體 143 條；方向相反亦不異常（D-4 樣本 7/15 而母體 3/143 —— 其集中於 pilot 所抽之 batch16/17）。**不調和，記為抽樣代表性之限制** |
| §2.5 D-3／D-4 未執行 | **正確**。升級條件命中即中止其後之項，本層之意旨如此 |
| W-130 四項錨點全可失敗 | **本 feature 首次四項全數可失敗**（67→0／3→0／5→0／10→0）。記明 |

---

## 5. 47 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/73_rvs67_narrowing.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/40_narrowing.md，六節先留空。
D-2  逐字轉錄 73 包 §1 之 **R-VS67′** 入 RULINGS.md；
     **R-VS67 標「經 R-VS67′ 限縮」**（原文保留）。
D-3  `INPUTS.sha256` 補 PDT24 兩檔（**18 檔**）＋ `shasum -c`（46 輪未執行）
D-4  `AA` 欄作者定為 **`PeiPYHsu`**，寫入 `writeback_036.py` 並更新 dry-run
D-5  ANOMALIES.md：A-VS148 標「依 R-VS67′ 處置」；A-VS149／A-VS150 標處置。
     依 R-VS35 分線列兩數。D-6 骨架對照照做。

## 作業（三項，R-VS25）

W-133  **依 R-VS67′ 重跑**
       (1) 實作「能承載」判準：條文之相異狀態數 ≤ 欄組值域基數 ∧ 狀態名可對映
       (2) **錨點（R-VS54，兩側皆須有標的）**：
             必命中 —— `$FL_HS_RQ$` 須判 `Atlantis High` **不能承載**，
                       改取 `Atlantis` 欄組並標 `impl_gap`
             必不命中 —— `$HeatedSeatFL$`（狀態訊號，四階）須判
                         `Atlantis High` **能承載**，不標 `impl_gap`
       (3) 全量重跑分級，列 W0／W1／W2 與 **94/2/141** 及 **138/2/97** 兩組對照
       (4) 44 條之斷言回復成立者逐條列出；`dr15_exposed` 標記**保留**
       (5) §9 全母體自檢，**69 項違規之消解數**須逐項對應

W-134  **錨點改固定樣本**（73 包 §2）
       建 `tests/anchor_samples/`，逐項對應 §9 十七檢查 ＋ L-VS2 ＋ R-VS39 ＋ R-VS52；
       `selfcheck_anchored.py` 改用之，**不再以前一版為錨**。
       **驗收**：以乾淨之最新版執行，各錨點須全數「必命中」。

W-135  **D-3 之改採最弱斷言**（73 包 §3）
       5 條彈窗類依 §3 改寫；§5.5 之 5 項違規須消解。
       **必列**：改寫後 `screen_pending` 之數、由 PENDING 升為可驗者之累計數。

## 禁區

git 不執行。**不實寫 036 母本**。不執行備份（屬 Pei）。
不補素材、不代擬條文、不自行調和數字。各版保留不刪。
**不得為消解違規而改動 §5.5 或 R-VS39 之判準。**
PDT24 兩檔不得作為取值來源。

## 升級條件

W-133(2) 之任一錨點未命中；
W-133(5) 之 69 項違規消解後仍 > 10；
W-133(3) 之 `generatable` 未回升至 130 以上。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| **1** | ~~**R-VS67′ 之追認或推翻**~~ —— **已追認（Pei 2026-08-23）** |
| 2 | **G3 母本備份 ＋ sha256**（母本 `ebe5a65f…`） |
| 3 | pilot #3＋#4 之建議分類（72 包 §4：**不通過**，七項 defect） |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| **R-VS67′** | `Atlantis High` 不能承載條文語義者，取能承載之欄組並標 `impl_gap` | **Pei（追認 2026-08-23）** |
| 錨點改固定樣本 | 前一版為錨者其語意會反轉 | 分析層 |
| D-3 改最弱斷言 | 彈窗之存在為來源逐字，可斷言；內容待補於 AH | 分析層 |
