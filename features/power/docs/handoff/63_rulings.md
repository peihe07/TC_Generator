# 63 — 60/61/62 回報覆核；四項裁示

下放包 | 分析層 → 執行層 | 往返 NN = 63

前置：`data/60_62_report.md` 已覆核，判定 **ACCEPT**。
G0 7/7、R-P371 落實、R-P373 雙向重分類正確（(c)=2 為判準之正確結果，非偏差）、
丁案試作三項自陳完整且 (iii) 未淡化、候選強度分級為 R-P368(b) 之正確落實。
寫回移至 64 包，續受 S6 阻斷。

## 0. 分析層之誤（自陳）

A-PW362 為本族第三次，且本次是**分析層自行寫數未重數**（R-P372(b) 之「11 名」）。
R-P373(c) 之「15」同型（未待重分類即預寫結果）。二處皆登。
執行層指出之缺口成立：**無任何閘在查條文所引數字與附表一致**。R-P379 補之。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P376] 丁案不全推；限「因果同錨點段落」者逐條適用，本輪為 `-057` / `-065`。
         （a）採執行層觀察：丁案為逐條例外，非機制。適用要件三項並立：
              (i) 上游事件與下游效果載於**同一錨點之同一段落**；
              (ii) 上游事件為 `$MESSAGE.Signal$`（R-P368 三段皆過或 R-P371 型逐字證據）；
              (iii) 下游效果落 R-P353 白名單
         （b）本輪符合者 `-057`、`-065`（同錨點 `CFTS009-4941504`）；
              二條依 `pattern_d_trial_61.md` 之寫法入 corpus，`test_item` 括號下半改寫為
              丁版之驗證宣告，Remarks 標 `(R-P376 丁案；原驗 RemStartFail 內部值，改驗其下游效果)`
         （c）跨段落拼接因果者一律不適用（R-P368(b) 同型風險）；其餘 12 條維持 PENDING
         （d）R-13 之代價據實入交付說明之未驗證性質：
              「該二條不覆蓋 `RemStartFail` 內部值本身」
         裁決者：分析層（Tier 2，未全推；Pei 得於站④ 否決）。
```

```
[R-P377] 候選強度：強、中撤 PENDING；弱維持 PENDING。
         （a）強（`SwitchOff_Timeout_Setting.Req` / `SwitchOffSetting.Req` → PROXI `Switch_Off_Time`）
              與中（`Rear_Camera_Enable.Info` → SR26 `Rear Camera Present` / PROXI `Rear_View_Camera`）
              依 R-P375(d) 以候選寫入，Remarks 標待上游確認，PENDING 撤除
         （b）弱（`Auto_SwitchOn_Setting.Req` → `Auto-On Comfort`）：`Comfort` 為規格原名所無之
              語意成分，屬 R-P368(b) 所禁；且即 DR-PW25 未決項。**維持 PENDING**，
              候選記入 DR-PW25 附註供上游確認，不入 TC
         （c）R-P375(b) 以 `Auto_SwitchOn_Setting.Req` 為示例之陳述**作廢**，加註；
              示例改為 `SwitchOff_Timeout_Setting.Req`
         （d）PENDING 數以 `pending_recount_62.tsv` 之「強＋中撤」情形重算，條文不預寫數字
         裁決者：分析層（Tier 2）。
```

```
[R-P378] G251「ITD 非 NA 者」期望值改為附表機讀值；R-P372 複查照做，量依附表。
         （a）G251 該項期望值 = `family_k_disposition_55.tsv` 中 class ∈ {(b),(c)} 之列數，
              本輪為 16；R-P373(c) 所寫之 15 作廢，加註
         （b）R-P372 人讀複查照做，對象 = `proxy_reachability_55.md` 無錨名扣除
              逐字含 `antitheft` 者，本輪為 45；R-P372(b) 之「11 名／40」作廢，加註；
              產出 `proxy_reachability_63.md`
         裁決者：分析層（Tier 2）。
```

```
[R-P379] 條文所引之實測數字須有機讀來源；抄錄前重算，不符即 FAIL。
         A-PW358 / A-PW360 / A-PW362 三次同族：條文引附表數字而與附表不符，
         R-P348 / R-P364 皆查不到。
         （a）條文中每一實測數字（列數、名數、對數、比例）須以
              `<數字>（<檔名>，<產生指令或欄位篩選>）` 形式書寫；無來源者不得寫數字，
              改寫「依 <檔名> 之計數」
         （b）執行層抄錄前逐一重跑該來源，不符者**不抄**，回報差異，分析層訂正後再抄
         （c）新增 G255：上繳時列出本包條文之全部數字與其重算結果，一對一
         （d）本條自 63 包起適用；前包不回溯，惟 A-PW358/360/362 三處已加註
         裁決者：分析層（Tier 2，作業規則）。
```

## H. 作業指示

1. 抄 R-P376–R-P379（依 R-P379(b) 先重算本包數字：2 條、45 名、16）；R-P372 / R-P373 / R-P375 加註
2. `-057` / `-065` 依 R-P376(b) 改寫入 corpus；`pattern_d_trial_61.md` 加標「已採」
3. 強、中候選依 R-P377(a) 寫入；PENDING 重算 → `pending_recount_63.tsv`
4. R-P372 複查 45 名 → `proxy_reachability_63.md`，驗 G252 → **停，待覆核**
5. 上繳 `features/power/docs/upstream/63_rulings.md`，附 G255 表

## I. 禁區

沿用 62 包 §I，另增列：丁案不得用於 (a) 三要件未全備之列（R-P376(c)）；弱候選不得入 TC（R-P377(b)）；無來源之數字不得入條文（R-P379(a)）。

## J. 自檢

四條。C(4,2)：R-P376×R-P377 — `RemStartFail` 非候選，丁案二條不涉候選，無交集；R-P378×R-P379 — 前者之數字皆附來源，合；餘無交集。
對既有 canon：R-P376 對 R-13 — (d) 代價明列；對 R-P374(f) — 未全推，合；R-P377 對 R-P368(b) — (b) 合；對 R-P375(b) — 改其示例，加註；R-P378 對 R-P372/373 — 訂正，加註；R-P379 對 R-P348/364 — 補其缺口。無違反。

本包數字（R-P379(a)）：2 條（`pattern_d_trial_61.md` §選擇依據）；45 名（`proxy_reachability_55.md` 無錨名 51 − 含 `antitheft` 6）；16（`family_k_disposition_55.tsv` class ∈ {(b),(c)}）。

## K. 待 Pei

無阻斷項。B5 依 R-P374(a) 續凍；PENDING 重算後若 Pei 欲裁乙，數字在 `pending_recount_63.tsv`。
