# This code is test code

import cv2
import numpy as np
import comu

# Order number
ORD_STRAIGHT     = 2 
ORD_TURNLEFT     = 1
ORD_TURNRIGHT    = 3
ORD_TURNLEFT_90  = 4
ORD_TURNRIGHT_90 = 6

# Variable for lineTracing
vertical  = False
horiznal  = False
#numOfLine = 0
direction = False # False == Left

# LineTracing
def LineTracing(src):
    # src = cv2.equalizeHist(src)
    degree = np.array([])
    # line   = np.array([])
    # Convert BGR to Gray for reduce time
    # src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.inRange(s, 40, 255)
    hsv = cv2.bitwise_and(hsv, hsv, mask = s)
    src = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


    # Detect line using hough transformation
    
    canny = cv2.Canny(src, 50, 200)
    line  = cv2.HoughLines(canny, 1, np.pi/180, 50)

    # Find vertical line
    if np.any(line == None) :
        return
    degree = np.squeeze(line[:,:,1], axis = 1)
    degree = 1.57 - degree

    # Detect straight line
    if np.any( np.abs(degree) > 1.25 ) :
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
    
    if vertical == True & ( np.any( np.abs(degree) < 0.3 ) ):
        horiznal = True
        print("CRS")
        if direction :
            comu.TX_data(comu.serial_port, ORD_TURNLEFT_90)
        else :
            comu.TX_data(comu.serial_port, ORD_TURNRIGHT_90)
        horiznal = False

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
    if ret :
        LineTracing(frame)
        #comu.TX_data(comu.serial_port, ORD_STRAIGHT)
    else :
        print("No camera!")
        break

    if a == ord('q'):
        break
