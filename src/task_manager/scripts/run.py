#! /usr/bin/env python 
# Standard libraries
import os
import time

# External libraries
import rospy
import json
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler

# Path
current_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_directory, "..")

data_directory = os.path.join(parent_directory, "data")



class RunNode():
    """
    """
    def __init__(self):
        pass 

    def create_goal(self, data, index):
        """
        Create move base goal for navigation
        :param: data
        :param: index
        """
        goal_send = MoveBaseGoal()
        
        goal_send.target_pose.header.frame_id = "map"#goal.header.frame_id
        
        goal_send.target_pose.header.stamp = rospy.Time.now()#goal.header.stamp
        
        goal_send.target_pose.pose.position.x = data[index]["x"]#goal.pose.position.x
        
        goal_send.target_pose.pose.position.y = data[index]["y"]#goal.pose.position.y
        
        goal_send.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, data[index]["yaw"]))#goal.pose.orientation.z
        
        rospy.loginfo(goal_send.target_pose.pose.position.x)
        
        rospy.loginfo(goal_send.target_pose.pose.position.y)
        
        return goal_send    
    
    def move(self):
        """
        Move robot to specific point on waypoint
        """
        waypoint_file = open(os.path.join(data_directory, "waypoint.json"))

        data = json.load(waypoint_file)

        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        
        client.wait_for_server()

        for index in range(0, len(data)):
            goal_send = self.create_goal(data, index)
            
            rospy.loginfo("Send goal")
            
            client.send_goal(goal_send)
            
            wait = client.wait_for_result()
            
            rospy.loginfo("After waiting for result")
            
            if not wait:
                rospy.logerr("Action server not available!")
           
                rospy.signal_shutdown("SHUT")
            
            else:
                result = client.get_result()
                
                rospy.loginfo(result)


if __name__ == '__main__':
    rospy.init_node("run_node", anonymous = True)

    try:
        client = RunNode()

        client.move()
        
        rospy.loginfo("Goal execution done!")
    
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
