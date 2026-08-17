# 上繳 02 — User Profiles / 02a 裁決之落地與 02b 作業 1–5

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`02a_rulings.md`（R-U8、R-U9、R-G3、R-U10、R-U11、R-U12）＋ `02b_tasks.md`
- 範圍：**作業 1–5 已執行；作業 6–8 未執行** —— DR #1（037）仍 MISSING

---

## 0. 結果一覽

| 作業 | 狀態 | 一句話 |
|---|---|---|
| 1 RULINGS 追加 | ✅ | 六條逐字，附 supersede 註記；01 輪下放包未改寫 |
| 2 R-U9 PU 涵蓋驗證 | ✅ 已驗，**結論為不足** | **18 / 20**，缺 `PU1087`／`PU1088` → **DR #4**，未移入 `spec-index/`，A-UP06 不結案 |
| 3 R-G3 ＋ R-U10 canon 修補 | ✅ | `framework.md` §Workbook sync：加禁用警示、範例改 splice、分頁項標 rev A/B only |
| 4 R-U12 歸檔雜湊 | ✅ | `archive/forms_superseded/BASELINE.sha256`，`shasum -c` **3/3 OK，0 警告** |
| 5 ANOMALIES 狀態 | ✅ | A-UP05／07／08 RESOLVED；A-UP09 修補完成待覆核；02／04／06 維持 PENDING |
| 6–8 | ⛔ 未執行 | DR #1 未到齊，前置不成立 |

---

## 1. 作業 1 — RULINGS.md

六條**逐字**追加於 `features/user_profiles/RULINGS.md` §第二輪條文
（R19-2：原文貼入，不改寫、不摘要）。

**supersede 之處理**：`01b_tasks.md` **未被改寫**（已結輪次不回溯編輯），
其原文留存；於新章開頭加註記，指明「讀 01b 作業項 3 者，其預期值以 R-U8 為準」。

**`feature.yaml` 之 `recon_assertions` 已依 R-U8 改填**：

```yaml
functional_requirement_count: 180    # 由 TBD 改填
heading_count: 25                    # 由 TBD 改填（欄值 == "Heading"，非 len(headings)=27）
out_of_scope_count: 2
generation_population: 180
naive_leaf_shape_reference: 182      # 對照輸出，不作閘
```

**recon 本身未跑** —— 作業 6 之前置（037）不成立。**填了期望值不等於跑過閘**，
兩者於本包內分列。

---

## 2. 作業 2 — R-U9 之 PU 涵蓋驗證：**18 / 20，不足**

### 2.1 量測條件（自陳）

**對象**：`features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A
(Dec 15, 2023).xlsx`，工作表 `Main`，資料列 row 3–1343（**1341 列**，
A 欄非空 **1341**；header 在 row 2，row 1 為版本字串 `SR24 Post 2A CR25802`）。

**四種抽取式，逐一報數**（§4.3 之漏抽同型風險）：

| 抽取式 | 詞界 | 底線／空白分隔 | 範圍 | 唯一 id |
|---|---|---|---|---|
| `\bPU\d{4}\b` | 含 | 不涵蓋 | A 欄 | 1330 |
| `PU\d{4}` | 不含 | 不涵蓋 | A 欄 | 1330 |
| `PU\d{4}` | 不含 | 不涵蓋 | **全表 17 欄** | 1331 |
| `PU\s*_?\s*\d{3,5}` | 不含 | **涵蓋** | 全表 17 欄 | 1340 |

**四式在本 feature 之 20 個 id 上結論完全相同（皆 18/20）** ——
故本次之涵蓋數**與抽取式無關**。

> **此點必須明講**：DR #2 之首次量測曾因漏抽 `PU_0118`／`PU_0129` 之底線形態
> 而得 18，**那個 18 是本執行層之抽取缺陷**（canon §5a 第 7／12 條）。
> **本次之 18 不是缺陷** —— 兩次同數而不同因，若不分開講，
> 日後讀者會把已修好的缺陷讀成又犯了一次。

### 2.2 結果

**命中 18 / 20；缺 `PU1087`、`PU1088`。**

| 事實 | 實測 |
|---|---|
| 該表之編號區間 | `PU0001` – `PU1578`，唯一 id **1330** |
| 兩個缺者是否超出區間 | **否，在區間內** |
| 區間內之空號總數 | **248** |
| `PU1080`–`PU1095` 之實有者 | 僅 `PU1089`／`PU1090`／`PU1091`（本 feature 亦引用，**皆命中**）|
| 該表之 `Module` 欄相異值 | 181，含 `Profiles`、`Profile Setup Assistant`、`Personal Account/Driver Profiles`、`Connected Personal Account` |

**判讀**：候選**確為正確之文件家族**，缺者亦非「超出版本涵蓋範圍」——
**不是版本不對，是這一版就沒有那兩列。**

### 2.3 處置 —— 依 02b 明文，不採用

02b 作業項 2：「不足 → 具名列出缺哪幾個 id，轉 DR，**不以近似版本替代**」。

- **未**移入 `spec-index/`
- **未**更新任何 `BASELINE.sha256`
- **A-UP06 不結案**，維持 PENDING
- **已開 DR #4**：載有 `PU1087`／`PU1088` 之版本

> **18/20 不得充當到齊，理由不在比例而在位置**：兩個缺者皆出自 spec **`4.1.1`**
> （Profile Setup），而 spec 8.3 明文「The Profile Setup processes is a series
> of popups. Specific popups can be found in the HMI Pop Up List」——
> **缺口不在邊陲，在該功能的正中央。**

---

## 3. 作業 3 — R-G3 ＋ R-U10 之 canon 修補（`docs/fw036/framework.md`）

### diff 摘要（本輪唯一動到 `docs/` 之檔）

```
docs/fw036/framework.md | 51 insertions(+), 4 deletions(-)
```

單一節（§Workbook sync，原 line 234–253），三處變更：

| # | 變更 | 依據 |
|---|---|---|
| 1 | **新增禁用警示區塊** —— 標題 `⛔ NEVER openpyxl + wb.save() on a form workbook`，內含 A-UP09 之實測對照表（x14 節點 1→0、`R10:R1411` 消失、三條 legacy DV 存活、zip members 48→47、sheet 9→9、B 欄末列 1411→1411）| R-G3 |
| 2 | **範例改寫為 `xlsx_surgical` splice** —— `load_workbook` 保留（load 無害，**是 save 摧毀**），`wb.save()` 換成 `surgical_save(wb, src, out)`，並示範讀其 `differing` 與 `dv_counts` 之回報 | R-G3 |
| 3 | **`Test Case Framework` 分頁項標「rev A/B only」** —— 新增一段說明 rev C 為現行官方表單且無該分頁（9 sheets vs rev A/B 之 10），該分頁係 Media 時期工作流產物、非 STLA 表單要求；rev C 之 Test Set 詞彙以 H 欄為唯一載體 | R-U10 |

**警示之措辭刻意強調「選擇性損壞」**（照 A-UP09 之發現）：

> 損壞是選擇性的 —— sheet 數、列數、公式範圍、其他三條 DV 全部不變，
> zip member 只少一個，**它讀起來像一次無害的重新封裝**，
> 任何比對 sheet／列／公式之檢查都會全綠。

**兩處為同節修改，一併提交**（02b 作業項 3 之要求）。

---

## 4. 作業 4 — R-U12 歸檔三檔之雜湊保護

已建 `archive/forms_superseded/BASELINE.sha256`（3 檔）。

```
$ cd archive/forms_superseded && shasum -a 256 -c BASELINE.sha256
FM-WI-FSM-036-A01 …_SWQT_20260121.xlsx: OK
FM-WI-FSM-036-A01 …_SWQT_20260816_ext.xlsx: OK
FM-WI-FSM-036-A01 …_SWQT_Home_20260809.xlsx: OK
```

**3 / 3 OK，0 個 improperly-formatted 警告**（記錄間之空行已去除 ——
`features/comfort/BASELINE.sha256` 現行仍有 1 個該警告，本包不動他 feature，
記於此供日後一併整理）。

### 4.1 一個順帶查到的事：該雜湊檔原本也不會被追蹤

建檔後 `git status` **看不到它** —— `.gitignore` 之 `archive/forms_superseded/*`
把整個目錄排除，其註解逐字寫著

> archiving preserves the FILES, not their hashes-in-git … That gap is Tier 2,
> not settled here.

**R-U12 正是那條註解所指之 Tier 2，而它現在已裁。** 故本層於 `.gitignore`
加一條例外 `!archive/forms_superseded/BASELINE.sha256`（**xlsx 維持不追蹤**，
公司文件之規則不變），並改寫該段註解指向本輪之處置。

> **若不加這條，R-U12 只做了一半**：檔案在、雜湊也在，但雜湊只在磁碟上，
> 換一台機器或重新 clone 就沒了 —— **而那正是 R-U12 那句話本身在說的事。**

檔內另記每檔之 bytes 與 mtime，以及 R-U12 之理由逐字
（**保住檔案與保住雜湊是兩件事**），並具名
`…_Home_20260809.xlsx` 為 **R-U6 之 style authority 在 repo 內之唯一載體**。

| 檔 | bytes | SHA256（前 8）|
|---|---|---|
| `…_SWQT_20260121.xlsx` | 65,823 | `cd876c20` |
| `…_SWQT_20260816_ext.xlsx` | 200,654 | `4b3d4470` |
| `…_SWQT_Home_20260809.xlsx` | 119,885 | `1895fb2a` |

> 前後兩者之 bytes 與 02a §分析層自陳之錯誤第 3 點相符
> （65,823／119,885，非 65,822／119,890）。**本包之數字由 `os.stat` 實測取得。**

---

## 5. 作業 5 — ANOMALIES.md 狀態

| 項 | 新狀態 | 備註 |
|---|---|---|
| A-UP03 | RESOLVED | 01 輪已辦，未動 |
| **A-UP05** | **RESOLVED**（R-U11）| 裁定逐字照錄，**其「非經成因查證」之記載限制另立一段照錄並自陳其效力** |
| **A-UP07** | **RESOLVED**（R-U8）| 含「成因為下放包之誤、執行層停下為正確」之裁定文字 |
| **A-UP08** | **RESOLVED**（R-U10）| 採 (b)，不產生新 DR |
| A-UP09 | **PENDING → 修補完成待覆核** | 見下 |
| A-UP02／A-UP04／A-UP06 | PENDING | A-UP06 增記本輪 18/20 之實測 |

### 5.1 A-UP05 之記載限制，照錄後另加一段

02b 明文要求「須照錄其『非經成因查證』之記載限制」。除逐字引裁定外，
另立一段講明其效力：

> **本條之結案依據為裁定，不是查證。**
> 「123,717-byte 之檔到哪裡去了」這個問題**至今沒有答案**。
> **「已結案」與「成因已查明」是兩件事**，日後任何人引用本條時
> 不得把前者讀成後者。

### 5.2 A-UP09 —— 本層不自行改判 RESOLVED

02b 作業項 5 定「A-UP09 保持 PENDING **直至 R-G3 修補完成**」。
**修補已於本輪完成**（作業 3）。惟其**狀態變更屬 Tier 2**，
本層不自行改判，改標為「PENDING → 修補完成待覆核」並於條內記明。

> 若分析層認為修補完成即滿足解除條件，請下一包裁 RESOLVED；
> **本層不把「我做完了」當成「它結案了」。**

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷（02b 明文要求，不得省略）

**有，四項。** 逐項列其性質，不以「本輪未授權」帶過：

| # | 該驗而未驗 | 何以未驗 | 性質 |
|---|---|---|---|
| 1 | **R-G3 之修補是否真的擋得住** —— 本輪只**寫了**警示與範例，**沒有一道機器檢查**會在有人再次 `wb.save()` 時出聲 | 02b 只要求改 canon 文字 | **真缺口**。A-UP09 自己說了「靜態讀取驗不到只在寫入時才成立的性質」，而現行防線是一段散文。建議下一包立一道 gate：對產出檔驗 `x14:dataValidation` 節點數與 zip member 集合（Comfort 之 `write_back` §3.3 已有同型 assertion 可直接借） |
| 2 | **R-U10 之「不是交付要求」未向客戶側複驗** | 裁定為 Pei 之權限，本層照辦 | 記載限制。本層所驗者僅「rev C 無該分頁」（實測 9 sheets），**「客戶不要求它」是裁定，不是量測** |
| 3 | **`framework.md` 之 splice 範例未實跑** | 該範例之對象為 Media 之 rev A/B 工作簿，不在本 feature 之素材內 | 記載限制。`surgical_save` 本身在 Comfort 有 35 次實跑紀錄（ENTRY 001–035），但**本節之範例碼本身未被執行過** |
| 4 | **其餘三個 feature 之 `BASELINE.sha256` 是否也帶格式警告** | 本包不動他 feature | 已知：`features/comfort/` 有 1 個。未逐一掃 |

**另記一件不在作業項內、但本輪順帶查到的事**：`archive/forms_superseded/`
在本輪之前**不受任何 `shasum -c` 保護** —— R-G2 於 01 輪把檔案救了下來，
而其雜湊只存在於 FORMS.md 的散文裡。R-U12 正是補這一段；
**該缺口存在了一整輪而沒有人出聲**，這一點值得記，不只是修掉。

---

## 7. 未執行（作業 6–8）

| 作業 | 前置 | 現況 |
|---|---|---|
| 6 Recon | DR #1（037）| **MISSING** —— 期望值已填（R-U8），閘未跑 |
| 7 037 側複驗 | DR #1 | 未執行；`BASELINE.sha256` 尚未加入 037 |
| 8 Layer 2 草案第二版 | DR #1 之分群 | 未執行；§4.2 之三項命名問題（`All Profiles Tab` 為 UI widget 名、`Profile Overview`／`New Profile Setup` 與 Test Group 重複前綴）待 037 到齊後隨草案一併處理 |

**未動**：`docs/handoff/01*`（已結輪次不回溯編輯）、他 feature 之任何檔案、
`spec-index/`、任何 `BASELINE.sha256` 之既有列。**git 未執行。**

---

## 8. 本包所動之檔

| 檔 | 動作 |
|---|---|
| `features/user_profiles/RULINGS.md` | ＋六條逐字 ＋ supersede 註記 ＋ 執行層回報 |
| `features/user_profiles/ANOMALIES.md` | A-UP05／07／08 改 RESOLVED；A-UP06 增 18/20 實測；A-UP09 增修補完成記載 |
| `features/user_profiles/DATA_REQUESTS.md` | 第 2 列改「部分到齊 18/20」；**新增第 4 列**；＋第 4 列之實測依據 |
| `features/user_profiles/feature.yaml` | `recon_assertions` 三閘由 TBD 改填 |
| `features/user_profiles/docs/INDEX.md` | 新增第 02 列與現況更新 |
| **`docs/fw036/framework.md`** | §Workbook sync 三處（禁用警示／splice 範例／rev A/B only）—— **canon 級，diff 摘要見 §3** |
| **`archive/forms_superseded/BASELINE.sha256`** | 新建（3 檔）|
| **`.gitignore`** | 加 `!archive/forms_superseded/BASELINE.sha256` 例外並改寫該段註解（見 §4.1）|
