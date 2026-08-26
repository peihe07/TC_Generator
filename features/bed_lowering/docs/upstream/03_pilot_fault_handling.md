# 上繳包 03 — Bed Lowering Mode：pilot 批（Fault Handling）+ 四庫補綁（執行層回報）

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/03_pilot_fault_handling.md`
（sha256 `6c8967c5e7f6fd344e0288987bbd0d4423b807898af12c31b1cada80e855be67`）
執行層：Tier 1

**結論：§二 完成並驗證；§三 依其自身之 §三-3 停下回報（`vehicle_setting` 綁 0/4）；
§四 pilot 未執行 —— 受 §三 阻斷，而 §三 之標題自載「pilot 前完成」。**

本包一切數字自腳本 stdout 複製（R-G20）。R-G 引用一律 FO 讀法（R-BLM10）。

---

## 一、R-G20 —— 規則副本現行指紋

| 檔 | SHA256 |
|---|---|
| `docs/runtime/ASPICE_SWE6_AI_Instruction.md` | `0b0cea006552a2f244ba8e733ef6227b132b591a34defb65234934985fe2598e` |
| `features/bed_lowering/feature.yaml`（**本包改後**）| `b5104c6ecf8957611831586f7f18bffb6297d018c1310be7f1bd95642a81360e` |

改前為 `fbad5bc87e065cfe5e248ff57607c10576ffdda35af369a028e372d6b113f007`（上繳 02 §二）。

---

## 二、`feature.yaml` 補一鍵 —— 完成

`spec_mode: null` → `spec_mode: "D"`（R-BLM7）。其餘一字未動（R-BLM8 已追認現檔）。

重跑上繳 02 §七之載入指令，通過：

```
spec_mode = 'D'
spec_reference_template = None
四條 paths 各解析到恰好一個檔
```

`spec_reference_template` 仍為 `None`，未受本次改動影響 —— 該鍵與 `spec_mode`
在 `feature_config.py` 中無耦合，但仍實測確認而非推定。

**檔內註解已一併更新**：原 `spec_mode` 上方之「⚠ 未定 —— 不猜（A-BLM7）」
整段已改寫為 R-BLM7 之裁定與其理由。留著舊註解會使檔案自相矛盾。

---

## 三、四庫補綁 —— **停下回報（§三-3 之情形成立）**

### 3.1 停下之依據

§三-2 之指示為「讀 `features/vehicle_setting/feature.yaml` 之 `reference:` 節，
四項**逐字抄**檔名與路徑」。

**實測：`features/vehicle_setting/feature.yaml` 全檔 125 行，
無 `reference:` 節，四項綁 0 個。**
全檔僅兩處出現 "reference" 字樣，皆與參考資料庫無關
（第 52 行 `spec_reference_template`、第 69 行欄位字母 `spec_reference: "N"`）。

§三-3：「vehicle_setting 未綁全四項 → 缺項列出停下回報待 Pei 點名，**不得自擇**」。
四項全缺，故本節依該款停下。**下列各表為供點名之材料，不是提議。**

### 3.2 全案四庫綁定現況（實測）

掃 `features/*/feature.yaml` 之 `reference:` 節：

| feature | dbc_b | dbc_fd | lid | proxi |
|---|---|---|---|---|
| `display` | ✓ | ✓ | ✓ | ✓ |
| `vehicle_setting` | — | — | — | — |
| `vehicle_category` | — | — | — | — |
| `bed_lowering`（本 feature）| — | — | — | — |

**全案只有 `display` 綁了四庫。**

### 3.3 `vehicle_setting` 實際在用之四庫（雖未綁，但可查）

四檔實體存在於 `features/vehicle_setting/inputs/`，且其雜湊
**與該 feature 之 `INPUTS.sha256` 宣告 4/4 相符**（本包實算比對）：

| 庫 | 檔名 | SHA256（實算）| vs INPUTS.sha256 |
|---|---|---|---|
| lid | `Logical Identifiers and CAN Mapping v1_76.xlsx` | `ffceac36e9db145dc0311a25435b15249835e077bab264e71a95b0fb37a98ef4` | 相符 |
| dbc_b | `PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0` | 相符 |
| dbc_fd | `PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2` | 相符 |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2` | 相符 |

**這正是「不得自擇」所指之縫。** 兩種讀法皆說得通：

- 讀法甲：R-BLM9 說「沿 vehicle_setting **現綁**之版本」，而它綁 0 項 → 無可沿，停。
- 讀法乙：它**實際在用**的就是上表四檔，雜湊齊備且自洽 → 沿此四檔。

二者差別不在雜湊算不算得出（算得出，上表即是），而在
**「現綁」是否等同「在用」**。`INPUTS.sha256` 記的是「這個 feature 收了哪些檔」，
`reference:` 記的是「哪些檔一變動就使既有產出失效」——
兩者用途不同，前者不能自動當後者。執行層不代裁。

### 3.4 與 `display` 之版本歧異（點名前請一併看）

若採讀法乙，本 feature 將與 `display` 綁到**不同版本**：

| 庫 | vehicle_setting（讀法乙）| display（現綁）| 同否 |
|---|---|---|---|
| lid | `…v1_76.xlsx` | `…v1_78.xlsx` | **異** |
| dbc_b | `PDT27_E2A_R4_BHCAN.dbc` | `PDT27_E2A_R1_BHCAN2.dbc` | **異** |
| dbc_fd | `PDT27_E2A_R5_FDCAN8.dbc` | `PDT27_E2A_R1_FDCAN8.dbc` | **異** |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `PROXI_HDCC27_R3_20250424.xlsx` | 同 |

四項中三項相異。**這不是意外，正是 R-G15 立條的原因** ——
該條之理由段落逐字寫著「`features/vehicle_setting/` 使用 LID v1_76，
`features/display/` 使用 v1_78，而沒有任何條文在追這件事」。
本包實測確認該歧異至今仍在，且 `vehicle_setting` 至今仍未綁。

R-BLM9 已裁「沿 vehicle_setting（同 FROP、同 N1L 車系）」，
故版本歧異本身應為已知且被接受之後果，非新問題。**此表僅為點名時之對照。**

### 3.5 點名後執行層將做什麼

Pei 點名後，執行層逐項寫入本 feature `reference:` 節，
**sha256 一律自實體檔重算**（§三-2 明令不抄他檔之宣告值）。
若實算值與點名所據之來源不符，依 R-G23 停並回報兩值，不自行更新宣告值。

---

## 四、Pilot 批 —— **未執行**

### 4.1 未執行之依據

§三 之標題即「四庫補綁（R-BLM9，**pilot 前完成**）」。§三 停下，§四 隨之不開工。

### 4.2 這不只是形式上的順序 —— 實測 13 leaf 確有訊號依賴

以 `data/test_set_map.tsv` 過濾 `leaf_inventory.tsv` 取 `Fault Handling` 組，
得 **13 leaf**（與 §四、framework Part III、上繳 02 §4.3 三處相符）：

```
SWE1-HMI-BLM-011-01  [HMI/High]    Detect Lowering Fault Condition
SWE1-HMI-BLM-011-02  [HMI/Medium]  Detect Angle Achievement Failure
SWE1-HMI-BLM-011-03  [HMI/High]    EVIC Failure Message Output
SWE1-HMI-BLM-011-04  [HMI/Medium]  Air Suspension Service Indication
SWE1-HMI-BLM-037-01  [HMI/High]    Detect Command Processing Failure
SWE1-HMI-BLM-037-02  [HMI/High]    Receive Air Suspension Fault Feedback
SWE1-HMI-BLM-037-03  [HMI/High]    Turn Off Button Highlight
SWE1-HMI-BLM-037-04  [HMI/High]    Remove Highlight on Fault Feedback
SWE1-HMI-BLM-037-05  [HMI/High]    Failure Highlight Removal Feedback
SWE1-HMI-BLM-038-01  [HMI/High]    EVIC Unsuccessful Message
SWE1-HMI-BLM-038-02  [HMI/Medium]  EVIC User-Visible Failure Output
SWE1-HMI-BLM-038-03  [HMI/Medium]  Air Suspension Service Indication
SWE1-HMI-BLM-038-04  [HMI/Medium]  Failure Message Reference Alignment
```

13 leaf 全為 `Sub Categorization = HMI`，與 framework Part III 之 `13 | 13/0` 相符。

關鍵字掃描（母體 = 13 leaf 之 title＋description＋verification criteria／method 全文）：

| 探針 | 命中 | 內容 |
|---|---|---|
| PROXI／車型配置 | **0** | — |
| LID／logical identifier | **0** | — |
| 速度門檻（DR-1）| **0** | 與 §四「011/037/038 群預期不含」相符 |
| fault 注入 | 48 | `fault` 18／`failure` 18／`unsuccessful` 12 |
| EVIC | 18 | — |
| CAN／訊號 | 20 | **全部為 `message` 一詞** |

**那 20 個 `message` 須小心讀：逐條看過，全指 EVIC 顯示訊息（文案），
不是 CAN message。** 若只看計數會誤判為訊號密集群 ——
此即 R-G19 所指「數字對而理由錯」之形態，故此處具名。

真正的依賴在別處，且不靠關鍵字看得出來 ——
`SWE1-HMI-BLM-037-02 Receive Air Suspension Fault Feedback` 之原文為
「The system shall **receive fault feedback from the air-suspension system**
when a command-processing failure occurs」。要寫出可執行之 PROC，
須注入或觀察 air suspension 之 fault 回饋；依 IN §8.7.5 v3（R-1 v3），
訊號須寫作 `$<MESSAGE>.<Signal>$ = <raw> (<label>)`，label 取自 DBC `VAL_`，
**DBC 查無者才保留來源名不加 `$`**。

「查無」與「沒查」是兩件事：**沒綁 DBC 就不是查無，是沒查**。
在四庫未綁之前生成該條，只能造一個看起來合理的訊號名 ——
IN §8.4 之 fabrication，FO §0 escalation trigger 5。

### 4.3 為何不先做不含訊號的那幾條

§四 明令「以 `data/test_set_map.tsv` 過濾取列，**不手挑**」。
挑出「看起來不需訊號的」再生成，正是手挑；且該判斷本身
（哪幾條真的不需訊號）尚未經驗證，用它當切分依據即以未驗之判斷切分批次。
**pilot 為一次交付 13 條之整批，部分生成不是打了折的 pilot，是另一個東西。**

### 4.4 已就緒者（點名後可立即開工）

- 批次名單：13 leaf 已由機器過濾產出，未手挑
- 語料欄位：`title`／`description`／`verification_criteria`／
  `verification_method`／`priority_037` 皆在 `leaf_inventory.tsv` 內，欄位齊備
- N 欄預期值：`SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)`，
  批內相異值數預期 **1**（R-BLM5）
- PDF 不入語料（R-BLM7）—— 本包未讀 PDF 任何內容入任何工件

---

## 五、執行層自陳 —— 逐項自問「這一項現在驗得了嗎」

### 5.1 `prompt_builder` 相容性（§五 特別點名）—— **部分驗得，且答案與提問之預設不同**

§五 預期「首次組批即是實測，無論過不過都寫明結果」。本包未組批，
**但該項不必等組批就驗得出一部分，已驗**：

`backend/prompt_builder.py` 之公開介面為 11 個函式，簽章形如
`build_batch_prompt(rows, context, spec_index, rules_text)`。
以 `inspect.getsource` 全文掃描：

| 探針 | 結果 |
|---|---|
| 原始碼含 `feature.yaml` | **False** |
| 原始碼含 `spec_mode` | **False** |
| 原始碼含 `leaf_inventory` | **False** |

**`prompt_builder` 根本不讀 `feature.yaml`。** 它收的是已組好的
`rows`／`context`／`spec_index`／`rules_text`。

故「`feature.yaml` 與 `prompt_builder` 相容嗎」這個問法本身有誤 ——
兩者之間沒有直接介面。真正承擔轉換的是各 feature 自己的
`scripts/make_batch_context.py`，而**本 feature 尚無此檔**
（實測：`features/bed_lowering/scripts/` 僅有本線自建之
`build_inventory.py` 與 `xlsx_structure_probe.py`）。
全案有此檔者為 `amfm`／`home`／`media`／`sxm` 四者，是移植來源。

**未驗之剩餘部分**：該 adapter 移植後能否正確餵飽 `prompt_builder`，
仍須實跑。本項於下一包必然被驗到，屆時如實回報。

### 5.2 其餘未驗項

1. **`recon.py` 仍未實跑** —— 沿上繳 02 §八-3 之理由。`spec_mode` 現已定為 D，
   該理由之一半已消失；另一半（recon 會寫 `RECON.md` 與 `data/` 下另一張表，
   R-G4 之覆寫事故形態）仍在。**本包未跑，故 `recon_assertions` 兩鍵
   至今仍是宣告而未經 recon 實跑驗證**，與上繳 02 之狀態相同，未改善。
2. **四庫之內容未查** —— 本包只算了四檔之 sha256，**未開啟任何一檔**，
   未驗證其中是否真有 air suspension 相關訊號。
   故「綁上就查得到」是預期，不是實測。點名並綁定後，
   生成期首批須先實查，查無者依 IN §8.7.5 v3 (d)/(g) 保留來源名。
3. **13 leaf 之關鍵字掃描為 lexical，非語意** —— §4.2 之 0 命中
   （PROXI／LID／速度門檻）只證明那些**詞**不出現，
   不證明那些**依賴**不存在。§4.2 之 `message` 一例即示範了同一枚硬幣的另一面：
   詞出現而依賴不存在。兩向皆為該方法之盲區（R-G11）。
4. **§三 之兩種讀法未窮舉** —— 只列了甲乙兩讀。可能另有第三讀
   （例如四庫應沿 `display` 而非 `vehicle_setting`），本包未窮舉，
   亦不宜由執行層窮舉 —— R-BLM9 已明文指定 vehicle_setting。

---

## 六、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`，owner: chassis engineering）| 已登記，未送出 |

本包未新增 DR。§4.2 實測 Fault Handling 13 leaf 之速度門檻命中 **0**，
與 §四「011/037/038 群預期不含」相符 —— pilot 批預期不觸發 DR-1 佔位。

---

## 七、待 Pei 之項

| # | 項 | 阻斷什麼 |
|---|---|---|
| 1 | **§三 四庫點名**（材料見 §3.2–3.4）| **pilot 批。唯一阻斷項** |
| 2 | （點名後無需再裁）adapter 移植與 pilot 生成 | 屬 Tier 1，點名後執行層逕行至「生成 13 TC 後停」 |
