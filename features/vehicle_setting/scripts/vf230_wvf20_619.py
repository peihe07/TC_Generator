"""W-VF20 —— 以 619 為母體之既有陳述之逐句判別（V07 §6.4；**只判不改**）。

依 **R-VF18**：

  不改  作成當時為正確量測之歷史紀錄 —— 上繳包、已結案之報告、
        條文中引為理由之當時實測值
  須改  現行有效之陳述 —— 後續作業會據以行動者

**判斷須逐句為之，不得以檔為單位整批處理**（R-VF18）。故本腳本之判別
以**每一行之文字**為輸入，規則明列於 `classify()`，每筆附理由；
規則無法決斷者標 `待人工`，不臆測。

依 **R-VF11／R-VF21** 附錨點：
  必為「不改」  `docs/upstream/vf230/00_intake.md` 之任一行（已上繳之歷史紀錄）
  必為「不改」  `feature.yaml` 內含 `388/619` 之行 —— **逐行覆寫之標的**，
                其位於現行有效之設定檔而判為歷史紀錄，
                本錨點證明逐行覆寫確有生效（若覆寫失效，其將判為「須改」）

**R-VF22 施行後之預期為「須改 0」**：原判出之 2 處
（`feature.yaml:29`、`vf230_layer2.py:113`）已改為 627，不再含 `619`。
**首版之必為「須改」錨點指向 `feature.yaml:29`，於 R-VF22 施行後即失效而停** ——
此為 R-VF21 第 1 項（存在性先驗）之正面作用：錨點察覺其所指之行已不存在。

輸出：docs/reports/wvf20_619_triage.md ＋ data/_wvf20_619.json
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 「須改」之判準：現行有效之陳述所在
LIVE_FILES = ("feature.yaml", "PLAYBOOK.md", "RUNBOOK.md", "framework.md")
# 對照式書寫（`619 → 627`／`619 版`／`619 或 627`）為變更之紀錄本身，一律不改
CONTRAST = re.compile(r"619\s*(→|->|版|或)|（619\s*[＋+]|619\s*[＋+]\s*8")


# R-VF18 明言「同一檔內可能兼有兩類」，故逐行覆寫優先於逐檔規則。
# 覆寫須逐筆附理由，且列於報告，不得隱形。
# 鍵為 (檔, 內容片段) 而非 (檔, 行號) —— 行號會被同檔他處之編輯位移：
# R-VF22 改 `feature.yaml:29` 後，本覆寫之標的自 118 移至 119，
# 首版之行號鍵即失配。**位置型鍵不穩定，內容型鍵才是識別。**
OVERRIDE = {
    ("feature.yaml", "388/619"): (
        "不改",
        "此行為 **當時之 Sub Categorization 實測**（388/619），"
        "非後續作業據以行動之設定值 —— 其所支持之判定（Test Group）"
        "已由 R-VF9 裁定，本行僅存為裁定當時之證據。"
        "雖位於現行有效之 `feature.yaml`，依 R-VF18「逐句為之」判為歷史紀錄。"),
}


def classify(f: str, text: str) -> tuple[str, str]:
    if f.startswith("docs/handoff/"):
        return "不改", "下放包 —— 作成當時之指示與量測，改之使「當時據何而裁」不可考"
    if f.startswith("docs/upstream/"):
        return "不改", "上繳包 —— 已提交之歷史紀錄"
    if CONTRAST.search(text):
        return "不改", "對照式書寫（619→627／619 版／619＋8）—— 其為變更之紀錄本身"
    if f in LIVE_FILES:
        return "須改", "現行有效之設定／作業文件，後續作業據以行動"
    if f.startswith("docs/reports/"):
        return "不改", "已結案之報告 —— 作成當時之正確量測"
    if f == "RULINGS.md":
        return "不改", "條文中引為理由之當時實測值"
    if f == "ANOMALIES.md" or f == "DATA_REQUESTS.md":
        return "不改", "登記簿 —— 記錄開立當時之事實"
    if f.startswith("scripts/"):
        # 逐行分辨：可執行之常數／斷言 vs docstring 或輸出字串之敘述。
        code = not text.lstrip().startswith(("#", '"', "'", "f\"", "f'", "*", "`"))
        if code and re.search(r"(==|=|<|>)\s*619\b", text):
            return "須改", "腳本內之可執行常數／斷言 —— 現行行為據以判定"
        return "不改", ("腳本之 docstring 或輸出字串 —— 敘述當時之量測，"
                        "非現行行為所依")
    return "待人工", "規則未涵蓋"


def main() -> None:
    out = subprocess.run(
        # 詞界必要：`data/lid_pairs.tsv` 有 `1619`／`2619`／列號 619，
        # 皆與 leaf 母體無關。首版未加詞界，混入 4 筆偽陽性。
        ["grep", "-rnE", r"\b619\b", "--include=*.md", "--include=*.py",
         "--include=*.yaml", "."],
        capture_output=True, text=True, cwd=ROOT).stdout

    rows = []
    for ln in out.splitlines():
        m = re.match(r"^\./([^:]+):(\d+):(.*)$", ln)
        if not m:
            continue
        f, n, txt = m.group(1), int(m.group(2)), m.group(3).strip()
        if f == "data/vf230_leaves.tsv":
            continue          # 產物本身，已為 627
        if f.endswith("vf230_wvf20_619.py"):
            continue          # 本腳本自身之敘述，非受判標的
        ov = next((v for (of, frag), v in OVERRIDE.items()
                   if of == f and frag in txt), None)
        verdict, why = ov or classify(f, txt)
        rows.append({"file": f, "line": n, "text": txt[:160],
                     "verdict": verdict, "why": why})

    # --- R-VF11 錨點 ---
    a_ovr = next((r for r in rows
                  if r["file"] == "feature.yaml" and "388/619" in r["text"]), None)
    a_hist = next((r for r in rows if r["file"].startswith("docs/upstream/vf230/")), None)
    if a_ovr is None or a_hist is None:
        raise SystemExit("R-VF21(1)：錨點所指之行不存在，停 "
                         f"（覆寫錨點={a_ovr is not None}／歷史錨點={a_hist is not None}）")
    if a_ovr["verdict"] != "不改" or a_hist["verdict"] != "不改":
        raise SystemExit(f"R-VF11 錨點不符，停："
                         f"{a_ovr['verdict']} / {a_hist['verdict']}")

    n_live = [r for r in rows if r["verdict"] == "須改"]
    n_hist = [r for r in rows if r["verdict"] == "不改"]
    n_man = [r for r in rows if r["verdict"] == "待人工"]

    L = ["# W-VF20 —— 以 619 為母體之陳述之逐句判別（R-VF18）", "",
         "**V07 §6.4 之工單。只判不改。**", "",
         "## 0. 錨點（R-VF11）", "",
         "| 錨點 | 位置 | 判別 |", "|---|---|---|",
         f"| 必為「不改」（逐行覆寫之標的） | `feature.yaml:{a_ovr['line']}`"
         f"（含 `388/619`） | {a_ovr['verdict']} |",
         f"| 必為「不改」（已上繳之歷史紀錄） | `{a_hist['file']}:{a_hist['line']}` | {a_hist['verdict']} |",
         "", "**錨點皆符。**", "",
         "> **R-VF22 施行後，「須改」應為 0** —— 原判出之 2 處已改為 627。",
         "> 首版之必為「須改」錨點指向 `feature.yaml:29`，於 R-VF22 施行後",
         "> 即因該行不再含 `619` 而停 —— **R-VF21 第 1 項之正面作用**。", "",
         "## 1. 判別規則（明列，逐行套用）", "",
         "| 條件 | 判別 | 依 R-VF18 之理由 |", "|---|---|---|",
         "| 位於 `docs/handoff/` | 不改 | 下放包，作成當時之指示與量測 |",
         "| 位於 `docs/upstream/` | 不改 | 上繳包，已提交之歷史紀錄 |",
         "| 文字為對照式（`619 → 627`／`619 版`／`619 或 627`／`619 ＋ 8`） | 不改 | "
         "其為變更之紀錄本身，改之即抹除變更 |",
         f"| 位於 {'／'.join(f'`{x}`' for x in LIVE_FILES)} | **須改** | "
         "現行有效之設定／作業文件 |",
         "| 位於 `docs/reports/` | 不改 | 已結案之報告 |",
         "| `RULINGS.md` | 不改 | 條文中引為理由之當時實測值 |",
         "| `ANOMALIES.md`／`DATA_REQUESTS.md` | 不改 | 登記簿，記錄開立當時之事實 |",
         "| `scripts/` 且該行為可執行之常數／斷言 | **須改** | 現行行為據以判定 |",
         "| `scripts/` 之 docstring 或輸出字串 | 不改 | 敘述當時之量測 |",
         "",
         "**逐行覆寫**（R-VF18：同一檔內可能兼有兩類，判斷須逐句為之）：", "",
         "| 檔:行 | 覆寫為 | 理由 |", "|---|---|---|"]
    for (of, ofrag), (ov, ow) in OVERRIDE.items():
        L.append(f"| `{of}` 含 `{ofrag}` 之行 | {ov} | {ow} |")
    L += ["",
         f"## 2. 結果：{len(rows)} 處 ／ {len({r['file'] for r in rows})} 檔", "",
         f"- **須改 {len(n_live)}**",
         f"- **不改 {len(n_hist)}**",
         f"- **待人工 {len(n_man)}**", ""]

    if n_live:
        L += ["### 2.1 須改（現行有效之陳述）", "",
              "| 檔:行 | 逐字 | 理由 |", "|---|---|---|"]
        for r in n_live:
            L.append(f"| `{r['file']}:{r['line']}` | `{r['text']}` | {r['why']} |")
        L += ["", "**本輪未改**（V07 §6.4：只判不改，改動清單待分析層核可）。", ""]

    if n_man:
        L += ["### 2.2 待人工（規則不決斷）", "",
              "| 檔:行 | 逐字 |", "|---|---|"]
        for r in n_man:
            L.append(f"| `{r['file']}:{r['line']}` | `{r['text']}` |")
        L += [""]

    L += ["### 2.3 不改（逐檔計數）", "", "| 檔 | 處 |", "|---|---:|"]
    cnt: dict[str, int] = {}
    for r in n_hist:
        cnt[r["file"]] = cnt.get(r["file"], 0) + 1
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        L.append(f"| `{k}` | {v} |")

    L += ["", "## 3. 留痕（R-VF18 末段：改與不改皆須留痕）", "",
          f"本表即為留痕。**{len(n_hist)} 處判「不改」者，其理由逐條見 §1 之規則**；",
          f"**{len(n_live)} 處判「須改」者逐處列於 §2.1，本輪未改。**", ""]

    out_p = ROOT / "docs" / "reports" / "wvf20_619_triage.md"
    out_p.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf20_619.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{len(rows)} 處／{len({r['file'] for r in rows})} 檔")
    print(f"須改 {len(n_live)}／不改 {len(n_hist)}／待人工 {len(n_man)}")
    for r in n_live:
        print(f"  須改  {r['file']}:{r['line']}  {r['text'][:70]}")
    for r in n_man:
        print(f"  待人工 {r['file']}:{r['line']}  {r['text'][:70]}")
    print(f"wrote {out_p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
