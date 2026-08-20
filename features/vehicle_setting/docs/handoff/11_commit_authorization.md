# 11 下放包 — P2 入庫之窄口授權與指令

分析層寫入，2026-08-20。

```
R-VS22（Pei 2026-08-20，窄口授權，一次性）
R-G5「全部 git 操作屬 Pei」於本次入庫作業開一個窄口：

得執行：git status / git diff / git check-ignore / git ls-files（唯讀）
        git add（限下列 pathspec）
        git commit（限本次，訊息如指令所載）

不得執行：push / amend / rebase / reset / restore / checkout / branch /
          tag / stash / clean / merge / cherry-pick / rm / mv
          —— 其中 push 為不可逆，其餘為改寫既有狀態，皆仍屬 Pei。

pathspec 限於 features/vehicle_setting/ 之下；出現任何該路徑以外之
變更被暫存，即為異常，停下回報。

本授權於本次 commit 完成後失效，不延伸至後續輪次。
理由：commit 為本地且可逆（git reset），push 不可逆 ——
風險界線劃在 push 而非 commit。
```

指令見 §2；`_cfts_values*.json` 之處置須 Pei 於指令首行填答（版控範圍屬 Pei）。
