# 上繳包 07 — B1-GATE-1 停手回報（profile 未核可）

執行層 → 分析層。2026-08-13。本份合併回報下放包 **05 / 06 / 07** 之執行，
並說明 **08 未執行**之理由。

> ## ⛔ 停手條件 2 觸發 —— B1-GATE-1 有兩筆對映與 framework Part VI 不符
>
> 07 包 §7.2：「B1-GATE-1 任一筆對映與 framework Part VI 不符 →
> **停止全部後續**，續行回報。」
>
> **-003 … -010 八筆完全相符。-001 與 -002 兩筆不成立**，且性質不同：
> 一筆指向**文件中不存在的 id**，一筆指向**內容不對的條款**。
> 這正是這兩筆先前被標為「未逐條驗證」的那兩筆。

---

## 1. B1-GATE-1 —— 全 10 筆獨立重驗

### 1.1 方法（未引用 framework Part VI 之表）

- **037 側**：`inputs/SWE1_CFTS_022-Privacy_Features.xlsx` →
  `Analysis Report` 表頭第 7 列，取 `SWE-Requirement ID`（欄 0）、
  `Source Requirement ID`（欄 1）、`Requirement Title`（欄 2）、
  `Requirement Description`（欄 3）。10 筆資料列
- **CFTS022 側**：`inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional
  Specification_20250910_1708.docx`，以 `python-docx` 讀段落，
  NFKC 正規化後以 `^\s*(\d{7})\s*:\s*\[` 切出 artifact 區塊
  —— **共 336 個**，與 ECU tag 行數 336 相符
- 判定不採「id 是否存在」單一條件（那只是必要條件），而是
  **取該 artifact 之條文全文，與 leaf 之 Title/Description 逐筆語意對照**

**一項方法上的自我更正**：第一次跑用了 `\*\*(\d{7})\s*:` 的表頭樣式
（沿用下放包 00 §3.2 對 CFTS022 的描述），結果切出 **0 個區塊**，
十筆全報 CHECK。那是**擷取失敗，不是對映失敗**。實際格式為
`4915171: [Artifact Type:…]`，無 `**`。修正後才得到下列結果。
若當時把 0/10 當成對映結論回報，會是一次嚴重誤報。

### 1.2 結果

| leaf | Source | PROF | 計算 id（−1） | artifact 存在 | 條文對應 |
|---|---|---|---|---|---|
| -001 | PROF-023 | 23 | 4915022 | ❌ **不存在** | ❌ |
| -002 | PROF-160 | 160 | 4915159 | ✅ | ❌ **內容不符** |
| -003 | PROF-169 | 169 | 4915168 | ✅ | ✅ |
| -004 | PROF-170 | 170 | 4915169 | ✅ | ✅ |
| -005 | PROF-171 | 171 | 4915170 | ✅ | ✅ |
| -006 | PROF-172 | 172 | 4915171 | ✅ | ✅ |
| -007 | PROF-173 | 173 | 4915172 | ✅ | ✅ |
| -008 | PROF-174 | 174 | 4915173 | ✅ | ✅ |
| -009 | PROF-175 | 175 | 4915174 | ✅ | ✅ |
| -010 | PROF-176 | 176 | 4915175 | ✅ | ✅ |

**8/10 相符，2/10 不成立。**

### 1.3 -002 —— 指向了錯的條款（差一號）

| | 內容 |
|---|---|
| 037 -002 Title | Personalization Display – Restore on Interior CAN Wake-Up |
| 037 -002 Desc | Upon wake-up of the Interior CAN network, the HU shall restore the last known state of the configured personalization features. |
| framework 主張 **4915159** | *The set of features shall be ready to be displayed within the time to complete the splash screen. Note: See {VF169} for the splash screen behavior.* |
| **實際對應 4915158** | *Each time the Interior CAN wakes up, the HU shall recall the last known state for the configured set of personalization features to be displayed.* |

4915159 講的是**開機畫面計時**，與 leaf 無關。正解是 **4915158**，
即該筆之 offset 為 **−2**，不是 −1。

### 1.4 -001 —— 目標 id 根本不存在

| | 內容 |
|---|---|
| 037 -001 Title | Input Monitoring – Resume After Sleep Mode Exit |
| 037 -001 Desc | Upon exit of the A&T System from SLEEP MODE, the HU shall resume monitoring of button press status. |
| framework 主張 **4915022** | **文件內無此 artifact** |
| 語意候選 **4914955** | *When the A&T System exits 'SLEEP MODE', the HU and external DVD player shall monitor the button pressed status.* |
| 語意候選 4914954 | *When the A&T System exits 'SLEEP MODE', the **SCCM** shall monitor…*（SCCM 版，非 HU）|

4914955 是 HU 版，與 leaf 之 "the HU shall resume monitoring" 相符；
4914954 是 SCCM 版。**執行層不裁定何者為正**（R22-5）——
但可確定的是：**不是 4915022，因為那個 id 不在文件裡。**

### 1.5 根因：−1 不是規則，是 SCV 區塊的局部巧合

CFTS022 的 artifact id **不連續**：4914928–4915339 這段區間內
**缺 79 個號**。id 有缺號時，`4915000 + PROF − 1` 這種算術推定
在任何缺號跨越處都會失準 —— -003…-010 全中，是因為那八筆落在
SCV 這個沒有缺號的連續區塊內。

**這正是 canon「以算術推定 id 者，必須以已知全集驗證」的實例。**
framework Part VI 原文寫「實測連續 8 筆全中，**offset 恆為 −1**」——
「恆為」是從 8 筆連續樣本外推的，而那 8 筆全在同一個無缺號區塊裡。

### 1.6 建議處置（不自裁）

1. framework Part VI 之 Layer 2/3 表，`-001` 之 `4915022` 與 `-002` 之
   `4915159` 兩格須修訂；「offset 恆為 −1」之措辭須改為
   「SCV 區塊（-003…-010）之局部規律」
2. profile §1 之對映條款同步修訂
3. **-001 之正解需 Tier 2 裁定**（4914955 vs 4914954，HU 版 vs SCCM 版）
4. 其餘八筆經獨立重驗成立，可照用

---

## 2. 因停手而未執行者

| 項目 | 狀態 |
|---|---|
| 07 §6.2 profile 三項修訂 | ❌ 未執行 |
| 07 §6.3 移除 DRAFT、標 Approved | ❌ **未執行 —— profile 維持 DRAFT** |
| 07 §6.7 換檔後三處連動 | ❌ 未執行 |
| **下放包 08 全部（R29）** | ❌ **未執行** |

**為何連 08 也停**：08 §2.5 要改的正是 profile §5 / §6，而 profile 現在
處於「§1 對映條款已知有誤、核可被擱置」的狀態。在一份待修訂的文件上
執行局部解除，會產生一份既未核可、又被改過兩處的中間態。
08 之其餘各項（R29-1 Excel 確認、BASELINE 換行、A-PV14 → RESOLVED）
本身證據充分且與對映無關，**一聲令下即可補做**。

**特別提醒**：A-PV14 目前仍標 PENDING，但換檔實測已完成
（`e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2`，
177,388 bytes，與 R29-2 預期值相符）。狀態落後於事實，是停手的副作用，
不是新的未決。

---

## 3. 已執行者（05 / 06 / 07 之可行部分）

### 3.1 下放包 05（R26）

| # | 作業 | 狀態 |
|---|---|---|
| 1 | R26 貼入 | ✅ |
| 2–3 | 兩份摘要建立 | ✅（同日依 Pei 聊天指示先行完成）|
| 4 | 確認未被排除 | ✅ 見下 |
| 5 | `output/` 目錄 | ✅ 已存在（R23 產物寫入時建立），未放 `.gitkeep` |
| 6 | `feature.yaml` 寫回路徑 | ⛔ **停手條件 3 觸發** |
| 7 | PLAYBOOK P7 加註 | ✅ |

**第 4 項之確認方式**：

```
$ git check-ignore -v features/privacy/BASELINE.sha256 features/privacy/DELIVERY.sha256
  （無輸出 → 未被任何層級排除）
$ git check-ignore -v features/privacy/output/x.xlsx
  features/privacy/.gitignore:17:output/    features/privacy/output/x.xlsx
$ git ls-files features/privacy | grep sha256
  features/privacy/BASELINE.sha256
  features/privacy/DELIVERY.sha256
```

**第 6 項停手 —— `feature.yaml` 實際欄位結構**：`write_back:` 區段現有
`author_value`、`tc_ref_id_value`、`tc_id_format`、`fill_test_group_set`、
`scope_label`、`scope_source` 六個欄位，**沒有任何輸出路徑欄位**。
其餘 feature 之輸出路徑皆由 `--out` 參數或腳本內預設決定，非由
`feature.yaml` 指定。未自行新增欄位。Privacy 之寫回腳本尚未建立（R20-5），
該欄位要不要有、叫什麼名字，宜於建腳本時一併裁定。

### 3.2 下放包 06（R27）

| # | 作業 | 狀態 |
|---|---|---|
| 1 | R27 貼入 | ✅ |
| 2 | DELIVERY 檔頭補記錄單位判準與旗標代價 | ✅ |
| 3 | 依序執行 04、03 | ✅ 已於前一輪完成 |
| 4 | PLAYBOOK 補「台帳綠燈 ≠ 產出俱在」 | ✅ |

**R27-2 之理由更正已接受**：原理由（怕清理後 shasum 失敗）確實與自身的
`--ignore-missing` 決定自相矛盾 —— 被清掉的條目本來就會靜默略過。
**結論對、理由錯**，已改為記錄單位判準。這是 R27-2 §5a
（保守處置之理由與結論須分別檢驗）的一次現場實例。

### 3.3 下放包 07 之可行部分

- **§6.1 R28 貼入** ✅
- **§6.4 framework 首句補 Part V** ✅ —— 依 R28-3「純事實性補正得逕行」。
  現為：`Media (Part I) / Home (Part II) / AMFM (Part III) / SXM (Part IV) /
  Projection (Part V) / Privacy (Part VI)`
- **§6.5 rev C 之 T–Z 標頭實測** ✅ —— 見 §4

---

## 4. §6.5 —— rev C 車型欄實測（P-5 之前置）

`Test Case Specification 測試用例規範` 分頁，第 8–9 列：

| cell | 值 |
|---|---|
| **T8:Z8**（合併）| `Vehicle Model 車型` |
| S9 | `Functional Safety\n功能安全` |
| **T9** | `HDCC27\nAtl-Hi` |
| **U9** | `DT27\nAtl-Hi` |
| **V9** | `VF(ProMaster)637\nAtl-Mi` |
| **W9** | `Commander (598)\nAtl-Mi` |
| **X9** | `Regengade (5210)\nAtl-Mi` |
| **Y9** | `Toro(2261)\nAtl-Mi` |
| **Z9** | `Fastack (376)\nAtl-Mi` |

**停手條件 4 未觸發** —— T–Z 確為車型欄（T8:Z8 合併儲存格標題即
`Vehicle Model 車型`），語意相符。

**兩點供 P-5 裁定參考（僅陳述，不建議）**：

1. **本專案平台為 HDCC28，而 T9/U9 是 HDCC27 / DT27。** 範本列的七個車型
   欄位裡**沒有 HDCC28**。這與 A-PV14 同源 —— 該案是 VF 檔混入 DT 平台，
   此處是欄位本身停在 27 世代。
2. `Regengade` 疑為 `Renegade` 之拼寫錯誤（範本原文如此，未更動）。

---

## 5. 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。**

1. **-001 的正解我沒有定，也不應該定。** 4914954（SCCM）與 4914955（HU）
   都以 `When the A&T System exits 'SLEEP MODE'` 起首，差別在主體。
   leaf 寫的是「the HU shall resume monitoring」，字面指向 4914955 ——
   但**這是我讀出來的，不是量出來的**，且 037 的 Source 欄寫的是
   PROF-023，與這兩個 id 都對不上任何規律。需 Tier 2。

2. **其餘八筆「相符」的判定門檻是關鍵詞覆蓋率 ≥ 0.4，不是逐字比對。**
   八筆的條文與 leaf 標題語意明確一致（例如 -008 對 4915173
   「When the AMP wakes up on the Interior CAN, the AMP shall recall…」），
   但**判定規則本身是我訂的**。若分析層要更嚴的門檻，須重跑。

3. **336 個 artifact 我只查了 10 個。** 「4915022 不存在」是對這 336 個
   區塊的補集判定 —— 若 CFTS022 尚有未被我的表頭 regex 切到的 artifact，
   該結論會鬆動。佐證是 ECU tag 行數（336）與區塊數（336）相等，
   但那兩個數用的是同一個 regex，**不是獨立驗證**。

4. **profile 目前是「已起草、未核可、且已知 §1 有誤」的三重狀態。**
   我沒有動它任何一個字（連修訂 1 那個與對映無關的 design method 條款
   也沒改），因為部分修訂會讓它更難判斷處於哪一版。
   **這是刻意的保守處置，但代價是修訂 1 也一併延後了。**

<!-- UPSTREAM-COVERS: 05 06 07 -->
