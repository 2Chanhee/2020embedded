# This code is test code

import cv2
import numpy as np
import comu

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cap.set(3, 640)
cap.set(4, 480)

# Order number
ORD_STRAIGHT     = 0
ORD_TURNLEFT     = 1
ORD_TURNRIGHT    = 2
ORD_TURNLEFT_90  = 3
ORD_TURNRIGHT_90 = 4

# Variable for lineTracing
vertical  = False
horiznal  = False
#numOfLine = 0
direction = False # False == Left

# LineTracing
def LineTracing(src):

    degree = np.array([])
    line   = np.array([])
    # Convert BGR to Gray for reduce time
    cv2.cvtColor(src,src, cv2.COLOR_BGR2GRAY)

    # Detect line using hough transformation
    canny = cv2.Canny(src, 50, 200)
    line  = cv2.HoughLines(canny, 1, np.pi/180, 100)

    # Find vertical line
    if line.shape[0] > 0 :
        degree = np.squeeze(line[:,:,1], axis = 1)
        degree = 1.57 - degree
    if np.any( np.abs(degree) > 1.27 ) :
        vertical = True
        comu.TX_data(serial_port, ORD_STRAIGHT)

    elif np.any( degree < 0) :
        vertical = False
        comu.TX_data(serial_port, ORD_TURNLEFT)

    else :
        vertical = False
        comu.TX_data(serial_port, ORD_TURNRIGHT)
    
    if vertical == True | ( np.any( np.abs(degree) )  < 0.3 ):
        horiznal = True
        if directoin :
            comu.TX_data(serial_port, ORD_TURNLEFT_90)
        else :
            comu.TX_data(serial_port, ORD_TURNRIGHT_90)

# main
if __name__ == "__main__":

    while(True):
        ret, frame = cap.read()
        LineTracing(frame)
        comu.TX_data(serial_port, ORD_STRAIGHT)
