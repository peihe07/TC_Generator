# 下放包 04 — F7 回調、判準改內容判準、台帳收斂

日期：2026-08-28
Feature slug：`popup`
前置：上繳包 03 已入庫並經分析層覆核。本包為 pilot 之最後一輪修正；
其後即進入交付準備（05）。

## 禁區

- git 屬 Pei（R-G5）；xlsx 寫入一律 `surgical_save`（R-G3／A-POP5）
- 不代改他 feature 之 ANOMALIES.md／DATA_REQUESTS.md（R-POP16 甲、R-POP19）
- `ledger_xref.py` **不接入 `gate_all.py`**（見 §五）

## 裁決引用（R-G13）

本輪新立 R-POP18／19／20，並修訂 R-POP13（兩處）與 R-POP15 F1。
全文見 `features/popup/RULINGS.md` 現行文。

---

## 一、分析層之誤（先行揭露，第二次）

上繳包 03 §一-1／§一-2 指出之兩處，**皆為分析層之誤，照收**：

1. 下放包 03 §三令修 `feature.yaml` 之 `PROJ` —— **該標的不存在**。
   分析層把 A-POP9(4) 所記之錯誤述值連同處分寫進 R-POP13，
   使 A-POP9 之錯誤於其自身處分條文內再現。已修訂 R-POP13。
2. 下放包 03 §三「全簿掃 `newR1L`／`POP-` 須為 0」—— **不可達成且不應
   達成**（D2 為專案名稱欄、D10:D14 為 req_id）。分析層下預期數字時
   未先確認欄位語義即定「全簿」之範圍。已修訂 R-POP13 之量測界。

執行層兩處皆停下回報未自為，處置正確。

## 二、F7 回調（R-POP20）—— 本包主件

F1 之實作使四條 Final Step 超出 IN §5.2B 之 ≤ 18 words
（實測 31／19／29／29／17）。**F1 不推翻，只限長度。**

逐條回調，check target 保留、細節退回 ER：

| 條 | 現行詞數 | 回調後應 ≤ 18 | 退回 ER 之細節 |
|---|---|---|---|
| 001 | 31 | ✓ | 5 秒、`PU0942 Timeout (sec)` → ER 3（已載）|
| 002 | 19 | ✓ | 「immediately after the second press」可縮 |
| 003 | 29 | ✓ | 5 秒時窗、`PU0580` → ER 3（已載）|
| 004 | 29 | ✓ | 3 秒時窗、`PU0949` → ER 3（已載）|
| 005 | 17 | 不動 | — |

**ER 不得因此縮減** —— 回調是把細節留在 ER，不是刪掉。
回調後須複驗：五條 Final Step 仍 5/5 含 `check that`，且 ER 3 之
時限與 PU 出處字樣一字未減。

## 三、判準改內容判準（R-POP18）

`scripts/lint_docs036.py` 之 `series_in()`：**廢「限檔內首個表格」**，
改內容判準 ——

1. 一張表格若其**首欄有 ≥ 2 列**匹配 `^(A|DR|R)-[A-Z]+\d+$`
   （去除包覆之 `[]`、粗體記號後）→ 視為登記表
2. 一檔可有多張登記表；同檔各登記表之編號**合併為一序列**後再判跳號
   （power 之空行切段情形）
3. 標題式 `## A-XXn` 與 `## [A-XXn]` 兩式皆認
4. R-POP16 乙之其餘兩項（同表重複判紅／跨表降 note）**不變**

**迴歸四向**（G-K／G-N，前三向為既有、第四向為本包新增）：

- (a) 放寬向仍成立：`power_moding` DR-PMH 系列仍為 note、`--gate` exit 0
- (b) 注入向仍成立：主表內注入真重複 → FAIL
- (c) 假前綴向：`privacy` 之 `S` 仍排除 —— **須實證，不得推定**
- (d) **回收向（新）**：A-POP10 所記之丟棄真陽性應回到受檢
  —— sxm 4／audio_mgmt 7／projection 63 之「略過數」應降為 0，
  且其中之真跳號應現身。逐 feature 前後對照輸出。

**(d) 之預期產物**：若回收後浮現新的真跳號，**只造清單、不代改**
（R-POP16 甲），逐筆入各該 feature 之 BACKLOG，格式沿 03 包所建兩本。

## 四、A-POP6 甲類訂正（R-POP19）

- sxm `A-SX18`／`A-SX19` **撤回**（假陽性，執行層已正確未寫入）
- A-POP6 §甲 之標題數字（「4 個 feature，5 筆」）改為訂正後之
  **2 個 feature／2 筆**，並於該節註明三個數字之由來（原標題／原表列／
  訂正後）—— 不刪除原數，加註保留（R-TM13 形制）
- A-POP10／A-POP11 之主表狀態改 RESOLVED（R-POP18／R-POP19），
  明細節標題同步

## 五、`ledger_xref.py` 之處置

- **另立於 `scripts/` 之判斷追認**（不改 vehicle_category 之同名檔）
- **不接入 `gate_all.py`**：跨 feature 掃描實測 6 綠／6 紅
  （power_moding 7、driver_distraction 7、projection 24、
  time_management 29、audio_mgmt 43、vehicle_setting 473），
  接入即全 repo 轉紅。是否接入、以何為基線，屬全域政策，留 Pei（§九-3）
- 開發中三次判準修正（處分條號限狀態欄取、號碼跨全檔收集、
  兩式標題皆認）**追認**，且其第 2 點正是 R-POP18 所以與 lint 分野之理由
- 本包續用其 `--feature popup` 於 §七 之收斂複驗

## 六、上繳包 03 §十三 之一項失準（校正，不新開 anomaly）

§十三 第 9 項稱「`DECISIONS.md` 之 [PROPOSED]／[PEI] 未裁、Sign-off 未填」。
**實測不符**：`features/popup/DECISIONS.md` 之 Sign-off 逐字為
`Reviewed by: PeiPYHsu  Date: 2026-08-27`，§6 兩筆 `[PEI 2026-08-27]` 已回填，
`Overridden items` 載「8 個 `[PROPOSED]` 未動，binding as proposed」。

此為 R-POP17 第 1 項所禁之「手寫重述」殘留（§十三為人工清單，未 live 產）。
**處置**：§十三 改由 live 產或逐項複驗後重寫；**不新開 anomaly 號**
（同 A-POP9 之型，已有條文管轄）。順帶複驗 §十三 其餘 11 項是否亦有失準。

## 七、寫回與 gate

- `sandbox/` 作業、`surgical_save` 寫回、`zipfile` 複驗 x14 存活
- `lint036.py --profile popup` 全跑（21 項）
- `ledger_xref --feature popup` 須 PASS
- `rulings_hash.py` 重產（R-POP18／19／20 新增；R-POP13／R-POP15 之
  sha **會變**，因本輪修訂其條文 —— **此二者之變動為預期，非違反
  R-POP11 之 invariant**；其餘既有列 sha 變動須為 0）

## 八、預期數字（[MANUAL]）

| 項 | 預期 | 量測條件 |
|---|---|---|
| Final Step 詞數 ≤ 18 之條數 | 5/5 | 以空白切詞，`(sec)` 括弧不計，逐條 |
| Final Step 含 `check that` | 5 | 逐條末步驟 |
| ER 3 含時限字樣之條數 | 3（001／003／004）| 回調前後相同，逐條比對 |
| TC 總數 | 5 | 語料陣列長度 |
| PENDING 佔位 | 0 | 全簿全欄 |
| `input_test_data` = `NA` | 5 | 逐條等值 |
| lint 略過數（sxm／audio_mgmt／projection）| 0／0／0 | 新輸出之「略過」欄 |
| `privacy` 前綴集含 `S` | 否 | 前綴集輸出 |
| RULINGS.sha.tsv 新增列 | 3 | R-POP18／19／20 |
| RULINGS.sha.tsv 變動列 | 2 | R-POP13／R-POP15（本輪修訂）|
| 其餘既有列 sha 變動 | 0 | 逐列比對 |
| x14 DV | 1，存活 | `zipfile` 直讀 |
| `canon_refs` | 說明歸因即可，不求綠 | 見 §九-4 |

## 九、留給 Pei（本包不處理，承 03 §十三並校正）

1. R-POP5（Heading 台帳處置 [DEFAULT]）追認
2. `-002-05` 之 `design_method`：狀態轉換（現行）vs 負向測試
   —— **分析層意見：維持狀態轉換**。受測者是同一台 popup 狀態機在
   特定輸入下**不發生轉移**，仍屬 state-change focus；且與 001–004 同法
   可對讀。IN §12 之 Negative 係指非法輸入，本條之按鍵是合法操作
3. `scripts/ledger_xref.py` 與 vehicle_category 同名檔是否合併；是否接入
   `gate_all.py`（接入即全 repo 轉紅）
4. `canon_refs` +3（兩本 BACKLOG ＋ 上繳包之 `R-G29` 引用）：修 `R-G29`
   之可解析性／改寫引用／維持。**分析層意見：維持** —— 執行層拒絕塞
   waiver 且拒絕刪引用，兩者皆對；+3 是誠實的帳
5. Priority／Estimated Test Time 欄之政策（Q 欄未寫入）
6. `forms/` 落點政策（全域，承 03 §十二）
7. `sources/` 版控條文之 R- 取號
8. `lint_paths` 之紅（driver_distraction 在製品，他 feature）
9. **pilot review** —— 分析層已於 2026-08-28 覆核五條全文，除 F7 外無
   其他發現；F7 修畢即建議放行

**已自 03 §十三 移除**：原第 9 項「DECISIONS.md 未簽」—— 實測已簽（§六）。

## 十、升級條件

- F7 回調後某條 Final Step 失去 check target 或 ER 資訊減損
- R-POP18 之內容判準回收後，(a)(b)(c) 三向任一由綠轉紅
- `privacy` 之 `S` 未被排除（判準未達預期，停下勿硬調）
- 除 R-POP13／R-POP15 外之既有 sha 變動
- §六 複驗發現 §十三 尚有第二項失準（回報，勿逕改上繳包 03 之歷史文）

## 十一、未結 DR（IN §8.4.3）

DR-POP2／DR-POP3／DR-POP4，皆「已登記，未送出」，皆不阻斷。
DR-POP1 已 RESOLVED。

## 十二、上繳要求

- **摘要一律自 repo live 產**（R-POP17-1）；§十三 型之人工清單須逐項複驗
- 預期數字對照（相符者亦列）；不符停下不調和
- R-G13 引用表（含 R-POP13／R-POP15 之**新** sha8）
- 迴歸四向實跑輸出（含 (d) 回收向之逐 feature 前後對照）
- 五條 TC 全文（回調後）
