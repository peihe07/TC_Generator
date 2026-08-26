# Audio Management — 上繳包 15：B4 第二路對帳（R-AM15／R-AM20 綠色通道首批）

- 日期：2026-08-26
- 對應下放包：`docs/handoff/13_B4_anchor_candidates.md`
- 分段依包 13 §五：**池內一致（逕寫）／池內不一致（對帳）／池外（待裁）**

第二路語料：**Basic Report 匯出**（R-AM2 主池），與第一路之全文 PDF 相異。
`scripts/route2_b3.py --batch B4` 可重跑。

---

## 一、池內一致（逕寫，R-AM20 綠色通道）

B 級 15 葉中，**8 葉池內且兩路一致**，依 R-AM20 逕入生成，不待裁定：

| 葉 | 錨 | 匯出本文之對應 |
|---|---|---|
| SWE1_AMM_003 | 4865915 | 「Entertainment sources … shall be continuous until they are paused or deactivated by the user or by the activation of a higher priority source」 |
| SWE1_AMM_009 | 4865932 | 「The following Information sources shall be assigned to the Information 1 audio path: Navigation, Text to Speech, Voice Prompts」 |
| SWE1_AMM_013 | 4865967 | 「Confirmation tones shall be played on the front channels in non-Amplified systems」 |
| SWE1_AMM_202 | 4866843 | 五個狀態訊號之更新，與葉逐項對應 |
| SWE1_AMM_204 | 4866845 | 同上（去活化側）。**註：錨文含 `<Temp Ramp Down>`，屬 A-AM04／DR-AM5 之未定義參數，時序須掛 PENDING** |
| SWE1_AMM_207 | 4866854 | 同上（Entertainment 轉換側）。**同一 PENDING** |
| SWE1_AMM_228 | 4866904 | 「HFP audio shall be directed to the passenger side channel source until the NAV prompt ends」 |
| SWE1_AMM_263 | 4867584 | 「Mute rear speaker channels」 |

A 級 30 葉抽核未見異常，亦入逕寫。

## 二、池內不一致（對帳，須裁）

### 二.1 SWE1_AMM_002 — **錯配，建議改錨 4865913**

候選 4867570 之匯出本文：

> `[Information] HU has to acquire the left or right **drive**, for the
> management of audio output channels.`

「left or right drive」為**左駕／右駕車型**，非左右聲道。前一物件 4867569
可證：`IF $DriverSide$ contains any value other than [LHD] or [RHD] …`。

葉 002 為「將 Entertainment 音訊路由至設定之 Left 與 Right 輸出通道」。
正確候選 **4865913**（池內）：

> `The HU shall assign Entertainment sources to the Entertainment Left and
> Right audio paths.`

錯配來源可辨：兩者同含 left／right 與 audio output channels 之詞面，
語意分屬車型配置與聲道指派。

### 二.2 SWE1_AMM_122 — **候選為表名，建議改錨 4866444**

候選 4865895 之匯出本文為 `[Information] CIP Market Configuration Table`
—— 一張表之**標題**，非需求條文。

葉 122 為「依核准之 Audio Routing Table 進行仲裁與路由」。較佳候選
**4866444**（池內）：

> `For further details about audio arbitration to the Routing Table in
> {Component Technical Specification - VP1 and VP2 System}.`

惟該物件為**外部參照句**，與 076b／087 同型，故建議錨定 4866444 並標
**部分覆蓋**，Routing Table 之具體對應併入 DR-AM1。

## 三、C 級五葉之查證

### 三.1 SWE1_AMM_145 — **解決，建議升 A，錨 4866497**

包 13 之警示為「4866494 已為 B1 之 144 錨，取之須依 R-AM16 論證」。
第二路查得 **4866497 為獨立物件**，非 4866494：

> `The HU shall Ramp Down the current Entertainment audio source on the
> "Applied Channels" noted in the Information Source Handling Table
> according to its deactivation sequence.`

與葉「Applied Channel Ramp-Down」逐項相符，且**不需共錨論證** ——
4866494（144）為一般去活化斜坡，4866497（145）為 Applied Channels 面向，
兩物件不同。警示解除。

### 三.2 SWE1_AMM_155 — **解決，建議升 A，錨 4866513**

包 13 之問題為「4866512 已為 B1 之 154 錨；是否共錨或另有通道句」。
第二路查得 **4866513 即該通道句**，為獨立物件：

> `The HU shall Ramp Up the Information source using a Ramp Up function of
> <Tinfo Ramp Up>. The Ramp Up shall be applied to the channel indicated in
> the …`

154／4866512 為**音量位準**面向（"Volume Level" defined in the table），
155／4866513 為**通道**面向。**不需共錨**，各有其物件。

### 三.3 SWE1_AMM_020 — 未決，附線索

「Alert 前聲道路由」之直接對應未尋得。最近者 **4865981**（池內）：

> `Entertainment and information alerts can be played on all channels …`

該物件言「**all** channels」，葉言「**front** 通道」，範圍不符，**不採**。
建議維持 C 級掛 `PENDING: DR-AM1`；若分析層於 1.3.1.5／1.3.2.6 另有查得，
第二路可再核。

### 三.4 SWE1_AMM_024 — 未決

「external amplifier」與輸出對映同現之物件**零命中**。
包 13 所疑之 4866289 實為一般性通道指派：

> `Audio channel assigning shall be performed after individual source
> amplitude adjustment to separate and assign the entertainment, information
> and signal audio …`

該物件未提外部擴大機。與 108 共錨之推定**無文本支持**，第二路不採。
建議維持 C 級掛 PENDING。

### 三.5 SWE1_AMM_146 — 未決

「remaining channel」**零命中**。包 13 所疑之 HALF／SDW 子集區
（4866620–4866662）第二路亦未見對應「剩餘通道音量調整」之條文。
建議維持 C 級掛 PENDING。

## 四、池外（待裁，R-AM20 除外條款）

已知池外 5 葉，第二路無獨立語料可用（匯出無該物件），依 **R-AM18**
只能回讀全文，與第一路同源，**不構成獨立佐證**：

| 葉 | 錨 | 題旨 | 佐證 |
|---|---|---|---|
| SWE1_AMM_264 | 4867598 | Surround HMI 啟用 | 單源 |
| SWE1_AMM_266 | 4867604 | Surround 停用 | 單源 |
| SWE1_AMM_306 | 4866207 | 座艙音訊作用中之預設警示音量 | 單源 |
| SWE1_AMM_307 | 4866208 | 座艙音訊非作用之預設警示音量 | 單源 |
| SWE1_AMM_308 | 4866242 | SVC 停用處置 | 單源 |

C 級三葉（020／024／146）若後續查得之錨落池外，一併適用本段。

**306 之附記**：葉載「低於座艙音量 15 dB 或音量步階 6 之等效值，取較大者」
—— 為含實值之雙分支條款，撰寫時須兩分支各一條（§7 列舉配對），
且 15 dB 與 step 6 皆須溯源至錨文，不得僅取其一。

## 五、統計

| 段 | 葉數 |
|---|---|
| 池內一致（逕寫，含 A 級 30） | **38** |
| 池內不一致（待裁） | 2（002、122） |
| C 級未決（待裁） | 3（020、024、146） |
| C 級已解（建議升 A） | 2（145、155） |
| 池外（待裁） | 5 |
| 合計 | **50** |

綠色通道實際覆蓋 38/50 ＝ 76%；待裁 10 葉、已解 2 葉。

## 六、待分析層裁定

1. 002 改錨 4865913（§二.1）。
2. 122 改錨 4866444 並標部分覆蓋（§二.2）。
3. 145 升 A、錨 4866497；155 升 A、錨 4866513（§三.1／§三.2）——
   兩者皆**不需**共錨論證。
4. 020／024／146 維持 PENDING 或另提候選（§三.3–§三.5）。
5. 池外 5 葉之定案（§四）。
6. 204／207 之 `<Temp Ramp Down>` 依 DR-AM5 掛 PENDING，確認無異議。
