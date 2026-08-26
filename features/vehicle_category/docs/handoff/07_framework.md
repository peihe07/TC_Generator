# 下放包 07 —— Vehicle Category：Layer 2 定案 + framework 授權 + DECISIONS 簽出

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/07_framework.md`
- 前一包：`docs/handoff/06_partN_addendum.md`
- 裁定：Pei 2026-08-26 —— **Layer 2 邊界准／Test Set #5 名稱采 `Settings List`／
  DECISIONS 簽出**。三項全准，無待裁項。

---

## 〇、本包解除之前置

下放包 05 §三所設「T33 為 Tier 2，須 Pei 簽署 §二之邊界後始得執行」
之前置，**由本包解除**。T33／T34 可執行。

`DECISIONS.md` 之簽署經 Pei 授權（Tier 3），可由執行層依送簽稿寫入。

---

## 一、裁決條文（逐字抄入 `RULINGS.md`）

```
R-VC16（Layer 2 定案：8 個 Test Set）

（Pei 2026-08-26 裁定：邊界准、#5 名稱采 `Settings List`。）

Layer 1 Test Group ＝ `Vehicle Category`（R-VC1）。
Layer 2 Test Set ＝ **8 組**，其邊界以**可執行之規則**定義如下，
規則為權威，節次清單為其展開結果：

    章 2                → `Category Structure`
    章 3                → `Controls`
    章 4 / 5 / 6 / 7    → `Glove Box`
    章 11，次級節號 ≤ 6 → `Settings Behavior`
    章 11，次級節號 ≥ 7 → `Settings List`
    章 12               → `Settings List`
    章 13               → `Ignition Availability`
    章 14               → `Brake Service`
    章 16               → `Cabrio Widget`

其中「章」取 037 `HMI Source ID` 尾段章節號之首段，
「次級節號」取其第二段（`11.7.1` 之次級節號為 7）。

驗算目標（**母體標註依 R-VC15**）：

  # 1 `Category Structure`   24 leaf ／ 13 section
  # 2 `Controls`             17 leaf ／ 12 section
  # 3 `Glove Box`            12 leaf ／  8 section
  # 4 `Settings Behavior`    15 leaf ／  6 section
  # 5 `Settings List`        30 leaf ／ 17 section
  # 6 `Ignition Availability` 16 leaf ／  8 section
  # 7 `Brake Service`         2 leaf ／  1 section
  # 8 `Cabrio Widget`         1 leaf ／  1 section
  ── 合計                   117 leaf ／ 66 section

拘束五項：

(a) **Layer 3（spec section）不入工作簿**（IN §4.1.5）。不得存為任何
    欄值，不得串接進 Test Set 名稱（不寫 `Settings List 12.3`）。
    section 與 TC 之關聯由 `specification_reference` 承載（R-VC4），
    那是 traceability 欄位，不是 Layer 3 欄位。

(b) **#4 / #5 之分界（11.6｜11.7）為本 framework 唯一有二來源交叉驗證
    之邊界** —— 規格目次 ＋ 037 `Sub Categorization`（章 11 為唯一混章，
    切換次數 = 1，Service 15 ／ HMI 5）。其餘 7 個邊界僅有規格目次
    單一來源支撐。此弱點須記於 `framework.md`，不得因已簽署而略去。

(c) **#7（2 leaf）與 #8（1 leaf）之保留，非 outlier 特許**，而係
    二者皆為「待補節會使其長大」之組（#7 待 14.2 與 §15；#8 待 16.2.1
    與 16.2.2）。DR-VC3 回覆為「應補」時，此二組之邊界**須重審**：
    屆時章 8／9 之 Cabrio 本體（7 節）應另立 `Cabrio Rooftop`，
    不得併入 #8。

(d) **11.9 群（11.9／11.9.1／11.9.2／11.9.3）歸 #5**（下放包 06 §二預裁，
    以權威複本實測為據）。上開規則之「章 11，次級節號 ≥ 7」已涵蓋之，
    不需另設例外。條件性生效，待 DR-VC3。

(e) **FROP 之對應**：FROP = `Power Management` 之 16 列（**145 列母體**）
    其章別分布為 `{'13': 16}`，即全部落在 #6 `Ignition Availability`；
    FROP = `Audio Management` 之 1 列（`VC-048-02`，§12.3.2）落在 #5。
    R-VC3 表 A 據此編製。**此為成員集合之比對結果，非計數相等之推論**
    （R-VC15）。
```

---

## 二、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T40 | 抄錄 R-VC16 入 `RULINGS.md`（接 R-VC15 之後），附 byte-level diff | 1 |
| T41 | **簽出 `DECISIONS.md`** —— 以 `docs/DECISIONS_signoff_draft.md` 為內容寫入 `DECISIONS.md`。寫入前先 `list_directory` 確認現況，寫入後複驗其內容與送簽稿逐字一致。**簽署後 recon 不再覆寫該檔（A-TM15），此步不可逆，執行前再讀一次送簽稿確認無誤** | 1（Pei 已授權）|
| T42 | 寫 `features/vehicle_category/framework.md`，比照 comfort 之形制：<br>§1 三層定義與去向（含 Layer 3 不入工作簿之二禁）<br>§2 Layer 2 之 8 組表（leaf／section／節範圍／Sub Cat）<br>§3 分組判準（含 R-VC16(b) 之單一來源弱點揭露、§2.4 三個已排除替代案）<br>§4 待補節對 #7／#8 之影響（R-VC16(c)）<br>§6 逐節明細（66 節逐節列其 Test Set） | 1 |
| T43 | 產出 `data/layer3_map.tsv`（117 列：req_id、section、test_set）與 `data/test_set_map.tsv`（66 列：section、test_set、leaf 數）| 1 |
| T44 | 產出 `scripts/verify_partn.py`，至少五個 assertion：<br>(1) leaf 合計 == 117<br>(2) section 合計 == 66<br>(3) 各組之 leaf 數與 section 數與 R-VC16 之驗算目標逐組相符<br>(4) 無 leaf 落於二組或零組<br>(5) 各組之 `Sub Categorization` 為單一值<br>**分組須以 R-VC16 之規則實作，不得硬編 leaf 清單** | 1 |
| T45 | 承前包 —— **T38（R-VC15 全面覆核）如尚未完成則於本輪完成**，其結果一併上繳 | 1 |

**不在本輪範圍**：任何 TC、任何寫回工作簿、任何 git 操作、
pilot Test Set 之選定（Tier 2，見 §三）。

---

## 三、下一個里程碑

framework 落地後，Phase 3 完成，下一步為 **Phase 4 之 pilot**。

上繳包 05 §2 已建議 pilot 取 `Glove Box`（12 leaf，邊界清楚、
含完整流程〔啟用／錯誤／停用／停用錯誤〕、無待補節、
`Sub Cat` 單一值）。**分析層同意此建議**，惟 pilot 之選定屬 Tier 2，
待 framework 落地後另行提案裁定，本包不預作。

另二項在 Pei 手上、與 framework 無關：
- **同批 A 之發送**（DR-VC2 ＋ DR-VC7 ＋ A-VC2 ＋ A-VC10）
- **DR-VC3 之發送** —— 其回覆牽動 R-VC16(c)(d) 與表 B，是本 feature
  現存最大的未定量

---

## 四、上繳包要求

1. T40–T45 逐項結果，附實際指令與原始輸出
2. R-VC16 之 byte-level diff
3. **T41 之簽出前後對照**：送簽稿與簽出後 `DECISIONS.md` 之逐字一致確認
4. T44 之五個 assertion 全數 PASS 之原始輸出
5. `framework.md` 之 §2 表（供交叉核對）
6. T45（R-VC15 全面覆核）之結果表
7. 更新後之未結 DR（七筆）與 A（八筆）清單
8. 量測條件揭露（R-G8）
