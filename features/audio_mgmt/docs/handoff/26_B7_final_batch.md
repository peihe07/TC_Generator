# Audio Management — 下放包 26：A-AM15 裁定 ＋ Batch B7 錨表（最終批）

- 日期：2026-08-26
- 內容：(一) A-AM15 之 268 裁定；(二) B7 = Power and Persistence 後 15 ＋
  Logistic Mode 3 = 18 葉之錨表；(三) DR-AM3 理由改寫確認；(四) 收官清單。
- 葉集差集核對：已交付∪B7 = **317 唯一 SWE ID（318 列，076 碰撞兩列）**，
  差集 **0**。B7 完成即全表覆蓋。

---

## 一、A-AM15 裁定：SWE1_AMM_268 → **CFTS019-4867640**（改錨）

### 實讀之兩平行區塊

| Copy A | Copy B | 內容 |
|---|---|---|
| 4867639 | 4867646 | loudness menu **present** IF `$AudioSystemType$ == "Base"` |
| **4867640** | 4867647 | `In this case loudness shall be performed on entertainment sources only.` |
| 4867641 | 4867648 | loudness menu **not present** IF `== "Fiat Booster"` |

4867640 與 4867647 **逐字相同** —— 標準孿生案，依 **D-B6-01：同文場合
文本核驗必然一致，位置法為唯一區辨依據**。

### 位置夾定

267→4867639（Copy A）、269→4867641（Copy A）**夾住** 268 ⇒ **4867640**。
SYS-RA 序 810／811／812 與 4867639／4867640／4867641 單調對應，無反轉。
現行 268→4867647 使 267/269 之間出現跨區塊跳躍，位置不單調。

**定案：268 → CFTS019-4867640。**

### 執行層所慮之「代價」——不成立

23／25 包憂「若改，4867646 無對應葉」。實測：**兩種指派下 Copy B 都有
未覆蓋物件**（現行指派下 4867640 與 4867646 皆無葉；改後 4867646 與
4867647 皆無葉）。差別只在**哪一份 Copy 被 268 錨定**，不在覆蓋總量。
且 271→4867648 已錨 Copy B，證明上游對 Copy B 僅作部分覆蓋。
故代價不構成保留現況之理由。

**Coverage gap 揭露（不擴編）**：4867646、4867647（Copy B 之 Base 兩句）
無 SWE.1 葉，隨交付揭露。

### 回修

268 在 B6 已交付，spec_reference 為交付欄 → 真回修。
**併入 R-AM18 回溯站**（同 264 之處置），不單項回修。

**執行層依裁定交付而未自改，正確**——R-AM15 禁單路定案，已裁之錨非
執行層可逕改。此為制度按預期運作，非保守。

---

## 二、B7 錨表（18 葉，最終批）

### Power and Persistence 後 15

| 葉 | 錨 | 池 | 佐證／備註 |
|---|---|---|---|
| SWE1_AMM_174 | CFTS019-4866662 | ✓ | `Then, HU shall recall last audio settings`（與 173→4866629 之 store 同序列尾）。**與 B4 之 176 同物件 → 共錨申報**，見 §三 |
| SWE1_AMM_177 | CFTS019-4866674 | ✓ | `When HU/AMP needs to activate audio on at least one loudspeaker … shall store the current audio mode settings`（HALF 系統段，HU/AMP 並列，符葉之「HU/AMP 啟用前儲存」） |
| SWE1_AMM_178 | CFTS019-4866677 | ✓ | 同序列之 recall 句（位置夾定：177→4866674 之後首個 recall）。**第二路須讀 4866675–4866680 確認**，池籍已驗 |
| SWE1_AMM_188 | CFTS019-4866714 | ✓ | `Save the volume level of all currently active sources to memory`（4866713 `IF $TBMMuteRq$ = [Mute] THEN` 之子句一） |
| SWE1_AMM_221 | CFTS019-4866489 | ✓ | `store the current mode settings`（Entertainment 序列）。**注意**：131 已裁改為 4866466（Information 序列），兩者同文；221 取 4866489 使兩葉各據一序列，位置與語境雙合 |
| SWE1_AMM_245 | CFTS019-4867162 | ✓ | HU 偵測電氣故障（開路／對電源短路／對地短路／端子間短路）之喇叭診斷 |
| SWE1_AMM_246 | CFTS019-4867426 | ✓ | `IF HU receives $AMPAudioStatus$ == "Not_Available" THEN HU shall set $HUAudioStatus$ to "Not_Available" until … "Available"` —— 逐字對應，**且在池內**（原候選 4867177 為 AMP 側且池外，不取） |
| SWE1_AMM_247 | CFTS019-4867457 | ✓ | `Each time the BH-CAN bus wakes up, the HU shall recall the last known configuration settings`（HU 側；4867458 為 AMP 側，不取） |
| SWE1_AMM_297 | CFTS019-4866141 | ✗ | `Last NAV Volume used … less than <NAV vol min>` |
| SWE1_AMM_298 | CFTS019-4866142 | ✗ | Phone Volume `< <HFP Vol Th min>`（非 LATAM） |
| SWE1_AMM_299 | CFTS019-4866143 | ✗ | Phone Volume `< <HFP Vol Th min LATAM>`（**改自候選 4866142**；LATAM 變體為獨立物件） |
| SWE1_AMM_300 | CFTS019-4866144 | ✗ | Phone Volume `> <HFP Vol Th max>` |
| SWE1_AMM_301 | CFTS019-4866145 | ✗ | Ringer Volume `< <HFP Vol Th min>`（**改自候選 4866146**） |
| SWE1_AMM_302 | CFTS019-4866146 | ✗ | Ringer Volume `> <HFP Vol Th max>` |
| SWE1_AMM_303 | CFTS019-4866147 | ✗ | VR Volume `< <HFP Vol Th min>`（**改自候選 4866106**） |

**297–303 為七條連號單調對應**（4866141–4866147），SYS-RA 1074–1080
與 ObjectID 完全同序，位置與文本雙合。匹配器原給 299/301/303 三葉
撞題（同句型不同變體），已依**閾值變體**區辨：min／min LATAM／max
三值各自獨立物件。

**門檻實值**（依 IN §8.7.1 入 TC，不留 PENDING）：
`<HFP Vol Th min>` = 15 step（4867753）、`<HFP Vol Th min LATAM>` = 19 step
（4867754）、`<HFP Vol Th max>` = 38 step（4867752）、
`<NAV vol min>` = 依 {CIP Market Configuration Table}，**預設 15 step**
（4867755；R1 版 4867756 同值）。

### Logistic Mode 3

| 葉 | 錨 | 池 | 佐證 |
|---|---|---|---|
| SWE1_AMM_242 | CFTS019-4867027 | ✓ | 進入 Logistic Mode → 停用全部音訊輸出通道 |
| SWE1_AMM_243 | CFTS019-4867028 | ✓ | 設 `$HUAudioStatus$` = Not_Available |
| SWE1_AMM_244 | CFTS019-4867029 | ✓ | Logistic_Mode_ON → Standard_Power 之離開處置 |

三葉連號單調，本 feature 最乾淨之一組。

### 池外統計
**7 筆**（297–303 全段）。休眠回復段整段未匯出——**DR-AM3 之又一實例**，
且此段為普通條文非圖表，與 A-AM13 之改寫方向一致。

## 三、共錨申報（R-AM21 新制）

| 錨 | 葉 | 括號下半分野 |
|---|---|---|
| CFTS019-4866662 | **174（B7）** ／ **176（B4，已交付）** | 174 取「喇叭啟用序列完成後之回復」；176 取「路由變更後之回復」。跨批共錨，R-AM21 涵蓋 |

174/176 之 SYS-RA 為 474／492，分屬同一 recall 句之兩次上游分解，
形態同 031/032、199/195。核可後方寫入。

## 四、DR-AM3 理由改寫（A-AM13）— 確認

圖表論據作廢、一般性缺漏成立。**先前代擬之更正函已覆蓋此旨，維持該函，
不另發**（同 21 包 §九.3 之裁定）。B7 之 297–303 七筆池外可作補充實例
附於下次往來，不另開 DR。

## 五、收官清單（B7 上繳後執行）

1. **R-AM18 回溯站**（六項）：287／312–317 spec_reference 補列、264 改錨、
   268 改錨、169 reasoning 補註、098 已於 B6 入表（無須回溯）、
   池外錨以新池重跑第二路。**DR-AM3 未結前，末項僅能標記待辦。**
2. **R-AM21 全簿終掃**（350＋18 條）。
3. **同文異錨終掃**（`same_text_anchors.py` 全簿）。
4. **葉集差集終核**：應為 0（本包 §首已預核）。
5. **未結 DR 九件**之最終清單，隨交付附上。
6. **DELIVERY_NOTE.md**：揭露 PENDING（140／DR-AM10、026／076a／DR-AM1）、
   池外錨總數與單源佐證限制、coverage gap（4867646/47、4867568、
   4867485、1.3.3.14、PF/EQ/DSPPP 177 條）、九件未結 DR。

## 六、開工

B7 可跑第二路。18 葉中 15 葉附文本佐證、3 葉（178 之序列尾、
174 共錨、221 之序列歸屬）需第二路確認。完成即全表 317 葉覆蓋。
