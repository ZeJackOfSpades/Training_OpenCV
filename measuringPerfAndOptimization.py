import numpy as np
import cv2

e1 = cv2.getTickCount()
# Code execution
e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()

print(time)


