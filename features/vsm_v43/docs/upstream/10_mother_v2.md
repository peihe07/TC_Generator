# 上繳包 10 — vsm_v43：暫代母體 v2 建檔（R-VT22 甲案）＋ K-10 回掃

日期：2026-09-02　執行層　對應下放包：`docs/handoff/10_mother_v2.md`
台帳不重生；DR 不代發；**未寫工作簿；已凍 b1 與 v1 皆一位元未動（E77 已驗）**。

---

## 〇、一句話結論

**v2 = 336 列，算式逐項對帳相符；19 組無處可放 0；K-10 回掃出 14 列涉及 R4 已刪除／已取代之內容。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E73 | v2 列數 | 295 − 3 ＋ (38＋5) ＋ 1 | **336**（292＋38＋5＋1），算式 = 336 | ✅ |
| E74 | Layer 2 v2 | 各組合計 = E73；無處可放 = 0 | **合計 336**；**無處可放 0** | ✅ |
| E75 | `spec_section` 覆蓋 | 三類計數 | `segment_map` **195**／`none` **99**／`direct` **42** | ✅ |
| E76 | K-10 | 修訂項數／可機掃／命中 | **28 項**／可機掃 **8**／命中 **16 列次、14 相異列** | ✅ |
| E77 | b1／v1 | b1 一位元不動；v1 未覆寫 | b1 **21 檔 cmp 差異 0**；`leaves_interim.tsv` 與 HEAD 逐位元相同 | ✅ |

**§四升級條件皆未觸**：無處可放 0（故無硬配）；`segment_map` 所用偏移值 **{0, 1, 2, 3}** 全數見於
`section_map_v43.tsv`（無新造值）；b1／v1 零寫入。

## 一、W-1 —— 母體 v2（`data/leaves_interim_v2.tsv`）

### 合成對帳（E73）

| 來源 | 列數 | 依據 |
|---|---|---|
| 295 批保留 | **292** | (i) 128 逐字重複對取 295 側；(iii) 扣除 3 列 superseded |
| VF655 無對應 | **38** | (ii) |
| VF655 近似對 | **5** | (ii)，以 `k6_vf655_vs_interim.tsv` 之對號實取，**未重判** |
| DocID 空獨有 | **1** | (iv)（`-1278`，`01.14.02.01.28`） |
| **合計** | **336** | 算式 295 − 3 ＋ (38＋5) ＋ 1 = **336** ✅ |

落於 R-VT22(a) 之預期區間 336–339 之下界。

### superseded 3 列（`data/superseded_by_r4.tsv`，R-TM13 不刪只標）

| 廢止列（295） | chapter | 取代列（VF655） | R4 修訂說明逐字 |
|---|---|---|---|
| `-475` | `01.11.01.01.07` | `-994` | `- Replacement of IPC_VEHICLE_SETUP.RainSensorLevel by IPC_VEHICLE_SETUP2.RainSensorSensibility, …` |
| `-570` | `01.11.01.01.14` | `-1074` | （對 4：VF655 側多 `IF "Brand_configuration_2" == "Jeep" THEN` 前綴；**非 Replacement/Deleted 型**） |
| `-597` | `01.11.01.01.18` | `-1094` | `- Deleted Model_Year PROXI parameter` |

### `spec_section` 推導（E75，R-VT22(c)）

| 來源 | 列數 | 規則 |
|---|---|---|
| `direct` | **42** | VF655／nodocid 批之 `chapter` 即規格節號（08 包實證偏移 0）；限 `1.11.1.1.*` |
| `segment_map` | **195** | 295 批依 `coverage_union_v43.tsv` 之有效對映（命中 ≥ 3）逐 chapter 換算 |
| `none` | **99** | 無有效對映者 |

**`segment_map` 所用之偏移值集合 = {0, 1, 2, 3}**，全數見於 `section_map_v43.tsv`；
**未出現任何 section_map 未載之偏移**（§四升級條件之一，未觸）。

`none` 99 列之 chapter 分布（逐列見 TSV）：

| chapter | 列數 | 原因 |
|---|---|---|
| `01.14.01` | 38 | 組態參數表，不在 `1.11.1.1.*` 框內 |
| `01.14.02.01.01`〜`.29` | 29 | 同上 |
| `01.11.01.01.15` | 6 | 295 批獨有之 chapter，**規格無對應節**（Blind Spot；見 §三 K-10 段 21／26） |
| `01.11.01.01.07` | 5 | 命中 2 < 3，未達有效門檻 |
| `01.11.01.01.31`／`.32` | 各 4 | 同上（命中 1／0） |
| `01.13.02.01.01`〜`.03` | 5 | TBM 側，對應 `1.11.1.2.*`，不在框內（09 包 K-8） |
| `01.11.01.01`（根） | 2 | 真離群（R-VT19 第 15 組） |
| `01.11.01.01.22`／`.23` | 各 2 | 命中 2 < 3 |
| `01.11.01.01.10` | 1 | 命中 9 但其 top1 為 `.10.2`，本列 chapter 自身無獨立對映 |

## 二、W-2 —— Layer 2 v2 各組列數（E74）

**執行層只出列數，不定表、不命名**（R-VT22(b)：分析層定表、Pei 准後鎖）。

| # | Test Set | v2 列數 | v1 列數 | 增量 |
|---|---|---|---|---|
| 1 | PROXI Configuration | **68** | 67 | +1（`-1278`） |
| 2 | Exterior Lighting | **32** | 32 | 0（＋AHB 2 −舊 2） |
| 3 | Door Lock and Access | **30** | 30 | 0 |
| 4 | Units | **27** | 26 | +1（FuelCons） |
| 5 | Clock and Time | **25** | 24 | +1（`01.08.03`） |
| **6** | **EPB Maintenance Mode** | **19** | — | **新組** |
| 7 | Lane Departure Warning | **18** | 18 | 0 |
| 8 | Park Sense | **17** | 15 | +2 |
| 9 | Side and Blind Spot Warnings | **16** | 16 | 0 |
| 10 | Forward Collision Warning | **15** | 15 | 0 |
| 11 | Privacy and Service Data Reset | **14** | 14 | 0 |
| 12 | Setup Acknowledge and Recovery | **13** | 13 | 0 |
| 13 | Interior Ambient Lighting | **10** | 10 | 0（**b1 之組，未增減**） |
| **14** | **Rearview Camera** | **10** | — | **新組** |
| 15 | Wiper and Sensor | **7** | 5 | +2（RainSensor） |
| **16** | **Auto Park Brake** | **5** | — | **新組** |
| 17 | Language | **4** | 4 | 0 |
| 18 | Phone and Navigation Repetition | **4** | 4 | 0 |
| 19 | Menu Access and Persistence | **2** | 2 | 0 |
| | **合計** | **336** ✅ | 295 | **+41** |

**無處可放 = 0。** 歸組以 `spec_section` 為橋（節 ↔ 功能一對一），
無 `spec_section` 者依 chapter 前綴（`1.14.*` → PROXI Configuration、`1.13.*` → Setup Acknowledge and Recovery、
根 → Menu Access and Persistence）與 R-VT22(b) 之明列規則。

> **`Interior Ambient Lighting` 10 列未增減** —— 已凍之 b1 所依之 10 leaf 在 v2 中原封不動，
> 其 `spec_section` 經 `segment_map` 換算為 `1.11.1.1.27`（Δ=+1），與 08 包之強列一致。

## 三、W-3 —— K-10 回掃（`data/k10_stale_hits.tsv`，只報不修）

R4 修訂說明整節（para 9–68）以 `-` 起首之項目 **28 項**；
可機掃（Replacement/Deleted 型且含具名 token）**8 項**；**命中 16 列次、14 相異列**。

### 命中清單

| 修訂項（逐字） | 掃描之舊名 | 命中列 |
|---|---|---|
| `- Replacement of IPC_VEHICLE_SETUP.RainSensorLevel by IPC_VEHICLE_SETUP2.RainSensorSensibility, TELEMATIC_VEHICLE_SETUP.RainSensorLevel_Req by …` | `TELEMATIC_VEHICLE_SETUP.RainSensorLevel_Req` | **`-472`／`-473`** |
| `- Deleted IPC_VEHICLE_SETUP.BSDEnable, TELEMATIC_VEHICLE_SETUP.BSDEnable_Req CAN signals` | `IPC_VEHICLE_SETUP.BSDEnable`／`TELEMATIC_VEHICLE_SETUP.BSDEnable_Req` | **`-582`／`-579`／`-580`／`-581`** |
| `- Deleted Model_Year PROXI parameter` | `Model_Year` | **`-844`**（組態表列）／**`-907`** |
| `- Deleted ID14 (CAN node 51(LBSS))` | `CAN node 51 (LBSS)` 之 token | **`-577`／`-578`／`-824`／`-897`** |
| `- Deleted ID15 (CAN node 52(RBSS))` | `CAN node 52 (RBSS)` 之 token | **`-577`／`-578`／`-825`／`-899`** |
| `- Deleted "Units_Setting.Req" internal signal` | `Units_Setting.Req` | 無命中 |
| `- Deleted Units_settings.req internal signal` | `Units_settings.req` | 無命中 |
| `- Deleted BLIND SPOT ALERT menu` | `BLIND`／`SPOT`／`ALERT` | 無命中（**見下之抽取限制**） |

### 不可機掃 20 項

皆為 `- Added …`（14 項）、`- Updated …`（2 項）、`- Modification of …`（1 項）、
`- Removal of requirements related to …`（1 項）、`- Added … as a condition …`（2 項）型 ——
**無「舊名」可掃**（Added 型之名本就該存在；Updated／Modification 型未指名被改之字串）。逐項照列於 TSV。

### 抽取限制（如實揭露）

`- Deleted BLIND SPOT ALERT menu` 之 token 抽取得 `BLIND`／`SPOT`／`ALERT` 三個裸詞，
而需求文本寫作 `Blind Spot`（大小寫不同、非底線連綴），詞界式逐字比對故無命中。
**但該項之實質命中已由「段 21 Deleted …BSDEnable」之 4 列涵蓋**（同一功能）。
**不調整抽取式、不放寬比對**（R-VT22(d)「只報不自修」）。

### 觀察（陳述，不定性）

- **`-472`／`-473` 與 VF655 之新寫法列並存於 v2**：v2 同時含 295 批之
  `TELEMATIC_VEHICLE_SETUP.RainSensorLevel_Req`（舊）與 VF655 批之
  `IPC_VEHICLE_SETUP2.RainSensorSensibility`（新，`.07` 之 2 列無對應者）。
  R-VT22(a)(iii) 只令廢 `-475` 一列（該列為近似對之對 1），
  **`-472`／`-473` 不在近似對中，故未被廢** —— 版次衝突留存於 v2。
- **`01.11.01.01.15`（Blind Spot，6 列）於規格無對應節**，且 R4 兩處修訂說明
  （段 21 刪 BSDEnable 訊號、段 26 刪 BLIND SPOT ALERT menu）均指其已刪除。
  該 6 列中 4 列經 K-10 命中。

## 四、W-4 —— framework／DECISIONS 加註

- **`framework.md` Layer 2 節**：R-VT19 之十六組表 **不刪只標**，其上加 R-VT22(b) 加註 ——
  v2 336 列、19 組（三新組列數）、**表待分析層定／Pei 准**、`spec_section` 三類計數。
- **`DECISIONS.md`**：母體列新增 **3″**（v2，336，`[AUTO]` 落實 R-VT22），
  第 3／3′ 列**不刪**（R-TM13）；Sign-off **未動**。

## 五、E 對照

見 §〇。E77 之驗法：b1 之 21 檔逐檔 `git show HEAD:<path> | cmp -s -` → **差異 0**；
`leaves_interim.tsv` 之 `git diff --name-only` → **空**。

## 六、§K

| # | 項 | 待裁 |
|---|---|---|
| **K-11**（新） | **v2 內存在版次衝突**：`-472`／`-473`（舊 `RainSensorLevel_Req`）與 VF655 之新寫法列並存；R-VT22(a)(iii) 只涵蓋近似對，未涵蓋此二列 | 是否比照 superseded 廢除？或保留待 037 重錨時處理 |
| **K-12**（新） | **`01.11.01.01.15`（Blind Spot 6 列）於規格無對應節，且 R4 兩處明載已刪** | 是否自 v2 移除（→ 330）或標為 `deprecated` 保留 |
| **K-13**（新） | K-10 之 14 列涉及 R4 已刪除／已取代之內容（含 Model_Year、LBSS／RBSS 組態） | 逐項裁；其中 `-824`／`-825`／`-844` 為組態參數表列，`-897`／`-899`／`-907` 為條件敘述 |
| K-6(c) | Layer 2 v2 之表 | **列數已出**（§二 19 組）；表由分析層定、Pei 准 |

## 七、anomaly／DR

**本包無新登 anomaly。**

| DR | 狀態 | 本包 |
|---|---|---|
| DR-VT1 | 裁送出，待發 | 未代發 |
| DR-VT2 | 建議併送（定性已由 R-VT22(e) 更新） | superseded 3 列與 K-10 之 14 列可作附件 |
| DR-VT3 | 暫持 | 未變 |
| DR-VT4 | 先不送 | 未變 |

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 507
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 上表所嵌之 gate 跑得 507；歸因複跑時基線已為 **508**（他線於本包執行期間持續作業）。將本包六份產出全數移出／還原至 `HEAD` 後重跑**仍為 508** → 本包貢獻 **0**。計數漂移不動搖此結論（移除歸因法為直接證據） |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT22 十二條未入台帳；重生歸 Pei 提交前一次 |
| `gates_tsv`／`lint_paths` | **無關** | 紅列全屬他 feature |

---

## 九、獨立判斷

1. **v2 解決了 K-9，但把 K-10 的問題留在裡面。**
   三個功能（EPB 19／Auto Park Brake 5／Rearview Camera 10）現在有組了，零覆蓋消失。
   但 K-10 回掃顯示 v2 仍有 **14 列**帶著 R4 已刪除／已取代之內容，
   其中最尖銳的是 **Blind Spot 那 6 列（K-12）** —— 規格根本沒有那一節，
   R4 兩處修訂說明都說刪了，而它們現在是 `Side and Blind Spot Warnings` 組的一部分。
   **若不處理，暫代期會為「已被刪除的功能」產出 TC。**

2. **K-11 是 R-VT22(a)(iii) 的規則邊界問題，不是執行偏差。**
   (iii) 只處理「近似對」中的同功能新舊對。而 `-472`／`-473` 與 VF655 新寫法列
   之間**不是近似對關係**（VF655 側那 2 列在 09 包被歸為「無對應」），
   所以規則掃不到它們。**規則本身沒錯，是覆蓋面不足。**

3. **`spec_section` 有 99 列是 `none`，其中 67 列是組態表，那是結構性的。**
   `1.14.*` 的 67 列本來就不在 `1.11.1.1.*` 框內 —— 它們對應規格的
   `Configuration Parameters` 節（para 1287 起），本包未建該節之對映。
   若 P4 要為 PROXI Configuration 組寫 spec 錨，**需另建 `1.14.*` ↔ 規格組態節之對映**。

4. **本包未驗而下放包亦未要求者**：
   (a) 128 列逐字全等者之版次未查（09 §十-2 之未竟項仍未竟）——
       K-10 只掃「舊名出現」，掃不到「新名未出現」型的過時；
   (b) v2 之 `n_signals`／`n_solved_signals` 兩欄沿用各批原值，**未對 v2 重算**
       （VF655 批之值是在 08 包以同一 v5 事實表算的，可比；但 43 新列從未進過
       「含解得占比」之統計）——**交付說明之 43% 是 v1 的數字，v2 需重算**；
   (c) 三新組之 `spec_section` 皆為 `direct`，其正確性繫於 08 包之偏移 0 實證，
       本包未再獨立複驗。

---

## 十、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1／3／4／6 | git 未動；未寫 profiles；`sources/raw/` 唯讀；未代發 DR |
| 00 包 §零 2 | 未寫、未讀 `vehicle_setting`／`vsm_v42` |
| 10 包 §四 | **無處可放 0**（無硬配）；`segment_map` 偏移 ⊆ {0,1,2,3} 皆見於 section_map；**b1 21 檔 cmp 差異 0、v1 未覆寫**（E77） |
| 不寫工作簿 | 未寫 |

本包寫入之檔：
`data/leaves_interim_v2.tsv`（新）、`data/superseded_by_r4.tsv`（新）、`data/k10_stale_hits.tsv`（新）、
`framework.md`（加註，R-VT19 表不刪）、`DECISIONS.md`（加 3″ 列，3／3′ 不刪、Sign-off 未動）、
`docs/upstream/10_mother_v2.md`（新）。
`data/leaves_interim.tsv`、`generated/`、`RULINGS.md`、`DATA_REQUESTS.md`、`ANOMALIES.md` **未動**。

---

## 十一、下一步

1. **分析層定 Layer 2 v2 表 → Pei 准後鎖**（列數已備，§二）
2. **Pei 裁 K-11／K-12／K-13** —— **K-12（Blind Spot 6 列）最急**，它直接決定會不會為已刪功能生成 TC
3. 重算 v2 之「含解得訊號占比」（§九-4(b)）——交付說明之 43% 是 v1 數字
4. 若 PROXI Configuration 組要 spec 錨，需另建 `1.14.*` ↔ 規格組態節之對映（§九-3）
5. Pei：發送 DR-VT1（併 DR-VT2）；台帳重生（R-VT11–R-VT22 十二條）
