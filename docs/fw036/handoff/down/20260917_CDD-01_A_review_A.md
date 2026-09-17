# CDD-01_A 審閱追補 A —— `RULINGS.sha.tsv` 併發覆寫已實現

前件：`down/20260917_CDD-01_A_review.md`（11:32 落檔，依 `up/20260917_CDD-01_A.md` 11:28 版審）。
執行層於審閱後回報：上繳包 §3／§11 之「32 → 48」實際落地為 **33 → 49**，
起點多出併行 Security session 之 `R-SEC23`；上繳包四處數字已就地更正，並於 §9.1-1 改記為「風險已實現」。
本追補只處理此事與追認，**主審閱之通過結論不變**。

## 一　事實與判定

| 項 | 值 |
|---|---|
| 主審閱所據 | 32 → 48（up 11:28 版） |
| 實際落地 | **33 → 49** |
| 差 1 之來源 | `R-SEC23`（SEC-10，commit `ce77a40`）於本包作業期間 append |
| 內容完整性 | **待執行層確認**：49 列須 = 原 32 ＋ `R-SEC23` ＋ `R-DIAG1～9` ＋ 5 amend ＋ `R-G73/74`，且 `rulings_hash.py --check` 對這 16 列逐一相符。若有任一列缺失或 sha8 不符 → 覆寫已造成資料損失，立即升級 |

判定：`[A-DIAG15]` 由「範圍不符」升為「**併發覆寫事件**」；主審閱 §三-1 之建議不變且更急 ——
**GC-16 全 repo 重生 ＋ `--check` 轉綠**，單 session、兩線暫停 append。

## 二　追認

- `VM-DIAG` 沿用既有 `Z`：**追認**（主審閱 §一 已列，判準同一不另立實作）。
- `$XXXX` 白名單 36 種：**追認**（主審閱 §一、§二 A8 已列，分析層數字錯，執行層依定義取數正確）。

## 三　commit

執行層請示是否 commit 上繳包數字更正（`b432893` 為舊數字）。
分析層建議 **准**，訊息沿用執行層所擬：
`docs(diagnostics): correct RULINGS.sha.tsv row counts in the CDD-01_A package`
`sources/MANIFEST.tsv` 之 Security 兩列不入此 commit（歸 Security 線）。
**git 為 Pei 專有，此為建議非授權。**

## 四　待 Pei（與主審閱 §三／§四合併，共四件）

1. `[A-DIAG15]` → GC-16 全 repo 重生（SEC-11 上繳後、單 session）。
2. `-157` 之 `Unsupported service requests` 視同 `Service Not Supported`（PENDING 3 → 2）。
3. 上述 commit。
4. CDD-02 pilot 範圍（主審閱 §四，12 列 → 16–20 TC ＋ R-DIAG10 Priority 判準）。
