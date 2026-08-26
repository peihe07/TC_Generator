# 下放包 23 —— Vehicle Category：CONT 第三處置類 ＋ 第 4 批生成授權

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/23_batch4_tc.md`
- 前一包：`docs/handoff/22_batch4_survey.md`
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `22_`，無碰撞。
- **本包授權生成第 4 批 16 筆。不授權寫回工作簿。**

---

## 一、上繳包 22 之覆核

**核可。** 三項具名：

1. **§2 之交叉比對解得漂亮**：三候選逐一判定（(a) 部分成立且更正為
   「路徑」非「狀態」、(b)(c) 不成立），以 §13.5 之
   `tab **or a Settings category**` 為旁證 —— 措辭級的證據。
   且 §8 誠實標其為否定性判斷、列明已讀範圍。**規格自身無衝突，
   不發 DR** —— 免掉一輪空往返，並提前解了第 5 批的狀態定義。
2. **`038-04` 為第一層偽陰性之第二實例**（`then` 承接、二特徵不命中），
   且你們正確地把它與 `038-03` 綁成同一個待裁 —— 二筆確為同一問題。
3. **斷言 5（節對句錯應 FAIL）PASS** —— 句級細化之驗收乾淨。

## 二、`038-03`／`038-04`：裁**結構解**，CONT 增第三處置類

### 2.1 關鍵觀察 —— 該狀態不是為解指涉而加的

`038-03` 之驗證標的是「彈窗**持續顯示**直到完成或按 X」——
其 Pre-Condition **本來就必須**建立「語言變更彈窗已顯示」，
那是驗證持續性之前提，**不是為了讓 `This pop-up` 可解而額外加的**。

`038-04` 同理：其驗證標的是「返回語言設定畫面」，
其 Procedure **必然含**「按 X 關閉彈窗（或等系統完成）」——
`then` 之時序由步驟天然承載。

**二筆之指涉，其先行詞恰為該 TC 結構必然建立之狀態。**
取整段是把 TC 已有的資訊再抄一遍進上半 —— `038-03` 為此撞上 R-3，
付出的代價買的是冗餘。

### 2.2 裁定

```
CONT 收錄判準之擴充 —— 第三處置類 `resolved-by-structure`：

指涉型 leaf，其指涉之先行詞**即為該 TC 之 Pre-Condition 或
Procedure 所必然建立之狀態**（即：不解指涉，該 TC 也必須建立它）者，
得以**單句**為上半，指涉由 TC 結構承載。

層次（依序適用，不得跳層）：
  1. 預設 —— 取含先行詞之整段（既有處置）
  2. 整段逾 R-3 之 50 token，**或**先行詞為結構必然狀態 →
     得採 `resolved-by-structure`：單句上半 ＋ CONT 登記
     `resolution`（`PC` 或 `Step-n`）與 `resolution_key`
     （先行詞之關鍵詞，如 `popup`）
  3. 二者皆不合 → 停並回報

登記可驗（第三個檢查點）：`resolution=PC` 者，收斂時檢該 TC 之
pre_conditions 含 `resolution_key`；`Step-n` 者檢該步驟含之。
聲稱「結構會解」而結構裡沒有 —— FAIL。
```

**即時適用**：
- `038-03` → 單句 s3，`resolution=PC`，`resolution_key=popup`
- `038-04` → 單句 s4，`resolution=Step`（關閉彈窗／等待完成之步驟），
  `resolution_key=popup`
- **`038-02` 不改** —— 其 `1-2` 登記未撞任何限制，已驗證通過；
  改動無收益（層次 1 之預設對它成立）。

> 非連續 `1,3` 不採：verbatim 之連續性是子串判準（第 7b／第二層）
> 之基礎，破壞它會使二個機器檢查對該筆失效 —— 為省 token 而放棄
> 機器保護，方向反了。

### 2.3 R-3 之 token 工作定義（§8 揭露之處置）

canon 未定義 R-3 之 token 化方式。**以空白切分為本 feature 之工作定義**，
記入 profile（新條或附於 §8），標明「canon 若日後定義，以 canon 為準，
屆時全表重算」。§4.2 之 54／42／21 隨之為正式值而非近似值。

---

## 三、第 4 批生成授權（16 筆）

`Test Group` = `Vehicle Category`／`Test Set` = `Settings Behavior`（16 筆皆同）

### 3.1 範圍

15 leaf → **16 TC**（`038-05` 拆 2，`split_delta: 1`）。
a 段 15、b 段 0、**PENDING 0** —— 本批為首個全潔批。

### 3.2 本批特有拘束

| 筆 | 拘束 |
|---|---|
| `034-02` | **進入路徑不得為 Settings 頁籤**（§13.1 於 key-off 擋之，上繳包 22 §2.3）—— 經 §13.2–13.4 之可用路徑（Phone screens／Media／Software Updates）進入。**測試資料**（哪個設定於 key-off 不可用）：自 `HMI Settings List` 查證，查得則具名；查無則以規格語言之通稱表述（如 `a setting available to the vehicle but not in key-off`），**不得自行指定某一設定**（§8.4.1）。`reasoning` 載 §2 交叉比對之結論與此路徑拘束 |
| `035-03`／`036-02` | **R-VC25 例外路徑**：上半取 Title，三件逐筆記（理由／R-VC24 判別結果／非行為主張）。ER **必含 baseline**（§5.6）：記錄現值 → Cancel → 驗值未變。二筆之括號下半以 prompt 之別區分（restore-defaults／clear-personal-data）|
| `036-01` | `reasoning` 載 R-VC14(b) 分歧揭露（執行失效非 data-loss；隱私風險記 reasoning 不入 priority）|
| `037-01`／`037-02` | 一靜一動之括號區分；`-02` 之 ER 含 baseline（記現態 → 開新者 → 驗餘者 off）|
| `038-03`／`038-04` | 依 §二之 `resolved-by-structure`；CONT 登記先行，收斂時第三檢查點生效 |
| `038-05` | 拆 2（complete → normal／not complete → 灰化持續至完成），同 req_id，括號下半以分支區分 |
| `039` | 彎雙引號與 `X/Close` 斜線逐字保留；**Driver screen 之中文顯示屬叢集側** —— ER 限於 HU 彈窗之出現與其文字，叢集顯示記委派於 reasoning |
| 記法 | 三筆二欄不對稱（`035-02`／`036-01`／`038-01`）—— 取一欄保持一致，reasoning 載取自哪欄（第 7b 之分布自動記錄）|

### 3.3 收斂條件

20 項沿用。第 15 項：`len(tcs) == 15 + 1`。
**新增第三檢查點**（§2.2 之 `resolution` 驗證）—— 併入第 17 項或獨立編號，
執行層定並回報；**依 §7.1.1 self-test 前置**
（已知標的 = `038-03` 之 PC 應含 `popup`；反向 = 臨時將 `resolution_key`
改為 PC 所無之詞 → 應 FAIL）。
**第 7b 之取材分布預期**：`Title` 首次非零（2 筆），逐筆檢 R-VC25(3) 三件。

---

## 四、執行層任務

| # | 任務 |
|---|---|
| T121 | CONT 收錄判準增第三處置類（§2.2 逐字入 profile 該節）；表增 `resolution`／`resolution_key` 欄；`038-03`／`038-04` 登記；`cont_deferred.tsv` 清空（本批列冊二筆皆已判定）|
| T122 | token 工作定義入 profile（§2.3）|
| T123 | 第三檢查點實作，self-test 前置 |
| T124 | 生成第 4 批 16 筆，`generated/batch4_settings_behavior.json` |
| T125 | 收斂全項通過；四批回歸 |

**不在本輪範圍**：寫回工作簿、b 段生成、第 5 批。

---

## 五、上繳包要求

1. T121–T125 逐項結果
2. 16 筆 TC 全文；收斂全輸出；第 7b 取材分布（Title 二筆之三件逐筆）
3. 第三檢查點之 self-test 輸出
4. 量測條件揭露（R-G8）

---

> 待 Pei（Tier 3）：同批 A（六項）、DR-VC3、DR-VC9(一)。
> 第 4 批收斂後：96/117，剩第 5 批（16）＋ 第 6／7 批（3）＋ b 段（3）。
> **第 5 批無 DR-VC5 之答覆亦可生成**（R-VC3 已裁全取，FROP 揭露為表 A 之事）——
> 尾段真正的硬阻斷只有 DR-VC3（第 6／7 批邊界）與 DR-VC9(二)（b 段 3 筆）。
