# CDD-01_A 審閱追補 B —— 覆寫為兩次；工作區修復以 HEAD 合併；commit 建議

前件：`_review.md`、`_review_A.md`。執行層完成追補 A §一之完整性確認並回報事件實為兩次。

## 一　完整性確認：通過，無資料損失，不升級

50 = 原 32 ＋ Security 2（`R-SEC23`、`R-SEC22(a)`）＋ DIAG 16；缺失／多出／重複 0／0／0；
18 列對現行條文 sha8／body_sha8／sha256／source 全數相符；原 32 列無變動。

## 二　事件重判：兩次覆寫，第二次發生於 commit 之後

| 次 | 時點 | 結果 |
|---|---|---|
| 1 | T3 落檔後、`b432893` 前 | DIAG 16 列消失 → 執行層重 append → 提交 |
| 2 | `b432893` 後 | 工作區再度 34 列、DIAG 0 列（Security 加了 `R-SEC22(a)`）|

HEAD 完好，損失只在工作區；但 Security 線若以該工作區狀態提交此檔，16 列即從 HEAD 消失。
執行層之修復方式正確：**以 HEAD 為底併入工作區獨有列**（不是再 append，那會反丟對方的 `R-SEC22(a)`），現 50 列。

`[A-DIAG15]` 再升一級：「提交不終止爭用」。

## 三　過渡規則（GC-16 落地前即刻生效；寫入 CDD-02 §0 與 Security 線下一包 §0）

```text
R-G{live}  RULINGS.sha.tsv 之併發寫入過渡規則（GC-16 前）
  (a) 任何 session 動 `docs/fw036/RULINGS.sha.tsv` 前，先 `git diff HEAD -- docs/fw036/RULINGS.sha.tsv`；
      工作區與 HEAD 不一致者，以 HEAD 為底合併工作區獨有列後再寫，不得逕自 append 或覆寫。
  (b) 寫後立即以 ruling_id 集合比對：HEAD ∪ 工作區獨有 ∪ 本次新增 = 寫後內容，缺一即回報。
  (c) 上繳包記寫前／寫後／HEAD 三個列數。
  (d) 本規則於 GC-16（全 repo 重生 ＋ 單一維護者）落地後廢止。
```

取號期望 `R-G75`（執行層現查）；落 `RULINGS_LEDGER.md` 由 CDD-02 之 T0 執行。

## 四　commit

建議 **准**，訊息沿執行層所擬：
`docs(diagnostics): correct CDD-01_A row counts and repair RULINGS.sha.tsv overwrite`
四檔中 `sources/MANIFEST.tsv` 之 Security 兩列不入。git 為 Pei 專有，此為建議。

## 五　追認

`[A-DIAG17]`／`[A-DIAG14]` 已登為已追認，收。

## 六　依 Pei 2026-09-17 常規（審閱後即發下一包，不待准），CDD-02 隨本追補同時落檔

以主審閱 §三／§四 ＋ 本追補 §三 為依據；Pei 不同意之處於 CDD-02 上繳後撤回。
