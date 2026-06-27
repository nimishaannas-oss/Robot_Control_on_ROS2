#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Wheels(Node):

    def __init__(self):
        super().__init__('wheels')

        self.subscription = self.create_subscription(
            Float32,
            'lidar_distance',
            self.lidar_callback,
            10
        )

        self.wheels_moving = False

    def lidar_callback(self, msg):

        distance = msg.data

        if 0.0 <= distance <= 3.0:

            if self.wheels_moving:
                self.get_logger().info(
                    f'Obstacle detected! Distance={distance:.1f} m -> STOP'
                )

            self.wheels_moving = False

        else:

            if not self.wheels_moving:
                self.get_logger().info(
                    f'Distance={distance:.1f} m -> MOVE'
                )

            self.wheels_moving = True


def main(args=None):

    rclpy.init(args=args)

    node = Wheels()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
