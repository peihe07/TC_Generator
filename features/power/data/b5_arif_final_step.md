# B5 —— Arif 144 列 done region 之末步素材（15 §B5）

> **本檔僅為裁定素材。Q3 屬 Pei 之裁定，執行層未據此改動 G77 或任何 TC。**

> 母體檔：`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Home_20260809.xlsx`
> SHA256：`42d9544eed7127f9fe912588715b144d9f2f3412d9e961efe450cc03da15551f`
> 選取器：Z 欄（Author）== `ArifChen`；母體列數 assertion **144 == 144** PASS
> `read_only=True`，**未呼叫 `save()`**。
> 產生指令：`python features/power/scripts/build_arif_final_step.py`

## 1. 母體

 done region **144** 列，其中 `test_procedure` 非空且可拆出末步者 **144** 條。

## 2. 驗證意圖措詞之命中

| 詞 | Arif 末步命中 | 佔比 |
|---|---|---|
| `check` | **77** | 53.5% |
| `verify` | **0** | 0.0% |
| `confirm` | **0** | 0.0% |
| `ensure` | **0** | 0.0% |
| `validate` | **0** | 0.0% |
| `observe` | **0** | 0.0% |
| `read` | **0** | 0.0% |
| `count` | **0** | 0.0% |
| `wait` | **0** | 0.0% |
| `compare` | **0** | 0.0% |
| `measure` | **0** | 0.0% |

**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）命中 18 / 144（12.5%）。**

## 3. 三個母體之並列比較

| 母體 | 末步條數 | §5.2B 措詞命中 | 佔比 |
|---|---|---|---|
| **Arif done region（Home）** | 144 | **18** | 12.5% |
| Comfort + Privacy 已交付（14 包 B4） | 472 | **0** | 0.0% |

## 4. Arif 末步之行首動詞（前 10）

| 動詞 | 次數 | 佔比 |
|---|---|---|
| `check` | 77 | 53.5% |
| `pres` | 35 | 24.3% |
| `select` | 28 | 19.4% |
| `drag` | 3 | 2.1% |
| `swipe` | 1 | 0.7% |

## 4.1 典型措詞形態（前 10 種，取前三字）

| 形態 | 次數 |
|---|---|
| `Select "Add Page"` | 8 |
| `Check the Home` | 8 |
| `Press the greyed` | 7 |
| `Check the default` | 6 |
| `Check the popup` | 6 |
| `Check the order` | 6 |
| `Press "X" button` | 5 |
| `Check the state` | 5 |
| `Check the pagination` | 4 |
| `Check that the` | 3 |

**關鍵區別（供裁定）**：`check` 出現於 **77 / 144（53.5%）**，其中 **77** 條以 `Check` 起首 —— 即驗證意圖確為 Arif 之慣例。
惟 §5.2B 所列之**完整措詞**（`check that` / `to check` / `and check`）僅命中 **18（12.5%）** —— 多數為祈使句 `Check the ...`，非 `check that ...`。
**現行 G77 之正則要求完整措詞，故對 Arif 之 59 條祈使式末步亦會判 FAIL。**
此點為素材，**執行層未據以改動 G77**（15 §I）。

## 5. Arif 末步全文（144 條，逐條列出，不節錄）

1. Check the default widget content displayed on the Home Screen.
2. Check the default widget content displayed on the Home Screen.
3. Check the default widget content displayed on the Home Screen.
4. Check the default widget content displayed on the Home Screen.
5. Check the default widget content displayed in each widget area.
6. Check the default widget content displayed in each widget area.
7. Press the edit pencil icon on the widget to enter Edit Widget page
8. Check the edit pencil icons on the Home Screen widgets.
9. Check that text "Select a Widget" is displayed **[含 §5.2B 措詞]**
10. Select a widget content type
11. Check that home screen widget with selected content is displayed **[含 §5.2B 措詞]**
12. Check that widget content cannot be duplicated on the same Home screen page **[含 §5.2B 措詞]**
13. Check that the content of the two widgets are swapped places. **[含 §5.2B 措詞]**
14. Check the source of the Media widget on the all pages.
15. Check the source of the Media widget
16. Check there is a preview of the widget area being edited in the edit widget content screen
17. Check the Navigation widget is disabled for the second page.
18. Press the full screen icon on the Media widget.
19. Press the widget text title (if available) on the Media widget.
20. Check that Edit Pages button is not displayed on Home screen with a vertical menu bar **[含 §5.2B 措詞]**
21. Check the displayed options to manage pages
22. Check that Edit Pages button is displayed on Home screen with a horizontal menu bar **[含 §5.2B 措詞]**
23. Check the options on Edit Pages menu.
24. Press the last pagination icon to open home screen management page
25. Check that options are greyed out and unavailable **[含 §5.2B 措詞]**
26. Check that "Edit Pages" button is greyed out and unavailable **[含 §5.2B 措詞]**
27. Press a greyed out option button
28. Press "OK" button to close the popup
29. Press "X" button to close the popup
30. Press a greyed out "Edit Pages" button
31. Press "OK" button to close the popup
32. Press "X" button to close the popup
33. Check that Reorder Pages is locked out when vehicle speed above the threshold. **[含 §5.2B 措詞]**
34. Check that Reorder Pages is locked out when vehicle speed above the threshold. **[含 §5.2B 措詞]**
35. Check that the page order changes are not saved. **[含 §5.2B 措詞]**
36. Check that the page order changes are not saved. **[含 §5.2B 措詞]**
37. Check the state of the "Delete Pages" and "Reorder Pages" options.
38. Check the state of the "Delete Current Page" and "Reorder Pages" options.
39. Press the greyed out "Delete Pages" option
40. Press the greyed out "Reorder Pages" option
41. Press the greyed out "Delete Current Page" option
42. Press the greyed out "Reorder Pages" option
43. Select "Add Page" button
44. Select "Add Page" button
45. Select "Add Page" button
46. Select "Add Page" button
47. Select a layout on the layout selection screen
48. Select a layout on the layout selection screen
49. Check the popup displayed after the page is added.
50. Check the popup displayed after the page is added.
51. Check the popup displayed after the page is added.
52. Check the popup displayed after the page is added.
53. Press and hold a Home Screen page in the view.
54. Press and hold a Home Screen page in the view.
55. Select "Add Page" button to add a page
56. Select "Add Page" button to add a page
57. Check the blank widget interface.
58. Select anywhere within the blank widget.
59. Check the blank widget interface.
60. Press the greyed out blank widget
61. Press the greyed out blank widget
62. Press "OK" button to close the popup
63. Press "X" button to close the popup
64. Select "Add Page" button
65. Check the state of the "Add Page" button
66. Select "Add Page" button
67. Check the state of the "Add Page" button
68. Select the greyed out "Add Page" button
69. Press "X" button to close the popup
70. Select the greyed out "Add Page" button
71. Press "X" button to close the popup
72. Check the pagination dots displayed on the Home Screen.
73. Check the pagination dots displayed on the Home Screen.
74. Check the pagination dots not displayed on the Home Screen.
75. Check the pagination dots displayed on the Home Screen.
76. Press another individual pagination dot
77. Press the "X" on the layout selection screen
78. Swipe left and right to view different Home Screen pages.
79. Select "X" or trashcan symbol to delete the page
80. Select "Delete Current Page" button
81. Select "Delete Current Page" button
82. Select "Delete Current Page" button
83. Check the popup displayed after the page is deleted.
84. Check the popup displayed after the page is deleted.
85. Select "Undo" button on the popup.
86. Select "Undo" button on the popup.
87. Select "Done" button
88. Select "Cancel" button
89. Select "Reorder Pages" button
90. Select "Reorder Pages" button
91. Check the order of the Home Screen pages
92. Check the order of the Home Screen pages
93. Check the text displayed on the Reorder Pages screen.
94. Check the text displayed on the Reorder Pages screen.
95. Check the Home Screen pages order
96. Check the Home Screen pages order
97. Check the Home Screen pages order
98. Check the Home Screen pages order
99. Check the Home Screen pages order
100. Check the Home Screen pages order
101. Check the Home Screen pages order
102. Check the Home Screen pages order
103. Check the order of the Home Screen pages
104. Check the order of the Home Screen pages
105. Check the order of the Home Screen pages
106. Check the order of the Home Screen pages
107. Drag the widget over another widget
108. Drag the 50% widget over a 25% widget size
109. Drag the 25% widget over a 50% widget size
110. Check the 25% Shortcuts widget content
111. Check the 50% Shortcuts widget content
112. Check that widget content displayed normally **[含 §5.2B 措詞]**
113. Check that loading widget screen displayed on widget content for a minimum of 2 seconds **[含 §5.2B 措詞]**
114. Check the Select a Widget screen for the downloaded app widget
115. Check the Select a Widget screen for heated/vented seats, heated wheel, and comfort
116. Check the shortcut selection menu for heated/vented seats, heated wheel, and comfort
117. Check the content and text for available widgets which based on vehicle configuration, screen size and radio type
118. Select the "Remove Widget" button
119. Check widget logic and layout on a 25% widget
120. Check widget logic and layout on a 50% widget
121. Check the widgets title matches the text string defined in corresponding Feature Specs
122. Press "+" button on the Shortcuts Widget
123. Check that available shortcuts are dependent on vehicle configuration **[含 §5.2B 措詞]**
124. Press "Controls" button
125. Check  "Controls" category
126. Press "Make a Call" button
127. Press "Set a Route" button
128. Press "Media" button
129. Press "Seats & Wheel" button
130. Press "Seats" button
131. Check "Seats & Wheel" category
132. Press "Apps" button
133. Select the AA source button on shortcut selection menu
134. Select the CP source button on shortcut selection menu
135. Check that AA source option is not displayed **[含 §5.2B 措詞]**
136. Check that CP source option is not displayed **[含 §5.2B 措詞]**
137. Check the shortcut icon in the Shortcut Widget
138. Check the shortcut icon in the Shortcut Widget
139. Check the state of the "plus" button on the Shortcut widget.
140. Press the greyed out "plus" on the Shortcut widget
141. Press "OK" to close the popup
142. Press "X" to close the popup
143. Select any apps from Shortcut Selection screen
144. Check that Shortcut widget content is updated **[含 §5.2B 措詞]**
