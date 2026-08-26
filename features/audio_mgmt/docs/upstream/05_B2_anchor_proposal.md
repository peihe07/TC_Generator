# Audio Management — 上繳包 05：B2 候選錨表（**提案，不具裁定效力**）

- 日期：2026-08-26
- 執行層：Claude Code
- 性質：**提案**。錨定屬分析層（03 包 §三.4「執行層不得自行改錨」）。
  本件僅為 §四 型表格提供一份已算過的起點，附證據與召回率。

---

## 一、先讀這節：本表的準確率是量測出來的，不高

以 B1 之 43 個**池內已裁定錨**回測本演算法（同一批葉、同一個池、標準答案
為 Pei 已准之 03 包 §四 表）：

| 指標 | 值 |
|---|---|
| top-1 命中 | 21/43 = **49%** |
| top-3 命中 | 29/43 = 67% |
| top-5 命中 | 33/43 = 77% |
| top-10 命中 | 36/43 = **84%** |
| top-20 命中 | 42/43 = 98% |
| 正解排名中位數 | **2** |

**結論：可當候選清單讀，不可當答案收。** 逐葉取 top-1 會有約一半錯配。

**已撤除之誤導設計：** 本腳本初版對每葉輸出單一挑選並標 `strong`／`weak`
信心度。回測顯示標為 `strong` 者僅 6/10 正確 —— 該標籤所傳達的把握程度
是它沒有掙得的，若分析層據以略過複核，反而比沒有本表更糟。已改為輸出
top-10 候選清單、只附原始分數，不作信心宣稱。

## 二、方法與其限制

SWE1_AMM ↔ CFTS019 ObjectID 無正式橋接欄（F1／DR-AM1），故採內容對位：
以 SWE.1 之 Title＋Description 對 Basic Report 之 Description，去停用詞後
計 Jaccard 相似度，候選限縮於 R-AM2 主池（811 物件）。

已知限制，均為回測中觀察到者：

1. **同文異錨無法區辨。** 池中存在逐字相同或近乎相同之 Description
   （如 queue 判定於兩子章節重複、SOS 靜音於兩處同文），演算法對此類必然
   在並列候選間任選，正解是否居首屬偶然。B1 之 130/139、198/218、199/219
   四組即屬此類。
2. **圖表型物件不在池中。** 其 Description 多為「Refer to the … figure」，
   本就缺可比對之內容，且 12/13 根本不在池內（A-AM03／DR-AM3）。B2 若含
   此類葉，本表對其無能為力，需比照 R-AM2′ 走全文佐證。
3. **短描述葉分數普遍偏低。** 詞彙少則 Jaccard 分母小、雜訊大。

## 三、批次組成（依 02 包 §三 之批次計畫）

| Test Set | 葉數 |
|---|---|
| Audio Arbitration | 13 |
| Focus and Ducking | 18 |
| Mute Requests | 19 |
| **合計** | **50** |

Audio Arbitration 取 B1 未用之 13 葉；Focus and Ducking 全 18 葉；
Mute Requests 取前 19 葉。與 02 包 §三 之「B2 = Audio Arbitration 後 13
＋ Focus and Ducking（18）＋ Mute Requests 前 19 = 50」逐項相符。

## 四、候選錨表（每葉 top-5，完整 top-10 見 `batches/B2_anchor_proposal.json`）

括號內為相似度分數，非機率、非信心度。

| SWE ID | Source ID | Title | Test Set | 候選（top-5） |
|---|---|---|---|---|
| SWE1_AMM_229 | SYS-RA-AMM-576 | Ignore TA During Active VR Session | Audio Arbitration | `4866906`(0.261) `4866929`(0.261) `4866913`(0.238) `4866933`(0.238) `4866908`(0.227) |
| SWE1_AMM_230 | SYS-RA-AMM-578 | Cancel VR for User-Selected Navigation Promp | Audio Arbitration | `4866908`(0.217) `4866930`(0.217) `4866906`(0.2) `4866929`(0.2) `4866913`(0.174) |
| SWE1_AMM_231 | SYS-RA-AMM-579 | Delay Navigation During Active VR Session | Audio Arbitration | `4866911`(0.189) `4866931`(0.184) `4866908`(0.148) `4866930`(0.148) `4867238`(0.147) |
| SWE1_AMM_232 | SYS-RA-AMM-581 | Ignore TA During Active Phone Audio | Audio Arbitration | `4866913`(0.316) `4866933`(0.316) `4866906`(0.273) `4866929`(0.273) `4866908`(0.238) |
| SWE1_AMM_234 | SYS-RA-AMM-592 | Cancel TA or Navigation for Phone/VR Request | Audio Arbitration | `4866966`(0.2) `4866901`(0.167) `4866905`(0.167) `4866912`(0.167) `4866925`(0.167) |
| SWE1_AMM_235 | SYS-RA-AMM-593 | Cancel TA on Incoming Call | Audio Arbitration | `4865871`(0.286) `4866903`(0.188) `4866927`(0.188) `4865881`(0.143) `4866901`(0.143) |
| SWE1_AMM_236 | SYS-RA-AMM-595 | Ignore TA During Active VR Session | Audio Arbitration | `4866906`(0.261) `4866929`(0.261) `4866913`(0.238) `4866933`(0.238) `4866908`(0.227) |
| SWE1_AMM_237 | SYS-RA-AMM-596 | Cancel VR for Customer-Selected Navigation P | Audio Arbitration | `4866908`(0.263) `4866930`(0.263) `4866906`(0.238) `4866929`(0.238) `4866913`(0.211) |
| SWE1_AMM_238 | SYS-RA-AMM-597 | Delay Navigation Until VR Completion | Audio Arbitration | `4866911`(0.242) `4866931`(0.235) `4866908`(0.217) `4866930`(0.217) `4866906`(0.2) |
| SWE1_AMM_239 | SYS-RA-AMM-599 | Ignore TA During Phone Audio | Audio Arbitration | `4866913`(0.278) `4866933`(0.278) `4866906`(0.238) `4866929`(0.238) `4866908`(0.2) |
| SWE1_AMM_259 | SYS-RA-AMM-787 | Handle Invalid Cabin EQ IDs (S00 / SFF) | Audio Arbitration | `4867579`(0.25) `4867580`(0.185) `4867578`(0.143) `4867084`(0.125) `4867577`(0.118) |
| SWE1_AMM_260 | SYS-RA-AMM-788 | Handle Unknown Cabin EQ IDs | Audio Arbitration | `4867579`(0.227) `4867580`(0.214) `4867581`(0.143) `4867578`(0.13) `4867084`(0.111) |
| SWE1_AMM_310 | SYS-RA-AMM-1094 | VR Session Cancellation on Call Initiation | Audio Arbitration | `4866908`(0.174) `4866930`(0.174) `4866906`(0.16) `4866907`(0.16) `4866929`(0.16) |
| SWE1_AMM_004 | SYS-RA-AMM-085 | Entertainment Audio Priority Handling | Focus and Ducking | `4865916`(0.273) `4866107`(0.24) `4866718`(0.231) `4866719`(0.231) `4865931`(0.227) |
| SWE1_AMM_008 | SYS-RA-AMM-097 | Information Source Audio Focus Priority | Focus and Ducking | `4866107`(0.273) `4865931`(0.263) `4866966`(0.263) `4866838`(0.211) `4866940`(0.211) |
| SWE1_AMM_014 | SYS-RA-AMM-123 | Confirmation Tone Mixing with ENT and INFO1 | Focus and Ducking | `4865968`(0.138) `4866316`(0.111) `4866059`(0.107) `4865969`(0.103) `4866291`(0.098) |
| SWE1_AMM_015 | SYS-RA-AMM-124 | Confirmation Tone Suppression on INFO2 | Focus and Ducking | `4866284`(0.192) `4865969`(0.16) `4865967`(0.12) `4866059`(0.12) `4865970`(0.115) |
| SWE1_AMM_030 | SYS-RA-AMM-173 | Audio Source Priority Arbitration | Focus and Ducking | `4866718`(0.152) `4866719`(0.152) `4866451`(0.143) `4866970`(0.139) `4866966`(0.138) |
| SWE1_AMM_031 | SYS-RA-AMM-178 | INFO2 Priority and Entertainment Interruptio | Focus and Ducking | `4866055`(0.167) `4866107`(0.167) `4866838`(0.154) `4866849`(0.154) `4866940`(0.154) |
| SWE1_AMM_032 | SYS-RA-AMM-179 | INFO2 Source Priority Handling | Focus and Ducking | `4866055`(0.242) `4865915`(0.194) `4866451`(0.156) `4866452`(0.154) `4866966`(0.154) |
| SWE1_AMM_086 | SYS-RA-AMM-272 | Audio Source Priority Management | Focus and Ducking | `4866107`(0.25) `4866442`(0.25) `4866220`(0.241) `4866916`(0.2) `4866838`(0.19) |
| SWE1_AMM_233 | SYS-RA-AMM-583 | Mix Signal Source with Active Information So | Focus and Ducking | `4866916`(0.562) `4866955`(0.294) `4866838`(0.25) `4866862`(0.25) `4866935`(0.25) |
| SWE1_AMM_286 | SYS-RA-AMM-895 | Alternate and Main Audio Mixing | Focus and Ducking | `4866916`(0.19) `4866152`(0.111) `4866153`(0.111) `4866838`(0.111) `4866849`(0.111) |
| SWE1_AMM_287 | SYS-RA-AMM-896 | Main Audio Ducking for Alternate Audio | Focus and Ducking | `4866566`(0.129) `4866891`(0.118) `4866696`(0.111) `4866697`(0.111) `4866895`(0.106) |
| SWE1_AMM_309 | SYS-RA-AMM-1089 | User Playback Interruption during HFP Call | Focus and Ducking | `4866055`(0.226) `4865936`(0.12) `4866904`(0.108) `4866935`(0.108) `4866028`(0.107) |
| SWE1_AMM_312 | SYS-RA-AMM-1106 | Fixed Navigation Entertainment Fade-Out | Focus and Ducking | `4866127`(0.167) `4866151`(0.129) `4867642`(0.117) `4866088`(0.114) `4866126`(0.114) |
| SWE1_AMM_313 | SYS-RA-AMM-1107 | Relative Navigation Entertainment Fade-Out | Focus and Ducking | `4866875`(0.143) `4866874`(0.138) `4866295`(0.136) `4866494`(0.136) `4866107`(0.125) |
| SWE1_AMM_314 | SYS-RA-AMM-1108 | Navigation Entertainment Attenuation | Focus and Ducking | `4866107`(0.227) `4866838`(0.222) `4866940`(0.222) `4866566`(0.208) `4866457`(0.2) |
| SWE1_AMM_315 | SYS-RA-AMM-1109 | Entertainment Mute at Minimum Attenuated Vol | Focus and Ducking | `4866107`(0.182) `4866916`(0.182) `4866838`(0.167) `4866849`(0.167) `4866940`(0.167) |
| SWE1_AMM_316 | SYS-RA-AMM-1110 | Adjusted Entertainment Volume Transmission D | Focus and Ducking | `4866130`(0.143) `4866875`(0.143) `4866874`(0.139) `4866113`(0.133) `4866127`(0.121) |
| SWE1_AMM_317 | SYS-RA-AMM-1111 | Navigation Volume Adjustment Synchronization | Focus and Ducking | `4866107`(0.208) `4866295`(0.174) `4866298`(0.174) `4866113`(0.167) `4866891`(0.133) |
| SWE1_AMM_027 | SYS-RA-AMM-160 | TLM Idle State Mute Handling | Mute Requests | `4866032`(0.417) `4866033`(0.265) `4866132`(0.206) `4866127`(0.2) `4866151`(0.2) |
| SWE1_AMM_028 | SYS-RA-AMM-170 | TLM Operational State Unmute Handling | Mute Requests | `4866033`(0.343) `4866032`(0.267) `4866240`(0.242) `4866126`(0.231) `4866150`(0.22) |
| SWE1_AMM_058 | SYS-RA-AMM-223 | Entertainment Mute Status Communication | Mute Requests | `4866129`(0.227) `4866120`(0.182) `4866121`(0.182) `4866132`(0.176) `4866122`(0.16) |
| SWE1_AMM_059 | SYS-RA-AMM-224 | ENTMuted Source Scope | Mute Requests | `4866440`(0.261) `4866495`(0.222) `4866835`(0.208) `4866121`(0.19) `4866129`(0.182) |
| SWE1_AMM_060 | SYS-RA-AMM-225 | Entertainment Mute Toggle Request Handling | Mute Requests | `4866122`(0.286) `4866132`(0.226) `4866131`(0.158) `4866120`(0.143) `4866121`(0.143) |
| SWE1_AMM_061 | SYS-RA-AMM-226 | Power Button Mute Handling | Mute Requests | `4866122`(0.143) `4866132`(0.109) `4866131`(0.096) `4866902`(0.091) `4866926`(0.091) |
| SWE1_AMM_066 | SYS-RA-AMM-231 | Entertainment Mute Status Synchronization | Mute Requests | `4866121`(0.211) `4866129`(0.2) `4866132`(0.156) `4866120`(0.15) `4866689`(0.136) |
| SWE1_AMM_068 | SYS-RA-AMM-233 | TLM Mute Switch Handling without ICS Node | Mute Requests | `4866131`(0.475) `4866132`(0.325) `4866157`(0.324) `4866122`(0.167) `4867518`(0.118) |
| SWE1_AMM_069 | SYS-RA-AMM-234 | TLM Entertainment Mute Request Handling | Mute Requests | `4866132`(0.371) `4866131`(0.256) `4866122`(0.194) `4866158`(0.172) `4866032`(0.171) |
| SWE1_AMM_070 | SYS-RA-AMM-235 | Internal Mute State Preservation and Restora | Mute Requests | `4866133`(0.265) `4866024`(0.212) `4866134`(0.196) `4866032`(0.188) `4866025`(0.162) |
| SWE1_AMM_071 | SYS-RA-AMM-236 | Entertainment Mute Release on Volume Adjustm | Mute Requests | `4866134`(0.292) `4866131`(0.184) `4866132`(0.182) `4866025`(0.163) `4866133`(0.163) |
| SWE1_AMM_076 | SYS-RA-AMM-246 | Information Source Mute Routing Configuratio | Mute Requests | `4866495`(0.167) `4866155`(0.148) `4866154`(0.132) `4866718`(0.13) `4866719`(0.13) |
| SWE1_AMM_078 | SYS-RA-AMM-248 | Ignore Information Mute Request Without ICS | Mute Requests | `4866157`(0.36) `4866131`(0.297) `4866132`(0.2) `4866122`(0.192) `4866495`(0.19) |
| SWE1_AMM_079 | SYS-RA-AMM-249 | Ignore Information Mute Status Event Without | Mute Requests | `4866158`(0.381) `4866132`(0.344) `4866157`(0.296) `4866131`(0.256) `4866122`(0.185) |
| SWE1_AMM_179 | SYS-RA-AMM-501 | VSIM Entertainment Mute Handling | Mute Requests | `4866689`(0.286) `4866695`(0.192) `4866477`(0.19) `4866693`(0.182) `4866024`(0.172) |
| SWE1_AMM_180 | SYS-RA-AMM-502 | VSIM Information 1 Mute Handling | Mute Requests | `4866690`(0.25) `4866503`(0.2) `4866691`(0.19) `4866696`(0.185) `4866718`(0.182) |
| SWE1_AMM_181 | SYS-RA-AMM-503 | VSIM Information 2 Mute Handling | Mute Requests | `4866691`(0.25) `4866508`(0.2) `4866690`(0.19) `4866697`(0.185) `4866719`(0.182) |
| SWE1_AMM_182 | SYS-RA-AMM-504 | VSIM Hands-Free Microphone Mute | Mute Requests | `4866692`(0.364) `4866698`(0.308) `4866256`(0.182) `4866693`(0.174) `4866259`(0.16) |
| SWE1_AMM_184 | SYS-RA-AMM-507 | VSIM Entertainment Unmute Handling | Mute Requests | `4866695`(0.154) `4866121`(0.143) `4866477`(0.143) `4866129`(0.136) `4866693`(0.136) |

## 五、建議分析層之作法

1. 逐葉讀候選之 Description（JSON 內含前 160 字），非只看分數。
2. 命中者採為錨；候選皆不合者，優先於全文 PDF 直接檢索該葉語意
   （B1 之 275–278 即以此法人工改錨至 1.5.4 Variables）。
3. 兩處以上同文者，比照 R-AM2 之「一對多者填 PENDING: DR-AM1」處置，
   或依 B1 先例以不同子章節錨區分並於 sibling 提示註明。
4. 定案後之 §四 表下放，執行層即可開 B2；本表不入交付、不作錨源。
