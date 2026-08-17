# 01 下放包 — User Profiles Phase 0 intake

同輪：`01a_rulings.md`（裁決條文）、`01b_tasks.md`（作業指示）

## 素材

- 037：`FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`
- spec：`SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_(February_10_2023).xlsx`
- 036 母本：`forms/…_SWQT_20260817_ext.xlsx`（R-G1）

## 實測（2026-08-17，沙箱唯讀探測；欄位以 Analysis Report 欄序計）

- 表頭列 7；資料列 207（A 欄非空）
- Categorization：Functional Requirement 180 / Heading 25 / Out of scope 2
- 葉節點（ID 非任何其他 ID 之前綴）182；生成母體 180（R-U4 排除 2）
- SWE1-HMI-PROF-001～135；Source Requirement ID 唯一值 135
- FROP 欄 182 列全為 `User Profiles`
- Sub Categorization：HMI 160 / Service 22
- 037 Priority：High 79 / Medium 75 / Low 28
- 引用之唯一 HMI Source ID 135 個，全數存在於 spec，缺漏 0
- spec work items 169；未被 037 引用 34（純章節標題 11、ch1 12、ch2 2、ch3 6、10.1／11.1／11.2 3）
- 被引 135 條正文長度中位數 193 字元、最短 65、最長 728；含圖片參照 14 條，扣圖後正文 < 40 字者 0 → spec_mode A，不需 OCR
- spec 全文唯一 PU id 20 個

## 章節骨架（Layer 3 起點）

1 Assumptions｜2 Reference Documentation｜3 Profile Linked Preferences｜
4 Profile Overview｜5 All Profiles Tab｜6 Default Profiles - No Custom Profiles｜
7 Welcome Screen (Custom Profile)｜8 New Profile Setup｜9 Editing a Profile｜
10 Profile Info Page｜11 Connected Profile App｜12 Valet Mode｜
13 Valet Mode - SPAAK｜14 Valet Mode - Exit

葉節點章節分布：4:29　5:41　6:11　7:14　8:25　9:22　10:3　11:6　12:25　13:4　14:2

## Anomalies

- **A-UP01 RESOLVED** — 初次附上之 SYS1 為 Personal Assistant（Siri）誤件；正確 spec 已補入並通過覆蓋驗證。
- **A-UP02 PENDING** — spec 3.1–3.5（PLP1–PLP5）、10.1、11.1、11.2 共 8 條實質條文無任何 SWE 需求覆蓋，其中 PROF-001-01 之 Verification Criteria 本身即引用 PLP 表。RD-1 候選；依 §8.4.2 不得自行吸收進 TC。
- **A-UP03 PENDING** — `FORMS.md` 之 `20260816_ext` 條目已與磁碟脫鉤：manifest 記 123,717 bytes／SHA256 `6d53056e…`，實測 200,654 bytes、mtime 2026-08-17 09:45:54。
