#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class Arms(Node):

    def __init__(self):
        super().__init__('arms')

        self.subscription = self.create_subscription(
            Bool,
            'wheel_status',
            self.wheel_callback,
            10
        )

        self.arms_moving = False

    def wheel_callback(self, msg):

        wheels_moving = msg.data

        if wheels_moving and self.arms_moving:
            self.arms_moving = False
            self.get_logger().info(
                'Wheels moving -> Arms STOPPED'
            )

        elif not wheels_moving and not self.arms_moving:
            self.arms_moving = True
            self.get_logger().info(
                'Wheels stopped -> Arms MOVING'
            )


def main(args=None):

    rclpy.init(args=args)

    node = Arms()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
