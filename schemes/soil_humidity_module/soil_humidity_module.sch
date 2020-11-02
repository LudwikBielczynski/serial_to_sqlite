EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Soil humidity sensor with remote communication"
Date "2020-09-16"
Rev "1.0"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text GLabel 3100 4550 2    50   Input ~ 0
MISO
Text GLabel 3100 4650 2    50   Output ~ 0
SCK
Text GLabel 3100 4450 2    50   Output ~ 0
MOSI
Text GLabel 3100 4250 2    50   Output ~ 0
CSN
Text GLabel 3100 4150 2    50   Output ~ 0
CE
$Comp
L trial:SEN0193 U2
U 1 1 5F33FAC0
P 6075 2725
F 0 "U2" V 6121 2395 50  0000 R CNN
F 1 "SEN0193" V 6030 2395 50  0000 R CNN
F 2 "Connector_JST:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical" H 5975 2325 50  0001 C CNN
F 3 "" H 5975 2325 50  0001 C CNN
	1    6075 2725
	0    1    -1   0   
$EndComp
Text GLabel 6275 2625 2    50   Output ~ 0
SEN_A0
Text GLabel 3100 5050 2    50   Input ~ 0
SEN_A0
Text GLabel 3100 6350 2    50   Output ~ 0
Q2_D5
Text GLabel 9100 4725 0    50   Input ~ 0
CE
Text GLabel 9100 4525 0    50   Input ~ 0
CSN
Text GLabel 9100 4225 0    50   Input ~ 0
MOSI
Text GLabel 9100 4425 0    50   Input ~ 0
SCK
Text GLabel 9100 4325 0    50   Output ~ 0
MISO
Text GLabel 6275 3225 0    50   Input ~ 0
Q2_D5
Text GLabel 3100 5250 2    50   Input ~ 0
DIV_A2
Text GLabel 2650 1900 2    50   Output ~ 0
DIV_A2
$Comp
L Device:R R4
U 1 1 5F2E0DD1
P 2400 2150
F 0 "R4" H 2450 2150 50  0000 L CNN
F 1 "10k" V 2400 2100 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2330 2150 50  0001 C CNN
F 3 "~" H 2400 2150 50  0001 C CNN
	1    2400 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5F2DE1F5
P 2400 1650
F 0 "R3" H 2450 1650 50  0000 L CNN
F 1 "100k" V 2400 1550 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2330 1650 50  0001 C CNN
F 3 "~" H 2400 1650 50  0001 C CNN
	1    2400 1650
	1    0    0    -1  
$EndComp
Text GLabel 3100 6250 2    50   Output ~ 0
Q1_D4
Wire Wire Line
	6675 2725 6275 2725
NoConn ~ 3100 4350
NoConn ~ 3100 5150
NoConn ~ 3100 5350
NoConn ~ 3100 5450
NoConn ~ 3100 5550
$Comp
L Device:CircuitBreaker_1P CB1
U 1 1 5F830F0C
P 2100 1400
F 0 "CB1" V 2350 1300 50  0000 L CNN
F 1 "Power_Switch" V 2250 1150 50  0000 L CNN
F 2 "Connector_JST:JST_XH_B2B-XH-AM_1x02_P2.50mm_Vertical" H 2100 1400 50  0001 C CNN
F 3 "~" H 2100 1400 50  0001 C CNN
	1    2100 1400
	0    -1   -1   0   
$EndComp
Text GLabel 9000 2750 0    50   Input ~ 0
Q1_D4
Wire Wire Line
	2400 1800 2400 1900
Wire Wire Line
	2650 1900 2400 1900
Connection ~ 2400 1900
Wire Wire Line
	2400 1900 2400 2000
Wire Wire Line
	2400 1400 2400 1500
$Comp
L power:+3.3V #PWR0102
U 1 1 5F67EEDB
P 9800 2400
F 0 "#PWR0102" H 9800 2250 50  0001 C CNN
F 1 "+3.3V" H 9815 2573 50  0000 C CNN
F 2 "" H 9800 2400 50  0001 C CNN
F 3 "" H 9800 2400 50  0001 C CNN
	1    9800 2400
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0108
U 1 1 5F6B62C2
P 9600 3825
F 0 "#PWR0108" H 9600 3675 50  0001 C CNN
F 1 "+3.3V" H 9615 3998 50  0000 C CNN
F 2 "" H 9600 3825 50  0001 C CNN
F 3 "" H 9600 3825 50  0001 C CNN
	1    9600 3825
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 5F6F5C3C
P 1800 2500
F 0 "#PWR0106" H 1800 2250 50  0001 C CNN
F 1 "GND" H 1805 2327 50  0000 C CNN
F 2 "" H 1800 2500 50  0001 C CNN
F 3 "" H 1800 2500 50  0001 C CNN
	1    1800 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 2400 1800 2500
$Comp
L power:GND #PWR0109
U 1 1 5F6F8FD6
P 2500 6950
F 0 "#PWR0109" H 2500 6700 50  0001 C CNN
F 1 "GND" H 2505 6777 50  0000 C CNN
F 2 "" H 2500 6950 50  0001 C CNN
F 3 "" H 2500 6950 50  0001 C CNN
	1    2500 6950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0110
U 1 1 5F6FCC14
P 9600 5200
F 0 "#PWR0110" H 9600 4950 50  0001 C CNN
F 1 "GND" H 9605 5027 50  0000 C CNN
F 2 "" H 9600 5200 50  0001 C CNN
F 3 "" H 9600 5200 50  0001 C CNN
	1    9600 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 1400 1800 1700
$Comp
L power:PWR_FLAG #FLG0103
U 1 1 5F746E11
P 2400 1150
F 0 "#FLG0103" H 2400 1225 50  0001 C CNN
F 1 "PWR_FLAG" H 2400 1323 50  0000 C CNN
F 2 "" H 2400 1150 50  0001 C CNN
F 3 "~" H 2400 1150 50  0001 C CNN
	1    2400 1150
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0104
U 1 1 5F74A67D
P 6875 2825
F 0 "#FLG0104" H 6875 2900 50  0001 C CNN
F 1 "PWR_FLAG" H 6875 2998 50  0000 C CNN
F 2 "" H 6875 2825 50  0001 C CNN
F 3 "~" H 6875 2825 50  0001 C CNN
	1    6875 2825
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2400 2300 2400 2400
Wire Wire Line
	1800 2000 1800 2400
Connection ~ 1800 2400
Connection ~ 2400 1400
Wire Wire Line
	2400 2400 1800 2400
Wire Notes Line
	4600 3100 4600 7300
Wire Notes Line
	4600 7300 1500 7300
Wire Notes Line
	1500 7300 1500 3100
Wire Notes Line
	1500 3100 4600 3100
Text Notes 2500 3050 0    50   ~ 0
ATmega with the oscillator
Text Notes 8900 3575 0    50   ~ 0
Communication module
Wire Notes Line
	7575 3875 7575 2025
Wire Notes Line
	5275 2025 5275 3875
Text Notes 6075 1975 0    50   ~ 0
Soil humidity sensor
Wire Wire Line
	2400 1150 2400 1400
Wire Notes Line
	1500 2750 1500 750 
Text Notes 1700 700  0    50   ~ 0
Power supply and monitoring
Wire Notes Line
	3050 2750 3050 750 
$Comp
L RF:NRF24L01_Breakout U1
U 1 1 5F8AF8DA
P 9600 4525
F 0 "U1" H 9550 4525 50  0000 L CNN
F 1 "NRF24L01_Breakout" V 10000 4175 50  0000 L CNN
F 2 "RF_Module:nRF24L01_Breakout" H 9750 5125 50  0001 L CIN
F 3 "http://www.nordicsemi.com/eng/content/download/2730/34105/file/nRF24L01_Product_Specification_v2_0.pdf" H 9600 4425 50  0001 C CNN
	1    9600 4525
	1    0    0    -1  
$EndComp
NoConn ~ 9100 4825
$Comp
L Device:LED_ALT D2
U 1 1 5F9A1E59
P 7325 2525
F 0 "D2" V 7364 2407 50  0000 R CNN
F 1 "LED_ALT" V 7273 2407 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 7325 2525 50  0001 C CNN
F 3 "~" H 7325 2525 50  0001 C CNN
	1    7325 2525
	0    1    -1   0   
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 5F706F73
P 6675 3625
F 0 "#PWR0111" H 6675 3375 50  0001 C CNN
F 1 "GND" H 6680 3452 50  0000 C CNN
F 2 "" H 6675 3625 50  0001 C CNN
F 3 "" H 6675 3625 50  0001 C CNN
	1    6675 3625
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7325 2675 7325 2725
Wire Notes Line
	7575 2025 5275 2025
Wire Notes Line
	5275 3875 7575 3875
$Comp
L Device:R R6
U 1 1 5F9BDA04
P 7325 2875
F 0 "R6" H 7375 2875 50  0000 L CNN
F 1 "1k" V 7325 2825 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7255 2875 50  0001 C CNN
F 3 "~" H 7325 2875 50  0001 C CNN
	1    7325 2875
	-1   0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR01
U 1 1 5F9CC68A
P 10350 3450
F 0 "#PWR01" H 10350 3300 50  0001 C CNN
F 1 "+3.3V" H 10365 3623 50  0000 C CNN
F 2 "" H 10350 3450 50  0001 C CNN
F 3 "" H 10350 3450 50  0001 C CNN
	1    10350 3450
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_ALT D1
U 1 1 5F9CC690
P 10350 3650
F 0 "D1" V 10389 3532 50  0000 R CNN
F 1 "LED_ALT" V 10298 3532 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 10350 3650 50  0001 C CNN
F 3 "~" H 10350 3650 50  0001 C CNN
	1    10350 3650
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R5
U 1 1 5F9CC699
P 10350 4000
F 0 "R5" H 10400 4000 50  0000 L CNN
F 1 "1k" V 10350 3950 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 10280 4000 50  0001 C CNN
F 3 "~" H 10350 4000 50  0001 C CNN
	1    10350 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6875 2825 6675 2825
Wire Wire Line
	7325 3025 6675 3025
Wire Wire Line
	6675 2825 6675 3025
Connection ~ 6675 2825
Wire Wire Line
	6675 2825 6275 2825
Wire Wire Line
	10350 3800 10350 3850
Wire Wire Line
	10350 4150 10350 4200
Wire Wire Line
	6675 2325 6675 2725
Wire Wire Line
	7325 2325 7325 2375
$Comp
L Device:C_Small C6
U 1 1 5F6FCC61
P 8700 4025
F 0 "C6" H 8700 4100 50  0000 L CNN
F 1 "100nF" H 8700 3950 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 8700 4025 50  0001 C CNN
F 3 "~" H 8700 4025 50  0001 C CNN
	1    8700 4025
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C5
U 1 1 5F71A188
P 8500 4025
F 0 "C5" H 8500 4100 50  0000 L CNN
F 1 "10uF" H 8500 3950 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 8500 4025 50  0001 C CNN
F 3 "~" H 8500 4025 50  0001 C CNN
	1    8500 4025
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 5F76E9AB
P 8600 4225
F 0 "#PWR0104" H 8600 3975 50  0001 C CNN
F 1 "GND" H 8605 4052 50  0000 C CNN
F 2 "" H 8600 4225 50  0001 C CNN
F 3 "" H 8600 4225 50  0001 C CNN
	1    8600 4225
	1    0    0    -1  
$EndComp
Text Notes 4875 6075 0    50   ~ 0
Debug/Programmator connector
Text GLabel 3100 5850 2    50   Input ~ 0
RXD_J1
Text GLabel 3100 5950 2    50   Output ~ 0
TXD_J1
Text GLabel 5625 6325 2    50   Output ~ 0
RXD_J1
Text GLabel 5625 6225 2    50   Input ~ 0
TXD_J1
Wire Wire Line
	2500 6850 2500 6950
$Comp
L Connector_Generic:Conn_01x03 J1
U 1 1 5F6F29C1
P 5425 6325
F 0 "J1" H 5505 6367 50  0000 L CNN
F 1 "Conn_01x03" H 5505 6276 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5425 6325 50  0001 C CNN
F 3 "~" H 5425 6325 50  0001 C CNN
	1    5425 6325
	-1   0    0    1   
$EndComp
Text GLabel 5625 6425 2    50   Output ~ 0
RESET_J1
Wire Notes Line
	4825 6125 6075 6125
Wire Notes Line
	6075 6575 4825 6575
Wire Notes Line
	4825 6125 4825 6575
Wire Notes Line
	6075 6125 6075 6575
Wire Wire Line
	10350 3450 10350 3500
Wire Wire Line
	8500 4175 8600 4175
Wire Wire Line
	8600 4225 8600 4175
Connection ~ 8600 4175
Wire Wire Line
	8600 4175 8700 4175
Wire Wire Line
	6675 3575 6675 3625
Wire Wire Line
	2600 3800 2600 3850
$Comp
L Device:C_Small C8
U 1 1 5F82A0D2
P 1850 4250
F 0 "C8" H 1725 4325 50  0000 L CNN
F 1 "100nF" H 1600 4175 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 1850 4250 50  0001 C CNN
F 3 "~" H 1850 4250 50  0001 C CNN
	1    1850 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 4150 1850 4150
$Comp
L Device:C_Small C9
U 1 1 5F87EBA9
P 3400 3900
F 0 "C9" H 3400 3975 50  0000 L CNN
F 1 "100nF" H 3400 3825 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 3400 3900 50  0001 C CNN
F 3 "~" H 3400 3900 50  0001 C CNN
	1    3400 3900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 5F88C553
P 3400 4050
F 0 "#PWR05" H 3400 3800 50  0001 C CNN
F 1 "GND" H 3405 3877 50  0000 C CNN
F 2 "" H 3400 4050 50  0001 C CNN
F 3 "" H 3400 4050 50  0001 C CNN
	1    3400 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3400 4000 3400 4050
Wire Wire Line
	2600 3800 3400 3800
Connection ~ 2600 3800
$Comp
L Device:L_Small L1
U 1 1 5F8A9F5B
P 2600 3650
F 0 "L1" H 2648 3696 50  0000 L CNN
F 1 "10uH" H 2648 3605 50  0000 L CNN
F 2 "Inductor_SMD:L_0805_2012Metric" H 2600 3650 50  0001 C CNN
F 3 "~" H 2600 3650 50  0001 C CNN
	1    2600 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 3500 2600 3550
Wire Wire Line
	2600 3750 2600 3800
$Comp
L power:PWR_FLAG #FLG0105
U 1 1 5F8CA288
P 2600 3850
F 0 "#FLG0105" H 2600 3925 50  0001 C CNN
F 1 "PWR_FLAG" V 2600 4150 50  0000 C CNN
F 2 "" H 2600 3850 50  0001 C CNN
F 3 "~" H 2600 3850 50  0001 C CNN
	1    2600 3850
	0    1    -1   0   
$EndComp
$Comp
L Device:R R8
U 1 1 5F8E6B44
P 6325 3375
F 0 "R8" H 6175 3375 50  0000 L CNN
F 1 "1M" V 6325 3325 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6255 3375 50  0001 C CNN
F 3 "~" H 6325 3375 50  0001 C CNN
	1    6325 3375
	1    0    0    -1  
$EndComp
Wire Wire Line
	6325 3525 6325 3575
Wire Wire Line
	6375 3225 6325 3225
Wire Wire Line
	6675 3575 6325 3575
Wire Wire Line
	6675 3425 6675 3575
Connection ~ 6675 3575
Wire Wire Line
	6325 3225 6275 3225
Connection ~ 6325 3225
Wire Wire Line
	8500 3875 8700 3875
Wire Wire Line
	8700 3875 8700 3925
Wire Wire Line
	8500 3875 8500 3925
Wire Wire Line
	8500 4125 8500 4175
Wire Wire Line
	8700 4125 8700 4175
Wire Wire Line
	8700 3875 9600 3875
Connection ~ 8700 3875
Wire Wire Line
	9600 3875 9600 3925
Wire Wire Line
	9600 3825 9600 3875
Connection ~ 9600 3875
$Comp
L power:VCC #PWR0114
U 1 1 5F8A5DC3
P 2750 1350
F 0 "#PWR0114" H 2750 1200 50  0001 C CNN
F 1 "VCC" H 2765 1523 50  0000 C CNN
F 2 "" H 2750 1350 50  0001 C CNN
F 3 "" H 2750 1350 50  0001 C CNN
	1    2750 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 1400 2750 1400
Wire Wire Line
	2750 1400 2750 1350
Wire Notes Line
	1500 750  3050 750 
Wire Notes Line
	1500 2750 3050 2750
Text Notes 9000 2150 0    50   ~ 0
Power regulation
$Comp
L power:VCC #PWR0107
U 1 1 5F848456
P 2500 3450
F 0 "#PWR0107" H 2500 3300 50  0001 C CNN
F 1 "VCC" H 2515 3623 50  0000 C CNN
F 2 "" H 2500 3450 50  0001 C CNN
F 3 "" H 2500 3450 50  0001 C CNN
	1    2500 3450
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0115
U 1 1 5F851B17
P 6675 2325
F 0 "#PWR0115" H 6675 2175 50  0001 C CNN
F 1 "VCC" H 6690 2498 50  0000 C CNN
F 2 "" H 6675 2325 50  0001 C CNN
F 3 "" H 6675 2325 50  0001 C CNN
	1    6675 2325
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0116
U 1 1 5F856CAD
P 7325 2325
F 0 "#PWR0116" H 7325 2175 50  0001 C CNN
F 1 "VCC" H 7340 2498 50  0000 C CNN
F 2 "" H 7325 2325 50  0001 C CNN
F 3 "" H 7325 2325 50  0001 C CNN
	1    7325 2325
	1    0    0    -1  
$EndComp
$Comp
L soil_humidity_module:DMG6968U Q2
U 1 1 5F8967C3
P 6575 3225
F 0 "Q2" H 6780 3271 50  0000 L CNN
F 1 "DMG6968U" H 6780 3180 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 6825 3150 50  0001 L CIN
F 3 "" H 6575 3225 50  0001 L CNN
	1    6575 3225
	1    0    0    -1  
$EndComp
Connection ~ 6675 3025
Connection ~ 2600 3850
$Comp
L MCU_Microchip_ATmega:ATmega328P-PU U4
U 1 1 5F62712C
P 2500 5350
F 0 "U4" H 2550 5350 50  0000 R CNN
F 1 "ATmega328P-PU" H 2800 5250 50  0000 R CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 2500 5350 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 2500 5350 50  0001 C CNN
	1    2500 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:Battery_Cell BT1
U 1 1 5F71FB83
P 1800 1900
F 0 "BT1" V 1550 1900 50  0000 L CNN
F 1 "+3.3-4.2V" V 1650 1750 50  0000 L CNN
F 2 "Connector_AMASS:AMASS_XT30U-F_1x02_P5.0mm_Vertical" V 1800 1960 50  0001 C CNN
F 3 "~" V 1800 1960 50  0001 C CNN
	1    1800 1900
	1    0    0    -1  
$EndComp
NoConn ~ 3100 6450
$Comp
L Device:LED_ALT D3
U 1 1 5FC1BCD8
P 3575 6700
F 0 "D3" V 3614 6582 50  0000 R CNN
F 1 "LED_ALT" V 3523 6582 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 3575 6700 50  0001 C CNN
F 3 "~" H 3575 6700 50  0001 C CNN
	1    3575 6700
	0    1    -1   0   
$EndComp
$Comp
L Device:R R10
U 1 1 5FC1BCDF
P 3325 6550
F 0 "R10" V 3250 6500 50  0000 L CNN
F 1 "1k" V 3325 6500 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 3255 6550 50  0001 C CNN
F 3 "~" H 3325 6550 50  0001 C CNN
	1    3325 6550
	0    -1   1    0   
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 5FC4AD43
P 3575 6925
F 0 "#PWR0118" H 3575 6675 50  0001 C CNN
F 1 "GND" H 3580 6752 50  0000 C CNN
F 2 "" H 3575 6925 50  0001 C CNN
F 3 "" H 3575 6925 50  0001 C CNN
	1    3575 6925
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 6550 3175 6550
Wire Wire Line
	3475 6550 3575 6550
Wire Wire Line
	3575 6850 3575 6925
$Comp
L power:GND #PWR0103
U 1 1 5F8ADFB0
P 1850 4400
F 0 "#PWR0103" H 1850 4150 50  0001 C CNN
F 1 "GND" H 1855 4227 50  0000 C CNN
F 2 "" H 1850 4400 50  0001 C CNN
F 3 "" H 1850 4400 50  0001 C CNN
	1    1850 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 4350 1850 4400
$Comp
L Device:C_Small C11
U 1 1 5F8FAF67
P 2325 3450
F 0 "C11" V 2275 3475 50  0000 L CNN
F 1 "100nF" V 2275 3175 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 2325 3450 50  0001 C CNN
F 3 "~" H 2325 3450 50  0001 C CNN
	1    2325 3450
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 5F8FAF6D
P 2225 3500
F 0 "#PWR0113" H 2225 3250 50  0001 C CNN
F 1 "GND" H 2230 3327 50  0000 C CNN
F 2 "" H 2225 3500 50  0001 C CNN
F 3 "" H 2225 3500 50  0001 C CNN
	1    2225 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2225 3450 2225 3500
Wire Wire Line
	2500 3500 2500 3850
Wire Wire Line
	2600 3500 2500 3500
Wire Wire Line
	2425 3450 2500 3450
Wire Wire Line
	2500 3500 2500 3450
Connection ~ 2500 3500
Connection ~ 2500 3450
NoConn ~ 3100 4750
NoConn ~ 3100 4850
$Comp
L soil_humidity_module:AP7365 U3
U 1 1 5F912462
P 9350 2750
F 0 "U3" H 9475 3075 50  0000 L CNN
F 1 "AP7365" H 9400 3000 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5_HandSoldering" H 9600 2950 50  0001 C CNN
F 3 "" H 9600 2950 50  0001 C CNN
	1    9350 2750
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0112
U 1 1 5F8A02AF
P 9350 2400
F 0 "#PWR0112" H 9350 2250 50  0001 C CNN
F 1 "VCC" H 9365 2573 50  0000 C CNN
F 2 "" H 9350 2400 50  0001 C CNN
F 3 "" H 9350 2400 50  0001 C CNN
	1    9350 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 3050 9350 3150
$Comp
L power:GND #PWR0105
U 1 1 5F6F1DCB
P 9350 3150
F 0 "#PWR0105" H 9350 2900 50  0001 C CNN
F 1 "GND" H 9355 2977 50  0000 C CNN
F 2 "" H 9350 3150 50  0001 C CNN
F 3 "" H 9350 3150 50  0001 C CNN
	1    9350 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9800 2750 9800 2850
$Comp
L Device:C_Small C2
U 1 1 5F63D266
P 9800 2950
F 0 "C2" H 9800 3025 50  0000 L CNN
F 1 "1uF" H 9800 2875 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 9800 2950 50  0001 C CNN
F 3 "~" H 9800 2950 50  0001 C CNN
	1    9800 2950
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C1
U 1 1 5F63B2EF
P 8575 2550
F 0 "C1" H 8450 2625 50  0000 L CNN
F 1 "1uF" H 8325 2475 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 8575 2550 50  0001 C CNN
F 3 "~" H 8575 2550 50  0001 C CNN
	1    8575 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 2400 9350 2450
$Comp
L power:GND #PWR07
U 1 1 5F947427
P 8575 2650
F 0 "#PWR07" H 8575 2400 50  0001 C CNN
F 1 "GND" H 8580 2477 50  0000 C CNN
F 2 "" H 8575 2650 50  0001 C CNN
F 3 "" H 8575 2650 50  0001 C CNN
	1    8575 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	9700 2750 9800 2750
Connection ~ 9800 2750
$Comp
L power:GND #PWR08
U 1 1 5F9A11AC
P 10350 4200
F 0 "#PWR08" H 10350 3950 50  0001 C CNN
F 1 "GND" H 10355 4027 50  0000 C CNN
F 2 "" H 10350 4200 50  0001 C CNN
F 3 "" H 10350 4200 50  0001 C CNN
	1    10350 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 2450 8575 2450
Connection ~ 9350 2450
Wire Wire Line
	9600 5125 9600 5200
Wire Wire Line
	9800 2400 9800 2750
Wire Notes Line
	8300 5425 10800 5425
Wire Notes Line
	8300 2025 10800 2025
Wire Notes Line
	10800 2025 10800 5425
Wire Notes Line
	8300 2025 8300 5425
Text Notes 10175 3200 0    50   ~ 0
Control LED
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5FA6BA9C
P 9800 5200
F 0 "#FLG0101" H 9800 5275 50  0001 C CNN
F 1 "PWR_FLAG" H 9800 5373 50  0000 C CNN
F 2 "" H 9800 5200 50  0001 C CNN
F 3 "~" H 9800 5200 50  0001 C CNN
	1    9800 5200
	-1   0    0    -1  
$EndComp
Wire Wire Line
	9800 5200 9600 5200
$Comp
L power:GND #PWR0101
U 1 1 5FAAD2D8
P 9800 3150
F 0 "#PWR0101" H 9800 2900 50  0001 C CNN
F 1 "GND" H 9805 2977 50  0000 C CNN
F 2 "" H 9800 3150 50  0001 C CNN
F 3 "" H 9800 3150 50  0001 C CNN
	1    9800 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9800 3050 9800 3150
Wire Wire Line
	3550 5650 3625 5650
Wire Wire Line
	3550 5550 3550 5650
$Comp
L Device:C_Small C7
U 1 1 5F7A3C8E
P 3725 5650
F 0 "C7" V 3775 5675 50  0000 L CNN
F 1 "100nF" V 3775 5400 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 3725 5650 50  0001 C CNN
F 3 "~" H 3725 5650 50  0001 C CNN
	1    3725 5650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3550 5200 3550 5250
$Comp
L power:VCC #PWR0117
U 1 1 5F85D722
P 3550 5200
F 0 "#PWR0117" H 3550 5050 50  0001 C CNN
F 1 "VCC" H 3565 5373 50  0000 C CNN
F 2 "" H 3550 5200 50  0001 C CNN
F 3 "" H 3550 5200 50  0001 C CNN
	1    3550 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3825 5650 3925 5650
Text GLabel 3925 5650 2    50   Input ~ 0
RESET_J1
$Comp
L Device:R R2
U 1 1 5F753278
P 3550 5400
F 0 "R2" V 3625 5325 50  0000 L CNN
F 1 "10k" V 3550 5325 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 3480 5400 50  0001 C CNN
F 3 "~" H 3550 5400 50  0001 C CNN
	1    3550 5400
	-1   0    0    1   
$EndComp
Wire Wire Line
	3100 5650 3550 5650
Connection ~ 3550 5650
NoConn ~ 3100 6050
NoConn ~ 3100 6150
$EndSCHEMATC
