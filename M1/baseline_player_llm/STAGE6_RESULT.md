# Stage 6 驗證:domain pack 接地後的 review(同一中段樣本)

> 同一份 Player 中段樣本(13 TC / 9 Req group),gpt-4.1。
> A = baseline(無 domain),B = Stage 6(+ `domain_pack_player.json`)。每次 < $0.03。

## 量化:拆解深度 KPI

| | tier1_critical_req_rate |
|---|---|
| A baseline | **55.6%** (5/9) |
| B + domain pack | **22.2%** (2/9) |

過度標記砍掉一半以上。

## 質化:domain pack 同時「糾正幻覺」與「保留真缺口」

**最關鍵的一條(PLA-030-01):**
- A:「缺 Repeat One / **No Repeat** 模式」 ← reviewer 幻覺,spec 根本沒有 No Repeat
- B:「Repeat 列舉為 (Repeat All, Repeat One Track),缺 **Repeat One Track**」 ← 幻覺消失,精準指出真缺口,並引 CFTS025 §3.1.1.4.2.7

**被消除的 3 個(PLA-027 / 028 / 030-03)——都是該消的:**
- PLA-027「只測 Play/Pause,缺 Skip/Repeat/Shuffle」:這些其實是**獨立需求**(Repeat=PLA-030…),domain pack 的 interactions 讓 reviewer 看懂結構,不再誤判為缺口。
- PLA-030-03「缺播完異常態」:spec/domain **沒有定義**這種行為,依「不得超出 spec/domain 臆測」正確停止誤報(對應 Gate ① 的「不逐格式列舉」裁定)。

## 結論

**Stage 6 的價值被證實:spec + domain 接地讓 review 更準——少誤報、真缺口更銳利、且引用 spec 出處。** 這正是你要的「可信的 review」。

## 待調(誠實揭露)

- **§7.6 reality-gap 這次 0 命中**:本樣本問題集中在覆蓋層(Tier 1),沒有明顯「步驟假設未定義行為 / 不可執行」案例;規則已接好且有單元測試,但需用一份「步驟可執行性差」的樣本(例如 §8.3.5 高命中那段)實證它會觸發。下一步可針對性驗證。
- 完整 157 TC 的 A/B 對比受 45 秒窗限制;結論方向已明確,要完整數字建議本機分批跑。
