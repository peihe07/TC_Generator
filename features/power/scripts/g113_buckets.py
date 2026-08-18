"""G113 未覆蓋分支之分桶（R-P171）。

R-P166 方將透鏡 1 之裁決負擔降下，G113 隨即加回一份（23 §八第 2 項：
未覆蓋分支 55、真陽性 2，3.6%）。R-P171 遂令比照 R-P127 對殘差詞之作法，
將未覆蓋分支歸入三桶，**僅 `真缺口` 需完整理由並依 R-P118(d) 裁決**。

**分桶判準（機械，先寫定後執行；不因結果調整）**：

  桶 1 `規格未定義該支` —— 該支**無任何具名標的**，或其內容為
       **示例**（`for example …` / `like …`）或**交叉參照**
       （`refer to … Specification`）。規格就該支未給可測之判準，
       依 R-P118 之「不可獨立驗證」同理，登記不補。

  桶 2 `已由他條或他 leaf 涵蓋` —— 該支之**全部具名標的**
       （訊號名、參數名、模式名、數值）皆見於該 leaf 之任一 TC。
       其未覆蓋判定係由**散文詞**（`user`、`equal`、`respectively`
       一類非標的詞）所致，非標的漏測。

  桶 3 `真缺口` —— 該支有具名標的，而其中至少一個**未見於任何 TC**。
       須完整理由並依 R-P118(d) 裁決。

具名標的之抽取沿用透鏡 2 之 `NAMED_RE` / `NAMED_SKIP`（R-P118），
**未為本閘另訂**，以免以標的定義遷就分桶結果。

用法：
    python features/power/scripts/g113_buckets.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import or_branch_coverage as ob  # noqa: E402
from reverse_coverage import NAMED_RE, NAMED_SKIP, normalize, tc_text  # noqa: E402

# **連接詞不是具名標的**（結構性依據，非為降低真缺口數而設）：
# `IF` / `THEN` / `ELSE` / `AND` / `OR` … 是分支文法之**運算子**，
# 分支正是由它們切出來的；把運算子當成該分支之「標的」，
# 等於要求 TC 逐字寫出連接詞本身。此與 R-P169 所訂正者同類 ——
# **分詞器之錯誤分類**，非門檻或判準之調整。
# 訂正前後之計數一併回報（見上繳 §二），不以訂正後之數字單獨呈現。
CONNECTIVES = {"IF", "THEN", "ELSE", "AND", "OR", "NOR",
               "WHEN", "WHILE", "UNLESS", "END"}
# 黏連形（原文缺空白）：`THENTLM`、`StandbyTHEN`、`valueTHENIF`。
# 剝除連接詞後之殘餘方為標的候選。
#
# **邊界須明確界定**（25 包訂正）：初版以無邊界之 `re.sub` 剝除，
# 致 `Door_Ajar_Status` 之 `oor` 內之 `or` 被當成連接詞剝掉，
# 殘餘 `Do _Ajar_Status` 永不可能見於任何 TC，**虛構出一個真缺口**。
# `DOOR_OFF` 亦同型。此為分詞器之錯誤分類（同 R-P169 之判別），
# 非為降低真缺口數而設；訂正前後之計數並陳（R-P182）。
#
# 三種合法之剝除位置，其餘一律不剝：
#   （1）獨立詞元 —— 前後皆非字母（`IF PROXI` / `ELSE IF`），不分大小寫
#   （2）小寫之後之**大寫**連接詞 —— 黏連（`StandbyTHEN` / `valueTHENIF`）
#   （3）字串起首之**大寫**連接詞後接大寫 —— 黏連（`THENTLM`）
_CONN = "|".join(sorted(CONNECTIVES, key=len, reverse=True))
_STRIP_RES = [
    re.compile(rf"(?<![A-Za-z])(?:{_CONN})(?![A-Za-z])", re.I),   # (1)
    re.compile(rf"(?<=[a-z])(?:{_CONN})(?![a-z])"),               # (2) 大小寫敏感
    re.compile(rf"^(?:{_CONN})(?=[A-Z])"),                        # (3) 大小寫敏感
]


def _strip_connectives(token: str) -> str:
    """剝除連接詞（含黏連形），回傳殘餘。"""
    # 迭代至不動點 —— 剝除一個連接詞可能使下一個成為獨立詞元
    # （`valueTHENIF` 剝 `THEN` 後方露出獨立之 `IF`）。
    t, prev = token, None
    while t != prev:
        prev = t
        for rx in _STRIP_RES:
            t = rx.sub(" ", t)
    return t.strip(" _.-")


# 示例與交叉參照之標記 —— 規格以此引出說明性文字，非可測之分支。
ILLUSTRATIVE_RE = re.compile(
    r"for example|like\s|rather than|refer to .*specification", re.I)

# 抽樣率下限（R-P171）
SAMPLE_RATE = 1 / 6  # 16.7%

# **裁決（R-P118(d)）** —— 機械分桶落入 `真缺口` 者逐項裁決，沉默不算裁決。
# 鍵：(leaf, 組, 支)。值：(裁決, 理由 —— 須指出證據所在)。
ADJUDICATION = {
    ("SWE-PM-031", 1, 1): (
        "已由他條或他 leaf 涵蓋",
        "缺之標的為 `PROXI`，係該參數之**類別名**而非獨立標的；"
        "其所指之參數 `Rear_View_Camera` 已逐字見於 `NR1L-PowerManagement-105` "
        "前提第 2 條（`Rear_View_Camera reads \"Present\"`），"
        "而 `show or not` 兩支分別由該 TC 之 ER 1 / ER 2 承擔。"),
    ("SWE-PM-030", 1, 2): (
        "真缺口",
        "`SWE-PM-030` 僅一條 TC（`NR1L-PowerManagement-104`），其前提為 "
        "`Auto_SwitchOn_Setting.Req reads \"Active\"` —— 即 OR 之**左支**。"
        "右支 `Auto_SwitchOn_Setting.Req == Recall_Last AND VPLastStatus == On` "
        "無任何 TC 覆蓋。**此即「原文以 OR 並列而 TC 只取其一」之同型**，"
        "且係由 G113 於現況資料上前瞻攔下（承第八、第九例，為**第十例**）。"
        "依 R-P118(d) 裁為真缺口，**已補 `NR1L-PowerManagement-105`**"
        "（第三批 63 → 64；其後二條之臨時號順移）。"),
}

BUCKETS = ["規格未定義該支", "已由他條或他 leaf 涵蓋", "真缺口"]


def targets(text: str) -> list[str]:
    """該支之具名標的。"""
    out = []
    for m in NAMED_RE.findall(normalize(text)):
        t = m.strip()
        if not t or t.upper() in NAMED_SKIP:
            continue
        # 點分識別子之左段須含大寫（`Phone_Call.Info` / `TLM_Status.Info`）——
        # `state.In` / `value.The` 係原文句點後缺空白所致之**句讀黏連**，
        # 非識別子（結構性依據，同 R-P169 之分詞器訂正）。
        if "." in t and not any(ch.isupper() for ch in t.split(".")[0]):
            continue
        rest = _strip_connectives(t)
        if not rest or rest.upper() in NAMED_SKIP:
            continue           # 純連接詞（`IF` / `ELSE IF`）或剝除後僅剩載體詞
        if rest not in out:
            out.append(rest)
    return out


def classify(branch_text: str, tc_blob: str,
             group_text: str = "") -> tuple[str, list[str], list[str]]:
    """回傳（桶名、標的、未見於任何 TC 之標的）。

    `group_text` 為**同組全部分支**之文字。示例之判定須於**組層**為之 ——
    `(for example … like DAB Tuner, rather than USB or BT streaming audio)`
    之 `or` 落在示例括號**之內**，其右運算元 `BT streaming audio)` 單獨看
    不含示例標記，但該 OR 本身即為示例之一部分，非規範分支。
    此為結構性依據（OR 之位置），非為降低真缺口數而設。
    """
    tg = targets(branch_text)
    blob = normalize(tc_blob).lower()
    absent = [t for t in tg if t.lower() not in blob]
    if not tg or ILLUSTRATIVE_RE.search(group_text or branch_text):
        return BUCKETS[0], tg, absent
    if not absent:
        return BUCKETS[1], tg, absent
    return BUCKETS[2], tg, absent


def collect() -> list[dict]:
    rows = []
    for p in sorted(GENERATED.glob("*.json")):
        batch = json.loads(p.read_text(encoding="utf-8"))
        by_leaf: dict[str, list[dict]] = {}
        for tc in batch.get("tcs", []):
            by_leaf.setdefault(tc["req_id"], []).append(tc)
        res = ob.analyse(batch)
        for leaf, r in ob.uncovered(res):
            blob = " ".join(tc_text(tc) for tc in by_leaf.get(leaf, []))
            group_text = " ".join(x["text"] for x in res[leaf]
                                  if x["group"] == r["group"])
            bucket, tg, absent = classify(r["text"], blob, group_text)
            raw = bucket
            verdict, reason = ADJUDICATION.get((leaf, r["group"], r["branch"]),
                                               (None, ""))
            if verdict:
                bucket = verdict
            rows.append({"batch": batch.get("batch", "?"), "leaf": leaf,
                         "group": r["group"], "branch": r["branch"],
                         "text": r["text"], "missing": r["missing"],
                         "targets": tg, "absent": absent,
                         "bucket": bucket, "raw": raw, "reason": reason})
    return rows


def render(rows: list[dict]) -> str:
    tot = len(rows)
    counts = {b: sum(1 for r in rows if r["bucket"] == b) for b in BUCKETS}
    out = ["# G113 未覆蓋分支之分桶（R-P171）\n",
           "\n> 判準見 `scripts/g113_buckets.py` docstring —— **先寫定後執行**。\n",
           "> 前二桶給計數與抽樣例示（抽樣率 ≥ 16.7%）；"
           "`真缺口` 逐項完整理由並依 R-P118(d) 裁決。\n",
           f"\n## 計數\n\n| 桶 | 數 | 佔比 |\n|---|---|---|\n"]
    for b in BUCKETS:
        out.append(f"| `{b}` | **{counts[b]}** | {counts[b]/tot*100:.1f}% |\n")
    out.append(f"| **合計** | **{tot}** | 100% |\n")

    for b in BUCKETS[:2]:
        sub = [r for r in rows if r["bucket"] == b]
        k = max(1, -(-len(sub) * 1 // 6)) if sub else 0
        # 抽樣：等距抽樣，非挑選（避免挑好看的）
        step = max(1, len(sub) // k) if k else 1
        sample = sub[::step][:max(k, 1)] if sub else []
        rate = len(sample) / len(sub) * 100 if sub else 0
        out.append(f"\n## 桶 `{b}` —— {len(sub)} 支，抽樣 {len(sample)} 支"
                   f"（{rate:.1f}% ≥ 16.7%）\n\n"
                   "| leaf | 組/支 | 分支文字 | 具名標的 | 觸發未覆蓋之詞 |\n"
                   "|---|---|---|---|---|\n")
        for r in sample:
            tg = "、".join(f"`{t}`" for t in r["targets"][:4]) or "**無**"
            ms = "、".join(f"`{w}`" for w in r["missing"][:4])
            out.append(f"| `{r['leaf']}` | {r['group']}/{r['branch']} | "
                       f"{r['text'][:60]} | {tg} | {ms} |\n")

    moved = [r for r in rows if r["raw"] == BUCKETS[2] and r["bucket"] != BUCKETS[2]]
    if moved:
        out.append(f"\n## 機械落入 `真缺口` 而經裁決改桶者 —— {len(moved)} 支\n\n"
                   "| leaf | 組/支 | 缺之標的 | 改判為 | 理由 |\n|---|---|---|---|---|\n")
        for r in moved:
            out.append(f"| `{r['leaf']}` | {r['group']}/{r['branch']} | "
                       f"{'、'.join('`'+t+'`' for t in r['absent'])} | "
                       f"`{r['bucket']}` | {r['reason']} |\n")

    # 裁為真缺口並已補 TC 者 —— 補後其分支已覆蓋，不再現於上表，
    # 故於此**無條件列出**，避免「補完就看不見」而失去追蹤（R-P171 之逐批追蹤）。
    fixed = [(k, v) for k, v in ADJUDICATION.items() if v[0] == BUCKETS[2]]
    if fixed:
        out.append(f"\n## 本包裁為 `真缺口` 並已補 TC 者 —— {len(fixed)} 支\n\n")
        for (leaf, g, br), (_, reason) in fixed:
            out.append(f"- `{leaf}` 組 {g} 支 {br} —— {reason}\n")
        out.append(f"\n**補前分支總數 {tot + len(fixed)}、真缺口 {len(fixed)}，"
                   f"真陽性率 {len(fixed)/(tot + len(fixed))*100:.1f}%**"
                   f"（23 包為 2 / 55 = 3.6%）。補後如上表。\n")

    gaps = [r for r in rows if r["bucket"] == BUCKETS[2]]
    out.append(f"\n## 桶 `真缺口` —— {len(gaps)} 支（逐項完整，無抽樣）\n")
    if not gaps:
        out.append("\n**無。**\n")
    for r in gaps:
        out.append(f"\n### `{r['leaf']}` 組 {r['group']} 支 {r['branch']}\n\n"
                   f"- 分支原文：`{r['text']}`\n"
                   f"- 具名標的：{'、'.join('`'+t+'`' for t in r['targets'])}\n"
                   f"- **未見於該 leaf 任何 TC 之標的**："
                   f"{'、'.join('`'+t+'`' for t in r['absent'])}\n"
                   f"- 觸發未覆蓋之獨有實詞：{'、'.join('`'+w+'`' for w in r['missing'])}\n"
                   f"- **裁決（R-P118(d)）：真缺口** —— {r['reason']}\n")
    return "".join(out)


def main() -> None:
    rows = collect()
    (DATA / "g113_buckets.md").write_text(render(rows), encoding="utf-8")
    counts = {b: sum(1 for r in rows if r["bucket"] == b) for b in BUCKETS}
    print(f"wrote {(DATA / 'g113_buckets.md').relative_to(ROOT)}")
    for b in BUCKETS:
        print(f"  {b}: {counts[b]}")
    print(f"  合計 {len(rows)}")


if __name__ == "__main__":
    main()
