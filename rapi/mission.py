import cv2
import numpy as np
import comunication as comu

# Suppose red is dangerous area
# Return Centroid of area
def GetCentroid(src):
    src = cv2.resize(src, dsize = (320, 240))
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    # Detect red color
    lower_hsv = (100,  70,   0)
    upper_hsv = (135, 255, 255)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # If no red area, then return 0
    if np.all(mask == 0):
        return None

    # Get centroid
    contuors, hierarchiy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contuors[0]
    M = cv2.moments(cnt)
    if M['m00'] ==0:
        M['m00'] = 1
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    # Return coordinate of centroid in the image
    return cx, cy

def GoToArea(src):
    cx, cy = GetCentroid(src)
    if cx < 130:
        while(cx > 130):
            comu.TX_data(comu.serial_port, comu.ORD_TURNRIGHT)
    elif cx > 230:
        while(cx < 230):
            comu.TX_data(comu.serial_port, comu.ORD_TURNLEFT)
    else:
        for i in range(10):
            comu.TX_data(comu.serial_port, comu.ORD_STRAIGHT)        
