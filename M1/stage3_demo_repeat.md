# Stage 3 深拆示範 — Repeat 功能(SWE1-PLA-030)

> 我(深拆 agent)用 CFTS025 §3.1.1.4.2.7 + Player domain pack,對 Repeat 需求做單需求深拆。
> 對照原檔 5 條 TC 的覆蓋,展示「拆得夠深」長什麼樣——且**不發明 spec 沒有的東西**。

## 原檔覆蓋(5 條 TC,~3 個情境)

| TC | 情境 |
|---|---|
| 094 / 095 | Repeat All 預設(BTSA) |
| 096 / 097 | Repeat All 連續循環行為 |
| 098 | Repeat Song(= One Track)行為 |

## 深拆計畫(11 個情境;=原檔已涵蓋,=缺口)

**A. 預設狀態**
- A1 /選源後 Repeat=All 預設 — *但原檔未驗 'repeat' softkey 應顯示 OFF 態*(domain:All↔softkey OFF)
- A2 進入時 softkey 視覺狀態 = OFF(對應 All)

**B. Repeat All 行為**
- B1 末曲後循環回第一曲(連續)
- B2 **邊界**:播放清單僅 1 首 + Repeat All → 同曲循環

**C. 模式切換(toggle)**
- C1 按 'repeat' softkey → 切到 Repeat One Track,softkey 顯示 ON
- C2 再按一次 → 切回 Repeat All,softkey 顯示 OFF

**D. Repeat One Track 行為**
- D1 當前曲目重複
- D2 One Track 期間 softkey 持續顯示 ON 態

**E. 跨功能互動**
- E1 Repeat + Shuffle On 組合行為(domain:Shuffle On 隨機序)
- E2 Seek Up 跨清單尾端 wrap-around 後 Repeat 狀態維持

**F. Per-source siblings**(domain:USB/BTSA/AUX/CD 行為一致)
- F1 同樣 Repeat 行為在 **HU USB**(原檔只測 BTSA)

**反情境(明確不測)**
- **不得**測「Repeat Off / No Repeat」——CFTS025 只定義 All↔One Track 兩態(domain pack boundary)。這正是 baseline reviewer 之前幻覺要加的,深拆 agent 因為有 domain pack 而**正確排除**。

## 深度對比

| | 原檔 | 深拆 |
|---|---|---|
| 涵蓋情境 | ~3 | **11** |
| 新增缺口 | — | **8 個**(toggle、softkey 狀態、單曲邊界、Shuffle 互動、wrap-around、USB sibling) |
| 幻覺情境 | — | **0**(明確排除 Repeat Off) |

## 重點

深拆把覆蓋從 ~3 → 11 個情境,**而且每一個都能引 spec/domain 出處**;同時靠 domain pack **擋掉**「Repeat Off」這種看似合理、實則 spec 沒有的情境。這就是「深度 + 接地」同時到位——正是 Stage 3 + Stage 1 的合體價值。

(此為人在迴圈的互動式深拆示範;`avg_decompose_depth` KPI 將以「每需求情境/步數」量化此深度,見 Stage 3 code 改造。)
