# 上繳 17 —— batch01_v3（缺陷修正、10 降 8）與 batch02（第二批 10 條）

執行層寫入。依據：`docs/handoff/38_pilot_review2.md` §7。canon §8.2 六節。

**pilot 第一批：Pei 於 2026-08-22 裁定通過。**
**DR 送件文 1–5 已由 Pei 送出（2026-08-22）。**

| 項 | 內容 | 狀態 |
|---|---|---|
| — | 依 R-VS18（常設）先建本檔 —— 38 包 §7 未列此項，本層依常設條文補 | ✅ |
| D-5 | 鎖定 `framework.md` | ✅ **已鎖定** |
| D-6 | Layer 3 正規化名欄 ＋ 三項標已解 | ✅ |
| D-7 | `PLAYBOOK.md` §6 狀態板 | ✅ P0–P5 結案 |
| D-8 | DR 標送出／待覆 | ✅ **5 送出／4 待送** |
| D-9 | 未結 DR 兩態分列 | ✅ |
| D-10 | 37 包記明送出項次 | ✅ 第 1–5 項 |
| D-11 | A-VS62 ＋ profile 增列 D-3 | ✅ |
| **W-56** | `batch01_v3.json` | ✅ **8 條，§9 檢查 0 違規** |
| **W-57** | `batch02.json` | ⚠ **10 選入，4 條因缺件未撰寫，交付 6** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-56 —— batch01_v3

| 項 | v2 | **v3** |
|---|---:|---:|
| 批次條數 | 10 | **8**（38 包 §4 之預期為 8，**符**） |
| 移出待覆 | — | **2**（`Stop-Start-006` DR-19／`SwitchLHD/RHD-010` DR-20） |
| §9 機械檢查違規 | 1 | **0** |
| DBC `VAL_` 逐字核對 | 27 行 0 不符 | **0 不符** |

三項缺陷逐項：

| 缺陷 | leaf | 修法 | 結果 |
|---|---|---|---|
| **D-1** false pass | `SwitchLHD/RHD-009` | 改為 §5.6 之 baseline 比較：左駕記錄 → 右駕比較「與 step 2 相同」 | ✅ `design_method` 隨之由 Functional Based 改為 **Equivalence Partitioning**（其驗證的是兩個等價類之輸出相同） |
| **D-2** 末步驟無 action | `Stop-Start-004`／`-005` | 驗證併入最後一個**可執行**步驟（送 `$STATUS_CCAN3.ESS_ENG_ST$` ＋ check） | ✅ 二者末步驟皆含 action ＋ check |
| **D-3** 可執行步驟 < 2 | `Stop-Start-006` | 自批次移出，`split_reason` 記 `BLOCKED-BY-DR-19: executable steps < 2` | ✅ 另存 `blocked_pending_dr.json` |

### 1.2 W-57 —— batch02 之選取與 sibling 比對

| 項 | 值 |
|---|---:|
| Common Features 可用 leaf | 42 |
| batch01 已用 | 10 |
| **本批可選** | **32** —— 「可用 leaf 不足 10」之升級條件**未命中** |
| 依 reqid 升冪選入 | **10** |
| **因來源缺件未撰寫** | **4** |
| **實際交付** | **6** |
| §9 機械檢查違規 | **0** |

**Sibling Rows 已注入**（本輪起不得再省）：本批 10 條與 batch01_v3 之
`ThirdRowHeadrestDump-025` **同屬 Layer 3 `ThirdRowHeadrestDump`**，
故 11 列全數互為 sibling 候選（canon §4.1.4(2)）。

| 項 | 結果 |
|---|---|
| `duplicate_of` | **無** —— 11 列之 trigger 與 verification target 皆相異 |
| 與 batch01_v3 **已放行**之 `-025` 是否重複 | **否** —— `-025` 驗致動行為（按鍵→頭枕下降），本批驗**可及性與可選性** |
| `distinguishing_axis` | **6 / 6 全數輸出**，軸為 `mode`（進入路徑）2／`trigger_state`（電源模式值）3／`input_data`（PROXI 配置）1 |

**「sibling 比對發現 batch01 已放行者與新批重複」之升級條件未命中。**

### 1.3 `$PowerMode$` 之值域 —— 三個值可用、兩個不可用，逐項具名

DBC `CmdIgnSts`（`STATUS_BH_BCM2` id 1132／`BCM_FD_10` id 1153，兩份**值表相同**）：
`0 Initialization／1 IGN_LK／3 ACC／4 RUN／5 START／7 SNA`

| CFTS044 值 | 全文次數 | 依據 | 可用？ |
|---|---:|---|---|
| `[Ignition lock / IGN_LK]` | 11 | DBC 標籤**逐字相符** | ✅ |
| `[4h:Ignition run]` | **5** | **CFTS044 自載原始碼值 `4h`** → DBC `4 (RUN)` | ✅ |
| `[IGN_RUN]`／`[Ignition run / IGN_RUN]`／`[Ignition run]` | 20／5／9 | 同上之並列 | ✅ |
| `[Ignition start / IGN_START]` | 3 | 無對應、無原始碼值 | ❌ DR-21 |
| `[Ign. off & acc. … / IGN_OFF_ACC]` | 4 | 無對應 | ❌ DR-21 |

> **`IGN_RUN` 之可用不靠推理** —— 靠 CFTS044 自己在 5 處寫了 `4h`。
> 若無該原始碼值，`IGN_RUN` 與 `IGN_START` 之處境完全相同。

### 1.4 D-8／D-10 —— DR 送出項次（**依 Pei 回報，未推定**）

| 送件文項次 | DR | 狀態 |
|---:|---|---|
| 1 | DR-15 | **已送出 2026-08-22 —— 待覆** |
| 2 | DR-17 | **已送出 —— 待覆** |
| 3 | DR-14′ | **已送出 —— 待覆** |
| 4 | DR-19 | **已送出 —— 待覆** |
| 5 | DR-20 | **已送出 —— 待覆** |
| 6 | DR-18 | **未送出 —— 待送** |
| 7 | （`$VC_VEH_LINE$` 車型碼） | **未送，且無 DR 編號** |
| 8 | （`$PowerMode$` 之 `IGN_OFF_ACC`） | **未送，且無 DR 編號** |

**送出 5 項，與 Pei 回報之「1–5」相符。** 未送者一律維持待送。

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **第二批 10 條中有 4 條無法撰寫 —— 缺件是系統性的，不是個案**

17 輪之 A-VS58／A-VS59 曾看似個案（3 leaf ＋ 1 leaf）。本批 **10 選 4 中**：

| leaf | 缺何物 | DR |
|---|---|---|
| `-028` | `VC_HdRstPrsnt` 於 LID（2,710 列）／兩份 DBC／`spec_variables.tsv`（30 token）**三處皆 0 命中** | **DR-22** |
| `-029` | `$PowerMode$ = [Ignition start / IGN_START]` 於 DBC 無對應且無原始碼值 | **DR-21** |
| `-031` | `$PowerMode$ = [… / IGN_OFF_ACC]` 於 DBC 無對應 | **DR-21** |
| `-039` | `follow the HMI Logic & Flow` —— **未具名任何文件或章節** | **DR-23** |

**四條皆未撰寫 TC** —— 撰寫即為 §8.4.1 之造值。記於 `generated/blocked_pending_dr.json`
之 `batch02_not_written`，**與 batch01 之「已寫後移出」分開記載**（兩者狀態不同）。

**累計阻塞**：batch01 移出 2 ＋ batch02 未撰寫 4 = **6 條**，
分屬 **5 個 DR**（DR-19／20／21／22／23）。

### 2.2 `A-VS59` 之形態在同一 feature 內第二次

`4858560`：`the HMI shall be modified as defined by **HMI requirements**`（DR-20）
`4859032`：`the HU shall follow the **HMI Logic & Flow** to update the state`（DR-23）

**兩條所指之文件名不同**，故不併為同一 DR。
但**同型缺陷兩次出現**，其意義超出個案：
CFTS044 對外部 HMI 文件之引用**慣於不具名**，
後續批次遇此者**很可能還有**。本層未全掃其數量（屬 backlog）。

### 2.3 `IGN_OFF_ACC` —— 送件文第 8 項已提出同一問題，但未送且無 DR 編號

37 包送件文第 8 項就 `4858978`（**Second Row** Headrest Dump）之 `IGN_OFF_ACC`
提出同一問題。Pei 本次僅送 1–5，**該項未送**。

本輪之 `-031` 為 **Third Row**，同一值、同一缺件、不同條文。
本層開 **DR-21** 併同 `IGN_START` 一併提出，**未將其併入未編號之第 8 項**
—— 未編號者無法在 `DATA_REQUESTS.md` 中被追蹤，亦無法標狀態。

### 2.4 `VC_HdRstPrsnt` 之發現路徑 —— R-VS36 之第二次奏效

該 token 於 CFTS044 中寫作**裸名 `VC_HdRstPrsnt`，無 `$...$` 包夾**。
早輪建 `spec_variables.tsv` 時以 `$var$` 形態掃描，**故未收入該 token**。

**R-VS36（token 比對之最小三形態試法）自 16 輪立條後第二次奏效**
（首次為 `$ESS_ENG_ST$` 之裸名多得 2 個 leaf）。
若本輪仍只試 `$X$`，`-028` 會被當成「可寫」而寫出一個**觸發訊號不存在**的 TC。

### 2.5 兩份 DBC 之 `CmdIgnSts` 值表相同 —— 與 `EngineSts` 之情形不同

`STATUS_BH_BCM2.CmdIgnSts`（BHCAN, id 1132）與 `BCM_FD_10.CmdIgnSts`（FDCAN8, id 1153）
之 `VAL_` **完全相同**，故本批取 `STATUS_BH_BCM2`／CAN-B 不生 17 輪 §2.6 之歧義
（該處 `EngineSts` 與 `EngineSts_W` 位於不同 message 且需與 `ESS_ENG_ST` 同段觀察）。
**此處之選擇無實質後果**，仍記明。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `framework.md` 鎖定（P19 簽核區塊 ＋ 重開條件逐字 ＋ 原草案標題加註保留）、Layer 3 增正規化名欄、阻塞項 8／10／底部第 5 標已解；`PLAYBOOK.md` §6 P0–P5 結案並增 DR 待送／待覆表；`DATA_REQUESTS.md` 五項標送出待覆、DR-21／22／23 開立；37 包記明送出項次；A-VS62 登記、profile 增列 D-3 裁定；`batch01_v3.json` 8 條 0 違規；`batch02.json` 6 條 0 違規、sibling 全數比對 |
| **核實無誤** | v3 之 8 條與 38 包 §4 之預期相符；DBC `VAL_` 逐字核對 0 不符；可選 32 ≥ 10；11 列 sibling 比對無 `duplicate_of`、與已放行之 `-025` 無重複；送出 5 項與 Pei 回報相符 |
| **正確地不動** | **未把 `IGN_START` 讀為 `START`**（R-VS9(2)）；**未為 `-039` 編造更新後之狀態**；**未撰寫 4 條缺件 TC**；**未將 DR-21 併入未編號之送件文第 8 項**；**v1／v2 保留不刪**；**未寫回工作簿**；**未執行任何 backlog 項**；DR-18／21／22／23 **皆未送出** |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| batch02 leaf 選取 | Layer 2 = `Common Features`（037 檔界，`data/_leaf_origin.json`）∧ Functional ∧ 不引用 `HdRstRelRq`（**裸名**，R-VS36(2)）∧ `reqid_list` 非空 ∧ 不在 batch01 之 10 條內；以最小 reqid 升冪取 10 |
| `$PowerMode$` 值域 | DBC `^VAL_\s+\d+\s+CmdIgnSts\s+(.*?);`（latin-1）；CFTS044 側以 `\$PowerMode\$\s*(?:=\|&lt;&gt;\|<>)\s*(\[[^\]]{0,70}\])` 取值並計次 |
| **原始碼值標記** | `\[([0-9A-Fa-f]h\s*:[^\]]{0,60})\]` 於含 `$PowerMode$` 之區塊內 —— **此式找出 `[4h:Ignition run]`，是 `IGN_RUN` 可解之唯一依據** |
| `VC_HdRstPrsnt` 之三處查詢 | `lid_pairs.tsv` 全列字串比對（2,710 列）／兩份 DBC 全文／`spec_variables.tsv` 之 30 個 token —— **皆 0**。查詢採**裸名**（R-VS36(2)），非 `$X$` |
| sibling 母體 | Layer 3 `ThirdRowHeadrestDump` 之全部已生成 TC（batch01_v3 之 `-025` ＋ 本批 10 選）＝ **11 列** |
| §9 自檢 | `scripts/selfcheck_w53.py <path>`，含 DBC `VAL_` 逐字核對、三件組殘留偵測、規格 token 殘留偵測 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS62** | —（style，不阻放行） | ER 之 `is registered without a bus error`（8 處）未能自交付本枚舉（38 包 §2 指定登記）。**pilot 已通過，依 (b) 暫為既定寫法** |
| **A-VS63** | **DR-21** | `$PowerMode$` 之 `IGN_START`／`IGN_OFF_ACC` 於 DBC 無對應；`IGN_RUN` 因 CFTS044 自載 `4h` 而可解。⚠ 阻塞 2 leaf |
| **A-VS64** | **DR-22** | `VC_HdRstPrsnt` 於 LID／DBC／值域資料三處 0 命中；R-VS36 第二次奏效。⚠ 阻塞 1 leaf |
| **A-VS65** | **DR-23** | `4859032` 交叉參照未具名之 HMI Logic and Flow；與 A-VS59 同型、同 feature 第二次。⚠ 阻塞 1 leaf |

**新開 DR：DR-21／DR-22／DR-23**，**提問文待分析層擬**（本層不代擬），**皆未送出**。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **4**（A-VS62／63／64／65） | **64**（相異編號；最大號 A-VS65，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **3**（DR-21／22／23） | 未結 **12** |

§5 表列 4 筆，登記簿逐筆核對皆在，**差額 0**。

### 5.2 未結 DR（12 條）—— 待送／待覆兩態

| 態 | DR | 數 |
|---|---|---:|
| **待覆** | DR-14′／DR-15／DR-17／DR-19／DR-20 | **5** |
| **待送** | DR-8／DR-11／DR-12／DR-18／**DR-21**／**DR-22**／**DR-23** | **7** |

**阻塞中之 TC：6 條**（batch01 移出 2 ＋ batch02 未撰寫 4），分屬 5 個 DR。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **「CFTS044 對外部 HMI 文件之引用慣於不具名」之數量未掃。**
   已知兩例（`4858560` 之 `HMI requirements`、`4859032` 之 `HMI Logic & Flow`）。
   **全文尚有幾條同型，本輪未數** —— 其直接決定後續批次還會卡住幾條。
   依 **R-VS40** 屬 backlog，**惟其滿足 (b)「阻塞具體 leaf」之解凍條件**，
   建議下輪解凍一掃。

2. **`spec_variables.tsv` 之 30 個 token 係以 `$var$` 形態建立。**
   A-VS64 證明**裸名 token 會被漏掉**。
   **全文尚有幾個裸名 token 未收入，本輪未掃** —— 同樣影響後續批次。

3. **batch02 之六條 `design_method` 中 3 條為 State Transition。**
   其判準為「State A → State B transition」。惟 `-030`／`-032` 之步驟 1
   （送 `Initialization`）僅為建立起始狀態，**其是否構成 §12 所指之
   「狀態轉移焦點」而非單純 setup，本層未經 review 確認**。
   若判為 Functional Based，三條之 `design_method` 須改。

4. **`$PowerMode$` 之 `[Ignition off (5 position switch) / IGN_OFF]`／`[IGN_OFF]`
   本批未涉，其於 DBC 亦無對應**（DBC 無 `IGN_OFF`）。
   **後續批次若有 leaf 引用該值，將與 A-VS63 同型受阻** —— 本輪未預先納入 DR-21。
