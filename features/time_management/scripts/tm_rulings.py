#!/usr/bin/env python3
"""本 feature 之裁決常數 —— **context 層與 lint 層之單一來源**。

modified by TC_Generator analysis round 06 under G-TM1 更正 / R-TM33

## 為何存在

`06` §4.2 要求：C-1（五條界線）與 C-2（A-TM13 缺口）之內容須與 lint 層之
`BOUNDARY_SIGNALS`、`lint_spec_gap` **取自同一來源**，不得各寫一份。

理由逐字：「兩份會漂移，且漂移時 lint 全綠（context 說 A、lint 驗 B，
生成照 A 寫則被 B 攔，看起來像模型出錯）」。

**該失效形態與本 feature 一路在防者同族**：兩處各自看都對，合起來才錯，
且錯誤呈現為「模型出錯」而非「規則不一致」—— 最難歸因的一種。

## 誰讀它

  build_batch_context.py   C-1 / C-2 / C-6 之內容來源（給生成看）
  lint_tcs.py              B3 / B4 之判準來源（驗生成）

**任一方增修本檔之常數，另一方自動同步。** 本檔不含邏輯，只含裁決值。

## 每一項之依據

值皆取自已裁定之條文與**已複驗之實測**，非本檔自行決定：
  TEST_SET_OF        framework Part VII Layer 2，R-TM17 簽核
  SPEC_GAP           A-TM13；物件 id 經 `01R` 全檔搜尋確認零命中
  BOUNDARY_SIGNALS   R-TM23 + R-TM25；訊號名與物件 id 經 `04` T3 複驗
                     （九 token 全命中、六物件章節歸屬全符）
  BATCHES            framework Part VII Batch plan，`03` §3
"""
from __future__ import annotations

# ── framework Part VII Layer 2（R-TM17 簽核）────────────────────
TEST_SET_OF = {
    "001": "Manual Setting",   "015": "Manual Setting",
    "002": "GPS Sync",         "003": "GPS Sync",
    "004": "GPS Sync",         "014": "GPS Sync",
    "005": "Master Clock",     "006": "Master Clock",
    "016": "Master Clock",     "018": "Master Clock",
    "021": "Master Clock",
    "008": "CAN Transmission", "009": "CAN Transmission",
    "017": "CAN Transmission", "020": "CAN Transmission",
    "007": "Display",          "011": "Display",
    "019": "Display",
    "012": "Zone and DST",     "013": "Zone and DST",
    "010": "Fault Handling",   "022": "Fault Handling",
}
TEST_SETS = set(TEST_SET_OF.values())

# ── framework Part VII Batch plan（`03` §3）────────────────────
# B1 七片各屬一組，故 pilot 一次檢驗全部七組之形態 —— 本 feature 無
# done region，pilot 是唯一人工閘門（canon §1.2 分層取樣）。
BATCHES = {
    "B1": ["001", "003", "006", "007", "008", "010", "012"],
    "B2": ["002", "004", "005", "014", "016", "018", "021"],
    "B3": ["009", "011", "017", "019", "020"],
    "B4": ["013", "015", "022"],
}

# ── A-TM13（R-TM41 處置訂正 + canon §8.4.3）────────────────────
# 兩片之受影響條目不得留空、不得填偽值，改填 PENDING: DR-5。
SPEC_GAP_DR = 5
SPEC_GAP = {
    "005": {"sys_ra": "SYS-RA-TIME&DATE-221", "object": "6151328",
            "note": "GPS_Presence=[Absent] 時之內部時鐘精度"},
    "002": {"sys_ra": "SYS-RA-TIME&DATE-224", "object": "6151331",
            "note": "GPS_Presence=[Present] 時之個人化設定"},
}
SPEC_GAP_LEAVES = {f"SWE-RA-TIME&DATE-{n}" for n in SPEC_GAP}


def spec_gap_placeholder(nums) -> str:
    """`PENDING: DR-5 …` 之字串產生器 —— context 與 lint 共用同一形式。"""
    return (f"PENDING: DR-{SPEC_GAP_DR} CFTS015 缺件物件 "
            + " / ".join(sorted(nums)))


# ── R-TM23 + R-TM25：五條 §8.2.1 界線 ──────────────────────────
# owns / not_ours 之訊號名與物件 id 取自 `04` T3 之複驗結果。
# lint 層以 not_ours 做**偵測**（TC 內文命中即報 boundary）；
# context 層以 owns + why 做**指示**（告訴生成端該片管什麼、不管什麼）。
BOUNDARY_SIGNALS = {
    "SWE-RA-TIME&DATE-011": {
        "owns": ["$DateTmFormat$"],
        "not_ours": ["$DateTmHour$", "$DateTmMinute$", "$DateTmSecond$"],
        "objects": ["4813974"],
        "why": "011 擁有格式跨喚醒週期之保存與重送（物件 4813974，"
               "1.3.1.1.5.1）；時間值之送出時機屬 008",
    },
    "SWE-RA-TIME&DATE-008": {
        "owns": ["$DateTmHour$", "$DateTmMinute$", "$DateTmSecond$"],
        "not_ours": ["$DateTmFormat$", "$GPSDateTm"],
        "objects": ["4813953", "4813960"],
        "why": "008 擁有主時間訊號之送出時機與觸發（1.3.1.1.4）；"
               "格式屬 011、GPS 來源值屬 014",
    },
    "SWE-RA-TIME&DATE-014": {
        "owns": ["$GPSDateTm"],
        "not_ours": ["$DateTmHour$", "$DateTmMinute$", "$DateTmSecond$"],
        "objects": ["4813999", "4814098"],
        "why": "014 擁有 GPS 來源值送出之正確性（1.3.1.1.3 / 1.5.2.5）；"
               "送出時機與通道屬 008/017",
    },
}

# 另兩條界線無訊號層之歸屬（其區辨在觸發源與規則歸屬），故不列於
# BOUNDARY_SIGNALS 而以敘述給 context。lint 層對其無自動判準。
BOUNDARY_NOTES = {
    "SWE-RA-TIME&DATE-004": "004 管 GPS **來源**不可用時改用內部時鐘；"
                            "010 管**收到之時間訊號**無效時用最後有效值。"
                            "觸發源不同，不得互相涵蓋。",
    "SWE-RA-TIME&DATE-010": "010 管收到之時間訊號無效／遺失；"
                            "GPS 來源可用性屬 004。",
    "SWE-RA-TIME&DATE-022": "SNA／預設值之送出規則屬 022。014 之描述含 "
                            "`or SNA if unavailable`，但該規則歸此片。",
    "SWE-RA-TIME&DATE-018": "018 管 reset／斷電後之時間日期預設值；"
                            "011 管格式跨喚醒週期之保存。兩者皆涉「重開之後」。",
}

# ── canon §8.7.5 / R-TM49 / R-TM51：訊號三件組 ─────────────────
SEGMENT_DR = 6
SEGMENT_PLACEHOLDER = (f"PENDING: DR-{SEGMENT_DR} CAN 網段依據"
                       "（無 DBC／架構文件）")

# ── canon §4.3.1：test_item 兩段式 ────────────────────────────
TEST_ITEM_TOKEN_MAX = 50

# ── R-TM8 / R-TM40 ───────────────────────────────────────────
TEST_GROUP = "Time and Date"
SPEC_REF_PREFIX = "CFTS015"
