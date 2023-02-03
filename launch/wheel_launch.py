from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package= "exercise_wheel", 
            executable= "rpm_publisher.py",
            name= "rpm_pub"
        ),
        
        Node(
            package= "exercise_wheel",
            executable= "speed_publisher.py",
            name= "speed_pub",
            parameters= [
                {"wheel_diameter" : 0.5}
            ]
        )
    ])