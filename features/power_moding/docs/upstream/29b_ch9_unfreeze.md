# 上繳包 29b —— ch 9 限縮解凍、章 9 × 矩陣全對照（與 29 同輪）

- 日期：2026-08-25
- 下放包：[handoff/29b_ch9_unfreeze.md](../handoff/29b_ch9_unfreeze.md)
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH111／R-PMH112 **2/2 逐字相符**，命中數各 1 |
| **8 章 9 × 矩陣全對照** | **⚠ 牴觸 2 列（`r31`／`r32`）—— 停止條件 10 觸發** |
| **9 batch 3 之產出** | **未執行** —— 下放包步驟 8 逐字令「發現牴觸即停並上呈」 |
| 10 `DR-PMH8` 之更正句 | 已落檔，新 SHA256 `162d551eb2861d59`，狀態維持 `DRAFT` |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH111 | ch 9 限縮解凍 | 690 | `94bdfb0c9888cb88` | `94bdfb0c9888cb88` | 1 | ✅ |
| R-PMH112 | 對上游陳述之更正義務 | 439 | `97b33607dd29c166` | `97b33607dd29c166` | 1 | ✅ |

---

## 2. 步驟 8 —— 章 9 × State Matrix 之全對照（**該對照因凍結而從未做**）

**章 9 之權威文本為 SYS1 之 9.1（R-PMH75）**，其內容為 `PM1)`：
IGN OFF 時之 popup 群（FOTA／FOTA via Wi-Fi／XEV key-off）及其 stay-awake 時序。
**p9 之能力矩陣不入本對照**（其來源未明，A-PMH18）。

### 2.1 範圍向：章 9 之關鍵名詞於矩陣之命中 —— **2/20**

```
    0  FOTA            0  Wi-Fi              0  Wi-fi
    0  Charge Now      0  stay awake         0  IGN OFF
    0  Power Accessory Delay                 0  popup
    0  popups          0  Preconditioning    0  XEV
    0  2.5 minutes     0  10 minutes         0  60
    0  priority        0  dismiss            0  update
    3  Radio Off Delay                      12  Radio off Delay
```

**命中之二者皆為 `Radio off Delay`，而 `PM1)` 所用之詞為 `Power Accessory Delay`
（矩陣全簿 0 命中）。** 此即 **A-PMH24** 之由來（見 §4）。

> **A-PMH18 之原判定（二矩陣主題不同）因而再獲一次獨立量測之支持。**
> ⚠ **惟字面比對之限度已具名**（`LIMITS`）：0 命中為 `未對照` 之**支持證據**，非其證明。

### 2.2 逐列對照 —— **30 列全具名，未具名 0**

**牴觸 2／印證 0／未對照 24／待定義 4**

| 列 | 記法 | 謂詞 |
|---|---|---|
| [區塊 r1] r6 | **待定義** | **pop-up 是否顯示／`VP` 之電源狀態** vs PM1 之 IGN OFF popup 群 |
| [區塊 r1] r7 | 未對照 | 門開啟之後果（事件忽略／電源鈕狀態）vs IGN OFF 之 popup 時序 |
| [區塊 r1] r8 | 未對照 | 門關閉之後果 vs IGN OFF 之 popup 時序 |
| [區塊 r1] r9 | 未對照 | 來電 → 電源開啟 vs IGN OFF 之 popup 時序 |
| [區塊 r1] r10 | 未對照 | 插入 Projection → 電源維持關閉 vs PM1 |
| [區塊 r1] r11 | 未對照 | VR 長按（無 Projection）→ 電源維持關閉 vs PM1 |
| [區塊 r1] r12 | 未對照 | VR 長按（Projection 中）→ 電源開啟 vs PM1 |
| [區塊 r1] r13 | 未對照 | 通話結束 → 回到 Power OFF state vs PM1 |
| [區塊 r1] r14 | 未對照 | Projection 通話結束 vs PM1 |
| [區塊 r1] r15 | **待定義** | **IGN OFF（key-off）時延遲參數為 0 → 顯示器是否關閉** |
| [區塊 r1] r16 | 未對照 | SRT／Off Road+ 硬鍵 → 電源喚醒並靜音 vs PM1 |
| [區塊 r19] r24 | **待定義** | key-off 狀態下按 ON/OFF 鍵 → `VP` 是否開啟 |
| [區塊 r19] r25 | **待定義** | key-off 狀態下門開啟 → `VP` 是否關閉 |
| [區塊 r19] r26 | 未對照 | 來電 → head unit 維持開啟至計時結束 vs PM1 之為 popup 而 stay awake |
| [區塊 r19] r27 | 未對照 | 插入 Projection → head unit 維持關閉 vs PM1 |
| [區塊 r19] r28 | 未對照 | VR 長按（無 Projection）→ head unit 維持關閉 vs PM1 |
| [區塊 r19] r29 | 未對照 | VR 長按（Projection 中）→ head unit 維持關閉 vs PM1 |
| [區塊 r19] r30 | 未對照 | key-off 狀態下門關閉 → 事件忽略 vs PM1 |
| [區塊 r19] r31 | **牴觸** | **key-off 狀態下延遲參數為 0 → head unit 是否關閉** |
| [區塊 r19] r32 | **牴觸** | **key-off 狀態下 Projection 通話結束 → head unit 是否關閉** |
| [區塊 r19] r33 | 未對照 | key-on → 回復 `VP` 之最後狀態 vs PM1 |
| [區塊 r37] r40 | 未對照 | key-on 且非倒車時按 ON/OFF 鍵 vs PM1 |
| [區塊 r37] r41 | 未對照 | key-on 且非倒車時之來電 vs PM1 |
| [區塊 r37] r42 | 未對照 | 排入 R 檔 → 顯示倒車影像 vs PM1 |
| [區塊 r37] r43 | 未對照 | 退出 R 檔 vs PM1 |
| [區塊 r37] r44 | 未對照 | Screen Off 鍵 vs PM1 |
| [區塊 r37] r45 | 未對照 | Mute 鍵 vs PM1 |
| [區塊 r37] r46 | 未對照 | Headunit Mode 鍵 vs PM1 |
| [區塊 r37] r47 | 未對照 | 經 VR 變更 Headunit Mode vs PM1 |
| [區塊 r37] r48 | 未對照 | HVAC 硬控調整 → popup vs PM1 之 IGN OFF popup 群 |

### 2.3 ⚠ 兩處牴觸（**未自行調和，依 R-PMH79 上呈**）

| 列 | 逐字 | 與 `PM1)` 何處相反 |
|---|---|---|
| **`r31`（Call Ended）** | `End Call but: If Radio off Delay = 0 or Radio off Delay timer expired, HU OFF`；`End Call, HU OFF` | `PM1)` 令 head unit 於 IGN OFF 且**有 popup 待顯示**時 `stay awake`（至多 2.5 分鐘） |
| **`r32`（Projection call ends）** | `End Projection Call and HU OFF` … 同上條件 | 同上；**其事件為 Projection 通話之結束，非一般通話** —— 依 R-PMH98／R-PMH100 逐列判定，不合併 |

**其主語為 `HU`（head unit）而非 `VP`** —— 故**不受 `DR-PMH7` 之未定義所阻**，
此二列之判定**已作成**，非 `待定義`。

**條件互斥未證**（R-PMH84）：本列之條件為「通話結束」，`PM1)` 之條件為「有 popup 待顯示」——
**二者可同時成立**（使用者於 key-off 後結束通話，而 FOTA popup 待顯示），**素材未載何者優先**。

### 2.4 四列 `待定義` 之理由

`r6`／`r15`／`r24`／`r25` —— 其值皆由 **`VP`** 承載，而 `VP` 於規格全 11 頁 0 命中
（A-PMH20／`DR-PMH7` Q1）。依 **R-PMH85(c)** 於 `ANSWERED` 前不得轉為其他記法。

**`r15` 另受 A-PMH24 所阻** —— 即使 `VP` 之定義到達，`Radio Off Delay` 與
`Power Accessory Delay` 是否同一參數仍未定，該列仍無法判定。
**⚠ 若二問之答覆皆為肯定，`r15` 即為第三處牴觸** —— 該條件式已於其 `VERDICT` 內具名。

### 2.5 **印證 0** —— 此事本身須被記下

30 列中**無一列印證 `PM1)`**。矩陣全簿不含 `FOTA`／`Wi-Fi`／`Charge Now`／
`stay awake`／`IGN OFF`／`XEV`／`Preconditioning` 之任一詞。
**這與 `DR-PMH5` 所主張者一致**：該 Excel 與 p9／9.1 為不同主題之文件。

---

## 3. 步驟 9（batch 3）—— **未執行，停止條件 10 觸發**

下放包步驟 8 逐字：**「發現牴觸即停並上呈。」** 停止條件 10 逐字：
**「步驟 8 之 ch 9 × 矩陣對照發現牴觸」。**

**故 `Power Transitions` 之 7 leaf 未產出任何 TC。**

### 3.1 字面與目的（R-PMH77(c)）

| | 讀法 |
|---|---|
| **字面** | 發現牴觸即停 —— **步驟 9 不執行** |
| **目的** | 牴觸不得被執行層靜默調和；產出不得建立在未裁定之衝突上 |

**本包二者同向** —— `r31`／`r32` 之牴觸**正落在 batch 3 之射程內**
（`PM1)` 之 stay-awake 行為即 `-018-01`～`-05` 之標的），
**其產出若照常進行，等於以某一讀法作成 TC 而未經裁定。故我停在此處。**

### 3.2 我看見而未執行之解法

於 batch 3 之相關 TC 加**事件層限定**「無通話進行中／無 Projection 通話結束」，
`r31`／`r32` 即互斥可證。**該處置須 R-PMH87 型之授權，本包無之。**

### 3.3 已完成之準備（不含任何 TC）

- 章 9 之權威文本已確認為 **SYS1 之 9.1**（R-PMH75），其逐字已取得；
- batch 3 之範圍已確認為 **7 leaf**（`-002` / 7.1.1、`-018-01`～`-05` / 9.1、`-023` / 10.5），
  **非只 ch 9 之 5 leaf**；
- **R-PMH111 之判別法尚未逐條套用** —— 其須對「每一條 TC 之每一斷言」為之，
  **而 TC 尚未產出，故無可套用之對象**。停止條件 11 因而**不適用**（非「未觸發」）。

---

## 4. A-PMH24（新）—— 延遲參數之名稱歧義

`Power Accessory Delay`（規格 9.1）與 `Radio Off Delay`（矩陣 `r15`／`r31`／`r32`）
**從未同時出現於任一份文件**，其關係無一處定義。

**未開新 DR** —— 我判其與 `DR-PMH5` 之 (1)(2) 同源（皆為「矩陣與規格是否談同一件事」），
併入該 DR 之答覆時一併釐清為宜。**⚠ 該判斷未經裁定。**

---

## 5. 步驟 10 —— `DR-PMH8` 之更正句（R-PMH112）

首段已加入 29b §三之逐字更正句：我方於 `DR-PMH5` 中所稱「已暫停 section 9 之
TC 撰寫」因 R-PMH111 而不再成立，**已恢復撰寫**，並聲明將保留任何倚賴 p9 矩陣之個別 TC。

- 新全文 SHA256（前 16）：**`162d551eb2861d59`**（原 `b4aa530edf320216` 已被取代）
- **狀態維持 `DRAFT`，`SENT` 欄留空** —— 其發出仍屬 Pei（R-PMH83）
- 三問（一日起算點／設定路徑／`Sounds will sync` 是否涵蓋告別音）未改一字

> ⚠ **更正尚未送達上游** —— 在 `DR-PMH8` 發出之前，
> **上游所知之我方狀態仍是「section 9 已暫停」，而實際上其已解凍。**
> 此一不符**現在存在**，其存續時間等於 `DR-PMH8` 之延遲時間。

---

## 6. 檢查總表（程式產生，R-PMH92）

`matrix_vs_chapter.py 9` 已納入總表（**既有檢查對新資料之適用，R-PMH107**）：

```
| `matrix_vs_chapter.py 9` | ✅ | 1 | 1 | **PASS** | 含**牴觸 2**（`r31`／`r32` × `PM1)`）→ 退出碼 1 為設計 |
```

其餘：lint batch01／batch02 **32/32**、`--limit-must-hit` **19/19**、
`verdict_form` **0 failure**、`matrix_vs_chapter --must-hit` **PASS**、
**未註冊 must-hit 而標「未實測」者 = 4**（不變）。
**新增檢查程式 0、檢查項 0。**

---

## 7. 未結 DR —— **4 筆**

| DR | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|
| `DR-PMH5` | `SENT` | 2026-08-25 | **不再阻斷整組**（R-PMH111 限縮）；其 (1)(2) 仍待答 |
| `DR-PMH6` | `SENT` | 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` | 2026-08-25 | **矩陣四列之判定**（`r6`／`r15`／`r24`／`r25`） |
| `DR-PMH8` | **`DRAFT`** | （待填） | 否 —— **惟其載有 R-PMH112 之更正，延遲即不符延續** |

---

## 8. 本包是否仍有該驗而未驗者 —— **有**

1. **batch 3 未產出，而 ch 9 已解凍。** 解凍之目的是讓 5 leaf 動起來，
   **而本包之結果是它們仍然沒動** —— 只是理由由「p9 無來源」換成「矩陣有牴觸」。
   **這是本包最要緊的一項：需要的是一句授權，不是更多分析。**
2. **`r31`／`r32` 之牴觸我判為「不受 `VP` 未定義所阻」，因其主語為 `HU`。**
   該判斷倚賴「`HU` 與 `VP` 為不同之物」——**而若 `VP` 就是 `HU`，四列 `待定義` 之
   其中若干亦應改判牴觸。** 兩種讀法我都未採，只把分界具名於此。
3. **`r15` 之條件式判定未被任何檢查所承載。** 其「若二問皆為肯定即為牴觸」寫在
   `VERDICT` 之依據文字裡，**而依據文字不是機器可判之物** ——
   `DR-PMH5`／`DR-PMH7` 答覆到達時，**沒有任何東西會提醒我們回來改它**。
   （擴充檢查即新增檢查項，R-PMH104 之凍結；**我停在這裡並具名。**）
4. **章 9 之對照只做了矩陣側。** R-PMH98 之規格側全枚舉（235 行）於章 9 未做，
   其與 ch 7／8 之情形相同（KNOWN-INCOMPLETE 三）。
5. **A-PMH24 未開 DR 為我之判斷**，未經裁定（§4）。
6. **`-002`（7.1.1）與 `-023`（10.5）未受本次對照檢驗** —— 本次只對照章 9，
   而 batch 3 之範圍含此二 leaf。**其各自之章（7／10）之對照早已完成，
   惟「該二 leaf 之斷言」尚未存在，故無可掃描者。**

---

## 9. 建議之 commit（**未執行**）

```
feat(power_moding): package 29b — ch9 conditional unfreeze, ch9 x matrix comparison (2 conflicts), DR-PMH8 correction
```

pathspec（**9 路徑**）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/29b_ch9_unfreeze.md
features/power_moding/docs/upstream/29b_ch9_unfreeze.md
features/power_moding/scripts/check_table.py
features/power_moding/scripts/matrix_vs_chapter.py
```

### 9.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** —— `workbook_state = BLANK` 未變 |
| **batch 3** | **未產出** —— 停止條件 10 觸發（§3） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT` |
| 新增檢查程式／檢查項 | **0／0** |
| 他 feature／`docs/runtime/`／`scripts/new_feature.py` | **未觸** |
