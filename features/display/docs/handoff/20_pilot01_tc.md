# 下放包 20 —— A-DM32 裁定：值標籤缺 DBC 對應時之寫法；pilot-01 解封

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/20_pilot01_tc.md`
- **本包對交付物之推進：pilot-01 之三條 TC**（R-G31）
- **前置（已查證）**：上繳包 19 已回（`docs/upstream/19_consolidated.md`
  存在）；步驟 1–12、15 完成；`framework.md`、`BACKLOG.md`、
  `batches/pilot-01/batch_context.md` 皆已落檔；綁定 11/11；
  `DECISIONS.md` 已簽核且 `recon.py` 回 `REFUSED (R-C9)`

---

## 一、上繳包 19 之覆核

**核可。停止條件 46 之觸發正確，且拒絕做那個對應是對的。**

### 1.1 錯在下放包 18 §二.2，錯在分析層

18 §二.2 寫「值標籤 `DISP_HOT`／`DISP_OFF`／`DISP_NORMAL`，出處：
`data/signal_resolution.tsv`，三段鏈解至 DBC」。

**那三個標籤中只有 `DISP_HOT` 解得到 DBC。** 另兩個我是從 SYS2 之
`[VALUE]` token 清單抄來的（`DISP_OFF` 15 次、`DISP_NORMAL` 12 次，
下放包 05 之量測），**然後把「SYS2 有」寫成了「三段鏈解至 DBC」**。

這是把兩個不同來源的東西掛在同一個出處聲明底下。與 18 包檔頭那句
「前置：17 已執行」同型 —— **未查證之聲明，寫得像已查證。**

### 1.2 §7.2 之三項理由 —— 第 2 項最重要

執行層拒絕只交 #1，三項理由中第 2 項採認並記明：

> 對一條殘批執行 `lint036.py`，其 PASS 之涵蓋面會被誤讀為整批。

**這是 R-G26 在一個我沒預見的場合生效。** 該條立時針對的是綁定檢查之
`5 of 5`；此處是「一條 TC 全過」被讀成「這一批全過」。母體錯了，
綠燈只證明錯的那組東西彼此一致。

### 1.3 §3.1 —— `paths:` 與 `reference:` 之路徑基準不同

`resolve_glob()` 之基準是 feature 目錄，`verify_reference_binding.py`
之基準是 repo 根。**19 包步驟 7 只寫「納入」，未指明此事。**

執行層依 `home` 之既有先例處置（複本入 `inputs/`，SHA 逐檔相符），
並指出 R-DM38 講的是**用途**不是**基準**。採認，補條文見 §四 R-DM47。

### 1.4 §5.2 之自查

R-DM35(b) 之一次違反（未先改名即讓 `DECISIONS.new.md` 被覆寫），
自查、以 `git show HEAD:` 取回、加註保留。差異僅
`source files 5 → 7`。**程序違反屬實，內容未失，處置得當。**

### 1.5 §5.1 之附帶發現

`Contested attributions` 一項亦改 `[RULED]`，而**該項不在簽核稿所列
之三項內**。執行層單獨記出，未併入三項之計數。正確 —— 簽核稿之
「三項」是分析層之列舉，實際受影響者為四項，兩者之差須看得見。

---

## 二、A-DM32 裁定

### 2.1 問題之精確形狀

| 側 | 寫法 | 出處 |
|---|---|---|
| 規格（SYS2／CFTS） | `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]`／`[DISP_REAR_CAMERA]` | SYS2 `[VALUE]` token |
| 訊號（DBC＝LID，兩權威逐字一致） | `0 "OFF"` `1 "ON"` `2 "BLANK"` `3 "RR_CMRA"` `4 "DISP_HOT"` `7 "SNA"` | `DCSD_DISP_STAT` 之 `VAL_` |

**唯一逐字相符者：`DISP_HOT` = raw 4。**

執行層之判斷正確：`DISP_OFF → 0 (OFF)` 是推論。而
`DISP_REAR_CAMERA → 3 (RR_CMRA)` 更清楚地證明**不存在單純的
`DISP_` 前綴規則** —— 若有，`RR_CMRA` 應寫作 `DISP_REAR_CAMERA` 之
去前綴形 `REAR_CAMERA`，而它不是。**六個值裡的規則不一致，
正是不能外推的理由。**

### 2.2 裁定：三途皆不單獨採，改為「按可得性分寫」

執行層所提三途，各有其不可採之處：
(a) 對照表 —— **現在沒有並列出處可建**（R-DM22 之三要件不滿足）；
(b) 一律寫 DBC 側 —— 需要先知道 `[DISP_OFF]` 對應哪個 raw，
    即問題本身；
(c) 只開 DR —— 三條 TC 全部凍住，而其中兩條之驗證目標**根本不需要
    那個值**。

**裁定（R-DM48）：TC 之 ER 一律驗規格所載之可觀察行為；
訊號值只在其標籤逐字解得 DBC `VAL_` 時才寫入。**

理由：004／005 兩條 leaf 之需求標的是**顯示行為**（亮度降低、
顯示關閉、恢復），不是匯流排上的某個 raw 值。CFTS
`{4820288}`（HU 恢復正常顯示）、`{4820290}`（背光與觸控恢復、
DTC de-mature）**本身就是可觀察之行為陳述**，不經訊號即可判定。

即：**#2／#3 之阻塞不是缺值，是我在 18 §二.2 指定了一個它們不需要
的值。** 移除該指定，兩條即可寫。

### 2.3 逐條之可寫性（取代 18 §二.1）

| # | leaf | ER 之驗證對象 | 訊號值 |
|---|---|---|---|
| 1 | 004 | 亮度降低 ＋ `PU0517` 顯示（timeout 10） | **寫入** `$DCSD_DISP_STAT$ = 4 (DISP_HOT)` —— 逐字解得 |
| 2 | 005 | 顯示關閉 ＋ `PU0130` 顯示（timeout 10） | **不寫**；規格側之 `[DISP_OFF]` 記入 `reasoning` |
| 3 | 005 | 背光與觸控恢復、顯示回正常（`{4820288}`／`{4820290}` 之原文） | **不寫**；規格側之 `[DISP_ON]` 記入 `reasoning` |

三條皆可寫。**#2／#3 不得因「訊號值未寫」而降低 ER 之具體性** ——
其 ER 須逐字取自 CFTS 之行為陳述，非泛稱（§6 禁 `normal`／
`as expected`）。

### 2.4 同時開 DR-DM9

不因 2.2 之處置而免除向上游查證。**DR-DM9**（HIGH）：
請上游確認 SYS2／CFTS 之值標籤 `[DISP_OFF]`／`[DISP_ON]`／
`[DISP_NORMAL]`／`[DISP_REAR_CAMERA]` 各對應
`DCSD_DISP_STAT` 之哪一個 raw 值，並提供其並列出處。

取得後依 R-DM22 之三要件建值標籤 glossary，**屆時 #2／#3 之 ER
得增列訊號值**（增列不改變其既有之行為驗證）。

---

## 三、pilot-01 之生成（取代 18 §二）

除 §2.3 之訊號值處置外，18 §二.2（其餘值域與出處）、
§二.3（格式）**全部維持**，另補三項：

1. **溫度單位不統一之處置**：來源寫 `> 85 degrees C` 與 `<= 85 deg C`
   （執行層 §6 已測）。**兩處各依其原文，不統一**（§8.4.1：
   來源模糊即保留模糊）。於 `reasoning` 註明兩處單位寫法不同係來源如此。
2. **`PU0008` 不入本批** —— 執行層已判其為系統層而非螢幕層。
   於 `reasoning` 記其被排除及理由（§8.2.1 之委派記錄）。
3. **`test_item` 上半**取 037 原句 verbatim，token ≤ 50（R-3）；
   下半 `(...)` 之括號內容三條**不得逐字相同**（R-S4 之 sibling 區分）。
   #2 與 #3 同屬 005，其區分 token 尤須明顯（關閉 vs 恢復）。

---

## 四、裁決條文

```
R-DM47（`paths:` 與 `reference:` 之路徑基準不同）
`feature.yaml` 之兩節其路徑基準不同，宣告時不可互抄：

  `paths:`      —— 基準為 **feature 目錄**（`recon.py` 之
                    `resolve_glob()`）。宣告 repo 相對路徑會使
                    `recon.py` 以 `input not found` 中止
  `reference:`  —— 基準為 **repo 根**（`verify_reference_binding.py`）

`forms/` 之共用素材若須同時入兩節，依 `home` 之既有先例：
複本置於 `features/<f>/inputs/`（SHA 須與 `forms/` 之正本逐檔相符），
`paths:` 寫 `inputs/…`，`reference:` 寫 `features/<f>/inputs/…`。
`inputs/` 由 feature 之 `.gitignore` 排除，複本不入 git。

本條補 R-DM38 之未涵蓋處：該條界定兩節之**用途**
（`paths:` 記檔在哪、`reference:` 記檔是哪一份），**未及基準**。

實例（上繳 19 §3.1）：Pop Up List 兩檔首次以 `forms/…` 宣告於
`paths.popup_list`，`recon.py` 當場中止。
```

```
R-DM48（值標籤缺 DBC 對應時之寫法）
規格（SYS2／CFTS）所載之值標籤，其**逐字**解得 DBC `VAL_` 列舉者，
依 §8.7.5(a) 寫入 `= <raw> (<label>)`；**解不得者不寫入訊號值**，
ER 改驗規格所載之**可觀察行為**，規格側之值標籤記入 `reasoning`。

**不得以語意相近或前綴規則外推。** `DCSD_DISP_STAT` 之六個值中，
唯 `DISP_HOT`（raw 4）與規格側逐字相符；`[DISP_REAR_CAMERA]` 對
`RR_CMRA`（raw 3）證明不存在單純之 `DISP_` 前綴規則 ——
**規則在六個值裡就不一致，故不可外推**。

本條與 §8.7.5(g)（R-13：規格所載訊號名 DBC 查無時保留原文，
不代以語意相近之他訊號）同一理路：**代入會改變 TC 之驗證對象。**
差別在於 (g) 規制名稱、本條規制值。

適用之前提：該 leaf 之需求標的為可觀察行為。若某需求之標的
**就是**匯流排上的某個值，則其值不可得即為真阻塞，
應 deferred 並開 DR，不得以行為描述頂替。

配套：**DR-DM9** 已開（HIGH）。取得並列出處後依 R-DM22 之三要件
建值標籤 glossary，屆時得於既有 ER 增列訊號值 —— 增列不改變
其行為驗證，故不構成回修。
```

---

## 五、作業步驟

1. 抄錄 §四二條入 `features/display/RULINGS.md`（逐條獨立核對表）。
2. `DATA_REQUESTS.md` 開立 **DR-DM9**（內容見 §2.4，HIGH）。
   `ANOMALIES.md` 之 A-DM32 加註「已裁，見 R-DM48；查證面另開 DR-DM9」。
3. `batch_context.md` 依 §2.3 與 §三更新（訊號值處置、`PU0008` 排除、
   單位不統一之註記）。
4. **生成 pilot-01 之三條 TC**。
5. 逐條 canon §9 自檢十七項；`lint036.py` A–N 對**整批三條**執行。
6. 更新 `docs/INDEX.md`。

**不寫回 036 工作簿。**

---

## 六、停止條件

沿用 1–43、44–49（19 包），另加：

50. 任一 TC 之 ER 若須寫入一個未逐字解得 DBC `VAL_` 之值 → 停
    （R-DM48）。
51. #2／#3 之 ER 若因移除訊號值而落為泛稱（`normal`／
    `as expected`／`works correctly`）→ 停，**該條之 ER 須逐字取自
    CFTS 之行為陳述**（§6）。
52. 三條之 `test_item` 括號下半若有任二條逐字相同 → 停（R-S4）。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/20_pilot01_tc.md`）

1. §四二條之逐條抄錄核對表
2. DR-DM9 全文
3. `batch_context.md` 之更新差異
4. **三條 TC 全文**（10 key 齊備，§10.1）
5. 逐條 §9 自檢十七項
6. `lint036.py` 全文輸出（**整批三條**，附母體 `entries`／`rows`）
7. 未驗項分流（A／B，R-G29）
8. 建議之 commit 訊息與 pathspec（不執行）
