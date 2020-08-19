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
F 2 "Connector_AMASS:AMASS_XT30U-F_1x02_P5.0mm_Vertical" V 3300 4060 50  0001 C CNN
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
MISO
Text GLabel 6150 4650 0    50   Output ~ 0
SCK
Text GLabel 6150 4450 0    50   Output ~ 0
MOSI
Text GLabel 6150 4250 0    50   Output ~ 0
CSN
Text GLabel 6150 4150 0    50   Output ~ 0
CE
$Comp
L Device:R R3
U 1 1 5F2DE1F5
P 7550 3900
F 0 "R3" H 7620 3946 50  0000 L CNN
F 1 "100k" H 7620 3855 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7480 3900 50  0001 C CNN
F 3 "~" H 7550 3900 50  0001 C CNN
	1    7550 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5F2E0DD1
P 7550 4400
F 0 "R4" H 7620 4446 50  0000 L CNN
F 1 "10k" H 7620 4355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7480 4400 50  0001 C CNN
F 3 "~" H 7550 4400 50  0001 C CNN
	1    7550 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7550 4050 7550 4150
Connection ~ 7550 4150
Wire Wire Line
	7550 4150 7550 4250
Wire Wire Line
	7150 4150 7550 4150
$Comp
L trial:SEN0193 U2
U 1 1 5F33FAC0
P 8600 3850
F 0 "U2" V 8646 3520 50  0000 R CNN
F 1 "SEN0193" V 8555 3520 50  0000 R CNN
F 2 "Connector_JST:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical" H 8500 3450 50  0001 C CNN
F 3 "" H 8500 3450 50  0001 C CNN
	1    8600 3850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8100 3850 8100 2800
Text GLabel 8400 3750 0    50   Output ~ 0
SEN_A0
Wire Wire Line
	8100 3850 8400 3850
Wire Wire Line
	8100 3950 8400 3950
Text GLabel 7150 3950 2    50   Input ~ 0
SEN_A0
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
	-1   0    0    -1  
$EndComp
Text GLabel 6150 3850 0    50   Output ~ 0
Q2_B
Wire Wire Line
	6750 2800 8100 2800
Wire Wire Line
	4650 5300 5100 5300
Wire Wire Line
	4650 5300 4650 5200
Connection ~ 5100 5300
Wire Wire Line
	5100 5000 5550 5000
Connection ~ 5100 5000
Wire Wire Line
	4950 5000 5100 5000
$Comp
L RF:nRF24L01P U1
U 1 1 5F26A887
P 4750 3900
F 0 "U1" H 4700 3700 50  0000 L CNN
F 1 "nRF24L01P" H 4550 3800 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical" V 4659 4743 50  0001 L CIN
F 3 "http://www.nordicsemi.com/eng/content/download/2726/34069/file/nRF24L01P_Product_Specification_1_0.pdf" H 4750 4000 50  0001 C CNN
	1    4750 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5F31B617
P 5100 5150
F 0 "R1" H 5170 5196 50  0000 L CNN
F 1 "1M" H 5170 5105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5030 5150 50  0001 C CNN
F 3 "~" H 5100 5150 50  0001 C CNN
	1    5100 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 4700 4650 4800
Text GLabel 4150 3900 0    50   Input ~ 0
CE
Text GLabel 4150 3700 0    50   Input ~ 0
CSN
Text GLabel 4150 3400 0    50   Input ~ 0
MOSI
Text GLabel 4150 3600 0    50   Input ~ 0
SCK
Text GLabel 4150 3500 0    50   Output ~ 0
MISO
Wire Wire Line
	5550 3750 6150 3750
Wire Wire Line
	7550 4550 7550 5300
Connection ~ 7550 5300
Wire Wire Line
	7550 5300 8100 5300
Wire Wire Line
	8100 4800 8100 5300
Text GLabel 8400 4600 2    50   Input ~ 0
Q2_B
Wire Wire Line
	7550 2650 7550 3750
Wire Wire Line
	3300 2650 3300 3800
Wire Wire Line
	5550 3750 5550 5000
$Comp
L soil_humidity_module:IRL540N Q1
U 1 1 5F3D6F3F
P 4750 5000
F 0 "Q1" H 4955 5046 50  0000 L CNN
F 1 "IRL540N" H 4955 4955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5000 4925 50  0001 L CIN
F 3 "" H 4750 5000 50  0001 L CNN
	1    4750 5000
	-1   0    0    -1  
$EndComp
NoConn ~ 6150 4350
NoConn ~ 6150 4050
NoConn ~ 6150 3950
NoConn ~ 6150 3650
NoConn ~ 6150 3550
NoConn ~ 6150 3450
NoConn ~ 6150 3350
NoConn ~ 6850 2950
NoConn ~ 7150 3350
NoConn ~ 7150 3450
NoConn ~ 7150 3750
NoConn ~ 7150 4050
NoConn ~ 7150 4250
NoConn ~ 7150 4350
NoConn ~ 7150 4450
NoConn ~ 7150 4550
NoConn ~ 7150 4650
NoConn ~ 5350 4400
NoConn ~ 4750 4700
NoConn ~ 4850 4700
NoConn ~ 4950 4700
NoConn ~ 5350 4200
NoConn ~ 5350 3800
NoConn ~ 5350 3600
NoConn ~ 5350 3400
NoConn ~ 4850 3100
NoConn ~ 4750 3100
NoConn ~ 4150 4000
NoConn ~ 4150 4200
NoConn ~ 4150 4400
Connection ~ 4650 5300
Wire Wire Line
	3300 4200 3300 5300
Wire Wire Line
	3300 5300 4650 5300
Connection ~ 6650 5300
Wire Wire Line
	5100 5300 6650 5300
Wire Wire Line
	6650 4950 6650 5300
Connection ~ 6750 5300
Wire Wire Line
	6750 5300 7550 5300
Wire Wire Line
	6650 5300 6750 5300
Wire Wire Line
	6750 4950 6750 5300
Wire Wire Line
	6550 2650 7550 2650
Connection ~ 6550 2650
Wire Wire Line
	6550 2650 6550 2950
Connection ~ 4650 2650
Wire Wire Line
	4650 2650 6550 2650
Wire Wire Line
	3300 2650 4650 2650
Wire Wire Line
	4650 3100 4650 2650
$EndSCHEMATC
