# framework.md — Driver Distraction

狀態：**LOCKED**（Pei 裁准鎖定：下放包 03 §五；Layer 1 之 `Driver Distraction`
另由 **R-DD1** 定）。
Feature slug：`driver_distraction`
規範依據：IN §4.1（三層框架）、§4.1.5（僅 Layer 1 ＋ Layer 2 ＋ Layer 3）、
§4.2（Test Set）；FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）

**落檔註記（2026-08-28，下放包 14 §1.3）**：本檔於包 03 §五 提請、Pei 准，
惟包 04 起未列入任何一輪之任務表，**故遲至本輪始落**。
成因在分析層（未下落檔指令），非執行層漏做。
**pilot 4 則與 B1 10 則係在本檔不存在之下產出** —— 其 Test Set 已依
下放包 14 §六 T20a 對齊本檔（見 §變更紀錄）。

---

## Part I — Layer 1（Test Group，寫入工作簿）

```
Driver Distraction
```

依 **R-DD1**：取 037（FM-WI-FSM-037-A03）`Project Name` 欄實值。
CFTS022 章名 `Driver Distraction Lockout` 與 HMI spec 題名 `Driver Lockout`
**均不採** —— 037 為生成主驅動，Layer 1 從其命名。
寫入工作簿 Test Group 欄，全簿逐字一致。

---

## Part II — Layer 2（Test Set，寫入工作簿）

**六組，28 leaf 全分掛。** 下列六列逐字取下放包 01 §三 之草案、
經下放包 03 §五 提請並由 Pei 准鎖，下放包 14 §二 重申。

**閉合式（下放包 20 §四）**：**24 生成 ＋ 4 範圍外 ＝ 28**。
組數不變（**六組**）—— 組 6 之組名保留，其為 037 分組之事實；
**刪之則 28 之閉合無從交代**（R-DD25(d)／R-DD10(c)）。

| # | Test Set | leaf | 能力叢集 |
|---|---|---|---|
| 1 | `Body Off Init` | 001–002 (2) | 出眠初始化：Lock Out State 復位、process 終止後冷啟 |
| 2 | `Speed Monitoring` | 003–008 (6) | `$Speedometer$` 監看、≥5MPH 上鎖、≤3MPH 解鎖、訊號失效 |
| 3 | `Lockout Enforcement` | 009–012 (4) | Locked 態之存取阻擋、使用中之強制退出 |
| 4 | `Lockout Tables` | 013–016 (4) | Lockout Table 所列 feature 之逐項套用 |
| 5 | `Hong Kong Market` | 017–024 (8) | `Country_Code`=HK：自排 P 檔閘、手排手煞閘、輸入失效 |
| 6 | `Market Speed Gating` | 025–028 (4) | 5/3 MPH 門檻於市場條件下 —— **OUT OF SCOPE（R-DD25(b)）**；不生成 |

### ~~組 6 之 PENDING 拘束~~ —— **已由 R-DD25(b) 結案（下放包 20 §四）**

> ~~組名為市場中立之佔位措辭。DR-DD1 回覆前：組名不寫入工作簿任何列；
> DR-DD1 裁 HK → 併入組 5；DR-DD1 裁 LATAM → 更名 `LATAM Market`。~~
> **三項待決皆已消滅** —— 範圍裁定（R-DD25(a)）已定 LATAM 不在案，
> 該四列之歸屬不再取決於 DR-DD1 之回覆。

### 組 6 之 OUT OF SCOPE 拘束（現行）

- **組名保留，不刪組** —— 其為 037 分組之事實；刪之則 28 之閉合無從交代
- **不生成任何 TC；組名不寫入工作簿任何列**（拘束不變，理由改變）
- 差額之記錄義務由 `COVERAGE_GAPS.md` 之 **[CG-DD2]** 承接（R-DD25(d)）
- **不併入組 5** —— `-017`~`-024` 在案之依據為 RHD（R-DD25(a)(e)），
  與本組所依之 LATAM 需求無涉；**併組即把二個獨立維度混為一談**

（下放包 20 §二／§四；A-DD1 已 `CLOSED-BY-SCOPE`。）

### 反模式自查（IN §4.1.3）

- 28 leaf 分 6 組，**平均 4.7 leaf/組**（分組之母體為 037 之 28 列，
  **不因組 6 判範圍外而改** —— 分組為文件事實，範圍為裁定）
- 最小組 2 leaf（`Body Off Init`）為**真 outlier** —— 唯一之電源域行為，
  非逐 RD 立組（IN §4.1.3「Too granular」不成立）
- **無** `Misc`／`General`／`Unclassified`（「Too coarse」不成立）
- Decision test：以任一 Test Set 篩選工作簿，得 2–8 條之有意義叢集，
  非 1 條、非全簿

### 修訂途徑（下放包 14 §二）

對 Layer 2 之組名或邊界有實質異議者，**循 framework 修訂提出**，
**不得以 TC 欄位之既成事實變更之**。

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

依 IN §4.1.5：Layer 3 僅存本檔，不入工作簿、不併入 Test Set 名。
用途見 IN §4.1.4（TC 排序／sibling 判定／覆蓋分析／範圍漂移防制）。

座標為 **CFTS022 SYSRA 之 Heading 母號**（上游正式欄逐字值，可驗）：

| Layer 2 | CFTS Heading | 涵蓋 FR |
|---|---|---|
| `Body Off Init`／`Speed Monitoring`／`Lockout Enforcement` | `-110` Driver Distraction Lockout (SR23+) | 113–118 |
| `Lockout Tables` | `-119` Driver Distraction Lockout Tables | 120–121 |
| `Hong Kong Market` | `-123` Hong Kong Market Regulations | 125–129 |
| `Market Speed Gating` | `-130` LATAM Market Regulations（**依 CFTS 結構**；SWE1 內文歸 HK，見 A-DD1）| 132–133 |

### 範圍外之 CFTS 內容

CFTS022 另有 Volume／Personalization 等 **134 條 FR 不屬本 feature**：
SWE1 未分解即不生成（`bed_lowering` R-BLM6 同型之先例）。
惟本案之未分解者明顯屬他 feature 已有工作簿之範圍，**非懸置項，不登 coverage gap**。

`-112`（適用性總則）與 `-136`（Out of scope，Embedded NAV）SWE1 未引 ——
recon 時列覆蓋台帳註記即可。

---

## 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-28 | **初版落檔**（LOCKED）。Layer 2 六組逐字取經核准之草案 | 下放包 03 §五 Pei 准；下放包 14 §六 T20a |
| 2026-08-28 | 據本檔更正 B1 之 Test Set：`-003`~`-008` `Speed Threshold Judgment` → **`Speed Monitoring`**；`-013`~`-016` `Lockout Enforcement` → **`Lockout Tables`** | 下放包 14 §二 |
| 2026-08-28 | **組 6 `Market Speed Gating` 由 `PENDING（DR-DD1）` 改 `OUT OF SCOPE（R-DD25(b)）`**；閉合式改為 **24 生成 ＋ 4 範圍外 ＝ 28**；組名保留不刪組；「組 6 之 PENDING 拘束」節結案 | 下放包 20 §四 T26a |
