# 上繳 V19 —— pilot 批 10 條已生成（B 欄 238–247），PROXI 抽取式過窄

執行層寫入。依據：`docs/handoff/V19_pilot_start.md` §5。canon §8.2 六節。

**本輪為 VF230 之首次 TC 生成。**
**未執行任何寫回**（R-VF26）—— 產出落 `generated/`，不進工作簿。
**未生成第 2 批**（V19 §5.4）。

---

## 1. 交付總表

| 項 | 狀態 | 產物 |
|---|---|---|
| W-VF53 pilot 批 10 條 | **完成** | `generated/vf230_pilot1.json` |
| R-VF56／57／58 落檔 | **完成** | `RULINGS.md`（R-VF 現 **51 條**） |
| A-VF13 | **新開** | `ANOMALIES.md` |
| 並行 W-VF50／W-VF43／W-VF51／W-VF52 | **本輪前已完成** | 見上繳 V18 |

> **V19 §6 之並行工單清單須更正**：W-VF50／W-VF43／W-VF51／W-VF52 **四項皆已於
> 上繳 V18 完成**（委派 11 候選比對、146 處判線別、R-VF48 誤報 15→2、
> DR 兩套編號對照）。V19 成文時未見上繳 V18 —— **R-VF30／R-VF42 所防之形態再現。**

---

## 2. §1 之解讀確認：**取 P0 整類，無異議**

本層依 V19 §1 之解讀執行 —— pilot 批取**確認後之 P0 全體（88 leaf）**之池首 10 條，
非「限 P0(a) 九簇」。

**其結果使該解讀之差異可見**：10 條中 **7 條之標的為 P0(c) 之七簇或其同類**
（Blind Spot Alert／Lane Sense Warning／Park Sense／Blind Spot with Trailer
Detection 等），僅 3 條為 P0(a) 之實體致動類。
**若原意為「限 P0(a)」，本批之七成內容將不同。**

---

## 3. W-VF53 —— pilot 批

```
generated/vf230_pilot1.json     10 條     B 欄 238–247（連續）
Priority                        全 P0
Test Set                        8 個（Approach and Tailgate 2／
                                Driver Convenience 2／餘各 1）
writable                        W0 9 ／ W1 1
```

| # | leaf | Test Set | W |
|---:|---|---|---|
| 238 | `PowerLiftgate/TailgateAlert-016` | Approach and Tailgate | W0 |
| 239 | `BlindSpotAlert-002` | Driver Convenience | W0 |
| 240 | `LaneSenseWarning-014` | Lane and Lighting | W0 |
| 241 | `SuspensionServiceMode-002` | Suspension and Comfort | W0 |
| 242 | `Blind Spot with Trailer Detection-045` | Trailer and Signage | **W1** |
| 243 | `ParkSense-084` | Units and Cameras | W0 |
| 244 | `IlluminatedApproach-002` | Approach and Tailgate | W0 |
| 245 | `4AUXSwitches-027` | Auxiliary Switches | W0 |
| 246 | `DaytimeRunningLights-002` | Daytime Lighting | W0 |
| 247 | `PassiveEntry-009` | Driver Convenience | W0 |

**10 條同屬一形態**：PROXI 配置值決定該設定項是否顯示於 Vehicle Settings menu。
其可測結果為**選單項之有無**，非訊號斷言。

### 3.1 自檢（對照 V19 §5.3 之六項升級條件）

```
1 test_item 括號下半            10/10 有        ✅
2 R-1 v2 記法                   PROXI $P$ = "值"；Input Test Data 全為 NA   ✅
3 空欄／以 NA 充當未知           0               ✅
4 specification_reference       格式見 §3.2 —— **本層具名待確認**
5 Test Set 在已鎖 9 名內         10/10           ✅
6 畫面層敘述無素材來源可指        0 —— 其斷言為選單項之有無，來源即條文自身
其他：procedure 與 ER 步數逐條對齊；PENDING 僅出現於唯一之 W1 條
自檢失敗 0 項
```

### 3.2 ⚠ `specification_reference` 之形式係推得，非條文所定

本批採 **`VF230_V1-{n}`**，其 `n` 取自 037 之 `Source Requirement ID`
（`SYS-RA-VF230_V1-{n}`）。

**其依據為 Part 1 之實際慣例** —— Part 1 用 `CFTS044-{7 位 reqid}`，
即「去 `SYS-RA-` 前綴之來源 id」。VF230 之 037 **無 7 位 Polarion reqid**，
其來源 id 即 `SYS-RA-VF230_V1-{n}`。

**本層未查得任何條文定 VF230 之該欄形式** ——
`feature.yaml` 之 `spec_reference_template` 為 `<Spec Filename>_{outline}`
（spec_mode D），與 Part 1 之實作不符，二者本即不一致。

**V19 §5.3 第 4 項將此列為升級條件，故本層具名而不自行定案。**

### 3.3 W1 之一條

`Blind Spot with Trailer Detection-045` —— 其 `Blindspot_Trailer_Detection`
之允許值域不在 PROXI 表內（DR-34 之 11 參數之一），
步驟 1 之 ER 標 `PENDING: DR-34`，`dr_dependent = DR-34`。
**其餘二步可執行，故判 W1 而非 W2**（R-VS47／R-VS71）。

---

## 4. A-VF13 —— PROXI 抽取式過窄，**9 條之值域來源被誤記為「無」**

逐條讀來源條文時發現：10 條中 **9 條之 `value_source` 為「(無)」**，
而其條文實為 PROXI 取得型。

**W-VF44 之 `PROXI_REF` 僅認一式**（`retrieve the <X> PROXI configuration`），
漏下列變體：

```
retrieve the CAN node 82 (PTGM) PROXI configuration status     ← 含括號與 status
retrieve the [ DRL_Menu_Enable ] PROXI configuration status    ← 參數以方括號包夾
retrieve the AUX_Switch_Types configuration value              ← **無 PROXI 一詞**
```

**分級之結論偶然正確而依據錯**：該 9 條之正確分級確為 **W0**，
惟其理由應為「**條文自帶值**」（`[Absent]`／`[Not Present]`／`≠ [Type1]`
逐字載於條文），非「無訊號引用」。

**本輪未改分級、未改 `vf230_writability.tsv`** —— 其修法須重跑全量，屬下輪。
**pilot 批之 10 條已逐條人工確認其值域來源，故本批不受影響。**

---

## 5. R-VF58 之首次施行 —— **一個反向實例**

本條令「理由被更正者，結論須重新檢驗」。本輪之 A-VF13 為其**反向形態**：

```
W-VF44 之理由「252 leaf 之可測內容立於 PROXI 配置之取得」   —— 仍成立
其結論「該 9 條之值域無來源」                                —— 不成立
```

**理由未變，而結論因新事實（逐條讀條文）而不成立。**

→ **R-VF58 之步驟宜擴充**：不僅「理由被更正時檢驗結論」，
亦須「**取得新事實時檢驗既有結論**」。**建議納入。**

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **A-VF13 之影響面未測**（§4）。627 leaf 中有多少同受 PROXI 抽取式之漏，
   本輪未重跑。**其可能使 W1 之 28 條低估**（漏認之 PROXI 參數若不在表內，
   該 leaf 應為 W1 而現判 W0）。**此為本輪最須先辦者。**

2. **`specification_reference` 之形式未經確認**（§3.2）。10 條已用該形式寫出；
   若確認後之形式不同，**10 條皆須改**。

3. **本批 10 條同屬單一形態**（PROXI 決定選單項有無）。
   **pilot 之目的為驗證書寫形式之適用性，而單一形態只驗得一種形式** ——
   其餘形態（訊號斷言型、狀態轉換型、值域切換型）於本批**未受檢**。
   選池序（P0→逐 Test Set 輪流）使然，非本層所擇。

4. **R-VF57 之 P0(c) 界線在本批中受檢者為「有無」側**，
   而其 P1 側（音量／靈敏度／樣式）**本批無一條** ——
   **該界線之另一半未受 pilot 檢驗。**
