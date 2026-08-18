"""G190 —— 落底 17 條之功能數複查（R-P271(a)）。

39 §1.4：第 9 列之條件欄為 `Single feature check`，而落底 92 條中
**17 條之功能數為 2**。R-P271(a) 令先查其二功能是否**確為相異功能族**，
經複查仍為 2 者方構成 §12 之覆蓋缺口。

### 判準（本包所立，逐條適用）

**一個功能族僅因其為「受測行為之一部分」而計入。**
若某族之詞僅出現於下列二種位置，**不另計為一個功能**：

  (甲) **情境條件** —— 該族之詞用以指定測試所處之狀態或起點
       （如 `while the HU is in Standby mode`、`Set the boot target to Standby`），
       而受測之行為屬另一族；
  (乙) **觀察媒介** —— 該族之詞用以描述讀取結果之手段
       （如 `Read … the screen to check the antitheft request`），
       而被觀察之對象屬另一族。

**反面**：二族之詞**皆為受測標的**者（如「讀 audio path 與 display
以確認何者被允許」，二者皆為待判之輸出），計為 2。

### ⚠ 一項外部給定之判定，本判準須與之相容

**R-P259 逐字**：分析層判 `…-028`（撥出 → 接聽 → 讀路由與狀態）
為「**跨二個功能**，未達三」。
故「電話」與「音訊輸出」**於本專案已被認定為相異功能族** ——
R-P271(a) 所舉之「二者於通話情境下實為同一功能之二面」之假設，
**由該裁定本身之先例排除**。本檔據此保留其為 2，並將此列為回報事項。

用法：
    python features/power/scripts/recheck_two_features.py
"""

from __future__ import annotations

import collections
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from count_features import features_of  # noqa: E402
from rejudge_design_method import propose  # noqa: E402

# 逐條判定（tc_id 末三碼 → (複查後功能數, 型, 依據)）
# 型：甲＝情境條件、乙＝觀察媒介、—＝二族皆為受測標的
VERDICT: dict[str, tuple[int, str, str]] = {
    "002": (1, "甲", "`Set the boot target status to Standby` 為**情境條件**（起點狀態）；"
                     "受測者為 `Read the TLM display … no splash screen is shown` → 畫面顯示"),
    "008": (1, "甲", "`to the end of the ignition cycle` 為**時間範圍**之界定，非受測之電源行為；"
                     "受測者為 `AUD_LVL` 與 audio output → 音訊輸出"),
    "012": (2, "—", "**電話與音訊輸出皆為受測標的** —— `call audio routing … moved to the head set` "
                    "所驗者為通話之音訊路由；依 R-P259 對 `…-028` 之給定判定，二者為相異族"),
    "028": (2, "—", "**R-P259 逐字給定「跨二個功能」** —— 外部判定，不重判"),
    "098": (1, "乙", "`Read Antitheft_Activation.Req and the screen` 之 screen 為**觀察媒介**，"
                     "其所顯示者即防盜畫面；受測者為防盜"),
    "114": (1, "乙", "同 `…-098` —— `Read the antitheft request and the screen`"),
    "131": (1, "甲", "`while the HU is in Standby mode` 為**情境條件**；"
                     "受測者為 `Read the display backlight` → 畫面顯示"),
    "140": (1, "乙", "同 `…-098` —— `Read the antitheft request, the TLM state and the screen`"),
    "141": (1, "乙", "同 `…-140`"),
    "147": (1, "乙", "同 `…-140`"),
    "150": (1, "乙", "同 `…-140`"),
    "151": (1, "乙", "`brand logo screen presentation` 與 `Read the shown logo` —— "
                     "logo 呈現於畫面即同一事，screen 為**觀察媒介**；受測者為品牌與主題"),
    "202": (2, "—", "**二族皆為受測標的** —— `Read the audio path **and** the display "
                    "to check what is allowed`：音訊路徑與畫面二者皆為待判之輸出"),
    "203": (2, "—", "同 `…-202`"),
    "204": (2, "—", "同 `…-202`"),
    "205": (2, "—", "同 `…-202`"),
    "206": (1, "甲", "`the status related to TLM audio is OFF` 為**情境條件**；"
                     "受測者為 `Read the ICS functions and the DTV` → ICS 模組"),
}


def load() -> list[dict]:
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    return tcs


def main() -> None:
    tcs = load()
    # **⚠ 母體之時點（R-P268 之形態，發生於本包自身）**
    # §H 令 B2（本檔）先於 B1（第 4 列改值）執行 —— 當時落底為 **92** 條，
    # 其中功能數為 2 者 **17** 條，`VERDICT` 即對該 17 條所作。
    # B1 完成後落底縮為 **33** 條，2 功能子集縮為 **10** 條
    # （其餘 7 條移入第 4 列，不再落底）。
    # **本檔不硬斷言母體大小**，改為並陳二時點：
    # `VERDICT` 之 17 條為**分析當時之全集**，現行落底者為其子集。
    low = [t for t in tcs if propose(t)[0] == 9]
    two = [t for t in low if len(features_of(t["test_procedure"])) == 2]
    analysed = sorted(VERDICT)                      # 分析當時之 17 條
    still_low = {t["tc_id"][-3:] for t in two}      # 現仍落底者
    moved = sorted(set(analysed) - still_low)

    still2 = [k for k in analysed if VERDICT[k][0] == 2]
    merged = [k for k in analysed if VERDICT[k][0] == 1]
    kinds = collections.Counter(VERDICT[k][1] for k in merged)
    still2_low = [k for k in still2 if k in still_low]

    out = ["# G190 —— 落底 17 條之功能數複查（R-P271(a)）\n",
           "\n## 一、判準\n\n"
           "**一個功能族僅因其為「受測行為之一部分」而計入。**\n"
           "若某族之詞僅出現於下列二種位置，**不另計**：\n\n"
           "| 型 | 位置 | 例 |\n|---|---|---|\n"
           "| **甲** | **情境條件** —— 指定測試所處之狀態或起點 | "
           "`while the HU is in Standby mode`、`Set the boot target to Standby` |\n"
           "| **乙** | **觀察媒介** —— 讀取結果之手段 | "
           "`Read … the screen to check the antitheft request` |\n\n"
           "**反面**：二族之詞**皆為受測標的**者計為 2。\n",
           "\n## 二、⚠ 一項外部給定之判定\n\n"
           "**R-P259 逐字**：分析層判 `…-028` 為「**跨二個功能**，未達三」。\n"
           "故「電話」與「音訊輸出」**於本專案已被認定為相異功能族** ——\n"
           "R-P271(a) 所舉之「二者於通話情境下實為同一功能之二面」之假設，\n"
           "**由該裁定本身之先例排除**。本檔據此保留 `…-012` / `…-028` 為 2。\n",
           f"\n## 三、複查結果\n\n| 項 | 條數 |\n|---|---|\n"
           f"| 分析當時（落底 92）功能數為 2 | **{len(analysed)}** |\n"
           f"| 　B1 改值後移入第 4 列、不再落底 | **{len(moved)}**"
           f"（{'、'.join('`…-' + k + '`' for k in moved) or '—'}） |\n"
           f"| 　現仍落底者 | **{len(still_low)}** |\n"
           f"| 　複查後**降為 1**（歸第 9 列無虞） | **{len(merged)}** |\n"
           f"| 　　其中型甲（情境條件） | {kinds['甲']} |\n"
           f"| 　　其中型乙（觀察媒介） | {kinds['乙']} |\n"
           f"| 　複查後**仍為 2** —— 構成 §12 覆蓋缺口 | **{len(still2)}** |\n",
           "\n## 四、逐條\n\n| tc | leaf | 原族 | 複查 | 型 | 依據 |\n|---|---|---|---|---|---|\n"]
    for t in two:
        k = t["tc_id"][-3:]
        n, kind, why = VERDICT[k]
        out.append(f"| `…-{k}` | `{t['req_id']}` | {'、'.join(features_of(t['test_procedure']))} | "
                   f"{'**2**' if n == 2 else '1'} | {kind} | {why} |\n")

    if still2:
        out.append(f"\n## 五、(b) 成立 —— §12 之覆蓋缺口\n\n"
                   f"經複查仍為 2 者 **{len(still2)}** 條："
                   f"{'、'.join('`…-' + k + '`' for k in still2)}；\n"
                   f"其中 **{len(still2_low)}** 條於 B1 改值後**仍落於第 9 列**："
                   f"{'、'.join('`…-' + k + '`' for k in still2_low) or '（無）'} ——\n"
                   f"**缺口僅對此 {len(still2_low)} 條成立**，餘者已入第 4 列。\n\n"
                   "§12 第 8 列為 `End-to-end flow, ≥3 features`、"
                   "第 9 列為 `Single feature check` —— **「恰 2 個功能」無列可歸**。\n\n"
                   "依 R-P271(c)：該等條**暫維持第 9 列**（最近之列），"
                   "並於交付說明之驗證邊界載明其不符該列條件欄；"
                   "**另提請 canon 檢討** —— 屬跨 feature，由 Pei 決定是否上呈。\n")

    p = DATA / "g190_two_feature_recheck.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"分析當時 {len(analysed)} 條：降為 1 者 **{len(merged)}**"
          f"（甲 {kinds['甲']} / 乙 {kinds['乙']}）；**仍為 2 者 {len(still2)}** {still2}")
    print(f"B1 改值後：移入第 4 列 {len(moved)} 條 {moved}；現仍落底 {len(still_low)} 條")
    print(f"**缺口成立者 {len(still2_low)} 條**：{still2_low}")


if __name__ == "__main__":
    main()
