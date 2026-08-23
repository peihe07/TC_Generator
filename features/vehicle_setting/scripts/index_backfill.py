"""INDEX.md 補齊（61 包 §8 之末項）。

`INDEX.md` 現僅記至 NN=01，實際下放包已至 NN=61。本腳本以**可機械
驗證之欄位**回填，不臆測：

  NN            **往返輪次**，即 `docs/upstream/` 之序（既有表之 NN=00／01
                與之相符）。**handoff 之包號為另一套計數**（至 61），
                二者不可以號相等配對 —— 首版曾如此配對，造出 27 組假對應。
  主題          自各上繳之 H1 逐字取得
  下放          自各上繳前 6 列所自述之依據（`docs/handoff/NN_…` 之引用，
                或 `往返 NN = NN` 之自述）解出；一輪可對多包
  上繳          該輪之上繳檔本身
  新條文        該 handoff 為全庫**首次**提及某 R-VS 之文件者，計為其新條文
  新 anomaly    同上，對 A-VS

「結果」欄需逐輪之判斷，**不由本腳本產生** —— 一律填 `—（未回填）`，
其實質內容以對應之上繳文件為準。此為 61 包所允之「具名說明未補之範圍」。

既有之 NN=00／NN=01 兩列為人工撰寫且含補篇連結，**逐字保留不覆蓋**。
"""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "handoff"
UPSTREAM = ROOT / "docs" / "upstream"
KEEP_NN = {"00", "01"}          # 既有列，保留


def nn_of(name: str) -> str | None:
    """檔名前綴之 NN；補篇（00A 等）回 None。"""
    m = re.match(r"^(\d{2})_", name)
    return m.group(1) if m else None


def h1_of(path: Path) -> str:
    """H1 逐字，去前綴之 `# ` 與開頭之 `NN 上繳／下放包` 標號。"""
    first = path.read_text(encoding="utf-8").splitlines()[0]
    t = first.lstrip("#").strip()
    t = re.sub(r"^(上繳|下放包)?\s*\d{2}[A-Z]?\s*(上繳|下放包)?\s*", "", t)
    return re.sub(r"^[\s—\-–]+", "", t).strip()


def cited_handoffs(up: Path) -> list[str]:
    """一篇上繳所依據之 handoff 包號。

    30 輪起之上繳於前段逐字寫「依據：`docs/handoff/NN_…`」；
    早期者僅寫「往返 NN = NN」，其時兩套編號尚未分岔，故以該 NN 為包號。
    """
    head = "\n".join(up.read_text(encoding="utf-8").splitlines()[:8])
    # 引用為**完整檔名**：同一包號可有多檔（如 61_review_round37 與
    # 61_vf230_intake），只取包號會任選其一。
    hits = re.findall(r"docs/handoff/([0-9]{2}[A-Za-z0-9_]*\.md)", head)
    if hits:
        return [("cite", h) for h in dict.fromkeys(hits)]
    m = re.search(r"往返\s*NN\s*=\s*(\d{2})", head)
    return [("nn", m.group(1))] if m else []


def first_seen(dirs: list[Path], pat: str) -> dict[str, str]:
    """token -> 首次提及之檔名（依 NN 遞增掃描）。"""
    seen: dict[str, str] = {}
    files = sorted((f for d in dirs for f in d.glob("*.md")),
                   key=lambda f: (nn_of(f.name) or "99", f.name))
    for f in files:
        txt = f.read_text(encoding="utf-8")
        for tok in re.findall(pat, txt):
            seen.setdefault(tok, f.name)
    return seen


def compress(toks: list[str], prefix: str) -> str:
    """連號摺為區間：R-VS1,2,3,7 -> R-VS1–3、R-VS7。"""
    nums = sorted(int(t[len(prefix):]) for t in toks)
    if not nums:
        return "—"
    runs, start, prev = [], nums[0], nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        runs.append((start, prev))
        start = prev = n
    runs.append((start, prev))
    return "、".join(f"{prefix}{a}" if a == b
                     else (f"{prefix}{a}、{prefix}{b}" if b == a + 1
                           else f"{prefix}{a}–{b}")
                     for a, b in runs)


def main() -> None:
    ho: dict[str, list[Path]] = defaultdict(list)
    for f in sorted(HANDOFF.glob("*.md")):
        if nn_of(f.name):
            ho[nn_of(f.name)].append(f)
    by_name = {f.name: f for f in HANDOFF.glob("*.md")}
    ups = sorted((f for f in UPSTREAM.glob("*.md") if nn_of(f.name)),
                 key=lambda f: nn_of(f.name))

    # 首次提及：只掃 handoff 與 upstream，不掃 RULINGS/ANOMALIES
    # （後者為落檔簿，其提及不代表該輪新開）
    rul = first_seen([HANDOFF, UPSTREAM], r"\bR-VS\d+\b")
    ano = first_seen([HANDOFF, UPSTREAM], r"\bA-VS\d+\b")
    by_file_r: dict[str, list[str]] = defaultdict(list)
    by_file_a: dict[str, list[str]] = defaultdict(list)
    for tok, fn in rul.items():
        by_file_r[fn].append(tok)
    for tok, fn in ano.items():
        by_file_a[fn].append(tok)

    rows, claimed = [], set()
    for u in ups:
        nn = nn_of(u.name)
        cites = cited_handoffs(u)
        # 解為實體檔：`cite` 為逐字引用（可靠）；`nn` 為該上繳僅自述
        # 「往返 NN = NN」時之推得（同號之 handoff 全數列入，並標記）。
        files, derived = [], False
        for kind, val in cites:
            if kind == "cite" and val in by_name:
                files.append(by_name[val])
            elif kind == "nn":
                files += ho.get(val, [])
                derived = True
        claimed.update(f.name for f in files)
        if nn in KEEP_NN:
            continue
        dl = "／".join(f"[{f.name[:2]}](handoff/{f.name})" for f in files) or "—"
        if derived and files:
            dl += " ⟨依自述往返 NN⟩"
        rt = list(by_file_r.get(u.name, []))
        at = list(by_file_a.get(u.name, []))
        for f in files:
            rt += by_file_r.get(f.name, [])
            at += by_file_a.get(f.name, [])
        rows.append((nn, h1_of(u), dl,
                     f"[upstream/{u.name}](upstream/{u.name})",
                     compress(rt, "R-VS"), compress(at, "A-VS")))

    orphans = [f for fs in ho.values() for f in fs
               if f.name not in claimed and nn_of(f.name) not in KEEP_NN]

    src = (ROOT / "docs" / "INDEX.md").read_text(encoding="utf-8")
    lines = src.splitlines()
    last = max(i for i, ln in enumerate(lines) if ln.startswith("| 01 |"))
    new = [f"| {nn} | — | {topic} | {dl} | {ul} | {r} | {a} | —（未回填） |"
           for nn, topic, dl, ul, r, a in rows]

    note = [
        "",
        "> **本表 NN≥02 之列由 `scripts/index_backfill.py` 機械回填（38 輪，61 包 §8）。**",
        "> **NN 為往返輪次**（`docs/upstream/` 之序，現至 34），",
        "> **與 handoff 之包號（現至 61）為兩套計數**，不可以號相等配對。",
        "> 「下放」欄自各上繳前段之**逐字引用**（`docs/handoff/…md`）解出，",
        "> 一輪可對多包。標 ⟨依自述往返 NN⟩ 者為該上繳未逐字引用下放包、",
        "> 僅自述「往返 NN = NN」，故以同號之 handoff 推得 —— **該對應為推得，非引用**。",
        "> 「新條文」／「新 anomaly」之判準為**該輪之下放或上繳為 `docs/` 內",
        "> 首次提及該編號之文件**，非「該輪裁定成立」—— 一條文可先於某輪",
        "> 被提及而於後輪方裁定。",
        "> **「日期」與「結果」兩欄未回填** —— 二者需逐輪之判斷，不由機械產生；",
        "> 其實質以各列所連之上繳文件為準。此即 61 包所允之「具名說明未補之範圍」。",
        "",
    ]
    if orphans:
        note += [f"### 尚無對應上繳之下放包（{len(orphans)} 件）", "",
                 "下列包未被任何上繳自述為依據 —— 或為補篇／指令書，"
                 "或其輪次尚未上繳。", "",
                 "| 包號 | 主題 |", "|---|---|"]
        note += [f"| [{f.name[:2]}](handoff/{f.name}) | {h1_of(f)} |"
                 for f in sorted(orphans, key=lambda x: x.name)]
        note += [""]

    k = next((i for i, ln in enumerate(lines)
              if i > last and ln.startswith("## ")), len(lines))
    out = lines[:last + 1] + new + lines[last + 1:k] + note + lines[k:]
    (ROOT / "docs" / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"回填 {len(rows)} 列（往返 NN {rows[0][0]}–{rows[-1][0]}）")
    print(f"尚無對應上繳之下放包：{len(orphans)} 件")
    print(f"R-VS 首見總數 {len(rul)}；A-VS 首見總數 {len(ano)}")


if __name__ == "__main__":
    main()
