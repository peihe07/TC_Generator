# Audio Management — 上繳包 27：B7 第二路對帳（R-AM15）

- 日期：2026-08-27
- 下放包：`docs/handoff/26_B7_final_batch.md`（最終批錨表，18 葉）
- 池基準：展開池 v2，891 ID

---

## 〇、本站曾被跳過（先行說明）

B7 之第二路查證**已執行**（178 之序列尾、297–303 之閾值變體、174 之共錨、
221 之序列歸屬、其餘十葉之文本核驗），惟**未落地為文件**：`docs/upstream/`
最新一度停在 25，174 之共錨申報僅存於往來對話而無核可紀錄，221 更是在
生成端被移除而未見於任何上繳文件。

**查證做了而未成文＝該站未完成。** 本包補齊，並將 174 之申報正式提出。

## 一、包 26 §六 點名之三葉

### 一.1 SWE1_AMM_178 → CFTS019-4866677 — 確認

包 26 要求「第二路須讀 4866675–4866680 確認」。實讀：

| 物件 | 本文 |
|---|---|
| 4866674 | `When HU/AMP needs to activate audio on at least one loudspeaker … shall store the current audio mode settings` ← **177** |
| 4866675 | `Then, HU/AMP shall Ramp Up the signal source on the indicated channels` |
| 4866676 | `When ACC/FCW signal source becomes deactivated, HU/AMP shall Ramp Down…` |
| **4866677** | `Then, HU/AMP shall recall last audio settings` ← **178** |

序列完整（store → ramp up → ramp down → recall），178 取序列尾之 recall。
該段以 **HU/AMP 並列**書寫，與 B6 之 170–173（HU 單寫）分屬不同子章節，
故無共錨疑慮。**確認，逕寫。**

### 一.2 SWE1_AMM_174 → CFTS019-4866662 — 共錨申報（正式提出）

| 項 | 內容 |
|---|---|
| 錨 | **CFTS019-4866662** |
| 兩葉 | **174（B7）** ／ **176（B4，已交付）** |
| 性質 | **跨批共錨**，R-AM21 涵蓋 |
| 174 括號下半 | `Confirm the settings return once the speaker activation sequence ends` |
| 176 括號下半 | `Confirm the stored audio settings come back after the routing change` |
| 分野 | 176 觀察**路由變更後**之回復；174 觀察**喇叭啟用序列完成後**之回復 |

SYS-RA 為 474（174）／492（176），同一 recall 句之兩次上游分解，
形態同 031/032、199/195。**兩者括號下半實測逐字不同**，R-AM21 全簿掃描
綠燈。依包 22 §三 之申報制**正式提出，請核可**（已隨 B7 寫入；
若不予核可則需回修，spec_reference 為交付欄）。

### 一.3 SWE1_AMM_221 → CFTS019-4866489 — 依裁定寫入，異議留痕

**已依包 26 定案寫入**（Entertainment 序列，與 131 之 4866466＝Information
序列同文異錨，兩葉各據一序列）。

**第二路之異議記錄如下，非請求改判**：

| 測試 | 結果 |
|---|---|
| 位置 | 221 之 SYS-RA 為 **563**，夾於 220（561→4866891）與 222（564→4866894）之間；4866489 在窗外。同區塊之 139／140／141（370/371/372 → 4866488/89/90）完全單調，故偏離非雜訊 |
| 文本 | 葉為「儲存座艙音訊設定**與顯示設定**」；4866489 僅 `store the current mode settings`，未及顯示設定（該句為 4866490，141 之錨） |
| 替代 | **4866893**：`If an entertainment source is in use as a cabin audio source, when the second source becomes active … The HU shall store the current cabin mode settings (…). **The HU shall store the current display settings.**` —— 涵蓋兩半，且落於 4866891 與 4866894 之間 |

**交付之影響**：依 4866489，葉之**顯示設定半未覆蓋** → 標**部分覆蓋**，
TC 僅驗 mode settings，reasoning 明載異議與替代錨，俾日後查詢顯示設定
一半時可循線找到（A-AM16）。

## 二、其餘十五葉之第二路核驗

| 葉 | 錨 | 核驗 |
|---|---|---|
| 174／177／178 | 4866662／4866674／4866677 | 見 §一.1、§一.2 |
| 188 | 4866714 | `Save the volume level of all currently active sources to memory` 逐字對應 |
| 245 | 4867162 | **部分覆蓋**：錨為電氣故障之偵測（開路／對電源短路／對地短路／端子間短路），葉之「初始化時啟用診斷」之**時機**無明文 |
| 246 | 4867426 | 逐字對應；取 HU 側，不取 AMP 側之 4867177（且該物件池外） |
| 247 | 4867457 | HU 側；4867458（AMP）／4867459（ANC）為平行句，不取 |
| 297–303 | 4866141–4866147 | **七條連號單調**，每條之**閾值變體各異**：NAV min／Phone min 非 LATAM／Phone min LATAM／Phone max／Ringer min／Ringer max／VR min。包 26 對 299／301／303 之改錨**成立** |
| 242／243／244 | 4867027／4867028／4867029 | 三葉連號單調，逐字對應 |

**門檻實值**（1.5.4 Variables，依 IN §8.7.1 入 TC）：
`<HFP Vol Th min>`＝15 step、`<HFP Vol Th min LATAM>`＝19 step、
`<HFP Vol Th max>`＝38 step、`<NAV vol min>`＝15 step。

**池外七葉**（297–303，休眠回復整段）依 R-AM18 標單源佐證；
該段為普通條文非圖表，為 DR-AM3 改寫後之又一實例（A-AM13）。

## 三、統計

| 段 | 葉數 |
|---|---|
| 兩路一致（逕寫） | 17 |
| 依裁定寫入、異議留痕 | 1（221） |
| 共錨申報待核 | 1（174，已寫入） |
| 合計 | **18** |

## 四、待分析層

1. **174／176 共錨之核可**（§一.2）。
2. 221 之異議僅為留痕，**不請求改判**；若日後因顯示設定半而回查，
   4866893 為既有候選（§一.3）。
