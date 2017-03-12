# raspi_cpu_temp
A ROS node for CPU temperature of the Raspberry Pi. Used in my hobby project "ROSEAU" (see http://www.jacob-roboter.de/roboter/roseau/).

## Description
This ROS Python node reads the current CPU temperature from the ``/sys/class/thermal/thermal_zone0/temp`` file and publishes it via the ``cpu_temp`` topic. The default rate is 1 Hz.

## Tested platform
- Raspberry Pi 3 with Ubuntu MATE 16.04 and ROS Kinetic
