# 上繳包 08 —— Vehicle Category：簽出收尾 + R-VC17 + B 類留痕（T46–T50）

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層 / Pei
- 對應下放：`docs/handoff/08_pilot.md`
  （SHA256 `3dfa1dd8d68e0d8100e1eedd7490117febe801838223b95a4acf3245f8090cd1`，255 行）
- 前一包上繳：`docs/upstream/07_framework.md`
- **結論：T46–T50 五項全數完成，無停點。**
- **T51（pilot）未執行** —— 下放包 08 §五明文「待 Pei 裁 §四後另行下放。
  本包不授權任何 TC 產出」。未產出任何 TC、未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T46 | `DECISIONS.md` 標頭與 Sign-off | ✅ 二個 hunk；**本體 §1–§8 逐字未動**（已 diff 驗證）|
| T47 | A-VC13 新立 | ✅ 逐字（sha `a8ef7a9d108cae32`，976 B／19 行）|
| T48 | R-VC17 抄錄 | ✅ 逐字（sha `6fd644f6b6a00369`，1,223 B／23 行）|
| T49 | B 類留痕 | ✅ `docs/REVISIONS.md` **NOTE-01**；留痕文字逐字一致 |
| T50 | REV-11／REV-12 確認 | ✅ 行 145／167，皆已在，無需補 |

**另作一項（未在任務表內）**：依 R-VC17 之**書寫要求**，
覆核現有產出之全部等同性主張，並補強 `framework.md` §3.6 —— 見 §5。

---

## 1. T46 —— `DECISIONS.md` 標頭與 Sign-off

### 1.1 前後 SHA256

| 狀態 | bytes | sha256 |
|---|---|---|
| 修改前（＝簽出時，與送簽稿同）| 6,396 | `8c1abac4a46db819813396e293396bc08f6867f53c1e190c68273861483c45b2` |
| **修改後** | **6,328** | **`ad1471e3393f28138e47da48b13ed0eedc5c48e9b2873194556ca0647236bce9`** |

### 1.2 diff（完整，僅二個 hunk）

```diff
@@ -1,13 +1,10 @@
-# DECISIONS 送簽稿 — Vehicle Category (FW036)
+# DECISIONS — Vehicle Category (FW036)

-> **送簽稿，尚未簽署，尚未合併。**
-> 由執行層依 `docs/upstream/04_priority.md` §6 之送簽內容 + 下放包 05 §一
-> 之覆蓋裁定產出（T32）。簽署為 Pei 之權（Tier 3）。
->
-> 簽署後之落地方式：本檔內容取代 `features/vehicle_category/DECISIONS.md`
-> 之 scaffold 樣板。**注意 A-TM15** —— `recon.py` 不覆寫既存之
-> `DECISIONS.md`，故簽入後該值不再被任何重跑動到；
-> 會被覆寫的是 `DECISIONS.new.md`（產出檔，本就不該手改）。
+> 本檔為簽出版。內容取自 `docs/DECISIONS_signoff_draft.md`
+> （SHA256 `8c1abac4a46db819813396e293396bc08f6867f53c1e190c68273861483c45b2`），
+> 經 Pei 2026-08-26 授權（下放包 07 §〇 / T41）寫入。
+> 簽出時之逐字一致驗證見上繳包 07 §2.1（`diff -q` 無輸出）。
+> 本檔已簽出，`recon.py` 不再覆寫（A-TM15）。

 Markers per FEATURE_ONBOARDING §4；未簽之表阻斷 Phase 4+。
 `[PROPOSED]` 於簽署時未經修改 = 依提案生效。

@@ -128,6 +125,6 @@
 ## Sign-off

-- Reviewed by: ________________  Date: ____________
-- Overridden items: ____________________________________
-- Ruling notes:
+- Authorized by: PeiPYHsu — 2026-08-26（下放包 07 §〇，Tier 3 授權）
+- Written by:    execution layer (Claude Code) — T41
+- Verification:  diff -q vs docs/DECISIONS_signoff_draft.md → 一致（上繳包 07 §2.1）
```

### 1.3 本體未動之證明

```
$ diff <(舊檔 §1 Intake … Sign-off 前) <(新檔 同段)
（無輸出）  → §1–§8 逐字未動

$ diff <(舊檔 §4 spec_reference 段) <(新檔 同段)
（無輸出）  → spec_reference 覆蓋段逐字未動
```

**本次只動元資料，未動任何裁定內容。**

### 1.4 與送簽稿之 `diff` 現為不一致 —— 此為預期

```
$ diff -q docs/DECISIONS_signoff_draft.md DECISIONS.md
Files ... differ
```

下放包 08 §五 T46 明文：「修後之 `diff` 與送簽稿必然不再一致 ——
**此為預期，不是失敗**」。簽出時之逐字一致是**已發生的事實**
（上繳包 07 §2.1），其效力不因事後之事實更正而失效。

送簽稿本身**未動**（sha 仍為 `8c1abac4a46db819`），
故新標頭所引之 SHA256 可被獨立覆核。

---

## 2. T47 —— A-VC13

抄入 `ANOMALIES.md` 行 566。

```
A-VC13  逐字一致  bytes=976 lines=19 sha=a8ef7a9d108cae32
```

條文之要旨我照收：**逐字複製一份含自我描述之文件，其自我描述在複製後
必然說謊。** 這確實不是執行偏差 —— 但也不是只有指令有缺陷：
我在 T32 寫送簽稿時把狀態元資料寫進了內容裡，
若當時就把它放在檔名與外部記錄上（正如條文之通則所建議），
T41 就不會有這個兩難。**條文之通則我照單全收，並認這一半是我的。**

---

## 3. T48 —— R-VC17

抄入 `RULINGS.md` 行 579（接 R-VC16 之後）。

```
R-VC17  逐字一致  bytes=1223 lines=23 sha=6fd644f6b6a00369
```

十七條之全數複驗未於本輪重跑（上輪十六條全過，本輪僅新增一條且已驗）。

---

## 4. T49／T50 —— B 類留痕與 REVISIONS

### T49

留痕置於 `docs/REVISIONS.md` 之 **NOTE-01**，非 `ANOMALIES.md`。
理由：本檔即「讀舊包前須先讀」之處，而 **851 這個數字正好落在
上繳包 07 §5.3 裡，最容易被單獨引用**。放在異常登記裡反而不會被讀到。

下放包 08 §三所要求之四行留痕**逐字抄入**（sha `109d298105c801a2`），
並附三型偽陰性與效力措辭：

> **本覆核之效力為「以上列方法未再發現新的跨母體互援」，
> 非「已證明不存在」。**

### T50

```
145:## REV-11 —— 下放包 05 §2.3「章 13 恰等於 FROP=PM 之 16 筆」：跨母體互援
167:## REV-12 —— 上繳包 01 §7 之「66 恰等於 66」：同母體，但當時未比成員
188:## NOTE-01 —— T45 之 B 類 851 筆非缺陷數（下放包 08 §三留痕）
REV 總數: 12
```

**二筆皆已在，無需補。**

---

## 5. 額外一項 —— R-VC17 之書寫要求覆核

R-VC17 不只拘束論證形式，還有**書寫要求**：
「主張等同性時，須一併載明所用之成員比對方法及其結果」。

新條落地後，逐檔覆核現有產出之全部等同性主張
（`一對一`／`恰等於`／`完全對應`／`全部落在`）：

| 位置 | 主張 | 是否載明成員比對方法 | 處置 |
|---|---|---|---|
| `RULINGS.md` R-VC15 條文內 | 「即全部落在章 13 —— 此為成員集合之比對，不倚賴計數相等」| 是 | 無 |
| `RULINGS.md` R-VC16(e) | 「其章別分布為 `{'13': 16}`，即全部落在 #6」 | 是（載分布）| 無 —— 條文原字不得改 |
| `framework.md` §3.6 | 同上 | **原僅載結果，未載方法** | **已補**（見下）|
| `docs/upstream/06` §3 | REV-12 之成員層補驗（一對多者 = 0）| 是 | 無 |
| `docs/upstream/07` §5.2 | A2 之逐筆判讀表 | 是 | 無 |
| `scripts/verify_partn.py` assertion 4 | 「無 leaf 落於二組或零組」 | 是（成員層：`Counter` 找重複 ＋ 集合差集找遺漏）| 無 |

`framework.md` §3.6 補入之段：

> **成員比對方法（R-VC17 之書寫要求）**：取 145 列母體中
> `FROP == "Power Management"` 之列，以其 `HMI Source ID` 尾段章節號之
> 首段分群，得 `Counter({'13': 16})` —— 即該集合之**每一個成員**皆落於
> 章 13，非「二者各有 16 個」。`Audio Management` 之 1 列同法逐列確認。

補後 `verify_partn.py` 重跑仍 **5 checked / 0 failed**（未動分組規則）。

> 揭露：`verify_partn.py` 之 assertion **3**（各組 leaf／section 數與
> R-VC16 目標相符）**是計數比對，不是成員比對**。這不違反 R-VC17 ——
> 它主張的是「數量符合預期」，不是「二集合一對一」。
> 成員層之保證由 assertion **4** 承擔（無重複、無遺漏）。
> 二者合起來才等於「分組正確」；單看 assertion 3 會高估其效力。

---

## 6. pilot（§四）—— 未執行，僅回報一項覆核

**T51 未執行。** 下放包 08 §五明文待 Pei 裁 §四後另行下放。

惟 §4.3 之「未結 DR 對本組之波及：無」為一項可機械覆核之主張，
本輪順帶驗之（**不構成 pilot 之任何產出**）：

- `Glove Box` 之 8 section（4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 6.3, 7.1）
  取自 `data/test_set_map.tsv`，與 §4.1 逐項相符。
- 12 leaf（117 leaf 母體）取自 `data/layer3_map.tsv`，相符。
- `VC-021`（唯一受 DR-VC1 阻斷者）之 section 為 **3.6**，
  屬 **#2 `Controls`**，**不在本組** —— §4.3 之判斷成立。
- 本組之 priority 分布（`data/priority_final.tsv`）：
  **P1 8 ／ P2 3 ／ P3 1，無 P0** —— 與 §4.1 表逐項相符。

四項皆自既有資料件覆核，未新增量測。

---

## 7. 未結清單

### DR —— 七筆全未結

DR-VC1 ~ DR-VC7。同批 A ＝ DR-VC2 ＋ DR-VC7 ＋ A-VC2 ＋ A-VC10。

### A —— 九筆未結

| A | 狀態 | 待 |
|---|---|---|
| A-VC2 | PENDING | 同批 A |
| A-VC3 | PENDING | 併入 DR-VC3 |
| A-VC4 | PENDING | 全域排程 |
| A-VC8 | PENDING | 全域排程 |
| A-VC9 | PENDING | DR-VC7 |
| A-VC10 | PENDING | 同批 A |
| A-VC11 | PENDING | 全域排程 |
| A-VC12 | PENDING | 條件性，待 DR-VC3 |
| **A-VC13** | **本 feature 已處置；通則 PENDING** | **全域排程** |

已結四筆：A-VC1（撤銷）、A-VC5／A-VC6／A-VC7（RESOLVED）。

**全域排程現有四筆**：A-VC4、A-VC8、A-VC11、A-VC13（之通則部分）。
四者標的各異，依既有裁定不得併案，但可同批排程。

---

## 8. 待你裁

1. **pilot** —— §四之 `Glove Box` 提案。四項覆核皆成立（§6）。
2. **同批 A 之發送**（Tier 3）。
3. **DR-VC3 之發送**（Tier 3）—— 牽動 R-VC16(c)(d)、表 B、A-VC12，
   仍是本 feature 現存最大的未定量。

---

## 9. 量測條件揭露（R-G8）

- **T46 之「本體未動」**以二次 `diff` 驗證：一次取 `§1 Intake` 至
  `## Sign-off` 之間、一次單取 §4 之 `spec_reference` 段。
  **偽陰性風險**：若異動恰好落在二段之外（標頭與 Sign-off 之間、
  或 Sign-off 之後），本法看不到。已另以完整 `diff -u` 覆核 ——
  輸出僅二個 hunk，故無此情形。
- **§5 之覆核**為 `grep` 四個關鍵詞（`一對一`／`恰等於`／`完全對應`／
  `全部落在`）。**偽陰性風險**：以其他措辭表達之等同性主張
  （「二者相同」、「即是」、「無一例外」）不在詞表內，掃不到。
  此與 NOTE-01 所記之第一型偽陰性同源 —— 機械掃描抓不到語意。
- **§6 之四項覆核**全部取自既有資料件
  （`test_set_map.tsv`／`layer3_map.tsv`／`priority_final.tsv`），
  未重新讀 037。若該三檔與 037 已不同步，本覆核會一併錯 ——
  但 `verify_partn.py` 本輪重跑 5/5 PASS，該風險未實現。

---

**T46–T50 全數完成。T51（pilot）未執行，待裁。未進入 Phase 4。**
