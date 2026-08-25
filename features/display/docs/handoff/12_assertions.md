# 下放包 12 —— marker 衝突之裁定、已裁常數改為機器檢查

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/12_assertions.md`
- 前一包：`11_binding_verify.md`（上繳已覆核，見 §一）
- **Q2／Q3 仍在 Pei 處，本包之工作皆不依賴其裁定**

---

## 一、上繳包 11 之覆核

**核可。停止條件 29 之觸發正確，三項皆不得由執行層自行補。**

### 1.1 §0 之一句話

> 我上輪自陳「合併這個動作本身沒有被交叉檢查」時，那是一句還沒有代價
> 的話。本輪它有了代價：三項。

自陳未驗項而下一輪真的驗出東西，這是該機制第一次兌現。記明。

### 1.2 §3.3 之時序追查 —— 沒有把責任攬到自己頭上，也沒有推開

`Test Set table` 與 `profile [OVERRIDE]` 兩行之 `[PROPOSED]` 出自
`61d1c12`（02 輪），**早於 `recon.py` 首次成功執行（09 輪）**。
故非合併時之降格，而是**既存分歧未被察覺**。

執行層以 `git log -S` 查明時序而非憑印象歸因，且明確指出
**R-DM32 未涵蓋此向**（兩側都有該項、marker 不同、且較嚴者在機器側），
拒絕替一條不存在的規則作主。**正確。** 裁定見 §四 R-G24。

### 1.3 §3.4 —— 「空的項」之觀察

> 正因為它的值是 0，它最容易在合併時被略過：一個內容為空的項，
> 讀起來像沒有內容。但它記的是「本 feature 未宣告任何 ruled-constant
> assertion」這件事，而那是一個應該被看見的空。

採認，且本包據此立 R-DM36 —— 該項不只該補回，**它指出的空本身該被填**。

### 1.4 §4 之自陳

> 我對一份自己寫過的腳本做了一個未經查證的假設（`probe_spec_mode.py`
> 本來就沒有 `norm()`）。

與 R-G19 同型，且對象是自己的產出。記明。

---

## 二、三項分歧之處置

| # | 項 | 處置 |
|---|---|---|
| 1 | `ruled-constant assertions` 缺席 | **補入**，並依 R-DM36 填實其內容（不再是 0） |
| 2 | `Test Set table (Part N)` | **改為 `[PEI]`**（依 R-G24，較嚴者為準；且該項本即 Tier 2） |
| 3 | `profile [OVERRIDE] clauses` | **改為 `[PEI]`**（同上） |

第 2、3 項須另記：`recon.py` 是對的，我在 02 輪自行填 `[PROPOSED]` 是錯的。
`FEATURE_ONBOARDING` 已定 framework 之 Test Set 表與 profile override
條款屬 Tier 2；把它們標成 `[PROPOSED]`，等於讓兩件必須由 Pei 決定的事
在簽核時無聲通過 —— **與 recon 想把 `spec_reference` 降格為 `[PROPOSED]`
是同一個錯，方向相反，而這次錯的是我。**

---

## 三、`recon_assertions` —— 把已裁常數變成機器檢查

`ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL` 揭露的是
**本 feature 從未宣告任何 ruled-constant assertion**。

`recon.py` 之 `Assertions` 類其 docstring 已寫明其存在理由：

> A recon that only prints counts leaves the comparison to whoever reads
> it, and the ruling that says 403 is then enforced by attention rather
> than by the script.

本 feature 已有數個經十一輪確立、且被反覆引用之常數，目前**全部靠注意力
維持**。將其宣告入 `feature.yaml` 之 `recon_assertions`，即每次 recon
自動比對。

本包指定宣告下列常數（其值皆為已量測且經交叉檢查者）：

| assertion 鍵 | 值 | 依據 |
|---|---|---|
| `functional_requirement_count` | **8** | 037 之 leaf 全集；recon 與自寫腳本兩側相符（上繳 09 §4 第 2 項） |

**只宣告這一項。** 其餘候選（`distinct_spec_sections`、
`spec_reference_stem`）不宣告，理由：本 feature 之 `sections` 為 0、
`citation_stems` 為空（`src_i` 被 `forbid` 排除，上繳 09 §4 第 15 項），
宣告一個必然為 0 之 assertion 只會製造一個不可能失敗之檢查
（canon §5a：不可能失敗之檢查項標「未實測」而非 PASS）。

**若 Q2 裁為選項 B 或 C，`functional_requirement_count` 之值可能改變** ——
屆時須改宣告值並記其理由，不得靜默更新。

---

## 四、裁決條文

```
R-G24（marker 衝突以較嚴者為準 —— 全域）
同一項於兩份決策文件中皆存在而 marker 不同時，**一律取較嚴者**，
不論該較嚴者在人側或機器側。

嚴格序：`[PEI]` > `[PROPOSED]` > `[AUTO]`。
（`[RULED]` 不在此序中：其為已凍結之項，不開放於簽核，
 與其他 marker 衝突時停並回報。）

理由：`[PROPOSED]` 未經修改即生效（canon §4），`[PEI]` 必須被回答。
取較嚴者之失敗形態是「多問了一個問題」，取較寬者之失敗形態是
「一個該被決定的事無聲通過」。兩者代價不對稱。

本條補 R-DM32 之未涵蓋向。R-DM32 規制「機器不得降格人所標之
`[PEI]`」與「機器所增之項不得自動升格」；本條規制**兩側皆有該項
而 marker 不同**之情形，且不問較嚴者在哪一側。

實例（上繳 11 §3）：`Test Set table (Part N)` 與
`profile [OVERRIDE] clauses` 兩項，`recon.py` 標 `[PEI]`，
分析層於 02 輪自行填 `[PROPOSED]`。二者依 `FEATURE_ONBOARDING`
本即 Tier 2，**機器是對的**。
```

```
R-DM36（已裁常數宣告入 recon_assertions）
本 feature 之已裁常數須宣告入 `feature.yaml` 之 `recon_assertions`，
使其於每次 `recon.py` 執行時被機器比對，而非靠注意力維持。

本輪宣告一項：
  functional_requirement_count: 8
（037 之 leaf 全集，recon 與自寫腳本兩側相符 —— 上繳 09 §4 第 2 項）

不宣告 `distinct_spec_sections` 與 `spec_reference_stem`：本 feature
之 `sections` 為 0、`citation_stems` 為空，宣告必然為 0 之 assertion
只會製造一個不可能失敗之檢查（canon §5a）。

`DECISIONS.md` 之 `ruled-constant assertions` 一項自
`[AUTO] 0 checked` 改為實際值，並記其宣告內容。

**Q2 若裁為選項 B 或 C 而 leaf 母體改變，須改宣告值並記其理由，
不得靜默更新** —— 靜默更新 assertion 等同取消該 assertion。
```

```
R-DM37（036 母本納入 reference: 綁定）
`feature.yaml` 之 `reference:` 節現綁 dbc_b／dbc_fd／lid／proxi 四項，
**036 母本不在其中** —— 其 sha256 僅存在於 `paths.workbook` 之註解，
不被 `verify_reference_binding.py` 檢查。

而 036 母本是**寫回之標的**：其欄位配置一旦改變，
`workbook.columns` 之 15 個鍵、B 欄公式（R-DM15）、Q 欄之版面判準
（R-DM34(a)）全部受影響。

處置：於 `reference:` 節增 `workbook_master` 一項，綁其檔名與 sha256，
納入檢查範圍。

一般化：**凡其變動會使既有產出失效之素材，皆應在 `reference:` 節內。**
判準不是「它是不是參考資料庫」，是「它變了以後我們的東西還對不對」。
```

---

## 五、作業步驟

1. 抄錄 §四三條（`R-G24` 入 `docs/fw036/RULINGS_LEDGER.md`；
   `R-DM36`／`R-DM37` 入 `features/display/RULINGS.md`），
   核對表由腳本產出。

2. **處置 §二之三項分歧**：
   - 補入 `ruled-constant assertions` 項
   - `Test Set table (Part N)` 與 `profile [OVERRIDE] clauses`
     改為 `[PEI]`，並於該兩項下加註其於 02 輪之原標記與更正依據
     （R-G24；不刪除原記錄，R-TM13）
   - 三項處置後**再跑一次複驗**，確認 recon 之 24 項全部有對應

3. **合併複驗之反向**（上繳 11 §6 第 2 項）：
   系統性比對「合併檔有而 recon 無」之項。
   逐項判其為「自測獨有且應保留」或「recon 漏測」，
   **後者若存在即為新發現，須登記**。

4. **依 R-DM36 宣告 `recon_assertions`**，重跑 `recon.py`，
   確認該 assertion 出現於 `RECON.md` 之 Assertions 節且為 PASS。
   **PASS 之意義須寫明**：它證明的是「037 之 leaf 數仍為 8」，
   不是「8 這個數字是對的」。

5. **依 R-DM37 將 036 母本納入 `reference:`**，重跑
   `verify_reference_binding.py`，五項逐項回報。

6. **`verify_reference_binding.py` 之串接**（上繳 11 §6 第 3 項）：
   於本 feature 自有之四支讀取素材腳本
   （`signal_resolution.py`／`dbc_probe.py`／`proxi_candidates.py`／
   `lid_version_diff.py`）之進入點呼叫該檢查，不符即非 0 退出。
   **此四支為 feature 自有腳本，本包授權修改；共用 `scripts/` 不動。**
   串接前後各跑一次，確認其產出之資料列數不變（R-G16 還原檢查）。

7. **`spec_text_layer.tsv` 之無聲改變**（上繳 11 §6 第 5 項）：
   於 sidecar 記入三個數字之**當期值**作為期望值，
   並於 `probe_spec_mode.py` 加一項比對：現算值與 sidecar 所記不符時
   **印出警示並列兩值**，不自行更新。
   （與 R-G23 同分寸：察覺變動，不代為採納。）

8. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用既有各條（1–29），另加：

30. 步驟 3 之反向比對若發現任一項為「recon 漏測」→ 登記並停手回報。
    那會是共用管線之缺陷，不在本 feature 可處置之範圍。
31. 步驟 6 之串接若使任一支腳本之產出列數改變 → 停並回報。
32. 步驟 4 之 assertion 若為 **FAIL** → 停並回報。
    `recon.py` 於 assertion 失敗時不寫 `DECISIONS.md`，
    此為其設計，不是故障。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/12_assertions.md`）

1. §四三條之抄錄核對表（腳本產出）
2. §二三項處置後之複驗結果（recon 24 項全部有對應之證明）
3. 反向比對之逐項判定
4. `recon_assertions` 宣告後之 `RECON.md` Assertions 節
5. `verify_reference_binding.py` 五項輸出
6. 串接後四支腳本之列數前後並列
7. `spec_text_layer.tsv` 期望值比對之實作與其警示分支測試
8. **「本包是否仍有該驗而未驗者」之獨立判斷**
9. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-G24 | marker 衝突取較嚴者，不問在哪一側 | 全域 | 是 |
| R-DM36 | 已裁常數宣告入 `recon_assertions` | Display | 是 |
| R-DM37 | 036 母本納入 `reference:`；綁定判準為「變了以後產出還對不對」 | Display | 是 |

三條皆為獨立單一事項。
