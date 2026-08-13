# 上繳包 02 — R15 追認 + R16 交付件結構完整性

執行層 → 分析層。2026-08-13。回應 `docs/handoff/02_integrity.md` §5 之六項要求。

**一句話結論**：§3.1–§3.6 全數完成，AMFM v2 已重產且結構無損；
但 §3.4 回溯檢測翻出兩件事 —— **Home 確實受損**（觸發 §4 停手條件 4），
以及 **R16-2 記載的「SXM 尚未寫回」與事實不符，SXM 早已寫回且已受損**。

---

## 0. 停手條件檢查（§4）

| # | 條件 | 結果 |
|---|---|---|
| 1 | `RULINGS.md` 之 R15 / R16 編號已被占用 | ✅ 未占用（現有最高為 R14）。已寫入 |
| 2 | §3.1 探針驗證未達 LOSSLESS | ✅ 未觸發 —— 兩份workbook 皆 LOSSLESS |
| 3 | v2 產出在任一回報項與 v1 不符 | ✅ 未觸發 —— 逐項相符，唯一差異為刻意的日期 |
| 4 | §3.4 發現 Home 受損 | ⛔ **觸發** —— 見 §4.1，執行層只回報不動作 |

**對停手條件 4 的執行範圍解讀（如與分析層原意不符請糾正）**：該條寫的是
「回報後停手，重產與否由 Pei 裁」。執行層讀為「**停 Home 的重產動作**」，
而非「停整個下放包」—— 因為條文本身要求「回報」，而 §3.5 登記與 §3.6
草案正是回報的載體，且兩者都不動任何交付件。故 §3.5 / §3.6 照做，
**Home 一列未改、一次 `--write` 未跑**。

---

## 1. §3.1–§3.6 逐項完成狀態

| 項 | 內容 | 狀態 | 產出 |
|---|---|---|---|
| 3.1 | writer 改 zip 層外科手術 | ✅ 完成 | `backend/xlsx_surgical.py`（新）；`features/amfm/scripts/write_back.py` 改接 |
| 3.1 | 探針對客戶原件 + 空白範本各驗一次 | ✅ 皆 LOSSLESS | 輸出見 §2 |
| 3.2 | 寫回 invariant（ABORT 級） | ✅ 上線 | `xlsx_surgical.verify_structure()` |
| 3.3 | AMFM v2 重產 | ✅ 完成 | `output/v2/…Radio_20260129.xlsx`；比對見 §3 |
| 3.4 | 回溯檢測 Home / SXM | ✅ 完成 | **兩者皆受損**；見 §4 |
| 3.5 | 登記 | ✅ 完成 | 見 §5 清單 |
| 3.6 | canon 條文草案 | ✅ 完成 | `docs/fw036/CANON_DRAFT_r16_delivery_integrity.md` |

### 3.1 的實作取捨（一項需分析層知悉）

`write_back.py` 原本的一行 `wb.save(out)` 沒有改成「另一種存檔」，而是拆成
**openpyxl 算、zip 層寫**：openpyxl 仍負責 `insert_rows`、公式重排、
invariant 計算，`surgical_save()` 只把「與原檔相比改了哪些格」套回原始
sheet XML，其餘 zip 成員逐 byte 複製。

這個切法有一個刻意的限制，寫在程式裡也寫在這裡：**只能在原檔最後一列之後
append，不能在中間插列**。中間插列會讓下方每一列位移，而位移無法在不重建
整份 sheet XML 的前提下正確處理（合併儲存格、DV sqref、shared formula ref
全都會失準）。AMFM 是純 append，所以安全；`patch_sheet_xml()` 遇到中間插列
會直接 `StructureError`，不會默默做錯。**若日後有 feature 需要中間插列
（Home 的 interleaved 重寫就是），這條路徑要重新設計，不能沿用。**

副作用（正面）：未被改動的列連 shared formula group 都原樣保留 —— 因為
openpyxl 讀檔時會把 shared formula 展開成等值字串，diff 比對相等，那些列
就完全不進 patch。v2 的 sheet6 只改了 2,227 格。

---

## 2. §5.2 — 探針兩次驗證輸出（原文）

`features/privacy/scripts/xlsx_roundtrip_probe.py`，已改為呼叫**生產模組**
`backend.xlsx_surgical.surgical_save`，而非自帶一份平行實作。

### 2.1 AMFM 客戶原件

```
workbook : FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS024_Radio_20260129.xlsx
sheet    : 'Test Case Specification&Result' -> xl/worksheets/sheet6.xml
probe cell: AE1 (empty in the source)
baseline : 59 zip members, x14 DV 2 element(s) in 2 group(s), classic DV ['AE10:AE14', 'P10:P167', 'S10:Y229']

--- openpyxl load/save: LOSSY
  x14 DV elements  : 2 -> 0
  x14 DV groups lost: ['Q156 Q147 Q10:Q95', 'Q223:Q242 Q148:Q155 Q96:Q146 Q157:Q205']
  classic DV lost  : none
  zip members lost : ['xl/calcChain.xml', 'xl/comments1.xml', 'xl/diagrams/colors1.xml', 'xl/diagrams/data1.xml', 'xl/diagrams/drawing1.xml', 'xl/diagrams/layout1.xml', 'xl/diagrams/quickStyle1.xml', 'xl/drawings/_rels/drawing7.xml.rels', 'xl/drawings/drawing7.xml', 'xl/drawings/vmlDrawing1.vml', 'xl/media/image2.jpeg', 'xl/printerSettings/printerSettings1.bin', 'xl/printerSettings/printerSettings2.bin', 'xl/printerSettings/printerSettings3.bin', 'xl/printerSettings/printerSettings4.bin', 'xl/printerSettings/printerSettings5.bin', 'xl/printerSettings/printerSettings6.bin', 'xl/printerSettings/printerSettings7.bin', 'xl/sharedStrings.xml', 'xl/worksheets/_rels/sheet8.xml.rels', 'xl/worksheets/_rels/sheet9.xml.rels']
  zip members added: ['xl/comments/comment1.xml', 'xl/drawings/commentsDrawing1.vml', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']

--- zip-level surgical splice: LOSSLESS
  x14 DV elements  : 2 -> 2
  x14 DV groups lost: none
  classic DV lost  : none
  zip members lost : none
  zip members added: none

write landed: AE1 = 'round-trip probe' (OK)

verdict: surgical path is LOSSLESS and the write landed; openpyxl path is LOSSY
```

### 2.2 FW036 空白範本（Privacy `inputs/`）

```
workbook : FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx
sheet    : 'Test Case Specification 測試用例規範' -> xl/worksheets/sheet6.xml
probe cell: AF1 (empty in the source)
baseline : 48 zip members, x14 DV 2 element(s) in 2 group(s), classic DV ['P10:Q11', 'T10:Z11', 'AF10:AF11']

--- openpyxl load/save: LOSSY
  x14 DV elements  : 2 -> 0
  x14 DV groups lost: ['R10', 'R11:R59']
  classic DV lost  : none
  zip members lost : ['xl/calcChain.xml', 'xl/comments1.xml', 'xl/drawings/vmlDrawing1.vml', 'xl/media/image2.jpeg', 'xl/printerSettings/printerSettings1.bin', 'xl/printerSettings/printerSettings2.bin', 'xl/printerSettings/printerSettings3.bin', 'xl/printerSettings/printerSettings4.bin', 'xl/printerSettings/printerSettings5.bin', 'xl/sharedStrings.xml', 'xl/worksheets/_rels/sheet8.xml.rels']
  zip members added: ['xl/comments/comment1.xml', 'xl/drawings/commentsDrawing1.vml', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']

--- zip-level surgical splice: LOSSLESS
  x14 DV elements  : 2 -> 2
  x14 DV groups lost: none
  classic DV lost  : none
  zip members lost : none
  zip members added: none

write landed: AF1 = 'round-trip probe' (OK)

verdict: surgical path is LOSSLESS and the write landed; openpyxl path is LOSSY
```

### 2.3 ⚠️ R16 證據區塊之數字更正

R16 寫「x14 dataValidation（sheet6）: **6** → 0」。實測對不上：

| 量法 | AMFM 客戶原件 sheet6 |
|---|---|
| `<x14:dataValidation>` **元素數** | **2** |
| `<xm:sqref>` 群組數 | 2 |
| sqref 內 **range 總數** | 7 |
| classic `<dataValidation>`（sheet6）| 3 |
| classic `<dataValidation>`（全簿）| 4 |

「6」不等於任一量法。最接近的組合是 2 (x14) + 4 (classic 全簿) = 6，
疑為兩類 DV 相加而標成 x14。

**裁決結論不受影響**：「x14 → 0、交付件結構受損」由 21 lost / 10 added
的成員清單獨立成立，該清單已逐項複現、完全無誤。依 §4.3「不得自行調和」
與 R14-C7 量測口徑紀律，照實回報，`RULINGS.md` 原文未改，
只在其後加一段執行層更正。

---

## 3. §5.3 — AMFM v2 全部回報項，與 v1 逐項並列

產出：`output/v2/FM-WI-FSM-036-A01 …_SWQT_CFTS024_Radio_20260129.xlsx`
（v1 原地保留在 `output/`，未覆蓋、未刪除）

| 回報項 | 客戶原件 | v1 | v2 | 判定 |
|---|---|---|---|---|
| bytes | 136,004 | 171,631 | **153,485** | — |
| zip members | 59 | 48 | **59** | ✅ 與原件相同 |
| 對原件 lost / added | — | 21 / 10 | **0 / 0** | ✅ |
| classic DV / x14 DV | 4 / 2 | 4 / **0** | 4 / **2** | ✅ 完整保留 |
| SHA256 | `987cdead3775…` | `da18b5b0ca9e…` | `0daa6f29cecb…` | — |
| legacy hash（全長）| `30d9e4c0…f30a` | 同左 | **同左** | ✅ 三者一致 |
| 資料列數 | 158 | 301 | **301** | ✅ |
| legacy / regen | 158 / 0 | 158 / 143 | **158 / 143** | ✅ |
| segments | — | LEGACY 10-167, REGEN 168-310 | **同左** | ✅ |
| coverage | — | 102 == 102 exact | **同左** | ✅ |
| placeholders | — | none | **none** | ✅ |
| TC IDs (F) | — | `newR1L-AMFM-001…143` | **同左** | ✅ |
| lint | — | PASS 0 findings | **PASS 0 findings**（143 TCs / 102 leaves / 9 methods）| ✅ |

**legacy hash 全長（R15-4）**：
`30d9e4c0719a29292ff50123ead1003262652fbb8f301e93bf974fd2ee17f30a`
—— 前綴 `30d9e4c0719a2929`、續段 `2ff50123…`。
對 pristine input / v1 / v2 三份各自重算皆相同，且與
`data/legacy_baseline.json` 相符。
**證明範圍（R15-3）**：以相同雜湊定義重算，證「產出未自產生時漂移」，
不證「該定義正確」。

### 3.1 v1 vs v2 逐格內容比對（本包新增之驗證，非 §5 要求）

10 個分頁全部逐格比對：

| 分頁 | cell 差異數 |
|---|---|
| `Test Case Specification&Result` | **0** |
| `ChangeHistory 修訂履歷` | **1** — `D7` `'2026-08-10'` → `'2026-08-13'` |
| 其餘 8 個分頁 | 0 |

唯一差異是 ChangeHistory 的日期，來自 `--date 2026-08-13`（v2 的產製日）。
**TC 內容零差異 —— 本次確實只換了寫回方法，一列 TC 都沒重跑。**

### 3.2 可重現性

同參數連跑兩次，SHA256 皆為 `0daa6f29cecb…`。
`normalize_for_reproducibility()` 保留（zip 時戳歸零 + `docProps/core.xml`
dcterms 固定），該成員因此是 invariant 允許清單裡**唯一**額外項，
在呼叫點明文宣告，不是放寬 invariant。

---

## 4. §5.4 — Home / SXM 回溯檢測完整輸出

### 4.1 Home —— ⛔ **受損**（觸發停手條件 4）

```
source    : …_SWQT_Home_20260720.xlsx  (130,571 B, 52 members)
delivered : …_SWQT_Home_20260720.xlsx  (140,537 B, 48 members)
sheet     : 'Test Case Specification&Result' -> xl/worksheets/sheet6.xml

--- delivered vs customer original: LOSSY
  x14 DV elements  : 0 -> 0
  x14 DV groups lost: none
  classic DV lost  : none
  zip members lost : ['xl/calcChain.xml', 'xl/comments1.xml', 'xl/diagrams/colors1.xml', 'xl/diagrams/data1.xml', 'xl/diagrams/drawing1.xml', 'xl/diagrams/layout1.xml', 'xl/diagrams/quickStyle1.xml', 'xl/drawings/_rels/drawing7.xml.rels', 'xl/drawings/drawing7.xml', 'xl/drawings/vmlDrawing1.vml', 'xl/media/image2.jpeg', 'xl/printerSettings/printerSettings1.bin', 'xl/sharedStrings.xml', 'xl/worksheets/_rels/sheet7.xml.rels']
  zip members added: ['xl/comments/comment1.xml', 'xl/drawings/commentsDrawing1.vml', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']
  classic DV count : 0 -> 0
```

**lost 14 / added 10**，含整組 SmartArt（`xl/diagrams/*`）與列印設定。

**一件必須明說的事**：Home 原件**本來就沒有 x14 dataValidation**（0 → 0），
也沒有任何 classic DV（0 → 0）。也就是說 —— **如果只用 DV 當判準，
Home 會被判為無損**。實際仍失 14 個成員。這是 R16-5 盲區的第二個實例，
而且方向與第一個不同：R14-C1 是「用列內容量結構」，這裡是
「用一個該檔案天生就沒有的特徵量結構」。已寫進 §3.6 canon 草案 rule 5。

**執行層動作：無。** tag `fw036-home-regen-v2` 保留。重產與否由 Pei 裁。
若裁定重產，writer 已就位，成本是一次 `--write`，不需重跑生成 ——
但請注意 §1 那條限制：**Home 是 interleaved 重寫，不是純 append**，
現行外科手術路徑只支援 append，Home 重產前必須先擴充該路徑並重驗。
這點在裁決前就該知道，不宜等到動手才發現。

### 4.2 SXM —— ⚠️ **前提有誤，且已受損**

R16-2 記載「SXM 尚未寫回，攔得住」。**實測不成立**：
`features/sxm/output/` 已有交付件與 `.sha256` 併存，tag `fw036-sxm-v1`
亦已存在。寫回**已經發生**。

```
source    : …_SWQT_SXM_20260810.xlsx  (65,823 B, 48 members)
delivered : …_SWQT_SXM_20260810.xlsx  (148,734 B, 47 members)
sheet     : 'Test Case Specification 測試用例規範' -> xl/worksheets/sheet6.xml

--- delivered vs customer original: LOSSY
  x14 DV elements  : 2 -> 0
  x14 DV groups lost: ['R10', 'R11:R59']
  classic DV lost  : none
  zip members lost : ['xl/calcChain.xml', 'xl/comments1.xml', 'xl/drawings/vmlDrawing1.vml', 'xl/media/image2.jpeg', 'xl/printerSettings/printerSettings1.bin', 'xl/printerSettings/printerSettings2.bin', 'xl/printerSettings/printerSettings3.bin', 'xl/printerSettings/printerSettings4.bin', 'xl/printerSettings/printerSettings5.bin', 'xl/sharedStrings.xml', 'xl/worksheets/_rels/sheet8.xml.rels']
  zip members added: ['xl/comments/comment1.xml', 'xl/drawings/commentsDrawing1.vml', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']
  classic DV count : 3 -> 3
```

**lost 11 / added 10，x14 DV 2 → 0** —— 失去的正是 R 欄「測試用例設計方法」
下拉（`下拉選單!$A$1:$A$9` / `$A$1:$A$11`）。SXM 用的是與 Privacy 同一份
rev C 空白範本，症狀與 Privacy 探針的預測逐項吻合。

§3.4 對 SXM 只要求「確認其範本是否含 x14 DV 並登記」——
答案是**含，且已在交付時失去**。是否比照 AMFM 重產超出本包授權，回 chat。
（SXM 與 AMFM 同為 append 形態，重產不受 §4.1 那條 interleaved 限制。）

### 4.3 Projection 對照組

```
source    : NR1L_GEN1(HDCC)_Ver_20260813.xlsx  (574,700 B, 30 members)
delivered : NR1L_GEN1(HDCC)_Ver_20260813.xlsx  (574,700 B, 30 members)

--- delivered vs customer original: LOSSLESS
  x14 DV elements  : 0 -> 0 ; groups lost: none ; classic DV lost: none
  zip members lost : none ; added: none
```

與 R16 §2 記載一致。**但不得讀成「writer 安全」**，兩個理由缺一不可：
(a) 該簿本無 x14 DV，最顯眼的症狀天然不存在（同 Home 盲區）；
(b) 更關鍵 —— `output/` 與 `inputs/` **位元完全相同**（574,700 = 574,700），
該檔根本沒經過寫回路徑。零差異證明的是「沒被寫過」，不是「寫了沒壞」。

---

## 5. §3.5 登記清單

| 檔案 | 內容 |
|---|---|
| `features/amfm/RULINGS.md` | R15 全文、R16 全文、+ 執行層對 x14 計數之證據更正 |
| `features/amfm/ANOMALIES.md` | **A-AM18** v1 結構缺損（含 §2 全部證據 + v2 對照） |
| `features/home/ANOMALIES.md` | **A-H27** 已交付件缺 14 成員，重產待裁 |
| `features/sxm/ANOMALIES.md` | **A-SX28** 已交付件缺 11 成員 + x14 歸零 + 前提更正 |
| `features/projection/ANOMALIES.md` | **A-PJ-R16** 對照組結果 + 為何不足以證明 writer 安全 |
| `features/privacy/ANOMALIES.md` | **A-PV09** 升格，交叉引用 R16 |
| 五個 `PLAYBOOK.md` | 凍結狀態橫幅（含各 feature 個別狀態） |
| `features/amfm/PLAYBOOK.md` §6 P7 | legacy hash 全長 + R15-3 證明範圍註記（R15-4） |
| `docs/fw036/CANON_DRAFT_r16_delivery_integrity.md` | §3.6 canon 草案（未動 canon 本體） |

新增程式：`backend/xlsx_surgical.py`。
改動程式：`features/amfm/scripts/write_back.py`（emit 路徑）、
`features/privacy/scripts/xlsx_roundtrip_probe.py`（改用生產模組 + `--compare` 模式）。

**未執行**：任何 `git commit` / `git tag`（屬 Pei）；Home 與 SXM 的重產；
canon 本體的修改；凍結的解除。

---

## 6. §5.5 — 為 Pei 準備之 commit message（未執行）

```
fix(writer): emit deliverables by zip-level splice, not openpyxl save

openpyxl's Workbook.save() rebuilds the container instead of writing the
file it read. Measured on our own deliveries: AMFM v1 lost 21 zip members
(SmartArt, printer settings, comment VML, sharedStrings) and both x14
dropdowns; Home lost 14; SXM lost 11. Row values and lint were correct
throughout, which is why it went unseen (R16-5).

- add backend/xlsx_surgical.py: patch only the written sheets' XML, copy
  every other zip member byte-for-byte; ABORT-level structural invariant
  over member set and per-sheet data-validation counts
- write_back.py emits through it; openpyxl stays as the calculation layer
- xlsx_roundtrip_probe.py now exercises the production module and gains a
  --compare mode for retrospective checks (R16-3)
- regenerate AMFM v2: 59/59 zip members, DV 4/2 preserved, TC sheet
  byte-for-byte identical in content to v1, lint green, legacy hash
  30d9e4c0719a29292ff50123ead1003262652fbb8f301e93bf974fd2ee17f30a
- record R15/R16, A-AM18, A-H27, A-SX28, A-PJ-R16; upgrade A-PV09
- draft the canon P7 delivery-integrity clause for sign-off

Home and SXM deliveries are damaged and NOT regenerated here — Tier 2 call.
Note: Home is an interleaved rewrite, so the append-only surgical path must
be extended before it can be regenerated.
```

**建議分兩個 commit**（若 Pei 偏好細粒度）：
第一個只含 `backend/xlsx_surgical.py` + `write_back.py` + probe（程式）；
第二個含全部 `.md` 登記與 canon 草案。v2 產物在 `output/`，
`.gitignore:20` 已排除，不進 commit。

---

## 7. §5.6 — 本包是否仍有該驗而未驗者（獨立判斷）

**有，六項。**

1. **v2 沒有用 Excel 實際開啟驗證過。** 全部驗證都是程式層
   （zip 成員、DV 計數、openpyxl 讀回、逐格比對）。外科手術路徑寫的是
   inline string 與顯式 `<f>` 公式，而原檔第 11–229 列用的是 **shared
   formula**（`<f t="shared" si="0"/>`，master `B11:B229`）；新加的
   B243–B310 是顯式公式且**不在 `calcChain.xml` 內**（該檔被逐 byte 保留）。
   Excel 對「calcChain 與實際公式不同步」通常會靜默重建，但這是推論不是實測。
   **交付前應由人在 Excel 開一次 v2**，確認無「修復」提示、R/P/AE 下拉可用、
   SmartArt 與列印設定在。這件事執行層做不了。

2. **`normalize_for_reproducibility()` 之後沒有再跑一次探針。** invariant
   有重驗（§3.2 的 `verify_structure` 在 normalize 後再跑一次），但完整探針
   沒有。理論上 normalize 只改時戳與 `docProps/core.xml`，不動 sheet XML；
   實務上這是「應該不會」而非「量過」。

3. **外科手術路徑只在 append 形態上驗證過。** Home 的 interleaved 重寫、
   以及任何中間插列的情境，程式會 `StructureError` 擋下 —— 擋得住不等於
   支援得了。若 Pei 裁定重產 Home，這條路徑要先擴充再重驗，
   工作量不小（合併儲存格、DV sqref、shared formula ref 全要隨位移調整）。

4. **`sheet_members()` 的 rels 解析只在這四份檔案上驗過。** 它假設
   `<Relationship>` 是自閉合標籤、`<sheet>` 元素帶 `r:id`。四份都成立，
   但這是 Excel 的產出慣例，不是規格保證。遇到別的產生器可能要放寬。

5. **Privacy 範本的 A-PV07 清除計畫仍未執行、也未在真檔上驗過。**
   §3.6 草案與 A-PV07 都寫了做法，但 Privacy 尚未進 P4，
   「清 5 格值、保留 `s=` 樣式、B 欄公式自動跟隨」只在探針副本上試過一次。

6. **凍結解除的判準沒有被定義。** R16-2 寫解除條件是「§3.1 完成且 §3.2
   invariant 上線」，兩者都已完成 —— 但「完成」由誰認定、認定要看哪些證據，
   條文沒寫。執行層**沒有自行解除凍結**，五個 PLAYBOOK 的橫幅都寫
   「待 Pei 裁示」。若分析層認為本包 §2 的兩份 LOSSLESS 輸出即為解除依據，
   請明文簽一句，否則凍結會一直掛著。

另附一項不屬「未驗」但屬「已知偏差」：v2 的第 243–310 列**沒有儲存格樣式**
（`<row r="243">`，cells 無 `s=`），因為原範本的 template tail 只到第 242 列，
再往下是新建的列。**v1 也是如此**（已逐列比對確認），所以這不是本次
造成的迴歸；但它是一個獨立於 R16 的既有缺陷 —— 交付件下半部 68 列沒有
框線與格式。要不要修屬另一件事，本包不動，僅登記於此。
