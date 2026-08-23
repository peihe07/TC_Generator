"""W-119 —— Part 1 之 open DR 是否波及 VF230 之 leaf（62 包 §5.4）。

依 **R-VS65** 之掃描定義（逐字）：
  - 掃哪些欄：`title` ＋ `desc`（`swe_id`／`src_ref`／`family` 不掃）
  - 大小寫：不分
  - 詞界：以詞界為準，不作子字串命中
  - 每個 DR 各自列出其掃描 token，token 由該 DR 之提問正文取得，不自創

輸出三分類：波及（命中 ≥1，附命中數與 3 個示例 swe_id）／不波及（命中 0）／
待判（token 無法自 DR 正文機械取得者）。

**「命中 0」不等於「不波及」之證明** —— 其僅證該 token 未出現。
概念型 DR（其提問不繫於任何可掃之 token）一律標「待判」，不標「不波及」。

輸出：docs/reports/vf230_dr_impact.md ＋ data/_vf230_dr_impact.json
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 62 包 §5.4 指名之標的：Part 1 之全部 open DR
OPEN_DR = ["DR-8", "DR-11", "DR-12", "DR-14′", "DR-15", "DR-17", "DR-18",
           "DR-19", "DR-20", "DR-21", "DR-25", "DR-26", "DR-27"]

# token 之機械取得式 —— 三種形態，皆為 DR 正文之既有書寫，不自創
TOKEN_PATS = [
    re.compile(r"\$([A-Za-z][A-Za-z0-9_]{2,})\$"),          # $HSW_Stat$
    # 訊息.訊號 —— 取**全稱**。首版只取 group(1)（訊息名），致 DR-25 之
    # `TELEMATIC_VEHICLE_SETUP` 命中 172 leaf，而該 DR 所問者為其下之
    # 四個 Cmd_Tlm 訊號。此為 A-VS117 形態之再現（抽取式初版過寬）。
    re.compile(r"\b([A-Z][A-Z0-9_]{2,}\.[A-Za-z]\w{2,})\b(?!\.)"),
    re.compile(r"`\$?([A-Z][A-Za-z0-9_]{3,})\$?`"),          # `FL_HS_RQ`
]
# 掃描時排除之泛用詞（其為文件用語，非訊號名）
STOP = {"DR", "TC", "HU", "HMI", "CAN", "LID", "DBC", "SYS", "PROXI", "VHAL",
        "NEW", "OK", "ON", "OFF", "AND", "OR", "NOT", "ALL", "NA", "SNA",
        "CFTS", "VF", "SWE", "SWQT", "SWRA", "ID", "IDS", "REF", "PDO",
        "ASIL", "FTTI", "BLOCKED", "PENDING", "WARN", "FAIL", "TRUE", "FALSE"}


def split_drs(text: str) -> dict[str, str]:
    """`DATA_REQUESTS.md` 切為逐 DR 之正文（以 `## DR-` 標題切）。"""
    out: dict[str, str] = {}
    cur, buf = None, []
    for ln in text.splitlines():
        m = re.match(r"^##\s+(DR-[0-9]+[′']?)", ln)
        if m:
            if cur:
                out[cur] = out.get(cur, "") + "\n".join(buf)
            cur, buf = m.group(1), []
            continue
        if cur:
            buf.append(ln)
    if cur:
        out[cur] = out.get(cur, "") + "\n".join(buf)
    # 「仍開啟」表之列亦為 DR 正文（DR-8／DR-11／DR-12 等以表列存在，
    # 無 `## DR-N` 標題）。首版只切標題，致該類一律落入「待判」。
    for ln in text.splitlines():
        m = re.match(r"^\|\s*\*{0,2}(\d+)[^|]*\*{0,2}\s*\|", ln)
        if m:
            out.setdefault(f"DR-{m.group(1)}", "")
            out[f"DR-{m.group(1)}"] += "\n" + ln
    return out


def tokens_of(body: str) -> list[str]:
    """自 DR 正文機械取得之 token，去重、去泛用詞。

    **識別式判準**：本語料之訊號名一律含 `_` 或 `.`（`FL_HS_RQ`／
    `TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm`／`Hybrid_Type`）；
    不含者為英文常用詞（`High`／`Medium`／`START`／`Radio`），
    其以詞界掃 leaf 之 title/desc 必大量偽陽性。首版未設此判準，
    致 DR-15 命中 14（實為 `High` 9 ＋ `Medium` 5）、DR-25 命中 174
    （實為訊息名 `TELEMATIC_VEHICLE_SETUP` 172）——**皆為假波及**。
    """
    found = set()
    for i, pat in enumerate(TOKEN_PATS):
        for m in pat.finditer(body):
            t = m.group(1)
            if t.upper() in STOP or len(t) < 3:
                continue
            # `$X$` 與 `A.B` 為語料之明示訊號記法，其本身即為識別式，
            # 不再過濾（`$DriverSide$` 無底線，過濾會使 DR-20 空手）。
            # 反引號式則會抓到值與泛用詞（`High`／`Medium`／`Radio`），
            # 故僅於該式套「含 `_` 或 `.`」之識別式判準。
            if i == 2 and "_" not in t and "." not in t:
                continue
            found.add(t)
    return sorted(found)


def main() -> None:
    drs = split_drs((ROOT / "DATA_REQUESTS.md").read_text(encoding="utf-8"))
    leaves = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    # 掃描面：title ＋ desc（R-VS65）
    hay = [(l["swe_id"], (l["title"] + " " + l["desc"]).lower()) for l in leaves]

    rows = []
    for name in OPEN_DR:
        body = drs.get(name) or drs.get(name.rstrip("′'"), "")
        if not body:
            rows.append({"dr": name, "verdict": "待判",
                         "why": "本檔無其正文 —— `DATA_REQUESTS.md` 之「仍開啟」"
                                "表以**表列編號**（5-A／5-B／7／8／9／10）記之，"
                                "與內文之 DR-N 編號不同套。DR-11 僅於行 136 "
                                "以交叉參照出現（`即 DR-11`），指向表列第 9 項"
                                "（`HeatedSteeringWheel-009` 之 Source Requirement ID）。"
                                "**其提問為單一 leaf 之 reqid 更正，非 token 型**，"
                                "掃描無從施力。",
                         "tokens": [], "hits": 0, "examples": []})
            continue
        toks = tokens_of(body)
        if not toks:
            rows.append({"dr": name, "verdict": "待判",
                         "why": "正文無可機械取得之 token（概念型提問）",
                         "tokens": [], "hits": 0, "examples": []})
            continue
        hit_ids, per_tok = set(), {}
        for t in toks:
            pat = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(t.lower())
                             + r"(?![A-Za-z0-9_])")
            ids = [sid for sid, h in hay if pat.search(h)]
            if ids:
                per_tok[t] = len(ids)
                hit_ids.update(ids)
        rows.append({"dr": name,
                     "verdict": "波及" if hit_ids else "不波及",
                     "why": "", "tokens": toks, "token_hits": per_tok,
                     "hits": len(hit_ids), "examples": sorted(hit_ids)[:3]})

    L = ["# W-119 —— Part 1 之 open DR 對 VF230 leaf 之波及判定", "",
         "**依 R-VS65 之掃描定義（62 包 §3）。**", "",
         "- 掃描面：`data/vf230_leaves.tsv` 之 `title` ＋ `desc`"
         f"（{len(leaves)} leaf）；`swe_id`／`src_ref`／`family` 不掃",
         "- 大小寫不分；**以詞界為準，不作子字串命中**",
         "- token 由各 DR 之提問正文機械取得（`$X$`／`A.B`／`` `X` `` 三式），",
         "  去泛用詞後去重。**不自創 token。**", "",
         "> **「命中 0」不是「不波及」之證明** —— 其僅證該 token 未出現於 leaf 之",
         "> title/desc。概念型 DR（提問不繫於可掃之 token）一律標「待判」。", "",
         "| DR | 判定 | 命中 leaf | token 數 | 示例 swe_id |",
         "|---|---|---:|---:|---|"]
    for r in rows:
        ex = "／".join(f"`{e}`" for e in r["examples"]) or "—"
        L.append(f"| **{r['dr']}** | {r['verdict']} | {r['hits']} | "
                 f"{len(r['tokens'])} | {ex} |")

    L += ["", "## 逐 DR 之 token 與命中", ""]
    for r in rows:
        L += [f"### {r['dr']} —— {r['verdict']}", ""]
        if r["why"]:
            L += [f"**{r['why']}**", ""]
        if r["tokens"]:
            L += ["自正文取得之 token（" + str(len(r["tokens"])) + "）：", "",
                  "```", "  ".join(r["tokens"]), "```", ""]
            if r.get("token_hits"):
                L += ["命中之 token 與其 leaf 數：", ""]
                L += [f"- `{t}` — {n}" for t, n in
                      sorted(r["token_hits"].items(), key=lambda x: -x[1])]
                L += [""]
            else:
                L += ["**全部 token 命中 0。**", ""]

    v = {k: sum(1 for r in rows if r["verdict"] == k)
         for k in ("波及", "不波及", "待判")}
    L += ["## 小結", "",
          f"波及 **{v['波及']}** ／ 不波及 **{v['不波及']}** ／ 待判 **{v['待判']}**",
          "", "**未以任何 DR 為由阻塞 VF230 之 P1**（61 包 §4.6 之禁令）。", ""]

    out = ROOT / "docs" / "reports" / "vf230_dr_impact.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_vf230_dr_impact.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    for r in rows:
        print(f"  {r['dr']:8} {r['verdict']:5} hits={r['hits']:3} "
              f"tokens={len(r['tokens']):2} {r['why']}")
    print(f"\n波及 {v['波及']} ／ 不波及 {v['不波及']} ／ 待判 {v['待判']}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
