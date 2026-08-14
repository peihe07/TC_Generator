# 06 — Comfort HMI / 單一 spec 來源 ＋ 適用性判讀指示

- 產出層：分析層
- 日期：2026-08-14
- 對象：執行層
- 裁定：Pei，2026-08-14（來源重複之處置，選項 1）

---

## 1. 已簽裁決條文

```
R-C11  spec 來源之單一性

Comfort 之 SR24 SYS1 export 只保留一份，位於
spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_
CR24879_(September_25_2023).xlsx。

features/comfort/inputs/ 下之同名副本刪除。feature.yaml 維持以
../../spec-index/… 全名相對路徑回指，不改為 inputs/。

理由：R-C1 之遵守目前靠「feature.yaml 寫全名指向唯一檔案」達成機械強制
（上繳 01 §2）。同一基線存在兩份副本時，該強制降級為「目前取對」——
兩份副本一旦分歧，無任何機制會報錯。

推廣：spec 素材一律留在 spec-index/，不複製進 feature 之 inputs/。
inputs/ 只放該 feature 專屬且不屬 spec-index 管轄者（037、036 範本、
CFTS 等引用文件）。
```

刪除為不可逆操作，已由 Pei 裁定（2026-08-14，「1」）。執行層執行並於
`ANOMALIES.md` 登記 `A-CF10`：inputs/ 曾存在 SR24 export 副本
（70,040 bytes，與 spec-index 同大小），依 R-C11 移除，記錄其曾存在之事實。

刪除前確認 `spec-index/cache/` 該份仍在且為 70,040 bytes；不確認即不刪。

---

## 2. 素材落位實測（2026-08-14）

`features/comfort/inputs/`：

| 檔案 | bytes | 對來源 |
|---|---|---|
| `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx` | 143,292 | 一致 |
| `FM-WI-FSM-036-A01 …_SWQT_20260121.xlsx` | 65,821 | 範本，rev C |
| `SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx` | 914,043 | 一致 |
| `R1LR_Atl-H_25PI3.5_Cabin_CFTS_043 HVAC Controls and Displays _SR26_20250909-1852.doc` | 2,469,376 | 一致 |
| ~~`SYS1_HMI_Comfort_…SR24_…(September_25_2023).xlsx`~~ | 70,040 | 依 R-C11 刪除 |

CFTS043 之 release 為 25PI3.5，與既有 feature 基線一致。

---

## 3. 適用性判讀（執行 handoff 05 §5）

對 17 節 `substantive` 產出
`features/comfort/data/sr24_substantive_applicability.tsv`，欄位：
`outline`｜`scope_verdict`｜`basis`｜`variant_condition`。

`scope_verdict` 三值：`in_scope` / `out_of_scope` / `undetermined`。

判定依據逐節具名，不得以形態推論代替：

| 節 | 依據 |
|---|---|
| 20.1 ~ 20.4.3（10 節） | CFTS043。優先 `SYS1_CFTS043-…Tree view_R1L-R scope.xlsx`；其未涵蓋者查 CFTS043 主檔 `.doc` |
| 19.1 ~ 19.3（7"）、18.2 ~ 18.4（10.25"） | 螢幕尺寸對 R1LR ATL-H 機種配置之適用性。**「spec 有寫」不等於在範圍內** |
| 16.1（EMEA ICS CARRYOVER） | 市場適用性 |

`undetermined` 為合法且鼓勵之結論：判不出來即標 `undetermined`，並於
`basis` 具名缺何素材，勝於填一個看起來完整的判定。缺料者同時開
`DATA_REQUESTS.md` 列（file-supply gap 須同時建 ANOMALIES 與
DATA_REQUESTS，standing rule）。

`.doc` 為 OLE 舊格式，非 OOXML；若解析工具不足，此為工具缺口，登
`ANOMALIES.md` 與 `DATA_REQUESTS.md`，不得以「讀不到所以判 out_of_scope」
代替 —— 讀不到即 `undetermined`。

**本項為量測，非處置。** 不得產 TC、不得入 coverage 分母、不得列 BLOCKED、
不得補 RD 項目、不得改 R-C5 或 R-C5-1。

---

## 4. 其他作業（延續 handoff 05 §6）

1. R-C5-1、R-C11 原文貼入 `RULINGS.md`。
2. A-CF08 更新（16 節退出 R-C5）；A-CF09 範圍限縮為實測之空白範本清單；
   新登 A-CF10。
3. `DECISIONS.md` 仍不簽署（Tier 2）。第 6／10 項之調整建議見 05 §4。
4. Phase 3 不開始。
5. 上繳 `docs/upstream/03_applicability.md`，附「本包是否仍有該驗而未驗者」
   之獨立判斷，並更新 `docs/INDEX.md`。
6. git 不執行，只準備 commit message。

---

## 5. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C11 spec 來源之單一性 | ✅ §1 | 已簽 2026-08-14 |

R-C11 須貼入 `features/comfort/RULINGS.md`。其推廣段（spec 素材一律留在
spec-index/）適用全 feature，安置位置於下次 canon re-sync 時處理。
