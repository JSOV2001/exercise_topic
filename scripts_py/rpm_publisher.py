#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

class rpmPublisherNode(Node):
    def __init__(self):
        super().__init__("rpm_pub")
        self.rpm_publisher = self.create_publisher(Float64, "/rpm", 10)
        self.rate = 2
        self.timer = self.create_timer(2, self.publish_rpm)
        self.rpm = 30.5
    
    def publish_rpm(self):
        msg = Float64()
        msg.data = self.rpm
        self.rpm_publisher.publish(msg)

def main():
    rclpy.init()
    node = rpmPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()