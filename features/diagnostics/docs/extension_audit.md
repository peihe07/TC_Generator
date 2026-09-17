# Diagnostics —— 延伸審計（R-DIAG23／R-DIAG24／R-DIAG25）

母體：037 V1 (3) 之 **389** 列（`layer2_assign.tsv`）。逐列比對三個延伸來源，
候選明細見 `extension_audit.tsv`（**355** 列）。本檔為摘要。

## 一　依 source 之候選數／已產數／N 數

| source | 候選列數 | `Y` | `P` | `N` | 已產出／已斷言 |
|---|--:|--:|--:|--:|---|
| `037-VC` | 11 | 11 | 0 | 0 | 邊界軸／順序軸／值域軸 —— 全數已由既有 TC 斷言 |
| `037-VM` | 25 | 25 | 0 | 0 | 天線態軸 **新產 4 條**；enable／disable 態軸 **Revise 2 條**；逾時／重試／逐欄位軸已斷言 |
| `CFTS004-INFO` | 319 | 39 | 13 | 267 | **新產 3 條**（4940293／4940480／4940338）|
| **合計** | **355** | **75** | **13** | **267** | **新增 12 條 ＋ Revise 8 條** |

> **表中之列數為「037 列 × 錨」之配對數，不是相異候選數。** 同一個 CFTS004 Information 列會
> 對應到同節內的每一個 037 列（例：`Externally generated tone` 一句對應 `$5000` 之 39 個 037 列），
> 故 `Y` 75 列去重後之**相異候選只有 10 個**（`037-VC` 4 軸／`037-VM` 5 軸／`CFTS004-INFO` 1 句），
> `P` 13 列去重後為 **2 個**。實際產出 12 條新 TC ＋ 8 條 Revise 即由此 12 個相異候選而來。

`037-DESC`（定型句之失效型態）**零殘餘** —— R-DIAG22／R-DIAG22(amend) 落地後，
「invalid length／incorrect format／unsupported DID」三型分由長度軸與 unsupported DID 軸斷言，
`without side effects` 由 `*_initial` 比對斷言。故該 source 於本表不出現任何候選列。

## 二　`N` 之集中原因 —— 267 列中 **243 列是「引言句」**

`CFTS004-INFO` 之 319 列去重後僅 **12 個相異原句**，其中五句為列表引言
（`… the following items:`／`The following tones shall be selectable in this DID:`／
`… the following information as provided by the internal GPS receiver.`／
`… the following data shall be readable from and writeable to this DID:`），
**其列表本身未隨 CFTS004 匯出帶出**（與 `$5000` r328／`$5001` r320 同一現象，已載於 `asset_request.md`）。
引言句無列舉內容可斷言，故一律 `N`；缺的是資料，不是 TC —— 對應 `DR-DIAG-4`／`DR-DIAG-5`。

## 三　新增與 Revise 清單

| 動作 | TC | 037 列 | 依據 |
|---|---|---|---|
| Revise ＋ 新增 3 | `-335`／`-545`～`-547` | `-266` | R-DIAG25(a)：Subscription status 四態各一條（取代 CDD-07 之單條收斂）|
| Revise 2 ＋ 新增 2 | `-526`／`-527`／`-548`／`-549` | `-213` | R-DIAG25(a)：Signal 0–3 bars 四值各一條（值數 4 ≤ 8，逐值優於 BVA 兩點）|
| Revise ＋ 新增 2 | `-523`／`-550`／`-551` | `-211` | R-DIAG24(b)：037 VM 天線態情境 ＋ CFTS004-4939801 三態（引兩錨）|
| Revise ＋ 新增 2 | `-530`／`-552`／`-553` | `-215` | 同上（Satellite signal）|
| 新增 1 | `-554` | `-115` | R-DIAG23(c)：CFTS004-4940293 補充已引之 4940296 |
| 新增 1 | `-555` | `-151` | R-DIAG23(c)：CFTS004-4940480（`P` —— 多訊號線輸入清單未載，佔位）|
| 新增 1 | `-556` | `-035` | R-DIAG23(c)：CFTS004-4940338（`P` —— F／S 值未載，佔位）|
| Revise 1 | `-134` | `-056` | R-DIAG25(b)：錨列舉六子項 → ER 依 §6.1 逐項 |
| Revise 2 | `-219`／`-223` | `-007`／`-010` | R-DIAG24(b)：enable／disable 之可觀察面改以 `$500B` 讀回斷言（CFTS004-4939956）|

單一 SWE1 列拆分最大 **5**（`SWE1-Diagnostics-028`），未達 R-DIAG25(c) 之上限 8。

## 四　環境／持久軸 —— 未延伸之由（R-DIAG23 末句）

canon §8.3 之環境／持久軸（重開機／電源循環／設定保存）於 CFTS004 全文 grep：

| 詞 | CFTS004 命中列數 |
|---|--:|
| `reboot` | 0 |
| `power cycle` | 0 |
| `persist` | 0 |
| `retain` | 0 |
| `ignition` | 1 |

**五詞全為 0。** 依 §8.4.1（不造值），無來源即不得自行擬定「重開機後設定應保留」之斷言；
037 之 VC／VM 亦零命中。故本 feature **不延伸環境／持久軸**，並將此事實記於 coverage 說明。
若 RD 確認該行為存在，應由 CFTS004 補件後再行延伸（併 FB 送出）。

## 五　未列為候選而另送 RD 者

| 錨 | 原句 | 由 |
|---|---|---|
| `CFTS004-4939889`（`SYS-RA-DIAG-055`，Information）| `The radio shall return the current Sirius XM package ID when the radio receives a read request.` | `$2847` 之**讀**行為為獨立行為（037 只引其寫向 4939890／4939891／4939892），非補充已引 FR → 依 R-DIAG8(a) 不產；**新開 FB-DIAG-s** |
