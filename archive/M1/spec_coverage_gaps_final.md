# Player SPEC-only 缺口 — 最終清單(L2 覆蓋)

> 「SPEC 原文有、但 94 個需求都沒涵蓋」的行為——生成測項時必須主動補,即使沒有對應需求。
> 方法:桶③(11 條)確定性判定;桶②(26 條)由 Claude 互動式語意比對(算訂閱額度,$0,非 API)。
> 來源:`spec_coverage_player.json` + Media HMI PC 規則 · 日期:2026-06-27

## 結論

| | |
|---|---|
| SPEC PC 規則總數 | 55 |
| 真實覆蓋(有需求涵蓋) | ~25/55 = **~45%** |
| **SPEC-only 缺口** | **~30/55** |
| 對比:`requirement_coverage`(對 94 需求) | 100% ← 完全看不到這 30 條 |

> 桶②濾掉 7 條(基本 skip/play/pause/resume + 不支援隱藏 track info,確實有需求覆蓋)。

---

## 缺口清單(依主題,可直接當生成/補測項的依據)

### A. 進度條 / Slider / 時間顯示(最大群,~12 條)
需求母體對「進度條行為、時間格式、elapsed/total time」幾乎 0 覆蓋(只有 PC1.1 樣板句把 Progress Bar 列為 Play Control)。
- `PC6.1` 支援 position jumping 時進度條可操作
- `PC6.1.1` Slider 移動並指示 elapsed time
- `PC6.1.2` 拖曳 slider 放開 → 從新位置播放
- `PC6.2` 不支援 position jumping → 移除 slider 只留 bar
- `PC6.4` 時間格式 HH:MM:SS（桶②假覆蓋,實為缺）
- `PC6.6` USB 插入顯示 '<n> Songs Found'
- `PC6.6.1` 播放就緒 → 正常畫面含 track counter
- `PC6.8` 移除整個進度條的條件
- `PC6.8.1` 無法判定是否支援 position jumping
- `PC6.8.1.1` 該情況維持 current/total time
- `PC6.8.2` 無法顯示 current time on bar
- `PC6.8.2.1` 該情況連 time 也移除
- `PC6.8.3` 曲目中途進度條顯示不應改變

### B. Shuffle 清單建構 / 來源相依(~6 條)
Shuffle 需求(PLA-010)只有 On/Off 切換,清單時序與來源記憶全缺。
- `PC5` Shuffle 預設 OFF
- `PC5.2` 洗牌清單以當前曲目為第一首
- `PC5.2.1` 當前曲目播完前不播洗牌清單
- `PC5.2.2` 到尾端不重新洗牌
- `PC5.2.3` Browse Tab 在 shuffle 時仍顯示原始順序
- `PC5.3.1` Shuffle 來源相依(換來源記住各自狀態)

### C. Repeat 持續性 / 來源相依 / 互動(~4 條)
- `PC4.4` Repeat 持續到使用者關閉或裝置斷線
- `PC4.4.1` Repeat 來源相依
- `PC4.5` Repeat 啟用時 Skip F/B 維持正常行為
- `PC4.7` Repeat Off 不支援時不呈現該選項 **(與 Repeat Off 議題相關)**

### D. Audiobook / Podcast 變體(2 條)
- `PC1.1.1` Audiobook/Podcast 把 Shuffle 換成 Rewind 15s、Repeat 換成 Forward 15s
- `PC6.5` Audiobook track number 顯示為「第 X 章 / 共 Y 章」

### E. 硬體控制 / 邊界(4 條)
- `PC1.2` Tune knob 切換上/下一曲
- `PC1.4` 命令不可用又無法 grey out → 顯示「Function currently...」popup
- `PC2.1` 清單只有一首時按 next → 重播該首
- `PC2.2.1` 放開 FF/Rewind 按鈕後續播

### F. 雜項(2 條)
- `PC1` Play Controls 適用來源(含 SD-Card / HDMI,需求只覆蓋 USB/BTSA)
- `PC3.2` 暫停時 mute icon 顯示於 Status-Alert box

---

## 對生成 / 標準的意義

1. **這 30 條是 L2 覆蓋的待補清單**——生成 TC 時要主動涵蓋,不能只看 94 需求。
2. **A、B 兩群(進度條、Shuffle 時序)是穩定 SPEC 行為**,建議回填成 Player domain pack 的 feature_model / boundary,讓未來生成與 review 都能接地。
3. **C 群與 Repeat Off 議題合併處理**(SPEC PC4 說 Repeat 有 3 態含 Off,需求簡化成 2 態)。
4. 把「L2 SPEC 覆蓋率(~45%)」做成與 L1 並列的 KPI。

> 註:桶②的判定由互動式語意比對得出(非 API 計費)。若日後要無人值守重算,可用 `archive/M1/spec_coverage_verify.py`(走 API,計費)。
