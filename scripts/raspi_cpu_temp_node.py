#!/usr/bin/env python

#import os
import rospy
from sensor_msgs.msg import Temperature

frame_id_param = rospy.get_param('/rpi_cpu_temp/output_frame_id', 'rpi_frame')
#frame_id_param = rospy.get_param('~output_frame_id', 'rpi_frame')

def read_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as tempFile:
        cpu_temp = tempFile.read()
    msg = Temperature()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = frame_id_param
    msg.temperature = float(cpu_temp)/1000
    msg.variance = 0.0
    return msg

def rpi_cpu_temp_node():
    pub = rospy.Publisher('rpi/cpu_temp', Temperature, queue_size=10)
    rospy.init_node('rpi_cpu_temp')
    rate = rospy.Rate(0.2) # 1 message every 5 seconds
    rospy.loginfo(rospy.get_caller_id() + "  rpi_cpu_temp node launched.")

    while not rospy.is_shutdown():
        msg = read_cpu_temp()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rpi_cpu_temp_node()
    except rospy.ROSInterruptException:
        pass

