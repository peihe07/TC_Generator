# 17 — Comfort HMI / G-1 判定、BASELINE 涵蓋範圍、窮盡性複核

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/09_partN_amendment_and_profile.md`
- 結論：**PASS**。G-1 判 PASS 並解除 pending；三項裁示見下。

---

## 1. G-1 —— 判 **PASS**，`pending G-1` 標註解除

實測：`forms/…_SWQT_Home_20260809.xlsx`（`1895fb2a…`），
sheet `Test Case Specification&Result`，I 欄，母體 `Z == ArifChen` 共 144 列
（assertion PASS），modal 判準 `\b(shall|will|should|would)\b` 詞界比對。

**含 modal 143 / 144（99.3%）**，`shall` ×176。唯一例外（row 135）為
widget 對照表而非行為陳述。Test Item 長度中位 **273 字元** —— 相對於 §4.3
之 tc_title 2–14 words，形態差異明確，profile §3.1 之 [OVERRIDE] 有據。

### 1.1 provenance 但書 —— 降為 note，不阻卻判定

執行層指出量測對象非 home RECON 所測之原檔（`0e72b1ec…`），亦非 Home v2
（`cfc007f3…`），二者皆不在 repo；FORMS.md 所記四道編修為 D5／F／G／K／Z，
**I 欄不在其中**，但該論據出自 FORMS.md 自身之 diff，無 Home v2 可交叉驗證。

**此揭露正確且必要，但不改變判定**，理由為 R-C15 之判準（蘊含，非直接）：

結論為「home 之 Test Item 帶 modal 且為需求陳述之濃縮」。可設想之 provenance
風險是「該副本之 I 欄曾被編修」；然**一次「把 `shall` 引入 144 列中 143 列」
之編修並非可信之情形**。證據為真即蘊含結論，縱使其來源鏈有一段未經交叉
驗證。

處置：`FW036_R1L_Comfort_Profile.md` §3.1 之
`pending G-1` / `G-1 PASS（附 provenance 但書）` 改為
**`G-1 PASS 2026-08-15`**，但書移至該段之腳註，保留其事實記載，
不再具阻卻效力。

**母體選擇器之發現須保留**：`feature.yaml` 之 `done_region.author_value`
為 `Arif`，而該副本實為 `ArifChen`；以 `Arif` 選取得 0 列，而 0 列會產出
「全數不含 modal」之空集合結論。母體列數 assertion 擋下此事 —— 此為
「檢查項須確認其在該階段確實可能失敗」之正例，**登為 A-CF14**
（`features/home/feature.yaml` 之 author_value 與實際不符），並列 home 之
DATA_REQUESTS，不逕改 home。

---

## 2. 乙 —— BASELINE 涵蓋 `spec-index/`：**採納，並升格為條文**

執行層之判斷正確，且它指出的是**我造成的副作用**：R-C11 要求 spec 留在
`spec-index/` 以保單一來源，而 `.gitignore:58` 使該處不入版控 —— 若 BASELINE
只涵蓋 `inputs/`，R-C11 之淨效果就是把 Comfort 唯一之 spec 來源移出雜湊
保護。這不是任何人的本意，而我立 R-C11 時未察。

```
R-C20  BASELINE 之涵蓋範圍以來源為準，不以目錄為準

features/<feature>/BASELINE.sha256 須涵蓋該 feature 賴以生成之全部來源檔，
不論其位於 inputs/、spec-index/ 或其他路徑。

判準為「此檔若變動或消失，該 feature 之產出是否失去依據」，
而非「此檔在不在 inputs/」。

理由：目錄型判準會在來源被搬移時靜默失效（R-C11 將 spec 移出 inputs/ 即為
一例），而 gitignore 之涵蓋範圍與 BASELINE 之涵蓋範圍各自獨立演變，
兩者之交集無人維護。

Comfort 之 BASELINE 為 8 檔：inputs/ 5 檔 ＋ spec-index/ 之 SR24
export .xlsx／.json 與 SR24 PDF。
```

此條適用全 feature；既有 feature 之 BASELINE 是否補齊，屬 Pei 裁定，另案，
**不在本包自行擴及**。

---

## 3. §7.2 第 3、4 項 —— 窮盡性複核：**做，且分層**

15 §3.2 之「逐節出現」與 §3.4 之四類 token 皆為全稱陳述，而全稱陳述可機械
複核。歸屬如下：

- **掃描與候選清單 = 量測，下放執行層**
- **「這算不算一個配置軸」= 判斷，分析層**

### 3.1 §3.4 token 窮盡性（純機械）

對 `section_fulltext.tsv` 全部 129 列掃描並輸出**相異 token 全集**：

- 非 ASCII 字元（`«»`、`°`、`’`、`‘`、`—` 等），逐字元列出並附出現節次
- 引號類：`"`、`'`、`[`、`]`、`<`、`>`
- 數字後綴／比值形態：`\d+h`、`\d+/\d+`、`\d+-\d+`、`\d+°`
- 全大寫連續詞（`MAX A/C`、`REAR DEFROST`、`LO`、`HI` 等）

輸出 `data/source_tokens.tsv`：`token`｜`出現次數`｜`出現節次`。
**不判斷是否應照錄**，僅列全集。

### 3.2 §3.2 配置軸窮盡性（機械候選 ＋ 分析層判定）

對 129 列掃描條件句式並輸出**全句**：
`Some vehicles`、`In some vehicles`、`For vehicles with`、
`if the vehicle is configured`、`when equipped`、`in certain modes`、
`R1 Low`／`R1 High`／`R1H`、`is available`、`if this feature available`、
`depending on vehicle configuration`、`(… only)`。

輸出 `data/config_axis_candidates.tsv`：`outline`｜`匹配句式`｜`全句`。

**紀律**：本掃描為詞彙型工具，其陰性結果只是索引層事實（R-C13）——
**未命中不等於該節無配置條件**。故另附一項：隨機抽 15 節全文人工過目，
回報是否見到未被上列句式捕捉之配置條件。抽樣 seed 固定並記載。

分析層據兩份輸出裁定 profile §3.2／§3.4 是否需增補。

---

## 4. 上繳包 NN 碰撞之處置

`09_partN_amendment.md` 與 `09_partN_amendment_and_profile.md` 並存。

**兩檔皆保留，不刪、不改名** —— 前者是當時之準確紀錄，改寫已交付之上繳包
即重寫歷史。

`INDEX.md` 以 **`09a`（部分交付：14 §5 六項）**／
**`09b`（完整交付：14＋15＋16，內含 09a 之複驗索引）** 標記，並註明
09b 不取代 09a 之事實記載。

**往後**：一次往返一個上繳包。若下放包分批落檔致執行層先行完成部分作業，
**先完成之部分不另行上繳，併入該次往返之單一上繳包**。此次之成因是我把
14 與 16 分兩次落檔，責在分析層。

---

## 5. 執行層作業指示

1. R-C20 原文貼入 `RULINGS.md`。
2. profile §3.1 之標註改為 `G-1 PASS 2026-08-15`，但書移為腳註。
3. 登 A-CF14（home `feature.yaml` 之 `author_value` 與實際不符），
   並於 `features/home/DATA_REQUESTS.md` 開列。**不逕改 home 之任何檔案。**
4. 執行 §3.1 與 §3.2 兩項掃描，產兩份 TSV，上繳包附全集與抽樣結果。
5. `INDEX.md` 依 §4 標記 09a／09b。
6. **Phase 4 仍不開始** —— 唯一未達成條件為 A-CF07 之 Excel 確認（待 Pei）。
7. 上繳 `docs/upstream/10_exhaustiveness.md`。git 不執行。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C20 BASELINE 涵蓋範圍以來源為準 | ✅ §2 | 已簽 2026-08-15 |

R-C20 適用全 feature，安置位置待 canon re-sync。§1 之 G-1 判定、§3 之掃描
指示、§4 之 NN 處置皆為狀態或作業，不產生條文。
