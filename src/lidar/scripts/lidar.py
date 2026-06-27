#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')

        self.publisher_ = self.create_publisher(
            Float32,
            'lidar_distance',
            10
        )

        self.value = 0.0

        # Publish every 1 second
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = Float32()
        msg.data = self.value

        self.publisher_.publish(msg)

        self.get_logger().info(f'LiDAR Distance: {self.value}')

        self.value += 1.0

        if self.value > 10.0:
            self.value = 0.0


def main(args=None):
    rclpy.init(args=args)

    node = LidarPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
