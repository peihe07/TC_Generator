# 68 — 67 回報覆核；刺激擇定；第二批放行

下放包 | 分析層 → 執行層 | 往返 NN = 68

前置：`data/67_report.md` 已覆核，判定 **ACCEPT**。第一批 37/37；G245／G250 歸零；
IN §11 引號為書寫規則之自我糾正正確；`-155`/`-185` 為 R-P357(b) 型非回歸，判斷正確；
A-PW367（`VC_*` 命名空間整體不在參考檔）之「未查得非查無」判斷正確；
家族 K `Repeat … N times` 補入正確。寫回移至 69 包，續受 S6 阻斷。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P392] 刺激訊號擇定：chime 取 `PARK_INFO.ChimeActivation_LHF`；ICS 可用取觸控座標上線。
         （a）`-055` chime 刺激 = `$PARK_INFO.ChimeActivation_LHF$ = 1 (Active)`。
              依據：`CM_` 逐字「indicates the chime activation request for the left hand,
              front audio speaker」—— 明述為 chime 啟動請求且指明喇叭，接收節點 ETM/LTM；
              38 候選中唯此組（`PARK_INFO.ChimeActivation_*` 四支）之 `CM_` 同時述「request」與
              「audio speaker」，取 LHF 為代表。ER：左前喇叭有 chime 聲 (iii)
         （b）`-202` ICS 可用之觀察 = 觸螢幕後 bus 上
              `$TELEMATIC_FD_5.CM_TCH_STAT$ = 1 (TCH_PSD)` 與 `CM_TCH_X_COORD`/`CM_TCH_Y_COORD` 有值 (i)。
              依據：`4941453` Idle 列之 Display 欄逐字「DCSD sends touch coordinates」——
              **此為規格自給之該態觀察面**，非以 ICS 一詞語意擇定；`CM_` 逐字「Touch Screen Status」
              「touch screen X axis coordinates」。ICS 與 DCSD 之等同性**不認定**，Remarks 記
              「觀察面取自 4941453 Idle 列」，並入 DR-PW29 附問
         （c）`DIS_CENTERSTACK.DCSD_DISP_STAT`（SGW→ETM，遠端顯示狀態）為輸入非 HU 輸出，不取
         裁決者：分析層（Tier 2，R-P390(b)）。
```

```
[R-P393] R-P389(c) 推廣至所有未查得之規格 `$…$` 名；第二批放行；`-169` 拆分本批補做；互註追認。
         （a）凡規格 `$X$` 經 R-P368 全鏈與 R-P389(a) 六處查詢皆未查得者（本輪 `$Themed_Sound$`、
              `$VC_BODY_STYLE$`、`$Door_Ajar_Status$` 止於段 2），一律依 R-P389(c)：
              保留原名不加 `$`，`Set X = <值> (DR-PW28)`，併入 DR-PW28 附表，**不算 PENDING**
         （b）R-P391(b) 第二批**放行**，含 `-233~238`、`-228~230`、`-242/243`、`-249/250`、
              `-222/223/224` 之 `TBM_Present` 項、`-055`（依 R-P392(a)）、`-202`（依 R-P392(b)）、
              `-081`、`-186/187/191`、`-281`；`-125`／`-182` 之 `ENTER_SLEEP` 項維持 `PENDING: DR-PW26`
              但其餘欄位照改
         （c）§8.3 拆分本批補做：`-169` 三個離開條件各一（現行條為 1 分鐘支，增 FOTA dismissed 支、
              `$ACCDlyAct$` active→inactive 支，後者之 `$ACCDlyAct$` 走 R-P368／(a)）；
              `-249` 補 M240 支；`-222`/`-223` 依 `Country_Code` 分支各一；`-182` 拆二
              （30 分鐘支／下一喚醒週期支）
         （d）R-P357(b) 之 12 對 24 處互註**追認**；該項本應於 B5 施作，執行層先行補全屬合規
              （非改寫 TC 內容，不違 R-P374(a)）
         （e）`4941453` 之聯集作法與 DR-PW29 採；DR-PW28（High）、DR-PW30（Medium）核可
         裁決者：分析層（Tier 2）。
```

## H. 作業指示

1. 抄 R-P392–R-P393
2. 第二批改寫 ＋ (c) 拆分，tc_id 續號；`-055`／`-202` 依 R-P392
3. 全 corpus 重跑 G245／G246／G247／G249／G250／G251，出全表
4. PENDING 重算 → `pending_recount_68.tsv`；三代對照表更新（拆分增列）
5. 上繳 `features/power/docs/upstream/68_batch2.md`，附 G255 表

## I. 禁區

沿用 67 包 §I。ICS↔DCSD 不得寫成等同（R-P392(b)）；未查得之 `$X$` 不得寫 `$`（R-P393(a)）。

## J. 自檢

二條。R-P392×R-P393 — `-055`/`-202` 同在第二批，(b) 引 R-P392，一致。
對既有 canon：R-P392 對 R-P390(b) — `CM_` 逐字引用，合；對 R-P368(b) — (b) 明示不認定 ICS=DCSD，合。R-P393 對 R-13 — (a) 為其推廣；對 S6 — (a) 沿 R-P389(c) 之解釋，Pei 未否決前有效；對 R-P374(a) — (d) 說明不違；對 §8.3 — (c) 落實。無違反。

本包數字（R-P379(a)）：37（`67_report.md` §1）；12 對 24 處（同 §7）；拆分增列數由執行層計。

## K. 待 Pei

無阻斷項。第二批完成後即為站④ 前之全表，下一包給你看總帳。
