# 上繳包 09 — B1 pilot digest（leaves -001…-005）

執行層 → 分析層。2026-08-13。回應 `docs/handoff/09_b1_pilot.md` §3 之七項。

**四項停手條件全部未觸發。** 台帳於生成前後各驗一次，皆綠。
**本批未寫回 workbook**（§3 明文）。

---

## 1. §3.2 —— 一頁 digest

### 1.1 TC 數與分布

**5 leaves → 6 TC。** 落在 §2.4 之預估區間（5–7）下緣。

| leaf | Test Set | artifact | TC 數 | design_method | priority |
|---|---|---|---|---|---|
| -001 | Input Monitoring | 4914955 | 1 | 狀態轉換 | **P0** |
| -002 | Personalization Display | 4915158 | 1 | 狀態轉換 | P1 |
| -003 | Speed-Controlled Volume | 4915168 | 1 | 狀態轉換 | P1 |
| -004 | Speed-Controlled Volume | 4915169 | 1 | 狀態轉換 | P1 |
| -005 | Speed-Controlled Volume | 4915170 | **2** | 等價劃分 / 負向測試 | P1 / P2 |

design_method 分布：狀態轉換 4、等價劃分 1、負向測試 1。
priority 分布：P0 ×1、P1 ×4、P2 ×1。

### 1.2 每葉之切分理由與所引條號

| leaf | 切/不切 | 依據 |
|---|---|---|
| -001 | 不拆，1 TC | 條文為單一觸發（退出 SLEEP MODE）對單一結果（監測按鍵狀態），無切分軸 |
| -002 | 不拆，1 TC | 同上；功能清單未列舉故無法以項目切（§8.4.1）|
| -003 | 不與 -004 合併 | §8.2.1 —— 觸發措辭不同（`wakes up on Interior CAN` vs `wakes up`）、驗證面不同（recall vs send）|
| -004 | 不與 -003 合併 | 同上 |
| -005 | **拆 2 TC** | **§7**（列舉之支援項須配至少一負向）+ **§5.2**（禁止程序內分支）—— 正向側驗四個等價類、負向側驗集合外之值不出現，兩者驗證目標不同 |

**未為湊數而拆，亦未為省事而併**：-005 是本批唯一被拆的葉子，
理由是條文本身列舉了四個有效值並明文界定「其餘為無效」。

### 1.3 priority 之依據（framework Part I：由「失敗時偵測不到什麼」決定）

| TC | priority | 失敗時偵測不到的是 |
|---|---|---|
| -001 | **P0** | 退出 SLEEP MODE 後 HU 完全不監測按鍵 → 每次喚醒後實體按鍵全數失效。這是功能面之全失，非顯示層缺陷 |
| -002 | P1 | 個人化設定顯示為預設值而非上次狀態 —— 使用者可見之資料錯誤，非功能喪失 |
| -003 | P1 | SCV 狀態未召回，行為回到預設 |
| -004 | P1 | $VolumeSCV$ 未於時限內送出，下游取不到狀態 |
| -005 TC1 | P1 | 四個有效值未被正確送出 |
| -005 TC2 | P2 | 集合外之值被送出。此為穩健性檢查，其失敗多半已在 TC1 之範圍內顯現，故低一級 |

**本批有一個 P0。** 依 framework Part I，不為平衡而調整 —— P0 給 -001
是因為它的失敗面確實是全域輸入失效，不是因為批次「該有一個 P0」。

### 1.4 `distinguishing_axis` 清單

| leaf | axis | delta |
|---|---|---|
| -001 | none | — |
| -002 | none | — |
| -003 | verification face | 驗喚醒後之**內部狀態召回**（recall）|
| -004 | verification face | 驗喚醒後之**對外訊號傳送**（send）|
| -005 | partition side | TC1 驗有效值四個等價類之傳送；TC2 驗集合外之值不被送出 |

---

## 2. §3.3 —— 逐葉範圍指示之遵守自證

### 2.1 -001：排除 4914956 與 external DVD player

- **4914956（120 秒 stuck button DTC）已排除。** 全 TC 內**無**
  「120」、「DTC」、「stuck」、「not pressed value」等字樣。
  說明位置：`reasoning` 第四句，明指其為另一條 SFR、依 §8.2.1 排除。
- **ECU 範圍已收斂至 HU 側。** `test_item` 把條文之
  `the HU and external DVD player` 收為 `the HU`；
  說明位置：`reasoning` 末句，指出 4914955 之 ECU tag 為
  `ETM, RRM, ICS, DVD, LTM`、本交付件為 LTM、DVD 播放器之行為屬該 ECU
  自身之驗證（§8.4.2）。

### 2.2 -002：排除 4915159 —— 本批最需防守的一條

- **TC 內無任何 splash screen 或時間門檻字樣**（已機械檢查：
  `splash`、`VF169`、秒數皆為 0 命中）。
- 說明位置：`reasoning` 第四句，並**明寫該條正是先前對映誤填之 id
  （R30-1）、相鄰且語意相近**，特別標記以免被吸收。
  這是照 §2.2 之警語辦理，不是事後補述。
- **4915157 未列為 `specification_reference`**：其 `Artifact Type` 為
  `Description`（實測），僅供背景理解。`reasoning` 內載明。
- **功能清單未自行列舉**：條文只寫
  `the configured set of personalization features`，步驟與 ER 一律沿用
  該措辭，未出現任何具體功能名（§8.4.1）。

### 2.3 -003 / -004：不互相補齊

- -003 之 `test_item` 為 `When the HU wakes up on Interior CAN`；
  -004 為 `When the HU wakes up` —— **各自照條文原樣**，
  未把 Interior CAN 補進 -004，也未把它自 -003 拿掉。
- `distinguishing_axis` 已指出 recall vs send（見 §1.4）。

### 2.4 -004：`<Tsend>` 未填任何數值

- `test_item`、`test_procedure` 步驟 4、`expected_result` 步驟 4
  **一律寫 `<Tsend>` 原符號**。全檔無任何秒數／毫秒數（機械檢查：
  數字僅出現於步驟序號）。

### 2.5 -005：不 BLOCKED、方括號保留、逐 TC 判定設計方法

- **未 BLOCKED**：四個有效值 `[Off]` / `[level 1]` / `[level 2]` /
  `[level 3]` 存在於條文內，本條自足。
- **方括號保留**：`[Off]` 等以 source-quoted signal value 形式出現於
  `input_test_data` 與 ER（profile §3.4 之 §11 例外）。作者自撰之 UI
  label 本批未出現，故無 `"..."` 用例。
- **設計方法逐 TC 判定**：TC1（驗劃分本身）為
  `等價劃分 (Equivalence Partitioning, EP)`；TC2（只驗無效側）為
  `負向測試 (Negative / Invalid)` —— 即 profile §3.3 修訂 1
  「若拆為多 TC，每個 TC 各自適用 §12」之首次適用。**未全批一律。**

---

## 3. §3.4 —— -005 之 ECU 範圍：兩種讀法（不自行結論）

條文之 outcome 主詞為 **AMP**：
「All other signals shall be considered invalid **by the AMP** and no action
shall be taken.」而本交付件之 ECU 為 **LTM**（HU 側）。

| 讀法 | 可觀察面 | 本 ECU 可驗？ |
|---|---|---|
| **(i) HU 側** | HU 只送出有效值集合內之值 | ✅ 可（CAN trace 觀察 $VolumeSCV$）|
| **(ii) AMP 側** | AMP 收到無效值時不改變狀態 | ❌ 屬另一 ECU 之行為 |

**依 §2.2 之指示採 (i) 產出**，兩條 TC 皆自 HU 側可觀察。
**(ii) 之歸屬未自行結論** —— 已完整陳述於 -005 之 `reasoning` 末段。

**停手條件 3 未觸發**：(i) 讀法能產生可觀察之 Final Step ——
TC1 之 ER 為「$VolumeSCV$ 訊號攜帶 [level N]」，TC2 之 ER 為
「trace 內每一筆 $VolumeSCV$ 皆為四值之一，無其他值」，兩者皆在
CAN trace 上可判定。

**待 pilot review 裁定者**：若裁定 (ii) 才是本葉之驗證目標，
則本葉之兩條 TC 須改寫，且該行為之歸屬（AMP 之 037）須另案處理。

---

## 4. §3.5 —— lint 結果

⚠️ **Privacy 尚無 lint 腳本。** `features/privacy/scripts/` 下目前只有
`xlsx_roundtrip_probe.py`。試以 `features/amfm/scripts/lint_tcs.py
--feature-dir features/privacy` 執行，於前置檢查即中止：

```
data/stla_to_cfts.json missing — run build_stla_map.py
```

該 gate 讀的是 AMFM 專屬之 STLA→CFTS 對映檔，Privacy 之對映結構不同
（PROF→artifact，且已知不可算術推定），**不能直接沿用**。

**代用之機械檢查（非等同 lint）** —— 只驗可機械判定且權威明確者：

```
TC 數: 6
design_method 分布: {'狀態轉換 (State Transition Testing)': 4,
                      '等價劃分 (Equivalence Partitioning, EP)': 1,
                      '負向測試 (Negative / Invalid)': 1}
priority 分布: {'P0': 1, 'P1': 4, 'P2': 1}

檢查項: design_method∈下拉選單9詞條 / test_group=Privacy / test_set∈3 Set /
        priority∈P0..P3 / remarks 空 / spec_ref 格式 CFTS022-{7位} /
        artifact∈§2.1 表 / artifact 確實查得於 CFTS022 全集 /
        ER 無 modal 動詞 / 步驟與 ER 條數相符 / 步驟≥2 /
        未用被禁之 'HU is powered on' / assumptions 空

findings: 0
PASS
```

**這不是 lint。** 未涵蓋者包括：spec_reference 是否對應正確條文（語意）、
Test Item 措辭是否合於 profile §3.1、切分是否合於 §8.3、
absorption gate、cross-reference gate。**Privacy 之 lint 腳本應在 P6 之前建立**
（見 §6.1）。

---

## 5. §3.6 —— 台帳兩條指令輸出

生成前（停手條件 4 之前置檢查）與生成後各一次，四次皆綠：

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=1  FAILED=0
```

`DELIVERY` 之 1 OK 為 ENTRY 001 之準備完成工作簿。**本批未寫回**，
故未新增 ENTRY —— 符合 R27-2 之記錄單位判準（記的是一次 `--write`
之輸入基準與輸出，生成階段不入台帳）。

---

## 6. §3.7 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。第 1、2 項建議在 pilot review 一併處理。**

### 6.1 Privacy 沒有 lint，而 §3.5 要的是 lint

上面那份機械檢查是我自己訂的檢查項，**權威來源是我對 profile 的閱讀，
不是一份被核可過的 gate**。它驗不到任何判斷型規則。
AMFM 與 SXM 都有 `lint_tcs.py`，Privacy 沒有 —— B1 只有 6 條 TC，
人工可讀完；**B2 之後不行**。建議在 P6 之前建立，且其 gate 應涵蓋
profile §3.3（design method 逐 TC）、§3.5（spec_reference 形式）、
§3.9（車型欄留白）、§3.8（欄 S = NA）。

### 6.2 ⚠️ 037 之 Requirement Description 主張了 CFTS 條文沒有的行為

這是本批最需要裁定的一件事，**三片葉子都有**：

| leaf | CFTS022 條文 | 037 Description / Verification Criteria 額外主張 |
|---|---|---|
| -001 | 「退出 SLEEP MODE 後，HU 監測按鍵按壓狀態」 | 「**轉換階段中按鍵輸入不得被處理**，只有在達到 active 狀態後才處理」—— 條文**無**此句 |
| -002 | 「Interior CAN 喚醒時召回上次狀態以供顯示」 | 「**不得顯示預設值或錯誤值**」、「**無需使用者互動**」—— 條文未明文 |
| -003 | 「HU 於 Interior CAN 喚醒時召回 SCV 狀態」 | 「**喚醒後音量隨車速調整之行為須持續正確**」—— 條文未及於行為本身 |

我**依 CFTS022 條文產出**（spec_mode D：clause 權威為 CFTS022），
未把 037 的額外主張寫進 TC —— 若寫了，該 TC 的
`specification_reference` 會指向一條沒有那句話的條文。

**但這代表 037 葉子自身陳述的一部分目前無 TC 覆蓋。** 這不是我能裁的：
它牽涉「037 Description 是否為獨立之需求來源」這個層級的問題，
而 canon 的 trace chain 寫的是 CFTS022 → 037 → TC。
**未創設 marker、未登 assumption**（依 §2.3「不自行創設 marker」與
停手條件 2 之界線 —— 我沒有做出任何假設，只是照條文寫），
但請於 pilot review 裁定：補 TC、登 anomaly、或確認 037 Description
僅為闡釋而非追加需求。

### 6.3 -001 之 P0 是我判的

framework Part I 給的是判準（由失敗時偵測不到什麼決定），不是分級表。
「退出睡眠後按鍵全失效」我判為 P0，但**本批唯一的 P0 出自我的判斷**，
且 AMFM 之同類可用性檢查用的是 P1。若 review 認為應為 P1，改起來是一格。

### 6.4 Pre-Condition 之措辭未回溯 CFTS022 原文

profile §3.2 列了三組合法 spec-trigger，我照它寫。但
`The A&T System is in 'SLEEP MODE'`、`The Interior CAN is asleep`
等措辭是我依條文改寫的，**未逐句回到 CFTS022 核對其原始措辭**
—— 這是上繳包 04 §6.3 已列而至今未辦的同一項。

### 6.5 CAN trace 類步驟假定了工具能力

-004 / -005 之步驟寫「CAN interface tool 連接並記錄」。
CFTS022 未規定測試環境，profile 亦無測試環境條款。
這是**測試可執行性之假定**，非需求之假定，故未登 assumption ——
但若實驗室無此能力，這三條 TC 不可執行。宜於 review 確認。

---

## 附：§3.1 生成之 JSON 全文（5 leaves）

#### `SWE1-HMI-PRIVACY_FEATURES-001.json`

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-001",
 "batch": "Input Monitoring",
 "reasoning": "驗證目標：A&T System 退出 SLEEP MODE 後，HU 對按鍵按壓狀態之監測確實恢復（CFTS022-4914955）。關鍵情境條件：系統先進入 SLEEP MODE，再以正常喚醒路徑退出，於恢復為 active 後操作實體按鍵。為什麼這樣切：條文只陳述「退出 SLEEP MODE 後監測按鍵狀態」一件事，單一觸發對單一結果，一條 TC 足夠。刻意排除兩項：其一，4914956（按壓超過 120 秒 → 設 stuck button DTC 並送 not pressed 值）是另一條 SFR，其門檻、DTC 與 not pressed 值一律不進本 TC（§8.2.1）；其二，條文主詞為 the HU and external DVD player，而 external DVD player 為另一 ECU（該 artifact 之 ECU tag 為 ETM, RRM, ICS, DVD, LTM），本交付件之 ECU 為 LTM，故只驗 HU 側，DVD 播放器之行為屬該 ECU 自身之驗證（§8.4.2）。",
 "keywords": [
  "SLEEP MODE",
  "button pressed status",
  "monitor",
  "wake-up"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "none",
  "delta": ""
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-001",
   "tc_title": "Button press monitoring resumes after the A&T System exits SLEEP MODE",
   "test_group": "Privacy",
   "test_set": "Input Monitoring",
   "test_item": "When the A&T System exits 'SLEEP MODE', the HU shall monitor the button pressed status",
   "pre_conditions": "1. The A&T System is in 'SLEEP MODE'\n2. A CAN interface tool is connected and able to log the button status messages sent by the HU",
   "input_test_data": "NA",
   "test_procedure": "1. Trigger the wake-up of the A&T System from 'SLEEP MODE'\n2. Wait until the A&T System has reached the active operational state\n3. Press a hard-key button on the HU\n4. Release the button\n5. Press a different hard-key button on the HU",
   "expected_result": "1. The A&T System starts to exit 'SLEEP MODE'\n2. The A&T System is in the active operational state\n3. The HU reports the pressed state for the operated button\n4. The HU reports the not pressed state for the released button\n5. The HU reports the pressed state for the second operated button",
   "specification_reference": "CFTS022-4914955",
   "priority": "P0",
   "design_method": "狀態轉換 (State Transition Testing)",
   "remarks": ""
  }
 ]
}
```

#### `SWE1-HMI-PRIVACY_FEATURES-002.json`

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-002",
 "batch": "Personalization Display",
 "reasoning": "驗證目標：Interior CAN 每次喚醒時，HU 對「已組態之個人化功能集合」召回其最後已知狀態並據以顯示（CFTS022-4915158）。關鍵情境條件：先把個人化功能設為非預設值，進入睡眠，再以 Interior CAN 喚醒。為什麼這樣切：條文之觸發（Interior CAN 喚醒）與結果（召回上次狀態以供顯示）為一組，一條 TC 足夠。刻意排除：4915159「features 須在 splash screen 完成時間內備妥顯示」是時序需求，與召回狀態是兩件事，且其 Note 指向 {VF169}；本 TC 不出現任何 splash screen 或時間門檻 —— 該條正是先前對映誤填之 id（R30-1），相鄰且語意相近，特別標記以免被吸收。4915157 為 Description 型（HU 決定車上存在哪些 features），僅供背景理解，不列為 specification_reference。另：條文未給出「configured set of personalization features」之具體清單，依 §8.4.1 不自行列舉功能項，步驟與 ER 一律以 spec 措辭表述。",
 "keywords": [
  "Interior CAN",
  "wake up",
  "personalization features",
  "last known state",
  "recall"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "none",
  "delta": ""
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-002",
   "tc_title": "Personalization features are recalled to their last known state on Interior CAN wake-up",
   "test_group": "Privacy",
   "test_set": "Personalization Display",
   "test_item": "Each time the Interior CAN wakes up, the HU shall recall the last known state for the configured set of personalization features to be displayed",
   "pre_conditions": "1. The configured set of personalization features is set to states other than their default states\n2. The Interior CAN is asleep",
   "input_test_data": "NA",
   "test_procedure": "1. Record the state of each feature in the configured set of personalization features\n2. Trigger the wake-up of the Interior CAN\n3. Read the state of each feature in the configured set of personalization features as displayed by the HU\n4. Trigger the Interior CAN to sleep and wake it up a second time\n5. Read the state of each feature in the configured set of personalization features as displayed by the HU",
   "expected_result": "1. The state of each feature in the configured set is recorded\n2. The Interior CAN is awake\n3. Each feature in the configured set is displayed in the state recorded in step 1\n4. The Interior CAN is awake\n5. Each feature in the configured set is displayed in the state recorded in step 1",
   "specification_reference": "CFTS022-4915158",
   "priority": "P1",
   "design_method": "狀態轉換 (State Transition Testing)",
   "remarks": ""
  }
 ]
}
```

#### `SWE1-HMI-PRIVACY_FEATURES-003.json`

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-003",
 "batch": "Speed-Controlled Volume",
 "reasoning": "驗證目標：HU 於 Interior CAN 上喚醒時，召回 speed controlled volume 之狀態（CFTS022-4915168）。關鍵情境條件：先把 SCV 設為非預設狀態，睡眠後以 Interior CAN 喚醒 HU。為什麼這樣切：本條與兄弟 leaf -004 觸發條件不同、驗證面也不同，不得合併 —— 本條之觸發為 wakes up on Interior CAN（明文限定 Interior CAN），驗的是內部狀態之召回；-004 之觸發為 wakes up（未限定介面），驗的是對外訊號之傳送。兩者照條文原樣寫，不互相補齊。刻意略過：SCV 隨車速調整音量之行為本身不在本條範圍，本條只驗喚醒後狀態被召回這一層。",
 "keywords": [
  "$VolumeSCV$",
  "speed controlled volume",
  "Interior CAN",
  "wake up",
  "recall"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "verification face",
  "delta": "-003 驗喚醒後之內部狀態召回（recall）；-004 驗喚醒後之對外訊號傳送（send）"
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-003",
   "tc_title": "Speed controlled volume state is recalled when the HU wakes up on Interior CAN",
   "test_group": "Privacy",
   "test_set": "Speed-Controlled Volume",
   "test_item": "When the HU wakes up on Interior CAN, the HU shall recall the state of the speed controlled volume",
   "pre_conditions": "1. The speed controlled volume is set to a state other than its default state\n2. The HU is asleep",
   "input_test_data": "NA",
   "test_procedure": "1. Record the state of the speed controlled volume\n2. Trigger the wake-up of the HU on Interior CAN\n3. Read the state of the speed controlled volume on the HU\n4. Set the speed controlled volume to a different state, put the HU to sleep and trigger the wake-up of the HU on Interior CAN again\n5. Read the state of the speed controlled volume on the HU",
   "expected_result": "1. The state of the speed controlled volume is recorded\n2. The HU is awake\n3. The speed controlled volume is in the state recorded in step 1\n4. The HU is awake\n5. The speed controlled volume is in the state set in step 4",
   "specification_reference": "CFTS022-4915168",
   "priority": "P1",
   "design_method": "狀態轉換 (State Transition Testing)",
   "remarks": ""
  }
 ]
}
```

#### `SWE1-HMI-PRIVACY_FEATURES-004.json`

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-004",
 "batch": "Speed-Controlled Volume",
 "reasoning": "驗證目標：HU 喚醒時，於 <Tsend> 內以 $VolumeSCV$ 訊號送出 speed controlled volume 之狀態（CFTS022-4915169）。關鍵情境條件：SCV 先設為已知狀態，HU 睡眠後喚醒，於匯流排上觀察 $VolumeSCV$ 之發送時點與值。為什麼這樣切：與 -003 之區辨軸為「內部召回 vs 對外傳送」，觸發措辭亦不同（本條為 wakes up，未限定 Interior CAN），照條文原樣寫。刻意不填具體時間：<Tsend> 在條文內未定義具體值，依 §8.4.1 保留原符號，步驟與 ER 一律寫 <Tsend>，不填入任何秒數或毫秒數。",
 "keywords": [
  "$VolumeSCV$",
  "<Tsend>",
  "speed controlled volume",
  "wake up",
  "signal transmission"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "verification face",
  "delta": "-004 驗對外訊號之傳送與時限；-003 驗內部狀態之召回"
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-004",
   "tc_title": "$VolumeSCV$ is sent within <Tsend> when the HU wakes up",
   "test_group": "Privacy",
   "test_set": "Speed-Controlled Volume",
   "test_item": "When the HU wakes up, the HU shall send the status of the speed controlled volume in the $VolumeSCV$ signal within <Tsend>",
   "pre_conditions": "1. The speed controlled volume is set to a known state\n2. The HU is asleep\n3. A CAN interface tool is connected and logging with timestamps",
   "input_test_data": "NA",
   "test_procedure": "1. Record the state of the speed controlled volume\n2. Start the CAN trace\n3. Trigger the wake-up of the HU\n4. Read the first $VolumeSCV$ signal in the CAN trace and its timestamp relative to the wake-up\n5. Read the value carried in that $VolumeSCV$ signal",
   "expected_result": "1. The state of the speed controlled volume is recorded\n2. The CAN trace is running\n3. The HU is awake\n4. The $VolumeSCV$ signal is sent within <Tsend> of the wake-up\n5. The $VolumeSCV$ signal carries the state recorded in step 1",
   "specification_reference": "CFTS022-4915169",
   "priority": "P1",
   "design_method": "狀態轉換 (State Transition Testing)",
   "remarks": ""
  }
 ]
}
```

#### `SWE1-HMI-PRIVACY_FEATURES-005.json`

```json
{
 "parent": "SWE1-HMI-PRIVACY_FEATURES-005",
 "batch": "Speed-Controlled Volume",
 "reasoning": "驗證目標：$VolumeSCV$ 之有效值集合為 [Off] / [level 1] / [level 2] / [level 3]，集合外之值為無效（CFTS022-4915170）。為什麼切兩條：依 §7，列舉之支援項須配至少一條負向 TC；正向側驗「四個等價類各自被正確送出」，負向側驗「集合外之值不出現」，兩者驗證目標不同，不得併為一條（§5.2 禁止程序內分支）。設計方法逐 TC 判定（profile §3.3 修訂 1）：驗劃分本身者為等價劃分，只驗無效側處置者仍適用 §12 第一列之負向測試。本條自足不 BLOCKED —— 有效值表存在於條文內，四個值逐一列出。方括號保留為 source-quoted signal value（profile §3.4 之 §11 例外）。**ECU 範圍問題，本輪不結論**：條文之 outcome 主詞為 AMP（considered invalid by the AMP and no action shall be taken），而本交付件之 ECU 為 LTM。可觀察面有兩種讀法 —— (i) HU 側：HU 只送出有效值集合內之值，本 ECU 可觀察；(ii) AMP 側：AMP 收到無效值不動作，屬另一 ECU 之行為。依下放包 09 §2.2 依 (i) 產出，(ii) 之歸屬待 pilot review 裁定。",
 "keywords": [
  "$VolumeSCV$",
  "[Off]",
  "[level 1]",
  "[level 2]",
  "[level 3]",
  "invalid"
 ],
 "duplicate_of": "",
 "distinguishing_axis": {
  "axis": "partition side",
  "delta": "TC1 驗有效值四個等價類之傳送；TC2 驗集合外之值不被送出"
 },
 "assumptions": [],
 "tcs": [
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-005",
   "tc_title": "$VolumeSCV$ carries each of the four valid values",
   "test_group": "Privacy",
   "test_set": "Speed-Controlled Volume",
   "test_item": "Valid signals for the $VolumeSCV$ signal are $VolumeSCV$ = [Off], [level 1], [level 2] and [level 3] — valid value set",
   "pre_conditions": "1. The HU is awake\n2. A CAN interface tool is connected and able to log the $VolumeSCV$ signal",
   "input_test_data": "$VolumeSCV$ = [Off]\n$VolumeSCV$ = [level 1]\n$VolumeSCV$ = [level 2]\n$VolumeSCV$ = [level 3]",
   "test_procedure": "1. Set the speed controlled volume to the state that corresponds to $VolumeSCV$ = [Off] and read the $VolumeSCV$ signal in the CAN trace\n2. Set the speed controlled volume to the state that corresponds to $VolumeSCV$ = [level 1] and read the $VolumeSCV$ signal in the CAN trace\n3. Set the speed controlled volume to the state that corresponds to $VolumeSCV$ = [level 2] and read the $VolumeSCV$ signal in the CAN trace\n4. Set the speed controlled volume to the state that corresponds to $VolumeSCV$ = [level 3] and read the $VolumeSCV$ signal in the CAN trace",
   "expected_result": "1. The $VolumeSCV$ signal carries [Off]\n2. The $VolumeSCV$ signal carries [level 1]\n3. The $VolumeSCV$ signal carries [level 2]\n4. The $VolumeSCV$ signal carries [level 3]",
   "specification_reference": "CFTS022-4915170",
   "priority": "P1",
   "design_method": "等價劃分 (Equivalence Partitioning, EP)",
   "remarks": ""
  },
  {
   "req_id": "SWE1-HMI-PRIVACY_FEATURES-005",
   "tc_title": "$VolumeSCV$ carries no value outside the valid set — invalid value set",
   "test_group": "Privacy",
   "test_set": "Speed-Controlled Volume",
   "test_item": "All signals other than $VolumeSCV$ = [Off], [level 1], [level 2] and [level 3] are invalid — invalid value set",
   "pre_conditions": "1. The HU is awake\n2. A CAN interface tool is connected and able to log the $VolumeSCV$ signal",
   "input_test_data": "NA",
   "test_procedure": "1. Start the CAN trace\n2. Step through every selectable state of the speed controlled volume on the HU\n3. Trigger the HU to sleep and wake it up again\n4. Read every $VolumeSCV$ signal captured in the CAN trace",
   "expected_result": "1. The CAN trace is running\n2. Every selectable state of the speed controlled volume is reached\n3. The HU is awake\n4. Every $VolumeSCV$ signal in the trace carries [Off], [level 1], [level 2] or [level 3], and no other value is present",
   "specification_reference": "CFTS022-4915170",
   "priority": "P2",
   "design_method": "負向測試 (Negative / Invalid)",
   "remarks": ""
  }
 ]
}
```

<!-- UPSTREAM-COVERS: 09 -->
