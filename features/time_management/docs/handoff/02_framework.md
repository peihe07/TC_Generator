# 下放包 02 — Time Management：01Z-A4 覆核 + framework Part N 草案

分析層 → 執行層。往返編號 `02`。對應上繳
`docs/upstream/02_framework.md`。

`01Z-A4` 上繳受理，`01` 往返全部結案。本包含三部分：
§1 覆核與三項裁決、§2 framework Part N 草案（待 Pei 簽）、§3 指令。

---

## 1. 對 `01Z-A4_corrections.md` 之覆核

### 1.1 §3 之偏離 —— **採納執行層之作法，指令有誤在我**

T4 寫「整段換為」，執行層改為加刪除線 + 區塊引言標明作廢並保留。
**執行層正確，指令錯誤。**

理由如其所述且與本專案既有作法一致：A-TM09 §D 保留首版錯誤數字與其
論證缺陷、R-TM9／R-TM10 原文於被撤銷／暫停後全文保留、A-TM12 首版兩案
保留、T6 自身明令「上繳包是軌跡，不回頭改」。我在 T4 寫「整段換為」是
與這些作法直接矛盾的措辭。

且其補充理由成立且我未想到：**該段記載的是一個被證否的推理，而執行層
在有 Home 樣本可比對的情況下仍做了同一個誤讀，這件事本身就是 A-TM16
的佐證** —— 刪掉就把這個訊號消掉了。

```
R-TM13（分析層自裁，2026-08-20）—— 條文之作廢一律加註保留，不刪除

任何已寫入 RULINGS.md／ANOMALIES.md 之條文、提案或推理，經證否或撤銷後
一律保留原文，加刪除線並以區塊引言標明作廢時點、依據包、與作廢理由。
下放包不得使用「整段換為」「刪除該段」等措辭。

被證否的推理本身是證據：它記錄了誤讀曾經發生，而誤讀之可重複性
（不同人在有對照樣本時仍犯同一錯）是判斷該問題嚴重性的訊號。

依據：01Z-A4 T4 之措辭與本專案既有作法矛盾（A-TM09 §D、R-TM9／R-TM10、
A-TM12 首版、T6 自身）。執行層於 01Z-A4 上繳 §3 指出之。
本條與 R-TM11／R-TM12 同族：三者皆為下放包自身之缺陷。
```

### 1.2 §4 A-TM02a 未升級 —— **我的指派缺口**

`01Z-A3` §3.1(c) 與 §8(1) 都寫了 A-TM02a 已升為阻塞項，而 `01Z-A4`
的 T1–T5 沒有一項指派去改那條條文與索引。**A4 漏了。**
執行層未逕改、僅提請，符合「範圍不自行擴大」，正確。

本包 §3 T1 補上指派，建議之改法照執行層所提。

### 1.3 §6.4 第 1 項 —— **提請成立，本包指派**

「A-TM16 之全部論證建立在三個 037 檔名形態一致之上，而執行層未複驗，
僅轉述」—— 此自我指認正確，且與 `00Z` §2 所立之常態（上游給的數字同樣
受查證義務拘束）一致。

其對禁令射程之推理亦正確：A4「不得開啟交付路徑之 Home 複本檢查其內容」
所禁者為**開啟檔案**，目錄列舉不在其內；但未經指派即擴大掃描範圍與禁令
意旨不合，故不逕行而提請 —— 這是對禁令的正確讀法。

本包 §3 T2 指派以純 `ls` 複驗。**在複驗完成前，A-TM16 之結論確為單方
實測**，此標示準確。

### 1.4 其餘

- §5 之附加限制（`repr()` 取自 archive 複本，而 A-TM14 已載其身分不確定，
  故只能證明「archive 那一份的 D5 是這個值」）—— **採納**。A4 未要求而
  執行層主動加註，且理由正確：不加註會讓 A-TM16 讀起來比其證據更確定。
- §6.5 之「本包無適用對象，如實記為無適用而非已檢查且無問題」——
  **這是「無」的正確寫法**。與 `01Z` 上繳之「037 leaf 無缺號，依據為
  22 列全集列舉」同為正確形態，兩者形態不同但都交代了依據。
- 四處 `str.replace` 全面加 `assert old in t` —— A-TM15 之教訓已內化為
  作法，非僅記錄。

---

## 2. framework Part N 草案（**[PROPOSED]，待 Pei 簽，Tier 2**）

依 canon §4.1。本節為草案，**未經 Pei 簽核前不得據以生成任何 TC**。

### 2.1 Layer 1 — Test Group

```
Test Group = "Time and Date"
```

依 R-TM8，已裁定，非提案。

### 2.2 Layer 2 — Test Set（7 組，[PROPOSED]）

取 037 之 22 筆 leaf 標題與 CFTS015 之章節結構之交集。每筆 leaf 恰屬
一組，無重複、無遺漏。

| # | Test Set | leaf | 數 |
|---|---|---|---|
| 1 | `Manual Setting` | 001 Manual Time Setting、015 Manual Date Handling | 2 |
| 2 | `GPS Sync` | 002 GPS Sync Enable/Disable Logic、003 GPS Time Calculation、004 GPS Fallback Handling、014 GPS Date/Time Broadcast | 4 |
| 3 | `Master Clock` | 005 Internal Clock Accuracy、006 Internal Time Representation、016 Date Master Function、018 Default Initialization、021 Sleep/Wakeup Handling | 5 |
| 4 | `CAN Transmission` | 008 Time Transmission on CAN、009 Time Signal Validation、017 Date Transmission、020 IPC Synchronization | 4 |
| 5 | `Display` | 007 Time Display Handling、011 Time Format Handling、019 Proxi-Based Behavior | 3 |
| 6 | `Zone and DST` | 012 Time Zone Handling、013 DST Handling | 2 |
| 7 | `Fault Handling` | 010 Invalid Data Handling、022 SNA Handling | 2 |

**合計 22，與 leaf 全集相等。**

設計說明（供 Pei 判斷）：

- **不以時間／日期二分**。若切成 Time / Date 兩組，`Master Clock` 與
  `CAN Transmission` 之每一項都要在兩邊各出現一次，Test Set 欄會失去
  索引價值（§4.1.3「太粗」）。時間與日期在本 spec 中共用主控、共用傳輸、
  共用初始化，是同一能力之兩個資料欄位，不是兩種能力。
- **`Master Clock` 吸收 021 Sleep/Wakeup**。021 之內容為睡眠期間以內部
  計數器維持時間，與 005（內部時鐘精度）、006（內部時間表示）同屬內部
  計時能力。單獨成組會產生 §4.2 所禁之單需求 Test Set，而 021 不是
  outlier。
- **`Display` 含 019 Proxi-Based Behavior**。019 之內容為依 Proxi 參數
  啟用／停用時間日期功能，其可觀察面即顯示與否，與 007／011 共用同一
  UI 進入路徑（§4.2「同一 Test Set 應蘊含共用之 setup 與 UI 進入路徑」）。
  **此為七組中最不確定的一項**，若 Pei 認為 019 應獨立或歸入
  `Master Clock`，請直接改。
- **`Fault Handling` 只有 2 筆但為真 outlier**：010（無效／遺失訊號之
  處理）與 022（SNA／預設值）都是異常路徑，與任何正常路徑能力合併都會
  讓該組同時含正常與異常兩種 setup。

### 2.3 Layer 3 — 章節分組（**未鎖定，須先綁實測**）

canon §4.1.1 之 Layer 3 為 framework 內部之章節分組，不寫入工作簿。

**分析層目前無法產出可鎖定之 Layer 3。** 理由：Layer 3 須為
「leaf → spec 章節」之分組，而該對映之實測資料尚未產出 ——
`data/anchor_probe.txt` 現有者為 **SYS-RA → 章節**，非 **SWE leaf → 章節**。
兩者差一層（037 之 leaf 各引用數筆 SYS-RA）。

**不以推測填補**（§8.4.1）。本包 §3 T3 指派由現有資料推導該對映並回報，
Layer 3 於其回報後、與 §2.2 之七組比對通過，方鎖定。

**比對之用途**：若某 Test Set 之 leaf 散落於彼此無關之章節群，
即為 Layer 2 切錯之訊號（§4.1.4 第 4 用途）。此比對是七組草案唯一的
外部檢驗，故不可略過。

已知之外部事實（`anchor_probe.txt`，21 個可達章節）：全部落在
`1.3.1.*`（PNet/CUSW/AtlHi 共通）與 `1.5.2.*`（LTM）兩支，
**`1.5.3.*`（ETM）零命中**。此現象與 A-TM09 之 48 筆缺口可能相關，
但兩者是否同源尚未查證，**不在本包主張之列**。

---

## 3. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — A-TM02a 條文與索引升級

索引表該列整列換為：

```markdown
| A-TM02a | 037 之版本身分未定（原 A-TM02，經 R-TM6 分拆）—— **阻塞 D5 交付欄位** | PENDING | Tier 3（隨 RD-1 上問）|
```

A-TM02a 條文末尾追加，逐字：

```markdown
**性質升級（2026-08-20，依 `docs/handoff/01Z-A3_review.md` §3.1(c)）**

本條由「上游版本問題」升為 **阻塞交付欄位**。

036 工作簿之 `D5`（範圍 Scope）欄，其語意為「本工作簿所依據之 037 報告
之文件識別」，值即該 037 檔名去副檔名（R-TM9-A2）。交付路徑實測：

| 目錄 | 037 檔名 |
|---|---|
| `Core HMI/HomeHMI/` | `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx` |
| `Core HMI/Menu Bar and AppDrawer/` | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx` |
| `User Profiles/` | `FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` |
| `Time Management/` | **無任何符合該形態之檔案** |

本 feature 手上之 037 名為 `SWE1_Secure_Date&Time.xlsx`，不符該形態。
故 D5 在本條裁定前**無值可填**（非「暫緩填」）。

RD-1 應問：`Time Management` 是否另有正式 037，或
`SWE1_Secure_Date&Time.xlsx` 即是而命名未依慣例。
```

### T2 — 三個 037 檔名之複驗（**純目錄列舉，不開啟任何檔案**）

```bash
BASE="/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2"
ls "$BASE/Core HMI/HomeHMI/"
ls "$BASE/Core HMI/Menu Bar and AppDrawer/"
ls "$BASE/User Profiles/"
ls "$BASE/Time Management/"
```

回報四個目錄之完整列出結果。判準：前三者各應有恰一個
`FM-WI-FSM-037-A03-N1L-SWE1-*-HMI-V0.1 STLA 報告.xlsx`；
第四者應無任何 `FM-WI-FSM-037-*` 檔案。

**不符即回報並停**，不自行調整 A-TM16 之措辭。
相符則於 A-TM16 之來源限制註記後追加一行：

```markdown
**（2026-08-20）執行層以純目錄列舉獨立複驗三個 037 檔名，與分析層實測相符。
本條之檔名形態論證自此為雙方確認，非單方實測。**
```

**不得開啟任一檔案。**

### T3 — SWE leaf → 章節對映（Layer 3 之實測基礎）

```bash
python3 - <<'PY' > features/time_management/data/leaf_to_section_probe.txt
import re, openpyxl, pathlib, collections
F = pathlib.Path("features/time_management")
a03 = next(F.joinpath("inputs").glob("SWE1*.xlsx"))
sys2 = next(F.joinpath("inputs").glob("SYS2*.xlsx"))

# SYS-RA number -> section, re-derived from the same sources as anchor_probe
import zipfile, html
docx = next(F.joinpath("inputs").glob("*.docx"))
xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
paras = []
for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
    t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
    paras.append(html.unescape(re.sub(r"<[^>]+>", "", t)).strip())
HEAD = re.compile(r"^(\d+(?:\.\d+)*)\s+.*\{(\d+)\}$")
OBJ = re.compile(r"^(\d{6,8})\s*:")
cur, obj2sec = None, {}
for t in paras:
    if "\t" in t:
        continue
    m = HEAD.match(t)
    if m:
        cur = m.group(1); obj2sec.setdefault(m.group(2), cur); continue
    m2 = OBJ.match(t)
    if m2 and cur:
        obj2sec.setdefault(m2.group(1), cur)

wb = openpyxl.load_workbook(sys2, read_only=True, data_only=True)
n2src = {}
for r in wb["Basic Report"].iter_rows(min_row=2, values_only=True):
    m = re.search(r"-(\d{3})\s*$", str(r[1] or ""))
    if m:
        n2src[int(m.group(1))] = str(r[4] or "").strip()
wb.close()

wb = openpyxl.load_workbook(a03, read_only=True, data_only=True)
print(f"{'leaf':<26} {'sections':<40} {'#SYS-RA':>7}")
allsec = collections.Counter()
for r in wb["Analysis Report"].iter_rows(min_row=9, values_only=True):
    if not r[0]:
        continue
    leaf = str(r[0]).strip()
    t = str(r[1]).replace("\u2013", "-").replace("\u2014", "-")
    nums = set()
    for a, b in re.findall(r"(\d{3})\s*-\s*(\d{3})", t):
        nums |= set(range(int(a), int(b) + 1))
    t2 = re.sub(r"\d{3}\s*-\s*\d{3}", "", t)
    nums |= {int(n) for n in re.findall(r"\d{3}", t2)}
    secs = set()
    for n in nums:
        for oid in re.split(r"[,\n]+", n2src.get(n, "")):
            oid = oid.strip()
            if oid in obj2sec:
                secs.add(obj2sec[oid])
    allsec.update(secs)
    key = lambda s: tuple(int(x) for x in s.split("."))
    print(f"{leaf:<26} {','.join(sorted(secs, key=key)):<40} {len(nums):>7}")
wb.close()
print()
print("sections by leaf-count:", dict(allsec.most_common()))
PY
cat features/time_management/data/leaf_to_section_probe.txt
```

回報全表（22 列），並就 §2.2 之七組逐組回答：
**該組之 leaf 是否落在相鄰／相關之章節群？** 有無某組散落於彼此無關之
章節（§4.1.4 第 4 用途之訊號）。

**只回報觀察，不改 §2.2 之分組** —— Layer 2 屬 Tier 2，Pei 簽。

### T4 — 上繳

`docs/upstream/02_framework.md`，含：

1. T1 之寫入確認（改前／改後）
2. T2 之四個目錄完整列出結果 + A-TM16 之追加確認（或不符之回報）
3. T3 之 22 列全表 + 七組逐組觀察
4. 索引表條數複查（T1 不增條數，應仍為 **16**）
5. **本包是否仍有該驗而未驗者之獨立判斷**，並明列盤點所用之全集

### 不得執行者

- 不動 git
- 不開啟交付路徑之任何檔案（T2 為純目錄列舉）
- 不填 `D5`、不組任何 Scope 值
- 不改 §2.2 之 Test Set 分組（Tier 2，Pei 簽）
- 不產出 `leaf_to_section.tsv` 正式檔（T3 之輸出為 `*_probe.txt`，
  正式錨鏈建置待 A-TM12 裁定）
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不以 openpyxl 存回任何工作簿
- 不跑 `recon.py`（A-TM15）

---

## 4. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM13 | 分析層自裁，條文作廢一律加註保留不刪除 | ✅ §1.1 |
| framework Part N Layer 1 | 已由 R-TM8 裁定 | ✅ §2.1 |
| framework Part N Layer 2 | **[PROPOSED]，待 Pei 簽** | ✅ §2.2 |
| framework Part N Layer 3 | 未鎖定，待 T3 實測後綁定 | ✅ §2.3 |

分析層本包未動 git、未改腳本、未開啟任何 xlsx、未改執行層產出之任何檔案。
