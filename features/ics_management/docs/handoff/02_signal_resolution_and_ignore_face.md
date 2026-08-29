# 下放包 02 — ICS Management：訊號解佔位、Stuck Button ignore 面、CFTS020 偵察（2026-08-29）

## §0 背景與本包之量測時點

上繳包 01（`docs/upstream/01_onboarding_first_batch.md`）已審結。b01 六條收下，
不退件。分析層據其發現即裁 R-ICS5～R-ICS8，Pei 2026-08-29 裁定 R-ICS9、R-ICS10
（「准」）。本包三項作業皆源自上繳包 01 §六、§八之實測。

**本包所書之前提，其量測時點為 2026-08-29 上繳包 01 落檔之時**（R-DD26 v2(g)）。
執行前依 R-DD26 v2(f) 先驗前提，不符即驗而不做並寫出驗法。前提三條：

| # | 前提 | 上繳包 01 之出處 |
|---|---|---|
| P1 | `forms/Logical Identifiers and CAN Mapping v1_78.xlsx` 存在，`CAN Mapping` 分頁 9 個 ICS LID 全命中 | §六-4 |
| P2 | `forms/DTCs Matrix Core List Rev. 1.6.xlsx` 存在於 repo | §六-3 第 3 點 |
| P3 | `inputs/R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD_20260310-1533.docx` 存在，407 個相異 ObjectID | §六-2 |

## §1 禁區

1. **git 一律禁**：`add`／`commit`／`push`／`checkout`／`stash` 皆不執行（FO §8.8）。
2. **分析層之簿不動**：`framework.md`、`RULINGS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md` 一字不改；建議事項寫入上繳包，由分析層落。
3. **不代擬條文**：新條文編號、條文內容由分析層出（FO §8.5 之一）。
4. **不改全域**：canon（IN／FO）、`GATES.tsv`、`RULINGS.sha.tsv`、`PATH_POLICY_BASELINE.tsv` 皆不動。四支開工前即紅之閘不在本包射程。
5. **不搬素材**：外部素材一律綁原件不複製（R-ICS10）。`inputs/` 之增減屬 Pei。
6. **不擴範圍**：Display／Browse／Navigation 三面本包**只偵察不生 TC**（R-ICS9(e)）。
7. **不挪門檻**：ignore 面不得挪用 DTC 面之 120 s（R-ICS9(d)）。

## §2 裁決引用

| 條 | sha8 | 本包用於 |
|---|---|---|
| R-ICS1 | `3e48552b` | Test Group = `ICS` |
| R-ICS2 | `ad557b5d` | 適用域三軸（ECU／Radio／EE） |
| R-ICS3 | `b10318e0` | DTC 面 120 s；**不得外溢至 ignore 面** |
| R-ICS4 | `85de9871` | verbatim 來源分流 |
| R-ICS5 | 待實測 | 落點 `sandbox/`／`generated/b02/` |
| R-ICS6 | 待實測 | priority 依 TEST_CASE_PRIORITY.md 自判 |
| R-ICS7 | 待實測 | Description 型物件充錨之限制 |
| R-ICS8 | 待實測 | LID→CAN 解佔位路徑（作業 A 之全部依據） |
| R-ICS9 | 待實測 | CFTS020 納源、010 二行為面、ignore 面佔位 |
| R-ICS10 | 待實測 | 外部素材綁原件 |

R-ICS1～4 之 sha8 取自上繳包 01 §1（執行層實測）；R-ICS5～10 為本包落檔之新條，
**其 sha8 由執行層以 `scripts/rulings_hash.py --target features/ics_management/RULINGS.md`
實測後回報**，分析層不自記憶推定（R-G23／R-G13）。回報之 sha8 與本表「待實測」
之格併入上繳包 §1。

## §3 作業清單

### 作業 A — 依 R-ICS8 解 b01 之 DR-ICS8 佔位

對 b01 之 S1／S2／S3 三處 `PENDING: DR-ICS8 <ICSMuteButton CAN signal>`：

1. 依 R-ICS8(a)(b) 自 LID v1_78 `CAN Mapping` 取 `ICSMuteButton` 之 Atlantis High 欄 Signal Name。
2. 該格多名並列時依 R-ICS8(c)：以綁定之二 DBC 篩，查有者取之；**二 DBC 皆查有且不同名者，停下回報**（升級條件 E1），不自選。
3. 依 R-ICS8(d) 取值之逐字列舉，套 IN §8.7.5(a) 之 `$MESSAGE.Signal$ = <raw> (<label>)`。
4. 改寫後 `has_pending` 隨之更新；**V3 之 `PENDING: DR-ICS4` 不動**（CFTS019 未到）。
5. b01 之 JSON 就地修訂，`manifest.json` 之 `tcs_sha256` 重算（該檔自注之義務）。

### 作業 B — DTC 成熟條件實測，修訂 S1／S2

上繳包 01 §八-4 指出 S1／S2 未給 DTC 成熟等待時間，台架可能誤判 FAIL。

1. 自 CFTS020-4819296 取 ICS stuck DTC 之 monitor type／rate／healing 逐字。
2. 依其所轉引，查 `forms/DTCs Matrix Core List Rev. 1.6.xlsx` 之 ICS stuck button 條目，取 Enable／Mature 條件。
3. **查得具體成熟條件** → S1／S2 之 procedure 增一等待步驟（`Wait for <值> …`，值逐字取自該表），ER 對應一行；**查無或條件不以時間表述** → 不臆造，於該步驟寫 `PENDING: DR-ICS11 <ICS stuck button DTC maturation condition>`，並於上繳包建議登 DR-ICS11（編號由分析層確認）。
4. 不動 S1／S2 之其餘欄位，不改其 priority（R-ICS6 已採認）。

### 作業 C — Stuck Button ignore 面 TC（b02 新增）

依 R-ICS9(c)(ii)。上半 verbatim 取 CFTS020-4819617 原句（不改字，正規化四項照上繳包 01 §0）。

- **預期 2 條**（IN §8.2.2，二獨立 partial failure）：
  - I1：持續按壓逾 `<Tstuck_button>` 後，該按鍵之按壓請求被忽略
  - I2：放開按鍵、收到 released 訊號後，該按鍵恢復回應
- 門檻一律 `PENDING: DR-ICS10 <Tstuck_button value>`（R-ICS9(d)）。**不得寫 120 s**。
- Test Set = `Stuck Button`，trace `SWE-ICS-010`，錨 `CFTS020-4819617`。
- 4819617 末句轉引 `{CFTS020-479}`（physical button press signals）—— 該號為**短號需求 ID 非 ObjectID**，依 IN §10.7(a) **不得作錨**，僅得於 reasoning 引用。
- 執行層若判 1 條或 3 條較合，照判並寫出理由（預期數字為分析層之預期，非拘束；差異須具名，見 §5）。

### 作業 D — CFTS020 三面偵察（不生 TC）

對 Display／Browse／Navigation 三面，各出一份偵察，內容限：

1. 該面之 CFTS020 章節與其下**逐物件**之 ObjectID、Artifact Type、ECU／Radio／EE 三軸實值。
2. 依 R-ICS2 三軸判定**適用／不適用**，逐物件給判與所印之理由（R-DD23 三欄）；first-match 落 fallback 者標 WARN 並列出所有未命中之判準（R-DD24）。
3. 與 SWRA 003／004／006／007／008／009 之對應建議（哪個 ObjectID 對哪條 RD），**只建議不裁**。
4. `1.5.1.1.2 {4819389}` 之分支歸屬須明測 —— 上繳包 01 §六-2 稱 `1.5` 為 PowerNet only，若確認則該節不適用本 DUT，Display 面只餘 `1.8.1.1.1 {4819556}`。
5. 是否觸及 A-ICS1 之錯置列（006／009）—— 若 CFTS020 有直載原句，依 R-ICS4 可繞過 SWRA 位移；**此判由分析層下，本包只列材料**。

## §4 掃描條件

| 項 | 條件 |
|---|---|
| docx 抽取 | 沿上繳包 01 §0 之法（`word/document.xml`、`</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape`） |
| 逐字比對正規化 | 沿上繳包 01 §0 四項（彎引號→直引號、NBSP→空格、連續空白摺一、去頭尾空白、去句末單一句號），**除此不動一字** |
| CFTS020 物件辨識 | 粗體行首 `{7 位數字}:` 之屬性頭；屬性軸取 `[ECU:…]`／`[Radio:…]`／`[EE Architecture:…]` 三者，逗號切分後去頭尾空白 |
| LID 掃描 | `CAN Mapping` 分頁；表頭列與 `Atlantis High` 欄群之欄號**須實測回報**，不沿用上繳包 01 之 26／28（該值為 v1_78 當次實測，本包須自驗） |
| DTCs Matrix 掃描 | 分頁名、表頭列、所取欄名須逐一書出；以欄名引用不以 `c{n}`（R-DD10） |
| 字數 | `str.split()` token 數 |
| TC 欄位掃描 | 限 `pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`／`test_item`／`specification_reference` 六欄 |
| 列號 | 一律 1-based（R-DD10） |

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | b01 之 DR-ICS8 佔位 | 3 處 → 0 處（或具名列出因 DBC 查無而保留者及其備援名） |
| 2 | b01 之 DR-ICS4 佔位 | 1 處 → 1 處（不動） |
| 3 | b02 新增 TC | 2 條（I1／I2） |
| 4 | b02 新增 TC 之 trace | 皆 `SWE-ICS-010` |
| 5 | b02 新增 TC 之錨 | 皆 `CFTS020-4819617`；不得出現 `CFTS020-479` |
| 6 | b02 新增 TC 之門檻佔位 | ≥ 1 處 `PENDING: DR-ICS10` |
| 7 | S1／S2 修訂 | 各 +1 等待步驟，或各 +1 `PENDING: DR-ICS11` 佔位 |
| 8 | 偵察面 | 3 面，逐物件三軸實值齊備，**TC 新增 0** |
| 9 | Test Set 相異值 | b01+b02 合計仍為 `Stuck Button`、`Volume Control` 二者 |
| 10 | 語言 | 交付六欄與 test_item 無非 ASCII（R-DD22 同族） |

**相符者亦列**（FO §8.2）。不符者不自行調和，逐項具名回報。

## §6 升級條件（遇則停，寫出所驗與所停之處，不自裁）

- **E1**：LID 之 Atlantis High 欄多名並列，且綁定二 DBC 皆查有而名不同 —— R-ICS8(c) 之 first-match 無法決斷。
- **E2**：`ICSMuteButton` 於 LID Atlantis High 欄查無，或 v1_78 檔不存在（P1 不成立）。
- **E3**：DTCs Matrix 無 ICS stuck button 條目，或其 Enable／Mature 條件轉引第三份未在 repo 之文件（P2 部分不成立）。
- **E4**：CFTS020-4819617 之 ECU／Radio／EE 三軸實測**不含**本 DUT —— 則 R-ICS9(c)(ii) 之範圍前提失據，ignore 面 TC 不得生成。
- **E5**：偵察發現 CFTS020 直載 006／009 之原句，且與 SWRA 位移之判定衝突 —— 屬 A-ICS1 之再判，Tier 3。
- **E6**：任一作業須改動分析層四簿方能完成。

## §7 上繳要求

1. 沿上繳包 01 之體例（§0 量測基礎先揭露、§三分法、§獨立判斷、§未結 DR 清單）。
2. **§1 須含 R-ICS1～10 之實測 sha8**（R-ICS5～10 為新條，本包標「待實測」者由此填實）。
3. §預期數字對照須逐項對本包 §5 之 10 項，相符者亦列。
4. 未結 DR 清單：現為 **DR-ICS1～10 全開**；若作業 B 觸發 DR-ICS11 之需求，於清單具名建議（編號待分析層確認）。
5. 落點依 R-ICS5：`.json` → `generated/b02/`，`.xlsx` → `sandbox/`。
6. 四支全域紅閘之開工前／完工後兩次實跑照列，差為 0 即書 0。
7. §獨立判斷：本包是否仍有該驗而未驗者 —— 特別是 b01 之 VOLUME POP_UP 顯示條件（上繳包 01 §八-3 之 FF 風險）本包未列作業，執行層若認為應先處置，具名回報。

## §8 追補（2026-08-29，分析層；執行前必讀）

依 Pei 同日「裁」（R-ICS11／12）與分析層實測（R-ICS13）追補四項：

1. **E1 預解（R-ICS13）**：§6 之 E1 不再成立 —— LID 多名且綁定 DBC 皆查有時，取發送節點 = ICS 之訊息（CLIMATIC_PANEL.*）為主路徑，DIS_CENTERSTACK 記備援不入 TC。執行層仍須逐訊號實測 BO_ 發送節點回報；非 ICS 發送而無他選者依原 E1 停下。實測基礎：`BO_ 1050 CLIMATIC_PANEL: 8 ICS`（BHCAN）。
2. **作業 D 新線索（只偵察不裁）**：`spec-index/sources/` 實有 33 本 HMI L&F。相干四本：`Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf`（knob2 browse/tune UI 面候選）、`Core HMI Logic and Flow … (February 2 2023).pdf`（Screen Off／電源鍵 UI 面候選）、`Menu Bar and App Drawer … (September 11 2023).pdf`（Enter/Back 導航面候選）、`RVC+PAM R1 Low SR24 1A (June 25 2021).pdf`（(012) 面候選）。作業 D 一併列此四本之目次命中情形（只列章節與命中，不判採用 —— 納源屬裁決）。
3. **CFTS022 新版（R-ICS12）**：26PI2.5 真 docx 待 Pei 置入 inputs/。本包執行時已落檔 → 依 R-ICS12(b)(c) 改綁並覆驗 b01 之 4 句／6 物件，結果入上繳包；未落檔 → 依 (d) 維持現狀。
4. **CFTS019（R-ICS11）**：作業 D 附帶偵察 `features/audio_mgmt/inputs/` 之 CFTS019 七件：音量階數域與 VOLUME POP_UP 顯示條件所在章節（只入報告；不解 V3 之 PENDING、不充 verbatim 來源 —— 版本未確認）。

預期數字修正：§5-1 之「因 DBC 查無而保留」依 R-ICS13 實測預期不發生（Radio_btn4 在庫含 VAL_），發生即屬意外，須具名。§5 其餘不變；本追補新增預期一項：作業 D 之四本 HMI L&F 目次命中清單、CFTS019 七件偵察各一節。
