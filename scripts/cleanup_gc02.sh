#!/usr/bin/env bash
# Pei 專門 commit 用（R-G65：改動連同其母體一併引用；R-G47：lint 報告歸位）。
# 由 GC-02 §一-4 產生、GC-03 §二-4 加註，執行層**未執行**。每行一 pathspec（R-G51）。
# 依據：docs/reports/lint_reports_refs_20260905.tsv（106 列，GC-01 §二-3）
#   removable=Y 81 檔 → git rm；removable=N 25 檔留，
#   其中 sw_update 相關且非 0821 基線者 2 檔 → git mv 至 features/sw_update/reports/。
# 跑之前：git status 應乾淨；跑之後：git commit 只帶本腳本所動之 pathspec。
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# --- 一、移除無任何指名者（81 檔，basis=NO_REF）---
git rm -- "docs/fw036/lint_reports/BedLowering_efa1da4c_20260829.md"
git rm -- "docs/fw036/lint_reports/Comfort_235f2ca7_20260829.md"
git rm -- "docs/fw036/lint_reports/Comfort_6d53056e_20260829.md"
git rm -- "docs/fw036/lint_reports/Comfort_b68117a2_20260829.md"
git rm -- "docs/fw036/lint_reports/Display_06972455_20260829.md"
git rm -- "docs/fw036/lint_reports/Display__display_06972455_20260827.md"
git rm -- "docs/fw036/lint_reports/Popup_a13559d5_20260829.md"
git rm -- "docs/fw036/lint_reports/PowerModing_01e917b8_20260829.md"
git rm -- "docs/fw036/lint_reports/PowerModing_070ef73c_20260829.md"
git rm -- "docs/fw036/lint_reports/PowerModing_8f471ddf_20260829.md"
git rm -- "docs/fw036/lint_reports/Privacy_ad595ed0_20260829.md"
git rm -- "docs/fw036/lint_reports/Privacy_ed741d8d_20260829.md"
git rm -- "docs/fw036/lint_reports/SWUpdate_EMPTY_3d439541_20260829.md"
git rm -- "docs/fw036/lint_reports/SWUpdate__sw_update_4f6caa35_20260830.md"
git rm -- "docs/fw036/lint_reports/SXM_0b9cb4f6_20260829.md"
git rm -- "docs/fw036/lint_reports/UserProfiles_0e40ff5b_20260829.md"
git rm -- "docs/fw036/lint_reports/UserProfiles_570eb7cd_20260829.md"
git rm -- "docs/fw036/lint_reports/UserProfiles_cbd04af6_20260829.md"
git rm -- "docs/fw036/lint_reports/VehicleCategory_c470defd_20260829.md"
git rm -- "docs/fw036/lint_reports/driver_distraction_00__driver_distraction_f5a16c7b_20260829.md"
git rm -- "docs/fw036/lint_reports/prepared_step1_cleared_b68117a2_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_032c2cd3_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_05e330dd_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_086e471c_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_0a66e037_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_1324e85f_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_201bfeb0_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_20902564_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_26341ffe_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_26407fb9_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_2a956804_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_2ea0cf03_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_32391150_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_34253730_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_36593403_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_3bf20ab4_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_40ecacdb_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_45da648e_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_4b398976_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_4c6ca79c_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_528f56ed_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_52ae3b17_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_57f80b7c_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_5a881012_20260828.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_5b1e785c_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_5caa4794_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_663d8b02_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_6af353ee_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_6d907b29_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_711a5854_20260828.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_7bab8660_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_7c5e94c3_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_7efbc509_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_81afdf7f_20260828.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_8a78b9e6_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_8d4aa2ca_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_8ee0c46a_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_904998e5_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_93320f41_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_aadfb087_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_ab27fcce_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_ab9415bb_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_abbe7b95_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_ad131475_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_b164dc6a_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_bc66d5b5_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_bff1d63b_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_c349aefd_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_c94963b8_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_cc5ac549_20260828.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_ce2aa160_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_d3dde30c_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_da955241_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_e06d54b8_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_e0daffc0_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_f00f2a75_20260829.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_f41e1abb_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_f8eaca24_20260828.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_faaeeea9_20260830.md"
git rm -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_ff976761_20260829.md"
git rm -- "docs/fw036/lint_reports/time_management_20260825_717d48d8_20260829.md"

# --- 二、sw_update 之報告歸位（2 檔，R-G47：feature 級落 features/<f>/reports/）---
#     每筆之上一行 `# was: <old> ; referenced by: <file>` 即路徑遷移對照
#     （GC-02 審閱 §二-3：歷史檔不追改，對照就地入腳本，不另出檔）。
test -d features/sw_update/reports || mkdir -p features/sw_update/reports
# was: docs/fw036/lint_reports/SWUpdate__sw_update_7f019b37_20260830.md ; referenced by: docs/fw036/upstream/72_delivery.md
git mv -- "docs/fw036/lint_reports/SWUpdate__sw_update_7f019b37_20260830.md" "features/sw_update/reports/SWUpdate__sw_update_7f019b37_20260830.md"
# was: docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_a3633876_20260828.md ; referenced by: features/sw_update/docs/upstream/25_batch1_review.md
git mv -- "docs/fw036/lint_reports/sw_update_20260817_ext__sw_update_a3633876_20260828.md" "features/sw_update/reports/sw_update_20260817_ext__sw_update_a3633876_20260828.md"

# --- 三、留於 lint_reports/ 者（23 檔，不動）---
#   AMFM_20260821.json  [FROZEN_BASELINE(R-G47)]
#   AMFM_20260821.md  [FROZEN_BASELINE(R-G47)]
#   BT_20260821.json  [FROZEN_BASELINE(R-G47)]
#   BT_20260821.md  [FROZEN_BASELINE(R-G47)]
#   CFTS012_DealerMode_20260821.json  [FROZEN_BASELINE(R-G47)]
#   CFTS012_DealerMode_20260821.md  [FROZEN_BASELINE(R-G47)]
#   CFTS026_HandsFreePhone_20260821.json  [FROZEN_BASELINE(R-G47)]
#   CFTS026_HandsFreePhone_20260821.md  [FROZEN_BASELINE(R-G47)]
#   Home_20260821.json  [FROZEN_BASELINE(R-G47)]
#   Home_20260821.md  [FROZEN_BASELINE(R-G47)]
#   MediaHMI_20260821.json  [FROZEN_BASELINE(R-G47)]
#   MediaHMI_20260821.md  [FROZEN_BASELINE(R-G47)]
#   PowerManagement_20260821.json  [FROZEN_BASELINE(R-G47)]
#   PowerManagement_20260821.md  [FROZEN_BASELINE(R-G47)]
#   Projection_20260821.json  [FROZEN_BASELINE(R-G47)]
#   Projection_20260821.md  [FROZEN_BASELINE(R-G47)]
#   pm_25__power_20260824.md  [REFERENCED]
#   pm_26__power_20260824.md  [REFERENCED]
#   pm_27__power_20260824.md  [REFERENCED]
#   pm_28__power_20260824.md  [REFERENCED]
#   pm_29_35305835_20260829.md  [FROZEN_BASELINE(R-G47)]
#   pm_29__power_35305835_20260824.json  [FROZEN_BASELINE(R-G47)]
#   pm_29__power_35305835_20260824.md  [FROZEN_BASELINE(R-G47)]

echo "cleanup_gc02: 81 removed, 2 moved, 23 kept"
