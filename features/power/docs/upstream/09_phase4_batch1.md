# 09 — 補閘與 Phase 4 首批（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 09
結果：**九步全部完成。首批 9 條 TC 已產出，真實檔案 lint 全閘 PASS。**
**R-P71 於首次執行即抓到一個會使 G45 全面誤殺之 bug。**

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| 覆寫 `handoff/09_phase4_batch1.md`（完整版） | DONE（§A 7 區塊 / §J 7 列 / §H 9 步，自檢一致） |
| 1 G0 前置閘 | **PASS 7 / 7** |
| 2 補 G45 / 改 G40 / 補 G46，fixture 驗證 | DONE —— **23 個 TC fixture ＋ G46 三案全數如期** |
| 3 `feature.yaml` 更新與盤點 | DONE —— **盤點查出 `workbook.columns` 全面錯位** |
| 4 R-P62 加註 | DONE —— 原文雜湊未變 |
| 5 首批 TC（R-P72） | DONE —— **9 條，涵蓋 3 個 leaf** |
| 6 真實檔案 lint（R-P71） | DONE —— **首次全滅、修正後全 PASS**（見 §五） |
| 7 §D 全表自驗 | DONE |
| 8 §A 七條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE（RULINGS R-P1–R-P72；ANOMALIES A-PW01–A-PW42） |
| 9 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

### 三項最重要之結果

1. **R-P71 在第一次執行就兌現。** 23 個合成 fixture 全數通過的 G45，
   碰到真實檔名時**把 9 條 TC 全部判 FAIL** —— 因為初版正則要求檔名不含空白，
   而真實規格檔名含空格（§10.7 自身的範例也含空格）。
2. **首批 9 條 TC 全閘 PASS**，0.22 秒，無任何 `load_tcs()` 解析問題。
   R-P42(b) 未觸發任何一次，故本包無 R-P67 之人工裁決可登記。
3. **`feature.yaml` 之 `workbook.columns` 自 `priority` 起全部錯位**，
   靠 R-P69(d) 之盤點查出，非靠閘門（A-PW40）。

---

## 一、B1 —— 三閘（R-P66 / R-P68 / R-P69(c)，**上繳項三**）

`--self-test`：**23 個 TC fixture ＋ G46 三案全數如期**（全為合成）。

### 1.1 G45 —— §10.7（R-P66）

| fixture | 期望 | 實際 |
|---|---|---|
| 非空且形態正確（`CFTS010_1.7.1.1.1; CFTS010_1.7.2`） | （無） | （無） |
| 為空 | `§10.7` | **`§10.7`** |
| **檔名含空格與括號**（§10.7 範例形態） | （無） | （無） |
| 形態不符（`see the power down chapter`） | `§10.7` | **`§10.7`** |

第三個 fixture 為 §五之 bug 修正後**補上以鎖住回歸**者。

> 附帶效果：G37 之第二個 fixture（spec_reference 引用 `SWE-PM-089`）
> 在 G45 上線後同時觸發 §10.7，二閘皆觸發為正確行為，
> 期望值已改為 `["R-P1", "§10.7"]` 並於程式碼註明。

### 1.2 G40 改為子集檢查（R-P68）

| 項 | 有效範圍 | 首批實測 |
|---|---|---|
| (a) 各 Test Set 已產出 leaf 數 ≤ 定版 | **每批皆驗** | `Power Down` 3 ≤ 3 **PASS** |
| (b) 逐 leaf 歸屬符 `leaf_testset.tsv` | 每批皆驗 | 3 / 3 PASS |
| (c) 114 齊備時驗相等 | 齊備時 | 未達，跳過 |

**首批正是原讀法完全不判定的情形**（3 ≠ 114）。
fixture 另證「4 個 leaf 全記 `Power Down`」實際觸發 `R-P35`。

### 1.3 G46 —— `feature.yaml` 一致性（R-P69(c)）

三案，違規以**合成 yaml 注入**（不以 repo 現況為對照，09 §I）：

| 案例 | 期望 | 實際 |
|---|---|---|
| 合成之一致 yaml | （無） | （無） |
| **合成之漂移 yaml**（`test_group` / `spec_mode` / 殘留 placeholder） | FAIL | **3 項 FAIL** |
| repo 現況之 `feature.yaml` | （無） | （無） |

---

## 二、B2 —— `feature.yaml` 更新與盤點（R-P69(a)(d)）

### 2.1 已更新

| 欄位 | 原 | 現 | 依據 |
|---|---|---|---|
| `spec_mode` | `"A"` | **`"D"`** | R-P9 / R-P3′ |
| `test_group` | `"Power"` | **`"Power Management"`** | R-P2 |
| `paths.*` | 全為 `<placeholder>` | **七份素材實際檔名** | 02 包 §二台帳 |
| `tc_id_format` | 無此欄 | **`"NR1L-PowerManagement-{NNN}"`** | R-P2 |
| `spec_reference_template` | `"<Spec Filename>_{outline}"` | `"{spec_filename}_{section_id}"` | §10.7 / G45 |

### 2.2 盤點 —— `workbook.columns` 自 `priority` 起全部錯位（A-PW40）

| 欄位 | scaffold | **實測應為** | 該 scaffold 欄實際是什麼 |
|---|---|---|---|
| `req_id` | D | D | ✓ |
| **`tc_id`** | **無此欄** | **F** | scaffold 完全沒有 |
| `test_group` … `tc_ref_id` | G–O | G–O | ✓（九欄） |
| **`priority`** | **P** | **Q** | P 是 `Estimated Test Time` |
| **`design_method`** | **Q** | **S** | Q 是 `Test Case Priority` |
| **`functional_safety`** | **R** | **T** | R 是第二個 `Estimated Test Time` |
| **`author`** | **Z** | **AB** | Z 是車型欄 `Toro(2261) Atl-Mi` |
| **`remarks`** | **AH** | **AI** | AH 是 `Defect ID` |

成因：本 workbook 之 r9 有**兩個標頭逐字相同**的 `Estimated Test Time` 欄（P 與 R）。
Privacy 之 A-PV13 / R39-2 曾訂正 Revision C 於 Q 插一欄並右移三格；
**本 workbook 較該版又多插一欄**。→ A-PW40、A-PW41。

**若未查出，Phase 4 寫回會把 priority 寫進預估工時欄、author 寫進依 R30-3/R30-4
應留白的車型欄、remarks 寫進 Defect ID 欄。**

### 2.3 其餘欄位

| 欄位 | 現值 | 相符情形 |
|---|---|---|
| `workbook.sheet` / `header_row` | `"Test Case Specification&Result"` / `9` | **相符**（03 包 G12） |
| `done_region.author_value` | `"Arif"` | **可疑** —— scaffold 樣板值。Comfort 於同為 BLANK 之情形刻意留空並註明「填佔位作者值會靜默匹配零列，使空的 invariant 看起來像已滿足」。**未改**（R-P69 未點名），見 §七第 3 項 |
| `write_back.fill_test_group_set` | `false` | 與其自身註解「true only under BLANK」矛盾，而本 workbook 實測即為 BLANK。**未改**，見 §七第 3 項 |
| `lint.design_method_source` | `"dropdown_sheet"` | **相符** —— 02 包實測 `下拉選單!A1:A9` 九詞條 |

---

## 三、B3 —— R-P62 加註（R-P66）

| | SHA256 |
|---|---|
| 加註前 | `ed8fe3a5b6e889a5989f55a4e1001a6303c5fa294c7b9d0509a53882e03b91a1` |
| 加註後 | `ed8fe3a5b6e889a5989f55a4e1001a6303c5fa294c7b9d0509a53882e03b91a1` |

**UNCHANGED PASS。** 註記文字即 §B3 逐字指定者。
加註逐處獨立完成、未共用預先算好之偏移量（06 §六之教訓）。

---

## 四、B4 —— 首批 TC（R-P72，**上繳項一**）

`features/power/generated/batch_001_power_down.json`（17,685 bytes）。
**9 條 TC，涵蓋 3 個 leaf，tc_id `001`–`009` 連號。**

| tc_id | req_id | tc_title | §ref | priority | design_method |
|---|---|---|---|---|---|
| 001 | SWE-PM-071-01 | Splash screen shown after SplashScreen_Time on normal boot | 1.7.1.1.1 | P1 | 狀態轉換 |
| 002 | SWE-PM-071-02 | No splash screen when TLM passes to Standby or Bench | 1.7.1.1.1 | P2 | 狀態轉換 |
| 003 | SWE-PM-071-03 | Standard screen shown after StandardScreen_Time | 1.7.1.1.1 | P1 | 狀態轉換 |
| 004 | SWE-PM-072-01 | Events during boot are buffered without loss | 1.7.1.1.1 | **P0** | 功能測試 |
| 005 | SWE-PM-072-02 | Buffered events processed after boot completes | 1.7.1.1.1 | P1 | 狀態轉換 |
| 006 | SWE-PM-073-01 | Load Shed limits volume and mutes TLM | 1.7.2 | **P0** | 決策表 |
| 007 | SWE-PM-073-02 | Load Shed signals lost: last values retained | 1.7.2 | P1 | 基礎故障注入 |
| 008 | SWE-PM-073-03 | Battery Critical minimizes draw and keeps ACN active | 1.7.2 | **P0** | 決策表 |
| 009 | SWE-PM-073-04 | Normal operation resumes 10 seconds after recovery | 1.7.2 | P1 | 狀態轉換 |

### 4.1 §8.2.2 之拆分判斷（3 leaf → 9 TC）

| leaf | 錨點 | 拆為 | 壓力測試（「若只有部分行為失效，pass/fail 是否明確？」） |
|---|---|---|---|
| `SWE-PM-071` | `4942337` | **3** | splash 顯示、splash 抑制（Standby/Bench）、standard screen —— 三者為互斥分支或獨立時序點；併為一條則任一失效之判讀不明確 |
| `SWE-PM-072` | `4942338` | **2** | 緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）—— 緩衝成功而處理未發生仍屬失敗，反之亦然 |
| `SWE-PM-073` | `4942354` | **4** | Load Shed 與 Battery Critical 為**不同控制實體**（`PN14_LS_*` vs `Batt_ST_Crit`），依 §8.2.2「不同控制實體則拆分」；各自之故障分支與回復分支再各拆一條 |

**未合併任何 RD sub-id**（§8.2.2 之反向禁止）；九條皆追溯其原 leaf。

### 4.2 priority 判定（§10.2，依測項內容非 037 欄）

三個 leaf 之 037 `Priority` 皆為 `High`。判定結果為 **P0 ×3、P1 ×5、P2 ×1** ——
非一對一映射，符 R-P8。依據：

- **P0**：`004`（事件遺失 = data-loss risk）、`006` / `008`
  （涉 Ecall / ACN，屬 vehicle-critical CAN signal 與 safety）
- **P1**：主要使用者可見功能或關鍵邏輯流
- **P2**：`002` 為抑制分支，失效影響有限

### 4.3 R-P42 之遵守（一項明確之範圍排除）

`4942338` 之內文引用「the transitions described in par. "TLM_Status.Info setting"」——
該章節為 **CFTS009 §1.6.2.1.15**，**非本 leaf 所引用之錨點**。
依 **R-P42**，其行為不納入測試範圍；TC `005` 之 ER 僅述「轉換順序與注入事件之紀錄相符」，
不測該章節所定之具體轉換內容。已於 `reasoning` 逐字說明。

### 4.4 §8.4 不造值

`4942337` 未給 `SplashScreen_Time` / `StandardScreen_Time` 之數值，
故 procedure 以「與設定值比對」表述，**未編造秒數**。

### 4.5 canon 自查（全數通過）

四個長欄位無 trailing period；procedure 無 `observe` / `verify` 等禁用主動詞為主要動詞；
每條 ≥ 3 個編號步驟（§10.5 要求 ≥ 2）；`tc_title` 皆 8–11 字、無 modal/hedge、九條互異；
方括號僅用於訊號值 `[1h]` / `[0h]`（逐字引自規格），無 UI 標籤使用方括號；
`design_method` 四值皆取自 `下拉選單!A1:A9`。

---

## 五、B5 —— 真實檔案 lint（R-P71，**上繳項四**）

### 5.1 首次執行 —— **9 條 TC 全部 FAIL**

```
檢查 9 個 TC —— **9 項 FAIL**
  §10.7 NR1L-PowerManagement-001: specification_reference 之項目
    `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
    不符 {spec_filename}_{section_id} 形態
  …（001–009 全部）
real 0.24
```

**成因**：`SPEC_REF_ITEM_RE` 初版為 `^\S+_\d+(?:\.\d+)*$` —— `\S+` 要求檔名不含空白。
而真實規格檔名含空格，**§10.7 自身之範例亦然**：
`Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023)_2.5`。

**23 個合成 fixture 全數通過，卻在第一次碰到真實檔名時全滅。**
這正是 R-P71 條文所述之情形逐字命中：「fixture 驗證了邏輯正確，未驗證能讀真實檔案」。

**修正**：改為 `^.+_\d+(?:\.\d+)*$`，並**補一個含空格與括號之 fixture** 鎖住此回歸。
程式碼就地註明成因與發現來源。→ **A-PW39**

### 5.2 修正後重跑 —— 全閘 PASS

```
R-P42 黑名單 814 個錨點；其中 733 個具獨有特徵字串（共 1398 句，最短 40 字元）
檢查 9 個 TC —— PASS
real 0.22   user 0.17   sys 0.02
exit=0
```

| 項目 | 結果 |
|---|---|
| R-P42(a) spec_reference 命中黑名單 | 0 |
| **R-P42(b) 內容逐字引用特徵字串** | **0 觸發** —— 故本包無 R-P67 之人工裁決可登記 |
| R-P1 / R-P2 / R-P8 / R-P35 / §10.7 / R-P69 | 全 PASS |
| `load_tcs()` 解析問題 | **無** |
| 執行時間 | **0.22 秒**（9 TC；黑名單 814、特徵字串 1398 句） |

---

## 六、§D 全表實測值對照（**上繳項二**）

G0–G16、G13b、G18–G44 沿用，本包 G0 復驗 PASS。

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | 7 / 7 | PASS |
| **G45** | §10.7 閘門 | 正常 PASS、違規實際 FAIL | 4 fixture 全如期（2 PASS + 2 FAIL） | **PASS** |
| **G46** | `feature.yaml` 一致性 | 正常 PASS、違規實際 FAIL | 3 案全如期（含合成漂移 yaml 實際 FAIL） | **PASS** |
| **G47** | 首批 TC 數與 leaf 涵蓋 | 3 leaf；TC 數 ≥ 3 | **3 leaf（071/072/073）、9 TC** | **PASS** |
| **G48** | 首批 lint 全閘 | 全數 PASS | **全 PASS**（修正 A-PW39 後）；R-P42(b) 0 觸發 | **PASS** |
| **G49** | 首批 `specification_reference` | 全指 CFTS010，章節在 §1.7.1 / §1.7.2 內 | **9 / 9 指向 CFTS010**；章節 `1.7.1.1.1`、`1.7.2` | **PASS** |

**無 MISMATCH。**

---

## 七、獨立判斷：本包是否仍有該驗而未驗者（**上繳項五**）

08 上繳包 §七之六項，本包處置：第 1 項→R-P67（改為持續量測；首批 0 觸發）；
第 2 項→R-P68（已改，首批實測生效）；第 3 項→R-P66（**部分**）；
第 4 項→R-P69(d)（盤點查出 A-PW40）；第 5 項→R-P71（已執行，抓到 bug）；
第 6 項→R-P70（追認）。

### 7.1 就第 3 項「僅部分處置」之獨立判斷（下放包指定）

**覆蓋率為 8 / 72 ≈ 11.1%**（G33 之 (a)(b) 計為兩項則 9 項）。
下放包稱「五閘增為八閘，仍僅 8 條有執行期閘門」。

**執行層判斷：分母用「72 條裁決」會低估實際覆蓋，但結論方向不變。**

72 條中有相當比例**本質上不可機械檢查**或**已失效**：
撤回者（R-P3、R-P16）、一次性程序指令（R-P19 訂正條數、R-P29/R-P30 加註）、
量測任務（R-P28、R-P39、R-P40）、方法論宣示（R-P36、R-P50、R-P59、R-P64）。
粗估**可機械檢查者約 15–20 條**，故實際覆蓋率約 **40–55%**，非 11%。

**但仍有明確缺口**，且都在 Phase 4 會用到的路徑上：

- **R-P24（Layer 3 記全集）** —— TC 之 `specification_reference` 是否涵蓋該 leaf 之
  全部 Layer 3 章節，無閘門。首批 9 條各只引一個章節，而三個 leaf 在
  `layer3_full.tsv` 中各只有一列，故本批恰好無違；**多章節 leaf 之批次會暴露此缺口**。
- **R-P42 之 `reasoning` 欄禁令** —— 條文明言「不得於 `reasoning` 欄以『為求完整』為由納入」，
  現行 G33 只檢查 TC 內容欄位，**不檢查 `reasoning`**。
- **§4.4 Pre-Condition 不得含動作** —— 可機械檢查（動詞偵測），無閘門。
- **§11 trailing period / 方括號** —— 完全可機械檢查，本包靠自查通過，**無閘門**。

### 7.2 新增未驗項（五項）

**1.（最重）`workbook.columns` 之一致性閘仍未補設，而寫回不可逆。**
   A-PW40 是靠 R-P69(d) 的盤點偶然查出的。G46 只驗三個值，不驗欄位對應。
   下一包若進入寫回，**這是最後一道可能出錯而無人攔截的環節**。
   本包已於 08 §七第 1 項提過，09 包未納入，此處再提。

**2. §11 / §4.4 等純格式規則靠人工自查通過，未進 lint。**
   §四之 canon 自查（trailing period、禁用動詞、方括號、步驟數、字數）
   是我自己寫腳本查的，**不在 `lint_tcs.py` 內**。
   下一批若由不同流程產生，這些檢查不會自動跑。
   §11 尤其應入閘 —— 它是純字串規則，零判斷成分。

**3. 首批之 R-P42(b) 零觸發，不足以支撐 R-P67 之偽陽性統計。**
   9 條 TC、0 觸發 —— 樣本太小。R-P67 要求「累積至首批完成後統計真實偽陽性率」，
   而首批的統計量是 0/9，**無法據以再議 R-P62 之門檻**。
   需累積至數十條後才有意義。

**4. `design_method` 之指派無任何交叉驗證。**
   §12 是 first-match 表，我逐條套用，但**沒有第二意見也沒有閘門**。
   lint 目前只驗值域（`下拉選單!A1:A9`），不驗「這條 TC 是否真的屬於這個方法」。
   九條中五條判為「狀態轉換」—— 若我的 first-match 順序理解有偏差，會系統性地偏向同一值。

**5. 首批未經任何人工覆核即上繳。**
   §8.2.2 之拆分、priority 判定、§4.3 tc_title 形態選擇，全是我的判斷。
   R-P51 曾裁定「Phase 4 撰寫 TC 時作者必然再次接觸同一批錨點，該接觸即為天然之第二次判讀」——
   但那指的是 B2 判讀 vs TC 撰寫；**TC 本身的判斷沒有第二次接觸**。

---

## 八、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | **未寫回**。僅以 `read_only=True` 讀 r9 表頭與 037 |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補；首批不含該 leaf |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改。A-PW39 所修者為 G45 之 `SPEC_REF_ITEM_RE`，非 §C |
| 不得修改任何已落檔裁決條文之內文（R-P36） | R-P62 加註以雜湊證原文未變 |
| **不得測試未被引用之錨點（R-P42）** | 九條 TC 皆只引 `4942337` / `4942338` / `4942354`。`4942338` 所引之 CFTS009 §1.6.2.1.15 **明確排除**，見 §4.3 |
| 不得解析任何 RTF 或 OLE stream 之內容 | 未讀任何 RTF 或 OLE stream |
| 不得續行章節層反向缺口調查（R-P37） | 未做任何章節層量測 |
| 不得變更 §E 之分布數字（R-P35） | 63/24/16/8/3 未動 |
| 不得以 A-PW29 之存在逕行填寫車型欄（R-P54） | **未填**；`reasoning` 已逐字說明車型欄依 R30-3 / R30-4 留白 |
| 不得調整 `MIN_FINGERPRINT`（R-P62） | 維持 40 |
| **不得擴大首批範圍超出 `Power Down` 3 leaf（R-P72）** | **3 leaf，未擴大**。9 條 TC 係 §8.2.2 之拆分，非範圍擴大 |
| **R-P42(b) 之觸發不得自動判 FAIL（R-P67）** | 首批 **0 觸發**，未發生。實作上仍列入 findings，若日後觸發須人工裁決 —— 此處登記為**尚未實作分流**，見 §九 Q3 |
| **不得以 repo 現況作為任何 fixture 之測試對照** | 23 個 TC fixture 與 G46 之違規 yaml 全為合成 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

---

## 九、待裁

- **Q1（Phase 4 寫回前必須解決）§七第 1 項：補設 `workbook.columns` 與 FW036 r9
  實測標頭之一致性閘。** A-PW40 靠盤點偶然查出，寫回不可逆。
- **Q2 §七第 2 項：§11（trailing period / 方括號 / UI 引號）與 §4.4（Pre-Condition
  不得含動作）是否入 lint。** 純字串規則，零判斷成分，本包靠人工自查通過。
- **Q3 R-P67 之「不得自動判 FAIL」尚未實作分流。** 首批 0 觸發故未暴露，
  但目前 R-P42(b) 之 finding 與其他閘門混在同一份 findings、同樣使 exit=1。
  應否分為「阻斷」與「待人工裁決」兩類輸出？
- **Q4 首批 9 條 TC 之內容覆核** —— §8.2.2 拆分、priority 判定、design_method 指派、
  §4.3 tc_title 形態，全為執行層單方判斷（§七第 4、5 項）。
- **Q5 A-PW40 之欄位更新請覆核**（priority Q / design_method S / functional_safety T /
  author AB / remarks AI ＋ 新增 `tc_id: F`）。
- **Q6 A-PW41：FW036 r9 有兩個標頭逐字相同之 `Estimated Test Time` 欄**（P 與 R）。
  何者為權威、另一者是否留空？
- **Q7 §2.3：`done_region.author_value: "Arif"` 與 `write_back.fill_test_group_set: false`
  二者皆可疑，本包未改**（R-P69 未點名）。是否處置？
- **Q8 anomaly 編號衝突之處置已自行決定，請追認。** 09 §F 指定新增
  A-PW37（R-P62 論證前提）與 A-PW38（G43 分層有效性），
  而執行層於前一輪（下放包中斷版）已用掉 A-PW37/38/39。
  依「撤回列不刪、不重編號」之精神，**將執行層原有三條改編為 A-PW40/41/42**，
  §F 指定之兩條取用 A-PW37/38，本包新登之 G45 bug 取 A-PW39。
  現 A-PW01–A-PW42 連續無缺。
