# ros-navigation-example
Using ros navigation package and turtlebot3, this repositories provides an example to 
Author: Tran Viet Thanh

## Depedencies 
- Ubuntu 18.04
- ROS Melodic

## Build 
```
cd ros-navigation-example
catkin_make
```

## Run 
Start simulation for tutorial in an example world
```
cd ros-navigation-example
bash start_simulation.sh
```

Start navigitaion including AMCL and move_base packages from ROS
```
cd ros-navigation-example
bash start_navigation.sh
```

### For define a move_base goal for navigation 
1. Open Rviz windows, choose "2D Nav Goal" and click on the position that you want the robot to come. 

2. Or run move_base client in task_manager package. Change waypoint.json in src/task_manager/data folder, then
```
cd ros-navigation-example
bash start_navigation.sh
```
With default way.point, the robot will move toward, turn left then return to starting point.
