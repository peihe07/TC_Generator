# INDEX — b07（形制補正，下放包 CAM-25 §2）

**CAM-24 審閱 §一-1** 判定 canon **§8.3**（boundary 每點一 TC）與 **§5.7**（不同觸發須拆）
**勝於**本 feature 之既有寫法；B 本三列違之，原地收斂為單點，其餘拆出為本批 **4 列**｜
TC ID `NR1L-RVCHMI-207`～`-210`｜計畫 `features/camera/data/b07_plan.tsv`。

| 母列 | 章 | 母列改後只留 | 本批拆出 |
|---|---|---|---|
| `NR1L-RVCHMI-036` | §7.5.3 | raw **206**（on-point，退出）| `-207`：raw **205**（off-point，仍顯示）|
| `NR1L-RVCHMI-111` | §28.7.1.1 | **pinch out**（zoom in）| `-208`：**pinch in**（zoom out）|
| `NR1L-RVCHMI-142` | §30.1.3 | **OK** 清除 | `-209`：**`‘X’`** 清除；`-210`：**5 秒逾時**自動清除 |

**三列之原地修改為既有列之唯一改動**（其餘 449 列不動），逐列 diff 見 CAM-25 上繳 §2-1。
登 **A-CA37**（三列經批次審閱未抓；責任在抽讀式審閱，同 GCB-12 之成因）。

**`-210` 不夾 4／6 兩點** —— 5 秒為 **timeout 而非門檻**（下放包 §2 明載此判），
只取逾時後之觀察點 6 秒。

`coverage_b.tsv` 之 3 個母 leaf 其 `tc_id` 欄已追加、`batch` 欄加 `;b07`。B 本 206 → **210**。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-207` | `SWE1-RVC-023-02` | §7.5.3 | the camera image is still displayed at the 8 mph off-poi | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-208` | `SWE1-RVC-103-02` | §28.7.1.1 | the pinch inwards gesture zooms the wireless AUX video f | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-209` | `SWE1-RVC-116` | §30.1.3 | the favorite confirmation is cleared by pressing X | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-210` | `SWE1-RVC-116` | §30.1.3 | the favorite confirmation is dismissed automatically aft | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py`：ERROR 級十項**全 0**；第 10 項（WARN）之候選見全案統計。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `I-cross` 4（`U`／`X`／`J`／`Z` 皆 0）。
