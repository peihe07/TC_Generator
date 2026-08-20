# 57 上繳 — Input Test Data 之孤兒值與 §4.5 欄位歸屬（AE-1）＋ ENTRY 005

| 項 | 結果 |
|---|---|
| §二 立閘 | **IT-1**（值之使用）與 **IT-2**（§4.5 欄位歸屬）入 `audit_consistency`；方向性案例 **56 → 65** |
| §二 G-K | **`TC-166` 之現況命中**、`TC-173` 綠、`NA` 者不轉紅 —— 三向皆先證後跑 |
| §二 首跑 | **IT-1 紅 6 處**（全文見 §2.3）；**IT-2 待判 3 處** |
| §一 處置 | 互動資料 2 條移入步驟並改 `NA`；獨立資料集 2 條補綁定引用；邊界值 2 條補入步驟 |
| §一 重跑 | IT-1 **0 處**；IT-2 留 **1 處待判**（`049`），人工判為**保留** |
| §三 `about` | `163`／`166` 之模糊語隨移入去除 |
| §五 自檢 | **十項**交付前自檢（**新增第 j 項：IT**），全綠 |
| §四 ENTRY 005 | 已產出（AD-1 ＋ AE-1 同一次重出）；四份 pack 重出；四份靜態轉錄重新標記 |

---

## 1. AE-1 —— 這一欄從來沒有人查過有沒有人用它

`TC-166`：

| 欄 | 內容 |
|---|---|
| `input_test_data` | `Screen pressed about five seconds after the popup appears` |
| `test_procedure` 1 | `Press the screen while the Valet Mode welcome popup is displayed` |

**「約五秒」不出現於任何步驟。** 測試員讀到該筆資料，
卻無任何指示告訴他在哪裡用它。

而 `G17`／`G18` 查的是「TC 內之字面值有無 spec 出處」（**方向往上游**），
`T-1`／`U-2` 查的是 ER ↔ procedure 之接合（**TC 內，另一組欄位**）。
**`input_test_data` 這一組從未被納入。**

---

## 2. IT-1 —— 立閘

### 2.1 判準

對 `input_test_data != NA` 之每一條，取其**具體值**，
逐一要求出現於 `test_procedure` 或 `pre_conditions`：

- **含數字之詞** —— `29`、`10th`、`30-second`、`3.1`（取其數字核心比對，
  故資料之 `30-second` 與步驟之 `30 seconds` 相認）
- **數字詞與序數** —— `five`、`tenth` 正規化為阿拉伯數字；
  比對時兩造皆正規化，故資料寫 `4 → 5`、步驟寫 `Four`／`five` 判綠
- **專有名詞** —— 首字大寫者，**但不取全欄之第一個詞**（那是句首大寫）

**綁定引用視同已使用**：步驟或前提若寫 `the three preferences listed in
Input Test Data` 或 `the preference under test`，即已指明該欄之用處，
**不再逐值比對**。`TC-001` 一族（11 條 PLP 資料集）即此形 ——
逐值比對會把 `3.1`／`SiriusXM` 一律判紅，而那些值本就不該出現在步驟裡。

### 2.2 G-K —— 三向皆先證後跑

```
PASS — [it1] **TC-166 之現況**：資料寫「約五秒」而步驟無此值 → 紅
PASS — [it1] **TC-173 之現況**：資料之 `Alex` 出現於步驟 1 → 綠
PASS — [it1] **範圍向**：`input_test_data` 為 NA 者不得因本閘轉紅 → 綠
PASS — [it1] **數字詞 ↔ 阿拉伯數字**：資料 `4 → 5`、步驟 `Four`／`five` → 綠
PASS — [it1] **綁定引用**：步驟指名 Input Test Data 而不逐值列出 → 綠
PASS — [it1] **改法之回歸**：時點移入步驟後 → 綠
PASS — [it2] **TC-166 之現況**：互動之時點寫在 `input_test_data` → 紅
PASS — [it2] **TC-173 之形狀**：值本身為資料（username）→ 綠
PASS — [it2] **範圍向**：邊界值資料集不得列待判 → 綠

65 / 65 directional cases PASS   （56 → 65）
```

### 2.3 首跑之紅色輸出（**修正之前**，語料 189 條）

```
## IT-1 —— `input_test_data` 之具體值未見於步驟或前提：6 處

  NR1L-UserProfiles-004 (5.9)   孤兒值 ['3.5']
      「Preference under test: Memory Profiles (Seats, mirrors, steering wheel」
  NR1L-UserProfiles-100 (4.5.4) 孤兒值 ['3.1','3.2','3.4','360L','Cluster',
                                       'Home','Listener','Nav','Saved','SiriusXM']
      「Preferences under test: Cluster Home screen (3.1), SiriusXM 360L Liste」
  NR1L-UserProfiles-163 (7.4)   孤兒值 ['30-second', 'five']
      「Screen pressed about five seconds after the popup appears, that is bef」
  NR1L-UserProfiles-166 (7.5)   孤兒值 ['five']
      「Screen pressed about five seconds after the popup appears」
  NR1L-UserProfiles-175 (8.7)   孤兒值 ['0']
      「Username length: 0 → 1 characters」
  NR1L-UserProfiles-176 (8.7)   孤兒值 ['12', '13']
      「Username length: 12 → 13 characters (eleven letters plus one space, th」

## IT-2 —— §4.5 欄位歸屬：互動資料在 `input_test_data`：3 處待判

  NR1L-UserProfiles-049 (12.3) 互動動詞「chosen」
  NR1L-UserProfiles-163 (7.4)  互動動詞「pressed」；互動之時點「seconds after」
  NR1L-UserProfiles-166 (7.5)  互動動詞「pressed」；互動之時點「seconds after」
```

**全批 189 條中 `input_test_data != NA` 者 32 條**（處置後 30 條），
逐條判畢：6 條命中，26 條接上。

### 2.4 盲區（R-G11）

1. **以同義語句表達同一值者抓不到** —— 資料寫 `five seconds`、
   步驟寫 `after a short pause`，本閘判綠而孤兒仍在。
2. **只查「有沒有出現」，不查「用得對不對」** ——
   步驟裡的 `30` 若與資料的 `30` 語意無關，本閘一樣判綠。
3. **綁定引用之放寬**：`under test` 一詞即可豁免全欄之逐值比對，
   故一筆內容錯誤之資料集只要被指名，本閘不會叫。
   **這是為了 11 條 PLP 資料集刻意付出的代價**，在此具名。

---

## 3. 逐條處置（**六條，逐條具名所擇**）

### 3.1 互動資料 → 移入 procedure，欄改 `NA`（§4.5 明文允許）

| tc_id | 原 `input_test_data` | 改後之步驟 1 | 欄 |
|---|---|---|---|
| `163` | Screen pressed **about** five seconds after the popup appears, that is before the 30-second timeout | `Press the screen five seconds after the popup, before the 30-second timeout` | `NA` |
| `166` | Screen pressed **about** five seconds after the popup appears | `Press the screen five seconds after the Valet Mode welcome popup appears` | `NA` |

`about` 為 §2 之模糊語，隨移入一併去除（57 包 §1.2）。
兩條之 `remarks` 同步更正 —— `163` 原本**明寫**「互動之時點寫在
`input_test_data`」，那一句現在是錯的。

### 3.2 獨立資料集未被引用 → 補入綁定引用

| tc_id | 補在哪 | 內容 |
|---|---|---|
| `004` | **pre-condition 1** | `A Driver Profile is active with the preference under test available` |
| `100` | **步驟 1** | `Record the three preferences under test for both default Profiles` |

`004` 補在前提而非步驟，是因為其步驟 2 已達 §5.2 之 12 詞上限
（首次改法寫成 13 詞，`lint_tcs` G15 判紅 —— 見 §6-2）。

### 3.3 邊界值未被引用 → 補入步驟

| tc_id | 值 | 改後 |
|---|---|---|
| `175` | `0`（下界） | 步驟 1：`Read the Next button with zero characters in the username field` |
| `176` | `12`／`13`（上界兩側） | 步驟 1：`Type eleven letters and one space, giving twelve characters`；步驟 3：`Type a thirteenth character and read the username field` |

### 3.4 IT-2 之 3 處待判 —— 人工判讀

| tc_id | 判 | 理由 |
|---|---|---|
| `163`／`166` | **移入步驟** | 「何時按下畫面」為 tester 之互動時點，§4.5 逐字歸 Procedure step |
| `049` | **保留** | `PIN: a 4-digit one-time PIN chosen at activation` —— **值本身是資料**（一組 4 位數），`chosen at activation` 只是說它從哪裡來，不是要 tester 執行的動作。IT-2 之動詞比對讀不出這個差別，**故它是待判清單而不是紅燈** |

### 3.5 重跑

```
## IT-1 —— `input_test_data` 之具體值未見於步驟或前提：0 處
## IT-2 —— §4.5 欄位歸屬：互動資料在 `input_test_data`：1 處待判
  NR1L-UserProfiles-049 (12.3) 互動動詞「chosen」
```

---

## 4. ENTRY 005（AD-1 ＋ AE-1 同一次重出）

### 4.1 十項交付前自檢（**新增第 j 項：IT**）

```
a) 189 列：非空 189／相異 180；row199 D=None
b) 列序依 Requirement ID 遞增：True
c) 必填 13 欄 × 189 = 2457 格空值 0；priority ⊆P0–P3 True；design_method 6 種
d) 多行格 753；含 CR 之格 0；<t> 內 &#13; 0
e) emoji 0 格；方括號 {'[username]': 3}
f) 行尾句點（J–M）0／受檢 1804 行
g) zip members 48→48（集合相同 True）
h) 內部字樣掃描，命中 0 格
i) Test Item 兩段：合格 189／189；違規 0
   留空欄非空數：O 0／Q 0／T 0／AA 0／AB 0／AH 0
j) **IT**：input_test_data 非 NA 30／189；IT-1 孤兒值 0 處；
   IT-2 §4.5 欄位歸屬待判 1 處（049，人工判為保留）
```

`verify_dv_integrity` 另跑：**違規 0**（zip 48、x14 節點 1、sqref `R10:R1411`）。

### 4.2 台帳

```
…_20260820_itemdata.xlsx: OK   （ENTRY 005，現行）
size 206499 bytes
sha 570eb7cd8d1049de0e24f897c4acc376ed6dfd2b9089795991ae799aabbac5f5
```

**ENTRY 004 從未產出** —— 56 包曾指定，57 包 §四指示與 AE-1 合併為同一次重出，
故台帳號次跳空。台帳 append-only，不回頭改號，
於檔內以一個「未產出」區塊說明之。

### 4.3 全閘

```
lint_tcs 64/64（語料 189，違規 0）    audit_consistency **65/65**
audit_delivery_fields 16/16（違規 0） audit_pending 5/5（違規 0）
audit_enums 7/7      audit_verbs 5/5        audit_variant_pairs 7/7
audit_assignment 6/6                        audit_delegation 8/8（紅 0）
lint_variant_labels 11/11                   lint_outbound_doc 8/8
verify_dv_integrity 6/6                     build_review_pack 4/4
stamp_static_doc 5/5                        write_back 12/12
verify_locator 8/8   verify_recon_gates 6/6 audit_second_segment **13/13**
```

**四份 pack 重出**：`57_24a` 11／0、`57_24b` 11／0、`57_33a` 17／0、`57_33b` 16／0。
**四份靜態轉錄**：`27`／`28`／`34`／`48` 四檔之語料指紋因第二段改寫而全數過期，
**逐檔複核其轉錄內容未受影響後**（四檔皆不轉錄 `test_item`）**重新標記為 57 輪**，
現皆「不符 0 條」。

---

## 5. 附帶發現（**未擅自修改**）

1. **`build_review_pack.py` 之產出日期是寫死的** —— `emit()` 逐字印
   `產出層：執行層｜2026-08-18`。本輪四份新 pack 因此都標著 8/18，
   而實際產於 8/20。**它不影響任何判定**（pack 之新鮮度由語料指紋管，不由日期管），
   故本輪不動它；但那一行現在是假的，**建議改為由參數帶入或取檔案 mtime**。

2. **`audit_pending` 之 PJ-2 在本輪叫了兩次，兩次都是對的。**
   `TC-004` 之 AB-1 判定登記於 42 輪，本輪動了它的 pre-condition，
   digest 立刻不符 → 回列待判。**重判之結論不變**（兩端仍為同一組三個位置，
   中間事件仍為 key cycle），digest 由程式重取後登記，並在 `reason` 欄
   逐字記下本輪改了什麼。**第二次是我把改法從步驟挪到前提時又觸發一次** ——
   這正是它該有的行為。

---

## 6. 獨立判斷

1. **57 包 §七那句話應該再往前推一層。**
   > 欄位之間的接合，要一組一組地查 —— 查過兩組不代表查過全部。

   本輪查完第三組（`input_test_data` → 步驟／前提）。
   **交付欄位有 13 欄，兩兩之間的接合關係遠不止三組**，
   而目前是「出事一組、補一組」。真正的缺口不是第四組沒查，
   是**沒有人列過「哪些欄位對之間應該有接合」的清單** ——
   有了清單才知道查了幾分之幾。這件事我沒有做，因為它需要 canon 之欄位語義權威，
   **在此具名為建議**。

2. **這一輪的兩個 defect 是同一個形狀。**
   `TI-2` 驗了「第二段非僅重複第一段」而只比字面；
   `G17`／`G18` 驗了「值有沒有出處」而不問值有沒有被用。
   **兩者都是「閘檢查了那個欄位存在且合法，而沒有檢查它有沒有在做事」。**
   欄位級的閘查得到形態，查不到**用途**；用途只在欄位之間看得出來。

3. **`049` 之保留比 `163`／`166` 之移動更值得記。**
   IT-2 三處命中，兩處是真的、一處不是，而**分辨它們靠的不是更好的正規表達式，
   是讀那條 TC**。若當初把 IT-2 設成紅燈，`049` 的 `input_test_data`
   現在已經被清成 `NA`，而那組 PIN 是真的資料 —— **會壞掉一條好的 TC**。
   「列待判不轉紅」在這一輪救回了一條。

4. **關於 ENTRY 004 的跳空**：我選擇留下一個「未產出」區塊而不是把本次記成 004。
   理由是 56 包確實指定過 ENTRY 004，而**台帳要能解釋自己的號次**；
   若逕自記為 004，日後讀 56 上繳與 57 上繳的人會看到兩份文件指同一個號。
