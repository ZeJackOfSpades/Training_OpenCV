"""
	For color conversion, we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.

For BGR -> Gray conversion we use the flags cv2.COLOR_BGR2GRAY. 
Similarly for BGR -> HSV, we use the flag cv2.COLOR_BGR2HSV

If you want to know the others flags you should run this command :
>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
>>> print flags

WARNING !!! For HSV, Hue range is [0,179], Saturation range is [0,255] 
and Value range is [0,255]. 
Different softwares use different scales. 
So if you are comparing OpenCV values with them, 
you need to normalize these ranges.
"""
import numpy as np
import cv2
"""
	If you want to know How to find HSV values to track (for example green):
		>>> green = np.uint8([[[0,255,0 ]]])
		>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
		>>> print hsv_green
		[[[ 60 255 255]]]
"""

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()