# 00 上繳 — Vehicle Setting 進場與偵察（Phase 0/1）

執行層寫入。往返 NN = 00。**本輪未生成任何 TC，未寫回任何工作簿，未執行任何 git 寫入性操作。**

---

## 0. 先講三件會改變後續作業的事

1. **R-VS3 內部不一致，且不可能同時滿足**（A-VS19）。其指定之指令
   `new_feature.py "Vehicle Setting"` 產生 `features/vehicle setting`（**含空白**），
   而其同時指定目錄為 `features/vehicle_setting`。已依**目錄名**為準處置，
   空白目錄**未刪**，指令備於 §10。
2. **錨鏈在 1 個 leaf 上不成立**（升級條件 2）。`SWE1-VC-HeatedSteeringWheel-009` 之
   `Source Requirement ID` 逐字為 `SYS-RA-CFTS100` —— 指向 CFTS100 且無 `-N` 序號。
   下放包記其原因為「SYS2 該列 `Source Requirement items` 為空」，**該原因不符實測**。
3. **A 組未全數完成**。W-8／W-9／W-13 未執行，理由見 §9。**不是漏做，是本輪做不完**；
   逐項具名於 §9，未以任何方式暗示其已完成。

---

## 1. 預期 vs 實測 —— 逐項對照（相符者亦列出）

### 1.1 下放包 §5.2 之 24 項

| 項目 | 預期 | 實測 | 判定 |
|---|---|---|---|
| 037 leaf 總數 | 271 | **271** | 符 |
| ── Common Features | 56 | **56** | 符 |
| ── HeatedSeat | 99 | **99** | 符 |
| ── VentedSeat | 81 | **81** | 符 |
| ── Heated Steering Wheel | 35 | **35** | 符 |
| 完整 SWE ID 跨四檔重複數 | 0（271 uniq） | **0（271 uniq）** | 符 |
| 尾碼 `-001` 出現次數 | 4；最大尾碼 99 | **4；最大 099** | 符 |
| 037 之 SYS-RA 引用（distinct） | 273，全部指向 CFTS044 | **273，全指 CFTS044** | 符（**但見 §2.2**） |
| 被兩個以上 leaf 共用之 SYS-RA | 0 | **0** | 符 |
| SYS-RA 編號域 | 19–336，缺 45 號 | **19–336，缺 45** | 符 |
| 036 資料列 | 237 | **237** | 符 |
| 036 qualifying done row | 0 | **0**（F 欄非空 = 0） | 符 |
| 036 填充 B/D/H/I/N | 各 237 | **各 237** | 符 |
| 036 填充 L/M | 各 191 | **各 191** | 符 |
| 036 填充 C/E/F/G/J/K/O/P/Q/R/S/T–Z/AA/AH | 各 0 | **各 0** | 符（清單少列 `A`、`AB`–`AG`，實測亦 0） |
| I==desc／H==title／N==src | 237/237/237 | **237/237/237** | 符 |
| L 相異值／M 相異值 | 17／44 | **17／44** | 符 |
| L 為 `Requirement is not clear…` | 12（10/1/1） | **12（10/1/1）** | 符 |
| 036 D 欄全落在 leaf 全集內 | 是（237/237，0 未匹配 0 重複） | **是** | 符 |
| 未被 036 覆蓋之 leaf | 34（10/11/9/4） | **34（10/11/9/4）** | 符 |
| SYS2 `Basic Report` 資料列 | 538 | **538** | 符 |
| SYS2 `Sys-RA-Feature-ID` 非空 | 0 | **0** | 符 |
| SYS2 全表 `SYS-RA-CFTS…` 命中 | 0 | **0** | 符 |
| 037 desc ↔ SYS2 desc 全等對照組 | 31；offset −1/+1 各 0 | **31；−1 = 0、+1 = 0** | 符 |
| 271 leaf 之 SYS-RA 全落在 SYS2 列範圍內 | 是 | **是**（可解析之 273 引用全部） | 符 |
| SYS-RA 指向列之 Category（逐引用 273） | FR 239／Heading 25／Information 9 | **239／25／9** | 符 |
| 7 位數 ID 出現於 CFTS044 者 | 270 / 271 | **270 / 271** | 符 |
| 例外 | `SWE1-VC-HeatedSteeringWheel-009`（**SYS2 該列 src items 為空**） | 該 leaf 為唯一例外，**惟原因不符** | **不符（原因）** |
| CFTS044 文字中 7 位數 ID（distinct） | 2302 | **未量**（§9） | 未做 |
| 037 desc 含 `$var$` 之 leaf | 196／271；相異 token 30 | **196／271；30** | 符 |
| 出現最多之 token | VentedSeatFR 89／VentedSeatFL 80／HSW_Stat 48 | **89／80／48** | 符 |

### 1.2 CFTS044 原始 docx（00C）

| 項目 | 預期 | 實測 | 判定 |
|---|---|---|---|
| PK zip、zip member | PK、28 | **PK、28** | 符 |
| body heading | 270 | **270** | 符 |
| 需求段落（`[Artifact Type` 錨定） | 2030 | **2030** | 符 |
| leaf → 章節 | 245／25 有 id 無章節／1 無 id | **245／25／1** | 符 |
| 245 leaf 落在相異章節數 | 20 | **21**（展開多章節者後）；**20**（僅計單章節 leaf） | **不符，見 §2.3** |
| 檔名式正則命中全簿 | 1（`RAR_LTM-R1L_SR21_1A_r8.xlsx`） | **1**（另命中一個 MIME 型別字串，非檔名） | 符 |
| TLM HMI Document | 24 | **24** | 符 |
| PDO graphics | 2 | **2** | 符 |
| DBC | 13 | **13**（body 段落文字、**不分大小寫**）／18（全 xml part、區分大小寫） | 符（條件已揭露，見 §4） |
| body heading 之相異 `{7位數}` | 254（A-VS06 差額 16） | **270，差額 0** | **不符，見 §2.4** |

### 1.3 DBC（00C／00H）

| 項目 | 預期 | 實測 | 判定 |
|---|---|---|---|
| R4_BHCAN signals／messages | 883／155 | **883／155** | 符 |
| R4_BHCAN VersionYear／Week／BusType | 25／50／無 | **25／50／無** | 符 |
| R5_FDCAN8 signals／messages | 1755／323 | **1755／323** | 符 |
| R5_FDCAN8 VersionYear／Week／BusType | 25／50／`"CAN FD"` | **25／50／`"CAN FD"`** | 符 |
| 僅 BHCAN／僅 FDCAN8／共有 message | 119／287／36 | **119／287／36** | 符 |
| `HSW_StatFailSts` 僅於 R4_BHCAN | 是（STATUS_CSWM, id 1169） | **是（STATUS_CSWM, 1169）** | 符 |
| `TGW_DISP_STATSts` 所在 | TELEMATIC_DISPLAY2(1500)／TELEMATIC_FD_4(1427) | **相同** | 符 |
| SHA256 | — | BHCAN `9ef1ec98…`；FDCAN8 `51c8fd60…` | 新登記 |

### 1.4 LID 表（00G）

| 項目 | 預期 | 實測 | 判定 |
|---|---|---|---|
| 相異 LID（CAN Mapping + Proxi） | 2,974 | **2,974** | 符 |
| ── CAN Mapping 列數 | 2,629 | **2,626** | **不符（3 列）** |
| ── Proxi & Configuration 列數 | 449 | **446** | **不符（3 列）** |
| 30 token：逐字／近似／無對應 | 27／2／1 | **27／3／0** | **不符（分類法），見 §2.5** |
| `Format = See Proxi Table` 之 LID | 6（本 feature 用得到 4） | **8**（本 feature 仍為 4） | **不符，見 A-VS16** |
| `VC_VEH_LINE` Format 全長／結尾 | 491 字元／`101 = WL (65 Hex) # = Not Used` | **未逐字複驗長度**；`# = Not Used` 結尾形態已由 `TRUNCATED_ENUM` 旗標捕獲（全簿 15 個 LID） | 部分 |
| Atlantis High 空而 Atlantis 有值 | 10（上界） | **10 個相異 LID（12 列）** | 符，**但其性質不同，見 §2.6** |

---

## 2. 不符項目逐項說明（**不調和**）

### 2.1 `SWE1-VC-HeatedSteeringWheel-009` —— 原因不符（A-VS12，升級條件 2）

其 `Source Requirement ID` 逐字為 **`SYS-RA-CFTS100`**：

- 指向 **CFTS100**，非 CFTS044
- **無 `-N` 序號** —— 無法對應到 SYS2 之任何資料列

下放包記其原因為「SYS2 該列 `Source Requirement items` 為空」。
**實測：SYS2 全 538 列之該欄無一為空**，且此 leaf 根本解析不到列，
故不存在「該列」。**兩者所指非同一件事。**

→ **錨鏈於此 leaf 不成立**，已依升級條件 2 停下回報。開 DR-9。

### 2.2 「273 全部指向 CFTS044」為真，但其為真之原因是正則看不見反例（A-VS13）

| 正則 | 逐引用 | distinct |
|---|---|---|
| `SYS-RA-CFTS\d+-\d+`（下放包 §5.1 指定） | 273 | 273 |
| `SYS-RA-CFTS\d+(?:-\d+)?` | **274** | **274** |

多出者即 `SYS-RA-CFTS100`。依文件號分布：CFTS044 **273**、CFTS100 **1**。
**canon §5a 第 12 條之標準形態：抽取式少抽不會報錯。**

### 2.3 相異章節 21 vs 20 —— 兩個數字量的是兩件事（A-VS14）

- **僅計對映到單一章節之 leaf**：相異章節 **20**（與預期相符）
- **含對映到多章節者展開後**：相異章節 **21**

5 個 leaf 對映到 >1 章節：

| leaf | 章節 |
|---|---|
| `SWE1-VC-LeftFrontHeatedSeat-004` | `1.3.2.1.3.1;1.3.2.1.3.2;1.3.2.1.3.3;1.3.2.1.3.4` |
| `SWE1-VC-LeftFrontHeatedSeat-011` | 同上 |
| `SWE1-VC-HeatedSteeringWheelManagement-025` | `1.3.2.1.3;1.3.3.3.6.1` |
| `SWE1-VC-HeatedSteeringWheelManagement-026` | 同上 |
| `SWE1-VC-HeatedSteeringWheelManagement-027` | 同上 |

後三者各有 **2 個 SYS-RA 引用**（271 leaf 中僅此 3 個有 2 個）；
前二者為單一 SYS-RA 但其 SYS2 列之 `Source Requirement items` 含多個 7 位數 ID。

**`specification_reference` 之單值形式對此 5 leaf 不成立** → 開 DR-10（裁決類）。

### 2.4 A-VS06 之差額 16 於原始 docx 上不重現

以 `word/styles.xml` 之 heading 1–7 樣式取 body heading：

| 量 | 值 |
|---|---|
| body heading | 270 |
| 其 `{7位數}` 逐處 | 270 |
| 其 `{7位數}` 相異 | **270** |
| 差額 | **0** |

分析層之 254 係在**轉檔文字**上以較寬形態（`章節號 + 標題 + {7位數}`，不限 heading 樣式）量得。
本輪以同形態於 body 段落文字重量：**逐處 444、相異 259** —— 仍非 254。

→ **A-VS06 改寫為 A-VS06′**：原差額不重現；254 為轉檔文字之產物，非規格之性質。

### 2.5 30 token 之「近似／無對應」分類法不同

| | 預期 | 實測 |
|---|---|---|
| 逐字命中 | 27 | **27** |
| 近似 | 2 | **3** |
| 無對應 | 1（`Heated_Steats_Levels`） | **0** |

**底層事實一致**：`Heated_Steats_Levels` **無逐字對應之 LID**（A-VS05 成立）。
差別在我的「近似」判準為 8 字元前綴匹配，把它歸入近似而非無對應。
**掃描條件：對 3,000 個相異 LID 作不分大小寫之全字串比對。**

### 2.6 「Atlantis High 空欄」之性質與 00G 所述不同（A-VS15）—— **直接影響 R-VS11**

12 列（**10 個相異 LID**，與 00G 之 10 相符）標為 `ATL_HIGH_EMPTY`，
**全部位於 `Proxi & Configuration` 分頁**。

該分頁**列 2 之欄組標題**逐字為：

```
LID Information | Powernet | CUSW | Atlantis & Atlantis High | Compact | Comments
```

而 `CAN Mapping` 分頁為：

```
LID Information | Powernet | CUSW | Atlantis | Compact | Atlantis High | Comments
```

→ **`Proxi & Configuration` 根本沒有獨立的 `Atlantis High` 欄組**；
其第 16 欄一欄兼管 Atlantis 與 Atlantis High，**且該表在列 2 自己寫明了**。

00G §4 讀的是**列 3 之逐欄表頭**（`Signal Name`／`CAN`／`Format`…），未讀列 2 之欄組標題，
因而把「該分頁無此欄組」誤讀為「該欄為空」。

**R-VS11 之兩難消解**：00G 稱「(a) 同 Atlantis 與 (b) 不適用兩種讀法在本表上長得一模一樣」
—— **實測並非如此，該表以欄組標題區分了二者**。
本輪**不代為裁定**（R-VS11 屬 Pei），僅提供此事實。

### 2.7 LID 列數 2,626／446 vs 2,629／449

相異 LID 總數 **2,974 完全相符**，僅列數各差 3。
本輪之列判準為「資料自列 4、A 欄 `Logical Identifier` 非空」。
差額 6 列未追因，**不調和**。

---

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | feature.yaml 之分頁名與欄位對映（scaffold 模板為 `Test Case Specification&Result`、design_method=`Q`、functional_safety=`R`、author=`Z`；**實測分別為 `Test Case Specification 測試用例規範`、`R`、`S`、`AA`**）；骨架落於 R-VS3 所指之底線目錄 |
| **核實無誤** | §1 之全部「符」項（共 41 項）—— 依 §4 之掃描條件於 `inputs/` 實體檔重測 |
| **正確地不動** | 未複製 `Comfort HMI L&F` 入 `inputs/`（禁區：素材補入僅 R-VS12 兩檔獲授權，DR-5-A 待 Pei）；未刪 `features/vehicle setting/`（禁區之外之破壞性動作，指令備於 §10）；未裁定 R-VS7／9／10／11（不代擬條文）；未調和 §2 之七項不符 |

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| 037 ×4 | 分頁 `Analysis Report`；**表頭列 7**；資料自**列 8**；A 欄非空 = leaf。**表頭比對前先 `\s+`→單一空格**（實測表頭為 `Requirement  Title` 雙空格，未正規化即找不到欄） |
| 036 | 分頁 `Test Case Specification 測試用例規範`；表頭列 9；資料列 **10–246**（實體列號）；**逐列**；空 = `None` 或 strip 後空字串 |
| 037↔036 比對 | `\s+`→單一空格後**全字串相等**，**區分大小寫** |
| SYS2 | 分頁 `Basic Report`；表頭列 1；資料自列 2；**「第 N 筆資料列」以資料序號計**（工作表列號 = N+1）；欄位 id=0、Feature-ID=1、Description=2、Source Requirement items=4、Category=9 |
| offset 驗證 | 037 desc 與 SYS2 desc **`\s+`→單一空格 + 轉小寫**後全字串相等 |
| SYS-RA | 嚴格式 `SYS-RA-CFTS\d+-\d+`（不分大小寫）＝下放包指定；另跑寬鬆式 `SYS-RA-CFTS\d+(?:-\d+)?` 作對照 |
| 7 位數 | `\b\d{7}\b`（**有詞界**） |
| `$var$` | `\$[A-Za-z0-9_]+\$`，**區分大小寫** |
| CFTS044 docx | `zipfile` 直讀；heading 樣式自 `word/styles.xml` 解 `w:name` 為 `heading 1`–`7`；章節式 `^\s*(\d+(?:\.\d+)*)\s+(.*?)\s*\{(\d{7})\}\s*$`；需求段落以字面 `[Artifact Type` 錨定；**「body 段落文字」＝ `word/document.xml` 之 `w:body` 內 `w:p` 之 `w:t` 串接**，與「全部 xml part 原始位元組」為兩個不同母體 |
| DBC | `BO_ (\d+) (\w+)\s*:` 取 message；`^\s*SG_\s+(\w+)` 取 signal；屬性以 `BA_ "(VersionYear\|VersionWeek\|BusType)"[^;]*;` 逐字取 |
| LID 表 | `CAN Mapping` 與 `Proxi & Configuration`，表頭列 3、資料自列 4、A 欄非空；**欄組自列 2 取**；另納十張 `* Specific Signals` 分頁（33 列）；LID 比對**不分大小寫、全字串** |

---

## 5. W-5 反向驗證實測（含對照向，R-G7-1）

母體：desc 非空之 leaf **271 / 271**；SYS2 desc 非空 **538 / 538**。

| 向 | 作法 | 命中 |
|---|---|---|
| **正向** | `SYS-RA-CFTS044-N` → 第 N 筆資料列 | **31** |
| 位移 −1 | 第 N−1 筆 | **0** |
| 位移 +1 | 第 N+1 筆 | **0** |
| **對照向（「什麼都沒做」）** | 以決定性打亂之列號 `(N*7+13) mod 538 + 1`，**與 offset 規則無關** | **0** |

**對照向之意義**：若比對式本身寬鬆到會亂命中，打亂列號後仍會有命中。
實測 0 → **31 個命中確實來自對應關係，不是比對式的產物**。

⚠ **本向之強度界線**：31 組對照組偏向「描述未被 SWE.1 改寫者」，其代表性未證
（沿用下放包 §5.3 第 3 項之聲明）。結論之強度來自「另三個位移皆為 0」，不來自樣本量。

---

## 6. W-8 之三來源不一致清單 —— **本輪未執行**

**空清單之原因不是「比對過而無不一致」，是根本沒比對。** 見 §9。

已具備之前置（供下輪直接接續）：
- 30 個 token 與其出現次數（`data/leaves.tsv` 可重算）
- LID 表側之 Format 欄（`data/lid_map.tsv`，含 `atlantis_high_format` 與 `atlantis_format`）
- DBC 側之 message／id（`inputs/*.dbc`）

**尚缺**：CFTS044 內嵌值域之抽取（兩式：`$var$ = [值]`、`路徑.名稱 == "值"`）。

---

## 7. 新開 anomaly 與 DR（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS12** | **DR-9** | `SWE1-VC-HeatedSteeringWheel-009` 之 src ref 為 `SYS-RA-CFTS100`，錨鏈斷 |
| **A-VS13** | —（無需索檔） | 嚴格正則使 `SYS-RA-CFTS100` 隱形；274 vs 273 |
| **A-VS14** | **DR-10** | 5 個 leaf 對映到 >1 章節，`specification_reference` 單值形式不成立 |
| **A-VS15** | —（裁決素材，供 R-VS11） | `Proxi & Configuration` 無獨立 Atlantis High 欄組，其列 2 欄組標題為 `Atlantis & Atlantis High` |
| **A-VS16** | —（併入 DR-7） | `See Proxi Table` 之 LID 實測 8 非 6 |
| **A-VS17** | —（供 R-VS9） | 141 個共有 signal 中 128 個起始位元不同 |
| **A-VS18** | —（內部工具） | `recon.py` leaf 數 46 vs W-2 之 56 |
| **A-VS19** | —（內部工具） | `new_feature.py` 目錄名與 R-VS3 不一致 |
| **A-VS06′** | —（改寫） | 原差額 16 於原始 docx 不重現，實測差額 0 |

---

## 8. 未預期之發現

1. **`Proxi & Configuration` 與 `CAN Mapping` 之欄組結構不同**（A-VS15）——
   下放包與 00G 皆假設兩表同構。**這一項直接改變 R-VS11 之問題形態。**
2. **128 / 141 個共有 signal 之起始位元不同**（A-VS17）。00H §5-3 自陳「同名不同定義本篇看不到」，
   實測顯示**它是常態而非例外**（91%）。**R-VS9 之條文若不強制指明網段，訊號斷言之位元位置即不確定。**
3. **037 表頭含雙空格**（`Requirement  Title`／`Requirement  Description`）。
   未正規化空白之欄位定位會直接失敗 —— 本輪首跑即因此拋錯。
4. **`recon.py` 之 leaf 判準與下放包 §5.1 不同**（46 vs 56）。
   兩者皆宣稱在數 leaf，**差額 10 未追因**。
5. **scaffold 模板之欄位對映與本 feature 之 036 不符**（design_method／functional_safety／author 三欄）。
   模板註解寫「verified by recon header match — do not guess」，**而模板自身之預填值即為未驗證之猜測**。
6. **`SYS-RA-CFTS100` 之存在**意味 037 之來源引用可跨文件。
   本 feature 之「上游規格為 CFTS044」此一前提，**在 1 / 271 上不成立**。

---

## 9. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，八項**

### 9.1 本輪未執行之作業（**具名，不假裝已做**）

| 作業 | 狀態 | 影響 |
|---|---|---|
| **W-8** 三來源 `$變數$` 對照 | **未執行** | 升級條件 3 未被觸發**不是因為沒有不一致，是因為沒比對**。CFTS044 內嵌值域之抽取未做 |
| **W-9** Comfort 43 leaf 逐條對照 | **未執行** | R-VS7 之裁定素材未備；B 組之「必停」未觸發 |
| **W-13** 26PI2.5/HMI 全文掃描（約 112 檔） | **未執行** | 00D 之「失效彈窗不在該目錄」仍為**已知未查**，非已查為綠。A-VS10 未複驗 |
| **W-15(b)(c)** 之 (b) 逐屬性比對 DBC ↔ LID 表 | **僅做 DBC↔DBC** | LID 表側之 signal 名／CAN id／起始位元未與 DBC 交叉比對 |
| **W-14** 之 `TRUNCATED_ENUM` 判準 | **僅以 `# = Not Used` 結尾偵測** | 其他截斷形態（如以 `...` 結尾、或列舉中斷而無標記）偵測不到 |

### 9.2 沿用而未複驗者（**照錄分析層，非本輪實測**）

`A-VS03`／`A-VS04`／`A-VS07′`（部分）／`A-VS08`／`A-VS09`／`A-VS10`／`A-VS11`；
`DATA_REQUESTS.md` 之「已查而不取用」一節之七份檔案判定；
SYS3 SYSAD 內文（00C §5-1 之待辦，**自 00C 起未做至今**）。

### 9.3 三項結構性疑慮

1. **`specification_reference` 之形式尚未定案，而下放包稱 R-VS2(c) 已解除。**
   00E §3 記其「解除」，依據為 245/271 已解析。**但 5 個 leaf 落多章節（A-VS14）、
   1 個 leaf 無錨鏈（A-VS12）、25 個 leaf 有 id 無章節** ——
   即 **31 / 271 之 N 欄形式仍未定**。「解除」為過早之判定。
2. **本輪之三個「相符」其實是同一個來源在自我印證。**
   037 leaf 數、SYS-RA 數、Category 分布三者皆自四份 037 與 SYS2 算得，
   而下放包之預期值亦自同一批檔案之沙箱副本算得。
   **兩者相符只證明我與分析層讀了同一份檔且讀法相同，不證明該檔正確。**
   真正的獨立檢驗是 W-5 之對照向（§5）與 CFTS044 docx 之樣式階層（§2.4）—— 只有這兩處。
3. **A-VS17 使 R-VS9 之現行草案不足。** 00H §3 之草案第 (3) 項僅要求「網段依 LID 表 CAN 欄註明」，
   **未要求 TC 內文指明**。而 128/141 之起始位元差異意味：
   同一個 signal 名在兩條匯流排上是兩個不同的量測點。
   **建議 R-VS9 增列：訊號斷言須同時指明 message 與網段。** —— 此為建議，**不代擬條文**。

---

## 10. 給 Pei 之 git 與檔案指令草稿（**未執行，帶 pathspec**）

```bash
# 一、移除 new_feature.py 依 R-VS3 之指令誤建之空白目錄（A-VS19）
#     先確認其內為 scaffold 模板、無任何本輪產物：
ls -la "features/vehicle setting"
rm -rf "features/vehicle setting"

# 二、入庫本輪產物（唯讀 git 已跑：git status --porcelain features/vehicle_setting/）
git add features/vehicle_setting/
git commit -m "feat(vehicle_setting): round 00 — intake, recon, anchor chain, LID and DBC baselines"
```

> **git 唯讀與改狀態分列**（R-G6）：
> 本輪執行之 git 指令僅 `git status --porcelain`（用於確認 handoff 未被 scaffold 覆寫）。
> **未執行任何 add／commit／checkout／restore／stash／clean／tag。**

---

## 11. 產出清單

| 檔 | 內容 |
|---|---|
| `inputs/INPUTS.sha256` | 14 檔，`shasum -a 256 -c` 全數 OK |
| `data/leaves.tsv` | 271 leaf（swe_id／family／src_ref／title／desc） |
| `data/uncovered_leaves.tsv` | 34 未覆蓋 leaf |
| `data/sysra_to_polarion.tsv` | 273 筆錨鏈（含 category 與 7 位數 ID） |
| `data/outline_map.tsv` | 271 leaf → CFTS044 章節（245 OK／25 NO_SECTION／1 NO_ID） |
| `data/lid_map.tsv` | 3,105 列、3,000 相異 LID，含 flags |
| `docs/reports/036_baseline.md` | W-3 逐欄填充率與 R-VS1 依據 |
| `ANOMALIES.md` | A-VS01–A-VS19 |
| `DATA_REQUESTS.md` | 含路徑與 SHA；新開 DR-9／DR-10 |
| `RECON.md` / `DECISIONS.md` / `data/recon.json` | recon 產出，state=BLANK |
| `feature.yaml` | `spec_mode: D`；分頁名與欄位對映依實測填實 |
