# 下放包 06 —— 縮寫錨定案、聚合缺陷通則、PROXI 續查

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/06_glossary_anchor.md`
- 前一包：`05_proxi_and_values.md`（上繳已覆核，見 §一）

---

## 一、上繳包 05 之覆核

**核可，無退回項。**

### 1.1 59 vs 44 之調和 —— 成因比數字重要

執行層查明：兩次**擷取**都是 59，差異在**聚合** —— `coverage_map.py`
把每列 token 以逗號串成字串寫入 TSV，統計時再 `split(",")` 切回，
而 token 自身含逗號（`[Radio:R1M, VP5R120, R1H]`、
`[EE Architecture:Atlantis Mid, PowerNet]`），切碎後去重才塌成 44。
上繳 04 §0.2 所報之 `' Atlantis High'`、`' R1H'` 等前導空白 token
即為切壞之殘骸。

**這個調和的價值不在把 44 改成 59，在於指出我上一包問錯了方向。**
我要求說明「換行、`_x000D_`、儲存格合併」之切分差異 —— 三項皆非成因，
執行層逐項排除後另尋，才找到真因。若它照我列的三項去找，會找不到而
回報「無法調和」。

執行層自陳「這是第三次同型錯誤：不是量錯，是量完之後那一步錯」，
此判斷正確且應升為全域條文，見 §四 R-G16。

### 1.2 A-DM17 —— R-G13 在 PROXI 上重演

以 Logical Identifier 查 PROXI `Parameter Name` 得 70/446；改以 LID
`Atlantis & Atlantis High` 欄組之 `Signal Name`（該欄組 `CAN` 值為
`PROXI`）為鍵，得 **177/446**。漏 107 列，佔 60%。

**R-G13 第 (2) 要件「用什麼名字查」不限於 DBC。** 見 §四 R-G13 之補充。

### 1.3 拒絕把 `Display_OFF_SoftKey`(r692) 認作 `DSP_SK_PRSNT`

兩者只差 `_Prsnt` 尾綴，且同分頁另有三個同類 soft-key 參數作為
「涵蓋範圍應含」之證據。執行層仍不認定，開 DR-DM6 與 M-3。
**這是對的** —— 尾綴之有無在 PROXI 中可能正是「參數本身」與
「參數是否存在」之別。

### 1.4 停止條件 15 之判定 —— 差一點誤判

`TELEMATIC_VEHICLE_SETUP` 在 vehicle_setting 之 20+ 檔中命中，但相異之
單位是其下之訊號 `CallAction`，該訊號 0 命中。執行層之自註採認：

> 若只查訊息名就會報「有命中 → 停」。相異之單位是**訊號**，
> 查詢也必須以訊號為單位。

LID 兩版 2,548 個 identifier 相異僅 2、單側有 0、本 feature 15 個
`$Signal$` 全同。§7.3 之結論採認：「差異小是量測結果，不是可以省略
綁定的理由」。

---

## 二、縮寫錨 —— 定案（第三次受阻，本包解除）

執行層於上繳 03 §4.4、05 §6.3、05 §9 第 2 項連續三輪提出此阻塞，
分析層兩輪未裁。**這是我的拖延，不是執行層的疏漏。**

### 2.1 為何原禁令過寬

下放包 03 §七第 10 條寫「錨必須是逐字比對，不逐字即無錨」。該條之
用意是排除 bag-of-words 重疊（token 重疊、相似度、模糊比對）。但
**一份封閉、逐條列舉、且每條都有出處的縮寫對照表，不是相似度** ——
它是有限的逐字替換清單，每一條都可稽核。原禁令把兩者一起擋掉，過寬。

### 2.2 出處已查得 —— `RVC` 之展開不需要猜

分析層實測（`openpyxl`、`data_only=True`、非唯讀全表掃描）：

**037 `SWE1 Requirements` r14（`SWE-DM-007`）之
`Requirement Description` 內含逐字片語：**

```
... shall transition display state to Rear View Camera (RVC) mode when
reverse gear signal is detected ...
```

r15（`SWE-DM-008`）同樣含 `Rear View Camera (RVC) display`。

**縮寫與其展開在同一句、同一份來源文件中並列。** 故
`RVC = Rear View Camera` 是**查得**，不是推定 —— 不觸及 canon §8.4.1。

### 2.3 展開後之錨確實接得上，但接的不是 heading

分析層以展開後之片語逐字查 SYS2 `Basic Report` 之 `Description` 欄
（母體：333 資料列；比對：區分大小寫之子字串包含）：

| 標的 | 命中 |
|---|---|
| `Description` 含逐字片語 `Rear View Camera` | **24 列** |
| Heading 列含 `Rear View Camera` | **0** |
| Heading 列含 `Rear Camera`（無 `View`） | 8（r36／40／43／51／318／320／322／325） |

**heading 錨仍然接不上** —— SYS2 之 heading 寫 `Rear Camera Events`／
`Rear Camera Interrupts`，少一個 `View`，展開後仍不逐字相符。
接得上的是 **body 之 `Description` 欄**，其中 24 列逐字含
`Rear View Camera`，且多列同時含 `$TGW_DISP_STAT$ = [DISP_NORMAL]`、
`$RQ_DISP_INTS$` 等訊號（例 r41／r42／r44／r45）。

**故本包開放之錨是「片語錨」，不是「把 heading 錨放寬」。** 兩者不同，
不得混用。

---

## 三、仍待 Pei 裁定之一項（第四輪未決，現正式提交）

執行層連續四輪（02／03／04／05）於「該驗而未驗」中列同一項：

> `recon.py` 仍未跑通（A-DM8，Q5 未裁）。本 feature 至今十支腳本全為
> 自寫，**無一項經 repo 既有管線複核**。本輪三處自我更正（分隔符、
> PROXI 查詢鍵、多值拆分）全靠事後自查抓到 —— 三次都通過了
> 「輸出看起來合理」這一關。

這不再是可以掛著的事項。三次自查抓到，是執行層品質好；但**沒有任何
獨立管線在交叉檢查**，第四次可能就抓不到。

**Q5 正式提交裁定**（原為 `[PROPOSED]`，改列 `[PEI]`）：

| 選項 | 內容 | 代價 |
|---|---|---|
| **A** | 授權修 `scripts/intake.py` 之 `SHEET_SIGNATURES`，增以 `"SWE1 Requirements" in names` 判 `swra_report`，使 `recon.py` 可跑 | 改判準會改結論，且該分類器為全案共用 —— 須複驗其對既有十二個 feature 之分類是否改變 |
| **B** | 不修共用腳本，改於 `feature.yaml` 允許人工指定 `a03_report` 之 kind，由 `intake.py` 讀取覆寫 | 覆寫機制本身是新程式碼，仍須驗；但影響範圍限於有覆寫之 feature |
| **C** | 維持現狀，接受本 feature 全程以自寫腳本為之 | 十支腳本無交叉檢查；R-DM19 之承載範圍全部掛在未經獨立複核之產出上 |

分析層提案 **B**：影響範圍最小，且 A-DM7（scaffold 模板欄位表有 3 處
與母本不符）顯示共用預設值本就需要 per-feature 覆寫機制。

---

## 四、裁決條文

```
R-DM22（縮寫錨 —— glossary_phrase）
下放包 03 §七第 10 條之禁令（「不逐字即無錨」）**限縮**：其所禁者為
token 重疊、相似度、模糊比對；**不禁**封閉且逐條有出處之縮寫對照表。

本 feature 建立 `features/display/data/glossary.tsv`，欄位：

  abbrev | expansion | source_file | source_locator | cooccurrence_quote

**每一條目必須引一處「縮寫與其展開在同一句並列」之來源。**
查無此種並列者，不得建立條目 —— 那會是以領域常識填入，觸 canon §8.4.1。

首條（分析層已查得）：

  RVC | Rear View Camera | Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx
      | SWE1 Requirements r14 (SWE-DM-007), 亦見 r15 (SWE-DM-008)
      | "transition display state to Rear View Camera (RVC) mode"

以對照表展開後之比對，其 `anchor_kind` 為 **`glossary_phrase`**，
與 `verbatim`、`signal`、`value`、`heading` 分列，**不得合併計數**。
引用時依 R-DM12 須連同 `anchor_kind` 一併引用。

拘束三項：
(a) 展開後之片語須 **≥ 2 個詞**。單詞展開不得作為錨（鑑別力不足）。
(b) 比對為**逐字子字串包含**，區分大小寫；大小寫折疊須另行裁定。
(c) 展開後仍不逐字相符者，即為不相符，**不得再放寬一層**。
    實例：`RVC` → `Rear View Camera` 後，SYS2 之 heading
    `Rear Camera Events`（少一個 `View`）仍**不**相符。
```

```
R-DM23（未追查 ≠ 查無）
`proxi_candidates.tsv` 之 269 列 `anchor_kind = none`，其狀態為
**未追查**，非查無。本輪只追了 A-DM16 指名之三個起點。

凡輸出中以 `none`／`無`／空值表示之列，其欄位或說明須明載該值之語意
屬下列何者：

  (1) 已依 R-G13 三要件查證而確認不存在（= 查無）
  (2) 本輪未追查（= 未知）
  (3) 方法之界線所致（= 接不上，非不存在）

三者不得共用同一個表示。本 feature 現有之三處輸出
（`coverage_sys2_vs_swe_dm.tsv` 之 76 列無候選、
`proxi_candidates.tsv` 之 269 列、`signal_resolution.tsv` 之
`resolved = N`）須逐處補上其語意別。

理由：`LOOKUP_MISSES.md` 記的是 (1)，而 (2) 與 (3) 若混入，
台帳就變成「已查過而沒有」的假象，下一個讀者不會再去查。
```

```
R-G16（量測與聚合分離 —— 全域）
量測正確而聚合錯誤，是本專案已重複三次之缺陷型態：

  上繳 04 §5.3  DBC 以字典序取首個含該訊號名者 → 匯流排接錯
  上繳 05 §2    TSV 以逗號串接 token，而 token 自身含逗號 → 59 塌成 44
  上繳 05 §6.1  LID 多值儲存格未拆、拆後未做欄內空白正規化 → 漏 107 列

三者之共同特徵：**擷取階段正確，其後的選取／序列化／正規化階段出錯，
且輸出「看起來合理」，不會自曝。**

拘束三項：
(a) 序列化之分隔符不得為資料中可能出現之字元。逗號、分號、頓號、
    空白一律不得作為多值分隔符；採資料中不出現之字元（如 ` ¦ `）
    並於檔頭載明。
(b) 多值儲存格一律**逐值一列**輸出，不合併；若必須合併，須另存
    未合併之原始欄供稽核。
(c) 凡「自多個候選中選定一個」之步驟（選 DBC、選 LID 列、選 PROXI 列），
    其選定判準須逐筆記錄於 `note` 欄，不得只留結果。

驗收方式：任一產出之筆數，須能由擷取階段之筆數與各階段之增減量還原。
還原不出，即為聚合階段有未申報之操作。
```

```
R-G13 補充（查詢鍵不限於 DBC —— 併入原條）
原條第 (2) 要件「用什麼名字查」之適用範圍，及於**任何以名稱為鍵之
查找**，不限 DBC：PROXI 之 `Parameter Name`、LID 之
`Logical Identifier`、CFTS 之條號、Polarion 之 Melco ID 皆同。

實例（上繳 05 §6.1）：以 Logical Identifier 查 PROXI `Parameter Name`
得 70/446；改以 LID `Atlantis & Atlantis High` 欄組之 `Signal Name`
為鍵得 177/446，漏 107 列（60%）。
兩次都是「查了同一個檔」，差別只在用什麼名字查。
```

---

## 五、作業步驟

1. 抄錄 §四四條入指定檔（`R-G16` 與 `R-G13 補充` 入
   `docs/fw036/RULINGS_LEDGER.md`，後者併入 R-G13 原條之下、
   原文不動；`R-DM22`／`R-DM23` 入 `features/display/RULINGS.md`），
   附逐條核對表。
2. 依 R-DM22 建 `features/display/data/glossary.tsv`，
   首條 `RVC` 已由分析層查得（見條文）。
   **另行清點 037 與 SYS2 中其他「縮寫(展開)」或「展開(縮寫)」之並列**，
   逐條建立；查無並列者不建條目。至少須查：`DCSD`、`ICS`、`HU`、
   `FPDM`、`LVDS`、`SK`、`TGW`、`SGW`、`ETM`。
3. 依 R-DM22 重跑覆蓋對照，新增 `glossary_phrase` 錨層（優先序置於
   `heading` 之後、`melco` 之前），重出
   `data/coverage_sys2_vs_swe_dm.tsv`。
   舊檔依 R-TM13 保留（改名加 `.PRE_GLOSSARY`），不刪除。
   **`SWE-DM-007`／`008` 之候選數為本步驟之重點觀察項**，但不得以
   分析層 §2.3 之 24 為目標值 —— 先算後比。
4. 同步以 `glossary_phrase` 重跑 `proxi_candidates.tsv` 之
   `related_leaf` 欄。
5. 依 R-DM23 逐處補上 `none`／空值之語意別（三處輸出）。
6. 依 R-G16(a)(b)(c) 複查本 feature 現有之十支腳本：
   逐支檢其序列化分隔符、多值處理、選定判準是否留痕。
   **不符者逐支列出並修正**，修正前後之筆數變化逐支報告。
   此為 `features/display/scripts/` 下之自有腳本，不受
   「不修 `scripts/` 既有腳本」之拘束。
7. **PROXI 之 `Used by NODE(VFXXX)` 與 `Checked by NODE(CHECK)` 兩欄**
   （上繳 05 §9 第 4 項自陳未用）：實測其形態與取值分布，
   判其可否用於判定某參數是否適用於本專案之 VF。
   可用則納入 `proxi_candidates.tsv`；不可用則說明理由。
8. **037 之 `Requirement Description` 全文逐條精讀**（連續四輪未清）。
   八條逐條輸出：其所述之行為、其所含之具體值（若有）、
   其所引之外部文件、其與 SYS2 何列相關（依現有錨）。
   **本步驟不產出 TC，不作範圍裁定。**
9. **SYS2 之 `Polarion`／`_polarion` 兩分頁**（連續四輪未清）：
   實測其內容與用途，判其是否含本 feature 需要之資訊。
10. 更新 `docs/INDEX.md`。

> 步驟 8、9 為連續四輪之積欠，本輪清償。若因工作量須分輪，
> **先做步驟 8**（037 是判讀基準之上游，其未精讀影響最大），
> 並於上繳包明記步驟 9 順延及其理由。

---

## 六、停止條件

沿用既有各條，另加：

16. 步驟 2 之縮寫清點若發現任一縮寫在 037 與 SYS2 中之展開**不一致**
    （同一縮寫兩種展開）→ 停並回報。不得擇一。
17. 步驟 6 之複查若發現任一既有產出之筆數，**無法由擷取階段還原**
    （R-G16 驗收方式）→ 該產出標記為不可信並停手回報，
    不得逕行重算蓋過。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/06_glossary_anchor.md`）

1. §四四條之抄錄核對表
2. `glossary.tsv` 全文與各條之出處引句
3. 重跑後之 `coverage_sys2_vs_swe_dm.tsv` 錨分布，
   `glossary_phrase` 單獨列示
4. `proxi_candidates.tsv` 之 `related_leaf` 更新結果
5. R-DM23 之三處語意別補註
6. R-G16 對十支腳本之複查結果，逐支列筆數變化
7. PROXI 兩個 NODE 欄之實測與可用性判定
8. 037 八條之逐條精讀輸出
9. SYS2 兩個 Polarion 分頁之實測（或順延之理由）
10. **「本包是否仍有該驗而未驗者」之獨立判斷**
11. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-DM22 | 縮寫錨 `glossary_phrase`；每條須引並列出處 | Display | 是 |
| R-DM23 | 未追查 ≠ 查無；`none` 須標語意別 | Display | 是 |
| R-G16 | 量測與聚合分離；分隔符、多值、選定判準三拘束 | 全域 | 是 |
| R-G13 補充 | 查詢鍵不限於 DBC | 全域 | 是 |

四條皆為獨立單一事項。
