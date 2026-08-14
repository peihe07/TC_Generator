# 02 — Comfort HMI / R-C6・R-C7 裁決補遺

- 產出層：分析層
- 日期：2026-08-14
- 關係：補 `01_phase0_intake.md`（rev.1）之 open PENDING P-C1／P-C2
- 說明：01 之 rev.2 整份改寫於寫入時逾時未落地（實測 01 仍為 9.91 KB =
  rev.1）。改以小檔補遺，01 不再改寫。

---

## 已簽裁決條文

```
R-C6  Test Group
workbook Test Group 欄一律填 "Comfort"。

依 §4.1.1：Layer 1 Test Group 等同 spec 文件標題之模組名；spec 標題為
"Comfort HMI Logic and Flow"，故模組名為 Comfort。客戶交付路徑中之
"Climate Control Interface" 為資料夾分類，非 spec 標題，不作為 Test Group
來源。

Test Set（Layer 2）不得重複 "Comfort" 前綴（§4.2）。
```

```
R-C7  tc_id scheme
tc_id 格式為 NR1L-ComfortHMI-{NNN}，NNN 為三位零填補序號，於同一
NR1L-ComfortHMI 群組內單調遞增。

序號由 generator 指派，LLM 不得自行產生 tc_id（§10.3）。
本 scheme 自本包起凍結，生成開始後不得變更。
```

---

## 對 01 之影響

- 01 §4「Open PENDING」之 P-C1、P-C2 兩列即日關列，以本包 R-C6、R-C7 取代。
  Comfort 現無 open PENDING，Phase 3 framework 之前置裁決齊備。
- `feature.yaml` 之 `test_group` = `Comfort`；`tc_id_prefix` =
  `NR1L-ComfortHMI`。
- 執行層須將 R-C6、R-C7 原文一併貼入 `features/comfort/RULINGS.md`
  （與 01 之 R-C1～R-C5 合計七條）。

---

## 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C6 Test Group = Comfort | ✅ | 已簽 2026-08-14 |
| R-C7 tc_id = NR1L-ComfortHMI-{NNN} | ✅ | 已簽 2026-08-14 |

兩條均已以區塊形式出現，須貼入 `RULINGS.md`（R19-2）。
