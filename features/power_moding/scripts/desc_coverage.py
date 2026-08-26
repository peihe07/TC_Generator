#!/usr/bin/env python3
"""`desc_coverage.py` —— DESC 逐斷言涵蓋表之程式化承載（R-PMH138，36 包步驟 3）。

**其為 apparatus 之第二次解凍所產出，用畢即恢復凍結。**

**四項要求**（R-PMH138）：
  (a) 自 037（經 `layer3_sections.tsv` 之 `requirement_description` 欄）讀 DESC，
      依 R-PMH101 切分（**機器候選 ＋ 人讀複核**）；
  (b) **正向** —— 每一 leaf 之每一斷言 × 其 TC 集合之涵蓋，未涵蓋者標 `未涵蓋`，
      並依 **R-PMH137** 區分「重複於他 leaf」者；
  (c) **反向**（R-PMH136）—— TC 之每一 ER 斷言須有其 leaf 之 DESC 依據，
      無者標 `無依據`（其為 canon §8.4.1 之造值或 §8.4.2 之範圍捏造）；
  (d) **must-hit** 二項，見 `--must-hit`。

**本檔之判定為人讀之結果，其存於 `FORWARD`／`REVERSE` 二常數；
程式所驗者為「其存在、其可解析、其所指之 ER 確實存在」，不驗其正確。**
"""

# R-PMH92 —— must-hit 之註冊
HAS_MUST_HIT = True
MUST_HIT_NOTE = ("`--must-hit` 兩項：刪去 `-016` 之 ER4 → 正向須報 `未涵蓋`；"
                 "於 `-035` 增一條 DESC 所無之 ER → 反向須報 `無依據`")

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# R-PMH101 之切分：機器候選（句末標點 ＋ 大寫起首）
SPLIT = re.compile(r"(?<=[.;])\s+(?=[A-Z(])")

# **人讀複核之覆寫** —— 機器候選與人讀不同者列於此。現為空：
# 55 個候選全數經人讀確認（36 包步驟 3），**其空值為複核之結果，非未做**。
SPLIT_REVIEW: dict[str, list[str]] = {}

LIMITS = [
    "**切分仍以句末標點為候選** —— 一句內含二斷言者（如 `-009-01` 之三個後果）計為一項；"
    "其是否應再切屬人讀，本檔只承載其結果",
    "**`FORWARD`／`REVERSE` 之值為人讀所寫** —— 本檔驗其存在與可解析，**不驗其正確**",
    "**反向之 `測試執行` 類不需 DESC 依據**（R-PMH97 之二分）—— 其為測試員之行為或資料蒐集；"
    "**該分類本身為人讀，錯分即漏檢**",
    "**未涵蓋-重複 之認定依 R-PMH137** —— 其行為由他 leaf 之 TC 涵蓋；"
    "**本檔不驗該他 leaf 之 TC 是否真涵蓋它**",
]

FORWARD = {
    "SWE1-HMI-PM-026-01|1": [
        "049|3",
        ""
    ],
    "SWE1-HMI-PM-026-02|1": [
        "050|2",
        ""
    ],
    "SWE1-HMI-PM-026-03|1": [
        "051|2",
        ""
    ],
    "SWE1-HMI-PM-026-04|1": [
        "052|2",
        ""
    ],
    "SWE1-HMI-PM-026-05|1": [
        "053|2",
        ""
    ],
    "SWE1-HMI-PM-001-01|1": [
        "未涵蓋-重複",
        "`-028` ER1（掛 `SWE1-HMI-PM-006-01`）—— R-PMH137"
    ],
    "SWE1-HMI-PM-001-01|2": [
        "025|2",
        ""
    ],
    "SWE1-HMI-PM-001-02|1": [
        "026|3",
        ""
    ],
    "SWE1-HMI-PM-001-03|1": [
        "001|1",
        ""
    ],
    "SWE1-HMI-PM-001-03|2": [
        "001|3",
        ""
    ],
    "SWE1-HMI-PM-001-04|1": [
        "002|2",
        ""
    ],
    "SWE1-HMI-PM-001-05|1": [
        "004|2",
        ""
    ],
    "SWE1-HMI-PM-003|1": [
        "005|1",
        ""
    ],
    "SWE1-HMI-PM-003|2": [
        "未涵蓋-重複",
        "`-004` ER2（掛 `SWE1-HMI-PM-001-05`）—— R-PMH137"
    ],
    "SWE1-HMI-PM-004|1": [
        "006|2",
        ""
    ],
    "SWE1-HMI-PM-005|1": [
        "007|4",
        ""
    ],
    "SWE1-HMI-PM-005|2": [
        "007|3",
        ""
    ],
    "SWE1-HMI-PM-006-01|1": [
        "028|3",
        ""
    ],
    "SWE1-HMI-PM-006-02|1": [
        "029|3",
        ""
    ],
    "SWE1-HMI-PM-006-03|1": [
        "030|3",
        ""
    ],
    "SWE1-HMI-PM-007|1": [
        "031|1",
        ""
    ],
    "SWE1-HMI-PM-008-01|1": [
        "032|2",
        ""
    ],
    "SWE1-HMI-PM-008-02|1": [
        "033|1",
        ""
    ],
    "SWE1-HMI-PM-009-01|1": [
        "034|1",
        ""
    ],
    "SWE1-HMI-PM-009-02|1": [
        "035|2",
        ""
    ],
    "SWE1-HMI-PM-010|1": [
        "036|2",
        ""
    ],
    "SWE1-HMI-PM-010|2": [
        "037|2",
        ""
    ],
    "SWE1-HMI-PM-011|1": [
        "027|2",
        ""
    ],
    "SWE1-HMI-PM-012|1": [
        "009|3",
        ""
    ],
    "SWE1-HMI-PM-012|2": [
        "010|4",
        ""
    ],
    "SWE1-HMI-PM-012|3": [
        "未涵蓋-部分",
        "`-009` ER4 只涵蓋啟動音側；**告別音側未涵蓋（A-PMH23，`DR-PMH8` Q3）**"
    ],
    "SWE1-HMI-PM-013|1": [
        "011|2",
        ""
    ],
    "SWE1-HMI-PM-014|1": [
        "012|6",
        "（39 包 R-PMH147：ER6 擴及告別音側）"
    ],
    "SWE1-HMI-PM-015|1": [
        "013|6",
        "（39 包 R-PMH147：ER6 擴及告別音側）"
    ],
    "SWE1-HMI-PM-016|1": [
        "014|3",
        ""
    ],
    "SWE1-HMI-PM-017|1": [
        "015|5",
        ""
    ],
    "SWE1-HMI-PM-018-01|1": [
        "016|1",
        ""
    ],
    "SWE1-HMI-PM-018-01|2": [
        "016|4",
        ""
    ],
    "SWE1-HMI-PM-018-01|3": [
        "016|5",
        ""
    ],
    "SWE1-HMI-PM-018-02|1": [
        "017|2",
        ""
    ],
    "SWE1-HMI-PM-018-02|2": [
        "017|3",
        ""
    ],
    "SWE1-HMI-PM-018-03|1": [
        "018|3",
        ""
    ],
    "SWE1-HMI-PM-018-03|2": [
        "019|2",
        ""
    ],
    "SWE1-HMI-PM-018-04|1": [
        "021|2",
        ""
    ],
    "SWE1-HMI-PM-018-04|2": [
        "022|2",
        ""
    ],
    "SWE1-HMI-PM-018-05|1": [
        "023|3",
        ""
    ],
    "SWE1-HMI-PM-022-02|1": [
        "008|3",
        "**其例外 `unless certain phone call scenarios …` 未涵蓋 —— `DR-PMH8` Q8**"
    ],
    "SWE1-HMI-PM-019|1": [
        "038|3",
        ""
    ],
    "SWE1-HMI-PM-020|1": [
        "039|1",
        ""
    ],
    "SWE1-HMI-PM-020|2": [
        "039|2",
        ""
    ],
    "SWE1-HMI-PM-020|3": [
        "039|4",
        ""
    ],
    "SWE1-HMI-PM-021|1": [
        "040|1",
        ""
    ],
    "SWE1-HMI-PM-021|2": [
        "040|3",
        ""
    ],
    "SWE1-HMI-PM-022-01|1": [
        "041|2",
        ""
    ],
    "SWE1-HMI-PM-024-01|1": [
        "042|2",
        ""
    ],
    "SWE1-HMI-PM-024-02|1": [
        "043|2",
        ""
    ],
    "SWE1-HMI-PM-024-03|1": [
        "044|3",
        ""
    ],
    "SWE1-HMI-PM-025|1": [
        "045|3",
        ""
    ],
    "SWE1-HMI-PM-027|1": [
        "046|2",
        ""
    ],
    "SWE1-HMI-PM-029|1": [
        "047|4",
        ""
    ]
}

REVERSE = {
    "012|6": [
        "A1",
        "（39 包 R-PMH147 所擴之 ER）"
    ],
    "013|6": [
        "A1",
        "（39 包 R-PMH147 所擴之 ER）"
    ],
    "049|1": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "049|2": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "049|3": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "050|1": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "050|2": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "051|1": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "051|2": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "052|1": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "052|2": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "053|1": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "053|2": [
        "A1",
        "（batch 6：其 leaf 之 DESC 僅一斷言）"
    ],
    "001|1": [
        "A1",
        "其依據為 A1（`if the system is not ready, it displays \"Loading…\"`）"
    ],
    "001|2": [
        "A1",
        ""
    ],
    "001|3": [
        "A2",
        ""
    ],
    "002|1": [
        "A1",
        ""
    ],
    "002|2": [
        "A1",
        ""
    ],
    "003|1": [
        "A1",
        ""
    ],
    "003|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "003|3": [
        "A1",
        ""
    ],
    "003|4": [
        "A1",
        ""
    ],
    "004|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "004|2": [
        "A1",
        ""
    ],
    "004|3": [
        "例外-本體",
        "**R-PMH139：例外條款之依據取自本體 leaf** —— `-001-05` 之 DESC 只載「無逾時、須手動按 Accept」，**未載按下之後之結果**；`The last mode screen is displayed` 之依據在 `-001-04` 之 DESC（`press Accept to go directly to last mode screen`）。**37 包裁（乙）：依 R-PMH139 不計為 §8.4.2 之範圍捏造** —— 其本體 leaf 已於 `-004` 之 reasoning 具名。"
    ],
    "005|1": [
        "A1",
        ""
    ],
    "005|2": [
        "A1",
        ""
    ],
    "006|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "006|2": [
        "A1",
        ""
    ],
    "007|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "007|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "007|3": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "007|4": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "007|5": [
        "A2",
        ""
    ],
    "007|6": [
        "A2",
        ""
    ],
    "007|7": [
        "A2",
        ""
    ],
    "008|1": [
        "A1",
        ""
    ],
    "008|2": [
        "A1",
        "觸發之複述（`presses the power button to change to On state`）"
    ],
    "008|3": [
        "A1",
        ""
    ],
    "009|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "009|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "009|3": [
        "A1",
        ""
    ],
    "009|4": [
        "A3",
        ""
    ],
    "009|5": [
        "A1",
        ""
    ],
    "010|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "010|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "010|3": [
        "A2",
        ""
    ],
    "010|4": [
        "A2",
        ""
    ],
    "010|5": [
        "A2",
        ""
    ],
    "011|1": [
        "A1",
        ""
    ],
    "011|2": [
        "A1",
        ""
    ],
    "012|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "012|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "012|3": [
        "A1",
        ""
    ],
    "012|4": [
        "A1",
        ""
    ],
    "012|5": [
        "A1",
        ""
    ],
    "013|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "013|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "013|3": [
        "A1",
        ""
    ],
    "013|4": [
        "A1",
        ""
    ],
    "013|5": [
        "A1",
        ""
    ],
    "014|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "014|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "014|3": [
        "A1",
        ""
    ],
    "014|4": [
        "A1",
        ""
    ],
    "014|5": [
        "A1",
        ""
    ],
    "015|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "015|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "015|3": [
        "A1",
        ""
    ],
    "015|4": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "015|5": [
        "A1",
        ""
    ],
    "016|1": [
        "A1",
        ""
    ],
    "016|2": [
        "A2",
        ""
    ],
    "016|3": [
        "A1",
        ""
    ],
    "016|4": [
        "A2",
        ""
    ],
    "016|5": [
        "A3",
        ""
    ],
    "016|6": [
        "A1",
        ""
    ],
    "017|1": [
        "A1",
        ""
    ],
    "017|2": [
        "A1",
        ""
    ],
    "017|3": [
        "A2",
        ""
    ],
    "018|1": [
        "A1",
        ""
    ],
    "018|2": [
        "A1",
        ""
    ],
    "018|3": [
        "A1",
        ""
    ],
    "019|1": [
        "A2",
        ""
    ],
    "019|2": [
        "A1",
        ""
    ],
    "020|1": [
        "A1",
        ""
    ],
    "020|2": [
        "A1",
        ""
    ],
    "021|1": [
        "A1",
        ""
    ],
    "021|2": [
        "A1",
        ""
    ],
    "022|1": [
        "A1",
        ""
    ],
    "022|2": [
        "A1",
        ""
    ],
    "023|1": [
        "A1",
        ""
    ],
    "023|2": [
        "A1",
        ""
    ],
    "023|3": [
        "A1",
        ""
    ],
    "025|1": [
        "A2",
        ""
    ],
    "025|2": [
        "A2",
        ""
    ],
    "026|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "026|2": [
        "A1",
        ""
    ],
    "026|3": [
        "A1",
        ""
    ],
    "026|4": [
        "A1",
        ""
    ],
    "026|5": [
        "A1",
        ""
    ],
    "026|6": [
        "A1",
        ""
    ],
    "027|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "027|2": [
        "A1",
        ""
    ],
    "027|3": [
        "A1",
        ""
    ],
    "027|4": [
        "A1",
        ""
    ],
    "028|1": [
        "A1",
        ""
    ],
    "028|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "028|3": [
        "A1",
        ""
    ],
    "029|1": [
        "A1",
        ""
    ],
    "029|2": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "029|3": [
        "A1",
        ""
    ],
    "030|1": [
        "A1",
        ""
    ],
    "030|2": [
        "A1",
        ""
    ],
    "030|3": [
        "A1",
        ""
    ],
    "031|1": [
        "A1",
        ""
    ],
    "031|2": [
        "A1",
        ""
    ],
    "032|1": [
        "A1",
        ""
    ],
    "032|2": [
        "A1",
        ""
    ],
    "033|1": [
        "A1",
        ""
    ],
    "033|2": [
        "A1",
        ""
    ],
    "034|1": [
        "A1",
        ""
    ],
    "034|2": [
        "A1",
        ""
    ],
    "035|1": [
        "A1",
        "觸發之複述（`When the Power Button is pressed On`）"
    ],
    "035|2": [
        "A1",
        ""
    ],
    "036|1": [
        "A1",
        ""
    ],
    "036|2": [
        "A1",
        ""
    ],
    "037|1": [
        "A2",
        ""
    ],
    "037|2": [
        "A2",
        ""
    ],
    "038|1": [
        "A1",
        ""
    ],
    "038|2": [
        "A1",
        ""
    ],
    "038|3": [
        "A1",
        ""
    ],
    "039|1": [
        "A1",
        ""
    ],
    "039|2": [
        "A1",
        ""
    ],
    "039|3": [
        "A3",
        ""
    ],
    "039|4": [
        "A1",
        ""
    ],
    "040|1": [
        "A1",
        ""
    ],
    "040|2": [
        "A1",
        ""
    ],
    "040|3": [
        "A1",
        ""
    ],
    "041|1": [
        "A1",
        ""
    ],
    "041|2": [
        "A1",
        ""
    ],
    "042|1": [
        "A1",
        ""
    ],
    "042|2": [
        "A1",
        ""
    ],
    "043|1": [
        "A1",
        ""
    ],
    "043|2": [
        "A1",
        ""
    ],
    "044|1": [
        "A1",
        ""
    ],
    "044|2": [
        "A1",
        "觸發之複述（`upon the call ending`）"
    ],
    "044|3": [
        "A1",
        ""
    ],
    "045|1": [
        "A1",
        ""
    ],
    "045|2": [
        "A1",
        ""
    ],
    "045|3": [
        "A1",
        ""
    ],
    "046|1": [
        "A1",
        ""
    ],
    "046|2": [
        "A1",
        ""
    ],
    "047|1": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "047|2": [
        "A1",
        ""
    ],
    "047|3": [
        "測試執行",
        "R-PMH97 之二分：其標的為測試員之行為或資料之蒐集，非 SUT 之行為，**不需 DESC 依據**"
    ],
    "047|4": [
        "A1",
        ""
    ]
}


def load_desc() -> dict:
    return {r["swe_requirement_id"]: r["requirement_description"]
            for r in csv.DictReader(
                (ROOT / "data" / "layer3_sections.tsv").open(encoding="utf-8"),
                delimiter="\t")}


def load_tcs(mutate=None) -> dict:
    out = {}
    for p in sorted((ROOT / "generated").glob("batch*.json")):
        for tc in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            er = [x.split(". ", 1)[-1]
                  for x in tc["expected_result"].split("\n") if x.strip()]
            out[tc["tc_id"][-3:]] = {"leaf": tc["leaf_id"], "er": er}
    if mutate:
        mutate(out)
    return out


def assertions(desc: str, leaf: str) -> list:
    if leaf in SPLIT_REVIEW:
        return SPLIT_REVIEW[leaf]
    return [x.strip() for x in SPLIT.split(desc) if x.strip()]


def run(tcs: dict, quiet=False) -> tuple:
    desc = load_desc()
    leaves = sorted({v["leaf"] for v in tcs.values()})
    fwd_bad, rev_bad, rows = [], [], []
    n_unc = 0
    for lid in leaves:
        for i, a in enumerate(assertions(desc[lid], lid), 1):
            key = f"{lid}|{i}"
            ent = FORWARD.get(key)
            if ent is None:
                fwd_bad.append((key, "無判定"))
                continue
            cov, note = ent
            if cov.startswith("未涵蓋"):
                n_unc += 1
                rows.append((lid, i, a, cov, note))
                continue
            sfx, k = cov.split("|")
            tc = tcs.get(sfx)
            if tc is None:
                fwd_bad.append((key, f"所指之 TC `-{sfx}` 不存在"))
            elif len(tc["er"]) < int(k):
                fwd_bad.append((key, f"所指之 `-{sfx}` ER{k} 不存在（該條僅 {len(tc['er'])} 條 ER）"))
            else:
                rows.append((lid, i, a, f"`-{sfx}` ER{k}", note))
    for sfx, tc in sorted(tcs.items()):
        for k in range(1, len(tc["er"]) + 1):
            ent = REVERSE.get(f"{sfx}|{k}")
            if ent is None:
                rev_bad.append((f"-{sfx} ER{k}", "**無依據**（未具名其 DESC 依據）", tc["er"][k - 1]))
            elif ent[0] == "無依據":
                rev_bad.append((f"-{sfx} ER{k}", ent[1], tc["er"][k - 1]))
            elif ent[0] == "例外-本體":
                # R-PMH139（37 包）：例外條款之 ER 得以其**本體 leaf** 之 DESC 為依據，
                # **不計為 §8.4.2 之範圍捏造**。其二條件（行為非新增、本體已具名）
                # 之檢查屬人讀，本檔只承載其結果。
                pass
    if not quiet:
        print("=== 正向：DESC 之每一斷言 × 其 leaf 之 TC 集合（R-PMH133）===")
        print(f"  leaf = **{len(leaves)}**；斷言 = **{sum(1 for _ in rows) + len(fwd_bad)}**；"
              f"**未涵蓋 = {n_unc}**；**未判定／不可解析 = {len(fwd_bad)}**\n")
        for lid, i, a, cov, note in rows:
            if cov.startswith("未涵蓋"):
                print(f"  {lid} A{i}  **{cov}**  {note}")
                print(f"      {a[:96]}")
        for k, why in fwd_bad:
            print(f"  ⚠ {k} —— {why}")
        print(f"\n=== 反向：TC 之每一 ER 斷言 × 其 leaf 之 DESC（R-PMH136）===")
        print(f"  ER 斷言 = **{sum(len(t['er']) for t in tcs.values())}**；"
              f"**無依據 = {len(rev_bad)}**\n")
        for a, why, er in rev_bad:
            print(f"  **{a}** —— {why}")
            print(f"      逐字：{er}")
    return fwd_bad, rev_bad, n_unc


def must_hit() -> int:
    print("=== R-PMH138(d) —— 兩項錨點 ===\n")

    def drop_er(d):
        d["016"]["er"] = d["016"]["er"][:3]

    def add_er(d):
        d["035"]["er"] = d["035"]["er"] + ["The head unit plays a confirmation tone"]

    base_f, base_r, _ = run(load_tcs(), quiet=True)
    ok0 = not base_f and not base_r
    print(f"  (0) 現況：正向不可解析 {len(base_f)}、反向無依據 {len(base_r)}"
          f"  ← **現況之 1 處無依據為實測所得（`-004` ER3），非錨點**")
    f1, _, _ = run(load_tcs(drop_er), quiet=True)
    # ⚠ **本錨點曾偽陽**（36 包實測）：原判準為「輸出中含 `016` 或 `ER4`」，
    # 而現況已有一筆不可解析（`-036` ER3 之筆誤），**其使錨點在未攔到任何東西時亦報 True**。
    # 改為：**須較基準線新增一筆，且該新增之筆須指名 `-016` 所掛之 leaf**。
    new1 = [x for x in f1 if x not in base_f]
    hit1 = bool(new1) and all("018-01" in k and "-016" in w for k, w in new1)
    print(f"  (1) 刪去 `-016` 之 ER4 → 正向新增一筆且指名其 leaf：{hit1}   {new1}")
    _, r2, _ = run(load_tcs(add_er), quiet=True)
    hit2 = len(r2) > len(base_r)
    print(f"  (2) 於 `-035` 增一條 DESC 所無之 ER → 反向報無依據：{hit2}"
          f"   （{len(base_r)} → {len(r2)}）")
    print("\n" + "=" * 60)
    print(f"錨點 (1) {hit1}；錨點 (2) {hit2}")
    return 0 if (hit1 and hit2) else 1


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--must-hit", action="store_true", help="R-PMH138(d) 之兩項錨點")
    a = ap.parse_args()
    if a.must_hit:
        rc = must_hit()
        print_limits()
        sys.exit(rc)
    fwd_bad, rev_bad, _ = run(load_tcs())
    print_limits()
    sys.exit(1 if (fwd_bad or rev_bad) else 0)


if __name__ == "__main__":
    main()
