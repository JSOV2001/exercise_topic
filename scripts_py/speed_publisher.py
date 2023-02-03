#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class SpeedPublisherNode(Node):
    def __init__(self):
        super().__init__("speed_publisher")
        self.rpm_subscriber = self.create_subscription(Float64, "/rpm", self.rpm_callback, 10)
        self.speed_publisher = self.create_publisher(Float64, "/speed", 10)
        self.diameter_default = 25/100
        self.diameter = self.declare_parameter("wheel_diameter", self.diameter_default)
    
    def rpm_callback(self, rpm_message):
        speed_message = Float64()
        diameter_parameter = self.get_parameter("wheel_diameter").get_parameter_value().double_value
        speed_message.data = rpm_message.data * diameter_parameter * math.pi / 60
        print(f"Speed: {round(speed_message.data, 2)} m/s")
        self.speed_publisher.publish(speed_message)

def main():
    rclpy.init()
    node = SpeedPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()