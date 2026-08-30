#!/usr/bin/env python3
"""T66b —— batch 7：`Wi-Fi Download` 29 列扣除 `057` = 28 列（下放包 54 §二 #4）。

**`057` 不起草**（下放包 54 §二 #1）—— 其 `30 分鐘` 於 037 與嵌入物件 `4908702`
之起算點不一致，二者皆為上游文件，我方無權擇一。

**本批之特徵**：五列自帶門檻（`043`／`054`／`065`／`069`／`071`），
**IN §8.7.1 之門檻條款於本 feature 首次實際套用** —— 其值逐字取自 037，
逐列記於 `REASONING.md`。

**⚠ 遮蔽測試前置**（下放包 52 §二 #6）：本批不使用共通形態函式產出 Final Step，
每列之末步各自帶入其判定核心。
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import _set_row, MASTER, SHEET_NAME, HEADER_ROW, FEAT  # noqa: E402

TAG = "batch7"
OUT = FEAT / "sandbox" / TAG / MASTER
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"
START_N = 82
TS = "Wi-Fi Download"

FN = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
DT = "決策表 (Decision Table Testing)"
BV = "邊界值分析 (Boundary Value Analysis, BVA)"

# 共用前提（逐列組合，非共通形態函式）
B = "1. The vehicle is in Body ON mode"
AP = "2. A password-protected Wi-Fi access point with internet access is within range of the head unit"
PAGE = "3. The software download via Wi-Fi page is open on the head unit"
CONN = "3. The head unit is connected to a saved Wi-Fi access point with internet access"
PKG = "4. An update package is staged on the OTA Server for this head unit"

REC = ("2. Record the head unit screen content as continuous video capture "
       "until the check in the final step is completed")
ER_REC = ("2. The head unit screen content until the check in the final step is completed "
          "is recorded as continuous video capture")


def tc(req, spec, dm, prio, conf, note, item, paren, pre, proc, er):
    return dict(req=req, spec=spec, dm=dm, prio=prio, conf=conf, note=note,
                item=[item, f"({paren})"], pre=pre, proc=proc, er=er)


TCS = [
 # ── HMI 流程（可觀測、可觸發）────────────────────────────────────────
 tc("SWE1-FOTA-039", "CFTS057-4907421", FN, "P1", "高", "HMI 選項之存在與可選，全程可觀測",
  "The SW Update HMI shall provide a selectable option to enable software download via Wi-Fi when the user enters the software download via Wi-Fi page.",
  "Enable option is offered and can be selected on the Wi-Fi download page",
  [B, AP, "3. The software update menu is open on the head unit"],
  ["1. Open the software download via Wi-Fi page on the head unit",
   "2. Check that the page shows an option to enable software download via Wi-Fi",
   "3. Select the option to enable software download via Wi-Fi",
   "4. Check that the head unit accepts the selection of the enable option"],
  ["1. The software download via Wi-Fi page is shown",
   "2. The page shows an option to enable software download via Wi-Fi",
   "3. The option to enable software download via Wi-Fi is selected",
   "4. The head unit accepts the selection and the option is shown as enabled"]),

 tc("SWE1-FOTA-040", "CFTS057-4907418", FN, "P1", "中",
  "判定核心為警示提示之內容；`notify subscribed modules` 為統攝殘餘（R-SU37 v2），記於 REASONING 不掛 PENDING",
  "Upon detecting the selection, the SW Update HMI shall display a prompt informing the user that enabling software download via Wi-Fi may disable services including Wi-Fi Hotspot, Android Auto, and Apple CarPlay.",
  "Service impact warning names Wi-Fi Hotspot, Android Auto and Apple CarPlay",
  [B, AP, PAGE],
  ["1. Select the option to enable software download via Wi-Fi",
   REC,
   "3. Check that the displayed prompt names Wi-Fi Hotspot, Android Auto and Apple CarPlay as services that may be disabled"],
  ["1. The option to enable software download via Wi-Fi is selected",
   ER_REC,
   "3. The recorded screen content shows a prompt naming Wi-Fi Hotspot, Android Auto and Apple CarPlay as services that may be disabled"]),

 tc("SWE1-FOTA-041", "CFTS057-4907419", FN, "P1", "中",
  "Client Mode 之外部表徵取熱點不再可用 ＋ 掃描清單出現，非屬性值（R-SU25）",
  "After successful transition to Client Mode, the WiFi Update Service shall request WiFi Manager to initiate a scan for available Wi-Fi networks.",
  "Available network list appears after the user confirms with “Yes”",
  [B, AP, PAGE, "4. The head unit Wi-Fi hotspot is available to a companion device"],
  ["1. Select the option to enable software download via Wi-Fi and select the “Yes” option on the confirmation prompt",
   REC,
   "3. Check that the head unit shows a list of available Wi-Fi networks",
   "4. Check that the head unit Wi-Fi hotspot is no longer available to the companion device"],
  ["1. The “Yes” option on the confirmation prompt is selected",
   ER_REC,
   "3. The recorded screen content shows a list of available Wi-Fi networks",
   "4. The head unit Wi-Fi hotspot is no longer available to the companion device"]),

 tc("SWE1-FOTA-042", "CFTS057-4907421", FN, "P2", "高", "純畫面導覽，可觀測可觸發",
  "Upon detecting the user selection of “No”, the SW Update HMI shall navigate back to the software download via Wi-Fi page.",
  "Screen returns to the Wi-Fi download page when the user selects “No”",
  [B, AP, PAGE],
  ["1. Select the option to enable software download via Wi-Fi",
   REC,
   "3. Select the “No” option on the confirmation prompt",
   "4. Check that the head unit shows the software download via Wi-Fi page"],
  ["1. The option to enable software download via Wi-Fi is selected",
   ER_REC,
   "3. The “No” option on the confirmation prompt is selected",
   "4. The recorded screen content shows the software download via Wi-Fi page after the “No” selection"]),

 # ── 門檻列 1：15 秒（Host → Client）────────────────────────────────
 tc("SWE1-FOTA-043", "CFTS057-4907433", BV, "P1", "中",
  "**門檻列**：`within 15 seconds` 逐字取自 037；時間由連續錄影之時戳量（R-SU36）",
  "The WiFi Manage shall complete the transition from Host Mode to Client Mode within 15 seconds.",
  "Client Mode is reached within 15 seconds of the user confirmation",
  [B, AP, PAGE, "4. The head unit Wi-Fi hotspot is available to a companion device"],
  ["1. Record the head unit screen content as continuous video capture until the available Wi-Fi network list is shown",
   "2. Select the option to enable software download via Wi-Fi and confirm the start of software download via Wi-Fi",
   "3. Read from the recording the time of the user confirmation and record it as Time_confirm",
   "4. Read from the recording the time at which the available Wi-Fi network list is first shown and record it as Time_client",
   "5. Check that Time_client is not later than 15 seconds after Time_confirm"],
  ["1. The head unit screen content until the available Wi-Fi network list is shown is recorded as continuous video capture",
   "2. The start of software download via Wi-Fi is confirmed",
   "3. Time_confirm is recorded",
   "4. Time_client is recorded",
   "5. Time_client is not later than 15 seconds after Time_confirm"]),

 tc("SWE1-FOTA-044", "CFTS057-4907423", FN, "P1", "中",
  "`within Wi-Fi range` 之判定以台架佈置給出（在範圍內之 AP 與已關閉之 AP）",
  "The HMI shall display the password-protected Wi-Fi networks that are within Wi-Fi range.",
  "Password-protected networks in range are listed",
  [B, AP, PAGE,
   "4. A second password-protected Wi-Fi access point is switched off so that it is out of range"],
  ["1. Enable software download via Wi-Fi and wait for the available Wi-Fi network list to be shown",
   REC,
   "3. Check that the list shows the password-protected access point that is within range",
   "4. Check that the list does not show the access point that is switched off"],
  ["1. The available Wi-Fi network list is shown",
   ER_REC,
   "3. The recorded screen content shows the password-protected access point that is within range",
   "4. The recorded screen content does not show the access point that is switched off"]),

 tc("SWE1-FOTA-045", "CFTS057-4907424", FN, "P1", "高", "密碼輸入與連線建立全程可觀測",
  "The HMI shall provide an input interface for the user to enter the password for the selected Wi-Fi network.",
  "Password can be entered for the selected network and the connection is established",
  [B, AP, PAGE],
  ["1. Enable software download via Wi-Fi and select the password-protected access point from the available Wi-Fi network list",
   REC,
   "3. Check that the head unit shows an input interface for the password of the selected network",
   "4. Enter the password of the selected access point",
   "5. Check that the head unit shows the selected network as connected"],
  ["1. The password-protected access point is selected from the available Wi-Fi network list",
   ER_REC,
   "3. The recorded screen content shows an input interface for the password of the selected network",
   "4. The password of the selected access point is entered",
   "5. The recorded screen content shows the selected network as connected"]),

 tc("SWE1-FOTA-047", "CFTS057-4907426", FN, "P1", "中",
  "判定核心為**再次自動連線**；四個欄位（SSID／security／encryption／passphrase）於外部無逐項表徵，為殘餘（R-SU37 v2），記於 REASONING",
  "Connectivity Manager shall use the stored Wi-Fi network configuration for subsequent automatic Wi-Fi connection attempts.",
  "Head unit reconnects to the saved network without the password being entered again",
  [B, AP, PAGE],
  ["1. Enable software download via Wi-Fi, select the password-protected access point and enter its password",
   "2. Exit the software download via Wi-Fi page and open it again",
   REC.replace("2.", "3."),
   "4. Check that the head unit connects to the same access point without asking for the password again"],
  ["1. The head unit is connected to the password-protected access point",
   "2. The software download via Wi-Fi page is opened again",
   ER_REC.replace("2.", "3."),
   "4. The recorded screen content shows the head unit connected to the same access point and shows no request for the password"]),

 tc("SWE1-FOTA-048", "CFTS057-4907427", NEG, "P1", "高", "以錯誤密碼觸發連線失敗，手段可得",
  "The HMI shall display a prompt indicating that the Wi-Fi connection was not successful.",
  "Connection failure prompt is shown when a wrong password is entered",
  [B, AP, PAGE],
  ["1. Enable software download via Wi-Fi and select the password-protected access point from the available Wi-Fi network list",
   REC,
   "3. Enter a password that does not match the password of the selected access point",
   "4. Check that the head unit shows a prompt indicating that the Wi-Fi connection was not successful"],
  ["1. The password-protected access point is selected from the available Wi-Fi network list",
   ER_REC,
   "3. A password that does not match the password of the selected access point is entered",
   "4. The recorded screen content shows a prompt indicating that the Wi-Fi connection was not successful"]),

 tc("SWE1-FOTA-049", "CFTS057-4907428", FN, "P2", "高", "同 `048` 之情境，判定對象為返回選項而非失敗提示",
  "The HMI shall provide an option for the user to navigate back to the software download via Wi-Fi screen when Wi-Fi connection establishment is unsuccessful.",
  "Back option after a failed connection returns to the Wi-Fi download screen",
  [B, AP, PAGE],
  ["1. Enable software download via Wi-Fi, select the password-protected access point and enter a password that does not match it",
   REC,
   "3. Check that the head unit offers an option to navigate back to the software download via Wi-Fi screen",
   "4. Select the option to navigate back and check that the head unit shows the software download via Wi-Fi screen"],
  ["1. A password that does not match the selected access point is entered and the connection is unsuccessful",
   ER_REC,
   "3. The recorded screen content shows an option to navigate back to the software download via Wi-Fi screen",
   "4. The recorded screen content shows the software download via Wi-Fi screen after the back option is selected"]),

 tc("SWE1-FOTA-050", "CFTS057-4907429", FN, "P2", "中",
  "移除之外部表徵為**再次連線時重新要求密碼**；儲存欄位本身無逐項表徵（同 `047`）",
  "Upon receiving the request, WiFi Manager shall remove the stored Wi-Fi network configuration and associated credentials for the selected network, including SSID, security type, encryption type, and passphrase.",
  "Forgotten network asks for the password again on the next connection",
  [B, AP, PAGE, "4. The head unit has a saved connection to the password-protected access point"],
  ["1. Select the “Forget Network” option for the saved access point",
   REC,
   "3. Select the same access point from the available Wi-Fi network list",
   "4. Check that the head unit asks for the password of the selected access point"],
  ["1. The “Forget Network” option for the saved access point is selected",
   ER_REC,
   "3. The same access point is selected from the available Wi-Fi network list",
   "4. The recorded screen content shows a request for the password of the selected access point"]),

 tc("SWE1-FOTA-051", "CFTS057-4907430", FN, "P2", "中",
  "以第二個 AP 於重新整理前後之開關，使更新後之清單與更新前可區分",
  "The HMI shall display the updated Wi-Fi network list to the user.",
  "Refresh shows a network that was switched on after the previous scan",
  [B, AP, PAGE, "4. A second Wi-Fi access point is switched off"],
  ["1. Enable software download via Wi-Fi and wait for the available Wi-Fi network list to be shown",
   REC,
   "3. Switch on the second Wi-Fi access point",
   "4. Select the refresh option for the available Wi-Fi network list",
   "5. Check that the refreshed list shows the second access point"],
  ["1. The available Wi-Fi network list is shown without the second access point",
   ER_REC,
   "3. The second Wi-Fi access point is switched on",
   "4. The refresh option is selected",
   "5. The recorded screen content shows the refreshed list containing the second access point"]),

 tc("SWE1-FOTA-052", "CFTS057-4907431", FN, "P2", "中",
  "掃描之外部表徵為畫面上之掃描指示；其停止即判定核心",
  "The HMI shall detect the user selection of the “Stop Scanning” option and request WiFi Manager to stop the ongoing Wi-Fi network scanning process.",
  "Scanning indication ends after “Stop Scanning” is selected",
  [B, AP, PAGE],
  ["1. Enable software download via Wi-Fi so that Wi-Fi network scanning is active",
   REC,
   "3. Select the “Stop Scanning” option while the scanning indication is shown",
   "4. Check that the head unit no longer shows the scanning indication"],
  ["1. The scanning indication is shown on the head unit",
   ER_REC,
   "3. The “Stop Scanning” option is selected",
   "4. The recorded screen content shows that the scanning indication has ended"]),

 tc("SWE1-FOTA-053", "CFTS057-4907432", FN, "P1", "中",
  "Host Mode 之外部表徵為熱點恢復可用（同 `041` 之反向）",
  "The SW Update HMI shall detect the user action to disable software download via Wi-Fi from the check box or to exit the software download via Wi-Fi page.",
  "Hotspot becomes available again after the user disables Wi-Fi download",
  [B, AP, PAGE, "4. Software download via Wi-Fi is enabled",
   "5. The head unit Wi-Fi hotspot is not available to a companion device"],
  ["1. Clear the check box for software download via Wi-Fi on the head unit",
   REC,
   "3. Check that the head unit Wi-Fi hotspot is available to the companion device again"],
  ["1. The check box for software download via Wi-Fi is cleared",
   ER_REC,
   "3. The head unit Wi-Fi hotspot is available to the companion device again"]),

 # ── 門檻列 2：15 秒（Client → Host），105 列 ───────────────────────
 tc("SWE1-FOTA-054", "CFTS057-4907432", BV, "P1", "中",
  "**門檻列**＋**105 列**：`within 15 seconds` 逐字取自 037；Host Mode 以熱點恢復為表徵（R-SU32 v2(e) 之又一例）",
  "The WiFi Update Service shall complete the transition from Client Mode to Host Mode within 15 seconds.",
  "Hotspot is available again within 15 seconds of the exit action",
  [B, AP, PAGE, "4. Software download via Wi-Fi is enabled",
   "5. The head unit Wi-Fi hotspot is not available to a companion device"],
  ["1. Record the head unit screen content and the companion device hotspot list as continuous video capture until the hotspot is available again",
   "2. Exit the software download via Wi-Fi page on the head unit",
   "3. Read from the recording the time of the exit action and record it as Time_exit",
   "4. Read from the recording the time at which the head unit hotspot is first available to the companion device and record it as Time_host",
   "5. Check that Time_host is not later than 15 seconds after Time_exit"],
  ["1. The head unit screen content and the companion device hotspot list until the hotspot is available again are recorded as continuous video capture",
   "2. The software download via Wi-Fi page is exited",
   "3. Time_exit is recorded",
   "4. Time_host is recorded",
   "5. Time_host is not later than 15 seconds after Time_exit"]),

 # ── IGN_OFF 與彈窗 ───────────────────────────────────────────────
 tc("SWE1-FOTA-056", "CFTS057-4907831", DT, "P1", "低",
  "⚠ 錨為機制 3 攔下之首選（0.237）；三個條件之合取以決策表法佈置",
  "If the FOTA package classification is Non-Critical, no previously configured Wi-Fi network is available, and when the vehicle PowerMode transitions to $PowerMode$ = [IGN_OFF], the WiFi Update Service shall request the SW Update HMI to display the Wi-Fi software download pop-up notification.",
  "Wi-Fi download pop-up appears at IGN_OFF when no network is saved",
  [B, "2. A Non-Critical update package is staged on the OTA Server for this head unit",
   "3. No Wi-Fi network is saved on the head unit"],
  ["1. Record the head unit screen content as continuous video capture until the ignition is switched off and the head unit screen turns off",
   "2. Switch the vehicle ignition off",
   "3. Check that the head unit displays the Wi-Fi software download pop-up notification after the ignition is switched off"],
  ["1. The head unit screen content until the head unit screen turns off is recorded as continuous video capture",
   "2. The vehicle ignition is switched off",
   "3. The recorded screen content shows the Wi-Fi software download pop-up notification after the ignition is switched off"]),

 tc("SWE1-FOTA-059", "CFTS057-4907402", FN, "P1", "低",
  "⚠ 錨為機制 3 攔下之首選（0.227）；`Verification Method` 僅 Integration Test，系統測之判定核心取自動連線",
  "The WiFi Update Service shall request Connectivity Service to establish Wi-Fi connectivity with a previously configured Wi-Fi network selected for OTA updates.",
  "Head unit connects to the saved network for the update without user action",
  [B, AP, "3. The password-protected access point is saved on the head unit", PKG],
  ["1. Disconnect the head unit from the saved access point and confirm that no Wi-Fi network is connected",
   REC,
   "3. Trigger an update availability check to the OTA Server",
   "4. Check that the head unit connects to the saved access point without any user action"],
  ["1. No Wi-Fi network is connected on the head unit",
   ER_REC,
   "3. The update availability check completes and an update is reported as available",
   "4. The recorded screen content shows the head unit connected to the saved access point and shows no user action in between"]),

 tc("SWE1-FOTA-060", "CFTS057-4907403", FN, "P1", "中",
  "以二個訊號強度不同之 AP 佈置選擇；`best preferred` 之判定核心取所連之網路",
  "The WiFi Update Service shall request the Connectivity Service to establish connectivity with the best preferred Wi-Fi network via WiFi Manager for OTA package download.",
  "Head unit connects to the stronger of two saved networks",
  [B, "2. Two password-protected Wi-Fi access points with internet access are saved on the head unit",
   "3. One access point is placed close to the head unit",
   "4. The other access point is attenuated so that the head unit shows it with fewer signal bars",
   "5. An update package is staged on the OTA Server for this head unit"],
  ["1. Disconnect the head unit from both saved access points",
   REC,
   "3. Trigger an update availability check to the OTA Server",
   "4. Check that the head unit connects to the access point shown with more signal bars"],
  ["1. No Wi-Fi network is connected on the head unit",
   ER_REC,
   "3. The update availability check completes and an update is reported as available",
   "4. The recorded screen content shows the head unit connected to the access point shown with more signal bars"]),

 tc("SWE1-FOTA-061", "CFTS057-4907420", NEG, "P1", "低",
  "⚠ 錨為機制 3 攔下之首選（0.256）＋**105 列**；以關閉之 AP 佈置「不在範圍內」",
  "The WiFi Update Service shall request Connectivity Manager to establish Wi-Fi connectivity only with configured Wi-Fi networks that are available within range.",
  "Saved network that is out of range is not connected",
  [B, "2. Two password-protected Wi-Fi access points are saved on the head unit",
   "3. One saved access point is switched off",
   "4. The other saved access point is within range",
   "5. An update package is staged on the OTA Server for this head unit"],
  ["1. Disconnect the head unit from the saved access points",
   REC,
   "3. Trigger an update availability check to the OTA Server",
   "4. Check that the head unit connects to the access point that is within range and does not connect to the access point that is switched off"],
  ["1. No Wi-Fi network is connected on the head unit",
   ER_REC,
   "3. The update availability check completes and an update is reported as available",
   "4. The recorded screen content shows the head unit connected to the access point that is within range and shows no connection to the access point that is switched off"]),

 tc("SWE1-FOTA-062", "CFTS057-4907405", FN, "P2", "低",
  "⚠ **第三型**：遮蔽測試抓出其 Final Step 與 `060` 逐字相同 —— 其唯一之區分為排除清單，而該清單無外部表徵，故不可區辨（R-SU32(iii)），入 DR-SU2(c)",
  "The WiFi Update Service shall use Wi-Fi signal strength as the primary selection criterion and shall request the Connectivity Service to establish the Wi-Fi connection with the network.",
  "Signal strength decides the connection among networks that are not excluded",
  [B, "2. Two password-protected Wi-Fi access points with internet access are saved on the head unit",
   "3. One access point is placed close to the head unit",
   "4. The other access point is attenuated so that the head unit shows it with fewer signal bars",
   "5. PENDING: DR-SU2 means of placing a Wi-Fi network on the WiFi Manager exclusion list and of reading that list",
   "6. An update package is staged on the OTA Server for this head unit"],
  ["1. Disconnect the head unit from both saved access points",
   REC,
   "3. PENDING: DR-SU2 step to place the access point shown with more signal bars on the exclusion list",
   "4. Trigger an update availability check to the OTA Server",
   "5. PENDING: DR-SU2 check that the head unit connects to the remaining access point because the stronger one is on the exclusion list"],
  ["1. No Wi-Fi network is connected on the head unit",
   ER_REC,
   "3. PENDING: DR-SU2 observable evidence that a network is on the exclusion list",
   "4. The update availability check completes and an update is reported as available",
   "5. PENDING: DR-SU2 observable evidence distinguishing this connection from the one verified by SWE1-FOTA-060"]),

 tc("SWE1-FOTA-063", "CFTS057-4907406", FN, "P2", "低",
  "第二型＋值未載：分類結果於外部無表徵，且 `predefined thresholds` 之值 037 未給（自訂即造值，§8.4.1）",
  "The WiFi Manager shall classify each Wi-Fi network into one of the following categories based on predefined Wi-Fi signal strength thresholds: High Signal Strength Medium Signal Strength Low Signal Strength",
  "Networks in range are classified as high, medium or low signal strength",
  [B, AP, PAGE,
   "4. PENDING: DR-SU2 means of observing the signal strength category assigned to a Wi-Fi network",
   "5. PENDING: DR-SU2 values of the predefined Wi-Fi signal strength thresholds that separate the high, medium and low categories"],
  ["1. Enable software download via Wi-Fi and wait for the available Wi-Fi network list to be shown",
   "2. PENDING: DR-SU2 step to read the signal strength category assigned to each access point in range"],
  ["1. The available Wi-Fi network list is shown",
   "2. PENDING: DR-SU2 observable evidence of the signal strength category assigned to each access point in range"]),

 tc("SWE1-FOTA-064", "CFTS057-4907407", FN, "P1", "中",
  "與 `060`／`062` 之別：本列驗**首次嘗試限於最高類別**，故第三個 AP 之存在為其判定核心之一部",
  "During the initial Wi-Fi connection attempt, the WiFi Update Service shall restrict network selection to Wi-Fi networks belonging only to the identified highest signal strength category.",
  "First connection attempt uses a network from the strongest group only",
  [B, "2. Three password-protected Wi-Fi access points with internet access are saved on the head unit",
   "3. One access point is placed close to the head unit",
   "4. The other two access points are attenuated so that the head unit shows them with fewer signal bars",
   "5. An update package is staged on the OTA Server for this head unit"],
  ["1. Disconnect the head unit from all three saved access points",
   REC,
   "3. Trigger an update availability check to the OTA Server",
   "4. Check that the first access point the head unit connects to is the one shown with the most signal bars"],
  ["1. No Wi-Fi network is connected on the head unit",
   ER_REC,
   "3. The update availability check completes and an update is reported as available",
   "4. The recorded screen content shows that the first access point the head unit connects to is the one shown with the most signal bars"]),

 # ── 門檻列 3：5 次連續失敗 ────────────────────────────────────────
 tc("SWE1-FOTA-065", "CFTS057-4907408", BV, "P1", "低",
  "**門檻列**（`5 consecutive`，逐字取自 037）＋⚠ 錨為機制 3 攔下之首選（0.215）；移除之表徵取可選網路清單",
  "If OTA package download completion fails for 5 consecutive Wi-Fi connection attempts using the same previously configured Wi-Fi network, the WiFi Update Service shall request WiFiManager to remove the Wi-Fi network from the selectable known Wi-Fi network list.",
  "Network is dropped from the selectable list after five failed download attempts",
  [B, "2. A password-protected Wi-Fi access point without internet access is saved on the head unit",
   "3. The saved access point is the only Wi-Fi network in range", PKG],
  ["1. Trigger an update availability check to the OTA Server and let the OTA package download fail on the saved access point",
   REC,
   "3. Repeat the download attempt on the same saved access point until the download has failed five times in a row",
   "4. Open the Wi-Fi network list on the head unit",
   "5. Check that the saved access point is no longer shown in the selectable known Wi-Fi network list"],
  ["1. The OTA package download on the saved access point fails",
   ER_REC,
   "3. The OTA package download on the same saved access point has failed five times in a row",
   "4. The Wi-Fi network list is shown on the head unit",
   "5. The recorded screen content shows that the saved access point is no longer in the selectable known Wi-Fi network list"]),

 tc("SWE1-FOTA-066", "CFTS057-4907414", FN, "P1", "中",
  "與 `056` 之別：`056` 之條件含 Non-Critical 分類，本列只條件於無已存網路",
  "Upon the next transition of $PowerMode$ t= [IGN_OFF] received through CarProperty Manager, the HMI shall display the pop-up .",
  "Pop-up is displayed at the next IGN_OFF while no network is saved",
  [B, "2. No Wi-Fi network is saved on the head unit", "3. The vehicle ignition is on"],
  ["1. Record the head unit screen content as continuous video capture until the ignition is switched off and the head unit screen turns off",
   "2. Switch the vehicle ignition off",
   "3. Check that the head unit displays the pop-up at the ignition off transition that follows the state in which no Wi-Fi network is saved"],
  ["1. The head unit screen content until the head unit screen turns off is recorded as continuous video capture",
   "2. The vehicle ignition is switched off",
   "3. The recorded screen content shows the pop-up at the ignition off transition that follows the state in which no Wi-Fi network is saved"]),

 tc("SWE1-FOTA-067", "CFTS057-4907396", FN, "P2", "低",
  "**105 列**＋⚠ 錨為機制 3 攔下之首選（0.261）；前提之評估本身於外部無表徵，其後果屬 `070`",
  "Upon the IGN_OFF event, the WiFi Update Service shall evaluate the configured preconditions for software download via Wi-Fi.",
  "Preconditions for Wi-Fi download are evaluated at the IGN_OFF event",
  [B, AP, "3. The password-protected access point is saved on the head unit", PKG,
   "5. PENDING: DR-SU2 means of observing that the preconditions for software download via Wi-Fi have been evaluated"],
  ["1. Trigger an update availability check to the OTA Server so that a software download is available",
   "2. Switch the vehicle ignition off",
   "3. PENDING: DR-SU2 step to read the outcome of the precondition evaluation at the ignition off event"],
  ["1. The update availability check completes and a software download is reported as available",
   "2. The vehicle ignition is switched off",
   "3. PENDING: DR-SU2 observable evidence that the preconditions for software download via Wi-Fi were evaluated at the ignition off event"]),

 # ── 門檻列 4：SOC 65% ────────────────────────────────────────────
 tc("SWE1-FOTA-069", "CFTS057-4907398", DT, "P1", "中",
  "**門檻列**（`$IBS_SOC$ > [65]` 逐字取自 037）；取負向面以與 `070` 之正向面區分",
  "If $IBS_SOC$ is available, the WiFi Update Service shall verify that the battery State of Charge is greater than 65%.($IBS_SOC$ > [65])",
  "Download does not start while the battery state of charge is not above 65%",
  [B, AP, "3. The password-protected access point is saved on the head unit", PKG,
   "5. The battery state of charge reported on $IBS_SOC$ is set to 60%"],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server so that a software download is available",
   "3. Switch the vehicle ignition off",
   "4. Check that no software download over Wi-Fi starts while the battery state of charge reported on $IBS_SOC$ is 60%"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The update availability check completes and a software download is reported as available",
   "3. The vehicle ignition is switched off",
   "4. The recorded screen content shows no software download over Wi-Fi starting while the battery state of charge reported on $IBS_SOC$ is 60%"]),

 tc("SWE1-FOTA-070", "CFTS057-4907396", FN, "P1", "低",
  "**105 列**＋⚠ 錨為機制 3 攔下之首選（0.189）；正向面，與 `069` 之負向面互為對照",
  "If the preconditions are satisfied and a previously configured Wi-Fi network is available, the WiFi Update Service shall request WiFiManager and Connectivity Manager to establish Wi-Fi connectivity.",
  "Download over Wi-Fi starts when the preconditions are satisfied",
  [B, AP, "3. The password-protected access point is saved on the head unit", PKG,
   "5. The battery state of charge reported on $IBS_SOC$ is set to 80%"],
  ["1. Record the head unit screen content as continuous video capture until the check in the final step is completed",
   "2. Trigger an update availability check to the OTA Server so that a software download is available",
   "3. Switch the vehicle ignition off",
   "4. Check that the head unit connects to the saved access point and that the software download over Wi-Fi starts while the battery state of charge reported on $IBS_SOC$ is 80%"],
  ["1. The head unit screen content until the check in the final step is completed is recorded as continuous video capture",
   "2. The update availability check completes and a software download is reported as available",
   "3. The vehicle ignition is switched off",
   "4. The recorded screen content shows the head unit connected to the saved access point and the software download over Wi-Fi starting while the battery state of charge reported on $IBS_SOC$ is 80%"]),

 # ── 門檻列 5：3 分鐘 ─────────────────────────────────────────────
 tc("SWE1-FOTA-071", "CFTS057-4907400", BV, "P1", "中",
  "**門檻列**（`within 3 minutes` 逐字取自 037）；以不回應之 AP 佈置逾時，時間由錄影時戳量",
  "If Wi-Fi connection establishment is unsuccessful within 3 minutes, the WiFi Update Service shall terminate the active Wi-Fi connection attempt.",
  "Head unit moves to the next saved network after the three-minute attempt fails",
  [B, "2. Two password-protected Wi-Fi access points are saved on the head unit",
   "3. The access point with the higher priority is configured to accept no connection while remaining in range",
   "4. The second saved access point has internet access",
   "5. An update package is staged on the OTA Server for this head unit"],
  ["1. Record the head unit screen content as continuous video capture until the head unit is connected to the second saved access point",
   "2. Trigger an update availability check to the OTA Server and switch the vehicle ignition off",
   "3. Read from the recording the time at which the connection attempt to the higher priority access point starts and record it as Time_start",
   "4. Read from the recording the time at which the head unit connects to the second saved access point and record it as Time_next",
   "5. Check that Time_next is not earlier than 3 minutes after Time_start"],
  ["1. The head unit screen content until the head unit is connected to the second saved access point is recorded as continuous video capture",
   "2. The vehicle ignition is switched off after the update availability check completes",
   "3. Time_start is recorded",
   "4. Time_next is recorded",
   "5. Time_next is not earlier than 3 minutes after Time_start"]),
]

# `低` 之理由 × 是否由 `PENDING` 承載（下放包 51 §一 #5）
LOW_REASONS = {
 "SWE1-FOTA-056": [("錨為機制 3 攔下之首選（0.237），未經 GT 驗證", False)],
 "SWE1-FOTA-059": [("錨為機制 3 攔下之首選（0.227），未經 GT 驗證", False)],
 "SWE1-FOTA-061": [("錨為機制 3 攔下之首選（0.256），未經 GT 驗證", False)],
 "SWE1-FOTA-062": [("與 `060` 不可區辨（區分繫於無外部表徵之排除清單）", True)],
 "SWE1-FOTA-063": [("分類結果無外部表徵", True), ("門檻值 037 未載", True)],
 "SWE1-FOTA-065": [("錨為機制 3 攔下之首選（0.215），未經 GT 驗證", False)],
 "SWE1-FOTA-067": [("前提評估本身無外部表徵", True),
                   ("錨為機制 3 攔下之首選（0.261），未經 GT 驗證", False)],
 "SWE1-FOTA-070": [("錨為機制 3 攔下之首選（0.189），未經 GT 驗證", False)],
}
# 下放包 54 §二 #4：機制 3 攔下之六列一律進抽驗，不因 `PENDING` 排除
MECH3 = ["SWE1-FOTA-056", "SWE1-FOTA-059", "SWE1-FOTA-061",
         "SWE1-FOTA-065", "SWE1-FOTA-067", "SWE1-FOTA-070"]


def main():
    import openpyxl, warnings
    from collections import Counter
    warnings.filterwarnings("ignore")
    src = FEAT / "inputs" / MASTER
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = {str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)}
    if {t["dm"] for t in TCS} - legal:
        sys.exit("T66b：`design_method` 有清單外之值 —— 停（R-SU40(a)）")
    from corpus_v2 import _rows_desc
    _, desc = _rows_desc()
    bad = [t["req"] for t in TCS if t["item"][0] not in desc[t["req"]]]
    if bad:
        sys.exit(f"T66b：`test_item` 上半非逐字：{bad} —— 停（R-S4）")
    if "SWE1-FOTA-057" in {t["req"] for t in TCS}:
        sys.exit("T66b：`057` 於門檻裁定前不得起草 —— 停（下放包 54 §二 #1）")

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("## T66b —— batch 7 之產出（`Wi-Fi Download`，28 列）\n")
    rows = []
    for i, t in enumerate(TCS):
        n = START_N + i
        tcid = f"{proj}-SU-{n:03d}"
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": TS,
                "I": "\n".join(t["item"]), "J": "\n".join(t["pre"]),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t["dm"],
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, HEADER_ROW + i + 1, vals)
        pend = sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])
        rows.append((HEADER_ROW + i + 1, tcid, t["req"], t["conf"], pend))

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("| 列 | TC ID | 037 | 自信度 | PENDING |")
    print("|---|---|---|:--:|---:|")
    for r, tid, req, cf, pd in rows:
        print(f"| {r} | `{tid}` | `{req[-3:]}` | **{cf}** | {pd} |")
    c = Counter(t["conf"] for t in TCS)
    excl, keep = [], []
    for i, t in enumerate(TCS, START_N):
        if t["conf"] != "低":
            continue
        rs = LOW_REASONS.get(t["req"], [])
        (excl if rs and all(ok for _, ok in rs) else keep).append((i, t["req"], rs))
    mid = [(i, t["req"]) for i, t in enumerate(TCS, START_N) if t["conf"] == "中"]
    m3 = [(i, t["req"]) for i, t in enumerate(TCS, START_N) if t["req"] in MECH3]
    union = sorted({i for i, _, _ in keep} | {i for i, _ in mid} | {i for i, _ in m3})
    print(f"\n- **`PENDING` 合計 {sum(r[4] for r in rows)}**｜TC **{len(rows)}**")
    print(f"\n### 分層抽驗（下放包 54 §二 #4 之加重規則）\n")
    print(f"- 自信度：高 {c['高']}／中 {c['中']}／低 {c['低']}")
    print(f"- 可排除之 `低`：{len(excl)} 列 —— "
          + ("、".join(f"`SU-{i:03d}`" for i, _, _ in excl) or "**無**"))
    for i, req, rs in keep:
        un = [r for r, ok in rs if not ok]
        print(f"- ⚠ **`SU-{i:03d}`（`{req[-3:]}`）不可排除** —— 未由 `PENDING` 承載者："
              + "、".join(f"**{r}**" for r in un))
    print(f"- **機制 3 攔下之 6 列**（不因 `PENDING` 排除）："
          + "、".join(f"`SU-{i:03d}`" for i, _ in m3))
    print(f"- **抽驗組成 = 低 ∪ 中 ∪ 機制 3 = {len(union)} 列** —— "
          + "、".join(f"`SU-{i:03d}`" for i in union))
    print(f"- **退回訊號**：扣除後 `低` = **{len(keep)}** "
          + ("**> 3 → 觸發**" if len(keep) > 3 else "≤ 3 → **不觸發**"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
