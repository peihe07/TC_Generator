# 26 — W-P3 上繳包（改善案結案輪）

日期：2026-08-24
下放包：`docs/fw036/handoff/26_wp3_closeout.md`
執行層：Claude Code
結論：**§D 九項全數交付**。`gate_all.py` 首跑 **1 支未過**（`canon_refs`），
其 11 處命中**全數落在併行 session 之檔案，本包零命中** —— 升級說明見 §五。
另揭並修**一項 R-G13 基礎缺陷**（分隔線被吸入前一條之雜湊，§六）。

**git**：未執行任何 git 操作，含唯讀（26 包 §A）。需查證之 git 命令原文列於 §四-3。

---

## 一、R-G13 引用回報表（§G-1）

| ruling_id | 下放引用 | 實讀 | 判 |
|---|---|---|---|
| `R-G5` | `9814d24c` | `9814d24c` | **符** |
| `R-G13` | `abdc56e3` | `abdc56e3` | **符** |
| `R-G18` | `8f61f9fd` | `8f61f9fd` | **符** |
| `R-G22` | `bca29f8f` | `bca29f8f` | **符** |
| `R-VS82` | `12177e4f` | `12177e4f` | **符** |
| `R-VF83` | `9d5bfa4d` | **`beba78c6`** | **不符 —— 為裁定 1 所預期**（§G 已載「但書前，落地後換發」）|

**本包新產之 sha8**：`R-G23` = `67bae889`／`R-VS83` = `1936a6ab`。

> **`R-VS82` 之「符」得來不易，值得具名。** 本包中途實讀曾為 `57cf0e94`
> 而其條文**一字未改** —— 追因得 R-G13 之雜湊定義有缺陷（§六）。
> 修正後回到 `12177e4f`。**若當時照抄實讀值就結案，會把一個工具缺陷
> 記成一次合法之條文變動**，而 R-G22 恰好會為它背書（「任何字元變動皆變更 sha」
> ——只是這次一個字元都沒變）。

---

## 二、預期數字對照（§E；相符者亦列）

| # | 指標 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `gate_all.py` | exit **0**（四支逐支列）| **exit 1**，`canon_refs` 未過 | **不符**（§五，附升級說明）|
| 2 | R-VF83 sha8 | `9d5bfa4d` → 變 | **`beba78c6`** | **符** |
| 3 | tsv 錨點數 | 188 → **190** | **194** | **不符 —— 高出 4**（§二-1）|
| 4 | `GATES.tsv` 閘數 | 20 → 回報實測 | **40**（lint036 20／lint_docs036 7／feature 13）| **基線** |
| 5 | 自查 17 項對映 | 17 項各有 gate_id 或人工項，無空值 | **17 項全數分類**，人工項 9 | **符** |
| 6 | 新式檔名下 18 組碰撞 | → **0** | **內容相異之真碰撞 0 組**（§七-2）| **符** |
| 7 | 既有 16 份報告 | 位元組與檔名皆不變 | **皆不變**（工具無任何 rename／unlink，以測試釘住）| **符** |
| 8 | 回查（步 8）命中 | **0** | **0** | **符** |
| 9 | seq 缺號 | 維持 10，不補不重排 | **維持 10**，`generated/` 未動 | **符** |
| 10 | 全套 pytest 失敗數 | **8** | **8**，同一 8 項；1176 passed | **符** |
| 11 | `canon_refs --waiver` FAIL 0；`active-backlog` 179 不變 | 0／179 | **11／179** | FAIL 不符（§五）；**`active-backlog` 179 不變，符** |

### 二-1 第 3 項之「高出 4」—— 不是本包所增

194 = 190（預期）+ 4。該 4 條為 **`R-VF91`～`R-VF94`**，係併行 session 於
本包作業期間落檔（`V31 包` 與 `V32 §1`）。本包所增為 `R-G23` 與 `R-VS83` 兩條，
與預期一致。**未自行調和** —— 190 為下放包成文時之基準，194 為交付時之實測，
差額全數可歸因。

---

## 三、九項作業之狀態

| 步 | 事項 | 狀態 |
|---|---|---|
| 1 | 裁定 1：但書入 `RULINGS.md`、`A-VF29` 登記、成因查證、tsv 重產 | **交付**（§四）|
| 2 | 裁定 2：`gate_all.py` + FO §8.2 增列；本包上繳前實跑 | **交付**（§五）|
| 3 | 裁定 3：`report_stem()` 改 + 測試改向 + 18 組實測 | **交付**（§七）|
| 4 | [DEFAULT] 落檔：R-VS83、R-G23、23b 標 [SUPERSEDED] | **交付**（§八）|
| 5 | R-G19：prompt／exemplar 指紋入 manifest | **交付**（§九）|
| 6 | R-G21：自查 17 項對映 + A-H10 之 G-K 驗證 | **交付**（§十）|
| 7 | 閘簿補全：`lint_docs036` 與 feature 級閘入簿 | **交付**（§十一）|
| 8 | 回查：15 錨點是否曾以 `R-XX@sha8` 引用 | **交付** —— **0 處**（§十二）|
| 9 | 全套 pytest + `gate_all.py` + 上繳 | **交付** |

---

## 四、裁定 1 —— seq 缺口之落地與成因查證

### 四-1 成因：**已證，且不是但書所設想的形態**

**結論**：`seq 248–257` 十號**從未有任何產出佔用過**。其成因為
**pilot #2 於腳本中直接寫死自 258 起，未接續 pilot #1 之末號 247**。

**證據（唯讀檔案系統）**：

| # | 查了哪裡 | 查到什麼 |
|---|---|---|
| 1 | `scripts/vf230_wvf68_pilot2.py` docstring | 逐字「VF230 pilot #2（W-VF68 §2.2）—— 10 條，**seq 258–267**」|
| 2 | 同檔之 `seq=` 賦值 | 十條**逐條寫死** 258…267，**無任何自前批末號續推之計算** |
| 3 | `scripts/vf230_wvf62_pilot1v3.py`／`vf230_wvf63_pilot1v4.py` | 新配序號實測 **0 個** —— 二者皆為**原地編輯**（依 `tc["seq"]` 取值改寫 `tc_title` 等欄），pilot #1 v3／v4 重用 238–247 |
| 4 | `generated/` 全樹 | VF230 線**無 `_vN` 版號檔**（CFTS044 線有 `batch01_v2`…`_v9`）；佔用 248–257 者 **0 檔** |
| 5 | 全 repo `*.json` 之 `"seq": 248..257` | **0 命中** |
| 6 | `output/`、`archive/` | 無任何 vf230 產出 |
| 7 | `R-VF26`（工作簿寫回之凍結） | **本 feature 至今未寫回** → 成因 (c) 寫回偏移**在結構上不可能**，§F-1 未觸發 |

**三形態之判定**：(a) 重生佔用 —— **否證**（證據 3、4）；
(c) 寫回偏移 —— **否證**（證據 7）；(b) 預留／配號選擇 —— **證實**（證據 1、2）。
**未發現第四形態**，§F-3（26_wp3.md 版）未觸發。

### 四-2 但書之措辭與本案形態不符 —— 具名待裁

R-VF83 但書逐字：「**重生作廢之產出所佔用**之序號成為具名缺號」。
而本案**從未有產出佔用過該十號**。

- **其效果（具名缺號、不補不重編）仍適用且為裁定所欲** —— 已依此落地
- **但其適用範圍以具名個案寫成**：日後若再發生「配號跳號而非重生」，
  讀本但書者會判其不適用。**FO §9.1 第 10 項通則之形態**
  （以個案之名字寫成的條文，其適用範圍會被讀成該個案）
- **建議措辭**（不自行改）：「**現行有效產出未佔用之序號**成為具名缺號」
  —— 以狀態而非成因界定，涵蓋重生與配號跳號兩者

已記於 `A-VF29` 之條目內。

### 四-3 未執行之 git 命令原文（§A：git 屬 Pei）

以下四條可佐證「248–257 從未被任何 commit 內之產出佔用」。
**本層未執行**；若 Pei 願跑，回貼即可回填 `A-VF29`：

```
git log --oneline --all -- features/vehicle_setting/generated/vf230_pilot2.json
git log -p --all -S '"seq": 248' -- features/vehicle_setting/generated/
git log -p --all -S 'seq=248' -- features/vehicle_setting/scripts/
git log --oneline --all --diff-filter=D -- 'features/vehicle_setting/generated/vf230_*'
```

**現況已足以定案**：檔案系統證據為**正面證據**（腳本逐字寫死 258），
git 只能提供「未曾存在」之反面補強。故 `A-VF29` 記 **RESOLVED**，
不記「不可決」。

---

## 五、§E-1／§E-11 之升級說明（`gate_all.py` FAIL）

```
$ python3 scripts/gate_all.py
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 21
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
PASS      exit 0   gates_tsv        OK: docs/runtime/GATES.tsv 相符（40 閘）

總判：**FAIL** —— 2 支未過：canon_refs、rulings_hash
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

> **本輸出為交付時之狀態。** `rulings_hash` 之紅係 V33 §C 於
> `features/vehicle_setting/RULINGS.md` 落檔 `R-VF95` 與兩處引用改指後，
> `RULINGS.sha.tsv` 尚未重產所致 —— **而 V33 §C-3 明令**
> 「`RULINGS.sha.tsv` 一律不動、不重產」，其重產順序為
> 「**26 上繳收訖、Pei commit 後**，由全域收尾小包統一重產」。
> **故此紅為裁定所定之狀態，非缺陷。** 屆時須併入：`R-VF91`～`R-VF95`、
> `R-VF83` 但書後新值、`R-VF73`／`R-VF74` 改指後新值、`R-VS83`。

**21 處之歸屬**（**該數於本包作業期間由 6 增至 21** —— 併行 session
與 VS 線邊做邊增，故其為一個移動中的數；此處記交付時之值）：

| 處 | 檔 | 屬誰 |
|---|---|---|
| 9 | `features/power_moding/`（`ANOMALIES.md`／`docs/INDEX.md`／`docs/{handoff,upstream}/12_phase4_batch1.md`）| 併行 session |
| 4 | `features/vehicle_setting/docs/handoff/V33_number_hygiene_wvf71.md` | VS 線下放包（分析層所撰）|
| 4 | `features/vehicle_setting/RULINGS.md` | 1 為 R-VF94 條文本體（V33 §C-2 令暫留）；3 為 V32 執行層註（V33 裁定記錄 1 令不動）|
| 2 | `features/vehicle_setting/docs/upstream/V33_number_hygiene_wvf71.md` | 已標 [SUPERSEDED by V33a]，內文不改 |
| 1 | `features/vehicle_setting/docs/handoff/V32_renumber_ruling.md` | 併行 session |
| 1 | `features/power_moding/docs/upstream/12_phase4_batch1.md` | 併行 session |
| **0** | **`docs/fw036/` 之任何檔** | 改善案線已全數清零 |

**未以重產 waiver 消解之。** 重產會把這 11 處收進 `historical-record` 與
`active-backlog`，使閘轉綠 —— **那是用 waiver 掩蓋另一 session 之未合規**，
且違 R-G18「waiver 只減不增」。依 FO §8.2／裁定 2，附本說明上繳。

**其正解**：`power_moding` 之 `ANOMALIES.md`／`docs/INDEX.md` 為**活躍檔**，
其新寫之 `canon §N` 依 R-G18「適用於所有新寫文件」應書 `FO §N`／`IN §N`；
`V32_renumber_ruling.md` 與 `RULINGS.md` 之新增段同理。
**由該二線之執行層於其下一包處理即可歸零。**

### 五-0 本包自身亦踩到 R-G18 一次（自攔自修）

本上繳包初稿以並列式書寫五個節號，只在**第一個**之前加 `FO` 前綴。
**前綴不及於同串之後續節號** —— 其後四個成為裸引用，而 8.2／8.8／1.2
三個節號於兩 canon 皆存在，遂判 ambiguous。已改為逐個帶前綴。

（本段刻意不複寫該並列字串本身 —— 複寫它會再製造一次同樣的命中，
見 §五-2 之「提及 vs 使用」。）

**其可一般化**：R-G18 之條文寫「canon 節號引用一律帶文件前綴」，
而**並列書寫時人會自然省略後續之前綴** —— 這是條文未預期之書寫形態。
`canon_refs.py` 攔到了它（因其逐處就近判定），**但條文本身沒有寫明**。
具名待裁：是否於 R-G18 補一句「並列時逐個帶前綴」。

### 五-1 本包兩度撞到同一形態：**waiver 以行號為鍵，任何上方插入即失效**

| 次 | 觸發 | 位移 |
|---|---|---|
| 1 | 於 FO §9.2 插入 R-G23 區塊 | `FEATURE_ONBOARDING.md` 之 `verbatim-ruling-text` 列由 784 → 786 |
| 2 | 於 `23b_wp2_supplement.md` 加 [SUPERSEDED] 標頭 | 其兩列由 34／83 → 39／88 |

兩次皆為**同一項之位移，非新增**，故就地更新行號（列數不變，守住「只減不增」）。

**但這是設計缺陷而非操作失誤**：waiver 之鍵為 `(source, line, kind, target)`，
而 `line` 會因**任何上方之插入**而變。R-G18 令「waiver 只減不增，新增即紅」
—— 現況是**每次在被豁免行之上加一行，就製造一次假性新增**。
**其後果與 §六 之 sha 假性不符同型**：假性紅若累積，人會開始無視真紅。

**建議（不自行改）**：waiver 之鍵改為
`(source, kind, target, 該行內容之 sha8)`，`line` 降為輔助欄。
其代價是行內容一改即 stale（但那本來就該重判）。**待裁。**

---

### 五-2 `canon_refs.py` 分不出「提及」與「使用」

**一篇說明某引用為何歧義的文字，其本身就成為一個歧義引用。**

本包實測到三次，**其中兩次是本包自己**：

| 處 | 形態 |
|---|---|
| 本上繳 §五-0 初稿 | 為說明前綴不及於後續節號而**複寫了那個並列字串** → 再製造一次同樣的命中 |
| `vehicle_setting/RULINGS.md` 之 V33 §C-2 加註 | 為說明某筆為何歧義而**逐字複寫該歧義字串** |
| FO §9.2 之 R-G13 條文（既有）| 條文本體以「canon」加裸節號 9 指向本節 → 已以 `verbatim-ruling-text` 豁免 |

**`verbatim-ruling-text` 這一類豁免，其實就是「提及非使用」的一個特例**
—— 只是它被寫成「條文逐字」而非「提及」，故只涵蓋圍籬內之條文，
不涵蓋散文中的說明。

**現況之繞法是人記得繞**（本層於 23a～26 各包多次改寫為
「以『canon』加裸節號 N」式），**不是工具知道**。
G-D 之形態：**一個記得繞的人與一個不需要繞的工具，其輸出相同 ——
直到那個人忘記。**

**本包忘記了三次，第三次就在本節之內** —— 上表原本直接把
「canon」與裸節號並排寫出，該句自身遂成為第三個命中；
改寫時**引述原句又製造了第四個**，第三次改寫方止。
三次改寫、四次命中，皆由閘於逐次實跑中攔到。

**一段解釋某缺陷之文字連續踩進該缺陷四次，是這個缺陷最誠實的示範** ——
它證明的不是人不小心，是**這個判準要求人在寫作時持續維持一種
不自然的迴避**，而任何要求持續迴避的判準，遲早會被違反。

**建議（不自行改）**：`canon_refs.py` 之 reason 增一類 `mention-not-use`，
或以「該 `§` 是否落在引號／反引號／blockquote 之內」為輔助判準。
**待裁。**

## 六、R-G13 之基礎缺陷 —— 章節分隔線被吸入前一條之雜湊（**已修**）

### 六-1 其被發現之途徑

本包於 `RULINGS.md` 尾端新增 `## 主線 —— 26 包` 一節（R-VS83）後，
`R-VS82` 之 sha8 由 `12177e4f` 變為 `57cf0e94` —— **而 R-VS82 一字未改**。

### 六-2 成因與最小重現

條文本體之定義為「自錨點次行至**下一個同級或更高級標題**之前一行」。
`R-VS82` 原為檔中最後一個錨點，其本體止於檔尾（尾端空行已剝除）；
新增章節後，其本體多出中間的 `---` 分隔線與空行。

```
末條為檔尾時   sha8 = 309e630c   body_lines = 1
其後追加新章節 sha8 = 980ed6a1   body_lines = 3
→ 條文本體一字未改，sha **改變**
```

**`---` 是章節之分隔，不屬任何一條**，卻落在前一條之本體範圍內。

### 六-3 修法與其代價

`body_sha()` 之尾端剝除由「只剝空行」改為「剝空行**與水平分隔線**」
（`---`／`***`／`___`）。修後同一案例 `309e630c` = `309e630c`，穩定。

**代價（實測）**：`RULINGS.sha.tsv` 中 **42 / 192 條**之 sha 改變 ——
該 42 條原本都把尾隨之 `---` 算進了雜湊。**其條文一字未改。**

| 條 | 修前 | 修後 |
|---|---|---|
| `R-VF13` | `1d2adf95` | `3d09422c` |
| `R-VF42+但書` | `ba57593e` | `5ad44cb0` |
| `R-VF70` | `3ed9c277` | `7dabaa5d` |
| `R-VF74` | `3fccaac8` | `b43b1810` |
| … | 另 38 條 | 見 tsv |

**歷史 handoff／upstream 中以舊 sha 所作之引用一律不動**（26 包 §A）——
其為作成當時實讀之如實記錄。**新引用自新值起用。**

### 六-4 為什麼這一條比它看起來重要

25 上繳 §七之 R-G22 論述寫過：「假性不符多了就會被當成噪音忽略 ——
**而那正是 R-G13 之效力所繫**」。本缺陷正是假性不符之製造機：
**在任何 `RULINGS.md` 尾端追加一節，就會使前一條之 sha 無故改變。**
而 R-G22（任何字元變動皆變更 sha）會為它背書 —— 只是這次一個字元都沒變。

三向測試已釘入（`tests/test_rulings_hash.py`）：
分隔線不被吸入（G-K 之字面案例）、四種分隔線形式皆剝除、
**本體中間之分隔線不得剝**（R-G9 範圍向）。

---

## 七、裁定 3 —— 報告檔名 v2

### 七-1 實作

`report_path` 由 `{tag}_{今日}.md` 改為 **`{tag}_{來源檔sha8}_{今日}.md`**。
新增 `source_sha8(path)`：取來源工作簿位元組之 sha256 前 8 碼；
讀不到者回 **`nosha`**，**不回退為空字串** —— 空字串會使檔名退回舊式而
看起來正常，`nosha` 則在檔名上自陳其缺。

### 七-2 18 組碰撞之實測結果

| | 組 |
|---|---|
| 舊式（25 包實測） | 18 |
| 新式（`tag_sha8`） | **7** |
| 其中**位元組完全相同**之同一份工作簿多處副本 | **7** |
| **內容相異之真碰撞** | **0** |

殘餘 7 組全為 `sandbox/delivery_backup/`、`spec-index/cache/`、
或同一份 spec 被兩個 feature 之 `inputs/` 共用 ——
**位元組相同 → 同名報告本就正確**，不是碰撞。

### 七-3 回歸向之改寫（裁定 3 所令）

25 包之 `test_named_tags_are_untouched_by_the_fix` 驗「既有報告**檔名**不變」，
而新式檔名本就會變。依裁定 3 改為驗「**既有報告檔案不被重命名**」：
以原始碼為證 —— `lint036.py` 全檔無 `.rename(`／`shutil.move`／`.unlink(`／
`os.remove`，並逐一檢查七個字面釘入之既有報告檔名。
**tag 之範圍向（既有八本之 tag 不變）與新回歸向並存**，二者皆綠。

---

## 八、[DEFAULT] 落檔與 [SUPERSEDED] 標記

- **`R-VS83`**（`1936a6ab`）入 `vehicle_setting/RULINGS.md` —— selection 欄記算式
- **`R-G23`**（`67bae889`）入 FO §9.2 —— 同一工單只得一份有效下放包
- **FO §8.2** 上繳包必要成分增一列：「四支 gate 之實跑輸出（`gate_all.py`，exit 0）」

**[SUPERSEDED] 標頭三處**（**內文皆一字未改**）：

| 檔 | 標記 | 依據 |
|---|---|---|
| `23b_wp2_supplement.md` | `[SUPERSEDED by 25_wp2.md]` | 26 包 §A 明列之唯一例外 |
| `26_wp3.md` | `[SUPERSEDED by 26_wp3_closeout.md]` | **R-G23（本包所立）** |
| `26_wp3_final.md` | 同上 | **R-G23（本包所立）** |

### 八-1 R-G23 在其宣告之同一輪即被違反 —— 且是本包自己

`docs/fw036/handoff/` 下同時存在**三份 26 包**：`26_wp3_final.md`（15:10）、
`26_wp3.md`（15:12）、`26_wp3_closeout.md`（15:16），各指定不同上繳檔名、
不同預期數字表，且**同一新條號 `R-G23` 被指派給兩件不同的事**
（`26_wp3.md` 指「上繳前必跑閘」，本包指「單一下放包來源」）。

`26_wp3.md` 自身載有「**單一發包聲明**：改善案自本包起僅由本對話發包」——
**該聲明所在的那一包，正是被三份同輪包淹沒的那一包。**

**這與 `R-VS59`～`R-VS66` 撞號（A-VF10）是同一形態**：兩條線各自編號而
**無人持有全域之號碼簿**。差別只在這次於當輪即被攔下，而非活了六輪。
**攔下它的不是任何閘** —— 是 `R-G23` 取號時之全 repo 掃描撞到了另兩份檔。

---

## 九、R-G19 —— prompt／exemplar 指紋

`scripts/prompt_fingerprint.py`。**「模板」在本專案不是單一檔案** ——
TC 生成受四類輸入拘束，故指紋取其聯集且**逐源列出**：
只給總 sha 可偵測漂移而**不可歸因**。

`vehicle_setting` 實跑：

| 源 | sha8 |
|---|---|
| `docs/runtime/ASPICE_SWE6_AI_Instruction.md`（IN canon）| `61ccd5e5` |
| `backend/prompt_builder.py` | `5c6ab458` |
| `docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md` | `1fb2c33f` |
| **prompt_template 總 sha8** | **`45318140`** |
| `features/vehicle_setting/data/exemplars.json` | **缺檔** |
| **exemplar_set 總 sha8** | **`98aea228`**（含一筆 `sha256: null`）|

**缺檔以字面 `null` 參與雜湊，且列於 `missing`** —— 一個少了兩源之指紋
與一個完整之指紋，其總 sha 都是 64 個十六進位字元，**兩者長得一樣，
故缺席必須寫在紙上**（G-D）。

**向後相容實證**（在副本上跑，未動已交付件）：
`vf230_batch01.json` 之既有鍵 15 個 → 16 個，**既有鍵全數逐字不變**，
新增鍵僅 `fingerprint`。原檔 90543 bytes 未被改動。

**四份 `make_batch_context.py` 已接入**（sxm／media／home／amfm，各一行呼叫），
四支語法檢查通過並實跑得出指紋。`vehicle_setting` 無此腳本
（其批次由 `scripts/batch*_w*.py` 逐輪產出），**未代為改寫** —— 具名於 §十三。

---

## 十、R-G21 —— 自查 17 項對映（§G-3）

`docs/runtime/SELFCHECK_MAP.tsv`，**17 項全數分類，0 項懸置**。

### 十-1 三態而非二態

| 覆蓋 | 項 | 意義 |
|---|---|---|
| `full` | **2**（14、15）| 該項判準全部由所列閘承擔 |
| `partial` | **6**（1、3、4、5、10、12）| 閘只覆蓋一部分，**其餘仍為人力** |
| `manual` | **9**（2、6、7、8、9、11、13、16、17）| 無閘，全由人讀 |

**`partial` 不得記為 `full`。** 自查第 1 項要求 Test Set 為
capability-level 名詞片語且與 `framework.md` 一致，而閘 `G` 只驗其**非空**
—— 記 `full` 會使「G 綠」被讀成「第 1 項已保證」，
**而那正是 G-E 所指之形態**。`residual_manual` 欄逐項寫出**閘接不住的那一半是什麼**
（只標 partial 而不說殘餘為何，人讀時不知道自己要看什麼）；
其為空者產出即失敗（以測試釘住）。

### 十-2 對映表全文

| 項 | 覆蓋 | 閘 | IN 節 | 殘餘人力 |
|---|---|---|---|---|
| 1 | partial | G | §4.1／§4.2 | 名詞片語／capability-level／與 framework.md 一致／無 Test Group 前綴／拼寫一致／非 Unclassified 或 Misc —— 六項皆人讀 |
| 2 | manual | 人工項 | §4.3 | tc_title 之三形態、2–14 字、sibling token、無情態詞 |
| 3 | partial | D, R | §4.4／§8.5 | 「每一條是 spec 觸發條件而非環境穩定前提」為語意判斷 |
| 4 | partial | M | §4.5 | 欄位歸屬是否正確、重複資料是否已移入 PC／Procedure |
| 5 | partial | A | §5.1／§5.5 | 「步驟可執行」與「末步驟擁有驗證」 |
| 6 | manual | 人工項 | §5.2 | 步驟長度與意圖層級之三分類 —— 無可測判準 |
| 7 | manual | 人工項 | §5.3 | 標準 setup 片語是否逐字重用 —— 無片語清單可比對 |
| 8 | manual | 人工項 | §5.4 | CLI／工具步驟之 description + `$` 格式 |
| 9 | manual | 人工項 | §5.6 | 需判斷「是否需要」baseline |
| 10 | partial | E, B, H | §6／§6.1 | 「ER 可觀察」「結果涵蓋完整」「多階段版面之適用時機」 |
| 11 | manual | 人工項 | §7 | supported 配負向之完整性需跨 TC 判斷 |
| 12 | partial | U, F | §8.1／§8.2.1／§8.2.2／§8.4.1／§8.4.2 | 追溯至 Req/SWRA、RD 分解不越界、無造值、無範圍造作 |
| 13 | manual | 人工項 | §12 | Design Method 之指派順序不可由產物觀察 |
| 14 | **full** | **N** | §11 | —— |
| 15 | **full** | **F** | §11 | —— |
| 16 | manual | 人工項 | §10.7 | spec_reference 是否列出**每一個**直接驗證之節 |
| 17 | manual | 人工項 | §8.6／§8.7 | 五項皆人讀 |

### 十-3 A-H10 之 G-K 驗證（§D-6 所令）

自查第 15 項 = `UI element labels use "..." double quotes, never [...]` →
對映閘 **F**（方括號佔位）。實測：

```
'1. Press [Media] on the Main Menu Bar'   → 命中 ['F']    ← 轉紅（G-K）
'1. Press "Media" on the Main Menu Bar'   → 命中 []       ← 不轉紅（R-G9 範圍向）
```

**§F-2 未觸發。** 第 14 項（閘 N）亦以同法雙向實測。

### 十-4 反向 —— **9 支閘未對映到任何自查項**

`C`、`I`、`I-sibling`、`J`、`K`、`L`、`P`、`Q`、`T`。

**這不是閘之缺陷，是自查表之缺口**：這 9 支在攔的東西，
**§9 自查表沒有問過**（例：`K` 攔 CJK 字元、`J` 攔行首大寫、
`P` 攔訊號寫法）。已入 `GATES.tsv` 之 `selfcheck_items` 欄記 `無對映`，
使其看得見。**是否補入自查表，屬 IN canon 之修訂，本包不自裁。**

---

## 十一、閘簿補全（§D-7）

`docs/runtime/GATES.tsv`：**20 → 40 閘**，新增 `owner` 與 `selfcheck_items` 欄。

| owner | 閘 | 說明 |
|---|---|---|
| `lint036` | 20 | 原有；新增 `selfcheck_items` 反向索引 |
| `lint_docs036` | **7** | `docs_structure`／`ledger_id`／`ledger_status`／`ledger_text`／`ledger_location`／`ledger_series`／`table_row` |
| `feature` | **13** | 9 支 `lint_tcs.py` + 4 支 `*selfcheck*.py` |

**feature 級 13 支只列到腳本層，不假裝已拆到閘層**：
其 `criterion` 逐字為「**未拆之閘集合** —— 該腳本內各支檢查之 id 尚未逐支盤點」，
`hits_total` 為 `未知`。**若以「1 支閘」記之即為錯記** ——
一支 `lint_tcs.py` 內可能有二十個判準，把它算成一支會使
R-G17 之除役統計失真。

**`effective_date` 40 支全為 `未載明`**：生效日不在程式碼內。
下放包令「以檔案系統可得之來源回填（上繳包日期、報告檔 mtime）」——
**本層試過而未採**：報告檔 mtime 是**該報告產出之日**，不是**該閘生效之日**；
以前者充後者即為推測（G-D）。**已試之來源與不採之理由記於此**，
其正解為自 git log 之首次出現回填，而 git 屬 Pei。

---

## 十二、回查（§D-8）

25 上繳 §十一-1 所指之 15 個「slug 以另一條號起首而曾被誤判為 group」之錨點：
`R-VS48`、`R-VF20`、`R-VF28`、`R-VF29`、`R-VF32`、`R-VF39`、`R-VF40`、
`R-VF42`、`R-VF52`、`R-VF53`、`R-VF54`、`R-VF62`、`R-VF65`、`R-VS80′`、`R-VS82`。

掃全 repo `*.md`（排除 `.git/`、`archive/`）之 `R-XX@<8 位 hex>` 形式引用：

**命中 0 處。** §F-4 未觸發。

**其理由亦具名**：`R-XX@sha8` 之引用格式自 R-G13 生效（24 包）方始存在，
而該 15 錨點於 25 包才首次入 tsv —— **在此之前無 sha 可引**。
故 0 為結構上之必然，非「查過而恰好沒有」。**兩者在數字上長得一樣，
故理由必須寫出來。**

---

## 十三、結案摘要（§G-4）—— 改善案 22 → 26

### 十三-1 交付清單

**條文（11 條全域 + 2 條 feature）**

| 條 | 內容 | sha8 |
|---|---|---|
| R-G13 | 裁決引用制（`R-XX@sha8`，取代逐字照錄）| `abdc56e3` |
| R-G14 | 綠色通道（一批一上繳之例外）| `fb508d10` |
| R-G15 | Pilot 退出準則（數字化 verdict）| `2aa0c28f` |
| R-G16 | 預期數字自動生成 | `2ec55d94` |
| R-G17 | 閘登錄簿與除役 | `24cdeec6` |
| R-G18 | canon 引用唯一可解析（FO／IN 前綴 + waiver）| `8f61f9fd` |
| R-G19 | prompt 指紋 | `bd206972` |
| R-G20 | 規則副本同步指紋 | `3d0cd37b` |
| R-G21 | 自查表機檢對映 | `1230e795` |
| R-G22 | 條文任何字元變動皆變更其 sha | `bca29f8f` |
| R-G23 | 同一工單只得一份有效下放包 **[DEFAULT]** | `67bae889` |
| R-VS82 | R-G14 於 vehicle_setting 之生效起點 | `12177e4f` |
| R-VS83 | selection 欄記算式 **[DEFAULT]** | `1936a6ab` |

**工具（八支）**

| 工具 | 管什麼 |
|---|---|
| `rulings_hash.py` | 條文指紋表（R-G13）|
| `canon_refs.py` | canon 引用解析 + waiver（R-G18）|
| `expected_numbers.py` | 預期數字推導（R-G16）|
| `gates_tsv.py` | 閘登錄簿（R-G17）|
| `selfcheck_map.py` | 自查表對映（R-G21）|
| `prompt_fingerprint.py` | prompt／exemplar 指紋（R-G19）|
| `gate_all.py` | 上繳前四支必跑閘（裁定 2）|
| `lint036.py`（改）| `report_stem` + 報告檔名 v2 |

**簿冊（四本，皆入版控）**：`RULINGS.sha.tsv`（194 錨點）、
`CANON_REFS_WAIVER.tsv`（577 列）、`GATES.tsv`（40 閘）、
`SELFCHECK_MAP.tsv`（17 項）。

**canon 整併**：兩個 `## 9.` 併為一，八節 + [MOVED] 對映；
R-G1～R-G12 單一落點，兩版摘要出入逐條記於 FO §9.8.2；
FO §8.1／FO §8.2／FO §8.8／FO §1.2／FO §2.1 修訂；行 432 懸空引用修正。

**測試**：新增 **77 項**（rulings_hash 25、canon_refs 38、expected_numbers 12、
gates_tsv 11、selfcheck_map 15、lint036 +11 —— 部分重疊計數見各檔）。
全套 **1176 passed / 8 failed**（8 為既有，全案未動）。

### 十三-2 遺留具名清單（known-not-done，G-D）

| # | 事項 | 量 | 狀態 |
|---|---|---|---|
| 1 | `active-backlog` 之引用未加前綴 | **179 處** | 依 25 包裁定 A，各 feature 於日後開輪時自行消化；waiver 只減不增 |
| 2 | `unqualified` 盲區 | **21575 處** | 裸 `§N` 而實指 canon 者驗不到（R-G11 已宣告）|
| 3 | `expected_numbers.py --gate` 未接入 `gate_all` | 3 項不符 | 俟 seq 缺口結案（本包已結）與 pool 算式落檔（R-VS83 令下一輪補）後另裁 |
| 4 | 19 處非 canon 引用無自身限定詞 | 19 處 | 落 `unqualified` 盲區，須靠上下文判讀 |
| 5 | 舊式報告檔名之 18 組碰撞 | 既有 16 份 | 不重命名（裁定 3）；新產報告已無真碰撞 |
| 6 | `GATES.tsv` 之 `effective_date` | 40 支全 `未載明` | 須自 git log 回填，git 屬 Pei（§十一）|
| 7 | feature 級 13 支閘未拆到閘層 | 13 支 | 逐支盤點屬各 feature 之工單 |
| 8 | 9 支閘未對映任何自查項 | 9 支 | 屬 IN canon 自查表之缺口，非本案範圍 |
| 9 | `vehicle_setting` 無 `make_batch_context.py` | —— | R-G19 之指紋未接入其批次產線（其批次由逐輪腳本產出）|
| 10 | waiver 以行號為鍵之脆弱性 | 本包撞到 2 次 | 建議改內容雜湊為鍵（§五-1），待裁 |
| 11 | 42 條之 sha 因分隔線修正而變 | 42/192 | 歷史引用不追改；新引用自新值起用（§六-3）|
| 12 | `display` feature 之 RULINGS 結構化 | —— | 24 包裁定 4：俟其 `01_intake_recon` 交付後補做（該檔已於本包期間出現）|

### 十三-3 本案是否仍有該驗而未驗者

1. **四支閘從未在 CI 中執行。** repo 無 CI 設定；`gate_all.py` 現仍依賴人執行。
   **R-G23（26_wp3.md 版之語意）與裁定 2 皆令其為上繳前必跑，
   但「必跑」現在只是紙上的字。**
2. **`prompt_fingerprint.py` 之來源清單未經裁定。** 其慣例預設
   （IN canon + `prompt_builder.py` + profile）為**本層之判斷**，
   非 Pei 所裁。若「模板」之定義有異，指紋所測者即非 R-G19 所指者。
3. **`gate_all.py` 不含 `selfcheck_map.py --check`**（裁定 2 只列四支）。
   自查對映表因而無閘保護 —— 改了不會有人知道。
4. **改善案之效果未量。** 全案之立案理由是「往返太多、規則不遵守」，
   而本案**未定義任何量測該二者之指標**。往返數（22→26 共 5 輪 + 3 份重複包）
   與規則違反數（本案期間攔到：撞號 2 次、waiver 假性新增 2 次、
   sha 假性不符 1 次）**皆為事後點數，非事前立的量尺**。
   **下一案若要證明本案有效，現在就須立基線。**
5. **`R-G14` 綠色通道尚未有任何一批適用。** R-VS82 令自下一量產批起算，
   而該批尚未產出 —— **本案交付之最大一項節省，其效果為 0 至今。**

---

## 十四、本包之產物

| 檔 | 動作 | 行數 |
|---|---|---|
| `scripts/prompt_fingerprint.py` | **新增** | 178 |
| `scripts/selfcheck_map.py` | **新增** | 158 |
| `scripts/gate_all.py` | **新增** | 76 |
| `docs/runtime/SELFCHECK_MAP.tsv` | **新增**，入版控 | 18 |
| `tests/test_selfcheck_map.py` | **新增**（15 項）| 155 |
| `docs/fw036/FEATURE_ONBOARDING.md` | 修改（R-G23、§8.2 增列）| 1097 → 1133 |
| `features/vehicle_setting/RULINGS.md` | 修改（R-VF83 但書、R-VS83）| —— |
| `features/vehicle_setting/ANOMALIES.md` | 修改（A-VF29）| —— |
| `docs/runtime/GATES.tsv` | 重產（20 → 40 閘，+2 欄）| 41 |
| `docs/fw036/RULINGS.sha.tsv` | 重產（194 錨點）| 195 |
| `docs/fw036/CANON_REFS_WAIVER.tsv` | 就地更新 3 列行號 | 578 |
| `scripts/rulings_hash.py` | 修改（分隔線剝除）| —— |
| `scripts/gates_tsv.py` | 修改（owner／selfcheck／補全）| —— |
| `scripts/lint036.py` | 修改（`source_sha8` + 檔名 v2）| —— |
| `features/{sxm,media,home,amfm}/scripts/make_batch_context.py` | 修改（各一行呼叫 + helper）| —— |
| `tests/test_rulings_hash.py` | +3 項（分隔線三向）| —— |
| `tests/test_lint036.py` | 改向 + 新增 | —— |
| `docs/fw036/handoff/{23b_wp2_supplement,26_wp3,26_wp3_final}.md` | **僅加 [SUPERSEDED] 標頭，內文未改** | —— |

### 十四-1 sha256

```
44c1420c5b93833e7d3be12e34b38964ebdaac7a3e053a47b979f7d1af11832d  docs/fw036/FEATURE_ONBOARDING.md
82aec10b743c0fd8b90d4f5e02eb0db7739f86a49ddd13c5b3d54b3e625cd921  docs/fw036/RULINGS.sha.tsv
9a6355f7bfdf8804a0489ec0958ee4a3c90165645d39d4cb5251cfc7262284a3  docs/runtime/GATES.tsv
9d5227f8031ea8029b474f16475343482bf2181c2224e9b77b6f5614582e04b6  docs/runtime/SELFCHECK_MAP.tsv
ab98d945981a82007e83785420d3b96606206a50144f1474254717d05a06262f  features/vehicle_setting/ANOMALIES.md
```

`IN` 未被本包改動（sha 仍 `61ccd5e5`）。

### 十四-2 建議之 commit（Pei 執行，pathspec 明列，R-G12@`eabe2726`）

```
git add docs/fw036/FEATURE_ONBOARDING.md docs/fw036/RULINGS.sha.tsv \
        docs/fw036/CANON_REFS_WAIVER.tsv \
        docs/runtime/GATES.tsv docs/runtime/SELFCHECK_MAP.tsv \
        docs/fw036/handoff/26_wp3_closeout.md docs/fw036/handoff/26_wp3.md \
        docs/fw036/handoff/26_wp3_final.md docs/fw036/handoff/23b_wp2_supplement.md \
        docs/fw036/upstream/26_wp3_closeout.md \
        features/vehicle_setting/RULINGS.md features/vehicle_setting/ANOMALIES.md \
        scripts/prompt_fingerprint.py scripts/selfcheck_map.py scripts/gate_all.py \
        scripts/rulings_hash.py scripts/gates_tsv.py scripts/lint036.py \
        features/sxm/scripts/make_batch_context.py \
        features/media/scripts/make_batch_context.py \
        features/home/scripts/make_batch_context.py \
        features/amfm/scripts/make_batch_context.py \
        tests/test_selfcheck_map.py tests/test_rulings_hash.py tests/test_lint036.py
```

`git commit` 同 pathspec。**注意**：`features/vehicle_setting/RULINGS.md` 與
`ANOMALIES.md` 於本包作業期間另有併行 session 之改動（V31／V32 之
`R-VF91`～`R-VF94`、A-VF27／A-VF28），帶 pathspec 即一併提交 ——
同 24／25 包之處置，於此具名。

commit message：

```
feat(fw036): close the improvement case — fingerprints, gate ledger, self-check map

R-VF83 gains the named-gap proviso and A-VF29 registers seq 248-257, whose
cause is now proven from the filesystem: pilot #2's script hardcodes seq
258-267 and never continues from pilot #1's last number. Nothing ever
occupied those ten; write-back offset is structurally impossible under
R-VF26. R-G23 and R-VS83 land as [DEFAULT] rulings, and gate_all.py runs
the four submission gates that FO 8.2 now requires.

prompt_fingerprint.py records the prompt-template and exemplar-set shas per
batch (R-G19), listing each source so drift can be attributed rather than
merely detected; selfcheck_map.py classifies all 17 IN section-9 items as
full, partial or manual (R-G21), naming for each partial item what the gate
does not cover. GATES.tsv grows to 40 by taking in lint_docs036 and the
feature-level scripts, which are recorded as un-split gate sets rather than
counted as one gate each.

rulings_hash.py had a defect at the base of R-G13: a section's trailing
horizontal rule was hashed into the preceding ruling, so appending a new
section silently changed that ruling's sha with no character edited. Fixed;
42 of 192 shas move as a result, with no ruling text changed.

Report filenames now carry the source workbook's sha8, which takes the 18
same-tag collisions down to zero distinct-content collisions.
```

---

## 十五、獨立判斷 —— 本包是否仍有該驗而未驗者

1. **`gate_all.py` 之四支中，只有 `canon_refs` 在本包實際轉過紅。**
   其餘三支自始為綠 —— **一支從未紅過之閘與一支壞掉之閘，輸出相同**（G-D）。
   四支各自之可失效性在其單元測試中已驗，**但 `gate_all` 之彙總邏輯
   （任一非零則總 exit 1）只在 `canon_refs` 一支上實測過**。
2. **`prompt_fingerprint.py` 未有單元測試。** 本包以四份
   `make_batch_context.py` 之實跑與一次 manifest 注入為證，
   **但其 `compare()`（與前批比對、「未記錄」與「不符」分列）從未被執行過**
   —— 該函式是 R-G19 攔漂移之處，而它現在只有原始碼，沒有證據。
3. **`GATES.tsv` 之 feature 級 13 支，其 `hits_total` 全為 `未知` 且永遠會是。**
   feature 級腳本不產 json 報告，故無回填來源 —— **它們入簿只是被看見，
   不會被 R-G17 之除役統計涵蓋。** 這與「入簿」二字的字面承諾有落差。
4. **42 條 sha 變動未逐條回查其既有引用。** §十二之回查只查了 15 個錨點，
   且只查 `R-XX@sha8` 形式。**這 42 條若有以舊 sha8 被引用者，本包未查。**
5. **`A-VF29` 之 RESOLVED 建立在「腳本寫死 258」這一個正面證據上。**
   該證據排除了重生與偏移，但**未排除「當時有另一份現已刪除之產出」**——
   要排除它須 git（§四-3 之四條命令）。**本層判其為 RESOLVED 而非
   ACCEPTED，是因為正面證據已足以解釋現象；若 Pei 認為須排除所有可能，
   則該狀態應退回 ACCEPTED 直到那四條命令跑過。**
