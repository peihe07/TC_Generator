# Audio Management — 上繳包 05：B2 候選錨表（**提案，不具裁定效力**）

- 日期：2026-08-26（rev 2）
- 執行層：Claude Code
- 性質：**提案**。錨定屬分析層（03 包 §三.4「執行層不得自行改錨」）。

---

## 一、方法與其實測準確率

採 03 包 §四 所揭露之方法：**全域單調序列對位**（SWE.1 文序 × CFTS 文序）。

改採此法之依據為實測，非偏好。B1 之 50 個已裁定錨依 SWE 編號排序後，
**49 個相鄰對中錨值下降次數為 0** —— 完全單調。此結構約束為逐葉取最相似者
所完全捨棄之訊息。

以 B1 之 43 個池內已裁定錨回測（標準答案為 Pei 已准之 03 包 §四 表）：

| 方法 | 命中 |
|---|---|
| 純內容相似度取 top-1（rev 1 之作法） | 21/43 = 49% |
| **全域單調序列對位（本版）** | **42/43 = 98%** |

唯一錯配：`SWE1_AMM_226` 正解 4866902、提案給出 **4866901**（相鄰一位）。
以 `--validate` 可重現本數字。

**rev 1 已撤除之設計：** 初版逐葉輸出單一挑選並標 `strong`／`weak` 信心度；
回測顯示標為 `strong` 者僅 6/10 正確，該標籤所傳達之把握是它沒掙得的。
本版不作信心宣稱，改以**兩法是否一致**作為需人工細讀之訊號。

## 二、本批結果：需細讀者僅 13 葉

| 狀態 | 葉數 | 意義 |
|---|---|---|
| 對位定錨且內容清單印證 | **37** | 兩獨立方法一致，優先採信 |
| 對位定錨但內容清單不含 | 4 | **兩法分歧，需人工判讀** |
| 對位無解 | 9 | **需人工判讀**，多疑為池外錨 |
| 合計 | 50 | |

分析層之工作量因此自 50 葉降為 **13 葉**。

## 三、批次組成（依 02 包 §三）

| Test Set | 葉數 |
|---|---|
| Audio Arbitration | 13 |
| Focus and Ducking | 18 |
| Mute Requests | 19 |
| **合計** | **50** |

與 02 包 §三「B2 = Audio Arbitration 後 13 ＋ Focus and Ducking（18）
＋ Mute Requests 前 19 = 50」逐項相符。

## 四、需人工判讀者（優先處理）

### 4.1 兩法分歧（4 葉）

| SWE ID | Title | Test Set | 對位給出 | 內容 top-3 |
|---|---|---|---|---|
| SWE1_AMM_030 | Audio Source Priority Arbitration | Focus and Ducking | `CFTS019-4866047` | `4866718` `4866719` `4866451` |
| SWE1_AMM_031 | INFO2 Priority and Entertainment Interru | Focus and Ducking | `CFTS019-4866054` | `4866055` `4866107` `4866838` |
| SWE1_AMM_286 | Alternate and Main Audio Mixing | Focus and Ducking | `CFTS019-4867773` | `4866916` `4866152` `4866153` |
| SWE1_AMM_061 | Power Button Mute Handling | Mute Requests | `CFTS019-4866123` | `4866122` `4866132` `4866131` |

### 4.2 對位無解（9 葉）

| SWE ID | Title | Test Set | 對位給出 | 內容 top-3 |
|---|---|---|---|---|
| SWE1_AMM_310 | VR Session Cancellation on Call Initiati | Audio Arbitration | — | `4866908` `4866930` `4866906` |
| SWE1_AMM_287 | Main Audio Ducking for Alternate Audio | Focus and Ducking | — | `4866566` `4866891` `4866696` |
| SWE1_AMM_309 | User Playback Interruption during HFP Ca | Focus and Ducking | — | `4866055` `4865936` `4866904` |
| SWE1_AMM_312 | Fixed Navigation Entertainment Fade-Out | Focus and Ducking | — | `4866127` `4866151` `4867642` |
| SWE1_AMM_313 | Relative Navigation Entertainment Fade-O | Focus and Ducking | — | `4866875` `4866874` `4866295` |
| SWE1_AMM_314 | Navigation Entertainment Attenuation | Focus and Ducking | — | `4866107` `4866838` `4866940` |
| SWE1_AMM_315 | Entertainment Mute at Minimum Attenuated | Focus and Ducking | — | `4866107` `4866916` `4866838` |
| SWE1_AMM_316 | Adjusted Entertainment Volume Transmissi | Focus and Ducking | — | `4866130` `4866875` `4866874` |
| SWE1_AMM_317 | Navigation Volume Adjustment Synchroniza | Focus and Ducking | — | `4866107` `4866295` `4866298` |

此組多為序列尾端之高編號葉。B1 之經驗顯示，對位無解常見成因為**該葉之錨
根本不在池中**（圖表型物件遭匯出遺漏，A-AM03／DR-AM3）。建議比照 R-AM2′
之處置：於全文 PDF 檢索該葉語意，尋得 `State:Approved` 物件即為池外錨，
並登記於池外錨表。

## 五、兩法一致者（37 葉，建議逕採）

完整表（含錨之 Description 前 200 字供核）見
`batches/B2_anchor_proposal.json` 之 `anchor` / `anchor_desc` 鍵。

| SWE ID | Title | Test Set | 對位給出 | 內容 top-3 |
|---|---|---|---|---|
| SWE1_AMM_229 | Ignore TA During Active VR Session | Audio Arbitration | `CFTS019-4866906` | `4866906` `4866929` `4866913` |
| SWE1_AMM_230 | Cancel VR for User-Selected Navigation P | Audio Arbitration | `CFTS019-4866908` | `4866908` `4866930` `4866906` |
| SWE1_AMM_231 | Delay Navigation During Active VR Sessio | Audio Arbitration | `CFTS019-4866911` | `4866911` `4866931` `4866908` |
| SWE1_AMM_232 | Ignore TA During Active Phone Audio | Audio Arbitration | `CFTS019-4866913` | `4866913` `4866933` `4866906` |
| SWE1_AMM_234 | Cancel TA or Navigation for Phone/VR Req | Audio Arbitration | `CFTS019-4866925` | `4866966` `4866901` `4866905` |
| SWE1_AMM_235 | Cancel TA on Incoming Call | Audio Arbitration | `CFTS019-4866927` | `4865871` `4866903` `4866927` |
| SWE1_AMM_236 | Ignore TA During Active VR Session | Audio Arbitration | `CFTS019-4866929` | `4866906` `4866929` `4866913` |
| SWE1_AMM_237 | Cancel VR for Customer-Selected Navigati | Audio Arbitration | `CFTS019-4866930` | `4866908` `4866930` `4866906` |
| SWE1_AMM_238 | Delay Navigation Until VR Completion | Audio Arbitration | `CFTS019-4866931` | `4866911` `4866931` `4866908` |
| SWE1_AMM_239 | Ignore TA During Phone Audio | Audio Arbitration | `CFTS019-4866933` | `4866913` `4866933` `4866906` |
| SWE1_AMM_259 | Handle Invalid Cabin EQ IDs (S00 / SFF) | Audio Arbitration | `CFTS019-4867579` | `4867579` `4867580` `4867578` |
| SWE1_AMM_260 | Handle Unknown Cabin EQ IDs | Audio Arbitration | `CFTS019-4867580` | `4867579` `4867580` `4867581` |
| SWE1_AMM_004 | Entertainment Audio Priority Handling | Focus and Ducking | `CFTS019-4865916` | `4865916` `4866107` `4866718` |
| SWE1_AMM_008 | Information Source Audio Focus Priority | Focus and Ducking | `CFTS019-4865931` | `4866107` `4865931` `4866966` |
| SWE1_AMM_014 | Confirmation Tone Mixing with ENT and IN | Focus and Ducking | `CFTS019-4865968` | `4865968` `4866316` `4866059` |
| SWE1_AMM_015 | Confirmation Tone Suppression on INFO2 | Focus and Ducking | `CFTS019-4865969` | `4866284` `4865969` `4865967` |
| SWE1_AMM_032 | INFO2 Source Priority Handling | Focus and Ducking | `CFTS019-4866055` | `4866055` `4865915` `4866451` |
| SWE1_AMM_086 | Audio Source Priority Management | Focus and Ducking | `CFTS019-4866220` | `4866107` `4866442` `4866220` |
| SWE1_AMM_233 | Mix Signal Source with Active Informatio | Focus and Ducking | `CFTS019-4866916` | `4866916` `4866955` `4866838` |
| SWE1_AMM_027 | TLM Idle State Mute Handling | Mute Requests | `CFTS019-4866032` | `4866032` `4866033` `4866132` |
| SWE1_AMM_028 | TLM Operational State Unmute Handling | Mute Requests | `CFTS019-4866033` | `4866033` `4866032` `4866240` |
| SWE1_AMM_058 | Entertainment Mute Status Communication | Mute Requests | `CFTS019-4866120` | `4866129` `4866120` `4866121` |
| SWE1_AMM_059 | ENTMuted Source Scope | Mute Requests | `CFTS019-4866121` | `4866440` `4866495` `4866835` |
| SWE1_AMM_060 | Entertainment Mute Toggle Request Handli | Mute Requests | `CFTS019-4866122` | `4866122` `4866132` `4866131` |
| SWE1_AMM_066 | Entertainment Mute Status Synchronizatio | Mute Requests | `CFTS019-4866129` | `4866121` `4866129` `4866132` |
| SWE1_AMM_068 | TLM Mute Switch Handling without ICS Nod | Mute Requests | `CFTS019-4866131` | `4866131` `4866132` `4866157` |
| SWE1_AMM_069 | TLM Entertainment Mute Request Handling | Mute Requests | `CFTS019-4866132` | `4866132` `4866131` `4866122` |
| SWE1_AMM_070 | Internal Mute State Preservation and Res | Mute Requests | `CFTS019-4866133` | `4866133` `4866024` `4866134` |
| SWE1_AMM_071 | Entertainment Mute Release on Volume Adj | Mute Requests | `CFTS019-4866134` | `4866134` `4866131` `4866132` |
| SWE1_AMM_076 | Information Source Mute Routing Configur | Mute Requests | `CFTS019-4866155` | `4866495` `4866155` `4866154` |
| SWE1_AMM_078 | Ignore Information Mute Request Without  | Mute Requests | `CFTS019-4866157` | `4866157` `4866131` `4866132` |
| SWE1_AMM_079 | Ignore Information Mute Status Event Wit | Mute Requests | `CFTS019-4866158` | `4866158` `4866132` `4866157` |
| SWE1_AMM_179 | VSIM Entertainment Mute Handling | Mute Requests | `CFTS019-4866689` | `4866689` `4866695` `4866477` |
| SWE1_AMM_180 | VSIM Information 1 Mute Handling | Mute Requests | `CFTS019-4866690` | `4866690` `4866503` `4866691` |
| SWE1_AMM_181 | VSIM Information 2 Mute Handling | Mute Requests | `CFTS019-4866691` | `4866691` `4866508` `4866690` |
| SWE1_AMM_182 | VSIM Hands-Free Microphone Mute | Mute Requests | `CFTS019-4866692` | `4866692` `4866698` `4866256` |
| SWE1_AMM_184 | VSIM Entertainment Unmute Handling | Mute Requests | `CFTS019-4866695` | `4866695` `4866121` `4866477` |

## 六、已知限制

1. **同文異錨無法區辨。** 池中存在逐字相同之 Description（queue 判定、
   SOS 靜音等），對位在此類並列候選間之選擇仍屬偶然；B1 之 130/139、
   198/218、199/219 即屬此類，惟單調約束使其多能落在正確位置。
2. **單調性為經驗事實而非保證。** B1 實測 0 反轉，但若上游文件重排，
   本法之準確率將隨之失效，須以 `--validate` 重測後再用。
3. **池外錨無解。** 見 §4.2。

## 七、建議之後續

1. 分析層讀 §四 之 13 葉並定案，§五 之 37 葉可逕採或抽查。
2. 定案後之 §四 型表下放，執行層即可開 B2（context 建置、生成、自檢、
   lint、寫回之流程已於 B1 跑通，可直接沿用）。
3. 本表不入交付、不作錨源。
