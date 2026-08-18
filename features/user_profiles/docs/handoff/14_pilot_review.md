# 14 下放包 — pilot 覆核結果與修正（canon §1.2）

**本包無裁決條文。** 以下為分析層之 pilot 覆核判定
（發現之分類與作業指示屬分析層自裁），不佔 Pei 之裁定。
唯一送 Pei 者為 `052f67d`（(a) 類不可逆），另行處理。

13 輪上繳包**核可**：p17 四步紅過才綠、R-U52 兩向 tamper、
`052f67d` 之三案重述與兩處記載更正，皆成立。
16 條 TC 之**形狀**無違規；以下為**內容**之覆核 —— lint 驗形狀，
不驗「這句 ER 是不是那條 spec 說的」。

## 分類（canon §1.2）：defect 5／style-divergence 1／note 3

### D-1（阻塞）TC-002 之 priority 違反 R-U5

`PROF-002-03` 為 **Restore Settings to Default**（回復原廠）之分支，
標 `P2 — 037 先驗 Low`。

R-U5 逐字：「上調至 P0 僅限符合 §10.2 P0 條件者（…資料遺失風險）——
**本 feature 之 Clear Personal Data／刪除全部 profile／回復原廠
（5.13.x）屬資料遺失風險，為 P0 候選**」，且「037 之 High/Medium/Low
僅為先驗，**衝突時以 TEST_CASE_PRIORITY.md 為準**」。

以 037 先驗覆蓋 rubric，方向與 R-U5 相反。**改 P0**，
並於 reasoning 具名 §10.2 依據。
連帶：全批以「037 先驗」作 priority 理由者逐條複核，
凡落在 R-U5 核心五類內者一律改判。

### D-2（阻塞）TC-004 不可執行 —— 受測偏好未指名

`PROF-032` 之步驟 2：「Change a Profile-linked preference」——
**哪一項未指名**，而 `input_test_data` 為 `NA`。
同批之 TC-001 指名了 3.1／3.2／3.4 三項，**同一份 PLP 表，兩種待遇**。

測試者無法據此執行；§2「no vague wording」、§4.5 之獨立資料集應入
`input_test_data`。**指名至少一項具體偏好**（取自 PLP 表逐字，不自擬）。

### D-3（阻塞，2 條）ER 以 spec 表號／註記號指代內容

- TC-013 ER2：「…and **the list items of Table CPA2**」
- TC-003 ER3：「…the icon and the string **described in note PRACC7.2**…」

測試者讀 ER 無從得知該檢查什麼，須回查 spec —— §6 要求
「observable, judgeable」。

`must_carry` 之存在理由正是把這些列項帶進來（R-U35(b)、p17 → 11.5、
p14 → 9.1）。13 輪 §5.3 第 6 項判「must_carry 之效力為強制入 prompt
context，非強制入 ER」——**該判斷本身成立**，但結論不成立：
不是 must_carry 強制它入 ER，是 §6 要求 ER 可觀察。

**改**：ER 列出該表之實際列項（來源為 must_carry 之 PDF 原文，逐字，
不改寫）。若列項過多，以 §6.1 之 `a./b./c.` 子層列出。

### D-4（不阻塞，第一批前修）lint 缺 §5.2 之步驟長度閘

14 閘中無步驟長度檢查，故以下未被攔下：

- TC-010 步驟 3：`Switch the ignition off and on, then open the Profile
  List and check that the Profile carrying the username and avatar from
  steps 1 and 2 is listed` —— **約 29 詞**（§5.2 B 上限 18）
- TC-011 步驟 3：**約 21 詞**
- TC-013 步驟 2：**約 19 詞**（邊界）

補閘：normal ≤12、final ≤18、§5.1 例外之 intent 步驟 ≤18。
**補閘後須先紅再綠**（同 R-U49 之順序），並含範圍向（R-G9）：
證明它對 12 詞之正常步驟不轉紅。

### D-5（不阻塞）`feature.yaml` 之 popup_ids 20 vs 現測 21

13 輪處置為「lint 改現測、`feature.yaml` 不動」。
不動之理由（它是有量測條件的紀錄）成立，惟結果是**兩個數並存而無指引**。

**改**：`feature.yaml` 更新為 21 並標其量測條件為 `pdf_text`；
原 20 之記載移入註記欄並保留其當時之量測條件。
依 R-U25：判讀基準為 PDF 側，`feature.yaml` 應與基準一致。

### S-1（style-divergence，不阻塞）PU id 記法不一致

TC-002 同一條內並存 `PU_0118` 與 `PU1087`／`PU1088`。
若二者皆為 spec 原文，依 §11 profile 例外得保留；
**惟須具名確認其各自之來源列**，不得為抽取造成之變體。
確認後若同源而寫法不同，統一之。

### N-1 `variant_of()` 不處理否定 —— 本輪修

TC-013 之 pre-condition 為「**not** an R1 High variant」卻被判為 R1 High。
本批無害（該 TC 未含禁用字串），但它是潛在誤報源，
而**誤報之規則終將被關掉**（R-G9 之立條理由）。修，並加對照向。

### N-2 `p17 → 11.5` 未經 PDF 複位

該值來自 R-U49 之裁定，非來自對 PDF p17 之重新定位；
且第 7 項自檢驗「有歸宿」不驗「歸宿正確」（p17 誤填 9.1 仍會綠）。
**對 p14／p17 各做一次 PDF 複位驗證**，並將「歸宿正確」納入該自檢。

### N-3 `/tmp/sample.json` 仍為 `--selfcheck` 之讀取對象

依 13 輪 §7 第 6 項之建議，落為 `data/pilot_sample.tsv`。

## 作業

1. D-1～D-3 修正（阻塞項），逐條回報修正前後之欄位全文
2. D-4 補閘：**先紅、再修、後綠**，四步輸出皆附；含範圍向
3. D-5、S-1、N-1、N-2、N-3 處置
4. 全批 16 條之 priority 依 R-U5 複核（不只 TC-002）
5. 重跑全部 lint 與 `--selfcheck`，貼輸出
6. `PROF-111` 之 R1 High 反面（§7 負向配對）**列入第一批正式批次之取樣**，
   本輪不生成

## 不在本包授權範圍

- 任何 git 操作（R-G5）；`052f67d` 屬 Pei
- 寫回工作簿（R-U14）
- 開第一批正式批次 —— 待本包覆核

## 上繳

`docs/upstream/14_pilot_fixes.md`，更新 `docs/INDEX.md`，附獨立判斷。
