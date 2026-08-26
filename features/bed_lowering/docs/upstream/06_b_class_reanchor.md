# 上繳包 06 — Bed Lowering Mode：B 類四條改錨（R-BLM13）

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/06_b_class_reanchor.md`
（sha256 `bacce7b0f353988082477ffdaaa8d5cfdd98a0efd094518d1086cb69dd6574b2`）
執行層：Tier 1

**結論：四條改錨完成，13 條完整版停在 `batches/pilot/`，未寫回。
機檢全綠、長度分級全綠、三對 sibling 區分逐字複核通過。
另有一項本包自行發現之不一致（§五-1）須 Pei 決定。**

---

## 一、四條改錨

### 011-01（R-BLM13(a)）

Final 由 `Read $ASCM_FD_2.ASCM_Stat$ ... 10 (SYSFAIL)` 改為
`Check that a Bed Lowering fault indication appears in the EVIC area`。
`ASCM_Stat` 讀取降為第 4 步（注入生效確認），其 ER 之結論子句
`showing the fault condition is detected` 已移除，**結論只在 Final ER 出現一次**（§二-1）。

括號下半：`(Fault indication presence only; message wording is owned by 011-03)`
Pre-Condition 增第 4 條（EVIC 可見）。

### 011-02（R-BLM13(a)，baseline 保留）

角落高度之讀取(1)／再讀(4)／比較(5)三步依指令原樣保留，
Final 新增為第 6 步：EVIC unsuccessful 指示**出現**。
`$ASCM_FD_1.RL_Lvl$`／`$RR_Lvl$` 因而**續用**，manifest 維持「查有」。

比較步(5)之 ER 亦已去結論子句，結論移至第 6 步。

括號下半：`(Corner levels unchanged; indication presence only, wording owned by 011-03)`

### 037-01（R-BLM13(c)，trigger 區分，未動用 (a)）

步序改為 **故障先於按鍵**：
`ASCM_SysFail = 1`(1) → `ASCM_Stat` 確認(2) → `Press "Bed Lowering"`(3) →
Final `Check that the "Bed Lowering" button highlight is not shown after the press`。

因採 (c) 之 trigger 區分，本條**得逕行斷言 highlight 之終態**，
不受 (a) 之「只斷言存在」限制 —— 這是 (c) 優先於 (a) 的實際差別，
非措辭偏好。reasoning 已載此點。

括號下半：`(Pre-existing fault at request time; mid-cycle removal is owned by 037-03)`

### 037-02（R-BLM13(a)，同 trigger）

與 037-03 同 trigger（故障後於啟動），無法以 trigger 區分，故依 (a) 錯開層級：
Final 為 `Check that the "Bed Lowering" button highlight state changes from the
state in step 1` —— **斷言「有變化」，不斷言「熄滅」**。

括號下半：`(Reaction presence only; specified highlight behavior is owned by 037-03)`

### 委派句（R-BLM13(b)）

四條之 reasoning 皆依 IN §8.2.1 工作流第 4 步具名持有 leaf 號，例如 011-01：

> 刻意未涵蓋：EVIC 訊息之逐字文字由 SWE1-HMI-BLM-011-03 與
> SWE1-HMI-BLM-038-01 涵蓋；highlight 之撤除行為由 SWE1-HMI-BLM-037-03 涵蓋。

---

## 二、§二-3 sibling 區分複核 —— 三對逐字比對

| 對 | 下半相同？ | Final 相同？ |
|---|---|---|
| 011-01 vs 011-03 | 否 | 否 |
| 037-01 vs 037-03 | 否 | 否 |
| 037-02 vs 037-03 | 否 | 否 |

逐字對照（節錄 037-02 vs 037-03，區分最細的一對）：

```
037-02 下半 : (Reaction presence only; specified highlight behavior is owned by 037-03)
037-03 下半 : (Highlight state before and after the fault response)
037-02 Final: Check that the "Bed Lowering" button highlight state changes from the state in step 1
037-03 Final: Check that the "Bed Lowering" button highlight is no longer shown
```

`state changes` vs `is no longer shown` 即 (a) 所要求之層級差：
**前者對「熄滅」與「由亮轉某狀態」皆為 pass，後者只對「熄滅」為 pass。**
若 highlight 變成閃爍而非熄滅，037-02 pass 而 037-03 fail —— 兩條因而不冗餘。

---

## 三、§二-4 長度分級

```
PASS —— 全批無超限
```

改動之四條 Final 分別為 12／12／13／15 words，皆在 §5.2 B 類之 18w 內，
無需再拆。

---

## 四、修訂後義務

### 4.1 全批機檢 + 括號下半語言檢

```
TC 數 13
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 8, 'P2': 5}
design_method 分布 {'Fault Injection': 13}
Input Test Data == NA 之比例 13/13
機檢項全數 PASS
```

機檢不覆蓋之 §9 項次仍為 3／5(可執行性)／6／7／8／9／11／12／17，未縮短。

### 4.2 manifest 重 stamp

| 項 | 值 |
|---|---|
| `pilot_tcs.json` | `90d44ea39c3c1671bdbb5097039b5d146efedad712ec7ae32469d4668d54ac2b` |
| `manifest.json` | `aef641ff75b730044e3eeaa7e1b2d7607d63880ead55cfee277a1aed246e2688` |
| `context.json` | `94792691209039060c5de0abba9e991c3c9f60698211d5f757aa0b498b15a7eb`（未變）|
| prompt_template | `75e7763d0397addc04815b209816bcdf444a657b6c44237525afb4e393016764` |
| exemplar_set | `e3b0c442…`（空集，未變）|

重 stamp 後比對相符。

`b_class_halted` 四筆已加 `resolved: R-BLM13` 與 `branch_used`（逐條記 (a) 或 (c)），
**原停下紀錄一字未刪**（R-TM13）。加註之措辭刻意寫成：

> 停下當時之判斷（無 DUT 輸出可錨）在事實上仍然成立，
> 改變的是裁定允許以 sibling 持有之觀察物為錨並錯開斷言層級，**非事實翻案**。

`signals_absent` 亦加一句：**R-BLM13 未使該訊號出現，只是不再需要它。**
查無之事實不變 —— 這兩處措辭是為了讓日後稽核不會把「不再需要」讀成「後來查到了」。

### 4.3 修訂 diff

四條之 `tc_title`（下半）、`pre_conditions`（011-01／011-02 增 EVIC 可見）、
`test_procedure`、`expected_result`、`reasoning` 全數重寫；
其餘九條本包未動。分支引用逐條見 §一與 manifest 之 `branch_used`。

---

## 五、執行層自陳

### 5.1 **本包造成一項批內不一致，須 Pei 決定**

R-BLM13(b) 令四條之 reasoning 載委派句，本包因而為該四條加了
**per-TC 之 `reasoning` 欄**。但 **IN §10.4 明定 `reasoning` 為
top-level field（"Top-level field on the response (not per-TC)"）**。

結果是：批內 13 條中，4 條有自己的 `reasoning`，9 條沒有，
另有一個涵蓋全批的 top-level `reasoning`。**這是本包產生的不一致，
不是本來就有的。**

三個選項（**本包不自擇**）：

1. 四條之委派句改寫入 top-level `reasoning`，移除 per-TC 欄 —— 合 §10.4 字面，
   但委派與 leaf 之對應會變模糊（一段文字要講四條的委派）
2. 十三條全數補 per-TC `reasoning` —— 批內一致，但擴大 §10.4 之偏離面
3. 維持現狀並於 profile 立 `[OVERRIDE IN §10.4]` —— 需 Tier 2 之 override 裁定

**未自擇之理由**：這不是「怎麼做」而是「做出來對不對」，
且 §10.4 與 R-BLM13(b) 兩條文皆可支持不同讀法（FO §0：同一條文兩種讀法
即非機械套用）。寫回工作簿時 `reasoning` 不入交付欄，故本項**不阻斷寫回**，
但會影響交付說明與日後批次之一致性。

### 5.2 其餘未驗項（狀態未改善，逐輪重述）

1. **`prompt_builder` 相容性未驗**（自上繳 03 起第四次記載）。
2. **本 feature 仍無 `scripts/lint_tcs.py`**，13 條未過交付用 lint（第三次記載）。
3. **台架可執行性未驗**（第三次記載）。本包新增之「EVIC 指示出現」
   類觀察尤其需要實機確認 —— **「指示出現」比「文字正確」更難機械判定**，
   台架若只能截圖比對文字，本類斷言之執行方式須另議。
4. **`recon.py` 仍未實跑**（第四次記載）。
5. **R-BLM13(a) 之代價未量化**：(d) 已言明交付本會出現觀察物重疊之 TC 對。
   本包僅複核三對之區分 token 可見，**未評估審查者實際閱讀時是否分得開** ——
   那要靠 pilot 人審回答。

---

## 六、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |

本包未新增 DR。R-BLM13 已明文不採出路 3（登 DR）。

---

## 七、停點

**已停。** 13 條完整版在 `batches/pilot/`（`batches/` 不入版控，交審讀磁碟，
sha256 見 §4.2）。未寫回、未續批、未自評通過。

下放包 06 §三-4 載明此輪過後即為 pilot 退出審（R-G15，FO 讀法）
與工作簿寫回授權，由 Pei 裁。**執行層之待決項為 §5.1 一項。**
