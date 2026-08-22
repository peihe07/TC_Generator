# 36 下放包 — framework 簽核（P19）與鎖定

分析層寫入，2026-08-20。Pei 於 2026-08-20 簽核 framework（Tier 2）。

---

## 1. 簽核之標的與範圍

```
P19（Pei 2026-08-20：簽核）
`features/vehicle_setting/framework.md` 之三層結構定案並鎖定：

  Layer 1  `Vehicle Setting`（R-VS3′）
  Layer 2  `Common Features` 46／`Heated Seat` 88／`Vented Seat` 72／
           `Heated Steering Wheel` 31 ＝ 237（R-VS4、R-VS15）
  Layer 3  19 個，依 R-VS37′ 四分支以 CFTS044 章節判定

簽核之依據（皆已實測）：
  Layer 2 歸屬以 037 檔界逐 leaf 驗證，**0 / 237 不一致**（16 輪 W-52）
  Layer 2 四數與 R-VS15 逐項相符
  左右對稱 HeatedSeat 15/15、VentedSeat 15/15
  分支使用 (1)231／(2)2／(3)3／(4)1 ＝ 237
  token 判定與章節判定不一致者 2，皆逐筆記明依據

**簽核不涵蓋**（各自另有其關卡）：
  TC 內容（pilot review）
  委派狀態之逐 leaf 正確性（R-VS7(a)′ 為群層級）
  未結 DR 之答覆
```

---

## 2. 鎖定前最後三項之處置

### 2.1 阻塞項 8（`SwitchLHD/RHDConfiguration` 之 `/`）—— **不阻塞，收斂**

實測其影響範圍：

| 用途 | Layer 3 是否進入 | 結論 |
|---|---|---|
| 工作簿欄位 | **否**（canon §4.1.5：Layer 3 不出工作簿） | 無影響 |
| `tc_id` | **否**（canon §10.3：`{project}-{abbr}-{NNN}`，不含 Layer 3） | 無影響 |
| `generated/` 之檔名／批次名 | **是** | **唯一受影響者** |

```
Layer 3 名稱之轉寫（framework 定義之一部分，隨本次簽核生效）
`framework.md` 內之顯示名維持 `SwitchLHD/RHDConfiguration`（037 之逐字）。
凡用於檔名、批次名、或任何不接受 `/` 之識別碼者，
取其**正規化形式** `SwitchLHDRHDConfiguration`（去 `/`，不補底線）。
兩者於 `framework.md` 之 Layer 3 表並列，逐字對照。

**阻塞項 8 就此關閉。**
```

### 2.2 阻塞項 10（訊號書寫形式）—— **已由 R-VS41 解**（35 包 §1）

三件組撤回，改依 canon §8.7.5 v3；`framework.md` 之該列標「已解」。

### 2.3 底部「草案階段之三項未定」第 5 項（`Common Features` 名稱衝突）
**為過期記載** —— 15 輪已改名 `CrossZone Common`。標「已解」，不再列。

---

## 3. 鎖定後之重開條件（**須明記，否則鎖定即成僵化**）

```
framework 重開之條件（分析層裁定，隨簽核記載）
下列任一發生時，`framework.md` 解鎖、修訂、重送 Pei 簽核：

(1) **DR-15 之答覆改變階數之地位**。現行 Layer 3 以
    `OneStage`／`TwoStages`／`ThreeStages` 切分（合計 56 leaf）。
    若上游答覆顯示階數非配置維度而是同一需求之分支，該三個 Layer 3
    須合併。
(2) **DR-17 之答覆改變 `OneStageHeatedSeat` 之委派狀態**（12 個 `pending`）。
    委派狀態不影響 Layer 3 之界定，但若答覆顯示單階座椅之需求歸屬
    另有文件，該 Layer 3 之 leaf 組成可能變動。
(3) **DR-11 之答覆使 `HeatedSteeringWheel-009` 取得 reqid**。
    其現依分支 (4) 以 token 判定；取得 reqid 後須依 (1)(2)(3) 重判。
(4) pilot review 發現某 Layer 3 之 leaf 無法在該分組下寫出 TC。

**重開不需 Pei 事先同意**，但修訂後之 framework 須重簽。
未重簽前，已生成之 TC 依鎖定版之 Layer 3 標記，不追溯改寫。
```

---

## 4. 19 輪指令（併入 18 輪，不另開輪次）

35 包 §5 之 18 輪指令仍為現行，**增列三項文書**：

```text
（追加於 35 包 §5 之 18 輪指令之「文書」段）

D-5  依 36 包 §1 鎖定 `framework.md`：
     檔頭狀態改為
       **狀態：已鎖定。Pei 簽核 2026-08-20（P19）。**
     並附 36 包 §1 之簽核區塊逐字、§3 之重開條件逐字。
     **原「草案，未鎖定」之標題與「鎖定前尚未解之項目」表保留**，
     後者逐列更新其狀態（R-TM13：不刪，加註）。

D-6  依 36 包 §2.1 於 Layer 3 表增「正規化名」欄，
     `SwitchLHD/RHDConfiguration` → `SwitchLHDRHDConfiguration`；
     其餘 18 個 Layer 3 之正規化名等同其顯示名。
     阻塞項 8 標「已解」、阻塞項 10 標「已解（R-VS41）」、
     底部第 5 項標「已解（`CrossZone Common`，15 輪）」。

D-7  `PLAYBOOK.md` §6 狀態板更新：
     framework 已鎖定；當前階段＝首批改寫（W-55）；
     未結 DR 五份（DR-15／17／18／19／20）與其阻塞 leaf 數。
```

---

## 5. 現況（依 R-VS31，僅列狀態改變者）

| 項 | 變動 |
|---|---|
| P19 framework 簽核 | **已完成** |
| 阻塞項 8／10／底部第 5 | **關閉** |
| 尚待 Pei | **僅餘 DR-15／17／18／19／20 之送出**（4 份阻塞，共 178 leaf） |

**條文面已無待裁項。** R-VS1～R-VS41 全數裁定完畢。

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| P19 簽核區塊 | framework 三層定案並鎖定 | **Pei** |
| Layer 3 正規化名 | `/` 之轉寫（framework 定義之一部分） | 分析層（隨簽核生效） |
| framework 重開條件 | 四項，重開不需事先同意但須重簽 | 分析層 |

**未立新編號條文** —— 符合 R-VS40（本輪額度已於 35 包用於 R-VS41）。
