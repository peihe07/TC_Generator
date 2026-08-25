# 下放包 21a —— DR-PMH5／6 之發出授權與可寄出全文（與 21 同一往返，須併讀）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [21_predicate_criterion.md](21_predicate_criterion.md)
  同屬第 21 輪，上繳仍為 `docs/upstream/21_predicate_criterion.md`
- 21 本文未改一字

---

## 一、Pei 之裁定（2026-08-25，逐字）

> 「`DR-PMH5` 仍是 ch 9 開批的唯一阻斷；`DR-PMH6` 新開但不阻斷 都照你的建議 開」

即：**二者皆依分析層所擬之內容發出。**

**須先講明其不改變者**：發出**不等於**結案。`DR-PMH5` 之阻斷
（ch 9 不得開批）**於上游答覆前維持** —— 本裁定使其由「已登記未發出」
變為「已發出待覆」，不使其解除。

---

## 二、裁決條文（抄入 `RULINGS.md`）

```
R-PMH82（DR 之狀態機）
DR 之狀態分四級，`DATA_REQUESTS.md` 之狀態欄只得取其一：

  `DRAFT`      —— 已登記於本 repo，**尚未發出**。
  `SENT`       —— 已發出。**須同時記載：發出日期、發出對象、發出管道**。
                 三者缺一即不得標 `SENT`。
  `ANSWERED`   —— 已獲上游答覆。須記答覆日期與其逐字內容之出處。
  `CLOSED`     —— 已結案。須記其結案依據（`ANSWERED` 之內容，
                 或 Pei 之裁定條號）。

**未記載發出日期與對象者，一律為 `DRAFT`，不得稱「已發」。**

本條之必要性：`DR-PMH1`～`4` 自 2026-08-24 開立起，經執行層於六個往返
連續重申而其狀態欄始終為 `OPEN` —— **該欄無法分辨「登記了」與「發出了」**，
致「尚未發出」這件事沒有任何欄位承載它。

**回溯適用**：`DR-PMH1`～`4` 已由 Pei 之裁定結清，其狀態改為
`CLOSED`（依 R-PMH72／73／74／75），**其歷程中從未 `SENT`，此事實須記明**。
```

```
R-PMH83（DR-PMH5／DR-PMH6 之發出授權）
Pei 於 2026-08-25 授權發出 `DR-PMH5` 與 `DR-PMH6`，其內容依 21a §三之全文。

發出後二者之狀態改為 `SENT`，並記其發出日期與對象；
**執行層不得代為發出** —— 對外發文為 Pei 之行為，
執行層只更新狀態欄且須以 Pei 告知之實際日期為準，
**不得以「下放包之日期」充當發出日期**（R-PMH43：已發生變更之陳述須有證據）。

**阻斷不變**：`DR-PMH5` 於 `ANSWERED` 前，ch 9（`Power Transitions` 組，
5 leaf）**維持不得開批**。`DR-PMH6` 不阻斷 —— `Power Off Behavior` 組
已由 R-PMH80 以限縮 ＋ 揭露解除。
```

---

## 三、兩份可直接寄出之全文

> 收件對象為規格文件所載之 HMI Lead（PDF p1：`HMI Lead: Paolo Visconti`）
> 或其現任接手人。**以英文撰寫**，其依據為規格與素材皆為英文。
> **凡引規格與素材處皆為逐字**，未加任何推論。

---

### 3.1 DR-PMH5

```text
Subject: Power Moding HMI — request for the source of the capability matrix on page 9

Hello,

We are preparing the SWE.6 test cases for Power Moding HMI
(FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1, based on
"Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023)").

Page 10 of the logic and flow document states, verbatim:

    POWER MODING STATE MATRIX: Power Moding behavior shall not be developed
    without following the Power Moding State Matrix, which is in a separate
    Excel document. If this document is not available, please request a copy
    from the author of this logic and flow document.

We have received a file named "Power Moding HMI State Matrix R1 SR24 Post 2A
DCR21421 (August 3 2022).xlsx". However, it does not appear to correspond to
the matrix printed on page 9 of the logic and flow document. The two differ in
structure:

  Page 9 matrix
    Rows    : KEY ON ENGINE ON / KEY OFF (ACC) / KEY OFF (No ACC)
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

We searched the Excel file for the terms used on page 9. The following strings
return zero matches across all 362 non-empty cells:

    HEADUNIT POWER, ICS Hard Controls, HVAC Knobs, Climate GUI,
    ENGINE ON, ENGINE OFF, Power Button only is functional,
    Fully functional, Power Accessory Delay, accessory delay,
    FOTA, Charge Now, stay awake

No cell in the Excel file describes the availability of ICS Hard Controls,
HVAC Knobs or Climate GUI in a given power state.

We also note that the page 9 matrix is absent from the SYS1 structured export
of this document, so it is not available to us in any machine-readable form.

Could you please clarify one of the following:

  (1) Is there a separate document that contains the page 9 capability matrix,
      and if so may we have a copy; or

  (2) Is the page 9 matrix itself the authoritative source for that content,
      with the DCR21421 Excel covering a different subject (event-driven power
      state transitions)?

Until this is clarified we have suspended test case authoring for section 9
(Power Moding), which covers 5 requirements (SWE1-HMI-PM-018-01 through -05).

One further observation, offered for your information only: the change log in
the DCR21421 Excel ends at 2021-10-20, which is earlier than the August 3 2022
date given on its own title sheet.

Thank you,
```

---

### 3.2 DR-PMH6

```text
Subject: Power Moding HMI — PITA6 and the state matrix appear to conflict for the reverse camera case

Hello,

While preparing the SWE.6 test cases for Power Moding HMI we found what appears
to be a conflict between the logic and flow document and the Power Moding State
Matrix. We would rather ask than choose one of them.

The logic and flow document, section "Additional Power Moding Behavior Notes",
states verbatim:

    PITA6: HVAC pop-ups shall be temporarily displayed during Power Button Off
    state.

This is written without exception.

The Power Moding State Matrix ("State Matrix" sheet, block "Key On, Gear =
Reverse", row "HVAC Hard Control Adjustment", column "Power Button State = OFF")
states verbatim:

    Popup not displayed over RVC

For the case where the vehicle is in reverse and the reverse camera is being
shown, these two cannot both hold: PITA6 says the HVAC pop-up is displayed
during Power Button Off state, and the matrix says it is not displayed over the
reverse camera view.

We considered reading PITA6 as a general rule with the reverse camera as an
exception, on the basis of PITA4. However PITA4 reads, verbatim:

    PITA4: Screen Off and HU Power button selections shall be ignored while
    backup cam is being shown.

PITA4 concerns user key inputs being ignored, not the display of pop-ups, so we
do not think it establishes an exception for PITA6. We have therefore not made
that assumption.

Two questions:

  (1) Should PITA6 be read as conditional, i.e. excluding the case where the
      reverse camera is being shown? If so, could the wording be updated
      accordingly?

  (2) The behaviour "Popup not displayed over RVC" appears only in the state
      matrix and not in the logic and flow document, and consequently has no
      corresponding requirement in the SWE.1 analysis report. Should it be
      added as a requirement? At present no test case will cover it, because we
      do not author test cases for behaviour that has no requirement of its own.

In the meantime we are writing the PITA6 test case with a pre-condition that
the reverse camera is not being shown, and recording the reverse camera case as
a coverage gap.

Thank you,
```

---

## 四、對 21 包之影響

| 21 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §六 步驟 4（`DR-PMH6` 之開立） | 開立即可 | **開立 ＋ 依 R-PMH82 標 `DRAFT`**；Pei 實際發出後方改 `SENT` 並記日期與對象 |
| §八 第 9 項（未結 DR 清單） | 「現應為 2 筆」 | 維持 2 筆，惟其狀態欄依 R-PMH82 之四級書寫 |
| §九 待 Pei 第 1、2 項 | `DR-PMH5`／`DR-PMH6` 之發出 | **已授權**（R-PMH83）；改為「待上游答覆」 |
| 其餘 | | 不受影響 |

### 4.1 增列之作業步驟

8. **`DATA_REQUESTS.md` 之狀態欄改制（R-PMH82）** ——
   全表改用四級狀態；`DR-PMH1`～`4` 標 `CLOSED` 並各記其結案之裁決條號，
   **且須記明其歷程中從未 `SENT`**；`DR-PMH5`／`DR-PMH6` 標 `DRAFT`，
   並附 21a §三之可寄出全文（或指向本檔）。

9. **發出日期之留空** —— `SENT` 欄位留白，
   **待 Pei 告知實際發出日期與對象後方填**。
   **不得以本包之日期充當**（R-PMH83）。

---

## 五、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH82 | DR 之四級狀態機；未記發出日期與對象者不得稱「已發」 | ✅ |
| R-PMH83 | `DR-PMH5`／`DR-PMH6` 之發出授權；執行層不得代為發出 | ✅ |

二條各管一事。

**待 Pei 者**：發出後告知其**實際日期與對象**，以便執行層將狀態由
`DRAFT` 改為 `SENT`（R-PMH83 明訂不得以下放包之日期充當）。
