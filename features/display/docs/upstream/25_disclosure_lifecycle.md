# 上繳包 25 —— 揭露機制之時效與 token 資料化；CFTS013 未到手

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/25_disclosure_lifecycle.md`
  （含下放包 24 之步驟 1–6、8）
- **停止條件 61／62 無從通過：CFTS013 檔案不在本機。**
  下放包 24 之步驟 **4／5／6 未執行**，理由見 §五。其餘全數執行
- 停止條件 60／63／64 皆未觸發；1–59 亦全未觸發
- **git 未執行**（§7 為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 25-1 抄錄 | R-DM51／R-DM52／R-DM53 → `RULINGS.md`；R-G34／R-G33(d) → ledger。**五條全相符**；R-DM 區塊累計 **55**，順序驗證 exit 0 |
| 25-2 `deferred` 物件化 | 三項四鍵齊備；**三條 TC 之任一欄位一字未動**；R-G33(c) 仍 PASS（停止條件 63 未觸發） |
| 25-3 雙向檢查 | `check_disclosure.py`：**MISSING 0／STALE 0**（停止條件 64 未觸發） |
| 25-4 BACKLOG | 末列依據升為 R-G33(d)，並記雙向判準與腳本 |
| 24-1 抄錄 | 已含於 25-1 |
| 24-2 A-DM31 修正 | 已執行，附本層無法重算之限定 |
| 24-3 DR-DM10(b) 問法 | 已執行，附「HU 側事實、不得代入」與未重算之限定 |
| 24-4 `popup_priority.tsv` | **未執行** —— 見 §5.3 |
| 24-5 綁定 12 項 | **不可執行** —— 無檔可綁；現為 `entries: 11`／11 of 11 |
| 24-6 獨立重算 | **不可執行** —— 無檔可算 |
| 25-6／24-8 INDEX | 已更新 |

**兩項是你的錯，我一項也沒少犯。** 上繳 23 我把 R-G33(c) 之三個
英文 token 稱為「對譯」並自陳其為判斷（B11）—— 那是對的；
但我**沒有想到把 token 移到宣告端**這個解法，是下放包 25 想到的。
我只診斷、沒開方。

---

## 一、三條之抄錄核對表（各自獨立，置放依 R-G34）

### 1.1 置放

- **`R-DM51`／`R-DM52`** → `features/display/RULINGS.md`
  之新節「來源：下放包 24」
- **`R-DM53`** → 同檔之新節「來源：下放包 25」
- **`R-G34`／`R-G33(d)`** → `docs/fw036/RULINGS_LEDGER.md`
  之新節「下放包 25 之全域條文」

**`R-G33(d)` 為對 `R-G33` 之補充，依 R-G34 置於本包之節而非 R-G33 條下。**
R-G33 條下已留指標：

> **補充（下放包 25）**：`R-G33(d)`（揭露句之時效）見本檔末
> 〈下放包 25 之全域條文〉節。**依 R-G34 置於該處而非本條之下**，
> 原條文不刪不改。

> R-G34 立條後**第一次適用，且這次是我自己的補充**（23 輪那次是
> R-DM48）。條文之「分析層之指示若與本條衝突，以本條為準」
> 本輪未被用到 —— 下放包 25 步驟 1 已自行寫明「置放依 R-G34」。

### 1.2 核對表

## 抄錄核對表 — 24_cfts013.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 53 | R-DM51 | `features/display/RULINGS.md` | 784 | `4229126d50d3f3a7` | 是 |
| 54 | R-DM52 | `features/display/RULINGS.md` | 357 | `6e5a416e08cad747` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **55** 個，與各下放包原檔逐字元比對 **全數相符**（55 vs 55）。

## 抄錄核對表 — 25_disclosure_lifecycle.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 55 | R-DM53 | `features/display/RULINGS.md` | 663 | `853186e2da1ef094` | 是 |
| — | R-G34 | `docs/fw036/RULINGS_LEDGER.md` | 585 | `1d9fd1d5e08c4efe` | 是 |
| — | R-G33(d) | `docs/fw036/RULINGS_LEDGER.md` | 633 | `1a8906abccf19569` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **55** 個，與各下放包原檔逐字元比對 **全數相符**（55 vs 55）。

兩表分列，即「各自獨立核對表」。`RULINGS.md` 之 R-DM 區塊自 52 增為
**55**（＋R-DM51／R-DM52／R-DM53），順序驗證 **exit 0**。

---

## 二、改寫後之 `deferred` 陣列全文（R-DM53）

```json
[
  {
    "leaf_id": "SWE1-DM-004",
    "token": "warning popup",
    "blocking_dr": "DR-DM10",
    "reason": "DR-DM10(a) 未結。組 B {4820289} 於越過門檻時即關背光，使 popup 之顯示不可觀測；組 A {4820283} 則蘊含警示階段。兩組皆宣告適用於 R1H / Atlantis High"
  },
  {
    "leaf_id": "SWE1-DM-005",
    "token": "protective shutdown",
    "blocking_dr": "DR-DM10",
    "reason": "組 A／組 B 何者為準未裁定，且 {4820283} 之警示階段無時長；DR-DM10 開立；21 包 §2.1 分支 3（原 pilot-01 #2）"
  },
  {
    "leaf_id": "SWE1-DM-005",
    "token": "multi-stage",
    "blocking_dr": "DR-DM4",
    "reason": "multi-stage 分級門檻 —— DR-DM4 未結（CFTS_013 之 629／633／952 未取得；下放包 24 之 SYSRA 檔不含該三條，且該檔本身未落磁碟，見上繳 25 §五）"
  }
]
```

四鍵齊備。三個 `token` 取上繳 23 §2.1 之既有對譯，**不重新決定**
（下放包 25 §三 R-DM53 末段之指定）。

**第三項之 `reason` 本輪加了一句**：`multi-stage` 之 blocking DR 為
DR-DM4，而下放包 24 已查明其所求之 `629`／`633`／`952` 不在 SYSRA 檔內
（R-DM52），**且該 SYSRA 檔本身未落磁碟**。兩層事實都記入，
以免日後讀到「DR-DM4 未結」時以為只差一份已在路上的檔。

### 2.1 改寫未動 TC 之證明（停止條件 63）

`deferred` 物件化前後，三條 TC 之 `test_item`／`pre_conditions`／
`input_test_data`／`test_procedure`／`expected_result`／
`specification_reference`／`split_reason` **七欄一字未動**。
R-G33(c) 之檢查於改寫後仍 PASS（§三），即 token 落定與既有揭露句相符。

**若 token 落定有誤，此處會顯示為 `MISSING` 非 0** —— 這正是
停止條件 63 之設計。實測 0，故 token 落定無誤。

---

## 三、雙向檢查之輸出（R-G33(d)(2)）

腳本：`features/display/scripts/check_disclosure.py`（本輪新增，
feature 自有；接入 `lint036` 屬 Tier 2，仍列 B10）。

```text
# R-G33(c) 雙向檢查（R-G33(d)(2)）
batch: generated/pilot-01.json
tcs: 3   deferred entries: 3

| TC | leaf | token | 方向 | 判定 |
|---|---|---|---|---|
| #1 | SWE1-DM-004 | `warning popup` | MISSING | 含 |
| #2 | SWE1-DM-004 | `warning popup` | MISSING | 含 |
| #3 | SWE1-DM-005 | `protective shutdown` | MISSING | 含 |
| #3 | SWE1-DM-005 | `multi-stage` | MISSING | 含 |

MISSING = 0   STALE = 0
```

**`MISSING = 0`、`STALE = 0`。停止條件 64 未觸發。**

判準說明（R-DM53 之效果）：`token` 直接取自 `deferred` 項之 `token` 鍵，
**檢查為純字串比對（`tok.lower() in low`），無對譯、無判斷成分**。
上繳 23 之 B11 至此結案 —— **不是因為對譯變可靠了，是因為不再需要對譯。**

`STALE` 之母體具名：對每一 TC，取「全部 token 減去該 leaf 之 token」
為 STALE 之候選集。本批 004 之 TC 檢 `protective shutdown`／`multi-stage`
兩個、005 之 TC 檢 `warning popup` 一個 —— **該方向有母體，0 為實測。**

> R-G33(d)(1) 要求該檢查於**兩個時點**各執行一次：TC 寫入時、
> **交付前（release gate）**。本輪為前者。**後者尚未發生，且目前
> 沒有任何機制保證它會發生** —— 交付前之 gate 尚未定義（見 §六 B12）。

---

## 四、`BACKLOG.md` 重審節之更新

末列改為：

> | **各 TC 之括號下半（R-G33(d)）** | **依據已升為條文 R-G33(d)（下放包 25），非僅本清單之一項。** deferred 項若解除，其括號下半之揭露句須同步移除 —— 否則工作簿上會留下一句已不成立的「is deferred」 | 3 條皆含揭露句（23 包補寫） |

節末之註記增列：

> 下放包 25 §1.3 採納並立為 **R-G33(d)**，其 (2) 另定交付前之檢查為雙向：
> 陣列有而括號無 → `MISSING`；陣列無而括號有 → `STALE`。
> 檢查腳本 `scripts/check_disclosure.py`（本輪實測 MISSING 0／STALE 0）。

原增列理由（雙向誤讀）之文字保留，不改寫。

---

## 五、下放包 24：CFTS013 檔案不在本機

### 5.1 查證

下放包 24 §一據
`SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx`
作出全部量測。**該檔不存在於本機任何位置。**

查證範圍（皆為實測，非推定）：

| 查法 | 結果 |
|---|---|
| `features/display/inputs/` 含 `013` 者 | **0** |
| 全 repo `find -iname "*CFTS013*"`（排除 `.git`） | 僅 `docs/handoff/24_cfts013.md` **本身** |
| `_intake/Display/` 全部檔案 | 4 個（037／CFTS_020 docx／SYS2 匯出／SYS3 SYSAD），**無 013** |
| 全 repo 檔名含 `Associated`／`ADspl`／`Radio*Error` | **0** |
| `~/Downloads`、`~/Desktop` 含 `CFTS013` | **0** |
| 全 repo 2026-08-20 後之 `.xlsx`（19 個） | 逐一檢視，**無一為 CFTS013** |

**這不是 01 輪那種檔名差異問題。** 01 輪之 037 確實在磁碟上，
只是命名用連字號（R-DM11）。本輪**沒有任何檔名近似之候選** ——
沒有 `Associated`、沒有 `ADspl`、沒有 `Radio Error`。

依 R-DM2(a)：**不以他檔替代、不自下放包之數字回填、停並回報。**

### 5.2 逐步驟之處置

| 24 包步驟 | 狀態 | 理由 |
|---|---|---|
| 1 抄錄 R-DM51／R-DM52 | **已執行** | 條文文字在下放包內，逐字可抄；且 R-DM51 為**保護性**條文（禁止代入），愈早生效愈好 |
| 2 A-DM31 敘述修正 | **已執行，附限定** | 見 §5.4 |
| 3 DR-DM10(b) 問法更新 | **已執行，附限定** | 見 §5.5 |
| 4 `popup_priority.tsv` 來源登記 | **未執行** | 見 §5.3 |
| 5 `reference:` 增 `cfts013_sysra`、綁定 12 項 | **不可執行** | 無檔可綁；`entries` 仍為 **11**、`11 of 11 match`。**停止條件 62（須 12/12 且 entries 12）無從通過** |
| 6 §一§二之獨立重算 | **不可執行** | 無檔可算。**停止條件 61 無從評估** —— 我無法確認 `Document ID` 全集是否含 `629`／`633`／`952` |

### 5.3 為何 24-4 未執行（本輪唯一一項「可寫而不寫」）

步驟 4 要求把 `{CFTS013-937}` 之優先序行為與 `PU0130` 之逐字出處
寫入 `data/popup_priority.tsv` 之來源清單。

**該表是交付所依之資料檔**（`BACKLOG.md` A4 列其為 006 之阻斷解除物），
其 sidecar 有 `generated_by` 欄。若本輪寫入，該欄只能填
「人工登記自下放包 24」——**而下放包 11 步驟 4 正是為了消滅
最後一份人工建檔而做的**（`spec_text_layer.tsv` 改為腳本產出）。

更關鍵：寫入之內容是**規格本體之逐字引用**（`the 'Screen is Hot' popup
(Popup PU0130, a.k.a. 'Display is Hot')`）。本 feature 自 02 輪起之
一貫作法是**規格內容一律機器抽取**，不從下放包轉抄。
**這是全案唯一一次我被要求把沒見過的規格文字寫進資料檔。**

故：**登記為待辦，不寫入。** 檔案一到手，該步驟可於單輪內完成
（含機器抽取與 sidecar）。

> 若分析層認為此判斷過嚴、要求先以「來源＝下放包 24、未經重算」
> 之形態登記，請明示；我會照做並在 sidecar 之 `generated_by`
> 與 `notes` 兩處具名其未經驗證。

### 5.4 24-2 之限定（A-DM31 已修正）

修正內容：`SYS2_CFTSnnn_*` 為 **SYSRA 報告（`FM-WI-FSM-035-A02`）
之命名慣例**，`SYS2_` 前綴不應被讀為「SYS2 匯出」。原判定
（CFTS043 為 HVAC、不答 DR-DM3）與其全部實測數字**不變**。

**本層採認之依據不是那份看不到的檔**，而是：`FM-WI-FSM-035-A02`
一詞**逐字見於本 feature 已持有之 CFTS043 檔名**
（`inputs/SYS2_CFTS043_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告…`）。
即該命名慣例在手上的材料裡就能自證，不必依賴 013。

限定已逐字寫入 A-DM31 之修正註記。

### 5.5 24-3 之限定（DR-DM10(b) 已更新）

問法由「警示階段之時長為何」改為
「**DCSD 側之 warning → off 是否亦為溫度分段？若是，其第二門檻為何？**」。

**這個更新我判斷是對的，而且它不依賴 013 之數字是否正確** ——
它改變的是**問題的變數**（時間 vs 溫度）。即使 §2.3 五列有出入，
「分段變數可能不是時間」這個提示仍成立，而問對變數比問對數字重要。

已於 DR 文字中逐字標明：該五列為 **Associated Display（HU 側）之事實，
非 DCSD 側**，依 R-DM51(a) 不得代入；且**本層未能重算**。

### 5.6 R-DM51 之拘束本輪已生效（停止條件 60）

```text
受檢母體：pilot-01.json 之 3 條 TC（7 欄）＋ batch_context.md 全文
判準：CFTS013 之門檻數字（50／51／55／56／60）後接 degree/deg/°C 者


hits = 0  →  停止條件 60：未觸發

對照：本批實際使用之溫度門檻（應只有 85）
  ['85']
```

**hits = 0，停止條件 60 未觸發。** 本批實際使用之溫度門檻只有 `85`
（CFTS_020 `{4820289}`／`{4820290}`），無一取自 CFTS013。

### 5.7 綁定現況（停止條件 62 之對照）

```text
entries: 11
**11 of 11 match.**
```

**`entries: 11`，非 12。** 下放包 24 步驟 5 要求 12/12 而
停止條件 62 規定「非 12/12 或 entries 非 12 → 停」——
**該條件無從通過，因為第 12 項之檔案不存在。** 依 R-G26，
本數字連同其母體一併引用：11 項為現有素材之全部，非「少了一項的 12」。

---

## 六、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A 與組 B 何者為本架構之準 | 004 之 popup 側；005 之關閉側 | DR-DM10(a) |
| A2 | DCSD 側 warning → off 之分段變數與第二門檻 | 原 #2；`PU0130` | DR-DM10(b)（**本輪已改問法**） |
| A3 | HU 側 `$TGW_DISP_STAT$` 之值標籤對應 | 007／008 之 HU 側訊號欄 | DR-DM9（**A-DM35：其前提須先更正**） |
| A4 | `popup_priority.tsv` | `SWE-DM-006` | DR-DM2 |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| **A6** | **CFTS013 SYSRA 檔本身** | 24 包步驟 4／5／6；DR-DM2 之 HU 側材料 | **新增：檔案未落磁碟** |

A6 為本輪新增。**A3 之範圍已依 A-DM35 縮小**（DCSD 側之
`[RR_CMRA]`／`[ON]` 逐字解得，不受阻）。

### B 類 —— 不阻斷交付

| 編號 | 項 | 為何不阻斷 |
|---|---|---|
| B1–B9 | 見上繳 23 §六 | 不變 |
| B10 | R-G33 判準未入 `lint036` | 已為 feature 自有腳本 `check_disclosure.py`；接入共用腳本屬 Tier 2 |
| ~~B11~~ | ~~token 為自訂對譯~~ | **結案** —— R-DM53 把 token 移到宣告端，檢查已無判斷成分 |
| **B12** | **交付前之 release gate 尚未定義** | R-G33(d)(1) 要求雙向檢查於交付前再執行一次，**但「交付前」是哪個動作、由誰觸發，目前無定義**；寫回 036 尚未發生，故不阻斷 |
| **B13** | **`{CFTS013-937}` 對 `PU0130` 之逐字出處未登記** | 24-4 未執行（§5.3）；`PU0130` 現已隨原 #2 deferred，本批不用 |

B12／B13 為本輪新增。**B11 結案。**

---

## 七、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/generated/pilot-01.json \
  features/display/RULINGS.md \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/scripts/check_disclosure.py \
  features/display/docs/handoff/24_cfts013.md \
  features/display/docs/handoff/25_disclosure_lifecycle.md \
  features/display/docs/upstream/25_disclosure_lifecycle.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): make the deferred disclosure checkable in both directions

- turn each deferred entry into an object carrying its own English token, so
  the R-G33 check is a plain string comparison instead of a translation the
  checker has to make (closes the B11 self-report)
- add check_disclosure.py: MISSING when the array has a token the bracketed
  note lacks, STALE when the note keeps a token the array no longer has
- add R-G33(d): a disclosure sentence must be removed when its deferral is
  lifted, or the workbook claims an already-tested facet was not tested
- add R-G34: a supplement goes in its own package section, never where it
  would break the transcription order check
- add R-DM51/R-DM52: CFTS013 covers the Associated Display, not the DCSD, so
  its thresholds may not be substituted, and the file at hand is a partial
  analysis that does not contain the three clauses DR-DM4 asks for
- reword DR-DM10(b) to ask whether the DCSD staging is by temperature rather
  than by time
- record that the CFTS013 workbook is not on disk, so its binding and the
  independent recount could not run
```

> `batches/pilot-01/batch_context.md` 不入 pathspec（`.gitignore` 已排除）。
> `docs/upstream/24_cfts013.md` **不產出** —— 24 包之產出併入本上繳包，
> 其步驟 4／5／6 未完成，單獨出一份會讀起來像已交付。
> 036 母本未變更，亦不入。

---

## 八、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **A-DM31 之修正、DR-DM10(b) 之新問法，其實質內容我都沒有驗過。**
   §5.4／§5.5 各給了一個「不依賴 013 也成立」的理由，我認為兩者都站得住。
   **但那是兩個繞道，不是驗證。** 若 24 包對 013 之量測整份是錯的
   （例如那根本是另一份文件），這兩處會留下錯誤的痕跡而沒有人再回頭看
   —— 它們不像 A6 那樣掛在一個 OPEN 項上。

2. **`STALE` 方向從未在真實情境下被觸發過。**
   本輪 0 是實測且有母體，但**沒有任何 deferred 曾被解除**。
   即這個方向的檢查只證明了「現在沒有殘留」，
   **沒有證明它在解除發生時抓得到**。R-G25（宣稱不做 X 須跑兩次）
   之精神在此適用而本輪未做 —— 我可以造一個假的解除來測它，本輪沒做。

3. **R-DM53 把 token 從檢查端移到宣告端，判斷沒有消失，只是換了人。**
   條文自己講明了這點（「`token` 之選定仍是人的決定」）。
   本批三個 token 是**沿用**上繳 23 的對譯 —— 也就是說，
   **這個機制的第一批資料，正是它想取代的那種判斷產生的。**
   下一批新寫的 deferred 才是它第一次真正被測試。
