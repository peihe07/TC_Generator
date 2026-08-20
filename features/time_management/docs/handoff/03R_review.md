# 03R — 覆核：四項停下全數成立，根因為分析層違反往返紀律

分析層。覆核對象：`docs/upstream/02R_corrections.md`、`docs/upstream/03_signoff.md`。

**結論：四項停下全數正確，無一項需要翻案。** R-TM16 之「缺號」不是缺號，
是分析層違反「一批一上繳」所造成的必然結果，說明於 §1。
`vehicle setting` 滅失與 git race 之處置見 §3，**呈報 Pei，本包不推進**。
腳本修法（T4/T5）**由分析層主動改判為 HOLD**，理由見 §4。

---

## 1. R-TM16 缺號之根因 —— 分析層連開兩包未待上繳

實測（2026-08-20）：

| 事實 | 量測 |
|---|---|
| `docs/handoff/02R-A1_framework_merge.md` | **存在於磁碟**（14,415 bytes，18:15 寫入）|
| `docs/fw036/framework.md` 檔尾 | Part VI Privacy 之結尾句，**無 Part VII** |
| `RULINGS.md` 條數 | 21（執行層實測），R-TM16 不在其中 |

R-TM16 由 `02R-A1` 之 T4 指派。**該包從未被執行**，故：

- Part VII 不存在 → `03` T2 之兩個目標字串零命中
- R-TM16 未落檔 → 編號在 16 斷開
- `02R` T3（不寫全域檔）與 `03` T2（改全域檔 Part VII）相反 ——
  因為中間那包（`02R-A1`，撤銷 T3、裁定併入）沒跑

**這不是跳號或計數誤植，是我的排程錯誤。** Project charter 明訂
「一批一上繳；前批未覆核不得開下批」。我違反兩次：`02R` 之上繳尚未回來
就發 `02R-A1`；`02R-A1` 之上繳尚未回來就發 `03`。三包疊在同一個未結的
往返上，後包依賴前包之產物而前包從未執行。

執行層依 `02R`（較早且理由完整）不動全域檔 —— **在收到相反指示而無仲裁
資訊時，取較早且理由完整者，是正確的處置**。

```
R-TM20（分析層自裁，2026-08-20）—— 下放包不得依賴未上繳之前包

分析層在前一包之上繳回來並經覆核前，不得發下一包。
若情況變更必須追發，該追發包須：
1. 於首節明列其所依賴之前包編號與**該前包尚未上繳**之事實
2. 將被依賴之指令原文併入本包，使本包自足可執行
3. 不得以「前包已指派」為由省略任何步驟

依據：02R → 02R-A1 → 03 三包連發，02R-A1 從未執行，導致 03 之 T2
目標不存在、R-TM16 編號斷裂、02R 與 03 對同一檔案給出相反指示。
執行層無從判斷何者有效，只能停下 —— 停對了，成本卻已產生。
```

### 1.1 `03` T6 判準 3、4 之假通過 —— 執行層自查正確，判準是我設計壞的

`grep -n '待簽'`（本就不存在，非清除所致）與 `grep -n 'B1（pilot）'`
（命中 2 處屬 Part VI Privacy 之批次表）**跑在一個七 feature 共用的檔案上，
沒有任何本 feature 定錨**，故必然假通過。

此自查與 `01Z` 之雙空格自查、`02` 之「章節證據無鑑別力」同族：
**檢查項須確認其在該階段確實可能失敗**（charter 明文），我三次寫出不可能
失敗的判準。

```
R-TM21（分析層自裁，2026-08-20）—— 跨 feature 共用檔之驗證判準須唯一定錨

驗證指令若跑在跨 feature 共用檔（docs/fw036/framework.md、
docs/runtime/*、scripts/* 等）上，其比對字串須含本 feature 之唯一識別
（`Part VII`、`Time and Date`、`SWE-RA-TIME&DATE` 等），不得使用
`待簽`、`B1（pilot）`、`pilot` 一類他 Part 亦有之泛用字串。

判準寫成後須自問：「本 feature 之工作若完全沒做，本判準會不會照樣通過？」
會 → 判準無效，重寫。

依據：03 T6 判準 3、4，執行層識破為假通過。
```

## 2. `02R` 四項驗證全符 —— 受理

`RULINGS.md` 18 條（含 R-TM14/R-TM15）、`ANOMALIES.md` 16 條、
A-TM13 下游影響已補、`features/time_management/framework.md` 已建。

該本地 framework 檔依 `02R-A1` R-TM16 應轉為作廢註記；但**其內容（七組、
Layer 1/3、三條界線）目前是簽核內容之唯一落檔處**，故 §5 之指令改為
「先併入全域檔，確認 Part VII 落地後，再於本地檔加作廢註記」，
順序不可顛倒 —— 否則會出現簽核內容無處可查的空窗。

## 3. `vehicle setting` 滅失 + git race —— **呈報 Pei，本包不推進**

執行層實測：原路徑不存在、`archive/` 內無、全 repo `os.walk` 零命中、
`git log --all` 從未追蹤過 → **形態為 rm 而非 mv，且不可復原。**
本 session 對該路徑只做過 `ls` 與 `git check-ignore`。

分析層獨立佐證：`features/vehicle_setting/ANOMALIES.md` 之 mtime 實測為
**16:51:28**，落在本 session 期間，而本 session 從未寫入該檔。
併行 session 確實存在且正在寫入。

**A-TM01 不得標 RESOLVED。** 執行層之理由成立且重要：若標了，等於用
「處置條文 R-TM18」記載一件與該條文不符之事實（R-TM18 明令只 mv 不 rm、
archive 內容須逐檔可讀，現況只滿足前半）。**這正是 R-TM13 所防之情形。**

處置（§5 T4）：A-TM01 標 `MOOT — 目標已滅失，非依 R-TM18 處置`；
R-TM18 依 R-TM13 加註「未能執行，目標於指派前已被他方刪除」，條文保留；
另立 A-TM17 登記滅失事件本身。

```
A-TM17（PENDING，Tier 3 —— 呈報 Pei）—— repo 內有身分不明之併行寫入者

三個獨立事實，時序相連：

1. （01Z-A3 §6 已報，Pei 未回覆）`features/vehicle_setting/` 於 session
   開始時整個 untracked，其後除 `docs/handoff/02_coverage_baseline_
   correction.md` 外似被 add 過。本 session 未動 git。
2. `features/vehicle_setting/ANOMALIES.md` mtime 16:51:28、`data/` 16:49，
   落在本 session 期間；本 session 未寫入該目錄任何檔案。
3. `features/vehicle setting/`（含空格）於 R-TM18 指派前已從磁碟消失，
   非 mv 至 archive，全 repo 零命中，git 從未追蹤故不可復原。

三者可能同源。**分析層與執行層皆未執行任何刪除或 git 操作。**

在併行者身分與作業範圍釐清前：
- 不對任何跨 feature 共用檔（scripts/、docs/fw036/、docs/runtime/、
  forms/）執行寫入以外之破壞性操作
- 不對 features/vehicle_setting/ 執行任何寫入或腳本實跑
- 腳本修法 HOLD（見 R-TM22）

呈報 Pei 之具體請求：確認另一 session 之身分與作業範圍；確認
`features/vehicle setting/` 之刪除是否為其所為（若是，事件關閉為已知；
若否，則 repo 有未受控之刪除行為，須先查明再繼續）。
```

## 4. 腳本修法 —— 分析層主動改判 HOLD

執行層之三個理由全部成立，尤以第 1 項為要：**「RECON.md 逐位元相同」
在受測目錄同時被他人編輯時，diff 有輸出無法區分成因** —— 判準失去鑑別力，
這與 R-TM21 是同一件事（判準須在該情境下真能鑑別）。

其建議之「改用其他 feature 當回歸對象」方向正確，但**分析層不逕採**：
`features/home/` 實測無 `inputs/` 目錄（gitignored，內容不在磁碟），
recon.py 對其未必跑得起來；其餘 feature 之靜止性亦未量測。
依 R-TM7，我不指定一個沒量過的受測物。

且更根本的一層：A-TM17 之刪除事件未釐清前，**改動全 feature 共用之腳本
本身就不該做**。這符合我自己訂的升級門檻（不可逆操作、跨 feature 影響）。

```
R-TM22（分析層自裁，2026-08-20）—— R-TM19 階段一、二 HOLD

R-TM19 之授權不撤銷，執行時機 HOLD。解除條件（兩項均須）：

1. A-TM17 釐清 —— Pei 確認併行 session 之身分與作業範圍，且
   `features/vehicle setting/` 之刪除有解釋
2. 回歸受測物經量測選定 —— 候選須同時滿足：
   a. `inputs/` 目錄存在且非空（recon.py 需其素材）
   b. `RECON.md` 與 `DECISIONS.md` 皆存在
   c. 靜止性：相隔 ≥10 分鐘取兩次 mtime 快照，全目錄無變動
   選定前 `/tmp` 備份該 feature 之 `DECISIONS.md` 與 `RECON.md`

R-TM19 之階段順序（A-TM15 最先）不變。
```

## 5. 037 leaf 描述 —— 提請成立，本包指派

執行層指出：`02R` §2 之全部語意複核（Set 3 維持五筆、Set 7 成組、
三條相鄰界線）建立在 `Requirement Description` 欄，**由分析層單方讀取**；
而 R-TM17 已把三條界線定為 §8.2.1 拘束條款，B1 生成時逐條適用。

**成立。** 未經雙方確認之單方讀取，不應成為生成時的拘束條款。
成本確如其所述極低（單欄 22 列唯讀）。此與 `01Z-A4` 之三個 037 檔名複驗
同型 —— 該次亦是執行層提請、分析層指派、結果相符。

---

## 6. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — Part VII 併入全域檔（**已含簽核後措辭與批次表，一次寫定**）

本步驟合併 `02R-A1` T2 與 `03` T2 —— 依 R-TM20，被依賴之指令併入本包，
不再要求先跑舊包。**不要先寫「待簽」再改**。

貼入前先 assert 檔尾：

```bash
tail -1 docs/fw036/framework.md
# 須為：查證（Tier 1）；若有，填入三個 Set 名稱，否則逐列欄位即足（AMFM 先例）。
```

確認後，將 **`docs/handoff/02R-A1_framework_merge.md` §2 之區塊全文**
追加至 `docs/fw036/framework.md` 檔尾，並於追加時做兩處替換：

| 位置 | 02R-A1 §2 原文 | 改為 |
|---|---|---|
| Part VII 開頭 | `下列七 Set 表待簽。` | `下列七 Set 表經 Pei 2026-08-20 簽核（R-TM17）。` |
| `### Batch plan` 段 | `**未定。** 待 Layer 2 經 Pei 簽核後另行起草。` | `docs/handoff/03_signoff.md` §3 之批次表全文（含 B1 取樣依據與 B2 集中依據兩段）|

### T2 — 全域檔標頭

第 3–6 行之 Covers 句，以檔案實際換行為準，將
`**Privacy** (Part VI, end of file)` 改為
`**Privacy** (Part VI), and **Time and Date** (Part VII, end of file)`。

`assert old in text` 前置，`replace(old, new, 1)`，改後複查（R-TM11）。

### T3 — 本地 framework 檔加作廢註記（**T1 完成後才做**）

確認 `docs/fw036/framework.md` 已含 Part VII 後，於
`features/time_management/framework.md` 檔首插入：

```markdown
> **⛔ 本檔作廢（2026-08-20，R-TM16）。**
> framework 之唯一位置為 `docs/fw036/framework.md`（Part VII）。
> 本檔係 `02R_framework_lock.md` T3 之誤指派所建，該指派已由 R-TM16 撤銷。
> 內容以全域檔為準，本檔不再維護，保留為軌跡（R-TM13）。
```

**不刪除本檔。** 順序不可顛倒 —— T1 未完成前本檔是簽核內容之唯一落檔處。

### T4 — `ANOMALIES.md`

**(a) A-TM01** 索引狀態改 `MOOT`，條文末尾追加：

```markdown
**處置（2026-08-20）—— MOOT，非依 R-TM18 完成**

R-TM18 指派將 `features/vehicle setting/` mv 至 `archive/`。執行時實測：
原路徑不存在、`archive/` 內無、全 repo `os.walk` 零命中、
`git log --all` 從未追蹤過 → 形態為 **rm 而非 mv，不可復原**。
分析層與執行層皆未執行任何刪除。

R-TM18 之「archive 內容須逐檔可讀」無法滿足，故**不標 RESOLVED** ——
標了等於以處置條文記載一件與該條文不符之事實（R-TM13 所防之情形）。

狀態改 **MOOT — 目標已滅失**。刪除事件本身另立 A-TM17。
```

**(b) A-TM17** 新增，內容為本包 §3 之區塊全文。索引追加一列：

```markdown
| A-TM17 | repo 內有身分不明之併行寫入者（含 `vehicle setting` 滅失、git race）| PENDING | Tier 3（呈報 Pei）|
```

索引條數 16 → **17**。

### T5 — `RULINGS.md`：追加 R-TM16、R-TM20、R-TM21、R-TM22

**R-TM16 補號**：內容取 `docs/handoff/02R-A1_framework_merge.md` §1 之
區塊全文，標題行 `## R-TM16 — framework 併入全域檔`。
**編號不重排** —— R-TM16 遲到而非不存在，補在 R-TM19 之後、以標題註明
`（追補：本條原由 02R-A1 指派，該包未執行，2026-08-20 補落）`。

R-TM20 / R-TM21 / R-TM22 依本包 §1 / §1.1 / §4 之區塊全文追加。

**R-TM18 依 R-TM13 加註**（不刪除條文），於其末尾追加：

```markdown
**未能執行（2026-08-20）**：目標 `features/vehicle setting/` 於本條指派前
已被他方自磁碟刪除，非 mv，不可復原。本條之處置無標的可施。
條文保留為軌跡。事件見 A-TM17。
```

追加後 `## R-TM` 條數應為 **25**（21 + R-TM16/20/21/22）。

### T6 — 037 leaf 描述之獨立複驗（§5）

```bash
python3 - <<'PY' > features/time_management/data/leaf_descriptions.txt
import openpyxl, pathlib
F = pathlib.Path("features/time_management/inputs")
a03 = next(F.glob("SWE1*.xlsx"))
wb = openpyxl.load_workbook(a03, read_only=True, data_only=True)
ws = wb["Analysis Report"]
hdr = list(ws.iter_rows(min_row=8, max_row=8, values_only=True))[0]
print("col3 header:", repr(hdr[2]))
print("col4 header:", repr(hdr[3]))
n = 0
for r in ws.iter_rows(min_row=9, values_only=True):
    if not r[0]:
        continue
    n += 1
    print(f"{str(r[0]).strip()} | {str(r[2]).strip()}")
    print(f"    {str(r[3]).strip()}")
wb.close()
print("rows:", n)
PY
cat features/time_management/data/leaf_descriptions.txt
```

回報全 22 列，並就下列**分析層之三項主張**逐項判定支持／不支持：

1. **Set 3 五片同語意軸**：005 / 006 / 016 / 021 之描述動詞受詞為
   `maintain internal {clock / time signal / calendar / counters}`，
   018 為該內部狀態之初始化
2. **Set 7 成組**：010 為收端（用最後有效值），022 為送端（發 SNA/預設值）
3. **三條相鄰界線**：004↔010 觸發源不同；014 描述含 `or SNA if unavailable`
   而 SNA 送出規則屬 022；018 管時間日期預設值、011 管格式跨喚醒週期

**任一項不支持即回報並停** —— R-TM17 已將三條界線定為 §8.2.1 拘束條款，
不支持即代表拘束條款須改，屬 Tier 2。

### T7 — 驗證（**唯一定錨，R-TM21**）

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md        # 期望 25
grep -c '^## A-TM' features/time_management/ANOMALIES.md      # 期望 17
grep -n '^## Part VII' docs/fw036/framework.md                # 期望恰 1 處
grep -c 'SWE-RA-TIME&DATE' docs/fw036/framework.md            # 期望 ≥1（本 feature 唯一字串）
grep -n 'Part VII, end of file' docs/fw036/framework.md       # 標頭，期望 1 處
grep -n '本檔作廢' features/time_management/framework.md        # 期望 1 處
grep -c '^SWE-RA-TIME&DATE' features/time_management/data/leaf_descriptions.txt  # 期望 22
```

任一不符即回報並停。

### T8 — 上繳

`docs/upstream/03R_corrections.md`，僅差異。須含：

1. T7 七項結果（實際輸出，非「相符」二字）
2. T1 之 assert 結果與兩處替換之改前／改後
3. T6 之 22 列全表 + 三項主張之逐項判定
4. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git
- **不改任何腳本**（R-TM22 HOLD）
- **不對 `features/vehicle_setting/` 做任何寫入或腳本實跑**（A-TM17）
- **不開始 B1 生成**（待 T6 三項主張確認）
- 不刪除 `features/time_management/framework.md`
- 不 rm 任何檔案或目錄
- 不送出 RD-1（Tier 3）
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不以 openpyxl 存回任何工作簿
- 不跑 `recon.py`（A-TM15 未修）

---

## 7. 呈報 Pei

| # | 事項 | 為何要你 |
|---|---|---|
| 1 | **A-TM17 —— 併行 session 身分未明** | git race（01Z-A3 §6 已報未覆）+ `vehicle_setting` 於 16:49/16:51 被他方寫入 + `vehicle setting` 被 rm 且 git 從未追蹤故不可復原。三者可能同源。**在釐清前腳本修法 HOLD。** 若刪除非該 session 所為，repo 有未受控之刪除行為 |
| 2 | R-TM10-A1 替代樣式來源 | 仍無候選，維持 SUSPENDED |
| 3 | RD-1 Q-TM1–3 | 草案已落 `docs/fw036/RD1_questions_time_management.md`，送出屬你 |

## 8. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM16（追補） | 裁決，framework 併入全域檔 | 引 02R-A1 §1 | ✅ T5 |
| R-TM20 | 分析層自裁，不得依賴未上繳之前包 | §1 | ✅ T5 |
| R-TM21 | 分析層自裁，共用檔判準須唯一定錨 | §1.1 | ✅ T5 |
| R-TM22 | 分析層自裁，R-TM19 階段一二 HOLD | §4 | ✅ T5 |
| R-TM18 加註未能執行 | 依 R-TM13 保留加註 | §3 | ✅ T5 |
| A-TM01 → MOOT | anomaly 狀態變更 | §3 | ✅ T4(a) |
| A-TM17 | anomaly，PENDING，Tier 3 | §3 | ✅ T4(b) |
| Part VII 併入 + 批次表 | 簽核內容落全域檔 | §6 T1 | ✅ T1 + T2 |

分析層本包未動 git、未改腳本、未寫 `docs/fw036/`、未觸 `vehicle_setting/`。
