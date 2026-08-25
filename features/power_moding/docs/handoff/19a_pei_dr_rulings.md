# 下放包 19a —— Pei 之四項裁定（與 19 同一往返，須併讀）

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [19_broken_source.md](19_broken_source.md) 同屬第 19 輪，
  上繳仍為 `docs/upstream/19_broken_source.md`
- 19 本文未改一字

---

## 一、Pei 之裁定（2026-08-24，逐字）

> 「DR-PMH1 拿掉
> DR-PMH2 /Users/peihe/Work_Projects/TC_Generator/features/power_moding/inputs/Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421 (August 3 2022).xlsx
> DR-PMH3 037沒有納入就不放
> DR-PMH4 以刪掉之後的為主」

四筆 DR 一次結清。**四筆之處置各自推翻了一條既有條文，逐條見下。**

### 1.1 一項解讀須先講明（DR-PMH1）

「拿掉」有二解：**(甲) 該 DR 不發**，**(乙) 該列不放進工作簿**。

**採（乙）**。理由：同一則裁定中之 DR-PMH3 逐字為「**就不放**」，
DR-PMH2／DR-PMH4 亦皆為「內容如何定」之答覆，四者為同一形態之並列 ——
Pei 在裁的是**交付內容**，不是**是否發文**。

**若原意為（甲），一句話即可反轉**，其差別為：
（甲）該列仍寫入工作簿並以 `PENDING` 佔位、交付前仍阻斷；
（乙）該列不寫入工作簿、交付不再受其阻斷。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH72（`SWE1-HMI-PM-028` 不寫入工作簿）
Pei 於 2026-08-24 裁定「DR-PMH1 拿掉」。

`SWE1-HMI-PM-028`（outline 12.2，內文為 `OFF2.) Please refer to CFTS009 for
complete behavior.`）**不寫入交付工作簿**，不產出 TC，不以 `PENDING` 佔位。

**R-PMH47 之 (b)(c) 撤回**：
(b) 「該列仍寫入工作簿並揭露（比照 R-VF12）」—— 撤回；
(c) 「開 DR-PMH1」—— 撤回，該 DR 標 `CLOSED-BY-RULING`（未答覆而結案）。
**R-PMH47 之 (a)（判為 out of scope，不得為其撰寫驗證 CFTS009 行為之 TC）
維持有效** —— 本裁定只改其揭露方式，不改其 out of scope 之判定。

**repo 內部之紀錄不受本條影響**：`ANOMALIES.md` 之 A-PMH13、
`DECISIONS.md` 之登記、本條文本身**皆保留** ——
「拿掉」之範圍為**交付件**，非本 feature 之內部台帳（G-D：
「不做」與「沒發現」須在紙上分得開）。

**連帶（須重算，不得沿用）**：
  Layer 2 之 `Off Road Plus` 組由 3 leaf 降為 **2**（`-027`／`-029`）；
  有 TC 之 leaf 總數由 48 降為 **47**；
  granularity 之分母 `n_leaf` 隨之改變，G1–G5 須以 47 重跑。
分析層之對照值：8/47 = 0.170（G1 ✅）、min = 2（G2 ✅）、
max = 9/47 = 0.191（G4 ✅）、全組落 [2, 23]（G5 ✅）。
**先算後比，不得引用本行數字為結果。**
```

```
R-PMH73（Power Moding State Matrix 已到，DR-PMH2 結案）
Pei 於 2026-08-24 提供 DR-PMH2 所索取之文件：

  features/power_moding/inputs/Power Moding HMI State Matrix R1 SR24 Post 2A
  DCR21421 (August 3 2022).xlsx

該檔為本 feature 之**第六筆素材**，須依 R-PMH4 補入
`inputs/MANIFEST.sha256`（SHA256 ＋ `shasum -c` 通過方為到齊）。

**其效力**：PDF p10 逐字載 `Power Moding behavior shall not be developed
without following the Power Moding State Matrix` —— 該矩陣自此為
**ch 9（`Power Transitions` 組）之判讀背景，具規範性**，
非參考資料。ch 9 之 TC 撰寫須以其為據。

**A-PMH14 之新漏 2（p9 狀態矩陣於 SYS1 全缺）與新漏 3（p10 之
`POWER MODING STATE MATRIX:` 段於 SYS1 全缺）之補救來源自此確定** ——
二者不再是無解之缺口，而是「內容在另一份素材裡」。
**其 anomaly 不撤銷**（SYS1 匯出確實缺該內容，該事實不變），
狀態改為 `RESOLVED（來源已補）`。

**素材真確性**：該檔之 DCR 編號（`DCR21421`）與日期（`August 3 2022`）
**早於**規格 PDF（`DCR22412`／`January 24 2023`）—— 執行層須於上繳
具名此一事實並回報矩陣內容與 PDF p9／p10 是否一致；
**不一致者不得自行取捨，停並上呈。**
```

```
R-PMH74（`SU9.)`／`SU9.1)` 不納入，DR-PMH3 結案）
Pei 於 2026-08-24 裁定「037 沒有納入就不放」。

`SU9.)` 與 `SU9.1)` **不補入本 feature 之 leaf 母體**；
leaf 母體維持 **48**（R-PMH1 不變），`Disclaimer Screen` 維持 **7 leaf**。
`DR-PMH3` 標 `CLOSED-BY-RULING`。

**A-PMH14 之新漏 1 不撤銷** —— 「PDF 有而 SYS1／037 無」之事實不變，
其狀態改為 `ACCEPTED（經裁定不補）`。

**R-PMH55 之適用繼續成立** —— 該條原載「若 DR-PMH3 回覆為
『SU9／SU9.1 應在 037』，則本條之適用即告終止」。
**本裁定為其反面**，故 batch 1 之 `-003`／`-004` 依 PDF `SU9.1` 所加之
「不按任何硬鍵」限定**繼續有效**，其三項判準（作用為使既有 leaf 之驗證
正確、只出現於步驟限定子句、於 reasoning 具名）仍須逐條滿足。

**18 包所預先登記之四項連帶（Layer 2 計數、granularity 分母、
`layer3_sections.tsv`／`outline_map.json`、batch 1 增 2 條）全部不觸發。**
```

```
R-PMH75（outline 9.1 以 SYS1 為權威，DR-PMH4 結案）
Pei 於 2026-08-24 裁定「以刪掉之後的為主」。

outline `9.1` 之權威文本為 **SYS1 匯出之版本**（即已刪去 PDF 疊寫舊文字者），
**非 PDF**。

**R-PMH50 於 outline 9.1 反轉**：該條「`source_clause` 取自 PDF，
不取自 SYS1」於 `9.1` 之 5 個 leaf（`SWE1-HMI-PM-018-01`～`-05`）
**不適用**，其 `source_clause` 取自 SYS1；`source_clause_origin`
須逐字記 `sys1_export 9.1`，並註 `R-PMH75`。
**R-PMH50 於其餘 47 leaf 維持不變。**

**A-PMH16 之三處改判**：由「SYS1 漏字」改判為「**編輯後之定稿**」——
  (1) `for 60 seconds` —— 舊文字，已刪，**不驗**；
  (2) `seconds`（`within 60 seconds`）—— 舊文字，已刪，**不驗**；
  (3) `the radio should shut Off the` —— 舊文字，已刪，**不驗**。
A-PMH16 狀態改為 `RESOLVED（PDF 側為未刪淨之舊文字）`，**原文保留**
（R-PMH44）；其原判定「(1)(2) 為時序漏失、(3) 為獨立行為結果」
**逐條標記為已被本條推翻**。

**⚠ 承擔之風險須具名**：依本裁定，`the radio should shut Off`
（逾時後收音機關機）**不會有任何一條 TC 驗到**。
若上游日後主張該行為仍屬需求，本 feature 之 ch 9 覆蓋即有缺口 ——
**該風險由本裁定承擔，已於此具名。**

**`Power Transitions` 組解凍**（R-PMH69 之凍結解除），
惟其開批仍以 R-PMH73 之矩陣一致性查核通過為前提。
```

---

## 三、對 19 包之影響

| 19 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §五 R-PMH69 | 立條，`Power Transitions` 凍結 | **凍結解除**（R-PMH75）；R-PMH69 之條文**維持有效**，其判準留待下次「來源損壞」時適用 |
| §六 步驟 3（開立 DR-PMH4） | 待做 | **改為**：`DATA_REQUESTS.md` 四筆全部標結案狀態（`CLOSED-BY-RULING`×2、`RESOLVED`×1、`CLOSED-BY-RULING`×1），並記其裁定逐字 |
| §六 步驟 2（章 7／10／12 殘餘人讀） | 最高優先 | **維持最高優先** —— 不受本裁定影響 |
| §六 步驟 4／5／6／7 | 待做 | 維持 |
| §七 停止條件 7 | 章 7 殘餘發現漏字即停、batch 1 重做 | **維持** |

### 3.1 增列之作業步驟

8. **素材補入（R-PMH73）** —— 矩陣檔已在 `inputs/`
   （實測 100,941 bytes，mtime 2026-08-24 20:38）。
   補入 `MANIFEST.sha256`，`shasum -c` 須 **6/6 OK**。
   讀其分頁結構與內容（`read_only=True, data_only=True`，**不得 save**），
   回報：分頁清單、矩陣之列／欄維度、其狀態名與 PDF p9 之
   `HEADUNIT POWER OFF/ON`／`KEY ON ENGINE ON`／`KEY OFF (ACC)`／
   `KEY OFF (No ACC)` 是否逐字對應。**不一致即停。**

9. **`-028` 之移除（R-PMH72）** —— `Off Road Plus` 組由 3 降為 2；
   `layer3_sections.tsv` 與 `outline_map.json` **保留該列**（內部台帳），
   但於其加註 `EXCLUDED-BY-R-PMH72`；
   `check_granularity.py` 之 `n_leaf` 由 48 改為 **47** 並全項重跑
   （含六個 must-hit 錨點之期望值須隨分母重算）；
   `framework.md` 之 Layer 2 表與合計數改為 47 ＋ 一列註記。

10. **9.1 之 `source_clause` 換源（R-PMH75）** —— 本輪**只做準備不改 TC**：
    `Power Transitions` 組尚未開批，故無 TC 需改。
    於 `feature.yaml` 或 profile 之 §1 加註本例外，
    使開批時不會誤用 R-PMH50 之通則。**profile 之修改須經 Pei 核可
    （R-PMH46 之授權已用畢）—— 本輪只在 `DECISIONS.md` 登記，不動 profile。**

---

## 四、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH72 | `-028` 不寫入工作簿；R-PMH47(b)(c) 撤回；leaf 47 之連帶 | ✅ |
| R-PMH73 | State Matrix 已到，為 ch 9 之規範性判讀背景；第六筆素材 | ✅ |
| R-PMH74 | `SU9.)`／`SU9.1)` 不納入；R-PMH55 適用繼續成立 | ✅ |
| R-PMH75 | 9.1 以 SYS1 為權威；R-PMH50 於該處反轉；風險具名 | ✅ |

四條各管一事。R-PMH72／R-PMH75 為**部分撤回型**，其撤回與保留之範圍
已於條內分別明載。

**待 Pei 者**：§1.1 之解讀確認（若「拿掉」原意為「DR 不發」而非
「該列不放」，一句話反轉）；18／19 之 commit 授權。
