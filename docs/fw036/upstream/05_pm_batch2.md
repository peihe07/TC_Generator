# 上繳 05：PM 第二批（M17 禁用動詞 + DR-PW12 增列）

執行層：Opus5（Claude Code）｜日期：2026-08-21｜新規 0 條
基底：`features/power/sandbox/b02/pm_remediated.xlsx`（批 1 工作副本，
sha256 `cfda6769…aa`）
產出：`features/power/sandbox/b02/pm_batch2.xlsx`（sha256 `f59de2e7…4d`）
**未交付**：未複製回交付路徑、未動 ChangeHistory（屬 Pei）。

## 1. 驗收對照

| 項目 | 目標 | 實測 | 判定 |
|---|---|---|---|
| A 禁用動詞 | 0 | **20 → 0** | 達成 |
| B C D E F G H I I-sib J K L M N P | 不得變動 | 0 / **2** / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0，全數與批 1 後相同 | 達成 |
| 逐格 diff | 20 格，皆 proc | **20 格，涉及欄 `['L']`，非 proc 欄變動：無** | 達成 |
| 新增／刪除之格 | — | 0 | 達成 |
| x14 下拉讀回 | 前後相等 | 1 → 1；zip 成員 42 全保留，僅目標 sheet XML 相異 | 達成 |
| 寫入路徑 | `surgical_save` 唯一 | 是；全域無 `Workbook.save()` | 達成 |

回修後全 16 項檢查中僅 C=2 非零（rows 32、147 之 hedge，位於 test_item
上半 verbatim 內，非本包範圍）。

## 2. 改動列清單（20 列，皆 proc 欄）

### 型 B —— `Observe` 作主動詞（2 列，改 step 1）

rows 210、225，逐字照下放包給定值：

```
前：1. Observe the bus traffic while the CAN network stays awake
後：1. Read the bus traffic while the CAN network stays awake and record
    the $Radio_Theme$ message
```

### 型 A —— `to check whether` → `to check that`（18 列，改 step 2）

| 列 | 改寫後之 step 2 |
|---|---|
| 15 | …to check that the images are provided |
| 86 | …to check that the transition of this clause **does not occur** |
| 128 | …to check that the backlight is off |
| 178、292 | …to check that the disclaimer screen **is bypassed** |
| 205 | …to check that **no** reset occurs |
| 238、242 | …to check that the start-up animation **is skipped** |
| 255–257 | …to check that a startup sound accompanies the animation |
| 275–281 | …to check that the disclaimer and splash screen are skipped |

每列僅改動含禁用動詞之該一行；step 1（型 A）、ER 欄、test_item 欄
均未觸碰 —— 逐格 diff 之 20 格皆落於 proc 欄可證。

## 3. 與下放包附表相異之 6 列（依「以 ER 為準」之規則取值）

下放包 §一載「全 18 列皆為肯定式，無否定分支（分析層實測）」——
**該陳述不成立**。實測 6 列之 ER 為否定式或「skipped／bypassed」，
附表給定之述語與其 ER 相反。若照附表機械寫入，將產生 proc 與 ER
相互矛盾之測項（canon §7 False Fail）。

下放包同時明訂「**依該列 ER 之實際極性調整述語，不得機械替換**」與
「**改寫須以 ER 為準**」。規則優先於附表，故依規則取值：

| 列 | 附表給定 | 本包依 ER 取值 | ER 逐字 |
|---|---|---|---|
| 86 | …that the transition occurs | …that the transition of this clause **does not occur** | `TLM_Status.Info does not pass to "Standby" through the transition of this clause` |
| 178 | …that the disclaimer appears | …that the disclaimer screen **is bypassed** | `The disclaimer screen is bypassed` |
| 292 | …that the disclaimer appears | …that the disclaimer screen **is bypassed** | `The disclaimer screen is bypassed` |
| 205 | …that a reset occurs | …that **no** reset occurs | `The HU does not reset due to a power button reset` |
| 238 | …that the animation is played | …that the start-up animation **is skipped** | `The HU skips the start-up animation` |
| 242 | …that the animation is played | …that the start-up animation **is skipped** | `The HU skips the start-up animation` |

下放包已自行標出 rows 255–257 與 275–281 之同型問題並於附表更正；
上列 6 列為**同一形態而未被標出者**。三組合計 16 列（6 + 3 + 7）
之現行 proc 述語與其 ER 不對應，即 18 列型 A 中之 16 列 ——
此非本包引入，係既有內容缺陷，M17 一併帶出。

## 4. 抽驗結果（下放包指定 10 列）

**rows 255–257**（3 列）：改寫後 proc step 2
`Read the audio output to check that a startup sound accompanies the animation`
↔ ER step 2 `A startup sound accompanies the animation for the new day`。
3 / 3 對應（述語與受詞一致；ER 之 `for the new day` 為補語，proc 不重述）。

**rows 275–281**（7 列）：改寫後 proc step 2
`Read the screen to check that the disclaimer and splash screen are skipped`
↔ ER step 2 `The disclaimer and splash screen are temporarily skipped`。
7 / 7 對應。改寫前 proc 問「the startup screens **appear**」而 ER 為
「**skipped**」，語意相反，此次一併校正。

另對 §3 之 6 列逐列列印 proc／ER 併排比對，6 / 6 極性一致。

## 5. DR-PW12 增列（不新開 DR）

已寫入 `features/power/DATA_REQUESTS.md` 之 DR-PW12 **列末**，
比照該檔 R-P270(b) 之既有增列格式（追加於列末欄，非併入「內容」欄）。
**Urgency 未改（Medium／live）、編號未改。** 該列由 6 欄增為 7 欄。

增列全文：

> **【批 1 覆核增列，05 包 §二】第六對：`SWE-PM-080` ≡ `SWE-PM-086`。**
> 工作簿 rows 210/225（TC `PowerManagement-201`/`216`）與
> rows 211/226（TC `-202`/`-217`）之 test_item 上半、括號下半、
> pre／input／proc／er 四欄**逐字全同**，僅 Requirement ID 與 row 210 之
> Priority（P0 vs P1）相異。依 §8.2.1 不得由 TC 側合併或刪列 ——
> 刪任一側將使該 leaf 失去覆蓋。TC 側維持現狀，待上游答覆。
> （分析層 04 包覆核；原登記編號 A-PM04 撤銷，併入本 DR。）
> ⚠ 執行層註：rows 210/225 之 proc 已於批 2 依 M17 改寫
> （`Observe` → `Read … and record`），二列改寫後仍逐字相同，
> 重複狀態未因回修而改變。

執行層獨立複驗該重複主張：rows 210/225 與 211/226 之
test_item／pre／input／proc／er **五欄全同**（回修後仍然），
Requirement ID 分別為 `SWE-PM-080` 與 `SWE-PM-086`。主張成立。

## 6. 對 04 包一項計數之更正（§5a）

04 包 §一 style-divergence 載「上繳所列 9 列中，rows 47、55、58、59、
136、137 經複驗**實際不以連接詞起首**，真值為 3 列」。

**實測不成立。** 對 `pm_remediated.xlsx` 之 test_item 首行逐列讀取：

```
row  47: 'AND\xa0STATUS_BH_BCM2.RemStActvSts\xa0has\xa0a\xa0transition…'
row  55: 'AND\xa0STATUS_BH_BCM2.RemStActvSts\xa0has\xa0a\xa0transition…'
row  58: 'AND Rear Camera is not Active\xa0(provided that proxi parameter…'
row  59: 'AND Rear Camera is not active\xa0(provided that proxi parameter…'
row 136: 'AND Rear_Camera_Enable.Info == "True" THENeven IF…'
row 137: 'AND Rear_Camera_Enable.Info == "True" THENeven IF…'
row 239: 'Or if HU changes mode (due to ignition event or to due to…'
row 240: 'Or if HU changes mode…'
row 241: 'Or if HU changes mode…'
```

九列皆以連接詞起首，**真值為 9 列，非 3 列**。差異之可能成因：
rows 239–241 之原文為小寫 `or`，經 R-4 正規化為 `Or`；rows 47 等原文
即為大寫 `AND`，R-4 未改動之。若複驗僅比對 R-4 正規化後之
`Or`／`And`／`Then` 三式，即會漏掉 `AND` 六列。

**對裁定無影響** —— 04 包「維持現狀、不擴充 R-4」之理由（刪詞即改動
verbatim）對 9 列一體適用，本包亦未處置。惟該 6 列於 04 包紀錄中
被登記為「不存在」，建議更正其 style-divergence 計數。

## 7. 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項：**

1. **§3 之 6 列改寫係執行層依 ER 推導，未經分析層覆核。** 本包能自證
   改寫後 proc 與該列 ER 極性一致；**不能自證該 ER 本身正確**。
   若 ER 才是錯的一方（例如 row 86 之 ER 應為肯定式），則本包之改寫
   會把錯誤從 proc 移到 proc＋ER 一致的錯誤，更難察覺。
   16 列（6+3+7）之 proc／ER 原本互相矛盾，**矛盾之哪一側為真，
   須回溯需求原文判定**，本包未做，亦不在授權範圍。
2. **C=2 未處置且性質未定。** rows 32、147 之 hedge（`properly`／
   `Successfully`）位於 test_item 上半 verbatim 內。依 R-6 之同一理據
   （verbatim 保留來源原文），此二列疑應豁免 C，但 **R-6 僅裁定 P，
   未及於 C**。現況為 lint 持續回報 2 筆而無處置路徑。
3. **型 A 之 18 列僅改 step 2，step 1 未經檢視。** 下放包限定
   「不得順帶改動 step 2 以外行」，故未查 step 1 是否另有品質問題
   （如 rows 275–281 之 step 1 `Bring the HU to Timed mode while the
   event listed in Input Test Data holds` 是否可執行）。
4. **PM 全案未結項未動**：M16-PM（spec_reference 283 列 R-2 遷移，
   需先建 SWE-PM→ObjectID 對照表）、12 項 live DR（含本包增列之
   DR-PW12 第六對、批 1 新登之 DR-PW16／17／18）。
   另，批 1 上繳 §8 項 5 所指之 R-P309 授權問題仍在：
   PM 內容經批 1（154 列）與批 2（20 列）兩次實質變動，
   **原授權不及於變動後版本**，交付前須重新取得。

## 8. 引用之既有裁決

canon §5.1（禁用動詞與 preferred verb）、§7（False Pass／False Fail，
§3 之判準）、§8.2.1（不得由 TC 側合併或刪列，§5）、§8.4.1（不得造值）、
R-4（首字轉大寫，§6）、R-6（verbatim 區段豁免 R-1，§7 項 2 之類比）、
R16／R-G3（`surgical_save` 唯一寫入路徑）、R-P270(b)（DR 列末增列格式，§5）、
R-P309（授權效力範圍，§7 項 4）、§5a（不以自身先前輸出為來源，§6）。
編號落檔見 `docs/fw036/RULINGS_LEDGER.md` 與 `features/power/RULINGS.md`。

## 9. 產出檔案

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b02/pm_batch2.xlsx` | 批 2 工作副本（M3/M15/M10/M11/M17 全數完成） |
| `features/power/sandbox/b02/m17_edits.json` | 20 格編輯集與 6 列附表偏離紀錄 |
| `features/power/sandbox/b02/pm_batch2_20260821.md/.json` | 批 2 後 lint036 報告 |
| `features/power/scripts/b02/m17_edits.py` | M17 改寫規則（含 ER 極性依據） |
| `features/power/scripts/b02/apply_m17.py` | 寫回程式 |
