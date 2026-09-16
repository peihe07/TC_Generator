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

## 執行層回報（CAM-01，2026-09-16）

- R-G23 取號現查：`grep -rn "R-CAM"` 於全 repo（排除本包下放檔）無命中；
  `docs/fw036/RULINGS.sha.tsv` 之 prefix 清單為 `R-AM R-C R-DD R-G R-ICS R-PH
  R-PMH R-POP R-TM R-U R-VF R-VL R-VS R-VT`，無 `R-CAM`。`{live}` = 1 成立，
  三條實際號為 **R-CAM1／R-CAM2／R-CAM3**。
