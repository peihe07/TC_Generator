# 77 下放包 — R-VS71／R-VS72、拆分稽核、50 輪

分析層寫入，2026-08-23。Pei 裁定：**值未解不阻塞生成；未生成者留列；一次交付。**

**現況**：母本已寫入 143 列（`6d3797d4…`），**但該版不交付** ——
待四項作業完成後以全量 237 列一次寫回。

---

## 1. 三條裁決

```
R-VS71（Pei 2026-08-23）
**值之未解不阻塞生成。**

凡條文有可測之行為者，一律產 TC：
  值於 LID／DBC 有對應   → `= <raw> (<label>)`
  值無對應而來源有逐字   → `= <來源逐字值>`，**不附 raw**（R-VS61），
                            標 `dr_dependent` 或 `impl_gap`
  值於來源亦無           → 該處寫 `PENDING: DR-{n}`，**其餘步驟照寫**

**得判 W2 者僅二類**：
  (a) 條文無可測內容（適用性前言、純章節宣告）
  (b) 與他 leaf 之可測內容不可分辨（§8.2.2 禁合併，故不重複產出）

**「扣除 PENDING 後不足 2 步」之判準廢止** —— 其前提為「值未解即不可寫」，
而 R-VS61 已否定該前提。R-VS47 之 W1／W2 分界依本條重定。

理由：SWE.6 之測項依需求而立。值測不到是實作或資料之缺口，
**開 issue 或掛 DR，不是不寫**。
```

```
R-VS72（Pei 2026-08-23）
交付之工作簿須為**母體全量 237 列**，一 Functional leaf 一列（拆分者見下），
依 R-VS4 之 Test Set ＋ reqid 升冪排列。

  **已生成者**：十六欄照 66 包 §3 之對映填入
  **未生成者**：
      C／D／G／H／N 欄 **照填**（其值皆已解）
      I／J／K／L／M／P／R 欄 **留空**
      AH 欄 **必填**其阻塞類別與所待之 DR，例：
        `NOT GENERATED: B4-preamble — 條文無可測內容`
        `NOT GENERATED: B7-indistinguishable — 見 DR-27`

  **一 leaf 拆為多條者**：各條佔一列，D 欄同值，
      F 欄（Test Case ID）各自遞增，`split_flag = true`、
      `split_reason` 記其拆分軸（§10.3 之 workbook handling）。

理由：D 欄之 leaf 清單即需求追溯之骨幹。未生成而不留列者，
**「已標記之缺口」與「遺漏」在工作簿上不可分辨**。
```

```
分析層裁定 2026-08-23（拆分之現況）
143 條對 143 個 leaf，**`split_flag` 自 batch01 起無一為 true**。
canon §8.2.2 明文「RD 是需求單位、TC 是驗證單位，**二者之數不必 1:1**」，
而 §8.3 之壓力測試（「若兩個不同之部分失效皆經由本 TC 落到 fail，即為綑綁」）
**從未逐 leaf 施行**。

**應交付之 TC 總量因而未知** —— W-145 之產出方為其實測。
```

---

## 2. 50 輪指令

```text
你是 FW036 管線之執行層。repo: /Users/peihe/Work_Projects/TC_Generator
本輪為 Vehicle Setting 之第 50 輪。

**四項作業，順序不得調換** —— W-145 之結果決定 W-143 之規模，
W-142 之結果決定 W-143 之池，二者皆須先於 W-143；W-144 為最末。

## 先讀

  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md   **§7／§8.2.2／§8.3 為本輪之核心**
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/66_writeback_procedure.md  欄位對映
  features/vehicle_setting/docs/handoff/77_split_and_full.md       本輪依據

## 禁區

- git 不執行。不補素材、不代擬條文、不自行調和數字。各版保留不刪。
- **不得以 openpyxl 存檔任何 xlsx**（R-VS70）。
- **不得為使拆分數上升而拆**：拆分須通過 §8.3 之壓力測試，
  「同一控制元件之多列 ER」依 §8.2.2 **維持一條**。
- W-144 之寫回前須另備份（母本現 `6d3797d4…`）。

## 文書

D-1  依 R-VS18 建 docs/upstream/43_split_and_full.md，六節先留空。
D-2  逐字轉錄 77 包 §1 之 **R-VS71**、**R-VS72** 入 RULINGS.md；
     **R-VS47 之「扣除 PENDING 不足 2 步」段標「經 R-VS71 廢止」**（原文保留）。
D-3  依 R-VS35 分線列兩數。D-6 骨架對照照做。

## 作業

### W-145  拆分稽核（**首項**）

對 **237 個 Functional leaf** 逐一施 §8.3 之壓力測試，
產 `docs/reports/split_audit.tsv`：

    leaf_id / 現行 TC 數 / 應拆 TC 數 / 拆分軸 / 依據（§7／§8.2.2／§8.3）/ 節錄

**三類須特別檢**：
  (1) **多值列舉** —— 一條 TC 驗多個值者（如「三個有效值」）。
      判準：其任一值顯示錯即 fail，而 fail 不可分辨是哪一值 → 拆
  (2) **Decision Table** —— 條文列多列真值表者，每列為獨立之部分失效 → 每列一條
  (3) **§7 之負向配對** —— 「enumerated supported items → **ALWAYS** pair with
      at least one unsupported negative TC」。
      **列出：列舉型 leaf 之數、其現有負向 TC 之數、應補之負向 TC 數**
      （現行 `Negative / Invalid` 僅 **5** 條）

**維持一條者亦須列**（依 §8.2.2「同一控制元件之多列 ER 維持一條」），
並記其依據 —— **不得只列應拆者**。

**必列**：應拆之 leaf 數、拆後之 TC 預估總量、與現行 143 之差。

### W-142  依 R-VS71 重跑分級

  (1) 「扣除 PENDING 不足 2 步」之判準移除
  (2) W2 僅存二類：條文無可測內容／與他 leaf 不可分辨
  (3) **錨點（R-VS54，兩側皆須有標的）**：
        必命中 —— 62 包 §2 之「未解值位於後件」24 條
                  ＋「前件無已解條件」16 條 ＋ `HSW_Cmd_Tlm` 之 B6 4 條
                  **須全數由 W2 轉可寫**
        必不命中 —— B4-preamble 之 6 條 ＋ B7-indistinguishable 之 2 條
                    **須維持 W2**
  (4) 全量重跑，列 W0／W1／W2 與 **138/2/97** 之對照；`generatable` 之新數

### W-143  補寫 ＋ 拆分

  (1) 自 W-142 之池補寫未生成者
  (2) 依 W-145 之稽核拆分**既有 143 條與新寫者**；
      拆出之各條 `split_flag = true`、`split_reason` 記其軸
  (3) 套 profile ＋ 各現行條文（R-VS52／56／57／59／61／62′／67′／69／71）
      ＋ Sibling Rows ＋ 無效值優先序
  (4) §9 十七項自檢 ＋ 值表核對 ＋ R-VS54 之固定錨點（20 項）
  **必列**：新增條數、拆分條數、TC 總量

### W-144  全量寫回（**最末**）

  (1) **寫前另備份**：`REF/036_pre_fullwrite_<YYYYMMDD>.xlsx`，記其 sha256；
      **現有 `036_pre_writeback_20260823.xlsx` 不覆蓋、不改名**
  (2) 依 **R-VS70** 以 **XML 外科式**寫入（**不得用 openpyxl 存檔**）
  (3) 依 **R-VS72** 寫入**全量**：一 leaf 一列（拆分者多列），
      未生成者 C／D／G／H／N 照填、I/J/K/L/M/P/R 留空、AH 記其阻塞
  (4) **寫前後比對 raw XML**：`<dataValidation`／`x14:dataValidation`／
      `<conditionalFormatting`／分頁數／`drawing`＋`chart` 之 rel 數
      —— **任一下降即中止並還原**
  (5) 重讀逐列比對十六欄，不符即中止並還原
  (6) 實寫後 sha256 記入上繳

## 升級條件

W-145 之三類特別檢有任一類「應拆數為 0」（則該類之判準未生效）；
W-142(3) 之任一側錨點未命中；
W-143 之 §9 自檢非 0；
W-144(4) 之任一計數下降；
W-144(5) 之重讀比對不符。
```

---

## 3. 待 Pei

| # | 事項 |
|---|---|
| 1 | **本輪不交付** —— 母本現行之 143 列版待 W-144 覆寫 |
| 2 | x14 下拉之修復**移至 W-144 之後**（其寫回會再動一次母本） |
| 3 | PDT24 兩檔複製入 `inputs/`（不擋本輪） |

---

## 4. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| **R-VS71** | 值未解不阻塞生成；W2 僅二類；「不足 2 步」判準廢止 | **Pei** |
| **R-VS72** | 工作簿為母體全量 237 列；未生成者留列並於 AH 記其阻塞 | **Pei** |
| 拆分之現況 | 143:143 為 1:1，`split_flag` 從無 true；應交付量待 W-145 實測 | 分析層 |
