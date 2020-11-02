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
P 1400 3900
F 0 "BT1" H 1508 3946 50  0000 L CNN
F 1 "3.3-4.2V" H 1508 3855 50  0000 L CNN
F 2 "Connector_AMASS:AMASS_XT30U-F_1x02_P5.0mm_Vertical" V 1400 3960 50  0001 C CNN
F 3 "~" V 1400 3960 50  0001 C CNN
	1    1400 3900
	1    0    0    -1  
$EndComp
Text GLabel 5200 3050 2    50   Input ~ 0
MISO
Text GLabel 5200 3150 2    50   Output ~ 0
SCK
Text GLabel 5200 2950 2    50   Output ~ 0
MOSI
Text GLabel 5200 2750 2    50   Output ~ 0
CSN
Text GLabel 5200 2650 2    50   Output ~ 0
CE
$Comp
L trial:SEN0193 U2
U 1 1 5F33FAC0
P 9150 3750
F 0 "U2" V 9196 3420 50  0000 R CNN
F 1 "SEN0193" V 9105 3420 50  0000 R CNN
F 2 "Connector_JST:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical" H 9050 3350 50  0001 C CNN
F 3 "" H 9050 3350 50  0001 C CNN
	1    9150 3750
	0    -1   -1   0   
$EndComp
Text GLabel 8950 3650 0    50   Output ~ 0
SEN_A0
Text GLabel 5200 3550 2    50   Input ~ 0
SEN_A0
Wire Wire Line
	8550 3850 8550 4300
$Comp
L Transistor_BJT:BC547 Q2
U 1 1 5F3574C8
P 8650 4500
F 0 "Q2" H 8841 4546 50  0000 L CNN
F 1 "BC547" H 8841 4455 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 8850 4425 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 8650 4500 50  0001 L CNN
	1    8650 4500
	-1   0    0    -1  
$EndComp
Text GLabel 5200 4850 2    50   Output ~ 0
Q2_D5
$Comp
L RF:nRF24L01P U1
U 1 1 5F26A887
P 7300 3950
F 0 "U1" H 7250 3750 50  0000 L CNN
F 1 "nRF24L01P" H 7100 3850 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical" V 7209 4793 50  0001 L CIN
F 3 "http://www.nordicsemi.com/eng/content/download/2726/34069/file/nRF24L01P_Product_Specification_1_0.pdf" H 7300 4050 50  0001 C CNN
	1    7300 3950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5F31B617
P 6900 5200
F 0 "R1" H 6970 5246 50  0000 L CNN
F 1 "1M" H 6970 5155 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6830 5200 50  0001 C CNN
F 3 "~" H 6900 5200 50  0001 C CNN
	1    6900 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 4750 7200 4850
Text GLabel 6700 3950 0    50   Input ~ 0
CE
Text GLabel 6700 3750 0    50   Input ~ 0
CSN
Text GLabel 6700 3450 0    50   Input ~ 0
MOSI
Text GLabel 6700 3650 0    50   Input ~ 0
SCK
Text GLabel 6700 3550 0    50   Output ~ 0
MISO
Text GLabel 8850 4500 2    50   Input ~ 0
Q2_D5
NoConn ~ 7900 4450
NoConn ~ 7300 4750
NoConn ~ 7400 4750
NoConn ~ 7500 4750
NoConn ~ 7900 4250
NoConn ~ 7900 3850
NoConn ~ 7900 3650
NoConn ~ 7900 3450
NoConn ~ 6700 4050
NoConn ~ 6700 4250
NoConn ~ 6700 4450
$Comp
L MCU_Microchip_ATmega:ATmega328P-PU U4
U 1 1 5F62712C
P 4600 3850
F 0 "U4" H 3956 3896 50  0000 R CNN
F 1 "ATmega328P-PU" H 3956 3805 50  0000 R CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 4600 3850 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 4600 3850 50  0001 C CNN
	1    4600 3850
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:LD1117S33TR_SOT223 U3
U 1 1 5F63098D
P 3200 2150
F 0 "U3" H 3200 2392 50  0000 C CNN
F 1 "LD1117S33TR_SOT223" H 3200 2301 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 3200 2350 50  0001 C CNN
F 3 "http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000544.pdf" H 3300 1900 50  0001 C CNN
	1    3200 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C1
U 1 1 5F63B2EF
P 2700 2350
F 0 "C1" H 2792 2396 50  0000 L CNN
F 1 "100nF" H 2792 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 2700 2350 50  0001 C CNN
F 3 "~" H 2700 2350 50  0001 C CNN
	1    2700 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C2
U 1 1 5F63D266
P 3650 2350
F 0 "C2" H 3742 2396 50  0000 L CNN
F 1 "10uF" H 3742 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 3650 2350 50  0001 C CNN
F 3 "~" H 3650 2350 50  0001 C CNN
	1    3650 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 2150 2700 2150
Wire Wire Line
	3500 2150 3650 2150
Wire Wire Line
	2700 2150 2700 2250
Connection ~ 2700 2150
Wire Wire Line
	2700 2150 2900 2150
Wire Wire Line
	3650 2150 3650 2250
Wire Wire Line
	3650 2450 3200 2450
Connection ~ 3200 2450
Wire Wire Line
	2700 2450 3200 2450
Wire Wire Line
	1400 2150 1400 3700
Wire Wire Line
	1400 4100 1400 4250
Wire Wire Line
	4600 5600 4600 5350
Wire Wire Line
	1400 5600 2300 5600
Wire Wire Line
	3200 2450 3200 5600
Wire Wire Line
	3200 5600 4600 5600
Wire Wire Line
	4600 2150 4600 2350
Connection ~ 3650 2150
$Comp
L Device:C_Small C4
U 1 1 5F6D6BAE
P 5950 3750
F 0 "C4" H 5800 3750 50  0000 C CNN
F 1 "22pF" H 5750 3850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 5950 3750 50  0001 C CNN
F 3 "~" H 5950 3750 50  0001 C CNN
	1    5950 3750
	-1   0    0    1   
$EndComp
$Comp
L Device:C_Small C3
U 1 1 5F6DEF30
P 5750 3750
F 0 "C3" H 5900 3750 50  0000 C CNN
F 1 "22pF" H 5900 3850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 5750 3750 50  0001 C CNN
F 3 "~" H 5750 3750 50  0001 C CNN
	1    5750 3750
	-1   0    0    1   
$EndComp
$Comp
L Device:Crystal_Small Y1
U 1 1 5F6EFD57
P 5850 3450
F 0 "Y1" H 5800 3200 50  0000 L CNN
F 1 "Crystal_Small" H 5600 3300 50  0000 L CNN
F 2 "Crystal:Crystal_HC49-4H_Vertical" H 5850 3450 50  0001 C CNN
F 3 "~" H 5850 3450 50  0001 C CNN
	1    5850 3450
	-1   0    0    1   
$EndComp
Wire Wire Line
	5950 3850 5950 4000
Wire Wire Line
	5750 3850 5750 4000
Wire Wire Line
	5950 3450 5950 3650
Wire Wire Line
	5750 3650 5750 3450
Connection ~ 5950 3450
Wire Wire Line
	5950 4000 5850 4000
Wire Wire Line
	5850 4000 5850 5600
Connection ~ 5850 4000
Wire Wire Line
	5850 4000 5750 4000
Wire Wire Line
	5750 3450 5750 3350
Connection ~ 5750 3450
Wire Wire Line
	5950 3250 5950 3450
Wire Wire Line
	5200 3250 5950 3250
Wire Wire Line
	5200 3350 5750 3350
Text GLabel 5200 3750 2    50   Input ~ 0
DIV_A2
Wire Wire Line
	3650 2150 4600 2150
Text GLabel 2550 4150 2    50   Output ~ 0
DIV_A2
Wire Wire Line
	2300 4550 2300 5600
Wire Wire Line
	2300 2150 2300 3750
$Comp
L Device:R R4
U 1 1 5F2E0DD1
P 2300 4400
F 0 "R4" H 2370 4446 50  0000 L CNN
F 1 "10k" H 2370 4355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2230 4400 50  0001 C CNN
F 3 "~" H 2300 4400 50  0001 C CNN
	1    2300 4400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5F2DE1F5
P 2300 3900
F 0 "R3" H 2370 3946 50  0000 L CNN
F 1 "100k" H 2370 3855 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2230 3900 50  0001 C CNN
F 3 "~" H 2300 3900 50  0001 C CNN
	1    2300 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 5600 5850 5600
Connection ~ 4600 5600
$Comp
L soil_humidity_module:IRL540N Q1
U 1 1 5F3D6F3F
P 7100 5050
F 0 "Q1" H 7305 5096 50  0000 L CNN
F 1 "IRL540N" H 7305 5005 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 7350 4975 50  0001 L CIN
F 3 "" H 7100 5050 50  0001 L CNN
	1    7100 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 5600 6900 5600
Wire Wire Line
	7200 5250 7200 5600
Wire Wire Line
	6900 5350 6900 5600
Wire Wire Line
	7200 2150 7200 3150
Text GLabel 5200 4750 2    50   Output ~ 0
Q1_D4
Wire Wire Line
	8550 2150 7200 2150
Wire Wire Line
	8550 2150 8550 3750
Wire Wire Line
	8550 5600 7200 5600
Wire Wire Line
	8550 4700 8550 5600
Connection ~ 7200 5600
Wire Wire Line
	8550 3750 8950 3750
Wire Wire Line
	8550 3850 8950 3850
NoConn ~ 5200 2850
NoConn ~ 5200 3650
NoConn ~ 5200 3850
NoConn ~ 5200 3950
NoConn ~ 5200 4050
NoConn ~ 5200 4150
NoConn ~ 5200 4350
NoConn ~ 5200 4450
NoConn ~ 5200 4550
NoConn ~ 5200 4650
NoConn ~ 5200 4950
NoConn ~ 5200 5050
$Comp
L Device:CircuitBreaker_1P CB1
U 1 1 5F830F0C
P 1400 4550
F 0 "CB1" H 1452 4596 50  0000 L CNN
F 1 "Power_Switch" H 1452 4505 50  0000 L CNN
F 2 "Connector_JST:JST_XH_B2B-XH-AM_1x02_P2.50mm_Vertical" H 1400 4550 50  0001 C CNN
F 3 "~" H 1400 4550 50  0001 C CNN
	1    1400 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 4850 1400 5600
NoConn ~ 4700 2350
NoConn ~ 4000 2650
Wire Wire Line
	6900 5050 6750 5050
Connection ~ 6900 5050
Text GLabel 6750 5050 0    50   Input ~ 0
Q1_D4
Wire Wire Line
	2300 5600 3200 5600
Connection ~ 2300 5600
Connection ~ 3200 5600
Wire Wire Line
	1400 2150 2300 2150
Connection ~ 2300 2150
Wire Wire Line
	2300 4050 2300 4150
Wire Wire Line
	2550 4150 2300 4150
Connection ~ 2300 4150
Wire Wire Line
	2300 4150 2300 4250
Wire Wire Line
	4600 2150 7200 2150
Connection ~ 4600 2150
Connection ~ 7200 2150
Wire Wire Line
	5850 5600 6900 5600
Connection ~ 5850 5600
Connection ~ 6900 5600
NoConn ~ 7300 3150
NoConn ~ 7400 3150
$EndSCHEMATC
