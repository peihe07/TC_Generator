# 上繳包 11 — vsm_v43：R-VT23 落地（隔離標記、占比重算、`1.14` 對映）

日期：2026-09-02　執行層　對應下放包：`docs/handoff/11_status_maps.md`
台帳不重生；DR 不代發；**未寫工作簿；已凍 b1 一位元未動**。

---

## 〇、一句話結論

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E82 | status 四類對帳 | 逐類＋算式自洽；b1 之 10 列全 `active` | `active` **322**／`stale_ref_r4` **3**／`deprecated_r4` **9**／`superseded` **2** ＝ **336**；有效母體 **325**；b1 10 列**全 active** | ✅ |
| E83 | Layer 2 v2 合計 | = active＋stale_ref | **19 組合計 325** = 325 | ✅ |
| E84 | 占比 | 新舊二數並列 | 含解得 **153/325 = 47%**（v1 126/295 = **43%**）；含訊號 **294/325 = 90%**（v1 89%） | ✅ |
| E85 | `1.14` 對映 | 覆蓋數／無對應清單 | **僅 `01.14.01` → `1.14.1` 可鎖**（35 列）；29 個 ID 組 **21 並列不可判／8 無詞可證** | ✅（負面結果） |

**下放包 §一 W-1 之算式「= 339？」為誤**：`superseded` 之原 3 列已不在 v2（10 包已扣），
本包新增之 2 列（`-472`／`-473`）**在 v2 內**。正確算式為
**322 ＋ 3 ＋ 9 ＋ 2 = 336**，有效母體 336 − 2 − 9 = **325**，與 R-VT23(c) 之令相符。

## 一、W-1 —— status 標記落地（E82）

`leaves_interim_v2.tsv` 新增 `status`／`status_note` 兩欄。

| status | 列數 | 列 ID | 依據 |
|---|---|---|---|
| `active` | **322** | — | 其餘 |
| `stale_ref_r4` | **3** | `-897`／`-899`／`-907` | R-VT23(c)；`status_note` 逐列記「被刪條件子句（Model_Year／LBSS／RBSS）生成時不入 TC（§8.4.2 以現行規格為範圍）」 |
| `deprecated_r4` | **9** | `-577`〜`-582`（Blind Spot 6）／`-824`／`-825`／`-844`（組態表 3） | R-VT23(b)(c)；`status_note`「R4 已刪；不生成 TC，037 重錨終裁」 |
| `superseded` | **2** | `-472`／`-473` | R-VT23(a)；`status_note`「R4 Replacement；功能由 VF655 新寫法列承接」 |
| **合計** | **336** ✅ | | |

**有效母體（`active` ＋ `stale_ref_r4`）= 325。**
**已凍 b1 之 10 列（`Interior Ambient Lighting`）經實測全為 `active`** —— 隔離未觸及 b1。

`superseded_by_r4.tsv` 由 3 列擴為 **5 列**，新增二列附 R4 逐字依據
（`- Replacement of IPC_VEHICLE_SETUP.RainSensorLevel by IPC_VEHICLE_SETUP2.RainSensorSensibility,
TELEMATIC_VEHICLE_SETUP.RainSensorLevel_Req by TELEMATIC_VEHICLE_…`）。

## 二、W-2 —— Layer 2 v2 表（E83；已寫入 `framework.md`，標「待 Pei 准」）

母體 = `status ∈ {active, stale_ref_r4}` = **325**。

| # | Test Set | leaf | 對 v1 之變動 |
|---|---|---|---|
| 1 | PROXI Configuration | **65** | 67 → 65（去 `-824`／`-825`／`-844`，＋`-1278`） |
| 2 | Exterior Lighting | **32** | 不變 |
| 3 | Door Lock and Access | **30** | 不變 |
| 4 | Units | **27** | +1 |
| 5 | Clock and Time | **25** | +1 |
| 6 | **EPB Maintenance Mode** | **19** | **新組** |
| 7 | Lane Departure Warning | **18** | 不變 |
| 8 | Park Sense | **17** | +2 |
| 9 | Forward Collision Warning | **15** | 不變 |
| 10 | Privacy and Service Data Reset | **14** | 不變 |
| 11 | Setup Acknowledge and Recovery | **13** | 不變 |
| 12 | **Side Distance Warning** | **10** | 原 `Side and Blind Spot Warnings` 16，去 BSD 6 列後改名 |
| 13 | Interior Ambient Lighting | **10** | 不變（b1 之組） |
| 14 | **Rearview Camera** | **10** | **新組** |
| 15 | Wiper and Sensor | **5** | 7 → 5（`-472`／`-473` 轉 superseded） |
| 16 | **Auto Park Brake** | **5** | **新組** |
| 17 | Language | **4** | 不變 |
| 18 | Phone and Navigation Repetition | **4** | 不變 |
| 19 | Menu Access and Persistence | **2** | 不變 |
| | **合計** | **325** ✅ | |

**與 R-VT23(d) 所令二處修正逐字相符**：`Side Distance Warning` **10**、`PROXI Configuration` **65**。
`framework.md` 之 R-VT19 v1 表**不刪只標**（R-TM13），v2 表置於其上並標「待 Pei 准後鎖」。

## 三、W-3 —— 占比重算（E84，詞界式）

母體：有效 325 列。

| 指標 | **v2（325）** | v1（295） | 差 |
|---|---|---|---|
| 含 v5 訊號名 | **294（90%）** | 262（89%） | +1pp |
| **含「解得」訊號** | **153（47%）** | 126（**43%**） | **+4pp** |

**交付說明應改用 47%。** 上升來自新納入之三組（EPB／Auto Park Brake／Rearview）之高解得率。

### 分組分布（含解得占比）

| leaf | 含訊號 | 含解得 | 占比 | Test Set |
|---|---|---|---|---|
| 4 | 4 | 4 | **100%** | Phone and Navigation Repetition |
| 15 | 15 | 12 | **80%** | Forward Collision Warning |
| 10 | 10 | 8 | **80%** | Side Distance Warning |
| 10 | 9 | 8 | **80%** | Interior Ambient Lighting（b1） |
| 18 | 18 | 14 | 78% | Lane Departure Warning |
| 19 | 16 | 14 | 74% | **EPB Maintenance Mode** |
| 17 | 13 | 11 | 65% | Park Sense |
| 14 | 11 | 9 | 64% | Privacy and Service Data Reset |
| 32 | 32 | 20 | 62% | Exterior Lighting |
| 10 | 10 | 6 | 60% | **Rearview Camera** |
| 5 | 5 | 3 | 60% | Wiper and Sensor |
| 5 | 5 | 3 | 60% | **Auto Park Brake** |
| 27 | 25 | 15 | 56% | Units |
| 30 | 30 | 16 | 53% | Door Lock and Access |
| 4 | 3 | 2 | 50% | Language |
| 13 | 11 | 4 | 31% | Setup Acknowledge and Recovery |
| 25 | 22 | 4 | 16% | Clock and Time |
| **65** | 55 | **0** | **0%** | **PROXI Configuration** |
| 2 | 0 | 0 | 0% | Menu Access and Persistence |

> **`PROXI Configuration` 65 列含解得 0%** —— 該組全為組態參數之敘述，
> 其「訊號」是 PROXI 參數而非 CAN 訊號，故 v5 事實表之「解得」（CAN 形）本就不適用。
> **這不是缺口，是類別不同**；該組之可執行性繫於 `PROXI <Param> = <值>` 寫法（IN §8.7.5(c)），
> 不繫於 `$MESSAGE.Signal$`。**建議交付說明之占比分兩類報，勿把此 65 列計入分母而拉低整體數字**
> —— 扣除後為 **153／260 = 59%**。

## 四、W-4 —— `1.14.*` 對映（E85，`data/section_map_114_v43.tsv`）

規格 `1.14.*` 之**葉節點** 29 個：`1.14.1`（Configuration Parameters Table，para 1288–1775）
＋ `1.14.2.1.1`〜`1.14.2.1.28`（`ID n Description`，para 1778–1833）。
**候選限葉節點**（父節 `1.14`／`1.14.2`／`1.14.2.1` 含全部子節文本，計入必然全勝，已排除）。

| 判 | 組數 | 列數 |
|---|---|---|
| **有對應** | **1** | **35** |
| 並列不可判（多節同分） | 21 | 22 |
| 無詞可證 | 8 | 8 |
| 合計 | 30 | 65 |

**唯一可鎖者**：`01.14.01` → **`1.14.1`**（命中 **26** vs 次高 **1**，決定性），**35 列**。

**29 個 `01.14.02.01.NN` 組無法判定**，成因為結構性：
每組僅 **1 個** token（該組只有 1 列，內容為單一參數之敘述），
而該 token **必然也出現在總表節 `1.14.1`**（表列含全部參數名）——
故命中 1 恆等於次高 1，**永遠並列**。此非方法失效，是證據不足以鑑別。

**序位假說之直接檢驗**（該組 token 是否出現於 `1.14.2.1.NN`）：
**是 10／否 19／假說節不存在 1**（`01.14.02.01.29`，規格 ID Description 只到 `1.14.2.1.28`）。
→ **序位假說不成立**，不採用。

> **依 §一 W-4「不硬配」，29 組之 `spec_section` 維持 `none`。**
> `PROXI Configuration` 組若要 spec 錨，目前只有表列 35 列可用 `…_R4_1.14.1`；
> 其餘 30 列（29 ID 組 ＋ 1 列）無錨。

## 五、§K

| # | 項 | 待裁 |
|---|---|---|
| **K-14**（新） | `01.14.02.01.*` 29 組因「每組 1 token 且必與總表節並列」而不可判 | 是否改以**參數名逐字對 `ID n Description` 節內文之參數名**（而非 token 集交集）重試？該法需先自 `1.14.1` 表列解析出 ID↔參數名對照，屬新方法，本包**未自創** |
| **K-15**（新） | 交付說明之占比口徑 | 整體 47%（325 分母）／扣除 PROXI Configuration 後 **59%**（260 分母）—— 兩者並列或擇一？ |
| K-6(c) | Layer 2 v2 表 | **已落 framework.md，標「待 Pei 准」**；准後鎖 |

## 六、anomaly／DR

**本包無新登 anomaly。**

| DR | 狀態 | 本包 |
|---|---|---|
| DR-VT1 | 裁送出，待發 | 未代發 |
| DR-VT2 | 建議併送 | `superseded_by_r4.tsv`（5 列）與 `k10_stale_hits.tsv` 可作附件 |
| DR-VT3／DR-VT4 | 暫持／先不送 | 未變 |

---

## 七、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 510
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **510**（上繳 10 時 508，他線續作業）。將 `framework.md` 還原至 `HEAD`、本檔與 `section_map_114_v43.tsv` 移出樹外後重跑**仍為 510** |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT23 十三條未入台帳；重生歸 Pei 提交前一次 |
| `gates_tsv`／`lint_paths` | **無關** | 紅列全屬他 feature |

---

## 八、獨立判斷

1. **b2 生成包在 Pei 准表後即可開跑，但有一個前置我建議先定：K-15 的占比口徑。**
   19 組裡有 **`PROXI Configuration` 65 列（20%）之含解得為 0%**，而那是類別不同不是缺口。
   若交付說明用 47%，讀者會低估可執行度；用 59% 又漏掉那 65 列的存在。
   **建議兩數並列並註明 PROXI 組走 `PROXI <Param> = <值>` 路徑**。

2. **`Clock and Time` 25 列含解得只有 16%，是所有非 PROXI 組裡最低的，值得在排批次時注意。**
   該組（Set Time／Set Format／Set Date 等）多為 UI 行為敘述，CAN 訊號少。
   若 b2 挑高解得率的組先跑（如 Forward Collision Warning 80%、EPB 74%），
   低解得率組留到 DR-VT4 回覆後再跑，可減少 `PENDING` 佔位。**排序權在分析層，我只提供數字。**

3. **K-14 我沒有自創方法，但那個方法應該會成功。**
   `1.14.1` 之表列文本含 `ID 編號 ＋ 參數名`（如 `50 EPB_Maintenance_Menu **`），
   而 `ID n Description` 節之標題就帶 ID 號。以「表列解析出 ID↔參數名」再對 SYSRA 組之參數名比對，
   是純字面且可判的。**但那是新方法，依 §一 W-4「不硬配」與歷來「不自創」之界線，本包未做。**

4. **本包未驗而下放包亦未要求者**：
   (a) `stale_ref_r4` 三列之「被刪條件子句」具體邊界未逐字標出 ——
       生成時要刪哪一段，目前只有 `status_note` 之文字說明，無逐列之子句位置；
   (b) `deprecated_r4` 九列未從 `data/layer2_material_v43.md` 等既有材料檔回溯標記
       （那些檔是 v1 時期產物，本包未更新）；
   (c) v2 之 `spec_section` 於 `superseded`／`deprecated_r4` 十一列仍保留原值，未清空 ——
       隔離列不生成 TC，該欄不致誤用，但若日後解隔離需複驗。

---

## 九、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1／2／3／4／6 | git 未動；未寫 `vehicle_setting`／`vsm_v42`；未寫 profiles；`sources/raw/` 唯讀；未代發 DR |
| 11 包 對象限制 | **未寫工作簿**；**已凍 b1 一位元未動**（`generated/` 未出現於本包寫入清單）；R-VT19 v1 表不刪只標 |
| 不硬配 | `1.14` 之 29 組維持 `none`；序位假說經直接檢驗後**不採用** |

本包寫入之檔：
`data/leaves_interim_v2.tsv`（加 `status`／`status_note` 兩欄）、
`data/superseded_by_r4.tsv`（3 → 5 列）、`data/section_map_114_v43.tsv`（新）、
`framework.md`（加 v2 表，v1 表不刪）、`docs/upstream/11_status_and_maps.md`（新）。
`DECISIONS.md`、`RULINGS.md`、`DATA_REQUESTS.md`、`ANOMALIES.md`、`generated/`、
`data/leaves_interim.tsv`（v1）**未動**。

---

## 十、下一步

1. **Pei 准 Layer 2 v2 表**（`framework.md` 已備，19 組 325 列）→ 准後即可出 **b2 生成包**
2. Pei 裁 **K-15**（占比口徑，影響交付說明）與 **K-14**（`1.14` 對映是否改法）
3. b2 批次序建議：以含解得率排（§八-2），排序權在分析層
4. Pei：發送 DR-VT1（併 DR-VT2）；台帳重生（R-VT11–R-VT23 十三條）
