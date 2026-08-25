# 下放包 28a —— 核可、apparatus 凍結生效與三筆 DR 之最終全文（與 28 同一往返）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [28_batch2.md](28_batch2.md) 同屬第 28 輪
- 28 本文未改一字

---

## 一、Pei 之裁定（2026-08-25，逐字）

> 「寄 核可」

即：**三筆 DR 發出**；**R-PMH103／R-PMH104 核可**。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH105（R-PMH103／R-PMH104 之核可生效）
Pei 於 2026-08-25 核可 R-PMH103（覆核線之收束判準）與
R-PMH104（apparatus 凍結）。二條即刻生效。

**其效力起算之三項**：
(a) batch 1（8 條、7 leaf）之覆核線**結束** ——
    其殘餘為三項精化（切分之連接詞列舉／`SPLIT_REVIEW` 無第二來源／
    規格側全枚舉未做）＋ `-007` 之 `L160` 待確認，
    全數入 `DECISIONS.md` 之 KNOWN-INCOMPLETE，**不阻斷開批**；
(b) **不再新增檢查程式或檢查項** —— 現有 32 項 lint 與 13 支程式
    全數保留並繼續執行；
(c) batch 2（`Startup Sounds`，ch 8，6 leaf）**開批**。

**解凍條件不變**（R-PMH104(a)(b)）：某條已產出之 TC 經**實測**有誤
且為現行檢查所不能攔者，或 Pei 裁定。
```

```
R-PMH106（三筆 DR 之發出授權）
Pei 於 2026-08-25 裁定發出 `DR-PMH5`／`DR-PMH6`／`DR-PMH7`，
其內容依 28a §三之最終全文。

**執行層不得代為發出**（R-PMH83）。其職責為：
(a) 將 §三之三份全文寫入 `DATA_REQUESTS.md`（或指向本檔）；
(b) `SENT` 欄**留空**，待 Pei 告知**實際發出日期與對象**後方填
    —— **不得以本包之日期充當**（R-PMH43）；
(c) 三者之狀態於填入日期前維持 `DRAFT`。

**內容之變更須記明**：`DR-PMH5` 自 21a 之初版起經**兩次變更**
（24 包增欄位之問；25 包該問由字級座標自答，性質降為「請確認」），
且 **21a 所載之「p9 矩陣與 p8 之 `SU3.)` 相衝」一項已撤回** ——
A-PMH21 於 24 包改判為 `未對照`（其欄位為 `HEADUNIT POWER OFF`，
而 `PITA6.1` 逐字載免責畫面顯示於 head unit 轉為 On，二者互斥）。
**寄出之版本不得含該已撤回之主張。**
```

---

## 三、三份最終全文（可直接寄出）

> 收件對象：規格 p1 所載之 `HMI Lead: Paolo Visconti` 或其現任接手人。
> **凡引規格與素材處皆為逐字**。

---

### 3.1 DR-PMH5 —— p9 之能力矩陣

```text
Subject: Power Moding HMI — source of the capability matrix on page 9

Hello,

We are preparing the SWE.6 test cases for Power Moding HMI
(FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1, based on "Power Moding HMI
Logic and Flow R1 SR24 2A DCR22412 (January 24 2023)").

Page 10 of the logic and flow document states, verbatim:

    POWER MODING STATE MATRIX: Power Moding behavior shall not be developed
    without following the Power Moding State Matrix, which is in a separate
    Excel document. If this document is not available, please request a copy
    from the author of this logic and flow document.

We have received "Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421
(August 3 2022).xlsx". It does not appear to correspond to the matrix printed
on page 9. The two differ in structure:

  Page 9 matrix
    Rows    : KEY ON ENGINE ON / KEY ON ENGINE OFF (ACC or RUN) /
              KEY OFF (No ACC position) / KEY OFF (ACC position available)
    Columns : ICS Hard Controls / HVAC Knobs / Climate GUI / Headunit,
              each split by HEADUNIT POWER OFF and HEADUNIT POWER ON
    Cells   : whether the item is available in that power state

  Excel "State Matrix" sheet
    Blocks  : Key-on / Key-off / Key On, Gear <> Reverse
    Rows    : events (ON/OFF button Pressed, Door opened, Incoming Call,
              Plug in Projection, VR button long press, Call Ended,
              SRT or Off Road+ Hard Button press, Screen Off Button Pressed,
              Mute Button Pressed, HVAC Hard Control Adjustment, ...)
    Columns : context conditions (Turn Off @ door opening Enabled/Disabled,
              HU on / HU off / Power Button OFF, Call Active/Not Active,
              Door Open/Closed)
    Cells   : the resulting state after the event

We searched all 362 non-empty cells of the Excel file for the terms used on
page 9. The following return zero matches:

    HEADUNIT POWER, ICS Hard Controls, HVAC Knobs, Climate GUI,
    ENGINE ON, ENGINE OFF, Power Button only is functional,
    Fully functional, Power Accessory Delay, accessory delay,
    FOTA, Charge Now, stay awake

No cell in the Excel file describes the availability of ICS Hard Controls,
HVAC Knobs or Climate GUI in a given power state.

The page 9 matrix is also absent from the SYS1 structured export of this
document, so we have it only as a rendered image.

Three questions:

  (1) Is there a separate document that contains the page 9 capability matrix,
      and if so may we have a copy?

  (2) If not, is the page 9 matrix itself the authoritative source for that
      content, with the DCR21421 Excel covering a different subject
      (event-driven power state transitions)?

  (3) Please confirm one reading of the page 9 layout. The text "HVAC Knobs:
      Fully functional. Pop-ups still shown." appears twice, in the
      KEY ON ENGINE ON row and in the KEY ON ENGINE OFF (ACC or RUN) row. From
      the horizontal positions we read both as sitting in the HEADUNIT POWER
      OFF column, alongside "Climate GUI: Not Visibile due to power off". Is
      that correct?

Until (1) and (2) are clarified we have suspended test case authoring for
section 9 (Power Moding), which covers 5 requirements
(SWE1-HMI-PM-018-01 through -05).

One observation offered for information only: the change log in the DCR21421
Excel ends at 2021-10-20, which is earlier than the August 3 2022 date on its
own title sheet.

Thank you,
```

---

### 3.2 DR-PMH6 —— PITA6 與矩陣之衝突，及三項無需求之行為

```text
Subject: Power Moding HMI — PITA6 vs the state matrix, and three behaviours that have no requirement

Hello,

Two related items from our SWE.6 test case work on Power Moding HMI. We would
rather ask than choose.

--- 1. PITA6 and the state matrix appear to conflict for the reverse camera case

The logic and flow document states, verbatim:

    PITA6: HVAC pop-ups shall be temporarily displayed during Power Button Off
    state.

This is written without exception.

The Power Moding State Matrix ("State Matrix" sheet, block "Key On, Gear =
Reverse", row "HVAC Hard Control Adjustment", column "Power Button State =
OFF") states verbatim:

    Popup not displayed over RVC

Where the vehicle is in reverse and the reverse camera is being shown, these
two cannot both hold.

We considered reading PITA6 as a general rule with the reverse camera as an
exception, on the basis of PITA4. However PITA4 reads, verbatim:

    PITA4: Screen Off and HU Power button selections shall be ignored while
    backup cam is being shown.

PITA4 concerns user key inputs being ignored, not the display of pop-ups, so we
do not think it establishes an exception for PITA6, and we have not assumed one.

  Q1: Should PITA6 be read as conditional, excluding the case where the reverse
      camera is being shown? If so, could the wording be updated?

--- 2. Three behaviours appear only in the state matrix

The following cells describe pop-up behaviour that has no corresponding
statement in the logic and flow document, and therefore no requirement in the
SWE.1 analysis report:

  (a) Key-on block, row "ON/OFF button Pressed", Call Active:
      "VP Stays ON Pop-up: Cannot Power Off System during active phone call."

  (b) Key-on block, row "Key-off", Call Active, R1High:
      "VP display pop-up: 'Power OFF System. Continue call on mobile phone?
      Yes or NO'"

  (c) "Key On, Gear <> Reverse" block, row "HVAC Hard Control Adjustment":
      "Show Pop-Up ..."

  Q2: Should these be added as requirements? At present no test case will cover
      them, because we do not author test cases for behaviour that has no
      requirement of its own.

In the meantime we are writing the PITA6 test case with a pre-condition that
the reverse camera is not being shown, and recording the reverse camera case
and the three behaviours above as coverage gaps.

Thank you,
```

---

### 3.3 DR-PMH7 —— 素材中三處未定義之記法

```text
Subject: Power Moding HMI State Matrix — three notations we cannot resolve

Hello,

Three items in "Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421
(August 3 2022).xlsx" that we are unable to interpret from the documents we
hold. The matrix is normative for us (page 10 of the logic and flow document
states that Power Moding behavior "shall not be developed without following"
it), so we would rather ask than guess.

  Q1: What does "VP" stand for?

      The abbreviation appears in 30 cells of the State Matrix, for example:
          "VP Stays ON" / "VP Turns OFF"
          "VP display pop-up: 'Power OFF System. Continue call on mobile
           phone? Yes or NO'"
          "If Radio Off Delay = 0 minutes then VP turns OFF Else VP stays ON"

      From these we can tell that VP is something that can be on or off and
      that can display pop-ups, but the term does not appear anywhere in the
      logic and flow document (zero matches across all 11 pages) and is not
      defined in any material we hold. Is VP the head unit display?

  Q2: In the rows "Headunit Mode Button Pressed" and "Headunit Mode Change via
      VR", several cells read:

          "Else: Mute Active"

      Does this mean the mute state is left unchanged, or that mute becomes
      active as a result of the event? The matrix uses an arrow notation
      elsewhere (for example "Mute --> Active") but the convention is not
      stated, so we cannot tell which reading applies here.

  Q3: The logic and flow document contains the note, verbatim:

          Note: do not show popup again if popup was shown at Radio Off.

      Which pop-up does this refer to, and over what scope does it apply
      (a single ignition cycle, until the next Radio Off, or otherwise)?

None of these three blocks our current work. Q1 and Q2 affect how we classify
four rows of the matrix against the requirements; Q3 affects one test case.

Thank you,
```

---

## 四、對 28 包之影響

| 28 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §七 待 Pei 第 1、2 項 | 待裁 | **已裁** —— DR 發出（R-PMH106）、二條核可（R-PMH105） |
| §四 全部步驟 | 待做 | **不受影響，照原文執行** |
| §五 停止條件 9（本包新增任何檢查即停） | 生效 | **維持** —— apparatus 凍結自 R-PMH105 起正式生效 |

### 4.1 增列之作業步驟

7. **三份 DR 全文之落檔（R-PMH106）** —— 寫入 `DATA_REQUESTS.md`
   或於其中指向 28a §三；三者狀態維持 `DRAFT`、`SENT` 欄留空。
   **`DR-PMH5` 須確認其內容不含 21a 所載之「p9 與 `SU3.)` 相衝」一項**
   （已於 24 包改判 `未對照`，R-PMH106 明令）。

---

## 五、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH105 | R-PMH103／R-PMH104 核可生效；覆核線結束、apparatus 凍結、batch 2 開批 | ✅ |
| R-PMH106 | 三筆 DR 之發出授權；已撤回之主張不得寄出 | ✅ |

二條各管一事。**本檔未新增任何檢查程式或檢查項**（符合 R-PMH104）。

**待 Pei 者一項**：發出後告知**實際日期與對象**，以便狀態由 `DRAFT` 改 `SENT`。
