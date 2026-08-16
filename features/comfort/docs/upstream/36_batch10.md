# 36 — Comfort HMI / 條級等價、對照關係類、軸類別常設複檢、批次 10

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 52／53
- 結果：五項全數落實。`equivalent_tc_pairs` 欄已增並記兩對，開 DR #39。
  DR #32 改為類項並納入 `-133`。**`axis-type-reverse-test` 已實作為第 43 道 gate**，
  反向驗證九案全過 —— **且其驗證過程當場抓到批次 8 之兩條 TC 缺一行 PC，已修**。
  批次 10 產 **14 條**（`-153`…`-166`），停下 9 leaf。
  lint **43/43 PASS，166 條**。ENTRY 007 已產出，3 項 FAIL 同源，不可交付。

---

## 0. 下放包五項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | sibling 表增 `equivalent_tc_pairs` 欄，記兩對；開 DR | ✅ §1 —— DR #39 |
| 2 | DR #32 改名納入 `-133`；`RUNBOOK` 記類項標題須隨成員更新 | ✅ §2 |
| 3 | 實作 `axis-type-reverse-test`，反向驗證；profile 記各功能型軸判定當時之 N | ✅ §3 —— **驗證過程查出一項實質缺陷**，見 §3.3 |
| 4 | 收窄 `Climate Popups` 之阻塞記載（本輪不生成該組）| ✅ §4 |
| 5 | 執行批次 10 | ✅ §5 —— 產 14、停 9；**「2 leaf」實為 9 leaf**，見 §5.2 |
| — | 上繳 36 | 本件 |

---

## 1. `equivalent_tc_pairs` —— 條級等價記於 sibling 表

`data/pending_sibling.tsv` 增第六欄 `equivalent_tc_pairs`，置於 `source`
之後。`2.6.1 ↔ 2.11` 一列記**兩對**：

```
NR1L-ComfortHMI-053 = NR1L-ComfortHMI-150
NR1L-ComfortHMI-054 = NR1L-ComfortHMI-151
```

判定依據逐項載於同欄（§10.6 四項）：trigger（SYNC on ＋ 改駕駛側／乘客側
溫度）、outcome（乘客側跟隨／SYNC 關閉）、input（皆 `NA`）、
verification target（該連動或中斷本身）—— **四項全同**。

`duplicate_of` **維持不填**，理由同記於該欄：§10.6 之該欄為**節級**且為
工具側注入之列號，跨節等價不在其射程（52 §1）。

**重建保留該欄**：`sibling_candidates.py --rebuild` 之 `emit()` 以
`rec.get("equivalent_tc_pairs", "")` 帶過，已實測冪等（連跑兩次 md5 相同）。
這一行是刻意的 —— 該欄是**人工維護**的，而重建每輪重寫全表；
沒有這一行，第一次重建就會把它清空，而**清空不會有任何東西出聲**
（與 32 §1.5 之 `provisional` 自行清旗同型）。

**DR #39 已開**（Medium）：037 將 SYNC 之同一組行為分解為 `2.6.1` 與 `2.11`
兩個 leaf，致本交付件產生兩對嚴格等價之 TC。**此為 RD 層之分解問題** ——
依 §8.2.2 TC 作者不得合併 leaf，依 R-C33 單位歸 037，故兩條 TC 皆保留。

---

## 2. DR #32 改為類項，納入 `-133`

標題改為「**條文要求一組對照關係而未定義之**」。三個成員，逐項列其節次與
所缺之對照：

| 成員 | 節 | 缺什麼 |
|---|---|---|
| (a) | `16.16` ICE15 | `system configuration → icon` 之對照（座椅 off icon）|
| (b) | `2.5` C4 | `vehicle model → icon` 之對照（「as displayed in **the table**」未指名節次；`16.5` 逐字重述且把表寫成 `Climate Main page table`，**仍未給對照**，故兩側皆無）|
| (c) | `2.3` C2 | `auto mode → manual mode` 之對照（「most closely matches」）—— `-133` 只驗確定之一半，TC 內容不動 |

`RUNBOOK.md` 已記「**類項之標題須隨成員擴充而更新**」，含其理由：

> **以首個成員為名的類，會使後來者看不出自己屬於它。**
> 第二個成員出現時，第一個反應會是「這是新的一項」——
> 於是同一形態被開成兩個 DR，而它們的處置一模一樣。

並記其與 50 §3「處置相同者不分類」之關係：**兩者是同一原則的兩個方向** ——
處置相同就不該分成兩項；合成一項之後，名字得跟著涵蓋範圍走。

---

## 3. `axis-type-reverse-test` —— 第 43 道 gate

### 3.1 機制

profile 增 `function-axis-reverse-test` 區塊，**每一個判為功能型之軸各一塊**
（共 **14** 塊：軸 1–8、10、11、14–16 與機型軸）。欄位：
`function-keywords`／`removed-interface-keywords`／`axis-pc-keywords`／
`judged-at-tc-count`／`judged-at`。**判準自 profile 讀入，不寫死於腳本**（52 §3）。

gate 每次 lint 執行，具名回報行輸出：

```
- PASS — axis-type-reverse-test re-ran on 166 TCs (52 §3): 14 功能型 axes
  declared, 1 with a removed interface (live test), 13 declaring `none`
  (vacuous by claim, not by omission)
```

**「顯式聲明與漏寫不同」**：`removed-interface: none` 是一個主張，
漏寫是沉默 —— 故 gate 另檢查 profile 軸表中每個標 `功能型` 之列**都有區塊**，
無區塊即 FAIL 並具名該軸。這一項才是「常設」的意思：
新增功能型軸而忘了聲明，會當場出聲。

`judged-at-tc-count` 記判定當時之 N（軸 16 為 **124**，其餘補登者為 **152**），
使「以多少條驗過」可查。

### 3.2 一處解讀，須明說

52 §3 之問句為「是否存在任一條 TC，**其功能為該軸所轄**，而其可觀察量位於
該軸之某值所移除之介面上？」。照字面實作會把 `-125`／`-126`
（17.3 自身之兩條）判成違反 —— 它們的功能確為軸 16 所轄，可觀察量確在
widget 第二頁上。

但那兩條**帶著軸 16 之 PC**，已被限定於某一值，其可觀察量不會意外消失。
故實作加一條：**已帶該軸 PC 者不算違反**。此解讀已寫入區塊之註解與本包。

### 3.3 反向驗證當場抓到一項實質缺陷 —— 批次 8 之 `-115`／`-117`

`verify_axis_type_gate.py`（新增）九案，其中第 3 案「把 PC 拿掉之後同一條
TC 必須觸發」**第一次執行時失敗**。追查後發現**不是 gate 錯，是我的探針
挑錯了 TC**：它挑到 `-117`，而 `-117` 之功能不受軸 16 所轄，
故 gate 的沉默是對的。

**但追這個差異的過程查出了真的東西**：

> `-117`（第二個 widget 畫面是 Seats）與 `-115`（widget 有兩個畫面）
> **其可觀察量都在 widget 第二頁上，而 17.3 明定「若未配備 Comfort Features
> 則該頁不顯示」** —— 兩條卻**都沒有帶軸 16 之 PC**。
> 於是它們在無 Comfort Features 之車上為假，而其自身之主題（17.1 之兩個畫面）
> 並未消失。

**這正是 52 §3 之問句所要找的形態，只是方向相反**：問句要求「功能為該軸
所轄」，而此處是「**功能不為該軸所轄，卻仍失去觀察端**」——
即 35 §1／50 §1 當初立反面檢驗時所述之目的
（「功能仍在而**別條 TC** 之可觀察量消失」）。

**措辭與目的發散了。** 處置：

1. **`-115` 與 `-117` 已補上軸 16 之 PC**（spec-verbatim，出處 17.3），
   `17.3` 併入其 `specification_reference`（R-C29）。`-116`（第一頁是
   Comfort）不受影響，未動。
2. 反向驗證增第 3b 案 —— **目的版檢驗**：任一條 TC 若依賴該介面而未陳述
   該軸之值即報。現為 0。
3. gate 本身**仍依 52 §3 之字面實作**，因為改問句是改裁定。
   **兩版皆跑、皆綠**，其差異記於此。

> **一道符合自己措辭卻錯過自己理由的 gate，是最糟的一種綠。**

### 3.4 反向驗證之九案

```
PASS — every 功能型 axis in the table has a block: 14 axes, all declared
PASS — at least one axis declares a removed interface: live: ['16']
PASS — axis 16: TCs exist on the removed interface (3: -117 / -125 / -126)
PASS — axis 16: those TCs carry the axis pre_condition, so they stay silent
PASS — axis 16: a TC matches BOTH the interface and the function filter (-125)
PASS — axis 16: the SAME TC without the axis pre_condition DOES fire
PASS — axis 16: no TC depends on that interface WITHOUT stating the axis value
PASS — axis 16: a TC on another interface stays silent (-042)
PASS — axis 1: declares `none` and fires on nothing (all 166 TCs)
```

---

## 4. `Climate Popups` 之阻塞收窄

DR #37 之影響欄已改：**整組 42 leaf 不再阻塞，僅 `14.12` 自身之 leaf 停下**。
理由照 53 §1 記入：原顧慮為「軸未定而生成將導致大批回溯補 PC」，
而本項之實測結論是 `14.12` **不是缺一個軸，是該句無法適用** ——
**既非軸，即無「軸未定而生成」之回溯風險**。

**本輪不生成該組**（53 §1 明示此為阻塞範圍之收窄而非新授權）。

---

## 5. 批次 10 —— `Airflow and Defrost`

### 5.1 節次與 leaf 數，自 framework.md 導出，與 037 相符

| outline | leaves |
|---|---|
| `2.8` | 6 |
| `2.9` | 4 |
| `2.12` | 3 |
| `2.12.1` | 2 |
| `2.12.2` | 6 |
| `2.15` | 2 |
| **合計** | **23** |

037 獨立實測：012(6)＋013(4)＋016(3)＋017(2)＋018(6)＋021(2) = **23**。相符。

### 5.2 停下為 **9 leaf**，非下放包所記之 2

53 §2 寫「DR #31 僅卡其 **2 leaf**（`2.12`／`2.12.2` 之 PC）」。
**那是把節數讀成了 leaf 數**：`2.12` 與 `2.12.2` 是 **2 個節、9 個 leaf**
（3 ＋ 6）。**處置不變**（兩節皆停），**但覆蓋率之算術不同**：
14/23（61%），不是 21/23。

**何以兩節全停而非部分停**：C13 全節之主體是 4 模式配置
（「There are 4 Airflow Mode displayed in this order」），C13.1 之循環序即
該集合。DR #31 是「4 模式這個值沒有正面之適用條件」——
故該二節之下**沒有任何 leaf 能陳述自己的適用車輛**。
其中 `016-03`（「Only one airflow mode can be selected at a time」）
**於 tri-mode 車直接為假**（C19 之三鍵可個別 toggle），尤須先能陳述本車之值。

**`2.12.1` 不受影響** —— C13.0 自帶正面限定語
（「In some **non-tri mode equipment types**」），**這正是第三軸當初得以換軸
的同一個理由**（32 §3）。三值之中，只有它自己說得出「哪些車是我」。

### 5.3 產出

| leaf | 節 | TC | tc_id |
|---|---|---|---|
| `SWE1-HVAC-012` | 2.8 | 6 | `-153`…`-158` |
| `SWE1-HVAC-013` | 2.9 | 4 | `-159`…`-162` |
| `SWE1-HVAC-017` | 2.12.1 | 2 | `-163`／`-164` |
| `SWE1-HVAC-021` | 2.15 | 2 | `-165`／`-166` |
| **合計** | | **14** | 14 emitted ＋ 9 withheld ＝ **23** |

### 5.4 一項不對稱，呈報而未自行處置

`2.9`（C8）以「**if this feature available**」把對外後視鏡除霜寫成**可選配備**，
而 `2.15`（C16.）陳述該功能之 on/off 與獨立性時**無任何配置限定語**。

處置：`-162`（C8 之連動）帶該條件為 PC，出處標 `2.9` ——
**條文自帶之情境條件（§8.5／R-C28 第二問），非新軸**，形態同 `2.13` 之
「when CCM relays presence of MAX A/C functionality」。
`2.15` 之兩條**不補配置式 PC**，與 `2.4`／`2.5` 同例（其條文亦無限定語）。

**待裁**：「對外後視鏡除霜有無」是否應登為軸？若登，`-165`／`-166` 須補值。
本輪不自取（增軸屬 profile 變更）。

### 5.5 R-C36-1 —— 14 條中 **9 條為 `no`**

比批次 9 之 6/26 更密集，成因是本組之 ch16 對造多為 `partial` 且其分界
正落在本節所驗之處：

| TC | ch16 | 何以 `no` |
|---|---|---|
| `-153`～`-158`（2.8 全部 6 條）| 16.4 | 分界欄：「涵蓋 MAX DEF 之 on/off；**未涵蓋 C7 之 Defrost 自動開啟等連動**」。**且 ICE3 所述 on/off 之對象是 MAX DEF，而本節之對象是 C7 之 `FRONT DEF`** —— 兩者非同一控制 |
| `-161`／`-162`（2.9 之獨立性與鏡面連動）| 16.9 | **ICE8 僅兩句**（on/off 與灰化），不含 C8 之獨立性與鏡面連動 |
| `-166`（2.15 之獨立性）| 16.15 | **ICE14 僅一句**（on/off），不含 C16 之獨立性 |

`-159`／`-160`／`-163`／`-164`／`-165` 五條為 `yes`，各指向 ICE8／ICE11／
ICE14 之逐字相同句。

**`-164` 另記一項條文內部不一致**：其對造 ICE11 自身寫 `5 states`
而其呈現句寫 `ON state for the **four** airflow modes` —— 與 A-CF13 同型。
本條只驗「所選模式呈現為作用中」，**不驗按鈕數**。

### 5.6 §8.2.1 之界線，逐項具名（53 §2.1）

| 不移植者 | 理由 |
|---|---|
| `3.2`（C20）之 MAX DEF 七項連動 | 本批之 Defrost 為 C7 之 `FRONT DEF`，與 MAX DEF 為**不同控制、不同條文** |
| `3.3`（C21）之 climate off 可用性 | 本批之灰化來自 **CCM 之可用性狀態**，與 climate off 之狀態無關 |
| `2.15` 之條款標籤 `C16.` | 與 `16.17` 之 `C16.` 撞號（A-CF13 第一項）—— traceability 一律以 outline 為鍵，`spec_ref` 記 `2.15` |

### 5.7 §4.6 回填與 49 列重新確認

`2.12.1 ↔ 3.1` 之 `distinguishing_axis` 已補：軸為第三軸，
`2.12.1` 取 **5 狀態**、`3.1` 取 **tri-mode 7 組合**。
**兩者為同一需求在該軸兩值上之陳述，故 verification target 必然相異**
—— 四項嚴格等價不成立，`duplicate_of` 不填。
（該軸第三值 4 模式因 DR #31 未生成，故三值中目前僅二值有 TC。）

49 列 provisional 到期，全部逐對判完並清旗。`false` 現 **287**／`true` 1381。

---

## 6. lint 與 §9 自評

```
43 / 43 gates PASS; 0 finding(s) across 166 TCs
```

gate 42 → **43**（新增 `axis-type-reverse-test`）。
TC 152 → **166**；leaf 147 → **161**；已生成節 46 → **50**。

**§9 十七項**：新增 14 條（批次 10）＋ 修改 2 條（`-115`／`-117` 補 PC）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition | 變 | 第十軸（`2.9`，出處 3.4）／第三軸之 5 狀態值（`2.12.1`）／第一軸 ATC（`-157`）／C8 自帶條件（`-162`）＋ 軸 13＋EMEA＋軸 9；**`-115`／`-117` 補軸 16 之值（17.3）** |
| 5–8 | 步驟 | 變 | 每條 2–3 步，末步持驗證 |
| 9 | Baseline | 變 | `-154`～`-157`／`-159`／`-162`／`-165` 需前後對照 |
| 10 | Procedure ↔ ER 1:1 | 變 | 14 條全數 1:1 |
| 11 | FP／FF | 變 | `-154`（不顯示變化）、`-157`（互相關閉）、`-161`／`-166`（獨立性以反例否證）皆配正向步驟 |
| 12 | 溯源、§8.2.1、§8.4 | 變 | 14 leaf 各溯其 037 req_id；§8.2.1 三處不移植見 §5.6；9 leaf 依 §8.4.2 停下 |
| 13 | Design Method | 變 | 13 條功能測試、`-157` 狀態轉換 |
| 16 | `specification_reference` | 變 | 各條含自身節次＋2.14＋16.2＋6.3；`2.9` 加 3.4、`-157` 加 2.3、`-115`／`-117` 加 17.3 |
| 17 | §8.6／§8.7 | 變 | `-164` **不驗按鈕數**（ICE11 之 5 vs four 不一致）；C7 之「Recirc **is may or may not be** available」為語病，只依可判之灰化立 ER |
| 其餘 | — | 不變 | |

---

## 7. 「本包是否仍有該驗而未驗者」（R-C30）

1. **批次 10 之 14 條未經 §7 之 FP／FF 人工複核**，只經 lint。
2. **`-115`／`-117` 之修正是反向驗證的副產品** —— 若那一案沒挑錯 TC，
   我不會去追那個差異，這兩條就會維持缺一行 PC。**運氣參與了這次發現**，
   如實記之。同型之缺陷是否存在於其他批次，**未系統性複查**。
3. **`function-axis-reverse-test` 之 13 個 `none` 聲明，其依據是我逐軸讀條文
   所得，未經第二人複核。** 其中軸 2 最值得再看：2.11 之
   「Sync is not shown for single zone climate configurations」確實是一個
   介面後果，我判為「功能與觀察端同時消失」故仍為功能型 —— 該判斷可爭。
4. **`judged-at-tc-count` 對補登之 13 軸一律記 152**，而它們的類別其實是
   在更早的輪次判定的（軸 9／12／13 於 19–33 §）。**該數字是「補登時之 N」，
   不是「判定時之 N」** —— 措辭已於區塊註明為 `52 §3 之補登`，但兩者不同，記此。
5. **DR #31 未解前 `Airflow and Defrost` 停在 14/23**，且該組是 ch2 家族
   最後一塊；`Rear Climate`（46 leaf）屆時之對造仍缺 `2.12`／`2.12.2`。
6. **`2.15` 與 `2.9` 之配置不對稱（§5.4）未決前**，`-165`／`-166` 可能需補值。

---

## 8. 建議 commit message（git 未執行）

```
feat(comfort): batch 10 Airflow and Defrost; axis-type-reverse-test

- record TC-level strict equivalence in pending_sibling.tsv's new
  equivalent_tc_pairs column instead of forcing §10.6's duplicate_of, which
  is section-level and carries a tool-injected row number. Two pairs, both
  on 2.6.1<->2.11. DR #39: the cause is 037's decomposition, not ours
- the rebuild carries the new column through by hand-written intent — the
  table is machine-maintained, so an unpreserved hand-kept column would be
  wiped on the first rebuild and nothing would say so
- DR #32 becomes a class, "the clause requires a mapping and never defines
  it", with the seat off icon, the recirc icon and C2's "most closely
  matches" as its three members. RUNBOOK: a class named after its first
  member hides the second one from itself
- implement axis-type-reverse-test as the 43rd gate. Criteria come from the
  profile, not the script. 14 function-type axes declared, 13 saying
  `removed-interface: none` — an explicit none is a claim, a missing block
  is silence, and the gate fails on the silence
- its reverse validation caught a real defect: -115 and -117 observe the
  widget's SECOND page, which 17.3 makes conditional, and neither stated
  the axis value. Both fixed. The gate's wording asks for an axis-governed
  function; its stated purpose is the opposite case — another TC losing its
  observable. Both versions now run, and the divergence is reported rather
  than papered over
- batch 10: 14 TCs, -153..-166. DR #31 stops 2.12 and 2.12.2 — that is 2
  SECTIONS but 9 LEAVES, so coverage is 14/23, not 21/23 as the handoff's
  count implied. 2.12.1 is untouched because C13.0 carries its own "in some
  non-tri mode equipment types", the same reason axis 3 could be swapped
- R-C36-1: 9 of 14 answers are `no`. ICE3's on/off subject is MAX DEF while
  C7's is FRONT DEF — a different control, not a silent counterpart
- lint 43/43 PASS across 166 TCs; ENTRY 007, same three template FAILs
```

---

## 9. 待分析層

1. **§3.3** —— `axis-type-reverse-test` 之措辭與目的發散：問句是否改為
   「任一條 TC 依賴該介面而未陳述該軸之值」（即目的版）。
2. **§5.4** —— 「對外後視鏡除霜有無」是否登為軸；若登，`-165`／`-166` 補值。
3. **§7.3** —— 軸 2 之 `none` 聲明可爭（2.11 之 SYNC 不顯示是否算介面後果）。
4. **§7.2** —— `-115`／`-117` 同型之缺陷是否需對既有 166 條系統性複查。
5. **DR #31** —— 未解則 `Airflow and Defrost` 停在 14/23，且 `Rear Climate`
   之對造將缺兩節。
6. **DR #35 / A-CF26** —— 範本容量仍為交付硬阻塞（166 列，116 列無下拉）。
7. **批次 11 之授權**；`Climate Popups` 已解封至 41/42（僅 `14.12` 停），
   `Rear Climate`（46 leaf）之 `ch2_ch7_mirror_map` 已備。
