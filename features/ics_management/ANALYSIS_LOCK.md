# ANALYSIS_LOCK — ics_management

本檔為分析層台帳之**單一寫者權杖**。規範見 `RULINGS.md` R-ICS17。

```yaml
holder: analysis-A            # 現行持有者代號
holder_session: chat-2026-08-29-ics   # 持有者之對話識別
acquired: 2026-08-29T14:05+08:00
scope:                        # 僅持有者得寫之檔
  - features/ics_management/RULINGS.md
  - features/ics_management/ANOMALIES.md
  - features/ics_management/DATA_REQUESTS.md
  - features/ics_management/framework.md
  - features/ics_management/docs/handoff/*.md
released: null
```

## 非持有者之路徑

不得直接寫上列任一檔。改寫提案於
`features/ics_management/docs/handoff/proposals/NN_<slug>.md`，
內容為「擬增之條文全文 ＋ 其量測依據」，**不自取編號**（寫 `R-ICS?`）。
持有者合併時取號、落檔、並於 `ANOMALIES.md` 記其來源。

## 交接

1. 現持有者將 `released` 填時間戳，`holder` 改 `null`。
2. 新持有者填 `holder`／`holder_session`／`acquired`，`released` 回 `null`。
3. 交接前後各跑一次 `scripts/ledger_guard.py`，兩次輸出皆入下一份上繳包。

## 撞號之事後處理

先落檔者優先（R-BLM 之撞號警語同族）。後落者改號、於 `ANOMALIES.md`
具名記錄，**不得刪除先落者之條文**（R-TM13）。
