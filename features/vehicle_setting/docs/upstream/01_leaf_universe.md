# 01 上繳 — leaf 母體之判準追因與 N 欄未定項收斂

執行層寫入。往返 NN = 01。**本輪未生成任何 TC，未寫回任何工作簿，未執行任何 git 寫入性操作。**

作業：W-0c（素材補入）／W-16（recon 46 vs W-2 56 之追因）／W-18（N 欄未定 26 項）。
**W-8／W-9／W-13／W-15b′／W-17 本輪未執行**，見 §6。

---

## 1. 預期 vs 實測（相符者亦列出）

01 包未給 §5.2 式之預期數字表；本節以 **01 包正文所述之數字**為預期。

| 來源 | 預期 | 實測 | 判定 |
|---|---|---|---|
| 01 §6 W-0c：`inputs/` 檔數 | 15 | **15** | 符 |
| 01 §6 W-0c：`INPUTS.sha256` 可驗 | — | **15 / 15 `shasum -c` OK** | 符 |
| W-0c：落檔與客戶目錄來源位元組相同 | — | **相同**（`1ee4aaaa6506fb4497cfe0e026af8096d33815f9560d70cfb2a6417a6e14040b`） | 符 |
| 01 §2.2：N 欄未定 leaf | 26（25 無章節 ＋ 1 無錨鏈） | **26**（25 NO_SECTION ＋ 1 NO_ID） | 符 |
| 01 §2.2：單一章節 leaf | 240 | **240** | 符 |
| 01 §2.2：多章節 leaf | 5 | **5** | 符 |
| A-VS18：recon leaf 數 | 46（Common Features） | **46** | 符 |
| W-2 判準之 Common Features leaf | 56 | **56** | 符 |
| **差額之成因** | 未追因 | **`Categorization` 過濾**，見 §2 | **已追因** |

### 1.1 02 包 §1 之獨立複驗 —— 與本輪逐項相符

02 包分析層自 `inputs/` 實體檔重測，其數字與本輪完全一致：

| 量 | 02 包 | 本輪 | 判定 |
|---|---|---|---|
| `Functional Requirement` | 237 | **237** | 符 |
| `Heading` | 25 | **25** | 符 |
| `Information`（大寫） | 8 | **8** | 符 |
| `information`（小寫） | 1 | **1** | 符 |
| 非 Functional 合計 | 34 | **34** | 符 |
| 036 覆蓋 leaf | 237 | **237** | 符 |
| 交集 | 34 | **34** | 符 |
| 兩側差集 | 0 / 0 | **0 / 0** | 符 |
| 逐 family 可測 leaf | 46／88／72／31 | **46／88／72／31** | 符 |

> **⚠ 此處之「相符」為同源自我印證**（00 上繳 §9.3-2 之形態）——
> 雙方讀的是同一批 `inputs/` 檔案，相符只證明讀法相同。
> 本輪之跨源檢驗僅一處：**037 之 `Categorization` 對 SYS2 之 `Category`**
> （兩份不同上游文件），見 §3.2。

---

## 2. W-16 —— 追因完成

`scripts/recon.py:602`：

```python
is_leaf = cat.lower().startswith("functional")
```

即依 037 之 `Categorization` 欄過濾。下放包 §5.1 之判準為「**A 欄非空者為 leaf**」，**無此過濾**。

| family | A 欄非空 | `Categorization` = Functional* | 差額 | 非 Functional 之分布 |
|---|---|---|---|---|
| Common Features | 56 | **46** | 10 | Heading 8／Information 2 |
| HeatedSeat | 99 | **88** | 11 | Heading 8／Information 2／`information` 1 |
| VentedSeat | 81 | **72** | 9 | Heading 6／Information 3 |
| Heated Steering Wheel | 35 | **31** | 4 | Heading 3／Information 1 |
| **合計** | **271** | **237** | **34** | Heading 25／Information 9 |

**兩集合完全相同**：非 Functional 之 34 個 leaf 與 036 未覆蓋之 34 個 leaf，
交集 34、兩側差集皆 0、逐 family 亦相同（10／11／9／4）。

→ **A-VS18 除役**：recon 未錯。二者非「對同一件事給出不同答案」，
是**兩個判準在數兩件不同的事**，且 recon 之判準與 036 之實際投影一致。

---

## 3. W-18 —— 26 個未定收斂為 1 個

| 群 | 數 | 屬性 | 處置 |
|---|---|---|---|
| NO_SECTION | 25 | **全部為非 Functional**（Heading／Information） | **不需處置** —— 不產 TC，無 N 欄 |
| NO_ID | 1 | `SWE1-VC-HeatedSteeringWheel-009`，**Functional Requirement** | **待 DR-11**（CFTS100 之身分） |

**可測 leaf 237 個中，N 欄已定 236、未定 1。**
01 包 §2.2 之「245 / 271 已定，26 / 271 未定」，以可測母體重述為 **236 / 237**。

### 3.1 A-VS01 之除役（複驗 02 包 §1.4）

以 037 之 `Categorization` 對 SYS2 之 `Category` **逐 leaf** 交叉列表：

| 037 | SYS2 | 數 |
|---|---|---|
| Functional | Functional Requirement | 236 |
| Heading | Heading | 25 |
| Information | Information | 8 |
| `information` | Information | 1 |
| Functional | **NO_REF** | 1 ← `SWE1-VC-HeatedSteeringWheel-009` |

**零錯配。** 那 25 個不是錯配，是**同一批非需求列在兩份文件裡各自被正確標記**。
→ A-VS01 除役。

### 3.2 這是本輪唯一之跨源檢驗

037（SWE.1 作者）與 SYS2（SYS.2 作者）為**兩份不同上游文件**，
其分類欄逐 leaf 一致，是獨立來源之交叉印證，
**與 §1.1 之同源自我印證性質不同**。

---

## 4. 掃描條件揭露（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| 037 ×4 | `Analysis Report`；表頭列 7（**比對前 `\s+`→單一空格**）；資料自列 8；**A 欄非空 = 列**；`Categorization` 以表頭字串定位（實測第 6 欄，0-indexed 5） |
| Functional 判準 | `cat.lower().startswith("functional")` —— **不分大小寫**、**前綴比對非全等**（`Functional Requirement` 與 `Functional` 皆收） |
| 036 | `Test Case Specification 測試用例規範`；資料列 10–246（實體列號）；D 欄；**逐列** |
| 集合比對 | 以 `swe_id` 字串為鍵，**區分大小寫、全字串相等** |
| SYS2 交叉 | `Basic Report`；資料自列 2；`Category` 欄（第 10 欄，0-indexed 9）；經 `SYS-RA-CFTS\d+-\d+` 之錨鏈對映 |
| `INPUTS.sha256` | `shasum -a 256`，格式為 `shasum -a 256 -c` 可直接驗證；**排除其自身** |

---

## 5. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | ANOMALIES 四處（A-VS01 除役／A-VS06 → A-VS06′／A-VS18 除役／A-VS20 新增）；INDEX 之 NN=00 列兩處過時數字 |
| **核實無誤** | §1 之全部相符項；W-0c 之落檔與來源位元組相同；02 包 §1 之獨立複驗逐項一致 |
| **正確地不動** | 兩處疑似多位元組毀損 —— **實測無毀損，不逕改**（§7）；未裁定 R-VS7／R-VS9 v2／R-VS10；未執行 git |

---

## 6. 本輪未執行者（**具名，不假裝已做**）

| 作業 | 狀態 |
|---|---|
| W-8 三來源 `$變數$` 對照 | **未執行**。CFTS044 內嵌值域之抽取（兩式）尚未做 |
| W-13 26PI2.5/HMI 全文掃描 | **未執行**。目錄檔數已實測為 **107**（01 包所記「約 112」為目測） |
| W-15b′ DBC ↔ LID 逐屬性交叉 | **未執行**。本輪僅有 00 輪之 DBC↔DBC 比對 |
| W-17 LID 列數差 6／`TRUNCATED_ENUM` 其他形態 | **未執行** |
| W-9 Comfort 逐條對照 | **未執行**。其母體依 R-VS15 須改用 237 個 Functional leaf |

---

## 7. 位元層核對 —— **兩處皆無毀損**

| 位置 | 嚴格 UTF-8 解碼 | U+FFFD | 其後之實際碼位 |
|---|---|---|---|
| `ANOMALIES.md`「相異 259」後 | **通過** | 0 | `，`(U+FF0C) `亦`(U+4EA6) `非`(U+975E) ` 254）` |
| `handoff/00_intake_and_rulings.md` 之「沙」（3 處） | **通過** | 0 | 三處後皆為 `箱`(U+7BB1)，即「**沙箱**」 |

**repo 之位元組乾淨。** 分析層讀回時所見之 `沙??` 為**其端顯示或傳輸之產物**，
非檔案內容。**依指示回報而不逕改。**

---

## 8. 新開 anomaly 與 DR

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS20** | —（RD-1 FYI） | `Categorization` 大小寫不一致（`information` 一筆）。**影響 Information 側計數 8 vs 9，不影響 Functional 母體界定（皆 237）** |
| ~~A-VS01~~ | — | **除役** |
| ~~A-VS18~~ | — | **除役** |
| A-VS06 → **A-VS06′** | — | id 更正（內容已於 00 輪改寫） |

**無新開 DR。** DR-11（CFTS100）維持開啟，為 236/237 之外的那 1 個。

---

## 9. 未預期之發現

1. **`inputs/` 全目錄被 `.gitignore` 排除**（`features/vehicle_setting/.gitignore:2`），
   故 W-0c 所複製之 PDF 與更新後之 `INPUTS.sha256` **皆不入版控**。
   **素材落地之證據鏈在版控中是斷的** —— G-L 要求「有路徑」，現況有路徑但無版控痕跡。
   **不自行改 `.gitignore`**（禁區：不代擬條文、不自行調和）；提請 Pei 決定是否為
   `INPUTS.sha256` 開例外。
2. **26PI2.5/HMI 目錄實測為 107 檔**，非 01 包所記之「約 112」。02 包已接受以實測值取代。

---

## 10. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **§1.1 之十項「相符」為同源自我印證。** 分析層與執行層讀的是同一批 `inputs/` 檔案。
   本輪真正之跨源檢驗只有 §3.2（037 `Categorization` ↔ SYS2 `Category`）一處。
2. **R-VS15 之「036 之 237 列恰為 237 個 Functional leaf」尚未驗其反向。**
   已驗「兩集合相等」，**未驗「036 之 237 列各自對應到正確的那一個 Functional leaf」**
   —— 後者於 00 輪由 I／H／N 三欄之 237/237 逐字相等間接支持，
   但那是**投影正確性**之證據，非**列序正確性**之證據。
3. **`Categorization` 之值域未窮舉。** 本輪只見四種值；
   若某 037 版本另有第五種（如 `Constraint`、`Interface`），
   `startswith("functional")` 會把它歸入非 Functional 而不報錯（canon §5a 第 12 條）。
   **建議 W-16 之產物加一行：值域全集與其計數**（已於 §2 表列，但未宣告其為全集）。
4. **A-VS06′ 僅改 id，其內容之「差額 0」結論未再複驗。**
   00 輪量得 body heading 270 / 相異 270；本輪未重跑。

---

## 11. 給 Pei 之 git 指令草稿（**未執行，帶 pathspec**）

```bash
git add features/vehicle_setting/ANOMALIES.md \
        features/vehicle_setting/docs/upstream/01_leaf_universe.md \
        features/vehicle_setting/docs/INDEX.md
git commit -m "docs(vehicle_setting): round 01 upstream — leaf universe, A-VS01/18 retired, A-VS20 opened"
```

> **git 唯讀與改狀態分列**（R-G6）：本輪執行之 git 指令僅 `git status --porcelain`。
> **未執行任何 add／commit／checkout／restore／stash／clean／tag。**
