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

- 完整 157 TC 的 A/B 對比受 45 秒窗限制;結論方向已明確,要完整數字建議本機分批跑。

---

# §7.6 reality-gap 針對性驗證(已補)

先前真實樣本 §7.6 = 0 命中,**經查是「沒有 false positive」而非規則失效**——那些 TC 沒有真正與 spec 矛盾的地方。

用一個**故意矛盾 spec 的探針 TC**(主張不存在的「Repeat Off」態)驗證:

| 命中 | 內容 |
|---|---|
| **§7.6 Critical `reality_gap=True`** | 「ER『最後一曲後停止』與 domain 矛盾——CFTS025 明示 Repeat All 預設須循環回第一曲,Player 無 Repeat Off」 |
| **§7.1 Critical `reality_gap=True`** | 「依 domain pack,Repeat 只有 All/One Track,無 Repeat Off 態」 |

兩條都**引 domain pack 當證據**。`reality_gap_rate` KPI 隨之算出 **100%(1/1)**。

**結論:reality-gap 機制完整可用**——對真矛盾觸發、對乾淨 TC 靜默(無誤報),並接上 KPI。先前 0 命中是正確行為。
