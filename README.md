# turtlebot_teleop_keyboard #

use keyboard to control the base and the robot arm of turtlebot2i



**Full Installation**
***Set workstation***
1. install ROS (see www.ros.com)
2. 
```
> echo export ROS_MASTER_URI=http://IP_OF_TURTLEBOT:11311 >> ~/.bashrc  under intensechoi IP_OF_TURTLEBOT=192.168.178.25
> echo export ROS_HOSTNAME=IP_OF_PC >> ~/.bashrc
```
3.Connect to Turtlebot
```
ssh turtlebot@192.168.178.25
```
4.Launch Turtlebot
```
cd ~/turtlebot2i
source devel/setup.bash
roslaunch turtlebot2i_bringup turtlebot2i_basic.launchh 
```
5.Launch this package on workstation
```
cd ~/turtlebot_teleop_keyboard
source devel/setup.bash
roslaunch turtlebot_teleop_arm turtlebot2i_teleop.launch
```

### Activity Graph ###
![uml](teleop_uml.jpg)
