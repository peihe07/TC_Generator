# 下放包 03 — Layer 2 簽核、三項裁決、RD-1 草案、批次計畫

分析層 → 執行層。往返編號 `03`。對應上繳 `docs/upstream/03_signoff.md`。

Pei 2026-08-20 指示「都簽」。本包據以裁定，並明列**哪些不在簽核範圍**
—— 無具體提案者不能被簽，逐項說明於 §1.4。

---

## 1. 裁決

### 1.1 framework Layer 2 —— 簽核

```
R-TM17（Pei, 2026-08-20「都簽」）—— framework Part VII Layer 2 簽核

docs/fw036/framework.md Part VII 之七組 Test Set 簽核通過，
狀態由 [PROPOSED] 轉 SIGNED：

  Manual Setting (2) · GPS Sync (4) · Master Clock (5) ·
  CAN Transmission (4) · Display (3) · Zone and DST (2) · Fault Handling (2)
  合計 22 = 全 leaf set

Layer 1 `Time and Date`（R-TM8）與 Layer 3 主軸章節一併定案。
相鄰組界線三條（004↔010、014↔022、018↔011）為 §8.2.1 之拘束條款，
非說明文字，TC 生成時逐條適用。

「Layer 2 未經簽核不得生成 TC」之限制解除。其餘阻塞項不因本條解除
（A-TM02a 阻塞 D5、R-TM10-A1 仍 SUSPENDED、A-TM13 影響兩片之
spec_reference）。
```

### 1.2 A-TM01 孤兒目錄 —— 處置裁定

```
R-TM18（Pei, 2026-08-20「都簽」）—— features/vehicle setting/ 移入 archive

含空格之孤兒 scaffold `features/vehicle setting/`（A-TM01，成因為
A-TM04 之工具缺陷，非人為手滑）移入 `archive/`，比照 R-G2 不刪除慣例。

限制：
1. 只 mv，不 rm。移入後原路徑不得存在，archive 內容須逐檔可讀。
2. 移動前後各列舉一次兩處目錄，兩份清單須逐檔對應。
3. 不動 git —— 該目錄之 git 追蹤狀態變化由 Pei 處理。
4. 移入後於 archive 內該目錄建 `WHY_ARCHIVED.md`，記 A-TM01 與 A-TM04。
```

### 1.3 `recon.py` / `intake.py` 五項修法 —— 授權，但分兩階段

```
R-TM19（Pei, 2026-08-20「都簽」）—— 五項工具修法授權，A-TM15 優先

A-TM04 / A-TM05 / A-TM10 / A-TM12 / A-TM15 五項修法獲授權。
分兩階段，順序不可調換 —— 理由見下之「回歸之前提」。

**階段一（本包執行）**：A-TM15 單獨先修。
  recon.py 之 write_decisions()：目標檔已存在時一律寫
  DECISIONS.new.md，不得 write_text 覆寫既有檔。

**階段二（本包執行，階段一通過後）**：A-TM04 / A-TM05 / A-TM10。
  三者皆為 intake/scaffold 路徑之小改，互不相干。

**階段三（本包不執行）**：A-TM12（錨鏈解析路徑）另包處理。
  其為新增解析能力而非既有行為修正，回歸判準不同型。

**回歸之前提（此即階段順序之理由）**：
四項之回歸驗證均需對既有 feature 實跑 recon.py 並比對 RECON.md。
但在 A-TM15 修好之前，該實跑會沖掉受測 feature 之 DECISIONS.md ——
**回歸動作本身會造成它要防止的那種損害**。故 A-TM15 必須最先修。

回歸判準（階段一、二共用）：對 features/vehicle_setting 實跑
recon.py，RECON.md 之內容須與修改前逐位元相同；DECISIONS.md 之
mtime 與 SHA256 須不變。有任一差異即回報並停。
```

### 1.4 **不在簽核範圍者** —— 逐項說明

「都簽」只能及於已有具體提案之項。下列兩項無提案可簽，維持原狀：

| 項 | 為何不能簽 |
|---|---|
| **R-TM10-A1 替代樣式來源** | 分析層未提出任何候選 —— Home v2 經 150 筆 SHA 全域比對確認不在磁碟；交付路徑之同名複本**分析層明白建議不用**（其與 archive 版孰為 FORMS.md 受測物已不可判定，A-TM14）。**無候選則無可簽。R-TM10 維持 SUSPENDED**，TC 生成一律僅依條文。 |
| **A-TM02a / A-TM13 之上游答案** | 此二者為向上游提問，非本地裁決，不存在可簽之標的。可簽者僅「是否提問」，本包 §2 出 RD-1 草案，**送出屬 Pei（Tier 3）**。 |

**若 Pei 之「都簽」原意包含上列任一項，請明示該項之具體處置**；
分析層不以「都」字推定未曾提出之內容。

---

## 2. RD-1 問題草案（分析層擬，**送出屬 Pei**）

擬入 `docs/fw036/RD1_questions_time_management.md`，狀態 DRAFT。

```markdown
# RD-1 Questions — Time Management (CFTS015)

狀態：DRAFT。送出日期：____。送出屬 Pei。

## Q-TM1 — 037 之文件身分（阻塞交付欄位）

本 feature 收到之 SWE.1 分析報告檔名為 `SWE1_Secure_Date&Time.xlsx`，
封面 Project Name `New R1L`、日期 2020/09/05。

交付路徑 `ASW-R2/` 下其他三個 feature 之 037 命名形態一致：

| feature | 037 檔名 |
|---|---|
| Home | `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx` |
| AppDrawer | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx` |
| User Profiles | `FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` |

`ASW-R2/Time Management/` 下無任何符合該形態之檔案。

**問**：Time Management 是否另有依 FM-WI-FSM-037-A03 命名之正式報告？
或 `SWE1_Secure_Date&Time.xlsx` 即是而命名未依慣例？

**影響**：036 工作簿之範圍 Scope 欄（D5）值即為所依據 037 之文件識別，
在本問答覆前無值可填，交付件該欄將留空。

## Q-TM2 — 兩筆需求之來源物件不在 CFTS015 基線內

SYS2 匯出之下列兩筆，其 `Source Requirement items` 所指物件於 CFTS015
（R1LR Atl-H 25PI3.5 SR26, 20250909-1851）全檔零命中：

| SYS-RA id | 來源物件 id | 需求要旨（節錄自 SYS2） |
|---|---|---|
| `SYS-RA-TIME&DATE-221` | `6151328` | `$GPS_Presence$ = [Absent]` 時之內部時鐘精度 |
| `SYS-RA-TIME&DATE-224` | `6151331` | `$GPS_Presence$ = [Present]` 時之個人化設定 |

CFTS015 全篇物件 id 皆為 `481xxxx` 區段；`615\d{4}` 形態零命中。
兩者分別被 `SWE-RA-TIME&DATE-005`（Internal Clock Accuracy）與
`SWE-RA-TIME&DATE-002`（GPS Sync Enable/Disable Logic）引用。

**問**：此二物件源自 CFTS015 之較新版本，或源自另一份 CFTS？
應以哪一份文件為該二筆之 spec 依據？

**影響**：該二 leaf 之 `specification_reference` 於此二筆上無章節可寫。
依 §8.4.1 不得以鄰近章節填充，交付件將於 Remarks 標示缺口。

## Q-TM3 — 48 筆 SYS2 功能需求無對應 SWE leaf（分配政策）

SYS2 之 Functional Requirement 共 126 筆；037 之 22 片 leaf 合計引用
78 筆，**48 筆無任何 leaf 對應**（覆蓋率 61.9%）。

引用之 78 筆全數為 Functional Requirement，無懸空引用（037 未引用任何
不存在之 id）。48 筆清單可另附。

同時觀察到：037 可達之 21 個 CFTS 章節全落 `1.3.1.*`（PNet/CUSW/AtlHi
共通）與 `1.5.2.*`（LTM），**`1.5.3.*`（ETM）零命中**。兩者是否同源
尚未查證。

**問**：該 48 筆是否分配予其他 feature 之 037，或屬本 feature 之
分配缺口？若為後者，037 是否將補件？

**影響**：TC 生成單位為 037 之 22 片 leaf；48 筆無 leaf 即無工作簿列可
寫。依 §8.2 不得由 TC 作者自行創設 leaf 或分解 SYS2 條文湊覆蓋，
故此缺口以宣告處理，不以生成填補。
```

---

## 3. 批次計畫（生成批次 ≠ Test Set）

Layer 2 既簽，批次計畫定案如下。**B1 刻意避開 A-TM13 之兩片**
（002、005），使 pilot 不被任何未決項阻塞 —— Privacy B1 先例。

| Batch | Leaves | n | 內容 | A-TM13 曝險 |
|---|---|---|---|---|
| **B1（pilot）** | 001, 003, 006, 007, 008, 010, 012 | 7 | **七個 Test Set 各取一片** | **無** |
| B2 | 002, 004, 005, 014, 016, 018, 021 | 7 | GPS Sync 與 Master Clock 之餘片 | **002 + 005 同批，marker 一併審** |
| B3 | 009, 011, 017, 019, 020 | 5 | CAN Transmission 與 Display 之餘片 | 無 |
| B4 | 013, 015, 022 | 3 | Manual Setting / Zone and DST / Fault Handling 之餘片 | 無 |

合計 22 = 全 leaf set。

**B1 之取樣依據（canon §1.2 分層取樣）**：七片各屬一個 Test Set，
故 pilot 一次檢驗全部七組之 Test Set 值、setup 型態與 UI 進入路徑，
而非只驗一組之內部一致性。**本 feature 無 done region，pilot 是唯一
的人工閘門**（Part VII 已明記第三層不存在），取樣覆蓋面因此比有
done region 之 feature 更重要。

**B2 之集中依據**：002 與 005 是 A-TM13 之全部受影響者，同批生成使其
Remarks 缺口標示與 reasoning 寫法可一次比對，避免兩批各寫一套。
SXM B11 先例（`(add)` leaves 集中一批一起讀）。

**B1 不得開始生成**，直至 §4 之 T1–T5 完成且上繳經覆核。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM17 / R-TM18 / R-TM19

於末尾追加，標題行分別為：

```
## R-TM17 — framework Part VII Layer 2 簽核
## R-TM18 — features/vehicle setting/ 移入 archive
## R-TM19 — 五項工具修法授權，A-TM15 優先
```

內文為本包 §1.1 / §1.2 / §1.3 之區塊全文，逐字。
追加後 `## R-TM` 條數應為 **22**（19 + 3）。

### T2 — Part VII 狀態更新

`docs/fw036/framework.md` Part VII，將

```
下列七 Set 表待簽。
```

改為

```
下列七 Set 表經 Pei 2026-08-20 簽核（R-TM17）。
```

同節之 `### Batch plan` 段，將

```
**未定。** 待 Layer 2 經 Pei 簽核後另行起草。
```

整段換為本包 §3 之批次表全文（含 B1 取樣依據與 B2 集中依據兩段）。

**此處為「以定案內容取代佔位語」，非條文作廢，R-TM13 不適用。**

以 `assert old in text` 前置，`replace(old, new, 1)`，改後複查（R-TM11）。

### T3 — A-TM01 處置（R-TM18）

```bash
# 移動前列舉
ls -la "features/vehicle setting/"
ls -la archive/

mv "features/vehicle setting" archive/

# 移動後列舉，兩份清單須逐檔對應
ls -d "features/vehicle setting" 2>/dev/null && echo "ABORT: 原路徑仍存在"
ls -la "archive/vehicle setting/"
```

於 `archive/vehicle setting/WHY_ARCHIVED.md` 建檔，內容：

```markdown
# 為何封存

本目錄為 `features/vehicle setting/`（含空格），2026-08-20 依 R-TM18 移入。

**非人為手滑，係工具缺陷（A-TM04）**：`scripts/new_feature.py` 之
`feat_dir = root / "features" / feature.lower()` 無 slugify，
`new_feature.py "Vehicle Setting"` 即產生含空格之目錄，不報錯不警告。

實跑中之 feature 為 `features/vehicle_setting/`（底線版）。本目錄為
未填之 scaffold：paths 全為佔位符、`spec_mode: "A"`（模板預設）、
欄位為模板值（design_method `Q`、author `Z`）、無 `RECON.md`。

登記：`features/time_management/ANOMALIES.md` A-TM01、A-TM04。
處置條文：`features/time_management/RULINGS.md` R-TM18。
不刪除，比照 R-G2。
```

`ANOMALIES.md` 之 A-TM01 條末尾追加，並將索引該列狀態改 `RESOLVED`：

```markdown
**處置（2026-08-20，R-TM18）**：已 mv 至 `archive/vehicle setting/`，
原路徑不存在，`WHY_ARCHIVED.md` 已建。git 追蹤狀態之變化屬 Pei，未動。
本條轉 RESOLVED；成因 A-TM04 仍 PENDING（工具本身未修）。
```

### T4 — 階段一：A-TM15 修法

改 `scripts/recon.py` 之 `write_decisions()`。現行行為為
「`signoff["signed"]` 為真才轉寫 `DECISIONS.new.md`，否則整份覆寫」。

改為：**目標檔已存在時一律寫 `DECISIONS.new.md`**，僅在目標檔不存在時
才寫 `DECISIONS.md`。並於 stdout 明示所寫路徑。

改前先備份：

```bash
cp scripts/recon.py /tmp/recon.py.pre-A-TM15
```

回歸（本階段之判準，R-TM19）：

```bash
# 修改前基線
shasum -a 256 features/vehicle_setting/DECISIONS.md > /tmp/vs_dec.pre
cp features/vehicle_setting/RECON.md /tmp/vs_recon.pre

python scripts/recon.py --feature features/vehicle_setting

shasum -a 256 features/vehicle_setting/DECISIONS.md > /tmp/vs_dec.post
diff /tmp/vs_dec.pre /tmp/vs_dec.post && echo "DECISIONS 未被動 ✅"
diff /tmp/vs_recon.pre features/vehicle_setting/RECON.md && echo "RECON 逐位元相同 ✅"
ls -la features/vehicle_setting/DECISIONS.new.md
```

**兩個 diff 任一有輸出即回報並停，還原 `/tmp/recon.py.pre-A-TM15`。**

### T5 — 階段二：A-TM04 / A-TM05 / A-TM10

三項各自獨立，改法逐項寫死：

**A-TM04** — `scripts/new_feature.py` `scaffold()`：於
`feat_dir = root / "features" / feature.lower()` 之前插入

```python
if any(c.isspace() for c in feature):
    sys.exit(f"refusing: feature name contains whitespace: {feature!r} "
             f"(would create a directory with a space; see A-TM04)")
```

**不自動 slugify** —— 自動改名會靜默改變既有 feature 之目錄推導。
只擋，不代為決定。

**A-TM05** — `scripts/intake.py` `scaffold()`：將

```python
if not feat_dir.exists():
    subprocess.run([... "new_feature.py", feature ...], check=True)
```

改為既存目錄時以 `--adopt-existing` 呼叫，而非跳過。

**A-TM10** — `scripts/intake.py` 之 `KIND_TO_YAML` 加

```python
"cfts_doc": "spec_pdf",
```

**但僅在 `spec_pdf` 之現值仍為佔位符時回填**；已有真實路徑則不覆寫，
並於 `INTAKE.md` 註明衝突。

三項改完後跑一次 T4 之同一回歸（RECON.md 逐位元相同、DECISIONS.md 不變）。

### T6 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md   # 期望 22
grep -c '^## Part ' docs/fw036/framework.md              # 期望 7
grep -n '待簽' docs/fw036/framework.md                    # Part VII 應已無此字
grep -n 'B1（pilot）' docs/fw036/framework.md             # 應命中
ls -d "features/vehicle setting" 2>/dev/null || echo "原路徑已清 ✅"
test -f "archive/vehicle setting/WHY_ARCHIVED.md" && echo OK
grep -c '^## A-TM' features/time_management/ANOMALIES.md # 期望 16（T3 不增條）
```

### T7 — RD-1 草案落檔

建 `docs/fw036/RD1_questions_time_management.md`，內容為本包 §2 之
區塊全文。**狀態 DRAFT，不送出。**

### T8 — 上繳

`docs/upstream/03_signoff.md`，僅差異。須含：

1. T6 七項結果
2. T3 之移動前後兩份目錄清單，逐檔對應之確認
3. T4 / T5 之兩次回歸輸出（兩個 diff 之實際結果，非「相同」二字）
4. T2 之改前／改後實際字串
5. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git（`archive/` 之移動亦不 commit）
- **不開始 B1 生成**（待本包上繳經覆核）
- 不修 A-TM12（階段三，另包）
- 不 rm 任何檔案或目錄（T3 只 mv）
- 不送出 RD-1（Tier 3，屬 Pei）
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED，§1.4）
- 不以 openpyxl 存回任何工作簿

---

## 5. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM17 | 裁決（Pei），Layer 2 簽核 | §1.1 | ✅ T1 + T2 |
| R-TM18 | 裁決（Pei），孤兒目錄移入 archive | §1.2 | ✅ T1 + T3 |
| R-TM19 | 裁決（Pei），五項修法授權分階段 | §1.3 | ✅ T1 + T4 + T5 |
| A-TM01 轉 RESOLVED | anomaly 狀態變更 | §1.2 | ✅ T3 |
| RD-1 草案 Q-TM1–3 | DRAFT，送出屬 Pei | §2 | ✅ T7 |
| 批次計畫 B1–B4 | 定案，寫入 Part VII | §3 | ✅ T2 |

分析層本包未動 git、未改腳本、未寫 `docs/fw036/`（T2／T7 為執行層）。
