# 上繳 03R — Part VII 併入、A-TM17 登記、leaf 描述複驗

執行層 → 分析層。對應 `docs/handoff/03R_review.md`。
**僅回報差異。** 2026-08-20。

**T1–T7 全數完成，T7 七項全符。T6 之三項主張全部支持** ——
但另發現**兩處分析層未列之鄰接**，見 §4.2，屬 §8.2.1 範圍，提請裁定。

---

## 1. T7 七項驗證（實際輸出）

```
1. R-TM 條數                : 25          期望 25   ✅
2. A-TM 條數                : 17          期望 17   ✅
3. grep -c '^## Part VII'   : 1           期望恰 1  ✅   → framework.md:1274
4. grep -c 'SWE-RA-TIME&DATE': 2          期望 ≥1   ✅
5. 'Part VII, end of file'  : 1           期望 1    ✅   → framework.md:5
6. '本檔作廢'                : 1           期望 1    ✅
7. leaf_descriptions 列數    : 22          期望 22   ✅
```

判準 3、4、5 依 R-TM21 皆以本 feature 唯一字串定錨（`Part VII`、
`SWE-RA-TIME&DATE`），**本 feature 若未做即不可能通過**，非 `03` T6 之
假通過形態。

## 2. T1 — Part VII 併入全域檔

### 2.1 assert 結果

```
tail -1 docs/fw036/framework.md
→ 查證（Tier 1）；若有，填入三個 Set 名稱，否則逐列欄位即足（AMFM 先例）。
```

**與期望字串逐字相符**，確認未插錯位置。追加後該檔 `^## Part ` 計數由
**6 → 7**。

### 2.2 兩處替換（改前／改後）

**(a) Part VII 開頭**

```
改前：下列七 Set 表待簽。
改後：下列七 Set 表經 Pei 2026-08-20 簽核（R-TM17）。
```

**(b) Batch plan 段**

```
改前：### Batch plan

      **未定。** 待 Layer 2 經 Pei 簽核後另行起草。

改後：### Batch plan（生成批次 ≠ Test Set）
      + B1–B4 四列批次表（合計 22）
      + B1 取樣依據（canon §1.2 分層取樣）全段
      + B2 集中依據（SXM B11 先例）全段
```

兩處替換均以 `assert block.count(o) == 1` 前置，確保唯一命中後
`replace(o, n, 1)`。**依 R-TM20 之指示，未先寫「待簽」再改，一次寫定。**

## 3. T2 / T3 / T4 / T5 寫入確認

| T | 動作 | 改前／改後或位置 |
|---|---|---|
| T2 | 標頭 Covers 句 | 改前 `**Projection** (Part V), and **Privacy**\n(Part VI, end of file).`　改後 `**Projection** (Part V), **Privacy**\n(Part VI), and **Time and Date** (Part VII, end of file).` |
| T3 | 本地檔作廢註記 | `features/time_management/framework.md` 檔首插入，**未刪除**。**順序遵守**：先確認 `^## Part VII` 命中才執行，無空窗 |
| T4(a) | A-TM01 → **MOOT** | 索引狀態欄改 `**MOOT**（目標已滅失）`；條文末尾追加「處置（2026-08-20）—— MOOT，非依 R-TM18 完成」全段 |
| T4(b) | A-TM17 新增 | 置於 A-TM16 之後、`## Assumption markers` 之前；索引 16 → **17** |
| T5 | R-TM16 追補 | 標題註明「追補：本條原由 02R-A1 指派，該包未執行，2026-08-20 補落」，**編號不重排**，補於 R-TM19 之後 |
| T5 | R-TM20 / 21 / 22 | 逐字追加 |
| T5 | R-TM18 加註 | 依 R-TM13 於條末追加「未能執行（2026-08-20）」，**條文保留** |

### 3.1 A-TM17 之執行層補充：第 4 項事實

分析層 §3 之區塊列三項事實。執行層於該條下補登**第 4 項**（git race
之具體實例，本 session 實測）：

| | |
|---|---|
| commit | `554079e`，標題 `feat(vehicle_setting): rounds 02-03 …` |
| 內含 | **25 個 `time_management` 檔 + 12 個 `vehicle_setting` 檔** = 37 檔 |
| 本執行層之 commit message | **未進入 git**（`git commit` 回報 `nothing added to commit`）|
| 內容完整性 | 已驗：該 commit 內 R-TM 16 條、A-TM 16 條、`test_group` 正確、上繳 333 行皆完整 |
| push 狀態 | 未 push（`ahead 7`），歷史理論上可重寫 |

**其價值**：`554079e` 之 commit 時間為併行者活動之**具體時間錨點**，
可供釐清其作業範圍時比對。本項為 §3 第 1 項之後續實例，同一形態。

執行層未自行修復（重寫歷史會破壞併行者工作，且該 commit 不屬本 feature），
已呈報 Pei 未獲指示，維持現狀。

## 4. T6 — 037 leaf 描述獨立複驗

全 22 列已存 `data/leaf_descriptions.txt`。表頭實測：
`col3 = 'Requirement  Title'`、`col4 = 'Requirement  Description'`（皆雙空格）。

### 4.1 三項主張逐項判定 —— **全部支持**

**主張 1：Set 3 五片同語意軸 —— 支持**

| leaf | 描述動詞受詞（逐字） |
|---|---|
| 005 | shall **maintain internal clock** with ±2 sec accuracy per 24 hours when GPS is unavailable |
| 006 | shall **maintain internal time signal** and update HU_Time.Info |
| 016 | shall **maintain an internal calendar** and act as master for vehicle date (2010–2099) |
| 021 | shall **maintain time using internal counters** during sleep and update on wakeup |
| 018 | shall **initialize** time/date to default values after reset or battery reconnection |

四片逐字皆為 `maintain ... internal ...`，018 為該內部狀態之初始化。
**與 `02R` §2.1 所述相符。**

*字面上之一處小差異（不影響判定）*：021 為 `maintain time using internal
counters`，`02R` 之簡寫式 `maintain internal {…counters}` 將 `internal`
置於 `counters` 前。語意同一（以內部計數器維持時間），僅簡寫式之語序
與原文不同。記錄以備日後引用原文時不致誤植。

**主張 2：Set 7 成組 —— 支持**

- 010（收端）：shall handle **invalid/missing time signals using last valid
  values** and fallback mechanisms
- 022（送端）：shall **send SNA/default values** when time/date data is
  invalid or unavailable

同一能力（無效資料之處置）之兩個方向，逐字相符。

**主張 3：三條相鄰界線 —— 三條全部支持**

| 界線 | 逐字證據 | 判定 |
|---|---|---|
| 004↔010 觸發源不同 | 004：use internal clock when **GPS data is temporarily unavailable**；010：handle **invalid/missing time signals** using last valid values | ✅ 前者為來源不可用，後者為收到之訊號無效，觸發源確實不同 |
| 014 含 `or SNA if unavailable`，SNA 送出屬 022 | 014 逐字：transmit GPS-based date/time signals **or SNA if unavailable**；022 逐字：**send SNA/default values** when … invalid or unavailable | ✅ 字面命中。且界線之**必要性成立** —— 兩片確實都提及 SNA，不劃界會重複覆蓋 |
| 018↔011 | 018：initialize time/date to **default values after reset or battery reconnection**；011：store, recall, and broadcast **time format (12H/24H) across wake cycles** | ✅ 皆涉「重開之後」，一者時間值、一者格式 |

**三項主張全部支持，故未停，依 T6 續行 T7 / T8。**

### 4.2 執行層獨立發現 —— **兩處分析層未列之鄰接**（提請裁定）

複驗時另以「動詞軸」橫掃全 22 列，發現兩片之主要動詞與 `CAN
Transmission` 組同型，卻歸屬他組：

| leaf | 歸屬 Set | 描述之主要動詞 | 與 Set 4 之張力 |
|---|---|---|---|
| **014** GPS Date/Time Broadcast | Set 2 `GPS Sync` | **transmit** GPS-based date/time signals | Set 4 四片動詞為 transmit(008) / validate-before-transmission(009) / transmit(017) / synchronize(020)。**014 與 008、017 同動詞** |
| **011** Time Format Handling | Set 5 `Display` | store, recall, and **broadcast** time format | broadcast 為傳輸動詞，與 Set 4 同軸 |

**執行層不主張改組。** 兩片之歸屬各有其正當理由：014 之資料源為 GPS
（分組軸為資料來源）、011 之標的為顯示格式（分組軸為能力對象）。
`02R` §2 之語意軸判準（先讀描述語意再看章節）支持現狀。

**但此構成第四、第五處潛在鄰接，而 §8.2.1 之界線表現僅列三處。**
具體風險：

- **014 ↔ 008 / 017**：三片皆「送出時間日期資料」。若無界線，B2（含 014）
  與 B3（含 017）、B1（含 008）之作者可能各寫一套傳輸驗證步驟
- **011 ↔ 008**：011 之 broadcast 與 008 之 transmit 皆涉 CAN 送出；
  011 送的是格式、008 送的是時間值，但兩者之 setup 可能重疊

**提請**：§8.2.1 之界線表是否補列此二處。屬 Tier 2（拘束條款之增修），
執行層不自行增補。

**時機**：B1 含 008、B2 含 014、B3 含 011 —— **三片分屬三個不同批次**，
故該界線若要補，宜在 B1 生成前定案，否則 B1 之 008 寫法將成為
既成事實而反過來拘束後兩批。

## 5. T8(4) — 該驗而未驗者（續用五全集）

### 5.1 依全集 1（指令逐項）

T1–T7 全數完成，無停下項。T7 七項全符（§1）。

### 5.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `docs/fw036/framework.md` | Part 數、`^## Part VII`、標頭、`tail -3` | 7 / 1 / 1 / Part VII 結尾 ✅ |
| `features/time_management/framework.md` | `head -6` | 作廢註記在首 ✅ |
| `RULINGS.md` | 條數 | 25 ✅ |
| `ANOMALIES.md` | 條數 + 索引列 | 17 / 17 ✅ |
| `data/leaf_descriptions.txt` | 列數 | 22 ✅ |

五處 `str.replace` 全部前置 `assert`，其中三處另加 `count == 1`
唯一性檢查（Part VII 兩處替換、標頭一處）。

### 5.3 本包解除之「未驗」項

**037 leaf 描述全文 —— 已於本包複驗，不再是單方實測。**
此為 `02R_corrections.md` §3.3 與 `03_signoff.md` §6.3 第 1 項所提請者，
現已關閉。`02R` §2 之語意複核與 §3.4 之三條界線**自此為雙方確認**。

### 5.4 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **§8.2.1 是否補列第四、五處鄰接** | **本包新發現**，見 §4.2，待裁 |
| 2 | A-TM17 併行者身分 | Tier 3，呈報 Pei，**執行層不查**（§3 明令不對 `vehicle_setting/` 作業）|
| 3 | R-TM22 解除條件 2 之受測物 | 未掃描。**執行層補充**：`inputs/` 於各 feature `.gitignore` 均被排除，故條件 (a)「`inputs/` 存在且非空」恐為最難滿足者，宜先掃全部 feature 之 `inputs/` 存在性再選。**本包未掃**（未獲指派，且掃描本身無風險，可於下包指派）|
| 4 | 交付路徑 Home 複本內容 | 刻意不驗（R-TM10-A1 SUSPENDED）|
| 5 | PU 陽性對照 | 待 Pei 裁（跨 feature 取用）|
| 6 | `write_back` 兩值 | Phase 3 |
| 7 | `1.5.3.*` 與 A-TM09 之關聯 | 分析層明言不主張，一致 |

### 5.5 依全集 4（「不存在」之陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| Part VII 先前不存在（本包新增） | 同一 grep 於改前列出 Part I–VI 共 6、改後 7 | ✅ |
| 本地 framework.md 先前無作廢註記 | `assert not t.startswith(">")` 前置，防重複插入 | ✅ |

### 5.6 依全集 5（草案設計說明之逐項可驗性）

`02R-A1` §2 之 Part VII 全文含多項斷言，本包貼入時**未逐項複驗**，
僅複驗其中三項（§4.1）。未驗者及其性質：

| 斷言 | 本包 |
|---|---|
| 「`features/home/` 與 `features/amfm/` 皆無 framework.md」（R-TM16 依據 2）| **未驗** —— 可驗，成本極低 |
| 「Part I 之六項跨領域裁決適用 ALL Test Groups」（依據 3）| **未驗** —— 需讀 Part I |
| Granularity check、先例引用（AMFM 注 2、SXM Browse、Privacy 注 2）| **未驗** —— 需讀他 Part |

**執行層判斷**：此三項為 R-TM16 之立論依據，而 R-TM16 已由 Pei 授權裁定
且本包已據以執行（Part VII 已併入）。**現在複驗不改變已執行之結果**，
但若依據不實，影響的是該裁定之正當性而非本包之動作。

**提請**：是否值得補驗第一項（`ls features/*/framework.md`，單一指令）。
執行層傾向補驗 —— 因其為「repo 內一例也沒有」之全稱斷言，而全稱斷言
被單一反例推翻，成本與風險不對稱。**本包未逕行**（未獲指派）。

## 6. 本包未動之事項

未動 git。**未改任何腳本**（R-TM22 HOLD）。**未對
`features/vehicle_setting/` 做任何寫入或腳本實跑**（A-TM17）。
未開始 B1 生成。**未刪除 `features/time_management/framework.md`**。
未 rm 任何檔案或目錄。未送出 RD-1。未填 `D5`、未組 Scope 值。
未援引他 feature 樣式。未以 openpyxl 存回任何工作簿。未跑 `recon.py`。
未改 Part I–VI 之任何內容。未自行增補 §8.2.1 之界線表。
