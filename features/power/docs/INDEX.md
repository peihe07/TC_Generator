# Power — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案） | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-P1 ~ R-P8（該包步驟 5 未執行，於 02 包補抄） | A-PW01 ~ A-PW07（同上） | **停於步驟 2：素材台帳 7 份中 3 份雜湊不符（4 項待裁）** |
| 02 | 2026-08-17 | 素材重新定基（rebaseline） | [handoff/02_rebaseline.md](handoff/02_rebaseline.md) | [upstream/02_rebaseline.md](upstream/02_rebaseline.md) | R-P9 ~ R-P14；R-P3 撤回改立 R-P3′ | A-PW07 撤回；A-PW08 ~ A-PW11 | **停於步驟 7：§E leaf 分布重算不符；G6 / G12 亦不符（6 項待裁）** |
| 03 | 2026-08-17 | framework 定版所需輸入（B1/B2/B3 ＋ 四道補閘） | [handoff/03_framework_inputs.md](handoff/03_framework_inputs.md) | [upstream/03_framework_inputs.md](upstream/03_framework_inputs.md) | R-P15 ~ R-P23 | A-PW12 ~ A-PW16；A-PW03/04/05 複驗 | **PASS —— 十一步全完成，§D 十八項無 MISMATCH（8 項待裁）** |

---

## 2. 現況

### 已完成

- **素材已驗明並就位**（G0 = 7/7）。原始檔七份全 64 碼 SHA256 見
  [upstream/02_rebaseline.md](upstream/02_rebaseline.md) §二；
  衍生物（含 SYS3）與 R-P23 之（d）欄 OS／工具版本見
  [upstream/03_framework_inputs.md](upstream/03_framework_inputs.md) §二。
- **裁決台帳**：`RULINGS.md` 含 **R-P1 ~ R-P23** 全二十三條逐字照錄
  （R-P3 標註撤回，改立 R-P3′）。
  `ANOMALIES.md` 含 **A-PW01 ~ A-PW16**（A-PW07 撤回）。
  `DATA_REQUESTS.md` 含 DR-PW1 ~ DR-PW4（PW2 / PW4 撤回）。
- **spec_mode = D**（R-P3′）。文字層定義已由 **R-P17** 追認為條文。
- **B1 / B2 / B3 三項 framework 定版輸入齊備**：
  `data/multi_chapter_leaves.md`（11 條，無建議歸屬）、
  B2 素材（見 03 上繳包 §七）、`data/sys3_chapters.md`（47 heading）。
- **可重現腳本**（皆純讀取）：`scripts/extract_textlayer.py`、
  `scripts/build_b1.py`、`scripts/verify_gates_03.py`（§D 全表）、
  `scripts/verify_gates.py`（02 包版，含 §E 重算段）。

### 閃點現況（03 包 §D，18 項）

PASS：G0、G1、G2、G3、G4、G5、G5b、G7、G8（904/**196**）、G9（148/92）、
G10、G12、G13
已填空：G6a = **337/338**、G6b = 列層 **336/337** ／ token 層 438/439、
G14 = 丟棄 10 章／**未覆蓋 9 章**、G15、G16 = **0**（SYS3 無字面章節號）
已移除：G11（R-P14(b)）、G6（R-P18 拆為 G6a/G6b）

**無 MISMATCH。**

### framework 狀態

**§E 待定版**（標題已由「已定版」改為「待定版」，見
[handoff/01_intake.md](handoff/01_intake.md) §E）。
leaf 分布數字 64/24/16/7/3 未動。實測差額已完整閉合 ——
**全部來自 `SWE-PM-008` 與 `SWE-PM-057` 兩顆 leaf**（03 上繳包 §五）。
`§1.8.1` 依 R-P16 刪除，**惟前提待複核**（A-PW14）。

### 待裁 8 項（見 [upstream/03_framework_inputs.md](upstream/03_framework_inputs.md) §十一）

- **Q1（阻斷 framework）11 條跨章節 leaf 之歸屬**（R-P15(b)）——
  實務上僅 `SWE-PM-008`、`SWE-PM-057` 兩條改變分布
- Q2 `SWE-PM-057` 裁定後 R-P16 是否撤回（A-PW14）
- Q3 A-PW05 描述訂正、A-PW03 加註分類不實
- **Q4 A-PW16 之 9 個未覆蓋章節如何處置**（直接決定 Layer 3 是否完整）
- Q5 一個 leaf 是否得對應多個 Layer 3 章節（現行結構不支援）
- Q6 是否量測章節層反向缺口（288 章中僅 46 章被觸及）
- Q7 A-PW06 是否補驗（分批規劃即將用到）
- Q8 04 包是否安排 SYS3 §4.x 與 §E 之交叉比對（R-P20 之後半）

### 尚未進入

Phase 4 以降全部未開始。FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
