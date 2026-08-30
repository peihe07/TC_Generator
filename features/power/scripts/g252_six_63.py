"""R-P381(a) —— G252 六個「查無」之供料頁（64 包 §H 第 3 步）。

**執行層不判定、不查詢、不機掃**（R-P381(a) / 64 包 §I）。
本腳本只做四件事之搬運：
  1. 所屬 tc_id
  2. `test_item` 上半 verbatim
  3. 其錨點 ObjectID 之段落全文（自 CFTS009 / CFTS010 / SYS3 文字層逐字取）
  4. TC 之 Procedure / ER 現行文

人讀與判定由分析層於 65 包為之（R-P381(b)）。

用法：
    python features/power/scripts/g252_six_63.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import csv  # noqa: E402

import remeasure_55 as rm  # noqa: E402
import proxy_reachability_59 as pr  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
TEXT = ROOT / "features/power/data/textlayer"
OUT = ROOT / "features/power/data/g252_six_63.md"

SIX = [
    "call audio routing and the TLM state",
    "remote start outcome flag and the TLM state",
    "HU behavior and the stored logs",
    "shown wording",
    "TLM_Status.Info after each one",
    "TLM state again after Timeout1 has elapsed",
]
ANCHOR_RE = re.compile(r"^(49\d{5}):")


def leaf_anchors() -> dict[str, list[str]]:
    """`leaf` → 其錨點 ObjectID。

    現行 corpus 之 `specification_reference` 為 `{檔名}_{章節}` 式而無 ObjectID
    （A-PW344），`reasoning_note` 亦非每條皆載，故錨點改自
    `data/layer3_full.tsv`（G94 / G99 之來源）取。
    """
    out: dict[str, list[str]] = {}
    f = ROOT / "features/power/data/layer3_full.tsv"
    with f.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ids = [i.strip() for i in (row.get("item_ids") or "").split(",")
                   if i.strip()]
            out.setdefault(row["leaf"], []).extend(ids)
    return out


def paragraph(oid: str) -> tuple[str, str] | None:
    """回傳 (來源, 該 ObjectID 之段落全文)。逐字取，不截斷。"""
    for src in ("cfts009", "cfts010", "sys3"):
        f = TEXT / f"{src}_plain.txt"
        if not f.exists():
            continue
        lines = f.read_text(errors="ignore").splitlines()
        for i, ln in enumerate(lines):
            m = ANCHOR_RE.match(ln)
            if m and m.group(1) == oid:
                body = []
                for nxt in lines[i + 1:]:
                    if ANCHOR_RE.match(nxt) or re.match(r"^\d+(\.\d+)* ", nxt):
                        break
                    body.append(nxt)
                return src.upper(), "\n".join(body).strip()
    return None


def main() -> None:
    cur = rm.load_current()
    anchors = leaf_anchors()
    out = [
        "# G252 六個「查無」之供料頁（63 包產出，64 包 R-P381(a)）",
        "",
        "> **執行層供料，不判定、不查詢、不機掃**（R-P381(a) / 64 包 §I）。",
        "> 人讀與判定由分析層於 65 包為之（R-P381(b)）：",
        "> 有錨（指明段落與代理量）／查無（分析層自負 R-G13 三要件）／",
        "> TC 措辭問題（非觀察目標名，屬 Procedure 改寫，回 R-P353）。",
        "",
        "> 段落全文自 `data/textlayer/*_plain.txt` 逐字取，**未截斷、未摘要**。",
        "",
    ]
    for x in SIX:
        out += [f"## `{x}`", ""]
        owners = []
        for tc in cur:
            for f in ("test_procedure", "expected_result"):
                for line in (tc.get(f) or "").splitlines():
                    m = pr.READ_RE.match(line)
                    if not m:
                        continue
                    obj = re.sub(r"^(the|a|an)\s+", "", m.group(1).strip(),
                                 flags=re.I).strip(" .,")
                    if obj == x and tc not in owners:
                        owners.append(tc)
        for tc in owners:
            item = (tc.get("test_item") or "")
            head = item.split("\n\n(")[0]
            oids = sorted(set(re.findall(r"\b(49\d{5})\b",
                                         (tc.get("reasoning_note") or "")))
                          | set(anchors.get(tc["req_id"], [])))
            out += [
                f"### `{tc['tc_id']}`　（`{tc['req_id']}`）",
                "",
                "**`test_item` 上半 verbatim**",
                "",
                "```",
                head.replace("\xa0", " "),
                "```",
                "",
                "**現行 Procedure**",
                "",
                "```",
                (tc.get("test_procedure") or "").replace("\xa0", " "),
                "```",
                "",
                "**現行 Expected Result**",
                "",
                "```",
                (tc.get("expected_result") or "").replace("\xa0", " "),
                "```",
                "",
            ]
            if not oids:
                out += [f"**錨點段落**：`layer3_full.tsv` 未載 "
                        f"`{tc['req_id']}` 之 `item_ids`。", ""]
            for oid in oids:
                got = paragraph(oid)
                if got is None:
                    out += [f"**錨點 `{oid}`**：文字層查無該 ObjectID。", ""]
                    continue
                src, body = got
                out += [f"**錨點 `{src}-{oid}` 段落全文**", "",
                        "```", body.replace("\xa0", " "), "```", ""]
    OUT.write_text("\n".join(out))
    print(f"六名供料頁 → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
