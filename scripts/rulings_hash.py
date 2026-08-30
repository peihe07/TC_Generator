#!/usr/bin/env python3
"""裁決條文之指紋表（R-G13）。

R-G13 以 `R-XX@<sha8>` 為下放包之引用格式，執行層自 repo 讀原文並回報
所讀 sha8。本工具產生該對照表 `docs/fw036/RULINGS.sha.tsv`。

**條文本體之定義**（量測條件，須與上繳包所載一致）：
自錨點標題之**次行**起，至下一個同級或更高級標題之**前一行**止；
首尾空行去除，行尾空白去除，行間以 `\\n` 接合，UTF-8 編碼後取 sha256。
標題文字本身**不入雜湊** —— 標題含輪次與日期，其變動不應改變條文身分。

唯讀，只寫 `--out` 所指之 tsv。`--check` 時比對既有 tsv，不符 exit 1。
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# 錨點：`### R-XX <slug>`；階數 2~4 皆收，以 `#` 數記其級。
# 子條之三種書寫（`R-VS57 之 (4)`／`R-VS57(4)`／`R-VS7(a)′`）一律收進 id，
# 否則子條會與母條同 id 而假性碰撞。
RE_ANCHOR = re.compile(
    r"^(?P<hashes>#{2,4})\s*"
    r"(?P<base>R-[A-Z]{0,3}\d+[A-Za-z]?)"
    r"(?P<sub>(?:\s*之)?\s*\([0-9a-z]+\))?"
    r"(?P<prime>[′″‴]*)"
    r"(?P<qual>\s*(?:之補充|之修訂|之解釋|之更正|但書))?"
    r"\s*(?P<rest>.*)$"
)
RE_HEADING = re.compile(r"^(#{1,6})\s")
# 非條文段落：條號於此僅為標題重用（執行層回報、落實紀錄），其本體非條文
RE_NON_RULING = re.compile(r"執行層回報|落實紀錄|實測紀錄|回報摘要")
# 作廢標記：標題含之者，其自身與其下轄各級標題皆為 superseded
RE_SUPERSEDED = re.compile(r"作廢|SUPERSEDED|已撤回")
# 群組標題（`## R-C1 ~ R-C5 —— 下放包 01`）：其非單條之錨點，不得佔用首條之 id。
# 判別特徵為 slug **以分隔符或連接詞起首**再接另一條號；
# 不得只憑「slug 以條號起首」—— `### R-VS82 —— R-G14 綠色通道之生效起點`
# 之 slug 即以條號起首而其為單條錨點（W-P2 實測之假陽）。
RE_GROUP = re.compile(r"^\s*(?:[~～、／/,]|及|與|至)\s*R-[A-Z]{0,3}\d")

OUT_DEFAULT = "docs/fw036/RULINGS.sha.tsv"
COLUMNS = ["ruling_id", "kind", "sha8", "sha256", "body_sha8", "body_sha256", "body_kind",
           "source", "line", "body_lines", "ancestor", "slug"]
# W-P1 §4：本輪結構化範圍為 canon §9 與 vehicle_setting；其餘 feature 延後
# R-POP11（Pei 2026-08-27）：預設範圍納入**全部** `features/*/RULINGS.md`。
# 理由 —— R-G13 明定條文落各 feature 之 RULINGS.md，tsv 不涵蓋則引用制半殘：
# 下放包引 `R-XX@<sha8>`，而執行層無從自 tracked 表查證該 sha8。
# 原 W-P1 之兩檔窄範圍保留於 `SCOPE_W_P1`，供追溯與比對用，非預設。
SCOPE_W_P1 = ["docs/fw036/FEATURE_ONBOARDING.md", "features/vehicle_setting/RULINGS.md"]


@dataclass(frozen=True)
class Ruling:
    ruling_id: str
    kind: str            # ruling | report（report 為條號被重用作回報標題者）
    sha256: str          # === section_sha（該錨點至下一錨點之全部內容，含成因段）
    body_sha256: str     # 條文本體（首個 fenced block）；無 fence 者退回整節
    body_kind: str       # fenced | section —— `section` 者其二值相同（R-G22′ 之殘餘）
    source: str
    line: int
    body_lines: int
    ancestor: str        # 最近之 `## ` 祖先標題，供判讀重複之成因
    slug: str

    @property
    def sha8(self) -> str:
        return self.sha256[:8]

    @property
    def body_sha8(self) -> str:
        return self.body_sha256[:8]

    def row(self) -> str:
        return "\t".join([
            self.ruling_id, self.kind, self.sha8, self.sha256,
            self.body_sha8, self.body_sha256, self.body_kind,
            self.source, str(self.line), str(self.body_lines),
            self.ancestor, self.slug,
        ])


# 章節分隔線 —— 其不屬任何條文，卻落在前一條之本體範圍內
RE_HRULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
# 行內程式碼片段 —— `<details>` 於敘述文字中被反引號括起時是**談論**該標籤，
# 不是開啟一個摺疊區。計數前一律剝除，否則巢深永不歸零，
# 其後全部條文遭誤判 superseded（W-27 實測：VS RULINGS L5301／L5325 之敘述行
# 使 R-VF96 以降 46 條全數誤判）。
RE_INLINE_CODE = re.compile(r"`[^`]*`")


def body_sha(lines: list[str]) -> tuple[str, int]:
    """條文本體之雜湊與其行數（量測條件見 module docstring）。

    **尾端之分隔線與空行一律剝除**：`---` 為章節之分隔，不屬任何一條。
    不剝除者，同一條文之 sha 會因**其後是否追加新章節**而改變 ——
    W-P3 實測：R-VS82 在其後追加 `## 主線 —— 26 包` 後 sha 由 `12177e4f`
    變為另一值，**而其本體一字未改**。那種假性不符若累積，
    R-G13 之 sha 比對就會被當成噪音忽略，而**那正是 R-G13 之效力所繫**。
    """
    trimmed = [ln.rstrip() for ln in lines]
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    while trimmed and (not trimmed[-1] or RE_HRULE.match(trimmed[-1])):
        trimmed.pop()
    body = "\n".join(trimmed)
    return hashlib.sha256(body.encode("utf-8")).hexdigest(), len(trimmed)


def fenced_body(lines: list[str]) -> tuple[list[str], str]:
    """取條文本體（R-G22′，下放包 57 §二 #1）。

    **本體 = 該節之全部 fenced block 之內容串接**（不含 ``` 兩行，依出現序，無分隔符）。
    **取全部而非首個**（下放包 58 §三 #2）：條文分成二框者（如 `R-G23` 與其
    `[DEFAULT]` 段），**第二框亦為規範內容，取首個即漏掉一半規範**。
    其偏差方向安全 —— **多算使 sha 多變（可容忍），漏算使規範不受保護（不可容忍）**。
    節內無 fenced block 者**退回整節**，其 `body_kind` 記為 `section` ——
    **該類條之 `body_sha` 與 `section_sha` 相同，R-G13 之假性不符對其未解**
    （上繳包 57 §6 之自評；實測 74 條）。
    首個之後的 fenced block 視為實例或引文，不入本體（實測 19 條有二個以上）。
    """
    out: list[str] = []
    start = None
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            if start is None:
                start = i
            else:
                out.extend(lines[start + 1:i])
                start = None
    return (out, "fenced") if out else (lines, "section")


def extract(path: Path, root: Path) -> list[Ruling]:
    """自單一 markdown 檔抽出全部具錨點之條文。"""
    lines = path.read_text(encoding="utf-8").splitlines()
    source = str(path.relative_to(root))
    # (idx, level, id, ancestor, slug, superseded)
    anchors: list[tuple[int, int, str, str, str, bool]] = []
    ancestor = ""
    in_fence = False
    details = 0          # `<details>` 巢深；其內之條文一律 superseded（留痕用之原文）
    dead_level = 0       # >0 表尚在某作廢標題之轄下，其值為該標題之級
    for idx, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        bare = RE_INLINE_CODE.sub("", line)
        details += bare.count("<details") - bare.count("</details>")
        h = RE_HEADING.match(line)
        if h:
            level = len(h.group(1))
            if dead_level and level <= dead_level:
                dead_level = 0
            if RE_SUPERSEDED.search(line):
                dead_level = level
        if line.startswith("## "):
            ancestor = line[3:].strip()
        m = RE_ANCHOR.match(line)
        if m:
            sub = (m.group("sub") or "").replace("之", "").replace(" ", "")
            qual = (m.group("qual") or "").strip().lstrip("之")
            ruling_id = m.group("base") + sub + m.group("prime") + (f"+{qual}" if qual else "")
            slug = m.group("rest").strip().lstrip("—–-").strip()
            dead = details > 0 or (dead_level and len(m.group("hashes")) > dead_level)
            anchors.append((idx, len(m.group("hashes")), ruling_id, ancestor, slug, bool(dead)))

    out: list[Ruling] = []
    for idx, level, ruling_id, anc, slug, dead in anchors:
        end = len(lines)
        for j in range(idx + 1, len(lines)):
            h = RE_HEADING.match(lines[j])
            if h and len(h.group(1)) <= level:
                end = j
                break
        section = lines[idx + 1:end]
        sha, n = body_sha(section)
        # 本體之取材止於**下一個任何層級之標題**（下放包 60 T72b 實測）——
        # 否則巢狀之子條（`## R-AM2` 下之 `### R-AM2′`）其框會被算進母條之本體。
        own = section
        for k, ln in enumerate(section):
            if RE_HEADING.match(ln):
                own = section[:k]
                break
        bl, bkind = fenced_body(own)
        bsha, _ = body_sha(bl)
        if RE_GROUP.match(slug):
            kind = "group"
        elif dead:
            kind = "superseded"
        elif RE_NON_RULING.search(anc):
            kind = "report"
        else:
            kind = "ruling"
        out.append(Ruling(ruling_id, kind, sha, bsha, bkind,
                          source, idx + 1, n, anc, slug))
    return out


def collect(root: Path, targets: list[str]) -> tuple[list[Ruling], list[str]]:
    """掃描目標檔；回傳條文清單與重複 id 之警告。"""
    rulings: list[Ruling] = []
    for rel in targets:
        p = root / rel
        if not p.exists():
            continue
        rulings.extend(extract(p, root))

    seen: dict[str, Ruling] = {}
    dupes: list[str] = []
    for r in (x for x in rulings if x.kind == "ruling"):
        prev = seen.get(r.ruling_id)
        if prev is None:
            seen[r.ruling_id] = r
        else:
            dupes.append(
                f"{r.ruling_id}: {prev.source}:{prev.line} 與 {r.source}:{r.line}"
                + ("（本體相同）" if prev.sha256 == r.sha256 else "（**本體不同**）")
            )
    rulings.sort(key=lambda r: (r.source, r.line))
    return rulings, dupes


def default_targets(root: Path, w_p1_only: bool = False) -> list[str]:
    """預設為 canon ＋ 全部 feature 之 `RULINGS.md`（R-POP11）。

    `w_p1_only=True` 取回原 W-P1 之兩檔窄範圍 —— 保留是為了能回答
    「擴範圍前後某條之 sha 是否變動」，不是預設路徑。
    """
    if w_p1_only:
        return list(SCOPE_W_P1)
    targets = ["docs/fw036/FEATURE_ONBOARDING.md"]
    targets += sorted(
        str(p.relative_to(root)) for p in (root / "features").glob("*/RULINGS.md")
    )
    return targets


def main() -> int:
    ap = argparse.ArgumentParser(description="裁決條文指紋表（R-G13）")
    ap.add_argument("--root", default=".", help="repo 根目錄")
    ap.add_argument("--out", default=OUT_DEFAULT, help="輸出 tsv")
    ap.add_argument("--target", action="append", default=None, help="指定來源檔（可重複）")
    ap.add_argument("--check", action="store_true", help="只比對既有 tsv，不寫入")
    ap.add_argument("--all-features", action="store_true",
                    help="（R-POP11 後為預設行為；旗標保留為 no-op，不破既有呼叫）")
    ap.add_argument("--w-p1-only", action="store_true",
                    help="取回原 W-P1 之兩檔窄範圍（canon ＋ vehicle_setting），比對用")
    ap.add_argument("--gate", action="store_true", help="有重複 id 之本體歧異時 exit 1")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    targets = args.target or default_targets(root, args.w_p1_only)
    rulings, dupes = collect(root, targets)

    # 檔首註（下放包 56 T68a）—— 本檔為單一全域檔，其重生必然含當時全部線之條文
    note = ("# 本檔為單一全域檔：其重生一律掃描全部 canon 與各 feature 之 "
            "RULINGS.md，故其 commit 不可能只含單一變更之列。"
            "夾帶之他線列為結構性質，非該次提交之瑕疵（下放包 56 §二 #1）。\n")
    body = note + "\n".join(["\t".join(COLUMNS)] + [r.row() for r in rulings]) + "\n"
    out_path = root / args.out

    if args.check:
        if not out_path.exists():
            print(f"FAIL: {args.out} 不存在", file=sys.stderr)
            return 1
        if out_path.read_text(encoding="utf-8") != body:
            print(f"FAIL: {args.out} 與現行條文不符 —— 重跑本工具並覆核 diff", file=sys.stderr)
            return 1
        print(f"OK: {args.out} 與現行條文相符（{len(rulings)} 條）")
    else:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body, encoding="utf-8")
        tally: dict[str, int] = {}
        for r in rulings:
            tally[r.kind] = tally.get(r.kind, 0) + 1
        breakdown = "／".join(f"{k} {v}" for k, v in sorted(tally.items()))
        print(f"寫入 {args.out}：{len(rulings)} 錨點（{breakdown}），來源 {len(targets)} 檔")

    hard = [d for d in dupes if "本體不同" in d]
    if dupes:
        print(f"\n重複 ruling_id {len(dupes)} 組（其中本體不同 {len(hard)} 組）：", file=sys.stderr)
        for d in dupes:
            print(f"  {d}", file=sys.stderr)
    return 1 if (args.gate and hard) else 0


if __name__ == "__main__":
    sys.exit(main())
