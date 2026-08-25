# 下放包 28 —— CFTS_013 全文驗明、2021 矩陣判讀、007／008 批次（rvc-01）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/28_cfts013_full_and_rvc.md`
- **本包對交付物之推進：第二批 TC（007／008）；DR-DM4／DM10(b) 之量測**（R-G31）
- **前置（已查證）**：上繳包 27 已回全綠；A 類 5 項；綁定 `entries: 12`／
  12 of 12；R-DM 區塊 56，順序驗證 exit 0。
  **CFTS_013 全文 docx 已由 Pei 置入**（R-G35(a)，分析層以
  `get_file_info` 確認存在：520,083 B，mtime 2026-08-25 23:04）：
  `inputs/R1LR_Atl-H_26PI2.5 Jun Release-Activation and Configuration_CFTS_013_Radio Error Management_20260608-1149.docx`
  分析層**未讀其內容** —— 全部量測屬本包任務 A。

三項任務互不阻塞：A（CFTS_013）、B（矩陣判讀）、C（rvc-01 批次）。
任一停手不波及其餘。

---

## 一、任務 A —— CFTS_013 全文之驗明與抽取（DR-DM4／DM10(b) 之量測）

> 檔名顯示其 release 家族為 `26PI2.5 Jun Release`（2026-06-08），
> **與 CFTS_020 之 `26PI1.5 Mar Release` 不同期**。此差異須記入台帳，
> 是否構成版本錯配屬 Tier 2，量測後回報，不逕判。

A1. **台帳與綁定**：SHA256、mtime 入素材台帳；`reference:` 增
    `cfts013_doc`（**與 `cfts013_sysra` 分列** —— 一為規格本文、
    一為 SYSRA 分析，兩份不同檔），綁定 **13 項**、`entries: 13`。

A2. **DR-DM4 三條之抽取**（機器抽取，R-G36）：
    `{CFTS013-629}`／`{CFTS013-633}`／`{CFTS013-952}` 之逐字全文。
    - **判準為條號錨定**（R-DM52：`Document ID`／條號本體，
      非全檔子字串命中）
    - 查得 → 逐字全文入上繳包；**是否結案 DR-DM4 屬分析層**，
      本包只量測
    - 查無任一 → 停並回報（停止條件 71）

A3. **DM10(b) 之對照量測**：629／633／952 若查得，逐字回報其中
    DCSD 側 Display Hot 演算法之：
    (i) 分段變數（溫度？時間？）；(ii) 各級門檻值與單位；
    (iii) warning → off 之轉換條件；(iv) 回復條件。
    **只抽取並列表，不與 CFTS_020 之 85 併算、不下「何組為準」之判斷**
    （那是 DR-DM10(a)，屬上游）。

A4. **佔位符複核**：全文搜 `{CFTS013-XXX}` 字面（DM10(c) 之標的）
    與 `CFTS013-967`（B2）。計數附口徑（R-G16）。

A5. **A-DM37 三句之對照**：`-1192`／`-1197`／`-1194` 三個 id 在
    全文 docx 內是否同為殘句。SYSRA 之樣板殘渣若源自本文，
    其性質由「SYSRA 撰寫殘渣」升為「規格本文殘渣」，須記明。

---

## 二、任務 B —— 2021 Priority Matrix 之判讀（DM2 降級可行性，只回報）

對 `inputs/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`
（已綁定，`dc078763…`）作結構判讀：

B1. 其是否含**可機器化之仲裁順序**（矩陣／排序表／優先級數字）？
    抽樣三格逐字回報其形態。
B2. 其涵蓋之 popup id 集合與 `Pop Up List HMI R1 (26PI).xlsx` 之
    id 集合之交集／差集（**特別報 `PU0517`／`PU0130` 在不在矩陣內**）。
B3. 其版本（SR24 1A，2021）對 26PI 素材之潛在時差：矩陣內 id 有而
    26PI Pop Up List 無者幾個、反向幾個 —— **此數字即「2021 版是否
    仍可用」之證據基礎**。
B4. **不產出 `popup_priority.tsv`**。本任務是判讀，A4 之交付物
    待判讀結果與 DM2 之降級裁定（Tier 2）。

---

## 三、任務 C —— 007／008 批次生成（`rvc-01`）

### 3.1 範圍與框架

| 項 | 值 |
|---|---|
| leaf | `SWE1-DM-007`、`SWE1-DM-008`（framework 第四組，8/8 複驗已過） |
| test_group / test_set | `Display` / `Rear View Camera` |
| 批次檔 | `generated/rvc-01.json`（結構同 pilot-01：`deferred` 為 R-DM53 四鍵物件、R-DM54 lifted 語意） |
| 寫回 | **不寫回**（與 pilot 同，待 Pei 覆核） |

### 3.2 生成拘束（全部承襲，逐條有據）

1. **canon 全套**：§4.3 三形 tc_title、R-S4 兩段式 test_item、
   §4.4 PC 僅狀態、§5.5 Final Step、§6 無情態 ER、§9 十七項自檢
2. **R-G33(a)(b)(c)(d)**：ER 不涵蓋之上半面向 → 括號下半指名；
   deferred 項四鍵、token 宣告端決定；產出後跑 `check_disclosure.py`
   雙向皆 0
3. **訊號值（R-DM48／A-DM35 條款層級判定）**：
   - 條款逐字用短拼法（`= [RR_CMRA]` 等）→ **得寫 raw**
     （`$DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA)`，
     `signal_resolution.py` 選定判準不變）
   - 條款逐字用長拼法（`= [DISP_OFF]` 等）→ **不得寫 raw**，
     ER 改驗規格所載之可觀察行為（DR-DM9(a) 未結）
   - `$TGW_DISP_STAT$` 之值一律不得寫 raw（DR-DM9(b) 未結）
   - 逐條之拼法判定記入 `reasoning`
4. **R-DM51(a)**：CFTS013 之門檻（50／51／55／56／60）不得出現於
   DCSD 標的之 TC（停止條件 60 續用，掃描範圍含本批）
5. **RVC 為高優先畫面**：`{CFTS013-937}` 之優先序為 **HU 側**事實；
   DCSD 側之 RVC 優先行為以 CFTS_020 之 RVC 諸條為據，
   兩側不得混引（R-DM51(c)：引 CFTS013 之值須記其標的）
6. **§8.3 sibling 軸之分解記錄**：007／008 各自之軸
   （觸發／狀態／負向／邊界）列於 `reasoning`；
   一 TC 一驗證目標（§5.7），單一觸發之多重後果併一條多行 ER
7. **priority 依 §10.2**：RVC 涉安全視野，P0／P1 之判定附一句理由

### 3.3 產出後之機器檢查（全套）

`lint036.py --profile display`（拋棄式複本、母本 sha 前後不變）、
§9 十七項逐 TC、`check_disclosure.py`、tc_title 相異、
I-sibling 具名、綁定 13 項（任務 A1 之後）。

---

## 四、停止條件

沿用 1–70，另加：

71. 任務 A2 之 629／633／952 任一**以條號錨定查無** → 停任務 A
    後半（A3），A2 之查證結果照報；任務 B／C 續行。
72. 任務 C 若 007／008 之 037 需求文與 SYS2 RVC 12 列出現
    追溯斷裂（leaf 引之章節在 SYS2 無對應列）→ 該 leaf 停，
    另一 leaf 續行，斷裂證據入上繳包。
73. `rvc-01` 之任一 TC 若需引 CFTS_013 全文之值 → **停該 TC**
    （本批之值域來源為 CFTS_020＋DBC；CFTS_013 之採用待 DM4／
    DM10 之裁定，不得由批次先行引入）。

**全部 git 操作屬 Pei。**

---

## 五、上繳包要求（`docs/upstream/28_cfts013_full_and_rvc.md`）

1. 任務 A：台帳、綁定 13 項（`entries: 13`）、629／633／952 逐字全文
   （或查無之證據）、DM10(b) 四項對照表、佔位符計數、A5 對照
2. 任務 B：B1–B3 之判讀結果（含抽樣逐字與 id 交差集數字）
3. 任務 C：`rvc-01` 全部 TC 之十欄全文、`reasoning`（含逐條拼法判定
   與 sibling 軸）、deferred 陣列、三項機器檢查全輸出
4. 未驗項分流（A／B，R-G29）
5. 建議之 commit 訊息與 pathspec（不執行）
