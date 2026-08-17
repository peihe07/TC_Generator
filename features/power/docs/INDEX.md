# Power — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案） | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-P1 ~ R-P8（該包步驟 5 未執行，於 02 包補抄） | A-PW01 ~ A-PW07（同上） | **停於步驟 2：素材台帳 7 份中 3 份雜湊不符（4 項待裁）** |
| 02 | 2026-08-17 | 素材重新定基（rebaseline） | [handoff/02_rebaseline.md](handoff/02_rebaseline.md) | [upstream/02_rebaseline.md](upstream/02_rebaseline.md) | R-P9 ~ R-P14；R-P3 撤回改立 R-P3′ | A-PW07 撤回；A-PW08 ~ A-PW11 新增 | **停於步驟 7：§E leaf 分布重算不符（62/24/16/8/3 ＋ 未歸類 1）；G6 / G12 亦不符（6 項待裁）** |

---

## 2. 現況

### 已完成

- **素材已驗明並就位。** 七份原始檔全 64 碼 SHA256 登記於
  [upstream/02_rebaseline.md](upstream/02_rebaseline.md) §二，G0 前置閘 7/7 通過；
  已複製至 `features/power/inputs/`（`.gitignore` 已含，不入版控）。
- **裁決台帳已建。** `RULINGS.md` 含 R-P1 ~ R-P14 全十四條逐字照錄
  （R-P3 標註撤回）；`ANOMALIES.md` 含 A-PW01 ~ A-PW11；
  `DATA_REQUESTS.md` 含 DR-PW1 ~ DR-PW4（PW2 / PW4 撤回）。
- **`DECISIONS.md` 之 `[AUTO]` 項已填**（§1 Intake、§2 Workbook survey、
  §3 Coverage、§4 priority rubric、§7 BLOCKED batches）。
  `[PROPOSED]` / `[PEI]` 項留空待裁。
- **可重現腳本**：`scripts/extract_textlayer.py`（文字層抽取，R-P3′）、
  `scripts/verify_gates.py`（§D 自驗 ＋ §E 重算）。皆純讀取。
- **spec_mode = D**（R-P9 / R-P3′）。CFTS009 以 `zipfile` 讀，
  CFTS010（`.doc`，OLE2）以 `textutil` 讀。

### 閃點現況（02 包 §D）

PASS：G0、G1、G2、G3、G4、G5、G5b、G7、G10
已填空（R-P11）：G8 = 904 / **196**、G9 = 148 / 92
**MISMATCH**：G6（實測 337/337，期望 336/337）、G12（SYS2 CFTS009 座標漏一列）
已移除（R-P14(b)）：G11

### 待裁 6 項（見 [upstream/02_rebaseline.md](upstream/02_rebaseline.md) §九）

- **Q1（阻斷 framework）§E leaf 分布重裁** —— 含 **主章節判定規則**
  （11 / 114 個 leaf 取決於這條從未寫下的規則）、§1.6.2.1.17 之歸屬、
  §1.8.1 實測 0 leaf 之處置
- Q2 文字層統一定義是否追認為條文（rule 1 套 plain、rule 2 套 bold）
- Q3 G6 期望值與 §C 之 SYS2 CFTS009 座標訂正（A-PW09）
- Q4 02 包 §A「七條」vs §J「六條」之訂正
- Q5 是否讀 SYS3 SYSAD（R-P3′ 後技術障礙已消失）
- Q6 是否補設閘驗證 037 `SYS2 Traceability` / `Excluded NRLs` 兩分頁

### 尚未進入

Phase 1 recon 之後續、Phase 2 以降全部未開始。
FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
