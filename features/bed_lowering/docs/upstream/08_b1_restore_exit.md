# 上繳包 08 — Bed Lowering Mode：B1 批（Restore And Exit）+ R-BLM15 落地

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/08_b1_restore_exit.md`
（sha256 `68a1e10910d6b6a227e2ab43c74a3299b6a700e53d72e408ed765d3d3ddf6c94`）
執行層：Tier 1

**結論：B1 九條生成完成，六條寫回（列 23–28），三條依 IN §8.4.3 保留不寫回。
交付 lint 全簿 19 列 clean。但 R-BLM15(1) 之目標「recon 全綠 + DECISIONS.md 產出」
**未達成**，且其不可由本包達成 —— 見 §一-1。**

---

## 〇、三件要先講的

1. **R-BLM15(1) 選項 1 不足以讓 recon 全綠。** 兩條宣告已改，兩條 FAIL 清掉，
   但**第四條 assertion 是寫死的、不讀 feature.yaml**，仍 FAIL，
   DECISIONS.md 仍未產出。選項 1 在設計上到不了目標。（§一-1）
2. **`test_version = "1.0"` 我填錯了。** 四本可查之交付本共 775 列，
   AB 欄非空者 **0**。這欄全案沒人填，是我在上繳 07 自己造的。（§一-2）
3. **R-G19 指紋有一個「永遠相符」的缺陷，本包發現並修掉。** B1 之指紋
   原本蓋的是 **pilot** 的語料，而比對照樣回報「相符」。（§四-2）

---

## 一、R-BLM15 落地

### 1.1 recon_assertions 重宣 —— **改到一半，剩一條不可由宣告解**

已依 R-BLM15(1) 作廢 `spec_reference_stem`（註解留痕，標
`superseded by R-BLM15(1)`），並宣告 `distinct_spec_sections: 0`。

重跑 recon：

```
PASS — leaf count == Functional Requirement rows: expected 176, measured 176
PASS — distinct spec sections after citation parse: expected 0, measured 0
PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
FAIL — every leaf's citation parses to a section: expected 0, measured 176
FAILED: 1 ruled-constant assertion(s) do not hold. DECISIONS.md was NOT written.
```

**由 2 FAIL 降為 1 FAIL，但目標未達成。**

剩下這條清不掉，原因是結構性的：

```python
# scripts/recon.py:401 —— 注意它不在 `if ... in want:` 之內
if a03res["unparsed_citations"]:
    a.check("every leaf's citation parses to a section", 0, len(...))
```

**它是無條件觸發的，不讀 `feature.yaml` 的任何宣告。** 本 feature 之
037 `HMI Source ID` 無章節號，176 條全數「無法解析為 section」，
所以無論宣告怎麼改，這條都會 FAIL，DECISIONS.md 都不會被寫出。

R-BLM15(1) 明文不採選項 2（改全域腳本）與選項 3（留恆 FAIL），
但**選項 1 之射程不及於此條**。三個可能（**本包不自擇**）：

1. 接受 recon 對本 feature 恆 1 FAIL，DECISIONS.md 由他法產出
   —— 實質即選項 3，而 R-BLM15 已否決
2. `recon.py` 之該條加一個「無章節錨」分支 —— 選項 2，屬全域線
3. `recon.py` 把該條也納入 `want` 閘控（使其可宣告為 0 或關閉）
   —— 亦屬全域線，但改動面比 2 小

**現況影響**：DECISIONS.md 仍未產出。本 feature 之裁決權威為
`RULINGS.md`，實務不阻斷，但 R-BLM15(1) 所期待之「DECISIONS.md 回復產出、
定位為機器摘要」未實現。

### 1.2 兩常數查錨 —— **`test_version` 查無先例，且與我填的值相反**

R-BLM15(2) 指定之兩本**皆不可得**：

- **AMFM 已交付本**：`features/amfm/inputs/` 於本機為空目錄
  （`inputs/` 全案 gitignore，檔案不在此工作副本）。tag `fw036-amfm-regen-v1`
  存在，但 tag 只帶交付摘要，xlsx 本身不入 git。
- **SWC 0708**：全 repo 檔名搜尋 `*0708*` **零命中**。

依 R-BLM15(2)「查無 → 停下回報值域，待 Pei 點名」。為使點名有依據，
本包改測**磁碟上實有之四本交付／寫回本**，母體為各本「有 req_id 之列」：

| 本 | 列數 | S 欄 `functional_safety` | AB 欄 `test_version` |
|---|---|---|---|
| privacy 交付本 regen-v1 | 11 | **`NA` × 11**（全填）| 非空 **0** |
| vehicle_setting CFTS044 | 237 | 非空 **0** | 非空 **0** |
| vehicle_setting VF230 | 457 | 非空 **0** | 非空 **0** |
| audio_mgmt B1 generated | 70 | 非空 **0** | 非空 **0** |
| **合計** | **775** | 僅 privacy 填，值恆 `NA` | **全案 0 列填過** |

**結論分兩半：**

- `functional_safety = "NA"`：唯一有填的先例（privacy）填的就是 `NA`，
  我填的值與之一致。**但 775 列中有 764 列是空的** ——
  「填 NA」與「留空」兩派並存，我選了少數派。
- `test_version = "1.0"`：**775 列無一列填過**。
  這個值是我在上繳 07 §二-5 自己造的，**沒有任何先例**。
  上繳 07 我已標明「兩常數是我定的，請確認」，現在有了數據：**它應該是空的。**

**本包未自行改回**（R-BLM15(2) 令停下待點名）。
現行 19 列之 AB 欄皆為 `1.0`，若 Pei 裁定留空，需 patch 19 列。

### 1.3 DR-1

已裁定送出（Pei 執行）。B1 未等回覆，依 IN §8.4.3 落 PENDING（§二-3）。

---

## 二、B1 批：Restore And Exit，9 leaf

### 2.1 生成路徑

context 由 `make_batch_context.py --test-set "Restore And Exit"` 產出
（sha256 `aa0c3a2a4930d2c815222de679928f7fbf61d51c779feb94ab415ea354d03105`），
prompt 由 `backend/prompt_builder.build_batch_prompt` 組出（工程債已收，dry-run 通過）。

**須據實說明一件事**：prompt 是由 `prompt_builder` 真路徑組的，
但**完成（completion）仍由本 session 產出，未經 `backend/generator.py` 呼叫模型**。
故下放包 §二-1 所要之「模型輸出品質 vs pilot session 直寫品質之差異回報」
**本包給不出來** —— 沒有兩個樣本可比。要比得實際走一次 API 生成。

### 2.2 訊號預查 —— 車速訊號查有，但**單位與規格不符**

沿上繳 04 之教訓，先自 LID 英文描述查，再回 DBC 定位實名：

| 訊號 | 訊息 | tx | 編碼 | 用於 |
|---|---|---|---|---|
| `$BRAKE_FD_2.VehicleSpeedVSOSig$` | 0x102 | SGW | `4\|13@0+` factor 0.0625，範圍 0–511.875，**單位 `Km/h`** | 車速 |
| `$ASCM_FD_1.RL_Lvl$`／`$RR_Lvl$` | 0x52F | SGW | VAL_ 僅 `254 NOT_INIT`／`255 SNA` | ride height baseline |
| `$ASCM_FD_2.BDL_Enbl$` | 0x5A5 | SGW | `0 FALSE`／`1 TRUE` | 降床模式狀態 |
| `$ASCM_FD_2.ASCM_Stat$` | 0x5A5 | SGW | `9 LOWER`／`10 SYSFAIL`／`11 SRVS` | 降床狀態 |
| `$IPC_VEHICLE_SETUP2.Default_Ride_Height$` | — | — | `0 Normal`／`1 Aerodynamic` | 027-03 之非預設值設定 |

**單位不符要留意**：037 之門檻寫作 `*XX MPH`，而 DBC 訊號單位是 **Km/h**。
本包**不作換算** —— 沒有來源值可換（門檻本身就是 PENDING），
且擅自換算等於替上游決定單位。已記入 manifest。

`GW_C_I7`（LID 對 `VehSpd_MPH`／`VehSpdDisp` 所記之訊息）在兩個綁定 DBC 中
**皆查無**，屬上繳 04 已記之 LID 與 FD DBC 命名世代差異，非新問題。

### 2.3 DR-1 落法（首驗）—— 三條保留不寫回

| leaf | PENDING 落點 |
|---|---|
| 022-02 | Pre-Condition 4 + Procedure 2 |
| 022-03 | Pre-Condition 4 + Procedure 2 |
| 022-04 | Pre-Condition 4 + Procedure 4 |

句式依 IN §8.7.1 之 `<condition> >= <trigger value>`，value 位置置佔位：

```
4. Vehicle speed >= PENDING: DR-1 BLM operating speed threshold value is reachable on the bench
2. Send the signal $BRAKE_FD_2.VehicleSpeedVSOSig$ = PENDING: DR-1 BLM operating speed threshold value
```

**三條不入寫回**（IN §8.4.3：含 PENDING 之工作簿不得出貨）。
`write_back.py` 新增 `--skip-pending` 旗標使該過濾**顯式且會回報**，
而非靠寫回時記得處理：

```
IN §8.4.3 保留不寫回 3 條: ['SWE1-HMI-BLM-022-02', 'SWE1-HMI-BLM-022-03', 'SWE1-HMI-BLM-022-04']
```

其餘六條無一含 PENDING（已機檢）。

### 2.4 `022-02` 之 Title = `Detect` 單字

037 之 `Requirement Title` 欄逐字就是 `Detect`。依下放包 §二-4，
test_item 上半改取 `Requirement Description` 全句
（`The system shall detect when the vehicle speed threshold is exceeded during
Bed Lowering Mode.`，21 token，未逾 R-3 之 50 上限）。

manifest 已具名記載此一切換與理由。**要點：這是取材來源之切換，
不是改寫上游文字** —— Title 與 Description 皆為 037 正式欄之逐字值，
換的是取哪一欄，沒有一個字是我寫的。

### 2.5 「偵測／接收」類再現 —— 兩條用 (a)，一條用 (c)

依下放包 §二-5，先試 R-BLM13(c)：

| leaf | 分支 | 依據 |
|---|---|---|
| 022-02 | **(a)** | 與 022-03 同 trigger（速度越過門檻），無 trigger 可分。斷言 `BDL_Enbl` 之值「有變化」，不斷言終態 |
| 027-01 | **(a)** | 與 027-02 同 trigger（二次按壓）。斷言值有變化，不斷言「被解讀為取消」 |
| 027-04 | **(a)** | 與 027-03 同 trigger。斷言角落高度「有變化」（回復指令存在），不斷言回到哪個值 |
| 027-05 | **(c)** | **trigger 可分**：車輛移動中 vs 027-01 之靜止。故不動用 (a)，得逕行斷言「不執行回復」 |

per-TC reasoning 僅上列 (a) 三條有（profile §4：其存在本身即委派訊號）。

### 2.6 機檢

```
TC 數 9
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 9}
design_method 分布 {'Functional Based': 4, 'Negative / Invalid': 1, 'State Transition': 4}
Input Test Data == NA 之比例 9/9
機檢項全數 PASS
```

§5.2 長度分級與禁用主動詞（全行式）另跑，皆 PASS。

---

## 三、寫回

輸出 `features/bed_lowering/workbook/bed_lowering_02.xlsx`
sha256 `7e31199ebbc0f02b238d3931b1973bb6fd280c5607764dcb37d9419516514ce3`
來源 `bed_lowering_01.xlsx`（`aa1015f2…`）

| 項 | 值 |
|---|---|
| 寫入列 | 23–28（六條）|
| TC ID | `newR1L-BLM-014` … `newR1L-BLM-019` |
| patched 儲存格 | 96（6 列 × 16 欄）|
| round-trip | 6 列 × 16 欄，**差異 0** |
| 保全計數 | zip 48、sheet 9、legacy DV 4、**x14 DV 1**、extLst 3 —— 全等，差異僅 size/sha256 |
| 交付 lint（全簿 19 列）| **clean — 0 findings** |

pilot 本（13 列）回歸重跑亦 clean。

---

## 四、manifest 與指紋

### 4.1 B1 manifest

`batches/B1/manifest.json` sha256 `db4cec3bce0e19266083b9bfae608cf459206a6ed02c8b2d8436c87d9be50bca`
（含 `signals_verified` 六項、`pending_held_back` 三條、`title_source_switch`、
`written_back` 六條之列號與 TC ID）

### 4.2 **一個「永遠相符」的指紋缺陷，本包發現並修掉**

B1 首次蓋指紋後比對回報「相符」。但逐源展開一看：

```
features/bed_lowering/batches/pilot/context.json 88c1959e   ← B1 的指紋裡放著 pilot 的語料
```

成因：`fingerprint.prompt_sources` 是**per-feature** 宣告（我在下放包 04 寫的），
而 context 是 **per-batch** 工件。於是每一批之指紋都會蓋到 pilot 的 context，
**且因為它每批都一樣，比對永遠回報「相符」** ——
一個永遠相符的指紋不是保護，是裝飾。

已修：自 `prompt_sources` 移除 batch-specific 之 context，
只留跨批不變之四源（IN／profile／framework／RULINGS）；
每批之語料改由該批 manifest 自身之 `context_sha256` 承載。修後：

```
pilot  prompt_template 0ace0768…  context_sha256 88c1959e…
B1     prompt_template 0ace0768…  context_sha256 aa0c3a2a…
```

prompt_template 兩批相同是**正確的**（canon 確實沒變），
批間差異由 context_sha256 表示。

### 4.3 順帶查出 pilot manifest 之 context 雜湊已失效

比對時發現 pilot manifest 記的 `context_sha256` 與磁碟檔不符。
原因：pilot 之 context.json 於下放包 07／08 期間被 adapter 之改動重新產生
（新增 `test_item`／`project`／`matched_spec_context`，並改由 037 原欄讀常數），
而 **pilot 之 13 條 TC 產生於這些改動之前**。

處置：**不以現行值覆蓋歷史**。manifest 併記兩值 ——
`context_sha256_at_generation`（當初）與 `context_sha256`（現行），
並附註說明。覆蓋會讓稽核以為 TC 是照現行語料寫的。

---

## 五、連帶修改（本包因 R-BLM15(1) 而必須動的兩處）

`spec_reference_stem` 作廢後，兩支腳本讀該鍵而當場 KeyError：

- `make_batch_context.py`
- `lint_tcs.py`

**未改讀另一個宣告** —— 那只是把同一個錯誤搬家。
兩者改為共用一支 `_spec_reference_constant()`：直接讀 037 之
`HMI Source ID` 欄，並就地斷言「相異值恰為 1」（即 R-BLM5 之前提），
不成立即 `sys.exit`。**宣告會與檔案漂移，檔案不會與自己漂移。**

---

## 六、執行層自陳

1. **B1 之 completion 非模型產出**（§二-1）。下放包所要之品質對比給不出來。
2. **`022-01` 之 5 Km/h 與 `027-05` 之 5 Km/h 是我選的具體值**，
   037 未載。選擇理由：需要一個「非零但確定低於任何合理門檻」之值以驗
   「監看但不退出」。**若門檻回覆後低於 5 Km/h，這兩條要改。** 具名於此。
3. **台架可執行性仍未驗**（第五次記載）。本批新增之「注入車速」
   對台架之要求高於 pilot 之靜態注入。
4. **R-G14 綠色通道自 B1 起算**（下放包 §三）。本包為第 1 批，
   **但本包有 A 類項**（§一-2 之 `test_version`），故**不計入連續乾淨批數**
   —— 由分析層審定，執行層不自評。
5. **`022-01` 與 `022-02` 之區分**（監看 vs 偵測越限）依 trigger 分（低於／達到門檻），
   屬 R-BLM13(c)。惟 022-02 之 trigger 值為 PENDING，
   **該區分在門檻回覆前無法實際執行**，只在紙上成立。

---

## 七、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`；DBC 訊號單位為 Km/h，見 §二-2）| **已裁定送出**，Pei 執行；三條 TC 以 PENDING 承接，未寫回 |

---

## 八、停點與待裁

**已停。** B1 九條在 `batches/B1/`，六條已寫回 `bed_lowering_02.xlsx`。

| # | 項 | 阻斷 |
|---|---|---|
| 1 | §一-1 recon 剩餘 1 FAIL 之處置（三選一，兩項屬全域線）| DECISIONS.md 產出 |
| 2 | §一-2 `test_version` —— 資料指向「應留空」，現行 19 列填 `1.0` | 交付本正確性 |
| 3 | §一-2 `functional_safety` —— `NA` 與留空兩派並存，我選了少數派 | 同上 |
| 4 | §六-2 兩條 5 Km/h 具體值之追認 | 門檻回覆後可能需改 |
