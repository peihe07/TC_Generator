# 上繳包 01 — 跨 feature 條文承接 + Privacy 基準確認

執行層 → 分析層。2026-08-13。回應 `docs/handoff/01_carryover.md` §6 之三項要求。

> ## ⚠️ 本包之背景前提與實測不符
>
> 下放包 §背景寫「`features/` 下現僅存 `privacy/`，其餘五個 feature 目錄與
> repo 根 `output/` 已不在」。**實測：六個 feature 目錄全部都在。**
>
> ```
> features/amfm  features/home  features/media
> features/privacy  features/projection  features/sxm
> ```
>
> 消失的不是目錄，是**目錄裡未被 git 追蹤的素材**。詳見 §1。
>
> 本包據該前提做出的兩項範圍決定 —— 「其餘一律不追」與「下放包 08 內容
> 全部作廢」—— **其事實基礎不成立**。執行層依 §4「不追查已消失之 feature
> 目錄」未作任何追查，但**必須回報前提本身有誤**：作廢的決定建立在
> 「目錄不存在」上，而目錄存在，且其中 135 / 68 / 170 / 77 / 230 個
> 追蹤檔（含全部 ANOMALIES、RULINGS、PLAYBOOK、scripts）都還在。
> 是否恢復 08 包由分析層裁定。
>
> 此為 **R17-3** 之適用場景：關於 feature 處於何階段之陳述，撰寫當下須以
> 實測為據。本次未實測即陳述，且該陳述直接決定了工作範圍。

---

## 1. 實測：到底少了什麼

全程唯讀（`ls` + `git ls-files` + `git check-ignore`）。

| feature | 目錄 | 追蹤檔數 | `inputs/` 現存檔數 |
|---|---|---|---|
| amfm | ✅ 在 | 135 | **0** |
| home | ✅ 在 | 68 | **0** |
| media | ✅ 在 | 170 | **0** |
| projection | ✅ 在 | 77 | **0** |
| sxm | ✅ 在 | 230 | **2**（原 15）|
| privacy | ✅ 在 | — | **8**（完整）|

repo 根 `output/`：**不存在**（此項下放包所述正確）。

**成因之可陳述部分**：`inputs/` 與 `output/` 皆列於 `.gitignore`
（`features/*/.gitignore:2` 之 `inputs/`；根 `.gitignore:20` 之 `output/`），
且 `git ls-files output/` 回 0 筆。**故此類檔案從未進版控，git 無從還原。**
成因本身不判定（R22-5）。

**具體損失（僅陳述，不評估）**：

- AMFM v1（tag `fw036-amfm-regen-v1` 標註之交付件）與 v2（R18-2 裁定
  保留於 `output/` 不打 tag 者）**皆不在磁碟上**
- Home / SXM / Media / Projection 之客戶原件與交付件同樣不在
- 五個 tag 全部仍在：`fw036-amfm-regen-v1`、`fw036-home-regen-v2`、
  `fw036-regen-v1`、`fw036-sxm-v1`、`archive/new-frontend-v1`

**一項對後續有用的事實**：AMFM v2 **可決定性重產** —— 其 writer 已改為
`xlsx_surgical`，同參數連跑兩次 SHA256 相同（`0daa6f29cecb…`，上繳包 02
§3.2 記載），前提是客戶原件重新到位。
反之 **v1 不可重產** —— v1 需要 openpyxl 存檔路徑，而 AMFM 的
`write_back.py` 已改接外科手術路徑，該路徑在檔內已不存在。
tag 仍指向一個無法再現的產物。

---

## 2. §6.1 —— §2 基準確認：逐檔表與計數彙總

### 2.1 量測條件（逐項）

| 項目 | 實際採用 |
|---|---|
| 掃描對象 | `features/privacy/inputs/` 全部檔案，不限副檔名，排除 dotfile —— **8 檔** |
| 對照範圍 | **限定** `/Users/peihe/Work/02_Project_R1LR/` 之下（依 §2.2）|
| 樹外偵測 | 另掃 `/Users/peihe/Work/` 全樹以辨識 `OUT_OF_TREE`；樹外命中**不計入** `MATCH` |
| 比對方法 | **SHA256**（`hashlib`，1 MiB 分塊）。未以檔名、大小或 mtime 代替（R15-5）|
| 候選蒐集 | 以 basename 索引；**逐檔列出所有同名候選及其 SHA256**（A-PV04）|
| 多候選處置 | 命中任一樹內候選即 `MATCH`；**未取「最相似」之單一候選作結論** |
| 已知先例 | V6_R2 之 `49dd3c31405fb0c34d4cf11048d325d6f047c0d333c10248310e72c57e194fbb` 依 §2.6 可直接引用，**本次仍重算並確認相符** |
| 讀寫模式 | **全程唯讀**。未移動、改名、覆寫、刪除任一檔；未要求寫入權限（停手條件 3 未觸發）|

### 2.2 四類計數彙總

| 判定 | 檔數 |
|---|---|
| `MATCH` | **8** |
| `OUT_OF_TREE` | 0 |
| `NO_MATCH` | 0 |
| `NO_COUNTERPART` | 0 |
| 合計 | **8** |

**停手條件 2 未觸發**，故 §4.3 狀態板更新照辦。

**結論措辭（R22-1 現在式限縮）**：
`features/privacy/inputs/` 之 8 個檔案，**此刻**其 SHA256 各自命中
`02_Project_R1LR/` 樹內至少一個同名候選。
**此陳述不蘊含「該等檔案從未被覆寫」** —— 若某檔曾被改寫、隨後又自客戶樹
重新複製，本量測同樣顯示 `MATCH`。要排除該情形需 mtime／檔案系統事件／
備份比對，不在本包範圍。

**R22-2 本次未觸發**（`NO_COUNTERPART` 為 0 件），但方法學限制仍成立：
本次以 basename 索引建立候選集，客戶樹內若有改名之對應檔，本方法看不見。
8 件全數命中，故本次不受此限制影響。

### 2.3 逐檔表

| # | 檔名 | bytes | inputs SHA256 | 候選 樹內/樹外 | 相異內容數 | 判定 | 命中路徑 |
|---|---|---|---|---|---|---|---|
| 1 | `Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx` | 148,196 | `c54f700f81c4c70e…` | 3 / 0 | 2 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx<br>…/1_Customer_Requirement/VF/VF_Split document/HDCC28_Split/Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx |
| 2 | `Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx` | 184,808 | `49dd3c31405fb0c3…` | 7 / 0 | 6 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx<br>…/1_Customer_Requirement/VF/28DT_2A_LTM/LTM/VF - Functional Requirements/DT28_split/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx |
| 3 | `Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx` | 146,929 | `d5813bb7ccd6f721…` | 7 / 0 | 6 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx<br>…/1_Customer_Requirement/VF/VF_Split document/HDCC28_Split/Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx |
| 4 | `CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx` | 54,304 | `f46d15ca29b6a75d…` | 2 / 0 | 2 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx |
| 5 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx` | 65,823 | `cd876c202c71e74b…` | 1 / 1 | 2 | **MATCH** | …/9_ASPICE/SWE.6 Software Validation/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx |
| 6 | `R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx` | 79,276 | `5eb0dd739f002fe0…` | 2 / 0 | 1 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx<br>…/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Sub System/Privacy/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx |
| 7 | `SWE1_CFTS_022-Privacy_Features.xlsx` | 63,786 | `190e6f3ebaee5fe7…` | 2 / 0 | 2 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/SWE1_CFTS_022-Privacy_Features.xlsx |
| 8 | `SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` | 3,448,554 | `e534afa55710547f…` | 2 / 0 | 2 | **MATCH** | …/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx |


**「相異內容數」欄之意義**：同名候選之相異 SHA256 個數。
A-PV04 原本只在 `V2_R2` 上觀察到「同名不同容」，本次量測顯示這是常態而非例外
—— 8 個檔裡有 **7 個**的同名候選不只一種內容，其中 `V6_R2` 是
**7 個候選 / 6 種內容**。R15-5「同名檔一律以 hash 認定」在本 feature
不是保守規定，是必要條件。

### 2.4 稽核副產物 —— 已登記為 A-PV14

逐檔列出全部候選後，浮現一件與判定無關、卻直接影響 spec 引用的事：

| 檔案 | `inputs/` 命中之平台樹 |
|---|---|
| `…VF651_V2_R2.docx` | `VF_Split document/`**`HDCC28_Split`**`/` |
| `…VF651_V6_R2.docx` | `VF/`**`28DT_2A_LTM`**`/…/`**`DT28_split`**`/` |

同一個交付夾裡的兩份 VF651，一份對得上 HDCC28 樹、另一份對得上 DT28 樹。
V6_R2 的 HDCC28 副本（`e20ba7a4…`）與 `inputs/` 這份（`49dd3c31…`）**不同**。

本專案為 HDCC28 平台（A-PV04 之基線判定即據此）。若 V6_R2 該引用 HDCC28 版，
則 -007 / -008 / -010（AMP-present 三筆）之 `specification_reference`
會指向錯誤平台的文件。**R-PV01(c) 簽署時不可能發現這件事** —— 該裁決依據是
「需求本身要求 AMP-present」，不涉及平台版本。

**未判定何者為正**（R22-5）。**未做兩版 diff** —— 那會暗示成因，且屬 P2
spec 解析範疇。已登記 `ANOMALIES.md` **A-PV14**：在 P2 引用 V6_R2 任一條文
之前先裁定平台版本，裁定前 V6_R2 不得列為 `specification_reference`。

---

## 3. §6.2 —— 狀態板更新後全文

值之來源為 `RECON.md`、`_intake/Privacy/INTAKE.md`、`data/recon.json`
之實測，**未以本包或記憶為來源**（§4.3 明文要求）。

```markdown
## 6. Status board — Privacy

> 值之來源：`RECON.md` / `_intake/Privacy/INTAKE.md` / `data/recon.json`
> 之實測，非記憶或下放包轉述（R17-3）。更新於 2026-08-13。

- [x] P0 intake complete; INTAKE.md reviewed; 7 檔全數分類（零
      unclassified／unreadable）; spec_mode **D**;
      missing files: **無缺件**，但需求報告之 source 欄為 component/
      Polarion id，**need list 不可自該範本導出**（trace 走
      architecture／export 檔）
- [x] P1 recon complete; workbook_state: **BLANK**; leaves: **10**;
      targets: **10**（`SWE1-HMI-PRIVACY_FEATURES-001` … `-010`，
      covered nowhere = 10）
- [ ] P2 DECISIONS signed (date: ____) —— `DECISIONS.md` §8 已有三條簽署
      裁決（R-PV01(c)、R-PV01(a)(b)(d) 延後、R-PV02），
      但 sign-off 欄仍空，故不勾
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING rulings: **8 條** —— A-PV01 / A-PV04 / A-PV05 / A-PV07 /
  A-PV08 / A-PV10 / A-PV11 / A-PV12（A-PV14 為本日新登，見下）。
  另 DEFERRED 2 條（A-PV02 之 ANC 部分、A-PV03）、CLOSED 1 條（A-PV09）
- 基準確認（R22 §2, 2026-08-13）：`inputs/` 8 檔全數 **MATCH**
  `/Users/peihe/Work/02_Project_R1LR/` 樹內同名候選。
  **現在式陳述**（R22-1）：此刻相符，不蘊含「從未被覆寫」
```

**P2 未勾之理由**：`DECISIONS.md` §8 確有三條已簽署裁決
（R-PV01(c)、R-PV01(a)(b)(d) 延後、R-PV02），但該檔之 Sign-off 區塊
（`Reviewed by: ____  Date: ____`）仍空白。「個別裁決已簽」與
「DECISIONS 整份已簽核」是兩件事，故不勾，並在該列註明原因而非留白。

**P3–P7 留白之依據（本次補查，非推定）**：

| 階段 | 查證對象 | 結果 |
|---|---|---|
| P3 | `docs/runtime/profiles/` | 有 AMFM / BT / Home / Projection / SXM 五份 profile，**無 Privacy** |
| P4 | `features/privacy/data/` | 僅 `recon.json`（P1 產物），無其他 data artifact |
| P5–P6 | `features/privacy/generated/`、`batches/` | **兩者皆空** |
| P7 | `git tag` | 無任何 `fw036-privacy-*` tag |

四項皆為實測，故留白確為「未開始」而非「未查」。

---

## 4. §6.3 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。**

1. **`inputs/` 素材消失之成因完全未查，且本包明文禁止查（§4）。**
   但這件事對 Privacy 有直接影響：**同一個機制若再發生一次，Privacy 的
   8 個檔就是下一批。** 本包確認了它們此刻完整，卻沒有做任何事讓它們
   **保持**完整。最低成本的防護是把 8 個檔的 SHA256 落成一份**追蹤中**的
   baseline 檔（`inputs/` 本身 gitignored，但 hash 清單可以進版控），
   日後任何改動都會在 `git diff` 現形。本包未做 —— 不在作業清單內，
   且新增追蹤檔屬 repo 結構變更。**建議列入下一包。**

2. **R22-1 所指的「曾被覆寫又複製回來」，本次完全沒有偵測能力。**
   §2.2 已把結論限縮為現在式，措辭正確 —— 但**限縮措辭不等於補上量測**。
   若分析層要的是「Privacy 基準從未受損」這個完成式結論，
   本次稽核**不能**提供。

3. **`OUT_OF_TREE` 差一點觸發，其意涵未探究。**
   FW036 空白範本在 `03_Tools/037import036/template/` 有一份同名檔，
   SHA256 `069687e416ec…`，**與 `inputs/` 這份（`cd876c202c71…`）不同**。
   因樹內已命中故判 `MATCH`，`OUT_OF_TREE` 未觸發。
   但這代表**有一支工具夾帶著另一版的同名 036 範本**。
   該工具（`037import036`）若曾被用來產生或轉換 036 檔案，
   其產出的形態會與本 feature 的基線不同。未追 —— 超出 §2 範圍。

4. **A-PV14 的嚴重性未量，因此無法排優先序。**
   已登記兩版 hash 相異，但**未做內容 diff**，所以「相異」可能是整份改版，
   也可能是一兩個 PROXI 參數 —— 兩者對 -007/-008/-010 的影響天差地遠。
   不做是刻意的（R22-5：分類承載因果假設時停在原始量測；且屬 P2 範疇），
   代價是這條目前只能標 PENDING，不能標輕重。

<!-- UPSTREAM-COVERS: 01 -->
