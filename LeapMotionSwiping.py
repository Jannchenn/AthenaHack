import Leap, sys, math
from Leap import SwipeGesture

numberA = 0	
numberB = 0
numberC = 0
numberD = 0

class LeapMotionListener(Leap.Listener):
	state_names = ['STATE_INVALID','STATE_START','STATE_UPDATE','STATE_END']

	def on_connect(self, controller):
		print "Motion Sensor Connected"
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
		global numberD
		
		tempID = 0
		
		for gesture in frame.gestures():
			if gesture.type == Leap.Gesture.TYPE_SWIPE:
				swipe = SwipeGesture(gesture)
				swipeDir = swipe.direction
				
				"""if (self.state_names[gesture.state] == "STATE_START"):
					numberA = numberB = numberC = numberD = 0"""
				
				if(swipeDir.x>0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					"""print "Swipe right ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]"""
					numberA += 1
				elif(swipeDir.x<0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					"""print "Swipe left ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]"""
					numberB += 1
				elif(swipeDir.y>0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					"""print "Swipe up ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]"""
					numberC += 1
				elif(swipeDir.y<0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					"""print "Swipe down ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]"""
					numberD += 1
				
				if (self.state_names[gesture.state] != "STATE_UPDATE"):
					if (numberA > numberB and numberA > numberC and numberA > numberD):
						print "SWIPED RIGHT"
					elif (numberB > numberA and numberB > numberC and numberB > numberD):
						print "SWIPED LEFT"
					elif (numberC > numberB and numberC > numberA and numberC > numberD):
						print "SWIPED UP"
					elif (numberD > numberB and numberD > numberC and numberD > numberA):
						print "SWIPED DOWN"
					numberA = numberB = numberC = numberD = 0
				
				
				
				
				
"""				
				if (self.state_names[gesture.state] == "STATE_START"):
					tempID = swipe.id
					startPositionX = swipe.position.x
					startPositionY = swipe.position.y
					print "startPositionX: " + str(startPositionX) + " startPositionY: " + str(startPositionY) + " ID: " + str(tempID)

				if (self.state_names[gesture.state] == "STATE_END" and tempID == swipe.id):
					endPositionX = swipe.position.x
					endPositionY = swipe.position.y
					print "endPositionX: " + str(endPositionX) + " endPositionY: " + str(endPositionY) + " ID: " + str(tempID)


			swipeDir = swipe.direction
				
				if (self.state_names[gesture.state] == "STATE_START"):
					tempID = swipe.id
					print "tempID is " + str(tempID)
					print "position: " + str(swipe.position)
					print "x position: " + str(swipe.position.x)
					startPositionX = swipe.position.x
					print "startPositionX: " + str(startPositionX)
				
				
				
				if(swipeDir.x>0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]
					numberA -= 1
					print "Swipe right, Number of Boxes for Cookie A is: " + str(numberA)
				elif(swipeDir.x<0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]
					numberB -= 1
					print "Swipe left, Number of boxes for Cookie B is: " + str(numberB)
				elif(swipeDir.y>0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]
					numberC -= 1
					print "Swipe up, Number of boxes for Cookie C is: " + str(numberC)
				elif(swipeDir.y<0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state]
					numberD -= 1
					print "Swipe down, Number of boxes for Cookie D is: " + str(numberD)"""
				
			
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
	