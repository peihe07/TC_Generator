# 第四批素材（R-P174）—— 逐字原文

> R-P174 之範圍 `SWE-PM-033`–`063` 共 **31** leaf；
> **已於第二批產出者 6**（`SWE-PM-038`、`SWE-PM-057`、`SWE-PM-060`、`SWE-PM-061`、`SWE-PM-062`、`SWE-PM-063`），
> **本批實際待產出 25 leaf**。落差見上繳 §五。

> 原文取自 CFTS 文字層（R-P17），**未經任何改寫**；`source_clause` 即此串接（G94 之比對對象）。

## `SWE-PM-033` —— 章節 1.6.2.1.15（item 2，有內文 2）

- 錨點：`4941634,4941635`

```
IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation"AND signal LTM_OperationalModeSts has a transition to "Ignition Pre Off" OR to "Ignition Off" valueTHEN
TLM has to set TLM_Status.Info and $Telematic_Power$ to "Standby" value and it passes to TLM Standby state.
```

## `SWE-PM-034` —— 章節 1.6.2.1.15（item 3，有內文 3）

- 錨點：`4941638,4941639,4941641`

```
IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation"
AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” value)
THEN TLM has to set signal Antitheft_Activation.Req to "True" value. AND TLM has to show a proper Splash Screen, depending on  "Splash Screen logo visualization" logics, for Response_Wait_Time
```

## `SWE-PM-035` —— 章節 1.6.2.1.15（item 4，有內文 4）

- 錨點：`4941649,4941650,4941651,4941652`

```
IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activation.Req back to "False" value ANDit is possible to have three possible scenarios depending on user selectable parameter Auto_SwitchOn_Setting.Req
Behaviour 1: "Auto_SwitchOn_Setting.Req == Active":TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time. At Response_wait_Time expired TLM has to set VPLastStatus to “On” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation state.
Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":TLM has to set VPLastStatus to “Off” value and TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state.
Behaviour 3: "Auto_SwitchOn_Setting.Req  == Recall_Last":IF VPLastStatus == On TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time. At Response_wait_Time expired then TLM sets TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation stateIF VPLastStatus == Off then TLM sets TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state.
```

## `SWE-PM-036` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941654`

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal STATUS_BH_BCM2.RemStActvSts has a transition from "Remote Start Not Active" to “Remote Start Active”THENTLM has to set RemStartFail ="False" AND VPLastStatus = "On"AND TLM_Status.Info and $Telematic_Power$ to “Partial-Operation” value and it passes to TLM Partial Operation state.
```

## `SWE-PM-037` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941655`

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed" AND PhoneCall.Info becames "not Active"AND RemStartFail ==“True”THENTLM has to set RemStartFail  to “False” value and  TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.
```

## `SWE-PM-039` —— 章節 1.7.1.1.1（item 4，有內文 4）

- 錨點：`4941768,4941773,4941774,4941775`

```
In the following "Ignition Working Conditions": Ignition Off Ignition On Ignition On Engine On
IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs, according to par. "TLM Operative state management".
IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.Req was equal to "00 min" or (Auto_SwitchOn_Setting.Req == Active for LTM High Radio), then TLM has to set Timeout1 to the "Switch_Off_Time" PROXI value.
IF TLM passes to Timed status due to this two conditions, THEN only TLM menu items (not related to vehicle setup) must be guaranteed. See TLM HMI documents for TLM items.
```

## `SWE-PM-040` —— 章節 1.9.12（item 1，有內文 1）

- 錨點：`4941990`

```
When the HU shall power down in a normal sequence into Suspend to RAM. The following action shall be taken:If Suspend to RAM is allowed, HU shall start an 8 day timer and shall enter low power mode.
```

## `SWE-PM-041` —— 章節 1.6.2.1.6（item 4，有內文 4）

- 錨點：`4941410,4941411,4941412,4941413`

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
This status is related to TLM OFF with Network on
No TLM, FPDM, AMP, ICS, and DTV functionality is available.
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

## `SWE-PM-042` —— 章節 1.6.2.1.7（item 4，有內文 4）

- 錨點：`4941416,4941417,4941418,4941419`

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
This status is related to TLM OFF with Network off
No TLM, FPDM AMP, ICS, and DTV functionality is available.
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

## `SWE-PM-043` —— 章節 1.9.5（item 1，有內文 1）

- 錨點：`4941895`

```
The HU shall keep the backlight OFF during Standby mode except if it is required to display an HMI screen.
```

## `SWE-PM-044` —— 章節 1.6.2.1.15（item 2，有內文 2）

- 錨點：`4941578,4941584`

```
IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” value with Engineering Line deactivatedTHENTLM has to set signal Antitheft_Activation.Req to "True" value AND TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization", for Response_Wait_Time. For Splash Screen logo, refer to TLM HMI Specification
IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” value with Engineering Line deactivatedTHENTLM has to set signal Antitheft_Activation.Req to "True" value AND TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization", for Response_Wait_Time. For Splash Screen logo, refer to TLM HMI Specification
```

## `SWE-PM-045` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941585`

```
IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.Req back to "False" value and to stay in the original state (Standby OR Sleep), showing proper HMI Antitheft screens if needed, for a maximum time equal to Timeout1.
```

## `SWE-PM-046` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941601`

```
IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == "True" THENeven IF Antitheft_Result.Info is still equal to "In_Progress" or "Not_Successfully", TLM shall provide audio and video for rear view camera component, as soon as the images are available on TLM and as long as Rear_Camera_Enable.Info == "True".Refer to VF551 for details about video availability requirements on TLM screen
```

## `SWE-PM-047` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941602`

```
IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.Req back to "False" value and to stay in the original state (Standby OR Sleep),  showing proper HMI Antitheft screens, if needed (see VF210).
```

## `SWE-PM-048` —— 章節 1.6.2.1.15（item 5，有內文 5）

- 錨點：`4941603,4941605,4941608,4941610,4941611`

```
IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activation.Req back to "False" value AND it is possible to have three possible scenarios depending on user selectable parameter Auto_SwitchOn_Setting.Req
Behaviour 1: "Auto_SwitchOn_Setting.Req == Active"After the LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation state
Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":         After the LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state
Behaviour 3: "Auto_SwitchOn_Setting.Req  == Recall_Last":IF VPLastStatus == ON then TLM sets TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and it passes to TLM Full-Operation stateIF VPLastStatus == OFF then TLM sets TLM_Status.Info and $Telematic_Power$ to "Idle" value and it passes to TLM Idle state
Default:         The ex-factory default must be "Auto_SwitchOn_Setting.Req == Recall_Last" AND VPLastStatus == On.
```

## `SWE-PM-049` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941623`

```
IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.Req back to "False" value and to stay blocked in Idle state (see VF210 for blocked meaning), showing proper HMI Antitheft screens, if needed (see VF210).
```

## `SWE-PM-050` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941624`

```
ELSE TLM sets VPLastStatus to "Off" value and sets TLM_Status.Info and $Telematic_Power$ to “Idle” and then it passes to Idle state.
```

## `SWE-PM-051` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941643`

```
IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activation.Req back to "False" value ANDTLM has to set VPLastStatus to “On” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation"   value and then it passes to TLM Full-Operation state.
```

## `SWE-PM-052` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941648`

```
IF Antitheft_Result.Info == "Not_Successfully"THEN TLM has to set Antitheft_Activation.Req back to "False" value and to stay in the original state (Partial Operation),  showing proper HMI Antitheft screens, if needed (see VF210).
```

## `SWE-PM-053` —— 章節 1.6.2.1.16（item 1，有內文 1）

- 錨點：`4941668`

```
TLM has to read Brand_Configuration_2 PROXI parameter in order to show the vehicle brand logo screen.
```

## `SWE-PM-054` —— 章節 1.6.2.1.16（item 4，有內文 4）

- 錨點：`4941673,4941674,4941675,4941676`

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

## `SWE-PM-055` —— 章節 1.6.2.1.16（item 1，有內文 1）

- 錨點：`4941678`

```
The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ =    [2025] and $VC_VEH_LINE$ = [DT].      The ETM shall use $SplashScreen_Type$ = [Klipsch (7)]  to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ > [2025] and $VC_VEH_LINE$ = [DT].
```

## `SWE-PM-056` —— 章節 1.6.2.1.16（item 1，有內文 1）

- 錨點：`4941680`

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

## `SWE-PM-058` —— 章節 1.6.2.1.15（item 1，有內文 1）

- 錨點：`4941509`

```
Default:The ex-factory default must be "SwitchOff_Timeout_Setting.Req == 00 MIN" and  (Auto_SwitchOn_Setting.Req =="Active", and  Timeout1 == 00 MIN" for LTM High Radio)
```

## `SWE-PM-059` —— 章節 1.6.2.1.15（item 2，有內文 2）

- 錨點：`4941616,4941617`

```
IF TLM_Status.Info and $Telematic_Power$ == "Standby"AND a Network Sleep request occursTHEN, provided that the boot of TLM has been completed, TLM has to set TLM_Status.Info and $Telematic_Power$ to “Sleep” value and then it has to pass to Sleep state AND Shutdown_Time starts.
If TLM Boot is not ended, TLM has to wait for its end before passing to Sleep state and starting the Shutdown_Time.
```
