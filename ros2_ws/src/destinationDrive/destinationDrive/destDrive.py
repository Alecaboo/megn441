import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from turtlesim.msg import Pose
import math

linear_constant = 0.25
angular_constant = 2.0

class destDrive(Node):
    def __init__(self):
        super().__init__('destDrive')

        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0

        self.destination_x = 8.0
        self.destination_y = 8.0 # default destination if there's no message


        self.publisher = self.create_publisher(
            Twist, 'turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(
                    Pose, 'turtle1/pose', self.listener_callback, 10)
        self.target_subscriber = self.create_subscription(
             Point, 'destPoint', self.target_callback,10
        )
        
        timer_period = 0.1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
            self.current_x = msg.x
            self.current_y = msg.y
            self.current_theta = msg.theta

    def target_callback(self,msg):
         self.destination_x = msg.x
         self.destination_y = msg.y

    def timer_callback(self):
        outMsg = Twist()

        destination_theta = math.atan2 ((self.destination_y-self.current_y),  (self.destination_x-self.current_x) ) #atan2 was something i discovered far too late in this debugging process
        
        distance = math.sqrt(math.pow((self.destination_x-self.current_x),2)+math.pow((self.destination_y-self.current_y),2))

        if (distance > 0.5):
            vel = linear_constant*distance
            omega = angular_constant*(destination_theta-self.current_theta)
        else:
             vel = 0.0
             omega = 0.0
             self.get_logger().info("We're there!") #really I should not publish the 0,0 cmd_vel msg when this one is being pubbed, but oh well
        outMsg.angular.z = omega
        outMsg.linear.x = vel
        self.publisher.publish(outMsg)
        self.get_logger().info('Publishing: v={v}, omega={w}'.format(v=vel, w=omega))

def main():
    rclpy.init()
    destinationDrive = destDrive()
    rclpy.spin(destinationDrive)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

