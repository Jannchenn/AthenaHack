# AthenaHack

This is the python code that can extract useful gesture information from the Leap Motion Controller. 

The auxiliary files for the Leap Motion are from Leap_Motion_SDK_Windows_2.3.1, which allows the python code to control the Leap Motion detection. 

The main file is leapmotion.py, which detectes three different gestures as three different types of cookies. 
The cookie numbers are now hardcoded to 10, 20 and 30. 
Drawing a circle with index finger will decrement the number for cookie A
Tap forward horizontally with index fingure will decrement the number for cookie B
Tap down vertically with index finger will decrement the number for cookie C

There is also LeapMotionSwiping.py, which will detect the direction that the hand is swiping to.
It can detect the main direction of swiping at every millisecond. 
However, this file is not used as it cannot count one swipe as one action as the autodetection take place every milli second.


The commented out code for both the leapmotion.py and the LeapMotionSwiping.py are all runnable, but commented out as they are not used.
Those code can be uncommented and the program will still run with more information been printed out. 
