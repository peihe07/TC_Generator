# 下放包 22 —— Vehicle Category：sentence_index ＋ 第 4 批勘查前置

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/22_batch4_survey.md`
- 前一包：`docs/handoff/21_batch3_close.md`
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `21_`，無碰撞。
- **第 3 批 a 段收斂確認（20/0，四批回歸全綠）。本包不授權生成任何 TC。**

---

## 一、上繳包 21 之覆核

**核可。** 三項具名：

1. **第 11 項於生成當下攔到 `VC-018`** —— 包 12 之三類齊備檢查
   抓到同類錯誤之第二次發生。修 TC 不動檢查、reasoning 逐字記判讀，
   處置正確。**「太鬆會讓錯誤通過」之修補在第二次發生時證明了自己。**
2. **「列冊」第三態是你們補的，而且補得對。** 20a 只給二態
   （CONT／排除），而第 4／5 批之四筆兩者皆非 ——
   「已看見、待判定」與「已判定」是不同的認識狀態，混用任一既有態
   都是謊報。三態俱全後「默默不登記」才真的不可能。
3. **§8 之三項揭露皆為真缺口**，其中句序硬推見 §二；
   第 17 項之 subprocess 耦合（判定正確、可讀性受損）接受不改。

## 二、`sentence_index`：**准**，且驗證隨之細化到句級

CONT 表增 `sentence_index` 欄，**句序由程式硬推改為表中登記**：

- `continuation` 型：登記其來源句之序號（`012-02`→§2.6.2 s3、
  `012-03`→§2.6.2 s3、`013-02`→§2.6.3 s2、`013-03`→§2.6.3 s2）
- `reference` 型：登記為範圍或 `*`（取整段，句序不適用）

**登記了就能被驗** —— 第二層之內容驗證自節級細化到句級：

```
normalize(037 片段) ⊆ substring( normalize(SYS1 指定句) )
```

指錯句則子串關係不成立（同節他句之文字不同）——
**sentence_index 之正確性有了機器承載者**，
硬推之「無檢查」缺口隨之關閉。反向斷言更新：`013-02` 臨時改指
§2.6.3 s1 → 應 FAIL。

句子切分之偽陽性（縮寫句點）沿上繳包 16 §9 之既知揭露，
本批 CONT 之四節皆無縮寫，實害為零；記明即可。

---

## 三、第 4 批 `Settings Behavior` 之粗查（15 leaf）

> 分析層粗查，037 完整儲存格值（未截斷，長度已列）。
> 依 R-VC15 不得沿用，執行層重測。

### 3.1 ⚠ `034-02` 與章 13 之交叉 —— 本批最重要之勘查項

```
VC-034-02（§11.1，本批）  : If a setting is available to the vehicle but not
                            when key-off, they will appear grey when the
                            system is in key-off.
VC-057   （§13.1，第 5 批）: The Settings tab is unavailable while the vehicle
                            is in Key Off, Timed M…（第 2 批勘查時見其起首）
```

**表面矛盾**：`057` 說 Key Off 下 Settings **tab 整個不可用**；
`034-02` 說 key-off 下清單內項目**灰化** ——
**tab 都進不去，誰看得到清單內的灰化？**

可能之解（勘查判定，不預裁）：
(a) 二者之 key-off **非同一狀態**（章 13 之 §13.1 起首列了
    Key Off／Timed Mode／…多態，`034-02` 之 key-off 或指其中之別態）；
(b) `057` 之 unavailable 有範圍細分（某些電源態可進但降能）；
(c) 規格自身衝突 → DR。

**勘查 (d) 須同時取 SYS1 §11.1 與 §13.1（含全文）交叉比對。**
本項之結論同時影響第 5 批（`Ignition Availability` 全批之狀態定義）——
現在查清楚，第 5 批直接受益。

### 3.2 `035-03`／`036-02` —— Description 逐字相同，R-VC25 例外路徑之首次動用

二筆之 Description **逐字同**為
`Selecting cancel will take the user back to the previous screen.`（64 字元）。

- 上半若皆取 Description → 上半相同（合法，R-S4 只禁下半同），
  **但其 P0 判定之依據（不變更／不清除）不在 Description** ——
  A-VC10 第一面早已記明：該條件載於 **Title**
  （`without changing any settings`／`without clearing any data`）。
- **此即 R-VC25(3) 例外路徑之典型場景**：Title 載有 Description 未載
  而**為本 TC 驗證標的**之條件。二筆應取 Title，三件齊備：
  (a) reasoning 具名理由（如上）；(b) 施 R-VC24 判別 ——
  分析層預判二筆之 Title 謂語皆為本 leaf 行為（returns the user…），
  his 詞（restore-defaults／clear-personal-data prompt）為情境脈絡，
  **非行為主張**；(c) 由 (b) 之結果滿足。
- **本批為 R-VC25 立條後首次動用例外路徑** —— 第 7b 項之取材分布
  將首次出現 `Title` 非零，收斂時逐筆檢其三件。

### 3.3 `038-05` —— 拆分候選（雙分支）

```
If the voice commands are complete the screen will be shown as normal,
if not complete the current language is shown checked while the rest will
be greyed out. They will remain greyed out until the system has completed…
```

**一筆含二個 if 分支**（complete → normal／not complete → 灰化持續至完成）。
IN §5.2 禁一 TC 內寫條件分支；§8.2.2 壓力測試：二分支為二個獨立失效。
**拆分候選 → 2 TC**（同 req_id，同 §8.2.2 之工作簿處置）。
勘查 (g) 判定。

### 3.4 其餘四項

| 項 | 內容 |
|---|---|
| `038-02`／`038-03` | CONT 列冊 → 本批勘查時**判定並登記**（二筆皆指涉型：`It`＝`038-01` 之 pop-up、`This pop-up` 同）。SYS1 §11.5 之句構由勘查 (d) 取得，`sentence_index` 隨 §二之新欄登記 |
| `036-01` | R-VC14 改判 P1 之筆 —— 生成時 `reasoning` 須載 R-VC14(b) 之分歧揭露（執行失效非 data-loss、隱私風險記於 reasoning 而不入 priority）。**此為 R-VC14 立條後首次實際生成該筆** |
| `037-01`／`037-02` | 懸吊互斥：`-01` 為規則（same time 僅一）、`-02` 為行為（開一關餘）。**一靜一動，非重複** —— 括號下半以此區分。ER 之互斥驗證須含 baseline（§5.6：先記錄現態，開新者後驗餘者 off）|
| `039` | 彎雙引號 `“Language updates in progress...”` 逐字保留（R-VC23）；`X/Close button` 之斜線為來源原文，同保留。**中文顯示之驗證限於彈窗之出現與其文字**，Driver screen 之中文顯示屬叢集側 —— 勘查確認其是否在 HU 之可驗範圍，不在則 ER 縮限並記委派 |

### 3.5 P0 首次進批

`035-03`／`036-02` 為本 feature 5 個 P0 中之 2 個，**首次進入生成批次**。
priority 照 `priority_final.tsv`，不重判（R-VC11／13／14 已定案）。
其 ER 之攔阻驗證**必含 baseline**（§5.6）：
先記錄設定現值 → Cancel → 驗值未變 —— 「未變」無 baseline 即不可判。

---

## 四、勘查任務（T118）

| # | 勘查項 |
|---|---|
| a | 15 leaf 之 Title／Description 逐字全文（完整值）|
| b | §3.1~3.5 逐項覆核，**(3.1) 之章 13 交叉為重點** |
| c | 素材可用性 |
| d | SYS1 對照：§11.1~§11.6 全文、**§13.1 全文**（3.1 之交叉）、§11.5 句構（CONT 登記用）|
| e | 來源記法全批掃描 |
| f | 拆分候選逐筆壓測（`038-05` 為已知候選）|
| g | TC 數預估；a／b 段；PENDING 需求 |

**勘查後停，回報，不生成。**

---

## 五、其他任務

| # | 任務 |
|---|---|
| T119 | CONT 表增 `sentence_index` 欄（§二）；第二層細化至句級；反向斷言更新；既有四筆登記句序後全表重驗 |
| T120 | `cont_deferred.tsv` 之 `038-02`／`038-03` 隨 T118(d) 判定後移轉（列冊 → CONT）|

---

## 六、上繳包要求

1. T118 勘查表（a–g）、T119／T120 結果
2. **§3.1 之交叉比對結論**（含 SYS1 二節全文引錄）
3. 量測條件揭露（R-G8）

---

> 待 Pei（Tier 3）：同批 A（六項）、DR-VC3、DR-VC9(一)。
> 第 4 批含二筆 P0 —— **其後只剩第 5 批（DR-VC5 待答）與
> 第 6／7 批（DR-VC3 待答）**，DR 之回覆時程開始決定尾段之形狀。
