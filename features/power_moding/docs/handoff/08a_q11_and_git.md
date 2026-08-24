# 下放包 08a —— Q11 定案與 git 窄口授權（與 08 同一往返，須併讀）

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [08_criterion_repair.md](08_criterion_repair.md)
  同屬第 08 輪，上繳仍為 `docs/upstream/08_criterion_repair.md`
- 08 本文未改一字

---

## 一、Pei 之裁定（2026-08-24，逐字）

> 「甲 commit 交給claude code」

兩件：Q11 採（甲）；06＋07 之提交授權執行層執行。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH36（Q11 定案 —— Test Set #2 之名）
Layer 2 之第 2 組名為 `Disclaimer Screen`。Layer 2 自此**定版為 8 組**：

  Splash Screen(3)／Disclaimer Screen(7)／Startup Animation(9)／
  Startup Sounds(6)／Power Transitions(7)／Power Off Behavior(8)／
  Voice Assistant Key(5)／Off Road Plus(3)   —— 合計 48，餘數 0

本組名與 Test Group `Disclaimer screen` **字面重複，為 canon §4.2
「不得重複 Test Group 字樣」之明示例外**，其範圍嚴格限定為：
本 feature、本組、此一情形（Test Group 取交付夾標籤而非能力名，
致交付夾名恰等於其中一個能力群之名稱）。**不得外推至他 feature，
亦不得作為 §4.2 之一般性放寬。**

未採之兩案及其理由，須隨本條保留：
(乙) `Acceptance Screen` —— `Acceptance` 非規格用語（規格自 7.1 SU1 至
     10.4 PITA6.1 一律用 `disclaimer`），屬造詞，違 §8.4.1 之精神；
(丙) 併入 `Splash Screen` —— 合 §4.2 字面，但該 10 leaf 混兩個 FROP、
     兩種觸發情境（開機動畫 vs 免責畫面互動），且客戶無法以 H 欄過濾出
     disclaimer 之 7 條。

**granularity 判準對三案全部 PASS，對本題無鑑別力**（08 包 §2.3），
故不得引之為支持本條之理由。本條之依據為上開可過濾性與不造詞二者。
```

```
R-PMH37（git 窄口授權 —— 一次性）
Pei 於 2026-08-24 授權執行層執行**一次** git 提交，範圍嚴格限定如下。

**授權範圍**：06＋07 兩包之工作區異動，八個路徑：
  features/power_moding/ANOMALIES.md
  features/power_moding/RULINGS.md
  features/power_moding/framework.md
  features/power_moding/docs/INDEX.md
  features/power_moding/docs/handoff/06_framework_proposal.md
  features/power_moding/docs/handoff/07_gap_widening.md
  features/power_moding/docs/upstream/06_framework_proposal.md
  features/power_moding/docs/upstream/07_gap_widening.md

**訊息**（逐字）：
  feat(power_moding): packages 06-07 — layer 2 verified, granularity pass, CFTS009 gap widened

**時點**：於 08 包步驟 1 之前執行，使 08 之異動落在乾淨之工作樹上。

**明文不授權**：`push`／`amend`／`rebase`／`tag`／`reset`／`checkout`／
`stash`／分支操作；上列八路徑以外之任何檔案（含他 feature、
`scripts/new_feature.py`、`forms/`）；第二次提交。

**執行後義務**：於上繳包揭露 `git status --short` 與 `git log -1 --stat`
之實際輸出，並確認暫存區於提交後為空。

**失敗處置**：任一指令非零退出、或 `git status` 顯示上列八路徑以外之
檔案被暫存 —— **立即停手，不得補救、不得重試**，於上繳回報。

本授權用畢即失效。08 包及其後各包之提交仍須另行授權（R-G5 未變）。
```

---

## 三、對 08 包各節之影響

| 08 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §五 Q11 | 待裁，阻斷 Layer 2 定版 | **已裁（甲）** → R-PMH36；阻斷解除 |
| §五 5.1 git 未提交 | 屬 Pei 之動作 | **已授權執行層** → R-PMH37 |
| §七 停止條件「Test Set #2 仍不得預填」 | 生效 | **解除** —— 改為「須逐字填 `Disclaimer Screen`，大小寫敏感」 |
| §六 步驟 2、3 | 三案試算仍須跑 | **維持** —— 其產出為 R-PMH36 所引之無鑑別力證據，須實跑留檔 |
| §六 步驟 1–6 | 不受影響 | 不受影響，另增步驟 7、8（見下） |

### 3.1 增列之作業步驟

7. **執行 R-PMH37 之提交** —— **排在步驟 1 之前**。
   先 `git status --short` 確認工作區內容與 R-PMH37 之八路徑相符
   （若有其他檔案被改動，列出並停手），再 `add` 與 `commit`。
   **不得使用萬用字元**（R-PMH3(c)）。

8. **Layer 2 落地** —— Q11 解除後：
   - `framework.md` 之三處 `<PENDING Q11>` 改為 `Disclaimer Screen`，
     狀態由「未定版」改為**定版**，並記 R-PMH36 之例外範圍限定；
   - `feature.yaml` 增 `write_back.test_set_value` 之對照表（8 組），
     並依 **R-PMH18** 之精神加大小寫警語：
     Test Group `Disclaimer screen`（小寫 s）／
     Test Set `Disclaimer Screen`（大寫 S）**刻意不同，不得統一**；
   - `DECISIONS.md` 之 H 欄由 `[PEI — Phase 3]` 改為 `[RULED R-PMH36]`；
   - `PLAYBOOK.md` §6：Phase 3 標完成，Open rulings 表移除 Q11，
     下一步標 Phase 4。

   **此三處之大小寫比對須為敏感比對，並於上繳貼出實測輸出**
   （比照 03a 之 R-PMH18 驗證）。

---

## 四、本輪 open 項

| 項 | 狀態 |
|---|---|
| Q11 | **已結清** —— R-PMH36 |
| git 提交（06＋07） | **已授權** —— R-PMH37，一次性 |
| A-PMH13（`-028` 處置） | 待 Pei，Phase 4 前，提案 (ii)＋(iii) 併行且該列寫入並揭露 |
| Q10（`Product Document` 分頁） | 待 Pei，Phase 7 前，提案不填 |
| A-PMH03／04 | PENDING，Phase 4 複核 |
| A-PMH10／A-PMH12 | PENDING（A-PMH12 為 Phase 6／7 前置阻斷項） |
| A-PMH06 canon 層（`new_feature.py` 樣板） | PENDING-CANON |

**Phase 3 於步驟 8 完成後結束，Phase 4（TC 生成）之唯一前置為
A-PMH13 之處置** —— 其涉及 48 個 leaf 中之一個，可於首批不含 `-028` 之
情形下先行開批。

---

## 五、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH36 | Test Set #2 = `Disclaimer Screen`；Layer 2 定版 8 組；§4.2 例外之範圍限定 | ✅ |
| R-PMH37 | git 一次性窄口授權（八路徑、逐字訊息、明文不授權清單、失敗即停） | ✅ |

二條各管一事。R-PMH36 為**採納型**，未採之兩案及其理由已於條內保留；
R-PMH37 為**一次性授權型**，其失效時點已於條內明載。
