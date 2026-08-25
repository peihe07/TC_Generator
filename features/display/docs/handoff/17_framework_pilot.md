# 下放包 17 —— framework 三層草案、pilot 批（004／005）整備

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/17_framework_pilot.md`（可與 14/15/16 之上繳合併）
- **本包對交付物之推進：framework 草案（待 Pei 核）＋ pilot 批之全部
  生成素材（R-G31 之推進聲明，自本包起）**
- 前置：下放包 14/15/16 依 `docs/RETROSPECTIVE.md` §五修剪後執行；
  被撤回之步驟記入 `BACKLOG.md`，不做。

---

## 一、規則落地

1. 抄錄 `RETROSPECTIVE.md` §四之 **R-G28–R-G31** 入
   `docs/fw036/RULINGS_LEDGER.md`（核對表由腳本產出）。
2. 建 `features/display/BACKLOG.md`，收 RETROSPECTIVE §五之撤回項
   （14 包步驟 3、4；16 包步驟 2 之縮減差額），每項記其出處與
   原下放包編號。
3. `DECISIONS.md` 補記檔位：`process_tier: 輕量（R-G30，leaf=8）；
   本條生效前已按標準檔位走，不回溯重做`。

---

## 二、framework 三層草案（`[PROPOSED]`，待 Pei 核）

寫入 `features/display/framework.md`。**本節全文即草案**，執行層
逐字落檔，不增删內容；Pei 核可或修改後方鎖定（canon §4.1.2 步驟 5）。

### Layer 1 —— Test Group

`Display`（spec 模組名，R-C6；`feature.yaml` 已載）

### Layer 2 —— Test Set（4 組，寫入工作簿 H 欄）

| Test Set | leaves | 共同 setup 形態 | 命名依據 |
|---|---|---|---|
| `Operative State` | 001, 002, 003 | 電源狀態／喚醒操作 | 037 標題 `Display Operative State Management [ON/OFF/Wakeup]` |
| `Thermal Management` | 004, 005 | 溫度條件注入 | 037 Sub Categorization `Thermal Management`／`Thermal Protection Management` |
| `Pop Up Handling` | 006 | popup 觸發 | 037 標題 `Pop Up handling` |
| `Rear View Camera` | 007, 008 | RVC 觸發訊號 | glossary R-DM22 之 `RVC = Rear View Camera`；§4.2 禁縮寫入欄 |

§4.1.3 自檢：以任一 Test Set 過濾皆得 1–3 個 leaf 之 TC 群、
共享 setup 與入口，非逐 leaf 一組、無 Misc。單 leaf 之
`Pop Up Handling` 為真實離群（其 setup 與其他三組皆異），合於
「genuine outlier」例外。

### Layer 3 —— spec 章節分組（僅存 framework.md，不入工作簿）

| L3 | 對應 L2 | 已定錨之章節／列 | 待 Phase 2 查補 |
|---|---|---|---|
| `DM-OS` | Operative State | CFTS_020 splash 相關段（probe 命中 9 段，時段轉指 `{CFTS009-722}`） | 001/002 之 CFTS 條號 |
| `DM-TH` | Thermal Management | **CFTS `1.11.2.2 {4820281}`**（含 `{4820289}` `{4820290}`）；回復 `{4820287}` `{4820288}`；SYS2 r31–r34 | multi-stage（DR-DM4） |
| `DM-PU` | Pop Up Handling | Pop Up List `Main`（PU0130／PU0517 等）＋ Priority Matrix | popup↔leaf 歸屬逐條判 |
| `DM-RVC` | Rear View Camera | SYS2 r37/41/42/44/45/52/53/54（`SYS-RA-DM-036…053`） | r213–r226 區段之副本疑問 |

---

## 三、pilot 批整備（`pilot-01` = `SWE1-DM-004`、`SWE1-DM-005`）

**本包整備、不生成。** 生成之前置：Pei 簽核 `DECISIONS.md` ＋
核可 §二之 framework。整備物如下：

1. `features/display/batches/pilot-01/batch_context.md`，內容：
   - **範圍**：004 全部；005 之單級行為＋回復行為。
     005 之 multi-stage **不入本批**（DR-DM4），於 batch_context 明記
     為 deferred，非 PENDING 佔位列。
   - **req_id**：`SWE1-DM-004`／`SWE1-DM-005`（R-DM42）
   - **Test Group／Test Set**：`Display`／`Thermal Management`
   - **值域來源**（逐項附出處，不得另尋）：
     - 門檻：`> 85 degrees C`／`<= 85 deg C`，CFTS `{4820289}` `{4820290}`
       （§8.7.1：Pre-Condition 寫具體值）
     - 訊號：`signal_resolution.tsv` 之 `$DCSD_DISP_STAT$`／
       `$TGW_DISP_STAT$` 等，三段鏈解至 DBC（R-DM17）；
       值標籤 `DISP_HOT`／`DISP_OFF`／`DISP_ON` 依 R-DM43 取訊號側
     - popup：**PU0517**（004：亮度降，timeout 10，cat 1T）／
       **PU0130**（005：轉暗關閉，timeout 10，cat 1T），
       引用須連 `source_locator`；歸屬判定依 §8.5／§8.2.1 記入 reasoning
   - **格式**：訊號寫法依 §8.7.5 v3（`$MESSAGE.Signal$ = raw (label)`；
     Display 無 profile override）；test_item 兩段式（R-S4），
     上半 verbatim 保留 037 原文（含 `DISPLAY_ON` 拼法，R-DM43）；
     spec_reference 一 ObjectID 一行 `CFTS020-{7位}`（§10.7 之排列裁定）
   - **sibling 軸**：004 vs 005 之區分 token 須在 tc_title 可見
     （警告 vs 關閉／回復）；005 內部觸發與回復分 TC（§8.2.2 stress-test）
2. `lint.popup_ids` 填 `[PU0130, PU0517]`（僅此二值，逐字）。
3. 複驗生成前置之機器可查項：`recon_assertions` PASS、綁定 11/11、
   `DECISIONS.md` 簽核狀態（`read_signoff` 之判準）。**未簽核則
   整備完成即停，不生成**（canon：unsigned sheet blocks Phase 4+）。

---

## 四、停止條件

沿用 1–41，另加：
42. batch_context 中任何值找不到本包 §三所列之出處 → 停（§8.4.1）。
43. framework 草案落檔時若須改動 §二任何內容方能成立 → 停並回報。

**全部 git 操作屬 Pei。**

## 五、上繳包要求（`17_framework_pilot.md`）

R-G28–31 核對表；BACKLOG.md；framework.md 落檔確認；
batch_context 全文；前置複驗三項；未驗項分流（A/B 標記，R-G29）；
commit 訊息與 pathspec（不執行）。
