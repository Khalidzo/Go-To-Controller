#!/usr/bin/env python3
import rospy


if __name__ == '__main__':

    rospy.init_node("Test_node")
    rospy.loginfo("Test node just started")
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("Hey there!")
        rate.sleep()