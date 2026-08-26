# 上繳包 30 —— 五條轉指全部指向 CUSW：假說否證，而否證的方式指出了答案在哪

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/30_crossref_chase.md`
  ＋ 其附件 `30a_vf169.md`
- **停止條件 79／80／81 皆未觸發**；1–78 亦全未觸發
- **`pilot-01`／`rvc-01` 一字未動**；無 deferred 被解除
- **git 未執行**（§七為建議）

---

## 摘要

| 任務 | 結果 |
|---|---|
| §一 T1 | 五條**全部查得**（停止條件 79 未觸發） |
| §一 T2 | **五條全部 `[Radio:VP4R84] [EE Architecture:CUSW]` —— 不適用本專案** |
| §一 T3 | 全部落在 `§1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm`，**非組 A、非組 B**（停止條件 80 未觸發） |
| §一 T4 | 三方對照表見 §1.5 |
| §一 T5 | `{4821587}`／`{4821592}` 一併取，同為 CUSW |
| §四.1 | R-G37 抄錄相符；A-DM40 已於 29 輪登記，本輪補其與 R-G37 之連結 |
| §四.2 | `pilot-01` 凍結登記已入 `BACKLOG.md` |
| §四.3 | **`{CFTS013-930}` 逐字全文取得，R-DM51 之依據成立**（停止條件 81 未觸發） |
| §四.4 | DR-DM7 改 **CLOSED（R-DM44，16 輪）**；A-DM20 改 `RESOLVED-BY-SCOPE-CHANGE`；**A11 關閉** |
| 30a | 素材**未落磁碟**，T1 完成、T2–T5 待置入 |

**§1.1 之假說否證。** 但其否證方式產生了一件比假說更有用的事：
**答案看得見，只是掛在被宣告為不適用的條文上。**

---

## 一、五條轉指條號

### 1.1 T2 之判準與其值域（R-G37(b)）

**依 R-G37(c)，本檔之值域本輪重新實測**（不沿用 CFTS_013 之判準）：

```text
CFTS_020 之 `EE Architecture` 值域（出現次數計）
  'CUSW': 908 / 'Atlantis High': 764 / 'PowerNet': 749 / 'Atlantis Mid': 207 / 'All': 83
  通配值（All／ALL／Default／*）之出現：83

`Radio` 值域：`R1H` 850 ／ `All` 0 ／ `noSys` 198 ／ 相異值 23
```

**與 29 輪之認知不同須具名**：上繳 29 §2.2 我寫「CFTS_020 之
`EE Architecture` 值域**不含 `All`**」，並據此判 21／28 兩輪未受
A-DM40 影響。**本輪實測 `All` 出現 83 次。**

故判準改為 `("R1H" in Radio or "All" in Radio) and ("Atlantis High" in EE or "All" in EE)`，
且**回溯結論須修正** —— 見 §1.6。

### 1.2 T1／T2／T3 —— 逐字全文、適用性、章節位置

```text
# T1／T2／T3 —— 五條之逐字全文、適用性、章節位置

========================================================================
## {4821587}  適用本專案：**否**   para[7014]
   章節：1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm  （其標題於 para[7009]）
   Radio=VP4R84 | EE=CUSW
   ---
   When the DCSD is in 'Display Hot State' (refer to CFTS013-967), the DCSD shall notify the HU by sending $DCSD_DISP_STAT$ = [DISP_HOT]. See {CFTS013-967} for the DCSD Display Hot Algorithm. See the DCSD Display Hot Diagnostics below for other details.

========================================================================
## {4821589}  適用本專案：**否**   para[7020]
   章節：1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm  （其標題於 para[7009]）
   Radio=VP4R84 | EE=CUSW
   ---
   When the DCSD determines it wants to turn off it's backlighting (see {CFTS013-XXX}), the DCSD shall send $DCSD_DISP_STAT$ = [DISP_OFF].

========================================================================
## {4821590}  適用本專案：**否**   para[7023]
   章節：1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm  （其標題於 para[7009]）
   Radio=VP4R84 | EE=CUSW
   ---
   When the HU sees the transition from $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF] the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].

========================================================================
## {4821591}  適用本專案：**否**   para[7026]
   章節：1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm  （其標題於 para[7009]）
   Radio=VP4R84 | EE=CUSW
   ---
   When the DCSD sees the transition to $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] the DCSD shall stop displaying the screen sent by the HU and the DCSD shall turn off its backlighting in order to help it cool down.

========================================================================
## {4821592}  適用本專案：**否**   para[7029]
   章節：1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm  （其標題於 para[7009]）
   Radio=VP4R84 | EE=CUSW
   ---
   While the DCSD is still in the Hot state and the HU is sending $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity], if the HU determines it needs to have the display temporarily turn back on, the HU shall send $TGW_DISP_STAT$ <> [DISP_OFF] and $RQ_DISP_INTS$ = [current non-zero value].
```

**五條皆查得（停止條件 79 未觸發），五條皆不適用本專案。**
五條同屬 `§1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm`，
**既不在組 A（`4820282`–`4820288`）亦不在組 B（`4820289`–`4820292`）**
—— 停止條件 80 未觸發。

### 1.3 §1.1 假說之判定：**否證**

假說為「五條落在組 A 之範圍或其鄰近 → 組 A 與 CFTS_013 §1.5.3
為同一套流程之兩半」。

**實測：五條落在 CUSW 之 §1.15.5.5.2，Radio 為 `VP4R84`。**
與組 A（`R1H, VP5R120, R1M` ／ `PowerNet, Atlantis High`）無交集。

**A1／A2 不能因此自解。**

### 1.4 但否證之方式指出了答案在哪

追這五個句子在 CFTS_020 全檔之其他出現：

```text

========================================================================
## {4821587} 之句子在全檔之出現（key: the DCSD shall notify the HU by sending $DCSD_DISP_STAT$ = […）
   命中 5 處
     {4819860} 否  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=Atlantis Mid, PowerNet, Atlantis High
     {4820671} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820949} 否  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=Atlantis High, PowerNet, Atlantis Mid
     {4821309} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821587} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW

========================================================================
## {4821589} 之句子在全檔之出現（key: When the DCSD determines it wants to turn off it's backlight…）
   命中 5 處
     {4819862} 否  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=PowerNet, Atlantis High, Atlantis Mid
     {4820673} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820951} 否  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=PowerNet, Atlantis Mid, Atlantis High
     {4821311} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821589} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW

========================================================================
## {4821590} 之句子在全檔之出現（key: the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_…）
   命中 1 處
     {4820283} **適用**  §1.11.2.2 DCSD Display Hot Behavior
        Radio=R1H, VP5R120, R1M | EE=PowerNet, Atlantis High

========================================================================
## {4821591} 之句子在全檔之出現（key: the DCSD shall stop displaying the screen sent by the HU…）
   命中 5 處
     {4819864} 否  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=Atlantis High, PowerNet, Atlantis Mid
     {4820675} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820953} 否  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=noSys | EE=PowerNet, Atlantis Mid, Atlantis High
     {4821313} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821591} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW

========================================================================
## {4821592} 之句子在全檔之出現（key: if the HU determines it needs to have the display temporaril…）
   命中 12 處
     {4819854} 否  §1.8.2.5.1 Standard' DCSD Display Hot Algorithm
        Radio=VP384, VP5R120, VP4R84, VP484 | EE=PowerNet
     {4819865} **適用**  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=R1H, R1M, R1L-R, R1L | EE=Atlantis Mid, Atlantis High, PowerNet
     {4820028} 否  §1.8.5.7 FPDM Display Hot Algorithm
        Radio=noSys | EE=Atlantis High
     {4820285} **適用**  §1.11.2.2 DCSD Display Hot Behavior
        Radio=R1M, VP5R120, R1H | EE=Atlantis High, PowerNet
     {4820665} 否  §1.15.1.5.1 Standard' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820676} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820943} 否  §1.15.2.5.1 Standard' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4820954} **適用**  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=R1H, R1L, R1M, R1L-R | EE=PowerNet, Atlantis Mid, Atlantis High
     {4821303} 否  §1.15.4.5.1 Standard' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821314} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821581} 否  §1.15.5.5.1 Standard' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
     {4821592} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm
        Radio=VP4R84 | EE=CUSW
```

**兩項結構性事實（實測，非推論）**：

**(1) CFTS_020 把同一套 Multi-stage DCSD 演算法按架構複製了五份**
（`§1.8.2.5.2`／`§1.15.1.5.2`／`§1.15.2.5.2`／`§1.15.4.5.2`／`§1.15.5.5.2`），
而其中 **DCSD 側之條文一律為 `noSys` 或 `CUSW`** —— 五份無一適用
`R1H`／`Atlantis High`。

即：**CFTS_013 §1.5.3（13/13 適用本專案）所轉指之「關閉時實際送什麼」，
在 CFTS_020 之每一個版本裡都宣告不適用本專案。**
**這是一條跨檔之懸空引用。**

**(2) `{4821590}` 與組 A 之 `{4820283}` —— 後件逐字相同，前件不同。**

> `{4821590}`（CUSW）
> `When the HU sees the transition from $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF]` **the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].**
>
> `{4820283}`（**適用本專案**，組 A）
> `When the HU has finished displaying the Display Hot warning screen and determines that the DCSD display should now be 'Turned Off' to help it cool down,` **the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].**

**組 A 缺之判準（「何時算顯示完畢」），multi-stage 版本給了：
DCSD 送出 `[DISP_HOT] → [DISP_OFF]` 之轉換。**
而 CFTS_013 `{4943104}` 逐字說那個轉換發生在 popup 顯示 **10 秒**之後，
且 `Note: Only DCSD shall implement 10 sec timer.`

**——即 DR-DM10(b) 之答案是看得見的，只是掛在宣告為不適用之條文上。**

> **本層之比對限度須具名**：上述比對之 key 為**後件之子字串**
> （`the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity]`），
> 即 A-DM29 所警之形態。**故本層並列兩條之前件全文，使差異可見，
> 不宣稱兩條為同一條。** 是否 compose 屬 DR-DM10(a)，Tier 2。


### 1.7 【補測】適用本專案之對應條**存在** —— HU 側有，DCSD 側無

§九初稿我寫「一個適用本專案之 multi-stage DCSD 關閉序列是否存在於他處，
我沒有查」。**寫完就去查了**，結果推翻了那一句：

```text
# 判準：本體含 `turn off (its|it's|the) backlight`（忽略大小寫），R-G37 新判準判適用性
  全檔命中 13 條；**其中適用本專案 2 條**

  {4819862} 否  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4819864} 否  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4820025} 否  §1.8.5.7 FPDM Display Hot Algorithm
  {4820289} **適用**  §1.11.2.2 DCSD Display Hot Behavior
      When the DCSD Display transitions to a Hot state (> 85 degrees C) from a non-Hot state (<= 85 degrees C), and if there is no high priority screen (RVC), then DCSD shall: Send CAN signal $DCSD_DISP_STAT$=[DISP_HOT] Set the DTC (B1429-00) Radio Display High Temperature after the enable conditions and 
  {4820292} **適用**  §1.11.2.2 DCSD Display Hot Behavior
      During Display HOT condition, Upon dismissing high priority screen ( RVC ), DCSD shall turn OFF the backlight (full screen), disable the touch and send the $DCSD_DISP_STAT$ = [DISP_OFF].
  {4820673} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4820675} 否  §1.15.1.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4820951} 否  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4820953} 否  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4821311} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4821313} 否  §1.15.4.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4821589} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm
  {4821591} 否  §1.15.5.5.2 Multi-stage' DCSD Display Hot Algorithm

# 另測：適用本專案且本體含 `$DCSD_DISP_STAT$ = [DISP_OFF]` 者
  {4819863}  §1.8.2.5.2 Multi-stage' DCSD Display Hot Algorithm
      When the HU sees the transition from $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF] the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].
  {4820292}  §1.11.2.2 DCSD Display Hot Behavior
      During Display HOT condition, Upon dismissing high priority screen ( RVC ), DCSD shall turn OFF the backlight (full screen), disable the touch and send the $DCSD_DISP_STAT$ = [DISP_OFF].
  {4820952}  §1.15.2.5.2 Multi-stage' DCSD Display Hot Algorithm
      When the HU sees the transition from $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF] the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].
  適用者 = 3
```

**結構清楚（實測，非推論）**：五條 CUSW 條文各有**逐架構之孿生**。
以 `{4821589}`–`{4821591}` 之三元組為例，其對本專案之孿生為
`§1.8.2.5.2` 之 `{4819862}`／`{4819863}`／`{4819864}`
與 `§1.15.2.5.2` 之 `{4820951}`／`{4820952}`／`{4820953}`：

| 三元組之成員 | 角色 | 對本專案 |
|---|---|---|
| `{4819862}`／`{4820951}` | **DCSD 決定關背光 → 送 `[DISP_OFF]`** | **`Radio:noSys` —— 不適用** |
| **`{4819863}`／`{4820952}`** | **HU 見 `[DISP_HOT]→[DISP_OFF]` → 送 `[DISP_OFF]`＋`[0% Intensity]`** | **`[ECU:ETM, LTM]`，Radio 含 `R1H`，EE 含 `Atlantis High` —— 適用** |
| `{4819864}`／`{4820953}` | DCSD 見 HU 之 `[DISP_OFF]` → 停顯示、關背光 | `Radio:noSys` —— 不適用 |

即：**multi-stage 流程之 HU 側對本專案有定義，DCSD 側沒有。**
而 **CFTS_013 §1.5.3（13/13 適用）補的正是 DCSD 側** ——
監測頻率、三級門檻、10 秒計時器、`Only DCSD shall implement 10 sec timer`。

**兩份文件之分工在此對得上：CFTS_020 定 HU 側、CFTS_013 定 DCSD 側，
而 CFTS_020 內之 DCSD 側 multi-stage 條文一律 `noSys`（＝不由此檔定）。**

> **這使 §1.1 之假說以修正後之形態復活**：不是「五條落在組 A」，
> 而是「五條有逐架構之孿生，本專案之孿生其 HU 半適用、DCSD 半 `noSys`，
> 而 `noSys` 之空缺正由 CFTS_013 §1.5.3 填上」。
>
> **本層不作此裁定**（DR-DM10(a)，Tier 2）。**只陳列三項實測**：
> (a) 適用本專案之 `turn off … backlight` 條文全檔僅 **2** 條，
>     皆在 `§1.11.2.2`（組 B 之 `{4820289}`／`{4820292}`）；
> (b) 適用本專案且含 `$DCSD_DISP_STAT$ = [DISP_OFF]` 者 **3** 條 ——
>     `{4819863}`／`{4820952}`（multi-stage HU 側）與 `{4820292}`（組 B）；
> (c) multi-stage 之 DCSD 側對本專案 **0** 條。

**A13 之表述據此修正**（§七）：由「轉指全部指向不適用之條文」改為
「**轉指指向 CUSW 之副本，而本專案之副本其 DCSD 側為 `noSys`**」。


### 1.5 T4 —— 三方對照表（**只陳列，不判定**）

| 面向 | CFTS_020 組 A `{4820282}`–`{4820288}` | CFTS_020 組 B `{4820289}`–`{4820292}` | CFTS_013 §1.5.3 |
|---|---|---|---|
| 適用宣告 | `[Radio:R1H, VP5R120, R1M]` `[EE:PowerNet, Atlantis High]` | `[Radio:R1H]` `[EE:Atlantis High]` | `[Radio:R1L, R1H, R1L-R, R1M]` `[EE:All]` |
| 觸發門檻 | **未給**（DCSD 判定「in a Display Hot State」，轉指 `{CFTS013-629}`） | **`> 85 degrees C`** | **`50°C` 啟動／`51–55` 降亮度／`56–<60` 警示** |
| 有無警示階段 | **有**（`{4820283}` 之 `Display Hot warning screen`） | **無**（四動作中無警示） | **有**（`"Screen is Hot"`，`{4943100}`） |
| warning → off | **未給時長**（`has finished displaying … and determines`） | 不適用 | **`10 seconds`**，`Only DCSD shall implement 10 sec timer`（`{4943104}`） |
| 關閉時之動作 | `{4820284}` DCSD 收 `[DISP_OFF]`＋`[0%]` 才關，且 `continue to send [DISP_HOT]` | `{4820289}` DCSD 自主關背光並送 `[DISP_OFF]` | **轉指 `{4821589}`–`{4821591}` —— 該三條為 CUSW，不適用本專案** |
| 回復 | `{4820287}`／`{4820288}` 送 `[DISP_ON]` | `{4820290}` `<= 85 deg C` → 背光開、觸控啟用、`[DISP_ON]` | `{4943107}` `> 50 → <= 50` 恢復 `'Normal Screen Operation'` |
| 亮度降低之值 | **未給** | **未給** | **`每度 5%`（51→5%、55→25%）**（`{4943099}`） |

### 1.6 【更正】29 輪之回溯結論須修正

上繳 29 §2.2 之回溯檢查逐字為：

> 21／28 兩輪之適用性量測皆針對 CFTS_020，該檔之 `EE Architecture`
> 值域**不含 `All`**，**故未受本項影響**。

**本輪實測：CFTS_020 之 `EE Architecture` 含 `All`，出現 83 次。**
該回溯結論之依據為假。依 R-G19 具名更正，並重做回溯：

| 輪 | 量測 | 舊判準之風險 | 重做結果 |
|---|---|---|---|
| 21 | A-DM33 之組 A／組 B／Multi-stage 三組適用性 | 若某條之 EE 為 `All` 會被誤判為不適用 | **見下** |
| 28 | `rvc-01` 之 RVC 條文 24 條適用 | 同上 | **見下** |

```text
# 全檔重做：舊判準 vs 新判準之差集（實測）
  帶完整屬性行之條文 = 2169
  舊判準判「適用」 = 700
  新判準判「適用」 = 771
  **僅新判準命中（舊判準之漏網）= 71**
    {4819133}  Radio=VP5R120,VP1.5,VP3,High,VP2,VP2.5,VP4R7,VP484 | EE=All
    {4819134}  Radio=VP1.5,VP365,R1L,High,VP484,R1H,VP2R84,VP4,VP | EE=All
    {4819135}  Radio=R1M,R1L-R,VP384,R1L,VP3,VP2R7,VP4,High,VP1,V | EE=All
    {4819139}  Radio=R1M,R1H | EE=All
    {4819146}  Radio=R1H,R1L-R,R1L,R1M | EE=All
    {4819150}  Radio=R1H,R1L,R1L-R,R1M | EE=All
    {4819151}  Radio=R1H,R1L-R,R1M,R1L | EE=All
    {4819152}  Radio=R1M,R1L,R1H,R1L-R | EE=All
    {4819153}  Radio=R1M,R1L,R1L-R,R1H | EE=All
    {4819157}  Radio=R1L,R1H,R1M,R1L-R | EE=All
    {4819158}  Radio=R1M,R1L,R1H,R1L-R | EE=All
    {4819159}  Radio=R1L-R,R1H,R1L,R1M | EE=All
    {4819160}  Radio=R1L-R,R1H,R1M,R1L | EE=All
    {4819185}  Radio=R1H,R1L,R1L-R,R1M | EE=All
    {4819186}  Radio=R1H,R1M,R1L,R1L-R | EE=All
    {4819187}  Radio=R1L-R,R1M,R1H,R1L | EE=All
    {4819188}  Radio=R1L,R1M,R1H,R1L-R | EE=All
    {4819192}  Radio=R1L-R,R1L,R1H,R1M | EE=All
    {4819193}  Radio=R1H,R1M,R1L,R1L-R | EE=All
    {4819194}  Radio=R1M,R1H,R1L,R1L-R | EE=All
    …另 51 條

  21 輪之標的（4820282–4820292）落在漏網內者：**無**
  28 輪之標的（RVC × DCSD_DISP_STAT）落在漏網內者：**無**
```

**重做之結論**：全檔 2,169 條帶完整屬性行者中，舊判準判「適用」700 條、
新判準 771 條，**漏網 71 條**（其 `EE` 皆為 `All`）。

**惟 21 輪之標的（`4820282`–`4820292`）與 28 輪之標的
（RVC × `$DCSD_DISP_STAT$`）皆不在漏網內。**

即：**29 輪之結論（兩輪未受影響）仍然成立，但其理由是假的。**
真正的理由不是「該檔不含 `All`」，而是
**「我所量測的那兩組條文恰好逐一列舉架構名」**。
依 R-G19 分別更正 —— **這一次我重做了回溯，沒有再用一句斷言代替它。**

---

## 二、R-G37 之抄錄核對表

## 抄錄核對表 — 30_crossref_chase.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| — | R-G37 | `docs/fw036/RULINGS_LEDGER.md` | 815 | `0011b3b4bcac4ddb` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **57** 個，與各下放包原檔逐字元比對 **全數相符**（57 vs 57）。

置放依 R-G34：ledger 之新節「下放包 30 之全域條文」。
另於 **R-G27 條下留指標**（非 fence，不入核對表母體）：

> **對稱條之指標（下放包 30 §三，2026-08-26）—— 不改本條原文**：
> 本條防**過寬**（子字串／詞幹／近似比對）。其反面 —— 判準**過嚴**
> 而漏了涵蓋語意之通配值（`All`／`Default`）—— 由 **R-G37** 規制。
> **兩者同源：比對之語意未被明文界定。**

### 2.1 A-DM40 之狀態

**本項已於 29 輪登記**（本層自行登記）。下放包 30 §四.1 指定
「A-DM40 登記（HIGH）」—— 其內容已在，**狀態維持 `[CLOSED]`**：
缺陷已更正、回溯已重做（§1.6）。已於該節加註：下放包所稱之 HIGH 為
**其重要性**而非未結狀態，其重要性由 **R-G37** 承載。
**若分析層要求改標未結，請明示。**

---

## 三、`{CFTS013-930}` 之逐字全文與 R-DM51 依據之複核

以 `Document ID` 欄錨定（R-DM52），命中 **1 列**（`r14`，Category `Information`）：

```text
  --- Description 逐字全文 ---
  Note: There are essentially 2 variants of the LTM and ETM Radio HUs. Those with the touch screen integrated into the HU module are known as Associated variants while those HUs that interface to an external touch screen module (DCSD) are known as Disassociated variants (and are also referenced as a 'Silver Box' variants). In order to distinguish between these two types of HUs we are adding a suffix on the Component acronym of '_ADspl' for the Associated variants and '_DDspl'  for the Disassociated variants.

# R-DM51 之立條依據 —— 逐項複核
```

**逐項複核 R-DM51 之立條依據**：

| R-DM51 所稱 | 於 `{CFTS013-930}` |
|---|---|
| `Associated` 之定義 | **有** —— `Those with the touch screen integrated into the HU module are known as Associated variants` |
| `Disassociated` 之定義 | **有** —— `those HUs that interface to an external touch screen module (DCSD) are known as Disassociated variants` |
| `DCSD` 即 Disassociated | **有**（該括號逐字） |
| `_ADspl`／`_DDspl` 後綴 | **有** —— `adding a suffix on the Component acronym of '_ADspl' … and '_DDspl'` |

**R-DM51 之立條依據成立，且與其條文之表述逐字相符。停止條件 81 未觸發。**

全檔（`Analysis Report` 之 Description 欄）之命中：`_ADspl` 列計 2／
出現 5；`_DDspl` 列計 2／出現 6；`Associated` 列計 2／出現 6；
`Disassociated` 列計 2／出現 8。

> **上繳 29 §九第 2 項之自陳至此閉合** —— 我當時記「R-DM51 之立條依據
> 我仍未自行讀過」。**本輪讀了，它成立。**

---

## 四、DR-DM7 之更正、A-DM20 之記載、A11 關閉

### 4.1 DR-DM7 → **CLOSED（R-DM44，16 輪）**

其 `Status` 逐字改為：

> `**CLOSED（R-DM44，16 輪）**（下放包 30 §四.4 之更正）—— 其所求之用途已由
> R-DM33 消滅（PROXI 改需求驅動），**非取得所求之物**。28a §2.1(c) 之對帳判定為
> **全案結案而非部分結案**（R-DM44 引的就是本列原文，所求之物與所求之用途兩項逐字相同）。
> **Pei 2026-08-25 曾於封 4 發出本 DR** —— 該發信事實記此，惟本 DR 自 16 輪起即已結案。
> **重開條件（R-DM44）**：某參數之值域在 PROXI 中依 VF 而異時，以新編號重開`

**現行 DR 狀態**：12 筆 —— **9 SENT**、1 CLOSED（DM7）、
1 OPEN（DM11）、1 待 Pei 發（DM12）。

### 4.2 A-DM20 → `RESOLVED-BY-SCOPE-CHANGE`

依 R-DM44 之逐字指示（`不標 RESOLVED`）。其註記記明：

> R-DM44 立於 16 輪，其指示之兩處台帳動作**十二輪未執行** ——
> 直到 28a §2.1(c) 之對帳才被發現（A11）。**與 18 輪之「宣稱已執行而
> 未執行」同型，方向相反：那次是聲明超前事實，這次是事實落後裁決。**

並記 R-DM44 之重開條件與現況（`rvc-01` 已觸及 PROXI 之 RVC 兩參數，
惟六條 TC 未用到任何 PROXI 值，**故重開條件尚未成立**）。

### 4.3 A11 關閉

其內容（R-DM44 之台帳動作未執行）**本輪已執行完畢**，A11 自 A 類移除。

---

## 五、`BACKLOG.md` 之凍結登記

「DR-DM10 回覆後重審」節**首列**新增：

> | **`pilot-01` 三條之 `85 degrees C` —— 凍結，條件性正確**（下放包 30 §二）
> | 三條之 `85` 逐字取自 CFTS_020 `{4820289}`／`{4820290}`
> （`[Radio:R1H] [EE Architecture:Atlantis High]` 之專條），
> **其正確性以「本專案走 CFTS_020 之組 B」為前提**。
> CFTS_013 §1.5.3（13/13 適用，門檻 50）之出現使該前提成為**待證而非已證**
> | **維持現狀、不改、不寫回**；DR-DM10(a) 之答覆到達前不得寫回 |

第二列（原首列）標明其**已於 29 輪觸發**：#4 之 ER 3 之論據建立於
「只有組 A／組 B 兩種讀法」，**第三種讀法已出現**，故其前提已不完整。
**#4 未改**（停止條件 76）。

B 類另增 `B8`（五條轉指之追查，**本輪已執行**，其項改為「適用本專案之
對應版本是否存在」）、`B9`／`B10`（30a 之兩項 PROXI，素材未落磁碟）。

---

## 六、下放包 30a —— T1 完成，T2–T5 待素材

### 6.1 T1：查證本檔於 repo 內不存在

```text
# 查法（三處，逐字）
  features/display/inputs/ 含 'VF169' 者：0
  _intake/Display/ 含 'VF169' 者：0
  forms/ 含 'VF169' 者：0
  全 repo（排除 .git）含 'VF169' 之檔名：1
  全 repo 含 'Operative_States' 之檔名：0
```

**該檔不存在於 repo。** 30a §一已自行聲明其可及性（R-G35(c)），
**本層無須停手，T1 即為確認不存在。**

**T2–T5 未執行**（待 Pei 置入）。故：
- `reference:` 維持 **13 項**（未增 `vf169_doc`）
- `DATA_REQUESTS.md` 之 DR-DM5／DR-DM9(b) **未增附件欄**
- **A-DM41 未登記**
- PROXI 兩項以 `B9`／`B10` 記為待辦，**其逐字出處未登記**
  （其來源仍在分析層側，依 R-G36 不得自下放包轉抄）

### 6.2 停止條件 83 之自我複核

83：任一 TC 若引用 `RADIO_B3.RQ_DISP_INTS`、
`TELEMATIC_DISPLAY2.TGW_DISP_STATSts`、或兩項 PROXI 之任一者 → 停。

**`pilot-01`／`rvc-01` 九條之全部欄位實測：三者之出現皆為 0。**
（本輪未改任何 TC，故該結果與 29 輪相同。）

---

## 七、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | **組 A／組 B／CFTS_013 §1.5.3 三者何為準** | 004／005 全部門檻；**`pilot-01` 三條已凍結** | DR-DM10(a) |
| A2 | DCSD 側 warning → off | 原 pilot #2 | DR-DM10(b)（**答案在 CUSW 條文內，見 §1.4**） |
| A3 | 長拼法標籤與 HU 側值 | `{4820287}`；`rvc-01` 之 HU 側 | DR-DM9 |
| A4 | `Cat. SL` 之位置 | 凡涉 SL 之仲裁 | DR-DM2(a) |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| A9 | 倒車檔訊號 | 007 之觸發面向 | DR-DM11 |
| A10 | DR-DM4 之標的 | DR-DM4 之答覆 | 已重擬，待 Pei 發 |
| A12 | 007／008 之區分軸 | `rvc-01` 之 `leaf_id` | DR-DM12，待 Pei 發 |
| **A13** | **CFTS_013 §1.5.3 之轉指指向 CUSW 之副本；本專案之副本其 DCSD 側為 `noSys`、HU 側適用**（§1.7） | 該演算法之 DCSD 側關閉序列在 CFTS_020 內對本專案無定義 —— **其空缺是否正由 CFTS_013 §1.5.3 填上，屬 DR-DM10(a)** | **本輪新增，併入 DR-DM10(a)（建議）** |

~~A11~~ **本輪關閉**。A13 為本輪新增。

### B 類

| 編號 | 項 | 狀態 |
|---|---|---|
| B1–B19、B21 | 見上繳 25–29 | 不變 |
| B20 | CFTS_013 §1.5.1 未讀 | 29 輪解除 |
| B22 | CFTS_013 §1.5.2 未抽 | 不變（實測 0 條適用） |
| B23 | 五條轉指未追 | **本輪解除**（已追，皆 CUSW） |
| **B24** | **舊適用性判準之 71 條漏網未逐條複核** | §1.6 已證 21／28 之標的不在漏網內；**其餘 71 條之內容本輪未讀**，其中多條為 `Radio:R1H…R1M / EE:All` 之 R1 系列通條 |
| **B25** | **29 輪「CFTS_020 不含 `All`」之斷言未經量測即寫入上繳包** | 本輪更正（§1.6）。**其形態為 R-G22 所規制者 —— 斷言須由腳本產出，而我當時是憑印象寫的** |

B24／B25 為本輪新增。

---

## 八、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/30_crossref_chase.md \
  features/display/docs/handoff/30a_vf169.md \
  features/display/docs/upstream/30_crossref_chase.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): chase the five cross-references and find they are all CUSW

- all five clauses CFTS_013 points at for the shutdown sequence are declared
  for one CUSW radio, so the algorithm that governs this project points at a
  behaviour definition that does not
- the same five sentences recur in five parallel multi-stage sections, and
  every DCSD-side clause among them is either noSys or CUSW
- note that {4821590} and the applicable {4820283} share their consequent
  word for word while their antecedents differ, which is where the missing
  criterion for the warning stage would come from
- add R-G37: an applicability predicate must be derived from the values that
  file actually uses, wildcards included
- correct round 29's claim that CFTS_020 contains no All: it appears 83
  times, 71 clauses were being missed, and neither round's targets are among
  them, so those conclusions stand on a different reason
- verify {CFTS013-930}, which is what R-DM51 rests on, and it holds
- close DR-DM7 per R-DM44 and mark A-DM20 resolved by scope change, twelve
  rounds after the ruling said so
- freeze the pilot batch as conditionally correct until DR-DM10(a) answers
```

> `generated/pilot-01.json`／`generated/rvc-01.json` **一字未動**，不入。
> `feature.yaml` 未變更（30a T2 待素材），不入。036 母本未變更，亦不入。

---

## 九、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **B25 是本輪最難看的一項：我在上繳 29 寫了一句沒量過的話。**
   「CFTS_020 之 `EE Architecture` 值域不含 `All`」——
   那是**我用來證明 21／28 兩輪未受 A-DM40 影響的整個依據**。
   本輪一量，`All` 出現 83 次、漏網 71 條。
   **結論僥倖仍成立**（兩輪之標的不在漏網內），
   **但那是運氣，不是我的工作。** R-G22 立於 12 輪，
   規制的正是這件事，而我在一份宣告自己在做回溯檢查的文件裡犯了。

2. **71 條漏網之內容我沒讀**（B24）。
   我只證明了「21／28 之標的不在其中」，沒看那 71 條是什麼。
   其中多條為 `Radio:R1H…R1M / EE:All` 之 R1 系列通條 ——
   **那正是最可能與本專案相關的形狀。**

3. **§1.7 之補測把「查不到」變成「查到了」，而我原本打算只寫一句自陳交差。**
   初稿之第 3 項是「一個適用本專案之 multi-stage DCSD 關閉序列是否存在於
   他處，我沒有查」。**那句話寫完，我去查了，五分鐘的事** ——
   結果是 HU 側有、DCSD 側無，而那正好說明兩份文件如何分工。
   **本輪這是第二次**（27 輪之反向查證是第一次）**「自陳未驗」在寫下的
   當下就變成可驗**。**自陳欄不該是待辦清單的傾倒處。** 記此以為戒。
