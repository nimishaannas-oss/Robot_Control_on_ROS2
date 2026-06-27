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

        if wheels_moving:

            if self.arms_moving:
                self.get_logger().info(
                    'Wheels moving -> Arms STOPPED'
                )

            self.arms_moving = False

        else:

            if not self.arms_moving:
                self.get_logger().info(
                    'Wheels stopped -> Arms MOVING'
                )

            self.arms_moving = True


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
