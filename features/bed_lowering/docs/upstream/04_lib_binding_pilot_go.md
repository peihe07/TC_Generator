# 上繳包 04 — Bed Lowering Mode：四庫綁定 + pilot 批（Fault Handling）13 TC

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/04_lib_binding_pilot_go.md`
（sha256 `7785ccd10294585de26a6f279114bf7f41f4cbd28bad6bcacf4abe9eff53b21d`）
執行層：Tier 1

**結論：續行清單五項全數完成，13 TC 生成後停於 `batches/pilot/`，未寫回。
交 Pei 逐 TC 審。**

本包一切數字自腳本 stdout 複製（R-G20）。R-G 引用取 FO 讀法（R-BLM10）。

---

## 〇、先講最要緊的一件事 —— 上繳 03 的訊號結論不完整

上繳包 03 §4.2 我判 pilot 群「真正的依賴在別處，且不靠關鍵字看得出來」，
並以此支持 §三 之停下。**該判斷之方向對，但其掃描本身是壞的，而我當時
沒看出來。** 本包補綁四庫後第一件事就翻掉了它：

- 03 §4.2 之詞表取自 037 英文原文（`air suspension`／`fault`／`bed lowering`），
  在 DBC 訊號名上幾乎全數落空或命中雜訊 —— `lwr` 命中 `HVAC_Blwr_Perct`（暖氣鼓風機），
  而我當時把它當成「bed lowering 查有」。
- 成因：**DBC 以模組縮寫命名，空氣懸吊控制模組是 `ASCM`，
  而 `ASCM` 這個詞不出現在 037 任何一列。** 兩份文件之間沒有共同字串。

**橋樑是 LID。** `CAN Mapping` 分頁有英文描述欄，
`Air suspension status` → `AirSuspensionStatus` → `ASCM_Stat`。
亦即：**LID 不只是「第四個庫」，它是 037 語彙與 DBC 命名之間唯一的對照表。**
少綁它，另外三個庫綁了也查不到東西 —— 這一點 R-G15 之條文沒說，
本包實測補上。

改用「037 語彙 ∪ 自 LID 描述欄查得之 DBC 識別字」後，pilot 所需之訊號全部查有。
詞表兩者皆保留：只留後者會使查詢自我實現（拿 DBC 的名去查 DBC）。

---

## 一、續行清單 §二-1 —— `reference:` 四項寫入 + 重算

依 R-BLM11 綁 `vehicle_setting/inputs/` 之原件（不複製入本 feature `inputs/` ——
原件變動才是要偵測的事件，複本只會跟著變）。

sha256 **全數自實體檔重算**，與 R-BLM11 所載全長值逐字比對：

| 庫 | 檔 | 重算 sha256 | vs R-BLM11 |
|---|---|---|---|
| lid | `Logical Identifiers and CAN Mapping v1_76.xlsx` | `ffceac36e9db145dc0311a25435b15249835e077bab264e71a95b0fb37a98ef4` | 相符 |
| dbc_b | `PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0` | 相符 |
| dbc_fd | `PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2` | 相符 |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2` | 相符 |

比對程式落 `scripts/verify_reference_binding.py`（R-G23 之執行面：
綁定須**被檢查**，宣告不等於保護）。全節 8 項實跑：

```
8 bound, 0 failing
```

---

## 二、§二-2 —— 四庫開檔可用性（上繳 03 §5.2 自陳之未驗項，現已驗）

`scripts/probe_reference_dbs.py`，四庫全部開得起來：

| 庫 | 實測 |
|---|---|
| dbc_b | cp1252，8,591 行，BO_ **155** 訊息，SG_ **914**（相異 883），VAL_ **651** |
| dbc_fd | cp1252，20,972 行，BO_ **323** 訊息，SG_ **2,037**（相異 1,755），VAL_ **1,524** |
| lid | 14 分頁；`CAN Mapping` **2,629** 列、`Proxi & Configuration` 449 列 |
| proxi | 13 分頁；`Format` 1,060 列、`Revision Notes` 916 列 |

兩支 DBC 皆非 UTF-8（cp1252）—— 以 UTF-8 硬讀會 `UnicodeDecodeError`，
探針逐一嘗試 utf-8 → cp1252 → latin-1 並回報實際命中之編碼。

---

## 三、§二-3 —— pilot 13 leaf 之訊號預查：**全部查有**

### 3.1 承載訊息之權威為 DBC，不是 LID

LID 查得識別字後回 DBC 定位，發現**訊息名兩邊不一致**：

| 訊號 | DBC 實際承載（權威）| LID v1_76 記載 |
|---|---|---|
| `BDL_Enbl` | `ASCM_FD_2` (0x5A5) | `ASCM_3` |
| `ASCM_SysFail` | `ASCM_FD_2` (0x5A5) | `ASCM_2` |
| `ASCM_Srv` | `ASCM_FD_2` (0x5A5) | `ASCM_2` |
| `ASCM_Stat` | `ASCM_FD_2` (0x5A5) | `GW_C_I_11` |
| `FL/FR/RL/RR_Lvl` | `ASCM_FD_1` (0x52F) | `ASCM_1` |

八個全部不一致，且形態一致（LID 用 pre-FD 名，綁定之 FD DBC 用 `ASCM_FD_*`）。
依 IN §8.7.5(a)，`$<MESSAGE>.<Signal>$` 之 MESSAGE 取自 DBC，故 TC 一律用 `ASCM_FD_*`。
**此非錯誤，是兩份文件之命名世代不同**；記於此以免日後有人拿 LID 的名去對 TC 而誤判。

### 3.2 pilot 實際使用之四個訊號（VAL_ 列舉逐字取自 DBC，R-7）

| 訊號 | VAL_ 列舉 | 用於 |
|---|---|---|
| `$ASCM_FD_2.BDL_Enbl$` | `0 FALSE` / `1 TRUE` | 進入 Bed Lowering Mode |
| `$ASCM_FD_2.ASCM_SysFail$` | `0 FALSE` / `1 TRUE` | **故障注入點**（037-02 之「fault feedback」）|
| `$ASCM_FD_2.ASCM_Srv$` | `0 FALSE` / `1 TRUE` | 「Air Suspension Service Required」之來源 |
| `$ASCM_FD_2.ASCM_Stat$` | `0 NONE`…`9 LOWER`、`10 SYSFAIL`、`11 SRVS`、`15 SNA`（15 檔）| 降床與故障狀態觀察 |

`ASCM_Stat` 同時帶 `LOWER`(9) 與 `SYSFAIL`(10)，
與 Bed Lowering 之正常／失敗兩路徑逐一對應 —— 這是本批 ER 之主要觀察點。

**故本批無一條需要 (d)/(g) 之「保留來源名」，亦無「沒查」。**

落檔 `batches/pilot/signal_prelookup.json`
（sha256 `8ab834b5034ffb45ccba08637713634a7f935ea504732e97d91e3c8234761a84`）。

---

## 四、§二-4 —— adapter 移植

**移植來源：`features/amfm/scripts/make_batch_context.py`**（504 行）。
四個候選中選 amfm 之理由：它是另一個 `spec_mode: D` 之 feature
（home 為 A、media 之 feature.yaml 無 spec_mode 鍵、sxm 為 D 但 637 行且耦合較深），
已把 037 當文字權威而非讀 outline export，與本 feature 同構。

**移植時刪去者（逐項具名）**：amfm 之 context 以 `(doc, section)` 為鍵，
帶 `stla_id`／`section_title`／`spec_paragraph`，並對 037 title 與 CFTS 條文
做 `wording_agreement` 相似度比對。本 feature **無 CFTS 家族、無章節錨**
（R-BLM5 令 176 列 N 欄同值），上述每一欄若照搬皆為空值或常數。
**照搬會產出一份看起來比來源豐富的 context** —— 故刪，不留空欄。

**移植時新增者**：`signal_candidates`（自 R-BLM11 四庫）。amfm 無對應物，
因其 037 不帶 CAN 語彙。

**sibling 之等價物**：amfm 以 `(doc, section)` 括號；本 feature 以 037 母號括號
—— 母號即本 feature 之 Layer 3 單位（framework Part III），且為上游正式欄之逐字值。

實跑輸出：

```
test_set   Fault Handling
headings   ['011', '037', '038']
leaves     13
siblings   0
spec_ref   SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)
```

`siblings 0` 非缺陷：本批取的是三個母號之**全部** leaf（13/13），
括號內無批外成員，故 sibling 集為空。這正是「整組取用、不手挑」之結果。

---

## 五、§二-5 —— Pilot 13 TC，生成後停

落 `batches/pilot/pilot_tcs.json`
（sha256 `f0062c21fbb492c1a7c3005735a9b411a85345068b22d908c1e92e0e3621ff53`）。
**未寫回工作簿**（下放包 04 §三）。

### 5.1 批次統計（機器輸出）

```
TC 數 13
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 8, 'P2': 5}
design_method 分布 {'Fault Injection': 12, 'Functional Based': 1}
Input Test Data == NA 之比例 13/13
```

- **N 欄相異值數 = 1，與 R-BLM5 之單一指標相符。**
- priority：037 之 High → P1、Medium → P2（IN §10.2 之 P0–P3，
  037 之 High/Medium 不得直接入欄）。**未用 P0** —— P0 之判準為
  safety／boot／vehicle-critical CAN，本批為 HMI 顯示與 highlight 之觀察，
  故障注入之對象是台架訊號而非車輛安全機能。此映射為執行層判斷，**請一併審**。
- design_method：§12 first-match，「Simulated fault」→ Fault Injection 命中 12 條；
  038-04（訊息呈現與參考圖比對）無故障注入語意，落 Functional Based。
- Input Test Data 全 `NA`：依 §4.5 之 SWC 基準（訊號值內聯至 Procedure），
  與 SWC 0708 之 285/286 同形。

### 5.2 IN §9 自查 —— 機檢項全數 PASS，且明列機檢不覆蓋者

`scripts/selfcheck_pilot.py`：

```
機檢覆蓋之 §9 項次：1(部分) 2(部分) 4 5(部分) 10(計數) 13 14 15 16
機檢「不」覆蓋，留 pilot 人審：3 5(可執行性) 6 7 8 9 11 12 17
機檢項全數 PASS
```

機檢內容：§10.1 十鍵齊、§10.2 priority 值域、§12 design_method 值域、
§4.3.1 兩段式（下半括號、下半無中日韓字、上半 ≤50 token、同母號下半互異）、
§11（行首尾空白、尾句號、方括號、單引號）、§10.5（≥2 步）、
§6（Procedure ↔ ER 逐項 1:1、ER 無 modal）、R-BLM5（N 欄常數一致）。

**這份自查是刻意不完整的，且它自己說出來。** §9 之 3／6／7／9／11／12／17
（Pre-Condition 是否真為狀態而非動作、ER 是否真可觀察、有無 FP/FF、
是否真追溯到需求…）是閱讀判斷，機器判不了。
**一份把它們算成 PASS 的自查，比沒有自查更危險** —— 那正是 R-PMH153 之形態
（power_moding 51 條中 50 條下半為繁中，歷經多次 lint 全綠：
其 lint 只檢查括號存在，不檢查其語言）。本腳本因而檢查了下半之語言。

### 5.3 manifest（R-G19 指紋 + R-G20）

`batches/pilot/manifest.json`（sha256 `07fdf13ce20bde1ed6288449d7c013c6b29ffea5a6f38fda7ea4a871b415306f`），
指紋以 `scripts/prompt_fingerprint.py` 寫入（非手填）：

| 項 | 值 |
|---|---|
| prompt_template（五源聯集）| `0551dd30007aa5d97f6130205f8eaa4f6aba9a91e53e9cae1607abe68386bf11` |
| exemplar_set | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| IN 現行 sha256 | `0b0cea006552a2f244ba8e733ef6227b132b591a34defb65234934985fe2598e` |
| N 欄相異值數 | **1**（預期 1）|

**兩件關於指紋的事必須寫在紙上：**

1. **prompt 來源已於 `feature.yaml` 明文宣告，未取慣例預設。**
   預設為 `IN + backend/prompt_builder.py`，而
   **`backend/prompt_builder.py` 在本批未被使用** —— 本批之 TC 由
   Claude Code session 依 canon 直接撰寫，未組 prompt、未呼叫
   `backend/generator.py`。把一個未參與生成之檔列入指紋，
   會讓它的變動看起來影響產出、它的不變看起來是保證，兩者都不實。
   實際拘束本批者為五源：IN、profile、framework、RULINGS、context.json。
2. **`exemplar_set` 之 `e3b0c442…` 是空字串之 SHA256。**
   本批未使用任何 exemplar（BLANK 起建無既有 TC 可引，
   跨 feature 借用屬 Tier 2 未裁）。該值可辨識為空，非靜默之零；
   下一批若引入 exemplar，指紋即變 —— 應當變。

### 5.4 指紋比對曾不符一次，已修正 —— 並非白噪音

首次 stamp manifest 後我又改了 `feature.yaml`（加 `fingerprint:` 宣告節），
而 `context.json` 內含 `feature.yaml` 之 sha，遂連帶改變，
`--against` 比對即報：

```
prompt_template: **不符**  變動源 ['features/bed_lowering/batches/pilot/context.json']
```

**該工具指出了正確的那一個來源**，不是給一個總 sha 說「有東西變了」。
重建 context → 重 stamp 後複驗：

```
prompt_template: 相符
exemplar_set: 相符
```

記於此有兩個用處：一是證明本批之 manifest 與其產出**自我一致**（非只是「有填」），
二是 R-G19「逐源列出方能歸因」之實證 —— 若當初只存一個總 sha，
我會知道有東西變了，但不會知道是 context.json。

### 5.5 `batches/` 不入版控 —— 交審請讀磁碟

`features/bed_lowering/.gitignore` 之 `batches/` 使本批**三個產出檔皆不入 git**
（`pilot_tcs.json`／`context.json`／`manifest.json`／`signal_prelookup.json`）。
此為既有政策而非本包之疏漏：`pilot_tcs.json` 之 `tc_title` 上半為 037 需求原文
逐字，屬客戶散文，與 `inputs/` 同一政策（`projection/.gitignore` 之原文
「each row embeds the workbook's ... text verbatim」即此）。

**故交審時請直接讀磁碟上之 `features/bed_lowering/batches/pilot/pilot_tcs.json`**，
git 裡不會有。本上繳包（入版控）已載其 sha256，可對帳。
若希望 pilot 產物入版控以便日後稽核，那是一個政策裁定，本包不自行變更。

---

## 六、交審時請特別看的三處（執行層主動具名）

### 6.1 兩對近重複，未合併亦未填 `duplicate_of`

| 對 | 重疊處 |
|---|---|
| `011-03` vs `038-01` | 皆為「故障時 EVIC 顯示 `Bed Lowering Unsuccessful - Air Suspension Service Required`」。差異僅在觸發之描述：011-03 為「fault occurs 且角度未達」，038-01 為「進入 fault flow」|
| `011-04` vs `038-03` | 皆為「該訊息告知使用者需要空氣懸吊服務」。037 原文幾乎同義 |

未填 `duplicate_of`：該欄依 IN §10.6 為**列號字串**，須對應 Sibling Rows 注入之
`[row #N]`，而本批無該注入（sibling 集為空），無列號可填；
§10.6 末句「當有疑義即省略」。未逕行合併：IN §8.2.1 令尊重上游 RD 之分解，
合併等於替上游決定兩條 leaf 是一條。**故如實生成兩條並在此具名交審。**

另 `037-03`／`037-04`／`037-05` 三條同為「故障回傳 → highlight 撤除」，
以 IN §5.7 之判準看是同一 trigger 之同一結果，三條係上游自不同角度重述。
本批以三條區分之軸為：03 = 撤除本身、04 = 撤除之**時機**（fault 一回傳即撤，
其間無使用者輸入）、05 = 撤除作為**唯一** HU 端視覺回饋（tab 上無其他變化）。
**該三軸為執行層之讀法，非 037 明載，請審。**

### 6.2 懸吊角度之門檻值 037 未載

`011-02` 之原文為「failure to achieve **the specified** suspension angle」，
而 037 全欄未給該角度之數值。本批**未因此登 DR，亦未造值** ——
理由：該 TC 之注入點為 ASCM 之故障回報（`ASCM_SysFail`），
不需知道角度數值即可執行；角度由 ASCM 內部評估。
故本批以「後懸吊角落高度維持在降床前之記錄值」作為可觀察之替代判準（§5.6 baseline 形態）。

**但若 Pei 認為此群需要角度之邊界測試，該值即為缺件，屆時登 DR。**
本包把它寫在這裡而不是默默略過。

### 6.3 EVIC 文案之破折號

037 之 `Requirement Description` 用 en dash（`–`），
`Verification Criteria` 用 hyphen（`-`）。同一份文件內兩種寫法。
本批 13 條一律採 **hyphen**，依下放包 01 §四-7（以 SYS1 Basic Report
正規化文字為準）。**該選擇會逐字出現在交付欄，請確認。**

---

## 七、可重跑指令

```bash
python3 features/bed_lowering/scripts/verify_reference_binding.py   # §一
python3 features/bed_lowering/scripts/probe_reference_dbs.py        # §二
python3 features/bed_lowering/scripts/pilot_signal_prelookup.py     # §三
python3 features/bed_lowering/scripts/make_batch_context.py         # §四
python3 features/bed_lowering/scripts/selfcheck_pilot.py            # §五
python3 scripts/prompt_fingerprint.py --feature-dir features/bed_lowering \
        --against features/bed_lowering/batches/pilot/manifest.json
```

---

## 八、執行層自陳 —— 本包應驗而未驗者

1. **`backend/prompt_builder.py` 之相容性仍未驗，且本包未使本項前進。**
   上繳 03 §5.1 已查明它不讀 `feature.yaml`，真正的 adapter 是
   `make_batch_context.py`；本包移植了該 adapter 並產出 context.json，
   **但未把該 context 餵給 `prompt_builder` 實跑** —— 本批之 TC 由
   session 直接撰寫。故「context.json 之結構能被 `prompt_builder` 吃下」
   **仍是未驗**。下放包 04 §五 預期本包「必然驗到」，**實際沒有**，
   如實回報。要驗它需實際走一次 `backend/generator.py`，屬另一件事。
2. **13 條 TC 未經任何 lint 腳本。** 本 feature 尚無 `scripts/lint_tcs.py`
   （全案有者為 amfm／home／sxm／power／time_management 等）。
   §5.2 之自查為本包自寫，**與交付用 lint 非同一支**，
   其判準未經跨 feature 校準。
3. **`recon.py` 仍未實跑**（自上繳 02 起第三次記載，狀態未改善）。
   `recon_assertions` 兩鍵至今未經 recon 驗證。
4. **台架可執行性未驗。** 13 條之 Procedure 假定可於台架注入
   `$ASCM_FD_2.*$` 並觀察 EVIC。**DBC 有該訊號 ≠ 台架能注入它** ——
   後者需實機確認，本包無從驗。
5. **PROXI 未被本批使用。** 已綁、已開檔（13 分頁），
   但 pilot 13 leaf 之 PROXI 命中為 0，故本批無 `PROXI <Param> = <值>` 之步驟。
   DT/DJ/D2 變體軸（下放包 02 §七-2）落在 `Lowering Operation` 組，非本批。

---

## 九、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`）| 已登記，未送出 |

本批 13 條**無一條觸發 DR-1 佔位**，與下放包 03 §四之預期相符
（速度門檻關鍵字於本群命中 0）。本包未新增 DR，
惟 §6.2 之懸吊角度門檻為條件性 DR 候選，待 Pei 就 §6.2 表態後決定。

---

## 十、停點

**已停。** 13 TC 在 `batches/pilot/`，未寫回、未續批、未自評通過。
待 Pei 逐 TC 審（退出準則 R-G15，FO 讀法）。
