# 14 — Comfort HMI / Part N 修正案 ＋ R-C19

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/08_ch2_ch16_fulltext.md`
- 結論：**PASS**。依 R-C18 末句完成 ch2／ch16 章內歸屬之全文複核，
  **四節改置**。

---

## 0. 落檔延遲之說明

本包之內容於 2026-08-15 已於 chat 作成，但未即時寫入 repo，致執行層無指令
可跑一輪。「A ruling not written to the repo did not happen」雙向適用 ——
延遲期間該四節之歸屬與 R-C19 在 repo 內不存在，非「已定而未傳達」。
本包為其正式落檔，日期以本包為準。

---

## 1. Part N 修正案 —— 四節改置

依 R-C18 末句（凡以截斷欄位為輸入之既有判斷須以全文複核），對 ch2（22 節）
與 ch16（18 節）逐節複核。**11 組為整章對應，其章別來自 export 之
`chapter_title`（非截斷欄位），不在複核範圍**；受影響者僅章內切分之
#1–#4、#11–#14。

### 1.1 `2.16` / `16.17` —— 截斷造成之誤讀

```
截斷值：C18.) If blower reduction occurs automatically due to an act
全文  ：…due to an active Voice Recognition session, the change in fan speed
        is not displayed to the user. After blower reduction, return blower
        speed to previous speed without showing a change in fan speed.
```

主詞為**風量之顯示**。原歸 `Climate Modes` 係因「blower reduction」被讀為
氣候模式行為；揭露主詞之子句位於第 60 字之後。與 6.3 之 `secondary` 同型。

→ `2.16`（2 leaves）改置 `Temperature and Fan`
→ `16.17`（1 leaf）改置 `ICS Temperature and Fan`

### 1.2 `2.14` / `16.14` —— 分析層之分類錯誤（非截斷所致）

MTC 為**空調系統型別**（Manual Temperature Control，相對於 ATC），非
AUTO／AC／RECIRC 一類之模式開關。將系統型別與模式開關同置為類別錯誤。

`2.14` 全文另有一段僅全文可見：

> For MTC with ICS… certain types of physical knobs (3 knob HVAC controls)…
> **no HVAC menu bar icons, no HVAC screens and no HVAC pop ups will be
> displayed.**

此與 `6.3`（comfort section will be removed from the head unit）同屬
「**是否出現、出現哪一套**」之陳述，即 Anatomy 之範疇。

→ `2.14`（4 leaves）改置 `Front Climate Anatomy`
→ `16.14`（3 leaves）改置 `ICS Anatomy`（維持鏡像）

**此項非截斷所致，係分析層原始分類判斷有誤，如實記之。**

### 1.3 修正後之 Part N

| # | Test Set | 原 | **新** |
|---|---|---|---|
| 1 | `Front Climate Anatomy` | 12 | **16** |
| 2 | `Climate Modes` | 41 | **35** |
| 3 | `Temperature and Fan` | 17 | **19** |
| 4 | `Airflow and Defrost` | 23 | 23 |
| 11 | `ICS Anatomy` | 14 | **17** |
| 12 | `ICS Climate Modes` | 40 | **36** |
| 13 | `ICS Temperature and Fan` | 16 | **17** |
| 14 | `ICS Airflow and Defrost` | 29 | 29 |

其餘七組（#5–#10、#15）不變。

**驗算**：ch2 = 15（#1 扣除 ch6 之 6.3）+ 35 + 19 + 23 = **92** ✅；
ch16 = 17 + 36 + 17 + 29 = **99** ✅；總計仍 **403** ✅。
區間 14–59；最大者仍 `Heated Vented Seats`（59）。

### 1.4 一項附帶觀察

`Climate Modes` 由 41 降至 35。Pei 於 11 §4.2 裁定不拆該組，事後看為正解：
其問題不在過大，而在混入兩節不屬於它者。拆為兩組不會解決此事，只會把錯置
之節分到兩邊。

---

## 2. 刻意不動之一處（Phase 4 註記，非改置）

`2.6.1`（SYNC 開啟時調整駕駛側溫度連動副駕）屬 `Temperature and Fan`；
`2.11`（SYNC 開關狀態，及同一連動行為）屬 `Climate Modes`。兩節內容明顯
重疊而分屬兩組，siblings 不相鄰（§4.1.4 第 2 點）。ICS 側之 `16.6.1`／
`16.11` 同構。

**不改置。** 此非截斷所致之誤讀，而是分組偏好；本輪之授權為「依 R-C18
回溯複核」，非重開 Part N。

**Phase 4 指示**：撰寫 `2.6.1`／`2.11`（及 `16.6.1`／`16.11`）之 TC 時須
一併閱讀對造節，依 §4.6 作 sibling 判定，必要時輸出 `duplicate_of`。
若屆時顯示兩者確不應分置，屬 Part N 變更，回分析層重簽。

---

## 3. 已簽裁決條文

執行層於上繳 08 §1 自行於 `framework.md` 加入一條 Phase 4 約束，並主動聲明
「非分析層指示，若不同意請駁回」。**不駁回，升格為條文** —— 其理由具一般性，
不應只以 `framework.md` 內一句話之形式存在。

```
R-C19  裁定之表達形式一致性

凡分析層之裁定，其實質內容為「某差異屬 X 類而非 Y 類」者，Phase 4 之 TC
表達形式須與該分類一致，不得以不一致之形式將裁定於 TC 層推翻回去。

具體適用（ch11／ch12）：`opens popup` 既經裁定為輸出回饋而非進入路徑，
ch11 之 11.1／11.2 與 ch12 之 12.1／12.2 之差異一律以 **expected_result**
表達（是否出現 popup），**不得**寫成不同的 test_procedure 步驟或不同的
pre_conditions。

理由：分類裁定之效力止於文件，除非它同時約束 TC 的寫法。無任何機械檢查
會擋住「步驟寫得不一樣」，故須明文，且須在該裁定作成時一併寫下，
而非留待 pilot review 發現。

pilot review 時，違反本條者列為 defect（非 style-divergence）。
```

---

## 4. 接受、無須處置者

- **`12.1` 之 `LEDs (.`** 登為 A-CF13 第四項，並歸納「唯有讀全文可見」——
  此為 R-C18 之最強佐證：前三項標籤衝突由標籤即可見，第四項位於第 174
  字元，任何以 60 字截斷為輸入之比對都看不到。
- **不得靜默修正 spec 原文**（修正非 TC 作者權限，§8.4.2）：正確。
  Phase 4 若逐字引用該句，照錄或明示節錄。
- **18 節元件掃描**：`hard control` 之 2 處命中皆為條件子句、`status bar`
  之 4 處皆為顯示位置、`ICS`／`knob`／`physical` 零命中且另以全文逐節閱讀
  複核（不以零命中為結論，符合 R-C13）—— 方法正確，事實與 ch11／ch12
  合併之裁定方向一致。
- **「其餘 20 節」自我訂正為 18 節**（22 − 4，非 22 − 2）：接受。

---

## 5. 執行層作業指示

1. R-C19 原文貼入 `RULINGS.md`。
2. 依 §1 更新 `framework.md` §2 表、§6 明細、`data/test_set_map.tsv`、
   `data/section_fulltext.tsv` 之 `test_set` 欄、`scripts/verify_partn.py`
   之 `PART_N` 期望值 —— **五處同步**。
3. `verify_partn.py` 七項檢查全數重跑，期望值改為 §1.3 之新數字
   （寫死於腳本，不由資料回推）。**特別驗**：ch2 == 92、ch16 == 99、
   總計 == 403 於改置後仍成立。
4. `framework.md` 增記本包 §1.1／§1.2 之改置理由（含截斷原文對照），
   並移除或改寫 §1 中執行層自加之 Phase 4 約束段，改為指向 R-C19。
5. `DECISIONS.md` §6 之 Part N 條目增記「2026-08-15 修正案（下放包 14）」，
   **Sign-off 不重簽**（Part N 之結構未變，僅四節歸屬更正；若執行層認為
   此判斷有誤，回報，不自行重簽）。
6. §2 之 Phase 4 註記寫入 `RUNBOOK.md`。
7. Phase 4 仍不開始 —— profile `[OVERRIDE]` 為硬前置，草案見下放包 15。
8. 上繳 `docs/upstream/09_partN_amendment.md`。git 不執行。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C19 裁定之表達形式一致性 | ✅ §3 | 已簽 2026-08-15 |

R-C19 須貼入 `RULINGS.md`，適用全 feature，安置位置待 canon re-sync。
§1 之四節改置為 Part N 內容變更，隨 `framework.md` 更新，不入 `RULINGS.md`。
