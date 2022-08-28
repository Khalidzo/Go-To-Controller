#  🐢Turtle Controller 

This is my first small project on ROS Noetic. The goal is to get the turtle on turtlesim simulator to a specific (x,y) point by adjusting its linear and angular velocity. The (x,y) point is specified on a *.yaml* file.
## Step 1: Create the turtle_controller node
This is the node that'll be controlling the turtle by controlling its linear and angular velocity until it reaches the target point.
This node is subscribes to the **/turtle1/pose** topic where it'll get the turtle's x,y position as well as its angle. The node is a publisher to the **/turtle1/cmd_vel** topic where it'll adjust the turtle's linear and angular velocity.
### Node initialization
```python
  rospy.init_node("turtle_controller")
  pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
  rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
```
### Mathematical equations used

### Adjust the linear and angular velocity
```python
    x_linear_velocity  = beta * (math.sqrt(delta_x**2.0 + delta_y**2.0) )
    z_angular_velocity = phi * (-pose.theta + math.atan2(delta_y,delta_x))
    cmd.linear.x  = x_linear_velocity
    cmd.angular.z = z_angular_velocity
```
## Step 2: Create .yaml config file
This is where the x-goal and y-goal are specified as well as the constant parameters (beta and phi)
```yaml
target:
  x: 5.0
  y: 7.0
 
parameters:
  beta: 1.5
  phi: 6.0
```
## Step 3: Create the launch file
The launch file is the entry point for our program to start. It'll contain the nodes that'll be running in the program.
```xml
<launch>
	<rosparam command="load" file="$(find turtle_controller)/config/target.yaml"/>
	<node pkg="turtlesim" type="turtlesim_node" name="turtlesim_node" />
	<node pkg="turtle_controller" type="turtle_controller.py" name="turtle_controller" />
</launch>
```
## Final step: Lanuch! 🚀
```shell
~$ roslaunch turtle_controller control.launch
```
## Demo
![chrome-capture-2022-7-24](https://user-images.githubusercontent.com/78038233/186479958-b120b920-9395-4c24-85b0-35215766b461.gif)
