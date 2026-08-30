# 39 個有錨 `<X>` 之供料頁（65 包 R-P384(c)）

> **執行層供料，不判定、不查詢**。`observable_proxy_64.md` 已依 R-P384 退回；
> 39 名之代理量由分析層於 66 包逐名人讀裁定。

> **複合觀察目標（`A and B`、`X against Y`）保留原形，未預拆**（R-P384(d)）。
> R-P353(ii) 之「具名 UI 元件」指規格段落**指名**之元件，**不以規格原文帶引號為要件**（R-P384(b)）。

> 段落全文自 `data/textlayer/*_plain.txt` 逐字取，**未截斷、未摘要**。

> 母體 39 名，取自 `proxy_reachability_63.md` 之 `**有錨**` 列。

## `shown logos`

### `NR1L-PowerManagement-149`　（`SWE-PM-054`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-150`　（`SWE-PM-054`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The Beats Brand White logo is shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-151`　（`SWE-PM-054`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-152`　（`SWE-PM-054`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-192`　（`SWE-PM-101`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-193`　（`SWE-PM-101`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The Beats Brand White logo is shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-194`　（`SWE-PM-101`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `NR1L-PowerManagement-195`　（`SWE-PM-101`）

**`test_item` 上半 verbatim**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo
```

**錨點 `CFTS009-4941673` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
```

**錨點 `CFTS009-4941674` 段落全文**

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941675` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
```

**錨點 `CFTS009-4941676` 段落全文**

```
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

## `Timeout1 and then trigger an Ignition On event`

### `NR1L-PowerManagement-100`　（`SWE-PM-028`）

**`test_item` 上半 verbatim**

```
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**現行 Procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**現行 Expected Result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**錨點 `CFTS009-4941580` 段落全文**

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
```

**錨點 `CFTS009-4941581` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**錨點 `CFTS009-4941582` 段落全文**

```
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

### `NR1L-PowerManagement-101`　（`SWE-PM-028`）

**`test_item` 上半 verbatim**

```
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**現行 Procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**現行 Expected Result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**錨點 `CFTS009-4941580` 段落全文**

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
```

**錨點 `CFTS009-4941581` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**錨點 `CFTS009-4941582` 段落全文**

```
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

### `NR1L-PowerManagement-103`　（`SWE-PM-029`）

**`test_item` 上半 verbatim**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**現行 Procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**現行 Expected Result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**錨點 `CFTS009-4941586` 段落全文**

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
```

**錨點 `CFTS009-4941587` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**錨點 `CFTS009-4941588` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the value specified by $PwrAccDelayAct$ (for example 10  minutes if $PwrAccDelayAct$ == 10 minutes), only for this case,  restoring it to "00 minutes" at next Ignition  On event.
```

**錨點 `CFTS009-4941589` 段落全文**

```
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

### `NR1L-PowerManagement-104`　（`SWE-PM-029`）

**`test_item` 上半 verbatim**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the value specified by $PwrAccDelayAct$ (for example 10  minutes if $PwrAccDelayAct$ == 10 minutes), only for this case,  restoring it to "00 minutes" at next Ignition  On event.
```

**現行 Procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**現行 Expected Result**

```
1. Timeout1 reads 10 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**錨點 `CFTS009-4941586` 段落全文**

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
```

**錨點 `CFTS009-4941587` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
```

**錨點 `CFTS009-4941588` 段落全文**

```
IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the value specified by $PwrAccDelayAct$ (for example 10  minutes if $PwrAccDelayAct$ == 10 minutes), only for this case,  restoring it to "00 minutes" at next Ignition  On event.
```

**錨點 `CFTS009-4941589` 段落全文**

```
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

## `disclaimer wording`

### `NR1L-PowerManagement-216`　（`SWE-PM-106`）

**`test_item` 上半 verbatim**

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [SOS] the HU shall use the SOS text for the disclaimer.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the disclaimer wording to check which text the HU uses
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The HU uses the SOS text for the disclaimer
```

**錨點 `CFTS009-4941955` 段落全文**

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [SOS] the HU shall use the SOS text for the disclaimer.
```

### `NR1L-PowerManagement-217`　（`SWE-PM-107`）

**`test_item` 上半 verbatim**

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [Help] the HU shall replace the "SOS" text with the "Help" version of the disclaimer.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the disclaimer wording to check which text the HU uses
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The HU replaces the "SOS" text with the "Help" version of the disclaimer
```

**錨點 `CFTS009-4941956` 段落全文**

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [Help] the HU shall replace the "SOS" text with the "Help" version of the disclaimer.
```

### `NR1L-PowerManagement-222`　（`SWE-PM-111`）

**`test_item` 上半 verbatim**

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_Code$  does not require SOS or Geolocation) then the HU shall add the ADAS text to the disclaimer
```

**現行 Procedure**

```
1. Bring the HU to the disclaimer presentation
2. Read the disclaimer wording to check the added text
```

**現行 Expected Result**

```
1. The disclaimer screen is shown
2. The HU adds the ADAS text to the disclaimer
```

**錨點 `CFTS009-4941964` 段落全文**

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_Code$  does not require SOS or Geolocation) then the HU shall add the ADAS text to the disclaimer
```

### `NR1L-PowerManagement-223`　（`SWE-PM-111`）

**`test_item` 上半 verbatim**

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_Code$  does not require SOS or Geolocation) then the HU shall add the ADAS text to the disclaimer
```

**現行 Procedure**

```
1. Bring the HU to the disclaimer presentation
2. Read the disclaimer wording to check the added text
```

**現行 Expected Result**

```
1. The disclaimer screen is shown
2. The HU adds the ADAS text to the disclaimer
```

**錨點 `CFTS009-4941964` 段落全文**

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_Code$  does not require SOS or Geolocation) then the HU shall add the ADAS text to the disclaimer
```

## `season the HU determines`

### `NR1L-PowerManagement-255`　（`SWE-PM-096`）

**`test_item` 上半 verbatim**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**現行 Procedure**

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```

**現行 Expected Result**

```
1. The HU determines the season at Ignition On
2. The HU determines that Summer has started
```

**錨點 `CFTS009-4942091` 段落全文**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**錨點 `CFTS009-4942092` 段落全文**

```
If there has been a change in season, the HU shall play the new season startup animation.
```

**錨點 `CFTS009-4942093` 段落全文**

```
If there has not been a change in season, the HU shall play the normal Brand based startup animation.
```

**錨點 `CFTS009-4942096` 段落全文**

```
Season CalculationTo determine the correct season of the year, head unit must follow a pre-defined dates based on the meteorological definition of the seasons. It shall consider only the following seasons:- Summer starts at December, 21st ;- Fall starts at March, 20th ;- Winter starts at June, 21st ;- Spring starts at September, 23rd ;
```

### `NR1L-PowerManagement-256`　（`SWE-PM-096`）

**`test_item` 上半 verbatim**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**現行 Procedure**

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```

**現行 Expected Result**

```
1. The HU determines the season at Ignition On
2. The HU determines that Fall has started
```

**錨點 `CFTS009-4942091` 段落全文**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**錨點 `CFTS009-4942092` 段落全文**

```
If there has been a change in season, the HU shall play the new season startup animation.
```

**錨點 `CFTS009-4942093` 段落全文**

```
If there has not been a change in season, the HU shall play the normal Brand based startup animation.
```

**錨點 `CFTS009-4942096` 段落全文**

```
Season CalculationTo determine the correct season of the year, head unit must follow a pre-defined dates based on the meteorological definition of the seasons. It shall consider only the following seasons:- Summer starts at December, 21st ;- Fall starts at March, 20th ;- Winter starts at June, 21st ;- Spring starts at September, 23rd ;
```

### `NR1L-PowerManagement-257`　（`SWE-PM-096`）

**`test_item` 上半 verbatim**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**現行 Procedure**

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```

**現行 Expected Result**

```
1. The HU determines the season at Ignition On
2. The HU determines that Winter has started
```

**錨點 `CFTS009-4942091` 段落全文**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**錨點 `CFTS009-4942092` 段落全文**

```
If there has been a change in season, the HU shall play the new season startup animation.
```

**錨點 `CFTS009-4942093` 段落全文**

```
If there has not been a change in season, the HU shall play the normal Brand based startup animation.
```

**錨點 `CFTS009-4942096` 段落全文**

```
Season CalculationTo determine the correct season of the year, head unit must follow a pre-defined dates based on the meteorological definition of the seasons. It shall consider only the following seasons:- Summer starts at December, 21st ;- Fall starts at March, 20th ;- Winter starts at June, 21st ;- Spring starts at September, 23rd ;
```

### `NR1L-PowerManagement-258`　（`SWE-PM-096`）

**`test_item` 上半 verbatim**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**現行 Procedure**

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```

**現行 Expected Result**

```
1. The HU determines the season at Ignition On
2. The HU determines that Spring has started
```

**錨點 `CFTS009-4942091` 段落全文**

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

**錨點 `CFTS009-4942092` 段落全文**

```
If there has been a change in season, the HU shall play the new season startup animation.
```

**錨點 `CFTS009-4942093` 段落全文**

```
If there has not been a change in season, the HU shall play the normal Brand based startup animation.
```

**錨點 `CFTS009-4942096` 段落全文**

```
Season CalculationTo determine the correct season of the year, head unit must follow a pre-defined dates based on the meteorological definition of the seasons. It shall consider only the following seasons:- Summer starts at December, 21st ;- Fall starts at March, 20th ;- Winter starts at June, 21st ;- Spring starts at September, 23rd ;
```

## `selectable values offered for SwitchOff_Timeout_Setting.`

## `audio output against the animation start`

### `NR1L-PowerManagement-186`　（`SWE-PM-098`）

**`test_item` 上半 verbatim**

```
If $Themed_Sound$ = [Fiat Latam] and the "Welcome Onboard Sound" setting is set to "Always", the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

**現行 Procedure**

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```

**現行 Expected Result**

```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```

**錨點 `CFTS009-4941943` 段落全文**

```
If $Themed_Sound$ = [Fiat Latam] and the "Welcome Onboard Sound" setting is set to "Always", the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

### `NR1L-PowerManagement-187`　（`SWE-PM-099`）

**`test_item` 上半 verbatim**

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

**現行 Procedure**

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```

**現行 Expected Result**

```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```

**錨點 `CFTS009-4941944` 段落全文**

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

**錨點 `CFTS009-4941945` 段落全文**

```
For the purposes of CFTS009-2299, the HU shall consider it a new "day" to allow the sound to be played any time the customer selected date changes; including manual time adjustments from the user, the time passing midnight, or automatic adjustments due to time zones or Daylight Savings Time.
```

### `NR1L-PowerManagement-191`　（`SWE-PM-100`）

**`test_item` 上半 verbatim**

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Never", the HU startup animation shall not be accompanied by a startup sound that begins at the same time.
```

**現行 Procedure**

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```

**現行 Expected Result**

```
1. The HU startup animation is played
2. No startup sound accompanies the animation
```

**錨點 `CFTS009-4941947` 段落全文**

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Never", the HU startup animation shall not be accompanied by a startup sound that begins at the same time.
```

## `displayed font`

### `NR1L-PowerManagement-233`　（`SWE-PM-081`）

**`test_item` 上半 verbatim**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Chrysler font
```

**錨點 `CFTS009-4942019` 段落全文**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

### `NR1L-PowerManagement-234`　（`SWE-PM-081`）

**`test_item` 上半 verbatim**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Jeep font
```

**錨點 `CFTS009-4942019` 段落全文**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

### `NR1L-PowerManagement-235`　（`SWE-PM-081`）

**`test_item` 上半 verbatim**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Fiat font that the specification marks as DEFAULT
```

**錨點 `CFTS009-4942019` 段落全文**

```
The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid values are as follows:$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler font. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge font. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep font. $VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo font. $VC_VEH_BRAND$  = [Fiat] shall indicate Fiat font. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia font. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati font. $VC_VEH_BRAND$  = [Ram] shall indicate Ram font.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth font.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall font.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen font.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot font.
```

## `displayed App icon`

### `NR1L-PowerManagement-236`　（`SWE-PM-082`）

**`test_item` 上半 verbatim**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Chrysler App icon
```

**錨點 `CFTS009-4942025` 段落全文**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

### `NR1L-PowerManagement-237`　（`SWE-PM-082`）

**`test_item` 上半 verbatim**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Jeep App icon
```

**錨點 `CFTS009-4942025` 段落全文**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

### `NR1L-PowerManagement-238`　（`SWE-PM-082`）

**`test_item` 上半 verbatim**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU displays the Fiat App icon that the specification marks as DEFAULT
```

**錨點 `CFTS009-4942025` 段落全文**

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to display.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler App icon. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge App icon. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep App icon.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo App icon.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat App icon. (DEFAULT)$VC_VEH_BRAND$  = [Lancia] shall indicate Lancia App icon. $VC_VEH_BRAND$  = [Maserati] shall indicate Maserati App icon.$VC_VEH_BRAND$  = [Ram] shall indicate Ram App icon.$VC_VEH_BRAND$  = [Abarth] shall indicate Abarth App icon.$VC_VEH_BRAND$  = [Opel] shall indicate Opel font App icon.$VC_VEH_BRAND$  = [Vauxhall] shall indicate Vauxhall App icon.$VC_VEH_BRAND$  = [Citroen] shall indicate Citroen App icon.$VC_VEH_BRAND$  = [Peugeot] shall indicate Peugeot App icon.
```

## `call audio routing`

### `NR1L-PowerManagement-011`　（`SWE-PM-073`）

**`test_item` 上半 verbatim**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**現行 Procedure**

```
1. Send the two Load Shed signals listed in Input Test Data
2. Read the call audio routing to check that the call moved to the head set
```

**現行 Expected Result**

```
1. The TLM accepts both Load Shed signals without a bus error
2. The continuing call is routed to the head set and is not dropped
```

**錨點 `CFTS010-4942354` 段落全文**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

### `NR1L-PowerManagement-012`　（`SWE-PM-073`）

**`test_item` 上半 verbatim**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**現行 Procedure**

```
1. Send the Battery Critical signal listed in Input Test Data
2. Read the call audio routing to check that the call moved to the head set
```

**現行 Expected Result**

```
1. The TLM accepts the Battery Critical signal without a bus error
2. The continuing call is routed to the head set and is not dropped
```

**錨點 `CFTS010-4942354` 段落全文**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

## `parameters offered for user selection`

### `NR1L-PowerManagement-020`　（`SWE-PM-060`）

**`test_item` 上半 verbatim**

```
For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.
```

**現行 Procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that only one is present
```

**現行 Expected Result**

```
1. The timeout setting entry is shown in the TLM menu
2. Auto_SwitchOn_Setting.Req is the only parameter offered and SwitchOff_Timeout_Setting.Req is absent
```

**錨點 `CFTS009-4941702` 段落全文**

```
For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.
```

### `NR1L-PowerManagement-021`　（`SWE-PM-060`）

**`test_item` 上半 verbatim**

```
For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.
```

**現行 Procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that both are present
```

**現行 Expected Result**

```
1. The timeout setting entry is shown in the TLM menu
2. SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req are both offered for selection
```

**錨點 `CFTS009-4941702` 段落全文**

```
For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.
```

## `Timeout1 against the configured parameter`

### `NR1L-PowerManagement-119`　（`SWE-PM-039`）

**`test_item` 上半 verbatim**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read Timeout1 against the configured parameter to check the loaded value
```

**現行 Expected Result**

```
1. The TLM registers the value without a bus error
2. Timeout1 reads the "Switch_Off_Time" PROXI value
```

**錨點 `CFTS009-4941768` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Off Ignition On Ignition On Engine On
```

**錨點 `CFTS009-4941773` 段落全文**

```
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
```

**錨點 `CFTS009-4941774` 段落全文**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**錨點 `CFTS009-4941775` 段落全文**

```
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

### `NR1L-PowerManagement-120`　（`SWE-PM-039`）

**`test_item` 上半 verbatim**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read Timeout1 against the configured parameter to check the loaded value
```

**現行 Expected Result**

```
1. The TLM registers the value without a bus error
2. Timeout1 reads the "Switch_Off_Time" PROXI value
```

**錨點 `CFTS009-4941768` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Off Ignition On Ignition On Engine On
```

**錨點 `CFTS009-4941773` 段落全文**

```
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
```

**錨點 `CFTS009-4941774` 段落全文**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**錨點 `CFTS009-4941775` 段落全文**

```
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

## `FPDM, AMP, ICS and DTV functions`

### `NR1L-PowerManagement-123`　（`SWE-PM-041`）

**`test_item` 上半 verbatim**

```
No TLM, FPDM, AMP, ICS, and DTV functionality is available.
```

**現行 Procedure**

```
1. Bring the TLM to the status related to TLM OFF with Network on
2. Read the FPDM, AMP, ICS and DTV functions to check their availability
```

**現行 Expected Result**

```
1. The TLM reaches the status related to TLM OFF with Network on
2. No TLM, FPDM, AMP, ICS and DTV functionality is available
```

**錨點 `CFTS009-4941410` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**錨點 `CFTS009-4941411` 段落全文**

```
This status is related to TLM OFF with Network on
```

**錨點 `CFTS009-4941412` 段落全文**

```
No TLM, FPDM, AMP, ICS, and DTV functionality is available.
```

**錨點 `CFTS009-4941413` 段落全文**

```
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

### `NR1L-PowerManagement-125`　（`SWE-PM-042`）

**`test_item` 上半 verbatim**

```
No TLM, FPDM AMP, ICS, and DTV functionality is available.
```

**現行 Procedure**

```
1. Bring the TLM to the status related to TLM OFF with Network off
2. Read the FPDM, AMP, ICS and DTV functions to check their availability
```

**現行 Expected Result**

```
1. The TLM reaches the status related to TLM OFF with Network off
2. No TLM, FPDM AMP, ICS and DTV functionality is available
```

**錨點 `CFTS009-4941416` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**錨點 `CFTS009-4941417` 段落全文**

```
This status is related to TLM OFF with Network off
```

**錨點 `CFTS009-4941418` 段落全文**

```
No TLM, FPDM AMP, ICS, and DTV functionality is available.
```

**錨點 `CFTS009-4941419` 段落全文**

```
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

## `shown logo against the configured brand`

### `NR1L-PowerManagement-155`　（`SWE-PM-056`）

**`test_item` 上半 verbatim**

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo the HU displays
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```

**錨點 `CFTS009-4941680` 段落全文**

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

### `NR1L-PowerManagement-185`　（`SWE-PM-097`）

**`test_item` 上半 verbatim**

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo appears
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```

**錨點 `CFTS009-4941680` 段落全文**

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

## `applied theme against the brand signal`

### `NR1L-PowerManagement-228`　（`SWE-PM-078`）

**`test_item` 上半 verbatim**

```
If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU, the default theme based on the $VC_VEH_BRAND$ signal shall be used. See the latest version of [PDO Theme Configuration] for the default value definition.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the applied theme against the brand signal to check the fallback
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The default theme based on the $VC_VEH_BRAND$ signal is used
```

**錨點 `CFTS009-4942014` 段落全文**

```
If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU, the default theme based on the $VC_VEH_BRAND$ signal shall be used. See the latest version of [PDO Theme Configuration] for the default value definition.
```

### `NR1L-PowerManagement-229`　（`SWE-PM-078`）

**`test_item` 上半 verbatim**

```
If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU, the default theme based on the $VC_VEH_BRAND$ signal shall be used. See the latest version of [PDO Theme Configuration] for the default value definition.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the applied theme against the brand signal to check the fallback
```

**現行 Expected Result**

```
1. The HU accepts the configuration value
2. The default theme based on the $VC_VEH_BRAND$ signal is used
```

**錨點 `CFTS009-4942014` 段落全文**

```
If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU, the default theme based on the $VC_VEH_BRAND$ signal shall be used. See the latest version of [PDO Theme Configuration] for the default value definition.
```

## `$Radio_Theme$ against the applied theme`

### `NR1L-PowerManagement-231`　（`SWE-PM-080`）

**`test_item` 上半 verbatim**

```
When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. if the theme has changed, the HU will update and send the new $Radio_Theme$ within <Tsend> See the $VC_SpecialPKG$ column of the [PDO Theme Configuration] reference document for the value to send in $Radio_Theme$.
```

**現行 Procedure**

```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```

**現行 Expected Result**

```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```

**錨點 `CFTS009-4942017` 段落全文**

```
When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. if the theme has changed, the HU will update and send the new $Radio_Theme$ within <Tsend> See the $VC_SpecialPKG$ column of the [PDO Theme Configuration] reference document for the value to send in $Radio_Theme$.
```

### `NR1L-PowerManagement-246`　（`SWE-PM-086`）

**`test_item` 上半 verbatim**

```
When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. if the theme has changed, the HU will update and send the new $Radio_Theme$ within <Tsend> See the $VC_SpecialPKG$ column of the [PDO Theme Configuration] reference document for the value to send in $Radio_Theme$.
```

**現行 Procedure**

```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```

**現行 Expected Result**

```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```

**錨點 `CFTS009-4942041` 段落全文**

```
When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. if the theme has changed, the HU will update and send the new $Radio_Theme$ within <Tsend> See the $VC_SpecialPKG$ column of the [PDO Theme Configuration] reference document for the value to send in $Radio_Theme$.
```

## `shown recirc icon`

### `NR1L-PowerManagement-242`　（`SWE-PM-084`）

**`test_item` 上半 verbatim**

```
CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments.PNET: The HU shall use the $VC_VEH_LINE$ and the $VC_BODY_STYLE$ signals to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments
```

**現行 Procedure**

```
1. Send the configuration listed in Input Test Data
2. Read the shown recirc icon to check which assignment the HU applies
```

**現行 Expected Result**

```
1. The HU accepts the configuration
2. The recirc icon matches the assignment for that vehicle line and car shape
```

**錨點 `CFTS009-4942029` 段落全文**

```
CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments.PNET: The HU shall use the $VC_VEH_LINE$ and the $VC_BODY_STYLE$ signals to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments
```

### `NR1L-PowerManagement-243`　（`SWE-PM-084`）

**`test_item` 上半 verbatim**

```
CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments.PNET: The HU shall use the $VC_VEH_LINE$ and the $VC_BODY_STYLE$ signals to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments
```

**現行 Procedure**

```
1. Send the configuration listed in Input Test Data
2. Read the shown recirc icon to check which assignment the HU applies
```

**現行 Expected Result**

```
1. The HU accepts the configuration
2. The recirc icon matches the assignment for that vehicle line and body style
```

**錨點 `CFTS009-4942029` 段落全文**

```
CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments.PNET: The HU shall use the $VC_VEH_LINE$ and the $VC_BODY_STYLE$ signals to determine the correct recirc icon to display. See HMI release and PDO graphics files for ICON assignments
```

## `TLM screen content before and after StandardScreen_Time`

### `NR1L-PowerManagement-004`　（`SWE-PM-071`）

**`test_item` 上半 verbatim**

```
TLM boot requires following timings:
After SplashScreen_Time the splash screen is loaded and shown on TLM display (only if TLM has not to pass to Standby status nor to Bench status: in these cases no splash screen has to be shown);
 After StandardScreen_Time the standard screen is visualized on TLM screen
```

**現行 Procedure**

```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content before and after StandardScreen_Time to check that the standard screen is visualized
```

**現行 Expected Result**

```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized before StandardScreen_Time has elapsed, and it is visualized once that time has passed
```

**錨點 `CFTS010-4942337` 段落全文**

```
TLM boot requires following timings:
After SplashScreen_Time the splash screen is loaded and shown on TLM display (only if TLM has not to pass to Standby status nor to Bench status: in these cases no splash screen has to be shown);
 After StandardScreen_Time the standard screen is visualized on TLM screen
```

## `TLM_Status transitions during the remainder of the boot`

### `NR1L-PowerManagement-005`　（`SWE-PM-072`）

**`test_item` 上半 verbatim**

```
Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. “TLM_Status.Info setting” while the boot is still completing. TLM must buffer the events and process them as soon as possible, depending on boot timings.
```

**現行 Procedure**

```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log to check that every injected event was buffered without loss
3. Read the TLM_Status transitions during the remainder of the boot to check that every buffered event is processed
```

**現行 Expected Result**

```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The buffered event count equals the injected event count with no event dropped
3. Every buffered event is processed before the boot sequence completes and none remains pending at boot completion
```

**錨點 `CFTS010-4942338` 段落全文**

```
Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. “TLM_Status.Info setting” while the boot is still completing. TLM must buffer the events and process them as soon as possible, depending on boot timings.
```

## `three stored variables`

### `NR1L-PowerManagement-049`　（`SWE-PM-012`）

**`test_item` 上半 verbatim**

```
After a battery reconnection and also when TLM has to exit INIT state (as soon as the voltage is limited within certain thresholds), TLM is able to work properly again and it has to restore the last user settings and the last variables values: VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to their values before the battery disconnection / battery reset
```

**現行 Procedure**

```
1. Reconnect the battery and let the voltage settle within its thresholds
2. Read the three stored variables to check that their previous values returned
```

**現行 Expected Result**

```
1. The TLM leaves INIT state once the voltage is within its thresholds
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req read their values before the battery disconnection
```

**錨點 `CFTS009-4941449` 段落全文**

```
After a battery reconnection and also when TLM has to exit INIT state (as soon as the voltage is limited within certain thresholds), TLM is able to work properly again and it has to restore the last user settings and the last variables values: VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to their values before the battery disconnection / battery reset
```

**錨點 `CFTS009-4941450` 段落全文**

```
Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Info to "Sleep" first and starting from Sleep state.
```

## `TLM_Status.Info and the state machine`

### `NR1L-PowerManagement-050`　（`SWE-PM-012`）

**`test_item` 上半 verbatim**

```
Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Info to "Sleep" first and starting from Sleep state.
```

**現行 Procedure**

```
1. Let the TLM exit INIT state
2. Read TLM_Status.Info and the state machine to check the starting state
```

**現行 Expected Result**

```
1. The TLM leaves INIT state without an error being reported
2. TLM_Status.Info reads "Sleep" and the TLM starts from Sleep state
```

**錨點 `CFTS009-4941449` 段落全文**

```
After a battery reconnection and also when TLM has to exit INIT state (as soon as the voltage is limited within certain thresholds), TLM is able to work properly again and it has to restore the last user settings and the last variables values: VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to their values before the battery disconnection / battery reset
```

**錨點 `CFTS009-4941450` 段落全文**

```
Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Info to "Sleep" first and starting from Sleep state.
```

## `AMP, ICS and DTV power states and the audio paths`

### `NR1L-PowerManagement-055`　（`SWE-PM-013`）

**`test_item` 上半 verbatim**

```
This status is related to TLM OFF. AMP/ICS/DTV shall be OFF. Audio for ANC, ACN, and chimes (if equipped) shall be active in this state)
```

**現行 Procedure**

```
1. Let the TLM settle in Partial Operation
2. Read the AMP, ICS and DTV power states and the audio paths to check the active set
```

**現行 Expected Result**

```
1. The TLM stays in Partial Operation without further transition
2. AMP, ICS and DTV are OFF while audio for ANC, ACN and chimes is active
```

**錨點 `CFTS009-4941391` 段落全文**

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On, Ignition Off Ignition Pre-Off
```

**錨點 `CFTS009-4941392` 段落全文**

```
In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Active" is recieved and TLM sends $Telematic_Power$ = "Partial_Operation"
```

**錨點 `CFTS009-4941393` 段落全文**

```
This status is related to TLM OFF. AMP/ICS/DTV shall be OFF. Audio for ANC, ACN, and chimes (if equipped) shall be active in this state)
```

**錨點 `CFTS009-4941394` 段落全文**

```
All TLM, AMP, ICS, and DTV functionalities run in background and are ready but not HMI interaction is enabled within this status, except for the interaction that permit a change status.
```

## `TLM_Status.Info and the screen content`

### `NR1L-PowerManagement-081`　（`SWE-PM-021`）

**`test_item` 上半 verbatim**

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info passes from "False" to "True"THENTLM stays in Idle state but allows its screen only to show the rear view camera video on its screen.Refer to VF551 for details about video availability requirements on TLM screen state.
```

**現行 Procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and the screen content to check what the screen shows
```

**現行 Expected Result**

```
1. The TLM registers the transition without leaving Idle state
2. The screen shows the rear view camera video and nothing else
```

**錨點 `CFTS009-4941560` 段落全文**

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info passes from "False" to "True"THENTLM stays in Idle state but allows its screen only to show the rear view camera video on its screen.Refer to VF551 for details about video availability requirements on TLM screen state.
```

## `remote start outcome flags and the TLM state`

### `NR1L-PowerManagement-116`　（`SWE-PM-036`）

**`test_item` 上半 verbatim**

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal STATUS_BH_BCM2.RemStActvSts has a transition from "Remote Start Not Active" to “Remote Start Active”THENTLM has to set RemStartFail ="False" AND VPLastStatus = "On"AND TLM_Status.Info and $Telematic_Power$ to “Partial-Operation” value and it passes to TLM Partial Operation state.
```

**現行 Procedure**

```
1. Send the transition listed in Input Test Data
2. Read the remote start outcome flags and the TLM state to check the resulting behavior
```

**現行 Expected Result**

```
1. RemStartFail reads "False" and VPLastStatus reads "On"
2. TLM_Status.Info and $Telematic_Power$ read "Partial-Operation" and the TLM passes to TLM Partial Operation state
```

**錨點 `CFTS009-4941654` 段落全文**

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal STATUS_BH_BCM2.RemStActvSts has a transition from "Remote Start Not Active" to “Remote Start Active”THENTLM has to set RemStartFail ="False" AND VPLastStatus = "On"AND TLM_Status.Info and $Telematic_Power$ to “Partial-Operation” value and it passes to TLM Partial Operation state.
```

## `TLM state against the operative state management rules`

### `NR1L-PowerManagement-118`　（`SWE-PM-039`）

**`test_item` 上半 verbatim**

```
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the TLM state against the operative state management rules to check the resulting behavior
```

**現行 Expected Result**

```
1. The TLM registers the value without a bus error
2. The TLM behaves as for an Ignition Pre Off or Ignition Off event
```

**錨點 `CFTS009-4941768` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Off Ignition On Ignition On Engine On
```

**錨點 `CFTS009-4941773` 段落全文**

```
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
```

**錨點 `CFTS009-4941774` 段落全文**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**錨點 `CFTS009-4941775` 段落全文**

```
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

## `offered items against the TLM HMI documents`

### `NR1L-PowerManagement-121`　（`SWE-PM-039`）

**`test_item` 上半 verbatim**

```
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

**現行 Procedure**

```
1. Browse the menu items offered by the TLM
2. Read the offered items against the TLM HMI documents to check what is guaranteed
```

**現行 Expected Result**

```
1. The menu is reachable in the Timed status
2. Only TLM menu items that are not related to vehicle setup are guaranteed
```

**錨點 `CFTS009-4941768` 段落全文**

```
In the following "Ignition Working Conditions": Ignition Off Ignition On Ignition On Engine On
```

**錨點 `CFTS009-4941773` 段落全文**

```
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
```

**錨點 `CFTS009-4941774` 段落全文**

```
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
```

**錨點 `CFTS009-4941775` 段落全文**

```
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

## `user selectable parameter on an ex-factory unit`

### `NR1L-PowerManagement-143`　（`SWE-PM-048`）

**`test_item` 上半 verbatim**

```
Default:         The ex-factory default must be "Auto_SwitchOn_Setting.Req == Recall_Last" AND VPLastStatus == On.
```

**現行 Procedure**

```
1. Read the user selectable parameter on an ex-factory unit
2. Read the stored last status to check the ex-factory default of this clause
```

**現行 Expected Result**

```
1. Auto_SwitchOn_Setting.Req reads "Recall_Last"
2. VPLastStatus reads "On"
```

**錨點 `CFTS009-4941603` 段落全文**

```
IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activation.Req back to "False" value AND it is possible to have three possible scenarios depending on user selectable parameter Auto_SwitchOn_Setting.Req
```

**錨點 `CFTS009-4941605` 段落全文**

```
Behaviour 1: "Auto_SwitchOn_Setting.Req == Active"After the LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation state
```

**錨點 `CFTS009-4941608` 段落全文**

```
Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":         After the LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state
```

**錨點 `CFTS009-4941610` 段落全文**

```
Behaviour 3: "Auto_SwitchOn_Setting.Req  == Recall_Last":IF VPLastStatus == ON then TLM sets TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation stateIF VPLastStatus == OFF then TLM sets TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state
```

**錨點 `CFTS009-4941611` 段落全文**

```
Default:         The ex-factory default must be "Auto_SwitchOn_Setting.Req == Recall_Last" AND VPLastStatus == On.
```

## `shown logo against the configured parameter`

### `NR1L-PowerManagement-148`　（`SWE-PM-053`）

**`test_item` 上半 verbatim**

```
TLM has to read Brand_Configuration_2 PROXI parameter in order to show the vehicle brand logo screen.
```

**現行 Procedure**

```
1. Bring the TLM to the brand logo screen presentation
2. Read the shown logo against the configured parameter to check the source of the logo
```

**現行 Expected Result**

```
1. The brand logo screen is presented
2. The vehicle brand logo shown matches the Brand_Configuration_2 PROXI parameter
```

**錨點 `CFTS009-4941668` 段落全文**

```
TLM has to read Brand_Configuration_2 PROXI parameter in order to show the vehicle brand logo screen.
```

## `user selectable timeout parameter on an ex-factory unit`

### `NR1L-PowerManagement-156`　（`SWE-PM-058`）

**`test_item` 上半 verbatim**

```
Default:The ex-factory default must be "SwitchOff_Timeout_Setting.Req == 00 MIN" and  (Auto_SwitchOn_Setting.Req =="Active", and  Timeout1 == 00 MIN" for LTM High Radio)
```

**現行 Procedure**

```
1. Read the user selectable timeout parameter on an ex-factory unit
2. Read the auto switch on parameter and Timeout1 to check the ex-factory default of this clause
```

**現行 Expected Result**

```
1. SwitchOff_Timeout_Setting.Req reads "00 MIN"
2. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"
```

**錨點 `CFTS009-4941509` 段落全文**

```
Default:The ex-factory default must be "SwitchOff_Timeout_Setting.Req == 00 MIN" and  (Auto_SwitchOn_Setting.Req =="Active", and  Timeout1 == 00 MIN" for LTM High Radio)
```

## `HU mode after the idle period`

### `NR1L-PowerManagement-169`　（`SWE-PM-075`）

**`test_item` 上半 verbatim**

```
If the HU Transitions to Timed mode due to the condition described in CFTS009-1809, the HU shall transition to Standby mode after: -1 minute has passed without the user interacting with the pop-up -The FOTA pop up is dismissed -$ACCDlyAct$ transitions from active to inactive
```

**現行 Procedure**

```
1. Leave the FOTA pop-up without any user interaction
2. Read the HU mode after the idle period to check the transition
```

**現行 Expected Result**

```
1. The pop-up stays on the screen while no interaction occurs
2. The HU transitions to Standby mode after 1 minute has passed
```

**錨點 `CFTS009-4941977` 段落全文**

```
If the HU Transitions to Timed mode due to the condition described in CFTS009-1809, the HU shall transition to Standby mode after: -1 minute has passed without the user interacting with the pop-up -The FOTA pop up is dismissed -$ACCDlyAct$ transitions from active to inactive
```

## `both processors`

## `screen against the elapsed time`

### `NR1L-PowerManagement-182`　（`SWE-PM-093`）

**`test_item` 上半 verbatim**

```
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
```

**現行 Procedure**

```
1. Close the driver door again within the same CAN wakeup cycle
2. Read the screen against the elapsed time to check the replay rule
```

**現行 Expected Result**

```
1. No further start-up animation is played
2. A start-up animation plays again only at the next CAN wakeup cycle or after 30 minutes, whichever is greater
```

**錨點 `CFTS009-4941301` 段落全文**

```
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
```

**錨點 `CFTS009-4941941` 段落全文**

```
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
```

## `ICS functions and the DTV`

### `NR1L-PowerManagement-202`　（`SWE-PM-103`）

**`test_item` 上半 verbatim**

```
This status is related to TLM audio is OFF. TLM shall allow only Splash Screen visualization on its display.  ICS functionalities are available.  DTV shall be OFF.
```

**現行 Procedure**

```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the ICS functions and the DTV to check their availability
```

**現行 Expected Result**

```
1. ICS functionalities are available
2. DTV is OFF
```

**錨點 `CFTS009-4941364` 段落全文**

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

**錨點 `CFTS009-4941365` 段落全文**

```
This status is related to TLM audio is OFF. TLM shall allow only Splash Screen visualization on its display.  ICS functionalities are available.  DTV shall be OFF.
```

## `screen across the cycles`

### `NR1L-PowerManagement-218`　（`SWE-PM-108`）

**`test_item` 上半 verbatim**

```
If $VC_VEH_BRAND$ <> [Maserati] the R1 Head Unit shall only show the core disclaimer screen once every 30 ignition cycles
```

**現行 Procedure**

```
1. Run the head unit through consecutive ignition cycles
2. Read the screen across the cycles to check how often the disclaimer appears
```

**現行 Expected Result**

```
1. The core disclaimer screen is shown on the first ignition cycle
2. The core disclaimer screen is shown only once every 30 ignition cycles
```

**錨點 `CFTS009-4941958` 段落全文**

```
If $VC_VEH_BRAND$ <> [Maserati] the R1 Head Unit shall only show the core disclaimer screen once every 30 ignition cycles
```

## `shown element`

### `NR1L-PowerManagement-230`　（`SWE-PM-079`）

**`test_item` 上半 verbatim**

```
For all of the PDO branded elements listed, if the CAN signals referenced indicate a value that is not supported by the HU, the default value defined by PDO shall be used. See the latest version of [PDO Theme Configuration] and the "Theme Name" defaults for the values to use.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown element to check which value the HU falls back to
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The default value defined by PDO is used for that branded element
```

**錨點 `CFTS009-4942015` 段落全文**

```
For all of the PDO branded elements listed, if the CAN signals referenced indicate a value that is not supported by the HU, the default value defined by PDO shall be used. See the latest version of [PDO Theme Configuration] and the "Theme Name" defaults for the values to use.
```

## `shown seat graphic against the brand signal`

### `NR1L-PowerManagement-249`　（`SWE-PM-087`）

**`test_item` 上半 verbatim**

```
If $VC_VEH_LINE$ = [M240] The HU Shall use the M240 seat graphics.  If $VC_VEH_LINE$ <> [M240]The HU shall use $VC_VEH_BRAND$ to determine the correct settings seat graphic display.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown seat graphic against the brand signal to check the source
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The HU uses $VC_VEH_BRAND$ to determine the settings seat graphic
```

**錨點 `CFTS009-4942054` 段落全文**

```
If $VC_VEH_LINE$ = [M240] The HU Shall use the M240 seat graphics.  If $VC_VEH_LINE$ <> [M240]The HU shall use $VC_VEH_BRAND$ to determine the correct settings seat graphic display.
```

## `shown gauges`

### `NR1L-PowerManagement-250`　（`SWE-PM-088`）

**`test_item` 上半 verbatim**

```
The HU shall use the $VC_VEH_LINE$ signal to determine the correct performance gauges to display. See HMI release and PDO graphics files for performance gauge assignments.
```

**現行 Procedure**

```
1. Send the value listed in Input Test Data
2. Read the shown gauges to check which assignment the HU applies
```

**現行 Expected Result**

```
1. The HU accepts the signal value
2. The performance gauges match the assignment for that vehicle line
```

**錨點 `CFTS009-4942064` 段落全文**

```
The HU shall use the $VC_VEH_LINE$ signal to determine the correct performance gauges to display. See HMI release and PDO graphics files for performance gauge assignments.
```

## `audio power amplifier and the BoosterOUT states`

### `NR1L-PowerManagement-281`　（`SWE-PM-007`）

**`test_item` 上半 verbatim**

```
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
```

**現行 Procedure**

```
1. Read the audio power amplifier and the BoosterOUT states
2. Read the analog and digital antenna supplies
3. Read the USB and AUX MCU states to check that both are on
```

**現行 Expected Result**

```
1. The audio power amplifier is ON and not muted, and the BoosterOUT is ON
2. The analog and digital antenna supplies are ON
3. The USB and AUX MCU are ON when present
```

**錨點 `CFTS009-4941354` 段落全文**

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941355` 段落全文**

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941422` 段落全文**

```
In the "Ignition Working Conditions" "Ignition Off"
```

**錨點 `CFTS009-4941423` 段落全文**

```
This status is related to TLM AMP, ICS, and DTV ON only for testing, diagnostics and development of TLM component, relatively to Engineering Line.
```

**錨點 `CFTS009-4941453` 段落全文**

```
TLM Internal State
Source
Audio Power amplifier
Display / Illumination
BoosterOUT
Antenna / Analog tuner
Antenna / Digital tuner
MCU (USB)
MCU (AUX)
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Idle
OFF (None)  
ON (Muted) (***)
OFF (*) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Partial Operation
OFF (None)
OFF
OFF(**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Standby
OFF (None)
OFF
OFF (**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Sleep
OFF (None)
OFF
OFF (**) DCSD powered off, screen off, no backlight
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Logistic Idle
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Standby
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Sleep
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Init
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
```

## `analog and digital antenna supplies`

### `NR1L-PowerManagement-281`　（`SWE-PM-007`）

**`test_item` 上半 verbatim**

```
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
```

**現行 Procedure**

```
1. Read the audio power amplifier and the BoosterOUT states
2. Read the analog and digital antenna supplies
3. Read the USB and AUX MCU states to check that both are on
```

**現行 Expected Result**

```
1. The audio power amplifier is ON and not muted, and the BoosterOUT is ON
2. The analog and digital antenna supplies are ON
3. The USB and AUX MCU are ON when present
```

**錨點 `CFTS009-4941354` 段落全文**

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941355` 段落全文**

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941422` 段落全文**

```
In the "Ignition Working Conditions" "Ignition Off"
```

**錨點 `CFTS009-4941423` 段落全文**

```
This status is related to TLM AMP, ICS, and DTV ON only for testing, diagnostics and development of TLM component, relatively to Engineering Line.
```

**錨點 `CFTS009-4941453` 段落全文**

```
TLM Internal State
Source
Audio Power amplifier
Display / Illumination
BoosterOUT
Antenna / Analog tuner
Antenna / Digital tuner
MCU (USB)
MCU (AUX)
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Idle
OFF (None)  
ON (Muted) (***)
OFF (*) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Partial Operation
OFF (None)
OFF
OFF(**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Standby
OFF (None)
OFF
OFF (**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Sleep
OFF (None)
OFF
OFF (**) DCSD powered off, screen off, no backlight
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Logistic Idle
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Standby
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Sleep
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Init
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
```

## `USB and AUX MCU states`

### `NR1L-PowerManagement-281`　（`SWE-PM-007`）

**`test_item` 上半 verbatim**

```
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
```

**現行 Procedure**

```
1. Read the audio power amplifier and the BoosterOUT states
2. Read the analog and digital antenna supplies
3. Read the USB and AUX MCU states to check that both are on
```

**現行 Expected Result**

```
1. The audio power amplifier is ON and not muted, and the BoosterOUT is ON
2. The analog and digital antenna supplies are ON
3. The USB and AUX MCU are ON when present
```

**錨點 `CFTS009-4941354` 段落全文**

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941355` 段落全文**

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

**錨點 `CFTS009-4941422` 段落全文**

```
In the "Ignition Working Conditions" "Ignition Off"
```

**錨點 `CFTS009-4941423` 段落全文**

```
This status is related to TLM AMP, ICS, and DTV ON only for testing, diagnostics and development of TLM component, relatively to Engineering Line.
```

**錨點 `CFTS009-4941453` 段落全文**

```
TLM Internal State
Source
Audio Power amplifier
Display / Illumination
BoosterOUT
Antenna / Analog tuner
Antenna / Digital tuner
MCU (USB)
MCU (AUX)
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Idle
OFF (None)  
ON (Muted) (***)
OFF (*) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Partial Operation
OFF (None)
OFF
OFF(**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Standby
OFF (None)
OFF
OFF (**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Sleep
OFF (None)
OFF
OFF (**) DCSD powered off, screen off, no backlight
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates  
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Logistic Idle
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Standby
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Sleep
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Init
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
```
