# Player CFTS025 — TC 修正工單(§6.3 列舉缺口 + §7.6 reality-gap)

> 來源:`output/player_full/findings.json`(gpt-4.1 完整 review,假警報已全數修正後)
> 範圍:157 TC / 83 Req group · §6.3 共 28 筆、§7.6 共 32 筆
> 用法:每項列出「涉及 TC → 缺什麼 → 補什麼」。打勾追蹤。

---

## 先看:3 個需要你拍板的特殊項

- [x] ~~**Repeat All softkey 狀態(ON vs OFF)互相矛盾**~~ → **已裁決(2026-06-27)**:查 SWRA `FM-WI-SW-PLA-SWRA-A04.xlsx` SWE1-PLA-009,原文明載「CFTS 字面 Repeat All=OFF 與 HMI PC4.1=高亮衝突,**HMI 優先於 CFTS,HMI 文件為準**」,且其 Expected Result 寫「Repeat softkey shall be **highlighted** with labeling 'Repeat All'」。**結論:Repeat All = softkey 高亮(ON),標籤『Repeat All』。TC `NR1L-Player-023` 寫 ON 是對的;原 Domain Pack 寫 OFF 是錯的,已修正。§7.6 #6 那筆 reality-gap 是 Domain Pack 害的假警報,可忽略。**
- [x] ~~**疑似 Dealer Mode 測項混入 Player 檔**~~ → **已釐清(2026-06-27):不是放錯檔,是跨文件需求。** `SWE1-PLA-052「Video Player in Dealer Mode」`是 Player 的**指標型需求**,本身只寫「Refer to CFTS012-696、CFTS022、Showroom Demo Mode HMI」,實際行為定義在 **Dealer Mode CFTS012**。TC 137–141 正確掛在 PLA-052,且全部有 spec 依據:DEAL-026(play)、DEAL-028/028-01(exit lock)、DEAL-028-02(repeat loop)、**DEAL-030「Dealer Demo shall not play over ignition cycles」**(對應 Player-141 ER#7 不續播)。**§7.6 #28/#29 是假警報**——Player Domain Pack 缺跨文件知識所致,非 TC 缺陷。
  - **後續修法**:在 Player Domain Pack 加一段「Demo Video in Dealer Mode(跨文件,引 CFTS012 DEAL-026/028/030)」,下次重跑即可佐證 137–141;§6.6 對 PLA-052 的標記也應改引 DEAL-026/028/030 的 shall 句。
- [ ] **§6.6 無 spec句的 5 個 Req**(PLA-004/022/024-01/024-02/052)— 需你提供 Polarion/SWRA 的 canonical 英文 shall 句貼回,Tier 1 才能錨定。

---

## 一、§6.3 列舉覆蓋缺口(要補新 TC)

### A. Error Popup 三類列舉(PU0003 / PU0024 / PU0005)
依 Domain Pack,錯誤彈窗有三類,但各 Req group 只測其中一兩種:

- [ ] `PLA-001`(TC 001,002)— 只測 PU0003,缺 **PU0024、PU0005**
- [ ] `PLA-002`(TC 003,004,005)— 缺 **PU0003**
- [ ] `PLA-003`(TC 006,007)— 只測 PU0005,缺 **PU0003、PU0024**
- **補法**:每個 Req group 各補齊缺的 popup 類型;另對 PU0005(catch-all)補一條「未涵蓋錯誤→顯示 PU0005」驗證。

### B. Browse 分類完整列舉
- [ ] `PLA-005`(TC 012–014)— 只測 Radio Stations / Artist,缺 **Folders、Playlists、Songs、Albums、Genre**
- [ ] `PLA-020`(TC 071–075)— 只測支援裝置,缺 **不支援 Apple Music 裝置**的負向情境
- **補法**:每個分類各一條獨立 TC,驗證點選後跳對應清單。

### C. Repeat 模式 × 來源 列舉
- [ ] `PLA-006-01/02/03`(TC 016–019)— Repeat 只測 USB,缺 **BTSA、External CD** 來源
- [ ] `PLA-007`(TC 020)— Play Controls 只測 USB,缺其他來源
- [ ] `PLA-007`(TC 021)— Repeat 只操作功能,缺 **Repeat All / Repeat Song** 兩模式分別驗證
- [ ] `PLA-030-01`(TC 094,095)— 只測 Repeat All,缺 **Repeat Song(softkey ON)**
- [ ] `PLA-030-02`(TC 096,097)— Repeat All 只測 BTSA,缺 **USB、CD** 來源
- [ ] `PLA-030-03`(TC 098)— Repeat Song 只測 BTSA,缺 **USB、CD** 來源
- [ ] `PLA-033`(TC 101)— 只測 OFF,缺 **Repeat All/Song、Unavailable** 狀態
- **補法**:Repeat 模式(All/Song)× 來源(USB/BTSA/CD)矩陣補齊缺格。

### D. Shuffle 狀態 × 來源 列舉
- [ ] `PLA-010-01`(TC 024,025)— 缺「來源切換/媒體退出時 Shuffle 狀態維持或重置」驗證
- [ ] `PLA-010-01/02/03`(TC 026–028)— Shuffle 只測 USB,缺 **External CD、HU AUX、HU BTSA**
- [ ] `PLA-027`(TC 103,104)— 只測 Shuffle On,缺 **Shuffle Off**
- [ ] `PLA-037`(TC 106)— 只測 OFF,缺 **ON、Unavailable**
- [ ] `PLA-036`(TC 107)— 只測 Unavailable,缺 **ON、OFF**
- **補法**:Shuffle 狀態(On/Off/Unavailable)× 來源補齊。

### E. Alphajump 智慧字元過濾
- [ ] `PLA-015`(TC 036–040)— 只測 USB folder,缺 **DAP 類別瀏覽**
- [ ] `PLA-014-03`(TC 043–045 / TC 059)— 只測部分字母,缺「**清單首字母存在的全部字元啟用、不存在則禁用(灰階)**」完整覆蓋
- [ ] `PLA-014-05`(TC 047,048 / TC 061,062)— 只測單字元跳轉,缺所有首字母 + 不可選字元灰階
- **補法**:用一份含已知首字母分布的清單,驗證「存在字元可點、不存在字元灰階」。

### F. Play Controls 子功能完整性
- [ ] `PLA-021`(TC 076,077)— 只測 Skip Forward,缺 **Skip Back**
- [ ] `PLA-027`(TC 089,090)— 只測 Play/Pause,缺 **Repeat、Shuffle、Skip F/B、Progress Bar**
- **補法**:逐子功能補對應 TC。

### G. Metadata / 預設值 列舉
- [ ] `PLA-019`(TC 067–070)— 異常情境只分別測,缺「**同時缺所有資訊時 track#=0 / time=00:00:00 / metadata=Null** 一次全驗」
- [ ] `PLA-039`(TC 108–110)— Metadata 只測 Song,缺 **Podcast、Audio Book**
- **補法**:補全異常組合與媒體類型。

### H. 其他
- [ ] `PLA-043`(TC 116–120)— Currently Playing Playlist 來源未測全(缺 External CD、HU AUX)
- [ ] `PLA-056`(TC 147,148)— App icon 移除只測 disable,缺 **delete / uninstall** 路徑

---

## 二、§7.6 Reality-Gap(逐 TC 對 spec 修內容)

### 類型 1:**內容牴觸 spec(寫錯,必改)**
- [ ] `NR1L-Player-005`(#1)— 步驟 4 驗 PU0005,但 PLA-002 只規定 PU0024;PU0005 非本需求,移除或改正
- [ ] `NR1L-Player-023`(#6)— Repeat All 的 ER 與 Domain Pack 衝突(見上方特殊項)
- [ ] `NR1L-Player-136`(#27)— 步驟用「Page Down 一次一頁」,但 spec 是「**one row at a time**」,改正操作描述
- [ ] `NR1L-Player-062`(#14)— ER 假設 Alphajump 會改變/中斷播放,但 spec 無此行為 → 移除該推論
- [ ] `NR1L-Player-104`(#23)— ER 要求「每次隨機序列不同」,spec 未要求,且不可重現 → 改為可驗證的 Shuffle 狀態檢查
- [ ] `NR1L-Player-040`(#8)— ER 驗「不支援檔案不顯示」,但 spec 只定義「顯示支援檔案」→ 標準需再明確化

### 類型 2:**超出規格 / 假設未定義行為(需對 spec 確認)**
- [ ] `NR1L-Player-141`(#28,#29)— Demo Video / Dealer Mode(見特殊項,疑放錯檔)
- [ ] `NR1L-Player-110`(#24)— Test Item 講 BTSA Home Screen,但 spec 未界定 Home vs Playing Tab 差異
- [ ] `NR1L-Player-080`(#15)— ER「依 BTSA device behavior 更新」無法對齊具體 spec 結果

### 類型 3:**缺可觀察驗證 / 驗證不完整(補 check)**
- [ ] `NR1L-Player-012`(#2)— 只到顯示分類名稱,未驗各分類清單內容
- [ ] `NR1L-Player-013`(#3)— 只操作 Radio Stations,未切換驗證其他分類
- [ ] `NR1L-Player-014`(#4)— 只驗 Artists,未涵蓋所有分類
- [ ] `NR1L-Player-019`(#5)— Step 6 設 Repeat Song 但未檢查 softkey 顯示 ON
- [ ] `NR1L-Player-035`(#7)— ER 只驗 UI 切換,未驗「選曲後切回播放畫面並播放選中曲」
- [ ] `NR1L-Player-051`(#9)— 只檢查 category 顯示,未驗「select items」行為
- [ ] `NR1L-Player-052`(#10)— ER 只驗顯示 sub-items,未驗選取後操作流程
- [ ] `NR1L-Player-053`(#11)— 缺「選取 sub-item 並啟動播放」
- [ ] `NR1L-Player-054`(#12)— 只驗 unsupported 未顯示,未涵蓋 DB 更新/重讀情境
- [ ] `NR1L-Player-055`(#13)— 只驗空等級未顯示,未涵蓋 rescan/DB 重整
- [ ] `NR1L-Player-083`(#16)— 長按應觸發 Fast Forward + 進度條變化,步驟缺 UI observable
- [ ] `NR1L-Player-084`(#17)— 需驗 Fast Forward 狀態持續 + 滑桿動態更新
- [ ] `NR1L-Player-085`(#18,#19)— 滑桿應於長按結束後跳至新位置,缺明確 observable
- [ ] `NR1L-Player-089`(#20)— ER 只驗 Play softkey 顯示,未驗實際發送 Play 指令並播放
- [ ] `NR1L-Player-127`(#25)— ER 未驗 source-specific metadata 優先權顯示
- [ ] `NR1L-Player-128`(#26)— 未驗 metadata 缺漏時的 fallback(缺 Song 顯示 Device Name)
- [ ] `NR1L-Player-149`(#30)— delete app 後只檢查部分分頁,未驗所有分頁 icon 不存在

### 類型 4:**ER 漏列舉(與 §6.3 重疊,補完即同時解兩層)**
- [ ] `NR1L-Player-094`(#21)— ER 只驗 Repeat All,缺 Repeat Song
- [ ] `NR1L-Player-095`(#22)— ER 缺 Repeat Song 單曲循環
- [ ] `NR1L-Player-156`(#31)— 只測登入失敗,缺「已登入來源不跳登入 UI」正向分支
- [ ] `NR1L-Player-157`(#32)— 同上,缺正向二元分支

---

## 建議執行順序

1. **先拍板上方 3 個特殊項**(Repeat All ON/OFF、Dealer 混入、§6.6 spec句)— 影響後續判斷。
2. **§7.6 類型 1(牴觸 spec)**— 這些是「測錯」,風險最高,先改。
3. **§6.3 + §7.6 類型 4**— 列舉缺口,補新 TC(同時解兩層)。建議用矩陣法:模式 × 來源一次補齊。
4. **§7.6 類型 3**— 補可觀察驗證(多為在 ER/最後一步加明確 check)。
5. 改完**重跑 review**,看 first_pass_rate 與 tier1_critical_req_rate 是否達標。
