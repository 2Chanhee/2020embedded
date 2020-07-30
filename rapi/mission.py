import cv2
import numpy as np
# import comunication as comu

# Suppose red is dangerous area
# Return Centroid of area
def FindArea(src):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    lower_hsv = ( 0,  70,   0)
    upper_hsv = (25, 255, 255)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    #h, s, v = cv2.split(hsv)
    #h = cv2.inRange(h, 0, 20)
    #s = cv2.inRange(s, 100, 255)
    #mask = cv2.bitwise_and(h, s)

    return centroid
