# 下放包 02 —— Vehicle Category 裁定（A-VC5 / A-VC6 / A-VC7 + 四項）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/02_rulings.md`
- 前一包：`01_intake_recon.md`（SHA256 `e50b5508…c97a74`）
- 對應之上繳包：`docs/upstream/01_intake_recon.md` §8 待裁七項

---

## 〇、本包之性質

上繳包 01 停於 T4（30 項中 1 項 `≠`），並提出七項待裁。
本包**逐項裁定**並新立 R-VC6 ~ R-VC10 五條，撤銷 A-VC1，結案 A-VC5。

**本包更正下放包 01 之一處實質錯誤（§3.3 第 10–18 欄），
其性質為分析層之未量測斷言，非附件差異 —— 見 R-VC6。**

---

## 一、A-VC5 結案 —— 成因確認，非附件失值

### 分析層之附件雜湊（應上繳包 §8 第 1 項之要求）

```
cb80a77e8d57721ef0851c4ce263c46d3cbf5d028bd1a03c89c9d7debfd877ed  100475  037 A03 SWRA
1fcc87116ac3893602f933ea10b2116895265ea0375ed88d0bf02ebcdeb091d6   47458  SYS1 export
216cfa84dfb84c0b3c44e24881407521412e16d16728aaa49e90ff3b3275a455  3552260  規格 PDF
```

037 與 SYS1 之雜湊與 repo 內複本**逐字相同**。

### 判讀

上繳包 A-VC5 列出二種可能：
(a) 附件傳遞中該九欄失值；(b) §3.3 之量測方法判讀有誤。

**兩者皆非。** 037 只有一份位元組序列，分析層與執行層看的是同一個檔——
(a) 由雜湊相同排除。

分析層重跑量測，結果與上繳包 A-VC1 之重測表**逐格相同**：

```
欄10 Feasibility   {'Yes': 117, '\xa0': 28}
欄11 Desc/Feasib.  {'Achievable for this rule — …': 117, '\xa0': 28}
欄12 Impact        {'Yes': 117, '\xa0': 28}
欄13 Desc/Impact   {'\xa0': 28, "For this rule — 'When the u…": 15, …}
欄14 Risk Factor   {'Medium': 60, 'Low': 57, '\xa0': 28}
欄15 Desc/Risk     {'\xa0': 28, "Risk is Medium for 'When th…": 15, …}
欄16 Reusable      {'High': 116, '\xa0': 25, None: 3, 'Fully': 1}
欄17 Desc/Reusable {'Reuse is High (≥50%) for …': 38, '\xa0': 25, …}
欄18 Priority      {'Medium': 88, '\xa0': 28, 'High': 28, 'Low': 1}
```

(b) 亦不成立 —— **成因不是判讀有誤，是未曾判讀**。
下放包 01 起草時之量測程式只取索引 `0, 1, 3, 5, 6, 7, 8` 七欄，
索引 `9`–`17`（即第 10–18 欄）**未被讀取過一次**。
§3.3 之「全 145 列皆為 `\xa0`」係自表頭附近之局部觀察推廣為全稱斷言，
再以實測值之形式寫入表格。

**A-VC5 狀態改為 RESOLVED。** 成因記為：分析層之全稱斷言未經全表掃描。

### 此事之實質後果（大於一個數字）

037 於 **117 個 leaf 上提供完整之 Feasibility / Impact / Risk Factor /
Reusable / Priority 判斷，另有四欄逐條分析文字**。

下放包 01 不僅漏記，且據該漏記立 A-VC1 指示「不視為已填」。
若未經 T4 攔下，後果為 Phase 6 之 `priority` 欄失去上游依據而僅能本地推導
—— 即 IN §8.4.1 所禁之造值，且影響全部 117 列。

執行層攔下的不是量測誤差，是一條會使 117 列 TC 全面造值之路徑。
此為「下放包之數字非事實來源、須經 repo 重測」機制之首次實戰生效，
建議 Pei 於全域台帳留痕（R-G 層級，本包不代擬）。

---

## 二、裁決條文（逐字抄入 `features/vehicle_category/RULINGS.md`）

> 逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。抄畢附逐條核對結果。

```
R-VC6（037 分析九欄為有效上游輸入；A-VC1 撤銷）

037 `Analysis Report` 第 10–18 欄 ——
Feasibility / Description-Action for Feasibility / Impact /
Description-Action for Impact / Risk Factor /
Description-Action for Risk Factor / Reusable /
Description-Action for Reusable / Priority ——
於 117 個 leaf 上皆有實質內容；於 28 個「有子之父」為 `\xa0`（U+00A0）。
欄 16 `Reusable` 與欄 17 `Description-Action for Reusable` 另有 3 列為
`None`（真空儲存格）：SWE1-HMI-VC-034、SWE1-HMI-VC-052、SWE1-HMI-VC-063。

下放包 01 §3.3 所記「第 10–18 欄全 145 列皆為 `\xa0`，無內容」為分析層
未經全表掃描之全稱斷言，**作廢**。據其所立之 A-VC1 一併**撤銷**，
其條文不得於任何場合沿用或引述為判準。

拘束四項：
(a) 欄 18 `Priority`（實測分布 Medium 88 / High 28 / Low 1）為上游對各
    leaf 之優先級判斷。TC 之 `priority` 欄（IN §10.2 之 P0–P3）
    **不得於忽略本欄之情況下本地推導**。P0–P3 與 High/Medium/Low 之
    映射規則另裁，在該裁定落地前，priority 欄不得產出。
(b) 欄 11 / 13 / 15 / 17 之描述文字為 `reasoning` 與 test_item 括號下半
    之素材來源，須納入 Phase 4 之資料建置範圍。
(c) 欄 14 `Risk Factor` 與欄 12 `Impact` 為 §10.2 映射之佐證，
    不單獨作為 priority 之依據。
(d) 「讀取時 strip 含 `\xa0`」之技術手段**保留**（A-VC1 之正確部分）。
    作廢者為「不視為已填」之推論 —— 這九欄在 117 個 leaf 上是已填的。
```

```
R-VC7（規格 PDF 之權威複本）

分析層 Claude Project 附件之規格 PDF 為
3,552,260 B，SHA256
`216cfa84dfb84c0b3c44e24881407521412e16d16728aaa49e90ff3b3275a455`。
repo 內複本及全機 7 份複本一律為 2,828,253 B，SHA256
`3a6752c83bed1582485ad5e1aa7052ae63e6f0bb94304839beaf0e0b12776a76`。

二者為不同之檔。**repo 內複本為權威**；附件之份判為 Project 上傳時
重新渲染之衍生物，不得作為任何判準之來源。
（`scripts/recon.py` 檔頭已預告此情形：re-rendered copy 之文字層探測
結果會與原件不同，一律以 repo `inputs/` 之複本為準。）

連帶拘束：下放包 01 §4.2(b) 之 18 節「規格內容摘要」欄係讀該衍生 PDF
所寫。其**章節號**已由 T4 驗明相符，**摘要文字未經權威複本確認**。
DR-VC3 發出前須以 repo `inputs/` 之 PDF 逐節重驗；重驗前該摘要不得
引為 DR 之措辭依據，亦不得寫入表 B。
```

```
R-VC8（recon.py 於 spec_reference_template 為 null 時之行為；Tier 2 修法授權）

`scripts/recon.py:894` 之 `tpl = cfg.get("spec_reference_template", "{outline}")`
在鍵存在而值為 `None` 時取得 `None`，於 `:900` 之 `tpl.replace()` 崩潰。
R-VC4 明文要求該鍵為 `null`，故本 feature 必然觸發。

採上繳包 A-VC6 之提案 (b)：**`spec_reference_template` 為 null 時，
`data/recon_leaf_to_section.tsv` 之 `spec_reference` 欄改逐字取 037
`HMI Source ID` 欄之原值**，使資料件與 R-VC4 一致。

提案 (a)（`... or "{outline}"`）**不採**：其產出為光禿之章節號，
與 R-VC4 所裁之全名不同，等於在資料件中埋一個與裁決相左的值。
崩潰會停，錯值不會 —— 後者為害更甚。

實作拘束三項：
(a) `survey_a03()` 現將 citation 拆為 stem 與 sec 後僅保留 sec
    （`sections[rid] = m.group("sec")`），原值已丟失。修法須**同時保留
    `first` 之原值**（例如新增 `citations[rid] = first`），
    **不得**以 `stem + "_" + sec` 還原 —— 該還原式在 stem 本身以底線
    接數字結尾時會取錯切點。
(b) 未宣告 `spec_reference_template` 之 feature 行為不變（`dict.get`
    之預設值路徑保留），使其他 12 個 feature 之既有產出基線不動。
(c) 修法後須對至少一個既有 feature（建議 `home` 或 `comfort`，
    其 recon 有回歸基線）重跑並確認產出逐字不變，再對本 feature 重跑。

本條為 Tier 2 工具修法之授權，範圍僅限上述。
`recon.py` 之其他行為一律不動。
```

```
R-VC9（recon_assertions 之宣告範圍與未機器化之揭露義務）

`scripts/recon.py` 之 `run_assertions()` 僅實作三個鍵：
`functional_requirement_count`、`distinct_spec_sections`、
`spec_reference_stem`。`leaf_count` 與 `uncovered_content_sections`
**無對應實作，宣告不生效**。

本 feature 之 `recon_assertions` 僅宣告：

    recon_assertions:
      functional_requirement_count: 145

下放包 01 §八 所草擬之 `leaf_count: 117`、`distinct_spec_sections: 66`、
`uncovered_content_sections: 18` 三鍵中，`leaf_count` 與
`uncovered_content_sections` **刪除**；`distinct_spec_sections: 66`
得保留（該鍵有實作），由執行層於重跑後確認其 PASS 再定去留。

依據：宣告一個不被讀取之鍵，比不宣告更糟 —— 不宣告至少誠實，
宣告則製造一個永不失敗之檢查，並使讀者誤認該值已受保護。
此與 display 之「宣告必然為 0 之 assertion 只會製造一個不可能失敗之
檢查（canon §5a）」同源，本案為其鏡像。

揭露義務：R-VC3 之 leaf 全集 117 與覆蓋落差 18，在對應 assertion
落地前**僅靠 T4 重測與上繳包交叉檢查守護，非機器保證**。
此事實須逐包揭露，**不得因 feature.yaml 有寫而視為已守**。

leaf 判準三者並存之事實一併記於 feature.yaml 註解：
  145 —— Categorization == Functional（recon.py 在用）
  117 —— 子需求 ∪ 無子之父（R-VC3 所裁之驗證母體）
   79 —— id-suffix（recon.py 明記不生效）
display 未暴露此分歧，因其 037 之三值恰皆為 8。
```

```
R-VC10（素材之 paths / reference 分工）

**`paths:` —— 素材一律複製入 `features/vehicle_category/inputs/`，
路徑以本 feature 目錄為基準。**

    paths:
      popup_list:    "inputs/Pop Up List HMI R1 (26PI).xlsx"
      settings_list: "inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx"

下放包 01 §五 T1 之「forms/ 兩份不複製，僅綁定」**作廢**。
依據：`features/display/feature.yaml` 已記載此坑 —— 將 forms/ 之 repo
相對路徑填入 `paths:`，`recon.py` 隨即以 `input not found … under
features/display` 中止。素材複製入 `inputs/` 為 home / display / comfort /
power_moding 之一致慣例。執行層留 `null` 為正確之保守處置。

**`reference:` —— 六項，路徑以 repo 根為基準。**

    a03_report / sys1_export / spec_pdf   → features/vehicle_category/inputs/…
    workbook_master / popup_list / settings_list → forms/…（或 inputs/ 之複本，
      擇一並於註解記明所綁者為何份）

下放包 01 §五 T9 所記之「七項」為分析層計數錯誤，**正解為六項**。
執行層推定第七項為下放包全文並依 R-G15 判準排除 —— 推定過程正確，
惟結論應為「本無第七項」。下放包全文不入 `reference:`。

**明文排除四項**：`dbc_b` / `dbc_fd` / `lid` / `proxi` 不綁定。
依據：037 全文掃描之 CAN 訊號、PROXI 參數、VF 引用命中數皆為 0；
規格本文之 VF507 / VF352 落在 037 未涵蓋之 18 節內。
本 feature 之產出不觸及該四檔，不符 R-G15「其變動會使既有產出失效」
之判準。**此排除須寫入 feature.yaml 註解** —— 否則日後必有人問
為何本 feature 較 display 少綁四項。
```

---

## 三、A 登記之異動

| A | 異動 | 依據 |
|---|---|---|
| A-VC1 | **撤銷** —— 條文作廢，不得沿用或引述 | R-VC6 |
| A-VC5 | **RESOLVED** —— 成因為分析層之全稱斷言未經全表掃描；非附件失值（雜湊相同），非判讀有誤（未曾判讀）| §一 |
| A-VC6 | **RESOLVED** —— 採提案 (b)，修法授權見 R-VC8 | R-VC8 |
| A-VC7 | **RESOLVED** —— repo 內複本為權威；附件為衍生物 | R-VC7 |
| A-VC8 | **新立** —— 條文見下 | R-VC9 |
| A-VC2 | 維持 PENDING → 見 §四 | Pei 裁 |
| A-VC3 | 維持 PENDING（併入 DR-VC3）| 不變 |
| A-VC4 | 維持 PENDING → 見 §四 | Pei 裁 |

```
A-VC8（recon.py 缺 leaf_count assertion）

`scripts/recon.py` 之 `run_assertions()` 僅實作
`functional_requirement_count`（以 Categorization 計，本 feature = 145）、
`distinct_spec_sections`、`spec_reference_stem` 三鍵。
R-VC3 所裁之驗證母體為 leaf 全集 117（子需求 ∪ 無子之父），
該值無對應之 assertion 鍵，於 feature.yaml 宣告亦不生效。

leaf 判準三者並存且分歧：145 / 117 / 79。
display 未暴露此分歧，因其 037 之三值恰皆為 8；
Vehicle Category 為首個使三者分離之 feature。

提案處置：`recon.py` 增設 `leaf_count` assertion，判準取 R-VC3 之定義
（子需求 ∪ 無子之父），與現行 `functional_requirement_count` 併列而非
取代 —— 二者為兩個不同的量，皆應可宣告。
屬 Tier 2 工具修法，**與 R-VC8 之修法非同一件，不得併案順手為之**。
在其落地前，117 之守護僅靠 T4 重測與上繳交叉檢查（R-VC9 之揭露義務）。

狀態：PENDING。
```

---

## 四、上繳包 §8 第 7 項之裁定

**A-VC2（037 封面 Reviewer 空白、Date 2020/09/05）**

裁：**不單獨發 DR**。於 DR-VC2 發出時（同為對 037 作者之查詢）
附帶一句提及即可。理由：封面欄位不阻斷任何 Phase，
單獨往返一輪之成本高於其資訊價值。維持 PENDING 至 DR-VC2 回覆。

**A-VC4 與 A-TM04 之同批修法時程**

裁：**兩者維持 PENDING，不排入本 feature 之任何 Phase。**
理由：A-VC4 已由 T0b 之事後字串更正繞開，A-TM04 已由甲案傳參繞開
——**繞開不是壓制**，二者皆無阻斷。工具修法之時程屬全域議題，
待 Pei 於 FW036 全域排程時一併處理，本 feature 不代為決定。

R-VC8 之修法**不得順手併入** A-VC4 / A-TM04 —— 三者標的不同
（`recon.py` 之 template 處理 vs `new_feature.py` 之命名推導），
併案會使 R-VC8 之授權範圍失去邊界。

---

## 五、執行層續作任務

| # | 任務 | Tier |
|---|---|---|
| T10 | 抄錄 R-VC6 ~ R-VC10 五條入 `RULINGS.md`（接 R-VC5 之後），附逐條 byte-level diff 核對結果 | 1 |
| T11 | `ANOMALIES.md` 依 §三異動：A-VC1 標**撤銷**並註明依 R-VC6；A-VC5 / A-VC6 / A-VC7 標 RESOLVED 並附裁定依據；新增 A-VC8 | 1 |
| T12 | **T4 重新收斂** —— 第 23 項之下放包基準已由 R-VC6 作廢。改以 R-VC6 之條文為基準重跑 `t4_remeasure.py`，預期 30/30 `=`。**若仍有 `≠`，停並回報** | 1 |
| T13 | 依 R-VC8 修 `recon.py`。修法後先對 `home`（或 `comfort`）重跑並確認產出**逐字不變**，再對本 feature 重跑 —— 兩份證據皆附入上繳包 | 2（本包授權） |
| T14 | 重跑 `recon.py --feature features/vehicle_category`，取得 `data/recon.json`、`data/recon_leaf_to_section.tsv`、`DECISIONS.new.md`。逐項回報 assertion 之 PASS/FAIL 與 measured 值 | 1 |
| T15 | 依 R-VC9 修 `feature.yaml` 之 `recon_assertions`（刪二鍵，`distinct_spec_sections` 依 T14 之 PASS 結果定去留），並補 leaf 判準三者並存之註解 | 1 |
| T16 | 依 R-VC10 補填 `paths.popup_list` / `paths.settings_list`（複製二檔入 `inputs/`，複製前後各記 SHA256），確認 `reference:` 為六項，並補「明文排除四項」之註解 | 1 |
| T17 | 依 R-VC7 以 repo `inputs/` 之 PDF 逐節重驗 §4.2(b) 之 18 節「規格內容摘要」。**逐節回報「相符 / 不符 / 無法判讀」**，不符者以權威複本之內容為準改寫 | 1 |
| T18 | 依 R-VC6(a)(b) 盤點欄 11 / 13 / 15 / 17 之描述文字，回報其可用性（是否逐 leaf 皆有、是否含可直接引用之句），供 Phase 4 資料建置與 priority 映射之另裁使用 | 1 |

**不在本輪範圍**：priority 之 P0–P3 映射規則（R-VC6(a) 明列為另裁）、
`framework.md`、profile、任何 TC、任何寫回、任何 git 操作。

**T12 通過後 Phase 1 即收斂**，其後之 `DECISIONS.md` 簽署為 Phase 2 之
Tier 2 事項，執行層不自行進入。

---

## 六、上繳包要求

`features/vehicle_category/docs/upstream/02_rulings.md` 須含：

1. T10–T18 逐項結果，附實際指令與原始輸出
2. R-VC6 ~ R-VC10 之逐條抄錄核對（byte-level diff）
3. **T12 之 30 項比對表全表**（不得只報「已通過」）
4. T13 之兩份回歸證據（既有 feature 逐字不變 + 本 feature 產出）
5. T14 之 assertion 逐項 PASS/FAIL 與 measured 值
6. T17 之 18 節逐節重驗結果
7. T18 之四欄可用性盤點
8. 更新後之未結 DR 清單與 A 清單
9. 量測條件揭露（R-G8）：T12 / T17 / T18 各項之方法、工具、偽陽性風險
