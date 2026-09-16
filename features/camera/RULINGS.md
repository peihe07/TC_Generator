# RULINGS — Camera（FW036）

裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2），執行層之回報另起段落。
取號依 R-G23／R-G62′：落檔當下 live 取號 —— 本檔建立時全 repo 無既存
`R-CAM` 條號（2026-09-16 現查 `docs/fw036/RULINGS.sha.tsv` 與各 feature
`RULINGS.md` 皆無），故自 1 起。條文來源：下放包 `docs/fw036/handoff/down/20260916_CAM-01.md` §2。

---

### R-CAM1 — 兩本 037 皆須產出；A 本先、B 本後；互為步驟來源（Pei 裁，2026-09-16）

```text
R-CAM1  兩本 037 皆須產出；A 本先、B 本後；互為步驟來源
  (a) A 本（SWRA_V02，25 列）與 B 本（RVC-HMI-V0.1，230 列）各出一本 FW036 工作簿。
  (b) 生成順序 A → B。A 本之畫面入口／設定 hop 一律引 B 本之 SYS1 HeadUnitCameraSystems 匯出，
      不得自造；B 本之訊號／PROXI 前提一律沿用 A 本已定之寫法。
  (c) 追溯各歸各母體（IN §8.4.2）：A 本 spec_reference 引 CFTS092／VF551，B 本引 SYS1 HMI L&F 章節；
      互參只參考寫法，不複製對方之 spec_reference。
```

### R-CAM2 — Vehicle Model 七欄以 1／0 填寫；598／5210 一律 0（Pei 裁，2026-09-16）

```text
R-CAM2  Vehicle Model 七欄以 1／0 填寫；598／5210 一律 0
  (a) 工作簿 `Vehicle Model 車型` 七子欄（HDCC27 Atl-Hi／DT27 Atl-Hi／VF(ProMaster)637 Atl-Mi／
      Commander (598) Atl-Mi／Regengade (5210) Atl-Mi／Toro(2261) Atl-Mi／Fastack (376) Atl-Mi）
      每列填 `1`（適用）或 `0`（不適用），不留空、不用其他符號。
  (b) `Commander (598)` 與 `Regengade (5210)` 已不支援，Camera 兩本一律 `0`。
  (c) 五個有效車型欄每列至少一個 `1`。lint 新增檢查項（本 feature profile [ADD]）。
```

### R-CAM3 — 車型軸之拆分判準（Pei 裁，2026-09-16）

```text
R-CAM3  車型軸之拆分判準
  同一驗證點，若 PROXI 前提值、觸發訊號名（Atl-Hi vs Atl-Mi 之 CAN 訊號）、或 ER 可觀察結果
  任一因車型而異 → 拆 sibling，各列只勾自己的車型（§8.3 mode 軸），
  test_item 括號下半以車型／EE 作區分 token；全部相同 → 一列，勾全部適用車型。
```

### R-CAM4 — Test Group 與 TC ID（Pei 裁，2026-09-16；取代審閱 §三-1 之「共用 CAM」）

```text
R-CAM4  Test Group 與 TC ID（取代審閱 §三-1 之「共用 CAM」）
  (a) A、B 兩本之工作簿 Test Group 欄一律為 `Rear View Camera`。
  (b) TC ID 分兩組序號：A 本 `NR1L-RVC-{nnn}`、B 本 `NR1L-RVCHMI-{nnn}`，各自自 001 起連號。
      R-G42 第二項之 ABBR 於本 feature 即為 `RVC`（A）／`RVCHMI`（B）；審閱 §三-1「共用 CAM」作廢。
  (c) 交叉參考索引以 SWE ID 互指，不以 TC ID 互指（兩組序號獨立）。
```

### R-CAM5 — 品牌軸：label 隨品牌而異者拆列，品牌寫入 Pre-Conditions（Pei 裁，2026-09-16）

```text
R-CAM5  品牌軸：label 隨品牌而異者拆列，品牌寫入 Pre-Conditions
  (a) HMI Settings List 標 `*` 之設定項，`*` 不入 hop；hop label 依 `Brand-Specific Names` 分頁取值。
  (b) 同一驗證點若 hop label 因品牌而異 → 拆 sibling（§8.3 mode 軸之品牌分支），
      Pre-Conditions 首行寫明品牌（例：`Vehicle brand is Ram`），Vehicle Model 七欄依該品牌之車型勾 1。
  (c) 品牌 ↔ 車型之對照由執行層自 `forms/SR24 R1 Market Configuration Table v1.6.xlsx` 提候選，
      列 DECISIONS [PROPOSED]，不得自 anchor 前綴或車名推定。
  (d) 本條與 R-CAM3 併讀：車型軸與品牌軸皆為拆分判準，二者同時成立時以車型軸為外層。
```

### R-CAM6 — B 本追溯母體 ＝ spec-index/cache 之 RVC+PAM 本（Pei 裁，2026-09-16）

```text
R-CAM6  B 本追溯母體 = spec-index/cache 之 RVC+PAM 本
  `SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021).xlsx` 以 `spec-index/cache/` 本
  （sha16 `1a0bef53c6de975c`，64 列）為 B 本 spec_reference 之母體；REF 本（`5a1c0ab24991dcb1`）
  於 MANIFEST note 記「同名異體，cache 本之真子集，不作追溯母體」。DR-CAM-c 結案。
```

### R-CAM7 — V4 Layer 3 以 Description 前導章節號向下繼承（Pei 裁，2026-09-16）

```text
R-CAM7  V4 Layer 3 以 Description 前導章節號向下繼承
  SYS2 VF551_V4 之 Layer 3 章節取 `D` 欄前導號（heading 列）向下繼承（321/321、60 章），
  不回查 docx。DR-CAM-b 結案。
```

### R-CAM8 — ENTER_CAMERA_SETTINGS 常數（Pei 裁，2026-09-16）

```text
R-CAM8  ENTER_CAMERA_SETTINGS 常數
  `ENTER_CAMERA_SETTINGS`（3 hops，§5.3）：
    `Press "Apps" on Menu Bar to open App Drawer` → `Select "Settings" in the App Drawer` → `Select "Camera"`
  第 3 hop 之來源：`forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`，`Settings` 分頁 row 464
  `13. Camera`（序號非 label；canon §5.8(c) 明列 HMI Settings List 為路徑來源）。
  ER：`The "Camera" settings screen is displayed`。DR-CAM-d 結案；FO §4 [ADD] 之 §5.3 承接完成。
```

### R-CAM9 — Out of Scope 來源之處置（Pei 裁，2026-09-16）

```text
R-CAM9  Out of Scope 來源之處置
  SYS2 Category 為 `Out of Scope`（含 `Out of scope`）之 32 個來源一律不作 spec_reference 錨；
  其中 `SYS-RA-VF551_V2-578`／`-580`（Radio 端「RVC display active」條件）得作
  `-010`／`-017`／`-023` 之 Pre-Condition 措辭來源，reasoning 註明出處。上游分類不重判。
```


---

## 平台 ↔ VF ↔ PROXI 對照（下放包 §2 附表，分析層實測 `forms/proxi/` 六本）

| Vehicle Model 欄 | forms/proxi | VF551 | EE |
|---|---|---|---|
| HDCC27 Atl-Hi | `HDCC28_ATL_HI`／`HDCC27_initial` | V2 (`PHDCC27` anchor)／V4 | Atl-Hi |
| DT27 Atl-Hi | `DT28_ATL_HI` | V2 (`PDT27` anchor) | Atl-Hi |
| 637 Atl-Mi | `Promaster_ATL_MI` | V42 | Atl-Mi |
| 2261 Atl-Mi | `Toro_ATL_MI` | V33 | Atl-Mi |
| 376 Atl-Mi | `Fastback_ATL_MI` | V3 | Atl-Mi |
| 598／5210 | 無 | 無 | 一律 0 |

## 執行層回報（CAM-02，2026-09-16）

- R-G23 取號現查：本檔現有 `### R-CAM1`～`R-CAM3`，全 repo 無 `R-CAM4` 以上；
  `docs/fw036/RULINGS.sha.tsv` 無 `R-CAM` 列（該表未重生）。`{live}` = 4 成立。
  下放包 CAM-02 §1 之五條實際號為 **R-CAM4／R-CAM5／R-CAM6／R-CAM7／R-CAM8**；
  同 §1 末之「Out of Scope 來源之處置」條下放包未給 `{live+n}` 佔位，
  執行層依落檔順序取 **R-CAM9**（下放包 §1 五個 code block 之後、
  「裁定 6／9／10 為 DECISIONS 項」之前，故列為第六條）。
- **R-CAM4(a) 取代 CAM-01 之 Layer 1 提案**：Test Group 由 `Camera` 改為
  `Rear View Camera`，兩本同值。CAM-01 DECISIONS §6-1／§6-2 之提案作廢。

## 執行層回報（CAM-01，2026-09-16）

- R-G23 取號現查：`grep -rn "R-CAM"` 於全 repo（排除本包下放檔）無命中；
  `docs/fw036/RULINGS.sha.tsv` 之 prefix 清單為 `R-AM R-C R-DD R-G R-ICS R-PH
  R-PMH R-POP R-TM R-U R-VF R-VL R-VS R-VT`，無 `R-CAM`。`{live}` = 1 成立，
  三條實際號為 **R-CAM1／R-CAM2／R-CAM3**。
