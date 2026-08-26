# 上繳包 05 — Bed Lowering Mode：pilot 修正（R-BLM12）

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/05_pilot_fixes.md`
（sha256 `b6f3f63d3246bcdabfff0b2190e96b61ff2dc98437cc3f479ef2ceb48f3d157a`）
執行層：Tier 1

**結論：A 類全數完成（並含表列遺漏者）、C 類完成、B 類四條全部個案停。
修訂版停在 `batches/pilot/`，未寫回。**

---

## 〇、一句話先講 B 類

**B 類四條全部停，不是三條停一條過，也不是查得不夠。**
HU→ASCM 之 Bed Lowering 請求訊號**在兩個綁定 DBC 與 LID 中都不存在**，
且四條之其餘可觀察物全部落在 sibling 手上（EVIC 屬 011-03／038-01、
highlight 屬 037-03）。詳見 §二，含完整已查路徑。

---

## 一、A 類

### A1 `Observe` 主動詞改寫 —— 12 處，另含表列遺漏 2 處

下放包表列 10 處，實改 **12 處**（A1 末句「上表為指令非枚舉上限」）：

| TC | 步 | 改為 |
|---|---|---|
| 011-03 | P3 | `Check that the EVIC area of the instrument cluster displays "..."` |
| 011-04 | P4 | `Check that the EVIC message contains the wording "..."` |
| 037-03 | P1 | `Press "Bed Lowering" on the HU Controls tab, check that the button highlight is shown and record it` |
| 037-03 | P3 | `Check that the "Bed Lowering" button highlight is no longer shown` |
| 037-04 | P1 | `... and check that the button highlight is shown` ← **表列遺漏**（原文為 `and observe that`，非行首 `Observe`）|
| 037-04 | P3 | `Check that the "Bed Lowering" button highlight is removed with no further input given` |
| 037-05 | P1 | 同 037-04 P1 ← **表列遺漏**（同上）|
| 037-05 | P3 | `Check that the "Bed Lowering" button highlight is removed` |
| 038-01 | P1 | `Check that no Bed Lowering message is displayed in the EVIC area` |
| 038-01 | P4 | `Check that the EVIC area displays "..."` |
| 038-02 | P3 | `Check that the unsuccessful message is displayed in the EVIC area` |
| 038-03 | P4 | `Check that the EVIC unsuccessful message contains the wording "..."` |

兩處遺漏之形態值得記：**它們不是行首的 `Observe`，而是句中的
`and observe that`** —— 下放包之表以行首形態列舉，句中形態逃過。
本包之掃描改以「禁用詞出現於任何位置」為判準，改後複掃：

```
### 殘留禁用主動詞掃描（Procedure 全批）
  無
```

037-03 P1 之 `record whether` 與 ER 單態斷言之矛盾一併消除（R-BLM12 A(1)）：
`record whether its highlight is shown` → `check that the button highlight is
shown and record it`，ER 之 `is shown and recorded` 因而成立。

### A1 附帶 —— §5.2 長度複核發現 6 處超限，已拆

下放包令「改寫後逐條複核 §5.2」。複核結果**不是全綠**：

| TC | 原 | 處置 |
|---|---|---|
| 011-02 | Final 29w | 拆讀取(4)與比較(5)兩步 |
| 037-01 | P1 19w（設定步驟，超 §5.1 例外之 18w）| 收斂為 15w |
| 037-04 | Final 19w | 收斂為 14w |
| 037-05 | Final 21w | 拆 highlight 撤除(3)與無其他變化(4) |
| 038-02 | Final 21w | 拆 EVIC 有(3)與 HU 無(4) |
| 038-04 | Final 25w | 拆文字基準(3)與版面基準(4) |

全部保持 ER 1:1（拆步驟同時拆 ER）。複核後：

```
全批長度分級 PASS
```

一點口徑說明：訊號步驟多為 13–18 words，**未計入超限** ——
其 `to ...` 子句屬 §5.1 例外（target 為 internal signal，opaque），
故適用 §5.2 之 C 類（≤18w）而非 A 類（≤12w）。
ER 不受 §5.2 長度分級規制（該節規制對象為 step），故 037-04 之 ER
保留完整結果陳述而未隨 Procedure 收斂。

### A2 011-02 訊號驗名 —— **驗有**

| 訊號 | 結果 |
|---|---|
| `$ASCM_FD_1.RL_Lvl$` | 驗有，msg 0x52F，transmitter SGW |
| `$ASCM_FD_1.RR_Lvl$` | 驗有，msg 0x52F，transmitter SGW |
| VAL_ 列舉 | 二者皆僅 `254 NOT_INIT` / `255 SNA`，其餘為物理值 |

已補入 manifest 之 `signals_verified`。**惟 011-02 同時在 B 類停下範圍內**
（下放包 A2 已預期此情形）：該兩訊號目前仍被引用，故 manifest 記「查有」
而非「已退場」；若日後改錨使其退場，屆時改記。

### A3 038-04 `design_method` → `Fault Injection`

已改。全批 design_method 分布因而收斂為 `{'Fault Injection': 13}`。

### A4 Pre-Condition 車型限定

13 條全數 `The vehicle is a DT model equipped with the air suspension system`
→ `The vehicle is equipped with the air suspension system`。

---

## 二、B 類 —— 四條全部個案停（下放包 §二-4）

### 2.1 已查路徑（逐項具名，供覆核）

| 查詢 | 範圍 | 結果 |
|---|---|---|
| 訊號名含 `BDL`／`Bed` | dbc_fd 全 323 訊息／2,037 訊號 | **僅 1 個**：`$ASCM_FD_2.BDL_Enbl$` |
| 同上 | dbc_b 全 155 訊息／914 訊號 | 0 |
| LID 提及 Bed Lowering／BDL 之列 | `CAN Mapping` 2,629 列 | **僅 1 列**：`BDL_Enbl` = `Status of Bed Lowering Mode` |
| `GW_C_I_11` 線索（下放包指定）| LID 14 列 | 全為 ASCM→HU 方向之狀態（`ASCM_Stat`、`FL_Lvl`…），**無請求訊號** |
| ETM（HU）發送之訊息 | dbc_fd 全 31 個 | 名稱含 `ASCM`／`SUSP`／`BDL` 者 **0** |
| HU 側懸吊訊號 | `TELEMATIC_*` | 僅 `HU_AirSusp_UpSw1`／`DnSw1`（Up/Down 軟鍵）與 `Susp_*_Req`（設定選單項），**皆非 BLM 請求** |

### 2.2 判定之關鍵一步：transmitter

| 訊息 | transmitter | 方向 |
|---|---|---|
| `ASCM_FD_1` (0x52F) | **SGW** | 閘道 → HU，**DUT 輸入** |
| `ASCM_FD_2` (0x5A5) | **SGW** | 閘道 → HU，**DUT 輸入** |
| `TELEMATIC_FD_11` (0x260) | ETM | HU → 外，DUT 輸出 |

`BDL_Enbl` 之 transmitter 為 SGW，且 LID 對它的描述是
**"Status of Bed Lowering Mode"** —— 兩個獨立來源都說它是狀態回報，
不是 HU 發出的請求。**故「以 HU 發出之匯流排訊號改錨」在本 feature
不可行，不是查得不夠，是該訊號不存在於已綁之基線。**

### 2.3 另一條路也走不通：非 sibling 之顯示狀態

B 類原則 2 之第二選項為「HU/EVIC/cluster 上非 sibling 持有之顯示狀態」。
本 Test Set 之可觀察面只有兩樣，且兩樣都被 §二-3 明文劃走：

- EVIC 訊息文字 → 011-03／038-01 持有
- button highlight → 037-03（及 04／05）持有

規格另有 status bar 之 truck-lowering 圖示（下放包 01 §一-3），
但它屬 `HU Feedback` 組（母號 008／026／031／032／036），**是另一個 Test Set**。
取用它等於把本組之驗證錨到另一組的觀察物上，
既越 sibling 邊界之精神，亦為 scope drift。**未取用。**

### 2.4 四條之現狀

| leaf | 現行最終檢查對象 | 為何仍不合格 |
|---|---|---|
| 011-01 | `$ASCM_FD_2.ASCM_Stat$` = 10 (SYSFAIL) | 自身注入之下游狀態，SGW 發送，非 DUT 輸出 |
| 011-02 | 後角落高度 + `ASCM_Stat` | 同上；角落高度亦為 ASCM 側輸出 |
| 037-01 | `ASCM_Stat` = 10 且未報 9 | 同上 |
| 037-02 | `ASCM_SysFail` + `ASCM_Stat` | 同上，且「receive」本身只能由 DUT 反應觀察 |

**四條之 A 類修正已套用，B 類改錨未施行，錨點維持上繳 04 版。**
依下放包 §二-4「其餘照修不連坐」，另九條已完成全部修正。

### 2.5 執行層之觀察（非裁定）

這四條之共同形態是：**037 把「偵測到」「收到」寫成獨立需求，
而 SWE.6 層級唯一能觀察「偵測到」的方式就是它的下游反應** ——
而那些反應已被拆成別的 leaf。這不是本批之缺陷，是上游分解粒度
與可觀察性之間的結構性落差。可能的出路（**皆屬 Tier 2，本包不代裁**）：

1. 四條標為不可獨立驗證，入 coverage gap disclosure table（R-BLM2 之既有機制）
2. 放寬 sibling 邊界，允許四條以 EVIC／highlight 為錨並於 reasoning 註明
   其驗證目的與 011-03／037-03 不同
3. 向上游登 DR，要求補 HU→ASCM 請求訊號之對照（若實際存在於未綁之其他基線）

---

## 三、C 類

- **038-04 文字基準已落**：Pre-Condition 增第 6 條
  `The message wording baseline is the SYS1 normalised text of NRL-193702; the
  reference figure governs casing and line breaks only`，
  並於 A1 之拆步驟中使兩種基準各自可判（P3 對文字、P4 對版面）。
- 其餘三項（近重複保留、角度不登 DR、hyphen）**未動作**，依 R-BLM12 C(5)(6)(7)。

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

括號下半語言檢含在其中（CJK 掃描），13/13 通過。
機檢不覆蓋之 §9 項次仍為 3／5(可執行性)／6／7／8／9／11／12／17，
一如上繳 04 §5.2 —— **本包未擴大機檢覆蓋面，故該清單未縮短。**

### 4.2 manifest 重 stamp

| 項 | 值 |
|---|---|
| `pilot_tcs.json` | `c60f6dc0c935bb9b8f15f3ab58ebd702be1543b58b76259d0bf5c06129f8cf51` |
| `context.json` | `94792691209039060c5de0abba9e991c3c9f60698211d5f757aa0b498b15a7eb` |
| `manifest.json` | `e93df25c6f49d0556c3c9bf7b2ba23629f5742d0aadfb7f97d768050030dba8a` |
| prompt_template | `e4ebcede4ed9a6d6566738c6875143b4c103a3dfcff7d8d95513f2e5134d4d8a` |
| exemplar_set | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`（空集，未變）|
| IN sha256 | `0b0cea006552a2f244ba8e733ef6227b132b591a34defb65234934985fe2598e`（未變）|

`prompt_template` 自上繳 04 之 `0551dd30…` 變為 `e4ebcede…`。
**該變動之唯一來源為 `context.json`**，而 context 變是因 `pilot_tcs.json`
之修訂使 `feature.yaml` 以外之來源未動、context 內含之 sources sha 更新 ——
逐源列出後可直接指認，非「有東西變了」。重 stamp 後比對：

```
prompt_template: 相符
exemplar_set: 相符
```

manifest 另新增三鍵：`signals_verified`（A2）、`signals_absent`
（B 類之查無，含已查範圍）、`b_class_halted`（四條之停下紀錄）。
**`signals_absent` 之存在是刻意的** —— 一份只記「查到什麼」的 manifest，
與一份「沒查」的 manifest 長得一樣。

### 4.3 修訂 diff

逐 TC 之改動已列於 §一（A1 表、A1 附帶表、A3、A4）與 §三（C 類）。
本包共 **27 處**欄位層級修改：A4 13 處、A1 12 處、A3 1 處、C 類 1 處；
另 6 條之 Procedure／ER 因長度拆分而整體重寫（列於 A1 附帶表）。

---

## 五、執行層自陳 —— 本包應驗而未驗者

1. **B 類「查無」之範圍限於已綁之兩個 DBC 與 LID v1_76。**
   HU→ASCM 請求訊號可能存在於**未綁之其他基線**（如 display 綁的
   `PDT27_E2A_R1_*`，或更新版 LID）。本包**未跨基線查** ——
   R-BLM11 已裁定綁 vehicle_setting 之版本，跨基線查會使結論不對應交付基線。
   故「查無」之正確讀法是「**在本 feature 之裁定基線上查無**」，不是「全案不存在」。
2. **`prompt_builder` 相容性仍未驗**（自上繳 03 起第三次記載，狀態未改善）。
   本包未組 prompt、未走 `backend/generator.py`。
3. **本 feature 仍無 `scripts/lint_tcs.py`**，13 條仍未過交付用 lint（同上繳 04 §八-2）。
4. **台架可執行性仍未驗**（同上繳 04 §八-4）。本包新增之
   `$ASCM_FD_1.RL_Lvl$`／`$RR_Lvl$` 讀取步驟同受此限。
5. **§二-5 之三條出路未評估其代價**，僅列出。評估屬 Tier 2。

---

## 六、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |

本包未新增 DR。§二-5 之出路 3 若獲採，將產生一筆新 DR。

---

## 七、停點

**已停。** 修訂版 13 TC 在 `batches/pilot/`（`batches/` 不入版控，
交審請讀磁碟，sha256 見 §4.2）。未寫回、未續批、未自評通過。

**待 Pei 之項：B 類四條之處置（§二-5 三選一或另裁）。**
