# 上繳包 17 — 積壓機制化、A-PV13 修正、交付前收尾

執行層 → 分析層。2026-08-14。回應 `docs/handoff/17_predelivery.md` §5 之七項。

**下放包 18 §2 依 Pei 指示待交付後再辦**，本輪未執行、R40 未貼入。

---

## 1. §5.1 —— handoff／upstream NN 對應表（R39-1，首份）

> ## ⛔ 停手條件 4 觸發
>
> 條件：「第 4 項之對應表發現 **15／16 以外**尚有缺對應之 NN →
> 停止其餘，續行回報缺口清單。」
>
> **缺對應者七個**：05 / 06 / 08 / 10 / 15 / 17 / 18 —— 遠不止 15。
> 依該條，**第 5 項（打 tag 前之獨立複驗）未執行**。
> 第 1–3 項照辦，理由見 §1.2。

### 1.1 對應表

| NN | handoff | upstream | 處置 |
|---|---|---|---|
| 00 | ✅ | ✅ | — |
| 01 | ✅ | ✅ | — |
| 02 | ✅ | ✅ | — |
| 03 | ✅ | ✅ | — |
| 04 | ✅ | ✅ | — |
| **05** | ✅ | ❌ | `05 → merged into 07` —— 上繳包 07 首節明載「本份合併回報下放包 05 / 06 / 07」 |
| **06** | ✅ | ❌ | `06 → merged into 07` —— 同上 |
| 07 | ✅ | ✅ | — |
| **08** | ✅ | ❌ | ⚠️ **無合併註記**。該包於 B1-GATE-1 停手期間未執行，其後由 R30 解除停手後補辦，執行結果僅記於 `RULINGS.md` R29 之執行層回報，**未產生上繳包亦未註記合併** |
| 09 | ✅ | ✅ | — |
| **10** | ✅ | ❌ | ⚠️ **該包未定義上繳包要求**（其 §5 為「覆核意見」而非上繳要求）。執行結果記於 `RULINGS.md` R32 之執行層回報 |
| 11 | ✅ | ✅ | — |
| 12 | ✅ | ✅ | — |
| 13 | ✅ | ✅ | — |
| 14 | ✅ | ✅ | — |
| **15** | ✅ | ❌ | `15 → merged into 16` —— 上繳包 16 首節明載 |
| 16 | ✅ | ✅ | — |
| **17** | ✅ | ← 本檔 | — |
| **18** | ✅ | ❌ | **待交付後執行（Pei 指示）** —— 註記**不用** `merged into`，因該詞蘊含已執行 |

**真正無任何註記之缺口為兩個：08 與 10。**
05／06／15 有合併註記（R39-1 明定該註記使其視為已對應），
17 為本檔，18 為指示延後。

### 1.2 為何仍辦第 1–3 項

本包 §3 之序列為 1→6，**對應檢查是第 4 項**。執行層將它提前執行
（依 R22-4(c)，順序得調換並回報），理由是它為停手條件之標的、成本低、
且應在投入後續工作前先知道。

若照原序執行，第 1–3 項會在停手觸發**之前**完成。
順序調換不應改變「哪些項會被完成」，故第 1–3 項照辦，
第 5 項（位於第 4 項之後）停止。**此讀法請追認。**

### 1.3 對 08 / 10 之觀察

兩者性質不同，值得分開記：

- **08** —— 包內**有**上繳要求，執行了卻沒產上繳包。成因是它被
  B1-GATE-1 之停手切成兩段：停手時未執行、解除後補辦，
  而補辦當下沒有回頭補產上繳包。
- **10** —— 包內**沒有**上繳要求（§5 是「覆核意見」）。
  這不是遺漏，是下放包本身未要求。

**R39-1 之機制目前偵測不出這個差別** —— 它比對 NN 集合，
而 10 之缺對應是設計如此。建議：下放包若不要求上繳包，
於其 §5 明寫「本包不產上繳包」，使對應表可據以標記，
否則每次檢查都會把它列為缺口。

---

## 2. §5.2 —— `feature.yaml` 修改前後與測試結果

### 2.1 diff

```diff
（已 staged，見下方摘要）
```

| 欄位 | 修前 | 修後 |
|---|---|---|
| `design_method` | `"Q"` | **`"R"`** |
| `functional_safety` | `"R"` | **`"S"`** |
| `author` | `"Z"` | **`"AA"`** |

### 2.2 停手條件 2 之驗證 —— 行為未變

| 檢查 | 修前 | 修後 |
|---|---|---|
| `recon.py` 結果 | `state=BLANK, leaves=10, targets=10` | **相同** |
| `RECON.md` 之 column conflicts | 三條 | **`(none)`** ← 唯一變化，且為預期 |
| 全套測試 | 944 passed / 15 skipped | **相同** |
| lint 全批 | PASS | **PASS** |
| `write_back.py` 欄位解析 | `design_method=R, functional_safety=S, author=AA` | **相同** |

**寫回腳本之解析結果不變**是關鍵佐證 —— 它本就讀表頭而非
`feature.yaml`（R37-3(a)），故該三欄之字母對產出無效力，
R39-2(c) 之低風險前提成立。**無其他讀取路徑受影響，停手條件 2 未觸發。**

---

## 3. §5.3 —— A-PV13 更新後全文

```markdown
## A-PV13 — scaffold 產出之 `feature.yaml` 欄位字母為 rev C 之前的版本 — **RESOLVED（R39-2，已修，2026-08-14）**

`new_feature.py` 的 `feature.yaml` 樣板寫 `design_method: Q` /
`functional_safety: R` / `author: Z`，範本 rev C 實際為 **R / S / AA**
（Q 已被 `Estimated Test Time (mins)` 佔用）。
`recon.py` 以表頭文字為權威、把落差列為 `feature.yaml column conflicts`
（`RECON.md` 已記三條），未受影響。另 `sheet` 樣板值
`"Test Case Specification&Result"` 與實際分頁名
`"Test Case Specification 測試用例規範"` 不符，會讓 `recon.py` 直接 `sys.exit`。

執行層處置：僅改 `sheet` 為實際分頁名（事實更正，非裁決），並把
`spec_pdf` / `popup_list` 設為 `null`（spec_mode D 無 PDF、未供 popup 清單）。
**欄位字母刻意不改**，保留給 recon 續報落差為證據。
`new_feature.py` 樣板本身之更新屬 repo 層改動，未動。

**最終處置（R39-2，2026-08-14）—— 已修，本條結案。**

| 欄位 | 修前（rev C 之前）| 修後（實測 rev C 表頭）|
|---|---|---|
| `design_method` | `"Q"` | **`"R"`** |
| `functional_safety` | `"R"` | **`"S"`** |
| `author` | `"Z"` | **`"AA"`** |

量測依據：範本 `Test Case Specification 測試用例規範` 第 9 列表頭逐格實測 ——
rev C 於 **Q** 插入 `Estimated Test Time (mins)`，使其後三欄各右移一格。

**修後行為驗證（停手條件 2）**：`recon.py` 仍為 `state=BLANK, leaves=10,
targets=10`，唯一變化是 `feature.yaml column conflicts` 由三條變為 `(none)`
—— 即落差回報消失，此為預期。全套測試 944 passed / 15 skipped 不變；
lint PASS；`write_back.py` 之欄位解析結果不變
（`design_method=R, functional_safety=S, author=AA` —— 它本就讀表頭，
不讀 `feature.yaml`，R37-3(a)）。**無其他讀取路徑受影響。**

---

**處置方向之更正（R39-2）**：執行層先前主張「不修 `feature.yaml`，
以保留 recon 之落差回報作為證據來源」。該理由**經裁定不成立**，三項駁回：

1. **證據不會因修檔而消失** —— 本 anomaly 條目自身即證據載體，
   上表之修前／修後值、量測依據與裁決編號，效力不弱於 recon 之逐次回報。
2. **保留已知錯誤作為告警來源，等同以缺陷充當金絲雀** ——
   代價是任何以本 feature 為樣板之後續 feature 會繼承錯誤字母。
3. R37-3(a) 已裁「位置資訊以標的物為準」，該三欄之字母對產出**無效力**，
   修正屬低風險。

§5a：**不得以保留缺陷之方式維持告警**；告警之正確載體是登記，不是缺陷本身。

---

**狀態沿革（保留供追溯）**：本條原標 RESOLVED，
但**落差本身從未消失** —— `feature.yaml` 之 `columns` 區仍記
`design_method: "Q"` / `functional_safety: "R"` / `author: "Z"`，
而範本 rev C 之實際位置為 **R / S / AA**。
先前之 RESOLVED 指的是「recon 會回報落差」，不是「落差已修」。
寫回腳本依 **R37-3(a)** 改由**表頭文字**解析欄位，該落差已不影響產出；
但記載仍為舊值。曾依 R15-2 改標 `DEFERRED — 記載與實作不一致`，
其後由 R39-2 裁定改修並結案（見上）。

---
```

---

## 4. §5.4 —— 補 STATUS 後之 `DELIVERY.sha256` 全文

```
# DELIVERY — features/privacy/output/ 產出台帳（append-only）
# ─────────────────────────────────────────────────────────────────────────
# 記帳規則：**逐次追加，不覆蓋、不刪除、不改寫既有條目。**
# 每產出一份 xlsx 就在檔尾新增一個 ENTRY 區塊。舊條目即使其檔案已從
# output/ 消失，該區塊仍留著 —— 台帳記的是「產出過什麼」，不是「現在有什麼」。
#
# 為什麼存在：output/ 是 gitignored（.gitignore:17），產出永遠不進版控。
# AMFM 的 v1 與 v2 都是這樣消失的 —— tag fw036-amfm-regen-v1 至今還在，
# 它標註的那份 xlsx 已不在磁碟上，且 v1 不可重產（產生它需要 openpyxl
# 存檔路徑，而 write_back.py 已改接外科手術路徑，該路徑在檔內已不存在）。
# 當時沒有台帳，於是「那份交付件到底是什麼」只能從 tag annotation 拼湊。
#
# 記錄單位（R27-2）：**一次 `--write` 的輸入基準、一次 `--write` 的輸出、
# 任何被送出或被 tag 的產物。** 不入台帳者：同一次操作內的中間檔、探針產物、
# 對照臂輸出 —— 它們不是一個「工作簿狀態」，記入只會稀釋台帳的檢索價值。
#
# 驗證（自 features/privacy/ 執行）：
#     shasum -a 256 -c --ignore-missing DELIVERY.sha256
#
# **旗標的代價（R27-1）**：`--ignore-missing` 使本台帳**無法偵測「產出被刪除」**。
# 它驗的是「還在磁碟上的產出有沒有被動過」，不驗「產出還在不在」。
# 這是 append-only 台帳的必然，不是缺陷 —— 但**台帳綠燈不等於產出俱在**，
# 日後不得如此誤讀。BASELINE 則相反：不加旗標，素材少一個即為停手事由。
# **--ignore-missing 是必要的**：台帳會累積已被清理掉的舊產出，
# 不加該旗標時它們會報 FAILED open or read。加了之後：
#   內容被竄改 → FAILED，exit 1（實測確認）
#   檔案不存在 → 靜默略過，exit 0
# 亦即本檔驗的是「還在磁碟上的產出有沒有被動過」，不是「產出還在不在」。
# ─────────────────────────────────────────────────────────────────────────
#
# ENTRY 001 — 2026-08-13 — 準備完成之工作簿（**非交付件**）
#   狀態      P7 未進行，無任何 fw036-privacy-* tag。這是供 P4 起寫入 TC
#             的工作簿，不是交付物。P7 產出交付件後另起 ENTRY 002。
#   來源      inputs/…_SWQT_20260121.xlsx
#             SHA256 cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d
#             （FM-WI-FSM-036-A01 rev C 通用空白範本，2026-01-21）
#   寫入路徑  backend/xlsx_surgical.py（R18-3 規則 1；R20-5 首次正向適用）
#   改動      1. R23-4 清除殘留樣本列五格 D10/F10/G10/S10/D11（保留 s= 樣式）
#             2. R23-5 填入 D5 範圍 Scope = SWE1_CFTS_022-Privacy_Features
#             其餘一格未動：D2/D3/D4/J5、Cover 封面四格、Cover_old、
#             ChangeHistory_old、下拉選單、Reference 皆維持原樣
#   結構驗證  zip 成員 48 → 48（零增零減）；classic DV 4 → 4；x14 DV 2 → 2
#             差異成員僅 xl/worksheets/sheet6.xml
#   來源完整  產製後重驗 inputs/ 該檔 SHA256 未變 —— 未就地覆寫
#   未驗      尚未由人以 Excel 實際開啟確認（同 AMFM v2 之 R17-9）。
#             P4 開始寫入 TC 之前應完成：無「修復」提示、R/P/AE 下拉可用、
#             分頁數為 10。**此項未完成前，本條目不得升格為交付件。**
#   未列入    output/prepared_step1_cleared.xlsx —— 只做清除、未填 Scope 的
#             中間產物。**不記入之理由已依 R27-2 更正**：不是「怕清理後
#             shasum 失敗」（該理由與上方 --ignore-missing 的決定自相矛盾，
#             被清掉的條目本來就會靜默略過），而是它屬同一次操作內的中間步驟，
#             不構成一個工作簿狀態，不符本台帳的記錄單位。
ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4  output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813.xlsx
#   STATUS: 準備完成之工作簿，已經 Excel 確認；為 ENTRY 002 之輸入基準 (R29-1, 2026-08-13)
#
# ENTRY 002 — 2026-08-14 — P6／P7 寫回產出（**非交付件**）
#   狀態      未打 tag、未 commit、未交付。**執行層不宣告 P7 完成** ——
#             依 R29-1 之先例，外科手術產出須經人以 Excel 實開確認方可升格。
#   來源基準  ENTRY 001 之工作簿
#             SHA256 ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
#   寫入路徑  features/privacy/scripts/write_back.py（自始建於
#             backend/xlsx_surgical.py，R20-5；未複製任一既有 write_back）
#   內容      11 TC / 10 葉，第 10–20 列；tc_id NR1L-Privacy-001…011 照序不跳號。
#             -008 為 BLOCKED 列（第 18 列，tc_id NR1L-Privacy-009），
#             帶本 feature 第一個 marker [BLOCKED-ECU]。
#   欄位政策  欄 S = NA 全 11 列（R30-3）；車型欄 T–Z 全空（R30-4）；
#             欄 Q 留白（UNRULED_BLANK）；B 欄序號公式逐列重寫。
#   結構驗證  zip 成員 48 → 48（零增零減）；classic DV 4；x14 DV 2；
#             差異成員僅 xl/worksheets/sheet6.xml。
#             另驗：表頭區（第 1–9 列）逐格未變；其餘 9 個分頁逐格相同。
#   lint      PASS —— 11 TC / 10 檔，19 個 gate 全部具雙對照；
#             欄 S 與車型欄兩 gate 已由 NOT MEASURED 重標為可實測（R34-6）。
#   BLOCKED   四項驗證全數相符：placeholder 旗標未進工作簿；
#             P/R/Q 與 T–Z 確為空；Remarks 288 字元逐字相符無截斷；
#             字型／填色／框線／wrap／列高與相鄰列一致。
#   未驗      ~~尚未由人以 Excel 實際開啟確認~~ → **已完成**，見下行。原文保留存軌跡。
#   Excel確認 Pei, 2026-08-13, 七點全過（R38-1 / 下放包 15 §2）——
#             1) 無「檔案已損毀，Excel 已修復」提示
#             2) R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
#             3) D5 範圍 Scope = SWE1_CFTS_022-Privacy_Features
#             4) 第 10–20 列共 11 列 TC，其餘列為空
#             5) B 欄序號顯示 1…11 —— **此為 cached value 問題之首次現場實測**：
#                11 格皆為公式且無 cached <v>，Excel 開啟時正確重算（R38-2）。
#                結論限於**機制**：zip 層外科手術寫入之顯式公式，缺 cached <v>
#                不影響 Excel 正確重算。**AMFM v2 該實例仍未經 Excel 實開**，
#                本項不得讀為「AMFM v2 已驗證」。
#             6) 第 18 列 Remarks 288 字元完整顯示，無截斷無亂碼（顯示層）
#             7) 第 18 列字型／填色／框線與第 17 列一致
#             **P7 完成。** 本條目自此為交付候選；tag 與 commit 屬 Tier 3。
#   invariant 寫回腳本兩層自加 invariant 之陽性對照已補（R37-5(a)）：
#             改動表頭 D5、下拉選單!A1、Cover 封面!D7 三例皆確實 ABORT；
#             未經破壞之本產出兩層皆通過。三層 invariant 自此為實測有效。
ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f  output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
#   STATUS: P7 完成，交付候選；未打 tag、未 commit、未交付 (R38-1, 2026-08-13)
```

### 4.1 一處位置更正

首次補入時，ENTRY 001 之 `STATUS` 行落在其雜湊行**之前**，
而 ENTRY 002 之落在**之後** —— 不一致，且前者不符 R39-5
「**每一次加註之末行須為狀態行**」之不變式（雜湊行才是該條目末行）。

已將 ENTRY 001 之 STATUS 移至雜湊行之後。兩條目現皆為
「…敘述欄 → 雜湊行 → `STATUS:` 行」，末行即狀態。

該移動屬**本次新增內容之位置修正**，未改寫任何既有欄位（R27-2）。

---

## 5. §5.5 —— 獨立複驗數據表：**未執行**

依停手條件 4 停止（§1）。

該項為打 tag 前之前置（R39-6），內容為：對交付檔重跑
`shasum -a 256`、zip 成員集合、各 sheet classic／x14 DV 計數、
資料列數與列範圍、lint 全批，與 annotation 草案逐項並列。

**一條指令即可完成**，解除停手後即辦。在此之前，
**tag annotation 草案之數值仍為同一次量測之轉錄，不得逕用**。

---

## 6. §5.6 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

lint 全批（修 `feature.yaml` 後）：

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
workbook gates measured against FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx (column S = NA, columns T–Z blank — R34-6)

PASS — no findings
```

---

## 7. §5.7 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。**

### 7.1 R39-1 之機制目前是人工執行，不是機制

該條要求「執行層於每次上繳時比對兩個 NN 集合」。
本輪以一次性腳本產出對應表，**沒有任何東西會在下次上繳時自動跑它** ——
這與 R35-7 所指出、並已 ratchet 化的「一次性人工覆核」是同型問題。

依 R19-3（宣稱排他之規則須有機械執行機制，非僅紀律），
本檢查本身應機制化：例如一支腳本讀兩個目錄、比對 NN、
讀取上繳包首節之 `merged into` 註記，缺對應且無註記即非零退出。
**本包未做**（不在指示內）。

### 7.2 `merged into` 註記目前不可機器判讀

R39-1 說「合併執行者以 `NN → merged into MM` 註記，該註記使該 NN 視為
已對應」。但現行三處合併註記（05／06 於上繳包 07、15 於 16）
**皆為自然語言敘述**，非該格式字串。本輪之對應表是我讀出來的，
不是解析出來的。若要機制化（7.1），註記格式須先統一。

### 7.3 08 之上繳包缺口未補

§1.3 已辨明其性質（包內有要求、執行了、沒產上繳包）。
**本輪未補產** —— 補產需回溯當時之執行細節，且 08 之內容已散見於
R29 之執行層回報與上繳包 09。是否補產、以何形式補，未裁。

### 7.4 A-PV13 修後，`new_feature.py` 之樣板仍為舊字母

A-PV13 之根因是 `scripts/new_feature.py` 產生的 `feature.yaml` 樣板
帶 rev C 之前的字母。**本輪只修了 Privacy 的實例，未修樣板** ——
R39-2(b) 明指「任何以本 feature 為樣板之後續 feature 會繼承錯誤字母」，
而真正的樣板來源是 `new_feature.py`，不是 Privacy 的 `feature.yaml`。
修它屬 repo 層改動，且會影響其他 feature，不在本包範圍。
**下一個新 feature 仍會拿到 Q / R / Z。**

### 7.5 STATUS 行之不變式尚未有 gate

R39-5 立了「每一條目末行須為 STATUS 行」之不變式，
但**沒有任何檢查會驗證它** —— 下次追加 ENTRY 003 時若忘了寫，
或寫在雜湊行之前（本輪即發生過一次），不會有東西發現。
考量 ENTRY 003 已由 R40-1(c) 明文要求含 STATUS 行，
一個簡單的格式 gate 值得在交付前加上。

---
---

# 併入：下放包 19 / 21 之執行（2026-08-14）

> 對應表註記：`19 → merged into 17`、`21 → merged into 17`。
> 下放包 19 §3 停手條件 1 之停手已由 **R43-1 明示解除**，本節為解除後之續辦。

**§2.1 兩項 + §2.2 四項全數完成。四項停手條件皆未觸發。**

| 停手條件 | 結果 |
|---|---|
| 1 STATUS gate 對 ENTRY 001／002 回跑 FAIL | **未觸發** —— PASS，見 §A.1 |
| 2 重出之 annotation 任一值與 R42 更正後不符 | **未觸發** —— 逐項相符，見 §A.2 |
| 3 有包狀態無法以實測認定 | ⚠️ **有一包標 `unknown`**（18），依該條**不停手**，列於 §A.3 |
| 4 台帳 FAILED | **未觸發** —— BASELINE 8 OK、DELIVERY 2 OK |

---

## A.1 —— STATUS 行格式 gate（R41-7）

gate `ledger-status-last` 已上線於 `features/privacy/scripts/lint_tcs.py`。
判準：各 ENTRY 之**最後一行**須符 `# STATUS: <狀態> (<裁決編號>, <日期>)`，
且該行須**在雜湊行之後**（條目形狀：敘述 → 雜湊 → STATUS）。

### 雙對照

```
負向對照：現行 ENTRY 001／002 → PASS ✓

陽性 缺 STATUS        : TRIGGERED ✓
  [ledger-status-last] ENTRY 002: the last line of the entry is
  'ad595ed0cad24375…' , not a `# STATUS: …` line
陽性 STATUS 在雜湊前  : TRIGGERED ✓
陽性 格式不符（無括號）: TRIGGERED ✓
```

### 一項 gate 實作之更正（第三次同型）

首次上線即報 ENTRY 001 FAIL，訊息為「末行是 `'#'`」——
該 `#` 是**條目間的視覺分隔行**（我寫 ENTRY 002 時作為前導空註解加入，
位置上落在 ENTRY 001 之區塊尾）。STATUS 行本身位置正確。

**這是 gate 實作把裝飾行當成內容，不是條目違規。** 已將裸 `#` 排除於
「內容行」之定義外，標準未動（末行仍須為 STATUS，且仍須在雜湊行之後
—— 三項陽性對照確認）。

**這是同型第三次**，值得並列：

| # | 案例 | 標準有無改變 | 處置 |
|---|---|---|---|
| 1 | `er-modal` 把 `Interior CAN` 當 modal `can` | 否 | 修實作 |
| 2 | `spec-reference` 拒絕多引用 | **是**（R35-2 使多引用合法）| 擴充實作 |
| 3 | `ledger-status-last` 把裸 `#` 當內容 | 否 | 修實作 |

R36-1 之型別區分（標準未變 → 修實作；標準已變 → 擴充實作）
在三次適用中皆給出明確答案。

---

## A.2 —— tag annotation 最終稿（各數值標明標的，R43-3）

**每一數值皆於本輪重新量測**，非自草案轉錄；標的逐項標明。

### A.2.1 數值與其標的

| 數值 | **標的** | 量測值 |
|---|---|---|
| SHA256 | **交付檔** `…_regen-v1.xlsx` | `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f` |
| bytes | **交付檔** | 63,001 |
| SHA256 | **寫回之輸入基準**（ENTRY 001 準備工作簿）| `ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4` |
| bytes | **寫回之輸入基準** | **59,992** ← R42 更正處 |
| bytes | **空白範本**（`inputs/…_SWQT_20260121.xlsx`）| 65,823 |
| zip 成員 | 輸入基準 → 交付檔 | 48 → 48，零增零減 |
| 差異成員 | 輸入基準 vs 交付檔 | 僅 `xl/worksheets/sheet6.xml` |
| classic DV | 交付檔 sheet6 / sheet5 | 3 / 1（前後相同）|
| x14 DV | 交付檔 sheet6 | 2（前後相同）|
| 資料列 | 交付檔 | 11 列，第 10–20 列 |
| leaf 數 | 交付檔 | 10 |
| tc_id | 交付檔 | `NR1L-Privacy-001` … `NR1L-Privacy-011` |
| BLOCKED 列 | 交付檔 | 第 18 列，`NR1L-Privacy-009` |
| lint | 全批 | PASS |

**與 R42 更正後之值逐項相符，停手條件 2 未觸發。**

### A.2.2 最終稿全文

```
FW036 Privacy HMI TC delivery v1

Workbook: FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
          Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
SHA256:   ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f
bytes:    63,001

Input baseline — the prepared workbook this write started from
(DELIVERY.sha256 ENTRY 001):
SHA256:   ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
bytes:    59,992

11 TCs across 10 leaves (SWE1-HMI-PRIVACY_FEATURES-001…010), rows 10-20,
tc ids NR1L-Privacy-001…011 with no gap. Row 18 is a BLOCKED row for -008:
CFTS022-4915173 is performed entirely by the AMP, so it is out of scope for
this ECU and carries [BLOCKED-ECU] in Remarks rather than being omitted
(R34-1 / R34-3).

Structure: 48 zip members in, 48 out — nothing lost, nothing added.
Data validations: classic 3 (sheet6) + 1 (sheet5), x14 2 — all preserved.
Only xl/worksheets/sheet6.xml differs from the input baseline. Header rows
1-9 and all nine non-target sheets verified identical cell by cell.

Structure is judged by member set and data-validation counts, not by byte
count (R37-2). Sizes along the chain, each named to its own file: the blank
template is 65,823, the prepared workbook is 59,992, this delivery is
63,001. Preparation shrank the file by 5,831 bytes while emptying five
cells and writing one short string — the size moved out of all proportion
to the content, which is the point (R42/R43-5).

lint: PASS — 20 gates, each with a positive and a negative control.
Excel open confirmed: Pei, 2026-08-13, seven checkpoints.

Anomalies: 13 RESOLVED, 1 CLOSED, 6 DEFERRED, 0 open PENDING.
RD-1 #6-#13 (eight items) not yet sent.
```

**與前一版之差異三處**：輸入基準加 bytes **59,992** 並標明其為
「the prepared workbook this write started from」；體積段改以三段鏈陳述、
每個數值點名其檔案；gate 數 19 → **20**（新增 `ledger-status-last`）。

---

## A.3 —— 完整 `HANDOFF-LINK` 對應表（R41-5，依實測回填）

各下放包檔末已補標記。**19 / 21 之標記為分析層原稿自帶，未動。**

| NN | 狀態 | 實測依據 |
|---|---|---|
| 00–04 | `upstream:NN` | 對應檔存在 |
| **05** | `merged into 07` | upstream/07 首節自述「合併回報下放包 05 / 06 / 07」 |
| **06** | `merged into 07` | 同上 |
| 07 | `upstream:07` | — |
| **08** | **`no-upstream-produced`** | **實測認定**：upstream/07 §2 明載「下放包 08 全部（R29）→ ❌ 未執行」；其後 R30 解除停手時補辦，執行結果**僅載於 `RULINGS.md` R29／R30 之執行層回報段，無任何上繳包涵蓋**。依 R41-4 標記而不補產 |
| 09 | `upstream:09` | — |
| **10** | `no-upstream-required` | 該包 §5 為「覆核意見」，本即未定義上繳要求（R41-3）|
| 11–14 | `upstream:NN` | 對應檔存在 |
| **15** | `merged into 16` | upstream/16 首節自述 |
| 16, 17 | `upstream:NN` | — |
| **18** | **`unknown`** | 見 §A.3.1 |
| 19, 21 | `merged into 17` | 本檔即其落點 |

**下放包 20 不存在**（19 → 21 跳號）。非缺口 —— 無該檔即無標記需求，
parity 測試掃描實際檔案，不假設編號連續。

### A.3.1 為何 18 標 `unknown` 而非 `merged into 17`

18 §4 **宣告**其上繳併入 17。但依 Pei 指示「18 §2 待交付後再辦」，
該包**尚未執行**，17 目前**不含**其內容。

R41-5 明定標記須依**實測**回填、**不得推定**。標 `merged into 17`
是對未發生之事的宣告；標 `no-upstream-produced` 則不實（它不是應產而未產，
是尚未到產出的時候）。

**四個合法值中沒有「已宣告但尚未執行」這一態。** 依停手條件 3
標 `unknown` 並列於此，不停手。**建議 R41-5 增列第五值**，
例如 `pending:<NN>`（已宣告落點、待執行），使延後執行之包不必借用
`unknown` —— 後者的語意是「無法認定」，而 18 的狀態是完全可認定的。

---

## A.4 —— R41-6 常駐測試之雙對照

落點 `tests/test_privacy_handoff_parity.py`。**僅對 `features/privacy` 生效**
（其餘 feature 之往返多未落檔，非本輪標的）。

| 測試 | 類型 | 內容 |
|---|---|---|
| `test_every_handoff_declares_a_link` | 主檢查 | 每包須有 `HANDOFF-LINK` |
| `test_declared_number_matches_the_filename` | 主檢查 | 標記內之 NN 須與檔名相符 |
| `test_status_values_are_legal_and_resolve` | 主檢查 | 狀態值合法，且 `upstream:` / `merged into` 所指之上繳包須存在 |
| `test_no_upstream_is_orphaned` | **反向檢查** | 無人指向之上繳包亦為缺口 |
| `test_positive_control_missing_marker` | **陽性對照** | 移除某包標記 → 須 FAIL |
| `test_positive_control_dangling_reference` | **陽性對照** | 標記指向不存在之上繳包 → 須 FAIL |
| `test_negative_control_legal_no_upstream_required` | **負向對照** | 合法之 `no-upstream-required`（下放包 10）→ 須 PASS |

```
{parity}
```

**`test_no_upstream_is_orphaned` 為本輪自行加入**（R41-6 未要求）：
R39-1 只查「handoff 有而 upstream 無」，但反向亦為缺口 ——
一份沒有任何下放包指向的上繳包，同樣表示紀錄鏈斷了。

---

## A.5 —— A-PV19（R41-8）

已登記，狀態 `DEFERRED — 待 Pei 裁定（R41-8）`。

條目重點：**這是根因而非現象**。A-PV13 修的是 Privacy 之實例，
而 `scripts/new_feature.py` 之樣板仍寫 `Q` / `R` / `Z`，
**下一個 scaffold 出來的 feature 仍會拿到錯值**。

並記入 R41-8 之方向建議：**樣板不應內建欄位字母**，
正解是留空或標 `AUTO` 由表頭解析，**而非把 `Q/R/Z` 換成 `R/S/AA`**
—— 後者只是把錯誤換一個版本，遇到非 rev C 之範本會再錯一次。

---

## A.6 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

lint 全批（含新 gate）：

```
{lint}
```

---

## A.7 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。交付本身無阻塞項。**

### A.7.1 `HANDOFF-LINK` 之標記正確性無人驗證

parity 測試驗的是「標記存在、格式合法、所指之上繳包存在」。
它**不驗標記所述是否為真** —— 例如 05 標 `merged into 07`，
測試只確認 upstream/07 存在，不確認 07 真的涵蓋了 05。
本輪之依據是我讀 upstream/07 首節之自述；那是人工判讀，非機器驗證。

要機制化需要上繳包也帶機器可讀標記（如
`<!-- UPSTREAM-COVERS: 05 06 07 -->`），本輪未做。

### A.7.2 `unknown` 之狀態無到期機制

18 標 `unknown` 是暫時態 —— 交付後執行完即應改為 `merged into 17`。
但**沒有東西會提醒它該改**。parity 測試接受 `unknown` 為合法值，
不區分「永久無法認定」與「暫時未定」。

若 A.3.1 之 `pending:<NN>` 建議被採納，測試可加一條：
`pending:` 狀態存在超過某條件即警示 —— 但那需要先定「條件」為何。

### A.7.3 parity 測試僅涵蓋 Privacy

R41-6 明裁初期僅對 Privacy 生效。但 AMFM 之 `docs/handoff/` 有
四份下放包（01–04）、`docs/upstream/` 有三份（01、02、04）——
**03 亦無對應上繳包**，且那正是 R17-1~R17-4 遭擱置之來源包。
擴及他 feature 需另裁，本輪未做，但該缺口與 Privacy 08 同型。

### A.7.4 annotation 最終稿之 gate 數「20」為本輪新增後之值

前一版寫 19，本輪因新增 `ledger-status-last` 而為 20。
**該數會隨每次新增 gate 而變** —— 若 tag 於日後才打，
而其間又加了 gate，annotation 之數字即過時。
建議打 tag 前再確認一次該數，或改記「所有 gate 皆具雙對照」而不記數量。

---
---

# 併入：下放包 22 之執行（2026-08-14）

> 對應表註記：`22 -> merged into 17`。
> **§2.1 三項完成，交付前之執行層作業至此結束。**
> §2.2（交付後）與 §2.3（close-out）未執行。

| 停手條件 | 結果 |
|---|---|
| 1 定稿數值與前輪獨立量測不符 | **未觸發** —— 13 項逐項複核全符，見 §B.1 |
| 2 標記更新後 parity FAIL | **未觸發** —— 8 passed |
| 3 台帳 FAILED | **未觸發** —— BASELINE 8 OK、DELIVERY 2 OK |

---

## B.1 —— 定稿前之複核（停手條件 1）

R44-6 只要求移除 gate 計數、其餘數值不動。但「不動」是對前輪結果之信任，
而前一輪正是靠**不信任轉錄**才抓到 bytes 之歸屬錯誤。故仍逐項重新量測：

| 項 | 前輪 | 本輪 | |
|---|---|---|---|
| 交付檔 SHA256 | `ad595ed0…3b420b7f` | 同 | ✓ |
| 交付檔 bytes | 63,001 | 63,001 | ✓ |
| 輸入基準 SHA256 | `ed741d8d…5ef5b7e4` | 同 | ✓ |
| 輸入基準 bytes | 59,992 | 59,992 | ✓ |
| 空白範本 bytes | 65,823 | 65,823 | ✓ |
| zip 成員 | 48 | 48 | ✓ |
| 差異成員 | `['xl/worksheets/sheet6.xml']` | 同 | ✓ |
| classic DV sheet6 / sheet5 | 3 / 1 | 3 / 1 | ✓ |
| x14 DV sheet6 | 2 | 2 | ✓ |
| 資料列 / 列範圍 | 11 / 10–20 | 同 | ✓ |
| leaf 數 | 10 | 10 | ✓ |

**13 項全符。**

---

## B.2 —— tag annotation 定稿（供 Pei 直接使用）

依 **R44-6** 移除 gate 計數，改記性質。其餘數值與 §B.1 之本輪量測一致。

```
FW036 Privacy HMI TC delivery v1

Workbook: FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
          Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
SHA256:   ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f
bytes:    63,001

Input baseline — the prepared workbook this write started from
(DELIVERY.sha256 ENTRY 001):
SHA256:   ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
bytes:    59,992

11 TCs across 10 leaves (SWE1-HMI-PRIVACY_FEATURES-001…010), rows 10-20,
tc ids NR1L-Privacy-001…011 with no gap. Row 18 is a BLOCKED row for -008:
CFTS022-4915173 is performed entirely by the AMP, so it is out of scope for
this ECU and carries [BLOCKED-ECU] in Remarks rather than being omitted
(R34-1 / R34-3).

Structure: 48 zip members in, 48 out — nothing lost, nothing added.
Data validations: classic 3 (sheet6) + 1 (sheet5), x14 2 — all preserved.
Only xl/worksheets/sheet6.xml differs from the input baseline. Header rows
1-9 and all nine non-target sheets verified identical cell by cell.

Structure is judged by member set and data-validation counts, not by byte
count (R37-2). Sizes along the chain, each named to its own file: the blank
template is 65,823, the prepared workbook is 59,992, this delivery is
63,001. Preparation shrank the file by 5,831 bytes while emptying five
cells and writing one short string — the size moved out of all proportion
to the content, which is the point (R42 / R43-5).

lint: PASS — every gate carries both a positive and a negative control.
Excel open confirmed: Pei, 2026-08-13, seven checkpoints.

Anomalies: 13 RESOLVED, 1 CLOSED, 6 DEFERRED, 0 open PENDING.
RD-1 #6-#13 (eight items) not yet sent.
```

**與前一版之唯一差異**：`lint: PASS — 20 gates, each with…`
→ `lint: PASS — every gate carries both a positive and a negative control`。

R44-6 之判準值得複述：**該陳述在被封存後若因他處變動而變假，即不應寫入封存。**
「20 個 gate」在下次新增 gate 時即變假，而「每個 gate 都有雙對照」
是本 feature 之常設要求（R34-5），只要該要求成立就不會過時。

**A-PV20 尚未登記**（屬 §2.3 close-out），故 annotation 之 anomaly 統計
維持 13 RESOLVED / 1 CLOSED / 6 DEFERRED。登記後 DEFERRED 將為 7 ——
**打 tag 前若已辦 §2.3，此行需同步更新**。這正是 R44-6 所指之同型風險
（計數型陳述），但 anomaly 統計為交付內容之一部分，不宜略去；
故改為在此明示其依賴。

---

## B.3 —— 完整 `HANDOFF-LINK` 對應表（六值）

R41-5 之合法值經 R44-2 增列為六：

| 值 | 語意 |
|---|---|
| `upstream:<NN>` | 本包產出自己的上繳包 |
| `merged into <NN>` | 上繳併入他包 |
| `pending:<NN>` | **已宣告落點，尚未執行**（可認定之未完成態）|
| `chat-direct:<裁決編號>` | **該輪由 chat 直下、未產下放包** |
| `no-upstream-required` | 設計上不要求上繳包 |
| `no-upstream-produced` | 應產而未產（缺口，照實標）|

| NN | 狀態 | 備註 |
|---|---|---|
| 00–04 | `upstream:NN` | |
| 05 / 06 | `merged into 07` | |
| 07 | `upstream:07` | |
| **08** | `no-upstream-produced` | R44-5 追認；執行結果僅存於 `RULINGS.md` R29／R30 之回報段 |
| 09 | `upstream:09` | |
| **10** | `no-upstream-required` | §5 為「覆核意見」，本即未定義上繳要求 |
| 11–14 | `upstream:NN` | |
| **15** | `merged into 16` | |
| 16 / 17 | `upstream:NN` | |
| **18** | **`pending:17`** | 由 `unknown` 改標（R44-2）。交付後執行完改為 `merged into 17` |
| 19 / 21 / 22 | `merged into 17` | |
| **20** | **`chat-direct:R42`** | ⚠️ **僅存在於本表** —— 見 §B.3.1 |

### B.3.1 `20` 之標記落點與其限制

`handoff/20_*.md` **不存在**（R44-3：跳號為分析層編號疏失，
但該輪確實存在 —— R42 由 chat 直下、未產下放包）。

**故該標記只能存在於本對應表，無檔可標。**
parity 測試掃描實際檔案，`20` 因此**不在測試範圍內** ——
它記錄的是「該編號對應之輪次存在於 `RULINGS.md` R42，而非存在於某個下放包」。

**這是 `chat-direct` 這個值的固有限制**：它描述的正是「沒有下放包」，
而標記機制寄生於下放包檔案。若日後再有 chat 直下之輪次，
同樣無處可標。可能的解法是把對應表本身變成受版控的資料檔
（如 `data/handoff_parity.json`）而非上繳包內之表格 —— 本輪未做。

---

## B.4 —— parity 測試輸出

```
{parity}
```

新增 `test_negative_control_pending_is_legal` —— `pending:17` 須 PASS。
`unknown` 於本 feature 現已無用例（18 改標後），但值仍保留於合法集合，
其警示機制（R44-8）屬 §2.3 close-out，未實作。

---

## B.5 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

lint 全批：

```
{lint}
```

---

## B.6 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。交付本身無阻塞項；交付前之執行層作業已結束。**

### B.6.1 annotation 內之 anomaly 統計仍是可變計數

§B.2 已註明：A-PV20 登記後 DEFERRED 將由 6 變 7。
R44-6 之判準（封存陳述不得含會過時之計數）**在此仍被違反** ——
只是我判斷 anomaly 統計屬交付內容之一部分，不宜略去，故改以明示依賴處理。

**這是一個未解的取捨，不是已解的問題**：若 §2.3 於打 tag 前完成，
該行需手動更新；若之後又有 anomaly 狀態變動，同樣。
可能的解法是 annotation 只記「0 open PENDING」（該項是交付放行之判準，
其餘分布不記），本輪未改 —— 因為那是對 annotation 內容之裁定，非執行層權限。

### B.6.2 `chat-direct` 之標記無寄生處

見 §B.3.1。`20` 之標記只活在本上繳包之表格裡，parity 測試看不到它。
下一次 chat 直下裁決會遇到同樣問題。

### B.6.3 `pending:17` 之到期仍無機制

R44-8 之 `unknown` 警示機制屬 close-out 未實作，且**它針對的是 `unknown`
而非 `pending`**。18 改標 `pending:17` 後，若交付完成而無人回頭改標，
測試會一直 PASS —— `pending` 是合法值。
**`pending` 比 `unknown` 更需要到期機制**，因為它明確宣告了「會發生」。

### B.6.4 §2.3 三項 close-out 未辦

`UPSTREAM-COVERS` 雙向標記（R44-7）、`unknown` 警示（R44-8）、
A-PV20 登記（R44-9）皆未執行。本包 §2.3 標「時點自定」，
而本輪之指示為「§2.1 三項執行」，故未辦。
其中 A-PV20 影響 §B.2 之 anomaly 統計（見 B.6.1）。

---
---

# 併入：下放包 23 之執行（2026-08-14）

> 對應表註記：`23 -> merged into 17`。
> **§2 一項完成。交付前之執行層作業至此結束。**
> §3（交付後）與 §4（close-out 五項）未執行。

| 停手條件 | 結果 |
|---|---|
| 1 其餘任一行與前輪重量不符 | **未觸發** —— 15 項複核全符，見 §C.1 |
| 2 台帳 FAILED | **未觸發** —— BASELINE 8 OK、DELIVERY 2 OK |

---

## C.1 —— 封存前之最終量測（R45-1）

本包 §2 寫「其餘各行不動（13 項數值已於前輪全項重量且相符）」。
**執行層仍重量一次**，理由是 R45-1 本身：

> 封存前之最終量測不得繼承任何前輪結果，即使前輪剛驗過。

「前輪剛驗過」正是該條所排除的理由。且停手條件 1 要求比對，
比對之一端若取自前輪紀錄，該比對即為自我確認。

**本輪擴為 15 項**（前輪 13 項外加 BLOCKED 列位置與 tc_id 首末）——
兩者皆出現於 annotation 內文而前輪未列入複核表。

| 項 | 值 |
|---|---|
| 交付檔 SHA256 | `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f` |
| 交付檔 bytes | 63,001 |
| 輸入基準 SHA256 | `ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4` |
| 輸入基準 bytes | 59,992 |
| 空白範本 bytes | 65,823 |
| zip 成員 | 48 |
| 差異成員 | `['xl/worksheets/sheet6.xml']` |
| classic DV sheet6 / sheet5 | 3 / 1 |
| x14 DV sheet6 | 2 |
| 資料列 / 列範圍 | 11 / (10, 20) |
| leaf 數 | 10 |
| **BLOCKED 列** | `[18]` |
| **tc_id 首末** | `NR1L-Privacy-001` / `NR1L-Privacy-011` |

**15 項全符，停手條件 1 未觸發。**

---

## C.2 —— tag annotation 定稿全文（供 Pei 直接取用）

唯一改動：

```diff
- Anomalies: 13 RESOLVED, 1 CLOSED, 6 DEFERRED, 0 open PENDING.
+ Anomalies at tag time (2026-08-13): 0 open PENDING.
```

R45-2 之兩項處置在此合流：**加時點限定**使可變計數成為歷史事實
（其後 A-PV20 登記亦不使其變假）；**刪除分布**因
RESOLVED／CLOSED／DEFERRED 是 repo 之狀態快照，
而 `0 open PENDING` 才是交付放行之判準 —— 前者不屬封存範圍。

### 定稿全文

```
FW036 Privacy HMI TC delivery v1

Workbook: FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
          Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
SHA256:   ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f
bytes:    63,001

Input baseline — the prepared workbook this write started from
(DELIVERY.sha256 ENTRY 001):
SHA256:   ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
bytes:    59,992

11 TCs across 10 leaves (SWE1-HMI-PRIVACY_FEATURES-001…010), rows 10-20,
tc ids NR1L-Privacy-001…011 with no gap. Row 18 is a BLOCKED row for -008:
CFTS022-4915173 is performed entirely by the AMP, so it is out of scope for
this ECU and carries [BLOCKED-ECU] in Remarks rather than being omitted
(R34-1 / R34-3).

Structure: 48 zip members in, 48 out — nothing lost, nothing added.
Data validations: classic 3 (sheet6) + 1 (sheet5), x14 2 — all preserved.
Only xl/worksheets/sheet6.xml differs from the input baseline. Header rows
1-9 and all nine non-target sheets verified identical cell by cell.

Structure is judged by member set and data-validation counts, not by byte
count (R37-2). Sizes along the chain, each named to its own file: the blank
template is 65,823, the prepared workbook is 59,992, this delivery is
63,001. Preparation shrank the file by 5,831 bytes while emptying five
cells and writing one short string — the size moved out of all proportion
to the content, which is the point (R42 / R43-5).

lint: PASS — every gate carries both a positive and a negative control.
Excel open confirmed: Pei, 2026-08-13, seven checkpoints.

Anomalies at tag time (2026-08-13): 0 open PENDING.
RD-1 #6-#13 (eight items) not yet sent.
```

**至此 annotation 內已無可變計數。** 逐行檢視：
所有數值皆為被封存物之固有屬性（雜湊、大小、成員數、DV 計數、列數、
tc_id 範圍），或為作成封存時之放行判準並帶時點限定
（`Anomalies at tag time`、`Excel open confirmed: …2026-08-13`），
或為對外部事實之陳述並帶否定時態（`RD-1 … not yet sent`）。

最後一行仍值得注意：`RD-1 #6-#13 (eight items) not yet sent` ——
`eight items` 是計數，但它描述的是**封存時之 RD-1 清單狀態**，
且 `not yet sent` 已隱含時點。若 RD-1 於打 tag 前新增項目，該數會變 ——
**建議打 tag 當下確認一次 `DATA_REQUESTS.md` 之 RD-1 列數**。
未改為時點限定形式，因該行同時承載「尚未送出」這個放行相關事實，
改寫會使其變得累贅；改以此處明示其依賴。

---

## C.3 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

lint 全批：

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
workbook gates measured against FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx (column S = NA, columns T–Z blank — R34-6)

PASS — no findings
```

---

## C.4 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，三項。交付前作業已結束，三項皆不阻塞。**

### C.4.1 `RD-1 … eight items` 為 annotation 內最後一處計數依賴

見 §C.2 末段。它與 anomaly 那行同型，但因兼載放行事實而未改寫。
**打 tag 當下應確認 `DATA_REQUESTS.md` 之 RD-1 列數仍為八。**
現況為 #6–#13 共八項（實測）。

### C.4.2 R45 尚未貼入 `RULINGS.md`

本包 §4.4 將「貼入 R45」列為 **close-out**，而非 §2 之交付前作業。
故本輪未貼。**這意味著本輪之作業依據（R45-1／R45-2）目前只存在於
下放包內，未進 repo 之裁決登記** —— 正是 R39-1／R41-4 所指之同型狀態。

下放包 23 之 `HANDOFF-LINK` 標記為 `merged into 17`，parity 測試因此
PASS；但標記記的是「上繳包在哪」，不是「其裁決是否已登記」。
**兩者是不同的鏈**，目前只有前者有機制。

### C.4.3 close-out 五項未辦，其中兩項互鎖

§4 之五項（R45 貼入、`UPSTREAM-COVERS`＋`pending` 到期互鎖、
`handoff_parity.json`、`unknown` 警示、A-PV20）皆未執行。

其中 R44-7 與 R45-4 已由 R45-4 裁定為**互鎖關係** ——
`UPSTREAM-COVERS` 不再只是雙向驗證，它同時是 `pending` 的到期訊號。
故兩者須一併實作，單獨做其一不會產生到期機制。

本 feature 現有唯一 `pending` 項為 18，其到期時點即交付後之 §3；
屆時人工改標亦可，故不阻塞。

<!-- UPSTREAM-COVERS: 17 18 19 21 22 23 -->
