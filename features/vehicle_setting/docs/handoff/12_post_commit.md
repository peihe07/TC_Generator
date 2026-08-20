# 12 下放包 — 入庫覆核、P1 關閉、附錄授權、04 輪開跑

分析層寫入，2026-08-20。

---

## 1. 覆核：接受，且拒絕重跑之判斷正確

`2c6c9b3` 之 7 檔與步驟 4 之 pathspec 一致；步驟 5 三項、步驟 7 三項
（`ls-files` 僅 `INPUTS.sha256`、`shasum -c` 15/15 OK）皆已完成並留痕。

**拒絕重跑正確**：R-VS22 明文「於本次 commit 完成後失效」。
授權用畢即失效，不因指令被再次貼上而復活 —— **這正是窄口授權該有的行為。**

---

## 2. P1 已關閉 —— 執行層之待辦清單有一項過期

執行層列「P1 刪 `features/vehicle setting/`」為仍待處理。**該項已關閉**：

| 查證 | 結果 |
|---|---|
| `find features -maxdepth 1 -type d -name '* '` | **無輸出** |
| `git ls-files --error-unmatch "features/vehicle setting"` | `did not match any file(s)` |

工作區與版控**皆無**該目錄。

→ **A-VS19 之措辭須改寫**：由「誤建目錄待刪」改為
「`new_feature.py` 之名稱正規化缺陷（`feature.lower()` 不轉空白）
會產生含空白之目錄名；**本 feature 未落地**，故無待刪標的。
該工具缺陷維持登記，不在本 feature 修。」

---

## 3. 須查證之一項 —— 分析層先前之陳述可能為誤

`2c6c9b3` 只含 **7 檔**，而步驟 4 之 pathspec 涵蓋
`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`DECISIONS.md`／
`RECON.md`／`PLAYBOOK.md`／`RUNBOOK.md`／`feature.yaml`／`docs/`／`data/`。

**若那些檔案已被追蹤且無改動，它們不會出現在本次 commit** ——
即它們**早已入庫**。

分析層自 07／09 包起連續三次陳述「三輪產物、十九條裁決全部不在版控中」，
**該陳述之依據為分析層自身之推測（Pei 未執行 P2），未曾實測。**

```
W-25（查證，04 輪首項之前置，唯讀）
執行 並記入上繳：
    git ls-files features/vehicle_setting/ | wc -l
    git ls-files features/vehicle_setting/ | head -40
    git log --oneline -- features/vehicle_setting | head -10

判定：
  (a) 若 vehicle_setting 之多數檔案早已被追蹤 →
      **分析層 07／09 包之「不在版控」陳述為誤**，須於上繳明記更正，
      並登記 A-VS25（分析層以推測代替實測）
  (b) 若確實只有 2c6c9b3 之 7 檔被追蹤 →
      其餘檔案為何未被 git add 帶入？（pathspec 有列 docs/ 與 data/）
      此時反而是 **git add 未如預期**，須追因

**兩種結果都要回報。** 不得只回報符合預期者。
```

---

## 4. 附錄 A 之入庫 —— 新授權

```
R-VS24（Pei 2026-08-20，窄口授權，一次性）
得執行：git add 與 git commit，pathspec 限
        features/vehicle_setting/docs/upstream/02_variables_and_sweep.md
        （即入庫紀錄附錄 A）
        ＋ 本輪 W-25 之結果若寫入該檔，一併帶入
訊息：docs(vehicle_setting): round 02 upstream appendix A — commit record

不得執行：push／amend／rebase／reset／restore／checkout／branch／tag／
          stash／clean／merge／cherry-pick／rm／mv
本授權於該 commit 完成後失效。

阻斷判準依 R-VS23：暫存區出現 pathspec 以外之路徑即停，
工作區存在他 feature 之在途變更則列出並續行。
```

**推送仍屬 Pei**，本授權不含。分支現領先 origin 8 個 commit。

---

## 5. 04 輪：開跑

依 R-VS21，頭部為連兩輪未執行之三項；其前不得插入新作業。
**W-25 為唯讀查證，不佔作業順位，與開上繳包同時完成。**

| # | 作業 |
|---|---|
| 0 | 開 `docs/upstream/03_*.md`（R-VS18）；併入 W-25 之結果 |
| 1 | **W-15b′** DBC ↔ LID 逐屬性交叉（signal 名／message 名／CAN id／起始位元／長度／factor／offset／VAL_）。通過條件寫成「與參照對象在所有可讀屬性上一致」 |
| 2 | **W-17** LID 列數差 6 之追因；`TRUNCATED_ENUM` 其他形態 |
| 3 | **W-9** Comfort 逐條對照（母體 **237** 個 Functional leaf）→ `docs/reports/comfort_overlap.md`，為 R-VS7 委派句之來源表。**必停已解除** |
| 4 | **W-22** 餘數驗證（09 包 §3）—— 通過條件為 (b) 類為 0 |
| 5 | **W-23** 歸因判準化 C1–C5 ＋ 修正 C3 解析式（09 包 §4） |
| 6 | **W-24** `IGN_OFF` 兩處條文是否落在 237 個 Functional leaf 內 |
| 7 | 改寫 A-VS19 之措辭（§2） |

**待裁而未裁者，不得預設答案**：R-VS18／R-VS19（P11）、
R-VS20／R-VS21（P12）、R-VS23／R-VS24（本包）。
本輪依現行草案作業，遇需其定案之判斷 → 登記待判，繼續其他作業。

**R-VS20 未裁定之影響**：`$HSW_StatFailSts$` 這類「in-scope 無值域」之
token 尚無合法取值路徑。W-22 產出後若需定案值域，即會擋住。

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS24 | 附錄 A 入庫之窄口授權 | ✔ §4 |
| W-25 | 版控現況查證（作業，非條文） | ✔ §3 |
