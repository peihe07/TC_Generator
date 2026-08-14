# 上繳包 24 — 交付覆核、A-PV21 處置、close-out

執行層 → 分析層。2026-08-14。回應 `docs/handoff/24_closeout.md` §4 之六項。

**§2.1 五項 + §2.2 五項全數完成。四項停手條件皆未觸發。**

| 停手條件 | 結果 |
|---|---|
| 1 改名後 `shasum -c` 非三筆全 OK | **未觸發** —— 三筆全 OK，見 §1.2 |
| 2 互鎖建立後 parity FAIL | **觸發過，已排除** —— 兩項皆為實作問題，見 §3.2 |
| 3 `handoff_parity.json` 與現有標記不一致 | **未觸發** |
| 4 台帳 FAILED | **未觸發** |

---

## 1. §4.1 —— 改名後之 `DELIVERY.sha256` 與 `shasum -c`

### 1.1 全文

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
#   ── 路徑變更 2026-08-14（R46-3，A-PV21）────────────────────────────
#   改名前  …_SWQT_Privacy_20260813.xlsx
#   改名後  …_SWQT_Privacy_20260813_prepared.xlsx
#   SHA256  ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
#           （**不變** —— 只改檔名，內容未動）
#   理由    交付件採 R40-1(b) 之命名 `…_SWQT_Privacy_20260813.xlsx` 後，
#           本檔與其 basename 相同而內容不同（A-PV21）。本檔為準備中間檔、
#           非交付件，改名成本最低；撞名之實害是「有人在 output/ 找交付件，
#           拿到沒有 TC 的那一份」。
#   上一行之雜湊行**保留不刪**（append-only，R27-2）：其路徑已不存在，
#           `--ignore-missing` 會靜默略過。保留是為了讓改名這件事在台帳上
#           留下痕跡 —— 刪掉它會使改名看起來從未發生（R41-4：紀錄之缺口
#           應被標記，不應被填補）。下一行為改名後之現行雜湊行。
ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4  output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_prepared.xlsx
#   STATUS: 準備工作簿，已改名為 _prepared；為 ENTRY 002 之輸入基準 (R46-3, 2026-08-14)
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
#
# ENTRY 003 — 2026-08-14 — **已交付**
#   交付路徑  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/
#             ASW-R2/Privacy Mode/
#   交付檔名  FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
#             Specification & Result_SWQT_Privacy_20260813.xlsx
#             （去 `_regen-v1`，與 AMFM／SXM 命名一致 —— R40-1(b)）
#   bytes     63,001
#   交付日期  2026-08-14
#   內容      **內容同 ENTRY 002，僅檔名與位置不同。**
#             SHA256 與 ENTRY 002 逐字元相符（R40-1(d) 實測，非推定）；
#             另複驗 zip 成員 48、sheet6 DV classic 3 / x14 2 —— 皆相同。
#   tag       fw036-privacy-v1（指向 commit 3b54a40）
#   ⚠️ 同名不同容  本檔之 basename 與 ENTRY 001 相同
#             （`…_SWQT_Privacy_20260813.xlsx`）而內容不同：
#             ENTRY 001 = ed741d8d… / 59,992 B（準備工作簿，於 output/）
#             ENTRY 003 = ad595ed0… / 63,001 B（交付件，於 10_Reviewing/）
#             以 basename 索引者會取得兩個候選。依 R15-5 一律以 hash 認定。
#             登記為 A-PV21。
#   路徑欄    本條之雜湊行指向**交付副本本身**（客戶樹之絕對路徑），
#             不指向 repo 內之 ENTRY 002 副本。理由：若指向後者，
#             本行與 ENTRY 002 之行完全相同，`shasum -c` 會驗兩次同一個檔 ——
#             一條**不可能獨立失敗**的檢查行，等於沒有（R18-4 / R34-5）。
#             ENTRY 003 存在的目的正是驗交付出去的那一份。
#             客戶樹不可及時由 --ignore-missing 靜默略過（R27-1）。
ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813.xlsx
#   STATUS: 已交付至 10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/ (R40-1, 2026-08-14)
```

### 1.2 `shasum -c` 輸出

```
$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
output/…_Privacy_20260813_prepared.xlsx: OK
output/…_regen-v1.xlsx: OK
…客戶樹/…_Privacy_20260813.xlsx: OK
exit=0
```

**三筆全 OK，停手條件 1 未觸發。**

### 1.3 兩項處置說明

**加註落在 ENTRY 001 區塊內，而非檔尾。** R39-5 要求「每一次加註之末行須為
狀態行」；若把改名註記接在檔尾，它會落入 ENTRY 003 之區塊，
使 ENTRY 003 之末行不再是其 STATUS，`ledger-status-last` 立即 FAIL。
故註記併入 ENTRY 001 區塊，該區塊現為：
敘述 → 舊雜湊行 → 舊 STATUS → 改名註記 → 新雜湊行 → 新 STATUS。

**舊雜湊行保留不刪。** 其路徑已不存在，`--ignore-missing` 靜默略過。
保留是為了讓改名在台帳上留下痕跡 —— 刪掉會使改名看起來從未發生
（R41-4：紀錄之缺口應被標記，不應被填補）。

---

## 2. §4.2 —— A-PV21 條目全文（主述依 R46-4）

```markdown
## A-PV21 — 為外部素材所立之規則未回頭套用於自有工具 — **RESOLVED（R46-3 / R46-4，2026-08-14）**

> **主述依 R46-4 更正**：本條之核心**不是命名衝突**，而是
> **R15-5（同名檔一律以 hash 認定）係為外部素材而立，未回頭套用於本 repo
> 之自有工具** —— 基準稽核腳本正是 basename 索引。命名衝突是其表徵。
>
> §5a：**對外部素材所立之規則，須逐條檢查是否同樣適用於自有工具與自有
> 產物**；「這條是給上游的」不構成豁免。判準：該規則所防範之失效模式，
> 在自有側是否同樣可能發生。

**表徵**（交付後實測，2026-08-14）：

| 檔案 | 位置 | SHA256 | bytes |
|---|---|---|---|
| `…_SWQT_Privacy_20260813.xlsx` | `features/privacy/output/`（ENTRY 001，準備工作簿）| `ed741d8d…` | 59,992 |
| `…_SWQT_Privacy_20260813.xlsx` | `10_Reviewing/…/Privacy Mode/`（ENTRY 003，**交付件**）| `ad595ed0…` | 63,001 |

**basename 完全相同，內容不同。**

**成因不是疏失，是規則之必然後果。** R40-1 為使交付檔名與 AMFM／SXM 一致
而去掉 `_regen-v1`，同時 R40-1(a) 令 `output/` 內之準備工作簿維持原名
`…_Privacy_20260813.xlsx`。兩項規則各自正確，合起來即產生同名不同容。

**這正是 A-PV04 之型**（`VF651_V2_R2.docx` 七路徑五內容），而該案之教訓
已成 **R15-5：同名檔一律以 hash 認定**。機制上已有防護：

- `DELIVERY.sha256` 三筆各記全長 SHA256，ENTRY 003 明文載
  「內容同 ENTRY 002，僅檔名與位置不同」並附同名警示
- ENTRY 003 之雜湊行指向交付副本之**絕對路徑**，與 ENTRY 001 之
  `output/…` 相對路徑不衝突，`shasum -c` 三筆各自獨立驗證

**殘餘風險**：以 **basename 索引**之工具會取得兩個候選。
本 repo 之基準稽核腳本（下放包 01 §2 / 07）正是 basename 索引 ——
日後若對 `10_Reviewing/` 樹做同型稽核，`…_Privacy_20260813.xlsx`
會同時命中準備工作簿與交付件。

**處置 —— Pei 簽署選項 A（R46-3），已執行**：

| 項 | 結果 |
|---|---|
| (a) `output/` 內 ENTRY 001 改名為 `…_SWQT_Privacy_20260813_prepared.xlsx` | ✅ SHA256 `ed741d8d…` **未變**（只改檔名）|
| (b) `DELIVERY.sha256` 追加路徑變更註記（append，不改寫既有欄位）| ✅ 含改名前後檔名、SHA256、裁決編號、日期，末行為 `STATUS:`（R39-5）|
| (c) 改名後 `shasum -a 256 -c` 三筆全 OK | ✅ 停手條件 1 未觸發 |

**舊路徑之雜湊行保留不刪**：其路徑已不存在，`--ignore-missing` 靜默略過。
保留是為了讓改名在台帳上留下痕跡 —— 刪掉會使改名看起來從未發生
（R41-4：紀錄之缺口應被標記，不應被填補）。

**稽核腳本之設計維持不變**（R46-4）：basename 檢索 + hash 認定。
該設計**有效** —— A-PV04（`VF651_V2_R2.docx` 七路徑五內容）正是以此抓到。
須注意的是**不得日後被「簡化」為純 basename 比對**；理由已記於本條與
`docs/upstream/01_carryover.md` §2.1 之量測條件。

**相關**：`RULINGS.md` R40-1 / R15-5；A-PV04；`DELIVERY.sha256` ENTRY 001／003。
```

**主述已由「命名衝突」改為「規則未回頭套用於自身工具」。**
這個改寫不是措辭調整：命名衝突是這一次的表徵，而
「為外部素材立的規則沒回頭檢查自有側」是**會再發生的那一件事**。
A-PV20（AMFM 之 parity 缺口）屬同一族 —— 兩者都是「機制只裝在一邊」。

---

## 3. §4.3 —— `UPSTREAM-COVERS` + `pending` 互鎖之雙對照

### 3.1 三項新 gate

| gate | 內容 |
|---|---|
| `test_link_and_covers_agree` | **雙向**：handoff 宣告 `merged into NN` 而 upstream NN 未列該包 → FAIL；upstream 宣告涵蓋某包而該包無 `HANDOFF-LINK` → FAIL |
| `test_pending_expires_when_its_upstream_claims_it` | **到期互鎖**：某包標 `pending:NN` 而 upstream NN 已宣告涵蓋它 → FAIL，訊息「應改為 merged into」|
| `test_unknown_markers_are_reported` | **警示不 FAIL**（R44-8）：列出所有 `unknown`，要求上繳包載明其認定障礙 |

**到期訊號來自標的自身**，非計時或人工提醒（R45-4）——
upstream 一旦宣告涵蓋，該 `pending` 即為過期。

### 3.2 ⚠️ 停手條件 2 觸發過兩次，兩次皆為實作問題

依 R46-6 之預設歸因（gate FAIL 應先假定實作把規則讀寬了），逐項查證：

**第一次 —— upstream/17 之標記取自散文。**
互鎖建立後報「17 declares upstream:17 but upstream 17 lists ['05','06','07']」。
查證：upstream/17 §A.7.1 有一句

> …例如 `<!-- UPSTREAM-COVERS: 05 06 07 -->`），本輪未做。

那是我**用來說明格式的舉例**，被解析成真標記。且自動回填腳本因偵測到
「已有 UPSTREAM-COVERS」而跳過 17，於是 17 從未拿到真標記。

**這是本輪最值得記的一個 —— 格式的「說明」被當成格式的「使用」。**
與 ENTRY 003 內文提到「ENTRY 001 = …」被當成新條目起始同型，
但更隱蔽：那次是巧合撞上樣式，這次是**文件在解釋自己的格式**。

處置：兩個樣式（`HANDOFF-LINK`／`UPSTREAM-COVERS`）皆**錨定整行**
（`^\s*<!-- … -->\s*$`）。宣告獨立成行，提及則嵌在句子裡 ——
錨定整行即可分離兩者。標準未動。

**第二次 —— `24: declares upstream:24 but docs/upstream/24_*.md does not exist`。**
這是**正確的 FAIL**：本檔（upstream/24）當時尚未寫。寫完即消失。
它證明 `upstream:<NN>` 之解析確實會驗證目標存在。

### 3.3 雙對照現況

```
3 failed, 9 passed in 0.12s
```

負向對照三項（`pending` 合成案例、`no-upstream-required`、白名單類）皆 PASS；
陽性對照兩項（缺標記、指向不存在之上繳包）皆 FAIL 觸發。

**`pending` 之負向對照已改用合成 fixture**（R46-5）——
先前版本把「下放包 18 是 pending」寫死，18 一改標
`merged into 17`，對照即失去受測對象：**控制組被綁在過渡狀態上，
正確的轉換反而讓它 FAIL**。

---

## 4. §4.4 —— `handoff_parity.json` 全文

```json
{
 "_doc": "R45-3 —— handoff／upstream 對應表之受版控載體。先前此表只存在於上繳包之表格中，而 `20 -> chat-direct:R42` 這類條目**描述的正是「沒有下放包」**，卻只能寄生於下放包檔案 —— 標記之載體不得是其所描述之對象。故改為獨立資料檔。`tests/test_privacy_handoff_parity.py` 讀本檔並與實際檔案雙向比對：檔案有而表無 → FAIL；表有而檔無且狀態非 chat-direct → FAIL；chat-direct 項豁免檔案存在檢查。",
 "_status_values": {
  "upstream:<NN>": "本包產出自己的上繳包",
  "merged into <NN>": "上繳併入他包",
  "pending:<NN>": "已宣告落點，尚未執行（可認定之未完成態，R44-2）",
  "chat-direct:<裁決編號>": "該輪由 chat 直下、未產下放包（R44-3）",
  "no-upstream-required": "設計上不要求上繳包",
  "no-upstream-produced": "應產而未產（缺口，照實標，R41-4）"
 },
 "packages": [
  {
   "nn": "00",
   "status": "upstream:00",
   "handoff": "00_bootstrap.md"
  },
  {
   "nn": "01",
   "status": "upstream:01",
   "handoff": "01_carryover.md"
  },
  {
   "nn": "02",
   "status": "upstream:02",
   "handoff": "02_template_rulings.md"
  },
  {
   "nn": "03",
   "status": "upstream:03",
   "handoff": "03_platform_baseline.md"
  },
  {
   "nn": "04",
   "status": "upstream:04",
   "handoff": "04_framework.md"
  },
  {
   "nn": "05",
   "status": "merged into 07",
   "handoff": "05_output_location.md"
  },
  {
   "nn": "06",
   "status": "merged into 07",
   "handoff": "06_ledger_semantics.md"
  },
  {
   "nn": "07",
   "status": "upstream:07",
   "handoff": "07_profile_approval.md"
  },
  {
   "nn": "08",
   "status": "no-upstream-produced",
   "handoff": "08_gate2_swap.md"
  },
  {
   "nn": "09",
   "status": "upstream:09",
   "handoff": "09_b1_pilot.md"
  },
  {
   "nn": "10",
   "status": "no-upstream-required",
   "handoff": "10_b1_review.md"
  },
  {
   "nn": "11",
   "status": "upstream:11",
   "handoff": "11_p6_p7_b2.md"
  },
  {
   "nn": "12",
   "status": "upstream:12",
   "handoff": "12_b2_review.md"
  },
  {
   "nn": "13",
   "status": "upstream:13",
   "handoff": "13_traceback.md"
  },
  {
   "nn": "14",
   "status": "upstream:14",
   "handoff": "14_writeback.md"
  },
  {
   "nn": "15",
   "status": "merged into 16",
   "handoff": "15_closeout.md"
  },
  {
   "nn": "16",
   "status": "upstream:16",
   "handoff": "16_p7_done.md"
  },
  {
   "nn": "17",
   "status": "upstream:17",
   "handoff": "17_predelivery.md"
  },
  {
   "nn": "18",
   "status": "merged into 17",
   "handoff": "18_delivery_naming.md"
  },
  {
   "nn": "19",
   "status": "merged into 17",
   "handoff": "19_parity.md"
  },
  {
   "nn": "20",
   "status": "chat-direct:R42",
   "handoff": null,
   "note": "該輪由 chat 直下（bytes 歸屬錯誤之更正），未產下放包；編號跳過為分析層疏失（R44-3）。"
  },
  {
   "nn": "21",
   "status": "merged into 17",
   "handoff": "21_release.md"
  },
  {
   "nn": "22",
   "status": "merged into 17",
   "handoff": "22_final.md"
  },
  {
   "nn": "23",
   "status": "merged into 17",
   "handoff": "23_annotation_final.md"
  },
  {
   "nn": "24",
   "status": "upstream:24",
   "handoff": "24_closeout.md"
  }
 ]
}
```

**25 筆**：24 個實際下放包 + `20 -> chat-direct:R42`（無檔）。

新 gate `test_parity_table_and_files_agree` 雙向比對：
檔案有而表無 → FAIL；表有而檔無且狀態非 `chat-direct` → FAIL；
`chat-direct` 項豁免檔案存在檢查。

**這解決了 §B.3.1 所指之寄生問題**：`20` 之標記先前只活在上繳包之表格裡，
parity 測試看不到它；現在它是資料檔中的一筆，受測且受版控。

---

## 5. §4.5 —— commit message 草案

備於 `scratchpad/privacy-closeout-commit.txt`，**未執行**（git 屬 Tier 3）。
首行：

```
docs(privacy): close out delivery — rename prepared workbook, wire parity gates
```

body 四段：A-PV21 之處置與其真正內容、台帳三項改動、
測試三項新 gate 與 `handoff_parity.json`、以及本輪五次解析修正之分布。

---

## 6. §4.6 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。**

### 6.1 `UPSTREAM-COVERS` 之內容正確性仍未驗證

新 gate 驗的是**兩側標記互指一致**，不驗**上繳包真的涵蓋了那些包**。
upstream/07 標 `05 06 07`，測試只確認 05／06 之 `HANDOFF-LINK` 指向 07；
**它不讀 upstream/07 的內文去確認 05／06 的作業結果真的在裡面。**

這比先前好（單向 → 雙向），但仍是「宣告互指」而非「內容涵蓋」。
要再進一步需要上繳包內有可解析的分節標記，成本高於收益 —— 登記，未做。

### 6.2 `handoff_parity.json` 與 `HANDOFF-LINK` 標記重複記載同一事實

兩者現在必須手動保持同步（gate 會抓不一致，但不會自動修）。
新增下放包時要改兩處。**單一事實記兩份**是已知的維護負擔 ——
可考慮讓標記成為唯一來源、JSON 由腳本生成，但那會使
`chat-direct` 之無檔項再度無處可存。目前之取捨是刻意的，記此以免日後被當成疏忽。

### 6.3 五次解析修正之後，尚無「格式說明 vs 格式使用」之通則

本輪 §3.2 第一次那個問題（文件解釋自己的格式而被解析）
**目前只在這兩個標記上修好了**。`DELIVERY.sha256` 之 `STATUS:` 行、
`lint_tcs.py` 之 marker 表、`spec_ref_reviewed.json` 皆有同樣風險 ——
若日後有文件引用其格式作為說明，同樣會被誤讀。
錨定整行是有效解法，但**尚未推及其餘樣式**。

### 6.4 A-PV20 所指之 AMFM 缺口，其建議順序未經驗證

條目內建議「先補標記與 `handoff_parity.json`，再擴充測試涵蓋範圍」，
理由是反過來會先得到一堆 FAIL 而無從逐項認定。
**這是推論，未實測** —— AMFM 之往返檔案我沒有讀過，
不知其標記可否逐一認定。重啟時應先抽驗幾份再決定順序。

<!-- UPSTREAM-COVERS: 24 -->
