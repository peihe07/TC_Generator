# 61 — K-2 預設甲；授權丁案試作一條

下放包 | 分析層 → 執行層 | 往返 NN = 61

前置：60 包 §K-2 之四選項，Pei 2026-08-30 未裁，逐字依據：「一定要我裁嗎？」→「是請落」。
分析層依 S6 之預設與 Tier 2 權限處置如下。寫回移至 62 包，仍受 S6 阻斷。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P374] K-2 不裁即甲；乙／丙仍為 Pei 專屬；丁授權試作一條，不推廣。
         （a）S6 之預設 = 甲：含 `PENDING: DR-PW23` 之 102 條不出貨，等上游回覆。
              本條不改 S6，不開例外
         （b）乙（帶 PENDING 分段出貨）與丙（降轉 NA）為 S6 明文之 Pei 專屬事項，
              分析層不觸、執行層不觸；Pei 未開口即不存在
         （c）丁案試作：執行層以 `RemStartFail` 為對象，選其所涉 TC 中**一條**
              （選擇依據：`test_item` 上半含 `RemStartFail` 且 CFTS009 對其
              上游事件與下游效果**皆有明文**者；查無明文者不選、不造），
              產出並列版：
                左：現行版（含 `PENDING: DR-PW23 RemStartFail`）
                右：丁版 —— Procedure 改驅動 CFTS 所載使 `RemStartFail` 變化之
                    上游 CAN 事件（`$MESSAGE.Signal$`，走 R-P368 三段鏈），
                    ER 改觀察 CFTS 所載之下游效果（R-P353 白名單四類），
                    `RemStartFail` 自 Procedure / ER 移除，僅留 `test_item` 上半 verbatim；
                    每一步附其 CFTS ObjectID
              落 `data/pattern_d_trial_61.md`，附 reasoning（繁中，§10.4 四項）
         （d）試作**不入 corpus、不入 batch、不計 G 閘**；僅供 Pei 站④ 目視
         （e）試作後執行層自陳三項：上游事件是否 CFTS 逐字、下游效果是否白名單、
              與原版相比驗證對象是否改變（R-13 之慮），逐項答是／否並引段落
         （f）推廣與否由 Pei 裁；未裁前其餘 101 條維持 PENDING
         裁決者：分析層（Tier 2）；(a)(b) 為 S6 之重述，非新裁。
```

## H. 作業指示

1. 抄 R-P374
2. 續 60 包 §H 第 2–4 步（`enter_state_55.md` 更新、`family_k_disposition_55.tsv` 更新、R-P372 人讀複查）→ 第 4 步後停，待覆核
3. R-P374(c) 試作 → `data/pattern_d_trial_61.md`
4. 上繳 `features/power/docs/upstream/61_pattern_d_trial.md`（含 60 包產出）
5. B5 續凍

## I. 禁區

沿用 60 包 §I，另增列：
- 試作不得入 corpus（R-P374(d)）
- 上游事件／下游效果查無 CFTS 明文者不得造（R-P374(c)）
- 不得對第二條 TC 施作丁案（R-P374(f)）

## J. 自檢

一條，一個頂層 block。對既有 canon：S6 — (a)(b) 重述不改；R-13 — (e) 明列自陳；R-P353 / R-P368 — (c) 引為判準；R-P200(a) — 60 包不改。無違反。

## K. 待 Pei

無阻斷項。試作出來後，Pei 得裁「丁全推」或「乙」；不開口即甲。
