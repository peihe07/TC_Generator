# 上繳包 22 —— Vehicle Category：sentence_index ＋ 第 4 批勘查（T118–T120）

- 日期：2026-08-26
- 對應下放：`docs/handoff/22_batch4_survey.md`
  （SHA256 `c271cc8e5d4862f8805adb962ef8e99ecb9cb5743748df68a4ba407ccc318684`，163 行）
- **結論：T118／T119 完成，T120 部分完成（一筆待裁）。勘查完成，未生成任何 TC。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T118 | 第 4 批勘查 a–g | ✅ **§3.1 之矛盾已解 —— 不是矛盾** |
| T119 | `sentence_index` ＋ 句級驗證 | ✅ self-test 增為**五個**斷言，新增之錯句斷言 PASS |
| T120 | 列冊 → CONT | ⚠️ `038-02` 已登記；**`038-03` 撞到 R-3，待裁** |

**三件請你先看**：
1. **§3.1 之「表面矛盾」不是矛盾，是進入路徑不同** —— 且其解法直接
   決定 `034-02` 之 TC 怎麼寫。見 §2。
2. **`038-03` 之登記範圍撞到 R-3 之 50 token 上限** —— 連續三句 54、
   非連續二句 42。二者各有代價，未自裁。見 §4.2。
3. **`038-04` 是第一層又一個偽陰性** —— `The user is **then** taken back…`
   之 `then` 承接前句，但非代名詞起首故未被偵測。見 §6。

---

## 1. T119 —— 句級驗證

CONT 表增 `sentence_index` 欄；句序由程式硬推改為表中登記。

```
self-test 1  第一層(b) 已知標的 019-02 應為候選        PASS
self-test 2  第一層(a) 反向 017 不應為候選              PASS
self-test 3  第二層(b) 第 1 批四筆登記應全過            PASS  不符=[]
self-test 4  第二層(a) 反向 012-03→§2.5 應 FAIL         PASS
self-test 5  第二層(a) 反向 013-02→§2.6.3 **s1** 應 FAIL PASS   ← 新增
```

**斷言 5 是句級細化之驗收** —— 節對而句序錯，節級時抓不到，句級抓得到。
`sentence_index` 之正確性至此有機器承載者，硬推之「無檢查」缺口關閉。

第 16 項亦改讀 `sentence_index`（不再由節號推），**並支援範圍**
（下放包 §二明文「reference 型：登記為範圍或 `*`」）。
四批回歸全綠：**pilot／第 1／第 2／第 3 批皆 20 checked / 0 failed。**

---

## 2. T118(b) §3.1 —— **不是矛盾，是進入路徑不同**

### 2.1 SYS1 二節逐字

```
§11.1  STN2.) Settings not contained within a specific vehicle will not be
       displayed in that vehicles Settings list. If a setting is available to
       the vehicle but not when key-off, they will appear grey when the system
       is in key-off.

§13.1  SBIS1.) The Settings tab is unavailable while the vehicle is in Key Off,
       Timed Mode or ACC.
```

### 2.2 解 —— 章 13 之其餘各節即答案

```
§13.2  SBIS2.) The user is able to access Phone settings through the Phone
       screens. Phone settings are available while the vehicle is in Key Off or ACC.
§13.3  SBIS3.) … access Audio settings through the Media. Audio settings are
       available while the vehicle is in Key Off or ACC.
§13.4  SBIS5.) Software Updates are available while the vehicle is in Key Off or ACC.
§13.5  SBIS4.) If Settings **tab or a Settings category** is opened which is not
       available in Key Off … show pop-up …
```

**§13.1 擋的是「Settings 頁籤」這一條進入路徑，不是所有設定清單。**
Phone settings 走 Phone screens、Audio settings 走 Media screens、
Software Updates 另有其路 —— 三者於 Key Off／ACC **明文可用**。

**§11.1 之灰化，治的是「已經進得去的那些清單」裡的項目。**
二者標的不同層：一個管入口、一個管入口之後的呈現。

**§13.5 之措辭是旁證**：`Settings tab **or a Settings category**` ——
明文承認 category 可獨立於 tab 被開啟。

### 2.3 對 `034-02` 之生成拘束（本項之實益）

`034-02` 之 TC **不得以 Settings 頁籤為進入路徑** —— 那條路在 key-off
下被 §13.1 擋住，該 TC 將不可執行。其 Pre-Condition／Procedure 須經
**§13.2–13.4 所載之可用路徑**（Phone screens／Media／Software Updates）
進入一個於 key-off 仍可達之設定清單，再驗其中不可用項之灰化。

**三候選解之判定**：(a) 部分成立（非「不同狀態」而是**不同路徑**）；
(b) 不成立（`unavailable` 無範圍細分，是整個 tab）；
(c) **不成立 —— 規格自身無衝突，不需 DR**。

> 本項同時釐清第 5 批之狀態定義：`057`（tab 不可用）與
> `059-02`／`060-02`／`061`（他路徑可用）**本就並存不悖**，
> 生成時不需視為例外。

---

## 3. T118(a)(c)(e) —— 基本盤

15 leaf，priority **P0 2 ／ P1 4 ／ P2 5 ／ P3 4**。

- **(c) 素材**：15 筆**全部僅需 037／SYS1 文字層**，無外部素材、
  **無 PENDING 需求**。
- **(e) 記法**：直單 7 leaf、彎單 3 leaf、彎雙 1 leaf。
  **`035-02`／`036-01`／`038-01` 三筆二欄記法不對稱**
  （Description 彎單 `‘…’`／Title 直單 `'…'`）—— 同 A-VC10 第三面，
  取材時二欄不得混用。
- **Title 越界（R-VC24）**：本批**候選 0 筆**。

---

## 4. T120 —— 列冊之判定

### 4.1 `038-02` —— 已登記（範圍 `1-2`）

SYS1 §11.5 為**六句**，與五個 leaf 之對應為
s1→`038-01`、s2→`038-02`、s3→`038-03`、s4→`038-04`、**s5+s6→`038-05`**。

`038-02` 之 `It` 先行詞（pop-up）在 s1 → 登記 `11.5` / `1-2`，
**33 token，未逾 R-3 之 50**。第二層句級驗證通過（CONT 表現 6 條，不符 0）。

### 4.2 ⚠ `038-03` —— 撞到 R-3，維持列冊待裁

其 `This pop-up` 之先行詞亦在 s1，但 s1 與 s3 之間隔著 s2：

| 取法 | token | 判 |
|---|---|---|
| 連續 `1-3` | **54** | **逾 R-3 之 50** |
| 非連續 `1,3` | 42 | 未逾，但**破壞 verbatim 之連續性** |
| 單句 `3` | 21 | 未逾，但 `This pop-up` 之指涉無解 |

**三者各有代價，未自裁。** 我的傾向是**單句 `3`** ——
理由：其 Pre-Condition 可載明「語言變更彈窗已顯示」，
使 `This pop-up` 於 TC 之脈絡內可解；而 CONT 之目的是讓**上半可讀**，
不是讓上半自足。但這會使 CONT 對該筆形同不適用，
**等於承認指涉型有一類靠 Pre-Condition 而非靠取整段來解** ——
那是對 CONT 收錄判準之擴充，屬 Tier 2。

`cont_deferred.tsv` 之該筆理由已改寫為此，未移轉。

---

## 5. T118(f)(g) —— 拆分與預估

### 5.1 `038-05` 確認拆 2

其 Description **含 s5＋s6 二句**（43 token），且 s5 自身即二個 if 分支：

```
If the voice commands are complete the screen will be shown as normal,
if not complete the current language is shown checked while the rest will be
greyed out. They will remain greyed out until the system has completed…
```

§8.3 壓測：「完成 → 正常畫面」與「未完成 → 灰化且持續」為**二個獨立失效**，
單一 TC 判準不明；且 IN §5.2 禁一 TC 內寫條件分支。**拆 2**。

### 5.2 其餘不拆

`035-*`／`036-*`／`037-*`／`038-01`~`-04`／`039` 逐筆壓測後皆為單一規則。

**`037-01`／`037-02` 之區分採認下放包 §3.4**：`-01` 為規則（同時僅一）、
`-02` 為行為（開一關餘），**一靜一動**；括號下半以此區分。
其 ER 之互斥驗證**須含 baseline**（§5.6）—— 先記錄現態，開新者後驗餘者 off。

### 5.3 預估

**15 leaf → 16 TC**（`038-05` +1）。`split_delta: 1`。
**a 段 15 筆、b 段 0 筆、PENDING 0 筆。**

### 5.4 二筆 P0 之生成拘束（下放包 §3.5）

`035-03`／`036-02` 之 ER **必含 baseline**：先記錄設定現值 → Cancel →
驗值未變。**「未變」無 baseline 即不可判。**

`036-01`（R-VC14 改判 P1）之 `reasoning` 須載 R-VC14(b) 之分歧揭露
（執行失效非 data-loss；隱私外洩風險記於 reasoning 而**不入 priority**）。

### 5.5 R-VC25 例外路徑之首次動用

`035-03`／`036-02` 之 Description **逐字相同**
（`Selecting cancel will take the user back to the previous screen.`），
而其 P0 判定之依據（`without changing any settings`／
`without clearing any data`）**只在 Title**。

**二筆應取 Title**，三件已備：
(a) 理由 —— Title 載有 Description 未載而為本 TC 驗證標的之條件（A-VC10 第一面）；
(b) R-VC24 判別 —— 二筆 Title 之謂語為 `returns the user…`（本 leaf 行為），
其 `restore-defaults prompt`／`clear-personal-data prompt` 為**情境脈絡**，
**非行為主張**；(c) 由 (b) 滿足。

**收斂時第 7b 項之取材分布將首次出現 `Title` 非零**，須逐筆檢其三件。

---

## 6. ⚠ 第一層之又一偽陰性：`038-04`

```
037 038-04: The user is then taken back to the language settings screen.
```

**`then` 承接 s3 之「使用者按 X 或系統完成」** —— 其時序指涉前句，
但**非代名詞起首、首字大寫、60 字元**（`short` 已移出候選）——
**二特徵皆不命中，第一層看不到。**

與 `013-02` 同型（該筆是「037 補句號」而未命中）。**已知偽陰性之第二個實例。**

**未自行登記** —— 其是否需 CONT 取決於「`then` 之指涉是否影響上半可讀」，
與 `038-03` 同屬 §4.2 之待裁範圍（靠 Pre-Condition 或靠取整段）。
建議二筆一併裁。

**本層仍為底網**：`038-02`／`038-03` 由特徵命中，`038-04` 由勘查 (d)
之 SYS1 對照發現 —— 分工與 20a §2.3 所述一致。

---

## 7. 待你裁

1. **`038-03`／`038-04` 之 CONT 處置**（§4.2／§6）——
   取整段 vs 靠 Pre-Condition 解指涉。後者需擴充 CONT 收錄判準。
2. **第 4 批之生成授權**：15 leaf → 16 TC，`split_delta: 1`，
   無 b 段、無 PENDING。
3. 同批 A（六項）、DR-VC3、DR-VC9(一)（Tier 3）。

---

## 8. 量測條件揭露（R-G8）

### §2 之交叉比對

以 SYS1 §11.1／§13.1–13.5 之**全文**為據，非摘句。
**其結論為「規格自身無衝突」，屬否定性判斷** ——
其強度限於所讀之五節；若章 13 另有節（§13.1.1 已讀，含彈窗行為）
或他章另有相關條款而未讀到，結論可能改變。**已讀範圍已列明。**

### `sentence_index` 之句子切分

沿用 `(?<=\.)\s+(?=[A-Z])`。§11.5 之 s1 結尾為 `…process…’ .`
（**省略號＋引號＋空格＋句點**）—— 切分正確，但**該形態脆弱**：
若他節出現 `e.g.` 之類縮寫，會被誤切而使 `sentence_index` 指錯。
**本批四節無此形態，實害為零**（沿上繳包 16 §9 之既知揭露）。

### token 計數

以空白切分計詞，**非 R-3 所定義之 token 化方式**（該定義未見於 canon）。
故 §4.2 之 54／42／21 為**近似值** —— 若 R-3 之 token 另有定義
（如含標點），`1-3` 之 54 可能更高或更低，但**其與 `1,3` 之相對大小不變**。
