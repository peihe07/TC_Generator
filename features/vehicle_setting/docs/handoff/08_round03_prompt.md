# 08 下放包 — 03 輪啟動指令（取代 06）

分析層寫入，2026-08-20。`06_round02_prompt.md` 標為 SUPERSEDED：
其作業清單已完成 W-8／W-13，且上繳次序依 R-VS18 改變。

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文（已落檔）
  features/vehicle_setting/docs/handoff/07_review_round02.md 本輪依據
  features/vehicle_setting/docs/handoff/05_rulings.md        R-VS7~R-VS17 全文
00～06 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 第一件事：開上繳包（R-VS18）

**開工第一個動作**，不是最後：
建立 docs/upstream/02_variables_and_sweep.md，寫入標題、本輪作業清單、
與 canon §8.2 之六個空節（預期 vs 實測／不符項目／三分法／掃描條件／
新開 anomaly 與 DR／獨立判斷），各節先留空。

先補記已完成之 W-8／W-13（其細節報告已在 docs/reports/，
上繳包引用之並補齊六節中逐項報告不會自然產生的部分：
跨項之預期 vs 實測對照、三分法、獨立判斷）。

其後每完成一項作業，**當下填入對應節**。reports/ 為附件不是替代。

## 作業（此順序）

W-19  值域完整性複驗 → 更新 data/spec_variables.tsv
      對 30 個 token 逐 token 逐來源列出**完整值集合**（非僅交集）。
      **判準改為：兩來源之值集合不相等即列出**（原判準「無交集才列」）。
      每筆附 arch_scope 欄 —— 該值域出自哪些 [EE Architecture] 標籤之
      條文（R-VS19）。跨架構之差異不列為不一致。
      已知案例：$HeatedSeatFL$ 於 CUSW 條文 4857940 列 0h/1h/3h 三階，
      於 Atlantis High 之具名式與 LID 表皆為四階（含 MED / 2）。

W-20  CFTS044 值域抽取之第三式
      現行兩式：`$var$ = [值]`、`路徑.名稱 == "值"`。
      已知漏抽之錨點：$HSW_StatFailSts$ 之 Fail_Present
      （DBC 與 LID 表皆載，式二只抓到 Fail_Not_Present）。
      以該錨點反推漏抽之記法，補為第三式，補後重跑 W-8 與 W-19。
      **不得以「找不到第三式」收尾而不說明其驗證方式**（§5a 條 12：
      抽取式須以已知全集驗證）。

W-15b′ DBC ↔ LID 表逐屬性交叉（本 feature 所用之 message／signal）
      比對 signal 名／message 名／CAN id／起始位元／長度／factor／offset／
      VAL_ 值表。通過條件寫成「與參照對象在所有可讀屬性上一致」，
      不寫成「已知的幾項正確」（§5a 條 14）。

W-17  LID 列數差 6 之追因（2,626／446 vs 2,629／449）；
      TRUNCATED_ENUM 之其他形態（現僅偵測 `# = Not Used` 結尾）。

W-9   Comfort 逐條對照 → docs/reports/comfort_overlap.md
      **本 feature 側母體為 237 個 Functional leaf，非 271**
      產出為 R-VS7 委派句之來源對照表：逐條列出命中座椅加熱／通風／
      方向盤加熱之 Comfort leaf 與其對應之本 feature leaf。
      **必停已由 R-VS7 解除**，做完併入本輪上繳。

W-16′ 於 W-16 產物補一行：Categorization 值域全集
      （Functional Requirement 237／Heading 25／Information 8／
        information 1，合計 271，無其他值、無空值）。

W-21  登記 A-VS22 入 ANOMALIES.md：$VentedSeatFL$ 之值中出現
      `Vented Seat Off / HS_OFF`（應為 VS_OFF），規格筆誤，RD-1 FYI。

## 禁區

git 寫入性操作一律不執行，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
.gitignore 之修改屬 Pei（R-VS16），不得自行改。

## 升級條件

W-19 出現**跨來源值集合不相等且非架構差異**者；
W-15b′ 出現 LID 表與 DBC 之屬性矛盾；
實測與 05／07 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
**本輪無「必停」項。**

## 仍開啟（不得預設答案）

DR-5-B（失效彈窗＋PDO 圖示，17 leaf 之畫面層 —— A-VS10 已查為綠，
        性質為上游未具名，走 RD-1）
DR-7（PROXI 表）／DR-8（VC_VEH_LINE 車型碼，W-8 已確認無交集）
DR-11（CFTS100，1 leaf）
遇到需要它們的判斷 → 依 R-VS17 標 BLOCKED 或登記待判，繼續其他作業。

## 完成後

下一步為 framework Part Vehicle Setting ＋ profile（Tier 2），
再首批生成，再 pilot。**本輪不做這三項。**
```
