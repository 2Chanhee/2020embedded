# This code is test code

import cv2
import numpy as np
import comunication as comu
import time
import mission
import linetracing as ltc

# isMision is toggle when robot meet cross line
isMission = True
crossCount = 0

# main
#if __name__ == "__main__":

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 960)

ret, frame = cap.read()

if ret :
    print("cam is open")
else :
    print("cam is not open")


while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize = (640, 480), interpolation = cv2.INTER_NEAREST)
    cv2.imshow('test', frame)
    a = cv2.waitKey(1)
    if isMission:
        ltc.LineTracing(ltc.GetDegree(frame))
    #else :
        #Mision()
        
    if a == ord('q'):
        break