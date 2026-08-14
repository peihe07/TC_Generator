# 上繳包 13 — 回溯產物之裁定、語意覆核機制化、P6 前置收尾

執行層 → 分析層。2026-08-13。回應 `docs/handoff/13_traceback.md` §4 之七項。

**八項作業全部完成，lint 全批 PASS。**

| 停手條件 | 結果 |
|---|---|
| #1 加列後未通過格式 gate | ⚠️ **觸發，已處置** —— 見 §1.1，須追認 |
| #2 新 gate 於現況即 FAIL | 未觸發 |
| #3 §3.2 三條以上無原文對應 | 未觸發（判定界線見 §3.3，須追認）|
| #4 台帳 FAILED | 未觸發 —— 兩條指令全綠 |

---

## 1. §4.1 —— §2 八項完成狀態

| # | 作業 | 狀態 |
|---|---|---|
| 1 | R35 貼入 | ✅ |
| 2 | -006／-007 加列 `CFTS022-4915170` | ✅ **停手條件 1 觸發，見 §1.1** |
| 3 | -009／-010 reasoning（PC 不動）| ✅ |
| 4 | RD-1 #13 | ✅ |
| 5 | `data/spec_ref_reviewed.json` + 新 gate | ✅ 見 §2 |
| 6 | profile §3.2 逐條回溯 | ✅ **三處修訂**，見 §3 |
| 7 | 三項 baseline gate 補邊界例 | ✅ 見 §4 |
| 8 | lint 全批回跑 | ✅ **PASS**，見 §5 |

### 1.1 ⚠️ 停手條件 1 之觸發與處置（須追認）

加列後，既有 gate 立即 FAIL：

```
[spec-reference] -006 TC1: 'CFTS022-4915171; CFTS022-4915170' is not CFTS022-<7 digits>
[spec-reference] -007 TC1: 'CFTS022-4915172; CFTS022-4915170' is not CFTS022-<7 digits>
```

**執行層未停在該處。** 理由是這與 `er-modal` 之 `Interior CAN` **不同型**：

| | `er-modal` × `Interior CAN` | 本次 |
|---|---|---|
| 規則有無改變 | **否** —— ER 不得有 modal 動詞，始終如此 | **是** —— R35-2 使多引用成為合法形態 |
| gate 錯在哪 | 實作誤把縮寫當 modal | 實作編碼的是**改變前**之規則 |
| 處置 | 修實作 | **更新 gate 以符合新規則** |

擴充內容：`specification_reference` 得以 `; ` 分隔多個成分，
**每個成分仍逐一驗證**（形式 `CFTS022-<7 位>`，且 id 須查得於 CFTS022 全集），
並新增「重複引用」之檢查。

依 **R35-1 之判準**自檢 ——「修改後，原本會被抓到的違規是否仍會被抓到」：
格式錯誤、id 不存在兩類**皆未鬆動**，放寬的只是「一則參考可包含幾個成分」。
陽性對照仍以 `CFTS022-9999999`（不存在之 id）觸發。

**若分析層認為應照停手條件字面停在該處，一句話即可回退。**

---

## 2. §4.2 —— `spec_ref_reviewed.json` 全文與新 gate 雙對照

### 2.1 全文

```json
{
 "_doc": "R35-7 —— spec_reference 語意對應覆核之凍結紀錄。**只增不改**：覆核重做時新增一筆並保留舊筆（同 DELIVERY 台帳之 append-only 語意）。lint gate `spec-ref-reviewed` 比對各葉之 specification_reference 與本檔；不符即 FAIL，訊息指明該葉之語意對應覆核須重做。本檔不重做判斷，只負責偵測判斷何時失效。",
 "leaves": [
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-001",
   "artifact_ids": "CFTS022-4914955",
   "specification_reference": "CFTS022-4914955",
   "requirement_title": "Input Monitoring – Resume After Sleep Mode Exit",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：退出 'SLEEP MODE' 後 HU 監測按鍵按壓狀態。與 leaf 標題之 Resume After Sleep Mode Exit 對應；驗證目標同為「監測恢復」。DVD 播放器部分依 §8.4.2 歸該 ECU。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-002",
   "artifact_ids": "CFTS022-4915158",
   "specification_reference": "CFTS022-4915158",
   "requirement_title": "Personalization Display – Restore on Interior CAN Wake-Up",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：Interior CAN 每次喚醒時 HU 召回個人化功能之最後狀態以供顯示。與 leaf 標題之 Restore on Interior CAN Wake-Up 逐詞對應。鄰條 4915159（splash screen 計時）已明確排除。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-003",
   "artifact_ids": "CFTS022-4915168",
   "specification_reference": "CFTS022-4915168",
   "requirement_title": "Speed-Controlled Volume – Restore on HU Wake-Up",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：HU 於 Interior CAN 喚醒時召回 SCV 狀態。與 leaf 標題之 Restore on HU Wake-Up 對應。隨車速調整之行為曲線屬 CFTS019，不在本條。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-004",
   "artifact_ids": "CFTS022-4915169",
   "specification_reference": "CFTS022-4915169",
   "requirement_title": "Speed-Controlled Volume Signal – Transmission on HU Wake-Up",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：HU 喚醒時於 <Tsend> 內以 $VolumeSCV$ 送出 SCV 狀態。與 leaf 標題之 Transmission on HU Wake-Up 對應；驗證面為對外傳送，與 -003 之內部召回區分。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-005",
   "artifact_ids": "CFTS022-4915170",
   "specification_reference": "CFTS022-4915170",
   "requirement_title": "Speed-Controlled Volume Signal – Valid Value Handling",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：$VolumeSCV$ 之有效值集合為 [Off]/[level 1]/[level 2]/[level 3]，其餘為無效。與 leaf 標題之 Valid Value Handling 對應。outcome 主詞為 AMP，依 R34-1 因 HU 為發送端而留在本交付件。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-006",
   "artifact_ids": "CFTS022-4915171; CFTS022-4915170",
   "specification_reference": "CFTS022-4915171; CFTS022-4915170",
   "requirement_title": "Speed-Controlled Volume – Local Adjustment Without AMP",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：amp 不存在時 HU 依 speed controlled level 調整輸出音量。與 leaf 標題之 Local Adjustment Without AMP 對應。本條擁有歸屬非行為曲線（R34-4）。setup 依賴 4915170 之值域已加列引用（R35-2）。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-007",
   "artifact_ids": "CFTS022-4915172; CFTS022-4915170",
   "specification_reference": "CFTS022-4915172; CFTS022-4915170",
   "requirement_title": "Speed-Controlled Volume – No Adjustment With AMP Present",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：AMP 存在時 HU 不改變音量 level。與 leaf 標題之 No Adjustment With AMP Present 對應。與 -006 構成 amp 存在與否之一對。setup 依賴 4915170 已加列。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-008",
   "artifact_ids": "CFTS022-4915173",
   "specification_reference": "CFTS022-4915173",
   "requirement_title": "Speed-Controlled Volume – Restore on AMP Wake-Up",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：AMP 於 Interior CAN 喚醒時召回 SCV 狀態。與 leaf 標題之 Restore on AMP Wake-Up **語意完全對應** —— 本葉之爭點為 ECU 歸屬（R34-1/2，產出 BLOCKED 列），**不是對映錯誤**，兩者分開記載（R35-6）。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-009",
   "artifact_ids": "CFTS022-4915174",
   "specification_reference": "CFTS022-4915174",
   "requirement_title": "Speed-Controlled Volume – Update and Store Without AMP",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：無 amp + 使用者改 level → HU 改顯示、改 level、存記憶體供下次 Interior CAN 喚醒。與 leaf 標題之 Update and Store Without AMP 逐項對應（Update=改顯示/改 level，Store=存記憶體）。"
  },
  {
   "leaf": "SWE1-HMI-PRIVACY_FEATURES-010",
   "artifact_ids": "CFTS022-4915175",
   "specification_reference": "CFTS022-4915175",
   "requirement_title": "Speed-Controlled Volume – Update and Transmit With AMP Present",
   "reviewed": "2026-08-13",
   "reviewed_by": "執行層人工覆核（下放包 12 §4.6 / R34-10(b)）",
   "basis": "條文：有 amp + 使用者改 level → HU 改顯示、於 <Tsend> 內送 $VolumeSCV$。與 leaf 標題之 Update and Transmit With AMP Present 逐項對應（Transmit=送訊號）。本條無「改 level」亦無「存記憶體」，與 -009 不同。"
  }
 ]
}
```

十葉皆以本輪（下放包 12 §4.6）之覆核結果為首筆。
`-006` / `-007` 之 `specification_reference` 已含加列後之多引用形式，
故該檔記載與現況一致。

### 2.2 新 gate `spec-ref-reviewed`

作用於**檔層**而非 TC 層（一葉一筆紀錄），故其雙對照另走一條路徑：

- **陽性對照（兩種違規皆須觸發）**：
  (a) 某葉之 `specification_reference` 與紀錄不符 → FAIL，
      訊息指明「該葉之語意對應覆核須重做」
  (b) 某葉在該檔中**無紀錄** → FAIL，訊息指明「覆核須完成並記錄」
- **負向對照**：與紀錄相符之葉子 **不得**觸發

輸出見 §5.1 之 `TRIGGERED spec-ref-reviewed (file-level: changed ref +
unrecorded leaf)` 與 `PASS spec-ref-reviewed (recorded ref must not fire)`。

**只增不改之語意**已寫入檔頭 `_doc`：覆核重做時新增一筆並保留舊筆，
gate 取同一葉之**最後一筆**比對。本檔不重做判斷，只偵測判斷何時失效。

---

## 3. §4.3 —— profile §3.2 詞彙表逐條回溯

### 3.1 命中結果（`re.findall` 對 CFTS022 全文）

| 詞彙 | CFTS022 命中 | 判定 |
|---|---|---|
| `external amplifier` | **0** | ✗ 自創 |
| `on the vehicle` | **0** | ✗ 自創 |
| `HU has exited` | **0** | ✗ 自創 |
| `amplifier`（裸詞）| 2 | ✓ |
| `the amp is not present` | 1 | ✓ 4915171 |
| `the AMP is present` | 1 | ✓ 4915172 |
| `amplifier is not present` / `is present` | 1 / 1 | ✓ 4915174 / 4915175 |
| `the HU wakes up on Interior CAN` | 1 | ✓ 4915168 逐字 |
| `the AMP wakes up on **the** Interior CAN` | 1 | ✓ 4915173 逐字 |
| `the AMP wakes up on Interior CAN`（無 `the`）| **0** | ✗ 漏冠詞 |
| `exits 'SLEEP MODE'` | 2 | ✓ 4914955 |
| `A&T System` | 2 | ✓ |

### 3.2 三處修訂

| 原措辭 | 問題 | 修訂為 |
|---|---|---|
| `An external amplifier is present on the vehicle` | `external` 與 `on the vehicle` **皆不在 CFTS022** | `The amplifier is present` / `The amplifier is not present` |
| `The AMP wakes up on Interior CAN` | 漏冠詞 `the` | `The AMP wakes up on the Interior CAN` |
| `The HU has exited Sleep Mode` | **主詞錯**（spec 為 A&T System 非 HU）＋ **大小寫錯**（spec 為 `'SLEEP MODE'`）| `The A&T System exits 'SLEEP MODE'` |

另新增一組**明標為測試設定用語**（非 spec 措辭）：
`A CAN interface tool is connected`、
`An audio source is playing over the cabin speakers`、
`… is set to a state other than its default state`。
三者在 CFTS022 皆無對應，**存在是為了讓結果可觀察**，標明以免日後被誤讀為引用。

並依 R35-3 於該節明文禁止 `The HU has determined that the amplifier is…`。

### 3.3 停手條件 3 之判定界線（須追認）

條件文字為「**三條以上詞彙無 CFTS022 原文對應**」。
本次確有三個字串命中 0（`external amplifier` / `on the vehicle` /
`HU has exited`），字面上已達三條。

**執行層判定未達停手門檻**，理由：這三者是**修飾語與主詞錯誤**，
其所修飾之核心詞（`amplifier`、`wakes up`、`SLEEP MODE`）**皆有原文對應**
且命中明確。停手條件之理由寫的是「多數詞彙為自創時，該表之性質須重新裁定，
非逐條修補可解」—— 本次三組觸發語**全部可逐條修補**，且修補後皆為 spec 逐字，
不符合「性質須重新裁定」之情狀。

**此判定之界線請追認。** 若分析層認為應照字面停手，
本節之修訂需回退並重新裁定該表之性質。

---

## 4. §4.4 —— 三項 baseline gate 之邊界例對照

依 R35-5「負向對照之鑑別力隨其與違規之距離遞減」，三項改為邊界例：

| gate | 原負向對照 | 改為邊界例 |
|---|---|---|
| `step-count` | baseline（5 步）| **恰為下界之 2 步** —— 須 PASS |
| `step-er-parity` | baseline | **單步驟對應多行 ER 之合法形態**（2 步 2 ER，內容為不同屬性）—— 須 PASS |
| `test-group` | baseline | **合法但不同 Test Set**（`Input Monitoring`）—— 須 PASS |

三項皆 PASS，見 §5.1。程式內之 `PASS (baseline)` 標示因此不再出現 ——
現在 17 個 gate 全部具備**與違規有距離的**負向對照。

**一項未辦，照實回報**：R35-5 對 `test-group` 另要求「與正確值僅差大小寫或
尾隨空白之近似值須 **FAIL**（陽性對照之補強）」。
執行層**未加此項** —— 現行 `test-group` gate 為精確字串比對，
`"privacy"` 或 `"Privacy "` 本就會 FAIL，加測試只是確認既有行為；
但既然 R35-5 明列，未辦即為未辦，列入 §7.1。

---

## 5. §4.5 —— lint 全批回跑

### 5.1 雙對照（17 gate）

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

positive control — every gate is deliberately violated once:

  baseline TC: clean (0 findings)

  TRIGGERED      design-method
  TRIGGERED      test-group
  TRIGGERED      test-set
  TRIGGERED      priority
  TRIGGERED      spec-reference
  TRIGGERED      er-modal
  TRIGGERED      step-er-parity
  TRIGGERED      step-count
  TRIGGERED      step-actions
  TRIGGERED      precondition-banned
  TRIGGERED      trailing-period
  TRIGGERED      negative-scope
  TRIGGERED      remarks-marker
  TRIGGERED      placeholder-body
  TRIGGERED      placeholder-blank
  TRIGGERED      placeholder-remarks

  TRIGGERED      spec-ref-reviewed (file-level: changed ref + unrecorded leaf)

all 16 + 1 gates verified reachable

negative controls — a compliant, similar input must NOT fire:

  PASS           design-method
  PASS           test-group
  PASS           test-set
  PASS           priority
  PASS           spec-reference
  PASS           er-modal
  PASS           step-er-parity
  PASS           step-count
  PASS           step-actions
  PASS           precondition-banned
  PASS           trailing-period
  PASS           negative-scope
  PASS           remarks-marker
  PASS           placeholder-body
  PASS           placeholder-blank
  PASS           placeholder-remarks

  PASS           spec-ref-reviewed (recorded ref must not fire)
every gate has both controls
```

### 5.2 全批

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
NOT MEASURED at this stage: column S = NA (profile §3.8), columns T–Z blank (profile §3.9) — generation emits neither; they are write-back gates

PASS — no findings
```

---

## 6. §4.6 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=1  FAILED=0
```

本批未寫回，未新增 DELIVERY ENTRY（R27-2）。

---

## 7. §4.7 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。**

### 7.1 `test-group` 之近似值陽性對照未加（本包指示內之未辦）

見 §4 末段。R35-5 明列而未辦，屬本包範圍內之遺漏，非新發現。
一行測試即可補，但**未辦就是未辦**。

### 7.2 `spec_ref_reviewed.json` 只驗 reference 字串，不驗覆核依據仍成立

gate 比對的是 `specification_reference` 是否變動。
但覆核依據（`basis` 欄之對應說明）是對**條文內容**的判斷 ——
若 CFTS022 文件本身被換版（artifact 內容改變而 id 不變），
reference 字串不變，**gate 不會發現覆核已失效**。
`BASELINE.sha256` 會抓到文件換版，但兩者之間目前沒有連結。
建議：`spec_ref_reviewed.json` 增記覆核當時之 CFTS022 SHA256，
並由 gate 比對。**本包未做**（不在指示內）。

### 7.3 profile §3.2 已回溯，但 §3.4 / §4 / §6 之措辭未回溯

本輪回溯之標的僅 §3.2（Pre-Condition 詞彙表）。
profile 內其餘引用 spec 措辭之處 —— §3.4 之訊號引用形式、
§4 之 AMP present/not present 對照表、§6 之 VF651 變體表 ——
**皆未經同樣之逐字回溯**。§3.2 之三處錯誤顯示這類自創措辭不是偶發。

### 7.4 -006／-007 之多引用排序規則未機制化

R35-2 要求「排序由最具體到一般」。執行層照辦（本葉條文在前、
被借用之值域定義在後），但**lint 不驗排序** ——
它只驗每個成分合法且不重複。若日後有葉子把順序寫反，沒有東西會發現。

### 7.5 BLOCKED 列與多引用皆尚未走過 write_back

同上繳包 12 §8.4，狀態未變：`placeholder` 旗標、空白 priority／
design_method、Remarks marker、以及**本輪新增之多引用字串**
（`CFTS022-4915171; CFTS022-4915170` 寫入單一儲存格之形態）
皆未經寫回路徑驗證。Privacy 之寫回腳本尚未建立（R20-5）。
下放包 13 §5 已預告此為下一階段重點。

<!-- UPSTREAM-COVERS: 13 -->
