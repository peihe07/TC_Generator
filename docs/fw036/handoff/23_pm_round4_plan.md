# PM 第四輪修改總計畫（Pei 三裁定落實，2026-08-21）

Pei 裁定：①主詞統一 HU ②內部變數觀察途徑依內部資料（SYSAD，
對照表已落檔 `internal_var_observability.md`）③A 型與 B 型皆拆。

## 工作順序（列結構先於內容）

**第一步：拆分設計（分析層）→ Pei 核准 → 執行層套用**

- A 型（多 trigger 違 §8.3）：初篩 25 列含誤判，分析層逐列複核
  後出正式清單與 before/after 對照。確定案例：row 11（4 個
  ignition trigger → 4 TC）、row 12／23（3 個 audio source →
  各 3 TC）、row 34–37 組已是分拆形（僅 34 需再查）。
- B 型（單 trigger 多面向，Pei 裁定拆）：30 列，每一觀察面向
  一列。例 row 24（Standby 7 面向）→ 7 列。
- 預估拆後總列數 283 → **約 430–470**。

**待 Pei 裁定（拆分執行前必須定）**：
```
新列之位置與 TC ID 政策：
(a) 新分支列插於原列之後（同 Requirement 分組相鄰），
    TC ID 自尾端遞增（既有 ID 不動）——分析層建議此案
(b) 原位插入且全本 ID 重排（追溯全變，不建議）
```

**第二步：內容三項（拆分套用後執行）**

| 項 | 量（拆前計） | 方式 |
|---|---|---|
| 主詞 TLM→HU | 448 行 | 執行層機械替換＋例外表：verbatim 上半不動；
規格訊號名（`TLM_Status.Info` 已改寫者無殘留）不動；
`LTM High Radio` 等 13 行 LTM 不動 |
| 內部變數行為化 | ~130 行 | 依 `internal_var_observability.md` 逐變數句式；
設定類改 HMI 讀值／PRE 之 `HMI: "…" is set to …`；
`RemStartFail` 弱觀察列由分析層逐列，無法間接驗證者
標 `PENDING: DR-PW23` |
| `Front_Panel_OnOff.Req` | 13 行 | 改 `Press the HU power button`；登記 DR-PW24 |

**第三步：全本覆核（分析層）→ Pei 授權 → 寫回 `(Revise2)`**

## 新開 DR

- DR-PW23（Medium）：`RemStartFail` 無直接 HMI 觀察途徑，
  間接驗證不可行之列需上游提供讀取方式（診斷指令？）
- DR-PW24（Low）：`Front_Panel_OnOff.Req` 與 SYSAD 之
  `$ICSPowerButton$` 對應確認

## 本包不做

- 其餘七本（凍結中）
- lint feature-scoped（獨立包，已排）
- spec_reference（已驗證正確，拆分之新列**沿用原列全部欄值**
  含 spec_ref 與 test_item——test_item 括號下半由拆分設計
  逐列改寫以維持 sibling 可分）
