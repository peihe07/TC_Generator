# 58 — 內部訊號解析改走 forms/（LID → DBC 三段鏈）

下放包 | 分析層 → 執行層 | 往返 NN = 58

前置：Pei 2026-08-30 口頭裁定，逐字：
「power PENDING的訊號實際名稱以/Users/peihe/Work_Projects/TC_Generator/forms為主 名稱不一定會完全一樣要看DBC實際名稱」。
57 包 §E「寫回移至 58 包」由本包取代，寫回移至 59 包。

## 0. 分析層之誤（自陳）

57 包 R-P365(b) 把 `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` 定為 power 之判準 DBC，
**未查 `forms/`**。`forms/FORMS.md` 自 R-G1（08-17）起即為全案參考資料庫，
`LOOKUP_MISSES.md` B-1 更明載 R4 BHCAN 與 forms 之 BHCAN2 **非版次關係**
（僅 R4 有 573、僅 BHCAN2 有 32）—— 分析層在 57 包把非權威檔納入台帳，
且 B4 之「DBC 對照 0/13」是以**規格原名直查 DBC**，跳過 LID，
在 R-DM17 三段鏈上只做了段 3，**故 0/13 不是查無，是未查**（R-G13）。
兩項皆登 A-PW。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P368] 內部訊號之實際名稱以 forms/ 為主，依三段鏈解析；DBC 實名勝規格原名。
         （a）解析鏈（R-DM17 / R-DM21 之全案慣例）：
              段 1  規格原名（`X.Info` / `X.Req` / `$X$` / 素材原文）
                    → `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`
                    之 `CAN Mapping` 分頁，`Atlantis High` 欄組 `Signal Name`
              段 2  → `MESSAGE.Signal`
              段 3  → `forms/PDT27_E2A_R1_BHCAN2.dbc` / `forms/PDT27_E2A_R1_FDCAN8.dbc`
                    之 `SG_` 逐字查得
              三段皆過者，TC 寫 `$MESSAGE.Signal$`（DBC 實名，含大小寫），
              規格原名保留於 `test_item` 上半 verbatim（R-6 不變）
         （b）**名稱不必逐字相同**：段 1 之比對得用 LID 之 `Logical Identifier`
              欄與 `Description` 欄，容許前綴／後綴／底線差異；
              惟每一對應須於附表載明比對依據（哪一欄、哪一列），不得憑語意跳接
         （c）PROXI 參數同理：段 1 → LID `Proxi & Configuration` → 段 3
              `forms/PROXI_HDCC27_R3_20250424.xlsx` `Format` 分頁 `Parameter Name`
         （d）止於段 1 或段 2 者，記「未解得（止於段 n）」；
              段 3 查無者始得記「查無」，且須滿足 R-G13 三要件並登
              `forms/LOOKUP_MISSES.md`（R-G14），同時 ANOMALIES + DR 三處各登
         （e）R4 BHCAN（`features/vehicle_setting/inputs/`）降為**旁證**：
              段 3 在 forms 二本查無而在 R4 查得者，**不得逕用 R4 名**，
              記為 B-1 型衝突，列 §K 交 Pei
         （f）R-13 續有效：三段鏈全程查無者，TC 保留規格原名不加 `$`，
              `PENDING: DR-PW23 <名>` 不變
         R-P355(b) 之「已有 DBC 對照者」自此指本條 (a) 三段皆過者。
         R-P365(b) 之台帳 DBC 改為 forms 三檔（LID、BHCAN2、FDCAN8，SHA 取自 FORMS.md），
         R4 BHCAN 另列「旁證，DR-PW21 歷史來源」；R-P365 依 R-P36 原文不改，加註。
         裁決者 Pei，逐字依據：「以…forms為主 名稱不一定會完全一樣要看DBC實際名稱」。
```

```
[R-P369] B4 附表重做；`ENTER_<STATE>` 之訊號同受 R-P368 複驗。
         （a）`data/dr_pw23_internal_signals_55.md` 之 13 名依 R-P368 逐名重解，
              附表改為：`規格原名 | 段1 LID 列與欄 | 段2 MESSAGE.Signal | 段3 DBC 檔 | 結果`
              結果 ∈ {解得, 未解得(止於段1), 未解得(止於段2), 查無(R-G13), B-1 衝突}
         （b）素材拼法不一致者（`Phone_Call.Info`/`PhoneCall.Info` 等）
              二名皆入段 1 查，若解至同一 `MESSAGE.Signal` 則為同物，TC 用 DBC 實名，
              二拼法之等同記入附表；解至不同者維持 DR-PW23 詢問
         （c）`ENTER_<STATE>` 六可用片段所用之 `$STATUS_BH_BCM1.OperationalModeSts$`、
              `$STATUS_TELEMATIC.PowerSts_Telematic$` 及 `VAL_`，**改以 forms 之 BHCAN2 複驗**；
              R4 有而 BHCAN2 無者即 B-1 衝突，該片段轉 PENDING 並列 §K
         （d）57 包定量「105 條 PENDING」作廢，待 (a) 重做後重算
         裁決者：分析層（Tier 2，落實 R-P368）。
```

## B. 本包須產出

- B4′：附表重做（R-P369(a)(b)），落 `data/dr_pw23_internal_signals_58.md`，舊檔保留加標「已由 58 取代」
- B2″：片段表訊號複驗（R-P369(c)），更新 `data/enter_state_55.md`
- G0 台帳：改列 forms 三檔 SHA（FORMS.md 所載）＋ R4 旁證
- `forms/LOOKUP_MISSES.md`：段 3 查無者依 R-G13 登 M-n（先讀現有 M-1~M-3，勿重複）
- PENDING 重算：`C3 111 → 依 R-P354 可解 / 依 R-P368 解得 / 仍 PENDING` 三分

## D. 閃點

| # | 項目 | 期望值 |
|---|---|---|
| G0 | 台帳 | forms 三檔 SHA 與 FORMS.md 一致；R4 列旁證 |
| G253（新） | B4′ 附表 | 13 名全有段 1–3 記錄；「查無」者皆有 M-n 與 DR 號；無「止於段 1/2」而標查無者 |
| G254（新） | 片段訊號複驗 | 六片段之每一 `$…$` 在 BHCAN2/FDCAN8 有 `SG_`；B-1 衝突數回報 |
| G247 | 依 R-P369(d) 重算 | PENDING 數回報，三分表 |

## F. Anomaly 異動（自現行最大號起，先查）

- 新增：分析層 57 包以 R4 BHCAN 為判準 DBC，未查 forms/ 與 LOOKUP_MISSES B-1
- 新增：B4 以規格原名直查 DBC，跳過 LID 段 1–2，「0/13」為未查非查無（R-G13）

## G. DATA_REQUESTS

DR-PW23 附表待重做；DR-PW26 不變。段 3 查無者之 DR 依 R-G14 與 M-n 並登。

## H. 作業指示

1. 讀 `forms/FORMS.md` 參考資料庫節與 `LOOKUP_MISSES.md` 全文
2. 抄 R-P368–R-P369；R-P355 / R-P365 加註；§F 入 ANOMALIES.md
3. G0 台帳改列
4. B4′ 重做，驗 G253
5. B2″ 複驗，驗 G254
6. PENDING 重算回報
7. 上繳 `features/power/docs/upstream/58_forms_resolution.md`

## I. 禁區

沿用 57 包 §I，另增列：
- 不得以規格原名直查 DBC 而稱「查無」（R-P368(d)）
- 不得逕用 R4 BHCAN 之訊號名（R-P368(e)）
- 不得憑語意將規格名接到 LID 列而不載明欄／列（R-P368(b)）

## J. 自檢

二條，二個頂層 fenced block，§H 第 2 步二條，一致。
R-P368×R-P369：後者為前者之施作，同解。
**對既有 canon（R-P364(d)）**：R-P368 對 R-6（verbatim 保留原文）— 合；對 R-13（查無保留原名）— (f) 合；對 R-1 v3 (a)(d) — 合，(a) 為其解析程序；對 R-G13/R-G14 — (d) 合；對 R-DM17/R-DM21 — 採其三段鏈；對 R-P355(b) — 重定義「已有 DBC 對照」，加註處理；對 R-P365(b) — 訂正，加註處理。無違反。

## K. 待 Pei 裁

- B-1 型衝突（forms 查無、R4 查得）出現時之處置 —— 目前為「列出交你」，數量待 G254 回報後再裁
