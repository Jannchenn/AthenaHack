import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

numberA = 100	
numberB = 200
numberC = 300

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb','Index','Middle','Ring','Pinky']
	bone_names = ['Metacarpel','Proximal','Intermediate','Distal']
	state_names = ['STATE_INVALID','STATE_START','STATE_UPDATE','STATE_END']
	
	
	print "There are 100 boxes of cookie A, 200 boxes of cookie B, and 300 boxes of cookie C. "
	print "To keep track of how many boxes of each types of cookie is left, use different hand gestures to represent the selling of cookies."
	print "If cookie A is sold, have the index finger placed horizontally above the sensor first and make a circle motion to decrement the cookie A box number"
	print "If cookie B is sold, have the index finger placed horizontally above the sensor first and move forward horizontally to decrement the cookie B box number"
	print "If cookie C is sold, have the index finger placed horizontally above the sensor first and tap down vertically to decrement the cookie C box number"
	print "If multiple boxes of the same type of cookie is sold, please remove the entire hand away from the sensor and repeat the steps stated above"
		
	
	
	def on_init(self, controller):
		print "Leap Motion Sensor Initialized"
		
	def on_connect(self, controller):
		print "Motion Sensor Connected"
		
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		print "Motion Sensor Disconnected"
		
	def on_exit(self, controller):
		print "Exited"
		
	def on_frame(self, controller):
		frame = controller.frame()
		global numberA
		global numberB
		global numberC
		
		"""print "Frame ID: " + str(frame.id) + " Timestamp: " + str(frame.timestamp) + " # of Hands " + str(len(frame.hands)) + " # of Fingers "+ str(len(frame.fingers)) \
			+ " # of Tools " + str(len(frame.tools)) + " # of Gestures " + str(len(frame.gestures()))"""
			
		"""for hand in frame.hands:
			handType = "Left Hand" if hand.is_left else "Right Hand"

			print handType + " Hand ID: " + str(hand.id) + " Palm Position " + str(hand.palm_position)
			
			normal = hand.palm_normal
			direction = hand.direction
			
			print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)
				
			arm = hand.arm
			print "Arm Direction: " + str(arm.direction) + " Wrist Position: " + str(arm.wrist_position) + " Elbow Position: " + str(arm.elbow_position)
			
			for finger in hand.fingers:
				
				print "Type: " + self.finger_names[finger.type] + " ID: " + str(finger.id) + " Length (mm): " + str(finger.length) + " Width (mm): " + str(finger.width)
				
				for b in range(0, 4):
					bone = finger.bone(b)
					print "Bone: " + self.bone_names[bone.type] + " Start: " + str(bone.prev_joint) + " End: " + str(bone.next_joint) + " Direction: " + str(bone.direction)
			"""
		
		for gesture in frame.gestures():
			hand = frame.hands
			
			if gesture.type == Leap.Gesture.TYPE_CIRCLE:
				circle = CircleGesture(gesture)
				"""
				if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
					clockwiseness = "clockwise"
				else:
					clockwiseness = "counter-clockwise"	
				swept_angle = 0
				if circle.state != Leap.Gesture.STATE_START:
					previous = CircleGesture(controller.frame(1).gesture(circle.id))
					swept_angle = (circle.progress - previous.progress) * 2 * Leap.PI
				print "ID: " + str(circle.id) + " Progress: " + str(circle.progress) + " Radius: " + str(circle.radius) + " Swept Angle: " + str(swept_angle * Leap.RAD_TO_DEG) + " " + clockwiseness
				"""	
				if circle.state == Leap.Gesture.STATE_START:
					numberA -= 1
					print "The number of boxes left for cookie A is: " + str(numberA)
			
			"""if gesture.type == Leap.Gesture.TYPE_SWIPE:
				swipe = SwipeGesture(gesture)
				print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]
				if swipe.state == Leap.Gesture.STATE_START:
					numberB -= 1
					print "The number of boxes for cookie B is: " + str(numberB)
					
				print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state] + " Position: " + str(swipe.position) + " Direction: " + str(swipe.direction)\
					+ " Speed (mm/s): " + str(swipe.speed)"""

			if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
				screentap = ScreenTapGesture(gesture)
				numberB -= 1
				print "The number of boxes left for cookie B is: " + str(numberB)
				"""print "Screen Tap ID: " + str(screentap.id) + " State: " + self.state_names[gesture.state]"""
			
			if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
				keytap = KeyTapGesture(gesture)
				numberC -= 1
				print "The number of boxes left for cookie C is: " + str(numberC)
				"""print "Key Tap ID: " + str(keytap.id) + " State: " + self.state_names[gesture.state]"""
			
def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	
	controller.add_listener(listener)
	
	print "Press Enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
	 	controller.remove_listener(listener)
		
		
if __name__ == "__main__":
	main()
	