# F1-a —— 框界送裁（前 6 條，下放包 62 §四）

> **F1 共 17 條，本包送前 6 條**（每包 5–6 條，與批次並行）。
> 其餘 11 條隨後續各包。**判準與其弱點同 `FRAME_F1.md` 之前言。**

**本批**：`R-POP1`、`R-POP5`、`R-POP6`、`R-POP8`、`R-POP11`、`R-POP14`

---

## `R-POP1` — `features/popup/RULINGS.md`（節首行 9，共 4 行）

- **建議界：前 1 個非空行為條文**｜訊號段起於第 2 個非空行｜**其後另有 2 個非訊號行**（**須人裁**）

```
    9 | Popup 立為獨立 feature，slug = `popup`。目錄 `features/popup/`，  ← **建議界**
   10 | 投遞區 `_intake/Popup/`（TitleCase，R-G24 已建妥並實測）。  ← 訊號
   11 | Feature 接手名稱「Pop-Up Queue and Priority Management」為工單稱謂；
   12 | 目錄與 slug 不帶 queue/priority 字樣（現有 037 內容見 R-POP2）。
```

---

## `R-POP5` — `features/popup/RULINGS.md`（節首行 44，共 7 行）

- **建議界：前 4 個非空行為條文**｜訊號段起於第 5 個非空行｜**其後另有 1 個非訊號行**（**須人裁**）

```
   44 | 覆蓋台帳收錄 Analysis Report 全部 7 列。Heading 2 列處置：
   45 | - SWE1-POP-002 標 `No TC — Heading; refer to child IDs -002-01..-05`
   46 | - SWE1-POP-001 標 `No TC — Heading; duplicated of SWE1-POP-002-02`
   47 |   （037 原文 K8 逐字：「Duplicated feature of SWE1-POP-002-02」）  ← **建議界**
   48 | 沿 bed_lowering R-BLM2 前例形制。  ← 訊號
   49 | 
   50 | **追認（2026-08-28，Pei「都裁過了」）**：照現裁確定，不再為 [DEFAULT]。
```

---

## `R-POP6` — `features/popup/RULINGS.md`（節首行 54，共 12 行）

- **建議界：前 2 個非空行為條文**｜訊號段起於第 3 個非空行｜**其後另有 6 個非訊號行**（**須人裁**）

```
   54 | 納入 `forms/Pop Up List HMI R1 (26PI).xlsx`（Main A1 逐字
   55 | `SR24 Post 2A CR25802`，與本 feature 規格基線同代）為 popup 素材，  ← **建議界**
   56 | **引用原位不搬**（既有共用件，sw_update A-SU3 前例；R-G27「既有檔案  ← 訊號
   57 | 不搬移」同精神）。feature.yaml `paths.popup_list` 指向之。DR-POP1 結案。
   58 | 
   59 | -002-01／-002-03／-002-05 之 TC 以該表實值填寫：選定 PU 逐字引值，
   60 | PU id 併記；PU 引文之控制記法（如 `<OK>`、`[OK, X]`）沿 IN §11
   61 | profile-scoped 例外（前例 Home A-H10）。  ← 訊號
   62 | 
   63 | 殘留兩點隨 RD-1 確認、不阻斷：
   64 | (a) CR25802（Pop Up List）vs CR22510（規格封面）之版位關係；
   65 | (b) 檔名 `(26PI)` 標記之車型／程式適用性。
```

---

## `R-POP8` — `features/popup/RULINGS.md`（節首行 78，共 9 行）

- **建議界：前 6 個非空行為條文**｜訊號段起於第 7 個非空行｜**其後另有 2 個非訊號行**（**須人裁**）

```
   78 | SWE1-POP-002-02 衍生 TC 之 specification_reference 併列兩行（升冪，
   79 | 前綴逐行重述，IN §10.7）：
   80 | `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.5`
   81 | `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.6`
   82 | 兩值皆為 037 C 欄逐字（C8／C10 起），非分析層推定之章節錨（與
   83 | bed_lowering R-BLM5 之 A-BLM4 情境不同，本 feature 不需 override）。  ← **建議界**
   84 | 其餘 leaf 單行 `_5.6`。理由：GP3 與 GP4 第 2 途徑為同一行為之兩處敘述  ← 訊號
   85 | （037 K8 之 duplicated 判定與規格對得上），該 TC 所直接驗證者含兩節
   86 | （IN §9-16）。
```

---

## `R-POP11` — `features/popup/RULINGS.md`（節首行 109，共 5 行）

- **建議界：前 2 個非空行為條文**｜訊號段起於第 3 個非空行｜**其後另有 2 個非訊號行**（**須人裁**）

```
  109 | `scripts/rulings_hash.py` 預設範圍納入 `features/*/RULINGS.md`，
  110 | 重產 `docs/fw036/RULINGS.sha.tsv`。invariant：既有 R-G 條之 sha 不得  ← **建議界**
  111 | 因本次擴範圍而變（變動即停下回報）。理由：R-G13 明定條文落各 feature  ← 訊號
  112 | 之 RULINGS.md，tsv 不涵蓋則引用制半殘。
  113 | **全域效力之工具政策，候升格 R-G。**
```

---

## `R-POP14` — `features/popup/RULINGS.md`（節首行 168，共 7 行）

- **建議界：前 1 個非空行為條文**｜訊號段起於第 2 個非空行｜**其後另有 3 個非訊號行**（**須人裁**）

```
  168 | **A-POP8** 三案採**乙案改良**：-002-05 照 GP4-4 規格原句生成，  ← **建議界**
  169 | `spec_reference` 單行 `_5.6`，**不引 PU**。理由：GP4-4 為規格自載之行為  ← 訊號
  170 | 陳述，`e.g in the search keyboard` 是規格自己的舉例，**不是向 Pop Up List  ← 訊號
  171 | 之委派**（對照 GP4-1 逐字 `timeout is defined in Pop-up List document`
  172 | 才是委派）。故不適用 R-POP6 之值引用規則，亦無須 PENDING。
  173 | 另開 **DR-POP4** 索 multi-task popup 之完整例外清單（不阻斷；
  174 | 回覆前不得自行列舉 search keyboard 以外之實例，IN §8.4.1）。  ← 訊號
```
