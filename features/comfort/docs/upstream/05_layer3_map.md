# 上繳包 05 — R-C15~R-C17 落實 ＋ DR #8 DEFERRED ＋ Layer 3 map

執行層 → 分析層。2026-08-14。回應下放包 `09_upstream04_review.md` §6
與 `10_phase3_start.md` §4。

**結論：兩包之作業全部完成。Layer 3 map 三個 assertion 全 PASS。**
未決定 Layer 2、未寫 profile、未產 TC、`DECISIONS.md` 未簽署。

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **下放包 09 之六項作業先前未執行** —— 我上一輪只收到 07／08。本包一併補做（R-C15／R-C16 貼入、TSV `disposition` 欄、`recon.py` fallback、DR #10 訂正）。10 §4 已把 R-C16 當現行條文使用，若不補做，本包會建立在未落地的條文上 |
| **乙** | **Layer 3 map 建立時撞見兩處 spec 內部標籤問題**，皆與 Part N 之切分直接相關，登記 **A-CF13**：`C16.)` 被 ch2.15 與 ch16.17 共用；`W0.)` 由 ch17.1／18.1／19.1 共用，且 037 對前兩者各產出一個獨立需求（6 leaves 覆蓋同一條規範句） |

---

## 1. 條文貼入（09 §6.1 ＋ 10 §6）

`RULINGS.md` 現載 **R-C1 ~ R-C17 + R-C4-1 + R-C5-1**，共 19 條，全部原文照錄。

- **R-C15／R-C16**（09 §2／§3）另立小節，標注適用全 feature、待 canon re-sync。
- **R-C17**（10 §1）另立小節。

R-C15 回答了我在上繳 04 §6.2 第 3 項標出的界線：判準是**蘊含**不是**直接**。
我當時照條文字面執行並標明界線所在，該處置獲追認 —— 但更值得記的是 09 §2
的那句「界線本身該由分析層畫，不該由條文的沉默決定」。我下次遇到同型情況
仍應標而不自裁。

## 2. DR #8 轉 DEFERRED ＋ R-C16 處置類別（09 §6.2、10 §2）

`data/sr24_substantive_applicability.tsv` 加第六欄 `disposition`。

**20.1 ~ 20.4.3 十節**：`pending_on` 改記
`DEFERRED — Pei 直接向 RD 反應（2026-08-14）；原 DR #8 …`。
verdict **維持 `undetermined`**（R-C12）—— 不升 `in_scope`、不降
`out_of_scope`。**把問題交給別人問，不等於問題有了答案**：矛盾未解這件事
不因誰去問而改變。

**16.1、18.2、18.3、18.4 四節**：`disposition` 記

> RD-1 coverage-gap item (R-C16) — 037 never analysed it; NOT a TC work item,
> no tc_id, not in the coverage denominator, not BLOCKED, pending upstream
> 037 analysis

R-C16 §2 澄清了一件我先前沒有問、但確實會出錯的事：**`in_scope` ≠「我們去
寫 TC」**。我在上繳 03／04 把 `in_scope` 當成「應由 Comfort 驗證」在用，
語意上沒錯，但若無 R-C16，Phase 4 很可能把這四節當工作項展開。

`undetermined` 之 13 節 `disposition` 記「—（verdict 未定，尚無處置）」，
不預先套用 R-C16 —— 該條適用於 `in_scope` 之節，而它們不是。

## 3. Layer 3 map（10 §4.1）

`features/comfort/data/layer3_map.tsv`，六欄，129 列，
由 `scripts/build_layer3_map.py` 產出（可重跑）。

### Assertion（PASS/FAIL + 實測值）

```
- PASS — leaf_count sum == 403: expected 403, measured 403
- PASS — row count == 129: expected 129, measured 129
- PASS — per-chapter distribution matches upstream 01 §3:
    expected `all 14 chapters equal`, measured `all 14 chapters equal`
    — 14 chapters compared: 2:92、3:14、6:1、7:38、9:8、10:15、11:37、
      12:22、13:14、14:40、15:2、16:99、17:18、18:3
```

期望之章別分布**寫死於腳本**（取自 10 §4.1 之下放值），不由同一份資料回推
—— 自己導出的期望值不可能失敗，那種 assertion 只是裝飾。

### 一個對 Part N 有用的結構事實

**section ↔ parent req_id 為 1:1 雙射**：129 個 section 對應 129 個相異
parent（`SWE1-HVAC-NNN`），無任何 section 跨多個 parent，亦無任何 parent
跨多個 section。故 `req_ids` 欄每列恰一個值。

這表示 Layer 2 無論怎麼切，都不會出現「一個 Test Set 必須跨切某個
parent 需求」的情形 —— 切分的自由度完全在 section 之間，不在 section 之內。

## 4. 章 2 與章 16 明細（10 §4.2）

兩章合計 **191 leaves / 40 sections**，佔 403 之 **47.4%**。

### 章 2 — Front Comfort/Climate（22 sections / 92 leaves）

| outline | section 標題（前 56 字） | leaves | parent |
|---|---|---|---|
| `2.1` | R1C1.) The comfort category will have up to 4 tabs depen | 3 | `SWE1-HVAC-001` |
| `2.2` | C1.) Whenever changes to the climate system are made via | 8 | `SWE1-HVAC-002` |
| `2.3` | C2.) AUTO has on/ off state. The fan speed indicator sho | 9 | `SWE1-HVAC-003` |
| `2.3.1` | C2.1) Some vehicles with dual zone climate with dual air | 2 | `SWE1-HVAC-004` |
| `2.4` | C3.) AC has on/ off state. Auto can automatically turn o | 4 | `SWE1-HVAC-005` |
| `2.5` | C4.) Recirc has on/ off state. RECIRC is not available i | 4 | `SWE1-HVAC-006` |
| `2.5.1` | C4.1) Some vehicles have a configuration for a 3 state t | 2 | `SWE1-HVAC-007` |
| `2.6` | C5.) Temperature ranges: LO, 60-84, HI (English), LO, 16 | 5 | `SWE1-HVAC-008` |
| `2.6.1` | C5.1) If SYNC is ON, adjusting driver temperature affect | 6 | `SWE1-HVAC-009` |
| `2.7` | C6.) Fan ranges: Off, 1-7, 15h (denoting to show AUTO in | 5 | `SWE1-HVAC-010` |
| `2.7.1` | C6.1) In some vehicles fan speed ranges for front hvac a | 1 | `SWE1-HVAC-011` |
| `2.8` | C7.) Defrost has on/ off state. Defrost can automaticall | 6 | `SWE1-HVAC-012` |
| `2.9` | C8.) Rear Defrost has on/ off state. REAR DEFROST is not | 4 | `SWE1-HVAC-013` |
| `2.10` | C11.) Climate off has on/off state that is indicated on | 6 | `SWE1-HVAC-014` |
| `2.11` | C12.) SYNC has on/ off state that is indicated on climat | 5 | `SWE1-HVAC-015` |
| `2.12` | C13.) There are 4 Airflow Mode displayed in this order ( | 3 | `SWE1-HVAC-016` |
| `2.12.1` | C13.0) In some non-tri mode equipment types, airflow mod | 2 | `SWE1-HVAC-017` |
| `2.12.2` | C13.1) If the Mode hard control is pressed the user will | 6 | `SWE1-HVAC-018` |
| `2.13` | C14.) MAX A/C screens/popups are to be used when CCM rel | 3 | `SWE1-HVAC-019` |
| `2.14` | C15.) MTC screens/popups are to be used when CCM relays | 4 | `SWE1-HVAC-020` |
| `2.15` | C16.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off stat | 2 | `SWE1-HVAC-021` |
| `2.16` | C18.) If blower reduction occurs automatically due to an | 2 | `SWE1-HVAC-022` |

### 章 16 — ICS CLIMATE EMEA – CARRYOVER（18 sections / 99 leaves）

| outline | section 標題（前 56 字） | leaves | parent |
|---|---|---|---|
| `16.2` | ICE1.) Whenever changes to the climate system are made v | 9 | `SWE1-HVAC-106` |
| `16.3` | ICE2.) AUTO has on/ off state. The fan speed indicator s | 9 | `SWE1-HVAC-107` |
| `16.4` | ICE3.) MAX A/C, A/C, RECIRC, MAX DEF, and REAR DEFROST h | 1 | `SWE1-HVAC-108` |
| `16.5` | ICE4.) The recirc icon will display the vehicle model sp | 2 | `SWE1-HVAC-109` |
| `16.6` | ICE5.) Temperature ranges: LO, 60-84, HI (English), LO, | 6 | `SWE1-HVAC-110` |
| `16.6.1` | ICE5.1) If SYNC is ON, adjusting driver temperature affe | 5 | `SWE1-HVAC-111` |
| `16.7` | ICE6.) Fan ranges: Off, 1-7 (denoting to show AUTO label | 5 | `SWE1-HVAC-112` |
| `16.8` | ICE7.) MAX DEF automatically turns on A/C, changes airfl | 12 | `SWE1-HVAC-113` |
| `16.9` | ICE8.) Rear Defrost has on/ off state. Gray out the REAR | 2 | `SWE1-HVAC-114` |
| `16.10` | ICE9.) Climate off has on/off state that is indicated on | 8 | `SWE1-HVAC-115` |
| `16.11` | ICE10.) SYNC has on/ off state that is indicated on clim | 4 | `SWE1-HVAC-116` |
| `16.12` | ICE11.) Airflow Modes has 5 states (1.Face, 2.Mix of Fac | 3 | `SWE1-HVAC-117` |
| `16.12.1` | ICE11.1) If the Mode hard control is pressed the user wi | 10 | `SWE1-HVAC-118` |
| `16.13` | ICE12.) If the system supports Max A/C it will be displa | 12 | `SWE1-HVAC-119` |
| `16.14` | ICE13.) MTC screens/popups are to be used when CCM relay | 3 | `SWE1-HVAC-120` |
| `16.15` | ICE14.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off st | 2 | `SWE1-HVAC-121` |
| `16.16` | ICE15.) Always show 'Driver' or 'Passenger'. Off icon of | 5 | `SWE1-HVAC-122` |
| `16.17` | C16.) If blower reduction occurs automatically due to an | 1 | `SWE1-HVAC-123` |

### 觀察（**陳述，非主張**；Layer 2 屬 Tier 2，10 §4.3）

**兩章高度平行。** 章 16 是 EMEA ICS 之 carryover，其條款與章 2 逐條對應：

| 主題 | 章 2 | 章 16 |
|---|---|---|
| 硬體控制變更之同步 | `C1.)` 2.2 | `ICE1.)` 16.2 |
| AUTO on/off | `C2.)` 2.3 | `ICE2.)` 16.3 |
| 溫度範圍 | `C5.)` 2.6 | `ICE5.)` 16.6 |
| SYNC 連動 | `C5.1)` 2.6.1 | `ICE5.1)` 16.6.1 |
| 風量範圍 | `C6.)` 2.7 | `ICE6.)` 16.7 |
| Rear Defrost | `C8.)` 2.9 | `ICE8.)` 16.9 |
| Climate off | `C11.)` 2.10 | `ICE9.)` 16.10 |
| SYNC | `C12.)` 2.11 | `ICE10.)` 16.11 |
| Airflow Mode | `C13.)` 2.12 | `ICE11.)` 16.12 |
| Mode 硬鍵 | `C13.1)` 2.12.2 | `ICE11.1)` 16.12.1 |
| MTC | `C15.)` 2.14 | `ICE13.)` 16.14 |
| 後視鏡除霜 | `C16.)` 2.15 | `ICE14.)` 16.15 |
| blower reduction | `C18.)` 2.16 | **`C16.)`** 16.17 ← 標籤異常，見 A-CF13 |

**不對稱處**（章 16 有而章 2 無、或反之），供 granularity 判斷：

- 章 16 獨有：`ICE3.)` 16.4（多鍵集合狀態）、`ICE4.)` 16.5（recirc 圖示
  依車型）、`ICE7.)` 16.8（MAX DEF，12 leaves）、`ICE12.)` 16.13
  （Max A/C，12 leaves）、`ICE15.)` 16.16（Driver/Passenger 標示）
- 章 2 獨有：`R1C1.)` 2.1（分頁數）、`C3.)` 2.4（AC）、`C4.)` 2.5 +
  `C4.1)` 2.5.1（Recirc 與三態切換）、`C7.)` 2.8（Defrost）、
  `C13.0)` 2.12.1（非 tri-mode）、`C14.)` 2.13（MAX A/C 畫面）
- leaf 集中處：章 16 之 16.8 與 16.13 各 12 leaves（合計佔章 16 之 24%）；
  章 2 最大為 2.3 之 9 leaves，分布較平均

**執行層不就 Layer 2 提出任何主張** —— 不建議 Test Set 數量、邊界或命名。
以上僅為量測與結構描述。

## 5. A-CF13 —— 兩處 spec 內部標籤問題（新登）

### 一、`C16.)` 被兩節共用，內容不同

`2.15`（EXTERIOR REAR-VIEW MIRROR DEFROST）與 `16.17`（blower reduction）
皆掛 `C16.)`。章 16 其餘 17 節一律 `ICE` 前綴，且 16.17 之內容對應章 2 的
**`C18.)`**（2.16）。故 16.17 掛 `C16.)` 最可能是誤植。

**影響**：TC 若於 test item 或 reasoning 引用條款標籤，`C16.)` 指向兩個
不同行為。Phase 4 撰寫 ch16 TC 時須以 **outline 節次**為準，不以條款標籤
為準。RD-1 候選。

### 二、`W0.)` 由三節共用，其中兩節各被分析為獨立需求

| 節 | 章 | 037 | 條文 |
|---|---|---|---|
| `17.1` | Home screen - Comfort Widget | 引用，3 leaves（`SWE1-HVAC-124`） | W0 + 交叉參照句 |
| `18.1` | 10.25" Home screen - Comfort Widget | 引用，3 leaves（`SWE1-HVAC-129`） | W0（純句） |
| `19.1` | 7" Home screen - Comfort Widget | **未引用** | 與 18.1 **逐位元組相同** |

037 對 17.1 與 18.1 各產出一個 parent，**合計 6 個 leaves 覆蓋同一條規範句**
（「Comfort widget 有 Comfort 與 Seats 兩個畫面」）。

**與上繳 04 之關係 —— 一處補充**：我在上繳 04 只比對了 18.1 與 19.1，
未察覺 17.1 亦為同一條款。這不改變當時對 18.2–18.4 之判定（依據是「037
引用了 10.25" 專章之 18.1」，仍成立），但當時的描述不完整。

**影響（Part N）**：若 Layer 2 依章切，ch17 與 ch18 各得一個 Test Set，
而兩者首節測同一件事。此為分析層起草時需知之事實，**執行層不就此提出
Test Set 主張**。

## 6. R-C17 —— 已貼入，並複測其所據之三項陳述

10 §3 對 Home Screen spec 之陳述，逐項複測：

| 陳述 | 實測 | 結果 |
|---|---|---|
| 該檔已在 repo（54.29 KB） | `spec-index/cache/SYS1_HMI_Home_Screen_…_SR24_Post_2A_(March_17_2023).xlsx`，**55,596 bytes** | ✅ |
| HS9.4 `Seats & Wheel`、HS9.5 `Comfort` 之 Reference Document 皆為 Comfort HMI | 見下 | ✅ |
| HSD13 之內容 | outline **4.11**：「When there is a lower non-articulating screen do not provide heated/vented seats, heated wheel, or comfort as widget or shortcut options.」逐字相符 | ✅ |

**HS9.4／HS9.5 之查證需要一步轉換，記於此以免下次重犯**：它們**不是
outline 9.4／9.5**（那兩節是 `HSS3.)`／`HSS4.)`，關於 shortcut 編輯），
而是 **outline 7.2.1 內 widget 一覽表的列標籤**：

```
HS9.4 | Seats & Wheel | Comfort HMI | High and Low
HS9.5 | Comfort       | Comfort HMI | High and Low
```

我第一次照 outline 查 9.4／9.5 得到不相干的內容，換去讀 7.2 `HS9.) Available
widgets` 之表格才對上。**條款標籤與 outline 節次是兩套編號**，這與 A-CF13
第一項是同一類問題，只是這次出現在 Home Screen 文件裡。

**R-C17 之直接文本支持**（本次併查所得，10 §3 未引）：Home Screen 7.1 ——
「Available widgets will vary depending on vehicle configuration, screen size
and radio type. **Widget content will be contained within the category
document.**」這句話正是 R-C17 之擁有者切分：Home Screen 擁有 widget 的
**放置與管理**，category document（即 Comfort HMI）擁有 widget 的**內容**。

**一個 R-C1 型陷阱，先記下**：`spec-index/cache/` 同時存有 Home Screen 之
**SR25** 版（`…_R1_SR25_Post_2A_(March_10_2023).xlsx`）。R-C17 指名的是
**SR24 Post 2A (March 17 2023)**。Phase 4 若引用該檔，須比照 R-C11 之作法
寫全名指向唯一檔案，不用萬用字元。

## 7. `recon.py` 之 `pdftotext` fallback（09 §4 授權）

`survey_spec_text_layer()` 改為：優先 `pymupdf` → 不可用時 poppler
`pdftotext` → **兩者皆不可用**時才回報 unknown，且訊息同時指名兩者
（原訊息只提 pymupdf，會讓讀者以為只有一條路）。

實測 `RECON.md` 現印 `text-layer: 62782 chars (via pdftotext)`。
**依 R-C8 未重跑任何既有 feature**，其 `RECON.md` 之該行維持原狀。

A-CF06 **CLOSED**；`DATA_REQUESTS.md` #3 標為已解。

## 8. 其他狀態更新

- **DR #10** 之性質依 09 §4 訂正為「**客戶端存在，待 Tier 3 補入**」，
  非「不存在」。我原記「全 repo 搜尋不存在」—— 該實測本身正確，但把它寫成
  檔案性質的結論是過度延伸；09 §4 之措辭訂正我接受。
- **DR #6** 依 09 §5 改為**請 Pei 指認來源**。10 §3 之 Home Screen spec
  **不關閉本項** —— 其 Assumptions 之機種列舉與 `Available Widget Size`
  兩表皆為平台配置，不宣告本次交付出哪幾種，與 SR24 §1.1 同型。
- `DECISIONS.md` **未簽署**；R-C10 警告持續正常輸出。

---

## 9. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 9.1 已驗

1. Layer 3 map 三個 assertion（403／129／逐章分布）。
2. section ↔ parent req_id 之 1:1 雙射（129 ↔ 129，無重複）。
3. `C16.)` 與 `W0.)` 兩處標籤共用，逐節比對條文。
4. 17.1／18.1／19.1 三者條文之異同（18.1 與 19.1 逐位元組相同）。
5. Home Screen spec 之三項陳述（檔案存在與大小、HS9.4/9.5 之 Reference
   Document、HSD13 全文）。
6. `pdftotext` fallback 於 recon 之實際輸出。
7. TSV 六欄、17 節、`disposition` 分派、20.x 之 DEFERRED 記法。

### 9.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **章 2／16 之逐條語意對應是否完整** | §4 之對應表以條款標籤與標題前 56 字比對得出，**未逐條讀全文**。可能有標題相近而內容分歧者 | **中** —— 若分析層要據此把兩章切成平行 Test Set，該對應表需先逐條覆核。我標為「觀察」而非「主張」正是因為它還沒到可據以決策的強度 |
| 2 | **16.17 之正確標籤應為何** | 需上游確認，非本地可判 | 低 —— 已列 RD-1 候選；Phase 4 以 outline 為準即可繞開 |
| 3 | **7" 螢幕配置**（DR #6） | 09 §5 已改為請 Pei 指認 | 中 —— 3 節 undetermined，不阻塞 Phase 3 |
| 4 | **Home Screen spec 之完整涵蓋範圍** | 只查了 R-C17 所需之三處與 7.1／7.2.1，**未通讀 105 節** | 中 —— Phase 4 寫 ch17／ch18 TC 時須通讀，否則 R-C17 之「判定測試」（該規則定義於何處）無法逐條施行 |
| 5 | A-CF02 交付夾 | 該樹本 session 不可達 | 低 |

第 1 與第 4 項是同一性質：**本包所做的是量測與結構描述，不是內容理解。**
Layer 3 map 告訴你有哪些節、多少 leaves、標題長什麼樣；它不告訴你這些節
在講什麼。Part N 若要切得站得住，第 1 項的逐條覆核遲早要做 —— 差別只在
分析層起草前做，還是起草後回頭補。

### 9.3 未做、亦未偷做者

- **未決定 Layer 2 Test Set**：未提數量、未提邊界、未提命名。§4 之
  「觀察」段明確標為陳述而非主張。
- 未寫 profile `[OVERRIDE]`。
- 未產 TC、未指派 tc_id。
- 未簽署 `DECISIONS.md`。
- 未把 16.1／18.2–18.4 四節當工作項展開（R-C16：RD-1 覆蓋缺口項）。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 9.4 執行層對「本包可否結案」之判斷

**可結案。** Layer 3 map 已可作為 Part N 之輸入：129 節、逐節 leaf 數、
1:1 雙射之結構事實、兩大章之明細與不對稱處，皆已具備。

**建議分析層起草 Part N 前先處理 §9.2 第 1 項**：章 2 與章 16 的平行性
是我從標籤與標題看出來的，若 Part N 打算利用這個平行性（例如兩章用同構的
Test Set 切法），那個對應表需要逐條覆核過才承得住。我可以做，但那是內容
理解而非量測，且會產生「哪些條文等價」的判斷 —— 若那屬 Tier 2，請明示由
分析層做；若可下放，請明示，我再執行。
