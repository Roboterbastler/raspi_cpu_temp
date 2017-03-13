#!/usr/bin/env python

import os
import rospy
from roseau_msgs.msg import CpuTemp

def read_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    msg = CpuTemp()
    msg.stamp = rospy.Time.now()
    msg.temp = float(cpu_temp)/1000
    return msg

def raspi_cpu_temp_node():
    pub = rospy.Publisher('cpu_temp', CpuTemp, queue_size=10)
    rospy.init_node('raspi_cpu_temp')
    rate = rospy.Rate(1) # 1 Hz

    while not rospy.is_shutdown():
        msg = read_cpu_temp()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        raspi_cpu_temp_node()
    except rospy.ROSInterruptException:
        pass
