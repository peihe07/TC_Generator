# ANOMALIES — FW036 Privacy HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PVnn]` — **note**: `new_feature.py` generated the skeleton
with `A-PRnn` (`feature[:2].upper()`); the analysis layer's handoff bundle 00
§2 mandates `A-PVnn`. Reported as-is, NOT self-corrected (A-PV06, Tier 2).
PENDING entries block their batch until a Pei ruling lands; RESOLVED entries
record the ruling verbatim. Registration is Tier 1 (record + propose);
disposition is Tier 2.

---

## A-PV01 — 交付目標 workbook：以空白範本開工 — PENDING (downgraded)

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

## A-PV02 — VF651 變體選擇 — **RESOLVED（Amplified 部分）／PENDING（ANC 部分）**

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

**仍 PENDING**：ANC 兩變體（V9_R3 / V11_R3）依裁決維持不索取，
`DATA_REQUESTS.md` #3 標為 Not requested。若 P2 解析發現任一 leaf 觸及 ANC
配置，回頭停手回報，不自行擴充。

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

## A-PV03 — ETM V3_R3 疑非本專案適用件 — **PENDING（R-PV01(a) 明示延後至 P2）**

證據：CFTS022 之 `R1L-R` × ETM-only artifact = 0 行；SYS.2
`VF651_Audio_Output_Management/` 8 個子目錄無任何 V3。

**Pei 裁示（2026-08-13）**：

> (a) 排除 ETM V3_R3 → 延後到 P2。那五個數是我單方掃描，未經重驗，
> 而排除是「縮範圍」，錯了會漏驗。V3_R3 就留在 `inputs/` 不引用，零成本。
> P2 重驗後再簽。

執行層據此：V3_R3 **留在 `inputs/`**，狀態為「在庫、不引用」——
不得列為 `specification_reference`，也不得因未列而視為已排除。
P2 進場時必須先重驗 handoff §3.2 / §3.4 兩組數（見 §7.6 未驗清單第 1、3 項），
重驗結果回報後才簽 R-PV01(a)。

**非對稱原則（本次確立，值得沿用）**：擴範圍的裁決（(c) 納入 V6_R2）證據若
自足即可立即簽；縮範圍的裁決（(a) 排除 V3_R3）因錯誤代價是「漏驗」而非
「多驗」，必須等證據重驗完成。兩者不必同批處理。

## A-PV04 — 同名不同內容（VF651_V2_R2）— **已量測，待處置** PENDING

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

## A-PV05 — SYSAD 混入 `cfts_doc` 分類 — PENDING

`SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` 為 SYS.3 架構
設計，非 CFTS 規格；`intake.py` 依副檔名把 `.docx` 一律歸 `cfts_doc`，實測
確已如此分類（見 `_intake` 產出之 `INTAKE.md`）。其角色是背景理解，
**不得作為 `specification_reference`**（§10.7 禁止引用分析類文件）。
建議處置：`feature.yaml` 標為 context-only。

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

## A-PV07 — 範本殘留樣本列（第 10–11 列）— PENDING

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

## A-PV08 — Scope / Purpose / Reviewer 三格待填，且 intake 誤讀 Scope — PENDING

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

## A-PV09 — openpyxl 寫回會損毀範本 — **已實測，處置已定** RESOLVED

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

## A-PV10 — 下拉選單清單範圍與內容不一致 — PENDING

`下拉選單` 分頁實有 **9** 個詞條（A1:A9），A10 / A11 為空。
但 R11:R59 的 DV 指向 `$A$1:$A$11`（含 2 個空選項），R10 指向 `$A$1:$A$9`。
同一欄兩種範圍，且較大那組帶空白項。
建議處置：登記即可，範本瑕疵屬上游；lint 以 A1:A9 之 9 詞條為準
（`feature.yaml` 之 `lint.design_method_source: dropdown_sheet` 即取此分頁）。

## A-PV11 — `Reference` 分頁與 `下拉選單` 詞條字串不符 — PENDING

`lint.design_method_source` 要求 exact-string 比對，兩分頁第 6 條不一致：

- `下拉選單!A6` = `組合測試 (Combinatorial Testing ; Pairwise / t-wise)`
- `Reference!C9`  = `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)`

建議處置：以 `下拉選單` 為 lint 權威（DV 實際引用的是它）；`Reference`
視為說明性附表，不入 lint。回報上游修正。

## A-PV12 — `Cover_old` / `ChangeHistory_old` 舊版分頁殘留 — PENDING

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

## A-PV13 — scaffold 產出之 `feature.yaml` 欄位字母為 rev C 之前的版本 — RESOLVED (執行層已處置)

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

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PVnn]`
（骨架產出為 `A-PRnn`，見 A-PV06）。
