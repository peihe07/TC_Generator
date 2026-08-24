"""W-161（84 包 §4／§5）—— `REGEN_ORDER.md`。

R-VS53 之「產物須可自 driver 重製」於早批**已不成立** ——
`batch17_v6` 非 `batch17` 之生成器重跑，而是 `batch17_v5` 加一層修正腳本。
84 包 §4 裁定：**不重構早批之生成器**，改記錄其**有序腳本鏈**。

本檔自 `generated/*.json` 之 `revision` 欄與各腳本之產出關係推得該鏈，
逐批列：原生成器 → 各層修正腳本（依序）→ 現行版本 → sha256。
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches      # noqa: E402

GEN = FEAT / "generated"

# **本表全數機械推導** —— 不得人工代擬檔名（56 輪首版曾自行編出 14 個
# 不存在之檔名，其為禁區「不代擬」之違反，已改）。
#
# `W-nn` → 腳本檔名：自 `scripts/` 掃其 docstring 首行之 `W-nn`。
def _writes_new_version(src: str) -> bool:
    """該腳本是否**產出新版檔**（`_v(n+1)`）—— 用以與原生成器區分。"""
    # 兩種寫法：**動態**（`_v{n+1}` 之組字）與**明列**（`("…_v4.json",
    # "…_v5.json")` 之對映表，如 `record_rewrite_w95.py`）。二者皆須認得。
    return bool(re.search(r"_v\{|\+ 1\}\.json|_v\d+\.json[\"']\s*\)", src)
                or re.search(r"_v\d+\.json[\"'],\s*[\"'][^\"']*_v\d+\.json", src))


def fixer_map() -> dict[str, str]:
    """`W-nn` → **修正腳本**檔名。

    一個 W 號可能出現在數支腳本之 docstring（如 `W-157` 見於
    `defect_scan_w157.py` 與 `earlyfix_w157.py`）——
    **取其中實際產出新版檔者**，掃描器（只讀不寫）不入表。
    """
    out: dict[str, str] = {}
    for p in sorted((FEAT / "scripts").glob("*.py")):
        src = p.read_text(encoding="utf-8")
        if not _writes_new_version(src):
            continue
        head = src[:400].split("\n\n")[0]
        for m in re.finditer(r"\bW-(\d+)\b", head):
            out.setdefault(f"W-{m.group(1)}", p.name)
    return out


FIXER_MAP = fixer_map()


FROZEN_NOTE = "**首版生成器未入庫；其產物以 sha256 凍結為基準**"


def frozen_point(stem: str) -> tuple[str, str, int]:
    """凍結點（86 包 §3）—— 該批**首版 JSON**，不在者取現存最早版。

    回傳（檔名, sha256, 其 TC 條數）。**取實檔**，不由版號推定。
    """
    vs = sorted(
        ((int(m.group(1) or 1), p) for p in GEN.glob(f"{stem}*.json")
         if (m := re.match(rf"{re.escape(stem)}(?:_v(\d+))?\.json$", p.name))),
        key=lambda x: x[0])
    if not vs:
        return "—", "—", 0
    p = vs[0][1]
    n = len(json.loads(p.read_text(encoding="utf-8"))["tcs"])
    return p.name, hashlib.sha256(p.read_bytes()).hexdigest(), n


def origin_of(stem: str) -> str:
    """原生成器 —— `scripts/{stem}_w*.py`。

    批 01–12 於本 repo **無此檔** —— 現存腳本中無任何一支產出其首版，
    只有其後之修正層。其回傳 `**缺**`，具名於表。
    """
    c = sorted((FEAT / "scripts").glob(f"{stem}_w*.py"))
    return c[0].name if c else "**缺**"


def chain(stem: str, origin: str = "") -> list[str]:
    """該批之修正層 —— 逐版讀其 `revision`，依版序累積。"""
    out, seen = [], set()
    vers = sorted(GEN.glob(f"{stem}.json")) + sorted(
        GEN.glob(f"{stem}_v*.json"),
        key=lambda p: int(re.search(r"_v(\d+)", p.name).group(1)))
    for p in vers:
        rev = str(json.loads(p.read_text(encoding="utf-8")).get("revision") or "")
        # **修正（59 輪 W-170）**：舊式為 `re.match(r"(W-\d+)", rev)` ——
        # 其**錨於字串首**，只取第一個標記。而一版之 `revision` 可被**追加**
        # 多個標記（48 輪之 D-3 即以 `；D-3（48 輪）：…` 追加於既有字串之後），
        # **該追加因而被靜默丟棄** —— A-VS162 之「鏈缺一層」實由此式所致，
        # 非由「未更新 revision」所致（其實已更新）。
        # 改為掃全串之 `W-nn` 與 `D-n（nn 輪）` 二式，依其出現序。
        marks = re.findall(r"W-\d+|D-\d+（\d+\s*輪）", rev)
        if not marks:
            continue
        # 首版之 `revision` 記的是**原生成器自己**之 W 號
        # （如 `batch13.json` 記 `W-100`，即 `batch13_w100.py`）——
        # 其已列於「原生成器」欄，不重複列為修正層。
        ow = re.search(r"_w(\d+)\.py$", origin)
        for mk in marks:
            # 首版之 `revision` 記原生成器自己之 W 號，其已列於「原生成器」欄
            if ow and f"W-{ow.group(1)}" == mk:
                continue
            # **不以標記形態推斷就地改動**（59 輪 W-170 之更正）——
            # `batch14_v2` 之首標記即 `D-4（38 輪）`，其為**該版之產出者**，
            # 非就地改動。就地改動須以 **git 之 commit 數**判定，見 `inplace()`。
            script = FIXER_MAP.get(mk, f"**{mk} 之腳本或作業不在 repo**")
            if script not in seen:
                seen.add(script)
                out.append(script)
    return out


def inplace() -> list[tuple[str, str, str]]:
    """**已入庫後被就地改動之版本檔**（R-VS80 所禁之形態）。

    判準為 **git 可驗者**：該檔之 commit 數 > 1 —— 即其入庫後另有 commit 改之。
    不以 `revision` 之標記形態推斷（該推斷於 `batch14_v2` 誤判）。
    回傳（檔名, 改動之 commit, 該次所改之欄位摘要）。
    """
    import subprocess
    out = []
    for f in sorted(GEN.glob("batch*.json")):
        rel = f.relative_to(FEAT.parents[1])
        cs = subprocess.run(["git", "log", "--format=%h", "--", str(rel)],
                            capture_output=True, text=True,
                            cwd=FEAT.parents[1]).stdout.split()[::-1]
        if len(cs) < 2:
            continue

        def load(rev):
            r = subprocess.run(["git", "show", f"{rev}:{rel}"], capture_output=True,
                               text=True, cwd=FEAT.parents[1])
            try:
                return json.loads(r.stdout)
            except Exception:
                return None

        for prev, cur in zip(cs, cs[1:]):
            a, b = load(prev), load(cur)
            if a is None or b is None:
                continue
            ta = {t["leaf_id"]: t for t in a["tcs"]}
            tb = {t["leaf_id"]: t for t in b["tcs"]}
            fields = {}
            for k in set(ta) & set(tb):
                for fld in set(ta[k]) | set(tb[k]):
                    if ta[k].get(fld) != tb[k].get(fld):
                        fields[fld] = fields.get(fld, 0) + 1
            if fields:
                out.append((f.name, cur, "／".join(
                    f"`{k}` {v}" for k, v in sorted(fields.items(), key=lambda x: -x[1]))))
    return out


def main() -> None:
    L = ["# `REGEN_ORDER.md` —— 各批之重製順序（W-161，56 輪）\n",
         "依 `docs/handoff/84_delivery.md` §4 之裁定。\n",
         "**R-VS53 之弱化，具名於此**：早批之產物**不可自單一 driver 重製** ——",
         "`batchNN_vM.json` 為「原生成器之輸出 ＋ 依序疊加之修正腳本」。",
         "重製須**按下表之順序**執行，跳過任一層其結果即不同。\n",
         "**分析層／稽核之可重現性由此鏈滿足，非由單一 driver 滿足。**\n",
         "| 批 | 原生成器 | 修正層（依序） | 層 | 現行版本 | sha256（前 16） | 凍結點 | `frozen_sha256`（前 16） |",
         "|---|---|---|---:|---|---|---|---|"]
    longest, worst, missing = 0, "", []
    for f in latest_batches():
        # **須用與 `latest_batches()` 相同之完整式**：無尾錨之
        # `(batch\d+(?:_[a-z]+)?)` 會把 `batch01_v9.json` 切成 `batch01_v`
        # （`_[a-z]+` 貪婪吃掉 `_v`，而無後續 pattern 迫其回溯）。
        stem = re.match(r"(batch\d+(?:_[a-z]+)?)(?:_v(\d+))?\.json$",
                        f.name).group(1)
        ch = chain(stem)
        if len(ch) > longest:
            longest, worst = len(ch), stem
        h = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        org = origin_of(stem)
        ch = chain(stem, org)
        fz_name, fz_hash, fz_n = frozen_point(stem)
        if org == "**缺**":
            missing.append((stem, fz_name, fz_hash, fz_n))
            org = FROZEN_NOTE
            frozen_cols = f" | `{fz_name}` | `{fz_hash[:16]}` |"
        else:
            frozen_cols = " | — | — |"
        L.append(f"| `{stem}` | " + (org if org == "**缺**" else f"`{org}`") + " | "
                 + (" → ".join(f"`{c}`" for c in ch) if ch else "—")
                 + f" | {len(ch)} | `{f.name}` | `{h}`" + frozen_cols)
    L += ["",
          f"**鏈長最長者：`{worst}`，{longest} 層。**",
          "",
          f"### 原生成器未入庫者 —— **{len(missing)} 批**，"
          f"其 R-VS53 以**雜湊凍結**滿足（86 包 §3）",
          "",
          "| 批 | 凍結點（現存最早版） | 其 TC | `frozen_sha256` |",
          "|---|---|---:|---|"]
    for stem, fz_name, fz_hash, fz_n in missing:
        L.append(f"| `{stem}` | `{fz_name}` | {fz_n} | `{fz_hash}` |")
    L += [f"| **合計** | | **{sum(x[3] for x in missing)}** | |",
          "",
          "**其意涵**（86 包 §3，須具名不得以「可重製」一語涵蓋）：",
          "",
          f"　該 {len(missing)} 批（**{sum(x[3] for x in missing)} 條**）之"
          "**首版生成過程不可重放** —— 現存腳本中無任何一支寫出其首版。",
          "　其後之**每一層修正皆有腳本且順序已記於上表**，故其變更歷程可稽核。",
          "",
          "　**可稽核之範圍為「自凍結點起之變更」，非「自需求起之產出」。**",
          f"升級門檻為「> 3 則重製之可行性須另議」——"
          f"{'**逾**' if longest > 3 else '**未逾**'}。\n",
          "## 重製之執行順序\n",
          "```",
          "cd features/vehicle_setting",
          "python3 scripts/<原生成器>.py          # 產 batchNN.json",
          "python3 scripts/<修正層 1>.py          # 產 batchNN_v2.json",
          "python3 scripts/<修正層 2>.py          # 產 batchNN_v3.json …",
          "```\n",
          "**各修正腳本皆掃全母體並自產下一版**，故其執行為「跑一次即處理所有批」，",
          "非逐批呼叫。上表之「修正層」為該批**實際被觸及**之層。\n",
          "## 驗證\n",
          "```",
          "python3 scripts/selfcheck_w53.py generated/<現行版本>   # §9 十七項",
          "python3 scripts/selfcheck_anchored.py                   # 固定錨點 20 項",
          "python3 scripts/defect_scan_w157.py                     # 五項 defect",
          "python3 scripts/backscan_w160.py                        # R-VS77 全母體回掃",
          "python3 scripts/completeness_w154.py                    # R-VS76 完整性",
          "```"]
    ip = inplace()
    L += ["", "### ⚠ 已入庫後之**就地改動**（R-VS80 所禁；A-VS162）",
          "",
          "判準為 **git 可驗者**：該版本檔之 commit 數 > 1，"
          "即其入庫後另有 commit 改其內容。",
          "**不以 `revision` 之標記推斷** —— `batch14_v2` 之首標記為 "
          "`D-4（38 輪）`，其為該版之產出者而非就地改動。",
          "",
          "| 版本檔 | 改動之 commit | 所改之欄位（條數） |",
          "|---|---|---|"]
    for n, c, f in ip:
        L.append(f"| `{n}` | `{c}` | {f} |")
    L += [f"| **合計** | **{len({c for _, c, _ in ip})} 個 commit** "
          f"／ **{len(ip)} 檔次** | |",
          "",
          "**該層皆不在鏈上** —— 其無腳本，亦不產新版；",
          "**其記錄僅存於上表之 git commit**。若該次未入庫，其缺口即永久不可見。",
          "",
          "**48 輪之就地改動（A-VS162）—— 其手段不可考，"
          "以 git commit `100d1e0` 為其記錄。**"]
    p = FEAT / "docs/reports/REGEN_ORDER.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print(f"{p} —— 鏈長最長 {longest} 層（`{worst}`）")


if __name__ == "__main__":
    main()
