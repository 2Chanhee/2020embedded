import cv2
import numpy as np
import comunication as comu

# Variable for lineTracing
direction = False # False == Left
cross_on  = True


# LineTracing function
def LineTracing(degree):
    
    # Detect cross line
    if  np.any( np.abs(degree) > 1.4 ) & ( np.any( np.abs(degree) < 0.1) ):
        print("CRS")
        if direction :
            comu.TX_data(comu.serial_port, comu.ORD_TURNLEFT_90)
        else :
            comu.TX_data(comu.serial_port, comu.ORD_TURNRIGHT_90)

    # Detect straight line
    if np.any( np.abs(degree) > 1.4 ) :
        comu.TX_data(comu.serial_port, comu.ORD_STRAIGHT)
        print("STR")

    elif np.any( degree < 0) :
        comu.TX_data(comu.serial_port, comu.ORD_TURNLEFT)
        print("LFT")

    else :
        comu.TX_data(comu.serial_port, comu.ORD_TURNRIGHT)
        print("RGT")

    return src

def GetDegree(src):
    degree = np.array([])
    
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
        FindLine(src)
        return GetDegree(src)
    degree = np.squeeze(line[:,:,1], axis = 1)
    degree = 1.57 - degree

    return degree

def FindLine(src):
    # Find yellow line
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.inRange(s, 120, 255)
    hsv = cv2.bitwise_and(hsv, hsv, mask = s)
    src = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Turn while find yellow line
    while(np.any(src > 0)):
        comu.TX_data(comu.serial_port, comu.ORD_TURNLEFT_90)

    return np.any(src > 0)