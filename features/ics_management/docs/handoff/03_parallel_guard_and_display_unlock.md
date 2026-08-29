# 下放包 03 — 並行防護、CFTS020 全域重判、Display 面解鎖（2026-08-29）

## §0 背景與量測時點

上繳包 02 已審結，b02 之 I1／I2 收下。分析層即裁 R-ICS14～R-ICS17，
並採認另一分析層實例所落之 R-ICS2 v2（A-ICS20）。

**本包所書之前提，量測時點為 2026-08-29 14:0x（分析層落檔之時）。**
執行前依 R-DD26 v2(f) 先驗，不符即驗而不做並寫出驗法。

| # | 前提 | 出處 |
|---|---|---|
| P1 | `RULINGS.md` 現有錨點 17 個（R-ICS1、R-ICS2 v1、R-ICS2 v2、R-ICS3～R-ICS17） | 分析層 live grep `^## R-ICS` |
| P2 | `ANALYSIS_LOCK.md` 存在，`holder: analysis-A`、`released: null` | 分析層落檔 |
| P3 | `ANOMALIES.md` 至 A-ICS20；`DATA_REQUESTS.md` 至 DR-ICS13，13 條全開 | 分析層落檔 |
| P4 | CFTS020 物件母數 **2180**（屬性頭 `^\d{7}: \[`）；407 為章節數，不得混用（R-ICS18 未立，見 A-ICS15） | 上繳包 02 §1.1 |
| P5 | b02 之 82 物件判定與「1.8.1.3 之 24 中 23 不適用」皆為 R-ICS2 **v1** 下之結果，**已作廢** | R-ICS2 v2(d) |

**開工第一件事**：重測本檔 sha256 並入上繳包 §0（R-ICS17(e)）。
與執行層自身記錄不符即停。

## §1 禁區

1. **git 一律禁**（FO §8.8）。
2. **分析層五類檔不動**：`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／
   `framework.md`／`docs/handoff/*.md`。**`ANALYSIS_LOCK.md` 亦不得寫**——
   執行層永非權杖持有者（R-ICS17(a)）。
3. **不代擬條文**（FO §8.5 之一）。建議入上繳包。
4. **不改全域**：canon、`GATES.tsv`、`RULINGS.sha.tsv`、`PATH_POLICY_BASELINE.tsv`。
5. **不搬素材**（R-ICS10）。
6. **不生成 009／005 之 TC**（R-ICS15(b)(c)：009 待 DR-ICS13、005 待 DR-ICS1）。
7. **不挪門檻**：ignore 面不得用 120 s（R-ICS9(d)）；`<TPeriodToCountKnobDetents>`
   不得臆值（DR-ICS12）。

## §2 裁決引用（sha8 由執行層以 `rulings_hash.py` 實測填實）

| 條 | 本包用於 |
|---|---|
| R-ICS2 **v2** | 作業 B 之判準（v1 一律不得再用）|
| R-ICS7 | Description 型物件之充錨限制 |
| R-ICS9 | CFTS020 之地位、(b) 章節屬性不代替子物件、(e) 三面解鎖之節奏 |
| R-ICS8／R-ICS13／R-ICS14 | 作業 E 之 LID→CAN 路徑與取捨 |
| R-ICS15 | 作業 C：006／007 解鎖，009／005 不解鎖 |
| R-ICS16 | b01 之 S1／S2 現狀為採認態，作業 D 不得回改 |
| R-ICS17 | 作業 A 之全部依據 |

上繳包 §1 須列 **R-ICS1～R-ICS17 全部**之實測 sha8（含 `R-ICS2 v1` 與 `v2` 兩列；
二者同 `ruling_id` 而內容不同，**須以 sha8 分辨**，體例沿 R-DD6 v1／v2 之並列法）。

## §3 作業清單

### 作業 A — `scripts/ledger_guard.py`（並行防護）

新腳本，落 `features/ics_management/scripts/`。功能限四項，不做他事：

1. 讀 `ANALYSIS_LOCK.md`，印出 `holder`／`acquired`／`released`；
   `released` 非 null 而 `holder` 非 null 者報 **INCONSISTENT**。
2. grep `RULINGS.md` 之 `^## R-ICS`，印出全部錨點與其行號；
   **同名錨點出現 ≥2 次且非 `vN` 形式者報 DUPLICATE**（`R-ICS2 v1`／`v2` 為合法並存）。
3. 對 `ANOMALIES.md`／`DATA_REQUESTS.md` 之 `A-ICS{n}`／`DR-ICS{n}` 作同樣重號檢查，
   並印出各自最大號。
4. 印出五類 scope 檔之 sha256 與 mtime。

exit code：有 DUPLICATE 或 INCONSISTENT → 1，否則 0。
**不自動修復、不寫任何檔。**

### 作業 B — CFTS020 全域重判（R-ICS2 v2）

1. 以 v2(b) 判準重跑全 **2180** 物件，四欄輸出（R-DD23／24）：數據、判斷、
   所印之理由、強度（正面命中／WARN）。
2. 重出偵察報告，**覆蓋** b02 之 `docs/reports/02_cfts020_face_recon.md`
   （新檔 `03_cfts020_recon_v2.md`，舊檔保留不刪，標 superseded 於新檔開頭）。
3. 報告須含：全域判定分佈（適用／不適用／WARN 各數）、
   與 v1 判定之**差異表**（由不適用轉適用者逐一列出，含 ObjectID 與轉變原因）。
4. 三面（Display／Browse／Navigation）之物件清單依 v2 重列。

### 作業 C — 006／007 之 TC 生成（R-ICS15(a)）

**前置**：作業 B 之 v2 判定須先確認 `1.8.1.1.1 {4819556}` 群與
`1.8.1.1.3 {4819570}` 群為適用。**判不適用即停下回報，不生成**（升級 E2）。

- 006（題 `ICSPowerButton`）→ Test Set `Display Control`，上半取 4819556 群直載原句。
- 007（題 `ICSScreenOffButton`）→ 同 Test Set，上半取 4819570 群直載原句
  （含 3 秒 `TOUCH SCREEN TO TURN ON` 計時、`$TGW_DISP_STAT$`／`$RQ_DISP_INTS$` 送出）。
- 訊號寫法依 IN §8.7.5(a)＋R-ICS8：`ICSPowerButton`／`ICSScreenOffButton` 之
  LID→CAN 由作業 E 供給；作業 E 未解者以 `PENDING: DR-ICS8 <…>` 佔位，不臆造。
- 3 秒為 spec 明載（4819572 逐字），得直用，非造值。
- 拆分依 IN §8.2.2／§8.3：一物件一 partial failure 即一 TC；
  同一觸發之多後果併一 TC 多行 ER（IN §5.7）。

### 作業 D — V3 補佔位（A-ICS17）

b01 之 V3「一次連轉三格」隱含 detent 計數時間窗。
於 `pre_conditions` 增一行 `PENDING: DR-ICS12 <detent counting time window>`。
**S1／S2／S3 與 V1／V2 一字不動**（R-ICS16 已採認其現狀）。
`b01_tcs.json` 就地修訂，`manifest.json` 之 `tcs_sha256` 重算。

### 作業 E — 其餘 8 個 LID 入 DBC 驗證（DR-ICS8 收口）

對 `ICS_KNOB1_DIR`／`ICS_KNOB1_VAL`／`ICS_KNOB2_DIR`／`ICS_KNOB2_VAL`／
`ICSPowerButton`／`ICSScreenOffButton`／`Enter_Button`／`Back_Button`
（`ICSMuteButton` 已於 b02 解），逐一：

1. LID v1_78 `Atlantis High` 欄之 `Signal Name`（多名並列時全列）；
2. 二綁定 DBC 之存在性與 `BO_` 發送節點；
3. 依 R-ICS13 取捨（發送節點 = ICS 者為主路徑），其餘記備援；
4. `VAL_` 列舉逐字（無列舉者記 `無 VAL_`，不自造 label）。

輸出對照表入上繳包並落 `generated/b03/lid_dbc_map.json`。
**本作業不改任何既有 TC**（除作業 C 取用之二訊號外）。

### 作業 F — §8 追補未執行之二偵察（補做）

1. `spec-index/sources/` 四本之目次命中：`Media HMI Logic and Flow R1L-L
   (Febuary 9th, 2026)`（knob2 browse/tune）、`Core HMI Logic and Flow
   (February 2 2023)`（Screen Off／電源鍵）、`Menu Bar and App Drawer
   (September 11 2023)`（Enter/Back）、`RVC+PAM R1 Low SR24 1A (June 25 2021)`（(012)）。
   **只列章節與命中，不判採用**（納源屬裁決）。
2. `features/audio_mgmt/inputs/` 之 CFTS019 七件：音量階數域與
   `VOLUME POP_UP` 顯示條件之所在章節（R-ICS11；只入報告，**不解 V3 之
   `PENDING: DR-ICS4`、不充 verbatim 來源**——版本未確認）。

## §4 掃描條件

沿上繳包 02 §0 全部條件。另：

| 項 | 條件 |
|---|---|
| CFTS020 物件母數 | **2180**（屬性頭 `^\d{7}: \[`）。407 為章節數，報告中若引須明標其為章節數 |
| v2 判準實作 | (i) Radio ∈ {R1L, R1L-R, allSys} ∧ EE ∈ {Atlantis High, All}；(ii) ECU 軸**存在時**須含 {ICS, LTM}，不存在時不視為不適用亦不記 WARN |
| 差異表 | 以 ObjectID 為鍵，v1 判定 → v2 判定，附轉變原因（軸缺／軸值） |
| PDF 目次抽取 | 作業 F 之四本為 PDF；抽取法須於上繳包 §0 載明，並註明是否為掃描檔（無文字層者記 `NO_TEXT_LAYER`，不強解） |
| LID 表頭 | 每次自驗，不沿用前包之欄號 |

## §5 預期數字（相符者亦列）

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard.py` 開工前實跑 | exit 0；錨點 17（含 `R-ICS2 v1`／`v2`）、A-ICS 最大 20、DR-ICS 最大 13 |
| 2 | CFTS020 重判母數 | 2180 |
| 3 | v2 之適用數 | > 28（v1 之數）；具體值實測，**分析層不預設** |
| 4 | 4819617 之 v2 判定 | 適用（R-ICS2 v2(e)）|
| 5 | `1.5` 之需求物件 | 仍 100% 不適用（v2 不改此結論，因其 EE = PowerNet 為實值命中失敗，非軸缺）|
| 6 | 006 面 TC | ≥ 2 條；實際數依 4819556 群之適用物件數，差異須具名 |
| 7 | 007 面 TC | ≥ 2 條；同上（4819570 群）|
| 8 | b03 新增 TC 之 Test Set | 皆 `Display Control`（framework 新增第三個相異值）|
| 9 | V3 之 PENDING | 1 → 2（增 DR-ICS12）|
| 10 | LID 驗證 | 8 個 LID 全數有判（取用名或備援或「DBC 查無」），無「未查」 |
| 11 | 作業 F | 四本目次命中清單 ＋ CFTS019 七件各一節；**TC 新增 0** |
| 12 | `ledger_guard.py` 完工後實跑 | exit 0，錨點／最大號與開工前相同（執行層不寫台帳）|

## §6 升級條件（遇則停，寫出所驗與所停之處）

- **E1**：`ledger_guard.py` 開工前實跑報 DUPLICATE 或 INCONSISTENT ——
  台帳已被他者寫入，**停下，不做任何作業**，立即回報。
- **E2**：作業 B 之 v2 判定顯示 `4819556` 群或 `4819570` 群不適用 ——
  R-ICS15(a) 之解鎖前提失據，作業 C 不得執行。
- **E3**：v2 判定使 b01／b02 之既有 8 條中任一條之錨物件轉為不適用 ——
  屬既有交付之回收，Tier 3。
- **E4**：LID 之某訊號於二 DBC 皆查無，且 CFTS020 亦無其他可觀察載體。
- **E5**：作業 C 所需之 3 秒／`TGW_DISP_STAT` 值域於 CFTS020 為符號無值 ——
  依 IN §8.4.3 佔位並建議新 DR，不臆造。
- **E6**：任一作業須改動 §1 禁區所列之檔方能完成。

## §7 上繳要求

1. 沿上繳包 01／02 之體例（§0 量測基礎、三分法、獨立判斷、未結 DR 清單）。
2. **§0 須含本檔之重測 sha256**（R-ICS17(e)）。
3. §1 須列 R-ICS1～R-ICS17 全部 sha8，`R-ICS2 v1`／`v2` 並列。
4. **§須含 `ledger_guard.py` 開工前／完工後二次實跑輸出**（R-ICS17(f)）。
5. §預期數字對照逐項對 §5 之 12 項，相符者亦列。
6. 落點依 R-ICS5：`.json` → `generated/b03/`，報告 → `docs/reports/`，
   腳本 → `features/ics_management/scripts/`。
7. 四支全域紅閘之開工前／完工後兩次實跑；`lint_paths` 之基線外數須逐筆具名
   （b02 曾因他 feature 併行作業而 +1，本包須能分辨）。
8. §獨立判斷：特別回答——v2 重判後，`framework.md` 之 Layer 2 六組是否仍合
   IN §4.1.3 之 granularity（Display Control 面解鎖後 TC 數將變），
   **只建議不改**（framework 屬分析層之簿）。
