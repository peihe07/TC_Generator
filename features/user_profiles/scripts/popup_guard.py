#!/usr/bin/env python3
"""X-1 之十六條修正（41 包 §三）—— **集中一處，不散在四支生成器裡**。

## 為什麼不逐條改在各生成器內

十六條散在 `gen_pilot`／`gen_batch01`／`gen_batch03`／`gen_batch04` 四支。
逐條手改，等於**做十六次同一件事而沒有任何一處記得它們是同一件事** ——
下一批若再寫出同形態，改的人不會知道前面有十五個先例。

本檔把「這條 TC 之 procedure 切換了 profile，而 5.3.1 之 welcome popup
（PU0580）會出現」這件事變成**一張表**：新條目加一列，
`audit_consistency` 之 X-1 掃描仍是唯一的裁判 —— **本檔不關閉任何掃描**，
它只提供該掃描所要求的兩件事之一（pre-condition 之隔離，或 ER 之具名）。

## 兩種處置，逐條具名（41 包 §三之要求）

| kind | 意思 | 適用 |
|---|---|---|
| `off` | pre-condition 加「Welcome popup 設定為關閉」 | 該 popup 是**干擾**：本條之驗證目標與它無關 |
| `named` | remarks 具名該 popup **即本條 ER 所斷言者** | 該 popup 是**標的**：關掉它本條就沒東西可驗 |

**為什麼 `named` 不把 PU id 寫進 ER**：ER 之 PU id 須溯得到**被引之節**
（G18）。`PU0580` 定義於 5.3.1，而這些條引的是 7.2.1／4.x ——
把 id 寫進 ER 會逼引用欄併列 5.3.1，**引用欄遂變成導覽紀錄**
（同 `UI_LOCATORS` 當初的取捨）。故寫在 remarks：
X-1 之判準本就同時看 procedure／ER／remarks 三欄。
"""

# req_id → (kind, scope, 逐條理由)
GUARDS = {
    # ── kind='off' —— popup 為干擾 ────────────────────────────────────
    "SWE1-HMI-PROF-001-01": ("off", "both",
        "本條驗偏好之逐 profile 儲存與回復；welcome popup 與該斷言無關，"
        "但步驟 4 之連續兩次切換會各彈一次，遮住步驟 5 之讀值"),
    "SWE1-HMI-PROF-001-02": ("off", "both",
        "同上 —— 本條驗回復，popup 只會遮住步驟 3 之讀值"),
    "SWE1-HMI-PROF-001-03": ("off", "both",
        "本條驗不可用項之略過，其判定在選項清單而非 popup"),
    "SWE1-HMI-PROF-002-01": ("off", "both",
        "本條驗回復預設之範圍（只及現用 profile）；步驟 4 之切換會彈 popup"),
    "SWE1-HMI-PROF-004-02": ("off", "both",
        "本條驗自畫面選取 profile 後之偏好回復 —— **切換正是本條之動作**，"
        "故 popup 必然出現；但所驗者為偏好值，非 popup"),
    "SWE1-HMI-PROF-004-03": ("off", "both",
        "同上，觸發途徑為記憶座椅鍵"),
    "SWE1-HMI-PROF-004-04": ("off", "both",
        "同上，觸發途徑為 key fob"),
    "SWE1-HMI-PROF-005": ("off", "both",
        "本條驗「載入前先存」之順序；popup 出現在載入之後，"
        "**若不關閉，步驟 2 之讀值須先關掉 popup 才做得到**"),
    "SWE1-HMI-PROF-006-01": ("off", "both",
        "本條驗 key cycle 起始所載入之 profile；"
        "key-on 之 welcome popup（7.1）與切換之 popup（5.3.1）皆會出現"),
    "SWE1-HMI-PROF-013": ("off", "both",
        "本條驗狀態列按鈕之圖示隨現用 profile 改變；popup 會遮住狀態列"),
    "SWE1-HMI-PROF-018-02": ("off", "both",
        "本條驗分頁之 latch；步驟 4 之切換會彈 popup 而遮住分頁"),
    "SWE1-HMI-PROF-032": ("off", "active",
        "本條驗未按記憶座椅鍵亦存得下位置；只涉一個 profile，"
        "但步驟 1 之啟用與步驟 4 之 key cycle 各會彈一次"),
    "SWE1-HMI-PROF-112-01": ("off", "both",
        "本條驗 app 刪除之逐 profile 範圍；判定在 app tray"),
    "SWE1-HMI-PROF-112-02": ("off", "both",
        "本條驗 app 更新之跨 profile 生效；判定在版本號"),
    "SWE1-HMI-PROF-112-03": ("off", "both",
        "本條驗 app 安裝之逐 profile 範圍；判定在 app tray"),

    # ── kind='named' —— popup 即標的，或 pre-condition 已明定其開啟 ────
    #
    # **這四條不在 41 包所點名之十六條內**：它們自 35 輪起就在 X-1 之待判清單裡，
    # 而其 pre-condition **早已明定「B 之 welcome popup 為開啟」** ——
    # 即該 popup 是**被看見並被決定的**，不是被忽略的。
    # X-1 看不到，是因為判準只認 `PU0580` 這個字串而不認那句中文前提。
    # 本輪一併具名，使該類清空 —— **不改 X-1 之判準，改記載**。
    "SWE1-HMI-PROF-022": ("named", None,
        "pre-condition 已明定「B 之 welcome popup 為開啟」——"
        "**該 popup 為本條所預期之中間狀態**：條文（5.3.1）給它 5 秒，"
        "且 7.4 定其於使用者互動時即清除，故步驟 3 之讀取在其之後；"
        "ER3 所斷言之 highlight 與分頁狀態在 popup 之下方，不因其顯示而改變"),
    "SWE1-HMI-PROF-024": ("named", None,
        "同 `SWE1-HMI-PROF-022` —— pre-condition 已明定其開啟；"
        "ER2 斷言之「分頁仍為 All Profiles」是 popup **下方**之畫面狀態"),
    "SWE1-HMI-PROF-025": ("named", None,
        "同上；本條步驟 2 之「載入中再選」發生在 popup 出現**之前**"
        "（5.3.1 之順序為載入訊息 → welcome popup），故不受其遮蔽"),
    "SWE1-HMI-PROF-059-03": ("named", None,
        "本條之 ER3 所斷言者**就是**該 welcome popup（`the applicable "
        "welcome popup for it is displayed`）—— 標的而非干擾"),
    "SWE1-HMI-PROF-059-01": ("named", None,
        "本條之 ER1 所斷言者**就是**該 welcome popup（7.2.1 之大版）。"
        "5.3.1 之 PU0580 為「切換後之 welcome popup」，"
        "與本條步驟 1 啟用 A 後所顯示者為同一個 popup 之同一次顯示 ——"
        "**關掉它本條就沒有東西可驗**"),
}

PRE_OFF = {
    "both": "The Welcome popup setting is off for both Driver Profiles",
    "active": "The Welcome popup setting is off for the active Driver Profile",
}

NOTE_OFF = (
    "**X-1（切換 profile 觸發 5.3.1 之 PU0580）**：{why}。"
    "故 pre-condition 指定 Welcome popup 設定為關閉 ——"
    "該設定之關閉途徑見 6.3.2（`SWE1-HMI-PROF-051`），"
    "**為合法之車輛狀態，非測試用旁路**。")
NOTE_NAMED = (
    "**X-1（切換 profile 觸發 5.3.1 之 PU0580）**：{why}。")


def _renumber(block: str) -> str:
    lines = [x for x in str(block).splitlines() if x.strip()]
    body = [l.split(". ", 1)[1] if ". " in l[:4] else l for l in lines]
    return "\n".join(f"{i}. {t}" for i, t in enumerate(body, 1))


def apply(rec: dict) -> bool:
    """對一個 `_rec()` 產物就地施加處置。回傳是否命中。"""
    g = GUARDS.get(rec["parent"]) or GUARDS.get(rec["tcs"][0]["req_id"])
    if not g:
        return False
    kind, scope, why = g
    tc = rec["tcs"][0]
    if kind == "off":
        tc["pre_conditions"] = _renumber(
            tc["pre_conditions"] + "\n0. " + PRE_OFF[scope])
        note = NOTE_OFF.format(why=why)
    else:
        note = NOTE_NAMED.format(why=why)
    tc["remarks"] = (tc["remarks"] + note) if tc["remarks"] else note
    return True
