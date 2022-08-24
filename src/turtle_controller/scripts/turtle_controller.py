#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import sqrt

target_x = float(rospy.get_param("/target/x"))
target_y = float(rospy.get_param("/target/y"))
beta = float(rospy.get_param("/parameters/beta"))
phi = float(rospy.get_param("/parameters/phi"))

# target_x = 8.0
# target_y = 5.0
# beta = 1.5
# phi = 6.0
#print(str(target_x)+","+str(target_y)+","+str(beta)+","+str(phi))
def pose_callback(pose: Pose):
    cmd = Twist()
    delta_x = target_x - pose.x
    delta_y = target_y - pose.y
    x_linear_velocity  = beta * (math.sqrt(delta_x**2.0 + delta_y**2.0) )
    z_angular_velocity = phi * (-pose.theta + math.atan2(delta_y,delta_x))
    cmd.linear.x  = x_linear_velocity
    cmd.angular.z = z_angular_velocity
    if round(delta_x,3) == 0 or round(delta_y,3) == 0:
        cmd.linear.x = 0
        cmd.angular.z = 0
    rospy.loginfo("(" + str(pose.x) + "," + str(pose.y) + ")")
    pub.publish(cmd)


if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    
    while(1):
        rospy.sleep(0.1)
    # rospy.loginfo("Node has been started")
    # rospy.spin()
