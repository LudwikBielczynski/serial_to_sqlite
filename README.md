# General scheme
General scheme of the watering control system is shown below:
![alt text](https://github.com/LudwikBielczynski/watering_control_system/blob/master/schemes/general.svg)

Code to program transmitter and receiver arduino microcontrollers are available in sensors directory.

# Wiring schemes
## Receiver module
The wiring scheme for the receiver module is as follows:
![alt text](https://github.com/LudwikBielczynski/watering_control_system/blob/master/schemes/receiver_module_scheme.svg)

## Soil humidity module
When compared with the receiver module, the wiring scheme of the soil humidity module has additionally (i) an external power supply, (ii) a voltage divider plugged to the analog pin (to measure the voltage of the battery), and (iii) the soil humidity sensor.
![alt text](https://github.com/LudwikBielczynski/watering_control_system/blob/master/schemes/2020-08-03_soil_humidity_module_scheme.svg)

A prototype is shown below:
![alt text](https://github.com/LudwikBielczynski/watering_control_system/blob/master/prototypes/2020-05-06_soil_humidity_module.jpg)

# Receiver module
## Install as a service
The sensor_listener.service script should be placed in the /etc/systemd/system folder.
