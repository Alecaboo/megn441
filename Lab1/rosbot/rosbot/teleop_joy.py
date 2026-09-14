import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class teleop_joy(Node):
	def __init__(self):
		super().__init__('teleop_joy')
		
		self.subscriber = self.create_subscription(Joy, 'ros_robot_controller/joy', self.listener_callback, 10)
		
		self.publisher = self.create_publisher(Twist,'cmd_vel', 10)
		
		self.speed = 0.0
		self.rotation = 0.0
		
		timer_period = 0.05
		self.timer = self.create_timer(timer_period,self.timer_callback)
		
	def listener_callback(self, msg):
		self.rotation = msg.axes[0]
		self.speed = msg.axes[1]
		
	def timer_callback(self):
		outMsg = Twist()
		
		outMsg.angular.z = self.rotation
		outMsg.linear.x = self.speed
		
		self.publisher.publish(outMsg)


def main():
	rclpy.init()
	NODE_NAME = teleop_joy()
	rclpy.spin(NODE_NAME)
	rclpy.shutdown()	


if __name__ == '__main__':
	main()
