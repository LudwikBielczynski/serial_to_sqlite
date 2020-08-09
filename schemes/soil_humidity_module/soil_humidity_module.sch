EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:Battery BT1
U 1 1 5F267CFE
P 3300 4000
F 0 "BT1" H 3408 4046 50  0000 L CNN
F 1 "Battery" H 3408 3955 50  0000 L CNN
F 2 "" V 3300 4060 50  0001 C CNN
F 3 "~" V 3300 4060 50  0001 C CNN
	1    3300 4000
	1    0    0    -1  
$EndComp
$Comp
L MCU_Module:Arduino_Nano_v3.x A1
U 1 1 5F2667E0
P 6650 3950
F 0 "A1" V 6700 3900 50  0000 R CNN
F 1 "Arduino_Nano_v3.x" V 6600 4200 50  0000 R CNN
F 2 "Module:Arduino_Nano" H 6650 3950 50  0001 C CIN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 6650 3950 50  0001 C CNN
	1    6650 3950
	1    0    0    -1  
$EndComp
Text GLabel 6150 4550 0    50   Input ~ 0
U1_MISO
Text GLabel 4100 3850 0    50   Output ~ 0
A1_D12
Text GLabel 4100 3950 0    50   Output ~ 0
A1_D13
Text GLabel 6150 4650 0    50   Input ~ 0
U1_SCK
Text GLabel 6150 4450 0    50   Input ~ 0
U1_MOSI
Text GLabel 4100 3750 0    50   Output ~ 0
A1_D11
Text GLabel 4100 4050 0    50   Output ~ 0
A1_D9
Text GLabel 6150 4250 0    50   Output ~ 0
U1_CSN
Text GLabel 4100 4250 0    50   Input ~ 0
A1_D8
Text GLabel 6150 4150 0    50   Input ~ 0
U1_CE
Wire Wire Line
	3300 5150 4600 5150
Wire Wire Line
	3300 4200 3300 5150
Wire Wire Line
	4600 5050 4600 5150
Wire Wire Line
	6650 5150 6650 4950
Connection ~ 4600 5150
$Comp
L Device:R R3
U 1 1 5F2DE1F5
P 7550 3900
F 0 "R3" H 7620 3946 50  0000 L CNN
F 1 "10k" H 7620 3855 50  0000 L CNN
F 2 "" V 7480 3900 50  0001 C CNN
F 3 "~" H 7550 3900 50  0001 C CNN
	1    7550 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5F2E0DD1
P 7550 4400
F 0 "R4" H 7620 4446 50  0000 L CNN
F 1 "1k" H 7620 4355 50  0000 L CNN
F 2 "" V 7480 4400 50  0001 C CNN
F 3 "~" H 7550 4400 50  0001 C CNN
	1    7550 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7550 5150 7550 4550
Connection ~ 6650 5150
Wire Wire Line
	7550 4050 7550 4150
Connection ~ 7550 4150
Wire Wire Line
	7550 4150 7550 4250
Wire Wire Line
	5800 3750 6150 3750
$Comp
L Device:R R1
U 1 1 5F31B617
P 5150 2750
F 0 "R1" H 5220 2796 50  0000 L CNN
F 1 "10k" H 5220 2705 50  0000 L CNN
F 2 "" V 5080 2750 50  0001 C CNN
F 3 "~" H 5150 2750 50  0001 C CNN
	1    5150 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 2700 4600 2600
Wire Wire Line
	4600 3100 4600 3450
$Comp
L trial:IRL540N Q1
U 1 1 5F29F1A2
P 4700 2900
F 0 "Q1" H 4905 2854 50  0000 L CNN
F 1 "IRL540N" H 4905 2945 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4950 2825 50  0001 L CIN
F 3 "https://www.infineon.com/dgdl/irl540npbf.pdf?fileId=5546d462533600a40153565fc2a62567" H 4700 2900 50  0001 L CNN
	1    4700 2900
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4900 2900 5150 2900
Wire Wire Line
	5800 2900 5800 3100
Connection ~ 5150 2900
Wire Wire Line
	5150 2900 5800 2900
$Comp
L Device:R R2
U 1 1 5F322358
P 5800 3250
F 0 "R2" H 5870 3296 50  0000 L CNN
F 1 "R" H 5870 3205 50  0000 L CNN
F 2 "" V 5730 3250 50  0001 C CNN
F 3 "~" H 5800 3250 50  0001 C CNN
	1    5800 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 3400 5800 3750
Wire Wire Line
	7150 4150 7550 4150
Wire Wire Line
	4600 5150 6650 5150
$Comp
L trial:SEN0193 U2
U 1 1 5F33FAC0
P 8600 3850
F 0 "U2" V 8646 3520 50  0000 R CNN
F 1 "SEN0193" V 8555 3520 50  0000 R CNN
F 2 "" H 8500 3450 50  0001 C CNN
F 3 "" H 8500 3450 50  0001 C CNN
	1    8600 3850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8100 3850 8100 2800
Text GLabel 8400 3750 0    50   Output ~ 0
A1_A0
Wire Wire Line
	8100 3850 8400 3850
Wire Wire Line
	8100 3950 8400 3950
Text GLabel 7150 3950 2    50   Input ~ 0
U2_A0
Wire Wire Line
	6650 5150 7550 5150
Wire Wire Line
	6750 2950 6750 2800
Wire Wire Line
	8100 3950 8100 4400
$Comp
L Transistor_BJT:BC547 Q2
U 1 1 5F3574C8
P 8200 4600
F 0 "Q2" H 8391 4646 50  0000 L CNN
F 1 "BC547" H 8391 4555 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 8400 4525 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 8200 4600 50  0001 L CNN
	1    8200 4600
	-1   0    0    1   
$EndComp
Text GLabel 8400 4600 2    50   Input ~ 0
U1_D5
Text GLabel 6150 3850 0    50   Output ~ 0
Q2_B
Wire Wire Line
	8100 4800 8100 5150
Wire Wire Line
	6750 2800 8100 2800
Wire Wire Line
	7550 5150 8100 5150
Connection ~ 7550 5150
$Comp
L RF:nRF24L01P U1
U 1 1 5F26A887
P 4700 4250
F 0 "U1" H 4650 4050 50  0000 L CNN
F 1 "nRF24L01P" H 4500 4150 50  0000 L CNN
F 2 "Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm" V 4609 5093 50  0001 L CIN
F 3 "http://www.nordicsemi.com/eng/content/download/2726/34069/file/nRF24L01P_Product_Specification_1_0.pdf" H 4700 4350 50  0001 C CNN
	1    4700 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 2450 4600 2450
Wire Wire Line
	3300 2450 3300 3800
Wire Wire Line
	7550 2450 7550 3750
Wire Wire Line
	6550 2450 6550 2950
Connection ~ 6550 2450
Wire Wire Line
	6550 2450 7550 2450
Wire Wire Line
	5150 2600 4600 2600
Wire Wire Line
	4600 2600 4600 2450
Connection ~ 4600 2600
Connection ~ 4600 2450
Wire Wire Line
	4600 2450 6550 2450
$EndSCHEMATC
