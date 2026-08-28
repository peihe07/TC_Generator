# 上繳包 05 — Popup 交付準備

日期：2026-08-28
Feature slug：`popup`
對應下放：[handoff/05_delivery_prep.md](../handoff/05_delivery_prep.md)
　　　　　＋ Pei 2026-08-28 口頭附加一件（R-POP25 第 3 點之補登，不另開包）
執行層：Claude（Opus 5）

**總判：交付候選已產出，15 項回讀複驗全數相符，`lint036 --profile popup`
21 項全 0，x14 DV 存活。**
`output/` 產出前 `list_directory` 實測為空（目錄不存在），無覆寫之虞。
`forms/FORMS.md` 已補登兩件 Pop Up。

**§八 升級條件命中一項**：`rulings_hash` 之既有 sha 除 R-POP18／R-POP20
外，另有 **R-POP5** 與 **R-POP13** 變動。**成因已逐條具名且全部為分析層
本輪之自身編輯**（`git diff` 可證），非語料漂移 —— 詳 §六-2。
**未停下**，理由與證據一併呈報，Pei 得否決。

---

## 一、Pei 之附加件：R-POP25 第 3 點之補登（先報，因不在下放包內）

### 1.1 補登前之實測

```
$ grep -ci "pop up" forms/FORMS.md
0
```

與 R-POP25 第 3 點所述「現有兩件 Pop Up 未登錄」相符。

### 1.2 補登內容

於 `forms/FORMS.md` 新增一節「**共用參考件 —— Pop Up（R-POP25 第 3 點）**」，
欄位形制**沿該檔既有之「參考資料庫（DBC / PROXI / LID）」六項 (a)–(f)**
（未自創格式）。兩件之 (a)／(b) 皆為本輪實測，非轉抄：

| 項 | `Pop Up List HMI R1 (26PI).xlsx` | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` |
|---|---|---|
| **(a)** sha256 | `ff47b7be63e5824cafe35deda9f9ddd0a63f6ea458169ef73689a1c559ea13ea` | `dc078763c67b52388eba8edf5c461515cfd2d92dd3a78dba0ce4e365e43ccc2f` |
| bytes ／ mtime | 2,951,835 ／ 2026-08-25T13:51:21 | 1,035,049 ／ 2026-08-25T13:50:34 |
| **(b)** 涵蓋範圍 | 3 分頁。`Main` 1,344 列 × 17 欄：**r1 = `SR24 Post 2A CR25802`**、r2 欄名、資料自 r3 起，`^PU\d` 之 ID 列 **1,340 筆**（`PU0001`～`PU1579`，編號不連續）；r2 之 12 個具名欄逐字入登錄。另 `Templates` 34×5、`Drop Down Fields` 73×8 | **10 頁**（`/Count` 與 `/Type /Page` 計數皆 10），含 `/Font` 79 處、`/Image` 66 處。**內容未解析** |
| **(c)** 版次 | `Main!A1` 逐字 `SR24 Post 2A CR25802`；檔名另載 `HMI R1 (26PI)` | `SR24 1A`／`May 3 2021`（皆檔名），**早於基線兩代** |
| **(d)** 已知不涵蓋 | 三項：只取規格明文委派之欄位（IN §8.4.2）；`search keyboard` 無對應列（A-POP8 之實測數字入登錄）；hard-button 分支無實例（A-POP7）| **不得解析** —— R-POP7 已裁不納入，逕行解析即把被排除之件讀進判斷 |
| **(e)** 取代關係 | 與該 PDF **非同一文件且非同代**，不互相取代；非 036 母本，與 R-G1／R-G2 無涉 | **被上游 SR24 Post 2A 現版取代**（即 DR-POP2 之標的）|
| **(f)** 首個採用 | `popup`，2026-08-27（R-POP6；DR-POP1 據此結案）| **尚無**，本輪僅登台帳 |

**R-POP25 之實作限於「登錄」**：本輪**未移動、未刪除、未改**任何檔。

### 1.3 順帶實測：`forms/` 尚有 3 件未登錄（未代登，已在 FORMS.md 內具名）

| 未登錄檔 | 誰該補 |
|---|---|
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | 其首個採用之 feature |
| `SR24 R1 Market Configuration Table v1.6.xlsx` | 同上 |
| `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | 同上 |

依 R-POP25 第 3 點三者皆應補，但**不在 Pei 指定之範圍**。
**未代登** —— (b) 涵蓋範圍與 (f) 首個採用須由實際使用者實測填寫；
由未使用它的 feature 代填會產出**無人負責的登錄**，那比空白更糟。
此限制已寫入 `forms/FORMS.md` 該節末之「本節之範圍限制」。

---

## 二、交付簿產出（§二）

### 2.1 落點與覆寫檢查（§八 升級條件之複驗）

```
list_directory features/popup/output/：（目錄不存在或為空）
```

**無同名檔，未觸發覆寫之升級條件。** 目錄由本包新建。

### 2.2 產出方式 —— 位元複製，非重寫（獨立判斷，揭露）

`sandbox/pilot01/` 之工作簿已由 `gen_pilot.py` 經 `surgical_save` 產出，
且經 `lint036` 全綠、x14 DV 實測存活。交付候選與它**不應有任何一格之差**，
故以 `shutil.copy2` 複製，再以 **sha256 相等**證明無損：

```
sha256 來源 dc0963d788244b149fd8716367744ae377d90245286aaea5b3812e55ce2519d8
sha256 產出 dc0963d788244b149fd8716367744ae377d90245286aaea5b3812e55ce2519d8
無損：兩者相等
```

**這比再跑一次 `surgical_save` 強**：後者只能證明「這次也沒壞」，
前者證明「與已驗過的那一份是同一份」。
R-G3 之禁令針對 `openpyxl.save()` 之**改寫**（A-POP5：靜默刪除 x14 下拉）；
本檔不改任何一格，故不觸發該路徑，**落檔後仍以 `zipfile` 直讀複驗**，
不以「應該沒事」代替量測。

產出檔：
`features/popup/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Popup_20260828.xlsx`
（檔名形制沿 Display／SXM／UserProfiles）。
腳本：`features/popup/scripts/gen_delivery.py`（可重跑；同名檔存在即 exit 2 不覆寫）。

### 2.3 落點合法性

`scripts/lint_paths.py` 之 `EXEMPT_TOPS` 含 `output` —— `features/<f>/output/`
不入 R-G25 之副檔名落點檢查。實測 `lint_paths` 之違規數**未因本包增加**
（仍為 1，且該筆屬 driver_distraction，見 §七）。

### 2.4 逐欄回讀複驗（15 項，自產出檔回讀，不自語料）

| 項 | 實測 | 預期 | 判 |
|---|---|---|---|
| 交付簿資料列（F 欄非空）| 5 | 5 | 相符 |
| F 欄值 `NR1L-Popup-001`～`-005` | 5 | 5 | 相符 |
| D 欄值 `SWE1-POP-002-01`～`-05` | 5 | 5 | 相符 |
| G 欄 = `Popup` | 5 | 5 | 相符 |
| H 欄 = `Pop-up Close` | 5 | 5 | 相符 |
| P 欄 = `P1` | 5 | 5 | 相符 |
| **Q 欄非空（R-POP22）** | **0** | 0 | 相符 |
| **E 欄非空（§三）** | **0** | 0 | 相符 |
| C 欄非空 | 0 | 0 | 相符 |
| R 欄值屬下拉 9 字串 | 5 | 5 | 相符 |
| O 欄 = `NEW` | 5 | 5 | 相符 |
| AA 欄（Author）= `PeiPYHsu` | 5 | 5 | 相符 |
| spec_reference 兩行者 | 1 | 1 | 相符 |
| PENDING 佔位（全簿全欄）| 0 | 0 | 相符 |
| x14 DV 個數 | 1 | 1 | 相符 |

R 欄之比對對象為 `下拉選單!$A$1:$A$9` 之**實際 9 個字串**（逐字印於工具輸出）；
五條所用之 `狀態轉換 (State Transition Testing)` 即 `A2`。

### 2.5 x14 DV（`zipfile` 直讀）

```
xl/worksheets/sheet6.xml: f='下拉選單!$A$1:$A$9'  sqref='R10:R1411'
```

**存活**，與母本逐字相同（§八 升級條件第 2 項未命中）。

### 2.6 B 欄（No.#）—— 一項與下放包措辭之出入

下放包 §二-2 之表寫「**B（No.#）1–5**」。實測 B10:B14 之內容為
**母本自帶之公式** `=IF(ISBLANK($D10),"",ROW()-9)`，非字面值；
以 `data_only=True` 讀取之快取值為 `[1, None, None, None, None]`。

**這不是缺陷，是既有交付件之共通形態**（逐簿實測）：

| 簿 | `data_only` 之 B10:B13 |
|---|---|
| `display` 20260826 | `[1, None, None, None]` |
| `sxm` 20260813 | `[1, 2, None, None]` |
| `user_profiles` 20260819 | `[1, 2, 3, 4]` |
| **popup**（本交付）| `[1, None, None, None, None]` |

差異只反映各檔曾被 Excel 開啟到第幾列。Excel 一開即計算為 1–5。
**未改寫 B 欄為字面值** —— 那會拿掉母本之機制（FORMS.md「B 欄編號公式」節），
且與三本既有交付件不一致。已於 `DELIVERY_NOTE.md` §7 對收件方明說
「以程式讀取本簿者請讀 B 欄公式或改讀 F 欄，勿以快取值判斷列數」。

---

## 三、TestRail 對映表（§三）

**空表加說明，非省略。** 已落 `DELIVERY_NOTE.md` §2：

- 舊 ID → 新 ID 對映：**無**
- 依據：`workbook_state` 實測為 `BLANK`（母本零填列、**無 done region**），
  五條皆新增，O 欄一律 `NEW`
- E 欄（TestRail）留空，待 TestRail 建號後回填

---

## 四、`DELIVERY_NOTE.md`（§四，新建）

落 `features/popup/output/DELIVERY_NOTE.md`（沿 user_profiles 之落點慣例）。
七節，四項必載逐項對照：

| 下放包所令 | 落於 | 內容摘要 |
|---|---|---|
| 1 交付範圍 | §1 | 5 leaf 一表列出；Heading 2 列標 `No TC`（R-POP5 —— **本包已可去掉「待追認」之保留**，見 §六-1）|
| 2 **範圍缺口具名上報（R-POP2）【醒目】** | §3 | 以引言塊起頭「**本交付不涵蓋 queue／priority**」，並列表逐節說明 spec 5.3（GP1）／5.4（GP2）／5.1（Priority Matrix）於 037 V0.2 **無任何 SWE1 列**，5.6 之 5 leaf 即交付之全部；明寫「不寫明則收件方會以工單名推定範圍」|
| 3 未結 DR 三件 | §4 | DR-POP2／3／4 逐件載標的與影響；DR-POP1 已 RESOLVED |
| 4 素材版位殘留兩點（R-POP6）| §5 | CR25802 vs CR22510、`(26PI)` 適用性；並記兩點不改所引之值（16 格引文已逐格複驗）|
| 5 指紋 | §6 | 交付簿 sha256、`pilot_01.json` sha256、來源三件之 doc_id ＋ sha256 ＋ 版次、素材 Pop Up List sha256 |

另加 §7「品質閘之實跑結果」與 B 欄公式之收件方須知（§二-6）。

---

## 五、gate 與複驗（§五）

### 5.1 `lint036.py --profile popup`（21 項）

對**交付簿本身**再跑一次（非只跑 sandbox 版）：

```
-> features/popup/reports/Popup__popup_dc0963d7_20260828.md
行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
     N=0 P=0 Q=0 R=0 T=0 U=0 V=0
```

報告檔名內嵌之 `dc0963d7` 即交付簿 sha256 前 8 碼，與 §二-2 相符。

### 5.2 `ledger_xref.py --feature popup`

**PASS**（8 檔、本 feature 引用 201 處、他 feature 37 處不對照、補零不一 0）。
依 R-POP24 第 2 點**未接入 `gate_all.py`**。

---

## 六、`rulings_hash` —— **§八 升級條件命中，成因已具名**

### 6.1 實測

重產後：**576 錨點**（前 557）、來源 16 檔。
`diff`（`cut -f1,3,5 | sort`）之**全部**輸出，逐列歸因：

| 列 | 變動 | 歸因 |
|---|---|---|
| R-POP18 | `18ddf460` → `bfbb3167` | **§五 已預期** —— 本輪「實作二項追認」入條文 |
| R-POP20 | `7ac862b3` → `2894aa0c` | **§五 已預期** —— 詞數算法訂正 ＋ 001 例外追認入條文 |
| R-POP21 | 新增 `bd4637b8` | **§五 已預期** |
| R-POP22 | 新增 `1bb746f6` | **§五 已預期** |
| **R-POP5** | `896b4b84` → `a6816cb1` | **§五 未列** —— 標題由「待 Pei 追認」改為「**Pei 追認 2026-08-28**」，並加「追認（2026-08-28，Pei『都裁過了』）：照現裁確定，不再為 [DEFAULT]」一段 |
| **R-POP13** | `bcd97ba8` → `89306542` | **§五 未列** —— 措辭「**作廃**」改為「**不再適用，此句撤回**」（順帶更正 `廃`／`廢` 之誤字）|
| **R-POP23** | 新增 `c5655c80` | **§五 未列** —— `-002-05` design_method 維持狀態轉換（Pei 追認）|
| **R-POP24** | 新增 `e362b2b6` | **§五 未列** —— `ledger_xref` 之存續與接入（Pei 追認）|
| **R-POP25** | 新增 `ec88e973` | **§五 未列** —— `forms/` 落點政策 |
| **R-DD1～R-DD13（14 列）** | 新增 | **非本 feature** —— 見 §六-3 |

### 6.2 升級條件之判斷（未停下，理由如下）

§八 第 4 項為「**除 R-POP18、R-POP20 外之既有 sha 變動**」。
R-POP5 與 R-POP13 兩列命中。**但**：

1. **成因為分析層本輪之自身編輯，`git diff features/popup/RULINGS.md`
   逐行可證**，非語料漂移、非工具異常
2. 下放包 05 §五之預測清單**寫於 §九 四項結案之前** —— R-POP23／24／25
   即那四項之處分，而 R-POP5 之追認正是 §九 第 1 項。
   **預測清單與其後才發生的裁定不同步，是清單過時，不是簿子壞了**
3. 該升級條件之目的是攔「沒有人說得出成因的 sha 變動」。
   本輪每一列都說得出成因，且來源是同一次分析層落檔

故**照常完成本包**，於此逐列具名呈報。**Pei 得否決本判斷**。

### 6.3 14 列 `R-DD*` 進入 tsv —— 非本包，但須提醒

`rulings_hash.py` 之預設範圍含 `features/*/RULINGS.md`（R-POP11）。
`features/driver_distraction/RULINGS.md` 於 `d3f70d8` 由他 session 首次
提交，故本輪重產時 14 條 `R-DD*` 首度入表。**兩點提醒**：

1. **該檔目前仍有未提交之改動**（`git status` 為 `M`）。本輪所記之
   14 個 sha 取自其**工作樹狀態**，該 session 落檔後會再變一次。
   本包**未也不應**代其凍結
2. 工具已警示 **`R-DD6` 同號兩體**：
   `features/driver_distraction/RULINGS.md:117` 與 `:197`（**本體不同**）。
   屬他 feature 之台帳，**未代改**，於此具名

**未以 `--target` 限縮範圍避開此事** —— 那會把其餘 15 個來源檔全部踢出
tsv，且 `rulings_hash --check` 隨即轉紅。維持預設範圍是唯一自洽之選擇。

---

## 七、gate_all 逐支歸因

| 閘 | exit | 04 包後 | 05 包後 | 歸因 |
|---|---|---|---|---|
| `lint_docs036 --gate` | **0** | PASS | PASS | — |
| `canon_refs --waiver --gate` | **1** | 470 | **470** | **本包 +0** —— 見下 |
| `rulings_hash --check` | **0** | PASS | PASS | 重產後相符（576 條）|
| `gates_tsv --check` | **1** | FAIL | **FAIL** | **非本包** —— `features/driver_distraction/scripts/selfcheck_pilot_group3.py` 未登錄，重產 diff 仍只有該列（同一成因另使 `test_gates_tsv::test_check_detects_drift` 轉紅，見 §八-1）|
| `lint_paths --gate` | **1** | 1 | **1** | **非本包** —— `features/driver_distraction/workbook/driver_distraction_00.xlsx` 落點違規 |

**`canon_refs` 本包 +0 —— 這是本包唯一一個「數字沒動」的成果，值得記**：

- 下放包 §五預測「本包新增之 `R-G29` 引用」會使其上升。**實際未上升**：
  本包新增之三份文件（`forms/FORMS.md` 之新節、`DELIVERY_NOTE.md`、
  本上繳包）**一處 `R-G29` 都沒引** —— 它們引的是 R-G1／R-G2／R-G12／
  R-G13／R-G15／R-G25／R-G27 與 R-POP 系列，皆可解析
- 且依 **R-POP21** 逐一冠 canon 前綴（如 `IN §8.4.1`、`IN §8.4.2`），
  未再製造裸引用之歧義。**上繳包 04 §八-5 所記之寫作陷阱，本包未再犯**

三支紅之中**兩支非本包**、一支（canon_refs 470）為既存值未變。

---

## 八、預期數字對照（§六，相符者亦列）

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| 交付簿資料列 | 5 | **5** | 相符 |
| F 欄值 | `NR1L-Popup-001`～`-005` | **5/5 逐列等值** | 相符 |
| D 欄值 | `SWE1-POP-002-01`～`-05` | **5/5 逐列等值** | 相符 |
| G 欄／H 欄 | `Popup` ×5 ／ `Pop-up Close` ×5 | **5／5** | 相符 |
| P 欄 | `P1` ×5 | **5** | 相符 |
| **Q 欄非空** | **0** | **0** | 相符 |
| E 欄非空 | 0 | **0** | 相符 |
| R 欄值屬下拉 9 字串 | 5/5 | **5/5** | 相符 |
| spec_reference 兩行者 | 1（002）| **1** | 相符 |
| PENDING 佔位 | 0 | **0** | 相符 |
| Final Step ≤ 18 words | 5/5 | **5/5**（R-POP20 訂正後之算法；語料未動，同上繳包 04 §八-1）| 相符 |
| x14 DV | 1，存活 | **1，存活** | 相符 |
| RULINGS.sha.tsv 新增／變動／其餘變動 | 2／2／0 | **7／2／0**（popup 側）＋ **14 列 R-DD**（他 feature）| **不符 —— 見 §六，不調和** |

### 8.1 單元測試

`python3 -m pytest tests/ -q` → **1260 passed, 9 failed, 15 skipped**
（上繳包 04 為 1261 passed／8 failed）。

**本包未新增測試**（`gen_delivery.py` 之複驗以其自身之回讀輸出為證，
未另立 pytest），故 passed 由 1261 降為 1260、failed 由 8 升為 9 —— 差額
即同一支測試由過轉紅：

| 測試 | 成因 | 是否本包 |
|---|---|---|
| **`test_gates_tsv.py::test_check_detects_drift`（新紅）** | 其首行斷言為「repo 內之 `GATES.tsv` 應為最新」（`assert r.returncode == 0`）。因 `features/driver_distraction/scripts/selfcheck_pilot_group3.py` 未登錄而失敗 —— **與 `gates_tsv` 閘同一成因**。該腳本於 04 包收尾後才由他 session 落入 | **否** |
| `test_intake_scaffold.py`（6 支）| `scripts/new_feature.py` 於 tmp root 找不到 `docs/fw036/templates/DECISIONS.md` | 否（04 包即如此）|
| `test_single_write_path.py`（2 支）| time_management／user_profiles／vehicle_category 之腳本呼叫 `openpyxl.save()` 而未列入 `KNOWN_VIOLATIONS` | 否（04 包即如此）|

**已實證本包未貢獻任何一支**：`gates_tsv` 重產後之 `diff` 只有
driver_distraction 那一列，`features/popup/scripts/gen_delivery.py`
**不在其中**（該工具未將其認作閘）。

---

## 九、三分法

| 類 | 內容 |
|---|---|
| **照裁定執行** | 交付簿產出與 15 項回讀複驗、TestRail 空表、`DELIVERY_NOTE.md` 五項必載、`lint036`／`ledger_xref` 實跑、tsv 重產、**R-POP25 第 3 點之兩件補登（Pei 附加）** |
| **實測後回報而不自為** | (a) B 欄為母本公式而非字面 1–5，未改寫（§二-6）；(b) `forms/` 另 3 件未登錄，未代登（§一-3）；(c) tsv 之 R-POP5／R-POP13 額外變動與 14 列 R-DD，未以 `--target` 迴避（§六）；(d) `R-DD6` 同號兩體，未代改 |
| **獨立判斷（已揭露）** | (a) 交付簿以**位元複製**產出而非重跑 `surgical_save`，並以 sha256 相等為無損之證明（§二-2）；(b) `FORMS.md` 之新節沿該檔既有六項 (a)–(f) 形制，未自創；(c) Priority Matrix PDF **只記結構事實、不解析內容** —— R-POP7 已裁不納入，解析即等於把被排除之件讀進判斷（§一-2 之 (d)）|

### 掃描條件揭露（R-G8）

| 掃 | 條件 |
|---|---|
| 交付簿逐欄 | `openpyxl` 載入產出檔（**不 save()**），`row 10`–`row 14` 逐格 `==` 比對；R 欄對 `下拉選單!$A$1:$A$9` 之實際 9 值比對 |
| PENDING | 全 sheet 全格 `str(cell.value)` 含 `PENDING:` |
| x14 DV | `zipfile` 直讀 `xl/worksheets/sheet*.xml`，正則取 `<xm:f>`／`<xm:sqref>` |
| sha256 | `hashlib.sha256`，1 MiB 分塊 |
| Pop Up List (b) | `openpyxl` read_only／data_only；`^PU\d` 之 A 欄比對；欄名取 r2 並將換行正規化為空白 |
| Priority Matrix (b) | **不解析內容**；以位元組正則計 `/Type /Page`、`/Type /Pages`、`/Count`、`/Font`、`/Image` |
| B 欄先例 | 對 display／sxm／user_profiles 三本交付簿各以 `data_only` 兩態載入比對 |
| FORMS.md 覆蓋 | 逐一 `basename` 對 `forms/FORMS.md` 作 `grep -F` |
| tsv 前後比對 | `cut -f1,3,5 \| sort` 後 `diff` |

---

## 十、R-G13 引用表（sha8 取自重產後之 `docs/fw036/RULINGS.sha.tsv`）

| 條 | sha8 | 標題 | 備註 |
|---|---|---|---|
| R-POP5 | `a6816cb1` | Heading 列之台帳處置 | **本輪變動**（Pei 追認，舊 `896b4b84`）|
| R-POP13 | `89306542` | TC ID 前綴定值 | **本輪變動**（措辭訂正，舊 `bcd97ba8`）|
| R-POP18 | `bfbb3167` | 主表辨識改內容判準 | **本輪變動**（實作二項追認，舊 `18ddf460`）|
| R-POP20 | `2894aa0c` | F1 修正過長之回調 | **本輪變動**（詞數算法訂正，舊 `7ac862b3`）|
| R-POP21 | `bd4637b8` | 節號列舉不得省略 canon 前綴 | 新立 |
| R-POP22 | `1bb746f6` | Estimated Test Time（Q 欄）留空 | 新立 |
| R-POP23 | `c5655c80` | `-002-05` design_method 維持狀態轉換 | 新立 |
| R-POP24 | `e362b2b6` | `ledger_xref.py` 之存續與接入 | 新立 |
| R-POP25 | `ec88e973` | `forms/` 落點政策 | 新立 |
| R-POP6 | （未變）| Pop Up List 納入為素材 | 本包 §一之依據 |
| R-POP7 | （未變）| Priority Matrix 不納入 | 本包 §一之依據 |
| R-POP14 | （未變）| `-002-05` 採規格原句生成 | — |

另引 R-G1、R-G2、R-G3、R-G5、R-G8、R-G12、R-G13、R-G15、R-G25、R-G27、
R-POP2、R-POP11、R-POP16、R-POP19、IN §8.4.1、IN §8.4.2、G-D。
（節號逐一冠 canon 前綴，R-POP21。）

---

## 十一、台帳現況（**自 repo live 產**，R-POP17-1）

`python3 scripts/ledger_xref.py --feature popup --live` 之輸出（節錄狀態欄）：

| 號 | 狀態 | 處分條 |
|---|---|---|
| A-POP1 ～ A-POP11 | **全 11 件 RESOLVED** | R-POP9／R-POP6・7／R-POP8／R-POP10／—／R-POP16・18・19／R-POP12／R-POP14／R-POP13・17／R-POP18／R-POP19 |
| DR-POP1 | RESOLVED（2026-08-27）| R-POP6 |
| DR-POP2 | 已登記，未送出 | — |
| DR-POP3 | 已登記，未送出 | — |
| DR-POP4 | 已登記，未送出 | — |

**本包未新開任何 anomaly 或 DR。** 三件未結 DR 皆不阻斷交付，
且皆已載於 `DELIVERY_NOTE.md` §4。

---

## 十二、待 Pei（逐項複驗後重寫，不轉抄）

下放包 §九 之四項**已於本輪全部結案**（R-POP23／R-POP24／R-POP25 ＋
R-POP5 之追認），故本清單為**重編**，非沿用：

| # | 事項 | 現況（本包實測）|
|---|---|---|
| 1 | **交付候選之人工抽查** | **本包之唯一出口** —— 五條 TC 全文見上繳包 04 §十二 與 `generated/pilot_01.json`；交付簿 sha256 `dc0963d7…` |
| 2 | `rulings_hash` 之 R-POP5／R-POP13 額外變動 | **本包判為成因具名而未停下**（§六-2），Pei 得否決 |
| 3 | `forms/` 另 3 件未登錄（R-POP25 第 3 點未竟之部分）| 未代登，待各該 feature 之首個採用者（§一-3）|
| 4 | 交付後 E 欄（TestRail）之回填時點與負責人 | 未定 —— `DELIVERY_NOTE.md` §2 已載「待 TestRail 建號後回填」|
| 5 | **交付產物是否入 git**（`output/` 現被各 feature 之 `.gitignore` 排除）| 現況：不入。交付簿之唯一入庫紀錄為其 sha256；檔案遺失只能自 `sandbox/pilot01/` 重產（§十三）。屬全域政策 |

**純他 feature，不入本清單**（沿下放包 §九 之界）：
vehicle_setting 之 31 項、`gates_tsv` 之 driver_distraction 未登錄、
`lint_paths` 之 driver_distraction 在製品、`media` 之 G-D 盲區、
`R-DD6` 同號兩體、tsv 內 14 列 R-DD 之未凍結狀態。

---

## 十三、git

**未執行任何 git 操作**（R-G5）。建議之 commit：

```
feat(popup): land handoff 05 - delivery candidate, delivery note, register Pop Up forms
```

本包改動之檔：

```
M  forms/FORMS.md
M  docs/fw036/RULINGS.sha.tsv
M  features/popup/docs/INDEX.md
?? features/popup/scripts/gen_delivery.py
?? features/popup/reports/Popup__popup_dc0963d7_20260828.md
?? features/popup/docs/handoff/05_delivery_prep.md
?? features/popup/docs/upstream/05_delivery_prep.md
```

### ⚠ 交付產物**不入 git**（既有慣例，實測後確認）

`features/popup/.gitignore:17` 為 `output/`，故
**交付簿與 `DELIVERY_NOTE.md` 皆不受 git 追蹤**。
非本包之選擇 —— 實測 `git ls-files features/display/output
features/user_profiles/output` 回傳**空**，三本既有交付件之 `output/`
同樣未追蹤（與 `inputs/`、`forms/*` 同policy：**產物不入 git、
其 manifest／指紋入 git**）。

**其後果須明說**：交付簿之唯一入庫紀錄是**它的 sha256**
（本上繳包 §二-2、§六 與 `DELIVERY_NOTE.md` §6 三處各載一次）。
檔案本身若遺失，**無法自 repo 復原**，只能以 `gen_delivery.py`
自 `sandbox/pilot01/`（該處**有**入 git）重產 —— 重產物之 sha256
須與上列相等，否則即為不可復原之損失。
本包**未強制 `git add -f`** 逾越該慣例；是否改為追蹤屬全域政策，
併入 §十二 之待裁。

**非本包所改而顯示為 M 者**：`features/popup/RULINGS.md`
（R-POP5／13／18／20 之修訂與 R-POP21～25，分析層本輪落檔）。

**注意**：`forms/*` 之檔案本身由根 `.gitignore` 排除，
**`FORMS.md` 為 tracked**（manifest 入 git、檔案不入 git，形狀未變）。
工作樹另有他 session 之未提交改動（driver_distraction、vehicle_setting、
sw_update、bed_lowering、docs/runtime 等）。
commit 時**務必帶 pathspec，勿 `git add -A`**。
