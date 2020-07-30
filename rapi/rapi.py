# This code is test code

import cv2
import numpy as np
import comu
import time
import mission

# Order number
ORD_STRAIGHT     = 24 
ORD_TURNLEFT     = 20
ORD_TURNRIGHT    = 21
ORD_TURNLEFT_90  = 22
ORD_TURNRIGHT_90 = 23

# Variable for lineTracing
vertical  = False
horiznal  = False
#numOfLine = 0
direction = False # False == Left

# isMision is toggle when robot meet cross line
isMision = False
crossCount = 0

# LineTracing function
def LineTracing(src):
    # src = cv2.equalizeHist(src)
    degree = np.array([])
    # line   = np.array([])
    # Convert BGR to Gray for reduce time
    # src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Find yellow line
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.inRange(s, 120, 255)
    hsv = cv2.bitwise_and(hsv, hsv, mask = s)
    src = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


    # Detect line using hough transformation
    canny = cv2.Canny(src, 50, 200)
    line  = cv2.HoughLines(canny, 1, np.pi/180, 100)

    # Find vertical line
    if np.any(line == None) :
        return
    degree = np.squeeze(line[:,:,1], axis = 1)
    degree = 1.57 - degree

    if  np.any( np.abs(degree) > 1.4 ) & ( np.any( np.abs(degree) < 0.1) ):
        horiznal = True
        print("CRS")
        if direction :
            comu.TX_data(comu.serial_port, ORD_TURNLEFT_90)
        else :
            comu.TX_data(comu.serial_port, ORD_TURNRIGHT_90)
        horiznal = False
        crossCount += 1
        # Toggle isMision
        if crossCount > 5
            isMision = not isMision
            crossCount = 0
        return

    # Detect straight linei
    if np.any( np.abs(degree) > 1.4 ) :
        vertical = True
        comu.TX_data(comu.serial_port, ORD_STRAIGHT)
        print("STR")

    elif np.any( degree < 0) :
        vertical = False
        comu.TX_data(comu.serial_port, ORD_TURNLEFT)
        print("LFT")

    else :
        vertical = False
        comu.TX_data(comu.serial_port, ORD_TURNRIGHT)
        print("RGT")

    return src

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
    # src = LineTracing(frame)
    cv2.imshow('test', frame)
    a = cv2.waitKey(1)
    if isMission:
        LineTracing(frame)
        #comu.TX_data(comu.serial_port, ORD_STRAIGHT)
    else :
        Mision()
        
    if a == ord('q'):
        break

    #time.sleep(1)
