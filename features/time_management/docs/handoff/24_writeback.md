# 下放包 24 — 交付說明草案、寫回執行、G-TM3 正向驗證

分析層 → 執行層。往返編號 `24`。對應上繳 `docs/upstream/24_writeback.md`。

Pei 2026-08-22「就下放吧」——本包含交付說明草案與**寫回之執行**。

**射程界定**：本包之 `--write` 只寫入 `features/time_management/output/`。
**交付路徑之寫入、git、tag、`DELIVERY.sha256` 一律屬 Pei，本包不涉。**

---

## 1. 交付說明草案（**[PROPOSED]，Pei 過目後定稿**）

擬置於交付信件或 `output/` 之 `DELIVERY_NOTE.md`。
**內容為事實陳述，不含辯解。**

```markdown
# Time and Date — FM-WI-FSM-036-A01 交付說明

## 範圍

本工作簿涵蓋 CFTS_015 Time and Date，兩種 EE architecture 剖面：
Architecture Profile A（ATL-Hi，HU-managed time）與
Architecture Profile B（ATL-Mi，IPC-master / LTM repetition）——
剖面之命名取自 SYS3 SYSAD V2 §4.1.1 / §4.1.2。

僅適用於單一剖面之測試用例，其 Pre-Condition 首行標明
`The vehicle is an Atlantis High/Mid architecture variant`。

## 需求覆蓋

| 層 | 數 |
|---|---|
| SYS2 功能需求（CFTS_015） | 126 |
| SYS3 SYSAD 涵蓋 | 126（與 SYS2 功能需求集合相等） |
| SWE.1 分析報告所引用 | 78 |
| **無對應 SWE leaf** | **48** |
| SWE leaf（測試用例生成單位） | 22 |
| 測試用例 | 59 |

**覆蓋率 78 / 126 = 61.9%**（分母為 SYS2 之功能需求全集）。

48 筆未覆蓋之需求，其成因在 SWE.1 分析報告未將其分解為 SWE leaf。
本工作簿之測試用例以 SWE leaf 為生成單位，故該 48 筆無對應用例。

**該 48 筆並非架構不適用**：其中 26 筆於 SYS3 標為 ATL-Hi，
內容包含 Nav / Non-Nav HU 之時間來源等 HU 軟體行為。
已列入待決事項，待 SWE.1 補件後另行補充用例。

## 待決事項

工作簿中之 `PENDING: DR-{n}` 標記為已識別而尚未取得來源之項目，
非遺漏。逐項如下：

| DR | 內容 | 處數 | 影響 |
|---|---|---|---|
| DR-5 | CFTS015 內查無物件 6151328 / 6151331 | 4 | 該二筆之 specification_reference |
| DR-6 | Atlantis Mid 側 11 個 LID 有訊號而 CAN 網段未載 | 1 | 訊號斷言之網段 |
| DR-8 | ECU 軟體重置（不斷電）之操作方式 | 1 | 該步驟之執行 |
| DR-9 | CAN sleep 之可觀察終止條件 | 1 | 該步驟之執行 |
| DR-10 | Bench 之 GPS 訊號控制（可用性／位置／時間） | 10 | 該等步驟之執行 |
| DR-12b | 設定頁名為 `Clock` 或 `Clock & Date` | 23 | UI 標籤字面 |
| DR-20 | 無效時間訊號之注入方式 | 9 | 該步驟之執行 |

DR-8 / 9 / 10 / 20 為測試環境操作方式，取得後可直接替換，
不影響用例之驗證邏輯。

## 參照體系

`Specification Reference` 欄採 `CFTS015-{7 位 Polarion ObjectID}`，
依 ASPICE SWE.6 作業指引 §10.7(a)。
CFTS015 文件內另有短號需求 ID（如 CFTS015-824），**與本欄之編號體系
不互通** —— 於文件中搜尋本欄之值時，請搜尋其 7 位數字部分。

## 未及事項

- 本工作簿未經 done-region 仲裁（本 feature 無既有已完成區）。
  人工覆核為 pilot 抽樣，59 條中 7 條經獨立覆核，其餘為產出方自檢。
- `範圍 Scope`（D5）留空 —— 其值為所依據之 SWE.1 報告之文件識別，
  而該報告之正式版本身分未定。
```

**兩處請 Pei 特別看**：

1. **「未及事項」之第一點** —— 我方主動揭露 pilot 之覆核比例
   （7/59 獨立覆核）。**此為誠實但可能招致質疑之陳述**，
   刪除與否屬你。分析層之意見是**保留**：該限制於交付後仍存在，
   由我方先說比被問到好。
2. **48 筆之措辭** —— 現行寫法明確指向 SWE.1 未補件。
   若你認為不宜在交付件中指名上游，可改為
   「該 48 筆尚未分解為 SWE leaf」（去成因）。**但事實不宜改。**

## 2. 寫回執行

### T1 — dry-run（R-TM78，必跑）

```bash
cd /Users/peihe/Work_Projects/TC_Generator
python3 features/time_management/scripts/write_back.py \
        --feature-dir features/time_management
```

**逐項核對並寫入上繳**：`rows`（期望 **59**）、`skipped`（期望 4 份
`.pre-arch.json`）、`tc_id` 區間（期望 `NR1L-TimeAndDate-001 … -059`）、
`columns` 十六欄、`unresolved`（期望空）、來源 SHA256
（期望 `6372fb6b…`）。

**任一不符即停，不進 T2。**

### T2 — 寫回

```bash
python3 features/time_management/scripts/write_back.py \
        --feature-dir features/time_management --write
```

**輸出落 `features/time_management/output/`，不得寫入任何交付路徑。**

**寫回後立即記錄**：輸出檔之 SHA256、大小、列數。

### T3 — G-TM3 正向驗證（**本次寫回之核心檢查**）

`surgical_save` 之寫入路徑**至今從未執行過**。G-TM3 為唯一能發現
「讀碼推論與實際行為不符」之機制。

**重新開啟輸出檔**（唯讀），取樣比對：

| 取樣 | 欄 | 比對對象 |
|---|---|---|
| 首列（row 10） | `tc_id` / `test_item` / `design_method` | 生成之 JSON |
| 末列（row 68） | 同上 | 同上 |
| 任一中間列 | 同上 | 同上 |

**`tc_id` 為首選取樣欄**（依序號必逐列互異，排除「兩欄值恰同」之偽陰性
—— G-TM3 訂正）。

**比對失敗即 raise，不得僅警告。**

### T4 — 結構完整性複驗

```bash
python3 - <<'PY'
import zipfile, hashlib
src="features/time_management/inputs/FM-WI-FSM-036-A01 …_20260817_ext.xlsx"
out="features/time_management/output/<輸出檔名>"
a,b=zipfile.ZipFile(src),zipfile.ZipFile(out)
sa,sb=set(a.namelist()),set(b.namelist())
print("member 增:", sorted(sb-sa), " 減:", sorted(sa-sb))
diff=[m for m in sa&sb if a.read(m)!=b.read(m)]
print("內容相異之 member:", sorted(diff))
PY
```

**期望**：member 增減皆為空；相異者**僅限目標分頁之 sheet XML
（與必然連動者）**。

**另須確認 R 欄之 x14 下拉存活** —— 依 FORMS.md 之實測形態，
zip member 數應維持 **48**（openpyxl 存回會降為 47）。
**若為 47，立即停止並回報：該情形代表寫回未走 `surgical_save`。**

### T5 — 交付說明落檔

§1 之草案寫入 `features/time_management/output/DELIVERY_NOTE.md`，
**標 `[PROPOSED]`**，待 Pei 定稿。

**DR 處數依 T1 之實測填入**（§1 之表為 `21` 之數字，
017 拆分後可能微變）。

### T6 — 上繳

`docs/upstream/24_writeback.md`。**依 R-TM74 列逐 T 對照表。**
須含 T1 六項核對、T2 之 SHA256、T3 之取樣比對輸出、T4 之 member 比對。

### 不得執行者

- **不動 git、不 tag、不寫 `DELIVERY.sha256`**（皆屬 Pei）
- **不寫入任何交付路徑**（`/Users/peihe/Work/02_Project_R1LR/…`）
- 不以 openpyxl 存回（唯一路徑為 `xlsx_surgical.py`）
- 不刪除 `.pre-arch.json`
- 不改 `Clock` 之頁名（A-TM28 未裁）
- 不改 §1 之交付說明內容（其為 [PROPOSED]，Pei 定稿）
- 不碰 `features/vehicle_setting/`

---

## 3. 呈報 Pei

本包完成後，`features/time_management/output/` 內為**可交付之工作簿**
與 `DELIVERY_NOTE.md` 草案。

**其後全部屬你**：交付路徑之複製、git、tag、`DELIVERY.sha256`。

**寫回時最可能出事的一處**：T4 之 zip member 數。
若為 47 而非 48，代表 R 欄之 x14 下拉已被摧毀 ——
**該損壞是選擇性的：工作表數、列數、公式、其他三條 legacy DV 全部不變，
只有那一條下拉消失。** 若只比對前述項目，檢查會全綠。
故 T4 之 member 數是唯一可靠之判別點。

## 4. 本包產生之新條文清單（自檢 —— R-TM14）

**無。** 本包為既有裁決之執行與交付說明草案。

分析層本包未動 git、未改任何腳本、未改任何 TC。
