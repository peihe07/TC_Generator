# 13 下放包 — 04 輪啟動指令（取代 08）

分析層寫入，2026-08-20。`08_round03_prompt.md` 標為 SUPERSEDED：
其作業清單已完成 W-19／W-20／W-16′／W-21，且順序依 R-VS21 重排。

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/12_post_commit.md    本輪依據
  features/vehicle_setting/docs/handoff/09_review_round03.md  W-22/W-23 之規格
00～08、10、11 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 第一件事：開上繳包（R-VS18）

建立 docs/upstream/03_crosscheck_and_overlap.md，寫入標題、本輪作業清單、
與 canon §8.2 之六個空節，各節先留空；其後每完成一項當下填入。
reports/ 為附件不是替代。

## W-25（唯讀查證，不佔作業順位，與開包同時做）

  git ls-files features/vehicle_setting/ | wc -l
  git ls-files features/vehicle_setting/ | head -40
  git log --oneline -- features/vehicle_setting | head -10

判定並**兩種結果都回報**：
 (a) vehicle_setting 之多數檔案早已被追蹤
     → 分析層 07／09 包之「三輪產物不在版控」為誤，上繳明記更正，
       並登記 A-VS25（分析層以推測代替實測）
 (b) 確實只有 2c6c9b3 之 7 檔被追蹤
     → 則 git add 未如預期（pathspec 有列 docs/ 與 data/），須追因
**不得只回報符合預期者。**

## 附錄 A 之入庫（R-VS24，窄口授權，一次性）

得執行 git add / git commit，pathspec 限
    features/vehicle_setting/docs/upstream/02_variables_and_sweep.md
（W-25 結果若寫入該檔一併帶入）
訊息：docs(vehicle_setting): round 02 upstream appendix A — commit record

不得執行：push／amend／rebase／reset／restore／checkout／branch／tag／
          stash／clean／merge／cherry-pick／rm／mv
本授權於該 commit 完成後失效。**推送屬 Pei，不做。**

阻斷判準（R-VS23）：**暫存區**出現 pathspec 以外之路徑即停；
工作區存在他 feature（time_management）之在途變更則列出並續行。

## 作業（順序即優先序，依 R-VS21 不得於頭部插入新項）

W-15b′ DBC ↔ LID 表逐屬性交叉 → data/can_signal_map.tsv
       對本 feature 所用之 message／signal，比對 signal 名／message 名／
       CAN id／起始位元／長度／factor／offset／VAL_ 值表。
       通過條件寫成「與參照對象在**所有可讀屬性**上一致」，
       不寫成「已知的幾項正確」（§5a 條 14）。
       收 W-8 盲區 3：橋接依賴 LID 表，其若錯則三來源一致地錯。

W-17   LID 列數差 6 之追因（2,626／446 vs 2,629／449）；
       TRUNCATED_ENUM 之其他形態（現僅偵測 `# = Not Used` 結尾）。

W-9    Comfort 逐條對照 → docs/reports/comfort_overlap.md
       **本 feature 側母體為 237 個 Functional leaf，非 271**
       逐條列出命中座椅加熱／通風／方向盤加熱之 Comfort leaf
       （SWE1-HVAC-*）與其對應之本 feature leaf，作為 R-VS7 委派句之
       來源表。另附 CFTS044 內文以 {CFTS043} 引用 Comfort 之 3 處上下文。
       **必停已由 R-VS7 解除**，做完併入本輪上繳。

W-22   餘數驗證 → data/value_extraction_residual.tsv
       逐 token 取其在 CFTS044 之全部出現位置，減去三式已命中者，
       逐筆檢視餘數上下文（前後 200 字元），分類為
         (a) 敘述性提及不帶值域
         (b) 帶值域但記法為三式所不涵蓋  ← 第四式之證據
         (c) 無法判定
       通過條件：**(b) 為 0**，或 (b) 全數化為新式並重跑。
       **不得以「餘數看起來都是敘述」收尾** —— 須逐筆分類並附計數。
       已知：式一 451／式二 45／式三 34 命中。

W-23   歸因判準化：將 02 上繳 §2.2 之五類寫成可機器判定之規則
       （C1 別名切分／C2 LID 列粒度／C3 Format 解析殘缺／
         C4 規格引用子集／C5 縮寫 vs 全名），套用於 W-19 之 39 項輸出。
       只有不落入 C1–C5 者進待判清單；每輪列 C1–C5 計數證明判準運作，
       不逐筆展開。**C3 為我方缺陷，判準化同時修正解析式**，
       不得長期以分類遮蓋。

W-24   `IGN_OFF` 之兩處條文（充電排程送 SDP server、charge end time 比較）
       是否落在 237 個 Functional leaf 內。小項。

W-26   改寫 A-VS19 措辭：由「誤建目錄待刪」改為
       「new_feature.py 之名稱正規化缺陷（feature.lower() 不轉空白）會
         產生含空白之目錄名；本 feature 未落地，無待刪標的。工具缺陷
         維持登記，不在本 feature 修。」
       依據：find 無輸出、git ls-files did not match（P1 已關閉）。

## 禁區

除 R-VS24 之窄口外，git 寫入性操作一律不執行。
不補素材、不代擬條文、不自行調和數字。
.gitignore 之進一步修改屬 Pei。

## 升級條件

W-15b′ 出現 LID 表與 DBC 之屬性矛盾；
W-22 之 (b) 類非 0 且無法化為新式；
實測與 09／12 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
**本輪無「必停」項。**

## 待裁而未裁（不得預設答案）

R-VS18／R-VS19（P11）、R-VS20／R-VS21（P12）、R-VS23／R-VS24（P13）。
本輪依現行草案作業，遇需其定案之判斷 → 登記待判，繼續其他作業。
**R-VS20 為唯一會擋路者**：`$HSW_StatFailSts$` 這類 in-scope 無值域之
token，於 W-22 產出後若需定案值域即會卡住。

## 完成後

下一步為 framework Part Vehicle Setting ＋ profile（Tier 2），
再首批生成，再 pilot。**本輪不做這三項。**
```
