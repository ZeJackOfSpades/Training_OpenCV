#coding:utf-8
"""
	This file is about how to load images with opencv
"""

import cv2
import numpy as np 

img	=	cv2.imread("Images/jotaro.jpg", cv2.IMREAD_UNCHANGED)

cv2.namedWindow('Window image', cv2.WINDOW_NORMAL)

cv2.imshow('Window image',img)
cv2.waitKey(0) 	& 0xFF		#Wait for an input key, and & 0xFF because of 64-bit machine
"""
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
"""
cv2.destroyAllWindows()