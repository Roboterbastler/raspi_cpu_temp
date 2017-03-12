# raspi_cpu_temp
A ROS node for CPU temperature of the Raspberry Pi

This ROS Python node reads the current CPU temperature from the ``/sys/class/thermal/thermal_zone0/temp`` file and publishes it via the ``cpu_temp`` topic. The default rate is 1 Hz.
