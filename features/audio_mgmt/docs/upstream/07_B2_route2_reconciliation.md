# Audio Management — 上繳包 07：B2 第二路對帳（R-AM15）

- 日期：2026-08-26
- 執行層：Claude Code
- 對應下放包：`docs/handoff/06_B2_anchor_candidates.md`
- 依據：R-AM15「雙路必經」。本件為第 (2) 路——**執行層全文獨立比對**——之結果，
  與第 (1) 路（分析層定向查證）對帳。

---

## 一、第二路之方法與其獨立性

語料刻意取**與第一路不同者**：第一路查 Basic Report（匯出摘要），
第二路讀 **CFTS019 全文 PDF** 之 1,730 個屬性物件原文。兩者為不同工件，
且全文含 Basic Report 所遺漏之物件（A-AM03），故第二路能觸及第一路
結構上看不到的範圍。

判定以**閱讀**為之：逐葉將 SWE.1 Description 與候選錨之 clause 原文並列，
另附全文相似度前 2–4 名作為「是否漏看更佳候選」之提示。
相似度分數不作判準——R-AM15 明文禁止單路演算法輸出作為定案依據，
本報告之任何分數僅為指路，不為裁決。

`scripts/route2_verify.py` 可重跑本比對。

## 二、對帳總表

| 級別 | 葉數 | 第二路結論 |
|---|---|---|
| A | 14 | **14 一致**；其中 2 條附但書（見 §四） |
| B | 33 | **33 一致**；其中 3 條附但書（見 §四） |
| C | 3 | **3 條均與第一路不一致** —— 第二路尋得證據，見 §三 |

47/50 兩路一致可寫入；3 條 C 級之處置待分析層裁。

## 三、C 級三葉：第二路找到第一路未見之證據

### 3.1 SWE1_AMM_309 → **CFTS019-4866484**（推翻「未決」）

第一路以「最近似 4866055，但需經 HFP ∈ INFO2（依 4865936）之推論一跳」
判為 R-13 所擋之代入型錯誤，不採，掛 PENDING。**該判斷對於 4866055 而言正確。**

第二路於全文檢索「HFP ∧ (pause|stop)」，得 9 個物件，其中：

> **4866484**：`When a CD, music player, MP3 or any other user initiated
> playing device is initiated that has the ability to be stopped or paused
> shall be paused during an HFP`
> `[Radio: High, VP2.5, R1L-R, VP1.5, VP2R5, VP1, R1L, VP2R84, CTS1_2, VP2R7, VP2]`

> **4866485**：同句，但結尾為 `during an HFP, E-Call, or R-Call`
> `[Radio: VP4R84, VP384, VP4R7, VP484, R1H, VP365, R1M, VP465, VP4, VP3]`

**取 4866484 之二重依據**（與第一路判別 310 用的是同一手法，獨立成立）：

1. **變體**：4866484 之 Radio 清單含 `R1L-R` 與 `R1L`；本案為 R1LR_Atl-H。
   4866485 之清單無之。
2. **本文**：葉描述僅言「HFP call」，4866484 亦僅言 HFP；4866485 尚含
   E-Call/R-Call，範圍較葉為寬。

**無需任何推論**：4866484 直述「user initiated playing device with pause/stop
capability shall be paused during an HFP」，即葉之全部內容。R-13 之代入疑慮
於此不存在。章節為 1.3.3.3 Information Sources {4866483}。

**建議**：C → A，錨定 4866484。此錨在池外（比照 R-AM2′ 處理）。

### 3.2 SWE1_AMM_030 → **CFTS019-4866054**（提案，非定案）

結構證據：**1.3.2.5 Source Selection {4866053} 整章僅含兩個需求物件**——
4866054 與 4866055，無第三者（全文逐物件掃描確認）。

> 4866054：`The HU shall perform source selection for Entertainment,
> Information 1, and Information 2 sources based upon established source
> priorities and user requests.`

位置證據：來源 ID 序列 029=SYS-RA-AMM-171（前章）、**030=-173**、
031=-178、032=-179、033=-181（→1.3.2.6 Confirmation Tone, 4866057）。
030 落在 1.3.2.5 之範圍內。

葉之核心「依設定優先權仲裁 ENT/INFO1/INFO2 之並發請求」與 4866054 相符。

**但須揭露一項未覆蓋**：葉尚含「衝突時套用設定之 duck／mute／reject／pause
動作」。全文檢索 `duck` 與 `reject|mute` 同現之行 **0 筆**——該動作集在
CFTS019 正文無對應文字。研判其來源為 1.3.4 Audio Arbitration Conditions
Tables {4866981}（framework 註明為條件表素材、隨引用不獨立成集），
或 4866447 所指之跨文件參照 `{CFTS019-5129}`。故 030 若錨定 4866054，
屬**部分覆蓋**，動作集部分無錨。

### 3.3 SWE1_AMM_031 → **與 032 共錨 CFTS019-4866055**（提案，非定案）

第一路之疑問為「4866054／4866055 之歸屬與 032 衝突」。第二路之證據：

- 該章僅兩物件，030 佔 4866054 後，031 與 032 只餘 4866055。
- 來源 ID **178／179 連號**，形態為上游將一條 CFTS 需求分解為兩個 SWE 葉。
- 兩葉內容確為 4866055 之互補讀法：031 側重「INFO2 取得優先權、衝突串流
  轉入 interrupted 狀態」，032 側重「具 pause/stop 能力者暫停至 INFO2 全部
  非作用」。4866055 原文兩者皆含。

共錨不違 R-AM6（該條處理的是同一 SWE ID 出現兩列；此處為兩個不同 SWE ID
指向同一 CFTS 物件，屬上游分解，非造 ID）。惟**是否允許共錨屬分析層之裁**，
第二路不逕行認定。

## 四、一致但附但書者（5 條）

| 葉 | 錨 | 但書 |
|---|---|---|
| SWE1_AMM_086 | 4866220 | 錨文為**範圍前提句**（"In any Ignition Working Conditions following requirements are valid IF…"），非行為需求本身。葉之「套用優先權與路由政策決定各通道可聞來源」在該物件無對應文字。全文另有 4866442 相似度更高（0.15 vs 0.14）。**建議分析層複讀** |
| SWE1_AMM_076 | 4866155 | 同型：錨文為前提句 ＋ 外部文件參照（`Routing_Table of {CTS - VP1 and VP2 System}`）。與 4866154 相似度並列（0.09/0.09），無區辨力。**建議分析層複讀** |
| SWE1_AMM_061 | 4866123 | 錨文為 `the HU shall apply the mute logic as described in {CFTS020}` —— **行為本體不在 CFTS019**。葉描述之音量/靜音狀態、螢幕 On/Off、螢幕優先權判斷，全文皆無。CFTS020 不在 `inputs/`。→ 新開 **DR-AM6** |
| SWE1_AMM_233 | 4866916 | 錨文僅述「signal source shall be mixed with all output channels」；葉尚含「對 Information 來源套用設定之 ducking level」，該部分在錨文無對應。**部分覆蓋** |
| SWE1_AMM_032 | 4866055 | 葉首句「INFO2 優先於 ENT 與 INFO1」不在 4866055，屬 4866054 之範圍。與 §3.3 之共錨議題同根 |

## 五、第二路查核之附帶結果

1. **310 之變體判別獨立成立。** 4866909 之 Radio 清單含 `R1L-R`（本案）且本文
   含 `E-Call/R-Call`；4866910 無 `R1L-R` 且僅提 HFP。第一路之判別於兩個
   依據上皆正確。
2. **VSIM 五葉無歧義。** 曾疑 179–184 之錨（4866689–4866695）與 4866696–4866698
   為同文異錨對；實查為 **mute 與 unmute 兩組**（4866689–4866694 為 mute、
   4866695–4866698 為 unmute），同章不同向，五葉各自對應唯一。疑慮不成立，
   不列入對帳。
3. **226/234 與 227/235 為跨 B1/B2 之同文異錨對。** 234→4866926 與 B1 之
   226→4866902 同文（1.3.3.18 vs 1.3.3.17）；235→4866927 與 B1 之 227→4866903
   同理。此對稱性反向佐證 **B1 之 226 錨定 4866902 為正確**——即執行層先前
   DP 之唯一錯配（給出 4866901）確為演算法之誤，非裁定之誤。
4. **058/066 為同文異錨對**（4866120「shall indicate … using the $ENTMuted$
   CAN signal」／4866129「has to indicate the possible mute status … using
   signal $ENTMuted$」），分屬不同章節。撰寫時 tc_title 之 sibling 區分
   token 須可辨，比照 06 包 §六.2 之處置。

## 六、執行層對先前主張之更正

上繳包 05 rev 2 主張全域單調 DP 對 B1 之池內錨達 **42/43 = 98%**，並據以
建議作為 B2 之起點。**該主張之樣本不具代表性，結論不成立。**

分析層之實測揭露失效模式：SWE.1 以 SYS-RA 號升冪排列，尾段葉
（SYS-RA 895–1111）所對應之 CFTS 章節位於文件前段，單調假設於該區崩潰，
DP 遂將 310、312–317 等硬配至尾段時序變數定義。B1 全批落在文件中段，
故 98% 是在「單調成立之區段」上量得，不能外推。

05 rev 2 §六.2 雖已載明「單調性為經驗事實而非保證」，但仍將 98% 置於
文件首節作為主要賣點，份量配置錯誤——限制被寫成註腳，而它其實是主結論。
本包不再以任何單路演算法輸出作為建議依據。

## 七、待分析層裁定

1. §三 之三葉（309／030／031）之錨定或維持 PENDING。
2. §四 之五條但書，特別是 086 與 076 是否改錨。
3. 031／032 共錨是否允許。
4. DR-AM6（CFTS020 缺件）是否送出。

## 八、下一步

裁定回件後即為定案錨表，執行層開 B2。B1 之流程
（context → 生成 → 自檢 → lint → 寫回）已跑通，可原樣沿用。
