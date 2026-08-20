# 03Z — `03` 往返結案：R-TM16 依據訂正、兩條新界線、受測物候選

分析層。對應上繳 `docs/upstream/03R_corrections.md`。**受理，`03` 往返結案。**

---

## 1. R-TM16 依據 2 —— **經補驗為偽，依 R-TM13 訂正**

執行層提請補驗（`03R` 上繳提請 1）。分析層即刻實測，結果：**你是對的，
而且反例比預期嚴重。**

實測（2026-08-20，逐目錄列舉，非 glob）：

| feature | `framework.md` | 於全域檔之 Part |
|---|---|---|
| `home` | 無 | Part II |
| `amfm` | 無 | Part III |
| `sxm` | 無 | Part IV |
| `media` | 無 | Part I |
| `projection` | 無 | Part V |
| `privacy` | 無 | Part VI |
| **`comfort`** | **有** | **無 —— 全域檔無 Comfort Part** |

R-TM16 依據 2 稱「feature-local framework 檔在本 repo 一例也沒有」，
**為偽**。且 Comfort 不只是多一份本地檔 —— 它的 framework **只在本地**，
未併入全域檔。故「全域檔為 framework 之唯一位置」在本 repo 亦非全稱真。

### 1.1 結論保留，依據訂正

R-TM16 之**結論（本 feature 併入全域檔為 Part VII）不變**，因其另兩項
依據未受影響且為實質理由：

- 依據 1：全域檔現含六個 feature 之 framework —— 仍為真（本次實測再證）
- 依據 3：全域檔開頭明載 Part I 之六項跨領域裁決適用於 ALL Test Groups，
  落在檔外等同不受其拘束 —— **這是實質後果，不依賴依據 2**

**結論對而理由錯，理由一樣要改。** 依 R-TM13 加註訂正，不刪原文。

### 1.2 我犯的是我自己罵過的錯

「查了 `home` 與 `amfm` 兩個目錄，寫成『一例也沒有』」——
以雙點代全集，與 A-TM09 首版之代理判準、與拿 `home` 無 `inputs/` 推論
其他 feature（見 §4）同族。**本輪同一形態犯兩次。**

canon §5a 之「代理判準不得凌駕實質判準」我引用過三次來評執行層，
這次犯在自己的裁決依據上。

```
A-TM18（PENDING，Tier 2 —— 屬 Comfort，非本 feature）

`features/comfort/framework.md` 存在，而 `docs/fw036/framework.md`
無 Comfort Part。故 Comfort 之 framework 僅存於本地，與其餘六個 feature
之作法不一致。

兩種可能，本包不判定：
(a) Comfort 仍在進行中，尚未併入全域檔 —— 則屬正常中間狀態
(b) Comfort 採本地檔為最終形態 —— 則全域檔非唯一位置，R-TM16 之
    依據 3（Part I 跨領域裁決之拘束）在 Comfort 亦未生效

**本條僅登記，不裁 Comfort 之事。** 供 Comfort owner 覆核。
本 feature 之處置不受影響：Part VII 已併入，位置正確。
```

---

## 2. 第四、第五處鄰接 —— 採納，Part VII 界線表三條增為五條

執行層以「動詞軸橫掃全 22 列」發現 014 與 011 之主要動詞與
`CAN Transmission` 同型卻歸在別組。**方法正確**：先前之複核以語意軸分組，
未再以同一軸橫掃檢查跨組同型，這是分組之後該做而未做的一步。

其不主張改組亦正確 —— 014 之分組軸為資料來源、011 為能力對象，
02R 之語意軸判準支持現狀。**問題不在歸屬，在界線缺漏。**

**時機論證是本包最要緊的一句**：008 在 B1、014 在 B2、011 在 B3，
三片分屬三批。B1 若先寫成，008 之傳輸驗證寫法即成既成事實，
反過來拘束後兩批。故界線須在 B1 生成前定案。

```
R-TM23（分析層裁定，2026-08-20）—— Part VII §8.2.1 界線表增列第四、五條

界線 4 —— 014 GPS Date/Time Broadcast ↔ 008 Time Transmission on CAN
                                        ／ 017 Date Transmission

  014 驗 **GPS 來源值送出之正確性**：GPS 訊號組
      （$GPSDateTmHour/Minute/Second/Month/Day/Year$）之內容是否為
      GPS 導出之值。
  008 擁有**送出時機與觸發**：週期訊息、CAN wakeup、使用者更新後之重送，
      作用於主時間訊號 $DateTmHour/Minute$。
  017 擁有**日期通道**：TELEMATIC_TIME_DATE 與 TLM LIDs 至 IPC。

  → 014 之 TC **不重驗送出時機、不重驗傳輸通道**；
    008/017 之 TC **不重驗 GPS 來源值之正確性**。
  spec 依據：GPS 訊號組定義於 1.3.1.1.3（GPS TIME）與 1.5.2.5；
            傳輸時機定義於 1.3.1.1.4（Time Information Transmission）。
            兩者為不同章節所有，界線與 spec 結構一致。

界線 5 —— 011 Time Format Handling ↔ 008 Time Transmission on CAN

  011 驗 **格式訊號 $DateTmFormat$ 跨喚醒週期之保存與重送**：
      sleep→wake 後 recall last known format，並以該訊號送出
      （spec 物件 4813974，章節 1.3.1.1.5.1）。
  008 擁有**時間值**之傳輸。

  → 011 之 TC **不驗任何時間值之送出時機**；
    008 之 TC **不驗格式之保存與重送**。

兩條皆只窄化範圍、不新增主張，屬既有 §8.2.1 條款之同型延伸。
Part VII 之相鄰組界線表由三條增為五條。
```

**呈 Pei 覆簽**：R-TM17 之簽核標的為三條界線，本條增為五條。
增列不改變任何 Set 之組成，且只窄化不擴張，故分析層先行裁定使 B1 不受阻；
**若 Pei 認為增列須另簽，B1 之 008 相關 TC 須依覆簽結果重審。**

---

## 3. 021 字面差異 —— 記錄採納

037 原文：`maintain time using internal counters`
`02R` §2.1 簡寫式：`maintain internal {… counters}`（將 `internal` 前移）

語意同一，但**引用原文時會誤植**。此正是 §4「`test_item` 上半為逐字原文」
會踩到之處：分析層之整理式簡寫一旦被當成原文複製，即成偽逐字。

```
R-TM24（分析層自裁，2026-08-20）—— 整理式簡寫不得與逐字原文混用

分析層為論證所作之整理式簡寫（同義改寫、語序正規化），須與逐字引用
在形式上可區分：逐字引用加引號並註明來源欄位，簡寫不加引號並註明
「整理式」。

依據：02R §2.1 將 `maintain time using internal counters` 簡寫為
`maintain internal counters`，形式上與逐字引用無異，日後可能被複製為
`test_item` 上半之「原文」。
```

---

## 4. R-TM22 解除條件 2(a) —— 提請成立，掃描已做一半

執行層指出：`inputs/` 在各 feature 之 `.gitignore` 皆被排除，故「無
`inputs/`」很可能不是 `home` 獨有；選受測物前宜先掃全部 feature。

**成立，且我拿 `home` 單點推論其他 feature 之作法與 §1.2 同族。**

分析層本次順帶實測（逐目錄列舉）：

| feature | `inputs/` | `RECON.md` | `DECISIONS.md` | 受測物資格 |
|---|---|---|---|---|
| `sxm` | ✅ | ✅ | ✅ | **候選** |
| `privacy` | ✅ | ✅ | ✅ | **候選** |
| `comfort` | ✅ | ✅ | ✅ | **候選** |
| `projection` | ❌ | ✅ | ✅ | 不合格（無素材）|
| `media` | ❌ | ❌ | ❌ | 不合格 |
| `home` | ❌ | ✅ | ✅ | 不合格（無素材）|

**未掃者**：`power`、`user_profiles`、`vehicle_setting`。
前兩者本包指派掃描；`vehicle_setting` 依 A-TM17 一律不碰、不列候選。

R-TM22 2(a) 已可判定為**可滿足**（至少三個候選）。
2(c) 之靜止性須由執行層實測（相隔 ≥10 分鐘兩次 mtime 快照）。
**2 之解除仍須先過 1（A-TM17 釐清），順序不變。**

---

## 5. Pei 授權範圍之落檔

```
授權記錄（Pei, 2026-08-20「都照你的建議做」）

涵蓋：03R_review.md 之全部指令與其中之 R-TM16/20/21/22、
      A-TM01→MOOT、A-TM17 登記。

**不涵蓋**（無提案可批，非以「都」字推定）：
  - A-TM17 之內容 —— 該項為向 Pei 索取資訊（併行 session 之身分、
    `features/vehicle setting/` 之刪除是否為其所為），非可批准之處置。
    **截至本包，三次呈報未獲答覆**（01Z-A3 §6、03R §7、以及聊天層之直問）。
  - R-TM10-A1 之替代樣式來源 —— 分析層未提出任何候選。

依 03 §1.4 之同一紀律：無具體提案者不能被簽。
```

---

## 6. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — R-TM16 依據訂正（R-TM13：加註不刪）

於 `RULINGS.md` 之 R-TM16 條末尾追加，逐字：

```markdown
**依據 2 經補驗為偽（2026-08-20，執行層 03R 上繳提請 1）**

原依據 2 稱「`features/home/` 與 `features/amfm/` 目錄實測皆無
framework.md —— feature-local framework 檔在本 repo 不存在，一例也沒有」。

補驗（逐目錄列舉七個 feature）：**`features/comfort/framework.md` 存在**，
且 `docs/fw036/framework.md` 無 Comfort Part —— Comfort 之 framework
僅存於本地。故該全稱斷言為偽，「全域檔為唯一位置」在本 repo 亦非全稱真。

**結論不變**：本 feature 併入全域檔為 Part VII 仍為正確處置，
依據 1（全域檔現含六個 feature 之 framework）與依據 3（Part I 之六項
跨領域裁決適用於 ALL Test Groups，落在檔外即不受其拘束）未受影響，
且依據 3 為實質理由。

**成因記錄**：原裁定僅查兩個目錄即寫成全稱斷言，屬以雙點代全集，
與 canon §5a 所禁之代理判準同族。Comfort 之不一致另記 A-TM18。
```

### T2 — `RULINGS.md`：追加 R-TM23、R-TM24

標題行分別為：

```
## R-TM23 — Part VII §8.2.1 界線表增列第四、五條
## R-TM24 — 整理式簡寫不得與逐字原文混用
```

內文為本包 §2 / §3 之區塊全文。
追加後 `## R-TM` 條數應為 **27**（25 + 2）。

### T3 — `ANOMALIES.md`：新增 A-TM18

內容為本包 §1.2 之區塊全文。索引追加：

```markdown
| A-TM18 | Comfort 之 framework 僅存本地、未併入全域檔 | PENDING | Tier 2（屬 Comfort）|
```

索引條數 17 → **18**。

### T4 — Part VII 界線表更新

`docs/fw036/framework.md` Part VII 之
`### 相鄰組界線（§8.2.1 —— 寫 TC 時據此避免重複覆蓋）` 節，
於現有三列之後追加兩列：

```markdown
| 014 GPS Date/Time Broadcast ↔ 008 Time Transmission / 017 Date Transmission | 014 驗 GPS 來源值送出之正確性（`$GPSDateTm*$` 訊號組內容，1.3.1.1.3 / 1.5.2.5）；008 擁有送出時機與觸發（1.3.1.1.4）、017 擁有日期通道（TELEMATIC_TIME_DATE + TLM LIDs）。**014 不重驗時機與通道；008/017 不重驗 GPS 來源值** |
| 011 Time Format Handling ↔ 008 Time Transmission | 011 驗 `$DateTmFormat$` 跨喚醒週期之保存與重送（物件 4813974，1.3.1.1.5.1）；008 擁有時間**值**之傳輸。**011 不驗時間值送出時機；008 不驗格式保存與重送** |
```

並將該節標題下方之引言（若有「三處鄰接」字樣）改為「五處鄰接」。

`assert old in text` 前置，`replace(old, new, 1)`，改後複查（R-TM11）。

### T5 — `inputs/` 掃描補完

```bash
for f in power user_profiles; do
  printf '%s: ' "$f"
  test -d "features/$f/inputs" && printf 'inputs=Y ' || printf 'inputs=N '
  test -f "features/$f/RECON.md" && printf 'RECON=Y ' || printf 'RECON=N '
  test -f "features/$f/DECISIONS.md" && printf 'DECISIONS=Y\n' || printf 'DECISIONS=N\n'
done
```

**不掃 `vehicle_setting`**（A-TM17）。結果併入 §4 之候選表回報。

### T6 — 驗證（唯一定錨，R-TM21）

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md              # 期望 27
grep -c '^## A-TM' features/time_management/ANOMALIES.md            # 期望 18
grep -n '依據 2 經補驗為偽' features/time_management/RULINGS.md       # 期望 1 處
grep -c 'GPSDateTm' docs/fw036/framework.md                         # 期望 ≥1（本 feature 唯一字串）
grep -c '4813974' docs/fw036/framework.md                           # 期望 ≥1（同上）
ls features/comfort/framework.md                                    # 反例存在之複驗
```

任一不符即回報並停。

### T7 — 上繳

`docs/upstream/03Z_corrections.md`，僅差異。須含：

1. T6 六項實際輸出
2. T4 之改前／改後實際字串
3. T5 之掃描結果
4. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git
- **不改任何腳本**（R-TM22 HOLD，未解除）
- **不碰 `features/vehicle_setting/`**（A-TM17）
- **不開始 B1 生成** —— 待本包上繳覆核，且 R-TM23 若經 Pei 覆簽有變更，
  008 相關 TC 須依覆簽結果重審
- 不裁 Comfort 之事（A-TM18 僅登記）
- 不刪除 `features/time_management/framework.md`
- 不送出 RD-1（Tier 3）
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不跑 `recon.py`（A-TM15 未修）

---

## 7. 呈報 Pei

| # | 事項 | 狀態 |
|---|---|---|
| 1 | **A-TM17 —— 併行 session 身分** | **三次呈報未獲答覆。** `features/vehicle setting/` 是否為你（或你開的另一 session）所刪？git 從未追蹤故不可復原；若非你所為，repo 有未受控之刪除行為，`features/vehicle_setting/` 與交付件暴露於同一風險 |
| 2 | R-TM23 兩條新界線是否須另簽 | R-TM17 之簽核標的為三條，現為五條。增列只窄化不擴張，分析層先行裁定使 B1 不受阻 |
| 3 | R-TM10-A1 替代樣式來源 | 仍無候選，SUSPENDED |
| 4 | RD-1 Q-TM1–3 | 已落 `docs/fw036/RD1_questions_time_management.md`，送出屬你 |

## 8. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM16 依據訂正 | 依 R-TM13 加註，結論不變 | §1.1 | ✅ T1 |
| R-TM23 | 分析層裁定，界線增列第四、五條 | §2 | ✅ T2 + T4 |
| R-TM24 | 分析層自裁，簡寫與逐字須可區分 | §3 | ✅ T2 |
| A-TM18 | anomaly，PENDING，Tier 2（屬 Comfort）| §1.2 | ✅ T3 |
| Pei 授權範圍記錄 | 授權事件落檔 | §5 | ✅ 本檔即落檔處 |

分析層本包未動 git、未改腳本、未寫 `docs/fw036/`（T4 為執行層）、
未觸 `vehicle_setting/`。
§1 與 §4 之目錄實測為 2026-08-20 對 repo 實際路徑之逐目錄列舉，非 glob。
