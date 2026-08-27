# 上繳包 09 — Bed Lowering Mode：R-BLM16 落地 + B1 三項 A 類修正

日期：2026-08-27
對應下放包：`features/bed_lowering/docs/handoff/09_r16_b1_fixes.md`
（sha256 `9b78e93df654eed76232594183612ac61ea05a36bb726e27463882babb4bbb5f`）
執行層：Tier 1

**結論：R-BLM16 四項全數落地，B1 三項 A 類修正完成。
recon 兩跑驗收皆過，DECISIONS.md 首次產出。交付本 19 列 lint clean。
另有一處 assertion 名稱與其數字語意相反，屬全域線，回報不動。**

---

## 一、R-BLM16 落地

### 1.1 `recon.py` want 閘控（全域腳本改動）

改動全文 diff：

```diff
     if a03res["unparsed_citations"]:
-        a.check("every leaf's citation parses to a section", 0,
+        # R-BLM16(1) — this check used to be unconditional, which made it
+        # unreachable for a feature whose citations carry no section at all.
+        # bed_lowering's 037 `HMI Source ID` is a bare filename (R-BLM5), so
+        # all 176 citations are "unparsed" BY RULING, and no declaration could
+        # clear the FAIL: the expected value was hard-coded to 0.
+        #
+        # The default is deliberately unchanged: a feature that does not
+        # declare the key still gets `expected 0`, so every existing baseline
+        # reports exactly what it reported before. Only a feature that states
+        # the number out loud in feature.yaml gets a different expectation —
+        # the same shape as lint's `--profile` opt-in.
+        a.check("every leaf's citation parses to a section",
+                want.get("unparsed_citations", 0),
                 len(a03res["unparsed_citations"]),
-                f"samples: {a03res['unparsed_citations'][:5]}")
+                f"samples: {a03res['unparsed_citations'][:5]}"
+                + ("; expected count is declared in feature.yaml "
+                   "recon_assertions.unparsed_citations"
+                   if "unparsed_citations" in want else ""))
     return a, misses
```

`scripts/recon.py` 新 sha256 `6aa5ed738a0ec49164fa4e03c22bb1ce652159e2e1ef8d483da54b532cc293aa`

**驗收 (a) 回歸跑**（本 feature 未宣告該鍵）：

```
PASS — leaf count == Functional Requirement rows: expected 176, measured 176
PASS — distinct spec sections after citation parse: expected 0, measured 0
PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
FAIL — every leaf's citation parses to a section: expected 0, measured 176
FAILED: 1 ruled-constant assertion(s) do not hold. DECISIONS.md was NOT written.
```

**與改動前之輸出逐字相同**，含 FAIL 那行之 `expected 0` 與 samples 列表。
未宣告時 `want.get(..., 0)` 取預設 0，且註記後綴之條件為
`"unparsed_citations" in want`，故未宣告者連訊息尾巴都不變。

**驗收 (b) 宣告跑**（`unparsed_citations: 176`）：

```
PASS — every leaf's citation parses to a section: expected 176, measured 176
       — samples: [...]; expected count is declared in feature.yaml
         recon_assertions.unparsed_citations
recon complete: state=BLANK, leaves=176, sections=0, targets=176
decisions written to: features/bed_lowering/DECISIONS.md
```

**四條全 PASS，DECISIONS.md 產出（2,009 bytes）** —— 本 feature 自 01 包起
首次有 DECISIONS.md，FO §4 之契約至此落地。

宣告之語意已寫入 `feature.yaml` 註解：**176 不是「容許 176 個錯」，
是「依裁定就該有 176 個」**。若日後 037 改版帶了章節號，此數會下降並使本條 FAIL
—— 那正是應該被叫住的事件。

**未跑其他 feature 之回歸。** 理由：`recon.py` 會寫該 feature 之
`RECON.md`／`DECISIONS.md`／`data/`，在別人的工作區產生副作用。
預設不變由兩件事保證：程式上 `want.get(key, 0)` 在鍵不存在時恆等於原本寫死的 `0`；
實測上 (a) 跑已在本 feature 證實逐字重現。**這是推論加單點實測，不是全案回歸。**

### 1.2 S／AB 兩欄清空

`scripts/patch_cells.py`（新建）以 XML 外科式僅改指名儲存格 ——
不重跑 write_back，因為那會由 batch json 重建每一格，
使 batch 內任何他處錯誤搭順風車混進修訂。

```
列範圍 10-28（19 列）
  清空 functional_safety（欄 S） 原值 ['NA']
  清空 test_version（欄 AB） 原值 ['1.0']
  sheets_patched 38    zip members 48    differing ['xl/worksheets/sheet6.xml']
  dv_counts {'sheet5': (1, 0), 'sheet6': (3, 1)}
  round-trip 讀回：38 格，未清空 0
```

同時 `write_back.py` 之 `CONST` 已清為空字典（保留該常數名而非刪除，
使「兩欄刻意不寫」在程式裡看得見），故**日後各批不會再填回**。

**lint gate 範圍之證據**（下放包 §1.2 所要）：

```
A-empty 檢查之欄位: ['req_id','tc_id','test_group','test_set','test_item',
                    'pre_conditions','test_procedure','expected_result',
                    'spec_reference','priority','design_method','author']
  functional_safety 在範圍內? False   <- 應為 False（裁定留空）
  test_version      在範圍內? False   <- 應為 False（裁定留空）
  test_set          在範圍內? True    <- 應為 True（空即錯）
```

兩欄自始未在 A-empty 清單內，故清空不觸發誤報；已於程式加註說明何以如此，
使其成為明示而非巧合。註解重點：**三個欄位都可能為空，
`test_set` 空是缺陷、另兩欄空是裁定，差別只在有沒有裁定。**

工作簿實測：S 欄與 AB 欄 19 列**全空**；`test_set`／`test_group`／`author`／
`tc_ref_id` 仍為 19/19 非空。

### 1.3 暫定值登記

`batches/B1/manifest.json` 新增 `provisional_inputs`，記 022-01／027-05 之
5 Km/h、其存在理由、單位註記，及**複驗義務指向 DR-1 結案動作清單**。

---

## 二、B1 三項 A 類修正

### 2.1 022 群入口改 HU 按鍵（四條）

四條之入口統一為：

```
1. Send the signal $BRAKE_FD_2.VehicleSpeedVSOSig$ = 0 (0 Km/h)
2. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode
3. Read the signal $ASCM_FD_2.BDL_Enbl$ and check that it is 1 (TRUE)
```

理由已入 manifest：`$ASCM_FD_2.BDL_Enbl$` 之 transmitter 為 **SGW**，
屬 ASCM 自發訊息。對它注入 —— 真件則與 ASCM 自身之週期發送在匯流排上衝突，
模擬則等於自己餵自己再讀回（迴路驗證，非 DUT 驗證）。
HU 按鍵是真實入口，其後 `BDL_Enbl`／`ASCM_Stat`／角落高度方為 DUT 側輸出。
027 群本即此型，未動。

022-04 另將角落高度 baseline 之讀取**置於入口之前**（新步 2），
因為該條要驗的是「回到**請求當時**之高度」—— baseline 必須錄在請求發生之前。

022-02 之 `value read in step 1` 指涉隨入口改寫自然消除，現指向入口第三步之 Read
（新步序：`changes from the value read in step 3`）。

### 2.2 027-03 隱藏狀態前置

Pre-Condition 增第 2 條：
`The active ride height setting is 0 (Normal) before the test begins`

理由：該條驗「回復目標為請求當時之設定」，步 1 將設定改為
`1 (Aerodynamic)`。**若 active 設定原本就等於 default，
「回到記錄值」與「回到 default」兩種實作都會通過** —— 假通過（IN §7 FF）。
先確立 Normal 再改 Aerodynamic，兩者方可區分。

### 2.3 波及範圍與寫回

| 條 | 處置 |
|---|---|
| 022-01 | 已寫回列 23 → patch |
| 027-03 | 已寫回列 26 → patch |
| 022-02／03／04 | batch json 內改，**維持 PENDING 不寫回** |
| 027-01／02／04／05 | 未變 |

寫回以 `--start-row 23` 覆寫既有六列（新增旗標），
`sheets_patched` = **3**：022-01 之 procedure 與 ER、027-03 之 pre_conditions。
**只有三格變動**，其餘 93 格逐格相同 —— 修訂之最小性由此可見。

```
round-trip 6 列 × 14 欄，差異 0
```

（欄數由 16 降為 14，即 S／AB 兩欄不再寫入。）

---

## 三、修訂後義務

```
機檢（B1 九條）        機檢項全數 PASS，N 欄相異值數 1
§5.2 長度／§5.1 主動詞／ER 1:1   全批 PASS
交付 lint（全簿 19 列） clean — 0 findings
指紋重 stamp           prompt_template 相符、exemplar_set 相符
```

| 產物 | SHA256 |
|---|---|
| `workbook/bed_lowering_04.xlsx` | `fd983361dde90948b1807e2e13bdfe9ecc857ba8ca65fc4027d887115cb13e5b` |
| `batches/B1/b1_tcs.json` | `e3ad9532e1ac26b303568ac03ce7f9a996e6b517bb1eec881014241a9205941e` |
| `batches/B1/manifest.json` | `8d0f08b827c90e3725f32d4588137821af32de5fb43424f112c25d292cee8b89` |
| `feature.yaml` | `b65d7c84fca2badd43a2518d5c5354adb9616ffe99504f78d17bb79d769636aa` |
| `scripts/recon.py` | `6aa5ed738a0ec49164fa4e03c22bb1ce652159e2e1ef8d483da54b532cc293aa` |

工作簿鏈（皆保留於磁碟，使每一段可獨立複驗）：

```
00 起建（= R-G1 母本，逐位元相同）
01 pilot 13 列寫回
02 B1 六列寫回（列 23–28）
03 R-BLM16(2)(3) 清 S/AB 兩欄（列 10–28，38 格）
04 下放包 09 §二 之三格修訂（列 23、26）   ← 現行
```

---

## 四、執行層自陳

### 4.1 一處 assertion 名稱與其數字語意相反（全域線，回報不動）

閘控化之後，本 feature 之輸出讀起來是這樣：

```
PASS — every leaf's citation parses to a section: expected 176, measured 176
```

**名稱說「每條都解析得出 section」，而 176 是「解析不出來的條數」。**
`a.check` 之 measured 值取自 `len(a03res["unparsed_citations"])`，
原本期望 0 時語意通順（「零條解析不出」），一旦可宣告非零，
名稱與數字就對不上了。

**本包不改名**：`a.check` 之 name 會逐字進每個 feature 之 `RECON.md`，
改名等於改動全案既有基線之輸出文字，超出 R-BLM16(1) 之授權
（該條只准把它納入 want 閘控）。建議由全域收尾包一併處理，
候選名如 `citations without a parsable section`。

### 4.2 其餘

1. **未跑其他 feature 之 recon 回歸**（理由見 §1.1 末）。
2. **B1 之 completion 仍非模型產出**（第二次記載）。本包為修訂，
   未重新生成，故下放包 08 §二-1 所要之品質對比仍給不出來。
3. **台架可執行性未驗**（第六次記載）。本包新增之
   「先置 ride height = Normal」前置，其台架確立方式未查證。
4. **`patch_cells.py` 無 `--set` 能力**，只能清空。
   DR-1 回覆後要代入實值時需擴充或改走 write_back，屆時再說。
5. **入口改寫之理由未經台架實證**：「對 ASCM 自發訊息注入會衝突」
   為依 transmitter=SGW 所作之推論，**未在真件上實測過衝突**。
   推論成立與否不影響改寫之正確性（HU 按鍵本就是真實路徑），
   但該理由本身是推論。

---

## 五、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；結案動作清單見 `DATA_REQUESTS.md`，本包已將 5 Km/h 之複驗義務掛入 manifest |

---

## 六、停點

**已停。** 交**分析層複審**。

複審通過後依 R-BLM16 末段：B1 定版（不回計乾淨批數，R-G14 計數自 B2 起），
B2（Activation Gating，28 leaf）由分析層逐包下放，不另經 Pei 關卡。
