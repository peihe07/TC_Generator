# ANOMALIES — FW036 Privacy HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PVnn]` — **note**: `new_feature.py` generated the skeleton
with `A-PRnn` (`feature[:2].upper()`); the analysis layer's handoff bundle 00
§2 mandates `A-PVnn`. Reported as-is, NOT self-corrected (A-PV06, Tier 2).
PENDING entries block their batch until a Pei ruling lands; RESOLVED entries
record the ruling verbatim. Registration is Tier 1 (record + propose);
disposition is Tier 2.

---

## A-PV01 — 交付目標 workbook：以空白範本開工 — **RESOLVED（R23-1）**

原始登記（handoff 00 §4）：6 份素材中無任何含 `Test Case Specification` 分頁
之檔案，`workbook_state` 無法判定，P7 無寫回標的。

**2026-08-13 更新**：Pei 指示以空白範本開工，範本已入 `inputs/`：
`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification &
Result_SWQT_20260121.xlsx`（SHA256 `cd876c202c71e74b…`，rev C，2026-01-21）。

阻塞解除：`workbook_state` = **BLANK**（recon 實測，見 `RECON.md`）。

**殘留問題**：這是「通用範本」而非「Privacy 專屬 workbook」——封面
（`Cover 封面`）之 Author 空、Reviewer 為範本預設 `張愷霏 ErinKFChang`、
TC 分頁之 Scope / Purpose / Reviewer 三格皆空（見 A-PV08）。
建議處置：Tier 2 確認「以通用範本產生 Privacy 交付件」即為最終交付形態，
或 Tier 3 另索 Privacy 專屬 workbook。P4 可在此前提下啟動。


**裁決 R23-1（Pei, 2026-08-13）逐字**：

> 不另索 Privacy 專屬 workbook。
> 依據：範本第 10 列原廠樣本為 NR1L-AntiTheft-001，該範本本即供各
> feature 各自開工之用。

即「以通用範本產生 Privacy 交付件」就是最終交付形態。原登記之殘留問題
（封面 Author 空、Reviewer 為範本預設）由 **R23-5** 一併處置：
該區為表單自身之文件管制區，不動。

## A-PV02 — VF651 變體選擇 — **RESOLVED（R38 close-out，2026-08-14）**

**R-PV01(c) 已簽署（2026-08-13，分批簽署第一批）**：

> (c) amplified 在範圍內 → V6_R2 入 `inputs/`。
> 依據不是我的 docx 掃描，是需求本身：SWE1 十片葉子裡 -007/-008/-010
> （PROF-173/174/176）明文以 "AMP is present" 為前提。這條證據在 037 檔內，
> 不依賴任何待重驗項目。ANC 兩份（V9_R3/V11_R3）維持不索取。

裁決依據之性質值得記錄：**證據鏈完全落在 ruled 037 內**，不觸及 handoff §3.2
/ §3.3 / §3.4 那三組未重驗的單方掃描數字。故本裁決不受 §7.6 之五項未驗項影響，
可獨立生效 —— 與 (a) 之延後理由（縮範圍、依賴未重驗證據）形成對照。

執行層已辦：
`Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx`
已入 `inputs/`（184,808 bytes，SHA256
`49dd3c31405fb0c34d4cf11048d325d6f047c0d333c10248310e72c57e194fbb`）。

**ANC 部分結案（R38 close-out，2026-08-14）**：十片葉子全數完成生成、
lint 與寫回，**無一觸及 ANC 配置** —— `Not requested` 之條件式停手
（「若 P2 解析發現任一 leaf 觸及 ANC 配置則停手回報」）自始未觸發。
V9_R3 / V11_R3 維持不索取，`DATA_REQUESTS.md` #3 維持 Not requested。
本條由 PENDING 轉 **RESOLVED**。

## A-PV02b — 原 A-PV02 之背景（保留供追溯）— 已被上條取代

手上 2 份（V2_R2 LTM Non-Amplified、V3_R3 ETM Non-Amplified）僅覆蓋
Non-Amplified 一格，全集為 5 變體（V2_R2 / V3_R3 / V6_R2 / V9_R3 / V11_R3）。
037 之 10 leaves 中 -007 / -008 / -010（PROF-173/174/176）明文以「AMP is
present」為前提，-006 / -009 以「AMP is not present」為前提 —— AMP-present
情境確在需求範圍內，Non-Amplified 單一變體不足以支撐。

**2026-08-13 執行層實測補充**：來源目錄
`10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/` 現為 **7 檔**，較 handoff 00
§1 所列 6 檔多出
`Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx`
（184,808 bytes，mtime 2025-05-22）—— 即 DATA_REQUESTS #2 所索之檔。
**未複製入 `inputs/`**：R-PV01(c) 未簽署，且 canon §6 停手條件（本 feature
特化）禁止在 5 個變體間自裁取捨。等待裁決後再納入。

## A-PV03 — ETM V3_R3 疑非本專案適用件 — **DEFERRED — 待 P2 證據重驗（R-PV01(a)）**

證據：CFTS022 之 `R1L-R` × ETM-only artifact = 0 行；SYS.2
`VF651_Audio_Output_Management/` 8 個子目錄無任何 V3。

**Pei 裁示（2026-08-13）**：

> (a) 排除 ETM V3_R3 → 延後到 P2。那五個數是我單方掃描，未經重驗，
> 而排除是「縮範圍」，錯了會漏驗。V3_R3 就留在 `inputs/` 不引用，零成本。
> P2 重驗後再簽。

**狀態依 R15-2 更正（下放包 04 §2.5 掃描，2026-08-13）**：本條原標 `PENDING`，
但 R-PV01(a) 已簽署且結論即為「延後至 P2」—— 屬「已裁而結果為延後」，
依 R15-2 不得留在 Open PENDING，改標 `DEFERRED — 待 P2 證據重驗`。
語意未變，只是狀態欄不再假裝這條在等裁決；它等的是重驗。

執行層據此：V3_R3 **留在 `inputs/`**，狀態為「在庫、不引用」——
不得列為 `specification_reference`，也不得因未列而視為已排除。
P2 進場時必須先重驗 handoff §3.2 / §3.4 兩組數（見 §7.6 未驗清單第 1、3 項），
重驗結果回報後才簽 R-PV01(a)。

**非對稱原則（本次確立，值得沿用）**：擴範圍的裁決（(c) 納入 V6_R2）證據若
自足即可立即簽；縮範圍的裁決（(a) 排除 V3_R3）因錯誤代價是「漏驗」而非
「多驗」，必須等證據重驗完成。兩者不必同批處理。

## A-PV04 — 同名不同內容（VF651_V2_R2）— **RESOLVED（R23-2）**

handoff 00 §4 只有 size 比對（未 hash）。執行層依 §7.4 補算 SHA256，
全庫掃描 `*VF651_V2_R2.docx` 得 **7 個路徑、5 種內容**：

| SHA256（前 8） | size | 路徑 |
|---|---|---|
| `d5813bb7` | 146,929 | `10_Reviewing/…/Privacy Mode/`（＝ `inputs/` 這份）|
| `d5813bb7` | 146,929 | `VF/VF_Split document/HDCC28_Split/` |
| `7b5fc875` | 146,899 | `VF/28HDCC_2A_LTM/LTM/VF - Functional Requirements/` |
| `dca55fc9` | — | `VF/VF_Split document/DT28_split/` |
| `6101f93b` | — | `Development Docs/27DT 2A_LTM/LTM/VF - Functional Requirements/` |
| `c8bd81fd` | — | `VF/28DT_2A_LTM/LTM/VF - Functional Requirements/DT28_split/` |
| `6ea616ed` | — | `VF/DT27_2A/27DT 2A_LTM/LTM/VF - Functional Requirements/` |

結論：交付夾那份與 `HDCC28_Split` **確為同源**（hash 相同，非僅 size 相同）；
`28HDCC_2A_LTM` 那份 **確為不同內容**，不得假設為重存。DT 系列（DT27/DT28）
另有三種內容，本專案為 HDCC28 平台，暫不列入。
建議處置：`inputs/` 現有這份（`d5813bb7`）視為 HDCC28 基線，Tier 2 追認。


**裁決 R23-2（Pei, 2026-08-13）逐字**：

> `inputs/` 現有之 SHA256 `d5813bb7…`（146,929 bytes）為 **HDCC28 平台
> 基線**，與 `VF/VF_Split document/HDCC28_Split/` 同源（hash 相同，非僅
> size 相同）。`28HDCC_2A_LTM/…` 之 `7b5fc875…` 確為不同內容，不得假設
> 為重存。DT 系列（DT27 / DT28）另三種內容不列入本專案。

**注意本裁決之範圍僅及 V2_R2。** 下放包 01 §2 之基準確認另發現 **V6_R2**
之 `inputs/` 副本對齊的是 **DT28** 樹而非 HDCC28 —— 該項另立
**A-PV14**，不因 R23-2 而解決。

## A-PV05 — SYSAD 混入 `cfts_doc` 分類 — **RESOLVED（R23-3）**

`SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` 為 SYS.3 架構
設計，非 CFTS 規格；`intake.py` 依副檔名把 `.docx` 一律歸 `cfts_doc`，實測
確已如此分類（見 `_intake` 產出之 `INTAKE.md`）。其角色是背景理解，
**不得作為 `specification_reference`**（§10.7 禁止引用分析類文件）。
建議處置：`feature.yaml` 標為 context-only。


**裁決 R23-3（Pei, 2026-08-13）逐字**：

> `SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` 於
> `feature.yaml` 標為 **context-only**。**不得**作為
> `specification_reference`（§10.7 禁引分析類文件；SYSAD 屬設計非規格）。
> 其角色限於背景理解。

執行層已辦：`feature.yaml` 之 `paths` 區加 `context_only` 清單並註明依據。

## A-PV06 — abbr `PR` vs `PV` — **RESOLVED（R-PV02, 2026-08-13）**

`new_feature.py` 取 `feature[:2].upper()` → **`PR`**；產生之骨架寫
`[A-PRnn]` / `[ASSUMPTION A-PRnn]`。

**Pei 裁決 R-PV02（2026-08-13）**：

> anomaly 前綴：`A-PV`，維持現況，不改 script
> TC id：`NR1L-Privacy-{NNN}`
> 依據：範本第 10 列的原廠範例就是 `NR1L-AntiTheft-001` —— 大小寫混合、
> 完整 feature 名，不是兩字母縮寫。照範本走。

執行層已辦：

1. `ANOMALIES.md`（本檔）用 `A-PVnn`，檔頭註明與 script 骨架之落差。
   `new_feature.py` **未動**。
2. `feature.yaml` 之 `write_back.tc_id_format` = `"NR1L-Privacy-{n:03d}"`，
   註解記載依據為範本樣本列形態。

**與 SXM 之慣例差異已知且刻意**：SXM 用 `NR1L-SXM-{NNN}`（取 `test_group` 之
縮寫），Privacy 用完整 feature 名。裁決依據是範本原廠樣本 `NR1L-AntiTheft-001`
本身就是「完整 feature 名、大小寫混合」形態，Home 交付之 `NR1L-HomeHMI-nnn`
亦然 —— SXM 的三字母是該 feature 名稱本身就是縮寫，非另立規則。

---

以下為 **Phase 1 recon 對空白範本實測新增**，handoff 00 未涵蓋。

## A-PV07 — 範本殘留樣本列（第 10–11 列）— **RESOLVED（R23-4，清除已執行）**

`Test Case Specification 測試用例規範` 分頁第 10–11 列帶範本示例殘留：

| cell | 值 |
|---|---|
| B10 / B11 | `1` / `2`（No.# 序號）|
| D10 / D11 | `xxx` / `xxx`（Requirement or Design ID）|
| F10 | `NR1L-AntiTheft-001`（Test Case ID）|
| G10 | `AntiTheft`（Test Group）|
| S10 | `NA`（Functional Safety）|

第 12–59 列全空。實測影響三處：

1. `recon.py` 判為 `rows 10-11: DRAFT (2 rows)`；因 done rows = 0，狀態仍落在
   `BLANK`（`recon.py:245`「drafts only: no done region」分支），與預期一致。
2. `xxx` 被登記為 traceability orphan（`RECON.md`「draft region: 1 ['xxx']」），
   是假陽性。
3. `intake.py` 之 `_workbook_profile` 讀第 10 列 D 欄推需求族 → 產出
   `rows trace xxx`（見 A-PV08 同一則 note）。

建議處置（**清除計畫，待 Tier 2 核可後才動手**）：

**修訂版（2026-08-13，A-PV09 實測後）** —— 原計畫寫「清空 B10:AH11 的值」，
實測 sheet XML 後發現兩點須修正：

1. **B 欄不必清，也不該清。** B10 實際內容是公式
   `=IF(ISBLANK($D10),"",ROW()-9)` —— 序號是自 D 欄推算的，
   清掉 D10 後 B10 自動顯示空白。手動清 B 欄反而會刪掉範本的序號機制。
   真正帶殘留「值」的只有 **D10 / F10 / G10 / S10 / D11** 五格。
2. **清除方式改為 zip 層外科手術**（A-PV09 策略 2）。範本這幾格的 XML 形如
   `<c r="D10" s="81" t="s"><v>44</v></c>`，就地換成
   `<c r="D10" s="81"/>` 即可 —— 值清掉、`s="81"` 樣式屬性原地保留，
   列高框線 DV 一律不動。已在探針中實測通過（五格清除後 openpyxl 讀回
   全為 `None`，B10 公式完好）。

原則不變：**不採「整列刪除」** —— 會連帶把 DV sqref 與 R10 的 x14 DV 移位。
BLANK 策略為「append from first data row」＝第 10 列，清乾淨後首筆 TC
即落第 10 列，`NR1L-Privacy-001` 起算（R-PV02）。


**裁決 R23-4（Pei, 2026-08-13）—— 核可修訂版計畫，逐字**：

> (1) 僅清 **D10 / F10 / G10 / S10 / D11** 五格之值
> (2) 方式為 zip 層就地改寫：
>     `<c r="D10" s="81" t="s"><v>44</v></c>` → `<c r="D10" s="81"/>`
>     —— 值清除、`s=` 樣式屬性原地保留
> (3) **B 欄不清** —— B10 為公式 `=IF(ISBLANK($D10),"",ROW()-9)`，
>     序號自 D 欄推算，清 D10 後自動空白；手動清 B 欄會刪掉範本之序號機制
> (4) **不採整列刪除** —— 會使 DV sqref 與 R10 之 x14 DV 移位

**已執行（2026-08-13）**，走 `backend/xlsx_surgical.py`（R18-3 規則 1 之
首次正向適用）。四組比對全數相符：五格讀回全 `None`、B10 公式完好、
zip 成員 48→48 零增零減、DV 4/2→4/2。

**輸出未寫入 `inputs/`**：客戶原件 SHA256 `cd876c202c71e74b…` 逐 byte 未動
（已驗證）。產物於 `features/privacy/output/`。

## A-PV08 — 表頭六格 + intake 誤讀 Scope — **RESOLVED（R23-5，D5 已填）**

TC 分頁表頭區實測：

| cell | 標籤 | 現值 |
|---|---|---|
| D2 | 專案名稱 Project Name | `newR1L` — 範本預設，**應改為本專案代號** |
| C3 → D3 | 審查者 Reviewer | **空** |
| C4 → D4 | 目的 Purpose | **空** |
| C5 → D5 | 範圍 Scope | **空** ← 待填 |
| J5 | 日期 Date | `2025/10/17` — 範本預設 |
| AH5 | 表單編號 | `FM-WI-FSM-036-A01` |

**intake.py 誤讀**：`_workbook_profile` 先把該列非空儲存格壓成緊密 list 再取
「Scope 標籤的下一格」，因 D5 為空，取到的是 I5 的標籤字串，故
`INTAKE.md` 印出 `Scope: 日期 Date：`。這是假值，非真 Scope。
在 AMFM 走的是同一段程式且 D5 有值（`FM-WI-SW-RAD-SWRA-A02`）故未暴露。
影響有限：Scope 僅在「多份 037 需仲裁」時被使用，Privacy 只有一份
（`SWE1_CFTS_022-Privacy_Features.xlsx`），仲裁未觸發。

**Scope 欄待填值（提案，Tier 2 裁定）**：比照 AMFM 慣例填「本 workbook 之
ruled 037 來源識別碼」，即 `SWE1_CFTS_022-Privacy_Features`
（該檔 cell AI2 標 `FM-WI-FSM-037-A03`，但檔內未給 037 文件編號，
故無法比照 AMFM 填 `FM-WI-SW-xxx-SWRA-Axx` 形式）。
Reviewer / Purpose / Project Name / Date 一併待 Pei 給值，執行層不自填。


**裁決 R23-5（Pei, 2026-08-13）—— 含分析層自我更正，逐字**：

> 分析層更正：原建議「D3 Reviewer 與 Cover 封面 Reviewer 由 Pei 給值、
> 交付件不該帶範本預設人名」**有誤**。

| cell | 欄位 | AMFM 已交付件實測 | Privacy 裁定 |
|---|---|---|---|
| D2 | 專案名稱 | `newR1L` | 維持 `newR1L` |
| D3 | 審查者 Reviewer | **空** | **留空** |
| D4 | 目的 Purpose | **空** | **留空** |
| D5 | 範圍 Scope | `FM-WI-SW-RAD-SWRA-A02` | `SWE1_CFTS_022-Privacy_Features` |
| J5 | 日期 Date | `2026/1/29`（交付日）| 交付日填，現在不預填 |

> Cover 封面之三格（核准者 / 審查者 / 作者）**一律不動**：此為
> **FM-WI-FSM-036-A01 表單本身之文件管制區**，記錄的是「誰核准了這份
> 表單」，非「誰審查了本次交付內容」。

**§5a（本裁決所立）**：表單自身之文件管制欄位與交付內容之責任欄位是兩件事；
判定某欄屬何者，須以同表單之已交付實例為據，**不得由欄位名稱推斷**。
—— 執行層原提案正是「由欄位名稱推斷」而錯，記為教訓。

**已執行**：D5 = `SWE1_CFTS_022-Privacy_Features`，讀回相符。
D2 / D3 / D4 / J5 與 Cover 封面四格經比對確認未變。

**intake 誤讀 bug 之實測（本包 §5.5 要求）**：D5 填入後，
`_workbook_profile` 之輸出由 `'Scope: 日期 Date：; rows trace xxx'`
變為 `'Scope: SWE1_CFTS_022-Privacy_Features; no data rows'` —— 症狀消失。
**但 bug 未修**：該函式仍以「壓縮非空儲存格後取下一格」定位 Scope 值，
只是 D5 有值時該壓縮恰好落點正確。**任何 D5 為空的 workbook 仍會複現。**
依本包指示未修程式碼。

## A-PV09 — openpyxl 寫回會損毀範本 — **CLOSED，已升格為常設規則 R18-3**（2026-08-13）

> **升格記錄**：本條原為 Privacy 單一 feature 之 anomaly。分析層據其實測
> 對 AMFM 客戶原件複驗，證實同一缺陷已造成 **AMFM v1 交付件缺 21 個 zip
> 成員**，遂簽 **R16 凍結令**（全文見 `features/amfm/RULINGS.md`）：
> 全 repo 寫回凍結、AMFM v1 停止送出、Home/SXM 回溯檢測、升 canon 條文。
> 執行層已完成 writer 改造（`backend/xlsx_surgical.py`）與四 feature 檢測，
> 結果見 `features/amfm/docs/upstream/02_integrity.md`。
> **本條先前建議之「分析層評估是否升為 canon 層條文」已獲採納並執行。**
>
> **2026-08-13 後續（R18-3）**：R16-2 之凍結令已解除，代之以三項常設規則
> —— `xlsx_surgical` 為唯一寫回路徑、zip 成員與 DV 計數不等即 ABORT、
> 違反者升 Tier 2。反向測試見 `tests/test_xlsx_surgical_invariant.py`。
> 本條至此 **CLOSED**：Privacy 之 P7 直接適用該常設規則，無須再個別追蹤。

回溯檢測發現 SXM 之已交付件（同一份 rev C 範本）確已失去 R 欄下拉，
與本條之預測完全一致 —— 見 `features/sxm/ANOMALIES.md` A-SX28。

Pei 2026-08-13 指示「x14 DV 往返實測照辦，P4 前做」——**已於本次執行完畢**。
可複現腳本：`features/privacy/scripts/xlsx_roundtrip_probe.py`。

範本之「測試用例設計方法」欄（R）用的是 **x14 擴充 data validation**：

```xml
<x14:dataValidation type="list" …><xm:f>下拉選單!$A$1:$A$11</xm:f>
  <xm:sqref>R11:R59</xm:sqref></x14:dataValidation>
<x14:dataValidation type="list" …><xm:f>下拉選單!$A$1:$A$9</xm:f>
  <xm:sqref>R10</xm:sqref></x14:dataValidation>
```

### 實測結果 —— 損失範圍遠大於原先預估

基線：48 個 zip 成員，x14 DV `['R11:R59','R10']`，傳統 DV
`['P10:Q11','T10:Z11','AF10:AF11']`。

**策略 1：openpyxl load → mutate → save = LOSSY**

- x14 DV 全失：`R10`、`R11:R59` 兩組都不見 → R 欄下拉消失（原預估命中）
- **原先未預料的額外損失**：
  - `xl/printerSettings/printerSettings1–5.bin`（5 個）全數丟失 → 列印設定歸零
  - `xl/drawings/vmlDrawing1.vml` + `xl/comments1.xml` 被改寫為
    `xl/drawings/commentsDrawing1.vml` + `xl/comments/comment1.xml`
    → 舊式註解的 VML 外框格式重繪
  - `xl/media/image2.jpeg` → `image2.png`，並多出 `image3–9.jpeg` 共 7 個
    → 內嵌圖片被重新編碼與複製
  - `xl/sharedStrings.xml` 消失，字串改為 inline（`<is><t>`）
  - `xl/worksheets/_rels/sheet8.xml.rels` 丟失
- 傳統 DV（P / T–Z / AF）確實保留 —— 這是唯一符合原預估的部分

**策略 2：zip 層外科手術（只換目標 sheet XML，其餘成員 byte-for-byte 複製）
= LOSSLESS**

- x14 DV 完整保留、傳統 DV 完整保留
- 48 個 zip 成員零增零減
- 寫入值可正確讀回；且範本的 styled-empty cell（如 `<c r="I10" s="81"/>`）
  是就地換內容，**樣式屬性隨之保留**，不需重建

### 處置（已定）

**P7 寫回一律走策略 2。** `backend/writer.py` 若以 openpyxl 存檔，
不得用於本 feature 之交付件產出；需要時另接外科手術寫入路徑。
探針腳本已入 repo，P4 前與任何 writer 改動後都應重跑一次確認 `LOSSLESS`。

**外溢提醒**：這不是 Privacy 特有問題，是 **FM-WI-FSM-036-A01 rev C 範本本身**
的性質。其他以此範本開工的 feature（SXM 亦為 BLANK + 同範本家族）有相同風險，
建議分析層評估是否升為 canon 層條文。

## A-PV10 — 下拉選單清單範圍與內容不一致 — **RESOLVED（R23-6，處置已定，缺陷續存於上游）**

`下拉選單` 分頁實有 **9** 個詞條（A1:A9），A10 / A11 為空。
但 R11:R59 的 DV 指向 `$A$1:$A$11`（含 2 個空選項），R10 指向 `$A$1:$A$9`。
同一欄兩種範圍，且較大那組帶空白項。
建議處置：登記即可，範本瑕疵屬上游；lint 以 A1:A9 之 9 詞條為準
（`feature.yaml` 之 `lint.design_method_source: dropdown_sheet` 即取此分頁）。


**裁決 R23-6（Pei, 2026-08-13）逐字**：

> 範本瑕疵屬上游，**登記即可，不修**。lint 以 `下拉選單!A1:A9` 之 9 詞條
> 為準。R10 指向 `$A$1:$A$9`、R11:R59 指向 `$A$1:$A$11`（含 2 空項）
> 之落差不修，隨 RD-1 回報上游。

狀態為 RESOLVED 係指**處置已定**，缺陷本身續存於上游範本。

## A-PV11 — `Reference` 分頁與 `下拉選單` 詞條字串不符 — **RESOLVED（R23-7）**

`lint.design_method_source` 要求 exact-string 比對，兩分頁第 6 條不一致：

- `下拉選單!A6` = `組合測試 (Combinatorial Testing ; Pairwise / t-wise)`
- `Reference!C9`  = `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)`

建議處置：以 `下拉選單` 為 lint 權威（DV 實際引用的是它）；`Reference`
視為說明性附表，不入 lint。回報上游修正。


**裁決 R23-7（Pei, 2026-08-13）逐字**：

> 以 **`下拉選單` 為 lint 權威**（DV 實際引用者）；`Reference` 分頁視為
> 說明性附表，**不入 lint**。第 6 條之落差
> （`Pair-wise / N-wise` 對 `Pairwise / t-wise`）隨 RD-1 回報上游。

## A-PV12 — `Cover_old` / `ChangeHistory_old` 舊版分頁殘留 — **RESOLVED（R23-8，案 1 原樣保留）**

範本含 9 個分頁，其中兩個為 2020–2021 年舊版遺留：

- `Cover_old`（A1:J15）：`Document: Test Case Specification & Result
  Templat_SWQT`、`Version: 1`、Approved by `Steve Tsai` 2020-12-07、
  Reviewed by `Dean Ku` 2020-11-05、Developed by `Andy Ko` 2020-10-05
- `ChangeHistory_old`（A1:J12）：僅 1 列 — `1 / Andy Ko / 2021-03-10 /
  Steve Tsai / Modify Logo、Name and Date`

現行封面為 `Cover 封面`（版本 C，核准者 劉安哲 AllenACLiu）與
`ChangeHistory 修訂履歷`（A/B/C 三列，C 版 2026-01-21 新增 Estimated Test
Time 欄），兩者已完整取代舊版。無任何 DV、公式或 defined name 指向 old 兩頁
（已掃 `xl/worksheets/*.xml` 之 x14 DV 與各頁 DV，均無跨頁引用）。

**處置建議（三案，Tier 2 擇一）**：

1. **原樣保留（建議）**——範本原貌即如此，交付件與公司範本逐頁一致，
   稽核時「為何少兩頁」不必解釋。兩頁不進 lint、不進 trace、不寫回。
2. 刪除兩頁——交付件較乾淨，但與 FM-WI-FSM-036-A01 原範本分頁數不符，
   且刪除屬對公司管制表單的結構性修改，超出執行層權限。
3. 保留但於 `Product Document 記錄封面頁` 註記「舊版分頁，僅供歷史對照」——
   需動封面頁，同樣屬表單結構修改。

執行層採 **案 1**（不動作）直到 Tier 2 另有裁示。


**裁決 R23-8（Pei, 2026-08-13）逐字**：

> 採**案 1 原樣保留**。兩頁不進 lint、不進 trace、不寫回。
> 理由：刪除屬對公司管制表單之結構性修改，且交付件分頁數與原範本不符時，
> 稽核反而須解釋「為何少兩頁」。
> 佐證：AMFM 之已交付件同樣保留 `Cover_old` / `ChangeHistory_old` 兩頁。

執行層原提案即案 1，獲採納；佐證由分析層自 AMFM 已交付件補實測。

## A-PV13 — scaffold 產出之 `feature.yaml` 欄位字母為 rev C 之前的版本 — **RESOLVED（R39-2，已修，2026-08-14）**

`new_feature.py` 的 `feature.yaml` 樣板寫 `design_method: Q` /
`functional_safety: R` / `author: Z`，範本 rev C 實際為 **R / S / AA**
（Q 已被 `Estimated Test Time (mins)` 佔用）。
`recon.py` 以表頭文字為權威、把落差列為 `feature.yaml column conflicts`
（`RECON.md` 已記三條），未受影響。另 `sheet` 樣板值
`"Test Case Specification&Result"` 與實際分頁名
`"Test Case Specification 測試用例規範"` 不符，會讓 `recon.py` 直接 `sys.exit`。

執行層處置：僅改 `sheet` 為實際分頁名（事實更正，非裁決），並把
`spec_pdf` / `popup_list` 設為 `null`（spec_mode D 無 PDF、未供 popup 清單）。
**欄位字母刻意不改**，保留給 recon 續報落差為證據。
`new_feature.py` 樣板本身之更新屬 repo 層改動，未動。

**最終處置（R39-2，2026-08-14）—— 已修，本條結案。**

| 欄位 | 修前（rev C 之前）| 修後（實測 rev C 表頭）|
|---|---|---|
| `design_method` | `"Q"` | **`"R"`** |
| `functional_safety` | `"R"` | **`"S"`** |
| `author` | `"Z"` | **`"AA"`** |

量測依據：範本 `Test Case Specification 測試用例規範` 第 9 列表頭逐格實測 ——
rev C 於 **Q** 插入 `Estimated Test Time (mins)`，使其後三欄各右移一格。

**修後行為驗證（停手條件 2）**：`recon.py` 仍為 `state=BLANK, leaves=10,
targets=10`，唯一變化是 `feature.yaml column conflicts` 由三條變為 `(none)`
—— 即落差回報消失，此為預期。全套測試 944 passed / 15 skipped 不變；
lint PASS；`write_back.py` 之欄位解析結果不變
（`design_method=R, functional_safety=S, author=AA` —— 它本就讀表頭，
不讀 `feature.yaml`，R37-3(a)）。**無其他讀取路徑受影響。**

---

**處置方向之更正（R39-2）**：執行層先前主張「不修 `feature.yaml`，
以保留 recon 之落差回報作為證據來源」。該理由**經裁定不成立**，三項駁回：

1. **證據不會因修檔而消失** —— 本 anomaly 條目自身即證據載體，
   上表之修前／修後值、量測依據與裁決編號，效力不弱於 recon 之逐次回報。
2. **保留已知錯誤作為告警來源，等同以缺陷充當金絲雀** ——
   代價是任何以本 feature 為樣板之後續 feature 會繼承錯誤字母。
3. R37-3(a) 已裁「位置資訊以標的物為準」，該三欄之字母對產出**無效力**，
   修正屬低風險。

§5a：**不得以保留缺陷之方式維持告警**；告警之正確載體是登記，不是缺陷本身。

---

**狀態沿革（保留供追溯）**：本條原標 RESOLVED，
但**落差本身從未消失** —— `feature.yaml` 之 `columns` 區仍記
`design_method: "Q"` / `functional_safety: "R"` / `author: "Z"`，
而範本 rev C 之實際位置為 **R / S / AA**。
先前之 RESOLVED 指的是「recon 會回報落差」，不是「落差已修」。
寫回腳本依 **R37-3(a)** 改由**表頭文字**解析欄位，該落差已不影響產出；
但記載仍為舊值。曾依 R15-2 改標 `DEFERRED — 記載與實作不一致`，
其後由 R39-2 裁定改修並結案（見上）。

---

## A-PV14 — V6_R2 之 `inputs/` 副本對齊 **DT28**，而 V2_R2 對齊 **HDCC28** — **RESOLVED（R29-2）**

**來源**：R22 §2 基準確認（2026-08-13）之副產物。原作業只要求判定
`inputs/` 檔是否與客戶樹相符（結果全數 `MATCH`），但逐檔列出**所有**同名
候選之 SHA256 後，浮現一件與判定無關、卻直接影響 spec 引用的事。

A-PV04 已就 `VF651_V2_R2.docx` 裁定：`inputs/` 那份（`d5813bb7…`）與
`HDCC28_Split` 同源，視為 **HDCC28 平台基線**。本次對 V6_R2 做同樣量測：

| 檔案 | `inputs/` SHA256 | 命中之樹內路徑 |
|---|---|---|
| `…VF651_V2_R2.docx` | `d5813bb7…` | 交付夾 ✔ ／ `VF_Split document/**HDCC28_Split**/` ✔ |
| `…VF651_V6_R2.docx` | `49dd3c31…` | 交付夾 ✔ ／ `VF/**28DT_2A_LTM**/LTM/VF - Functional Requirements/**DT28_split**/` ✔ |

**V6_R2 的 `HDCC28_Split` 副本是 `e20ba7a4…`，與 `inputs/` 這份不同。**

即：同一個交付夾（`10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/`）裡的兩份
VF651 檔，一份對得上 HDCC28 樹、另一份對得上 DT28 樹。

**候選分布（量測值）**：

| 檔案 | 樹內同名候選數 | 相異內容數 |
|---|---|---|
| `…V2_R2.docx` | 7 | 5 |
| `…V6_R2.docx` | 7 | **6** |
| `…V3_R3.docx` | 3 | 2 |

**為何重要**：本專案為 HDCC28 平台（A-PV04 之基線判定即據此）。
若 V6_R2 該引用的是 HDCC28 版而 `inputs/` 放的是 DT28 版，
則 -007 / -008 / -010（PROF-173/174/176，AMP-present 情境）
之 `specification_reference` 會指向錯誤平台的文件 —— 而 R-PV01(c)
簽署納入 V6_R2 的依據是「需求本身要求 AMP-present」，那條依據
不涉及平台版本，所以簽署時這個問題不可能被發現。

**不判定何者為正**（R22-5：分類承載因果假設時停在原始量測）。
可能是交付夾備錯、可能是 DT28 版才是本案適用、可能兩版在相關條文上無差異。
**執行層未做兩版的內容 diff** —— 那會暗示成因，且屬 P2 spec 解析範疇。

**建議處置（Tier 2）**：在 P2 引用 V6_R2 任一條文之前，先裁定平台版本，
或先做 `e20ba7a4…`（HDCC28）與 `49dd3c31…`（DT28）之全文 diff 再裁。
在裁定前 V6_R2 **不得列為 `specification_reference`**。

**相關**：A-PV02（R-PV01(c) 簽署納入 V6_R2）、A-PV04（V2_R2 之 HDCC28
基線判定）、`RULINGS.md` R22 / R15-5（同名檔一律以 hash 認定）。


---

### R24-2 執行結果（2026-08-13）

**(1) diff —— 已完成。** 全程唯讀，以 python-docx 抽段落＋表格文字後逐行比對。

| | HDCC28 副本 | `inputs/` 現存 |
|---|---|---|
| SHA256 | `e20ba7a4f8f7…` | `49dd3c31405f…` |
| bytes | 177,388 | 184,808 |
| 非空行 | 404 | 403 |
| 差異 hunk | — | **9** |
| SCV/AMP 相關行數 | **33** | **33** |
| **落在 SCV/AMP 條款之差異 hunk** | — | **0** |

比對詞集依 R24-2(1) 所列：`CTRL_AMP.*`、`$VolumeSCV$`、`Acustic_Configuration`
（含 `Acoustic_` 拼法）、`Audio_System_Type`、`amplifier` / `AMP ` 之
present / not present 敘述。

**九個 hunk 的性質**（皆不在上述條款內）：

| # | 內容 |
|---|---|
| 1 | 作者：`Keerthi Kambala` → `Abhishek Dwivedi` |
| 2 | 適用 VF 清單：`VF610` → `VF672` / `VF505` / `VF508` |
| 3 | 訊號表少 `ENGINE_FD_2.EngineSts_W` |
| 4 | 訊號表少 `BCM_FD_9.PowerModeSts` |
| 5 | 訊號表多 `TBM_FD_1.SOSCallType` |
| 6 | 訊號表少 `VSIM_FD_1.AudioMuteRq`（Audio mute request）|
| 7 | SGW gating 敘述 `B-CAN` → `BCAN`（同一 gating，寫法不同）|
| 8 | 修訂履歷（見下）|
| 9 | 純空白差異（`MdsActforANC` 後之空格數）|

**hunk 8 直接證明兩份的平台來源**：

```
HDCC28 −  Initial release derived from VF651_V6_R1_PHDCCMCA
inputs +  Initial release Derived from VF651_V6_R1_PDT26
```

`PHDCCMCA` 對 `PDT26` —— 稽核以檔案路徑推得的平台歸屬，在文件內文獲得
獨立佐證。A-PV14 的事實面至此無疑義。

**(2) 條件判定 —— 成立。** SCV/AMP 條款零差異，符合 R24-2(2)
「兩版於上述條款零差異 → 換入 HDCC28 版，記為『平台標籤更正，實質內容
無影響』，不回溯任何已簽裁決」。

**(3) 換檔 —— 未執行。** 覆寫 `features/privacy/inputs/` 之該檔的動作被
Claude Code 之權限分類器攔下兩次（先後以 Python `shutil.copyfile` 與
`cp` 嘗試，皆遭拒）。**執行層停止嘗試，未以任何其他方式繞過。**

待辦（一行，需 Pei 執行或授權）：

```bash
cp "/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/VF/VF_Split document/HDCC28_Split/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx" \
   "features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx"
```

換檔完成後尚須連動三處，**目前皆維持換檔前狀態**：

1. `BASELINE.sha256` 該行更新為 `e20ba7a4f8f7…`，並於檔頭記
   「依 R24-2(2) 換版」——BASELINE 的更新規則要求連同裁決編號
2. 本條轉 **RESOLVED**
3. framework Part VI 注 3 與 profile §6 之「A-PV14 未結案前不得於 B2 引用
   V6_R2」解除；B2 之依賴欄改為無

**(4) 換檔已完成（R29-2，Pei 執行，2026-08-13）。** 實測 `inputs/` 該檔：

```
SHA256 = e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2
size   = 177,388 bytes
```

與預期值相符。三處連動已辦：`BASELINE.sha256` 該行更新並於檔頭記
R24-2(2) / R29-2；framework Part VI 注 3 與批次表 B2 依賴欄解除；
profile §5 之 `[A-PV14]` marker **整條移除**、§6 該列改為 citable。

**平台歸屬之佐證有二且互相獨立**：檔案路徑（`HDCC28_Split`）與文件內文
（修訂履歷 `derived from VF651_V6_R1_PHDCCMCA`，hunk 8）。
**本條結案。**

## A-PV15 — 範本車型欄停在 27 世代，本專案為 HDCC28 — **DEFERRED — 待 RD-1 #6/#7 回覆（R30-4）**

**量測**（`Test Case Specification 測試用例規範`，第 8–9 列；T8:Z8 為合併儲存格
`Vehicle Model 車型`）：

| T9 | U9 | V9 | W9 | X9 | Y9 | Z9 |
|---|---|---|---|---|---|---|
| `HDCC27 Atl-Hi` | `DT27 Atl-Hi` | `VF(ProMaster)637 Atl-Mi` | `Commander (598) Atl-Mi` | `Regengade (5210) Atl-Mi` | `Toro(2261) Atl-Mi` | `Fastack (376) Atl-Mi` |

**七個車型欄裡沒有 HDCC28**，而本專案平台為 HDCC28（A-PV04 / R23-2 之基線
判定即據此）。範本 rev C 之車型區塊停在 **27 世代**。

**與 A-PV14 同源，方向相反**：A-PV14 是 VF 文件混入 DT 平台副本（素材側），
本條是**表單自身的欄位沒跟上世代**（載體側）。兩者都會讓交付件把
27/DT 世代的標籤套到 28/HDCC 專案上。

**處置（R30-4）**：**不自行對應**。不得把 `HDCC27` 欄當成 HDCC28 用，
也不得新增欄位。T–Z 一律留白 —— 該留白有獨立依據（AMFM 已交付件 158 列
**0/158** 有值），**不因本條未決而動搖**，故本條**不阻塞任何批次**。
登 RD-1 向上游提問：rev C 之車型欄是否應補 28 世代，或本專案本就不填。

**附帶觀察**：X9 之 `Regengade (5210)` 疑為 `Renegade` 之拼寫錯誤。
範本原文不動，一併進 RD-1。

**相關**：`RULINGS.md` R30-4；A-PV14；profile §3.9；framework Part VI
Workbook sync；`DATA_REQUESTS.md` #6–#8。

## A-PV16 — TC 步驟假定實驗室具備 CAN interface 記錄能力 — **DEFERRED — 待測試團隊確認（R32 N4）**

**來源**：B1 pilot review N4（下放包 10）。執行層於上繳包 09 §6.5 主動聲明。

`-004` 與 `-005` 兩條之 Pre-Condition／步驟寫「A CAN interface tool is
connected」「Read the $VolumeSCV$ signal in the CAN trace」。CFTS022 未規定
測試環境，profile 亦無測試環境條款。

**性質判定（分析層追認執行層之判斷）**：這是**測試可執行性之假定**，
不是**需求之假定** —— TC 沒有對規格內容做任何補充或推測，只是選用了一種
觀察手段。故**不登 assumption、不創 marker**（profile §5：本 feature
目前無 marker）。

**待確認**：與測試團隊確認實驗室具備 CAN trace 記錄能力。
若不具備，`-004`（`<Tsend>` 時限觀察）與 `-005`（$VolumeSCV$ 值觀察）
三條 TC 不可執行，須改以其他可觀察面重寫。

**不阻塞任何批次。**

**相關**：`RULINGS.md` R32 N4；上繳包 09 §6.5；profile §3.4（訊號引用）。

## A-PV17 — 037 Description 含 CFTS022 未載之行為主張 — **DEFERRED — 待 RD-1 #9 回覆（R33-2）**

**發現**：`SWE1-HMI-PRIVACY_FEATURES-001` 之 Requirement Description 第二段主張：

> The system shall detect and process button press inputs only after the
> transition from SLEEP MODE to an active operational state is completed

**CFTS022 全文無此語。** 涉及 `SLEEP MODE` 之 artifact 僅三條（全文掃描）：

| artifact | ECU | 條文 |
|---|---|---|
| 4914954 | SCCM | 退出 SLEEP MODE 後 SCCM 監測按鍵狀態（含 10 分鐘門檻）|
| **4914955** | ETM, RRM, ICS, DVD, LTM | 退出 SLEEP MODE 後 HU 與 external DVD player 監測按鍵狀態 ← **本葉來源** |
| 4915104 | — | Lock Out State 初始化 |

無一述及「轉換階段中按鍵輸入不得被處理」。

**處置（R33-2）—— 先問後補**：

- (a) -001 現行 TC **不改**：其驗證目標與 CFTS022-4914955 一致
- (b) `reasoning` 已明列該主張未被本 TC 覆蓋及其理由
- (c) 本條登記，狀態 PENDING
- (d) 列入 RD-1（`DATA_REQUESTS.md` #9）：請上游確認該句為需求或闡釋；
      若為需求，請指出其 CFTS022 出處或補充條文

**為何不逕行補測**：不對稱錯誤代價指向補測（擴範圍）而非不測（縮範圍），
**但補測之對象必須先確認是需求**。若該句為分析者之闡釋而非需求，
據以生成 TC 會對合規實作產生誤判（§7 FF）—— 一個正確實作會因為
「轉換階段有處理按鍵」而被判 fail，而該限制根本不在系統需求內。

**範圍提醒**：本條只針對 -001。-002 與 -003 之同型觀察經覆核後結論不同
（-002 已被現有 ER 涵蓋；-003 之排除有 {CFTS019} 外部歸屬佐證），
**不併入本條**（R33-2 / R33-3）。

**相關**：`RULINGS.md` R33-2；上繳包 09 §6.2；`DATA_REQUESTS.md` #9。

## A-PV18 — 037 將 outcome 主詞為 AMP 之條文分配予 HMI/HU 之 SWE.1 — **DEFERRED — 待 RD-1 #12 回覆（R34-3）**

**事實**：`SWE1-HMI-PRIVACY_FEATURES-008` 之來源條文 CFTS022-4915173 為

> When the AMP wakes up on the Interior CAN, the AMP shall recall the state of
> the speed controlled volume.

trigger 與 outcome 主詞**皆為 AMP**，條文全文**不提 HU**。而該葉被分配至
`SWE1-HMI-PRIVACY_FEATURES`（HMI/HU 之 SWE.1 分析）。

**四項證據同向**（分析層獨立複驗 ECU tag，執行層判定成立）：

| # | 證據 |
|---|---|
| (a) | trigger 主詞 = AMP |
| (b) | outcome 主詞 = AMP |
| (c) | 條文全文不提 HU |
| (d) | **ECU tag 含 `AMP` —— 十片葉子中唯一** |

十葉之 ECU tag 對照（(d) 之依據）：

```
4915171  RRM, LTM, ETM
4915172  ETM, LTM, RRM
4915173  ETM, AMP, RRM, LTM   ← 唯一含 AMP
4915174  RRM, LTM, ETM
4915175  LTM, ETM, RRM
```

**反向指標已照實回報**：該條 ECU tag 仍含 `LTM`。依 **R34-1** 之兩層判準，
tag 含本 ECU 僅為必要條件，充分條件（trigger 或 outcome 主詞含本 ECU，
或本 ECU 在訊號鏈上有可觀察之一端）不成立，故不足以推翻排除。

**處置（R34-2 / R34-3）**：排除於本交付件之驗證範圍，歸 AMP ECU；
但**交付件仍為該葉產出一列 BLOCKED**，非略去 —— 直接少一片葉子會讓追溯表
出現沒有說明的缺口，BLOCKED 列使缺口可見、可審。該列帶本 feature
**第一個 marker** `[BLOCKED-ECU]`（profile §5）。

**待上游確認**：-008 之葉子分配是否正確；若確為 HU 側需求，
請指出 HU 在該行為中之角色與可觀察面。已列 `DATA_REQUESTS.md` **#12**。

**相關**：`RULINGS.md` R34-1 / R34-2 / R34-3；profile §1.1（ECU 歸屬判準）、
§5（marker 表）；上繳包 11 §4。

## A-PV19 — `new_feature.py` 之樣板內建欄位字母，下一個 feature 仍會拿到錯值 — **DEFERRED — 待 Pei 裁定（R41-8）**

**根因，非現象。** A-PV13 記的是 Privacy 之 `feature.yaml` 帶 rev C 之前的
欄位字母（`Q` / `R` / `Z`），已於 R39-2 修為 `R` / `S` / `AA` 並結案。
**但那只修了實例。** 產生該實例的是 `scripts/new_feature.py` 之 `feature.yaml`
樣板，**其內仍寫舊字母** —— 下一個以 `new_feature.py` scaffold 的 feature
仍會拿到 `Q` / `R` / `Z`。

**分析層之修正方向建議（R41-8，供日後裁定，本輪不執行）**：

> **樣板不應內建欄位字母。** 依 R37-3(a)（位置資訊以標的物為準），
> 正解是樣板留空或標 `AUTO`，由 recon／writer 自表頭解析 ——
> **而非把 `Q/R/Z` 改成 `R/S/AA`**（後者只是把錯誤換一個版本，
> 遇到非 rev C 之範本會再錯一次）。

此方向與 A-PV13 之處置一致：Privacy 之 `write_back.py` 自始由表頭文字解析，
`feature.yaml` 之字母對產出無效力；修樣板時應把「字母為權威」這個假設一併
移除，而不是更新一份新的錯誤預設值。

**為何 DEFERRED 而非即辦**：`new_feature.py` 為**跨 feature 共用 script**，
改它會影響其餘五個 feature 之 scaffold 行為，且本 feature 正處交付前夕。
R41-8 明裁「交付前夕不動共用 script」。

**相關**：A-PV13（實例，已 RESOLVED）；`RULINGS.md` R41-8 / R39-2 / R37-3(a)。

## A-PV21 — 為外部素材所立之規則未回頭套用於自有工具 — **RESOLVED（R46-3 / R46-4，2026-08-14）**

> **主述依 R46-4 更正**：本條之核心**不是命名衝突**，而是
> **R15-5（同名檔一律以 hash 認定）係為外部素材而立，未回頭套用於本 repo
> 之自有工具** —— 基準稽核腳本正是 basename 索引。命名衝突是其表徵。
>
> §5a：**對外部素材所立之規則，須逐條檢查是否同樣適用於自有工具與自有
> 產物**；「這條是給上游的」不構成豁免。判準：該規則所防範之失效模式，
> 在自有側是否同樣可能發生。

**表徵**（交付後實測，2026-08-14）：

| 檔案 | 位置 | SHA256 | bytes |
|---|---|---|---|
| `…_SWQT_Privacy_20260813.xlsx` | `features/privacy/output/`（ENTRY 001，準備工作簿）| `ed741d8d…` | 59,992 |
| `…_SWQT_Privacy_20260813.xlsx` | `10_Reviewing/…/Privacy Mode/`（ENTRY 003，**交付件**）| `ad595ed0…` | 63,001 |

**basename 完全相同，內容不同。**

**成因不是疏失，是規則之必然後果。** R40-1 為使交付檔名與 AMFM／SXM 一致
而去掉 `_regen-v1`，同時 R40-1(a) 令 `output/` 內之準備工作簿維持原名
`…_Privacy_20260813.xlsx`。兩項規則各自正確，合起來即產生同名不同容。

**這正是 A-PV04 之型**（`VF651_V2_R2.docx` 七路徑五內容），而該案之教訓
已成 **R15-5：同名檔一律以 hash 認定**。機制上已有防護：

- `DELIVERY.sha256` 三筆各記全長 SHA256，ENTRY 003 明文載
  「內容同 ENTRY 002，僅檔名與位置不同」並附同名警示
- ENTRY 003 之雜湊行指向交付副本之**絕對路徑**，與 ENTRY 001 之
  `output/…` 相對路徑不衝突，`shasum -c` 三筆各自獨立驗證

**殘餘風險**：以 **basename 索引**之工具會取得兩個候選。
本 repo 之基準稽核腳本（下放包 01 §2 / 07）正是 basename 索引 ——
日後若對 `10_Reviewing/` 樹做同型稽核，`…_Privacy_20260813.xlsx`
會同時命中準備工作簿與交付件。

**處置 —— Pei 簽署選項 A（R46-3），已執行**：

| 項 | 結果 |
|---|---|
| (a) `output/` 內 ENTRY 001 改名為 `…_SWQT_Privacy_20260813_prepared.xlsx` | ✅ SHA256 `ed741d8d…` **未變**（只改檔名）|
| (b) `DELIVERY.sha256` 追加路徑變更註記（append，不改寫既有欄位）| ✅ 含改名前後檔名、SHA256、裁決編號、日期，末行為 `STATUS:`（R39-5）|
| (c) 改名後 `shasum -a 256 -c` 三筆全 OK | ✅ 停手條件 1 未觸發 |

**舊路徑之雜湊行保留不刪**：其路徑已不存在，`--ignore-missing` 靜默略過。
保留是為了讓改名在台帳上留下痕跡 —— 刪掉會使改名看起來從未發生
（R41-4：紀錄之缺口應被標記，不應被填補）。

**稽核腳本之設計維持不變**（R46-4）：basename 檢索 + hash 認定。
該設計**有效** —— A-PV04（`VF651_V2_R2.docx` 七路徑五內容）正是以此抓到。
須注意的是**不得日後被「簡化」為純 basename 比對**；理由已記於本條與
`docs/upstream/01_carryover.md` §2.1 之量測條件。

**相關**：`RULINGS.md` R40-1 / R15-5；A-PV04；`DELIVERY.sha256` ENTRY 001／003。

## A-PV20 — AMFM 之下放包 03 亦無對應上繳包（跨 feature 觀察）— **DEFERRED — 待 AMFM 重啟時處理（R44-9）**

**跨 feature 觀察**，記於 Privacy 之 ANOMALIES 因發現於 Privacy 之 parity 作業。

`features/amfm/docs/handoff/` 有四份下放包（01–04），
`docs/upstream/` 有三份（01、02、04）—— **03 無對應上繳包**。

**與 Privacy 之 08 同型**（應產而未產），且該包正是
**R17-1 ~ R17-4 遭擱置之來源包** —— 那四條簽署條文因 03 未產上繳包而
從未寫入 `RULINGS.md`，直到 R19-2 才補正。**同型缺口已造成過一次實害。**

**處置（R44-9）**：**登記，本輪不處理。** 依 Pei 2026-08-13 之裁示
（「只專心做 Privacy」）與 R18-1（做過的不重產），AMFM 不在現行工作焦點內。

**parity 測試維持僅涵蓋 `features/privacy`**（R41-6）。擴及他 feature 需另裁 ——
其餘 feature 之往返多未落檔，直接套用會產生大量 `unknown`，
反而稀釋該機制之訊號。

**重啟 AMFM 時之建議**：先為其 `docs/handoff/` 補 `HANDOFF-LINK` 標記
並建 `handoff_parity.json`，再擴充測試涵蓋範圍 ——
順序反過來會先得到一堆 FAIL 而無從逐項認定。

**相關**：`RULINGS.md` R44-9 / R19-2 / R41-4；A-PV21（同屬「規則未回頭套用」之族）。

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PVnn]`
（骨架產出為 `A-PRnn`，見 A-PV06）。
